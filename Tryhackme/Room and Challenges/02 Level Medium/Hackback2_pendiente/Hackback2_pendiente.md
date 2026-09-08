# Hackback2

| **Dificultad** | MEDIUM | **Tipo** | CTF (Evento con premios) | **Slug** | `hackback2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hackback2) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Web Exploitation / Forensics / Networking / Reverse Engineering / Steganography / Scripting / OSINT | **Impacto** | Evalúa habilidades multidisciplinares de CTF: web, forense, redes, reversing, estego y OSINT |

---

**Contexto:** Con premios, entrevistas aceleradas, swag y £1,000 en juego, haz tu mejor esfuerzo para resolver tantos desafíos como sea posible. También hay recompensas para los equipos que aprendan algo nuevo. Cuanto más difícil sea la pregunta, más puntos obtienes. Creado por **ben tryhackme**. *With prizes, accelerated interviews, swag and £1,000 up for grabs, do your best to solve as many challenges as possible. There are also rewards for teams that learn something new! The harder the question, the more points you get.*

## Solucionario

### Task 1: Introducción

**Explicación:** Tareas de puesta en marcha del evento: unirse al Slack y Discord, ver el live stream mediante Google Hangouts y leer las reglas (romper una regla resulta en descalificación y/o baneo de HackBack y de la plataforma).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Join our Slack and Discord server! | `No answer needed` |
| 2 | Watch the live stream using the Google Hangouts link. | `No answer needed` |
| 3 | Read the rules. Breaking a rule will result in you being disqualified and/or banned from HackBack and the platform. | `No answer needed` |

### Task 2: [Easy] [Web Exploitation] Avengers Blog

**Explicación:** Desafío web con 5 flags guiadas por hints: cookies (`Mmm, cookies.`), response headers (`Response Headers.`), nmap, GoBuster & SQLi, y RCE.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is flag1? (Hint: Mmm, cookies.) | `cookie_secrets` |
| 2 | What is flag2? (Hint: Response Headers.) | `headers_are_important` |
| 3 | What is flag3? (Hint: nmap) | `8fc651a739befc58d450dc48e1f1fd2e` |
| 4 | What is flag4? (Hint: GoBuster & SQLi) | `sanitize_queries_mr_stark` |
| 5 | What is flag5? (Hint: RCE) | `d335e2d13f36558ba1e67969a1718af7` |

### Task 3: [Easy] [Forensics] Plaintext

**Explicación:** Forense de tráfico/red: identificar la IP remota a la que se conectó Bob, el primer comando que ejecutó, y localizar y crackear la contraseña de Tony (Hint: HashCat + rockyou).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the IP of the remote machine that Bob connected to? | `54.229.180.40` |
| 2 | What command did Bob first run? | `echo 'test' >> hackback123.txt` |
| 3 | Locate and crack Tony's password. What is his plaintext password? (Hint: HashCat + rockyou) | `password123` |

### Task 4: [Insane] [Networking] Borderlands

**Explicación:** Desafío de red multi-capa (AND*/APK, WEB*/webapp, GIT*/git, /var/www, /root router1, UDP, TCP) con flags en los protocolos de límites del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | AND*, APK | `ANDVOWLDLAS5Q8OQZ2tuIPGcOu2mXk` |
| 2 | WEB*, webapp | `WEBLhvOJAH8d50Z4y5G5g4McG1GMGD` |
| 3 | GIT*, git | `GITtFi80llzs4TxqMWtCotiTZpf0HC` |
| 4 | /var/www | `{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}` |
| 5 | /root router1 | `{FLAG:Router1:c877f00ce2b886446395150589166dcd}` |
| 6 | UDP | `{FLAG:UDP:3bb271d020df6cbe599a46d20e9fcb3c}` |
| 7 | TCP | `{FLAG:TCP:8fb04648d6b2bd40af6581942fcf483e}` |

### Task 5: [Easy] [Reverse Engineering] Dysfunctional Pointer

**Explicación:** Binario con puntero de función corrupto; patch de 4 bytes para llamar a `get_flag`. Hint: check the function pointer.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? (Hint: check the function pointer) | `684DAD9F` |

### Task 6: [Medium] [Reverse Engineering] Checks

**Explicación:** 4 checks en `main`; patch para llamar directo a la función del flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `88ED12AC` |

### Task 7: [Easy] [Networking] Sharing Is Caring

**Explicación:** Desafío de acceso remoto a archivos compartidos (SMB/NFS): responder qué servicio permite acceso remoto a archivos, el fichero con credenciales, el usuario, el contenido de user.txt, el path a manipular para root y el contenido de /root/root.txt. (Formato de respuestas indicado entre paréntesis.)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What service allows you remotely access files? | `[Pendiente]` (Formato: \*\*\*) |
| 2 | What is the name of the file that contains login details? | `[Pendiente]` (Formato: \*\*\*\*\*.\*\*\*) |
| 3 | What is the name of the user used to access the system? | `[Pendiente]` (Formato: \*\*\*\*) |
| 4 | What is in the user.txt file? | `[Pendiente]` (Formato: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*) |
| 5 | What is the full path of the file you need to manipulate to gain root access? | `[Pendiente]` (Formato: /\*\*\*/\*\*\*\*\*\*\*.\*\*) |
| 6 | What is the content of the /root/root.txt file? | `[Pendiente]` (Formato: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*) |

### Task 8: [Easy] [Forensics] E-Corp Takeover

**Explicación:** Forense de compromiso en Windows con preguntas sobre el momento del compromiso, IP del servidor de actualizaciones malicioso (Hint: local DNS cache), logon fallido de Emily (Hint: audit failure), último logon exitoso, comando de la tarea programada "GameOver", web shell backdoor, último comando de powershell y servidor C2 externo del atacante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When did the compromise take place? | `[Pendiente]` (Formato: \*\*/\*\*/\*\*\*\*) |
| 2 | IP of the malicious update server? (Hint: local DNS cache) | `[Pendiente]` (Formato: \*\*.\*.\*.\*) |
| 3 | When did Emily last attempt, but fail, to logon? (Hint: audit failure) | `[Pendiente]` (Formato: \*\*/\*\*/\*\*\*\* \*:\*\*:\*\* \*\*) |
| 4 | What user last successfully logged onto the machine? | `[Pendiente]` (Formato: \*\*\*\*) |
| 5 | What command (with arguments) is run from the scheduled task "GameOver"? | `[Pendiente]` |
| 6 | Whats the name of the web shell backdoor placed on the system? | `[Pendiente]` (Formato: \*\*\*\*\*.\*\*\*) |
| 7 | What was the last powershell command to run? | `[Pendiente]` |
| 8 | What was the attackers external control and command servers IP? | `[Pendiente]` (Formato: \*\*.\*\*.\*.\*) |

### Task 9: [Medium] [Steganography] Now you see me

**Explicación:** 7 flags de esteganografía con hints: exiftool/quien tomó la foto (reverse image search), entropía en GitHub CyberChef, diff de imágenes, mensaje con clave `key=hey iv=seed` ("Think outside the box..."). Pregunta 6: número de empleado cuando entró (Hint: reverse image search).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is flag 1? (Hint: Whoever took that photo?) | `5f4dcc3b5aa765d61d8327deb882cf99` |
| 2 | What is flag 2? (Hint: Entropy on GitHub CyberChef) | `2KCABKCAH` |
| 3 | What is flag 3? | `00a92932a4fd522632cc7a3315ac22c0` |
| 4 | What is flag 4? (Hint: diff) | `HarvardMarkI` |
| 5 | What is flag 5? | `August 11, 1950` |
| 6 | What was his employee number when he first joined? (Hint: reverse image search) | `7` |
| 7 | What is flag 7? Think outside the box... (Hint: key=hey iv=seed) | `[Pendiente]` (Formato: \*\*\*\*\*\*\*\*\*\*) |

### Task 10: [Hard] [Web & Networking] Cardboard

**Explicación:** Desafío web & networking con 5 flags. (Formatos de respuesta de 32 caracteres cada uno.)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is flag 1? | `[Pendiente]` |
| 2 | What is flag 2? | `[Pendiente]` |
| 3 | What is flag 3? | `[Pendiente]` |
| 4 | What is flag 4? | `[Pendiente]` |
| 5 | What is flag 5? | `[Pendiente]` |

### Task 11: [Medium] [Networking] Jack and The ELK Stalk

**Explicación:** Desafío de networking/ELK: encontrar la contraseña en la base de datos y leer el /root.txt.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the password in the database | `[Pendiente]` |
| 2 | Read the contents of the /root.txt file | `[Pendiente]` |

### Task 12: [Easy] [Scripting/Linux] Ninja Skills

**Explicación:** 6 preguntas de scripting/filtrado de archivos sobre 10 archivos con nombres aleatorios: dueño del grupo best-group, contenido con IP, hash SHA1 `9d54da7584015647ba052173b84d45e8007eba94`, archivo con 230 líneas, owner ID 502 y ejecutable por todos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which files are owned by the best-group group? | `D8B3 v2Vb` |
| 2 | Which of these files contain an IP address? | `oiMO` |
| 3 | Which file has the SHA1 hash 9d54da7584015647ba052173b84d45e8007eba94? | `c4ZX` |
| 4 | Which file contains 230 lines? | `bny0` |
| 5 | Which file's owner has an ID of 502? | `X1Uy` |
| 6 | Which file is executable by everyone? | `8V2L` |

### Task 13: [Easy] [Exploit] Credit Rating Shenanigans

**Explicación:** Comprometer la máquina para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compromise this machine yourself. What is the flag? | `[Pendiente]` |

### Task 14: [OSINT] Sometimes a little is a lot

**Explicación:** OSINT a partir del email `johnson.lola1992@gmail.com`: ubicación vacacional, año de nacimiento, ocupación, teléfono, tiempo en el trabajo actual, fecha de la captura y una mujer famosa en su página web (Hint: reverse image search).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Where has Lola gone on holiday? | `San Diego` |
| 2 | What her year of birth? | `1992` |
| 3 | Whats her occupation? | `Professional Photographer` |
| 4 | What phone does she have? | `iPhone X` |
| 5 | How long ago did she start her current job? | `5 years ago` |
| 6 | What is the date of the capture? | `Oct 23rd` |
| 7 | What famous woman does Lola have on her web page? (Hint: reverse image search) | `Ada Lovelace` |

### Task 15: [Medium] [Scripting] Very Secure Protocol

**Explicación:** Desafío de scripting/protocolo: recibir la cadena PRE-AUTH-CONF, crackear el PSK Hash y obtener la flag final del servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the PRE-AUTH-CONF string you receive? | `[Pendiente]` |
| 2 | What is value of the cracked PSK Hash? | `[Pendiente]` |
| 3 | What is the value of the final flag you received from the server? | `[Pendiente]` |

---

**Metodología:**
1. Introducción: unirse a los canales del evento (Slack/Discord), ver el live stream y leer las reglas.
2. Avengers Blog (Web): inspeccionar cookies, headers de respuesta, escaneo nmap, fuzzing GoBuster, SQLi y RCE.
3. Plaintext (Forensics): analizar capturas de red para IP remota, comandos y hashes crackeados con HashCat + rockyou.
4. Borderlands (Networking): pivoting multi-proto (AND/WEB/GIT/UDP/TCP) para recoger flags en rutas y routers.
5. Dysfunctional Pointer (RE): parchear un puntero de función corrupto (4 bytes) para llamar a `get_flag`.
6. Checks (RE): parchear los 4 checks de `main` para llamar directo a la función del flag.
7. Sharing Is Caring (Networking): enumerar servicios de compartición de archivos, extraer credenciales, escalar a root.
8. E-Corp Takeover (Forensics): timeline de compromiso, DNS cache, audit failures, tarea programada, web shell y C2.
9. Now you see me (Stego): exiftool, CyberChef entropía, diff, reverse image search y descifrado con key/iv.
10. Cardboard (Web & Networking): flags en infraestructura web/red.
11. Jack and The ELK Stalk (Networking): extraer password de BD y root.txt.
12. Ninja Skills (Scripting/Linux): filtrar archivos por grupo, contenido, hash, líneas, UID y permisos.
13. Credit Rating Shenanigans (Exploit): comprometer la máquina.
14. Sometimes a little is a lot (OSINT): investigar email de Lola con técnicas de OSINT/reconocimiento inverso de imágenes.
15. Very Secure Protocol (Scripting): protocolo seguro con PRE-AUTH-CONF, PSK hash y flag final.

**Learning chain:** Checklist del evento → Web (cookies/headers/nmap/gobuster/SQLi/RCE) → Forensics Redes → Borderlands multi-proto → Reversing (puntero + checks) → Networking SMB/NFS → Forensics Windows E-Corp → Steganografía → Web&Networking Cardboard → ELK/DB → Scripting Linux Ninja → Exploit → OSINT Lola → Protocolo seguro

**Lección:** *Un CTF multidisciplinar premia la gestión del tiempo y la cobertura amplia de técnicas: cookies, headers, nmap, SQLi, RCE, forense de red, parcheo de binarios, estego y OSINT. Cuanto más duro el reto, más puntos; pero la constancia en tareas fáciles también construye la base.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1046 - Network Service Discovery; T1059 - Command and Scripting Interpreter; T1003 - OS Credential Dumping; T1203 - Exploitation for Client Execution; T1568 - Dynamic Resolution

**Fuente:** [TryHackMe - Hackback2](https://tryhackme.com/room/hackback2)