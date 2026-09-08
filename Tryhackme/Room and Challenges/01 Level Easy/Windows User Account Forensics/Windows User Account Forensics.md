# Windows User Account Forensics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `windowsuseraccountforensics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsuseraccountforensics) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Simon Taplin (simontaplin.net) |
| **Componentes** | DSInternals / bootKey / SIDs / NTLM handshake / DsGetDomainControllerInfo / GPO / Windows Defender / C2 |
| **Impacto** | Forense de cuentas de usuario Windows: enumeración con DSInternals, análisis del handshake NTLM y revisión de políticas y scripts maliciosos |

---

**Contexto:** Aprende dónde buscar artefactos asociados con usuarios y cuentas. La room trata sobre las cuentas de usuario de Windows y sus artefactos en una investigación de seguridad: enumeración de cuentas (DSInternals), handshake de autenticación NTLM y políticas/scripts de arranque maliciosos.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of accounts are used by the Windows operating system and various apps? | `System and Service Accounts` |

**Explicación:** Windows usa (además de las cuentas de usuario humanas) cuentas **System and Service Accounts** para que el propio SO y las aplicaciones se ejecuten con identidades dedicadas. La room enseña dónde buscar artefactos asociados con usuarios y cuentas en una investigación de seguridad.

### Task 2: User Accounts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many users were found using the DSInternals command? | `5` |
| 2 | What is the value of the "bootKey" variable? | `36c8d26ec0df8b23ce63bcefa6e2d821` |
| 3 | What is the SID of the domain user, m.ascot? | `S-1-5-21-1966530601-3185510712-10604624-1111` |

**Explicación:** **DSInternals** es un módulo de PowerShell/CLI para interactuar con el AD y el SAM; en este caso se enumeran las cuentas del sistema → **5** usuarios. El comando devuelve también la variable **bootKey** (`36c8d26ec0df8b23ce63bcefa6e2d821`, la clave usada para cifrar los hashes en el registro) y los SIDs de cada usuario, como el del usuario de dominio `m.ascot` → `S-1-5-21-1966530601-3185510712-10604624-1111`.

### Task 3: Authentication

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user name used for the NTLM authentication? | `admin` |
| 2 | What was the Server Challenge sent to the client during the Challenge stage of the NTLM handshake? | `212ba239356b3d82` |
| 3 | What is the Dns Name of the other result from the DsGetDomainControllerInfo response? | `dcfr.lab.lan` |

**Explicación:** En el análisis del handshake **NTLM** (captura de tráfico/investigación de autenticación): el usuario autenticado es `admin`; el **Server Challenge** que el servidor envía al cliente en la fase Challenge es `212ba239356b3d82` (valor crucial para crackear/validar el hash NT). En la respuesta de **DsGetDomainControllerInfo**, el otro DC del dominio devuelve el Dns Name `dcfr.lab.lan`.

### Task 4: Policies

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the user specified as the apply target for this Policy? | `Michael Ascot` |
| 2 | Under Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender Antivirus > Real-time Protection, what is the setting that was enabled? | `Turn off real-time protection` |
| 3 | There is an updated malicious startup PowerShell script. What is the filename of this script? (Without file extension) | `superimportant-updated` |
| 4 | What is the IP address of the C2 server the script would exfiltrate to? | `192.0.2.123` |

**Explicación:** Revisando las **GPO** se encuentra una policy cuyo **apply target** es el usuario `Michael Ascot`. Bajo Computer Configuration > ... > Windows Defender Antivirus > Real-time Protection se habilitó el ajuste **Turn off real-time protection** (T1562.001 Impair Defenses: Disable or Modify Tools), que desactiva la protección en tiempo real de Defender. Existe además un script de arranque PowerShell malicioso actualizado llamado `superimportant-updated` (sin extensión) que exfiltraría información al C2 `192.0.2.123` (T1041 Exfiltration Over C2 Channel).

---

**Metodología:**
1. **User accounts:** usar **DSInternals** para enumerar los usuarios (5 encontrados) y extraer el `bootKey` (`36c8d26ec0df8b23ce63bcefa6e2d821`) y los SIDs; el SID del usuario de dominio `m.ascot` es `S-1-5-21-1966530601-3185510712-10604624-1111`. Este paso responde también al tipo de cuentas usado por el SO y las apps: **System and Service Accounts**.
2. **Authentication:** analizar el handshake **NTLM**: usuario `admin`, **Server Challenge** `212ba239356b3d82`; en las respuestas DsGetDomainControllerInfo, el otro DC devuelve el Dns Name `dcfr.lab.lan`.
3. **Policies:** revisar las **GPO**: el objetivo de la policy es `Michael Ascot`; en Real-time Protection de Windows Defender Antivirus se habilitó el ajuste **Turn off real-time protection**; existe un script de arranque PowerShell malicioso actualizado llamado `superimportant-updated` (sin extensión) que exfiltraría al C2 `192.0.2.123`.

**Learning chain:** cuentas de usuario Windows (System and Service Accounts) → DSInternals (5 users, bootKey 36c8d26e..., SID m.ascot) → NTLM handshake (admin, Server Challenge 212ba239356b3d82, dcfr.lab.lan) → GPO (Michael Ascot, Turn off real-time protection) → script startup (superimportant-updated → C2 192.0.2.123)

**MITRE ATT&CK:** T1562.001 (Impair Defenses: Disable or Modify Tools), T1070 (Indicator Removal), T1003.002 (OS Credential Dumping: Security Account Manager), T1059.001 (Command and Scripting Interpreter: PowerShell), T1041 (Exfiltration Over C2 Channel)

**Fuente:** [TryHackMe - Windows User Account Forensics](https://tryhackme.com/room/windowsuseraccountforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
