# Holo

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `hololive` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hololive) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | WordPress / LFI / RCE / MySQL / Docker / sshuttle / Covenant / mimikatz / PrintNightmare / NTLM Relay |
| **Impacto** | Cadena completa de extremo a extremo: WordPress (LFI/RCE), escape de contenedor Docker vía MySQL, pivoting con sshuttle, compromiso de servidores Windows con webshell y mimikatz, PC-FILESRV01 con PrintNightmare y dominio completo del DC por NTLM Relay. |

---

**Contexto:** Holo es una cadena completa: WordPress 5.5.3 con LFI en `img.php`, credenciales de admin, RCE en `dashboard.php`, escape de contenedor Docker vía MySQL, pivoting con sshuttle, compromiso de S-SRV01 (webshell + mimikatz), luego PC-FILESRV01 (AMSI/Defender, AppLocker, PrintNightmare) y finalmente DC-SRV01 vía NTLM Relay (SMB signing deshabilitado).

## Solucionario

### Task 1: Flag del contenedor

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found inside of the container? | `HOLO{175d7322f8fc53392a417ccde356c3fe}` |

### Task 2: Flag de usuario en L-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found after gaining user on L-SRV01? | `HOLO{3792d7d80c4dcabb8a533afddf06f666}` |

### Task 3: Flag de root en L-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found after rooting L-SRV01? | `HOLO{e16581b01d445a05adb2e6d45eb373f7}` |

### Task 4: Flag de la aplicación web en S-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found on the Web Application on S-SRV01? | `HOLO{bcfe3bcb8e6897018c63fbec660ff238}` |

### Task 5: Flag de root en S-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found after rooting S-SRV01? | `HOLO{50f9614809096ffe2d246e9dd21a76e1}` |

### Task 6: Flag de usuario en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found after gaining user on PC-FILESRV01? | `HOLO{2cb097ab8c412d565ec3cab49c6b082e}` |

### Task 7: Flag de root en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found after rooting PC-FILESRV01? | `HOLO{ee7e68a69829e56e1d5b4a73e7ffa5f0}` |

### Task 8: Flag de root en DC-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag can be found after rooting DC-SRV01? | `HOLO{29d166d973477c6d8b00ae1649ce3a44}` |

### Task 9: Último octeto del servidor web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the last octet of the IP address of the public-facing web server? | `33` |

### Task 10: Puertos abiertos del servidor web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many ports are open on the web server? | `3` |

### Task 11: CME en el puerto 80

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What CME is running on port 80 of the web server? | `WordPress` |

### Task 12: Versión del CME

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What version of the CME is running on port 80 of the web server? | `5.5.3` |

### Task 13: Título HTTP del servidor web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the HTTP title of the web server? | `holo.live` |

### Task 14: Dominios que cargan imágenes en la primera página

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What domains loads images on the first web page? | `www.holo.live` |

### Task 15: Los otros dos dominios del servidor web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the two other domains present on the web server? Format: Alphabetical Order | `admin.holo.live, dev.holo.live` |

### Task 16: Archivo que filtra el directorio actual

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file leaks the web server's current directory? | `robots.txt` |

### Task 17: Archivo que carga imágenes en el dominio de desarrollo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file loads images for the development domain? | `img.php` |

### Task 18: Ruta completa del archivo de credenciales

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full path of the credentials file on the administrator domain? | `/var/www/admin/supersecretdir/creds.txt` |

### Task 19: Archivo vulnerable a LFI en el dominio de desarrollo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file is vulnerable to LFI on the development domain? | `img.php` |

### Task 20: Parámetro vulnerable a LFI

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What parameter in the file is vulnerable to LFI? | `file` |

### Task 21: Archivo del leak que devuelve 403

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file found from the information leak returns an HTTP error code 403 on the administrator domain? | `/var/www/admin/supersecretdir/creds.txt` |

### Task 22: Credenciales leídas por LFI

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using LFI on the development domain read the above file. What are the credentials found from the file? | `admin:DBManagerLogin!` |

### Task 23: Archivo vulnerable a RCE en el dominio de administrador

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file is vulnerable to RCE on the administrator domain? | `dashboard.php` |

### Task 24: Parámetro vulnerable a RCE

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What parameter is vulnerable to RCE on the administrator domain? | `cmd` |

### Task 25: Usuario del servidor web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user is the web server running as? | `www-data` |

### Task 26: Gateway por defecto del contenedor Docker

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Default Gateway for the Docker Container? | `192.168.100.1` |

### Task 27: Puerto web alto del gateway

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the high web port open in the container gateway? | `8080` |

### Task 28: Puerto de base de datos bajo del gateway

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the low database port open in the container gateway? | `3306` |

### Task 29: Dirección del servidor de base de datos remota

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the server address of the remote database? | `192.168.100.1` |

### Task 30: Contraseña de la base de datos remota

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password of the remote database? | `!123SecureAdminDashboard321!` |

### Task 31: Nombre de usuario de la base de datos remota

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the username of the remote database? | `admin` |

### Task 32: Nombre de la base de datos remota

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the database name of the remote database? | `DashboardDB` |

### Task 33: Usuario encontrado dentro de la base de datos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What username can be found within the database itself? | `gurag` |

### Task 34: Usuario con el que corre la base de datos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user is the database running as? | `www-data` |

### Task 35: Ruta completa del binario SUID en L-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full path of the binary with an SUID bit set on L-SRV01? | `/usr/bin/docker` |

### Task 36: Primera línea del exploit del SUID

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full first line of the exploit for the SUID bit? | `sudo install -m =xs $(which docker) .` |

### Task 37: Usuario no por defecto en el shadow de L-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What non-default user can we find in the shadow file on L-SRV01? | `linux-admin` |

### Task 38: Contraseña en claro crackeada del hash

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the plaintext cracked password from the shadow hash? | `linuxrulez` |

### Task 39: Usuario controlado para el reset de contraseña en S-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user can we control for a password reset on S-SRV01? | `gurag` |

### Task 40: Cookie interceptada en S-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the cookie intercepted on S-SRV01? | `user_token` |

### Task 41: Tamaño de la cookie interceptada

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the size of the cookie intercepted on S-SRV01? | `110` |

### Task 42: Página de redirección tras el reset autenticado

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What page does the reset redirect you to when successfully authenticated on S-SRV01? | `reset.php` |

### Task 43: Usuario de dominio cuyas credenciales se vuelcan en S-SRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What domain user's credentials can we dump on S-SRV01? | `watamet` |

### Task 44: Contraseña del usuario de dominio

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the domain user's password that we can dump on S-SRV01? | `Nothingtoworry!` |

### Task 45: Hostname del endpoint remoto autenticable

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the hostname of the remote endpoint we can authenticate to? | `PC-FILESRV01` |

### Task 46: Producto anti-malware en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What anti-malware product is employed on PC-FILESRV01? | `AMSI` |

### Task 47: Producto anti-virus en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What anti-virus product is employed on PC-FILESRV01? | `Windows Defender` |

### Task 48: Versión de CLR en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What CLR version is installed on PC-FILESRV01? | `4.0.30319` |

### Task 49: Versión de PowerShell en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What PowerShell version is installed on PC-FILESRV01? | `5.1.17763.1` |

### Task 50: Build de Windows de PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Windows build is PC-FILESRV01 running on? | `17763.1577` |

### Task 51: Aplicación vulnerable encontrada en PC-FILESRV01

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the vulnerable application found on PC-FILESRV01? | `kavremover` |

### Task 52: Primera DLL vulnerable en la carpeta de Windows

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first listed vulnerable DLL located in the Windows folder from the application? | `wow64log.dll` |

### Task 53: Host con SMB signing deshabilitado

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What host has SMB signing disabled? | `DC-SRV01` |

---

**Metodología:**
1. Reconocimiento en `10.200.112.0/24`: servidor web público `10.200.112.33` (último octeto 33). `nmap -sV -sC -p-` → 3 puertos: `22` (SSH/OpenSSH), `80` (Apache) y `33060` (mysqlx).
2. En el puerto 80 corre WordPress `5.5.3` con título `holo.live`; fuzzing de vhosts (wfuzz) revela `www.holo.live`, `admin.holo.live` y `dev.holo.live`.
3. `www.holo.live` y `admin.holo.live` tienen `robots.txt`; el de admin filtra el directorio `/var/www` y un archivo de credenciales en `supersecretdir/creds.txt` (HTTP 403).
4. En `dev.holo.live`, `img.php?file=images/korone.jpg` es vulnerable a LFI (parámetro `file`); con traversal se lee `/etc/passwd` y el `creds.txt` de admin → `admin:DBManagerLogin!`.
5. Login en `admin.holo.live`; `dashboard.php` es vulnerable a RCE con el parámetro `cmd` (fuzzing con wfuzz) como usuario `www-data`.
6. Reverse shell (nc) → TTY interactivo; `ifconfig` muestra `192.168.100.100`, por lo que el gateway del contenedor es `192.168.100.1`; puertos abiertos: `22`, `80`, `3306` (BD) y `8080` (web).
7. `db_connect.php` da credenciales `admin:!123SecureAdminDashboard321!`; en MySQL, la BD `DashboardDB` contiene usuarios (`admin:DBManagerLogin!`, `gurag:AAAA`).
8. Docker Breakout: en MySQL se inyecta PHP (`select '<?php ...system($cmd);?>' INTO OUTFILE '/var/www/html/shell-sv.php'`) → RCE en `http://192.168.100.1:8080/shell-sv.php?cmd=` → reverse shell como `www-data` en el host → flag de usuario en L-SRV01.
9. Privesc en L-SRV01: `linpeas` detecta `/usr/bin/docker` con SUID → desde GTFObins `/usr/bin/docker run -v /:/mnt --rm -it ubuntu:18.04 chroot /mnt sh` → root → flag de root. En `/etc/shadow`, crackear `linux-admin` (mode `1800`) → `linuxrulez`.
10. Pivoting con sshuttle desde `linux-admin@10.200.112.33` a `10.200.112.0/24 -x 10.200.112.33`; ping sweep + barrido de puertos → hosts `10.200.112.30` (DC-SRV01), `.31` (S-SRV01) y `.35` (PC-FILESRV01).
11. C2 con Covenant; S-SRV01 (`10.200.112.31`) tiene reset de contraseña: el usuario `gurag` (de la BD) recibe el reset, la cookie `user_token` (tamaño 110) se filtra al cliente y con `?token` se redirige a `reset.php` → login `gurag:password123`.
12. En S-SRV01 hay una subida de imágenes con filtro del lado cliente; se bypasea con Burp y se sube un webshell PHP a `/images` → RCE como `system` → web flag en el escritorio de Admin.
13. AMSI/Windows Defender bloquean webshells simples; con un PHP alternativo se obtiene RCE; `mimikatz` (transferido con `certutil`) vuelca `watamet:Nothingtoworry!`. Con `crackmapexec` esas credenciales sirven en DC-SRV01, S-SRV01 y PC-FILESRV01.
14. Acceso a PC-FILESRV01 con `xfreerdp` como `watamet` → user flag en el escritorio; AppLocker restringe ejecución: el checker vía PowerShell revela directorios permitidos (`C:\Windows\Tasks`, etc.).
15. Situational awareness con `Seatbelt` y `PowerView`; `Find-LocalAdminAccess` indica que tenemos admin local en S-SRV01. (AMSI, Windows Defender, CLR `4.0.30319`, PowerShell `5.1.17763.1`, build `17763.1577`).
16. Privesc en PC-FILESRV01: `kavremover` con DLL hijacking falla → PrintNightmare (`CVE-2021-1675`) crea el usuario `sv` (Administradores) → shell con `evil-winrm` → root flag. La primera DLL vulnerable es `wow64log.dll`.
17. NTLM Relay final: `crackmapexec`/`nmap` confirman que `DC-SRV01` tiene SMB signing deshabilitado. Se desactivan los servicios SMB de PC-FILESRV01 y se reinicia; se lanza un payload meterpreter y `ntlmrelayx.py -t smb://10.200.112.30 -smb2support -socks`.
18. La sesión relay de S-SRV02 pasa por SOCKS (`proxychains`); con `smbexec.py -no-pass HOLOLIVE/SRV-ADMIN@10.200.112.30` se obtiene shell en DC-SRV01, se crea usuario admin y se ejecuta `secretsdump.py` → root flag en DC-SRV01.

**Learning chain:** `WordPress 5.5.3 (.33) → vhosts www/admin/dev → robots.txt → creds.txt (403) → LFI img.php (file) → admin:DBManagerLogin! → dashboard.php?cmd RCE (www-data) → reverse shell → contenedor Docker (gateway 192.168.100.1) → MySQL DashboardDB (admin:!123SecureAdminDashboard321!) → INTO OUTFILE webshell → Docker breakout → L-SRV01 user flag → /usr/bin/docker SUID → root L-SRV01 → shadow crack (linux-admin:linuxrulez) → sshuttle pivoting → S-SRV01 reset gurag/user_token → webshell flags → mimikatz (watamet:Nothingtoworry!) → xfreerdp PC-FILESRV01 → Seatbelt/PowerView → PrintNightmare (CVE-2021-1675) → root PC-FILESRV01 → wow64log.dll → NTLM Relay (SMB signing disabled en DC-SRV01) → smbexec → DC-SRV01 root flag`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts), T1003.001 (OS Credential Dumping: LSASS Memory), T1557 (Adversary-in-the-Middle), T1105 (Ingress Tool Transfer), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Holo](https://tryhackme.com/room/hololive)