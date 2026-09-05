# Plant Photographer [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF
* **Slug:** `plantphotographer`
* **Link:** https://tryhackme.com/room/plantphotographer
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=plantphotographer` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala Web de dificultad Hard centrada en la combinación de **SSRF** (Server-Side Request Forgery) con la **consola interactiva de debug de Flask/Werkzeug**. Se explota una descarga por URL controlada por el usuario para filtrar la `X-API-KEY` del servicio de almacenamiento seguro, se usa la truncación con `%23` (`#`) para controlar la URL final, se abusa de `file://` para lectura arbitraria y de un endpoint interno `/admin`, y finalmente se obtiene **RCE** a través de la consola de debug (PIN de Werkzeug) para leer la flag del directorio web.
> **EN:** Web room of Hard difficulty centered on combining **SSRF** (Server-Side Request Forgery) with the interactive **Flask/Werkzeug debug console**. A user-controlled URL download is abused to leak the secure storage service's `X-API-KEY`, `%23` (`#`) truncation is used to take control of the final URL, `file://` is abused for arbitrary read and an internal `/admin` endpoint, and finally **RCE** is obtained through the debug console (Werkzeug PIN) to read the web-directory flag.

### Task 1 - Find the Flag

> **ES:** Servidor con nmap → puertos 22 y 80 (Werkzeug 0.16.0 con `debug=True`). La app expone `/download?server=<host>&id=<id>`: el parámetro `server` es un **SSRF** — al apuntarlo a un listener propio, el servidor hace un GET con el header `X-API-KEY: THM{...}` y User-Agent `PycURL` (Q1 = header filtrado). Si `id` no es entero, se dispara la página de debug de Werkzeug que filtra la ruta del código fuente `/usr/src/app/app.py`; el código muestra que la URL construida es `<server>/public-docs-k057230990384293/<id>.pdf` y usa `pycurl`. Al terminar `server` en `%23` (`#`) se corta el sufijo fijo y se controla la URL entera: apuntando a `/admin` interno se obtiene `flag.pdf` (Q2). Con `file://.../%23` se consigue lectura arbitraria de archivos. Finalmente, recopilando los datos del PIN (usuario root vía `/proc/self/status`, app path `/usr/local/lib/python3.10/site-packages/flask/app.py`, MAC `02:42:ac:14:00:02` → `2485378088962`, y machine-id SOLO del cgroup) y sabiendo que **Werkzeug 0.16.0 usa MD5 (no SHA1)**, se calcula el PIN (ejemplo `110-688-511`), se entra en `/console` → **RCE** en Python → se lee la flag del directorio web (Q3). 3 preguntas.
> **EN:** Server via nmap → ports 22 and 80 (Werkzeug 0.16.0 with `debug=True`). The app exposes `/download?server=<host>&id=<id>`: the `server` parameter is an **SSRF** — pointing it at your own listener makes the server issue a GET carrying the `X-API-KEY: THM{...}` header and a `PycURL` User-Agent (Q1 = leaked header). If `id` is not an integer, the Werkzeug debug page is triggered and leaks the source path `/usr/src/app/app.py`; the code shows the URL is built as `<server>/public-docs-k057230990384293/<id>.pdf` and uses `pycurl`. Ending `server` in `%23` (`#`) truncates the fixed suffix and gives full control of the URL: pointing at the internal `/admin` retrieves `flag.pdf` (Q2). With `file://.../%23` arbitrary file read is achieved. Finally, collecting the PIN data (root user via `/proc/self/status`, app path `/usr/local/lib/python3.10/site-packages/flask/app.py`, MAC `02:42:ac:14:00:02` → `2485378088962`, and machine-id ONLY from the cgroup) and knowing that **Werkzeug 0.16.0 uses MD5 (not SHA1)**, the PIN is derived (e.g. `110-688-511`), `/console` is entered → **RCE** in Python → the web-directory flag is read (Q3). 3 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What API key is used to retrieve files from the secure storage service? | `THM{...redacted...}` |
| What is the flag in the admin section of the website? | `THM{...redacted...}` |
| What flag is stored in a text file in the server's web directory? | `THM{...redacted...}` |

> **Nota / Note:** Los walkthroughs públicos no publican los valores literales de las tres respuestas (instancia dinámica / autores que los ocultan). Q1 es el header `X-API-KEY` filtrado por el SSRF; Q2 es la flag dentro del PDF devuelto por `/admin`; Q3 es la flag del archivo de texto del directorio web tras el RCE vía `/console`. Se documenta el método, no el flag exacto.
> **EN:** Public walkthroughs do not publish the literal answers for the three questions (dynamic instance / authors masking them). Q1 is the `X-API-KEY` header leaked via SSRF; Q2 is the flag inside the PDF returned by `/admin`; Q3 is the flag from the text file in the web directory after `/console` RCE. The method is documented, not the exact flag.

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `nmap -sV` → `22/tcp` SSH y `80/tcp` HTTP. El banner/encabezados revelan **Werkzeug 0.16.0** de Flask.
2. **Paso / Step - SSRF en `server`:** `GET /download?server=<host>&id=<id>` provoca que el servidor vuelva a tu listener un GET con `X-API-KEY: THM{...}` y el User-Agent `PycURL` → Q1 (filtración del header).
3. **Paso / Step - Source leak vía debug:** Al pasar un `id` no numérico, la página de debug de Werkzeug (activa por `debug=True`) filtra la ruta `/usr/src/app/app.py`. El código fuente muestra que la descarga construye `<server>/public-docs-k057230990384293/<id>.pdf` usando `pycurl`.
4. **Paso / Step - Truncación con `%23`:** Terminar el parámetro `server` en `%23` (`#`) corta el sufijo fijo `/public-docs-k057230990384293/<id>.pdf`, dejándote control total de la URL que pide el servidor.
5. **Paso / Step - Endpoint interno `/admin`:** Apuntando el `server` truncado a `http://localhost/admin%23` se obtiene `flag.pdf` servido por la sección admin → Q2.
6. **Paso / Step - Lectura arbitraria `file://`:** Con `file:///etc/...%23` (combinando `file://` con la truncación) se leen archivos arbitrarios del contenedor.
7. **Paso / Step - Recopilar datos del PIN:** Para la consola de debug se necesitan: usuario `root` (`/proc/self/status`), app path `/usr/local/lib/python3.10/site-packages/flask/app.py`, MAC de la interfaz `02:42:ac:14:00:02` → `2485378088962`, y el **machine-id SOLO del cgroup** (`/docker/77c09e…049ca`, ignora `/etc/machine-id`).
8. **Paso / Step - Calcular el PIN (Werkzeug 0.16.0):** Esta versión usa **MD5** (no SHA1) para derivar el PIN. Con los datos anteriores se calcula el PIN (ejemplo del writeup: `110-688-511`).
9. **Paso / Step - RCE vía `/console`:** Con `debug=True` y el PIN correcto se abre `http://<host>/console` → ejecución de código Python en el servidor → se lee la flag del directorio web (Q3).

### Cadena de ataque / Attack Chain

```
nmap -> 22/tcp + 80/tcp (Werkzeug 0.16.0, debug=True)
  -> /download?server=<host>&id=<id>  (server = SSRF)
  -> listener propio -> GET con X-API-KEY: THM{...} (UA PycURL)   [Q1]
  -> id no entero -> página debug Werkzeug -> filtra /usr/src/app/app.py
  -> url = <server>/public-docs-k057230990384293/<id>.pdf (pycurl)
  -> server terminado en %23 (#) -> corta sufijo -> control de URL
  -> /admin interno            -> flag.pdf                       [Q2]
  -> file:// + %23             -> lectura arbitraria
  -> PIN: root (/proc/self/status) + app path + MAC 02:42:ac:14:00:02 -> 2485378088962 + machine-id SOLO cgroup (/docker/77c09e...049ca)
  -> Werkzeug 0.16.0 usa MD5 (no SHA1) -> PIN 110-688-511
  -> /console + PIN -> RCE Python -> flag del directorio web      [Q3]
```

**Lección:** Combinar un SSRF con la consola de debug de Flask convierte una lectura de archivos controlada en RCE total; y el PIN de Werkzeug, además de usar datos del cgroup y la MAC, cambia de algoritmo según la versión (MD5 en las antiguas, SHA1 en las nuevas), así que hay que leer el código fuente de la versión desplegada.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
