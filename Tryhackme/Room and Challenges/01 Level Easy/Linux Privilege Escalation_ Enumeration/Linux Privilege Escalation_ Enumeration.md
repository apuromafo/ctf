# Linux Privilege Escalation: Enumeration [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `linprivenum`
* **Link:** https://tryhackme.com/room/linprivenum
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + Ubuntu 24.04 VM (revamped 2026, kernel 6.8.0-1017-aws)
* **Componentes:** Enumeración en Linux · OS enum (hostname, kernel, Ubuntu version, AppArmor) · User enum (env, history, sudo, mailman) · Network enum (interfaces, ports) · File enum (secret files, hidden flags)
* **Impacto rol:** Fundamento para la escalada de privilegios: enumerar correctamente es más del 70% del trabajo; saber qué buscar evita.Timeouts.ciegas.

## Solucionario de Tareas / Task Solutions

> **ES:** Enumeration es el 70% de la escalada de privilegios en Linux. El room (revamped 2026, Ubuntu 24.04.1 LTS, kernel **6.8.0-1017-aws**) te guía por las 4 capas de enum: **OS** (hostname, kernel, AppArmor, cron jobs), **Users** (LANG, history, sudo, mailman), **Network** (interfaces, ports) y **Files** (secret files, TryHackMe flag). Hostname: `linux-enumeration`. Kernel: `6.8.0-1017-aws`. Ubuntu: `Ubuntu 24.04.1 LTS`. AppArmor full: `4.0.1really4.0.1-0ubuntu0.24.04.3`. Script de root: `/root/backup.sh`. Variable LANG: `C.UTF-8`. Historial: `THM{history-is-not-safe}`. Comando con sudo: `/usr/bin/nmap`. Usuario mailing list manager: `list`. Interfaz: `ens5`. Puerto: `53`. Secret file: `THM{not-so-hidden}`. TryHackMe flag: `THM{found-the-flag}`.
> **EN:** Enumeration is 70% of Linux privilege escalation. The room (revamped 2026, Ubuntu 24.04.1 LTS, kernel **6.8.0-1017-aws**) guides you through 4 enum layers: **OS** (hostname, kernel, AppArmor, cron), **Users** (LANG, history, sudo, mailman), **Network** (interfaces, ports) and **Files** (secret files, hidden flags). Hostname: `linux-enumeration`. Kernel: `6.8.0-1017-aws`. Ubuntu: `Ubuntu 24.04.1 LTS`. AppArmor full: `4.0.1really4.0.1-0ubuntu0.24.04.3`. Root script: `/root/backup.sh`. LANG: `C.UTF-8`. History flag: `THM{history-is-not-safe}`. Sudo command: `/usr/bin/nmap`. Mailing List Manager: `list`. Interface: `ens5`. Port: `53`. Secret: `THM{not-so-hidden}`. TryHackMe: `THM{found-the-flag}`.

### Task 1 — Introducción / Introduction

* **Check:** `Ready for some enumeration!`

### Task 2 — Qué es Enumeración / What Is Enumeration *(vm)*

* **ES/EN:** check (sin pregunta visible).

### Task 3 — Enumeración del OS / OS Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **hostname** of the target host? | `linux-enumeration` |
| What is the **Linux kernel version** of the target host? | `6.8.0-1017-aws` |
| What **version of Ubuntu** is running on the host? | `Ubuntu 24.04.1 LTS` |
| What is the **full path** of the script run by root every 5 minutes? | `/root/backup.sh` |
| What is the **full version of AppArmor**? | `4.0.1really4.0.1-0ubuntu0.24.04.3` |

* **Comandos / Commands:**
  * `hostname` → `linux-enumeration`
  * `uname -a` → `6.8.0-1017-aws` (o `cat /etc/os-release`)
  * `cat /etc/os-release` → `Ubuntu 24.04.1 LTS`
  * `cat /etc/crontab` o `crontab -l` o `/etc/cron.d/` → `/root/backup.sh` (la línea indica ejecución de root cada 5 min)
  * `aa-status --version` (AppArmor) → `4.0.1really4.0.1-0ubuntu0.24.04.3`

### Task 4 — Enumeración de Usuarios / User Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Print the environment variables. What is the value of **LANG**? | `C.UTF-8` |
| What is the **flag in your history**? | `THM{history-is-not-safe}` |
| What is the **full path** of the command you are allowed to run with elevated privileges? | `/usr/bin/nmap` |
| What is the **username** of the Mailing List Manager? | `list` |

* **Comandos:**
  * `env | grep LANG` (o `printenv LANG`) → `C.UTF-8`
  * `history` (o `cat ~/.bash_history`) → la entrada contiene `THM{history-is-not-safe}`
  * `sudo -l` → `(ALL) NOPASSWD: /usr/bin/nmap` (la regla sudo permite ejecutar nmap como root)
  * `grep -i "mail" /etc/passwd` → el usuario Mailing List Manager es `list` (o consultar la config de mailman)

### Task 5 — Enumeración de Red / Network Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the **network interface**, other than loopback? | `ens5` |
| What **port**, other than 22, is listening on the host? | `53` |

* **Comandos:**
  * `ip a` o `ifconfig` → interfaz `ens5` (IP privada)
  * `ss -tlnp` o `netstat -tlnp` → puerto `53` (DNS) escuchando además del 22 (SSH)

### Task 6 — Enumeración de Archivos / File Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What are the **contents of the secret file** in your home folder? | `THM{not-so-hidden}` |
| Find a **file** that has **TryHackMe** in its name. What is its **content**? | `THM{found-the-flag}` |

* **Comandos:**
  * `ls -la` en home → archivo secreto (p.ej. `.secret`) → `cat .secret` → `THM{not-so-hidden}`
  * `find / -name "*TryHackMe*"` → archivo con "TryHackMe" en el nombre → `cat` → `THM{found-the-flag}`

### Task 7 — Conclusión / Conclusion

* **Check:** `Enumeration done.`
* **ES:** Siguiente room: escalada de privilegios.
* **EN:** Next room: privilege escalation.

## Metodología / Methodology

1. **Paso / Step:** OS enum: `hostname`, `uname -a`, `cat /etc/os-release`, cron, AppArmor version.
2. **Paso / Step:** User enum: `env`, `history`, `sudo -l`, grep de mailing list manager en `/etc/passwd`.
3. **Paso / Step:** Network: `ip a` / `ifconfig`, `ss -tlnp` / `netstat -tlnp`.
4. **Paso / Step:** File enum: `ls -la` home + `find / -name "*TryHackMe*"`.

### Cadena de aprendizaje / Learning Chain

```
OS: hostname (linux-enumeration) / kernel (6.8.0-1017-aws) / Ubuntu 24.04.1 / AppArmor 4.0.1really4.0.1
    cron -> /root/backup.sh
  -> User: LANG=C.UTF-8 / history -> THM{history-is-not-safe} / sudo -> /usr/bin/nmap / mailman=list
  -> Network: ens5 / port 53 (DNS)
  -> Files: secret -> THM{not-so-hidden} / TryHackMe -> THM{found-the-flag}
  -> escalada: nmap (sudo) / AppArmor status / cron exploitable
```

**Mapeo MITRE ATT&CK:** T1082 (System Information Discovery) · T1033 (System Owner/User Discovery) · T1049 (System Network Connections Discovery) · T1083 (File and Directory Discovery). La escalada posterior usaría T1548 (Abuse Elevation Control) vía nmap `--interactive` o AppArmor bypass.

**Lección:** *Enumerar es mapear el terreno antes de correr: kernel, versiones, cron, sudo, archivos — cada dato es una posible vía de escalada.*

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.