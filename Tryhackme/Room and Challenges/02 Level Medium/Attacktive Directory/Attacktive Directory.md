# Attacktive Directory [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `attacktivedirectory`
* **Link:** https://tryhackme.com/room/attacktivedirectory
* **Sección / Section:** Windows / Active Directory
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de CTF centrada en Active Directory que cubre la enumeración de puertos SMB, Kerberos (AS-REP Roasting), extracción de credenciales y dumping de NTDS.DIT.
> **EN:** Active Directory-focused CTF room covering SMB port enumeration, Kerberos (AS-REP Roasting), credential extraction, and NTDS.DIT dumping.

---

### Task 1 — Enumeración / Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What tool will allow us to enumerate port 139/445? | `enum4linux` |
| What is the NetBIOS-Domain Name of the machine? | `THM-AD` |
| What invalid TLD do people commonly use for their Active Directory Domain? | `.local` |

---

### Task 2 — Kerbrute: Enumeración de Usuarios / Kerbrute: User Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What command within Kerbrute will allow us to enumerate valid usernames? | `userenum` |
| What notable account is discovered? (These should jump out at you) | `svc-admin` |
| What is the other notable account is discovered? (These should jump out at you) | `backup` |

---

### Task 3 — AS-REP Roasting

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| We have two user accounts that we could potentially query a ticket from. Which user account can you query a ticket from with no password? | `svc-admin` |
| Looking at the Hashcat Examples Wiki page, what type of Kerberos hash did we retrieve from the KDC? (Specify the full name) | `Kerberos 5 AS-REP etype 23` |
| What mode is the hash? | `18200` |
| Now crack the hash with the modified password list provided, what is the user accounts password? | `management2005` |

---

### Task 4 — Enumeración SMB y Share de Backup / SMB Enumeration and Backup Share

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What utility can we use to map remote SMB shares? | `smbclient` |
| Which option will list shares? | `-L` |
| How many remote shares is the server listing? | `6` |
| There is one particular share that we have access to that contains a text file. Which share is it? | `backup` |
| What is the content of the file? | `YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw` |
| Decoding the contents of the file, what is the full contents? | `backup@spookysec.local:backup2517860` |

---

### Task 5 — Dump de NTDS.DIT / NTDS.DIT Dump

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What method allowed us to dump NTDS.DIT? | `DRSUAPI` |
| What is the Administrators NTLM hash? | `0e0363213e37b94221497260b0bcb4fc` |
| What method of attack could allow us to authenticate as the user without the password? | `Pass The Hash` |
| Using a tool called Evil-WinRM what option will allow us to use a hash? | `-H` |

---

### Task 6 — Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| svc-admin | `TryHackMe{K3rb3r0s_Pr3_4uth}` |
| backup | `TryHackMe{B4ckM3UpSc0tty!}` |
| Administrator | `TryHackMe{4ctiveD1rectoryM4st3r}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Enumerar el dominio con enum4linux para obtener información de puertos 139/445 y el nombre NetBIOS del dominio.
2. **Paso 2 / Step 2:** Usar Kerbrute con el comando userenum para descubrir usuarios válidos del dominio (svc-admin y backup).
3. **Paso 3 / Step 3:** Obtener y crackear el ticket Kerberos AS-REP del usuario svc-admin (modo hashcat 18200).
4. **Paso 4 / Step 4:** Enumerar shares SMB con smbclient -L y acceder al share backup para descifrar las credenciales en base64.
5. **Paso 5 / Step 5:** Dump NTDS.DIT mediante DRSUAPI y obtener los hashes NTLM de los usuarios.
6. **Paso 6 / Step 6:** Acceder al sistema mediante Pass The Hash con Evil-WinRM (-H) para recoger las flags.

### Cadena de ataque / Attack Chain

```
enum4linux → Kerbrute userenum → AS-REP Roasting → Hashcat 18200 → smbclient -L → Share backup → Base64 decode → DRSUAPI NTDS.DIT → NTLM hashes → Pass The Hash → Evil-WinRM -H → Flags
```

**Lección:** La enumeración de Active Directory combinando herramientas como enum4linux, Kerbrute y técnicas de robo de tickets Kerberos permite comprometer un dominio completo.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.