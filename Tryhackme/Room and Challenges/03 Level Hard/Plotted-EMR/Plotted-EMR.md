# Plotted-EMR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `plottedemr` | [TryHackMe](https://tryhackme.com/room/plottedemr) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=plottedemr` + websearch de walkthroughs) | OpenEMR / CVE-2018-15139 (RCE autenticado) / SQL Injection (user.sql) / Wildcard Injection (rsync) / cap_fowner (perl) / MySQL | Compromiso de un OpenEMR 5.0.1(3) mediante RCE autenticado, escalada a www-data por inyección de wildcards en un cron rsync y pivote a root abusando de la capability cap_fowner de perl. |

---

**Contexto:**

> **ES:** **Plotted-EMR** es un CTF Hard de explotación de **OpenEMR 5.0.1(3)**, un sistema de registros médicos electrónicos. La web está apuntando al puerto 80 y hay un MySQL 5900/tcp en loopback; se consigue RCE autenticado mediante el exploit **CVE-2018-15139** (SQL injection en el "slotting app" que permite escribir el sitio y obtener webshell). A continuación se escala a `www-data` abusando de un cron job con wildcards: el cron ejecuta `rsync -t *` como root y la inyección de wildcards permite escribir claves SSH autorizadas. Finalmente se explota la capability `cap_fowner` sobre el binario `perl` para escalar a root y leer la flag final. La sala retoma el universo "Plotted" junto a **Plotted-LMS**.
> **EN:** **Plotted-EMR** is a Hard CTF on exploiting **OpenEMR 5.0.1(3)**, an electronic medical records system. The web runs on port 80 and there is a MySQL 5900/tcp on loopback; authenticated RCE is achieved via the **CVE-2018-15139** exploit (SQL injection in the "slotting app" that lets you write to the site and get a webshell). Next, escalation to `www-data` is done by abusing a cron job with wildcards: the cron runs `rsync -t *` as root and wildcard injection allows writing authorized SSH keys. Finally, the `cap_fowner` capability on the `perl` binary is exploited to escalate to root and read the final flag. The room continues the "Plotted" universe along with **Plotted-LMS**.

---

## Solucionario

### Task 1: Hack the machine / Piratea la máquina

**Explicación:**
La sala pide obtener la flag 1 (el flag que se encuentra en el código/panel de OpenEMR) y las flags de usuario y root tras explotar la cadena completa: CVE-2018-15139 → webshell → cron wildcard con `rsync -t *` para subir clave SSH → acceso www-data → cap_fowner de perl → root.

1. No answer needed
2. 1. THM{EMR_PWn3d_CV3}
   2. 1aea32fbd5b592af1267d65dbcc3e212
   3. 827a0e697e1567f08022ba72106ace99

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |
| 2 | 1. What is the flag? | `THM{EMR_PWn3d_CV3}` |
| 2 | 2. What is user.txt? | `1aea32fbd5b592af1267d65dbcc3e212` |
| 2 | 3. What is root.txt? | `827a0e697e1567f08022ba72106ace99` |

---

**Metodología:**

1. Reconocimiento: `nmap` → puerto 80 (Apache/OpenEMR) y puerto 5900/tcp (MySQL) en loopback. Se apunta `plottedemr.thm` a `/etc/hosts`.
2. Identificación de la versión: el panel de login muestra **OpenEMR 5.0.1(3)**. La vulnerabilidad es la **CVE-2018-15139**: una SQL injection en el "slotting app" (fichero `file_download.php`/`sql_escape` ausente) que permite inyectar en la tabla `files` una entrada con el campo `path` controlado.
3. Fabricar el exploit: se crea un "fake user" (`admin`) con `sql_escape` vulnerable; vía la inyección se inserta un registro en `files` apuntando el `path` a una ruta que el script descarga/elimina, consiguiendo escribir un webshell en el DocumentRoot (por ejemplo `evil.php`).
4. WebShell → shell completa: se sube una reverse shell (p.ej. bash/PHP) y se recibe conexión como `www-data`. Flag 1 (`THM{EMR_PWn3d_CV3}`) se obtiene recorriendo el código de la app.
5. Enumeración: se descubre un cron que ejecuta `rsync -t *` como root desde un directorio donde www-data tiene escritura. Con **wildcard injection**: `ssh-keygen -t rsa` local → `cp id_rsa.pub authorized_keys` en el directorio del cron → además `touch -- "-e sh -c '...'"` y `cp authorized_keys -- '-e sh -c ...'` para que rsync lo trate como opción `--e sh -c 'cat...'` → Lograr que el cron escriba la clave en `/root/.ssh/authorized_keys` → SSH como root, o al menos como www-data con shell interactiva.
6. Escalada a root con cap_fowner: con `getcap -r /` se descubre que `/usr/bin/perl` conserva la capability `cap_fowner` (permite cambiar el propietario de ficheros ajenos). Con `perl -e 'chown(0,0,"/etc/shadow")'` se concede la propiedad de `/etc/shadow` (o `/etc/passwd`) y se escribe un nuevo usuario con UID 0 → `su newroot` / lectura de `root.txt`.

### Cadena de ataque / Attack Chain

`nmap → OpenEMR 5.0.1(3) login → CVE-2018-15139 (SQLi slotting app) → Inserción en tabla files (path controlado) → Webshell -> Reverse shell www-data → Flag 1 → Cron rsync -t * (root) → Wildcard injection (--e sh -c ...) → authorized_keys en /root/.ssh → SSH root → user.txt → getcap perl (cap_fowner) → chown /etc/shadow (o /etc/passwd) → New root user → root.txt`

**Learning chain:**

Fingerprint de OpenEMR → Búsqueda de CVE → SQL injection en "slotting app" → Fabricación de webshell vía BBDD → Reverse shell → Descubrimiento de cron jobs → Wildcard injection sobre `rsync -t *` → Escritura de claves SSH → Reconocimiento de capabilities (getcap) → Abuso de `cap_fowner` con perl → Lectura de root.txt

*Lección:* Una "afección" de log4j del mundo EMR: la SQLi del slotting app convierte una base de datos en una webshell. Y en el sistema, dos "errores de tuning" son la clave final: ejecutar `rsync -t *` con wildcards en un cron como root (inyección de opciones) y entregar `cap_fowner` a perl (cambio de propiedad de ficheros del sistema).

**MITRE ATT&CK:**

T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell: Server Software), T1053.003 (Scheduled Task/Job: Cron), T1548 (Abuse Elevation Control Mechanism: capabilities), T1068 (Exploitation for Privilege Escalation), T1552.001 (Unsecured Credentials: Credentials In Files)

**Fuente:** [TryHackMe - Plotted-EMR](https://tryhackme.com/room/plottedemr)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.