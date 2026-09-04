# Windows User Account Forensics [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `windowsuseraccountforensics`
* **Link:** https://tryhackme.com/room/windowsuseraccountforensics
* **Sección / Section:** DFIR / Windows / Advanced Endpoint Investigations
* **Fuente / Source:** Writeup de Simon Taplin (simontaplin.net)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Aprende dónde buscar artefactos asociados con usuarios y cuentas. La room trata sobre las cuentas de usuario de Windows y sus artefactos en una investigación de seguridad.
> **EN:** Learn where to search for artefacts associated with users and accounts. The room deals with Windows user accounts and their artefacts in a security investigation.

---

### Task 1 — Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of accounts are used by the Windows operating system and various apps? | `System and Service Accounts` |

---

### Task 2 — User Accounts

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many users were found using the DSInternals command? | `5` |
| What is the value of the "bootKey" variable? | `36c8d26ec0df8b23ce63bcefa6e2d821` |
| What is the SID of the domain user, m.ascot? | `S-1-5-21-1966530601-3185510712-10604624-1111` |

---

### Task 3 — Authentication

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user name used for the NTLM authentication? | `admin` |
| What was the Server Challenge sent to the client during the Challenge stage of the NTLM handshake? | `212ba239356b3d82` |
| What is the Dns Name of the other result from the DsGetDomainControllerInfo response? | `dcfr.lab.lan` |

---

### Task 4 — Policies

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the user specified as the apply target for this Policy? | `Michael Ascot` |
| Under Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender Antivirus > Real-time Protection, what is the setting that was enabled? | `Turn off real-time protection` |
| There is an updated malicious startup PowerShell script. What is the filename of this script? (Without file extension) | `superimportant-updated` |
| What is the IP address of the C2 server the script would exfiltrate to? | `192.0.2.123` |

---

## Metodología / Methodology

1. **User accounts:** usar DSInternals para enumerar usuarios y extraer el bootKey y SIDs.
2. **Authentication:** analizar el handshake NTLM (Server Challenge) y respuestas DsGetDomainControllerInfo.
3. **Policies:** revisar GPOs para detectar configuraciones maliciosas (desactivar protección en tiempo real de Defender) y scripts de inicio maliciosos.

**Lección:** las cuentas de usuario de Windows y sus artefactos (autenticación, políticas, scripts) son clave en una investigación de seguridad.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
