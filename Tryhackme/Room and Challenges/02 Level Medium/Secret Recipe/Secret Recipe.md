# Secret Recipe

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Forense de Registro de Windows (DFIR) | secretrecipe | https://tryhackme.com/room/secretrecipe | 02 Level Medium | TryHackMe | Forense del registro de Windows (Registry Explorer/EZ Tools), hives SYSTEM/SAM/SOFTWARE/NTUSER.DAT, UserAssist, RecentDocs, RunMRU, WordWheelQuery, NetworkList, Macros de análisis de actividad | Detección de una amenaza interna: un técnico de TI que exfiltró la "receta secreta" de una cafetería, con cuenta backdoor, VPN y transferencia de archivos evidenciada en el registro |

---

**Contexto:** La sala **Secret Recipe** presenta un caso de investigación de **amenaza interna**: Jasmine tiene la receta secreta de su cafetería en su portátil y el técnico de TI (James) es sospechoso de copiarla. Su equipo fue incautado pero no se encontraron rastros en disco, así que el equipo de seguridad extrajo los **hives del registro** (SYSTEM, SECURITY, SOFTWARE, SAM, NTUSER.DAT, UsrClass.dat) y pide analizarlos con **Registry Explorer** y las herramientas de la carpeta "EZ Tools". Las preguntas recorren el registro por sus rutas clave: nombre del equipo y cuenta backdoor en SAM, conexión VPN y zonas horarias en NetworkList, recursos compartidos en LanmanServer, IP DHCP en TCP/IP, y en NTUSER.DAT los artefactos de actividad del usuario (RecentDocs, RunMRU, WordWheelQuery, UserAssist) que delatan los archivos accedidos, los comandos ejecutados y el tiempo de cada programa en foco.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación del caso: James usó su máquina para copiar la receta secreta; los hives del registro están en `C:\Users\Administrator\Desktop\Artifacts` y las herramientas de análisis en `C:\Users\Administrator\Desktop\EZ Tools`. Se cargan los hives en Registry Explorer.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| 1. Leer el escenario y cargar los hives | `No answer needed` |
| 2. ¿Cuántos hives del registro se proporcionan para el análisis? | `6` |

### Task 2: Forense del registro de Windows / Windows Registry Forensics
**Explicación:** Análisis de los hives con Registry Explorer. En el hive **SYSTEM** (`CurrentControlSet\Control\ComputerName`) aparece el nombre del equipo; en **SAM** (`SAM\Domains\Account\Users`) la fecha de creación del Administrador, su RID (500), el número de cuentas y la cuenta backdoor `bdoor` con RID 1013; en **SOFTWARE** (`Microsoft\Windows NT\CurrentVersion\NetworkList`) la conexión VPN del host (ProtonVPN) y su hora de primera conexión; en **SYSTEM** (`LanmanServer\Shares` y `Services\Tcpip\Parameters\Interfaces`) el tercer recurso compartido y la última IP DHCP. Con **NTUSER.DAT** se revisan `Explorer\RecentDocs` (archivo de la receta, texto reciente y elementos por extensión), `RunMRU` (comando `pnputil /enum-interfaces`), `WordWheelQuery` (búsqueda de `netcat`) y `UserAssist` (ejecuciones de PowerShell, herramienta de monitoreo y tiempo en foco de ProtonVPN, además de la ruta de Everything.exe).

```text
SYSTEM\ControlSet001\Control\ComputerName\ComputerName -> JAMES
SAM\SAM\Domains\Account\Users -> Administrator "Created on" 2021-03-17 14:58:48, RID 500, 7 cuentas, bdoor (RID 1013)
SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList -> ProtonVPN, First Connect 2022-10-12 19:52:36
SYSTEM\CurrentControlSet\Services\LanmanServer\Shares -> 3er share C:\RESTRICTED FILES
SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces -> Last DHCP IP 172.31.2.197
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs -> secret-recipe.pdf, secret-code.txt
NTUSER.DAT\...\Explorer\RunMRU -> pnputil /enum-interfaces
NTUSER.DAT\...\Explorer\WordWheelQuery -> netcat
NTUSER.DAT\...\Explorer\UserAssist -> powershell.exe x3, wireshark, ProtonVPN 343s,
    C:\Users\Administrator\Downloads\tools\Everything\Everything.exe
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the computer name of the machine found in the registry? | `JAMES` |
| 2 | When was the Administrator account created? (format: YYYY-MM-DD HH:MM:SS) | `2021-03-17 14:58:48` |
| 3 | What is the RID of the Administrator account? | `500` |
| 4 | How many user accounts are present on this machine? | `7` |
| 5 | There seems to be a suspicious account created as a backdoor with RID 1013. What is the account name? | `bdoor` |
| 6 | What is the VPN connection this host connected to? | `ProtonVPN` |
| 7 | When was the VPN connection first observed? (format: YYYY-MM-DD HH:MM:SS) | `2022-10-12 19:52:36` |
| 8 | There were three shared folders observed on his machine. What is the path of the third share? | `C:\RESTRICTED FILES` |
| 9 | What is the last DHCP IP assigned to this host? | `172.31.2.197` |
| 10 | The suspect seems to have accessed a file containing the secret coffee recipe. What is the name of the file? | `secret-recipe.pdf` |
| 11 | The suspect executed multiple commands using the Run window. What command was used to enumerate the network interfaces? | `pnputil /enum-interfaces` |
| 12 | The user searched for a network utility tool to transfer files using the file explorer. What is the name of that tool? | `netcat` |
| 13 | What is the recent text file opened by the suspect? | `secret-code.txt` |
| 14 | How many times was PowerShell executed on this host? | `3` |
| 15 | The suspect also executed a network monitoring tool. What is the name of the tool? | `wireshark` |
| 16 | Registry Hives also note the amount of time a process is in focus. Examine the Hives and confirm for how many seconds was ProtonVPN executed? | `343` |
| 17 | Everything.exe is a utility used to search for files in a Windows machine. What is the full path from which everything.exe was executed? | `C:\Users\Administrator\Downloads\tools\Everything\Everything.exe` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the computer name of the machine found in the registry? | `JAMES` |
| 2 | When was the Administrator account created? (format: YYYY-MM-DD HH:MM:SS) | `2021-03-17 14:58:48` |
| 3 | What is the RID of the Administrator account? | `500` |
| 4 | How many user accounts are present on this machine? | `7` |
| 5 | What is the account name of the backdoor with RID 1013? | `bdoor` |
| 6 | What is the VPN connection this host connected to? | `ProtonVPN` |
| 7 | When was the VPN connection first observed? (format: YYYY-MM-DD HH:MM:SS) | `2022-10-12 19:52:36` |
| 8 | What is the path of the third shared folder observed on his machine? | `C:\RESTRICTED FILES` |
| 9 | What is the last DHCP IP assigned to this host? | `172.31.2.197` |
| 10 | What is the name of the file containing the secret coffee recipe? | `secret-recipe.pdf` |
| 11 | What command was used to enumerate the network interfaces (Run window)? | `pnputil /enum-interfaces` |
| 12 | What network utility did the user search for in the file explorer? | `netcat` |
| 13 | What is the recent text file opened by the suspect? | `secret-code.txt` |
| 14 | How many times was PowerShell executed on this host? | `3` |
| 15 | What network monitoring tool was executed? | `wireshark` |
| 16 | For how many seconds was ProtonVPN in focus (executed)? | `343` |
| 17 | What is the full path from which everything.exe was executed? | `C:\Users\Administrator\Downloads\tools\Everything\Everything.exe` |

---

**Metodología:** Carga de los hives en Registry Explorer (SYSTEM, SECURITY, SOFTWARE, SAM, NTUSER.DAT, UsrClass.dat) → revisión sistemática de claves: ComputerName y SAM (identidad, RID y cuentas) → NetworkList (VPN y conexiones) → LanmanServer y Tcpip (shares e IP) → artefactos de usuario en NTUSER.DAT (RecentDocs, RunMRU, WordWheelQuery, UserAssist) → correlación para reconstruir la exfiltración (acceso al PDF, uso de netcat, VPN e intentos de ocultación).

**Learning chain:** Forense de registro en Windows → mapeo hive/clave/valor → perfilado de usuario y sistema → rastreo de actividad reciente (RecentDocs/RunMRU/UserAssist) → detección de cuenta backdoor y VPN → evidencia de exfiltración y línea de tiempo.

**Lección:** *El registro de Windows es una fuente de evidencia forense persistente: aunque se borren los archivos, claves como RecentDocs, UserAssist y NetworkList delatan qué se abrió, cuándo, desde dónde y qué herramientas (netcat, VPN) se usaron para exfiltrar datos.*

**MITRE ATT&CK:** T1005 Data from Local System · T1105 Ingress Tool Transfer / transferencia con netcat · T1098 Account Manipulation (cuenta backdoor `bdoor`) · T1021.001 Remote Services (acceso remoto) · T1071 Application Layer Protocol (VPN) · T1560 Archive Collected Data / almacenamiento en `C:\RESTRICTED FILES` · T1070.001 Indicator Removal (intento de borrado de rastros).

**Fuente:** [TryHackMe - Secret Recipe](https://tryhackme.com/room/secretrecipe)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.