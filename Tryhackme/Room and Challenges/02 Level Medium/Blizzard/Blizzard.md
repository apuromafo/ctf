# Blizzard
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `blizzard` |
| **Link** | [TryHackMe](https://tryhackme.com/room/blizzard) |
| **Sección** | Digital Forensics / Incident Response |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Windows forensics, event log analysis, artifact timeline, credential extraction |
| **Impacto** | Enseña análisis forense de artefactos Windows: registro de eventos, líneas de tiempo de compromiso y extracción de credenciales para reconstruir un incidente de seguridad. |
---
**Contexto:** Blizzard es una sala de TryHackMe de forensics digital enfocada en analizar artefactos de un sistema Windows comprometido. El participante debe reconstruir la línea de tiempo del atacante extrayendo timestamps, credenciales y URLs de los eventos del sistema, incluyendo uso de herramientas como rclone para exfiltración.
*EN: Blizzard is a TryHackMe digital forensics room focused on analyzing artifacts from a compromised Windows system. The participant must reconstruct the attacker timeline by extracting timestamps, credentials, and URLs from system events, including use of tools like rclone for exfiltration.*
## Solucionario
### Task 1 — Initial Access
**Explicación:** Se analizan los primeros artefactos de compromiso: timestamps de acceso inicial, ruta del binario utilizado por el atacante (rclone), correo electrónico de registro y contraseña del servicio utilizado para la exfiltración. Los timestamps indican la secuencia cronológica del ataque.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When was the initial access performed? | `03/24/2024 19:38:48` |
| 2 | What is the full path of the binary used? | `C:\Users\dbadmin\.rclone\rclone-v1.66.0-windows-amd64\rclone.exe` |
| 3 | What is the email address used to register on the C2 service? | `annajones291@hotmail.com` |
| 4 | What is the password used to register? | `SecureUpdate` |
| 5 | When was the data exfiltration performed? | `03/24/2024 20:04:05` |
### Task 2 — Lateral Movement
**Explicación:** Se investigan eventos de movimiento lateral: timestamps de autenticación, dominio del atacante y credenciales utilizadas para pivotar entre sistemas. Los eventos revelan la progresión del atacante en la red.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When was the first authentication event? | `03/24/2024 19:06:27` |
| 2 | When was the second authentication event? | `03/24/2024 19:07:46` |
| 3 | When was the third authentication event? | `03/24/2024 19:16:23` |
| 4 | What is the domain used by the attacker? | `advancedsolutions[.]net` |
| 5 | What are the credentials used for lateral movement? | `db@dm1nS3cur3Pass!` |
### Task 3 — Phishing & Credential Harvesting
**Explicación:** Se analiza el vector de ataque inicial: un correo de phishing que simulaba ser Microsoft Identity Provider. Se reconstruye la URL de phishing, el mensaje mostrado al usuario y el timestamp de la interacción del usuario con el enlace malicioso.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When was the phishing email received? | `03/24/2024 18:36:34` |
| 2 | What was the sender display name? | `Microsoft Identity Provider` |
| 3 | What is the phishing URL? | `hxxps[://]login[.]sourcesecured[.]com/support/id/XkSkj321` |
| 4 | What was the button text on the phishing page? | `Sign in to your account` |
| 5 | When did the user click the phishing link? | `03/24/2024 18:38:29` |
---
**Metodología:** Análisis de Windows Event Logs → reconstrucción de timeline (phishing → credenciales → rclone → exfiltración) → extracción de URLs y credenciales → correlación de timestamps → documentación del incidente.
**Learning chain:** phishing (email + URL) → credenciales capturadas → movimiento lateral → herramienta de exfiltración (rclone) → timeline completa.
**Lección:** *Los timestamps de eventos Windows son la columna vertebral de toda investigación forense: cruzar autenticaciones, creaciones de procesos y conexiones de red permite reconstruir la cadena de ataque completa.*
**MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Link), T1078 (Valid Accounts), T1021.002 (SMB/Windows Admin Shares), T1567.002 (Exfiltration Over Web Service), T1059.001 (PowerShell).
**Fuente:** [TryHackMe - Blizzard](https://tryhackme.com/room/blizzard)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
