# Plant Photographer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `plantphotographer` | [TryHackMe](https://tryhackme.com/room/plantphotographer) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=plantphotographer` + websearch de walkthroughs) | SSRF / Werkzeug Debug Console / Flask / URL Truncation / file:// / PIN Derivation / MD5 | Cadena SSRF → lectura arbitraria de archivos → RCE vía consola de debug de Werkzeug para leer la flag. |

---

**Contexto:**

> **ES:** Sala Web de dificultad Hard centrada en la combinación de SSRF (Server-Side Request Forgery) con la consola interactiva de debug de Flask/Werkzeug. Se explota una descarga por URL controlada por el usuario para filtrar la X-API-KEY del servicio de almacenamiento seguro, se usa la truncación con `%23` (`#`) para controlar la URL final, se abusa de `file://` para lectura arbitraria y de un endpoint interno `/admin`, y finalmente se obtiene RCE a través de la consola de debug (PIN de Werkzeug) para leer la flag del directorio web.
> **EN:** A Web room of Hard difficulty centered on the combination of SSRF (Server-Side Request Forgery) with the Flask/Werkzeug interactive debug console. A user-controlled URL download is exploited to leak the X-API-KEY of the secure storage service, `%23` (`#`) truncation is used to control the final URL, `file://` is abused for arbitrary file read along with an internal `/admin` endpoint, and finally RCE is achieved through the debug console (Werkzeug PIN) to read the flag in the web directory.

---

## Solucionario

### Task 1: Find the Flag

**Explicación:**
La sala plantea una cadena en la que primero se pide la API key del servicio de almacenamiento seguro (filtrada vía SSRF en el header `X-API-KEY`), después la flag de la sección admin (accediendo al endpoint interno `/admin` mediante truncación de URL con `%23`) y, por último, la flag almacenada en un fichero de texto del directorio web del servidor (obtenida tras tomar RCE a través de la consola de debug de Werkzeug con el PIN derivado de los datos del sistema).

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

### Cadena de ataque / Attack Chain

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

*Lección:* Un `debug=True` en producción convierte cualquier fallo en una consola de código remota si se puede derivar el PIN de Werkzeug a partir de datos del sistema (usuario, app path, MAC, machine-id). El SSRF, además, deja de ser "solo lectura" cuando la URL se controla por completo con una simple truncación (`%23`), habilitando tanto peticiones internas como lectura arbitraria con `file://`.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1552.001 (Unsecured Credentials: Credentials In Files), T1210 (Exploitation of Remote Services)

**Fuente:** [TryHackMe - Plant Photographer](https://tryhackme.com/room/plantphotographer)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.