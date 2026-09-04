# AD: Authenticated Enumeration [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `adauthenticatedenumeration`
* **Link:** https://tryhackme.com/room/adauthenticatedenumeration
* **Sección / Section:** Active Directory / Enumeration
* **Fuente / Source:** Writeup de thmrevenant (GitHub), nithiya-rajesh (GitHub) y happycamper84 (Medium)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Explora cómo enumerar Active Directory con una cuenta autenticada. La room cubre AS-REP Roasting, enumeración manual con comandos nativos (net, whoami, wmic, sc), el módulo ActiveDirectory de PowerShell, PowerView y BloodHound.
> **EN:** Explore how to enumerate Active Directory with an authenticated account. The room covers AS-REP Roasting, manual enumeration with native commands (net, whoami, wmic, sc), the ActiveDirectory PowerShell module, PowerView, and BloodHound.

---

### Task 1 — Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| *(No hay preguntas / No questions)* | — |

---

### Task 2 — AS-REP Roasting

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag must be set on an AD account for it to be vulnerable to AS-REP Roasting? | `UF_DONT_REQUIRE_PREAUTH` |
| Which tool automatically identifies roastable users without needing a username list? | `Rubeus` |
| What is the Hashcat mode used to crack AS-REP hashes? | `18200` |
| What is the password of the user asrepuser1? | `qwerty123!` |

---

### Task 3 — Manual Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many domain user accounts are there? | `31` |
| What is the full name of the user rduke? | `Raoul Duke` |
| How many local user accounts are there on the WRK machine? | `5` |
| How many domain groups are there? | `21` |
| What is the distinguishedName value of the asrepuser1 account? | `CN=ASREPUSER1,CN=USERS,DC=TRYHACKME,DC=LOC` |

---

### Task 4 — Enumeration using the ActiveDirectory PowerShell Module

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| According to the "All Domain Admins" query, how many users are part of the Domain Admins group? | `4` |
| What is the type of relationship (edge) between the DRGONZ0 account and the DOMAIN ADMINS group? | `MemberOf` |

---

### Task 5 — Enumeration using PowerView

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many computer accounts were you able to find? | `2` |
| How many groups did Get-DomainGroup "*admin*" return? | `13` |

---

### Task 6 — Enumeration using BloodHound

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| *(No hay preguntas / No questions)* | — |

---

## Metodología / Methodology

1. **AS-REP Roasting:** enumerar cuentas con pre-autenticación Kerberos deshabilitada (`UF_DONT_REQUIRE_PREAUTH`). Usar `GetNPUsers.py` (Impacket) con un `users.txt` para obtener los hashes AS-REP, y crackearlos con `hashcat -m 18200` y rockyou. Rubeus (`Rubeus.exe asreproast`) identifica automáticamente las cuentas vulnerables en Windows.
2. **Enumeración manual (LOTL):** con `ssh asrepuser1@10.211.12.20` (credenciales `qwerty123!`), usar comandos nativos:
   - `whoami /all` — SID, grupos y privilegios (SeImpersonatePrivilege, SeBackupPrivilege, etc.)
   - `net user /domain` — listar usuarios del dominio; `net user <user> /domain` — detalles de cuenta
   - `net group /domain` — listar grupos; `net localgroup` — grupos locales
   - `quser` — usuarios con sesión activa; `wmic service get Name,StartName` / `sc query` — cuentas de servicio
   - `reg query` — credenciales de auto-logon, aplicaciones instaladas
3. **Módulo ActiveDirectory de PowerShell:** usar `Get-ADUser`, `Get-ADGroup`, `Get-ADDomain` para enumerar usuarios, grupos y propiedades (SID, whenCreated, DistinguishedName).
4. **PowerView:** usar `Get-DomainGroup "*admin*"`, `Get-DomainComputer` para enumerar grupos y equipos.
5. **BloodHound:** ejecutar SharpHound (`SharpHound.exe --CollectionMethods All --Domain za.tryhackme.com --ExcludeDCs`), importar el zip en BloodHound y analizar las relaciones (edges) como `MemberOf`.

**Lección:** una cuenta autenticada en AD permite una enumeración extensa y silenciosa. AS-REP Roasting es un ataque de bajo ruido que no requiere autenticación previa; la enumeración manual con herramientas nativas (living off the land) evita detección, y BloodHound mapea visualmente los caminos de ataque.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
