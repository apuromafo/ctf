# Hunt Me I: Payment Collectors

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Threat Hunting / DFIR | huntmeipaymentcollectors | https://tryhackme.com/room/huntmeipaymentcollectors | 02 Level Medium | TryHackMe | Elastic (ELK), Sysmon, Powercat, PowerView, DNS exfiltration | Exfiltración de datos financieros |

---

**Contexto:** El viernes 15 de septiembre de 2023, Michael Ascot, Director Financiero Senior de SwiftSpend, revisa su correo en Outlook y encuentra un mensaje aparentemente enviado por Abotech Waste Management sobre una factura mensual de sus servicios. Michael descarga y abre el adjunto sin pensarlo. A la semana siguiente recibe otro correo de su contacto en Abotech advirtiendo de que fueron hackeados y que revise con cuidado cualquier adjunto enviado por sus empleados, pero el daño ya está hecho. Se entrega una instancia Elastic para cazar actividad maliciosa en la estación de Michael (WKSTN-01) y dentro del dominio SwiftSpend. La cadena: phishing → ZIP malicioso → LNK (falsificado como PDF) → PowerShell → powercat (reverse shell) → enumeración → mapeo de recurso compartido → copia y compresión → exfiltración por DNS.

## Solucionario

### Task 1: Nombre del adjunto ZIP
**Explicación:**

Se buscan los eventos de creación de archivo (Sysmon Event ID 11) generados por Outlook (`OUTLOOK.EXE`) al descargar el adjunto de correo. Se filtra por `user.name: michael.ascot` y `*.zip*`.

Respuesta: `Invoice_AT_2023-227.zip`

### Task 2: Archivo contenido en el ZIP
**Explicación:**

Justo después del evento de creación del ZIP se observa un evento de flujo de archivo (Sysmon Event ID 15) que revela el archivo extraído y su ruta en Temp, un `.lnk` disfrazado de PDF.

Respuesta: `Payment_Invoice.pdf.lnk.lnk`

### Task 3: Proceso de línea de comandos que nació del archivo
**Explicación:**

Usando la función *View surrounding documents* sobre el archivo extraído, se localiza el evento de creación de proceso (Event ID 1) que lanza el payload. El campo `process.name` revela el intérprete.

Respuesta: `powershell.exe`

### Task 4: URL de descarga de la herramienta reverse shell
**Explicación:**

La línea de comandos de PowerShell muestra la descarga y ejecución de un script de reverse shell desde GitHub (`Invoke-Expression` + `DownloadString`), junto con el inicio de la conexión remota.

Respuesta: `https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1`

### Task 5: Puerto de conexión hacia el atacante
**Explicación:**

En la misma línea de comandos de powercat aparece el argumento `-p` con el puerto al que la estación inicia la conexión saliente para el reverse shell.

Respuesta: `19282`

### Task 6: Primer binario nativo de enumeración
**Explicación:**

Tras obtener acceso remoto, se buscan eventos de creación de proceso (Event ID 1) ordenados cronológicamente para ver la primera enumeración del sistema. El binario nativo consulta configuración y entorno del sistema operativo.

Respuesta: `systeminfo.exe`

### Task 7: URL del script de enumeración del dominio
**Explicación:**

Tras el acceso se descarga un script de enumeración de Active Directory. Se filtra por `*PowerView.ps1* AND *http*` para obtener la URL completa de descarga.

Respuesta: `https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerView/powerview.ps1`

### Task 8: Recurso compartido mapeado
**Explicación:**

El atacante usa `net.exe` para mapear una unidad de red apuntando a un recurso compartido del dominio (en este caso la unidad `Z:`).

Respuesta: `SSF-FinancialRecords`

### Task 9: Directorio de copia del recurso
**Explicación:**

Con `robocopy` (`"C:\Windows\system32\Robocopy.exe" . C:\Users\michael.ascot\downloads\exfiltration /E`) el atacante copia el contenido del recurso compartido a una carpeta local de staging.

Respuesta: `C:\Users\michael.ascot\downloads\exfiltration`

### Task 10: Archivo Excel extraído del recurso
**Explicación:**

Buscando creaciones de archivo dentro del directorio de staging (o filtrando por `*.xlsx`) se identifica el documento de interés extraído de `SSF-FinancialRecords`.

Respuesta: `ClientPortfolioSummary.xlsx`

### Task 11: Archivo comprimido para la exfiltración
**Explicación:**

Antes de exfiltrar, los datos se empaquetan. Se observa actividad de `Microsoft.PowerShell.Archive` (módulo `Compress-Archive`) y se busca el archivo `.zip` resultante en el staging.

Respuesta: `exfilt8me.zip`

### Task 12: MITRE ID de la técnica de exfiltración
**Explicación:**

Tras la creación del ZIP aparecen múltiples consultas `nslookup.exe` cuyo subdominio contiene datos codificados en Base64 (fragmentos del archivo): clásica **exfiltración por DNS**, un protocolo alternativo al canal habitual de datos.

Respuesta: `T1048`

### Task 13: Dominio del servidor del atacante
**Explicación:**

Todas las consultas DNS de exfiltración terminan en el mismo dominio, que es el que recoge los datos fragmentados.

Respuesta: `haz4rdw4re.io`

### Task 14: Flag tras reconstruir el archivo adicional
**Explicación:**

El atacante exfiltra además un archivo adicional (una wallet/cartera de Bitcoin, pista `BitcoinWalletPasscode.txt`). Se toman los fragmentos Base64 de los eventos `nslookup`, se concatenan y se decodifican (p. ej. en CyberChef) para reconstruir el archivo y obtener la flag.

Respuesta: `THM{1497321f4f6f059a52dfb124fb16566e}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del adjunto ZIP | `Invoice_AT_2023-227.zip` |
| 2 | Archivo contenido en el ZIP | `Payment_Invoice.pdf.lnk.lnk` |
| 3 | Proceso que nació del archivo extraído | `powershell.exe` |
| 4 | URL de descarga del reverse shell | `https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1` |
| 5 | Puerto de conexión al atacante | `19282` |
| 6 | Primer binario nativo de enumeración | `systeminfo.exe` |
| 7 | URL del script de enumeración del dominio | `https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerView/powerview.ps1` |
| 8 | Recurso compartido mapeado | `SSF-FinancialRecords` |
| 9 | Directorio de copia del recurso | `C:\Users\michael.ascot\downloads\exfiltration` |
| 10 | Archivo Excel extraído del recurso | `ClientPortfolioSummary.xlsx` |
| 11 | Archivo comprimido para exfiltración | `exfilt8me.zip` |
| 12 | MITRE ID de la técnica de exfiltración | `T1048` |
| 13 | Dominio del servidor del atacante | `haz4rdw4re.io` |
| 14 | Flag tras reconstruir el archivo | `THM{1497321f4f6f059a52dfb124fb16566e}` |

---

**Metodología:** Threat hunting sobre telemetría en ELK Stack (Kibana) con Sysmon (Event ID 1, 11, 15) y registros de PowerShell/red: pivotes de artefacto a proceso, seguimiento de cadena padre/hijo, enumeración (systeminfo, net, PowerView), colección (mapeo de recurso + robocopy), staging (Compress-Archive) y exfiltración por DNS (nslookup + Base64) con reconstrucción del archivo en CyberChef.

**Learning chain:** Phishing → descarga ZIP → extracción LNK (PDF falso) → PowerShell → powercat → reverse shell → enumeración del sistema → enumeración del dominio → mapeo de recurso → copia a staging → compresión → exfiltración por DNS → reconstrucción del flag.

**Lección:** *La exfiltración por DNS es sigilosa porque abusa de un protocolo de confianza: la señal de alarma aparece al ver nslookup con subdominios codificados en Base64 y latencias anómalas entre consultas.*

**MITRE ATT&CK:** T1566.001 Phishing: Spearphishing Attachment · T1204.001 User Execution: Malicious Link · T1059.001 PowerShell · T1105 Ingress Tool Transfer · T1012 Query Registry · T1016 System Network Configuration Discovery · T1082 System Information Discovery · T1087 Discovery · T1021.002 Remote Services: SMB/Windows Admin Shares · T1005 Data from Local System · T1560.001 Archive Collected Data · T1048 Exfiltration Over Alternative Protocol.

**Fuente:** [TryHackMe - Hunt Me I: Payment Collectors](https://tryhackme.com/room/huntmeipaymentcollectors)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.