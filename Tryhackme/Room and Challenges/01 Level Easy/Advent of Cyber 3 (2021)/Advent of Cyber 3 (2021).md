# Advent of Cyber 3 (2021)

| **Dificultad** | Easy |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber3` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber3) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | CyberChef / Wireshark / Nmap / Hydra / MSSQL / NFS / Docker / ExifTool / ClamAV / PowerShell (Invoke-Nightmare) / John |
| **Impacto** | Tercer Advent of Cyber: IDOR, cookies, WordPress, LFI, MSSQL, NFS, potencia su Windows con Iperius y PrintNightmare, y cierra con phishing, S3, Docker y OSINT. |

---

**Contexto:** Edición 2021 del Advent of Cyber, centrada en el Grinch y McSkidy. Los primeros días explotan identificadores (IDOR) y cookies de sesión, siguen con WordPress, LFI en Flask, SSRF/MongoDB, forense Windows de malware, FTP con Hydra, Apache 2.4.49 (CVE-2021-42013), MSSQL, NFS, escalada de privilegios en Windows con Iperius, crackeo de zips, OSINT de criptomonedas, buckets S3, capas de Docker, análisis de phishing, pruebas EICAR con ClamAV, análisis de metadatos, envío de correos SMTP, PrintNightmare y crackeo final de contraseñas.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Preparación del evento

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura tu entorno de trabajo. | `No answer needed` |
| 2 | Activa la máquina del día. | `No answer needed` |
| 3 | Accede por VPN/AttackBox. | `No answer needed` |
| 4 | Comprueba el acceso web. | `No answer needed` |

### Task 3: Historia de fondo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 4: Despliegue

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina objetivo del día. | `No answer needed` |

### Task 5: Primeros pasos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza los primeros pasos del reto. | `No answer needed` |

### Task 6: Día 1 - IDOR (Identificadores inseguros)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario '0' de la API? | `The Boss!` |
| 2 | ¿Cuál es el rol asociado al primer empleado? | `Build Manager` |
| 3 | ¿Cuál es el rol de la segunda persona implicada? | `Mischief Manager` |
| 4 | ¿Cuál es la flag del reto? | `THM{AOC_IDOR_2B34BHI3}` |
| 5 | Continúa con la exploración de la API. | `No answer needed` |
| 6 | Termina el apartado de enumeración. | `No answer needed` |

### Task 7: Día 2 - Cookies y autenticación

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Inicia sesión en la aplicación para generar tu cookie. | `No answer needed` |
| 2 | ¿Cuál es el nombre de la cookie de autenticación? | `user-auth` |
| 3 | ¿En qué formato está codificado el valor de la cookie? | `hexadecimal` |
| 4 | Tras decodificarla, ¿en qué formato están los datos? | `JSON` |
| 5 | ¿Cuál es el valor en bruto (hex) de la cookie de admin? | `7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d` |
| 6 | ¿Qué sección interna aparece al manipular la cookie? | `HR` |
| 7 | ¿Qué aplicación interna se puede abrir? | `Application` |
| 8 | Explota la cookie para acceder al resto de la aplicación. | `No answer needed` |
| 9 | Continúa y comprueba el panel interno. | `No answer needed` |

### Task 8: Día 3 - Software CMS (brute force/WordPress)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario con acceso de administrador que encuentras? | `admin` |
| 2 | ¿Qué cuenta de usuario confirma el acceso administrativo? | `administrator` |
| 3 | ¿Cuál es la flag del acceso administrativo? | `THM{ADM1N_AC3SS}` |

### Task 9: Día 4 - Sesiones y web cache

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue el flujo de la aplicación y las peticiones. | `No answer needed` |
| 2 | Manipula la sesión y la caché web. | `No answer needed` |
| 3 | ¿Qué componente/cabecera usas para el ataque? | `cookie` |
| 4 | ¿Cuál es la flag del reto? | `THM{SANTA_DELIVERS}` |

### Task 10: Día 5 - Reconocimiento web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida tras enumerar la aplicación? | `THM{NO_MORE_BUTTMAS}` |

### Task 11: Día 6 - Local File Inclusion (Flask)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué error/mensaje devuelve la aplicación al probar la entrada? | `err` |
| 2 | ¿Cuál es el contenido de la primera flag? | `THM{d29e08941cf7fe41df55f1a7da6c4c06}` |
| 3 | ¿Cuál es el contenido de la segunda flag? | `THM{791d43d46018a0d89361dbf60d5d9eb8}` |
| 4 | ¿Qué credenciales (usuario:contraseña) encuentras en el sistema? | `McSkidy:A0C315Aw3s0m` |
| 5 | ¿Cuál es el contenido de la tercera flag? | `THM{552f313b52e3c3dbf5257d8c6db7f6f1}` |
| 6 | ¿Cuál es el nombre del recurso/nombre clave del directorio LFI? | `lfi-aoc-awesome-59aedca683fff9261263bb084880c965` |
| 7 | Consolida el acceso con el LFI. | `No answer needed` |

### Task 12: Día 7 - Base de datos (MongoDB/SSRF)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el contenido de la primera flag? | `THM{8814a5e6662a9763f7df23ee59d944f9}` |
| 2 | ¿Cuál es el contenido de la segunda flag? | `THM{b6b304f5d5834a4d089b570840b467a8}` |
| 3 | ¿Cuál es el contenido de la tercera flag? | `THM{2ec099f2d602cc4968c5267970be1326}` |
| 4 | ¿Qué entrada de la base de datos contiene la clave del usuario admin? | `ID:6184f516ef6da50433f100f4:mcskidy:admin` |

### Task 13: Día 8 - Forense de malware (Windows)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Arranca la máquina Windows del laboratorio. | `No answer needed` |
| 2 | ¿Qué sistema operativo ejecuta la máquina Windows? | `Microsoft Windows 11 Pro` |
| 3 | ¿Cuál es la contraseña que se encuentra en el escritorio/registro? | `grinchstolechristmas` |
| 4 | ¿Cuál es la ruta del archivo UsrClass.dat que registra las ejecuciones? | `C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat` |
| 5 | ¿Qué herramienta se usó para transferir/descargar el archivo al laboratorio? | `certutil.exe` |
| 6 | Analiza las trazas del laboratorio. | `No answer needed` |
| 7 | ¿Qué directorio oculto aparece en el repositorio del atacante? | `.github` |
| 8 | ¿Cómo se llama el archivo comprimido del paquete? | `bag_of_toys.zip` |
| 9 | ¿Qué contraseña de extracción/identificador usa el paquete? | `Grinchiest` |
| 10 | ¿Cuál es el nombre de la operación/repositorio del atacante? | `operation-bag-of-toys` |
| 11 | ¿Qué instalador ejecuta el paquete malicioso? | `uharc-cmd-install.exe` |
| 12 | ¿Cuál es la contraseña del archivo comprimido interno? | `GRINCHMAS` |
| 13 | Sigue el rastro del paquete. | `No answer needed` |
| 14 | ¿Cuál es la contraseña de la siguiente fase/aplicación? | `TheGrinchiestGrinchmasOfAll` |
| 15 | ¿Cuál es el valor numérico que cierra el reto? | `228` |

### Task 14: Día 9 - FTP (Hydra)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿A qué página/directorio te lleva la web del servicio? | `login` |
| 2 | ¿Qué credenciales (usuario:contraseña) obtienes del análisis? | `McSkidy:Christmas2021!` |
| 3 | ¿Qué flag trae el user-agent personalizado que debes enviar? | `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}` |
| 4 | ¿Cuál es la flag del servidor FTP? | `THM{dd63a80bf9fdd21aabbf70af7438c257}` |
| 5 | ¿Cuál es la contraseña real de McSkidy en el FTP? | `TryH@ckM3!` |
| 6 | ¿Qué comando FTP se utiliza para subir un archivo al servidor? | `STOR` |
| 7 | ¿Cuál es la contraseña encontrada en las notas del servidor? | `123^-^321` |

### Task 15: Día 10 - Escaneo de puertos (Apache 2.4.49)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos abiertos se detectan en el escaneo inicial? | `2` |
| 2 | ¿Qué puerto corresponde al servicio SSH? | `22` |
| 3 | ¿Qué protocolo/nombre recibe el servicio del servidor web? | `HTTP` |
| 4 | ¿Se permite el acceso con las credenciales por defecto (sí/no)? | `Y` |
| 5 | ¿Qué versión de Apache httpd se está ejecutando? | `Apache httpd 2.4.49` |
| 6 | ¿Qué CVE permite explotar el servidor web? | `CVE-2021-42013` |
| 7 | ¿Cuál es el número del puerto adicional con acceso? | `20212` |
| 8 | ¿Qué servicio se ejecuta en ese puerto adicional? | `telnetd` |
| 9 | Explota la vulnerabilidad del servidor para terminar la tarea. | `No answer needed` |

### Task 16: Día 11 - Inyección SQL sobre MSSQL

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto usa el servicio de base de datos MSSQL? | `1433` |
| 2 | ¿Qué símbolo/prompt muestra la shell interactiva SQL? | `1>` |
| 3 | ¿Qué respuesta/valor se revela en la primera consulta? | `Rudolph` |
| 4 | ¿Qué ciudad/ubicación se devuelve en la consulta siguiente? | `Prague` |
| 5 | ¿Qué puerto UDP adicional se detecta en el host? | `25000` |
| 6 | ¿Cuál es la flag del reto? | `THM{YjtKeUy2qT3v5dDH}` |
| 7 | Continúa con la explotación de la base de datos. | `No answer needed` |

### Task 17: Día 12 - NFS

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos relevantes se detectan en el escaneo del host? | `7` |
| 2 | ¿Qué puerto usa el servicio NFS? | `2049` |
| 3 | ¿Cuántos shares/montajes se pueden enumerar? | `4` |
| 4 | ¿Cuántos archivos hay dentro del share montado? | `3` |
| 5 | ¿Cuál es el nombre del primer archivo encontrado? | `Meditations` |
| 6 | ¿Qué carpeta/fichero contiene el dato confidencial? | `confidential` |
| 7 | ¿Cuál es el contenido (hash) de la flag? | `3e2d315a38f377f304f5598dc2f044de` |

### Task 18: Día 13 - Escalada de privilegios Windows (Iperius)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué credencial de acceso inicial se menciona en el laboratorio? | `pepper` |
| 2 | ¿Qué versión de Windows ejecuta la máquina? | `10.0.17763 N/A Build 17763` |
| 3 | ¿Cómo se llama el servicio vulnerable que permite escalar? | `IperiusSvc` |
| 4 | ¿Cuál es la ruta del ejecutable del servicio Iperius? | `C:\Program Files (x86)\Iperius Backup\IperiusService.exe` |
| 5 | ¿Qué cuenta de usuario (dominio\usuario) se emplea para la escalada? | `the-grinch-hack\thegrinch` |
| 6 | ¿Cuál es la flag encontrada en el sistema? | `THM-736635221` |
| 7 | ¿Cuál es la contraseña del usuario thegrinch? | `jazzercize` |

### Task 19: Día 14 - Crackeo de archivos comprimidos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos archivos hay en el directorio del reto? | `4` |
| 2 | ¿Cuántos de ellos son archivos comprimidos? | `4` |
| 3 | ¿Cuál es la contraseña del primer archivo comprimido? | `ZUP42` |
| 4 | ¿Cuál es la contraseña/flag del archivo final? | `DI3H4rdIsTheBestX-masMovie!` |

### Task 20: Día 15 - Preparación del siguiente bloque

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el material teórico de la sección. | `No answer needed` |
| 2 | Sigue el vídeo/guía de preparación. | `No answer needed` |

### Task 21: Día 16 - OSINT (Grinch Who)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Inicia la investigación OSINT siguiendo las pistas. | `No answer needed` |
| 2 | ¿Cuál es el nombre de usuario del sospechoso en las redes sociales? | `GrinchWho31` |
| 3 | ¿En qué red social se descubrió su actividad pública? | `Twitter` |
| 4 | ¿Cuál es la primera dirección de criptomoneda asociada (sin prefijo http)? | `1GW8QR7CWW3cpvVPGMCF5tZz4j96ncEgrVaR` |
| 5 | ¿Qué sitio web de identidad/verificación mantiene el sospechoso? | `keybase.io` |
| 6 | ¿Cuál es la segunda dirección de criptomoneda (prefijo bc1q)? | `bc1q5q2w2x6yka5gchr89988p2c8w8nquem6tndw2f` |
| 7 | ¿Qué plataforma de código confirma su identidad? | `GitHub` |
| 8 | ¿Cuál es el correo electrónico asociado a la cuenta? | `DonteHeath21@gmail.com` |
| 9 | ¿Cuál es el nombre real del sospechoso? | `Donte Heath` |

### Task 22: Día 17 - Buckets S3 (AWS)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hostname subyacente del bucket S3? | `images.bestfestivalcompany.com` |
| 2 | ¿Qué mensaje se puede leer en el bucket público? | `It's easy to get your elves data when you leave it so easy to find!` |
| 3 | ¿Cómo se llama el archivo de backup que se descarga? | `wp-backup.zip` |
| 4 | ¿Cuál es la Access Key ID de AWS encontrada? | `AKIAQI52OJVCPZXFYAOI` |
| 5 | ¿Cuál es el Account ID de AWS del recurso? | `019181489476` |
| 6 | ¿Cuál es el correo del responsable de Recursos Humanos? | `ElfMcHR@bfc.com` |
| 7 | ¿Cómo se llama el portal interno de RRHH? | `HR-Portal` |
| 8 | ¿Cuál es la contraseña de acceso al portal? | `Winter2021!` |

### Task 23: Día 18 - Docker (capas de imagen)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando se usa para listar las imágenes locales de Docker? | `docker images` |
| 2 | ¿Qué comando se usa para guardar/exportar una imagen en un archivo? | `docker save` |
| 3 | ¿Cómo se llama el archivo que describe las capas (manifiesto) de la imagen? | `manifest.json` |
| 4 | ¿Cuál es el hash del blob/config que contiene el dato buscado? | `7095b3e9300542edadbc2dd558ac11fa` |

### Task 24: Día 19 - Análisis de phishing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Desde qué dirección se envía el correo legítimo en la comparativa? | `elfmcphearson@tbfc.com` |
| 2 | ¿Desde qué dirección se envía el correo suplantado? | `customerservice@t8fc.info` |
| 3 | ¿Qué dirección de correo responde el atacante? | `fisher@tempmailz.grinch` |
| 4 | ¿Qué error de escritura se detecta en el correo de phishing? | `stright` |
| 5 | ¿Cuál es el enlace de phishing completo (dominio + path)? | `https://89xgwsnmo5.grinch/out/fishing/` |
| 6 | ¿Qué cabecera personalizada añade el atacante? | `X-GrinchPhish: >;^)` |
| 7 | ¿Qué archivo adjunto malicioso acompaña al correo? | `password-reset-instructions.pdf` |
| 8 | ¿Cuál es la flag del análisis de phishing? | `THM{A0C_Thr33_Ph1sh1ng_An4lys!s}` |
| 9 | Realiza el análisis completo de cabeceras y adjuntos. | `No answer needed` |

### Task 25: Día 20 - Antivirus (ClamAV / EICAR)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la cadena de prueba EICAR del laboratorio? | `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*` |
| 2 | ¿Cómo identifica ClamAV esta amenaza de prueba? | `EICAR virus test files` |
| 3 | ¿Cuál es la fecha de la última actualización de firmas? | `2005-10-17 22:03:48` |
| 4 | ¿Qué nombre de detección concreta reporta ClamAV? | `Virus:DOS/EICAR_Test_File` |
| 5 | ¿Qué archivo de referencia/signatura se menciona en la explicación? | `ducklin.htm or ducklin-html.htm` |
| 6 | ¿Cuántos bytes ocupa el archivo de prueba? | `128` |

### Task 26: Día 21 - Análisis de metadatos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué instrucción/operación destaca al examinar el archivo binario? | `or` |
| 2 | ¿Qué bandera del comando hay que usar durante el análisis? | `-m` |
| 3 | ¿Qué sección/campo contiene la información buscada? | `metadata` |
| 4 | ¿Qué bandera adicional se necesita para la siguiente consulta? | `-n` |
| 5 | ¿Cuál es el resultado/valor de la consulta final? | `0` |

### Task 27: Día 22 - Envío de correos (SMTP)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Desde qué dirección de correo envía el Grinch sus mensajes? | `Grinch.Enterprises.2021@gmail.com` |
| 2 | ¿Cuál es la contraseña de la cuenta SMTP? | `S@ntai$comingt0t0wn` |
| 3 | ¿Cómo se llama el asunto/plantilla del correo? | `Christmas Wishlist` |
| 4 | ¿Qué puerto SMTP se usa para el envío? | `587` |
| 5 | ¿Cuál es el nombre de la cookie encontrada en el servidor de correo? | `YouFoundGrinchCookie` |
| 6 | ¿Cuál es la cadena/resultado final del envío (flag)? | `S@nt@c1Au$IsrEAl` |

### Task 28: Día 23 - Explotación (PrintNightmare)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta de PowerShell se usa para explotar PrintNightmare? | `Invoke-Nightmare` |
| 2 | ¿Qué usuario se crea tras la ejecución del exploit? | `adm1n` |
| 3 | ¿Qué host:puerto recibe el reverse shell? | `10.10.148.96,4321` |
| 4 | ¿Cuál es el ID de sesión/flag de la tarea oculta? | `j3pn50vkw21hhurbqmxjlpmo9doiukyb` |
| 5 | ¿Qué herramienta se utiliza para borrar los artefactos (sdelete)? | `sdelete.exe` |
| 6 | ¿Qué timestamp/fecha aparece en los registros de la máquina? | `11/11/2021 7:29:27 PM` |
| 7 | ¿Cuál es el mensaje final de Mission Control? | `Mission Control: letitsnowletitsnowletitsnow` |

### Task 29: Día 24 - Crackeo de contraseñas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario objetivo? | `emily` |
| 2 | ¿Cuál es el hash MD5 que hay que crackear? | `8af326aa4850225b75c592d4ce19ccf5` |
| 3 | ¿Cuál es la contraseña en texto plano? | `1234567890` |

### Task 30: Conclusión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por el evento. Introduce la flag de cierre. | `thm{thank_you_2021}` |
| 2 | Termina la encuesta del evento. | `No answer needed` |
| 3 | Comparte tu progreso en las redes. | `No answer needed` |

---

**Metodología:** El evento arranca con IDOR sobre una API y manipulación de cookies (hex→JSON). Continúa con brute force a WordPress, LFI en una app Flask que revela credenciales, y acceso a MongoDB vía SSRF. Los días de red usan Nmap para detectar Apache httpd 2.4.49 (CVE-2021-42013), MSSQL con xp_cmdshell, NFS (2049) y FTP con Hydra. En Windows se practica forense de malware con UsrClass.dat y escalada con el servicio Iperius; en el día final PrintNightmare (Invoke-Nightmare) otorga acceso total. Cierra con OSINT de criptomonedas, buckets S3, análisis de phishing, ClamAV, exif de metadatos y envío SMTP.

**Learning chain:** IDOR → cookies y JWT → brute force → LFI → SSRF/MongoDB → forense Windows → Hydra/FTP → Apache CVE → MSSQL → NFS → privesc Iperius → zip cracking → OSINT → AWS S3 → Docker → phishing → ClamAV → metadatos → SMTP → PrintNightmare → crackeo de hashes.

**MITRE ATT&CK:** T1213 (Data from Information Repositories), T1071 (Application Layer Protocol), T1190 (Exploit Public-Facing Application), T1548 (Abuse Elevation Control Mechanism), T1036 (Masquerading), T1566 (Phishing), T1020 (Automated Exfiltration), T1003 (OS Credential Dumping)

**Fuente:** [TryHackMe - Advent of Cyber 3 (2021)](https://tryhackme.com/room/adventofcyber3)