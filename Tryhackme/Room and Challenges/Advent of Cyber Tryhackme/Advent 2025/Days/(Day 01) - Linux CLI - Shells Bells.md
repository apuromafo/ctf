# Linux CLI - Shells Bells [EASY]

### Información de la Sala / Room Information

| Propiedad / Property | Valor / Value |
| --- | --- |
| **Nombre / Name** | Linux CLI - Shells Bells |
| **Evento / Event** | Advent of Cyber 2025 — Día 01 |
| **Sala / Room URL** | https://tryhackme.com/room/adventofcyber25 |
| **Dificultad / Difficulty** | Easy |
| **Descripción / Description** | Día 01 del calendario AoC 2025 (Linux CLI - Shells Bells). Solución/respuestas del reto diario. |

---


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

## Respuestas / Answers
- Which CLI command would you use to list a directory? : `ls`
- Which command helped you filter the logs for failed logins? : `grep`
- Which command would you run to switch to the root user? : `sudo su`
- Finally, what flag did Sir Carrotbane leave in the root bash history? : `THM{until-we-meet-again}`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
