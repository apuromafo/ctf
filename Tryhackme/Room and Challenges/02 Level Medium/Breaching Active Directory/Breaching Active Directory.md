# Breaching Active Directory

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Free) | **Slug** | `breachingad` |
| **Link** | [TryHackMe](https://tryhackme.com/room/breachingad) | **Sección** | 02 Level Medium | **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Password Spraying / LDAP Pass-back / Authentication Capture / PXE Boot Attack / Credentials in Configuration Files | **Impacto** | Enseña múltiples vectores para vulnerar Active Directory aprovechando credenciales débiles, configuraciones inseguras y credenciales almacenadas |

---

**Contexto:** Sala que cubre diferentes métodos para vulnerar Active Directory: password spraying, ataques LDAP pass-back, envenenamiento/captura de autenticaciones y robo de credenciales de configuraciones. Room covering different methods to breach Active Directory: password spraying, LDAP pass-back attacks, poisoning/capturing authentication, and credential theft from configurations.

## Solucionario

### Task 1: Password Spraying

**Explicación:** Se inicia un ataque de password spraying contra el portal web del cliente para obtener pares de credenciales válidas. Se usa HaveIBeenPwned para verificar si credenciales han sido expuestas en brechas. El mecanismo de autenticación challenge-response que usa NTLM se llama NetNtlm. El script de password spraying encontró múltiples pares válidos; el tercero es `gordon.stevens`. Al autenticarse con un par válido, la aplicación muestra "Hello World".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What popular website can be used to verify if your email address or password has ever been exposed in a publicly disclosed data breach? | `HaveIBeenPwned` |
| 2 | What is the name of the challenge-response authentication mechanism that uses NTLM? | `NetNtlm` |
| 3 | What is the username of the third valid credential pair found by the password spraying script? | `gordon.stevens` |
| 4 | How many valid credentials pairs were found by the password spraying script? | `4` |
| 5 | What is the message displayed by the web application when authenticating with a valid credential pair? | `Hello World` |

### Task 2: LDAP Pass-back Attack

**Explicación:** Se configura un servidor LDAP rogue para realizar un ataque LDAP Pass-back. Este tipo de ataque permite degradar la autenticación a texto plano. En el servidor rogue se habilitan los mecanismos `LOGIN,PLAIN` para capturar las credenciales en claro. La cuenta `svcLDAP` tiene la contraseña `tryhackmeldappass1@`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of attack can be performed against LDAP Authentication systems not commonly found against Windows Authentication systems? | `LDAP Pass-back Attack` |
| 2 | What two authentication mechanisms do we allow on our rogue LDAP server to downgrade the authentication and make it clear text? | `LOGIN,PLAIN` |
| 3 | What is the password associated with the svcLDAP account? | `tryhackmeldappass1@` |

### Task 3: Authentication Capture

**Explicación:** Se usa Responder para envenenar y capturar solicitudes de autenticación en la red. El desafío capturado pertenece al usuario `svcFileCopy`. Mediante cracking se obtiene la contraseña `FPassword1!`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the tool we can use to poison and capture authentication requests on the network? | `Responder` |
| 2 | What is the username associated with the challenge that was captured? | `svcFileCopy` |
| 3 | What is the value of the cracked password associated with the challenge that was captured? | `FPassword1!` |

### Task 4: PXE Boot Attack

**Explicación:** El ataque PXE Boot explota el servidor MDT (Microsoft Deployment Toolkit) que aloja imágenes de arranque de red. Se descarga la imagen de PXE Boot mediante TFTP y se extraen las credenciales almacenadas. La cuenta encontrada es `svcMDT` con contraseña `PXEBootSecure1@`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Microsoft tool is used to create and host PXE Boot images in organisations? | `Microsoft Deployment Toolkit` |
| 2 | What network protocol is used for recovery of files from the MDT server? | `TFTP` |
| 3 | What is the username associated with the account that was stored in the PXE Boot image? | `svcMDT` |
| 4 | What is the password associated with the account that was stored in the PXE Boot image? | `PXEBootSecure1@` |

### Task 5: Credentials in Configuration Files

**Explicación:** Los archivos de configuración a menudo contienen credenciales almacenadas. La base de datos `ma.db` de McAfee almacena configuración incluyendo credenciales usadas para conectarse al orquestador. La tabla `AGENT_REPOSITORIES` contiene las credenciales del orquestador. La cuenta de AD asociada al servicio McAfee es `svcAV` con contraseña `MyStrongPassword!`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of files often contain stored credentials on hosts? | `Configuration Files` |
| 2 | What is the name of the McAfee database that stores configuration including credentials used to connect to the orchestrator? | `ma.db` |
| 3 | What table in this database stores the credentials of the orchestrator? | `AGENT_REPOSITORIES` |
| 4 | What is the username of the AD account associated with the McAfee service? | `svcAV` |
| 5 | What is the password of the AD account associated with the McAfee service? | `MyStrongPassword!` |

---

**Metodología:**
1. Realizar password spraying contra el VPN/portal web del cliente para obtener pares de credenciales válidas.
2. Configurar un servidor LDAP rogue (LDAP Pass-back) para degradar la autenticación a texto plano y capturar las credenciales del servicio.
3. Usar Responder para envenenar y capturar solicitudes de autenticación y luego crackear los desafíos capturados.
4. Atacar el servidor PXE Boot (MDT) descargando la imagen por TFTP y extrayendo las credenciales de la cuenta utilizada en la instalación.
5. Buscar archivos de configuración con credenciales almacenadas, como la base de datos ma.db de McAfee, para recuperar credenciales del servicio.

**Learning chain:** Password Spraying → Credenciales válidas → LDAP Pass-back → Credenciales svcLDAP → Responder poisoning → Hash NetNTLM → Crackear → PXE Boot MDT → TFTP → Credenciales svcMDT → Config Files → ma.db → Credenciales svcAV

**Lección:** *Existen múltiples vectores para vulnerar Active Directory aprovechando credenciales débiles, configuraciones inseguras (LDAP, PXE) y credenciales almacenadas en archivos de configuración.*

**MITRE ATT&CK:** T1110.003 (Password Spraying), T1557 (Adversary-in-the-Middle / NTLM Relay), T1552.001 (Credentials In Files), T1187 (Forced Authentication / PXE), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Breaching Active Directory](https://tryhackme.com/room/breachingad)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
