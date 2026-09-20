# OAuth Vulnerabilities

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | oauthvulnerabilities | https://tryhackme.com/room/oauthvulnerabilities | 02 Level Medium | TryHackMe | OAuth 2.0, authorization code grant, implicit grant, CSRF, state parameter, access tokens, django-oauth-toolkit | Comprender y explotar las vulnerabilidades de OAuth 2.0: robo de tokens mediante phishing, CSRF a través de la falta del parámetro state, abuso del flujo implícito y riesgos del cliente de confianza. |

---

**Contexto:** La sala **OAuth Vulnerabilities** explica los fundamentos de **OAuth 2.0** (roles, tokens de acceso, tipos de grant) y cómo los errores de implementación generan vulnerabilidades explotables. Se practica el robo del access token mediante phishing sobre el **authorization code grant**, la **CSRF** en el endpoint de autorización cuando no se usa el parámetro `state`, la manipulación del **implicit grant** (fragmento `#` de la URL) y la revisión de *other* vulnerabilidades.de OAuth 2.1. El laboratorio gira en torno a una web vulnerable implementada con **django-oauth-toolkit** (app Django).

> **ES:** Room de seguridad web que enseña a explotar falencias de OAuth 2.0: phishing de tokens, CSRF sin parámetro state, abuso del flujo implícito y vulnerabilidades adicionales de OAuth 2.1.
> **EN:** A web security room teaching how to exploit OAuth 2.0 flaws: token theft via phishing, CSRF without a state parameter, implicit-flow abuse, and additional OAuth 2.1 issues.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la room: se plantea el objetivo de aprender a explotar vulnerabilidades de OAuth 2.0 y se explica cómo usar la máquina de laboratorio (Django vulnerable con OAuth). No hay pregunta que responder.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Indica que entiendes los objetivos de la sala (sin respuesta requerida). | `No answer needed` |

### Task 2: Conceptos Clave / Key Concepts
**Explicación:** Se revisan las piezas básicas de OAuth: el **authorization server** (AS), los **resource owner**, **client** y **resource server**, y los **tokens de acceso (access tokens)**. El parámetro **state** es una cadena opcional que la aplicación cliente incluye en la petición de autorización para prevenir ataques **CSRF**, y el **access token** es la credencial que el cliente usa para acceder a los recursos protegidos en nombre del resource owner.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which (optional) parameter can be used to prevent CSRF attacks? / ¿Qué parámetro (opcional) se puede usar para prevenir ataques CSRF? | `state` |
| 2 | What credentials can the client use to access protected resources on behalf of the resource owner? / ¿Qué credencial usa el cliente para acceder a recursos protegidos? | `access token` |

### Task 3: Tipos de Grant OAuth / OAuth Grant Types
**Explicación:** Se comparan los distintos grants de OAuth 2.0: **authorization code**, **implicit**, **resource owner password credentials** y **client credentials**. El grant pensado para comunicaciones de servidor a servidor (sin acceso a recursos del usuario, usando solo el client id y el client secret) es el **Client Credentials**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the grant type often used for server-server interaction? / ¿Qué grant se usa a menudo para interacción servidor-servidor? | `Client Credentials` |

### Task 4: Cómo Funciona el Flujo OAuth / How the OAuth Flow Works
**Explicación:** Se practica el flujo de authorization code contra el laboratorio (`http://coffee.thm:8000/`): al iniciar el flujo OAuth 2.0 se captura en el tráfico el valor del `client_id` (`zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt`). El campo del token response que determina la validez temporal del token es `expires_in`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the cliend_id value after initiating the OAuth 2.0 workflow? / ¿Cuál es el valor del client_id tras iniciar el flujo OAuth 2.0? | `zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt` |
| 2 | What parameter name determines the time validity of a token in the token response? / ¿Qué nombre de parámetro determina la validez temporal del token? | `expires_in` |

### Task 5: Identificando Servicios OAuth / Identifying OAuth Services
**Explicación:** Se aprende a reconocer cuándo una aplicación usa OAuth observando el tráfico (parámetros `client_id`, `redirect_uri`, endpoints `/authorize`, `/token`) y las cabeceras/respuestas del servidor. El laboratorio usa el toolkit de OAuth de Django (**django-oauth-toolkit**) en `http://coffee.thm:8000/`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the toolkit used for implementing Oauth in the URL http://coffee.thm:8000/? / ¿Qué toolkit implementa OAuth en esa URL? | `django-oauth-toolkit` |

### Task 6: Explotando OAuth: Robo de Token / Exploiting OAuth: Stealing Token
**Explicación:** Se simula un atacante que envía a la víctima una URL de autorización manipulada con un `redirect_uri` controlado por el atacante. El servidor de autorización entrega el código a la URL del atacante, que lo canjea por un token y accede a los datos de la víctima. Con el token robado se lee el chat de la víctima, cuya primera flag es `THM{GOT_THE_TOKEN007}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after getting the access token? / ¿Cuál es el valor de la flag tras obtener el access token? | `THM{GOT_THE_TOKEN007}` |

### Task 7: CSRF en OAuth / CSRF in OAuth
**Explicación:** Si la petición de autorización no usa el parámetro `state`, un atacante puede engañar a la víctima para que autorice un cliente del atacante vinculando su cuenta (CSRF). Se vincula la cuenta del atacante con la de la víctima (CSRF) y, al sincronizar los contactos, se captura la flag `THM{CONTACTS_SYNCED}`. El parámetro que la aplicación cliente incluye en la petición de autorización para evitar estos ataques CSRF es `state`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after attaching the attacker's account with the victim's account? / ¿Cuál es la flag tras vincular la cuenta del atacante con la víctima? | `THM{CONTACTS_SYNCED}` |
| 2 | What parameter name does the client application include in the authorization request to avoid CSRF attacks? / ¿Qué parámetro incluye el cliente en la petición de autorización para evitar CSRF? | `state` |

### Task 8: Flujo Implícito / Implicit Grant Flow
**Explicación:** El flujo implícito devuelve el access token directamente en el fragmento de la URL, separado por el símbolo `#`. Explotando el flagvalidator en `http://coffee.thm:8080/flagvalidator/` con el access token adquirido se obtiene la flag `THM{TOKEN_HACKED}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What symbol separates the access token from the OAuth 2.0 implicit grant flow URL? / ¿Qué símbolo separa el access token del flujo implícito? | `#` |
| 2 | Visit the URL http://coffee.thm:8080/flagvalidator/ and enter the access token you acquired. What is the flag value? / ¿Cuál es el valor de la flag tras validar el access token? | `THM{TOKEN_HACKED}` |

### Task 9: Otras Vulnerabilidades y OAuth 2.1 / Other Vulnerabilities and OAuth 2.1
**Explicación:** Se repasan vulnerabilidades adicionales y las mejoras que introduce **OAuth 2.1**. La pregunta es de opción múltiple: indicar cuál de las opciones ha sido **omitida** en OAuth 2.1 (respuesta correcta: opción **a**).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which of the following has been omitted from OAuth 2.1? / ¿Cuál de las siguientes opciones se ha omitido en OAuth 2.1? | `a` |

### Task 10: Conclusión / Conclusion
**Explicación:** Cierre de la room: se resumen las prácticas de explotación vistas sobre el authorization code grant y el implicit grant, y las mitigaciones clave (parámetro `state`, PKCE, validación ceñida de `redirect_uri`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa las vulnerabilidades y mitigaciones de OAuth vistas en la sala (sin respuesta requerida). | `No answer needed` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Introducción a la sala OAuth. | `No answer needed` |
| 2 | (Task 2) Which (optional) parameter can be used to prevent CSRF attacks? | `state` |
| 3 | (Task 2) What credentials can the client use to access protected resources on behalf of the resource owner? | `access token` |
| 4 | (Task 3) What is the grant type often used for server-server interaction? | `Client Credentials` |
| 5 | (Task 4) What is the cliend_id value after initiating the OAuth 2.0 workflow? | `zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt` |
| 6 | (Task 4) What parameter name determines the time validity of a token in the token response? | `expires_in` |
| 7 | (Task 5) Name of the toolkit used for implementing Oauth in http://coffee.thm:8000/. | `django-oauth-toolkit` |
| 8 | (Task 6) Flag value after getting the access token. | `THM{GOT_THE_TOKEN007}` |
| 9 | (Task 7) Flag value after attaching the attacker's account with the victim's account. | `THM{CONTACTS_SYNCED}` |
| 10 | (Task 7) Parameter included in the authorization request to avoid CSRF attacks. | `state` |
| 11 | (Task 8) Symbol that separates the access token from the implicit grant flow URL. | `#` |
| 12 | (Task 8) Flag value after entering the acquired access token in /flagvalidator/. | `THM{TOKEN_HACKED}` |
| 13 | (Task 9) Which of the following has been omitted from OAuth 2.1? | `a` |
| 14 | (Task 10) Conclusión de la sala. | `No answer needed` |

---

**Metodología:** Interceptar el tráfico de la aplicación vulnerable con Burp Suite → identificar el flujo OAuth (authorization code / implicit) → manipular `redirect_uri` para robar el code y canjearlo por un token → explotar la falta de `state` para CSRF → leer la API/chat con el token conseguido → revisión de las mejoras de OAuth 2.1.

**Learning chain:** fundamentos de OAuth 2.0 → grants (code, implicit, client credentials) → identificación de implementaciones OAuth → robo de token vía redirect_uri → CSRF / state → abuso del implicit grant → mitigaciones de OAuth 2.1.

**Lección:** *OAuth 2.0 es seguro solo si se implementa con rigor: un redirect_uri mal validado convierte el login de un usuario legítimo en la puerta de entrada del atacante.*

**MITRE ATT&CK:** T1557.002 (Adversary-in-the-Middle: ARP Cache Poisoning) · T1550.001 (Use Alternate Authentication Material: Application Access Token) · T1583.001 (Acquire Infrastructure: Domains) · T1189 (Drive-by Compromise) · T1539 (Steal Web Session Cookie).

**Fuente:** [TryHackMe - OAuth Vulnerabilities](https://tryhackme.com/room/oauthvulnerabilities)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.