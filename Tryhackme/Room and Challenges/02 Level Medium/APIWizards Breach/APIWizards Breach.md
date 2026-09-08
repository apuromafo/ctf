# APIWizards Breach
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `apiwizardsbreach` |
| **Link** | [TryHackMe](https://tryhackme.com/room/apiwizardsbreach) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | SSH, Nginx, Python API, OS Command Injection, cron, systemd, iptables, bashrc, SUID, timestomping, netcat bind shell, transfer.sh, bash history, base64 |
| **Impacto** | Investigación DFIR de la intrusión en un servidor Ubuntu desde el punto de vista blue team, identificando el vector de entrada, la escalada a root y las múltiples persistencias del atacante hasta el robo de la base de datos CDE. |
---
**Contexto:** Sala de DFIR desde el punto de vista blue team: APIWizards Inc. sufrió un breach en un Ubuntu que aloja una aplicación web vía Nginx. Accedemos por SSH como usuario `dev` e investigamos qué pasó y cuál fue el impacto. La cadena: inyección de comandos en la API, escalada a root vía config.py, malware `rooter2` (cron, systemd, iptables, .bashrc, usuario support, SUID, timestomping) y exfiltración de la base de datos de tarjetas (CDE).
## Solucionario
### Task 1: Introduction
**Explicación:** Escenario: la seguridad pudo marcar comandos sospechosos y ahora, como analista DFIR, debemos reconstruir la brecha del servidor Ubuntu.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conéctate por SSH a la máquina como usuario `dev` e investiga. | `No answer needed` |
### Task 2: Initial Access
**Explicación:** Revisando la configuración de Nginx, los puertos o el código fuente de la aplicación se determina que la web está escrita en **Python**. Los logs de Nginx muestran numerosas peticiones de tipo escaneo desde una IP externa (VPN), identificada como la IP atacante. En `/api/time?tz=` se inyectan comandos (patrón `tz=" whoami #`), confirmando **OS Command Injection**. El atacante acaba escribiendo su clave SSH pública en `/home/dev/.ssh/authorized_keys`. Con el bash history en claro se ve que usó las credenciales de `/home/dev/apiservice/src/config.py` para escalar a root y descargó el binario `rooter2` desde **transfer.sh**, ejecutándolo tras un primer volcado con `turbo` (por eso el malware ya no está en disco).

```bash
tail /var/log/nginx/access.log
curl "http://<ip>/api/time?tz=\" whoami #"
ls -la /home/dev/.ssh/authorized_keys
cat /home/dev/apiservice/src/config.py
cat /home/dev/.bash_history
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué lenguaje de programación está escrita la aplicación web? | `Python` |
| 2 | ¿Cuál es la IP que atacó al servidor web? | `149.34.244.142` |
| 3 | ¿Qué vulnerabilidad fue encontrada y explotada en el servicio API? | `OS command injection` |
| 4 | ¿Qué archivo contenía las credenciales usadas para escalar a root? | `/home/dev/apiservice/src/config.py` |
| 5 | ¿Qué archivo dejó y ejecutó el hacker para persistir en el servidor? | `/tmp/rooter2` |
| 6 | ¿Qué servicio se usó para alojar el malware "rooter2"? | `transfer.sh` |
### Task 3: Further Actions
**Explicación:** El `rooter2` corrió como root y dejó varias persistencias. En el cron se encontró un trabajo que evalúa la variable `SYSTEMUPDATE` cada día a las 4:20 con una reverse shell; la variable se alimenta desde `/etc/environment` (respuesta: `/etc/crontab, /etc/environment`). La reverse shell apunta a `5.230.66.147` (IP C2). El bind shell (forward shell) escucha en el puerto `3578` (proceso netcat como root) y persiste vía un **systemd service**: `/etc/systemd/system/socket.service` (se reinicia cada 20 segundos si netcat termina).

```bash
cat /etc/crontab /etc/environment
ss -tlnp
ps aux | grep -i nc
systemctl list-units
grep -r "nc -l" /etc/systemd/system/
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dos archivos de sistema fueron infectados para lograr persistencia vía cron? | `/etc/crontab, /etc/environment` |
| 2 | ¿Cuál es la IP del servidor C2 del actor malicioso? | `5.230.66.147` |
| 3 | ¿En qué puerto escucha el bind shell bash backdoored? | `3578` |
| 4 | ¿Cómo persiste el bind shell a través de los reinicios? | `systemd service` |
| 5 | ¿Cuál es la ruta absoluta del servicio malicioso? | `/etc/systemd/system/socket.service` |
### Task 4: Even More Persistence
**Explicación:** Listando reglas de iptables se ve que el puerto `3578` está bloqueado para todos salvo para la IP del C2. Las reglas se restauran desde un `.bashrc` comprometido (`/root/.bashrc`, que además contiene un `curl` que notifica al atacante cuando root inicia sesión). El usuario local backdoored es `support`, asignado al grupo privilegiado `sudo`. En las claves SSH se observa una con el comentario **ntsvc**. Otra persistencia clásica: un binario **SUID** (`/usr/bin/clamav`, copia de `/usr/bin/bash`) que permite ejecutar shell como root. Para ocultar su fecha de creación se aplicó **timestomping** (mtime manipulado).

```bash
iptables -L
cat /root/.bashrc
grep -v nologin /etc/passwd
cat /root/.ssh/authorized_keys /home/dev/.ssh/authorized_keys
find / -perm -4000 2>/dev/null
ls -l /bin/bash /bin/clamav
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto está bloqueado en el firewall de la víctima? | `3578` |
| 2 | ¿Cómo persisten las reglas del firewall a través de los reinicios? | `/root/.bashrc` |
| 3 | ¿Cómo se llama el usuario local Linux backdoored? | `support` |
| 4 | ¿Qué grupo privilegiado se asignó al usuario? | `sudo` |
| 5 | ¿Cuál es la palabra extraña en una de las claves SSH backdoored? | `ntsvc` |
| 6 | ¿Puedes detectar y nombrar un método de persistencia popular más? | `SUID binary` |
| 7 | ¿Cuáles son los binarios original y backdoored de la pregunta 6? | `/usr/bin/bash, /usr/bin/clamav` |
| 8 | ¿Qué técnica se usó para ocultar la fecha de creación de la backdoor? | `Timestomping` |
### Task 5: Final Target
**Explicación:** Con la misma técnica `find` se localiza `/root/.dump.json`, un JSON con valores base64 que recopila información de la víctima. Decodificando el valor `C1` aparece la versión del kernel (`5.15.0-78-generic`) y del `C2` las IPs internas activas encontradas por el escaneo de `rooter2` (`192.168.0.21, 192.168.0.22`). En el bash history de root está el escaneo de puertos con netcat y el `wget` que descargó `cde-backup.csv` desde el índice HTTP expuesto. Dentro de la base de datos exfiltrada se encuentra el flag.

```bash
cat /root/.dump.json
echo '<valor_C2>' | base64 -d
nc -zv 192.168.0.22 1024-10000 2>&1 | grep -v failed
wget 192.168.0.22:8080/cde-backup.csv
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué archivo se dejó caer y contenía la información recopilada de la víctima? | `/root/.dump.json` |
| 2 | Según el dump, ¿cuál es la versión del kernel del servidor? | `5.15.0-78-generic` |
| 3 | ¿Qué IPs internas activas fueron encontradas por el escaneo de red de "rooter2"? | `192.168.0.21, 192.168.0.22` |
| 4 | ¿Cómo encontró el hacker el índice HTTP expuesto en otra IP interna? | `nc -zv 192.168.0.22 1024-10000 2>&1 \| grep -v failed` |
| 5 | ¿Qué comando se usó para exfiltrar la base de datos CDE desde la IP interna? | `wget 192.168.0.22:8080/cde-backup.csv` |
| 6 | ¿Cuál es la cadena más secreta y preciosa almacenada en la base de datos exfiltrada? | `pwned{v3ry-secur3-cardh0ld3r-data-environm3nt}` |
---
**Metodología:** DFIR/blue team en Linux: análisis de logs (Nginx/history), revisión de persistencias (cron, systemd, iptables, bashrc, claves SSH, SUID), análisis de malware en disco y correlación con el dump del atacante.
**Learning chain:** Inyección de comandos → escalada a root heredando credenciales (config.py) → persistencias múltiples → análisis del dump exfiltrante → descubrimiento y robo de la CDE.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006/Python, T1098.004 (SSH Authorized Keys), T1053.003 (Cron), T1543.002 (Systemd Service), T1546.004 (.bashrc), T1548.001/SUID, T1070.006 (Timestomping), T1041 (Exfiltration Over C2 Channel), T1484/Discovery.
**Fuente:** [TryHackMe - APIWizards Breach](https://tryhackme.com/room/apiwizardsbreach)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
