# Traverse

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `traverse` | [TryHackMe](https://tryhackme.com/room/traverse) | 01 Level Easy | THM | directory traversal, directory listing, email dump, webshell, credenciales | Compromiso de un servidor web mediante directory traversal, robo de credenciales y restauración del sitio |

---

**Contexto:**

> **ES:** La sala plantea el compromiso de un servidor web mediante una vulnerabilidad de directory traversal. Se explota el listado de directorios para caminar por la estructura del sitio, extraer credenciales de un dump de correos, localizar el panel de administración real y desplegar una webshell renombrada para mantener el acceso, restaurar el sitio y capturar la flag final.

> **EN:** This room walks through the compromise of a web server via a directory traversal vulnerability. The directory listing is abused to walk through the site structure, extract credentials from an email dump, locate the real admin panel, and deploy a renamed webshell to keep access, restore the site, and capture the final flag.

## Solucionario

### Task 1: Resolución de la sala / Traverse Walkthrough

**Explicación:**

1. 1. HEX
   2. DIRECTORY LISTING IS THE ONLY WAY
   3. email_dump.txt
   4. planning
   5. THM{100100111}
   6. john@traverse.com
   7. 3
   8. /realadmin
   9. thm_shell.php
   10. renamed_file_manager.php
   11. THM{WEBSITE_RESTORED}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which encoding is used for the first directory name? | `HEX` |
| 2 | What message does the server reveal about the directory? | `DIRECTORY LISTING IS THE ONLY WAY` |
| 3 | Which email file is discovered in the listing? | `email_dump.txt` |
| 4 | Which sensitive subdirectory is located? | `planning` |
| 5 | What is the first flag? | `THM{100100111}` |
| 6 | Which user email is obtained from the dump? | `john@traverse.com` |
| 7 | How many traversal steps are needed? | `3` |
| 8 | Which path leads to the real admin panel? | `/realadmin` |
| 9 | Which webshell is uploaded to the server? | `thm_shell.php` |
| 10 | What is the renamed file manager used to stay hidden? | `renamed_file_manager.php` |
| 11 | What is the final flag? | `THM{WEBSITE_RESTORED}` |

---

**Metodología:** Se enumera el servidor web y se aprovecha el listado de directorios (directory listing) para descubrir la codificación y los directorios sensibles. Localizado el dump de correos, se extraen las credenciales y se determina la profundidad de traversal necesaria (3) para alcanzar `/realadmin`. Desde el panel de administración se sube una webshell (`thm_shell.php`) y se renombra el gestor de archivos (`renamed_file_manager.php`) para evadir detección, restaurar el sitio y obtener la flag final.

### Cadena de ataque / Attack Chain

Directory listing → HEX decoding → email dump → credential extraction → directory traversal → admin panel → webshell upload → site restoration → final flag.

**Learning chain:** Web recon → directory listing → email dump → credential extraction → traversal depth → admin panel → webshell upload → site restoration → final flag

**Lección:** *Un listado de directorios no es un fallo menor: es el primer eslabón que convierte un servidor web en una puerta totalmente abierta.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1083 (File and Directory Discovery), T1036 (Masquerading), T1505.003 (Web Shell)

**Fuente:** [TryHackMe - Traverse](https://tryhackme.com/room/traverse)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.