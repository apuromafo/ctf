# Extract

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `extract` |
| **Link** | [TryHackMe](https://tryhackme.com/room/extract) |
| **Sección** | 03 Level Hard |
| **Fuente** | Writeups públicos de Jery0843/TryHackMe, jaxafed, matty69v, Majid Banday (Medium), Wild Wild Wolf y 0xb0b. |
| **Componentes** | SSRF / gopher / Next.js / CVE-2025-29927 / PHP serialization / 2FA / Python |
| **Impacto** | Encadenamiento de vulnerabilidades web: SSRF con proxy gopher hacia un servicio interno Next.js, bypass de middleware (CVE-2025-29927) y manipulación de una cookie PHP serializada para saltar el 2FA. |

---

**Contexto:** Extract es un challenge web que encadena varias vulnerabilidades: un SSRF en `/preview.php` (parámetro `url`) bloquea `file://` pero permite `http://` y `gopher://`; se descubre un servicio interno Next.js en el puerto 10000, protegido por middleware vulnerable a CVE-2025-29927 (header `x-middleware-subrequest`), que tras el bypass entrega Flag 1 y las credenciales `librarian:L[REDACTED]!`. El SSRF reconvertido en proxy con gopher también salta la restricción de IP de `/management`, y una cookie PHP serializada no firmada (`O:9:"AuthToken":1:{s:9:"validated";b:0;}`) se altera a `b:1;` para saltar el 2FA y obtener Flag 2.

## Solucionario

### Task 1: Reconocimiento y SSRF en /preview.php

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Descubrimiento interno y proxy gopher

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 3: Bypass de middleware Next.js (CVE-2025-29927)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 (Next.js /customapi) | `THM{...redacted...}` |

### Task 4: Bypass de 2FA con manipulación de cookies

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 2 (management / 2FA) | `THM{...redacted...}` |

---

**Metodología:**
1. **Reconocimiento:** `nmap -sC -sV -p-` muestra 22 (SSH) y 80 (Apache); el sitio solicita PDFs vía `/preview.php?url=...`, que se identifica como vector de SSRF.
2. **Confirmar el SSRF:** `/preview.php?url=http://<IP-propia>/` genera un hit en el servidor del atacante; `file://` está bloqueado por keyword pero `http://` y `gopher://` funcionan.
3. **Enumeración interna:** fuzzing de puertos en `127.0.0.1` vía SSRF descubre el puerto 10000 con una aplicación Next.js y su `/customapi`.
4. **Proxy gopher:** un script Python escucha en local, hace doble URL-encoding de la petición y la entrega por `gopher://` al servicio interno, permitiendo mandar headers y métodos arbitrarios.
5. **Bypass de autenticación:** el header `x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware` explota CVE-2025-29927; `/customapi` devuelve Flag 1 y las credenciales `librarian:L[REDACTED]!`.
6. **Login interno:** apuntando el proxy gopher al puerto 80 se accede a `/management/` desde la IP interna, saltando la restricción de IP; el login con esas credenciales lleva a `/management/2fa.php`.
7. **Bypass de 2FA:** la cookie `auth_token` (objeto PHP serializado sin firma: `O:9:"AuthToken":1:{s:9:"validated";b:0;}`) se modifica de `validated;b:0;` a `validated;b:1;`; se elimina la capa de 2FA y `/management/2fa.php` entrega Flag 2, completando la sala.
8. **Nota:** las flags 1 y 2 solo aparecen redactadas en las fuentes públicas; se documenta el método completo para obtenerlas, no el literal exacto.

**Learning chain:** `nmap → 22 (SSH) + 80 (Apache, TryBookMe) → /preview.php?url= SSRF (file:// bloqueado, gopher:// OK) → fuzzing 127.0.0.1 → puerto 10000 (Next.js /customapi) → proxy local + gopher:// + doble URL-encode → x-middleware-subrequest → CVE-2025-29927 → /customapi → Flag 1 + librarian:L[REDACTED]! → gopher://127.0.0.1:80 → /management/ (bypass IP) → login → cookie auth_token (PHP serialized) → validated;b:0 → b:1 → /management/2fa.php → Flag 2`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1090 (Connection Proxy), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Extract](https://tryhackme.com/room/extract)