# NIS - Linux Part I

| **Dificultad** | Easy |
| **Tipo** | Fundamentos de Linux (laboratorio) |
| **Slug** | `nislinuxone` |
| **Link** | [TryHackMe](https://tryhackme.com/room/nislinuxone) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | SSH / ls / find / grep / echo / curl / wget / permisos de archivos |
| **Impacto** | Sala que refuerza los fundamentos de Linux: conexión por SSH, enumeración de archivos con las distintas variantes de `ls`, búsqueda de contenido (flags), nociones de permisos, y comandos de trabajo con red como `echo`, `find`, `curl` y `wget`, terminando con la recolección de varias flags a lo largo del sistema. |

---

**Contexto:** La sala guía al usuario por comandos esenciales de Linux partiendo de la conexión por SSH a la máquina (usuario `tryhackme`) y la lectura del archivo de bienvenida `linux.txt`. Después se practican las variantes de `ls` (incluyendo `-a`, `-A`, `-l`, `-h`, `--recursive` y el conteo de elementos del directorio: 13). Se cazan seis flags ocultas en distintos archivos del sistema y se repasan nociones de permisos (valores octales `rwx`). Se continúa con comandos de utilidad: imprimir texto con `echo`, encontrar y volcar archivos `.bak` con `find` y `xargs`, obtener cabeceras HTTP con `curl -I -s ... | grep HTTP` y descargar contenido con `wget` (descarga simple y recursiva con límite de profundidad). El recorrido culmina con cuatro flags finales de consolidación.

## Solucionario

### Task 1: Conexión y primeros archivos

**Explicación:** Se conecta por SSH a la máquina con el usuario `tryhackme` y una contraseña que el propio laboratorio facilita, y se lee el archivo `linux.txt` del directorio personal con `cat`.

```bash
ssh tryhackme@<MACHINE_IP>
cat linux.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Con qué usuario te conectas por SSH a la máquina? | `tryhackme` |
| 2 | ¿Qué comando habría que usar para leer el contenido del archivo linux.txt? | `cat linux.txt` |

### Task 2: Listando con ls

**Explicación:** El comando `ls` lista los archivos del directorio actual, pero sus opciones permiten verlos de muchas formas: `ls -a` muestra todos los archivos incluidos los ocultos, `ls -A` muestra todos excepto `.` y `..`, `ls -l` muestra permisos, propietario y tamaño en formato largo, `ls -h` imprime los tamaños en formato legible para humanos, y `ls --recursive` recorre los subdirectorios de forma recursiva. Al aplicar el listado sobre el directorio de trabajo se contabilizan `13` archivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando lista los archivos y directorios del directorio actual? | `ls` |
| 2 | ¿Qué comando lista también los archivos ocultos? | `ls -a` |
| 3 | ¿Qué comando lista todos los archivos excepto `.` y `..`? | `ls -A` |
| 4 | ¿Qué comando lista los archivos en formato largo (permisos, propietario, tamaño)? | `ls -l` |
| 5 | ¿Qué comando lista los archivos con tamaños legibles para humanos? | `ls -h` |
| 6 | ¿Qué comando lista los directorios de forma recursiva? | `ls --recursive` |
| 7 | ¿Cuántos archivos hay en el directorio actual? | `13` |

### Task 3: Cazando flags

**Explicación:** Recorriendo los archivos del sistema (combinando `ls -a`, `cat` y navegando por directorios) se localizan seis flags en distintos puntos del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag que encuentras? | `THM{11aadbee391acdffee901}` |
| 2 | ¿Cuál es la segunda flag? | `THM{acab0111aaa687912139}` |
| 3 | ¿Cuál es la tercera flag? | `THM{894abac55f7962abc166}` |
| 4 | ¿Cuál es la cuarta flag? | `THM{1689acafdd20751acff6}` |
| 5 | ¿Cuál es la quinta flag? | `THM{fac1aab210d6e4410acd}` |
| 6 | ¿Cuál es la sexta flag? | `THM{aa462c1b2d44801c0a31}` |

### Task 4: Nociones de permisos

**Explicación:** Se repasan los permisos de archivos en Linux usando la notación octal: cada tripleta `rwx` equivale al valor `7`, y las combinaciones parciales (como `r-x`) producen valores intermedios. El permiso numérico del propietario encontrado en el archivo analizado es `8` (bit especial + permiso) y el de "otros" es `0`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué valor de permiso en octal tiene el propietario del archivo analizado? | `8` |
| 2 | ¿Qué valor de permiso en octal tienen "otros" para ese mismo archivo? | `0` |

### Task 5: Contando elementos

**Explicación:** Aplicando los listados aprendidos se cuenta el número total de elementos (archivos y directorios) presentes en el directorio sobre el que se trabaja: `15`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos elementos hay en total en el directorio? | `15` |

### Task 6: Comprobando listados

**Explicación:** Se contrasta lo que devuelven las distintas invocaciones de `ls` para confirmar qué archivos aparecen en cada listado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Aparecen todos los archivos ocultos con el listado estándar? (Y/N) | `Nay` |

### Task 7: Explorando el sistema

**Explicación:** Navegación libre por el sistema de archivos para localizar los elementos sobre los que responderán las siguientes preguntas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora el sistema de archivos y localiza los ficheros interesantes. | `No answer needed` |

### Task 8: Escribiendo con echo

**Explicación:** El comando `echo` imprime texto por pantalla. Para imprimir literalmente la palabra "Hackerman" se escribe `echo "Hackerman"`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando usarías para imprimir la palabra "Hackerman" en la terminal? | `echo "Hackerman"` |

### Task 9: Buscando con find

**Explicación:** `find` localiza archivos por nombre y atributos. La cadena `find / -name *.bak -type f -print | xargs /bin/cat` busca desde la raíz todos los archivos regulares (`-type f`) que terminan en `.bak`, los imprime (`-print`) y, con `xargs`, pasa el resultado a `cat` para volcar su contenido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando usarías para encontrar todos los archivos `.bak` y leer su contenido? | `find / -name *.bak -type f -print | xargs /bin/cat` |

### Task 10: Repasando lo aprendido

**Explicación:** Ejercicio de consolidación de los comandos vistos hasta ahora.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica con los comandos vistos hasta ahora. | `No answer needed` |

### Task 11: Obteniendo cabeceras con curl

**Explicación:** `curl` transfiere datos por la red. Para obtener solo la línea de estado HTTP de una web se usa `curl -I -s https://tryhackme.com | grep HTTP`: `-I` hace una petición HEAD, `-s` suprime la barra de progreso y `grep HTTP` filtra la línea con la respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando usarías para ver únicamente la línea de estado HTTP de https://tryhackme.com? | `curl -I -s https://tryhackme.com | grep HTTP` |

### Task 12: Descargando con wget

**Explicación:** `wget` descarga recursos de la red. `wget https://tryhackme.com/flag.txt` descarga el archivo indicado, y `wget -r -l 10 https://tryhackme.com` descarga el sitio web de forma recursiva (`-r`) limitando la profundidad a `10` niveles (`-l 10`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando usarías para descargar el archivo https://tryhackme.com/flag.txt? | `wget https://tryhackme.com/flag.txt` |
| 2 | ¿Qué comando usarías para descargar recursivamente el sitio https://tryhackme.com hasta una profundidad de 10 enlaces? | `wget -r -l 10 https://tryhackme.com` |

### Task 13: Flag de consolidación 1

**Explicación:** Aplicando las técnicas de listado, búsqueda y lectura de archivos se obtiene el primer flag de consolidación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de esta parte del laboratorio? | `THM{C0FFE1337101}` |

### Task 14: Flag de consolidación 2

**Explicación:** Continuando con la exploración del sistema se localiza la segunda flag de consolidación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de esta parte del laboratorio? | `THM{0AFDECC951A}` |

### Task 15: Flag de consolidación 3

**Explicación:** El recorrido termina de confirmarse con la tercera flag de consolidación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de esta parte del laboratorio? | `THM{526accdf94}` |

### Task 16: Flag de consolidación 4

**Explicación:** Última flag recopilada dentro del ejercicio de fundamentos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de esta parte del laboratorio? | `THM{af5548a12bc2de}` |

---

**Metodología:** Se conecta por SSH y se recorren los comandos base de Linux de forma progresiva: `ls` y sus variantes para enumerar archivos, `cat`/`find` para localizar y leer contenido (flags), nociones de permisos en octal, y comandos de red (`echo`, `curl`, `wget`) para practicar impresión, cabeceras HTTP y descargas, cerrando con la recolección de flags.
**Learning chain:** autenticarse por SSH → enumerar con `ls -a/-A/-l/-h/--recursive` → leer archivos y cazar flags → comprender permisos (octal) → practicar `echo`, `find|xargs`, `curl -I|grep`, `wget -r -l` → consolidar con flags finales.
**MITRE ATT&CK:** T1021.004 (Remote Services: SSH), T1083 (File and Directory Discovery), T1555 (Credentials from Password Stores), T1040 (Network Sniffing), T1105 (Ingress Tool Transfer)
**Fuente:** [TryHackMe - NIS - Linux Part I](https://tryhackme.com/room/nislinuxone)