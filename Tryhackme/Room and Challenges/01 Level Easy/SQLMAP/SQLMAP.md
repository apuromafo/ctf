# SQLMAP

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `sqlmap` | [TryHackMe](https://tryhackme.com/room/sqlmap) | 01 Level Easy | TryHackMe | SQLMap, SQL Injection, MySQL, Database Dumping | Technical — Automating SQL injection with SQLMap |

---

**Contexto:** Este room enseña el uso de SQLMap para automatizar la detección y explotación de vulnerabilidades de inyección SQL. Se Cubren los parámetros de línea de comandos más importantes y su aplicación en la enumeración y extracción de bases de datos MySQL.

## Solucionario

### Task 1: SQLMap Introduction

**Explicación:** Se Introduce la herramienta SQLMap y su propósito sin requerir una respuesta específica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the introduction | `No answer needed` |

### Task 2: SQLMap Parameters

**Explicación:** Se Identifican los parámetros de línea de comandos de SQLMap y su funcionalidad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Parameter to specify the target URL | `-u` |
| 2 | Parameter to send POST data | `--data` |
| 3 | Parameter to specify the injectable parameter | `-p username` |
| 4 | Parameter to show extended help | `-hh` |
| 5 | Parameter to retrieve all data | `-a` |
| 6 | Parameter to select a database | `-D` |
| 7 | Parameter to list tables | `--tables` |
| 8 | Parameter to list columns | `--columns` |
| 9 | Parameter to dump all records | `--dump-all` |
| 10 | Parameter to open an interactive SQL shell | `--sql-shell` |
| 11 | Parameter to specify the DBMS | `--dbms=mysql` |

### Task 3: Database Exploitation

**Explicación:** Se Aplica SQLMap para enumerar la base de datos objetivo y extraer credenciales de forma automatizada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the database? | `blood` |
| 2 | What is the username found? | `root` |
| 3 | What is the flag? | `thm{sqlm@p_is_L0ve}` |

---

**Metodología:** Se Utiliza SQLMap para automatizar la detección y explotación de inyecciones SQL, desde la selección del parámetro inyectable hasta el volcado completo de la base de datos MySQL.

### Cadena de ataque / Attack Chain

**Learning chain:** SQLMap Basics → Parameter Enumeration → Database Discovery → Table Dumping → Credential Extraction

**Lección:** *SQLMap automatiza de manera eficiente el proceso de detección y explotación de inyección SQL, permitiendo enumerar bases de datos y extraer credenciales con unos pocos comandos bien parametrizados.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1083 — File and Directory Discovery

**Fuente:** [TryHackMe - SQLMAP](https://tryhackme.com/room/sqlmap)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.