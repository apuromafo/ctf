# SQL Injection Introduction

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `sqlinjectionintroduction` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sqlinjectionintroduction) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + máquina con laboratorio por niveles de SQLi |
| **Componentes** | SQL esencial (UNION, information_schema) / In-Band (UNION, error-based) / Blind (auth bypass, boolean, time-based) / Out-of-Band (DNS, xp_dirtree) / prepared statements / lab niveles 1–4 |
| **Impacto** | Cimientos completos de SQLi (In-band, Blind y OOB), detección, exfiltración y remediación, con práctica por niveles y flags |

---

**Contexto:** SQL Injection consiste en romper/alterar una consulta para cambiarle la lógica. Fundamentos: **UNION** combina dos SELECT; **information_schema** es la BD de metadatos de MySQL. Detección: la primera prueba es un carácter de **comilla simple (`'`)**. Modalidades: **In-Band** (el resultado vuelve a la página; el subtipo **error-based** extrae por los mensajes de error; la función **`database()`** devuelve el nombre de la BD actual), **Blind** (no hay respuestas visibles: auth-bypass con **`1=1`**, boolean-based, time-based con **`SLEEP()`**) y **Out-of-Band** (**DNS** para exfiltrar, con el stored procedure de MSSQL **`xp_dirtree`** que provoca nombres de archivo/DNS). La defensa primaria: **prepared statements** (parámetros). El lab práctico tiene 4 niveles con flags.

## Solucionario

### Task 1: Introducción / Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to learn about SQL Injection! | `No answer needed` |

**Explicación:** Introducción al room. Los fundamentos clave: **UNION** combina dos SELECT; **information_schema** es la BD de metadatos de MySQL.

### Task 2: SQL Esencial para Inyección / SQL Essentials for Injection

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What SQL statement combines results from two SELECT queries into one result set? | `UNION` |
| 2 | What built-in database contains metadata about all other databases, tables, and columns in MySQL? | `information_schema` |

**Explicación:** La sentencia **UNION** concatena filas de dos SELECT (requiere el mismo número de columnas) → es la base de la exfiltración con UNION-based SQLi. **information_schema** es la base de datos virtual de MySQL que contiene las bases SCHEMATA/TABLES/COLUMNS, piedra angular del reconocimiento post-inyección.

### Task 3: Qué es SQLi / What is SQL Injection?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What character is commonly used as a first test when probing for SQL Injection? | `'` |
| 2 | What type of SQL Injection returns results directly in the web page? | `In-Band` |

**Explicación:** La **comilla simple (`'`)** es la primera prueba: si rompe la consulta (error 500/comportamiento anómalo) hay entrada SQL dinámica. La modalidad que devuelve resultados directamente en la propia respuesta HTTP es **In-Band**.

### Task 4: SQLi In-Band

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What subtype of In-Band SQLi relies on database **error messages** to extract information? | `Error-based` |
| 2 | What SQL function returns the **name of the current database** in MySQL? | `database()` |

**Explicación:** El subtipo **Error-based** fuerza errores descriptivos (p. ej. con `extractvalue`/`updatexml`) que incluyen los datos buscados → se exfiltra a través de los mensajes de error. `SELECT database();` devuelve el nombre de la BD actual, esencial para orientar el mapeo.

### Task 5: SQLi Blind: Auth Bypass / Blind SQL Injection: Authentication Bypass

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What boolean condition is commonly injected to make a WHERE clause **always evaluate to true**? | `1=1` |

**Explicación:** Inyectar la condición booleana **`1=1`** hace que la WHERE siempre evalúe a verdadero. Ejemplo: `SELECT * FROM users WHERE user='x' AND pass='x' OR 1=1--` → el login se bypasea sin credenciales.

### Task 6: SQLi Blind: Boolean y Time-Based

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What MySQL function causes a **deliberate time delay** in a query's response? | `SLEEP()` |

**Explicación:** **SLEEP()** provoca un retardo deliberado. En time-based blind SQLi se inyecta `AND SLEEP(5)--`: si la respuesta tarda 5 s, la condición evaluó a verdadero → canal lateral de 1 bit por petición.

### Task 7: SQLi Out-of-Band

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What protocol beginning with **D** is commonly used to exfiltrate data in Out-of-Band SQLi? | `DNS` |
| 2 | What MSSQL stored procedure can be used to trigger **DNS lookups** for data exfiltration? | `xp_dirtree` |

**Explicación:** **DNS** exfiltra porque las consultas de nombre de dominio salen del entorno y dejan rastro en tu servidor DNS autoritativo. **`xp_dirtree`** es el stored procedure de MSSQL que lista directorios con rutas UNC → provoca resoluciones DNS usables como canal de exfiltración (combinado con `xp_fileexist` o variantes).

### Task 8: Remediación y Prevención / Remediation and Prevention

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the primary and most effective defence against SQL Injection? | `Prepared statements` |

**Explicación:** **Prepared statements** (también llamadas *parameterized queries*) separan el SQL de los datos: la entrada nunca se interpreta como código. Complementos: allowlist de input/WAF y mínimo privilegio en la cuenta de BD.

### Task 9: Práctica: SQL Injection / Practical: SQL Injection *(vm)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag after completing **Level 1**? | `THM{SQL_INJECTION_3840}` |
| 2 | What is the flag after completing **Level 2**? | `THM{SQL_INJECTION_9581}` |
| 3 | What is the flag after completing **Level 3**? | `THM{SQL_INJECTION_1093}` |
| 4 | What is the flag after completing **Level 4**? | `THM{SQL_INJECTION_MASTER}` |

**Explicación:** Lab de 4 niveles: Nivel 1 — bypass de login básico (`' OR 1=1--` o equivalente) → `THM{SQL_INJECTION_3840}`; Nivel 2 — inyección con UNION para extraer datos de otra columna/tabla → `THM{SQL_INJECTION_9581}`; Nivel 3 — bypass tipo boolean/tag de comentario distinto (bloqueo de espacios o de `#`) → `THM{SQL_INJECTION_1093}`; Nivel 4 — final "master": combinar técnicas (más niveles de filtrado) → `THM{SQL_INJECTION_MASTER}`.

### Task 10: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have completed the SQL Injection room! | `No answer needed` |

**Explicación:** Cierre del room; proceso completo: probar la comilla `'` → determinar nº de columnas (`ORDER BY n` / `UNION SELECT 1,2,3...`) → usar `database()` + `information_schema` para mapear BD/tablas/columnas → elegir modalidad según el canal (In-Band/Blind/OOB) → exfiltrar datos o bypassear auth.

---

**Metodología:**
1. **SQL esencial:** **UNION** concatena filas de dos SELECT (mismo nº de columnas); **information_schema** es la BD virtual de MySQL con SCHEMATA/TABLES/COLUMNS, piedra angular del reconocimiento post-inyección.
2. **Detección:** probar la **comilla `'`** en cada campo: si rompe la consulta (error 500/comportamiento anómalo) hay entrada SQL dinámica. La modalidad que devuelve resultados en la propia respuesta HTTP es **In-Band**.
3. **In-Band:** **Error-based** fuerza errores descriptivos (con `extractvalue`/`updatexml` se exfiltra) que incluyen datos; `SELECT database();` devuelve el nombre de la BD actual.
4. **Blind:** auth-bypass inyectando la condición booleana **`1=1`** (ejemplo: `SELECT * FROM users WHERE user='x' AND pass='x' OR 1=1--` → login sin credenciales); time-based con `AND SLEEP(5)--`: si la respuesta tarda 5 s, la condición evaluó a verdadero (canal lateral de 1 bit por petición).
5. **Out-of-Band:** **DNS** exfiltra porque las consultas de nombre de dominio salen del entorno y dejan rastro en tu servidor DNS autoritativo; **`xp_dirtree`** es el stored proc de MSSQL que lista directorios con rutas UNC → provoca resoluciones DNS usables como canal de exfiltración (combinado con `xp_fileexist` o variantes).
6. **Remediación:** **Prepared statements** (también llamadas *parameterized queries*) separan SQL de datos; la entrada nunca se interpreta como código. Complementos: allowlist de input/WAF, mínimo privilegio en la cuenta de BD.
7. **Lab práctico (4 niveles):** Nivel 1 bypass de login básico (`' OR 1=1--` o equivalente) → `THM{SQL_INJECTION_3840}`; Nivel 2 inyección con UNION para extraer datos de otra columna/tabla → `THM{SQL_INJECTION_9581}`; Nivel 3 bypass tipo boolean/tag de comentario distinto (bloqueo de espacios o de `#`) → `THM{SQL_INJECTION_1093}`; Nivel 4 final "master": combinar técnicas (más niveles de filtrado) → `THM{SQL_INJECTION_MASTER}`.
8. **Proceso completo:** probar la comilla `'` → determinar nº de columnas (`ORDER BY n` / `UNION SELECT 1,2,3...`) → usar `database()` + `information_schema` para mapear BD/tablas/columnas → elegir modalidad según el canal (In-Band/Blind/OOB) → exfiltrar datos o bypassear auth.

**Learning chain:** `'` (test) → 500/anómalo (SQL dinámico) → UNION SELECT n ... (nº de columnas) → information_schema + database() (recon) → canal de salida: In-Band / Blind / OOB → exfiltración de datos o bypass de auth → flags: THM{SQL_INJECTION_3840} ... THM{SQL_INJECTION_MASTER}

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 (Server Software Component: Web Shell), T1213 (Data from Information Repositories), CWE-89 (SQL Injection)

**Fuente:** [TryHackMe - SQL Injection Introduction](https://tryhackme.com/room/sqlinjectionintroduction)