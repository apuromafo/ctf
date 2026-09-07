# SQL Injection Introduction [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `sqlinjectionintroduction`
* **Link:** https://tryhackme.com/room/sqlinjectionintroduction
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + máquina con laboratorio por niveles de SQLi
* **Componentes:** SQL esencial (UNION, information_schema) · inyecciones In-Band (UNION/error-based) · Blind (auth bypass, boolean, time-based) · Out-of-Band (DNS, xp_dirtree) · remediación (prepared statements) · lab: niveles 1–4
* **Impacto rol:** El SQLi sigue siendo rey de los bugs web; este room te da cimientos completos (In-band, Blind y OOB) y termina con práctica por niveles con flags.

## Solucionario de Tareas / Task Solutions

> **ES:** SQL Injection consiste en romper/alterar una consulta para cambiarle la lógica. Fundamentos: **UNION** combina dos SELECT; **information_schema** es la BD de metadatos de MySQL. Detección: la primera prueba es un carácter de **comilla simple (`'`)**. Modalidades: **In-Band** (el resultado vuelve a la página; el subtipo **error-based** extrae por los mensajes de error; la función **`database()`** devuelve el nombre de la BD actual), **Blind** (no hay respuestas visibles: auth-bypass con **`1=1`**, boolean-based, time-based con **`SLEEP()`**) y **Out-of-Band** (**DNS** para exfiltrar, con el stored procedure de MSSQL **`xp_dirtree`** que provoca nombres de archivo/DNS). La defensa primaria: **prepared statements** (parámetros). El lab práctico tiene 4 niveles con flags.
> **EN:** SQL Injection breaks/alters a query to change its logic. Fundamentals: **UNION** combines two SELECTs; **information_schema** is MySQL's metadata DB. Detection: the first probe is a **single quote (`'`)**. Modes: **In-Band** (results come back in the page; the **error-based** subtype extracts via error messages; `database()` returns the current DB name), **Blind** (no visible output: auth-bypass with **`1=1`**, boolean-based, time-based with **`SLEEP()`**) and **Out-of-Band** (**DNS** exfil, using MSSQL's **`xp_dirtree`** stored procedure to force DNS lookups). Primary defence: **prepared statements**. The practical lab has 4 flag levels.

### Task 1 — Introducción / Introduction

* **Check:** `I am ready to learn about SQL Injection!`
* **ES:** Fundamentos de SQLi con práctica guiada.
* **EN:** SQLi fundamentals with guided practice.

### Task 2 — SQL Esencial para Inyección / SQL Essentials for Injection

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What SQL statement combines results from two SELECT queries into one result set? | `UNION` |
| What built-in database contains metadata about all other databases, tables, and columns in MySQL? | `information_schema` |

* **UNION:** concatena filas de dos SELECT (mismo nº de columnas).
* **information_schema:** BD virtual de MySQL con SCHEMATA/TABLES/COLUMNS → piedra angular del reconocimiento post-inyección.

### Task 3 — Qué es SQLi / What is SQL Injection?

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What character is commonly used as a first test when probing for SQL Injection? | `'` |
| What type of SQL Injection returns results directly in the web page? | `In-Band` |

* **Comilla / Quote `'`:** si rompe la consulta (error 500/comportamiento anómalo) hay entrada SQL dinámica.
* **In-Band:** los resultados se ven en la propia respuesta HTTP.

### Task 4 — SQLi In-Band

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What subtype of In-Band SQLi relies on database **error messages** to extract information? | `Error-based` |
| What SQL function returns the **name of the current database** in MySQL? | `database()` |

* **Error-based:** fuerza errores descriptivos (con `extractvalue`/`updatexml` se exfiltrata) que incluyen datos.
* **`database()`:** `SELECT database();` → nombre de la BD actual.

### Task 5 — SQLi Blind: Auth Bypass / Blind SQL Injection: Authentication Bypass

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What boolean condition is commonly injected to make a WHERE clause **always evaluate to true**? | `1=1` |

* **Ejemplo / Example:** `SELECT * FROM users WHERE user='x' AND pass='x' OR 1=1--` → la condición `OR 1=1` la vuelve siempre verdadera (login sin credenciales).

### Task 6 — SQLi Blind: Boolean y Time-Based

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What MySQL function causes a **deliberate time delay** in a query's response? | `SLEEP()` |

* **Time-based:** `AND SLEEP(5)--` → si la respuesta tarda 5 s, la condición evaluó a verdadero (canal lateral de 1 bit por petición).

### Task 7 — SQLi Out-of-Band

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What protocol beginning with **D** is commonly used to exfiltrate data in Out-of-Band SQLi? | `DNS` |
| What MSSQL stored procedure can be used to trigger **DNS lookups** for data exfiltration? | `xp_dirtree` |

* **DNS:** las consultas de nombre de dominio salen del entorno y dejan rastro en tu servidor DNS autoritativo.
* **`xp_dirtree`:** el stored proc de MSSQL que lista directorios con rutas UNC → provoca resoluciones DNS que puedes usar como canal de exfiltración (combinado con `xp_fileexist` o variantes).

### Task 8 — Remediación y Prevención / Remediation and Prevention

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the primary and most effective defence against SQL Injection? | `Prepared statements` |

* **Prepared statements** (también llamadas *parameterized queries*): separan SQL de datos; la entrada nunca se interpreta como código. Complementos: allowlist de input/WAF, mínimo privilegio en la cuenta de BD.

### Task 9 — Práctica: SQL Injection / Practical: SQL Injection *(vm)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag after completing **Level 1**? | `THM{SQL_INJECTION_3840}` |
| What is the flag after completing **Level 2**? | `THM{SQL_INJECTION_9581}` |
| What is the flag after completing **Level 3**? | `THM{SQL_INJECTION_1093}` |
| What is the flag after completing **Level 4**? | `THM{SQL_INJECTION_MASTER}` |

* **Nivel 1:** bypass de login básico (`' OR 1=1--` o equivalente).
* **Nivel 2:** inyección con UNION para extraer datos de otra columna/tabla.
* **Nivel 3:** bypass tipo boolean / tag de comentario distinto (bloqueo de espacios o de `#`).
* **Nivel 4:** final "master": combinar técnicas (más niveles de filtrado). Flags: `THM{SQL_INJECTION_3840}`, `THM{SQL_INJECTION_9581}`, `THM{SQL_INJECTION_1093}`, `THM{SQL_INJECTION_MASTER}`.

### Task 10 — Conclusión / Conclusion

* **Check:** `I have completed the SQL Injection room!`
* **ES:** Cierra con la lección: input validation + prepared statements vs. el "reino de las comillas".
* **EN:** Closes with the lesson: input validation + prepared statements vs. the "realm of quotes".

## Metodología / Methodology

1. **Paso / Step:** Probar la comilla `'` como test inicial en cada campo.
2. **Paso / Step:** Determinar nº de columnas (`ORDER BY n` / `UNION SELECT 1,2,3...`) y usar `database()` + `information_schema` para mapear BD/tablas/columnas.
3. **Paso / Step:** Elegir modalidad según el canal: **In-Band** (UNION/error), **Blind** (boolean/time con `SLEEP()`), **OOB** (DNS con `xp_dirtree`).
4. **Paso / Step:** Resolver los 4 niveles del lab en orden de complejidad.

### Cadena de ataque / Attack Chain

```
' (test) -> 500/anómalo (SQL dinámico)
  -> UNION SELECT n ... (nº de columnas)
  -> information_schema + database() (recon)
  -> canal de salida: In-Band / Blind / OOB
  -> exfiltración de datos o bypass de auth
  -> flags: THM{SQL_INJECTION_3840} ... THM{SQL_INJECTION_MASTER}
```

**Mapeo MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1505.003/T1213 (Data from Information Repositories/DB) para la exfiltración · CWE-89 (SQL Injection) = OWASP Top 10 A03.

**Lección:** *Toda entrada que toque una query es una puerta.* Si la defensa es concatenar strings en SQL, la comilla siempre gana; los prepared statements convierten los datos en datos.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.