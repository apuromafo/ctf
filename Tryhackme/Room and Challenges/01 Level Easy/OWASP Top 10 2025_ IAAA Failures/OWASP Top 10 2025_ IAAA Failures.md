# OWASP Top 10 2025: IAAA Failures

| **Dificultad** | Easy |
| **Tipo** | Laboratorio web (OWASP Top 10 2025) |
| **Slug** | `owasptopten2025one` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owasptopten2025one) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | OWASP Top 10 2025 / IAAA / A01 Broken Access Control / A07 Authentication Failures / A09 Logging & Alerting Failures / IDOR / escalada horizontal / registro de usuarios |
| **Impacto** | Sala de nivel introductorio que enseña el modelo IAAA (Identity, Authentication, Authorisation, Accountability) y tres categorías del OWASP Top 10 2025 ligadas a fallos en su implementación: A01 Broken Access Control (IDOR y escalada horizontal), A07 Authentication Failures (fallos lógicos en el registro/login que permiten suplantar cuentas) y A09 Logging & Alerting Failures (ausencia de registros y alertas que impide investigar ataques de fuerza bruta). |

---

**Contexto:** El módulo desglosa 3 categorías del OWASP Top 10 2025 que se relacionan con fallos en cómo se implementa Identity, Authentication, Authorisation y Accountability (IAAA) en las aplicaciones. En A01 se explota un IDOR manipulando el parámetro `accountID` de la URL para ver la cuenta de otro usuario con más de un millón de dólares (escalada horizontal), obteniendo una nota con la flag. En A07 se registra un usuario con el nombre canónico `ADmiN` (misma identidad que `admin`) para romper la lógica del login y entrar en el dashboard del administrador y robar su flag. En A09 se investiga una aplicación bajo ataque: los logs muestran 7 actividades sospechosas desde la IP `203.0.113.45`, un login exitoso con el usuario `admin` y el acceso al endpoint `/supersecretadminstuff`, evidenciando que sin registros y alertas es imposible entender un ataque. El título del volcado original de la sala describe: "Learn about A01, A07, and A09 in how they related to failures in the applied IAAA model".

## Solucionario

### Task 1: Introducción

**Explicación:** La sala se ha diseñado para principiantes y asume que no hay conocimientos previos de seguridad. Introducción del modelo IAAA y de las tres categorías que se practicarán en los siguientes tasks.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción y empieza el módulo. | `No answer needed` |

### Task 2: What is IAAA?

**Explicación:** IAAA es una forma sencilla de pensar en cómo se verifican los usuarios y sus acciones en las aplicaciones. Cada elemento desempeña un rol crucial y no es posible saltarse un nivel: **Identity** (la cuenta única, ej. user ID/email), **Authentication** (probar esa identidad: passwords, OTP, passkeys), **Authorisation** (lo que esa identidad puede hacer) y **Accountability** (registrar y alertar sobre quién hizo qué, cuándo y desde dónde).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa el acrónimo IAAA? | `Identity, Authentication, Authorisation, Accountability` |

### Task 3: A01: Broken Access Control

**Explicación:** El control de acceso roto ocurre cuando el servidor no aplica correctamente "quién puede acceder a qué" en cada petición. Un caso típico es IDOR (Insecure Direct Object Reference): si cambiar un ID (`?id=7` → `?id=6`) permite ver los datos de otra persona, el control de acceso está roto. En el reto se manipula el parámetro `accountID` en la URL para identificar qué usuario tiene más de un millón de dólares en su cuenta (escalada horizontal: mismo rol, datos de otro usuario) y leer su nota, que contiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Si no obtienes acceso a más roles pero puedes ver los datos de otro usuario, ¿qué tipo de escalada de privilegios es esta? | `horizontal` |
| 2 | ¿Cuál es la nota que encontraste al ver la cuenta del usuario con más de un millón de dólares? | `THM{Found.the.Millionare!}` |

### Task 4: A07: Authentication Failures

**Explicación:** Los fallos de autenticación ocurren cuando la aplicación no puede verificar o vincular de forma fiable la identidad de un usuario: enumeración de usuarios, contraseñas débiles sin bloqueo/rate-limit, fallos lógicos en el flujo de login/registro o manejo inseguro de cookies/sesiones. Sabiendo que el usuario administrador se llama `admin`, se registra un usuario llamado `ADmiN` (misma entidad canónica) y se inicia sesión con `admin` y la contraseña elegida, entrando así en el dashboard del administrador, donde en la "Account Description" se encuentra la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag en el dashboard del usuario admin? | `THM{Account.confusion.FTW!}` |

### Task 5: A09: Logging & Alerting Failures

**Explicación:** Cuando las aplicaciones no registran ni alertan sobre eventos relevantes de seguridad, los defensores no pueden detectar ni investigar ataques. Revisando el sitio estático de la tarea se observan 7 actividades sospechosas, todas desde la misma IP `203.0.113.45`, lo que indica un intento de fuerza bruta. Un POST devolvió status 200 (login exitoso) con el usuario `admin`, y posteriormente se accedió al endpoint `/supersecretadminstuff`. Sin estos registros, sería imposible reconstruir la secuencia del ataque.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Parece que un atacante intentó realizar un ataque de fuerza bruta, ¿cuál es la IP del atacante? | `203.0.113.45` |
| 2 | Parece que consiguieron acceder a una cuenta, ¿cuál es el nombre de usuario de esa cuenta? | `admin` |
| 3 | ¿Qué acción intentó hacer el atacante con la cuenta? Indica el endpoint al que accedió. | `/supersecretadminstuff` |

### Task 6: Conclusión

**Explicación:** Repaso final de los conceptos clave: A01 Broken Access Control exige comprobar en el servidor cada petición; A07 Authentication Failures requiere índices únicos sobre la forma canónica, rate-limit y rotación de sesiones; A09 Logging & Alerting Failures pide registrar todo el ciclo de vida de la autenticación, centralizar logs fuera del host y alertar de anomalías (ráfagas de fuerza bruta, elevación de privilegios).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión y continúa con la siguiente sala del módulo. | `No answer needed` |

---

**Metodología:** Enumeración de aplicaciones web estáticas de cada reto (parámetros de URL, registro de usuarios, logs), manipulación de identificadores para detectar IDOR, explotación de fallos lógicos de autenticación mediante canonicidad del nombre de usuario, y revisión de registros de actividad para reconstruir el ataque (fuerza bruta → acceso → endpoint privilegiado).
**Learning chain:** entender el modelo IAAA → probar control de acceso por objeto (IDOR, escalada horizontal) → explotar fallos lógicos de login/registro (canonicalización de usuarios) → revisar logs y alertas ante un ataque activo → recopilar flags.
**MITRE ATT&CK:** T1530 (Data from Cloud Storage Object), T1078 (Valid Accounts), T1110.001 (Brute Force: Password Guessing), T1087 (Account Discovery), T1021.001 (Remote Services: Remote Desktop Protocol)
**Fuente:** [TryHackMe - OWASP Top 10 2025: IAAA Failures](https://tryhackme.com/room/owasptopten2025one)