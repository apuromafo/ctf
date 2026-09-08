# Advent of Cyber 2022

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber4` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber4) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Wireshark / Burp Suite / CyberChef / GoBuster / curl / Hydra / peepdf / Detect It Easy / UPX / Sigma / YARA / MQTT / Logic Analyser / binwalk |
| **Impacto** | Advent of Cyber 2022: análisis de logs y emails, OSINT, SMB/VNC, Laravel RCE, análisis de malware con detección por Sigma/YARA, IoT (UART/MQTT), firmware y cierre con un gestor de contraseñas. |

---

**Contexto:** El Bandit Yeti ataca la aldea de Santa durante la Navidad de 2022. La sala recorre el perfil de un atacante completo: análisis SOC de logs y correos con macros, OSINT vía whois, recursos SMB, escritorio remoto (VNC), ejecución remota en Laravel (CVE-2021-3129), análisis de malware en varias fases (strings, empaquetado, comunicación C2), detección con Sigma/YARA, explotación web con subidas de archivos, SQLi, IoT con lógica UART y MQTT, firmware y mitigaciones de seguridad.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación de la edición 2022: un nuevo villano, el Bandit Yeti, ataca la aldea de Santa. El evento combina retos diarios de análisis SOC, malware, IoT y web con la narrativa navideña. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Historia de fondo

**Explicación:** Se narra el escenario: el Bandit Yeti sabotea la infraestructura de la aldea navideña (logística de regalos, cámara "Wishlist", red interna). La tarea introduce a los personajes y al villano. Solo lectura de la historia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 3: Preparación del evento

**Explicación:** Configuración del laboratorio: Activar la máquina del día, conectar por VPN o AttackBox, comprobar el acceso web a la interfaz del evento y verificar la conectividad de red. Tarea de preparación sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura tu entorno de trabajo. | `No answer needed` |
| 2 | Activa la máquina del día. | `No answer needed` |
| 3 | Accede por VPN/AttackBox. | `No answer needed` |
| 4 | Comprueba el acceso web. | `No answer needed` |
| 5 | Ejecuta los primeros pasos de configuración. | `No answer needed` |
| 6 | Verifica la conectividad de red. | `No answer needed` |
| 7 | Continúa con la configuración del laboratorio. | `No answer needed` |

### Task 4: Despliegue

**Explicación:** Se despliega la máquina objetivo diaria (o el entorno de la interfaz del evento) y se espera a que arranque antes de comenzar la tarea del día.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina objetivo del día. | `No answer needed` |

### Task 5: Primeros pasos

**Explicación:** Introducción interactiva a la interfaz del evento (simplejan / concurso navideño): entender cómo se navega, cómo se presentan las preguntas y cómo usar la API/web del propio Advent of Cyber. Paso guiado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza los primeros pasos del reto. | `No answer needed` |

### Task 6: Día 1 - Portal web del concurso

**Explicación:** Se analiza el portal web del concurso navideño manipulando los datos JSON que llegan de la API (interceptar con Burp o DevTools y editar el objeto del usuario). El administrador del portal es `The Bandit Yeti` y la flag del reto es `THM{IT'S A Y3T1 CHR1$TMA$}`. Lección: no confiar en la lógica de autorización del cliente y validar los datos en el servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario administrador del portal? | `The Bandit Yeti` |
| 2 | ¿Cuál es la flag del reto? | `THM{IT'S A Y3T1 CHR1$TMA$}` |
| 3 | Continúa con la exploración del portal. | `No answer needed` |

### Task 7: Día 2 - Análisis de logs (SOC)

**Explicación:** Primer análisis SOC: sobre la máquina Windows se abre el archivo `webserver.log` (2 días de logs). El incidente ocurrió en `Friday`, desde la IP `10.10.249.191`, que intentó robar `santaslist.txt`; el resultado es la flag `THM{STOLENSANTASLIST}`. Lección: revisar logs web busca patrones de exfiltración (GET sospechoso de archivos sensibles).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina Windows del laboratorio. | `No answer needed` |
| 2 | ¿Cuántos días de logs contiene el archivo analizado? | `2` |
| 3 | ¿Cuál es el nombre del archivo de log que debes revisar? | `webserver.log` |
| 4 | Abre el archivo y empieza el análisis. | `No answer needed` |
| 5 | ¿Qué día de la semana ocurrió el incidente? | `Friday` |
| 6 | ¿Desde qué dirección IP se realizó el ataque? | `10.10.249.191` |
| 7 | ¿Qué archivo se intentó robar del servidor? | `santaslist.txt` |
| 8 | ¿Cuál es la flag del incidente? | `THM{STOLENSANTASLIST}` |
| 9 | Termina el análisis y cierra el caso. | `No answer needed` |

### Task 8: Día 3 - OSINT (whois)

**Explicación:** OSINT con whois: el registrador del dominio es `NAMECHEAP INC` y el análisis da la flag `{THM_OSINT_WORKS}`. También quedó expuesto `config.php` y se detecta el subdominio de pruebas `qa.santagift.shop`, cuya contraseña es `S@nta2022`. Conectando con ese servicio QA (p. ej., escritorio remoto/panel) se cierra la tarea. Lección: las consultas whois/DNS y archivos de configuración expuestos filan infraestructura interna.

```bash
whois santagift.shop
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué organización aparece como registrador (whois) del dominio analizado? | `NAMECHEAP INC` |
| 2 | ¿Cuál es la flag del análisis OSINT? | `{THM_OSINT_WORKS}` |
| 3 | ¿Qué archivo de configuración quedó expuesto en el servidor? | `config.php` |
| 4 | ¿Qué subdominio/servidor de pruebas (QA) se detecta? | `qa.santagift.shop` |
| 5 | ¿Cuál es la contraseña del servicio QA? | `S@nta2022` |
| 6 | Conecta con el servicio QA y termina la tarea. | `No answer needed` |

### Task 9: Día 4 - Enumeración de servicios (SMB)

**Explicación:** Escaneo de puertos contra la máquina del reto: se detecta un servidor web `Apache` y `ssh` como servicio de administración remota. Enumerando el share SMB con enum4linux/smbclient se obtiene la flag `{THM_SANTA_SMB_SERVER}` y se descubre al usuario `santa25`. Lección: enumerar siempre los recursos SMB al descubrir el servicio.

```bash
enum4linux -a MACHINE_IP
smbclient -L //MACHINE_IP -N
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué servidor web se detecta en el escaneo de puertos? | `Apache` |
| 2 | ¿Qué servicio de administración remota aparece en los puertos abiertos? | `ssh` |
| 3 | ¿Cuál es la flag del recurso compartido SMB? | `{THM_SANTA_SMB_SERVER}` |
| 4 | ¿Qué usuario se descubre en el recurso compartido? | `santa25` |
| 5 | Enumerar el share y encontrar los datos del usuario. | `No answer needed` |

### Task 10: Día 5 - Escritorio remoto (VNC)

**Explicación:** El servicio VNC del escritorio remoto se fuerza bruta; la contraseña de acceso es `1q2w3e4r`. Conectando con un cliente VNC se ve en pantalla la flag `THM{I_SEE_YOUR_SCREEN}`. Lección: contraseñas débiles y previsibles en servicios de administración remota expuestos son un riesgo directo.

```bash
ncrack -p 5900 MACHINE_IP -P /usr/share/wordlists/rockyou.txt
# o Hydra sobre el servicio VNC
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de acceso al servicio VNC (fuerza bruta)? | `1q2w3e4r` |
| 2 | ¿Cuál es la flag que se ve en la pantalla del escritorio remoto? | `THM{I_SEE_YOUR_SCREEN}` |
| 3 | Conecta y lee la flag de la sesión. | `No answer needed` |

### Task 11: Día 6 - Análisis de correos (phishing)

**Explicación:** Análisis de cabeceras de un .eml en la interfaz del evento (Jim el analista SOC). El remitente aparente es `chief.elf@santaclaus.thm` ("Chief Elf"), pero el Reply-To real apunta a `murphy.evident@bandityeti.thm`. El correo lleva `3` adjuntos/enlaces, el caso se llama `AoC2022_Email_Analysis` y la puntuación de riesgo es `RISKY`. El adjunto `Division_of_labour-Load_share_plan.doc` (hash `0827bb9a2e7c0628b82256759f0f888ca1abd6a2d903acdb8e44aca6a1a03467`) usa macros de Office (táctica `Defense Evasion`) y se analiza con `macro_hunter`. Lección: ver cabeceras y adjuntos antes de confiar en un correo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Quién envía (de) el correo analizado? | `chief.elf@santaclaus.thm` |
| 2 | ¿Qué dirección responde (reply-to) el correo como remitente real? | `murphy.evident@bandityeti.thm` |
| 3 | ¿Cómo se llama la persona que aparece como remitente legítimo? | `Chief Elf` |
| 4 | ¿Cuántos adjuntos/enlaces lleva el correo? | `3` |
| 5 | ¿Cuál es el nombre del caso de análisis del correo? | `AoC2022_Email_Analysis` |
| 6 | ¿Cuál es la puntuación de riesgo asignada al correo? | `RISKY` |
| 7 | ¿Cómo se llama el documento adjunto al correo? | `Division_of_labour-Load_share_plan.doc` |
| 8 | ¿Cuál es el hash SHA256 del documento adjunto? | `0827bb9a2e7c0628b82256759f0f888ca1abd6a2d903acdb8e44aca6a1a03467` |
| 9 | ¿Qué táctica de MITRE ATT&CK describe el comportamiento del documento? | `Defense Evasion` |
| 10 | ¿Qué herramienta se utiliza para analizar las macros del documento? | `macro_hunter` |
| 11 | Completa el análisis del documento con macros. | `No answer needed` |

### Task 12: Día 7 - Análisis de malware (documento)

**Explicación:** Análisis del PDF malicioso con pdf-parser/pdfid: el campo producer es `9.49.0`, hay `10` modificaciones/acciones, el ejecutable descargado es `mysterygift.exe` y la URL del C2 (defanged) es `hxxps[://]cdn[.]bandityeti[.]THM/files/index/`. La flag del análisis es `THM_MYSTERY_FLAG`. Lección: los documentos pueden descargar y ejecutar payloads; parsear sus objetos revela dónde apuntan.

```bash
pdf-parser -f -a documento.pdf
pdfid documento.pdf
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la versión/creador (producer) del PDF analizado? | `9.49.0` |
| 2 | ¿Cuántas modificaciones/acciones se detectan en el documento? | `10` |
| 3 | ¿Qué ejecutable se descarga e intenta ejecutar? | `mysterygift.exe` |
| 4 | ¿Cuál es la URL del C2 al que accede (defanged)? | `hxxps[://]cdn[.]bandityeti[.]THM/files/index/` |
| 5 | ¿Cuál es la flag del análisis de malware? | `THM_MYSTERY_FLAG` |
| 6 | Continúa con la cadena de análisis del documento. | `No answer needed` |

### Task 13: Día 8 - Análisis de tráfico

**Explicación:** Análisis de una captura PCAP con Wireshark: siguiendo streams HTTP y buscando cadenas (Follow TCP Stream / "flag" en el paquete) aparece `flag{411_ur_37h_15_m1n3}`. Lección: el contenido de los paquetes puede contener credenciales, archivos o flags; usar filtros y búsquedas sobre el stream.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre la captura y empieza el análisis de tráfico. | `No answer needed` |
| 2 | ¿Cuál es la flag encontrada en el tráfico capturado? | `flag{411_ur_37h_15_m1n3}` |
| 3 | Finaliza la revisión de paquetes. | `No answer needed` |

### Task 14: Día 9 - Explotación web (Laravel)

**Explicación:** El servicio web del puerto `80` usa `laravel` y es vulnerable a `CVE-2021-3129` (Ignition, RCE). Con Metasploit se obtiene una sesión; `sessions -u -1` la eleva a interactiva/Meterpreter. La presencia de `/.dockerenv` confirma un contenedor; `.env` guarda las credenciales; la tabla `users` contiene al usuario con contraseña `p4$$w0rd`. Desde el contenedor se ven abiertos `22,80` en el host interno. La flag del contenedor es `THM{47C61A0FA8738BA77308A8A600F88E4B}`. Lección: pivote y reconocimiento interno tras RCE.

```bash
use exploit/multi/http/laravel_ignition_rce
set RHOSTS MACHINE_IP
run
# luego en la sesión:
sessions -u -1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto expone el servicio web vulnerable? | `80` |
| 2 | ¿Qué framework usa la aplicación web? | `laravel` |
| 3 | ¿Qué CVE permite la ejecución remota de código (Ignition)? | `CVE-2021-3129` |
| 4 | ¿Qué comando se usa para pasar a la sesión interactiva dentro de Metasploit? | `sessions -u -1` |
| 5 | ¿Qué archivo del sistema confirma que se está dentro de un contenedor? | `/.dockerenv` |
| 6 | ¿Qué archivo de configuración contiene las credenciales de la aplicación? | `.env` |
| 7 | ¿Cuál es el nombre de la tabla donde se almacenan los usuarios? | `users` |
| 8 | ¿Cuál es la contraseña del usuario encontrado? | `p4$$w0rd` |
| 9 | ¿Qué puertos están abiertos en el host interno de la red Docker? | `22,80` |
| 10 | ¿Cuál es la flag del contenedor comprometido? | `THM{47C61A0FA8738BA77308A8A600F88E4B}` |
| 11 | Escala y pivota al host interno. | `No answer needed` |

### Task 15: Día 10 - Almacenamiento en la nube (S3)

**Explicación:** El bucket S3 de la tienda navideña está listable públicamente. Navegando por el contenido se encuentran dos flags: `THM{5_star_Fl4gzzz}` y `THM{yetiyetiyetiflagflagflag}`. Lección: buckets S3 con permisos públicos (ListObjects) exponen todo su contenido; revisar siempre los permisos.

```bash
aws s3 ls s3://BUCKET --no-sign-request
aws s3 cp --recursive s3://BUCKET ./ --no-sign-request
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag encontrada en el bucket? | `THM{5_star_Fl4gzzz}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{yetiyetiyetiflagflagflag}` |
| 3 | Revisa los permisos y el objeto del bucket. | `No answer needed` |

### Task 16: Día 11 - Análisis de malware (strings)

**Explicación:** Extracción de cadenas de `mysterygift.exe` con `strings`: aparecen `10` URLs únicas, la fecha de compilación es `2040` y la última consulta devuelve `16` entradas clave. `strings` es la primera técnica de triage para confirmar dominios, URLs y comandos embebidos.

```bash
file mysterygift.exe
strings mysterygift.exe | grep -Ei "http|url"
strings mysterygift.exe | head -50
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántas URLs únicas se localizan con la utilidad strings? | `10` |
| 2 | ¿Cómo se llama el archivo de malware analizado? | `mysterygift.exe` |
| 3 | ¿Qué año/fecha de compilación aparece en los resultados? | `2040` |
| 4 | ¿Cuántos resultados/entradas clave devuelve la última consulta? | `16` |
| 5 | Documenta los indicadores extraídos del binario. | `No answer needed` |

### Task 17: Día 12 - Análisis de malware (DIE/UPX)

**Explicación:** Con Detect It Easy se identifica que `mysterygift.exe` es `64-bit`, está empaquetado con `upx` y escrito en `nim`. Desempaquetado (`upx -d`) muestra `2` secciones. El malware persiste vía `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` y deja `C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\wishes.bat`. Crea `test.jpg,wishes.bat`, contacta `bestfestivalcompany.thm,virustotal.com` y su C2 (favicon) es `http://bestfestivalcompany.thm/favicon.ico`. Lección: DIE + desempaquetado + strings para registrar IoC.

```bash
diec mysterygift.exe
upx -d mysterygift.exe -o mysterygift_unpacked.exe
strings mysterygift_unpacked.exe | grep -iE "HKCU|favicon"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué arquitectura tiene el ejecutable? | `64-bit` |
| 2 | ¿Con qué empaquetador está protegido el binario? | `upx` |
| 3 | ¿En qué lenguaje de programación está escrito el malware? | `nim` |
| 4 | ¿Cuántas secciones muestra el ejecutable tras desempaquetarlo? | `2` |
| 5 | ¿Qué clave de registro se usa para la persistencia? | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| 6 | ¿Cuál es la ruta del archivo que se deja en la carpeta de inicio de sesión? | `C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\wishes.bat` |
| 7 | ¿Qué archivos crea el malware (separados por coma)? | `test.jpg,wishes.bat` |
| 8 | ¿Qué dominios contacta el malware (separados por coma)? | `bestfestivalcompany.thm,virustotal.com` |
| 9 | ¿Cuál es la URL del C2 usada por el malware (favicon)? | `http://bestfestivalcompany.thm/favicon.ico` |
| 10 | Registra los IoC del análisis completo. | `No answer needed` |

### Task 18: Día 13 - Análisis de PCAP y detección

**Explicación:** Análisis de la captura del C2 con Wireshark (aquí se usa zeek + grep sobre conn.log/dns.log). El primer valor de la métrica de detección es `0.3`; hay sesión RDP en `3389` (protocolo `RDP`). DNS consulta `bestfestivalcompany[.]thm,cdn[.]bandityeti[.]thm`; se descargan `favicon[.]ico,mysterygift[.]exe`; la IP del centro de C2 es `10[.]10[.]29[.]186` resuelta por `cdn[.]bandityeti[.]thm`; el User-Agent del malware es `Nim httpclient/1.6.8`; la muestra tiene SHA256 `0ce160a54d10f8e81448d0360af5c2948ff6a4dbb493fe4be756fc3e2c3f900f` y al final contacta `20[.]99[.]133[.]109,20[.]99[.]184[.]37,23[.]216[.]147[.]64,23[.]216[.]147[.]76`. Lección: correlacionar DNS, HTTP y destinos para reconstruir la cadena de infección.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué valor de la métrica de detección aparece en la primera pregunta? | `0.3` |
| 2 | ¿Qué puerto se asociado al protocolo RDP en la captura? | `3389` |
| 3 | ¿Qué protocolo se detecta en esa sesión? | `RDP` |
| 4 | ¿Qué dominios se consultan por DNS (defanged, separados por coma)? | `bestfestivalcompany[.]thm,cdn[.]bandityeti[.]thm` |
| 5 | ¿Qué archivos se solicitan en la descarga (defanged, separados por coma)? | `favicon[.]ico,mysterygift[.]exe` |
| 6 | ¿Qué dirección IP del centro de la infraestructura aparece en el tráfico? | `10[.]10[.]29[.]186` |
| 7 | ¿Qué dominio del atacante resuelve a esa misma IP? | `cdn[.]bandityeti[.]thm` |
| 8 | ¿Qué user-agent utiliza el malware en sus peticiones? | `Nim httpclient/1.6.8` |
| 9 | ¿Cuál es el hash SHA256 de la muestra analizada? | `0ce160a54d10f8e81448d0360af5c2948ff6a4dbb493fe4be756fc3e2c3f900f` |
| 10 | ¿Qué IP de destino se observan al final de la cadena (separadas por coma, defanged)? | `20[.]99[.]133[.]109,20[.]99[.]184[.]37,23[.]216[.]147[.]64,23[.]216[.]147[.]76` |
| 11 | Correlaciona los hallazgos con las reglas de detección. | `No answer needed` |

### Task 19: Día 14 - Superficie de red

**Explicación:** Escaneo de todo el rango/VM: el host analizado tiene `134` puertos abiertos, una superficie enorme para un servidor. La flag es `THM{CLOSE_THE_DOOR}`. Hay que diseñar la mitigación (cerrar puertos no usados, aplicar firewall) para reducir la exposición. Lección: cuantificar la superficie atacable y reducirla por defecto.

```bash
nmap -p- --min-rate 5000 MACHINE_IP
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos abiertos se detectan en el host analizado? | `134` |
| 2 | ¿Cuál es la flag de la tarea? | `THM{CLOSE_THE_DOOR}` |
| 3 | Diseña la mitigación para reducir la exposición. | `No answer needed` |

### Task 20: Día 15 - Subida de archivos (RCE)

**Explicación:** El panel de subida (acceso como `SantaSideKick2`) permite una política `Unrestricted` de subida, lo que da RCE con una webshell y la flag `THM{Naughty.File.Uploads.Can.Get.You.RCE}`. Los controles correctos serían: `File Extension Validation` (validar extensión), `File Renaming` (renombrar para eliminar webshells con el nombre original) y `Malware Scanning` (analizar contenido). Lección: tres capas de defensa para subidas de archivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué política de subida de archivos permite obtener una shell? | `Unrestricted` |
| 2 | ¿Con qué usuario accedes al panel de subida? | `SantaSideKick2` |
| 3 | ¿Cuál es la flag del reto? | `THM{Naughty.File.Uploads.Can.Get.You.RCE}` |
| 4 | ¿Qué control hay que implementar para validar el tipo de archivo? | `File Extension Validation` |
| 5 | ¿Qué control asegura que un webshell no conserve su nombre original? | `File Renaming` |
| 6 | ¿Qué control analiza el contenido de los archivos subidos? | `Malware Scanning` |
| 7 | Implementa los tres controles en el servidor de pruebas. | `No answer needed` |

### Task 21: Día 16 - Seguridad en el código (Secure Coding)

**Explicación:** Cuatro ejercicios interactivos de código con bugs: las flags son `THM{McCode, Elf McCode}`, `THM{KodeNRoll}`, `THM{Are we secure yet?}` y `THM{SQLi_who???}` (este último introduce una inyección SQL en la consulta). Lección: aplicar saneamiento/validación y consultas parametrizadas en el código.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del primer ejercicio de código? | `THM{McCode, Elf McCode}` |
| 2 | ¿Cuál es la flag del segundo ejercicio? | `THM{KodeNRoll}` |
| 3 | ¿Cuál es la flag del tercer ejercicio? | `THM{Are we secure yet?}` |
| 4 | ¿Cuál es la flag del ejercicio final? | `THM{SQLi_who???}` |
| 5 | Revisa las buenas prácticas de codificación segura. | `No answer needed` |

### Task 22: Día 17 - Base de datos (SQLi)

**Explicación:** Práctica de inyección SQL contra una base de datos en la interfaz del riesgo (peticiones con parámetros manipulables). La primera consulta devuelve `8` registros; aparece el usuario `User35`; el segundo apartado da `11` resultados; la cuarta consulta responde `8`; los dominios del primer y segundo registro son `amg.com` y `fedfull.com`; el usuario ligado al dato buscado es `hussain.volt`; la penúltima consulta suma `16` y la última responde `7`. Lección: enumerar registros y columnas mediante consultas inyectadas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos registros devuelve la consulta de la base de datos? | `8` |
| 2 | ¿Cuál es el nombre del primer usuario encontrado? | `User35` |
| 3 | ¿Cuántos resultados se obtienen en la consulta del apartado 2? | `11` |
| 4 | ¿Cuál es el valor que responde a la cuarta consulta? | `8` |
| 5 | ¿Qué dominio aparece en el primer registro del resultado? | `amg.com` |
| 6 | ¿Qué dominio se asocia al segundo registro? | `fedfull.com` |
| 7 | ¿Qué nombre de usuario se relaciona con el dato buscado? | `hussain.volt` |
| 8 | ¿Cuál es el total de elementos de la penúltima consulta? | `16` |
| 9 | ¿Cuál es el resultado de la última consulta del reto? | `7` |
| 10 | Explora el resto de la base de datos. | `No answer needed` |

### Task 23: Día 18 - Detección (Sigma/YARA)

**Explicación:** Detección sobre el host comprometido: la primera flag es `THM{n0t_just_your_u$ser}`; el proceso que ejecuta el payload es `BanditYetiMini` (flag `THM{wh@t_1s_Runn1ng_H3r3}`); la regla Sigma detecta la tarea programada `SIGMA_AOC2022\Bandit Yeti` (flag `THM{sch3dule_0npo1nt_101}`) y el binario asociado tiene MD5 `2F6CE97FAF2D5EEA919E4393BDD416A7`. Se ajusta la regla y se valida contra el host. Lección: convertir IoC en reglas de detección (Sigma/YARA).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag de la tarea de detección? | `THM{n0t_just_your_u$ser}` |
| 2 | ¿Cómo se llama el proceso que ejecuta el payload malicioso? | `BanditYetiMini` |
| 3 | ¿Cuál es la flag del apartado de procesos en ejecución? | `THM{wh@t_1s_Runn1ng_H3r3}` |
| 4 | ¿Qué tarea programada detecta la regla Sigma (formato CARPETA\Nombre)? | `SIGMA_AOC2022\Bandit Yeti` |
| 5 | ¿Cuál es la flag relacionada con la persistencia por tarea programada? | `THM{sch3dule_0npo1nt_101}` |
| 6 | ¿Cuál es el hash MD5 del binario asociado a la tarea? | `2F6CE97FAF2D5EEA919E4393BDD416A7` |
| 7 | Ajusta la regla de detección y valídala contra el host. | `No answer needed` |

### Task 24: Día 19 - Hardware (UART)

**Explicación:** Con un `Logic Analyser` se captura la comunicación del dispositivo. Siguiendo el manual del conector: la tierra/alimentación (`Nay` los pines de poder no conectados), TX con señal (`Yea`), el pin de datos secundario sin conectar (`Nay`), la alimentación restante sin conectar (`Nay`) y RX con señal (`Yea`). El contador del conector de prueba marca `1008` y la velocidad de baudios del enlace es `9600`; la flag es `THM{Hacking.Hardware.Is.Fun}`. Lección: identificar pines TX/RX/GND y baud rate para leer tráfico UART.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta se utiliza para capturar la comunicación del dispositivo? | `Logic Analyser` |
| 2 | ¿Se conecta el pin de tierra/alimentación del conector UART? | `Nay` |
| 3 | ¿Se detecta señal en el pin TX del dispositivo? | `Yea` |
| 4 | ¿Se conecta el pin de datos secundario del conector? | `Nay` |
| 5 | ¿Se conecta el pin de alimentación restante? | `Nay` |
| 6 | ¿Se recibe señal en el pin RX del dispositivo? | `Yea` |
| 7 | ¿Qué valor aparece en el contador del conector de prueba? | `1008` |
| 8 | ¿Cuál es la velocidad de baudios del enlace UART? | `9600` |
| 9 | ¿Cuál es la flag del reto de hardware? | `THM{Hacking.Hardware.Is.Fun}` |
| 10 | Documenta la captura de la tarjeta. | `No answer needed` |

### Task 25: Día 20 - Análisis de firmware

**Explicación:** Extracción del firmware con `binwalk`: la primera flag es `THM{WE_GOT_THE_FIRMWARE_CODE}`; desempaquetando el sistema de archivos aparece la contraseña `Santa@2022` y el kernel ejecutado es `2.6.31`. Lección: `binwalk -e` sobre firmware revela filesystems completos con credenciales y configuraciones.

```bash
binwalk -Me firmware.bin
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del firmware analizado? | `THM{WE_GOT_THE_FIRMWARE_CODE}` |
| 2 | ¿Cuál es la contraseña extraída al desempaquetar el firmware? | `Santa@2022` |
| 3 | ¿Qué versión de kernel ejecuta el sistema del firmware? | `2.6.31` |
| 4 | Lista los archivos clave extraídos del firmware. | `No answer needed` |

### Task 26: Día 21 - IoT (MQTT)

**Explicación:** El dispositivo IoT usa MQTT (mosquitto) en el puerto `1883`. Suscribiéndose/publicando en los topics del dispositivo: la primera suscripción responde `y`, la versión del servicio es `1.6.9` y publicando en el topic correcto de la cámara se obtiene `THM{UR_CAMERA_IS_MINE}`. Lección: MQTT sin autenticación permite leer y controlar dispositivos.

```bash
mosquitto_pub -h MACHINE_IP -p 1883 -t 'topic/camara' -m 'mensaje'
mosquitto_sub -h MACHINE_IP -p 1883 -t '#'
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto utiliza el servicio MQTT del dispositivo? | `1883` |
| 2 | ¿Cómo responde el dispositivo a la primera suscripción (respuesta corta)? | `y` |
| 3 | ¿Qué versión del servicio mosquitto/firmware se muestra? | `1.6.9` |
| 4 | ¿Cuál es la flag de la cámara IoT? | `THM{UR_CAMERA_IS_MINE}` |
| 5 | Interactúa con el topic de la cámara para cerrar el reto. | `No answer needed` |

### Task 27: Día 22 - Reducción de superficie de ataque

**Explicación:** Se aplican reglas de mitigación (Windows Defender o firewall/local hardening) sobre el host de pruebas para reducir su superficie de ataque; la flag es `THM{4TT4CK SURF4C3 R3DUC3D}`. Lección: aplicar medidas de reducción (ASR, reglas de firewall, deshabilitar servicios) de forma medible.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto de reducción de superficie? | `THM{4TT4CK SURF4C3 R3DUC3D}` |
| 2 | Aplica las reglas de mitigación en el host de pruebas. | `No answer needed` |

### Task 28: Día 23 - Gestor de contraseñas (Secret Vault)

**Explicación:** Auditoría del gestor (patrón Bitwarden/Vaultwarden) del equipo. El cofre compartido se abre con `S3cr3tV@ultPW` (flag `THM{EZ_fl@6!}`); se filtra la contraseña compartida `MilkAndCookies`; la segunda cuenta del cofre usa `3XtrR@_S3cr3tV@ultPW` (flag `THM{m0@r_5t3pS_n0w!}`); la app interna comparte `BanoffeePie`; las apps del cofre usan `H0tCh0coL@t3_01` y `H0tCh0coL@t3_02`; el nuevo usuario es `N3w4nd1m` con la promovida a admin `Pr0v3dV@ultPW`; la combinación descifrada es `N3w4nd1mPr0v3dV@ultPW` (flag `THM{B@d_Y3t1_1s_n@u6hty}`); la consulta final da `2845` y el cierre entrega `THM{D3f3n5e_1n_D3pth_1s_k00L!!}`. Lección: gestión de privilegios y contraseñas compartidas mal controladas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del cofre secreto compartido? | `S3cr3tV@ultPW` |
| 2 | ¿Cuál es la primera flag del gestor de contraseñas? | `THM{EZ_fl@6!}` |
| 3 | ¿Qué contraseña compartida se filtra por descuido del equipo? | `MilkAndCookies` |
| 4 | ¿Cuál es la contraseña de la segunda cuenta del cofre? | `3XtrR@_S3cr3tV@ultPW` |
| 5 | ¿Cuál es la flag de la segunda parte? | `THM{m0@r_5t3pS_n0w!}` |
| 6 | ¿Qué credencial aparece como contraseña compartida en la aplicación interna? | `BanoffeePie` |
| 7 | ¿Cuál es la contraseña de la primera aplicación del cofre? | `H0tCh0coL@t3_01` |
| 8 | ¿Cuál es la contraseña de la segunda aplicación? | `H0tCh0coL@t3_02` |
| 9 | ¿Cuál es el nuevo nombre de usuario creado en el cofre? | `N3w4nd1m` |
| 10 | ¿Cuál es la contraseña de la cuenta promovida a administrador? | `Pr0v3dV@ultPW` |
| 11 | ¿Cuál es la contraseña descifrada de la combinación final? | `N3w4nd1mPr0v3dV@ultPW` |
| 12 | ¿Cuál es la flag de la parte final del gestor? | `THM{B@d_Y3t1_1s_n@u6hty}` |
| 13 | ¿Cuál es el número de la consulta final del reto? | `2845` |
| 14 | ¿Cuál es la flag de conclusiones (defensa en profundidad)? | `THM{D3f3n5e_1n_D3pth_1s_k00L!!}` |
| 15 | Asegura el cofre con las credenciales corregidas. | `No answer needed` |

### Task 29: Conclusión

**Explicación:** Cierre del evento: la flag de agradecimiento es `THM{AoC2022!thank_you!}`; después se comparte el progreso en redes y se rellena la encuesta del evento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por el evento. Introduce la flag de cierre. | `THM{AoC2022!thank_you!}` |
| 2 | Comparte tu progreso en las redes. | `No answer needed` |
| 3 | Termina la encuesta del evento. | `No answer needed` |

### Task 30: Encuesta

**Explicación:** Encuesta de valoración del evento: si te ha gustado, la respuesta es `Yea` (por la temática navideña del After Hack).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Te ha gustado el evento de este año? | `Yea` |

---

**Metodología:** El día 1 usa la web del concurso con manipulación de JSON. Los días SOC revisan logs de servidor y correos con macros (macro_hunter). La fase ofensiva combina OSINT con whois, enumeración SMB, brute force de VNC y explotación de Laravel con CVE-2021-3129 (pivote a la red Docker). El análisis de malware cubre strings, Detect It Easy, desempaquetado UPX, identificando Nim como lenguaje y su C2, con detección final por reglas Sigma/YARA. La parte hardware usa un Logic Analyser sobre UART y MQTT; y el firmware se extrae con binwalk. Cierra con el compromiso de un gestor de contraseñas y medidas de defensa en profundidad.

**Learning chain:** web/JSON → análisis SOC → OSINT → SMB/VNC → phishing email → malware (parsing, strings, empaquetado) → Sigma/YARA → Laravel RCE → S3 → upload RCE → SQLi → hardware UART → firmware → MQTT → hardening → secret vault.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1566 (Phishing), T1204 (User Execution), T1059 (Command and Scripting Interpreter), T1547 (Boot or Logon Autostart Execution), T1105 (Ingress Tool Transfer), T1071 (Application Layer Protocol), T1552 (Unsecured Credentials)

**Fuente:** [TryHackMe - Advent of Cyber 2022](https://tryhackme.com/room/adventofcyber4)