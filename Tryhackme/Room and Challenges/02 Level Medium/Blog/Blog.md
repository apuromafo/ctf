# Blog
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `blog` |
| **Link** | [TryHackMe](https://tryhackme.com/room/blog) |
| **Sección** | Web Exploitation / CMS Security |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | WordPress, USB exfiltration, web exploitation, CMS enumeration |
| **Impacto** | Enseña a enumerar y explotar un sitio WordPress, identificar dispositivos de almacenamiento conectados y extraer credenciales de la base de datos. |
---
**Contexto:** Blog es una sala de TryHackMe centrada en la explotación de un sitio web basado en WordPress. El participante debe enumerar el CMS, identificar artefactos de exfiltración de datos (dispositivo USB) y extraer las credenciales de la base de datos del sitio para obtener las flags.
*EN: Blog is a TryHackMe room focused on exploiting a WordPress-based website. The participant must enumerate the CMS, identify data exfiltration artifacts (USB device), and extract the database credentials to obtain the flags.*
## Solucionario
### Task 1 — WordPress Enumeration
**Explicación:** Se enumera el sitio WordPress para identificar el hash del administrador, el nombre del dispositivo de almacenamiento externo conectado (USB), la versión del CMS y las credenciales de la base de datos. Las respuestas se obtienen de la enumeración con herramientas como wpscan o inspección directa.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the admin password hash? | `9a0b2b618bef9bfa7ac28c1353d9f318` |
| 2 | What is the database password hash? | `c8421899aae571f7af486492b71a8ab7` |
| 3 | What is the mount point of the USB drive? | `/media/usb` |
| 4 | What CMS is the website running? | `Wordpress` |
| 5 | What version of the CMS is installed? | `5.0` |
### Task 2 — Exploitation
**Explicación:** Usando la información obtenida en la enumeración se completa la explotación del sitio WordPress. Tarea de cierre sin respuesta adicional requerida.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala. | `No answer needed` |
---
**Metodología:** Enumeración WordPress (wpscan, cms versioner) → identificación de hashes → descubrimiento de dispositivo USB montado → extracción de credenciales de BD → explotación del CMS.
**Learning chain:** WordPress expuesto → enumeración CMS → hashes de credenciales → USB exfiltration → flags.
**Lección:** *WordPress desactualizado y con credenciales débiles en la base de datos es un blanco habitual; la enumeración con wpscan revela versiones, plugins y usuarios en segundos.*
**MITRE ATT&CK:** T1592.002 (Gather Victim Host Information: Software), T1190 (Exploit Public-Facing Application), T1005 (Data from Local System), T1078 (Valid Accounts).
**Fuente:** [TryHackMe - Blog](https://tryhackme.com/room/blog)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
