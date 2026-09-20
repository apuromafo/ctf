# Cypheron

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `cypheron` | [TryHackMe](https://tryhackme.com/room/cypheron) | 04 Level Insane | Web (API THM `api/v2/rooms/tasks?roomCode=cypheron`, xGh05t/THM GitHub `2026_AI_Odyssey/04-Cypheron`) | pickle/torch.load/n8n/lfi/jwt/container-escape | Compromisión completa de la cadena de suministro de IA: pickle malicioso como RCE contra la inferencia y encadenado LFI→JWT→workflow RCE→container escape para romper el host. |

---

**Contexto:** Sala de evento (2026: An AI Odyssey) de dificultad Insane con 2 máquinas. El tema es la compromisión de la cadena de suministro de IA: un modelo empaquetado como pickle (`torch.load(weights_only=False)`) que es RCE directo contra un servicio de inferencia con push de proveedor, y una plataforma de automatización n8n con CVE de LFI que encadena con falsificación de JWT, RCE por flujo de trabajo y escape de contenedor vía bind-mount al host.

> **ES:** Sala de evento (2026: An AI Odyssey) de dificultad Insane con 2 máquinas. El tema es la compromisión de la cadena de suministro de IA: un modelo empaquetado como pickle (`torch.load(weights_only=False)`) que es RCE directo contra un servicio de inferencia con push de proveedor, y una plataforma de automatización n8n con CVE de LFI que encadena con falsificación de JWT, RCE por flujo de trabajo y escape de contenedor vía bind-mount al host.

> **EN:** Event room (2026: An AI Odyssey) of Insane difficulty with 2 machines. The theme is the compromise of the AI supply chain: a model packaged as pickle (`torch.load(weights_only=False)`) that is direct RCE against an inference service with vendor push, and an n8n automation platform with an LFI CVE chaining with JWT forgery, workflow RCE, and container escape via bind-mount to the host.

## Solucionario

### Task 1: Modelo Troyanizado - Beacon Neural C2 / Trojaned Model - Neural C2 Beacon

**Explicación:**
Target `10.67.188.40:8000` (Gunicorn/Flask). El servicio expone `POST /classify` (inferencia) y `POST /vendor/push` (actualizaciones de modelo de proveedor); su banner documenta que el push llama `torch.load(weights_only=False)` "por compatibilidad". Un `.pt` es un ZIP: se inyecta un pickle malicioso con reducers `(exec, (code,))`, la respuesta refleja la excepción, y `raise Exception(stdout+stderr)` convierte el canal de error en canal de salida de comandos. Con eso se leen `/flag` (flag 3) y `/etc/c2-hint.txt` (flag 2); la flag 1 se extrae exfiltrando `signal_classifier.pt` en base64 y leyendo su buffer `_calibration_constants`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the first flag? | `THM{artifact_suspicious}` |
| 2 | What's the second flag? | `THM{trigger_identified}` |
| 3 | What's the third flag? | `THM{neural_c2_compromise}` |

### Task 2: Modelo Troyanizado - Beacon Neural C2 (Archivo Descargable) / Trojaned Model - Neural C2 Beacon (Downloadable File)

**Explicación:**
Parte "sin servidor" de la misma sala: análisis estático del artefacto `signal-classifier-1778659286018.pt`. `file` dice ZIP; `unzip -l` muestra siete tensores (un MLP `Linear(16→64)+Linear(64→32)+Linear(32→2)`) más un buffer de 24 bytes = longitud exacta de un `THM{...}`. `unzip -p signal_classifier/data/0` imprime la flag. `pickletools.dis` confirma que `data/0` es un buffer `_calibration_constants` uint8 de longitud 24. No requiere red; solo cuando el target en vivo está caído o como warm-up.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Describe el artefacto descargable. | `THM{artifact_suspicious}` |

### Task 3: Pesadilla / Nightmare

**Explicación:**
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

### Cadena de ataque / Attack Chain

1. Banner del servicio → `torch.load(weights_only=False)`.
2. Pickle malicioso (`__reduce__` → `exec`) → RCE en inferencia.
3. Excepción reflejada como canal de comandos → flags del contenedor.
4. Exfiltración del `.pt` (base64) → buffer `_calibration_constants` → flag 1; variante estática `unzip -p` → flag artefacto.
5. Form Trigger n8n → JSON `filepath` → CVE-2026-21858 LFI.
6. `/proc/self/environ` → JWT secret; `database.sqlite` → user entity + bcrypt + webhook secreto.
7. LFI de `flag-user-lfi.txt` → user flag.
8. JWT HS256 truncado forjado → admin → PATCH Execute Command → PTY como `node`.
9. `/setup.sh` → password root hardcodeada → `su root` → bind-mount `/host-root/` → root flag.

**Learning chain:** banner/`torch.load(weights_only=False)` → pickle `__reduce__`→`exec` → excepción reflejada como canal de comando → flags del contenedor de inferencia → exfiltración del `.pt` (base64) → buffer `_calibration_constants` → artefacto estático (Task 2: `unzip -p`) → n8n Form Trigger → CVE-2026-21858 LFI → `/proc/self/environ` (JWT secret) → `database.sqlite` → user flag → JWT HS256 truncado forjado → admin → PATCH Execute Command → PTY como `node` → `/setup.sh` (password root hardcodeada) → `su root` → bind-mount `/host-root/` → root flag.

**Lección:** *La confianza ciega en formatos de serialización y en inputs de usuario dentro del flujo de IA/automatización convierte artefactos "legítimos" (pickle, webhooks, flujos n8n) en una cadena de RCE: verificar siempre el origen de los modelos y los destinos de los filepaths.*

**MITRE ATT&CK:** T1203 (Execution via Client Software), T1059 (Command and Scripting Interpreter), T1219 (Remote Access Software), T1005 (Data from Local System), T1078 (Valid Accounts), T1068 (Privilege Escalation), T1611 (Escape to Host)

**Fuente:** [TryHackMe - Cypheron](https://tryhackme.com/room/cypheron)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.