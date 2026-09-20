# Overpass

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `overpass` | https://tryhackme.com/room/overpass | 01 Level Easy | TryHackMe | Enumeración web, GoBuster, cookie auth, ROT13/hashing casero, credenciales reutilizadas, SSH, cron jobs, escalada de privilegios | Compromiso total de la máquina: acceso por credenciales reutilizadas y escalada a root vía cron para leer user.txt y root.txt |

---

**Contexto:** Overpass es una máquina Linux dedicada a un "gestor de contraseñas" homónimo. Se enumera un sitio web estático, se manipula la cookie de sesión del panel de administración explotando su hash casero, se recuperan credenciales que permiten entrar por SSH y, finalmente, se abusa de un cron job que ejecuta un script como root para obtener una shell root y leer root.txt.

> **ES:** Enumerar el sitio (GoBuster), revisar el JavaScript del panel `/admin`, falsificar la cookie `SessionToken` con el hash del propio login.js, escalar validando el token, obtener credenciales SSH reutilizadas y, por último, explotar el cron de root que descarga y ejecuta un script para conseguir la shell de root.
> **EN:** Enumerate the site (GoBuster), review the JavaScript behind the `/admin` panel, forge the `SessionToken` cookie using the homemade hash, gather SSH credentials and reuse them, then abuse the root cron job that downloads and runs a script to obtain a root shell.

## Solucionario

### Task 1: Hackea la máquina / Hack the machine

**Explicación:** El flujo del challenge es el siguiente:

1. **Reconocimiento:** `nmap` muestra los puertos 22 (SSH) y 80 (HTTP). Un listado de directorios con GoBuster (`-u http://IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt,php`) revela `/admin`, `/downloads`, `/css` e `/img`.
2. **Análisis del panel `/admin`:** El login comprueba la contraseña desde el lado del servidor a través de `POST /api/login`, pero el JavaScript `login.js` implementa un "hash" casero basado en `rot()` (ROT13 extendido), `wordfreq()` y `sort()`, además de exponer la función de login. Como el hash no necesita crackearse para entrar, basta con calcular el token de sesión manualmente: se define `this_body` y se invoca `LoginRequest(this_body)` en la consola para que `checkLogin()` devuelva una `SessionToken` válida, o directamente se llama a `hash()` para construir la cookie.
3. **Obtención de credenciales:** Dentro del panel se descubre el archivo `jack.txt`, que deja las credenciales SSH del usuario `james` y su contraseña (una contraseña reutilizada desde el panel de administración).
4. **Acceso por SSH:** `ssh james@IP` con las credenciales recuperadas. En `/home/james/user.txt` está la flag de usuario, mientras que `buildscript.sh` en el directorio home es la puerta de escalada (los permisos permiten leer, pero el cron lo ejecuta como root).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Hack the machine and get the flag in user.txt | `thm{65c1aaf000506e56996822c6281e6bf7}` |

### Task 2: Escalada de privilegios / Escalating privileges

**Explicación:** Con la sesión de `james` se revisa `/etc/crontab` y se observa una tarea que cada minuto ejecuta `buildscript.sh` como **root**. El script hace `curl` de otro script alojado en el "build server" de Overpass (la IP estática del build server es la propia AttackBox de TryHackMe, `192.168.170.10`) y lo ejecuta. La táctica es sencilla: servir desde el AttackBox en el puerto 80 un `buildscript.sh` malicioso (p. ej., un reverse shell) y esperar a que el cron lo descargue y ejecute con privilegios. Al minuto siguiente se recibe una shell como root y se lee `/root/root.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escalate your privileges and get the flag in root.txt | `thm{7f336f8c359dbac18d54fdd64ea753bb}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Hack the machine and get the flag in user.txt | `thm{65c1aaf000506e56996822c6281e6bf7}` |
| 2 | Escalate your privileges and get the flag in root.txt | `thm{7f336f8c359dbac18d54fdd64ea753bb}` |

---

**Metodología:** Reconocimiento inicial de servicios (SSH/HTTP), enumeración de directorios con GoBuster, análisis de JavaScript del lado cliente para descubrir el algoritmo de autenticación, falsificación de la cookie de sesión (hash casero), recuperación de credenciales reutilizadas para pivote a SSH y, finalmente, abuso de permisos de cron locales para ejecutar código arbitrario como root mediante un servidor HTTP controlado.

### Cadena de ataque / Attack Chain

```text
nmap -> GoBuster (/admin) -> login.js (rot + wordfreq + sort) -> SessionToken falsificada -> /admin -> jack.txt (creds SSH james) -> SSH -> user.txt -> /etc/crontab (root cron curl buildscript.sh) -> reverse shell como root -> root.txt
```

**Learning chain:** active reconnaissance → directory brute forcing → client-side JavaScript analysis → authentication bypass (goat/homebrew hash) → credential reuse → lateral movement (SSH) → cron abuse → privilege escalation (root)

**Lección:** *Un algoritmo de hashing casero es un eslabón débil en la autoestima de la seguridad: si el cliente expone la lógica de autenticación, la "seguridad" del servidor es solo cosmética. Además, los cron jobs que descargan y ejecutan scripts remotos sin autenticación convierten cualquier ejecutable del home en una puerta a root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) → T1078 (Valid Accounts) → T1053.003 (Cron) → T1059.004 (Unix Shell)

**Fuente:** [TryHackMe - Overpass](https://tryhackme.com/room/overpass)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.