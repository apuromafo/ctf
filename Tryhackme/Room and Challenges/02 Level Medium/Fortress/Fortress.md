# Fortress
| **Dificultad** | Medium |
| **Tipo** | CTF (Boot2Root Linux) |
| **Slug** | `fortress` |
| **Link** | [TryHackMe](https://tryhackme.com/room/fortress) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `fortress` + walkthroughs públicos: AbdullahRizwan101, Shivam Taneja, Chris Meistre) |
| **Componentes** | Linux, nmap, FTP anónimo, decompilación de `.pyc` (uncompyle2), telnet no estándar, Apache/PHP, colisión SHA-1 (SHAttered), SSH/rbash, sudo, logs (`/var/log/auth.log`), escalada de privilegios |
| **Impacto** | Máquina boot2root que encadena enumeración de servicios poco comunes (FTP anónimo, telnet en 5752), ingeniería inversa de un binario de credenciales, explotación de una comprobación PHP vulnerable a **colisión SHA-1**, escape de una shell restringida, lectura de clave privada ajena y escalada a root abusando de `sudo` y de credenciales filtradas en logs. |
---
**Contexto:** Fortress es un reto **boot2root** con varias capas de dificultad encadenadas. Se enumeran servicios atípicos (FTP anónimo en 5581 con un `.file` compilado, un servicio telnet en 5752 y Apache en 7331), se decompila el bytecode Python para extraer credenciales, se accede a un panel PHP cuya comprobación de identidad se basa en **SHA-1**, vulnerable a **colisiones** (los ficheros `shattered-1.pdf`/`shattered-2.pdf`), se obtiene una clave privada SSH, se escapa de una **restricted bash (rbash)**, se usa `sudo cat` sobre archivos de otro usuario y finalmente se lee la contraseña de root en los **logs de autenticación**.
*EN: Fortress is a **boot2root** challenge with several chained layers. Unusual services are enumerated (anonymous FTP on 5581 with a compiled `.file`, a telnet service on 5752 and Apache on 7331), Python bytecode is decompiled to extract credentials, a PHP panel is accessed whose identity check relies on **SHA-1**, vulnerable to **collisions** (the `shattered-1.pdf`/`shattered-2.pdf` files), an SSH private key is obtained, a **restricted bash (rbash)** is escaped, `sudo cat` is used on another user's files and finally root's password is read from the **authentication logs**.*
## Solucionario
### Task 1: Conexión / Deploy
**Explicación:** Despliegue de la máquina y conexión a la red de TryHackMe. Se añaden los dominios indicados por la room (`fortress`, `temple.fortress`) al `/etc/hosts`. Tarea de preparación, sin respuesta.
*EN: Deploy the machine and connect to the TryHackMe network. The domains given by the room (`fortress`, `temple.fortress`) are added to `/etc/hosts`. Preparation task, no answer.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and connect to our network. | `No answer needed` |
### Task 2: Compromiso y Escalada / Compromise and Privilege Escalation
**Explicación:** Cadena completa de explotación:
1. **Enumeración (nmap).** Puertos: `22` (OpenSSH 7.2p2), `5581` (vsftpd con **login anónimo**), `5752` (servicio desconocido) y `7331` (Apache 2.4.18). En el FTP anónimo aparece `marked.txt` y un archivo oculto `.file` (bytecode Python 2.7 compilado).
2. **FTP anónimo.** Se descargan los ficheros:
```bash
ftp <IP> 5581
# usuario: anonymous
ls -la
get .file
get marked.txt
```
`marked.txt` filtra el usuario **veekay**. El `.file` se decompila con `uncompyle2` para recuperar usuario y contraseña codificados como `bytes_to_long`.
3. **Telnet (5752).** El servicio responde "Chapter 1: A Call for help" con `Username:`/`Password:`. Con las credenciales obtenidas se devuelve el contenido de `secrets.txt` (p. ej. `t3mple_0f_y0ur_51n5`).
4. **HTTP (7331).** Se abre `t3mple_0f_y0ur_51n5.php`; su código compara `sha1($_GET['user']) === sha1($_GET['pass'])` exigiendo además longitudes mínimas (>600 y >500 bytes). Se explota una **colisión SHA-1** enviando dos ficheros *shattered* con el mismo hash pero contenido distinto:
```python
import requests
pdf1 = requests.get("http://localhost/shattered-1.pdf")
pdf2 = requests.get("http://localhost/shattered-2.pdf")
params = {'user': pdf1.content, 'pass': pdf2.content}
r = requests.get("http://temple.fortress:7331/t3mple_0f_y0ur_51n5.php/", params=params)
print(r.text)
```
5. **Clave privada y rbash.** El bypass revela `m0td_f0r_j4x0n.txt` y una clave privada SSH para el usuario. La shell es una **rbash**; se escapa con `ssh -t` y redefiniendo variables:
```bash
ssh -t <user>@<IP>
export SHELL=/bin/bash
export PATH=/usr/bin:/bin
```
6. **sudo y logs.** `sudo -l` muestra permiso `cat` como el usuario `j4x0n`; se copian sus archivos/clave privada. Al pertenecer al grupo `adm` se leen los logs y se encuentra en `/var/log/auth.log` la **contraseña de root**, con la que se accede por SSH y se obtiene el flag final.
*EN: Full exploitation chain: nmap enumeration (22/5581 FTP anon/5752 telnet/7331 Apache); anonymous FTP grabbing `marked.txt` and hidden `.file` (Python bytecode) decompiled with `uncompyle2`; telnet 5752 using the recovered credentials to read `secrets.txt`; PHP panel on 7331 vulnerable to **SHA-1 collision** bypassed with the shattered files; private key + rbash escape via `ssh -t` and redefined `SHELL`/`PATH`; `sudo cat` as `j4x0n`, and finally root's password found in `/var/log/auth.log`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag in user.txt? | `84589a1bb8a932e46643b242a55489c0` |
| 2 | Escalate your privileges, what is the flag in root.txt? | `3a17cfcca1aabc245a2d5779615643ae` |
### Task 3: Conclusión / Conclusion
**Explicación:** Cierre de la room. Se consolida el aprendizaje: valorar la seguridad de los hashes criptográficos obsoletos (SHA-1), el riesgo de servicios anónimos/legacy (FTP anónimo, telnet) y de shells restringidas mal configuradas, y la exposición de credenciales en logs. Tarea de repaso, sin respuesta.
*EN: Room wrap-up. Key takeaways: the security limits of obsolete cryptographic hashes (SHA-1), the risk of anonymous/legacy services (anonymous FTP, telnet) and poorly configured restricted shells, and credential exposure in logs. Review task, no answer.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Room complete! | `No answer needed` |
---
**Metodología:** Enumeración de puertos (nmap) → explotación de FTP anónimo → ingeniería inversa de bytecode Python → acceso a servicio telnet no estándar → descubrimiento de ruta web → explotación de **colisión SHA-1** → obtención de clave privada SSH → escape de rbash → `sudo` sobre `cat` → lectura de credenciales en logs → root.
**Learning chain:** enumerar servicios raros → decompilar y extraer credenciales → entender un panel vulnerable a colisiones → romper la restricción de shell → encadenar `sudo`/logs para escalar.
**Lección:** *Un hash roto (SHA-1) no sirve para autenticar; los servicios legacy y anónimos son puertas de entrada, y una shell restringida sin hardening real se escapa en dos comandos.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1110 (Brute Force), T1190 (Exploit Public-Facing Application), T1552.001 (Credentials In Files), T1548.003 (Sudo and Sudo Caching), T1005 (Data from Local System), T1070.002 (Indicator Removal: Clear Linux or Mac System Logs).
**Fuente:** [TryHackMe - Fortress](https://tryhackme.com/room/fortress)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
