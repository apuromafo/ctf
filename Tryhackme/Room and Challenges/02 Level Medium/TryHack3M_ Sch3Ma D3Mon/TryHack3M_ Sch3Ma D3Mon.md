# TryHack3M: Sch3Ma D3Mon

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `sch3mad3mon` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sch3mad3mon) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | SQL injection / os-shell / malware analysis / ransomware / nim / defang |
| **Impacto** | Explotar una SQLi para obtener shell OS y analizar/modificar un malware de venta para "defangearlo" |

---

**Contexto:** Sala CTF (TryHack3M) que parte de una SQL injection (`os_sqli.php`) para conseguir una shell en el sistema y llegar hasta una tienda de malware, donde se localiza el malware más vendido y se modifica ("defangea") para evitar su efecto dañino, obteniendo la flag tras recompilar.

## Solucionario

### Task 1: A Public Computer with a VPN

**Explicación:**

Se obtienen las credenciales del sospechoso: el usuario es `lannister` y la contraseña es `hrpTfL42wMv3`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the suspect's username? | `lannister` |
| 2 | What is the suspect's password? | `hrpTfL42wMv3` |

### Task 2: Connected Tables

**Explicación:**

Conceptos de bases de datos relacionales: **RDBMS** = `relational database management system`; **CRUD** = `create read update delete`; **SQL** = `Structured Query Language`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does RDBMS stand for? | `relational database management system` |
| 2 | What does CRUD stand for? | `create read update delete` |
| 3 | What does SQL stand for? | `Structured Query Language` |

### Task 3: Unlisted

**Explicación:**

La ruta oculta es `os_sqli.php` (endpoint vulnerable a inyección SQL).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the hidden path? | `os_sqli.php` |

### Task 4: From DB to OS

**Explicación:**

Ejecutando comandos a través de la inyección SQL (out-of-band / into outfile / SQLi a shell), el resultado de `pwd` es `/var/lib/mysql`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the output of pwd when run via an SQL injection attack? | `/var/lib/mysql` |

### Task 5: Finding a Needle in a Malwarestack

**Explicación:**

La ubicación del malware es `/home/products/malware/4sale/pal4t1n3/MisterMeist3r/2DC6C0` (en la fuente figuraba `pal4tln3`; el writeup público muestra `pal4t1n3`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the malware's location? | `/home/products/malware/4sale/pal4t1n3/MisterMeist3r/2DC6C0` |

### Task 6: Operation Defang

**Explicación:**

Explorando el directorio del malware objetivo se descubre algo que sugiere cómo deshabilitar sus efectos dañinos. El lenguaje de programación usado para desarrollar el malware es **nim**. Leyendo el código fuente, la extensión que se añade al final de los archivos cifrados es **.boogey**. Tras recompilar el malware "defangeado" (modificado para que no cause daño), la flag es `THM{3FDbU2nNy2FW7yMvMoH6WTMMM}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What programming language was used to develop the malware? | `nim` |
| 2 | Reading the source code, what file type is added to the end of encrypted files? | `.boogey` |
| 3 | What is the flag that appears after compiling the defanged malware? | `THM{3FDbU2nNy2FW7yMvMoH6WTMMM}` |

---

**Metodología:**

1. Obtener las credenciales del sospechoso (`lannister` / `hrpTfL42wMv3`) desde la máquina pública.
2. Relacionar conceptos SQL/RDBMS/CRUD y encontrar la ruta oculta `os_sqli.php`.
3. Explotar la inyección SQL para conseguir una shell OS (`pwd` → `/var/lib/mysql`).
4. Navegar a la tienda de malware y localizar el más vendido (`pel4t1n3/MisterMeist3r/2DC6C0`).
5. Analizar el código (nim), identificar la extensión de cifrado (`.boogey`) y modificar ("defangear") el malware.
6. Recompilar el malware "defangeado" y obtener la flag `THM{3FDbU2nNy2FW7yMvMoH6WTMMM}`.

**Learning chain:** lannister creds -> RDBMS/SQL -> os_sqli.php -> SQLi->shell -> /var/lib/mysql -> malware store -> pal4t1n3/MisterMeist3r/2DC6C0 -> nim -> .boogey -> defang -> recompilar -> flag

**Lección:** *La inyección SQL puede escalar a shell del sistema; una vez dentro de una infraestructura de venta de malware, entender el lenguaje y la mecánica del código (extensión `.boogey`) permite "defangearlo" para que no cause daño real.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1059 (Command and Scripting Interpreter) · T1486 (Data Encrypted for Impact) · CWE-89 (SQL Injection)

**Fuente:** [TryHackMe - TryHack3M: Sch3Ma D3Mon](https://tryhackme.com/room/sch3mad3mon)
