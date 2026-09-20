# Block
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `block` |
| **Link** | [TryHackMe](https://tryhackme.com/room/block) |
| **Sección** | Cryptography / Forensics |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | SMB, file decryption, credential extraction, NTLM hash, privilege escalation |
| **Impacto** | Enseña a descifrar archivos cifrados, extraer credenciales de sistemas Windows y escalar privilegios mediante SMB y análisis forense. |
---
**Contexto:** Block es una sala de TryHackMe que simula un incidente de ransomware parcial donde archivos han sido cifrados y se deben recuperar. El participante debe descifrar archivos SMB, extraer credenciales de usuario y escalar privilegios hasta obtener root en el sistema.
*EN: Block is a TryHackMe room simulating a partial ransomware incident where files have been encrypted and must be recovered. The participant must decrypt SMB files, extract user credentials, and escalate privileges to root on the system.*
## Solucionario
### Task 1 — File Decryption
**Explicación:** Se identifica y extrae un archivo cifrado desde el sistema. Se analiza el mecanismo de cifrado utilizado y se descifra para obtener las credenciales del usuario y la primera flag.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the username? | `mrealman` |
| 2 | What is the password? | `Blockbuster1` |
| 3 | What is the flag? | `THM{SmB_DeCrypTing_who_Could_Have_Th0ughT}` |
### Task 2 — Credential Extraction
**Explicación:** Usando las credenciales obtenidas se accede al sistema y se extrae un hash NTLM y la flag de escalada de privilegios. El hash corresponde al usuario sin contraseña configurada.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the service account? | `eshellstrop` |
| 2 | What is the NTLM hash of the service account? | `3f29138a04aadc19214e9c04028bf381` |
| 3 | What is the privilege escalation flag? | `THM{No_PasSw0Rd?_No_Pr0bl3m}` |
---
**Metodología:** Enumeración SMB → identificación de archivos cifrados → análisis del cifrado → descifrado → extracción de credenciales → obtención de hash NTLM → escalada de privilegios.
**Learning chain:** SMB compartido → archivos cifrados → descifrado → credenciales → hash NTLM → escalada → flags.
**Lección:** *Los servidores SMB mal configurados exponen tanto archivos cifrados como credenciales en claro; un atacante que descifra un archivo puede obtener acceso root sin exploit.*
**MITRE ATT&CK:** T1021.002 (SMB/Windows Admin Shares), T1003.002 (SAM), T1558.003 (Kerberoasting), T1078 (Valid Accounts).
**Fuente:** [TryHackMe - Block](https://tryhackme.com/room/block)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
