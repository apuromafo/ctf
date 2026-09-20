# Linux CLI - Shells Bells

| **Dificultad** | Easy | **Tipo** | CTF (Free Room) | **Slug** | `day01linuxclishellsbells` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | Linux CLI / Bash / Filesystem / Logs / Privilege / History | | **Impacto** | Día 01 del AoC 2025: introducción al manejo de la línea de comandos Linux (listar, filtrar logs, root y bash history) |

---

**Contexto:** Día 01 del calendario Advent of Cyber 2025 ("Linux CLI - Shells Bells"). Reto introductorio a la línea de comandos de Linux: listar ficheros, filtrar logs de fallos de login, cambiar a root y encontrar la flag que Sir Carrotbane dejó en el historial de bash. El documento original es bilingüe (ES/EN); se conservan los apuntes y las respuestas verbatim.

---

## Solucionario

### Día 01: Linux CLI - Shells Bells

**Explicación:** Apuntes del laboratorio (notas bilingües originales):

- `ls` is used to list the contents of the current directory
- `cat` will display the contents of the file mentioned after it
- `pwd` prints the home directory
- `cd` is used to change the current directory
- A file/folder can be hidden just by starting with a `.`
- `ls -la` shows hidden files, where `-a` shows hidden files and `-l` shows additional details(i.e, file permissions, owners, etc)
- `grep` looks for a specific test within the file
- files ending with `sh` are called shell scripts. List of commands that run one after another.
- `find` command searches for files with specific parameters, such as `-name`
- Switch to the root user by running the `sudo su` command
- every command you run is saved in a hidden history file, also called `Bash history`

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Which CLI command would you use to list a directory? | `ls` |
| 2 | Which command helped you filter the logs for failed logins? | `grep` |
| 3 | Which command would you run to switch to the root user? | `sudo su` |
| 4 | Finally, what flag did Sir Carrotbane leave in the root bash history? | `THM{until-we-meet-again}` |

---

**Metodología:**

1. Enumeración básica del sistema con `ls` / `cat` / `pwd` / `cd`

2. Búsqueda de ficheros ocultos (`ls -la`) y del log de intentos fallidos con `grep`

3. Escalada a root con `sudo su`

4. Revisión del historial de bash para encontrar la flag

**Learning chain:** Filesystem -> Log filtering -> Privilege -> Bash history

**Lección:** *El historial de bash y los ficheros ocultos son fuentes de información clave en un pentest; dominar comandos básicos de Linux (ls, cat, grep, find, sudo su) permite localizar rápidamente flags y actividad sensible.*

**MITRE ATT&CK:**

- T1059.004 - Command and Scripting Interpreter: Unix Shell

- T1552.003 - Unsecured Credentials: Bash History

- T1078 - Valid Accounts (uso de root)

**Fuente:** [TryHackMe - Linux CLI - Shells Bells](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.