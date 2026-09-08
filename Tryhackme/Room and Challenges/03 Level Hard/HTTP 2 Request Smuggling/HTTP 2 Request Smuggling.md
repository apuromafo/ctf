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

**Explicación:** Pregunta teórica de protocolo. HTTP/1.1 es textual y delimita cada cabecera con `\r\n`; HTTP/2 usa un **formato binario** con tramas (frames) y límites claramente definidos para cada elemento, por lo que no necesita secuencias de texto para separar cabeceras.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which version of the HTTP protocol uses \r\n to separate headers in a request? | `HTTP/1.1` |
| 2 | Which version of the HTTP protocol uses a binary format and clearly defines boundaries for elements in requests/responses? | `HTTP/2` |

### Task 2: Contrabando de peticiones (H2.CL / H2.TE)

**Explicación:** El frontend habla HTTP/2 y reescribe (o confunde) las cabeceras hacia un backend HTTP/1.1. Con técnicas **H2.CL** (Content-Length ambiguo) y **H2.TE** (Transfer-Encoding), se deja una petición "colgada" en el socket del backend; la siguiente petición de un usuario real se verá prefijada por la nuestra. Repitiendo el ejemplo práctico contra la app y esperando que una víctima caiga en la trampa, el usuario que dio "like" a nuestro post es el bot `THM{my_name_is_a_flag}`.

```http
# ejemplo de payload H2.TE: petición con x:keep-alive y transfer-encoding
POST / HTTP/2
content-length: 4
transfer-encoding: chunked

0

GET /messages HTTP/1.1
host: <app>
...
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repeat the request shown in the practical example against the app and wait for a user to fall for our trap. What is the username of the victim user who liked our post? | `THM{my_name_is_a_flag}` |

### Task 3: Fuga de cabeceras internas

**Explicación:** Con el smuggling activo se hace que el backend incluya cabeceras internas (las que la infraestructura añade, como `X-Internal-*` o la autenticación del proxy) dentro de nuestra respuesta. El valor de la cabecera interna filtrada es **`THM{not_secret_anymore}`**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the value of the leaked internal header? | `THM{not_secret_anymore}` |

### Task 4: Ruta protegida /admin

**Explicación:** El contrabando también sirve para alcanzar rutas que rechazan peticiones directas: dentro del flujo smuggled se pide `/admin` y el backend responde con el flag **`THM{staff_only}`**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the flag in /admin? | `THM{staff_only}` |

### Task 5: Envenenamiento de caché web

**Explicación:** Combinando el smuggled request con **Web Cache Poisoning**, se hace que la caché guarde una respuesta controlada (con un redirect/reflect) y la sirva a las siguientes víctimas: su cookie de sesión llega al atacante. El valor de la cookie robada es **`THM{nom_nom_cookies}`**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the cookie stolen using web cache poisoning? | `THM{nom_nom_cookies}` |

### Task 6: Ruta protegida /private

**Explicación:** Con la sesión/cookie robada o mediante una petición smuggled dirigida, se alcanza la ruta `/private`, que devuelve el flag **`THM{walls_are_a_suggestion}`**.

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