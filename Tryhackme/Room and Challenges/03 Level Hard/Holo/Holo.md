# Holo [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF (Free)
* **Slug:** `hololive`
* **Link:** https://tryhackme.com/room/hololive
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** thmrevenant (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** Holo es una cadena completa: WordPress 5.5.3 con LFI en `img.php`, credenciales de admin, RCE en `dashboard.php`, escape de contenedor Docker vía MySQL, pivoting con sshuttle, compromiso de S-SRV01 (webshell + mimikatz), luego PC-FILESRV01 (AMSI/Defender, AppLocker, PrintNightmare) y finalmente DC-SRV01 vía NTLM Relay (SMB signing deshabilitado).
> **EN:** Holo is a full chain: WordPress 5.5.3 with LFI in `img.php`, admin credentials, RCE in `dashboard.php`, Docker breakout via MySQL, pivoting with sshuttle, compromise of S-SRV01 (webshell + mimikatz), then PC-FILESRV01 (AMSI/Defender, AppLocker, PrintNightmare) and finally DC-SRV01 via NTLM Relay (SMB signing disabled).

### Task 1 — Flag del contenedor / Flag inside the container

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found inside of the container? | `HOLO{175d7322f8fc53392a417ccde356c3fe}` |

### Task 2 — Flag de usuario en L-SRV01 / User flag on L-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found after gaining user on L-SRV01? | `HOLO{3792d7d80c4dcabb8a533afddf06f666}` |

### Task 3 — Flag de root en L-SRV01 / Root flag on L-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found after rooting L-SRV01? | `HOLO{e16581b01d445a05adb2e6d45eb373f7}` |

### Task 4 — Flag de la aplicación web en S-SRV01 / Web Application flag on S-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found on the Web Application on S-SRV01? | `HOLO{bcfe3bcb8e6897018c63fbec660ff238}` |

### Task 5 — Flag de root en S-SRV01 / Root flag on S-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found after rooting S-SRV01? | `HOLO{50f9614809096ffe2d246e9dd21a76e1}` |

### Task 6 — Flag de usuario en PC-FILESRV01 / User flag on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found after gaining user on PC-FILESRV01? | `HOLO{2cb097ab8c412d565ec3cab49c6b082e}` |

### Task 7 — Flag de root en PC-FILESRV01 / Root flag on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found after rooting PC-FILESRV01? | `HOLO{ee7e68a69829e56e1d5b4a73e7ffa5f0}` |

### Task 8 — Flag de root en DC-SRV01 / Root flag on DC-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag can be found after rooting DC-SRV01? | `HOLO{29d166d973477c6d8b00ae1649ce3a44}` |

### Task 9 — Último octeto del servidor web / Last octet of the web server

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the last octet of the IP address of the public-facing web server? | `33` |

### Task 10 — Puertos abiertos del servidor web / Open ports on the web server

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many ports are open on the web server? | `3` |

### Task 11 — CME en el puerto 80 / CME on port 80

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What CME is running on port 80 of the web server? | `WordPress` |

### Task 12 — Versión del CME / Version of the CME

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What version of the CME is running on port 80 of the web server? | `5.5.3` |

### Task 13 — Título HTTP del servidor web / HTTP title of the web server

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the HTTP title of the web server? | `holo.live` |

### Task 14 — Dominios que cargan imágenes en la primera página / Domains that load images on the first page

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What domains loads images on the first web page? | `www.holo.live` |

### Task 15 — Los otros dos dominios del servidor web / The two other domains on the web server

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What are the two other domains present on the web server? Format: Alphabetical Order | `admin.holo.live, dev.holo.live` |

### Task 16 — Archivo que filtra el directorio actual / File that leaks the web server's current directory

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What file leaks the web server's current directory? | `robots.txt` |

### Task 17 — Archivo que carga imágenes en el dominio de desarrollo / File that loads images on the dev domain

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What file loads images for the development domain? | `img.php` |

### Task 18 — Ruta completa del archivo de credenciales / Full path of the credentials file

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the full path of the credentials file on the administrator domain? | `/var/www/admin/supersecretdir/creds.txt` |

### Task 19 — Archivo vulnerable a LFI en el dominio de desarrollo / File vulnerable to LFI on the dev domain

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What file is vulnerable to LFI on the development domain? | `img.php` |

### Task 20 — Parámetro vulnerable a LFI / Parameter vulnerable to LFI

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What parameter in the file is vulnerable to LFI? | `file` |

### Task 21 — Archivo del leak que devuelve 403 / Leaked file returning HTTP 403

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What file found from the information leak returns an HTTP error code 403 on the administrator domain? | `/var/www/admin/supersecretdir/creds.txt` |

### Task 22 — Credenciales leídas por LFI / Credentials read via LFI

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Using LFI on the development domain read the above file. What are the credentials found from the file? | `admin:DBManagerLogin!` |

### Task 23 — Archivo vulnerable a RCE en el dominio de administrador / File vulnerable to RCE on the admin domain

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What file is vulnerable to RCE on the administrator domain? | `dashboard.php` |

### Task 24 — Parámetro vulnerable a RCE / Parameter vulnerable to RCE

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What parameter is vulnerable to RCE on the administrator domain? | `cmd` |

### Task 25 — Usuario del servidor web / User the web server runs as

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What user is the web server running as? | `www-data` |

### Task 26 — Gateway por defecto del contenedor Docker / Default Gateway of the Docker Container

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the Default Gateway for the Docker Container? | `192.168.100.1` |

### Task 27 — Puerto web alto del gateway / High web port on the container gateway

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the high web port open in the container gateway? | `8080` |

### Task 28 — Puerto de base de datos bajo del gateway / Low database port on the container gateway

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the low database port open in the container gateway? | `3306` |

### Task 29 — Dirección del servidor de base de datos remota / Server address of the remote database

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the server address of the remote database? | `192.168.100.1` |

### Task 30 — Contraseña de la base de datos remota / Password of the remote database

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the password of the remote database? | `!123SecureAdminDashboard321!` |

### Task 31 — Nombre de usuario de la base de datos remota / Username of the remote database

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the username of the remote database? | `admin` |

### Task 32 — Nombre de la base de datos remota / Name of the remote database

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the database name of the remote database? | `DashboardDB` |

### Task 33 — Usuario encontrado dentro de la base de datos / Username found within the database

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What username can be found within the database itself? | `gurag` |

### Task 34 — Usuario con el que corre la base de datos / User the database runs as

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What user is the database running as? | `www-data` |

### Task 35 — Ruta completa del binario SUID en L-SRV01 / Full path of the SUID binary on L-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the full path of the binary with an SUID bit set on L-SRV01? | `/usr/bin/docker` |

### Task 36 — Primera línea del exploit del SUID / Full first line of the SUID exploit

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the full first line of the exploit for the SUID bit? | `sudo install -m =xs $(which docker) .` |

### Task 37 — Usuario no por defecto en el shadow de L-SRV01 / Non-default user in the shadow file on L-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What non-default user can we find in the shadow file on L-SRV01? | `linux-admin` |

### Task 38 — Contraseña en claro crackeada del hash / Plaintext cracked password from the shadow hash

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the plaintext cracked password from the shadow hash? | `linuxrulez` |

### Task 39 — Usuario controlado para el reset de contraseña en S-SRV01 / User we can control for password reset on S-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What user can we control for a password reset on S-SRV01? | `gurag` |

### Task 40 — Cookie interceptada en S-SRV01 / Cookie intercepted on S-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the cookie intercepted on S-SRV01? | `user_token` |

### Task 41 — Tamaño de la cookie interceptada / Size of the cookie intercepted

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the size of the cookie intercepted on S-SRV01? | `110` |

### Task 42 — Página de redirección tras el reset autenticado / Reset redirect page when successfully authenticated

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What page does the reset redirect you to when successfully authenticated on S-SRV01? | `reset.php` |

### Task 43 — Usuario de dominio cuyas credenciales se vuelcan en S-SRV01 / Domain user whose credentials we can dump on S-SRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What domain user's credentials can we dump on S-SRV01? | `watamet` |

### Task 44 — Contraseña del usuario de dominio / Domain user's password we can dump

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the domain user's password that we can dump on S-SRV01? | `Nothingtoworry!` |

### Task 45 — Hostname del endpoint remoto autenticable / Hostname of the remote endpoint we can authenticate to

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the hostname of the remote endpoint we can authenticate to? | `PC-FILESRV01` |

### Task 46 — Producto anti-malware en PC-FILESRV01 / Anti-malware product on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What anti-malware product is employed on PC-FILESRV01? | `AMSI` |

### Task 47 — Producto anti-virus en PC-FILESRV01 / Anti-virus product on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What anti-virus product is employed on PC-FILESRV01? | `Windows Defender` |

### Task 48 — Versión de CLR en PC-FILESRV01 / CLR version installed on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What CLR version is installed on PC-FILESRV01? | `4.0.30319` |

### Task 49 — Versión de PowerShell en PC-FILESRV01 / PowerShell version on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What PowerShell version is installed on PC-FILESRV01? | `5.1.17763.1` |

### Task 50 — Build de Windows de PC-FILESRV01 / Windows build of PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What Windows build is PC-FILESRV01 running on? | `17763.1577` |

### Task 51 — Aplicación vulnerable encontrada en PC-FILESRV01 / Vulnerable application found on PC-FILESRV01

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the vulnerable application found on PC-FILESRV01? | `kavremover` |

### Task 52 — Primera DLL vulnerable en la carpeta de Windows / First vulnerable DLL in the Windows folder

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the first listed vulnerable DLL located in the Windows folder from the application? | `wow64log.dll` |

### Task 53 — Host con SMB signing deshabilitado / Host with SMB signing disabled

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What host has SMB signing disabled? | `DC-SRV01` |

## Metodología / Methodology

1. **Paso / Step:** Reconocimiento en `10.200.112.0/24`: servidor web público `10.200.112.33` (último octeto 33). `nmap -sV -sC -p-` → 3 puertos: `22` (SSH/OpenSSH), `80` (Apache) y `33060` (mysqlx).
2. **Paso / Step:** En el puerto 80 corre WordPress `5.5.3` con título `holo.live`; fuzzing de vhosts (wfuzz) revela `www.holo.live`, `admin.holo.live` y `dev.holo.live`.
3. **Paso / Step:** `www.holo.live` y `admin.holo.live` tienen `robots.txt`; el de admin filtra el directorio `/var/www` y un archivo de credenciales en `supersecretdir/creds.txt` (HTTP 403).
4. **Paso / Step:** En `dev.holo.live`, `img.php?file=images/korone.jpg` es vulnerable a LFI (parámetro `file`); con traversal se lee `/etc/passwd` y el `creds.txt` de admin → `admin:DBManagerLogin!`.
5. **Paso / Step:** Login en `admin.holo.live`; `dashboard.php` es vulnerable a RCE con el parámetro `cmd` (fuzzing con wfuzz) como usuario `www-data`.
6. **Paso / Step:** Reverse shell (nc) → TTY interactivo; `ifconfig` muestra `192.168.100.100`, por lo que el gateway del contenedor es `192.168.100.1`; puertos abiertos: `22`, `80`, `3306` (BD) y `8080` (web).
7. **Paso / Step:** `db_connect.php` da credenciales `admin:!123SecureAdminDashboard321!`; en MySQL, la BD `DashboardDB` contiene usuarios (`admin:DBManagerLogin!`, `gurag:AAAA`).
8. **Paso / Step:** Docker Breakout: en MySQL se inyecta PHP (`select '<?php ...system($cmd);?>' INTO OUTFILE '/var/www/html/shell-sv.php'`) → RCE en `http://192.168.100.1:8080/shell-sv.php?cmd=` → reverse shell como `www-data` en el host → flag de usuario en L-SRV01.
9. **Paso / Step:** Privesc en L-SRV01: `linpeas` detecta `/usr/bin/docker` con SUID → desde GTFObins `/usr/bin/docker run -v /:/mnt --rm -it ubuntu:18.04 chroot /mnt sh` → root → flag de root. En `/etc/shadow`, crackear `linux-admin` (mode `1800`) → `linuxrulez`.
10. **Paso / Step:** Pivoting con sshuttle desde `linux-admin@10.200.112.33` a `10.200.112.0/24 -x 10.200.112.33`; ping sweep + barrido de puertos → hosts `10.200.112.30` (DC-SRV01), `.31` (S-SRV01) y `.35` (PC-FILESRV01).
11. **Paso / Step:** C2 con Covenant; S-SRV01 (`10.200.112.31`) tiene reset de contraseña: el usuario `gurag` (de la BD) recibe el reset, la cookie `user_token` (tamaño 110) se filtra al cliente y con `?token` se redirige a `reset.php` → login `gurag:password123`.
12. **Paso / Step:** En S-SRV01 hay una subida de imágenes con filtro del lado cliente; se bypasea con Burp y se sube un webshell PHP a `/images` → RCE como `system` → web flag en el escritorio de Admin.
13. **Paso / Step:** AMSI/Windows Defender bloquean webshells simples; con un PHP alternativo se obtiene RCE; `mimikatz` (transferido con `certutil`) vuelca `watamet:Nothingtoworry!`. Con `crackmapexec` esas credenciales sirven en DC-SRV01, S-SRV01 y PC-FILESRV01.
14. **Paso / Step:** Acceso a PC-FILESRV01 con `xfreerdp` como `watamet` → user flag en el escritorio; AppLocker restringe ejecución: el checker vía PowerShell revela directorios permitidos (`C:\Windows\Tasks`, etc.).
15. **Paso / Step:** Situational awareness con `Seatbelt` y `PowerView`; `Find-LocalAdminAccess` indica que tenemos admin local en S-SRV01. (`AMSI`, `Windows Defender`, CLR `4.0.30319`, PowerShell `5.1.17763.1`, build `17763.1577`).
16. **Paso / Step:** Privesc en PC-FILESRV01: `kavremover` con DLL hijacking falla → PrintNightmare (`CVE-2021-1675`) crea el usuario `sv` (Administradores) → shell con `evil-winrm` → root flag. La primera DLL vulnerable es `wow64log.dll`.
17. **Paso / Step:** NTLM Relay final: `crackmapexec`/`nmap` confirman que `DC-SRV01` tiene SMB signing deshabilitado. Se desactivan los servicios SMB de PC-FILESRV01 y se reinicia; se lanza un payload meterpreter y `ntlmrelayx.py -t smb://10.200.112.30 -smb2support -socks`.
18. **Paso / Step:** La sesión relay de S-SRV02 pasa por SOCKS (`proxychains`); con `smbexec.py -no-pass HOLOLIVE/SRV-ADMIN@10.200.112.30` se obtiene shell en DC-SRV01, se crea usuario admin y se ejecuta `secretsdump.py` → root flag en DC-SRV01.

### Cadena de ataque / Attack Chain

```
WordPress 5.5.3 (.33) -> vhosts www/admin/dev -> robots.txt -> creds.txt (403) -> LFI img.php (file) -> admin:DBManagerLogin! -> dashboard.php?cmd RCE (www-data) -> reverse shell -> contenedor Docker (gateway 192.168.100.1) -> MySQL DashboardDB (admin:!123SecureAdminDashboard321!) -> INTO OUTFILE webshell -> Docker breakout -> L-SRV01 user flag -> /usr/bin/docker SUID -> root L-SRV01 -> shadow crack (linux-admin:linuxrulez) -> sshuttle pivoting -> S-SRV01 reset gurag/user_token -> webshell flags -> mimikatz (watamet:Nothingtoworry!) -> xfreerdp PC-FILESRV01 -> Seatbelt/PowerView -> PrintNightmare (CVE-2021-1675) -> root PC-FILESRV01 -> wow64log.dll -> NTLM Relay (SMB signing disabled en DC-SRV01) -> smbexec -> DC-SRV01 root flag
```

**Lección:** Holo es una cadena de extremo a extremo que combina web (LFI/RCE), contenedores (Docker breakout por MySQL), pivoting (sshuttle), seguridad de Windows (AMSI/Defender, AppLocker), exploits (PrintNightmare, CVE-2021-1675) y dominio (NTLM Relay contra SMB signing deshabilitado).

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.