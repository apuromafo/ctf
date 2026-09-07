# Advent of Cyber 1 [2019]

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `25daysofchristmas` |
| **Link** | [TryHackMe](https://tryhackme.com/room/25daysofchristmas) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | CyberChef / Wireshark / Hydra / Ghidra / Elasticsearch (ELK) / sqlmap / Nmap |
| **Impacto** | Primera edición del Advent of Cyber: 24 días de retos navideños por web, OSINT, Linux, SQLi, forense y escalada de privilegios. |

---

**Contexto:** Edición inaugural (2019) del Advent of Cyber. Durante 24 días, una comunidad de fans de Santa contrarresta al Grinch con tareas guiadas: manipulación de cookies, descubrimiento de directorios y credenciales por defecto, análisis de PCAPs, bases del sistema Linux con entrenamiento de comandos, OSINT con imágenes, exfiltración de datos, binarios SUID, Metasploit, enumeración de apps web (JSON), cifrado/descifrado, una máquina retro, buckets S3, LFI, juegos web, Hydra, ejecutables ELF con JavaScript, comandos de Linux, escalada por cronjobs, ingeniería inversa, lógica, inyección SQL y análisis en ELK. El dump mantiene la numeración original de las respuestas.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Cómo unirse

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Únete al Discord/canal del evento. | `No answer needed` |
| 2 | Configura tu perfil para el evento. | `No answer needed` |

### Task 3: Historia de fondo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia y el calendario del evento. | `No answer needed` |

### Task 4: Preparación

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Activa la máquina de tu primera tarea. | `No answer needed` |
| 2 | Comprueba que puedes acceder a la VPN/AttackBox. | `No answer needed` |

### Task 5: Despliegue

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina objetivo del día. | `No answer needed` |

### Task 6: Día 1 - Inventory Management

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de la cookie utilizada para la autenticación? | `authid` |
| 2 | Si decodificas la cookie, ¿cuál es el valor de la parte fija? | `v4er9ll1!ss` |
| 3 | Tras iniciar sesión, ¿qué pidió el usuario mcinventory? | `firewall` |

### Task 7: Día 2 - Arctic Forum

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del directorio oculto que encuentras en el servidor web? | `/sysadmin` |
| 2 | ¿Cuál es la contraseña por defecto de la cuenta de administración? | `defaultpass` |
| 3 | ¿Qué valor/palabra de contraseña se revela tras el acceso al foro? | `Eggnog` |

### Task 8: Día 3 - Evil Elf

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Desde qué dirección IP se originó la petición maliciosa? | `63.32.89.195` |
| 2 | ¿Qué producto/consola buscaba el usuario comprometido? | `ps4` |
| 3 | ¿Cuál es la contraseña que se detectó en la actividad? | `rainbow` |

### Task 9: Día 4 - Training (Linux)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos archivos hay en el directorio? | `8` |
| 2 | ¿Cuál es el nombre del directorio donde se encuentran? | `recipes` |
| 3 | ¿Qué archivo contiene la dirección IP? | `file6` |
| 4 | ¿Cuál es la dirección IP que aparece en ese archivo? | `10.0.0.05` |
| 5 | ¿Cuántos usuarios pueden iniciar sesión con shell bash? | `3` |
| 6 | ¿Cuál es el hash SHA1 del archivo 8? | `fa67ee594358d83becdd2cb6c466b25320fd2835` |
| 7 | ¿Cuál es el hash de contraseña (crypt/sha512) del usuario mcsysadmin? | `$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/` |

### Task 10: Día 5 - Ho-Ho-Hosint

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fecha aparece en los datos de la imagen? | `December 29, 1900` |
| 2 | ¿Cómo se llama el recurso/imagen analizado? | `Santa's Helper` |
| 3 | ¿Qué modelo de teléfono aparece en la imagen? | `iPhone X` |
| 4 | ¿Qué fecha de creación/mensaje se muestra en los metadatos? | `23/10/2014` |
| 5 | ¿Cuál es el nombre de la autoría/firma indicada por la imagen? | `ada lovelace` |

### Task 11: Día 6 - Data Elf-iltration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del archivo/dato que se está exfiltando? | `Candy Cane Serial Number 8491` |
| 2 | ¿Qué herramienta/perfil se identifica en los registros del incidente? | `PenTester` |
| 3 | ¿Qué referencia/estándar se indica en el documento relacionado? | `RFC527` |

### Task 12: Día 7 - Skilling Up

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos resultados/carpetas de interés hay en el objetivo? | `3` |
| 2 | ¿Qué sistema operativo ejecuta el servidor de pruebas? | `Linux` |
| 3 | ¿Cuál es la versión del servicio/sistema detectado? | `7.4` |
| 4 | ¿Cómo se llama el archivo interesante que encuentras? | `interesting.file` |

### Task 13: Día 8 - SUID Shenanigans

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el UID del usuario 'nobody' listado en /etc/passwd? | `65534` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{d3f0708bdd9accda7f937d013eaf2cd8}` |
| 3 | ¿Cuál es el contenido de la segunda flag? | `THM{8c8211826239d849fa8d6df03749c3a2}` |

### Task 14: Día 9 - Metasploit-a-ho-ho-ho

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el payload/archivo que genera la sala para ganar acceso? | `sCrIPtKiDd` |

### Task 15: Día 10 - Elf Applications

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag que obtienes de la aplicación? | `THM{3ad96bb13ec963a5ca4cb99302b37e12}` |
| 2 | ¿Cuál es la contraseña encontrada en el flujo del reto? | `rudolphrednosedreindeer` |
| 3 | ¿Cuál es el primer nombre de empleado sospechoso? | `Melisa Vanhoose` |
| 4 | ¿Cuál es el segundo nombre de empleado implicado? | `Lindsey Gaffney` |

### Task 16: Día 11 - Elfcryption

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña utilizada para proteger la primera parte? | `securepassword123` |
| 2 | ¿Cuál es el nombre del archivo que debes descifrar? | `file.txt` |
| 3 | ¿Cuál es la contraseña de la segunda parte del reto? | `bestpassword` |

### Task 17: Día 12 - Santa's Grotto (cifrado)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash MD5 generado por la herramienta del reto? | `24cf615e2a4f42718f2ff36b35614f8f` |
| 2 | ¿Cuál es el nombre de la ubicación/carpeta clave del reto? | `Santa's Grotto` |
| 3 | ¿Cuál es la flag del reto? | `THM{ed9ccb6802c5d0f905ea747a310bba23}` |

### Task 18: Día 13 - Retro

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿A qué directorio apunta la pista de la consola retro? | `/retro` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{HACK_PLAYER_ONE}` |
| 3 | ¿Cuál es el contenido de la segunda flag (relacionada con la máquina recreativa)? | `THM{COIN_OPERATED_EXPLOITATION}` |

### Task 19: Día 14 - Unknown Storage (S3)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el archivo que encuentras en el bucket de almacenamiento? | `employee_names.txt` |
| 2 | ¿Qué usuario se puede deducir a partir de ese archivo? | `mcchef` |

### Task 20: Día 15 - LFI

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué contraseña/palabra clave aparece en los archivos accesibles por LFI? | `Hawaii` |
| 2 | ¿Con qué credencial puedes autenticarte en el servicio? | `password1` |
| 3 | ¿Cuál es la flag del reto? | `THM{4ea2adf842713ad3ce0c1f05ef12256d}` |

### Task 21: Día 16 - File Confusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué número aparece como respuesta de la primera parte del juego? | `50` |
| 2 | ¿Qué número se muestra en la segunda parte? | `3` |
| 3 | ¿Cómo se llama el archivo que permite completar el reto? | `dL6w.txt` |

### Task 22: Día 17 - Hydra-ha-ha-haa

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el contenido de la primera flag? | `THM{2673a7dd116de68e85c48ec0b1f2612e}` |
| 2 | ¿Cuál es el contenido de la segunda flag? | `THM{c8eeb0468febbadea859baeb33b2541b}` |

### Task 23: Día 18 - ELF JavaScript

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash SHA256 del binario ELF/JS analizado? | `2564799a4e6689972f6d9e1c7b406f87065cbf65` |

### Task 24: Día 19 - Commands

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el código de verificación que se te pide tras ejecutar los comandos? | `5W7WkjxBWwhe3RNsWJ3Q` |

### Task 25: Día 20 - Cronjob Privilege Escalation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto/servicio clave se aprovecha en el cronjob para escalar? | `4567` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{dec4389bc09669650f3479334532aeab}` |
| 3 | ¿Cuál es el contenido de la segunda flag? | `THM{b27d33705f97ba2e1f444ec2da5f5f61}` |

### Task 26: Día 21 - Reverse Elf-ineering

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de local_ch en la primera instrucción analizada? | `1` |
| 2 | ¿Cuál es el valor de eax en la instrucción imull? | `6` |
| 3 | ¿Cuál es el valor de local_4h antes de que eax se ponga a 0? | `6` |

### Task 27: Día 22 - If Santa, Then Christmas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Según el código/condición del reto, ¿cuál es la primera respuesta? | `9` |
| 2 | ¿Cuál es la segunda respuesta del reto? | `2` |

### Task 28: Día 23 - LapLANd (SQL Injection)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del campo vulnerable a la inyección SQL? | `log_email` |
| 2 | ¿Cuál es el correo del usuario comprometido? | `bigman@shefesh.com` |
| 3 | ¿Cuál es la contraseña del usuario? | `saltnpepper` |
| 4 | ¿Cuál es el secreto/pregunta de seguridad del usuario? | `Waterloo` |
| 5 | ¿Cuál es la flag del reto? | `THM{SHELLS_IN_MY_EGGNOG}` |

### Task 29: Día 24 - Elf Stalk (ELK)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el ID del documento que contiene la flag en Elasticsearch/ELK? | `9Qs58Ol3AXkMWLxiEyUyyf` |
| 2 | ¿Cuál es el valor almacenado en el campo 'flag' del documento? | `someELKfun` |

### Task 30: Conclusión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Responde a la encuesta de cierre del evento. | `No answer needed` |

---

**Metodología:** El evento se resuelve día a día. Los primeros días manipulan cookies (authid, recorrido por hex/JSON), directorios y credenciales por defecto (/sysadmin + defaultpass) y análisis de PCAPs (Wireshark). Los días de sistema usan comandos base de Linux, después binarios SUID y escaladas (cronjob). Las tareas web incluyen Hydra, juegos web, LFI y finalizan con una inyección SQL en LapLANd. La tarea de cierre utiliza ELK (Elasticsearch) para localizar un documento con la respuesta. Se respeta la numeración de respuestas del dump original.

**Learning chain:** cookies y credenciales → análisis de tráfico → comandos Linux → OSINT → exfiltración → SUID → Metasploit → aplicaciones web → cifrado → almacenamiento S3 → LFI → fuerza bruta → ejecutables → escalada → ingeniería inversa → lógica → SQLi → búsqueda en ELK.

**MITRE ATT&CK:** T1087 (Account Discovery), T1213 (Data from Information Repositories), T1548 (Abuse Elevation Control Mechanism), T1190 (Exploit Public-Facing Application), T1020 (Automated Exfiltration), T1110 (Brute Force), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Advent of Cyber 1 [2019]](https://tryhackme.com/room/25daysofchristmas)