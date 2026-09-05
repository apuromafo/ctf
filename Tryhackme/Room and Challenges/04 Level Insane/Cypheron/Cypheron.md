# Cypheron [INSANE]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** INSANE
* **Tipo / Type:** CTF (Evento "2026: An AI Odyssey" - Planeta 4/4)
* **Slug:** `cypheron`
* **Link:** https://tryhackme.com/room/cypheron
* **Sección / Section:** 04 Level Insane
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=cypheron`, xGh05t/THM GitHub `2026_AI_Odyssey/04-Cypheron`)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (2026: An AI Odyssey) de dificultad Insane con 2 máquinas. El tema es la **compromisión de la cadena de suministro de IA**: un modelo empaquetado como pickle (`torch.load(weights_only=False)`) que es RCE directo contra un servicio de inferencia con push de proveedor, y una plataforma de automatización n8n con CVE de LFI que encadena con falsificación de JWT, RCE por flujo de trabajo y escape de contenedor vía bind-mount al host.
> **EN:** Event room (2026: An AI Odyssey) of Insane difficulty with 2 machines. The theme is **AI supply-chain compromise**: a pickle-packaged model (`torch.load(weights_only=False)`) that is direct RCE against an inference service with vendor push, and an n8n automation platform with an LFI CVE chained into JWT forgery, workflow RCE and container escape via host bind-mount.

### Task 1 - Trojaned Model - Neural C2 Beacon

> **ES:** Target `10.67.188.40:8000` (Gunicorn/Flask). El servicio expone `POST /classify` (inferencia) y `POST /vendor/push` (actualizaciones de modelo de proveedor); su banner documenta que el push llama `torch.load(weights_only=False)` "por compatibilidad". Un `.pt` es un ZIP: se injecta un pickle malicioso con reducers `(exec, (code,))`, la respuesta refleja la excepción, y `raise Exception(stdout+stderr)` convierte el canal de error en canal de salida de comandos. Con eso se leen `/flag` (flag 3) y `/etc/c2-hint.txt` (flag 2); la flag 1 se extrae exfiltrando `signal_classifier.pt` en base64 y leyendo su buffer `_calibration_constants`. 3 preguntas.
> **EN:** Target `10.67.188.40:8000` (Gunicorn/Flask). The service exposes `POST /classify` (inference) and `POST /vendor/push` (vendor model updates); its banner documents that push calls `torch.load(weights_only=False)` "for backwards compatibility". A `.pt` is a ZIP: inject a malicious pickle with `(exec, (code,))` reducers, the response reflects the exception, and `raise Exception(stdout+stderr)` turns the error channel into a command-output channel. That reads `/flag` (flag 3) and `/etc/c2-hint.txt` (flag 2); flag 1 is pulled by exfiltrating `signal_classifier.pt` in base64 and reading its `_calibration_constants` buffer. 3 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the first flag? | `THM{artifact_suspicious}` |
| What's the second flag? | `THM{trigger_identified}` |
| What's the third flag? | `THM{neural_c2_compromise}` |

### Task 2 - Trojaned Model - Neural C2 Beacon (Downloadable File)

> **ES:** Parte "sin servidor" de la misma sala: análisis estático del artefacto `signal-classifier-1778659286018.pt`. `file` dice ZIP; `unzip -l` muestra siete tensores (un MLP `Linear(16→64)+Linear(64→32)+Linear(32→2)`) más un buffer de 24 bytes = longitud exacta de un `THM{...}`. `unzip -p signal_classifier/data/0` imprime la flag. `pickletools.dis` confirma que `data/0` es un buffer `_calibration_constants` uint8 de longitud 24. No requiere red; solo cuando el target en vivo está caído o como warm-up. Sin preguntas.
> **EN:** "No-server" half of the same room: static analysis of the artifact `signal-classifier-1778659286018.pt`. `file` says ZIP; `unzip -l` shows seven tensors (an MLP `Linear(16→64)+Linear(64→32)+Linear(32→2)`) plus a 24-byte buffer = exact length of a `THM{...}`. `unzip -p signal_classifier/data/0` prints the flag. `pickletools.dis` confirms `data/0` is a `_calibration_constants` uint8 buffer of length 24. No network needed; only when the live target is down or as a warm-up. No questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Informational) | Tarea informativa con archivo descargable. Define la misma flag que la Q1 de la Task 1: `THM{artifact_suspicious}` en `_calibration_constants`. |

### Task 3 - Nightmare

> **ES:** Target `10.67.145.144` (SSH:22, n8n:5678). n8n v1.120.4 con un Form Trigger público en `POST /form/file-processor` que también acepta `application/json` y **confía en el campo `filepath` enviado por el usuario** (CVE-2026-21858): LFI sin auth → `/proc/self/environ` (secrets `N8N_JWT_SECRET`, `N8N_ENCRYPTION_KEY`) → `/home/node/.n8n/database.sqlite` (webhook secreto `secret-webhook`, hashes bcrypt, paths de flags) → **user flag** vía `/home/node/flag-user-lfi.txt`. Luego falsificación de JWT (campo `hash` = `sha256("email:bcrypt").digest('base64')[:10]`, HS256 con el secret filtrado) → admin → PATCH del workflow con nodo Execute Command → shell PTY Node.js como `node` → `/setup.sh` filtra la password root hardcodeada `N1ghtm4r3R00t!CTF2026` → `su root` → `/host-root/flag.txt` (bind-mount del host) da la **root flag**. 2 preguntas.
> **EN:** Target `10.67.145.144` (SSH:22, n8n:5678). n8n v1.120.4 with a public Form Trigger at `POST /form/file-processor` that also accepts `application/json` and **trusts the user-supplied `filepath` field** (CVE-2026-21858): unauth LFI → `/proc/self/environ` (secrets `N8N_JWT_SECRET`, `N8N_ENCRYPTION_KEY`) → `/home/node/.n8n/database.sqlite` (secret webhook `secret-webhook`, bcrypt hashes, flag paths) → **user flag** via `/home/node/flag-user-lfi.txt`. Then JWT forgery (`hash` field = `sha256("email:bcrypt").digest('base64')[:10]`, HS256 with the leaked secret) → admin → PATCH the workflow with an Execute Command node → Node.js PTY shell as `node` → `/setup.sh` leaks the hardcoded root password `N1ghtm4r3R00t!CTF2026` → `su root` → `/host-root/flag.txt` (host bind-mount) gives the **root flag**. 2 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Whats the user flag? | `THM{nightmare_just_begun}` |
| Whats the root flag? | `THM{p4g3_c4ch3_g0t_wr1tt3n_k3rn3l_pwn3d_c0nt41n3r_3sc4p3d}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento (Trojaned Model):** El banner del servicio `10.67.188.40:8000` documenta dos endpoints: `POST /classify` (inferencia) y `POST /vendor/push` (push de modelo del proveedor), y declara que el push usa `torch.load(weights_only=False)` por compatibilidad.
2. **Paso / Step - Pickle RCE:** Un `.pt` de PyTorch es un ZIP cuyo `data.pkl` es pickle. Se crea una clase con `__reduce__` que devuelve `(exec, (codigo,))`; al deserializar en el push, el código se ejecuta en el contenedor de inferencia.
3. **Paso / Step - Exfiltración vía excepción:** El handler Flask envuelve la carga en `try/except` y refleja la representación de la excepción en el JSON. `raise Exception(stdout + stderr)` desde el pickle convierte el mensaje de error en un canal de salida de comandos.
4. **Paso / Step - Flags 3 y 2 (Trojaned Model):** `cat /flag` → `THM{neural_c2_compromise}`; `cat /etc/c2-hint.txt` (marcador "proof of execution") → `THM{trigger_identified}`.
5. **Paso / Step - Flag 1 (buffer del modelo):** Se exfiltra `/app/model/signal_classifier.pt` en base64 por el canal de excepción y se lee localmente el buffer `_calibration_constants`: `THM{artifact_suspicious}`.
6. **Paso / Step - Variante estática (Task 2):** `unzip -p signal_classifier/data/0` en el artefacto descargado imprime directamente `THM{artifact_suspicious}`; `pickletools.dis` de `data.pkl` prueba que es un buffer uint8 de 24 bytes.
7. **Paso / Step - Reconocimiento (Nightmare):** `nmap -sV --min-rate 3000 -p- 10.67.145.144` → `22/tcp` OpenSSH 9.6p1 y `5678/tcp` n8n v1.120.4 (confirmado por el meta tag `n8n:config:sentry`, base64). Único endpoint público: `POST /form/file-processor`.
8. **Paso / Step - CVE-2026-21858 (LFI):** El Form Trigger acepta `application/json` y confía en el campo `files[..].filepath` que manda el usuario. Con `"filepath":"/etc/passwd"` se obtiene el archivo; sin auth.
9. **Paso / Step - Loot de secretos:** LFI de `/proc/self/environ` (con `tr '\0' '\n'`) → `N8N_JWT_SECRET` y `N8N_ENCRYPTION_KEY`. LFI de `/home/node/.n8n/database.sqlite` → `user_entity` (email + bcrypt) y `workflow_entity` (workflow "Internal Automation — DO NOT SHARE" con webhook `secret-webhook`).
10. **Paso / Step - User flag:** LFI de `/home/node/flag-user-lfi.txt` → `THM{nightmare_just_begun}`.
11. **Paso / Step - JWT forgery:** El código fuente de n8n (auth.service.ts, v1.120.4) revela `createJWTHash(user) = sha256(email + ":" + bcrypt_hash).digest('base64').substring(0,10)`. Se forja un token HS256 (`{id, email, hash}`) con el secret filtrado y la cookie `n8n-auth`.
12. **Paso / Step - RCE vía workflow:** Como admin, PATCH del nodo "Execute Command" a `node -e "require('child_process').spawn('/bin/bash',['-i'],{stdio:'inherit'})"`; al re-disparar `/webhook/secret-webhook` se obtiene un PTY como `node`. (Alternativa inicial: el webhook fijo ejecuta `id`, RCE limitada sin auth.)
13. **Paso / Step - PrivEsc y escape:** `/setup.sh` (vía LFI o shell) contiene la password root hardcodeada `N1ghtm4r3R00t!CTF2026` → `su root` → `/host-root/` es bind-mount de la raíz del host → `cat /host-root/flag.txt` → root flag.

### Cadena de ataque / Attack Chain

```
Trojaned Model (10.67.188.40:8000)
  Banner -> POST /vendor/push usa torch.load(weights_only=False)
  -> pickle RCE (__reduce__ -> exec) deserializado en el push
  -> raise Exception(stdout+stderr) -> canal de error = canal de comando
  -> cat /flag                       -> THM{neural_c2_compromise}
  -> cat /etc/c2-hint.txt            -> THM{trigger_identified}
  -> exfiltrar signal_classifier.pt (base64) -> buffer _calibration_constants -> THM{artifact_suspicious}

Trojaned Model static (Task 2)
  file signal_classifier.pt -> ZIP -> unzip -p signal_classifier/data/0 -> THM{artifact_suspicious}

Nightmare (10.67.145.144)
  n8n v1.120.4 Form Trigger -> CVE-2026-21858 LFI (filepath confiado en JSON)
  -> /proc/self/environ -> N8N_JWT_SECRET + N8N_ENCRYPTION_KEY
  -> database.sqlite -> webhook secret-webhook + bcrypt + rutas de flags
  -> /home/node/flag-user-lfi.txt    -> THM{nightmare_just_begun}   [user flag]
  -> sha256("email:bcrypt")[:10] + HS256 -> JWT forjado -> admin
  -> PATCH Execute Command -> node -e spawn /bin/bash -> PTY como node
  -> /setup.sh -> N1ghtm4r3R00t!CTF2026 -> su root
  -> /host-root/flag.txt             -> THM{p4g3_c4ch3_g0t_wr1tt3n_k3rn3l_pwn3d_c0nt41n3r_3sc4p3d}  [root flag]
```

**Lección:** La cadena de suministro de IA encadena componentes "de confianza" que nunca fueron diseñados como frontera de seguridad: la deserialización (`torch.load` a medio camino de `exec`), el reflejo de excepciones como canal de exfiltración, los buffers de tensor que ocultan secretos, los parseadores de formularios que comparten confianza entre formatos (multipart vs JSON), los secretos en `/proc/self/environ`, el JWT con hash truncado de 10 caracteres, las passwords hardcodeadas en scripts de setup y los bind-mounts del host (`/host-root/`) que hacen del "container escape" un simple `cat`. Leer el código fuente real del producto objetivo ("source archaeology") suele ser la pieza que revela la vulnerabilidad invisible desde fuera.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.