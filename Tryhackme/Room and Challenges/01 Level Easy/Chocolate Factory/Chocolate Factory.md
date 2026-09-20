# Chocolate Factory

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `chocolatefactory` | [TryHackMe](https://tryhackme.com/room/chocolatefactory) | 01 Level Easy | THM | FTP anónimo, steghide, hash cracking, puerto 113, RCE web, SSH key, sudo vi, Fernet | Medio |

---

**Contexto:** Máquina temática de Willy Wonka ("Charlie and the Chocolate Factory"). El box expone FTP anónimo con la imagen gum_room.jpg que oculta (steghide, sin passphrase) un dump base64 de /etc/shadow, del que se extrae el hash de charlie y se crackea con rockyou (cn7824). El puerto 113 revela en su banner la ruta http://localhost/key_rev_key, un binario con la clave Fernet hardcodeada. El login web acepta charlie:cn7824 y ofrece una caja de comandos (RCE) desde la que se obtiene una reverse shell; allí aparecen user.txt y un par de claves SSH. Con la id_rsa se accede por SSH como charlie (user flag) y, dado que charlie puede ejecutar /usr/bin/vi como root sin contraseña (GTFOBins), se lanza una shell root y se ejecuta root.py con la clave Fernet para desencriptar el flag final.

> **ES:** Box CTF: FTP anónimo → gum_room.jpg → steghide → /etc/shadow → John (rockyou) → cn7824 → banner del puerto 113 → key_rev_key con la clave Fernet → login web charlie:cn7824 → RCE en la caja de comandos → reverse shell → id_rsa → SSH charlie → user flag → sudo /usr/bin/vi (GTFOBins) → shell root → root.py con la clave Fernet → root flag.

> **EN:** CTF box: anonymous FTP → gum_room.jpg → steghide → /etc/shadow → John (rockyou) → cn7824 → port 113 banner → key_rev_key with the Fernet key → web login charlie:cn7824 → RCE via the command box → reverse shell → id_rsa → SSH charlie → user flag → sudo /usr/bin/vi (GTFOBins) → root shell → root.py with the Fernet key → root flag.

## Solucionario

### Task 1: Enter the key you found / Ingresa la clave que encontraste

**Explicación:** Tras el escaneo de puertos se audita el banner del puerto 113, que revela `http://localhost/key_rev_key`. Al descargar el binario y analizarlo con strings se obtiene la clave de descifrado Fernet.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Enter the key you found! | `b'-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY='` |

### Task 2: What is Charlie's password? / ¿Cuál es la contraseña de Charlie?

**Explicación:** El FTP anónimo contiene gum_room.jpg. Con steghide (passphrase vacía) se extrae un archivo base64 que, decodificado, es un dump de /etc/shadow con el hash SHA-512 de charlie. Crackeando el hash con John the Ripper y rockyou se obtiene la contraseña.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is Charlie's password? | `cn7824` |

### Task 3: Change User to Charlie / Cambio de usuario a Charlie

**Explicación:** Con las credenciales charlie:cn7824 se entra en la parte privada de la aplicación web, que expone una caja de comandos (RCE). Con una reverse shell se enumeran los archivos de /home/charlie: user.txt y un par de claves SSH (teleport/teleport.pub). Se copia la id_rsa al equipo atacante y se conecta por SSH.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Pivot from the web user to charlie / Confirmación | `No answer needed` |

### Task 4: Enter the user flag / Ingresa el user flag

**Explicación:** Con la clave privada (chmod 600) se entra por SSH como charlie y se lee el primer flag en /home/charlie/user.txt.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Enter the user flag | `flag{cd5509042371b34e4826e4838b522d2e}` |

### Task 5: Enter the root flag / Ingresa el root flag

**Explicación:** `sudo -l` muestra que charlie puede ejecutar /usr/bin/vi como root sin contraseña. Usando la técnica de GTFOBins (`sudo vi -c ':!/bin/sh' /dev/null`) se obtiene una shell root. En /root está root.py, un script Python que cifra el flag con Fernet; introduciendo la clave `b'-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY='` se desencripta el root flag.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Enter the root flag | `flag{cec59161d338fef787fcb4e296b42124}` |

---

**Metodología:** nmap (21/22/80/113) → FTP anónimo → gum_room.jpg → steghide → b64.txt → /etc/shadow → John + rockyou → cn7824 → banner del puerto 113 → key_rev_key → strings → clave Fernet → login web charlie:cn7824 → RCE en la caja de comandos → reverse shell → id_rsa → SSH charlie → user flag → sudo /usr/bin/vi (GTFOBins) → shell root → python root.py + clave Fernet → root flag.

### Cadena de ataque / Attack Chain

FTP anónimo → esteganografía → dump de /etc/shadow → crackeo del hash → credenciales → banner del puerto 113 → binario key_rev_key → clave Fernet → login web → RCE → reverse shell → robo de id_rsa → SSH charlie → user flag → sudo vi sin contraseña → shell root → root.py (Fernet) → root flag.

**Learning chain:** Enumeración de puertos → FTP anónimo → esteganografía → hash cracking → análisis de banners → ingeniería inversa básica (strings) → RCE web → reverse shells → SSH key theft → sudo misconfigured (GTFOBins) → descifrado Fernet.

**Lección:** *Un FTP anónimo, un banner, un binario sin ofuscar y un vi con sudo sin contraseña forman una cadena que va de un archivo de imagen a la raíz del sistema: las pistas escondidas en puertos y binarios son la puerta de entrada y el descifrado final.*

**MITRE ATT&CK:** T1048 (Exfiltration Over Alternative Protocol), T1110.002 (Password Cracking), T1110 (Brute Force), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1204 (User Execution).

**Fuente:** [TryHackMe - Chocolate Factory](https://tryhackme.com/room/chocolatefactory)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.