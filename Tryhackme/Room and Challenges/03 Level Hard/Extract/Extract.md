# Extract [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF
* **Slug:** `extract`
* **Link:** https://tryhackme.com/room/extract
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Writeups públicos de Jery0843/TryHackMe, jaxafed, matty69v, Majid Banday (Medium), Wild Wild Wolf y 0xb0b.

## Solucionario de Tareas / Task Solutions

> **ES:** Extract es un challenge web que encadena varias vulnerabilidades: un SSRF en `/preview.php` (parámetro `url`) bloquea `file://` pero permite `http://` y `gopher://`; se descubre un servicio interno Next.js en el puerto 10000, protegido por middleware vulnerable a CVE-2025-29927 (header `x-middleware-subrequest`), que tras el bypass entrega Flag 1 y las credenciales `librarian:L[REDACTED]!`. El SSRF reconvertido en proxy con gopher también salta la restricción de IP de `/management`, y una cookie PHP serializada no firmada (`O:9:"AuthToken":1:{s:9:"validated";b:0;}`) se altera a `b:1;` para saltar el 2FA y obtener Flag 2.
> **EN:** Extract is a web challenge chaining several vulnerabilities: an SSRF in `/preview.php` (`url` parameter) blocks `file://` but allows `http://` and `gopher://`; an internal Next.js service on port 10000 is discovered, protected by middleware vulnerable to CVE-2025-29927 (`x-middleware-subrequest` header), which after the bypass yields Flag 1 and the `librarian:L[REDACTED]!` credentials. The SSRF turned into a gopher proxy also bypasses the IP restriction of `/management`, and an unsigned serialized PHP cookie (`O:9:"AuthToken":1:{s:9:"validated";b:0;}`) is tampered to `b:1;` to skip 2FA and obtain Flag 2.

### Task 1 - Reconocimiento y SSRF en /preview.php / Reconnaissance and SSRF in /preview.php

> **ES:** Nmap revela dos puertos: 22 (OpenSSH 9.6p1) y 80 (Apache 2.4.58). El sitio "TryBookMe - Online Library" carga una preview de PDFs mediante `/preview.php?url=...`. Probando contra un servidor propio se confirma el SSRF; los protocolos `file://` están bloqueados por keyword pero `http://` y `gopher://` funcionan.
> **EN:** Nmap reveals two ports: 22 (OpenSSH 9.6p1) and 80 (Apache 2.4.58). The "TryBookMe - Online Library" site loads a PDF preview via `/preview.php?url=...`. Testing against an owned server confirms the SSRF; `file://` schemes are blocked by keyword but `http://` and `gopher://` work.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea práctica / Practical task) | `No answer needed` |

### Task 2 - Descubrimiento interno y proxy gopher / Internal Discovery and Gopher Proxy

> **ES:** Fuzzeando `http://127.0.0.1:FUZZ/` a través del SSRF se encuentra un servicio interno en el puerto 10000: una aplicación Next.js con un endpoint `/customapi` que responde "Not Authorized". Se escribe un pequeño proxy en Python que escucha localmente, recibe la petición, la codifica dos veces en URL y la envía por `gopher://` al servicio interno vía `/preview.php`, devolviendo la respuesta.
> **EN:** Fuzzing `http://127.0.0.1:FUZZ/` through the SSRF finds an internal service on port 10000: a Next.js application with a `/customapi` endpoint answering "Not Authorized". A small Python proxy is written: it listens locally, receives the request, double URL-encodes it and sends it via `gopher://` to the internal service through `/preview.php`, returning the response.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea práctica / Practical task) | `No answer needed` |

### Task 3 - Bypass de middleware Next.js (CVE-2025-29927) / Next.js Middleware Bypass (CVE-2025-29927)

> **ES:** Se añade el header `x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware` a la petición contra `/customapi`: la autenticación que vive en el middleware de Next.js se bypasea y la API devuelve la Flag 1 junto con las credenciales `librarian:L[REDACTED]!`.
> **EN:** The `x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware` header is added to the request against `/customapi`: the authentication living in the Next.js middleware is bypassed and the API returns Flag 1 along with the `librarian:L[REDACTED]!` credentials.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Flag 1 (Next.js /customapi) | `THM{...redacted...}` |

### Task 4 - Bypass de 2FA con manipulación de cookies / 2FA Bypass via Cookie Manipulation

> **ES:** Reconfigurando el proxy gopher para apuntar al puerto 80, `/management/` responde a la IP interna y muestra un login. Con `librarian:L[REDACTED]!` se inicia sesión y la app redirige a `/management/2fa.php`; la cookie `auth_token` contiene `O:9:"AuthToken":1:{s:9:"validated";b:0;}` (objeto PHP serializado, sin firma). Cambiando `b:0;` a `b:1;` el 2FA se considera validado y se obtiene la Flag 2.
> **EN:** Reconfiguring the gopher proxy to target port 80, `/management/` answers from the internal IP and shows a login. Logging in with `librarian:L[REDACTED]!` redirects to `/management/2fa.php`; the `auth_token` cookie contains `O:9:"AuthToken":1:{s:9:"validated";b:0;}` (a serialized, unsigned PHP object). Changing `b:0;` to `b:1;` marks the 2FA as validated and Flag 2 is retrieved.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Flag 2 (management / 2FA) | `THM{...redacted...}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `nmap -sC -sV -p-` muestra 22 (SSH) y 80 (Apache); el sitio solicita PDFs vía `/preview.php?url=...`, que se identifica como vector de SSRF.
2. **Paso / Step - Confirmar el SSRF:** `/preview.php?url=http://<IP-propia>/` genera un hit en el servidor del atacante; `file://` es bloqueado pero `http://` y `gopher://` funcionan.
3. **Paso / Step - Enumeración interna:** fuzzing de puertos en `127.0.0.1` vía SSRF descubre el puerto 10000 con una aplicación Next.js y su `/customapi`.
4. **Paso / Step - Proxy gopher:** un script Python escucha en local, hace doble URL-encoding de la petición y la entrega por `gopher://` al servicio interno, permitiendo mandar headers y métodos arbitrarios.
5. **Paso / Step - Bypass de autenticación:** el header `x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware` explota CVE-2025-29927; `/customapi` devuelve Flag 1 y las credenciales `librarian:L[REDACTED]!`.
6. **Paso / Step - Login interno:** apuntando el proxy gopher al puerto 80 se accede a `/management/` desde la IP interna, saltando la restricción de IP; el login con las credenciales obtenidas lleva a `/management/2fa.php`.
7. **Paso / Step - Bypass de 2FA:** la cookie `auth_token` (objeto PHP serializado sin firma) se modifica de `validated;b:0;` a `validated;b:1;`; se elimina la capa de 2FA y `/management/2fa.php` entrega Flag 2, completando la sala.

### Cadena de ataque / Attack Chain

```
nmap -> 22 (SSH) + 80 (Apache, TryBookMe)
              |
   GET /preview.php?url=<URL>   <- SSRF
              |   (file:// bloqueado, gopher:// OK)
              v
   fuzzing 127.0.0.1 -> puerto 10000 (Next.js /customapi)
              |
   proxy local (socket) + gopher:// + doble URL-encode
              |
   x-middleware-subrequest header  ->  CVE-2025-29927
              |
   /customapi -> Flag 1  +  librarian:L[REDACTED]!
              |
   gopher://127.0.0.1:80 -> /management/ (bypass IP)
              |
   login librarian -> cookie auth_token (PHP serialized)
              |
   validated;b:0;  ->  validated;b:1;
              |
   /management/2fa.php -> Flag 2
```

**Lección:** Un SSRF no es solo "desde dónde leer": con `gopher://` se convierte en un proxy TCP arbitrario capaz de lanzar peticiones HTTP crudas, explotar CVEs de infraestructura (Next.js middleware) y manipular sesiones no firmadas para esquivar segundas autenticaciones.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.