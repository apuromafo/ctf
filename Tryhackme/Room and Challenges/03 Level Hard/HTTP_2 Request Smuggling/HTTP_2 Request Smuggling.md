# HTTP_2 Request Smuggling [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `http2requestsmuggling`
* **Link:** https://tryhackme.com/room/http2requestsmuggling
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** thmrevenant (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala que explora el contrabando de peticiones HTTP/2 (HTTP/2 Request Smuggling). Se estudian las diferencias entre HTTP/1.1 y HTTP/2, se explotan desalineaciones H2.CL / H2.TE para envenenar la caché web, robustecer peticiones, robar cabeceras internas y, finalmente, secuestrar cookies y acceder a rutas protegidas como `/admin` y `/private`.
> **EN:** Room exploring HTTP/2 Request Smuggling. It covers the differences between HTTP/1.1 and HTTP/2, exploiting H2.CL / H2.TE desynchronization to poison the web cache, smuggle requests, leak internal headers, steal cookies and reach protected paths such as `/admin` and `/private`.

### Task 1 — Diferencias entre HTTP/1.1 y HTTP/2

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which version of the HTTP protocol uses \r\n to separate headers in a request? | HTTP/1.1 |
| Which version of the HTTP protocol uses a binary format and clearly defines boundaries for elements in requests/responses? | HTTP/2 |

### Task 2 — Contrabando de peticiones (H2.CL / H2.TE)

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Repeat the request shown in the practical example against the app and wait for a user to fall for our trap. What is the username of the victim user who liked our post? | `THM{my_name_is_a_flag}` |

### Task 3 — Fuga de cabeceras internas

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the value of the leaked internal header? | `THM{not_secret_anymore}` |

### Task 4 — Ruta protegida /admin

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the value of the flag in /admin? | `THM{staff_only}` |

### Task 5 — Envenenamiento de caché web

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the value of the cookie stolen using web cache poisoning? | `THM{nom_nom_cookies}` |

### Task 6 — Ruta protegida /private

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the value of the flag on /private? | `THM{walls_are_a_suggestion}` |

## Metodología / Methodology

1. **Paso / Step:** Se comprende la diferencia base del protocolo: HTTP/1.1 delimita las cabeceras con `\r\n`, mientras que HTTP/2 usa un formato binario con límites claros. Esta asimetría (frontend HTTP/2 hacia backend HTTP/1.1) es el terreno donde nace el contrabando.
2. **Paso / Step:** Se identifica la desincronización de versiones: técnicas H2.CL (Content-Length confuso) y H2.TE (Transfer-Encoding) permiten que el atacante deje una petición "colgada" que el servidor procesa como si fuera legítima.
3. **Paso / Step:** Se construye una petición maliciosa y se envía contra la aplicación, esperando a que un usuario real caiga en la trampa y su petición sea prefijada por la nuestra (smuggling).
4. **Paso / Step:** Con el contrabando activo se puede hacer que el servidor incluya cabeceras internas (internal headers) en la respuesta, filtrándolas al atacante.
5. **Paso / Step:** Se combina el smuggling con envenenamiento de caché web: una respuesta controlada por el atacante es cacheada y servida a otras víctimas, permitiendo robar su cookie de sesión.
6. **Paso / Step:** Finalmente se accede a recursos protegidos como `/admin` y `/private`, recuperando las flags finales.

### Cadena de ataque / Attack Chain

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

**Lección:** El contrabando de peticiones explota la desalineación entre frontends HTTP/2 y backends HTTP/1.1, y sus consecuencias pueden amplificarse combinándolo con envenenamiento de caché web para robar sesiones.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.