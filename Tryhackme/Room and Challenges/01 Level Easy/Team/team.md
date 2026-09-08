# Team

| **Dificultad** | Easy |
| **Tipo** | CTF (boot2root) |
| **Slug** | `teamcw` |
| **Link** | [TryHackMe](https://tryhackme.com/room/teamcw) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Virtual Hosting / /etc/hosts / FFUF-Gobuster-feroxbuster / FTP / LFI / OpenSSH private key / sudo -l / inyección de comandos / cronjob / SUID bash |
| **Impacto** | CTF donde, tras añadir `team.thm` y `dev.team.thm` al fichero hosts, se obtienen credenciales FTP (decodificando un base64 de `script.old`), se explota un LFI para leer la clave privada SSH de Dale desde `sshd_config`, se accede por SSH y se escala privilegios explotando una inyección de comandos en un script de backup (sudo) y, finalmente, un cronjob que ejecuta un script editable por el grupo `admin` para suplantar bash con SUID y leer las flags `user.txt` y `root.txt`. |

---

**Contexto:** La máquina expone FTP (21), SSH (22) y HTTP (80). El sitio web indica que hay que añadir `team.thm` al archivo hosts. Tras la enumeración (feroxbuster) aparecen `/scripts/script.txt` y `/scripts/script.old`; este último tiene un blob base64 que decodificado devuelve `ftpuser:T3@m$h@r3`. Vía FTP, `New_site.txt` desvela el subdominio `.dev` (dev.team.thm). En `dev.team.thm` se explota un LFI en un parámetro del navegador para leer `/etc/passwd` y `/etc/ssh/sshd_config`, donde está la clave privada OpenSSH del usuario `dale`. Con `ssh -i key.pem dale@<IP>` se obtiene la primera flag. Con `sudo -l` se ve que `dale` puede ejecutar un script de backup de `gyles` que hace `$error 2>/dev/null` con entrada del usuario: introduciendo `/bin/bash` se obtiene shell de `gyles`. `gyles` pertenece al grupo `admin`, y el cronjob root ejecuta `/usr/local/bin/main_backup.sh` (propiedad `root:admin`), por lo que se añade `cp /bin/bash /tmp/rootbash` y `chmod +s /tmp/rootbash`, y con `/tmp/rootbash -p` se alcanza root y la segunda flag.

## Solucionario

### Task 1: Reconocimiento y acceso inicial

**Explicación:** Enumeración de puertos (nmap: 21/22/80) y directorios. Tras añadir `team.thm` a `/etc/hosts`, `feroxbuster` encuentra `/scripts/script.txt` y `/scripts/script.old`. El base64 de `script.old` entrega las credenciales FTP `ftpuser:T3@m$h@r3`. En el FTP, `New_site.txt` revela el subdominio `dev.team.thm` y pide copiar la `id_rsa` en un archivo de configuración.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Enumera puertos, añade `team.thm`/`dev.team.thm` a hosts, consigue las credenciales FTP y localiza el subdominio de desarrollo. | `No answer needed` |

### Task 2: Explotación del LFI y flag de usuario

**Explicación:** En `dev.team.thm` un parámetro del navegador permite LFI: se lee `/etc/ssh/sshd_config`, donde aparece la clave privada de `dale`. Se restaura el formato OpenSSH (la clave venía en una línea con caracteres `#` y espacios), se guarda como `key.pem` con `chmod 600` y se entra con `ssh -i key.pem dale@<IP>`. Dentro, `user.txt` contiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de `user.txt`? | `THM{6Y0TXHz7c2d}` |

### Task 3: Escalada de privilegios y flag de root

**Explicación:** `sudo -l` muestra que `dale` puede ejecutar el script de backup propiedad de `gyles`, que ejecuta `$error 2>/dev/null` sin sanitizar. En el primer prompt se pone cualquier nombre y en el segundo `/bin/bash`, obteniendo una shell de `gyles`. En `/home/gyles/.bash_history` se ve que este usuario usa `/opt/admin_stuff/script.sh`, un cronjob que cada minuto ejecuta `main_backup.sh` (root:admin) y `dev_backup.sh` (root:root). Como `gyles` pertenece al grupo `admin`, puede editar `main_backup.sh` e inyectar `cp /bin/bash /tmp/rootbash` + `chmod +s /tmp/rootbash`. Tras esperar un minuto, `/tmp/rootbash -p` da root y se lee `root.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de `root.txt`? | `THM{fhqbznavfonq}` |

---

**Metodología:** nmap → gobuster/ffuf/feroxbuster → vhost (`team.thm`, `dev.team.thm`) → credenciales FTP desde base64 → LFI para leer `sshd_config` → clave privada SSH → foothold como `dale` → inyección de comandos en script sudo → shell como `gyles` → abuso del cronjob (grupo `admin`) → bash con SUID → root.
**Learning chain:** reconocimiento y vhosts → robo de credenciales (base64) → LFI → clave SSH → escalada por inyección de comandos → squash root vía cronjob + SUID.
**MITRE ATT&CK:** T1595.001 (Active Scanning), T1083 (File and Directory Discovery), T1552.004 (Unsecured Credentials: Private Keys), T1059.004 (Unix Shell), T1053.003 (Cron), T1548.001 (Setuid and Setgid)
**Fuente:** [TryHackMe - Team](https://tryhackme.com/room/teamcw)