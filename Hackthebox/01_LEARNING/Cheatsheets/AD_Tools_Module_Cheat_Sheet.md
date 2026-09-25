# AD Tools — Cheat Sheet

> **Fuente / Source:** [m4riio21/HTB-Academy-Cheatsheets](https://github.com/m4riio21/HTB-Academy-Cheatsheets) (`AD-Tools.md`) — fecha de acceso: 2026-09-24. Herramientas de los módulos AD de HTB Academy.
> **Autor notas:** Apuromafo (curaduría local).

---

# Tools of the Trade

| Tool              | Description |
| ----------------- | ----------- |
| [PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1) / [SharpView](https://github.com/dmchell/SharpView) | PowerShell + port .NET para situational awareness en AD (reemplazo de `net*`, Kerberoasting, ASREPRoasting). |
| [BloodHound](https://github.com/BloodHoundAD/BloodHound) + [SharpHound](https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors) | Mapeo visual de relaciones AD y attack paths (ingestor + Neo4j). |
| [BloodHound.py](https://github.com/fox-it/BloodHound.py) | Ingestor Python (Impacket), corre sin estar unido al dominio. |
| [Kerbrute](https://github.com/ropnop/kerbrute) | Enumeración de cuentas AD vía Kerberos pre-auth + password spraying (Go). |
| [Impacket](https://github.com/SecureAuthCorp/impacket/) | Colección Python para protocolos de red (psexec, wmiexec, secretsdump, ticketer, etc.). |
| [Responder](https://github.com/lgandx/Responder) / [Inveigh](https://github.com/Kevin-Robertson/Inveigh) | Envenenamiento LLMNR/NBT-NS/mDNS (+ versión C# InveighZero). |
| [rpcclient](https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html) (Samba) | Enumeración AD vía RPC. |
| [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) → fork [NetExec](https://github.com/Pennyw0rth/NetExec) | "Swiss Army Knife" redes: SMB/WMI/WinRM/MSSQL, cmedb. |
| [Rubeus](https://github.com/GhostPack/Rubeus) | Abuso de Kerberos en C#. |
| [GetUserSPNs.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py) | SPNs de usuarios (Kerberoasting). |
| [Hashcat](https://hashcat.net/hashcat/) | Cracking de hashes. |
| [enum4linux](https://github.com/CiscoCXSecurity/enum4linux) / [enum4linux-ng](https://github.com/cddmp/enum4linux-ng) | Enumeración Windows/Samba. |
| [ldapsearch](https://linux.die.net/man/1/ldapsearch) / [windapsearch](https://github.com/ropnop/windapsearch) | Queries LDAP (manual + automatizado). |
| [DomainPasswordSpray](https://github.com/dafthack/DomainPasswordSpray) | Password spraying contra usuarios del dominio. |
| [LAPSToolkit](https://github.com/leoloobeek/LAPSToolkit) | Auditoría/ataque de entornos con LAPS (vía PowerView). |
| [smbmap](https://github.com/ShawnDEvans/smbmap) | Enumeración de shares SMB en el dominio. |
| [Snaffler](https://github.com/SnaffCon/Snaffler) | Credenciales en shares accesibles. |
| [smbserver.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py) | Servidor SMB simple (transferencia de archivos). |
| [Mimikatz](https://github.com/ParrotSec/mimikatz) | Pass-the-hash, plaintexts en memoria, tickets Kerberos. |
| [evil-winrm](https://github.com/Hackplayers/evil-winrm) | Shell interactiva por WinRM. |
| [noPac.py](https://github.com/Ridter/noPac) (CVE-2021-42278 + CVE-2021-42287) | Impersonar DA desde usuario estándar. |
| [PetitPotam](https://github.com/topotam/PetitPotam) (CVE-2021-36942) | Coerción de autenticación (MS-EFSRPC). |
| [PKINITtools](https://github.com/dirkjanm/PKINITtools) (`gettgtpkinit.py`, `getnthash.py`) | Certificados y TGTs (U2U/PAC). |
| [adidnsdump](https://github.com/dirkjanm/adidnsdump) | Dump de DNS del dominio (ADIDNS). |
| [gpp-decrypt](https://github.com/t0thkr1s/gpp-decrypt) | Credenciales en Group Policy Preferences. |
| [GetNPUsers.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetNPUsers.py) | ASREPRoasting (sin preauth). |
| [lookupsid.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/lookupsid.py) | SID bruteforcing. |
| [AD Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/adexplorer) (Sysinternals) | Visor/editor AD + snapshots offline. |
| [PingCastle](https://www.pingcastle.com/documentation/) | Auditoría de seguridad AD (risk/madurez). |
| [Group3r](https://github.com/Group3r/Group3r) | Auditoría de GPOs. |
| [ADRecon](https://github.com/adrecon/ADRecon) | Extracción de datos AD a Excel con análisis. |

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox.

_Fecha de edición: 2026-09-24_
