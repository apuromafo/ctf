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

**Explicación:** Presentación de la sala de ejercicios Linux: find, gestión de archivos, hashes, base64/john, GPG y retos finales. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Encontrando archivos

**Explicación:** find localiza archivos: `-group` busca por grupo; `find /home/francis -type f -user francis -size 52k` encuentra el archivo de francis (última modificación `2019-10-11`, propietario `ttitor`). La bandera de la tarea es `Flag{81726350827fe53g}`.

```bash
find /home/francis -type f -user francis -size 52k
ls -l /path/archivo
```

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

**Explicación:** Gestión de archivos: `mv * /home/francis/logs` mueve todo; `scp` copia a un host remoto (`scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts`); `--` evita que un guion inicial se lea como opción (`mv -- -logs -newlogs`); y las rutas con espacios/letras se operan entre comillas (`cp "encryption keys" /home/john/logs`). Bandera: `Flag{234@i4s87u5hbn$3}`.

```bash
mv * /home/francis/logs
scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts
mv -- -logs -newlogs
cp "encryption keys" /home/john/logs
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando mueve todos los archivos de /home/francis/Downloads al directorio /home/francis/logs? | `mv * /home/francis/logs` |
| 2 | ¿Qué comando copia script.py desde /home/james/Desktop al equipo de john por scp? | `scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts` |
| 3 | ¿Qué comando mv renombra el directorio "-logs" a "-newlogs" sin que lo interprete como una opción? | `mv -- -logs -newlogs` |
| 4 | ¿Qué comando copia el archivo "encryption keys" al directorio /home/john/logs? | `cp "encryption keys" /home/john/logs` |
| 5 | ¿Cuál es la bandera de la tarea? | `Flag{234@i4s87u5hbn$3}` |

### Task 4: Entiende los hashes

**Explicación:** Identificación de hashes por tamaño: `MD4` genera 128 bits; los ejemplos se crackean a `secret123`, `admin`, `unacvaolipatnuggi` y `letmein`; el segundo algoritmo es `SHA-1`.

```bash
echo -n "secret123" | md4sum
echo -n "admin" | sha1sum
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña cuyo hash aparece en el ejemplo? | `secret123` |
| 2 | ¿Qué algoritmo generó un hash de 128 bits? | `MD4` |
| 3 | ¿Cuál es la contraseña del segundo ejemplo? | `admin` |
| 4 | ¿Qué algoritmo generó el segundo hash? | `SHA-1` |
| 5 | ¿Qué contraseña está detrás del hash largo de la actividad? | `unacvaolipatnuggi` |
| 6 | ¿Cuál es la contraseña del último hash de la actividad? | `letmein` |

### Task 5: Craqueo de contraseñas

**Explicación:** El contenido base64 de la actividad se decodifica con la utilidad `base64` y el hash resultante se crackea con `john`.

```bash
base64 -d contenido.b64 > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Con qué utilidad se decodifica el contenido base64 de la actividad? | `base64` |
| 2 | ¿Qué herramienta se utiliza para craquear el hash de la actividad? | `john` |

### Task 6: Cifrado y descifrado digital

**Explicación:** GPG simétrico: `gpg --cipher-algo AES-128 --symmetric history_logs.txt` cifra con AES-128 y `gpg history_logs.txt.gpg` descifra pidiendo la frase. Bandera: `Flag{B07$f854f5ghg4s37}`.

```bash
gpg --cipher-algo AES-128 --symmetric history_logs.txt
gpg history_logs.txt.gpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación del laboratorio para la práctica de GPG. | `No answer needed` |
| 2 | ¿Qué comando cifra history_logs.txt de forma simétrica con AES-128 usando GPG? | `gpg --cipher-algo AES-128 --symmetric history_logs.txt` |
| 3 | ¿Qué comando descifra el archivo history_logs.txt.gpg? | `gpg history_logs.txt.gpg` |
| 4 | ¿Cuál es la bandera de la tarea? | `Flag{B07$f854f5ghg4s37}` |

### Task 7: Reto de cifrado

**Explicación:** El reto de cifrado se desbloquea con la contraseña `valamanezivonia` (obtenida craqueando el hash) y el mensaje final descifrado es `getting stronger in linux`.

```bash
hashcat/john hash.txt
gpg archivo.gpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Resuelve el reto completo de cifrado. | `No answer needed` |
| 2 | ¿Cuál es la contraseña encontrada para desbloquear el reto? | `valamanezivonia` |
| 3 | ¿Cuál es el mensaje final del reto? | `getting stronger in linux` |

### Task 8: Bandera

**Explicación:** Tras completar los ejercicios del laboratorio se obtiene la bandera de la tarea.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera de la tarea? | `Flag{13490AB8}` |

### Task 9: Reto final

**Explicación:** Reto final en fases con contraseñas craqueadas/cifradas: `thegreatestpasswordever000` (fase 1), `ebqattle` (fase 2) y `vuimaxcullings` (fase 3); completando los pasos finales se obtiene la bandera `Flag{6$8$hyJSJ3KDJ3881}`.

```bash
gpg -d fase1.gpg   # pass: thegreatestpasswordever000
gpg -d fase2.gpg   # pass: ebqattle
gpg -d fase3.gpg   # pass: vuimaxcullings
```

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
