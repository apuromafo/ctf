# Cypheron

| **Dificultad** | Insane |
| **Tipo** | CTF |
| **Slug** | `cypheron` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cypheron) |
| **Sección** | 04 Level Insane |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=cypheron`, xGh05t/THM GitHub `2026_AI_Odyssey/04-Cypheron`) |
| **Componentes** | pickle/torch.load/n8n/lfi/jwt/container-escape |
| **Impacto** | Compromisión completa de la cadena de suministro de IA: pickle malicioso como RCE contra la inferencia y encadenado LFI→JWT→workflow RCE→container escape para romper el host. |

---

**Contexto:** Sala de evento (2026: An AI Odyssey) de dificultad Insane con 2 máquinas. El tema es la compromisión de la cadena de suministro de IA: un modelo empaquetado como pickle (`torch.load(weights_only=False)`) que es RCE directo contra un servicio de inferencia con push de proveedor, y una plataforma de automatización n8n con CVE de LFI que encadena con falsificación de JWT, RCE por flujo de trabajo y escape de contenedor vía bind-mount al host.

## Solucionario

### Task 1: Trojaned Model - Neural C2 Beacon

Target `10.67.188.40:8000` (Gunicorn/Flask). El servicio expone `POST /classify` (inferencia) y `POST /vendor/push` (actualizaciones de modelo de proveedor); su banner documenta que el push llama `torch.load(weights_only=False)` "por compatibilidad". Un `.pt` es un ZIP: se inyecta un pickle malicioso con reducers `(exec, (code,))`, la respuesta refleja la excepción, y `raise Exception(stdout+stderr)` convierte el canal de error en canal de salida de comandos. Con eso se leen `/flag` (flag 3) y `/etc/c2-hint.txt` (flag 2); la flag 1 se extrae exfiltrando `signal_classifier.pt` en base64 y leyendo su buffer `_calibration_constants`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the first flag? | `THM{artifact_suspicious}` |
| 2 | What's the second flag? | `THM{trigger_identified}` |
| 3 | What's the third flag? | `THM{neural_c2_compromise}` |

### Task 2: Trojaned Model - Neural C2 Beacon (Downloadable File)

Parte "sin servidor" de la misma sala: análisis estático del artefacto `signal-classifier-1778659286018.pt`. `file` dice ZIP; `unzip -l` muestra siete tensores (un MLP `Linear(16→64)+Linear(64→32)+Linear(32→2)`) más un buffer de 24 bytes = longitud exacta de un `THM{...}`. `unzip -p signal_classifier/data/0` imprime la flag. `pickletools.dis` confirma que `data/0` es un buffer `_calibration_constants` uint8 de longitud 24. No requiere red; solo cuando el target en vivo está caído o como warm-up.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Describe el artefacto descargable. | `THM{artifact_suspicious}` |

### Task 3: Nightmare

Target `10.67.145.144` (SSH:22, n8n:5678). n8n v1.120.4 con un Form Trigger público en `POST /form/file-processor` que también acepta `application/json` y confía en el campo `filepath` enviado por el usuario (CVE-2026-21858): LFI sin auth → `/proc/self/environ` (secrets `N8N_JWT_SECRET`, `N8N_ENCRYPTION_KEY`) → `/home/node/.n8n/database.sqlite` (webhook secreto `secret-webhook`, hashes bcrypt, paths de flags) → user flag vía `/home/node/flag-user-lfi.txt`. Luego falsificación de JWT (campo `hash` = `sha256("email:bcrypt").digest('base64')[:10]`, HS256 con el secret filtrado) → admin → PATCH del workflow con nodo Execute Command → shell PTY Node.js como `node` → `/setup.sh` filtra la password root hardcodeada `N1ghtm4r3R00t!CTF2026` → `su root` → `/host-root/flag.txt` (bind-mount del host) da la root flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Whats the user flag? | `THM{nightmare_just_begun}` |
| 2 | Whats the root flag? | `THM{p4g3_c4ch3_g0t_wr1tt3n_k3rn3l_pwn3d_c0nt41n3r_3sc4p3d}` |

---

**Metodología:**
1. **Reconocimiento (Trojaned Model):** El banner del servicio `10.67.188.40:8000` documenta dos endpoints: `POST /classify` (inferencia) y `POST /vendor/push` (push de modelo del proveedor), y declara que el push usa `torch.load(weights_only=False)` por compatibilidad.
2. **Pickle RCE:** Un `.pt` de PyTorch es un ZIP cuyo `data.pkl` es pickle. Se crea una clase con `__reduce__` que devuelve `(exec, (codigo,))`; al deserializar en el push, el código se ejecuta en el contenedor de inferencia.
3. **Exfiltración vía excepción:** El handler Flask envuelve la carga en `try/except` y refleja la representación de la excepción en el JSON. `raise Exception(stdout + stderr)` desde el pickle convierte el mensaje de error en un canal de salida de comandos.
4. **Flags 3 y 2 (Trojaned Model):** `cat /flag` → `THM{neural_c2_compromise}`; `cat /etc/c2-hint.txt` (marcador "proof of execution") → `THM{trigger_identified}`.
5. **Flag 1 (buffer del modelo):** Se exfiltra `/app/model/signal_classifier.pt` en base64 por el canal de excepción y se lee localmente el buffer `_calibration_constants`: `THM{artifact_suspicious}`.
6. **Variante estática (Task 2):** `file` dice ZIP; `unzip -l` muestra siete tensores (MLP `Linear(16→64)+Linear(64→32)+Linear(32→2)`) y un buffer uint8 de 24 bytes. `unzip -p signal_classifier/data/0` imprime directamente `THM{artifact_suspicious}`; `pickletools.dis` de `data.pkl` prueba que es un buffer de longitud 24.
7. **Reconocimiento (Nightmare):** `nmap -sV --min-rate 3000 -p- 10.67.145.144` → `22/tcp` OpenSSH 9.6p1 y `5678/tcp` n8n v1.120.4 (confirmado por el meta tag `n8n:config:sentry`, base64). Único endpoint público: `POST /form/file-processor`.
8. **CVE-2026-21858 (LFI):** El Form Trigger acepta `application/json` y confía en el campo `files[..].filepath` que manda el usuario. Con `"filepath":"/etc/passwd"` se obtiene el archivo; sin auth.
9. **Loot de secretos:** LFI de `/proc/self/environ` (con `tr '\0' '\n'`) → `N8N_JWT_SECRET` y `N8N_ENCRYPTION_KEY`. LFI de `/home/node/.n8n/database.sqlite` → `user_entity` (email + bcrypt) y `workflow_entity` (workflow "Internal Automation — DO NOT SHARE" con webhook `secret-webhook`).
10. **User flag:** LFI de `/home/node/flag-user-lfi.txt` → `THM{nightmare_just_begun}`.
11. **JWT forgery:** El código fuente de n8n (auth.service.ts, v1.120.4) revela `createJWTHash(user) = sha256(email + ":" + bcrypt_hash).digest('base64').substring(0,10)`. Se forja un token HS256 (`{id, email, hash}`) con el secret filtrado y la cookie `n8n-auth`.
12. **RCE vía workflow:** Como admin, PATCH del nodo "Execute Command" a `node -e "require('child_process').spawn('/bin/bash',['-i'],{stdio:'inherit'})"`; al re-disparar `/webhook/secret-webhook` se obtiene un PTY como `node`. (Alternativa inicial: el webhook fijo ejecuta `id`, RCE limitada sin auth.)
13. **PrivEsc y escape:** `/setup.sh` (vía LFI o shell) contiene la password root hardcodeada `N1ghtm4r3R00t!CTF2026` → `su root` → `/host-root/` es bind-mount de la raíz del host → `cat /host-root/flag.txt` → root flag.

**Learning chain:** banner/`torch.load(weights_only=False)` → pickle `__reduce__`→`exec` → excepción reflejada como canal de comando → flags del contenedor de inferencia → exfiltración del `.pt` (base64) → buffer `_calibration_constants` → artefacto estático (Task 2: `unzip -p`) → n8n Form Trigger → CVE-2026-21858 LFI → `/proc/self/environ` (JWT secret) → `database.sqlite` → user flag → JWT HS256 truncado forjado → admin → PATCH Execute Command → PTY como `node` → `/setup.sh` (password root hardcodeada) → `su root` → bind-mount `/host-root/` → root flag.

**MITRE ATT&CK:** T1203 (Execution via Client Software), T1059 (Command and Scripting Interpreter), T1219 (Remote Access Software), T1005 (Data from Local System), T1078 (Valid Accounts), T1068 (Privilege Escalation), T1611 (Escape to Host)

**Fuente:** [TryHackMe - Cypheron](https://tryhackme.com/room/cypheron)