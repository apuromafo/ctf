# Python Playground

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `pythonplayground` | [TryHackMe](https://tryhackme.com/room/pythonplayground) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=pythonplayground` + websearch de walkthroughs) | Node Express / Python Sandbox (RCE) / Reverse shell / Docker (volumes /var/log→/mnt/log) / Hash JS (sha256) / SUID sh / SSH | A través de un sandbox de Python embebido en Node se escapa del sandbox (RCE), se crackea el hash JavaScript del usuario Connor para acceder por SSH a un contenedor y se escala a root con un binario SUID montado desde el host (/var/log → /mnt/log). |

---

**Contexto:**

> **ES:** **Python Playground** es un CTF Hard web. La máquina expone un "Python Playground": un servicio Node (Express) que ejecuta código Python enviado por el usuario dentro de un sandbox. La primera fase es escapar del sandbox aprovechando que hooks como `__import__` no están sanamente restringidos y conseguir ejecución de comandos arbitrarios en el contenedor (`flag 1`). En la segunda fase se crackea el hash JavaScript de la contraseña de `connor` y con el password (`spaghetti1245`) se conecta por SSH al host: un volumen Docker monta `/var/log` del host en `/mnt/log` del contenedor, y dentro se encuentra un binario `sh` con bit SUID → `./sh -p` → root → `flag 2` y `flag 3`.
> **EN:** **Python Playground** is a Hard web CTF. The machine exposes a "Python Playground": a Node (Express) service that runs user-submitted Python code inside a sandbox. The first phase is escaping the sandbox by taking advantage of hooks such as `__import__` not being safely restricted and achieving arbitrary command execution inside the container (`flag 1`). In the second phase the JavaScript hash of `connor`'s password is cracked and with that password (`spaghetti1245`) SSH access to the host is gained: a Docker volume mounts the host's `/var/log` into the container's `/mnt/log`, and inside there is an `sh` binary with the SUID bit → `./sh -p` → root → `flag 2` and `flag 3`.

---

## Solucionario

### Task 1: Hack the machine / Piratea la máquina

**Explicación:**
Completando las tres fases (escape del sandbox Python a un contenedor, crackeo del hash JS de connor + SSH, y escalada vía el binario SUID del volumen montado) se obtienen las tres flags.

1. 1. THM{7e0b5cf043975e3c104a458a8d4f6f2f}
   2. THM{69a36d6f9da10d23ca0dbfdf6e691ec5}
   3. THM{be3adc69c25ad14eb79da4eb57925ad1}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | 1. What is flag 1? | `THM{7e0b5cf043975e3c104a458a8d4f6f2f}` |
| 1 | 2. What is flag 2? | `THM{69a36d6f9da10d23ca0dbfdf6e691ec5}` |
| 1 | 3. What is flag 3? | `THM{be3adc69c25ad14eb79da4eb57925ad1}` |

---

**Metodología:**

1. Reconocimiento: `nmap` → puerto 80 (servicio "Python Playground") y SSH (22). La web permite ejecutar `print(locals())`, `dir()`, etc. para inspeccionar el entorno.
2. Escaneo del sandbox: probando payloads se ve que se llama a un ejecutable/sandbox propio; funciones como `exec`, `open`, `os` están "bloqueadas" pero hay hooks accesibles en el entorno (`__builtins__`, `__import__`).
3. Escape del sandbox → RCE: payload tipo `__import__('os').system('id')` — o variantes vía `().__class__.__bases__[0].__subclasses__()` para llegar a `os.system`/subprocess — consiguen ejecutar comandos en el contenedor donde corre el playground → reverse shell (bash/python) → **flag 1** en el contenedor.
4. Enumeración del contenedor: variables de entorno, `/mnt` y el árbol. Se encuentran los ficheros de la app y el usuario `connor` con su hash JavaScript (formato `sha256:`/PBKDF2 del entorno JS) en configuración/base.
5. Crackeo del hash JS: se extrae el hash y se crackea con john/hashcat (modo con formato JS) → password de `connor`: `spaghetti1245`.
6. SSH como connor: `ssh connor@<IP>` → flag 2 en el home del usuario. Tambien se observa el volumen montado `/mnt/log`.
7. Escalada a root vía SUID: en `/mnt/log` (montaje del `/var/log` del host) se inspeccionan los bins del sistema nodrizado: existe un binario `sh` con SUID (`-rwsr-xr-x root root`) → `cd /mnt/log && ./sh -p` (o copiar a /tmp) → shell con euid root → leer `flag 3` (root.txt).

### Cadena de ataque / Attack Chain

`nmap → Python Playground (Node+Express sandbox) → Enumeración del sandbox (dir()/locals()) → Bypass con __import__/subclasses → RCE en contenedor → Reverse shell → flag 1 → Enumeración (connor + hash JS) → Crack hash (john) → spaghetti1245 → SSH connor → flag 2 → /mnt/log = /var/log host (volumen docker) → sh SUID → ./sh -p → root → flag 3`

**Learning chain:**

Análisis de entorno de ejecución (playground) → Inspección de objetos/builtins en Python → Python sandbox escape (obtener módulo os/subprocess) → RCE dentro de contenedor → Enumeración de credenciales en ficheros → Cracking de hashes de frameworks JS → Acceso SSH → Deploy de contenedores con volúmenes host → Abuso de binarios SUID dentro del montaje → root.

*Lección:* Un "sandbox" de Python hecho con desmontajes superficiales de `__builtins__` se rompe con mirar dos capas más abajo (`.__class__.__bases__[0].__subclasses__()`). Y los volúmenes Docker son superficies de ataque: un binario SUID del host expuesto dentro del contenedor convierte el propio montaje en el vector de escalada privilegiada.

**MITRE ATT&CK:**

T1059.007 (Command and Scripting Interpreter: JavaScript), T1505.003 (Web Shell: Server Software), T1068 (Exploitation for Privilege Escalation), T1110 (Brute Force), T1071.001 (Application Layer Protocol: Web Protocols), T1548.001 (Abuse Elevation Control Mechanism: Setuid and Setgid)

**Fuente:** [TryHackMe - Python Playground](https://tryhackme.com/room/pythonplayground)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.