# Windows Threat Detection 2

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `windowsthreatdetection2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsthreatdetection2) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Sysmon / Event Viewer / discovery / credential harvesting / staging / exfiltration / stealer |
| **Impacto** | Detectar y analizar el post-exploit de un atacante en Windows (descubrimiento, robo de credenciales y exfiltración) |

---

**Contexto:** Segunda sala de la serie de detección de amenazas en Windows. Se analiza el post-exploit: descubrimiento, recolección de credenciales, staging y exfiltración usando Sysmon, Event Viewer y herramientas de datos/credenciales.

## Solucionario

### Task 1: Initial Checks

**Explicación:**

Abre CMD y teclea `net user Administrator`. El grupo privilegiado al que pertenece el usuario es `Administrators`. Abre Event Viewer y busca tu comando en los logs de Sysmon: el campo "Image" del comando net que acabas de ejecutar es `C:\Windows\System32\net.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which privileged group does the user belong to? | `Administrators` |
| 2 | What is the "Image" field of the net command you just run? | `C:\Windows\System32\net.exe` |

### Task 2: Invoice Malware (Discovery)

**Explicación:**

Mirando los logs de Sysmon, el primer comando que ejecuta `invoice.pdf.exe` es `whoami`. El comando usado por el malware para comprobar la presencia de MS Defender EDR es `cmd /c "tasklist /v | findstr MsSense.exe || echo No MS Defender EDR"`. El dominio al que el malware envió los datos descubiertos es `exfil.beecz.cafe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first command the invoice.pdf.exe executes? | `whoami` |
| 2 | Which command did the malware use to check the presence of MS Defender EDR? | `cmd /c "tasklist /v \| findstr MsSense.exe \|\| echo No MS Defender EDR"` |
| 3 | To which domain did the malware send the discovered data? | `exfil.beecz.cafe` |

### Task 3: Sensitive Data

**Explicación:**

La contraseña de Facebook que el usuario guardó en Chrome (Chrome menu > Passwords and autofill > Password Manager) es `nsAghv51BBav90!`. La clave SSH interesante que guarda el usuario en disco (empezando desde `C:\Users\Administrator`) es `thm-access-database.key`. El archivo PDF secreto que explica la red interna de TryHackMe (Desktop, Downloads y Documents) es `thm-network-diagram-2025.pdf`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Facebook password that the user saved in Chrome? | `nsAghv51BBav90!` |
| 2 | Which interesting SSH key does the user store on disk? (Start your search from C:\Users\Administrator) | `thm-access-database.key` |
| 3 | What is the secret PDF file explaining TryHackMe's internal network? (Desktop, Downloads, Documents) | `thm-network-diagram-2025.pdf` |

### Task 4: Stealer (Staging & Exfiltration)

**Explicación:**

Mirando los logs de Sysmon, el directorio que crea el stealer es `staging_58f1`. Las tres extensiones de archivo que busca el malware (formato: separadas por coma en orden alfabético) son `docx, pdf, xlsx`. El cmdlet de PowerShell que usa el malware para obtener el contenido del portapapeles es `Get-ClipBoard`. El dominio al que exfiltra el malware los datos es `collecteddata-storage-2025.s3.amazonaws.com`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What directory does the stealer create? | `staging_58f1` |
| 2 | Which three file extensions does the malware search for? | `docx, pdf, xlsx` |
| 3 | Which PowerShell cmdlet does the malware use to get clipboard content? | `Get-ClipBoard` |
| 4 | Which domain does the malware exfiltrate the data to? | `collecteddata-storage-2025.s3.amazonaws.com` |

### Task 5: Tool Transfer / Internet

**Explicación:**

Abre Chrome en la VM y navega a la URL. La flag en la respuesta es `THM{just_use_web_browser}`. Ahora abre CMD y descarga el archivo de la misma URL usando `curl.exe`: la flag es `THM{curl_is_cool}`. Continúa con el mismo CMD y URL, pero ahora usando `certutil.exe`: la flag es `THM{abusing_certutil}`. Finalmente, descarga el mismo archivo usando PowerShell IWR: la flag es `THM{power_of_powershell}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag in the response (Chrome)? | `THM{just_use_web_browser}` |
| 2 | What is the flag (curl.exe)? | `THM{curl_is_cool}` |
| 3 | What is the flag (certutil.exe)? | `THM{abusing_certutil}` |
| 4 | What is the flag (PowerShell IWR)? | `THM{power_of_powershell}` |

---

**Metodología:**

1. Verificar el usuario y el grupo privilegiado (`Administrators`) con `net user Administrator`, y localizar el "Image" del proceso en Sysmon.
2. Analizar el malware `invoice.pdf.exe`: primer comando (`whoami`), comprobación del EDR (`tasklist | findstr MsSense.exe`) y exfiltración a `exfil.beecz.cafe`.
3. Buscar datos sensibles en Chrome (Facebook password), disco (`thm-access-database.key`) y PDFs (`thm-network-diagram-2025.pdf`).
4. Rastrear el stealer: directorio `staging_58f1`, extensiones `docx,pdf,xlsx`, `Get-ClipBoard` y exfiltración a S3.
5. Probar distintas herramientas de descarga (Chrome, curl, certutil, IWR) y capturar las flags.

**Learning chain:** net user Administrator -> Administrators -> invoice.pdf.exe -> whoami -> tasklist/findstr (EDR check) -> exfil.beecz.cafe -> Chrome saved password -> thm-access-database.key -> thm-network-diagram-2025.pdf -> stealer staging_58f1 -> docx,pdf,xlsx -> Get-ClipBoard -> S3 exfil -> curl/certutil/IWR flags

**Lección:** *El post-exploit de un stealer en Windows se reconstruye cruzando Sysmon (procesos, comandos, creación de directorios) y datos de usuario (navegador, disco); herramientas legítimas como certutil o curl.exe son reutilizadas por los atacantes para transferir archivos.*

**MITRE ATT&CK:** T1059.001 (PowerShell) · T1555.003 (Web Session Cookies / Password Manager) · T1005 (Data from Local System) · T1567.002 (Exfiltration to Cloud Storage) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Windows Threat Detection 2](https://tryhackme.com/room/windowsthreatdetection2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
