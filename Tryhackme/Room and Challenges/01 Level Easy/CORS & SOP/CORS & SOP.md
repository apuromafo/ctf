# CORS & SOP

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `corsandsop` |
| **Link** | [TryHackMe](https://tryhackme.com/room/corsandsop) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeups públicos de Ehxb (Medium), James Hacks, Justin Thompson y thmrevenant |
| **Componentes** | Same-Origin Policy / CORS / Access-Control-Allow-Origin / Access-Control-Allow-Credentials / regex bypass / null origin / XHR / iframe |
| **Impacto** | Domina la Same-Origin Policy y CORS y explota tres misconfiguraciones (origen arbitrario, regex débil y origen null) para exfiltrar datos autenticados en el navegador. |

---

**Contexto:** La sala CORS & SOP (web application pentesting) explica la Same-Origin Policy (SOP) y el Cross-Origin Resource Sharing (CORS): qué los define, qué cabeceras los controlan y qué sucede cuando el servidor confía ciegamente en el origen de la petición. Incluye un laboratorio con tres misconfiguraciones explotables: reflejo arbitrario del origen (`arbitrary.php`), regex débil (`badregex.php`) y origen `null` (`null.php`), exfiltrando datos con una página de exploit y un servidor receptor.

## Solucionario

### Task 1: Introducción

**Explicación:** Vista general de la sala: se aprende qué son SOP y CORS y cómo abusar de configuraciones incorrectas para robar datos sensibles en el navegador. Tarea de introducción, no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - introductory task. | `No answer needed` |

### Task 2: Same-Origin Policy y CORS

**Explicación:** La SOP restringe que una página acceda a recursos de otro origen (esquema + host + puerto). CORS relaja esa política mediante cabeceras HTTP enviadas por el servidor: `Access-Control-Allow-Origin` (ACAO) indica qué dominios pueden acceder. Configuraciones peligrosas: el comodín `*` (Wildcard Origin) y aceptar el origen `null`. El navegador, y no solo el servidor, es quien ejecuta la política.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What policy instructs web browsers how they should interact between web pages? | `Same-origin Policy` |
| 2 | What HTTP header specifies which domains are allowed to access the resources hosted in its server? | `Access-Control-Allow-Origin` |
| 3 | What origin configuration permits requests from any origin, is the least secure configuration, and should be used cautiously? | `Wildcard Origin` |
| 4 | What CORS misconfiguration occurs when a server accepts requests from the "null" origin? | `Null Origin Misconfiguration` |

### Task 3: Configuración del laboratorio

**Explicación:** Se añaden dominios al `/etc/hosts` apuntando a la IP de la máquina: `corssop.thm` (sitio vulnerable), `exploit.evilcors.thm` (servidor del atacante que aloja el código) y `corssop.thm.evilcors.thm` (página que visita la víctima). Se prepara un `receiver.php` para capturar los datos exfiltrados y guardarlos en `data.txt`. Tarea práctica, sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - practical setup. | `No answer needed` |

### Task 4: Explotando Arbitrary Origin

**Explicación:** `arbitrary.php` refleja el valor de `HTTP_ORIGIN` en `Access-Control-Allow-Origin` y además activa `Access-Control-Allow-Credentials: true`, validando cualquier dominio. Un script en el navegador de la víctima envía peticiones cross-origin con cookies y el servidor receptor captura la respuesta sensible. Flag: `THM{4rB1tr4rY}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag from arbitrary.php? | `THM{4rB1tr4rY}` |

### Task 5: Explotando Bad Regex

**Explicación:** `badregex.php` valida el origen con `preg_match('#corssop.thm#')`, es decir, comprueba solo que la cadena `corssop.thm` aparezca en cualquier parte. Un dominio como `corssop.thm.evilcors.thm` cumple el patrón y consigue una respuesta legítima con `Access-Control-Allow-Credentials: true`. Flag: `THM{B4D_r363X}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag from badregex.php? | `THM{B4D_r363X}` |

### Task 6: Explotando Null Origin

**Explicación:** `null.php` responde `Access-Control-Allow-Origin: null` con credenciales. Un `iframe` con sandbox (o documentos del tipo `file://`/data) genera un origen `null` desde el navegador de la víctima, permitiendo leer la respuesta del endpoint protegido. Flag: `THM{nULL_0r1G1N}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag from null.php? | `THM{nULL_0r1G1N}` |

### Task 7: Conclusión

**Explicación:** La sala concluye recordando que CORS mal implementado convierte al navegador en una herramienta de exfiltración: siempre validar contra una lista blanca de orígenes y nunca reflejar `Origin` ni confiar en `null` o en comodines junto a credenciales. Tarea de cierre, sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - wrap-up task. | `No answer needed` |

---

**Metodología:**
1. **Conceptos:** se estudian los orígenes (esquema + host + puerto), la SOP como política por defecto y el rol del navegador en la aplicación de CORS.
2. **Cabeceras clave:** `Access-Control-Allow-Origin` decide los dominios permitidos; `Access-Control-Allow-Credentials: true` permite cookies; las preflights (`OPTIONS`) se activan con cross-origin requests complejas.
3. **Montar el laboratorio:** se configura `/etc/hosts` con `corssop.thm`, `exploit.evilcors.thm` y `corssop.thm.evilcors.thm`, y se aloja un `receiver.php` que guarda lo recibido en `data.txt`.
4. **Arbitrary Origin:** se envía `Origin: http://evilcors.thm` a `arbitrary.php`; el servidor lo refleja en ACAO con credenciales (`Access-Control-Allow-Credentials: true`), y un XHR desde la página de exploit extrae la flag `THM{4rB1tr4rY}`.
5. **Bad Regex:** `preg_match('#corssop.thm#')` se bypasea usando `corssop.thm.evilcors.thm` como origen, que contiene la cadena esperada; la respuesta legítima con credenciales permite leer la flag `THM{B4D_r363X}`.
6. **Null Origin:** se carga el exploit desde un `iframe` con sandbox (o documento `file://`/data) para forzar `Origin: null`; la respuesta de `null.php` con ACAO `null` y credenciales es legible, recuperando la flag `THM{nULL_0r1G1N}`.
7. **Mitigación:** la corrección pasa por una allow-list estricta de orígenes, sin reflejar `Origin`, y prefijos seguros en las regex de validación.

**Learning chain:** SOP (esquema+host+puerto) → cabecera ACAO + credentials → laboratorio /etc/hosts + receiver.php → arbitrary origin reflection → regex bypass (`.evilcors.thm`) → null origin via sandboxed iframe → exfiltración de flags.

**MITRE ATT&CK:** T1189 (Drive-by Compromise), T1041 (Exfiltration Over C2 Channel), T1059.007 (Command and Scripting Interpreter: JavaScript).

**Fuente:** [TryHackMe - CORS & SOP](https://tryhackme.com/room/corsandsop)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
