# Windows Incident Surface

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `winincidentsurface` |
| **Link** | [TryHackMe](https://tryhackme.com/room/winincidentsurface) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Simon Taplin (simontaplin.net) + thmrevenant (GitHub) |
| **Componentes** | DFIR / Windows triage / wevtutil / registro (WDigest, Userinit, netshell) / services / processes / network / SIDs / AnyDesk |
| **Impacto** | Implementar técnicas de DFIR para explorar la superficie de incidentes de Windows e identificar artefactos de alto ROI en la caza de amenazas |

---

**Contexto:** Aprende a implementar técnicas de DFIR para explorar la superficie de incidentes de Windows. Identifica artefactos que dan un buen ROI en la caza de amenazas: fiabilidad de las herramientas del sistema, información del sistema, cuentas de usuario, procesos, persistencia, servicios y actividad de red de un host comprometido.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** En el cambiante panorama de la ciberseguridad, no se puede depender solo de un enfoque reactivo. El objetivo no es un análisis exhaustivo, sino un triage eficiente y un descubrimiento accionable.

### Task 2: Reliability of the System Tools

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What **tool** did the adversary use to delete the logs? | `wevtutil` |
| 2 | What was the **registry path** used by the adversary to store and steal the login credentials? | `HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest` |

**Explicación:** Los atacantes pueden modificar las **variables de entorno** para secuestrar el flujo de ejecución (ATT&CK T1574.007). Un **perfil de PowerShell** es un script que se ejecuta cada vez que se lanza PowerShell, útil para persistir. La tool usada para borrar logs fue **`wevtutil`** (T1070.001 Clear Windows Event Logs); las credenciales se almacenaron/robaron vía la clave **WDigest** `HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest` (permite guardar credenciales en texto plano en memoria).

### Task 3: System Information

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **hostname** of the compromised host? | `CCTL-WS-018-b21` |
| 2 | What is the **OS version** of the compromised host? | `10.0.17763` |
| 3 | What is the **Time ID** of the compromised host? | `Turkey Standard Time` |

**Explicación:** El reconocimiento inicial del host comprometido (T1082 System Information Discovery) anota: hostname `CCTL-WS-018-b21`, OS version `10.0.17763` (build de Windows 10/Server 2019) y la zona horaria `Turkey Standard Time`.

### Task 4: User Accounts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the total number of suspicious accounts? | `3` |
| 2 | What is the security identifier (SID) of the Guest account? | `S-1-5-21-1966530601-3185510712-10604624-501` |
| 3 | When was the last time the Admin account (the one with the deliberate typo) was logged in? (Answer format: MM/DD/YY HH:MM:SS XM) | `2/28/2024 10:21:10 AM` |

**Explicación:** Los SIDs terminan en un **RID** (Relative Identifier): 500 = Administrator, 501 = Guest. Se identifican **3** cuentas sospechosas; el SID del Guest es `S-1-5-21-1966530601-3185510712-10604624-501` (RID 501). La cuenta Admin con el typo deliberado se logueó por última vez el `2/28/2024 10:21:10 AM`. Cazar cuentas inesperadas (nombre raro, RID unprivileged) es de alto ROI.

### Task 5: Processes

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **name** of the malicious process? Enter your answer in a **defanged** format. | `INITIAL_LANTERN[.]exe` |
| 2 | What is the **directory path** where the malicious process is located? | `C:\Users\Administrator\AppData\SpcTmp\` |
| 3 | What is the **remote port** used by the malicious process? | `8888` |
| 4 | What is the **full path** of the suspicious program for AnyDesk? Enter your answer in a **defanged** format. | `D:\AnyDesk[.]exe` |
| 5 | What **port** is used by the LMV Co. firewall rules? | `5985` |

**Explicación:** El análisis de procesos (T1055 Process Injection, T1059) encuentra el binario malicioso `INITIAL_LANTERN[.]exe` (defanged) en `C:\Users\Administrator\AppData\SpcTmp\` con conexión saliente al puerto remoto `8888`. Se detecta un AnyDesk sospechoso `D:\AnyDesk[.]exe` (RAT legítimo usado como backdoor) y las reglas de firewall de LMV Co. usan el puerto `5985` (WinRM).

### Task 6: Persistence

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which **user account** will be used to run the AnyDesk application? | `Public` |
| 2 | What is the **value data** stored in the **"Userinit" key**? Enter your answer in a **defanged** format. | `C:\Windows\system32\userinit[.]exe, cmd[.]exe /c "start /min netsh[.]exe -c"` |
| 3 | What is the **name** of the suspicious **DLL** linked under the **netshell** hive key? | `.\fwshield.dll` |

**Explicación:** La persistencia vía registro: AnyDesk se configura para ejecutarse con la cuenta `Public` (T1078 Valid Accounts / T1547.001). El key **Userinit** (`HKLM\SOFTWARE\...\Winlogon\Userinit`) fue modificado con valor defanged `C:\Windows\system32\userinit[.]exe, cmd[.]exe /c "start /min netsh[.]exe -c"` (T1547.004). El hive **netshell** enlaza la DLL sospechosa `.\fwshield.dll` (T1574.001 hijacking de DLL).

### Task 7: Services

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **name** of the suspicious active service? | `LMVCSS` |
| 2 | What is the **SHA256 value** of the suspicious active service executable? | `E9AA7564B2D1D612479E193A9F8CB70DF9CFBE02A39900EEE22FE266F5320EBF` |
| 3 | What is the **name** of the non-running service that caught our attention? | `aurora-agent` |
| 4 | What is the **SHA256 value** of the non-running service executable? | `D5C8BF2D3B56B21639D8152DB277DD714BA1A61BDAF2350BD0FF7E61D2A99003` |
| 5 | What is the **original filename** of the non-running service executable? Enter your answer in a **defanged** format. | `x3xv5weg[.]exe` |

**Explicación:** Crear **servicios** es una técnica de persistencia (T1543.003 Create or Modify System Process: Windows Service). El servicio activo sospechoso es `LMVCSS` (SHA256 `E9AA7564B2D1D612479E193A9F8CB70DF9CFBE02A39900EEE22FE266F5320EBF`); el servicio no activo que llama la atención es `aurora-agent` (SHA256 `D5C8BF2D3B56B21639D8152DB277DD714BA1A61BDAF2350BD0FF7E61D2A99003`) cuyo original filename es `x3xv5weg[.]exe` (defanged) — services con nombres no estándar y binarios en ubicaciones inusuales son indicadores claros.

### Task 8: Network

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **parent process** name of the suspicious executable (INITIAL_LANTERN) process? Enter your answer in a **defanged** format. | `services[.]exe` |
| 2 | Which **user name** is used for the SSH connection attempts? | `James` |
| 3 | What is the **parent process** of the malicious aurora process? Enter your answer in a **defanged** format. | `svchost[.]exe` |
| 4 | What is the **file name** located in the default user's temp directory? Enter your answer in a **defanged** format. | `jmp[.]exe` |
| 5 | What is the **name** of the potential proxy script located in the suspicious non-default temp folder? Enter your answer in a **defanged** format. | `Invoke-SocksProxy[.]psm1` |
| 6 | What is the **SHA256 value** of the potential proxy script located in the suspicious non-default temp folder? | `E7697645F36DE5978C1B640B6B3FC819E55B00EE8D9E9798919C11CC7A6FC88B` |
| 7 | What is the **label** of the hidden disc volume? | `Setups` |

**Explicación:** El análisis de red (activos espía: T1016, T1049) revela: el proceso padre del ejecutable INITIAL_LANTERN es `services[.]exe` (defanged); los intentos de conexión SSH usan el usuario `James` (T1021.001 Remote Services); el proceso aurora tiene como padre `svchost[.]exe` (defanged). En temp del usuario por defecto hay `jmp[.]exe` (defanged); en la carpeta temp no por defecto sospechosa hay un script proxy **`Invoke-SocksProxy[.]psm1`** (T1090 Proxy) con SHA256 `E7697645F36DE5978C1B640B6B3FC819E55B00EE8D9E9798919C11CC7A6FC88B`. El volumen oculto está etiquetado como `Setups`.

---

**Metodología:**
1. **Reliability of the System Tools:** revisar perfiles de PowerShell (script que se ejecuta cada vez que se lanza PowerShell) y variables de entorno, ya que los atacantes pueden modificarlas para secuestrar el flujo de ejecución (T1574.007). La tool usada para borrar logs fue `wevtutil`; las credenciales se almacenaron/robaron vía la clave WDigest `HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest`.
2. **System info:** anotar hostname (`CCTL-WS-018-b21`), OS version (`10.0.17763`) y zona horaria (`Turkey Standard Time`).
3. **User accounts:** identificar cuentas sospechosas (3) y sus SIDs; el SID de Guest es `S-1-5-21-1966530601-3185510712-10604624-501` y la cuenta Admin con el typo deliberado se logueó por última vez el `2/28/2024 10:21:10 AM`.
4. **Processes:** encontrar procesos maliciosos (defanged: `INITIAL_LANTERN[.]exe` en `C:\Users\Administrator\AppData\SpcTmp\` con puerto remoto `8888`), programas sospechosos de AnyDesk (`D:\AnyDesk[.]exe`) y puertos de reglas de firewall (`5985`).
5. **Persistence:** revisar claves de registro: AnyDesk correrá con la cuenta `Public`; el key **Userinit** tiene el valor defanged `C:\Windows\system32\userinit[.]exe, cmd[.]exe /c "start /min netsh[.]exe -c"`; el hive **netshell** enlaza la DLL sospechosa `.\fwshield.dll`.
6. **Services:** identificar el servicio activo sospechoso `LMVCSS` (SHA256 `E9AA7564...0EBF`) y el servicio no activo `aurora-agent` (SHA256 `D5C8BF2D...A99003`, original filename `x3xv5weg[.]exe`).
7. **Network:** analizar procesos padre (`services[.]exe` de INITIAL_LANTERN, `svchost[.]exe` del proceso aurora), intentos de conexión SSH (`James`), archivos en temp (`jmp[.]exe`), el script proxy `Invoke-SocksProxy[.]psm1` (SHA256 `E7697645...C88B`) y el volumen oculto etiquetado `Setups`.

**Learning chain:** system tools (wevtutil, WDigest) → system info (hostname/OS/time) → user accounts (3 sospechosas, SID Guest, login admin) → processes (INITIAL_LANTERN[.]exe, AnyDesk, puertos) → persistence (Public, Userinit, fwshield.dll) → services (LMVCSS, aurora-agent) → network (procesos padre, SSH James, proxy psm1, volumen Setups)

**MITRE ATT&CK:** T1070.001 (Indicator Removal: Clear Windows Event Logs), T1003.001 (OS Credential Dumping: LSASS), T1547.002 (Boot/Logon Autostart Execution: Authentication Package), T1574.007 (Hijack Execution Flow: Path Interception by PATH Environment Variable), T1055 (Process Injection), T1090 (Proxy), T1021.001 (Remote Services: Remote Desktop Protocol)

**Fuente:** [TryHackMe - Windows Incident Surface](https://tryhackme.com/room/winincidentsurface)