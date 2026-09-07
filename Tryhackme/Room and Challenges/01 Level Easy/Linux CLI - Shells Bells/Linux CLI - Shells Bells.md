# Linux CLI - Shells Bells

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `linuxcli-aoc2025-o1fpqkvxti` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/linuxcli-aoc2025-o1fpqkvxti) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Linux CLI, ls, grep, sudo, bash history |
| **Impacto** | Discovery — investigación del laptop de McSkidy usando la línea de comandos de Linux |

---

**Contexto:** En el Día 1 del Advent of Cyber 2025, McSkidy nos pide investigar su laptop usando la línea de comandos de Linux. Debemos recorrer directorios, analizar logs de intentos de login fallidos, examinar scripts sospechosos y revisar el historial de bash del root para encontrar las flags dejadas por Sir Carrotbane.

## Solucionario

### Task 1: Exploring Directories

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which CLI command would you use to list a directory? | `ls` |
| 2 | Identify the flag inside of McSkidy's guide | `THM{learning-linux-cli}` |

### Task 2: Investigating Login Attempts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which command helped you filter the logs for failed logins? | `grep` |

### Task 3: Examining the Eggstrike Script

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identify the flag inside the Eggstrike script | `THM{sir-carrotbane-attacks}` |

### Task 4: What Did Sir Carrotbane Do?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which command would you run to switch to the root user? | `sudo su` |
| 2 | What flag did Sir Carrotbane leave in the root bash history? | `THM{until-we-meet-again}` |

### Side Quest 1: McSkidy's Hidden Note

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | — |

---

**Metodología:** Se usaron comandos básicos de Linux (`ls`, `grep`, `cat`) para explorar el filesystem, filtrar logs de autenticación fallida, revisar scripts y examinar el historial de bash del usuario root.
**Learning chain:** ls → directory exploration → grep → log filtering → sudo su → privilege escalation → bash history → artifact recovery
**MITRE ATT&CK:** T1059.004 - Command and Scripting Interpreter: Unix Shell
**Fuente:** [TryHackMe - Linux CLI - Shells Bells](https://tryhackme.com/r/room/linuxcli-aoc2025-o1fpqkvxti)
