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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy de la máquina y lectura de la introducción. | `No answer needed` |

### Task 2: Preparación del entorno

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura la máquina y el AttackBox para comenzar. | `No answer needed` |

### Task 3: Día 1 - Autenticación (cookies)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede al portal y autentícate para generar tu cookie. | `No answer needed` |
| 2 | ¿Cuál es el nombre de la cookie usada para la autenticación? | `auth` |
| 3 | ¿En qué formato está codificado el valor de la cookie? | `Hexadecimal` |
| 4 | Tras decodificar la cookie, ¿en qué formato se almacenan los datos? | `JSON` |
| 5 | ¿Cuál es el valor de la cookie de Santa? | `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d` |
| 6 | ¿Qué flag se obtiene cuando la línea está totalmente activa? | `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}` |

### Task 4: Día 2 - Subida de archivos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cadena de texto hay que añadir a la URL para acceder a la página de subida? | `?id=ODIzODI5MTNiYmYw` |
| 2 | ¿Qué tipo de archivo acepta el sitio? | `Image` |
| 3 | ¿En qué directorio se almacenan los archivos subidos? | `/uploads/` |
| 4 | Explota la subida de archivos para ejecutar código. | `No answer needed` |
| 5 | ¿Cuál es la flag en /var/www/flag.txt? | `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}` |

### Task 5: Día 3 - Descubriendo credenciales

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza el ataque de autenticación indicado en el laboratorio. | `No answer needed` |
| 2 | ¿Cuál es la flag? | `THM{885ffab980e049847516f9d8fe99ad1a}` |

### Task 6: Día 4 - Enumeración web y fuzzing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta la enumeración de directorios contra el objetivo desplegado. | `No answer needed` |
| 2 | Dada la URL "http://shibes.xyz/api.php", ¿cuál sería el comando wfuzz completo para consultar el parámetro "breed" con la wordlist "big.txt"? | `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ` |
| 3 | Usando GoBuster (contra el objetivo desplegado, no shibes.xyz) para encontrar el directorio de la API, ¿qué archivo hay? | `site-log.php` |
| 4 | Fuzzea el parámetro "date" del archivo encontrado en el directorio de la API. ¿Qué flag muestra el post correcto? | `THM{D4t3_AP1}` |

### Task 7: Día 5 - Inyección SQL en el panel de Santa

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sin usar fuerza bruta de directorios, ¿cuál es el panel de login secreto de Santa? | `/santapanel` |
| 2 | Bypassea el login con inyección SQL. | `No answer needed` |
| 3 | ¿Cuántas entradas hay en la base de datos de regalos? | `22` |
| 4 | ¿Qué pidió Paul? | `Github Ownership` |
| 5 | ¿Cuál es la flag? | `thmfox{All_I_Want_for_Christmas_Is_You}` |
| 6 | ¿Cuál es la contraseña de admin? | `EhCNSWzzFP6sc7gB` |

### Task 8: Día 6 - Cross-Site Scripting (XSS)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora el foro y localiza el fallo de inyección. | `No answer needed` |
| 2 | ¿Qué tipo de vulnerabilidad se usó para explotar la aplicación? | `Stored cross-site scripting` |
| 3 | ¿Qué cadena de consulta puede abusarse para crear un XSS reflejado? | `q` |
| 4 | Prepara ZAP (zaproxy) contra el objetivo. | `No answer needed` |
| 5 | Ejecuta un escaneo automatizado de ZAP. ¿Cuántas alertas XSS hay? | `2` |
| 6 | Continúa con la explotación del XSS. | `No answer needed` |

### Task 9: Día 7 - Análisis de tráfico (Wireshark)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre "pcap1.pcap" en Wireshark. ¿Qué dirección IP inicia el ping/ICMP? | `10.11.3.2` |
| 2 | ¿Qué filtro usarías para ver solo peticiones HTTP GET en "pcap1.pcap"? | `http.request.method == GET` |
| 3 | Aplica este filtro. ¿Cómo se llama el artículo que visitó la IP "10.10.67.199"? | `reindeer-of-the-week` |
| 4 | Analiza "pcap2.pcap". ¿Qué contraseña se filtró durante el login FTP? | `plaintext_password_fiasco` |
| 5 | Continuando con "pcap2.pcap", ¿qué protocolo está cifrado? | `SSH` |
| 6 | ¿Qué quiere Elf McSkidy para sustituir a Elf McEager? | `Rubber ducky` |

### Task 10: Día 8 - Snort y Nmap

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el directorio del servidor FTP con datos accesibles por el usuario "anonymous"? | `public` |
| 2 | ¿Qué script se ejecuta dentro de este directorio? | `backup.sh` |
| 3 | ¿Qué película tenía Santa en su lista de compras de Navidad? | `The Polar Express` |
| 4 | Re-subida el script con datos maliciosos (como en la sección 9.6) y muestra el contenido de /root/flag.txt. | `THM{even_you_can_be_santa}` |

### Task 12: Día 10 - Samba

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usando enum4linux, ¿cuántos usuarios hay en el servidor Samba (MACHINE_IP)? | `3` |
| 2 | ¿Cuántos "shares" hay en el servidor Samba? | `4` |
| 3 | Usa smbclient para intentar entrar en los shares. ¿Qué share no requiere contraseña? | `tbfc-santa` |
| 4 | Entra en ese share. ¿Qué directorio dejó ElfMcSkidy para Santa? | `jingle-tunes` |

### Task 13: Día 11 - Escalada de privilegios (sudo)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de escalada de privilegios usa una cuenta de usuario para ejecutar comandos como administrador? | `Vertical` |
| 2 | ¿Cómo se llama el archivo que contiene la lista de usuarios del grupo sudo? | `sudoers` |
| 3 | Comprueba los privilegios sudo del usuario comprometido. | `No answer needed` |
| 4 | Escala privilegios para acceder a root. | `No answer needed` |
| 5 | ¿Cuál es el contenido del archivo /root/flag.txt? | `thm{2fb10afe933296592}` |

### Task 14: Día 12 - Apache Tomcat (Metasploit)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de versión del servidor web? | `9.0.17` |
| 2 | ¿Qué CVE puede usarse para crear una entrada Meterpreter en la máquina? (Formato: CVE-XXXX-XXXX) | `CVE-2019-0232` |
| 3 | Explota la máquina con Metasploit. | `No answer needed` |
| 4 | ¿Cuál es el contenido de flag1.txt? | `thm{whacking_all_the_elves}` |
| 5 | Escala a root y completa el reto. | `No answer needed` |

### Task 15: Día 13 - Escalada de privilegios (Dirty COW)

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la salida de True + True? | `2` |
| 2 | ¿Cómo se llama la base de datos para instalar librerías de otros desarrolladores? | `PyPi` |
| 3 | ¿Cuál es la salida de bool("False")? | `True` |
| 4 | ¿Qué librería permite descargar el HTML de una página web? | `Requests` |
| 5 | ¿Cuál es la salida del programa del "Código a analizar para la pregunta 5"? | `[1, 2, 3, 6]` |
| 6 | ¿Qué causa la salida anterior? | `Pass by reference` |

### Task 18: Día 16 - API del trineo de Santa

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de puerto del servidor web? | `80` |
| 2 | Sin herramientas de enumeración como Dirbuster, ¿cuál es el directorio de la API? (sin la API key) | `/api/` |
| 3 | ¿Dónde está Santa ahora mismo? | `Winter Wonderland, Hyde Park, London` |
| 4 | Encuentra la API key correcta. Recuerda: es un número impar entre 0 y 100 y, tras demasiados intentos, el trineo de Santa te bloqueará. | `57` |

### Task 19: Día 17 - Ingeniería inversa (Ghidra)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de local_ch cuando se llama a la instrucción movl correspondiente (la primera si hay varias)? | `1` |
| 2 | ¿Cuál es el valor de eax cuando se llama a la instrucción imull? | `6` |
| 3 | ¿Cuál es el valor de local_4h antes de que eax se ponga a 0? | `6` |

### Task 20: Día 18 - Crackeo de contraseñas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtén el hash y prepáralo para crackearlo. | `No answer needed` |
| 2 | ¿Cuál es la contraseña de Santa? | `santapassword321` |
| 3 | Ahora que recuperaste la contraseña, intenta iniciar sesión... ¿Cuál es la flag? | `thm{046af}` |

### Task 21: Día 19 - Explotación web (Naughty List)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de Santa? | `Be good for goodness sake!` |
| 2 | ¿Cuál es la flag del reto? | `THM{EVERYONE_GETS_PRESENTS}` |

### Task 22: Día 20 - Windows Forensics (los Elfos)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca el primer archivo elfo oculto dentro de la carpeta Documents. Léelo. ¿Qué quiere el Elfo 1? | `2 front teeth` |
| 2 | Busca en el escritorio una carpeta oculta con el archivo del Elfo 2. ¿Cómo se llama la película que quiere? | `Scrooged` |
| 3 | Busca en el directorio de Windows una carpeta oculta con los archivos del Elfo 3. ¿Cómo se llama la carpeta oculta? | `3lfthr3e` |
| 4 | ¿Cuántas palabras contiene el primer archivo? | `9999` |
| 5 | ¿Qué 2 palabras están en los índices 551 y 6991 del primer archivo? | `Red Ryder` |
| 6 | Esto es solo la mitad. Busca en el segundo archivo la frase de la pregunta anterior. ¿Qué quiere el Elfo 3? | `Red Ryder BB Gun` |

### Task 23: Día 21 - Windows Forensics (hashes y strings)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el archivo de texto de la carpeta Documents. ¿Cuál es el hash del archivo db.exe? | `596690FFC54AB6101932856E6A78E3A1` |
| 2 | ¿Cuál es el hash del ejecutable misterioso en la carpeta Documents? | `5F037501FB542AD2D9B06EB12AED09F0` |
| 3 | Usando Strings, encuentra la flag oculta dentro del ejecutable. | `THM{f6187e6cbeb1214139ef313e108cb6f9}` |
| 4 | ¿Qué flag se muestra al ejecutar el conector de la base de datos? | `THM{3088731ddc7b9fdeccaed982b07c297c}` |

### Task 24: Día 22 - KeePass

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de la base de datos KeePass? | `thegrinchwashere` |
| 2 | ¿Qué método de codificación aparece como 'Matching ops'? | `Base64` |
| 3 | ¿Cuál es el valor decodificado de la contraseña del Elf Server? | `sn0wM4n!` |
| 4 | ¿Cuál es el valor decodificado de la contraseña de ElfMail? | `ic3Skating!` |
| 5 | Decodifica el último valor. ¿Cuál es la flag? | `THM{657012dcf3d1318dca0ed864f0e70535}` |

### Task 25: Día 23 - Ransomware (Windows Forensics)

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continúa tu aprendizaje en Hacktivities y Pathways de TryHackMe. | `No answer needed` |

---

**Metodología:** El reto se resuelve como un calendario de adviento: cada tarea introduce una habilidad nueva. Las tareas web se resuelven con manipulación de cookies (base64/hex/JSON), subida de archivos, fuzzing con wfuzz/gobuster, SQLi en el panel de Santa y XSS; los días de red usan Wireshark, Nmap, FTP anónimo y enum4linux; la escalada pasa por sudo, Tomcat (CVE-2019-0232) y Dirty COW; el día final combina un sitio tipo TRON con abuso del grupo lxd para escapar del contenedor.

**Learning chain:** cookies y codificación → subida de archivos → enumeración web → SQLi → XSS → análisis de tráfico → servicios de red → escalada de privilegios → OSINT → scripting → ingeniería inversa → forense Windows → ransomware → contenedores.

**MITRE ATT&CK:** T1087 (Account Discovery), T1190 (Exploit Public-Facing Application), T1213 (Data from Information Repositories), T1548 (Abuse Elevation Control Mechanism), T1587 (Develop Capabilities), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - 25 Days of Cyber Security](https://tryhackme.com/room/learncyberin25days)