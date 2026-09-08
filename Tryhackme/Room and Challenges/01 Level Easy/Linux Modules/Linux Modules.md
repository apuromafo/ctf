# Linux Modules

| **Dificultad** | Easy |
| **Tipo** | Herramientas de línea de comandos Linux |
| **Slug** | `linuxmodules` |
| **Link** | [TryHackMe](https://tryhackme.com/room/linuxmodules) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Bash / grep / sed / awk / xargs / curl / wget / xxd / gpg / ss |
| **Impacto** | Sala práctica de herramientas de terminal de Linux: filtrado con clases de caracteres (`:digit:`, `:alpha:`, `:xdigit:`), procesamiento con awk y sed, encadenado con xargs, descargas con curl y wget, volcado hexadecimal con xxd, cifrado GPG y estadísticas de sockets con ss, cerrando con una bandera. |

---

**Contexto:** La sala es un taller de herramientas de terminal. En la práctica se usa el intérprete (con la flag `-v` para verificar la versión) y se combinan utilidades: grep con clases de caracteres POSIX, awk para reordenar campos de archivos, sed para sustituir patrones (incluida la eliminación de dígitos con `[[:digit:]]`), xargs para ejecutar comandos sobre listas de archivos, curl y wget con sus opciones (`--limit-rate`, `-A`, `-N`, `-a`, `-i`), xxd para inspección hexadecimal en bits (`-s`, `-l`, `-c`, `-g`), GPG para importar claves y la herramienta `ss` (Socket Statistics).

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación del taller de herramientas de terminal Linux que se practican en los módulos. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Preparación

**Explicación:** Instalación/configuración del entorno (máquina o terminal) donde se ejecutarán los ejercicios de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Instala y prepara el entorno de trabajo. | `No answer needed` |

### Task 3: El intérprete de comandos

**Explicación:** Se comprueba el shell: la flag `-v` muestra la versión del intérprete. El texto desplegado contiene la palabra `bobthebuilder`, la credencial `LinuxIsGawd` y el usuario `fs0ciety`.

```bash
bash -v
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre la terminal y comprueba la conexión. | `No answer needed` |
| 2 | ¿Está el entorno preparado para comenzar? | `Yea` |
| 3 | ¿Qué flag se utiliza para mostrar la versión del intérprete? | `-v` |
| 4 | Revisa la ayuda del intérprete. | `No answer needed` |
| 5 | ¿Cuál es la primera palabra del texto que despliega la sala? | `bobthebuilder` |
| 6 | ¿Cuál es la credencial de acceso indicada? | `LinuxIsGawd` |
| 7 | ¿Cuál es el nombre de usuario indicado? | `fs0ciety` |

### Task 4: Resumen del módulo

**Explicación:** Vista general de los módulos que se verán: filtros, awk, sed, xargs, curl, wget, xxd, GPG y ss.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el resumen de los módulos a trabajar. | `No answer needed` |

### Task 5: Filtros y búsquedas

**Explicación:** grep con clases de caracteres POSIX: `[:digit:]` (solo dígitos), `[:alpha:]` (solo letras) y `[:xdigit:]` (dígitos hexadecimales).

```bash
grep '[[:digit:]]' archivo.txt
grep '[[:alpha:]]' archivo.txt
grep '[[:xdigit:]]' archivo.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza las búsquedas propuestas en los archivos de ejemplo. | `No answer needed` |
| 2 | ¿Qué clase de caracteres coincide solo con dígitos? | `:digit:` |
| 3 | ¿Qué clase de caracteres coincide solo con letras? | `:alpha:` |
| 4 | ¿Qué clase de caracteres coincide con dígitos hexadecimales? | `:xdigit:` |

### Task 6: awk

**Explicación:** awk procesa campos por línea. Para imprimir campo 1 y 4 separados por ":" sobre awk.txt: `awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt`; para imprimir el campo 1 seguido de ", ": `awk 'BEGIN{ORS=", "} {print $1}' awk.txt`.

```bash
awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt
awk 'BEGIN{ORS=", "} {print $1}' awk.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica la lectura del archivo de ejemplo con awk. | `No answer needed` |
| 2 | ¿Qué comando awk muestra el campo 1 y el campo 4 separados por ":" usando el archivo awk.txt? | `awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt` |
| 3 | ¿Qué comando awk imprime el campo 1 de cada línea seguido de una coma y un espacio? | `awk 'BEGIN{ORS=", "} {print $1}' awk.txt` |

### Task 7: sed

**Explicación:** sed sustituye patrones: `'s/hack/back/3g'` (todas las apariciones a partir de la 3ª), `'3,4 s/.../'` (líneas 3 y 4), `'s/  */:/g'` (espacios múltiples → ":") y `'s/[[:digit:]]//g'` (eliminar dígitos). Retos resueltos devuelven `CONGRATULATIONS YOU MADE IT THROUGH THIS SMALL LITTLE CHALLENGE` y la frase final `"That's What"`.

```bash
sed 's/  */:/g' sed1.txt
sed 's/[[:digit:]]//g' texto.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando sed sustituye "hack" por "back" en todas las apariciones de la tercera línea de file.txt? | `sed 's/hack/back/3g' file.txt` |
| 2 | ¿Qué comando sed aplica la sustitución anterior a las líneas 3 y 4 de file.txt? | `sed '3,4 s/hack/back/3g' file.txt` |
| 3 | ¿Qué comando colapsa los espacios múltiples en ":" en sed1.txt? | `sed 's/  */:/g' sed1.txt` |
| 4 | ¿Qué mensaje obtienes al resolver el reto de sed? | `CONGRATULATIONS YOU MADE IT THROUGH THIS SMALL LITTLE CHALLENGE` |
| 5 | ¿Qué expresión sed elimina todos los dígitos de un texto? | `'s/[[:digit:]]//g'` |
| 6 | Resuelve la actividad final de sed. | `No answer needed` |
| 7 | ¿Cuál es la frase de salida del último reto? | `"That's What"` |

### Task 8: xargs

**Explicación:** xargs ejecuta comandos sobre listas: crea un archivo por elemento con chmod 400 (`cat file | xargs -I files -t sh -c "touch files; chmod 400 files"`), o añade nombres a shortrockyou y elimina (`ls | xargs -I word -n 1 -t sh -c 'echo word >> shortrockyou; rm word'`). Flags: `-n` limita argumentos por invocación y `--` define un delimitador explícito.

```bash
cat file | xargs -I files -t sh -c "touch files; chmod 400 files"
ls | xargs -I word -n 1 -t sh -c 'echo word >> shortrockyou; rm word'
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica el uso de xargs sobre listas de archivos. | `No answer needed` |
| 2 | ¿Qué comando crea un archivo por elemento de la lista y le aplica chmod 400? | `cat file \| xargs -I files -t sh -c "touch files; chmod 400 files"` |
| 3 | ¿Qué comando añade cada nombre de archivo a shortrockyou y lo elimina? | `ls \| xargs -I word -n 1 -t sh -c 'echo word >> shortrockyou; rm word'` |
| 4 | ¿Qué flag de xargs limita el número de argumentos pasados por invocación? | `-n` |
| 5 | ¿Qué flag de xargs define un delimitador explícito? | `--` |

### Task 9: Reto de xargs

**Explicación:** Reto encadenado con xargs: aparecen la palabra clave `lollol` y el número `2550` como datos del ejercicio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Resuelve el reto final de xargs. | `No answer needed` |
| 2 | ¿Cuál es la palabra clave de la primera parte del reto? | `lollol` |
| 3 | ¿Cuál es el número que aparece como parte del reto? | `2550` |

### Task 10: curl

**Explicación:** `curl --limit-rate` limita la velocidad; enviar un user agent personalizado: `curl -A 'juzztesting' https://tryhackme.com/`. Al completar la interacción con la web, la respuesta marca `Yea`.

```bash
curl --limit-rate 1m https://example.com
curl -A 'juzztesting' https://tryhackme.com/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica la descarga de páginas con curl. | `No answer needed` |
| 2 | ¿Qué flag de curl limita la velocidad de transferencia? | `--limit-rate` |
| 3 | ¿Qué comando envía una petición a tryhackme.com con el user agent "juzztesting"? | `curl -A 'juzztesting' https://tryhackme.com/` |
| 4 | ¿Quién completó la interacción? | `Yea` |

### Task 11: wget

**Explicación:** `wget -N` retoma descargas interrumpidas; `wget -a package-logs.txt https://xyz.com/mypackage.zip` descarga registrando el log; `wget -i file.txt --limit-rate=1m` descarga una lista con límite de velocidad.

```bash
wget -N https://example.com/archivo.zip
wget -a package-logs.txt https://xyz.com/mypackage.zip
wget -i file.txt --limit-rate=1m
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica la descarga de archivos con wget. | `No answer needed` |
| 2 | ¿Qué flag de wget retoma descargas interrumpidas? | `-N` |
| 3 | ¿Qué comando descarga mypackage.zip y registra el proceso en package-logs.txt? | `wget -a package-logs.txt https://xyz.com/mypackage.zip` |
| 4 | ¿Qué comando descarga los archivos de file.txt con un límite de velocidad de 1m? | `wget -i file.txt --limit-rate=1m` |

### Task 12: xxd

**Explicación:** xxd vuelca archivos en hexadecimal/binario: `xxd -s 0xa -l 50 -b file.txt` (50 bytes desde offset 0xa en binario), `xxd -c 9 -g 3 file.txt` (9 columnas, grupos de 3 bytes). La flag `-c` fija el número de columnas. El volcado esconde la bandera `flag{wh3sdw0lw1gl9oqasad2fs48as}`.

```bash
xxd -s 0xa -l 50 -b file.txt
xxd -c 9 -g 3 file.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre el archivo de ejemplo con xxd. | `No answer needed` |
| 2 | ¿Qué comando muestra 50 bytes a partir del offset 0xa en binario? | `xxd -s 0xa -l 50 -b file.txt` |
| 3 | ¿Qué comando muestra el archivo en 9 columnas y grupos de 3 bytes? | `xxd -c 9 -g 3 file.txt` |
| 4 | ¿Qué flag de xxd establece el número de columnas de salida? | `-c` |
| 5 | ¿Cuál es la bandera escondida en los datos hexadecimales? | `flag{wh3sdw0lw1gl9oqasad2fs48as}` |

### Task 13: Cifrado con GPG

**Explicación:** La clave de la sala es `Wrong`; se importa la clave pública con `gpg --import key.gpg`. Además: `ss` significa `Socket Statistics` y `reset` restablece la terminal si queda bloqueada.

```bash
gpg --import key.gpg
ss -tulpn
reset
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación del entorno de GPG. | `No answer needed` |
| 2 | ¿Cuál es la clave de la sala relacionada con GPG? | `Wrong` |
| 3 | ¿Qué comando importa la clave pública key.gpg? | `gpg --import key.gpg` |
| 4 | ¿Qué significa la abreviatura "ss"? | `Socket Statistics` |
| 5 | ¿Qué comando restablece la terminal si el terminal queda bloqueado? | `reset` |

### Task 14: Resumen

**Explicación:** La actividad final marca `F`: el módulo se considera cerrado cuando todos los ejercicios anteriores están completados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿La actividad final se considera completada? (T/F) | `F` |

---

**Metodología:** El taller se resuelve combinando utilidades de terminal: primero se verifica el intérprete y se ejecutan los comandos de filtrado (clases de caracteres POSIX con grep), después se procesan archivos con awk y sed (sustitución y borrado de dígitos) y se automatizan tareas repetitivas con xargs. La descarga de contenido se practica con curl y wget (límite de velocidad, user agents, retoma y logs), el análisis de datos binarios con xxd (offsets, columnas y grupos de bytes) permite localizar la bandera y, finalmente, se importa una clave GPG y se consultan sockets con `ss`.

**Learning chain:** intérprete → filtros → awk → sed → xargs → curl → wget → xxd → GPG/ss.

**MITRE ATT&CK:** T1059.004 (Command and Scripting Interpreter: Unix Shell), T1005 (Data from Local System), T1082 (System Information Discovery)

**Fuente:** [TryHackMe - Linux Modules](https://tryhackme.com/room/linuxmodules)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
