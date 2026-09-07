# Linux Privilege Escalation: Enumeration

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `linprivenum` |
| **Link** | [TryHackMe](https://tryhackme.com/room/linprivenum) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + Ubuntu 24.04 VM (revamped 2026, kernel 6.8.0-1017-aws) |
| **Componentes** | hostname / uname / cat /etc/os-release / crontab / aa-status / env / history / sudo -l / /etc/passwd / ip a / ss / find / ls |
| **Impacto** | Las 4 capas de enumeración (OS, usuarios, red, archivos) que revelan las vías de escalada de privilegios en Linux |

---

**Contexto:** Enumeración es el 70% de la escalada de privilegios en Linux. El room (revamped 2026, Ubuntu 24.04.1 LTS, kernel **6.8.0-1017-aws**) te guía por las 4 capas de enum: **OS** (hostname, kernel, AppArmor, cron jobs), **Users** (LANG, history, sudo, mailman), **Network** (interfaces, ports) y **Files** (secret files, hidden flags).

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ready for some enumeration! | `No answer needed` |

### Task 2: What Is Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 3: OS Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **hostname** of the target host? | `linux-enumeration` |
| 2 | What is the **Linux kernel version** of the target host? | `6.8.0-1017-aws` |
| 3 | What **version of Ubuntu** is running on the host? | `Ubuntu 24.04.1 LTS` |
| 4 | What is the **full path** of the script run by root every 5 minutes? | `/root/backup.sh` |
| 5 | What is the **full version of AppArmor**? | `4.0.1really4.0.1-0ubuntu0.24.04.3` |

### Task 4: User Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Print the environment variables. What is the value of **LANG**? | `C.UTF-8` |
| 2 | What is the **flag in your history**? | `THM{history-is-not-safe}` |
| 3 | What is the **full path** of the command you are allowed to run with elevated privileges? | `/usr/bin/nmap` |
| 4 | What is the **username** of the Mailing List Manager? | `list` |

### Task 5: Network Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the **network interface**, other than loopback? | `ens5` |
| 2 | What **port**, other than 22, is listening on the host? | `53` |

### Task 6: File Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the **contents of the secret file** in your home folder? | `THM{not-so-hidden}` |
| 2 | Find a **file** that has **TryHackMe** in its name. What is its **content**? | `THM{found-the-flag}` |

### Task 7: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Enumeration done. | `No answer needed` |

---

**Metodología:**
1. **OS enum:** `hostname` → `linux-enumeration`; `uname -a` (o `cat /etc/os-release`) → kernel `6.8.0-1017-aws` y `Ubuntu 24.04.1 LTS`; `cat /etc/crontab` / `crontab -l` / `/etc/cron.d/` → `/root/backup.sh` (root cada 5 min); `aa-status --version` → AppArmor `4.0.1really4.0.1-0ubuntu0.24.04.3`.
2. **User enum:** `env | grep LANG` (o `printenv LANG`) → `C.UTF-8`; `history` (o `cat ~/.bash_history`) → `THM{history-is-not-safe}`; `sudo -l` → `(ALL) NOPASSWD: /usr/bin/nmap`; `grep -i "mail" /etc/passwd` → Mailing List Manager `list`.
3. **Network enum:** `ip a` / `ifconfig` → interfaz `ens5`; `ss -tlnp` / `netstat -tlnp` → puerto `53` (DNS) además del 22 (SSH).
4. **File enum:** `ls -la` en home → archivo secreto (`cat .secret` → `THM{not-so-hidden}`); `find / -name "*TryHackMe*"` → contenido `THM{found-the-flag}`.

**Learning chain:** OS (hostname linux-enumeration / kernel 6.8.0-1017-aws / Ubuntu 24.04.1 / AppArmor 4.0.1really4.0.1 / cron /root/backup.sh) → Users (LANG=C.UTF-8 / history → THM{history-is-not-safe} / sudo /usr/bin/nmap / mailman=list) → Network (ens5 / port 53) → Files (THM{not-so-hidden} / THM{found-the-flag}) → escalada (nmap sudo, cron, AppArmor)

**MITRE ATT&CK:** T1082 (System Information Discovery), T1033 (System Owner/User Discovery), T1049 (System Network Connections Discovery), T1083 (File and Directory Discovery), T1548 (Abuse Elevation Control)

**Fuente:** [TryHackMe - Linux Privilege Escalation: Enumeration](https://tryhackme.com/room/linprivenum)