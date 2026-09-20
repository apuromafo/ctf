# Plotted-LMS

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `plottedlms` | [TryHackMe](https://tryhackme.com/room/plottedlms) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=plottedlms` + websearch de walkthroughs) | Moodle (3.9.0-beta) / CVE-2020-14321 (teacher→manager RCE) / Cron job con os.system / logrotten (logrotate 3.15.0) / PHP / Python | RCE en un LMS Moodle vulnerable (CVE-2020-14321), inyección de comandos en un script Python del cron mediante nombres de fichero y escalada a root reempleazando un binario por un logrotate mal configurado con logrotten. |

---

**Contexto:**

> **ES:** **Plotted-LMS** es un CTF Hard centrado en un **Moodle 3.9.0-beta** (Learning Management System). La escalada principal es el **CVE-2020-14321**: un usuario con rol Teacher puede convertirse en Manager y subir/ejecutar código (RCE) gracias a una validación insuficiente. La máquina además tiene un cron que ejecuta `backup.py` como root; `backup.py` usa `os.system` sobre el nombre del fichero, de modo que con un nombre de archivo tipo `;$(comando)` y la función `stdout` del script se ejecuta cualquier comando como root (retorno a la shell del usuario www-data). Finalmente se usa la herramienta **logrotten**: el logrotate del sistema (versión 3.15.0, sin protección de "create mode" seguro por el viejo `compress`) rota ficheros una vez al día y logrotten intercambia el binario `/usr/sbin/funlog` por la parte paylodada; al rotarse, se ejecuta como root → flag. La profesora/personaje de la sala siembra pistas tipo "sube el moodle", haciendo de la cadena un recorrido por un LMS escolapio vulnerable.
> **EN:** **Plotted-LMS** is a Hard CTF centered on a **Moodle 3.9.0-beta** (Learning Management System). The main escalation is **CVE-2020-14321**: a user with the Teacher role can become a Manager and upload/execute code (RCE) thanks to insufficient validation. The machine also runs a cron executing `backup.py` as root; `backup.py` uses `os.system` on the filename, so a filename like `;$(command)` combined with the script's `stdout` function executes any command as root (returning to the www-data shell). Finally the **logrotten** tool is used: the system's logrotate (version 3.15.0, without safe "create mode" because of the old `compress`) rotates files once a day and logrotten swaps the `/usr/sbin/funlog` binary for the payloaded part; when rotation triggers, it runs as root → flag. The teacher/character of the room plants hints like "upload moodle" along the way, turning the chain into a trip through a vulnerable school LMS.

---

## Solucionario

### Task 1: Hack the machine / Piratea la máquina

**Explicación:**
Completando el recorrido (RCE vía rol de profesor en el Moodle, inyección de comandos en el cron `backup.py`, y escalada con logrotten) se obtienen las flags de usuario y root.

1. 1. 7e0345c7c7c46668ad7d147ef53ce250
   2. 26d7752933d9ffcdbcbe4f640f54d8c2

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | 1. What is user.txt? | `7e0345c7c7c46668ad7d147ef53ce250` |
| 1 | 2. What is root.txt? | `26d7752933d9ffcdbcbe4f640f54d8c2` |

---

**Metodología:**

1. Reconocimiento: `nmap` → puerto 80 (Moodle) y SSH. Se añade `plottedlms.thm` a `/etc/hosts`.
2. Identificar Moodle 3.9.0-beta: la versión aparece en el footer/`version.php`. La vulnerabilidad es **CVE-2020-14321** (moodle_risk_xss → el rol Teacher puede escalar a Manager y con ello llegar a RCE).
3. Preparar el exploit (típicamente un PoC en Python): como Teacher se abusa de la falta de comprobación de capabilities en la gestión de cursos para convertirse en Manager.
4. Como Manager se sube un componente/tema de Moodle con código arbitrario (por ejemplo un webshell PHP dentro de un "template" o un plugin) → ejecución de código PHP en el servidor → reverse shell como `www-data`.
5. Enumeración: se detecta en `/etc/crontab` (o `/var/spool/cron`) una tarea que ejecuta `/opt/moodle/backup.py` como root cada minuto. `backup.py` construye un comando `tar`/`rsync`/shell con `os.system(nombre_de_archivo)`.
6. Inyección de comandos en el cron: se crea en el directorio de backups un fichero cuyo nombre contiene un comando entre `;$(...)` — ej. `standard;$(cp /root/root.txt /tmp/root.txt)` — acompañado de un "marker" para que el script lo detecte en su ciclo y ejecute (stdout). El comando se ejecuta como root; el resultado (root.txt) se lee como www-data → **user.txt** ya resuelta y flag de sistema extraída.
7. Escalada final con logrottten: se identifica `/etc/logrotate.conf` rotando `/usr/sbin/funlog` con logrotate 3.15.0 y `compress` activo (el estado `funlog` no se protege). Se descarga/compila **logrotten** y se genera el payload (reverse shell o copia de root.txt) → `logrotten /usr/sbin/funlog payload` → en cuanto rota, el binario sustituido se ejecuta → root → **root.txt**.

### Cadena de ataque / Attack Chain

`nmap → Moodle 3.9.0-beta → CVE-2020-14321 (Teacher → Manager) → Upload tema/plugin con webshell → RCE PHP → Reverse shell www-data → Cron backup.py (os.system sobre nombre de archivo) → ;$(comando) + stdout → Ejecución root → user.txt → logrotten: /usr/sbin/funlog + logrotate 3.15.0 compress → Binario sustituido → Ejecución como root → root.txt`

**Learning chain:**

Fingerprint de Moodle (versión) → Búsqueda de CVE y PoC → Escalada de rol dentro de la app (Teacher → Manager) → Upload de tema para webshell → Reverse shell → Descubrimiento de cron jobs → Inyección de comandos vía nombre de fichero en scripts que usan os.system → logrotten vs logrotate ≤ 3.15.0 (compress) → Sustitución de binario y ejecución root.

*Lección:* Un sistema de gestión de aprendizaje "viejo" es una mina: la validación de roles rota (CVE-2020-14321) convierte a un profesor en administrador de código. Y los cron jobs que concatenan nombres de fichero en `os.system` son bombs de ejecución silenciosa. La cadena termina explotando un logrotate sin las mitigaciones de "copytruncate + create" modernas, con logrotten.

**MITRE ATT&CK:**

T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1505.003 (Web Shell: Server Software), T1053.003 (Scheduled Task/Job: Cron), T1059.006 (Command and Scripting Interpreter: Python), T1574.007 (Hijack Execution Flow: Path Interception), T1552.001 (Unsecured Credentials: Credentials In Files)

**Fuente:** [TryHackMe - Plotted-LMS](https://tryhackme.com/room/plottedlms)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.