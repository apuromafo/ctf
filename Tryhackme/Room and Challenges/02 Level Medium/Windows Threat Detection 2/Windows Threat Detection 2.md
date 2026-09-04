# Windows Threat Detection 2 [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `windowsthreatdetection2`
* **Link:** https://tryhackme.com/room/windowsthreatdetection2
* **Objeto:** Detectar y analizar la actividad de un atacante tras el acceso inicial en una máquina Windows usando Sysmon, Event Viewer y herramientas de credenciales/datos (stealer).

---

## Solucionario de Tareas / Task Solutions

> Segunda sala de la serie de detección de amenazas en Windows. Se analiza el post-exploit: descubrimiento, recolección de credenciales, staging y exfiltración.
> Second room of the Windows threat-detection series. Post-exploit analysis: discovery, credential harvesting, staging and exfiltration.

### Tarea 1 / Task 1 — Initial Checks

**Abre CMD y teclea `net user Administrator`. ¿A qué grupo privilegiado pertenece el usuario? / Open CMD and type "net user Administrator". Which privileged group does the user belong to?**
`Administrators`

**Abre Event Viewer y busca tu comando en los logs de Sysmon. ¿Cuál es el campo "Image" del comando net que acabas de ejecutar? / Open Event Viewer and try to find your command in Sysmon logs. What is the "Image" field of the net command you just run?**
`C:\Windows\System32\net.exe`

Fuente / Source: https://simontaplin.net/2025/07/16/answers-for-the-tryhackme-windows-threat-detection-2-room/

### Tarea 2 / Task 2 — Invoice Malware (Discovery)

**Mirando los logs de Sysmon, ¿cuál es el primer comando que ejecuta invoice.pdf.exe? / Looking at Sysmon logs, what is the first command the invoice.pdf.exe executes?**
`whoami`

**¿Qué comando usó el malware para comprobar la presencia de MS Defender EDR? / Which command did the malware use to check the presence of MS Defender EDR?**
`cmd /c "tasklist /v | findstr MsSense.exe || echo No MS Defender EDR"`

**¿A qué dominio envió el malware los datos descubiertos? / To which domain did the malware send the discovered data?**
`exfil.beecz.cafe`

Fuente / Source: https://simontaplin.net/2025/07/16/answers-for-the-tryhackme-windows-threat-detection-2-room/

### Tarea 3 / Task 3 — Sensitive Data

**¿Cuál es la contraseña de Facebook que el usuario guardó en Chrome? (Chrome menu > Passwords and autofill > Password Manager) / What is the Facebook password that the user saved in Chrome?**
`nsAghv51BBav90!`

**¿Qué clave SSH interesante guarda el usuario en disco? (Empieza a buscar desde C:\Users\Administrator) / Which interesting SSH key does the user store on disk? (Start your search from C:\Users\Administrator)**
`thm-access-database.key`

**¿Cuál es el archivo PDF secreto que explica la red interna de TryHackMe? (Escritorio, Downloads y Documents) / What is the secret PDF file explaining TryHackMe's internal network? (Desktop, Downloads, Documents)**
`thm-network-diagram-2025.pdf`

Fuente / Source: https://simontaplin.net/2025/07/16/answers-for-the-tryhackme-windows-threat-detection-2-room/

### Tarea 4 / Task 4 — Stealer (Staging & Exfiltration)

**Mirando los logs de Sysmon, ¿qué directorio crea el stealer? / Looking at Sysmon logs, what directory does the stealer create?**
`staging_58f1`

**¿Qué tres extensiones de archivo busca el malware? (formato: separadas por coma en orden alfabético) / Which three file extensions does the malware search for?**
`docx, pdf, xlsx`

**¿Qué cmdlet de PowerShell usa el malware para obtener el contenido del portapapeles? / Which PowerShell cmdlet does the malware use to get clipboard content?**
`Get-ClipBoard`

**¿A qué dominio exfiltra el malware los datos? / Which domain does the malware exfiltrate the data to?**
`collecteddata-storage-2025.s3.amazonaws.com`

Fuente / Source: https://simontaplin.net/2025/07/16/answers-for-the-tryhackme-windows-threat-detection-2-room/

### Tarea 5 / Task 5 — Tool Transfer / Internet

**Abre Chrome en la VM y navega a la URL. ¿Cuál es la flag en la respuesta? / Open the Chrome browser on the VM and navigate to the URL. What is the flag in the response?**
`THM{just_use_web_browser}`

**Ahora abre CMD y descarga el archivo de la misma URL usando curl.exe. ¿Cuál es la flag? / Next, open CMD and download the file from the same URL using curl.exe. What is the flag in the response?**
`THM{curl_is_cool}`

**Continúa con el mismo CMD y URL, pero ahora usando certutil.exe. ¿Cuál es la flag? / Continue with the same CMD and URL, but now using certutil.exe. What is the flag in the response?**
`THM{abusing_certutil}`

**Finalmente, descarga el mismo archivo usando PowerShell IWR. ¿Cuál es la flag? / Finally, download the same file using PowerShell IWR. What is the flag in the response?**
`THM{power_of_powershell}`

Fuente / Source: https://simontaplin.net/2025/07/16/answers-for-the-tryhackme-windows-threat-detection-2-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/07/16/answers-for-the-tryhackme-windows-threat-detection-2-room/*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
