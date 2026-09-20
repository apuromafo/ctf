# SQLMap_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `sqlmapthebasics` | [TryHackMe](https://tryhackme.com/room/sqlmapthebasics) | 01 Level Easy | TryHackMe | SQLMap, SQL Injection, Boolean-based, Database Enumeration | Technical — Automating SQL injection with SQLMap |

---

**Contexto:** Este room introduce los fundamentos de SQLMap para automatizar la detección y explotación de inyecciones SQL. Se Cubre la detección de inyecciones boolean-based, la enumeración de bases de datos y la extracción de tablas y credenciales.

## Solucionario

### Task 1: Injection Detection

**Explicación:** Se Identifica una vulnerabilidad de inyección SQL y el tipo de inyección utilizado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of injection was detected? | `sql` |
| 2 | What boolean condition was used to confirm the injection? | `or` |
| 3 | Was the injection confirmed? | `YEA` |

### Task 2: Database Enumeration

**Explicación:** Se Enumera la base de datos objetivo y se identifica el comando utilizado para volcar las tablas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What parameter lists all databases? | `--dbs` |
| 2 | What command is used to enumerate tables in the members database? | `sqlmap -u http://sqlmaptesting.thm/search/cat=1 -D members --tables` |

### Task 3: Table Extraction

**Explicación:** Se Extrae la información de la tabla objetivo, incluyendo el usuario y la contraseña encontrados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many tables were found? | `6` |
| 2 | What is the username found? | `user` |
| 3 | What is the password found? | `12345678` |

---

**Metodología:** Se Utiliza SQLMap para automatizar la detección de inyecciones SQL, enumerar bases de datos con `--dbs` y volcar tablas completas para extraer credenciales.

### Cadena de ataque / Attack Chain

**Learning chain:** SQLi Detection → Boolean-Based Confirmation → Database Enumeration → Table Dumping → Credential Extraction

**Lección:** *SQLMap simplifica el proceso de explotación de inyecciones SQL, pero es esencial comprender los conceptos subyacentes de la inyección para interpretar correctamente los resultados y alcanzar los objetivos de extracción.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1048 — Exfiltration Over Alternative Protocol

**Fuente:** [TryHackMe - SQLMap_ The Basics](https://tryhackme.com/room/sqlmapthebasics)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.