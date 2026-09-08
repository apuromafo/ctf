# KoTH Hackers

| **Dificultad** | MEDIUM | **Tipo** | CTF — King of the Hill (KoTH) (Free Room) | **Slug** | `kothhackers` |
| **Link** | [TryHackMe](https://tryhackme.com/room/kothhackers) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | KoTH / Linux / Privilege Escalation / FTP / Web Exploitation / Capabilities / GTFOBins | **Impacto** | Evalúa la velocidad ofensiva y defensiva en una competición King of the Hill |

---

**Contexto:** Sala de competición **King of the Hill (KoTH)** ambientada en la película *Hackers* (1995): la máquina (hostname **`gibson`**, empresa "Ellingson Mineral") reta a **capturar las 9 banderas** de archivos y rootear el sistema. Como en todo KoTH, el objetivo es hacerte con `/root/king.txt` (King) y defenderlo del resto de jugadores; el sistema de puntuación usa el servicio del puerto 9999.

## Solucionario

### Task 1: Capture the flags

**Explicación:** La tarea consiste en rootear la máquina y capturar las 9 flags distribuidas por el sistema (archivos). No hay campo de envío de respuestas con formato. Las 9 flags son archivos distribuidos por el sistema (formato `thm{...}`, **valores generados por instancia** — varían en cada despliegue). Ubicaciones verificadas por varios writeups:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Capture the flags | `No answer needed` |

---

**Metodología:**

### 1. Reconocimiento / Recon

`nmap -sV -p- <IP>` → **4 puertos abiertos** (coinciden todos los walkthroughs):

| Puerto / Port | Servicio / Service |
|---|---|
| 21/tcp | FTP `vsftpd` (login anónimo HABILITADO) |
| 22/tcp | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 |
| 80/tcp | HTTP Golang ("Ellingson Mineral Company") |
| 9999/tcp | **Servicio KoTH `king` (infraestructura — NO tocar)** |

Enumeración web: `/robots.txt` (*"Skiddies keep out... you WILL be arrested. - plague"* → filtra el usuario **plague**), `/backdoor` (login), `/staff`, `/news`, `/contact`, `/img`.

### 2. Vectores de intrusión (3 cuentas paralelas)

**Vector A — FTP anónimo → `rcampbell` (SSH):**
- Login anónimo: archivo `note` (filtra usuarios con contraseñas débiles) + `.flag` oculto en `/var/ftp`.
- `note` → `rcampbell` ("Weak password") y `gcrawford` ("Exposing crypto keys, weak password").
- Hydra FTP/SSH con rockyou → `rcampbell:<débil>`. SSH → `sudo -l` sin permisos → privesc por **capabilities** de python3.

**Vector B — FTP `gcrawford` → clave SSH cifrada → root vía `nano`:**
- Hydra FTP como `gcrawford` → contraseña débil. En su home: `.ssh/id_rsa` (cifrada) + `business.txt` (flag + notas).
- Crack de la clave con `ssh2john` + `john` (frase dinámica).
- SSH como `gcrawford` → `sudo -l`: `(root) /bin/nano /home/gcrawford/business.txt`.
- **PrivEsc con GTFOBins `nano`** → spawn de shell root.

**Vector C — Backdoor web → `plague` → `production` → root vía `openssl`:**
- Login en `/backdoor` (redirige a `/backdoor/shell`); HTML de `/staff` filtra comentario con el usuario `plague`.
- Hydra sobre `POST /api/login` (cadena de fallo `Incorrect`) → `plague:<débil>`.
- RCE restringida en `/backdoor/shell` → reverse shell como `plague` → persistencia SSH como **production**.
- `sudo -l` production: `(root) NOPASSWD: /usr/bin/openssl`.
- **PrivEsc con GTFOBins `openssl`**: compilar en local `shell.so` con `_init()` (`setuid(0); setgid(0); system("/bin/sh")`) y `sudo openssl req -engine ./shell.so -new` → root.

**PrivEsc general — capabilities de Python (cualquier usuario, clave rcampbell/gcrawford):**
- `getcap -r /` → `/usr/bin/python3.6 = cap_setuid+ep` (y `python3.6m`).
- Root: `python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'`.

### 3. KoTH — Convertirse en King

Con root: `echo "<TU_USUARIO_THM>" > /root/king.txt` → el servicio `:9999` (binario `koth` en `/root/`) lee ese archivo cada minuto y te da ~10 puntos por minuto de control. Defensa: `chattr +i`/`+a` sobre `/root/king.txt` (si `chattr` no existe, usar binario static busybox), loops de persistencia del king, y múltiples backdoors (claves SSH, shells SUID, usuario UID 0). Reglas: no tocar el servicio 9999, no borrar flags, no romper la máquina para los demás, autopwns baneados en partidas públicas. English: With root: `echo "<YOUR_THM_USERNAME>" > /root/king.txt` → the `:9999` service (`koth` binary in `/root/`) reads it every minute and credits ~10 points per minute held. Defense: `chattr +i`/`+a` on `/root/king.txt` (if `chattr` is missing, use a static busybox binary), king-persistence loops, and multiple backdoors (SSH keys, SUID shells, UID-0 user). Rules: do not touch the 9999 service, do not delete flags, do not break the box for others, autopwns banned in public games.

### 4. Banderas (9)

Las 9 flags son archivos distribuidos por el sistema (formato `thm{...}`, **valores generados por instancia** — varían en cada despliegue). Ubicaciones corroboradas por varios writeups:

| # | Ubicación / Location | Flag |
|---|---|---|
| 1 | `/var/ftp/.flag` (FTP anónimo) | `thm{...redacted...}` |
| 2 | `/home/rcampbell/.flag` | `thm{...redacted...}` |
| 3 | `/home/tryhackme/.flag` | `thm{...redacted...}` |
| 4 | `/home/production/.flag` | `thm{...redacted...}` |
| 5 | `/root/.flag` | `thm{...redacted...}` |
| 6 | `/home/gcrawford/business.txt` | `thm{...redacted...}` |
| 7 | `/home/production/webserver/resources/main.css` (comentario) | `thm{...redacted...}` |
| 8 | `/etc/vsftpd.conf` (comentario) | `thm{...redacted...}` |
| 9 | `/etc/ssh/sshd_config` (comentario) | `thm{...redacted...}` |

**Learning chain:** Recon (nmap -sV -p-): 21 FTP / 22 SSH / 80 HTTP / 9999 king → FTP anon → note (rcampbell/gcrawford) + Web /robots.txt + /staff → usuario plague → FTP anon + hydra → rcampbell → python3 cap_setuid+ep → root → HTTP hydra /api/login → plague → /backdoor/shell RCE → SSH production → sudo openssl (GTFOBins) → root → FTP gcrawford → id_rsa (ssh2john/john) → SSH → sudo nano (GTFOBins) → root → echo <alias> > /root/king.txt (King) → Defensa: chattr +i/+a, loops, backdoors

**Lección:** *KoTH exige velocista en ofensiva y guardia en defensa: múltiples vías de entrada (FTP, web, capabilities, sudo GTFOBins) y un mismo objetivo final — el fichero `king.txt`. Las flags son el "decorado" del reto; ganar es mantener el cerro.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1068 - Exploitation for Privilege Escalation; T1078 - Valid Accounts; T1105 - Ingress Tool Transfer; T1548 - Abuse Elevation Control Mechanism; T1222 - File and Directory Permissions Modification

**Fuente:** [TryHackMe - KoTH Hackers](https://tryhackme.com/room/kothhackers)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
