# Linux CLI - Shells Bells

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `linuxcli-aoc2025-o1fpqkvxti` | [TryHackMe](https://tryhackme.com/room/linuxcli-aoc2025-o1fpqkvxti) | Advent of Cyber 2025 | TryHackMe | Linux CLI, ls, grep, sudo, bash history | Discovery — investigación del laptop de McSkidy usando la línea de comandos de Linux |

---

**Contexto:** En el Día 1 del Advent of Cyber 2025, McSkidy nos pide investigar su laptop usando la línea de comandos de Linux. Debemos recorrer directorios, analizar logs de intentos de login fallidos, examinar scripts sospechosos y revisar el historial de bash del root para encontrar las flags dejadas por Sir Carrotbane.

> **ES:** Uso de comandos básicos de Linux (ls, grep, cat, sudo su) para investigar el laptop de McSkidy, filtrar logs de autenticación fallida, revisar el script "Eggstrike" y extraer del historial de bash del root las flags de Sir Carrotbane.
> **EN:** Use of basic Linux commands (ls, grep, cat, sudo su) to investigate McSkidy's laptop, filter failed-login logs, review the "Eggstrike" script and pull Sir Carrotbane's flags from root's bash history.

## Solucionario

### Task 1: Explorando directorios / Exploring Directories
**Explicación:** Empezamos recorriendo el árbol de directorios del laptop de McSkidy con `ls`. Al listar un directorio aparentemente vacío o al inspeccionar la guía con `cat`, encontramos la primera flag escondida en el interior de la guía de McSkidy.

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | Which CLI command would you use to list a directory? | `ls` |
| 2 | Identify the flag inside of McSkidy's guide | `THM{learning-linux-cli}` |

### Task 2: Investigando intentos de acceso / Investigating Login Attempts
**Explicación:** Para averiguar quién intentó acceder al laptop, filtramos el log de intentos de login fallidos con `grep`, localizando la evidencia de los intentos de Sir Carrotbane.

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | Which command helped you filter the logs for failed logins? | `grep` |

### Task 3: Examinando el script Eggstrike / Examining the Eggstrike Script
**Explicación:** Se examina el script `Eggstrike.sh` encontrado en el sistema para entender qué acciones maliciosas realizaba, y al leerlo con `cat` se localiza otra flag en su interior.

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | Identify the flag inside the Eggstrike script | `THM{sir-carrotbane-attacks}` |

### Task 4: ¿Qué hizo Sir Carrotbane? / What Did Sir Carrotbane Do?
**Explicación:** Para ver qué hizo Sir Carrotbane con privilegios elevados usamos `sudo su` y cambiamos al usuario root. Revisando el historial de bash (`cat .bash_history`) del root encontramos sus comandos y la flag final que dejó.

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | Which command would you run to switch to the root user? | `sudo su` |
| 2 | What flag did Sir Carrotbane leave in the root bash history? | `THM{until-we-meet-again}` |

### Task 5 (Side Quest 1): Nota oculta de McSkidy / McSkidy's Hidden Note
**Explicación:** Búsqueda opcional de la nota oculta de McSkidy. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | No answer needed | — |

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which CLI command would you use to list a directory? | `ls` |
| 2 | Identify the flag inside of McSkidy's guide | `THM{learning-linux-cli}` |
| 3 | Which command helped you filter the logs for failed logins? | `grep` |
| 4 | Identify the flag inside the Eggstrike script | `THM{sir-carrotbane-attacks}` |
| 5 | Which command would you run to switch to the root user? | `sudo su` |
| 6 | What flag did Sir Carrotbane leave in the root bash history? | `THM{until-we-meet-again}` |
| 7 | No answer needed | `—` |

---

**Metodología:** Se usaron comandos básicos de Linux (`ls`, `grep`, `cat`) para explorar el filesystem, filtrar logs de autenticación fallida, revisar scripts y examinar el historial de bash del usuario root.

### Cadena de ataque / Attack Chain

```text
ls (listado de directorios) -> cat guía de McSkidy -> flag 1 -> grep en logs de login fallido -> cat Eggstrike.sh -> flag 2 -> sudo su -> cat .bash_history del root -> flag final
```

**Learning chain:** ls -> directory exploration -> grep -> log filtering -> sudo su -> privilege escalation -> bash history -> artifact recovery

**Lección:** *La línea de comandos es la navaja suiza de la investigación: listar, filtrar logs y revisar el historial de bash permite reconstruir la actividad de un usuario y encontrar artefactos (flags) dejados atrás.*

**MITRE ATT&CK:** T1059.004 - Command and Scripting Interpreter: Unix Shell

**Fuente:** [TryHackMe - Linux CLI - Shells Bells](https://tryhackme.com/room/linuxcli-aoc2025-o1fpqkvxti)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.