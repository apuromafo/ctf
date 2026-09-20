# SQL Injection
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `sqlinjection` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sqlinjection) |
| **Sección** | Web Application Security / SQL Injection |
| **Fuente** | TryHackMe |
| **Componentes** | SQL, MySQL, DBMS, in-band SQLi, error-based, blind SQLi, out-of-band (DNS), Prepared Statements |
| **Impacto** | Introducción completa a la inyección SQL: fundamentos de SQL/DBMS, tipos de inyección (in-band, blind, out-of-band) y sus mitigaciones, con retos prácticos para obtener flags. |
---
**Contexto:** Esta room introduce la inyección SQL desde sus fundamentos. Primero repasa qué es SQL, los DBMS y las sentencias básicas (`SELECT`, `UNION`, `INSERT`), para después explicar cómo un atacante rompe la consulta original mediante el terminador `;` y técnicas de inyección. Se cubren los tres tipos principales: **in-band** (UNION/error-based), **blind** (boolean/time-based) y **out-of-band** (exfiltración vía DNS), terminando con las contramedidas basadas en **Prepared Statements**.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de la sala y de los objetivos de aprendizaje sobre inyección SQL. Se introduce el significado de SQL: **Structured Query Language**, el lenguaje estándar para consultar y manipular bases de datos relacionales.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What does SQL stand for? | `Structured Query Language` |
### Task 2: SQL Basics / Fundamentos de SQL
**Explicación:** Conceptos básicos de bases de datos relacionales: el **DBMS** (Database Management System) es el software que gestiona la base de datos, y la **table** es la estructura que almacena filas y columnas con los datos.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the software that manages a database called? | `DBMS` |
| 2. Where are the records stored within a database? | `table` |
### Task 3: SQL Statements / Sentencias SQL
**Explicación:** Sentencias SQL fundamentales: **SELECT** recupera datos de una o varias tablas, **UNION** combina los resultados de dos consultas, e **INSERT** añade nuevas filas a una tabla.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Which statement is used to retrieve data? | `SELECT` |
| 2. Which statement combines the results of two queries? | `UNION` |
| 3. Which statement adds new records to a table? | `INSERT` |
### Task 4: SQL Injection / Inyección SQL
**Explicación:** El terminador de sentencia `;` permite al atacante finalizar la consulta original y concatenar una nueva, base de la inyección SQL. En este task se introduce el concepto y el carácter clave que rompe la query.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What character is used to terminate a SQL statement? | `;` |
### Task 5: In-Band SQL Injection / Inyección in-band
**Explicación:** En la inyección **in-band** el atacante obtiene los resultados en la misma respuesta de la aplicación (por ejemplo mediante `UNION SELECT`). Se explota para obtener la flag del reto.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the flag from the in-band SQL injection challenge? | `THM{SQL_INJECTION_3840}` |
### Task 6: Error-Based SQL Injection / Inyección error-based
**Explicación:** En la inyección **error-based** se fuerza a la base de datos a devolver información sensible a través de mensajes de error (nombres de columnas, versión, etc.). Se obtiene la flag correspondiente.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the flag from the error-based SQL injection challenge? | `THM{SQL_INJECTION_9581}` |
### Task 7: Blind SQL Injection / Inyección ciega
**Explicación:** En la **blind SQLi** la aplicación no devuelve los datos ni errores, por lo que se infiere la información mediante preguntas booleanas o retardos temporales (`time-based`). Se obtiene la flag.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the flag from the blind SQL injection challenge? | `THM{SQL_INJECTION_1093}` |
### Task 8: Out-of-Band SQL Injection / Inyección out-of-band
**Explicación:** En la inyección **out-of-band** la exfiltración se realiza por un canal distinto de la respuesta HTTP, normalmente mediante consultas DNS encadenadas. Se completa el reto de inyección avanzado y se obtiene la flag maestra.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the flag from the advanced SQL injection challenge? | `THM{SQL_INJECTION_MASTER}` |
### Task 9: Out-of-Band Exfiltration / Exfiltración out-of-band
**Explicación:** El canal out-of-band más común es **DNS**: la base de datos vulnerable resuelve un nombre de dominio controlado por el atacante, transportando los datos exfiltrados en la propia consulta DNS.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Which protocol is commonly used for out-of-band exfiltration? | `DNS` |
### Task 10: Mitigation / Mitigación
**Explicación:** La defensa principal contra la inyección SQL son las **Prepared Statements** (consultas parametrizadas), que separan el código SQL de los datos de entrada, además de validación de entrada y mínimo privilegio en la base de datos.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the recommended defense against SQL injection? | `Prepared Statements` |
---
**Metodología:** Entender SQL/DBMS → identificar el punto de inyección → clasificar la técnica (in-band, error-based, blind, out-of-band) → construir el payload adecuado (`UNION`, errores, booleanos, DNS) → extraer datos → aplicar la mitigación (Prepared Statements).
### Cadena de ataque / Attack Chain
```
Entrada controlada por el usuario -> concatenación insegura en la query SQL -> terminación con ; -> inyección (UNION/error/blind/OOB) -> exfiltración de datos
```
**Learning chain:** fundamentos SQL → punto de inyección → tipos de SQLi → exfiltración → mitigación.
**Lección:** *Nunca confíes en la entrada del usuario: separar datos de código con consultas parametrizadas elimina la inyección SQL de raíz; el resto de técnicas defensivas son complementarias.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell), T1041 (Exfiltration Over C2 Channel).
**Fuente:** [TryHackMe - SQL Injection](https://tryhackme.com/room/sqlinjection)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
