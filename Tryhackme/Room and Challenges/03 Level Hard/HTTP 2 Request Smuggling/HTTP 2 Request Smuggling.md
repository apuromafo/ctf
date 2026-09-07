# HTTP 2 Request Smuggling

| **Dificultad** | Hard |
| **Tipo** | Walkthrough |
| **Slug** | `http2requestsmuggling` |
| **Link** | [TryHackMe](https://tryhackme.com/room/http2requestsmuggling) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | HTTP/1.1 / HTTP/2 / H2.CL / H2.TE / Web Cache Poisoning / Burp Suite |
| **Impacto** | Contrabando de peticiones HTTP/2 combinado con envenenamiento de caché web para robar sesiones. |

---

**Contexto:** Sala que explora el contrabando de peticiones HTTP/2 (HTTP/2 Request Smuggling). Se estudian las diferencias entre HTTP/1.1 y HTTP/2, se explotan desalineaciones H2.CL / H2.TE para envenenar la caché web, robustecer peticiones, robar cabeceras internas y, finalmente, secuestrar cookies y acceder a rutas protegidas como `/admin` y `/private`.

## Solucionario

### Task 1: Diferencias entre HTTP/1.1 y HTTP/2

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which version of the HTTP protocol uses \r\n to separate headers in a request? | `HTTP/1.1` |
| 2 | Which version of the HTTP protocol uses a binary format and clearly defines boundaries for elements in requests/responses? | `HTTP/2` |

### Task 2: Contrabando de peticiones (H2.CL / H2.TE)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repeat the request shown in the practical example against the app and wait for a user to fall for our trap. What is the username of the victim user who liked our post? | `THM{my_name_is_a_flag}` |

### Task 3: Fuga de cabeceras internas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the value of the leaked internal header? | `THM{not_secret_anymore}` |

### Task 4: Ruta protegida /admin

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the flag in /admin? | `THM{staff_only}` |

### Task 5: Envenenamiento de caché web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the cookie stolen using web cache poisoning? | `THM{nom_nom_cookies}` |

### Task 6: Ruta protegida /private

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the value of the flag on /private? | `THM{walls_are_a_suggestion}` |

---

**Metodología:**

1. Se comprende la diferencia base del protocolo: HTTP/1.1 delimita las cabeceras con `\r\n`, mientras que HTTP/2 usa un formato binario con límites claros. Esta asimetría (frontend HTTP/2 hacia backend HTTP/1.1) es el terreno donde nace el contrabando.
2. Se identifica la desincronización de versiones: técnicas H2.CL (Content-Length confuso) y H2.TE (Transfer-Encoding) permiten que el atacante deje una petición "colgada" que el servidor procesa como si fuera legítima.
3. Se construye una petición maliciosa y se envía contra la aplicación, esperando a que un usuario real caiga en la trampa y su petición sea prefijada por la nuestra (smuggling).
4. Con el contrabando activo se puede hacer que el servidor incluya cabeceras internas (internal headers) en la respuesta, filtrándolas al atacante.
5. Se combina el smuggling con envenenamiento de caché web: una respuesta controlada por el atacante es cacheada y servida a otras víctimas, permitiendo robar su cookie de sesión.
6. Finalmente se accede a recursos protegidos como `/admin` y `/private`, recuperando las flags finales.

```
Recon (diferencias HTTP/1.1 vs HTTP/2)
  -> Identificar frontend HTTP/2 + backend HTTP/1.1 (desalineación de protocolos)
  -> Construir payload H2.CL / H2.TE (petición envenenada)
  -> Smuggle de petición contra la app
  -> Esperar a que una víctima caiga en la trampa (victim liked our post)
  -> Leak de cabecera interna (internal header)
  -> Web Cache Poisoning -> robo de cookie de sesión
  -> Acceso a /admin y /private -> flags
```

**Learning chain:** Recon HTTP/1.1 vs HTTP/2 → H2.CL / H2.TE smuggling → Petición envenenada → Leak de cabeceras internas → Web Cache Poisoning → Robo de cookie → Acceso a rutas protegidas → Flags

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1105 (Ingress Tool Transfer), T1530 (Data from Cloud Storage)

**Fuente:** [TryHackMe - HTTP 2 Request Smuggling](https://tryhackme.com/room/http2requestsmuggling)
