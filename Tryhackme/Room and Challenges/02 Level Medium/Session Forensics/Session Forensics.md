# Session Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / DFIR (Web) | sessionforensics | https://tryhackme.com/room/sessionforensics | 02 Level Medium | TryHackMe | Sesiones y JWT, logs de aplicación/servidor web/Identity Provider, análisis forense de tokens (jwt.io/base64), forgery de JWT (alg:none, secreto débil), localStorage, revocación, contención y remediación | Detección y análisis forense de un ataque de falsificación de JWT (role user → admin) en el portal interno TryFlufMe, con reconstrucción de la línea de tiempo y medidas de contención/remediación |

---

**Contexto:** La sala **Session Forensics** explica cómo se crean, almacenan y usan las **sesiones y los JSON Web Tokens (JWT)**, y cómo investigarlos cuando han sido comprometidos. Se repasan los mecanismos de defensa (revocación y protección contra session hijacking) y los tres tipos de registros útiles para el forense: **logs de aplicación** (escalada de privilegios), **logs del servidor web** (user-agent e IPs) y **logs del Identity Provider** (emisión y falsificación de tokens). En la parte práctica se analizan `webserver.log`, `app.log`, `idp.log` y un `browser_dump.txt`: el usuario **FluffyCat** obtuvo un token legítimo (HS256, rol `user`) y después usó un token falsificado (header `alg: none`, rol `admin`) para acceder a `/admin`, escalada que el IdP nunca emitió. El cierre cubre la contención (revocación de sesiones, restablecimiento de credenciales) y la remediación (validación estricta de firma, validación del issuer, cookies HTTP-only en lugar de localStorage y verificación/anti-replay de tokens).

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: sesiones y tokens en el corazón de la autenticación web y técnicas forenses para investigar sesiones y JWT comprometidos. No se requiere respuesta.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| 1. Leer la introducción | `No answer needed` |

### Task 2: Repaso de sesiones y JWT / Recap Session & JWT
**Explicación:** Los JWT son stateless (la sesión vive en el cliente, normalmente `localStorage`/`sessionStorage`), y el token tiene header, payload y firma. Para protegerlos hay que implementar **revocación**; robar la ID de sesión de otro usuario es un ataque de **session hijacking**.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| 1. What security mechanism do you have to implement when introducing JWT? | `revocation` |
| 2. What is the attack called when an attacker steals your session ID? | `session hijacking` |

### Task 3: Descifrado e inspección de tokens / Decoding and Inspecting Tokens
**Explicación:** Cada fuente de logs aporta una faceta distinta: los **application logs** (app.log) ayudan a rastrear escaladas de privilegios (cambios de rol, validaciones); los **web server logs** mapean user-agents e IPs y suelen llevar el token en el header `Authorization`; y los **Identity Provider logs** registran la emisión de tokens, por lo que son el lugar correcto para comprobar si un JWT ha sido **forjado**. El dump del navegador (`localStorage`) también es un artefacto forense valioso.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| 1. Where would you find logs useful for investigating privilege escalation? | `application logs` |
| 2. Where would you find logs useful for mapping user-agent and IP addresses? | `web server logs` |
| 3. Which logs would you check if a JWT token has been forged? | `Identity Provider logs` |

### Task 4: Forense de sesión, investigación de logs / Session Forensics, Log Investigation
**Explicación:** Análisis de los cuatro artefactos (`webserver.log`, `app.log`, `idp.log`, `browser_dump.txt`). En los logs del servidor web aparece el user-agent `Mozilla/5.0` y los tokens JWT; el IdP que los emite es `auth.catportal.internal` para el usuario `FluffyCat`. En `app.log` se ve un aviso por el cambio de rol disparado al pasar a `admin`. En `browser_dump.txt` (localStorage) está el token malicioso, cuyo header declara `alg: none`: un JWT firmado con "none" requiere que el servidor valide la firma; al no hacerlo, se acepta un token fabricado con rol `admin`. El token legítimo anterior (que otorgaba `role: user`, `exp` coincidente) está en `webserver.log` y está firmado con **HS256**.

```text
webserver.log  -> User-Agent: Mozilla/5.0, peticiones 200 con JWT legítimo
app.log        -> [INFO] Token validated: user=FluffyCat, role=user ; warning: rol->admin
idp.log        -> tokens emitidos solo con role=user (nunca admin por el IdP)
browser_dump.txt -> token malicioso con header {"alg":"none","typ":"JWT"} y payload role=admin
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What user-agent can be seen in the logs? | `Mozilla/5.0` |
| 2 | Based on the logs, what kind of tokens are we dealing with? | `JWT` |
| 3 | What is the IdP server that issued the tokens? | `auth.catportal.internal` |
| 4 | Which user has requested the tokens? | `FluffyCat` |
| 5 | Which role change triggered the warning? | `admin` |
| 6 | What was the malicious token used? | `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6IkZsdWZmeUNhdCIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcyMTQzMTgwMCwiZXhwIjoxNzIxNDM1NDAwfQ` |
| 7 | What algorithm did the malicious token use? | `none` |
| 8 | What was the previous legitimate token? | `***TOKEN-ELIMINADO***` |
| 9 | What algorithm did the legitimate token use? | `HS256` |

### Task 5: Hallazgos, contención y remediación / Investigation Findings, Containment and Remediation
**Explicación:** Se determina que el portal fue accedido mediante un **JWT forgery** (FluffyCat manipuló su token en localStorage, flipó `role: user → admin` y lo re-firmó, o el backend aceptó `alg: none`). Remedios: revocar sesiones y resetear credenciales, auditar tokens, notificar a seguridad, deshabilitar temporalmente los endpoints admin, validar la firma (rechazar `alg: none`), validar el issuer (`auth.catportal.internal`), usar cookies HTTP-only en lugar de localStorage y añadir **verificación de token** / anti-replay en el servidor.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| 1. What can you add to ensure a JWT token is not tampered with? | `token verification` |

### Task 6: Conclusión / Conclusion
**Explicación:** Cierre de la sala. No se requiere respuesta.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| 1. Leer el cierre de la sala | `No answer needed` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What security mechanism do you have to implement when introducing JWT? | `revocation` |
| 2 | What is the attack called when an attacker steals your session ID? | `session hijacking` |
| 3 | Where would you find logs useful for investigating privilege escalation? | `application logs` |
| 4 | Where would you find logs useful for mapping user-agent and IP addresses? | `web server logs` |
| 5 | Which logs would you check if a JWT token has been forged? | `Identity Provider logs` |
| 6 | What user-agent can be seen in the logs? | `Mozilla/5.0` |
| 7 | Based on the logs, what kind of tokens are we dealing with? | `JWT` |
| 8 | What is the IdP server that issued the tokens? | `auth.catportal.internal` |
| 9 | Which user has requested the tokens? | `FluffyCat` |
| 10 | Which role change triggered the warning? | `admin` |
| 11 | What was the malicious token used? | `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6IkZsdWZmeUNhdCIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcyMTQzMTgwMCwiZXhwIjoxNzIxNDM1NDAwfQ` |
| 12 | What algorithm did the malicious token use? | `none` |
| 13 | What was the previous legitimate token? | `***TOKEN-ELIMINADO***` |
| 14 | What algorithm did the legitimate token use? | `HS256` |
| 15 | What can you add to ensure a JWT token is not tampered with? | `token verification` |

---

**Metodología:** Repaso de sesiones/JWT y sus mecanismos defensivos → identificación de las fuentes de logs (app/webserver/IdP) y del dump del navegador → correlación temporal de eventos (token válido → warning de rol → acceso `/admin`) → decode de los JWT (header/payload/firma) y detección de `alg: none` → reconstrucción del ataque de forgery → contención (revocación, reset) y remediación (validación de firma, issuer y almacenamiento seguro).

**Learning chain:** Sesiones y JWT (estructura y almacenamiento) → forense de logs (app, webserver, IdP) → decode de tokens → detección de firma ausente (`alg: none`) → reconstrucción del timeline del ataque (rol user → admin) → recomendaciones de endurecimiento (revocación, verificación, almacenamiento).

**Lección:** *Un JWT almacenado en localStorage y un backend que no valida la firma permiten re-firmar el payload (rol user → admin) sin pasar por el IdP: la correlación de logs de aplicación, servidor e Identity Provider es la clave para detectar y reconstruir el forgery.*

**MITRE ATT&CK:** T1550.001 Use Alternate Authentication Material (Application Access Token) · T1078 Valid Accounts / T1535 Unused/Unsupported Cloud Regions — a nivel de aplicaciones: T1134 Access Token Manipulation · T1071 Application Layer Protocol (token en HTTP) · T1555 Credentials from web browsers (localStorage) · T1070.001 Indicator Removal (si se limpian logs del atacante).

**Fuente:** [TryHackMe - Session Forensics](https://tryhackme.com/room/sessionforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.