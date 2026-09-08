# Network Services 2

| **Dificultad** | Easy |
| **Tipo** | Enumeración y explotación de servicios de red (laboratorio) |
| **Slug** | `networkservices2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/networkservices2) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | NFS / showmount / mount / SMTP / PGP / Metasploit (auxiliary/scanner/smtp_version, smtp_enum) / MySQL / auxiliary/scanner/mysql/mysql_schemadump, mysql_hashdump / Hydra / SSH |
| **Impacto** | Sala que profundiza en tres servicios de red vistos en "Network Services": NFS (puerto 2049), SMTP (puerto 25) y MySQL (puerto 3306). Se estudia la teoría de cada servicio, su enumeración con escáneres de Metasploit, la explotación de malas configuraciones (permisos setuid en claves NFS, enumeración de usuarios SMTP para forzar contraseñas, hashdump y cracking de credenciales MySQL) y la captura de la flag de cada segmento. |

---

**Contexto:** El laboratorio continúa el recorrido por servicios de red. En el segmento NFS (Network File System) se explica el protocolo (montaje, file handles, RPC, autenticación basada en UID/GID) y se enumeran los shares con `showmount -e`, descubriendo una carpeta `/home` con el usuario `cappucino`. Al montar el share se detecta que su carpeta `.ssh` contiene la clave `id_rsa`, pero la clave tiene activos los bits setuid/setgid (-rwsr-sr-x) que impiden el login directo por SSH: el truco consiste en copiar el contenido del share y montarlo como propio para forzar la autenticación y obtener la flag `THM{nfs_got_pwned}`. El segmento SMTP empieza con la teoría (protocolo de transferencia de correo, handshake, puerto 25, cola SMTP, POP/IMAP) y usa el módulo de Metasploit `smtp_enum` para enumerar usuarios (se descubre `administrator` y `alejandro`); con Hydra se fuerza la contraseña por SSH de `alejandro` para acceder y leer la flag en `/root/flag.txt`. El último segmento trata MySQL (sistema de gestión de bases de datos relacional, SQL, modelo cliente-servidor, base de datos de backend): se conecta con el escáner `mysql_login`, se vuelcan los esquemas con `mysql_schemadump`, se extraen los hashes con `mysql_hashdump` y se crackea la contraseña `doggie` del usuario `carl`, que da paso a la flag.

## Solucionario

### Task 1: Conectando

**Explicación:** Despliegue del laboratorio: se arranca la máquina objetivo y se comprueba la conectividad con la red de TryHackMe.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Listo. ¡Conectémonos a la red y despleguemos la máquina! | `No answer needed` |

### Task 2: Entendiendo NFS

**Explicación:** NFS (Network File System) es un protocolo de sistema de archivos en red. El proceso que permite a los clientes acceder a los archivos remotos como si fueran locales es el `Mounting` (montaje). NFS usa `file handles` para representar archivos y directorios en el servidor, y se comunica entre servidor y cliente mediante `RPC`. La autenticación no se basa en usuario/contraseña sino en los identificadores numéricos `user id / group id` del cliente. Como la confianza se delega en el cliente y no hay autenticación fuerte a nivel de NFS, es explotable en ciertas condiciones; en el laboratorio se trabaja con la versión `4.2`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa NFS? | `Network File System` |
| 2 | ¿Qué proceso permite a los clientes acceder a los archivos remotos como si fueran locales? | `Mounting` |
| 3 | ¿Qué usa NFS para representar física o lógicamente los archivos y directorios del servidor? | `file handle` |
| 4 | ¿Qué protocolo usa NFS para comunicarse entre servidor y cliente? | `RPC` |
| 5 | ¿Qué dos piezas de información son necesarias para autenticarse y acceder a los archivos? | `user id / group id` |
| 6 | ¿El protocolo NFS autentica de forma inherente usando usuario y contraseña? (Y/N) | `Y` |
| 7 | ¿Es NFS explotable sin acceso al servidor? (Y/N) | `Y` |
| 8 | ¿Qué versión de NFS se está ejecutando en el objetivo? | `4.2` |

### Task 3: Enumerando NFS

**Explicación:** Un escaneo nmap inicial muestra `7` puertos abiertos y NFS en el puerto `2049`. Con `showmount -e <IP>` se enumeran los exports disponibles: el directorio `/home` está exportado a cualquier cliente. Al montarlo localmente se observa que contiene un único directorio, el del usuario `cappucino`, y al inspeccionarlo se encuentra la carpeta `.ssh` con la clave privada `id_rsa`; con esa clave deberíamos poder iniciar sesión (Y).

```bash
nmap -p- <IP>
showmount -e <IP>
sudo mkdir -p /mnt/nfs
sudo mount -t nfs <IP>:/home /mnt/nfs
ls -la /mnt/nfs
find /mnt/nfs -type f -name "id_rsa"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos están abiertos en la máquina objetivo? | `7` |
| 2 | ¿En qué puerto está el servicio NFS? | `2049` |
| 3 | Usando lo que has aprendido, enumera los exports de NFS. ¿Cuál es el mount point que podemos montar? | `/home` |
| 4 | Una vez montado el directorio, ¿qué nombre de usuario encontramos? | `cappucino` |
| 5 | Sigue los pasos de enumeración y localiza los archivos comprometidos. | `No answer needed` |
| 6 | ¿Qué directorio importante encontramos dentro de la carpeta del usuario? | `.ssh` |
| 7 | ¿Cuál es el nombre de la clave privada que podemos usar para entrar? | `id_rsa` |
| 8 | Con la información recopilada, ¿podemos acceder a la máquina usando esa clave? (Y/N) | `Y` |

### Task 4: Explotando NFS

**Explicación:** Tras descargar `id_rsa` y probar a conectarse por SSH la conexión falla porque los permisos del archivo no son los que SSH exige. Al listar los permisos se ve que la clave arranca con la letra `s` y tiene los bits setuid/setgid activados: `-rwsr-sr-x`. La técnica consiste en copiar la clave y montarla de forma que la propiedad coincida con la que el servidor espera (reducir el `group id`/`user id` local al del usuario protegido, o copiar la clave a un usuario local con ese UID) para que el servidor NFS confíe en el cliente; una vez ajustado, la conexión por SSH funciona y se lee la flag.

```bash
chmod 600 id_rsa
# Ajustar UID/GID local para que el servidor NFS confíe en el cliente
chown <uid_de_cappucino> id_rsa
ssh cappucino@<IP> -i id_rsa
cat flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descarga la clave y úsala para conectarte por SSH. | `No answer needed` |
| 2 | Si no puedes entrar, revisa los permisos de los archivos y el usuario que los posee. | `No answer needed` |
| 3 | ¿Con qué letra comienza la cadena de permisos que permite esta conexión? | `s` |
| 4 | ¿Qué permisos tiene el archivo descargado? | `-rwsr-sr-x` |
| 5 | Monta el directorio comprometido de forma que la propiedad de los archivos coincida con lo que espera el servidor. | `No answer needed` |
| 6 | Una vez conectado, ¿cuál es la flag? | `THM{nfs_got_pwned}` |

### Task 5: Entendiendo SMTP

**Explicación:** SMTP (Simple Mail Transfer Protocol) es el protocolo de transmisión de correo electrónico que gestiona el envío de `emails`. El proceso de comunicación comienza con un `SMTP handshake` (saludo) entre cliente y servidor, y el puerto estándar es el `25`. Los mensajes en espera se almacenan en la `smtp queue` antes de ser enviados. Para la recuperación (descarga) de correo se usan otros protocolos como `POP/IMAP`. SMTP no autentica a los usuarios a nivel de cabeceras (Y) y permite de forma inherente que cualquiera envíe correos (Y), lo que lo convierte en un vector de abuso habitual.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa SMTP? | `Simple Mail Transfer Protocol` |
| 2 | ¿Qué gestiona SMTP? | `emails` |
| 3 | ¿Qué proceso utiliza SMTP para empezar a conectarse a un servidor? | `SMTP handshake` |
| 4 | ¿En qué puerto corre SMTP por defecto? | `25` |
| 5 | ¿Dónde almacena el servidor SMTP los mensajes en espera de envío? | `smtp queue` |
| 6 | ¿Qué protocolo usa SMTP para recuperar los correos del servidor? | `POP/IMAP` |
| 7 | ¿Presenta SMTP autenticación en las cabeceras del protocolo? (Y/N) | `Y` |
| 8 | ¿Permite SMTP de forma inherente el envío de correos por parte de cualquiera? (Y/N) | `Y` |

### Task 6: Enumerando SMTP

**Explicación:** SMTP corre en el puerto `25`. En primer lugar se confirma la versión del servidor; estando en un SSO se hace a través del módulo de Metasploit `auxiliary/scanner/smtp/smtp_version` (tras arrancar `msfconsole`, se usa `options` para ver los parámetros y se fija `RHOSTS`). La respuesta identifica el hostname `polosmtp.home` y la versión `Postfix`. Para enumerar usuarios se usa el módulo `auxiliary/scanner/smtp/smtp_enum`, configurando el diccionario de nombres con la opción `USER_FILE` y el objetivo con `RHOSTS`; la enumeración (basada en el comando VRFY) encuentra el usuario `administrator`.

```bash
msfconsole
use auxiliary/scanner/smtp/smtp_version
options
set RHOSTS <IP>
run

use auxiliary/scanner/smtp/smtp_enum
set USER_FILE /usr/share/wordlists/metasploit/names.txt
set RHOSTS <IP>
run
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Mientras tanto, ejecuta un escaneo de puertos para localizar el servicio SMTP. ¿En qué puerto corre? | `25` |
| 2 | Abre `msfconsole` y carga el módulo de Metasploit para comprobar la versión del servidor. | `msfconsole` |
| 3 | ¿Cuál es el módulo auxiliar que usamos para detectar la versión del servidor SMTP? | `auxiliary/scanner/smtp/smtp_version` |
| 4 | ¿Qué comando de msfconsole usamos para ver las opciones del módulo? | `options` |
| 5 | ¿Qué opción necesitamos fijar para indicar la máquina objetivo? | `RHOSTS` |
| 6 | ¿Qué hostname encontramos en el resultado de la enumeración? | `polosmtp.home` |
| 7 | ¿Qué versión de servidor SMTP corre? | `Postfix` |
| 8 | ¿Cuál es el módulo auxiliar que usamos para enumerar usuarios? | `auxiliary/scanner/smtp/smtp_enum` |
| 9 | ¿Qué opción usamos para indicar el diccionario de nombres de usuario? | `USER_FILE` |
| 10 | ¿Qué opción usamos para indicar la máquina objetivo? | `RHOSTS` |
| 11 | Ejecuta el módulo para obtener la lista de usuarios. | `No answer needed` |
| 12 | ¿Qué usuario contiene el sufijo "min" y es el administrador de la máquina? | `administrator` |

### Task 7: Explotando SMTP

**Explicación:** De la enumeración de usuarios se obtiene también `alejandro`. Se fuerza la contraseña de ese usuario contra el servicio SSH con Hydra y, una vez dentro, se localiza y lee el archivo de flag (`/root/flag.txt`).

```bash
hydra -l alejandro -P /usr/share/wordlists/rockyou.txt ssh://<IP>
ssh alejandro@<IP>
cat /root/flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Con la lista de usuarios obtenida, ¿qué usuario podemos usar para acceder a la máquina? | `alejandro` |
| 2 | Fuerza la contraseña y entra en la máquina. ¿Cuál es la flag? | `THM{who_knew_email_servers_were_c00l?}` |

### Task 8: Entendiendo MySQL

**Explicación:** MySQL es un sistema de gestión de bases de datos relacional: `relational database management system`. El lenguaje con el que se comunica y gestiona es `SQL`. Usa un modelo de comunicación `client-server` y, en una arquitectura web típica, sirve como `back end database` (la base de datos del backend que almacena los datos de la aplicación). Es uno de los gestores de bases de datos más usados del mundo y lo mantiene la compañía `Facebook`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa MySQL? | `relational database management system` |
| 2 | ¿Qué lenguaje usa MySQL para gestionar los datos? | `SQL` |
| 3 | ¿Qué tipo de modelo de comunicación usa MySQL? | `client-server` |
| 4 | ¿Cómo se denomina a la base de datos que almacena los datos de una aplicación web en el backend? | `back end database` |
| 5 | ¿Qué gran compañía usa y contribuye masivamente a MySQL? | `Facebook` |

### Task 9: Enumerando MySQL

**Explicación:** MySQL corre en el puerto `3306`. Con Metasploit se lanza el escáner de login (`auxiliary/scanner/mysql/mysql_login`) usando credenciales por defecto; las opciones clave son `PASSWORD`, `RHOSTS` y `USERNAME`. Una vez conectado, se identifica la versión del servidor `8.0.42-0ubuntu0.20.04.1` y se comprueba que hay `4` bases de datos en el sistema.

```bash
msfconsole
use auxiliary/scanner/mysql/mysql_login
set PASSWORD <pass>
set RHOSTS <IP>
set USERNAME <user>
run
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Según el escaneo, ¿en qué puerto corre MySQL? | `3306` |
| 2 | Conectemos con el escáner de login. Carga el módulo en Metasploit. | `No answer needed` |
| 3 | Configura las opciones y ejecuta el módulo. | `No answer needed` |
| 4 | ¿Qué tres opciones necesitamos fijar para que funcione el módulo? | `PASSWORD/RHOSTS/USERNAME` |
| 5 | Tras conectarnos, ¿qué versión de MySQL está corriendo en la máquina? | `8.0.42-0ubuntu0.20.04.1` |
| 6 | ¿En cuántas bases de datos podemos entrar? | `4` |

### Task 10: Explotando MySQL

**Explicación:** Con acceso autenticado se vuelcan los esquemas con el módulo `auxiliary/scanner/mysql/mysql_schemadump`, que revela una base de datos accesible llamada `x$waits_global_by_latency`. A continuación se extraen los hashes de contraseñas con `auxiliary/scanner/mysql/mysql_hashdump`, obteniendo el hash del usuario `carl`: `carl:*EA031893AA21444B170FC2162A56978B8CEECE18`. Ese hash se crackea con john/hashcat y la contraseña resultante es `doggie`. Con esas credenciales se entra de nuevo por SSH y se pone en práctica el concepto de reutilización de contraseñas para leer la flag.

```bash
use auxiliary/scanner/mysql/mysql_schemadump
set RHOSTS <IP>
run

use auxiliary/scanner/mysql/mysql_hashdump
set RHOSTS <IP>
run

echo 'carl:*EA031893AA21444B170FC2162A56978B8CEECE18' > hash.txt
john --format=mysql-sha1 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
ssh carl@<IP>
# password: doggie
cat flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué módulo auxiliar usamos para volcar los esquemas de las bases de datos en MySQL? | `auxiliary/scanner/mysql/mysql_schemadump` |
| 2 | ¿Qué base de datos con acceso detectamos? | `x$waits_global_by_latency` |
| 3 | ¿Qué módulo auxiliar usamos para obtener los hashes de las contraseñas? | `auxiliary/scanner/mysql/mysql_hashdump` |
| 4 | Según el volcado de hashes, ¿para qué usuario tenemos el hash? | `carl` |
| 5 | ¿Qué hash de contraseña tenemos para ese usuario? | `carl:*EA031893AA21444B170FC2162A56978B8CEECE18` |
| 6 | Con la técnica de "descifra el hash", ¿qué contraseña obtenemos? | `doggie` |
| 7 | Pon en práctica la reutilización de credenciales y obtén la flag. | `THM{congratulations_you_got_the_mySQL_flag}` |

### Task 11: Conclusión

**Explicación:** Repaso final: NFS, SMTP y MySQL, cómo enumerarlos y explotar sus malas configuraciones y cómo combinar enumeración, fuerza bruta y reutilización de credenciales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Enhorabuena! Has completado la sala. | `No answer needed` |

---

**Metodología:** Se sigue el ciclo enumerar → explotar para cada servicio. En NFS se usa `showmount -e` para encontrar el export `/home` y se monta el share; la clave `id_rsa` con bits setuid/setgid (-rwsr-sr-x) impide el login, así que se fuerza la confianza del servidor NFS ajustando la propiedad del archivo (UID/GID) y se entra por SSH a leer la flag. En SMTP se detecta Postfix en el 25, se enumeran usuarios con el módulo `smtp_enum` (VRFY) y se fuerza por SSH a `alejandro` con Hydra. En MySQL se autentica con el escáner de login, se vuelcan esquemas (`mysql_schemadump`) y hashes (`mysql_hashdump`), se crackea la contraseña de `carl` con john y se reutiliza esa credencial para acceder por SSH y leer la flag.
**Learning chain:** teoría del servicio → enumeración (nmap, showmount, módulos auxiliares de Metasploit) → identificación de misconfiguraciones → explotación (setuid en NFS, VRFY/Hydra en SMTP, hashdump/cracking en MySQL) → captura de flags.
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1135 (Network Share Discovery), T1110.001 (Password Guessing), T1110.002 (Password Cracking), T1021.002 (Remote Services: SMB/Windows Admin Shares), T1078 (Valid Accounts)
**Fuente:** [TryHackMe - Network Services 2](https://tryhackme.com/room/networkservices2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
