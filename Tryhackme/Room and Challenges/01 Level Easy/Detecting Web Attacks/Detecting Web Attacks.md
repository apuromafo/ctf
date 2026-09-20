# Detecting Web Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `detectingwebattacks` | https://tryhackme.com/room/detectingwebattacks | 01 Level Easy | TryHackMe | FFUF v2.1.0 / fuzzing web / XSS / SQLi / logs web / reglas de detección / User-Agent | Detección de ataques web: fuzzing con FFUF, inyección SQL y creación de reglas de detección sobre logs web. |

---

**Contexto:** Sala defensiva de TryHackMe en la que se aprende a detectar ataques contra aplicaciones web. Se clasifican los ataques en client-side (con XSS) y server-side (con SQLi), se practica el descubrimiento de endpoints con el fuzzer FFUF v2.1.0, se explota un panel de login vulnerable a inyección SQL (`%' OR '1'='1`) para acceder a la base de datos y obtener la flag, y se termina escribiendo una regla de detección sobre la fuente de logs "Web Requests" para bloquear peticiones sospechosas.

> **ES:** Sala de detección de ataques web: tipos de ataque (client-side/server-side), fuzzing con FFUF, explotación SQLi y creación de reglas de detección.
> **EN:** Web attack detection room: attack types (client-side/server-side), FFUF fuzzing, SQLi exploitation and detection rule writing.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala de detección de ataques web. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Ataques client-side / Client-Side Attacks

**Explicación:** Se introducen los ataques que apuntan al cliente (al navegador de la víctima). El ejemplo central es XSS (Cross-Site Scripting), que inyecta scripts maliciosos que se ejecutan en el navegador del usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de ataque ataca al cliente? / Which type of attack targets the client? | `Client-Side` |
| 2 | ¿Qué ataque client-side inyecta scripts maliciosos en el navegador de la víctima? / Which client-side attack injects malicious scripts into the victim's browser? | `XSS` |

### Task 3: Ataques server-side / Server-Side Attacks

**Explicación:** Se presentan los ataques que apuntan al servidor. El ejemplo central es SQLi (SQL Injection), que inyecta consultas SQL maliciosas contra la base de datos del servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de ataque ataca al servidor? / Which type of attack targets the server? | `Server-Side` |
| 2 | ¿Qué ataque server-side inyecta consultas SQL maliciosas? / Which server-side attack injects malicious SQL queries? | `SQLi` |

### Task 4: Fuzzing con FFUF / Fuzzing with FFUF

**Explicación:** Se utiliza la herramienta FFUF v2.1.0 para fuzzear la aplicación web y descubrir rutas ocultas. El fuzzing revela la página de login `/login.php` y permite identificar el payload de inyección SQL `%' OR '1'='1` que later se usará para saltarse la autenticación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta y versión se usa para fuzzear la aplicación web? / Which tool and version are used to fuzz the web app? | `FFUF v2.1.0` |
| 2 | ¿Qué archivo de login se descubre mediante el fuzzing? / Which login file is discovered through fuzzing? | `/login.php` |
| 3 | ¿Qué payload de inyección SQL se utiliza para saltarse el login? / Which SQL injection payload is used to bypass the login? | `%' OR '1'='1` |

### Task 5: Explotación de la base de datos / Database Exploitation

**Explicación:** Con el login bypasseado se accede a la base de datos. La contraseña del usuario encontrada en la BD es `astrongpassword123` y, al dumpear la base de datos, se obtiene la flag `THM{dumped_the_db}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña encontrada en la base de datos? / What is the password found in the database? | `astrongpassword123` |
| 2 | ¿Cuál es la flag obtenida al dumpear la base de datos? / What is the flag obtained after dumping the database? | `THM{dumped_the_db}` |

### Task 6: Detección / Writing the Detection

**Explicación:** Se escribe la regla de detección. La fuente de logs utilizada es "Web Requests" y la regla completa bloquea las peticiones cuyo User-Agent contenga "BotTHM": `IF User-Agent CONTAINS "BotTHM" THEN block`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fuente de logs se utiliza para la regla de detección? / Which log source is used for the detection rule? | `Web Requests` |
| 2 | ¿Cuál es la regla de detección completa? / What is the complete detection rule? | `IF User-Agent CONTAINS "BotTHM" THEN block` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala con un repaso de las técnicas de detección aprendidas. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué tipo de ataque ataca al cliente? | `Client-Side` |
| 3 | ¿Qué ataque client-side inyecta scripts maliciosos en el navegador? | `XSS` |
| 4 | ¿Qué tipo de ataque ataca al servidor? | `Server-Side` |
| 5 | ¿Qué ataque server-side inyecta consultas SQL maliciosas? | `SQLi` |
| 6 | ¿Qué herramienta y versión se usa para fuzzear la aplicación web? | `FFUF v2.1.0` |
| 7 | ¿Qué archivo de login se descubre mediante el fuzzing? | `/login.php` |
| 8 | ¿Qué payload de inyección SQL se utiliza para saltarse el login? | `%' OR '1'='1` |
| 9 | ¿Cuál es la contraseña encontrada en la base de datos? | `astrongpassword123` |
| 10 | ¿Cuál es la flag obtenida al dumpear la base de datos? | `THM{dumped_the_db}` |
| 11 | ¿Qué fuente de logs se utiliza para la regla de detección? | `Web Requests` |
| 12 | ¿Cuál es la regla de detección completa? | `IF User-Agent CONTAINS "BotTHM" THEN block` |
| 13 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** El room recorre la clasificación de los ataques web (client-side con XSS frente a server-side con SQLi) y luego un escenario práctico: fuzzing con FFUF v2.1.0 para descubrir `/login.php`, bypass del login con el payload SQLi `%' OR '1'='1`, acceso a la base de datos con la contraseña `astrongpassword123` y extracción de la flag al dumpear la BD. Finaliza con la creación de una regla de detección sobre la fuente de logs "Web Requests" que bloquea las peticiones cuyo User-Agent contenga "BotTHM".

### Cadena de ataque / Attack Chain

```text
FFUF v2.1.0 (fuzzing) -> descubrir /login.php -> payload SQLi (' OR '1'='1) -> bypass del login -> contraseña astrongpassword123 -> dump de la BD -> THM{dumped_the_db} -> regla de detección en Web Requests (IF User-Agent CONTAINS "BotTHM" THEN block)
```

**Learning chain:** Clasificación de ataques web → client-side (XSS) → server-side (SQLi) → fuzzing con FFUF v2.1.0 → /login.php → bypass de login → dump de la BD → regla de detección sobre logs web.

**Lección:** *Entender la diferencia entre ataques client-side y server-side permite escribir reglas de detección precisas sobre los logs web, y el fuzzing con FFUF es la técnica estándar para descubrir endpoints ocultos como /login.php antes de que un atacante los explote.*

**MITRE ATT&CK:** T1059.007 (JavaScript), T1190 (Exploit Public-Facing Application), T1595 (Active Scanning), T1110.001 (Password Guessing)

**Fuente:** [TryHackMe - Detecting Web Attacks](https://tryhackme.com/room/detectingwebattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.