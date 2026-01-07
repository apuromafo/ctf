 1, Port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 20:26:88:70:08:51:ee:de:3a:a6:20:41:87:96:25:17 (RSA)
|   256 4f:80:05:33:a6:d4:22:64:e9:ed:14:e3:12:bc:96:f1 (ECDSA)
|_  256 d9:88:1f:68:43:8e:d4:2a:52:fc:f0:66:d4:b9:ee:6b (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://nocturnal.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Page check
![](images/Pasted%20image%2020250415012323.png)Then I have try to use login and register, but seems there is dashboard here, and we can upload a file from that.
![](images/Pasted%20image%2020250415012604.png)
![](images/Pasted%20image%2020250415023835.png)
After upload a pdf file, we can press that name to check the file
`http://nocturnal.htb/view.php?username=wither&file=test.pdf`
![](images/Pasted%20image%2020250415024310.png)
In this place, we can try to ffuf the web-content to check is there anything else here.
We can get a interesting file here
`nocturnal.htb/view.php?username=amanda&file=privacy.odt`
And there are something interesting here
```
Dear Amanda,
Nocturnal has set the following temporary password for you: arHkG7HAI68X8s1J. This password has been set for all our services, so it is essential that you change it on your first login to ensure the security of your account and our infrastructure.
The file has been created and provided by Nocturnal's IT team. If you have any questions or need additional assistance during the password change process, please do not hesitate to contact us.
Remember that maintaining the security of your credentials is paramount to protecting your information and that of the company. We appreciate your prompt attention to this matter.

Yours sincerely,
Nocturnal's IT team
```

Then we get the valid credit `amanda:arHkG7HAI68X8s1J`
And after login with this credit, we can access into something new
![](images/Pasted%20image%2020250415024856.png)
Then we finally access into the admin page
![](images/Pasted%20image%2020250415025020.png)
Then we can also backup the system and download it
![](images/Pasted%20image%2020250415025302.png)
We can also check the source code of these services.
From the backup, we can find a database file here `nocturnal_database.db`
![](images/Pasted%20image%2020250415025912.png)
We can find a few hashes here, and only the password of `tobias` could be cracked
`tobias:slowmotionapocalypse`
And we can use the ssh to login and get the user shell.

2, shell as root
Firstly, I would check the `sudo -l`
```
tobias@nocturnal:~$ sudo -l
[sudo] password for tobias: 
Sorry, user tobias may not run sudo on nocturnal.
```
Then I would continue to check the valid port and services
```
tobias@nocturnal:~$ netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:587           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      - 
```
There is a port 8080 seems like be our targets
Let's port forwarding to our local machine, then we can check this service
![](images/Pasted%20image%2020250415134504.png)
By searching the exploits of `ispconfig`
we can find something interesting here `ISPConfig - PHP Code Injection (CVE-2023-46818)`
Then we can also find the exploits script here
`https://github.com/bipbopbup/CVE-2023-46818-python-exploit.git`
Then we can run the script 
`python3 exploit.py http://localhost:8080 admin slowmotionapocalypse`

Finally we can get the root shell.
