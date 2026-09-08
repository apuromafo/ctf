# Linux Strength Training

| **Dificultad** | Easy |
| **Tipo** | Ejercicios de línea de comandos Linux |
| **Slug** | `linuxstrengthtraining` |
| **Link** | [TryHackMe](https://tryhackme.com/room/linuxstrengthtraining) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | find / cp / mv / scp / hashing / base64 / john / GPG |
| **Impacto** | Sala de ejercicios de terminal Linux: búsqueda con find (por grupo, usuario, tamaño y fecha), gestión de archivos y directorios (mv, cp, scp y opciones con "--"), identificación de hashes y cifrados, descifrado con john y GPG (incluido el cifrado simétrico AES-128), resolución de retos y captura de banderas. |

---

**Contexto:** La sala es una batería de ejercicios prácticos de Linux. Se buscan archivos con find usando flags como `-group`, `-user` y `-size` y se trabaja con permisos de propietario y fechas de modificación. Después se gestionan archivos y directorios con mv, cp y scp, manejando nombres que empiezan por guion con `--`. Los módulos siguientes identifican el tipo de hash de contraseñas (MD4, SHA-1) y su contenido (secret123, admin, letmein...), practican decodificación con base64 y craqueo con john, cifrado y descifrado simétrico con GPG (AES-128) y terminan resolviendo el reto final con bands.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Encontrando archivos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega el laboratorio y abre la terminal. | `No answer needed` |
| 2 | ¿Qué flag de find permite buscar por grupo de usuario? | `-group` |
| 3 | ¿Qué comando find encuentra los archivos de tipo f, propiedad de francis, de tamaño 52k, en /home/francis? | `find /home/francis -type f -user francis -size 52k` |
| 4 | ¿Cuál es la fecha de la última modificación del archivo? | `2019-10-11` |
| 5 | Cambia al usuario indicado y resuelve el reto. | `No answer needed` |
| 6 | ¿Cuál es el propietario del archivo? | `ttitor` |
| 7 | ¿Cuál es la bandera de la tarea? | `Flag{81726350827fe53g}` |

### Task 3: ¿Dónde? ¿Qué? ¿Dónde?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando mueve todos los archivos de /home/francis/Downloads al directorio /home/francis/logs? | `mv * /home/francis/logs` |
| 2 | ¿Qué comando copia script.py desde /home/james/Desktop al equipo de john por scp? | `scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts` |
| 3 | ¿Qué comando mv renombra el directorio "-logs" a "-newlogs" sin que lo interprete como una opción? | `mv -- -logs -newlogs` |
| 4 | ¿Qué comando copia el archivo "encryption keys" al directorio /home/john/logs? | `cp "encryption keys" /home/john/logs` |
| 5 | ¿Cuál es la bandera de la tarea? | `Flag{234@i4s87u5hbn$3}` |

### Task 4: Entiende los hashes

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña cuyo hash aparece en el ejemplo? | `secret123` |
| 2 | ¿Qué algoritmo generó un hash de 128 bits? | `MD4` |
| 3 | ¿Cuál es la contraseña del segundo ejemplo? | `admin` |
| 4 | ¿Qué algoritmo generó el segundo hash? | `SHA-1` |
| 5 | ¿Qué contraseña está detrás del hash largo de la actividad? | `unacvaolipatnuggi` |
| 6 | ¿Cuál es la contraseña del último hash de la actividad? | `letmein` |

### Task 5: Craqueo de contraseñas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Con qué utilidad se decodifica el contenido base64 de la actividad? | `base64` |
| 2 | ¿Qué herramienta se utiliza para craquear el hash de la actividad? | `john` |

### Task 6: Cifrado y descifrado digital

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación del laboratorio para la práctica de GPG. | `No answer needed` |
| 2 | ¿Qué comando cifra history_logs.txt de forma simétrica con AES-128 usando GPG? | `gpg --cipher-algo AES-128 --symmetric history_logs.txt` |
| 3 | ¿Qué comando descifra el archivo history_logs.txt.gpg? | `gpg history_logs.txt.gpg` |
| 4 | ¿Cuál es la bandera de la tarea? | `Flag{B07$f854f5ghg4s37}` |

### Task 7: Reto de cifrado

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Resuelve el reto completo de cifrado. | `No answer needed` |
| 2 | ¿Cuál es la contraseña encontrada para desbloquear el reto? | `valamanezivonia` |
| 3 | ¿Cuál es el mensaje final del reto? | `getting stronger in linux` |

### Task 8: Bandera

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera de la tarea? | `Flag{13490AB8}` |

### Task 9: Reto final

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Resuelve el reto final de la sala. | `No answer needed` |
| 2 | ¿Cuál es la contraseña de la primera fase del reto? | `thegreatestpasswordever000` |
| 3 | ¿Cuál es la contraseña de la segunda fase? | `ebqattle` |
| 4 | ¿Cuál es la contraseña de la tercera fase? | `vuimaxcullings` |
| 5 | Completa los pasos restantes del reto. | `No answer needed` |
| 6 | ¿Cuál es la bandera final? | `Flag{6$8$hyJSJ3KDJ3881}` |

---

**Metodología:** Se localizan archivos con find combinando tipo, usuario, tamaño y grupo, y se extraen propietario, fecha y banderas. La gestión de archivos se resuelve con mv/cp/scp, incluyendo el manejo de nombres con guion inicial mediante `--`. En la parte de hashing se identifican los algoritmos por la longitud y el formato (MD4 de 128 bits, SHA-1) y se descifran las contraseñas (secret123, admin, letmein, etc.); luego se decodifica base64 y se craquea el hash con john. El módulo de GPG cifra y descifra de forma simétrica con AES-128, y el reto final combina la contraseña de varias fases para entregar la bandera.

**Learning chain:** find → gestión de archivos (mv/cp/scp) → identificación de hashes → base64/john → cifrado GPG → reto final.

**MITRE ATT&CK:** T1552.001 (Unsecured Credentials: Credentials In Files), T1005 (Data from Local System), T1059.004 (Command and Scripting Interpreter: Unix Shell)

**Fuente:** [TryHackMe - Linux Strength Training](https://tryhackme.com/room/linuxstrengthtraining)