# SQL Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `sqlfundamentals` | [TryHackMe](https://tryhackme.com/room/sqlfundamentals) | 01 Level Easy | TryHackMe | SQL, Databases, DBMS, HID Attacks | Technical — SQL and database fundamentals |

---

**Contexto:** Este room introduce los fundamentos de SQL y bases de datos, incluyendo los diferentes tipos de bases de datos, los conceptos de clave primaria y clave foránea, y luego transita hacia dispositivos de ataque de hardware como Wi-Fi Pineapple, USB Rubber Ducky y Bash Bunny.

## Solucionario

### Task 1: Database Fundamentals

**Explicación:** Se Introducen los conceptos de bases de datos sin requerir una respuesta específica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the overview | `No answer needed` |

### Task 2: Database Concepts

**Explicación:** Se Identifican los conceptos fundamentales de bases de datos: tipos de bases de datos, estructura de filas y los tipos de claves.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of database stores data in a non-relational format? | `Non-relational database` |
| 2 | What type of database uses tables and relationships? | `relational database` |
| 3 | What is a single record in a table called? | `row` |
| 4 | What key references another table? | `foreign key` |
| 5 | What key uniquely identifies a record? | `primary key` |

### Task 3: DBMS and SQL

**Explicación:** Se Identifican los sistemas de gestión de bases de datos y el lenguaje de consulta SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What system manages databases? | `DBMS` |
| 2 | What language is used to query databases? | `SQL` |

### Task 4: SQL Syntax

**Explicación:** Se Resuelven los ejercicios de sintaxis SQL identificando las flags correspondientes a cada consulta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for the first query? | `THM{575a947132312f97b30ee5aeebba629b723d30f9}` |
| 2 | What is the flag for the second query? | `THM{692aa7eaec2a2a827f4d1a8bed1f90e5e49d2410}` |

### Task 5: Hardware Attacks

**Explicación:** Se Introducen los dispositivos de ataque de hardware, como el Wi-Fi Pineapple y los ataques USB.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What wireless attack device is used for rogue access points? | `Wi-Fi Pineapple` |
| 2 | What type of attacks are delivered via USB? | `USB attacks` |

### Task 6: USB Attacks Overview

**Explicación:** Se Analiza el número de dispositivos de ataque USB y los ejemplos más comunes como el Bash Bunny y el Wi-Fi Pineapple.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many USB attack devices are there? | `6` |
| 2 | What device is known for fast keystroke injection? | `Bash Bunny` |
| 3 | What wireless device can be used in combination? | `Wi-Fi Pineapple` |

### Task 7: Advanced Devices

**Explicación:** Se Analizan dispositivos avanzados de ataque, incluyendo el Flipper Zero, la clonación de RFID y el Lan Turtle.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What multi-tool device can interact with RFID? | `Flipper Zero` |
| 2 | What technique is used to duplicate RFID cards? | `RFID cloning` |
| 3 | What device is used for covert network access? | `Lan Turtle` |

### Task 8: Keystroke Injection

**Explicación:** Se Analiza el dispositivo de inyección de teclas más popular, sus especificaciones de velocidad y sus alternativas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the most popular keystroke injection device? | `USB Rubber Ducky` |
| 2 | What is the keystroke injection rate? | `1444` |
| 3 | What devices are alternatives to the Rubber Ducky? | `Flipper Zero & iCopy-XS` |

### Task 9: Practical Exercise

**Explicación:** Se Aplica los conocimientos de SQL y dispositivos de ataque en un ejercicio práctico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the practical exercise | `No answer needed` |

---

**Metodología:** Se Estudian los fundamentos de SQL y bases de datos, desde los tipos de bases de datos y claves hasta el lenguaje SQL, complementado con el análisis de dispositivos de ataque de hardware.

### Cadena de ataque / Attack Chain

**Learning chain:** Database Fundamentals → SQL Syntax → Primary/Foreign Keys → HID Attacks → Hardware Exploitation

**Lección:** *Comprender los fundamentos de SQL y bases de datos es esencial para el pentesting web, y conocer los dispositivos de ataque de hardware amplía el arsenal para escenarios de acceso físico y ofensiva.*

**MITRE ATT&CK:** T1110 — Brute Force; T1204 — User Execution

**Fuente:** [TryHackMe - SQL Fundamentals](https://tryhackme.com/room/sqlfundamentals)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.