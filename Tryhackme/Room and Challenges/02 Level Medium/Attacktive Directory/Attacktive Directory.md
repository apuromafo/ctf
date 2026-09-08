# Attacktive Directory
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `attacktivedirectory` |
| **Link** | [TryHackMe](https://tryhackme.com/room/attacktivedirectory) |
| **Sección** | Windows / Active Directory |
| **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Active Directory, SMB (enum4linux, smbclient), Kerberos (Kerbrute userenum, AS-REP Roasting), hashcat 18200, NTDS.DIT (DRSUAPI/secretsdump), Pass The Hash, Evil-WinRM (-H) |
| **Impacto** | Sala de CTF centrada en Active Directory que cubre la enumeración de puertos SMB, Kerberos (AS-REP Roasting), extracción de credenciales y dumping de NTDS.DIT hasta lograr dominio completo. |
---
**Contexto:** Sala de CTF centrada en Active Directory que cubre la enumeración de puertos SMB, Kerberos (AS-REP Roasting), extracción de credenciales y dumping de NTDS.DIT.
*EN: Active Directory-focused CTF room covering SMB port enumeration, Kerberos (AS-REP Roasting), credential extraction, and NTDS.DIT dumping.*
## Solucionario
### Task 1 — Enumeración / Enumeration
**Explicación:** Enumerar el dominio con `enum4linux` (editor de /etc/krb5.conf/setup) para los puertos SMB 139/445, obtener el NetBIOS-Domain Name **THM-AD** y añadir el dominio al `/etc/hosts` (dominio `spookysec.local`, DC `ATTACKTIVEDIRECTORY`). TLD inválido comúnmente usado: `.local`.
*EN: Enumerate the domain with `enum4linux` for SMB ports 139/445, get the NetBIOS-Domain Name **THM-AD** and add the domain to `/etc/hosts` (`spookysec.local`, DC `ATTACKTIVEDIRECTORY`). Common invalid TLD: `.local`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tool will allow us to enumerate port 139/445? | `enum4linux` |
| 2 | What is the NetBIOS-Domain Name of the machine? | `THM-AD` |
| 3 | What invalid TLD do people commonly use for their Active Directory Domain? | `.local` |
### Task 2 — Kerbrute: Enumeración de Usuarios / Kerbrute: User Enumeration
**Explicación:** Con **Kerbrute** (`./kerbrute userenum --dc <ip> -d spookysec.local userlist.txt`) se enumeran usuarios válidos del dominio. Cuentas destacadas descubiertas: `svc-admin` y `backup`.
*EN: Using **Kerbrute** (`./kerbrute userenum --dc <ip> -d spookysec.local userlist.txt`) valid domain users are enumerated. Notable accounts: `svc-admin` and `backup`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command within Kerbrute will allow us to enumerate valid usernames? | `userenum` |
| 2 | What notable account is discovered? (These should jump out at you) | `svc-admin` |
| 3 | What is the other notable account is discovered? (These should jump out at you) | `backup` |
### Task 3 — AS-REP Roasting
**Explicación:** Con `GetNPUsers.py spookysec.local/ -usersfile userlist.txt -dc-ip <ip>` se consulta un ticket AS-REP sin contraseña de `svc-admin` (hash **Kerberos 5 AS-REP etype 23**, modo hashcat **18200**). Se crackea con la wordlist modificada (`passwordlist.txt`): contraseña `management2005`.
*EN: With `GetNPUsers.py spookysec.local/ -usersfile userlist.txt -dc-ip <ip>` an AS-REP ticket is requested without password for `svc-admin` (hash **Kerberos 5 AS-REP etype 23**, hashcat mode **18200**). It is cracked with the modified wordlist: password `management2005`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | We have two user accounts that we could potentially query a ticket from. Which user account can you query a ticket from with no password? | `svc-admin` |
| 2 | Looking at the Hashcat Examples Wiki page, what type of Kerberos hash did we retrieve from the KDC? (Specify the full name) | `Kerberos 5 AS-REP etype 23` |
| 3 | What mode is the hash? | `18200` |
| 4 | Now crack the hash with the modified password list provided, what is the user accounts password? | `management2005` |
### Task 4 — Enumeración SMB y Share de Backup / SMB Enumeration and Backup Share
**Explicación:** Con `smbclient` (`-L` listar shares) se mapean los shares remotos: **6 shares**. Con el usuario `svc-admin:management2005` se accede al share **backup**, que contiene un texto base64: `YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw`, que decodifica a `backup@spookysec.local:backup2517860`.
*EN: Using `smbclient -L` the remote shares are listed: **6 shares**. Authenticating as `svc-admin:management2005` gives access to the **backup** share, holding the base64 string `YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw`, which decodes to `backup@spookysec.local:backup2517860`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What utility can we use to map remote SMB shares? | `smbclient` |
| 2 | Which option will list shares? | `-L` |
| 3 | How many remote shares is the server listing? | `6` |
| 4 | There is one particular share that we have access to that contains a text file. Which share is it? | `backup` |
| 5 | What is the content of the file? | `YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw` |
| 6 | Decoding the contents of the file, what is the full contents? | `backup@spookysec.local:backup2517860` |
### Task 5 — Dump de NTDS.DIT / NTDS.DIT Dump
**Explicación:** Dump de NTDS.DIT mediante **DRSUAPI** (`secretsdump.py`) con las credenciales de backup: se obtiene el hash NTLM del Administrador `0e0363213e37b94221497260b0bcb4fc`. Con **Pass The Hash** se puede autenticar sin contraseña; usando **Evil-WinRM** la opción que permite el hash es `-H`.
*EN: NTDS.DIT is dumped via **DRSUAPI** (`secretsdump.py`) with the backup credentials: the Administrator NTLM hash `0e0363213e37b94221497260b0bcb4fc` is retrieved. **Pass The Hash** allows authenticating without the password; with **Evil-WinRM** the hash option is `-H`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What method allowed us to dump NTDS.DIT? | `DRSUAPI` |
| 2 | What is the Administrators NTLM hash? | `0e0363213e37b94221497260b0bcb4fc` |
| 3 | What method of attack could allow us to authenticate as the user without the password? | `Pass The Hash` |
| 4 | Using a tool called Evil-WinRM what option will allow us to use a hash? | `-H` |
### Task 6 — Flags
**Explicación:** Acceso al sistema con Evil-WinRM vía Pass The Hash (administrator) y recogida de las flags de cada usuario (`svc-admin`, `backup`, `Administrator`).
*EN: Access the system with Evil-WinRM via Pass The Hash (administrator) and collect each user's flag (`svc-admin`, `backup`, `Administrator`).*

```
enum4linux → Kerbrute userenum → AS-REP Roasting → Hashcat 18200 → smbclient -L → Share backup → Base64 decode → DRSUAPI NTDS.DIT → NTLM hashes → Pass The Hash → Evil-WinRM -H → Flags
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | svc-admin | `TryHackMe{K3rb3r0s_Pr3_4uth}` |
| 2 | backup | `TryHackMe{B4ckM3UpSc0tty!}` |
| 3 | Administrator | `TryHackMe{4ctiveD1rectoryM4st3r}` |
---
**Metodología:** enum4linux → Kerbrute userenum → AS-REP Roasting (hashcat 18200) → smbclient -L → share backup (base64) → DRSUAPI NTDS.DIT → Pass The Hash → Evil-WinRM -H → flags.
**Learning chain:** enumeración AD → robo de tickets Kerberos → cracking → shares SMB → dump NTDS.DIT → Pass The Hash → compromiso del dominio.
**MITRE ATT&CK:** T1558.004 (AS-REP Roasting), T1110 (Brute Force)/kerbrute, T1049 (Network Share Discovery)/smbclient, T1003.003 (NTDS), T1550.002 (Pass-the-Hash), T1021.006 (WinRM).
**Fuente:** [TryHackMe - Attacktive Directory](https://tryhackme.com/room/attacktivedirectory)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
