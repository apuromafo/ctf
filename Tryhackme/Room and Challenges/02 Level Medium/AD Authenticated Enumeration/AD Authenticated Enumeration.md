# AD: Authenticated Enumeration
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `adauthenticatedenumeration` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adauthenticatedenumeration) |
| **Sección** | Active Directory / Enumeration |
| **Fuente** | Writeup de thmrevenant (GitHub), nithiya-rajesh (GitHub) y happycamper84 (Medium) |
| **Componentes** | Active Directory, Kerberos (AS-REP Roasting), Rubeus, hashcat, net/whoami/wmic/sc, PowerShell ActiveDirectory, PowerView, BloodHound/SharpHound, SSH |
| **Impacto** | Explora la enumeración de Active Directory con una cuenta autenticada: AS-REP Roasting, enumeración manual con herramientas nativas (LOTL), módulo ActiveDirectory, PowerView y BloodHound para mapear el dominio. |
---
**Contexto:** Explora cómo enumerar Active Directory con una cuenta autenticada. La room cubre AS-REP Roasting, enumeración manual con comandos nativos (net, whoami, wmic, sc), el módulo ActiveDirectory de PowerShell, PowerView y BloodHound.
*EN: Explore how to enumerate Active Directory with an authenticated account. The room covers AS-REP Roasting, manual enumeration with native commands (net, whoami, wmic, sc), the ActiveDirectory PowerShell module, PowerView, and BloodHound.*
## Solucionario
### Task 1 — Introduction
**Explicación:** Presentación de la room y del entorno de enumeración autenticada en Active Directory.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2 — AS-REP Roasting
**Explicación:** Enumerar cuentas con pre-autenticación Kerberos deshabilitada (`UF_DONT_REQUIRE_PREAUTH`). Usar `GetNPUsers.py` (Impacket) para obtener los hashes AS-REP y crackearlos con `hashcat -m 18200` y rockyou. `Rubeus.exe asreproast` identifica automáticamente las cuentas vulnerables en Windows.
```
GetNPUsers.py tryhackme.loc/asrepuser1:'qwerty123!' -dc-ip <ip> -usersfile users.txt
hashcat -m 18200 asrep_hash.txt rockyou.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag must be set on an AD account for it to be vulnerable to AS-REP Roasting? | `UF_DONT_REQUIRE_PREAUTH` |
| 2 | Which tool automatically identifies roastable users without needing a username list? | `Rubeus` |
| 3 | What is the Hashcat mode used to crack AS-REP hashes? | `18200` |
| 4 | What is the password of the user asrepuser1? | `qwerty123!` |
### Task 3 — Manual Enumeration
**Explicación:** Con `ssh asrepuser1@10.211.12.20` (credenciales `qwerty123!`), usar comandos nativos: `whoami /all` (SID, grupos y privilegios), `net user /domain`, `net user <user> /domain`, `net group /domain`, `net localgroup`, `quser`, `wmic service get Name,StartName`, `sc query` y `reg query` para enumerar usuarios, grupos y servicios sin herramientas externas (living off the land).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many domain user accounts are there? | `31` |
| 2 | What is the full name of the user rduke? | `Raoul Duke` |
| 3 | How many local user accounts are there on the WRK machine? | `5` |
| 4 | How many domain groups are there? | `21` |
| 5 | What is the distinguishedName value of the asrepuser1 account? | `CN=ASREPUSER1,CN=USERS,DC=TRYHACKME,DC=LOC` |
### Task 4 — Enumeration using the ActiveDirectory PowerShell Module
**Explicación:** Usar `Get-ADUser`, `Get-ADGroup`, `Get-ADDomain`, `Get-ADGroup -Identity "Domain Admins" -Properties *` para enumerar usuarios, grupos y propiedades (SID, whenCreated, DistinguishedName).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to the "All Domain Admins" query, how many users are part of the Domain Admins group? | `4` |
| 2 | What is the type of relationship (edge) between the DRGONZ0 account and the DOMAIN ADMINS group? | `MemberOf` |
### Task 5 — Enumeration using PowerView
**Explicación:** Usar `Get-DomainGroup "*admin*"`, `Get-DomainComputer` para enumerar grupos y equipos del dominio.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many computer accounts were you able to find? | `2` |
| 2 | How many groups did Get-DomainGroup "*admin*" return? | `13` |
### Task 6 — Enumeration using BloodHound
**Explicación:** Ejecutar SharpHound (`SharpHound.exe --CollectionMethods All --Domain za.tryhackme.com --ExcludeDCs`), importar el zip en BloodHound y analizar las relaciones (edges) como `MemberOf` para mapear visualmente los caminos de ataque.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Análisis de las relaciones en BloodHound (sin preguntas adicionales). | `No answer needed` |
---
**Metodología:** AS-REP Roasting (GetNPUsers.py/Rubeus + hashcat -m 18200) → enumeración manual LOTL (net/whoami/wmic/sc/reg) → módulo ActiveDirectory de PowerShell → PowerView → BloodHound para visualizar edges y caminos de ataque.
**Learning chain:** cuenta autenticada → AS-REP Roasting (bajo ruido) → enumeración silenciosa con herramientas nativas → PowerShell/PowerView → gráfica de privilegios con BloodHound.
**MITRE ATT&CK:** T1558.004 (AS-REP Roasting), T1087.002 (Domain Account), T1069.002 (Permission Groups Discovery: Domain), T1482 (Domain Trust Discovery), T1201 (Password Policy Discovery).
**Fuente:** [TryHackMe - AD: Authenticated Enumeration](https://tryhackme.com/room/adauthenticatedenumeration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
