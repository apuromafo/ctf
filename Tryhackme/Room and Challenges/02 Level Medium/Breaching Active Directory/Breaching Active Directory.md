# Breaching Active Directory [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `breachingad`
* **Link:** https://tryhackme.com/room/breachingad
* **Sección / Section:** Windows / Active Directory
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala que cubre diferentes métodos para vulnerar Active Directory: password spraying, ataques LDAP pass-back, envenenamiento/captura de autenticaciones y robo de credenciales de configuraciones.
> **EN:** Room covering different methods to breach Active Directory: password spraying, LDAP pass-back attacks, poisoning/capturing authentication, and credential theft from configurations.

---

### Task 1 — Password Spraying

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What popular website can be used to verify if your email address or password has ever been exposed in a publicly disclosed data breach? | `HaveIBeenPwned` |
| What is the name of the challenge-response authentication mechanism that uses NTLM? | `NetNtlm` |
| What is the username of the third valid credential pair found by the password spraying script? | `gordon.stevens` |
| How many valid credentials pairs were found by the password spraying script? | `4` |
| What is the message displayed by the web application when authenticating with a valid credential pair? | `Hello World` |

---

### Task 2 — Ataque LDAP Pass-back / LDAP Pass-back Attack

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of attack can be performed against LDAP Authentication systems not commonly found against Windows Authentication systems? | `LDAP Pass-back Attack` |
| What two authentication mechanisms do we allow on our rogue LDAP server to downgrade the authentication and make it clear text? | `LOGIN,PLAIN` |
| What is the password associated with the svcLDAP account? | `tryhackmeldappass1@` |

---

### Task 3 — Captura de Autenticación / Authentication Capture

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the tool we can use to poison and capture authentication requests on the network? | `Responder` |
| What is the username associated with the challenge that was captured? | `svcFileCopy` |
| What is the value of the cracked password associated with the challenge that was captured? | `FPassword1!` |

---

### Task 4 — Ataque PXE Boot / PXE Boot Attack

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What Microsoft tool is used to create and host PXE Boot images in organisations? | `Microsoft Deployment Toolkit` |
| What network protocol is used for recovery of files from the MDT server? | `TFTP` |
| What is the username associated with the account that was stored in the PXE Boot image? | `svcMDT` |
| What is the password associated with the account that was stored in the PXE Boot image? | `PXEBootSecure1@` |

---

### Task 5 — Credenciales en Configuraciones / Credentials in Configuration Files

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of files often contain stored credentials on hosts? | `Configuration Files` |
| What is the name of the McAfee database that stores configuration including credentials used to connect to the orchestrator? | `ma.db` |
| What table in this database stores the credentials of the orchestrator? | `AGENT_REPOSITORIES` |
| What is the username of the AD account associated with the McAfee service? | `svcAV` |
| What is the password of the AD account associated with the McAfee service? | `MyStrongPassword!` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Realizar password spraying contra el VPN/portal web del cliente para obtener pares de credenciales válidas.
2. **Paso 2 / Step 2:** Configurar un servidor LDAP rogue (LDAP Pass-back) para degradar la autenticación a texto claro y capturar las credenciales del servicio.
3. **Paso 3 / Step 3:** Usar Responder para envenenar y capturar solicitudes de autenticación y luego crackear los desafíos capturados.
4. **Paso 4 / Step 4:** Atacar el servidor PXE Boot (MDT) descargando la imagen por TFTP y extrayendo las credenciales de la cuenta utilizada en la instalación.
5. **Paso 5 / Step 5:** Buscar archivos de configuración con credenciales almacenadas, como la base de datos ma.db de McAfee, para recuperar credenciales del servicio.

### Cadena de ataque / Attack Chain

```
Password Spraying → Credenciales válidas → LDAP Pass-back → Credenciales svcLDAP → Responder poisoning → Hash NetNTLM → Crackear → PXE Boot MDT → TFTP → Credenciales svcMDT → Config Files → ma.db → Credenciales svcAV
```

**Lección:** Existen múltiples vectores para vulnerar Active Directory aprovechando credenciales débiles, configuraciones inseguras (LDAP, PXE) y credenciales almacenadas en archivos de configuración.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.