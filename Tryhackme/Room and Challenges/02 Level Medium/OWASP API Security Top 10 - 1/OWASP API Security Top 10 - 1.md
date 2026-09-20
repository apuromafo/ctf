# OWASP API Security Top 10 - 1

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Premium) | **Slug** | `owaspapisecuritytop101` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owaspapisecuritytop101) | **Sección** | Web / API | **Fuente** | TryHackMe |
| **Componentes** | API Security, BOLA, Broken User Authentication, Excessive Data Exposure, Rate Limiting, BFLA, Talend API Tester, Laravel | **Impacto** | Exposición de datos confidenciales, toma de cuentas y acceso no autorizado a funciones administrativas por malas prácticas de seguridad en el desarrollo de APIs |

---

**Contexto:** Esta sala es la primera parte del curso OWASP API Security Top 10 de TryHackMe y cubre los primeros cinco principios de la lista de 2019: Broken Object Level Authorisation (BOLA), Broken User Authentication (BUA), Excessive Data Exposure, Lack of Resources & Rate Limiting y Broken Function Level Authorisation (BFLA). Se practica sobre una aplicación Laravel desplegada en una VM Windows usando Talend API Tester, demostrando el impacto real de cada vulnerabilidad y sus mitigaciones.

> **ES:** Aprendizaje de los conceptos básicos para el desarrollo seguro de APIs (Parte 1): autorización a nivel de objeto (BOLA), autenticación de usuario rota (BUA), exposición excesiva de datos, falta de recursos y limitación de tasas, y autorización a nivel de función rota (BFLA), con ejemplos prácticos explotables.
> **EN:** Learning the basic concepts for secure API development (Part 1): Broken Object Level Authorisation (BOLA), Broken User Authentication (BUA), Excessive Data Exposure, Lack of Resources & Rate Limiting, and Broken Function Level Authorisation (BFLA), with practical exploitable examples.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se introduce el curso OWASP API Security Top 10 y se prepara la máquina vulnerable. OWASP es una comunidad global no lucrativa centrada en mejorar la seguridad de las aplicaciones; en 2019 publicó la lista de las diez principales vulnerabilidades de APIs. El participante solo debe conectarse a la máquina (No answer needed).

1. No answer needed

### Task 2: Entendiendo las APIs — Un repaso / Understanding APIs — A Refresher

**Explicación:** Se repasan los conceptos básicos de una API (capa de comunicación entre componentes, peticiones y respuestas estructuradas, documentación como contrato) y se analiza la brecha de LinkedIn de junio de 2021 donde un hacker publicó 1 millón de registros (muestra) en la dark web. La documentación de la API no es trivial ni se deja de usar tras el desarrollo (`nay`).

1. 1. 1
   2. nay
   3. No answer needed

### Task 3: Vulnerabilidad I — Autorización a Nivel de Objeto Rota (BOLA) / Broken Object Level Authorisation (BOLA)

**Explicación:** BOLA ocurre cuando la API usa IDs de objeto para obtener o actualizar datos sin verificar que quien pide esté autorizado; cambiando el ID se accede a información ajena (IDOR). Al incrementar el ID de empleado en `/apirule1/users/{ID}` se descubren 3 empleados en total, la flag asociada al empleado ID 2 es THM{838123} y el username del empleado ID 3 es Bob.

1. 1. 3
   2. THM{838123}
   3. Bob

### Task 4: Vulnerabilidad II — Autenticación de Usuario Rota (BUA) / Broken User Authentication (BUA)

**Explicación:** BUA ocurre cuando la autenticación está mal implementada o se valida de forma incompleta. Usando el endpoint de login vulnerable y el header `Authorization-Token` se obtiene el token de hr@mht.com, se determina que sales@mht.com pertenece al país China y se confirma que no es buena práctica enviar usuario y contraseña en una petición GET (`nay`).

1. 1. cOC%Aonyis%H)mZ&uJkuI?_W#4&m>Y
   2. China
   3. nay

### Task 5: Vulnerabilidad III — Exposición Excesiva de Datos / Excessive Data Exposure

**Explicación:** La API devuelve más información de la necesaria; los desarrolladores exponen todas las propiedades del objeto sin filtrar y dependen del frontend. En las respuestas se revelan campos sensibles: el device ID del post-ID 2 es iOS15.411, el username del post-ID 3 es hacker#!, y se confirma que no se deben usar dispositivos de red en lugar de gestionar la exposición a nivel de API (`nay`).

1. 1. iOS15.411
   2. hacker#!
   3. nay

### Task 6: Vulnerabilidad IV — Falta de Recursos y Limitación de Tasas / Lack of Resources & Rate Limiting

**Explicación:** Sin límites de peticiones ni de tamaño de payload el atacante puede saturar la API causando denegación de servicio. La limitación de tasas sí puede realizarse a nivel de red mediante firewalls (`yea`). Enviando un POST a `/apirule4/sendOTP_s` con el email hr@mht.com se obtiene el código HTTP 200, y usando sale@mht.com el valor de la clave "msg" es Invalid Email.

1. 1. yea
   2. 200
   3. Invalid Email

### Task 7: Vulnerabilidad V — Autorización a Nivel de Función Rota (BFLA) / Broken Function Level Authorisation (BFLA)

**Explicación:** BFLA ocurre cuando las funciones administrativas y las normales no están bien separadas y la validación de roles es débil. El número de móvil del username Alice es +1235322323, no es buena práctica enviar el valor isAdmin a través de campos ocultos en formularios (`nay`) y la address flag del username admin es THM{3432$@#2!}.

1. 1. +1235322323
   2. nay
   3. THM{3432$@#2!}

### Task 8: Conclusión / Conclusion

**Explicación:** Se concluye la primera parte del curso, habiendo estudiado los principios básicos de desarrollo de APIs: autorización y autenticación, y cómo la exposición excesiva de datos puede llevar a la toma completa de cuentas.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | In the LinkedIn breach (Jun 2021), how many million records (sample) were posted by a hacker on the dark web? | `1` |
| 2.2 | Is the API documentation a trivial item and not used after API development (yea/nay)? | `nay` |
| 2.3 | I understand the APIs and am ready to learn OWASP Top 10 Principles. | `No answer needed` |
| 3.1 | Suppose the employee ID is an integer with incrementing value. Can you check through the vulnerable API endpoint the total number of employees in the company? | `3` |
| 3.2 | What is the flag associated with employee ID 2? | `THM{838123}` |
| 3.3 | What is the username of employee ID 3? | `Bob` |
| 4.1 | Can you find the token of hr@mht.com? | `cOC%Aonyis%H)mZ&uJkuI?_W#4&m>Y` |
| 4.2 | To which country does sales@mht.com belong? | `China` |
| 4.3 | Is it a good practice to send a username and password in a GET request (yea/nay)? | `nay` |
| 5.1 | What is the device ID value for post-ID 2? | `iOS15.411` |
| 5.2 | What is the username value for post-ID 3? | `hacker#!` |
| 5.3 | Should we use network-level devices for controlling excessive data exposure instead of managing it through APIs (programmatically) - (yea/nay)? | `nay` |
| 6.1 | Can rate limiting be carried out at the network level through firewall etc. (yea/nay)? | `yea` |
| 6.2 | What is the HTTP response code when you send a POST request to /apirule4/sendOTP_s using the email address hr@mht.com? | `200` |
| 6.3 | What is the "msg key" value after an HTTP POST request to /apirule4/sendOTP_s using the email address sale@mht.com? | `Invalid Email` |
| 7.1 | What is the mobile number for the username Alice? | `+1235322323` |
| 7.2 | Is it a good practice to send isAdmin value through the hidden fields in form requests - yea/nay? | `nay` |
| 7.3 | What is the address flag of username admin? | `THM{3432$@#2!}` |

---

**Metodología:** Análisis de cada vulnerabilidad del OWASP API Security Top 10 (Parte 1) sobre la aplicación Laravel local. Para BOLA se manipularon los IDs de los objetos en `/apirule1`; para BUA se explotó el endpoint de login y el header `Authorization-Token` para obtener tokens y datos de otros usuarios; en Excessive Data Exposure se inspeccionaron las respuestas crudas de la API buscando campos sensibles; en Rate Limiting se interactuó con `/apirule4/sendOTP_s`; y en BFLA se probó el envío de campos ocultos como `isAdmin`.

**Learning chain:** Introducción al OWASP API Top 10 → Conceptos de API → BOLA (IDs incrementales y datos ajenos) → BUA (tokens y cabeceras de autorización) → Excessive Data Exposure (campos sensibles en respuestas) → Rate Limiting (códigos HTTP y mensajes) → BFLA (campos ocultos isAdmin) → Conclusión.

**Lección:** *Las APIs son tan seguras como su peor práctica de implementación: validar autorización por objeto y por función, no exponer credenciales en peticiones, limitar los datos devueltos al mínimo necesario e implementar rate limiting son controles imprescindibles para evitar la fuga de datos y la toma de cuentas.*

**MITRE ATT&CK:** T1082 (System Information Discovery), T1110 (Brute Force), T1213 (Data from Information Repositories), T1222 (File and Directory Permissions Modification)

**Fuente:** [TryHackMe - OWASP API Security Top 10 - 1](https://tryhackme.com/room/owaspapisecuritytop101)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.