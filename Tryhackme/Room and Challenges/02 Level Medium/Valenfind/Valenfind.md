# Valenfind [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e10`
* **Link:** https://tryhackme.com/room/lafb2026e10
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e10`, InfoSec Write-ups, medium.com/@sudoroot523, sahandbabali.com)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026) de dificultad Medium y tema **Web**. "Valenfind" es una app de citas recién lanzada ("vibe-coded"; el creador aprendió a programar recién este año). El objetivo es explotar una cadena sencilla: un endpoint de frontend con **LFI / path traversal** que, leyendo `/proc/self/cmdline`, revela la ruta del backend, permite leer el código fuente de la app Flask, extraer una **API key admin hardcodeada** y descargar la base de datos SQLite completa con la flag.
> **EN:** Event room (Love at First Breach 2026) of Medium difficulty focused on **Web**. "Valenfind" is a freshly launched dating app ("vibe-coded"; the creator only learned to code this year). The goal is to exploit a simple chain: a frontend endpoint with **LFI / path traversal** that, by reading `/proc/self/cmdline`, reveals the backend path, lets you read the Flask app source code, pull out a **hardcoded admin API key** and download the full SQLite database with the flag.

### Task 1 - Valenfind

> **ES:** Target `http://MACHINE_IP:5000`. Una app de citas escrita con código generado por IA. Al explotar una vulnerabilidad de path traversal en `/api/fetch_layout` (expuesto por el JS del frontend) se leen archivos del servidor: `/etc/passwd` confirma el LFI, `/proc/self/cmdline` revela que la app vive en `/opt/Valenfind/app.py`, y la lectura de ese source recoge la constante `ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO"`. Con ese token se llama a `/api/admin/export_db` y se descarga `cupid.db`; la flag está en la tabla `users`. 1 pregunta.
> **EN:** Target `http://MACHINE_IP:5000`. A dating app written with AI-generated code. By exploiting a path traversal in `/api/fetch_layout` (exposed by the frontend JS) you can read server files: `/etc/passwd` confirms the LFI, `/proc/self/cmdline` reveals the app lives at `/opt/Valenfind/app.py`, and reading that source yields the constant `ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO"`. With that token you call `/api/admin/export_db` and download `cupid.db`; the flag lives in the `users` table. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{v1be_c0ding_1s_n0t_my_cup_0f_t3a}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento y exploración:** `http://MACHINE_IP:5000` es una app de citas. La pista del enunciado apunta a "vibe-coding" (código generado por IA que suele ignorar la seguridad). Al registrarse y navegar los perfiles, el perfil de "Cupid" (mensajes/pistas de los desarrolladores) señala hacia el código fuente del frontend.
2. **Paso / Step - Endpoint vulnerable en el JS:** Revisando el código JavaScript de la página se encuentra un endpoint de frontend `/api/fetch_layout?layout=<path>` que devuelve el contenido de rutas sin sanitizar (path traversal / LFI). Confirmar leyendo `/etc/passwd`.
3. **Paso / Step - /proc/self/cmdline:** `http://MACHINE_IP:5000/api/fetch_layout?layout=../../../../proc/self/cmdline` devuelve la línea de comandos del proceso (`.` enmascarado como `/`): `/usr/bin/python3 /opt/Valenfind/app.py`. Con esto se conoce la ubicación exacta del backend.
4. **Paso / Step - Lectura del código fuente:** `layout=../../../../opt/Valenfind/app.py` devuelve el código completo de la app Flask. En él: `ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO"` hardcodeada y `DATABASE = 'cupid.db'`.
5. **Paso / Step - Endpoint de exportación admin:** El código revela la ruta `/api/admin/export_db` que exige el header `X-Valentine-Token` con el valor de `ADMIN_API_KEY`.
6. **Paso / Step - Descarga de la base de datos:** `curl -H "X-Valentine-Token: CUPID_MASTER_KEY_2024_XOXO" http://MACHINE_IP:5000/api/admin/export_db -o valenfind_leak.db`.
7. **Paso / Step - Flag:** `sqlite3 valenfind_leak.db` → `SELECT * FROM users;` → la flag está en los datos de los usuarios.

### Cadena de ataque / Attack Chain

```
App de citas (http://MACHINE_IP:5000)
  -> JS del frontend expone /api/fetch_layout?layout=<path>  (sin sanitizar)
  -> LFI: /etc/passwd                         confirma path traversal
  -> LFI: /proc/self/cmdline                  -> /usr/bin/python3 /opt/Valenfind/app.py
  -> LFI: /opt/Valenfind/app.py               -> ADMIN_API_KEY = "CUPID_MASTER_KEY_2024_XOXO"
  -> POST/GET /api/admin/export_db  con header X-Valentine-Token: CUPID_MASTER_KEY_2024_XOXO
  -> descarga cupid.db (SQLite)
  -> SELECT * FROM users                       -> THM{v1be_c0ding_1s_n0t_my_cup_0f_t3a}
```

**Lección:** El código generado por IA ("vibe-coding") suele reutilizar patrones inseguros que pasan desapercibidos en review humano: parámetros de ruta sin sanitizar (LFI), secretos hardcodeados en el código fuente y endpoints de administración protegidos solo por un token estático. Una vez que un LFI permite leer el código, cualquier secreto embebido en él queda expuesto; la combinación LFI → lectura de código → secretos → descarga de la BD es la cadena completa.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.