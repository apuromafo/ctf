# Linux Local Enumeration

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `lle` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/lle) |
| **Sección** | 01 Level Easy |
| **Fuente** | THM |
| **Componentes** | reverse shell, TTY, uname, bash history, sudo, /etc, find, SUID, GTFObins, netstat, LinPEAS, LinEnum |
| **Impacto** | Post-explotación: enumeración local que permite identificar credenciales, archivos sensibles y escalar a root vía SUID (grep) |

---

**Contexto:** Sala que enseña a enumerar eficientemente una máquina Linux tras obtener un reverse shell. Cubre estabilización de la shell (TTY), enumeración básica del sistema (uname, bash history, sudo), análisis de archivos en /etc, búsqueda de archivos interesantes con find, abuso de binarios SUID contra GTFObins y enumeración automatizada con LinPEAS y LinEnum.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's go! | `No answer needed` |

### Task 2: Unit 1: TTY

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How would you execute /bin/bash with perl? | `perl -e 'exec "/bin/bash";'` |

### Task 3: Unit 1: SSH

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Where can you usually find the id_rsa file? (User = user) | `/home/user/.ssh/id_rsa` |
| 2 | Is there an id_rsa file on the box? (yay/nay) | `nay` |

### Task 4: Unit 2: Basic Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How would you print machine hardware name only? | `uname -m` |
| 2 | Where can you find bash history? | `~/.bash_history` |
| 3 | What's the flag? | `thm{clear_the_history}` |

### Task 5: Unit 3: /etc

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you read /etc/passwd on the box? (yay/nay) | `yay` |

### Task 6: Unit 4: Find Command and Interesting Files

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the password you found? | `THMSkidyPass` |
| 2 | Did you find a flag? | `thm{conf_file}` |

### Task 7: Unit 4: SUID

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which SUID binary has a way to escalate your privileges on the box? | `grep` |
| 2 | What's the payload you can use to read /etc/shadow with this SUID? | `grep '' /etc/shadow` |

### Task 8: [Bonus] Port Forwarding

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Try using those commands on your system! | `No answer needed` |

### Task 9: Unit 5: Automating Scripts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Got it! | `No answer needed` |

### Task 10: Resources and What's Next?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above and consider completing mentioned rooms. | `No answer needed` |

---

**Metodología:** Se obtiene un reverse shell contra el puerto 3000 (MACHINE_IP:3000) usando un payload PHP y un listener netcat, y la shell se estabiliza a TTY completo con Python/Perl. La enumeración básica empieza con `uname -a`, revisión de `~/.bash_history` (donde aparece la flag `thm{clear_the_history}`), `sudo -V` (versiones < 1.8.28 son vulnerables a CVE-2019-14287) y `sudo -l`. Se exploran los archivos críticos de /etc (passwd, shadow, hosts) y se buscan archivos de interés por extensión (_*.log_, _*.conf_, _*.bak_) con `find`, encontrando `passwords.bak` con `THMSkidyPass` y `flag.conf` con `thm{conf_file}`. Con `find / -perm -u=s -type f` se identifica el binario SUID `grep`, que tras consultar GTFObins permite leer `/etc/shadow` (escalada a root). Finalmente se usa `netstat -tulpn` para enumeración de puertos/procesos y scripts como LinPEAS y LinEnum para verificación automatizada.

**Learning chain:** reverse shell (php + netcat) → TTY stabilization → uname/sudo/bash_history enumeration → /etc analysis → find for interesting files → credentials discovery → SUID grep + GTFObins → escalate to root → netstat port forwarding → LinPEAS/LinEnum automated verification

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1548.001 (Setuid and Setgid), T1082 (System Information Discovery), T1552.001 (Credentials In Files), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Linux Local Enumeration](https://tryhackme.com/r/room/lle)
