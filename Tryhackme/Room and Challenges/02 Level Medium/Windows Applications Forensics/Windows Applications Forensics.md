# Windows Applications Forensics

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `windowsapplications` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsapplications) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Windows forensics / browser artifacts / LNK / email / SharePoint / downloads / C2 |
| **Impacto** | Analizar artefactos de aplicaciones Windows (navegador, correo, SharePoint) para reconstruir una cadena de phishing/exfiltración |

---

**Contexto:** Sala DFIR de Windows centrada en artefactos de aplicaciones: análisis de navegador (historial, descargas), correo (julianne.westcott@hotmail.com), documentos LNK, SharePoint y URLs de C2/exfiltración para reconstruir el incidente.

## Solucionario

### Task 1: (Intro)

**Explicación:**

Introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: (Correo/Email artifact)

**Explicación:**

Artefacto de correo: el remitente es `mike.myers`; el enlace malicioso es `hxxp[://]hrcbishtek[.]com/a`; el asunto/motivo es `server power`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Sender) | `1. mike.myers` |
| 2 | (Link) | `2. hxxp[://]hrcbishtek[.]com/a` |
| 3 | (Subject) | `3. server power` |

### Task 3: (Descarga inicial / Initial download)

**Explicación:**

Descarga inicial: el archivo es `C:\Users\Public\pagefilerpqy.exe` y el timestamp `17:21`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (File path) | `1. C:\Users\Public\pagefilerpqy.exe` |
| 2 | (Timestamp) | `2. 17:21` |

### Task 4: (Artefacto LNK/malware)

**Explicación:**

El ejecutable malicioso es `C:\Windows\Temp\aKzjdD.exe` con fecha `03/07/2024 17:53:53`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Malware path) | `1. C:\Windows\Temp\aKzjdD.exe` |
| 2 | (Timestamp) | `2. 03/07/2024 17:53:53` |

### Task 5: (C2 / phishing login)

**Explicación:**

C2/phishing: la URL de login es `hxxps[://]login[.]lohelper[.]com/auth/client_id=59bcc3ad677`; el timestamp es `03/04/2024 20:53:32`; y la cookie/parámetro es `ESTSAUTHPERSISTENT`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Login URL) | `1. hxxps[://]login[.]lohelper[.]com/auth/client_id=59bcc3ad677` |
| 2 | (Timestamp) | `2. 03/04/2024 20:53:32` |
| 3 | (Cookie/param) | `3. ESTSAUTHPERSISTENT` |

### Task 6: (Tracking/Exfil URL)

**Explicación:**

La URL de tracking/exfiltración es `hxxps[://]kamehasuitens[.]info/track`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Tracking URL) | `1. hxxps[://]kamehasuitens[.]info/track` |

### Task 7: (C2 URL 2)

**Explicación:**

La URL C2 (login falso) es `hxxps[://]login[.]dxsupport[.]net/mmTQJpka`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (URL) | `1. hxxps[://]login[.]dxsupport[.]net/mmTQJpka` |

### Task 8: (Víctima / Victim)

**Explicación:**

El correo de la víctima es `julianne.westcott@hotmail.com`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Victim email) | `1. julianne.westcott@hotmail.com` |

### Task 9: (Staging/Exfiltration)

**Explicación:**

Staging/exfiltración: el archivo de staging es `system_update.zip` y la URL del script PowerShell es `hxxp[://]cdn[.]nautilusco[.]net/a[.]ps1`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Staging file) | `1. system_update.zip` |
| 2 | (PS1 URL) | `2. hxxp[://]cdn[.]nautilusco[.]net/a[.]ps1` |

### Task 10: (SharePoint / Lugar de exfil)

**Explicación:**

El sitio SharePoint donde se sube/exfiltra la información es `https://swiftspendlogistics.sharepoint.com/sites/ProjectManagement`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (SharePoint site) | `1. https://swiftspendlogistics.sharepoint.com/sites/ProjectManagement` |

### Task 11: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión) | `No answer needed` |

---

**Metodología:**

1. Analizar el artefacto de correo (remitente `mike.myers`, sujeto `server power`, enlace `hrcbishtek[.]com/a`).
2. Rastrear la descarga inicial (`pagefilerpqy.exe` 17:21) y el ejecutable malicioso `aKzjdD.exe` en Temp.
3. Identificar URLs de phishing/C2 (lohelper.com, kamehasuitens.info/track, dxsupport.net).
4. Identificar a la víctima (julianne.westcott@hotmail.com), el staging (`system_update.zip`) y el destino SharePoint de exfiltración.

**Learning chain:** mike.myers -> hrcbishtek[.]com/a -> pagefilerpqy.exe -> aKzjdD.exe -> lohelper login -> kamehasuitens track -> dxsupport.net -> julianne.westcott -> system_update.zip -> cdn.nautilusco a.ps1 -> SharePoint ProjectManagement

**Lección:** *Los artefactos de aplicaciones (correo, navegador, descargas, SharePoint) dejan la huella completa de una campaña de phishing: desde el email inicial hasta la exfiltración vía un sitio de SharePoint legítimo.*

**MITRE ATT&CK:** T1566 (Phishing) · T1105 (Ingress Tool Transfer) · T1071.001 (Web C2) · T1567 (Exfiltration Over Web Service) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Windows Applications Forensics](https://tryhackme.com/room/windowsapplications)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
