# CORS & SOP [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `corsandsop`
* **Link:** https://tryhackme.com/room/corsandsop
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Writeups públicos de Ehxb (Medium), James Hacks, Justin Thompson y thmrevenant.

## Solucionario de Tareas / Task Solutions

> **ES:** La sala CORS & SOP (web application pentesting) explica la Same-Origin Policy (SOP) y el Cross-Origin Resource Sharing (CORS): qué los define, qué cabeceras los controlan y qué sucede cuando el servidor confía ciegamente en el origen de la petición. Incluye un laboratorio con tres misconfiguraciones explotables: reflejo arbitrario del origen (`arbitrary.php`), regex débil (`badregex.php`) y origen `null` (`null.php`), exfiltrando datos con una página de exploit y un servidor receptor.
> **EN:** The CORS & SOP room (web application pentesting) explains the Same-Origin Policy (SOP) and Cross-Origin Resource Sharing (CORS): what defines them, which headers control them, and what happens when a server blindly trusts the request origin. It includes a lab with three exploitable misconfigurations: arbitrary origin reflection (`arbitrary.php`), weak regex (`badregex.php`) and the `null` origin (`null.php`), exfiltrating data with an exploit page and a receiving server.

### Task 1 - Introducción / Introduction

> **ES:** Vista general de la sala: se aprende qué son SOP y CORS y cómo abusar de configuraciones incorrectas para robar datos sensibles en el navegador.
> **EN:** Overview of the room: learn what SOP and CORS are and how to abuse misconfigurations to steal sensitive data in the browser.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea de introducción / Introduction task) | `No answer needed` |

### Task 2 - Same-Origin Policy y CORS / Same-Origin Policy and CORS

> **ES:** La SOP restringe que una página acceda a recursos de otro origen (esquema + host + puerto). CORS relaja esa política mediante cabeceras HTTP enviadas por el servidor: `Access-Control-Allow-Origin` (ACAO) indica qué dominios pueden acceder. Configuraciones peligrosas: comodín `*` (Wildcard Origin) y aceptar el origen `null`. El navegador, no solo el servidor, es quien ejecuta la política.
> **EN:** SOP restricts a page from accessing resources from another origin (scheme + host + port). CORS relaxes that policy through HTTP headers sent by the server: `Access-Control-Allow-Origin` (ACAO) states which domains may access. Dangerous configurations: the `*` wildcard (Wildcard Origin) and accepting the `null` origin. The browser, not only the server, enforces the policy.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What policy instructs web browsers how they should interact between web pages? | `Same-origin Policy` |
| What HTTP header specifies which domains are allowed to access the resources hosted in its server? | `Access-Control-Allow-Origin` |
| What origin configuration permits requests from any origin, is the least secure configuration, and should be used cautiously? | `Wildcard Origin` |
| What CORS misconfiguration occurs when a server accepts requests from the "null" origin? | `Null Origin Misconfiguration` |

### Task 3 - Configuración del laboratorio / Lab Setup

> **ES:** Se añaden dominios al `/etc/hosts` apuntando a la IP de la máquina: `corssop.thm` (sitio vulnerable), `exploit.evilcors.thm` (servidor del atacante que aloja el código) y `corssop.thm.evilcors.thm` (página que visita la víctima). Se prepara un `receiver.php` para capturar los datos exfiltrados.
> **EN:** Domains are added to `/etc/hosts` pointing to the machine's IP: `corssop.thm` (vulnerable site), `exploit.evilcors.thm` (attacker server hosting the code) and `corssop.thm.evilcors.thm` (page the victim visits). A `receiver.php` is prepared to collect the exfiltrated data.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea práctica / Practical task) | `No answer needed` |

### Task 4 - Explotando Arbitrary Origin / Exploiting Arbitrary Origin

> **ES:** `arbitrary.php` refleja el valor de `HTTP_ORIGIN` en `Access-Control-Allow-Origin` y además activa `Access-Control-Allow-Credentials: true`, validando cualquier dominio. Un script en el navegador de la víctima envía peticiones cross-origin con cookies y el servidor receptor captura la respuesta sensible.
> **EN:** `arbitrary.php` reflects the `HTTP_ORIGIN` value in `Access-Control-Allow-Origin` and also sets `Access-Control-Allow-Credentials: true`, trusting any domain. A script in the victim's browser sends cross-origin requests with cookies and the receiving server captures the sensitive response.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag from arbitrary.php? | `THM{4rB1tr4rY}` |

### Task 5 - Explotando Bad Regex / Exploiting Bad Regex

> **ES:** `badregex.php` valida el origen con `preg_match('#corssop.thm#')`, es decir, comprueba solo que la cadena `corssop.thm` aparezca en cualquier parte. Un dominio como `corssop.thm.evilcors.thm` cumple el patrón y consigue una respuesta legítima con `Access-Control-Allow-Credentials: true`.
> **EN:** `badregex.php` validates the origin with `preg_match('#corssop.thm#')`, i.e. it only checks that the string `corssop.thm` appears anywhere. A domain such as `corssop.thm.evilcors.thm` matches the pattern and gets a legitimate response with `Access-Control-Allow-Credentials: true`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag from badregex.php? | `THM{B4D_r363X}` |

### Task 6 - Explotando Null Origin / Exploiting Null Origin

> **ES:** `null.php` responde `Access-Control-Allow-Origin: null` con credenciales. Un `iframe` con sandbox (o documentos del tipo `file://`/data) genera un origen `null` desde el navegador de la víctima, permitiendo leer la respuesta del endpoint protegido.
> **EN:** `null.php` responds `Access-Control-Allow-Origin: null` with credentials. A sandboxed `iframe` (or `file://`/data documents) produces a `null` origin from the victim's browser, allowing the protected endpoint's response to be read.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag from null.php? | `THM{nULL_0r1G1N}` |

### Task 7 - Conclusión / Conclusion

> **ES:** La sala concluye recordando que CORS mal implementado convierte al navegador en una herramienta de exfiltración: siempre validar contra una lista blanca de orígenes y nunca reflejar `Origin` ni confiar en `null` o en comodines junto a credenciales.
> **EN:** The room concludes by reminding that poorly implemented CORS turns the browser into an exfiltration tool: always validate against an origin allow-list and never reflect `Origin` or trust `null` or wildcards alongside credentials.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea de cierre / Wrap-up task) | `No answer needed` |

## Metodología / Methodology

1. **Paso / Step - Conceptos:** se estudian los orígenes (esquema + host + puerto), la SOP como política por defecto y el rol del navegador en la aplicación de CORS.
2. **Paso / Step - Cabeceras clave:** `Access-Control-Allow-Origin` decide los dominios permitidos; `Access-Control-Allow-Credentials: true` permite cookies; las preflights (`OPTIONS`) se activan con cross-origin requests complejas.
3. **Paso / Step - Montar el laboratorio:** se configura `/etc/hosts` con `corssop.thm`, `exploit.evilcors.thm` y `corssop.thm.evilcors.thm`, y se aloja un `receiver.php` que guarda lo recibido en `data.txt`.
4. **Paso / Step - Arbitrary Origin:** se envía `Origin: http://evilcors.thm` a `arbitrary.php`; el servidor lo refleja en ACAO con credenciales, y un XHR from the exploit page extrae la flag.
5. **Paso / Step - Bad Regex:** `preg_match('#corssop.thm#')` se bypasea usando `corssop.thm.evilcors.thm` como origen, que contiene la cadena esperada.
6. **Paso / Step - Null Origin:** se carga el exploit desde un `iframe` sandbox para forzar `Origin: null`; la respuesta de `null.php` con ACAO `null` es legible y se recupera la última flag.
7. **Paso / Step - Mitigación:** la corrección pasa por una allow-list estricta de orígenes, sin reflejar `Origin`, y prefijos seguros en las regex de validación.

### Cadena de ataque / Attack Chain

```
Víctima visita corssop.thm.evilcors.thm (página del atacante)
                        |
              XMLHttpRequest / fetch (cross-origin)
                        |
   Origin: http://evilcors.thm | corssop.thm.evilcors.thm | null
                        |
   Servidor vulnerable: ACAO: <origen tal cual> + ACAC: true
                        |
   El navegador permite leer la respuesta sensible
                        |
       POST de los datos -> receiver.php -> data.txt (atacante)
```

**Lección:** Aceptar un origen arbitrario, confiar en `null` o en una regex débil convierte a CORS en una puerta abierta a la exfiltración de datos autenticados. La regla de oro es validar contra una lista blanca estricta y nunca combinar `*` con credenciales.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.