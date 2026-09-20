# Conti

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | DFIR · Threat Hunting | conti | https://tryhackme.com/room/conti | Incident Response | TryHackMe | Splunk · Sysmon · IIS Logs | Ransomware Conti sobre Exchange Server |

---

**Contexto:** El escenario simula un incidente real: los empleados no pueden acceder a Outlook y el administrador del Exchange queda bloqueado del Exchange Admin Center. El triage inicial detecta archivos "readme.txt" sospechosos desplegados en el servidor de Exchange. La sala entrega una instancia de Splunk con los logs del compromiso y pide reconstruir la cadena de intrusión del ransomware Conti mediante el análisis de eventos de Sysmon e IIS. El objetivo es extraer los IOCs del ataque: ejecutable del ransomware, su hash, comandos utilizados, el webshell y las CVEs explotadas.

## Solucionario

### Task 1: SITREP - Investigación del incidente

**Explicación:** La sala presenta el parte de situación (SITREP). Empleados y el administrador del sistema reportan fallos al acceder a Outlook y al Exchange Control Panel; el triage inicial encuentra notas de rescate (readme.txt) en el servidor de Exchange. Para investigar hay que conectar con OpenVPN o usar el AttackBox y acceder a la instancia de Splunk proporcionada:

Splunk Interface Credentials:
Username: `bellybear`
Password: `password!!!`
Splunk URL: `http://MACHINE_IP:8000`

La tarea pide asumir el rol de analista asignado a investigar la situación y usar Splunk para responder las preguntas sobre el ransomware Conti.

Respuesta de la tarea (pregunta de setup):

`No answer needed`

### Task 2: Análisis del compromiso de Exchange con Splunk

**Explicación:** En la consola de Splunk, estableciendo el timeframe a 'All Time', se ejecuta la búsqueda base `index=*` y luego se filtran los eventos por `EventCode=11` (Sysmon file creation events) para localizar archivos sospechosos. Los resultados muestran en el campo *Image* un ejecutable llamado `cmd.exe` en una ruta inusual, lo que delata la ubicación del ransomware.

**Q1. Can you identify the location of the ransomware?**

Filtro clave: `index=* EventCode=11` (o buscando por el campo Image del proceso). El resultado señala:

`C:\Users\Administrator\Documents\cmd.exe`

**Q2. What is the Sysmon event ID for the related file creation event?**

El Event ID de Sysmon asociado a la creación de archivos:

`11`

**Q3. Can you find the MD5 hash of the ransomware?**

Buscando sobre el image file el campo MD5:

```
Image="c:\Users\Administrator\Documents\cmd.exe" "MD5"
```

El hash resultante es:

`290c7dfb01e50cea9e19da81a781af2c`

**Q4. What file was saved to multiple folder locations?**

Revisando el campo TargetFileName de los eventos de creación (EventCode 11), el mismo archivo se reproduce en varias carpetas:

`readme.txt`

**Q5. What was the command the attacker used to add a new user to the compromised system?**

Búsqueda por `index=* "/add"`; el ParentCommandLine que coincide con el patrón de `net user` para añadir un usuario:

`net user /add securityninja hardToHack123$`

**Q6. The attacker migrated the process for better persistence. What is the migrated process image, and what is the original process image?**

Filtrando por Sysmon Event ID 8 (CreateRemoteThread) se obtienen los campos SourceImage y TargetImage:

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe,C:\Windows\System32\wbem\unsecapp.exe`

**Q7. The attacker also retrieved the system hashes. What is the process image used for getting the system hashes?**

En el primer registro filtrado (proceso de volcado de credenciales) el TargetImage apunta a:

`C:\Windows\System32\lsass.exe`

**Q8. What is the web shell the exploit deployed to the system?**

Cambiando el sourcetype a `iis` y filtrando por `cs_method=POST` y la extensión `.aspx`, el campo `cs_uri_stem` revela el webshell:

`i3gfPctK1c2x.aspx`

**Q9. What is the command line that executed this web shell?**

Buscando por el nombre del webshell, el campo CommandLine del primer registro:

`attrib.exe  -r \\\\win-aoqkg2as2q7.bellybear.local\C$\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\i3gfPctK1c2x.aspx`

**Q10. What three CVEs did this exploit leverage?**

Investigación externa sobre las CVEs asociadas al ransomware Conti (vulnerabilidades de Exchange y SMB), en orden ascendente:

`CVE-2018-13374,CVE-2018-13379,CVE-2020-0796`

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Can you identify the location of the ransomware? | `C:\Users\Administrator\Documents\cmd.exe` |
| 2 | What is the Sysmon event ID for the related file creation event? | `11` |
| 3 | Can you find the MD5 hash of the ransomware? | `290c7dfb01e50cea9e19da81a781af2c` |
| 4 | What file was saved to multiple folder locations? | `readme.txt` |
| 5 | What was the command the attacker used to add a new user to the compromised system? | `net user /add securityninja hardToHack123$` |
| 6 | The attacker migrated the process for better persistence. What is the migrated process image, and what is the original process image? | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe,C:\Windows\System32\wbem\unsecapp.exe` |
| 7 | The attacker also retrieved the system hashes. What is the process image used for getting the system hashes? | `C:\Windows\System32\lsass.exe` |
| 8 | What is the web shell the exploit deployed to the system? | `i3gfPctK1c2x.aspx` |
| 9 | What is the command line that executed this web shell? | `attrib.exe  -r \\\\win-aoqkg2as2q7.bellybear.local\C$\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\i3gfPctK1c2x.aspx` |
| 10 | What three CVEs did this exploit leverage? | `CVE-2018-13374,CVE-2018-13379,CVE-2020-0796` |

---

**Metodología:** DFIR / Threat Hunting basada en SIEM (Splunk): establecimiento del timeframe completo, búsqueda base sobre todos los índices y correlación de Event IDs de Sysmon (11 = creación de archivos, 8 = CreateRemoteThread), revisión del árbol de procesos (Image, SourceImage, TargetImage, ParentCommandLine), análisis de logs IIS (métodos POST y cs_uri_stem) e investigación externa de CVEs para completar la cadena de intrusión.

**Learning chain:** Splunk básico → detección de creación de archivos con EventCode 11 → localización del ransomware y su hash MD5 → identificación de persistencia (creación de usuario y proceso migrado) → volcado de credenciales vía LSASS → detección del webshell en logs IIS y su línea de comandos → mapeo de los exploits (CVEs) usados por la banda.

**Lección:** *Una intrusión de ransomware no es un único evento, sino una cadena: exploit público → webshell → ejecución → migración de procesos → credenciales → persistencia → cifrado. Con logs estructurados (Sysmon/Splunk) y una hipótesis clara se puede reconstruir cada eslabón sin ejecutar la muestra maliciosa.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application — Exchange/OWA), T1505.003 (Web Shell), T1059.001 (PowerShell), T1055 (Process Injection / migración vía CreateRemoteThread), T1003.001 (OS Credential Dumping: LSASS Memory), T1136.001 (Create Account: Local Account), T1486 (Data Encrypted for Impact).

**Fuente:** [TryHackMe - Conti](https://tryhackme.com/room/conti)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.