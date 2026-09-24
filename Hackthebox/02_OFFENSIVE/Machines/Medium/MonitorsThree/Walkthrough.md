*1, Enumerate the port and services*
```
22/tcp ssh
80/tcp http redirect to http://monitorsthree.htb/
```

`ffuf -u http://monitorsthree.htb/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt`

From the ffuf scan, we did not find something interesting.But In the index page, we can find the login page.

And from the `Password recovery` page, we have found the user admin exist.
In this place, we can try to brute crake it , we let's check other way.

We guess there would be other virtual host or sub-domain, So let's enumerate it by using ffuf.
`ffuf -u http://monitorsthree.htb -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host:FUZZ.monitorsthree.htb" -fw 3598`
Luckily, we get the sub-domain `cacti.monitorsthree.htb`

And we can get the version of cacti
`Version 1.2.26 | (c) 2004-2024 - The Cacti Group`

So let's check it and find something could be exploited.
Very sadly, there is only the exploits of version 1.2.22, so let's try some default credits.
`admin:admin` but it didnot work.
So let's continue to enumerate the web-contents of this subdomain page.

Then we can found  `\app`  is the original page of the main domain
`\cacti` is the subdomain service.

So let's try to catch the root path '\'. Sadly, there is nothing in the root path.

2, get the user shell
Let's come back to the original page.
We can try to use sqlmap to check the sql-injection for login page and password recovery page.

We use the payload `test' or 1=1-- -`, get the injection hint from password recovery page.

So let's use burp to catch the request and sqlmap it.

We need a python script to help us to get this hash because when we use the sqlmap and use the time-based and error-based it would be a long long time to get the mysql shell.

Then we get the hash 
`31a181c8372e3afc59dab863430610e8:greencacti2001`

When we search the github we find something interesting
` Exploit for Cacti Import Packages RCE CVE-2024-25641`
This is a new vulner and we can use msf or some exploits of github to get the www-data shell.

Then we can firstly check the essential user
```
marcus:x:1000:1000:Marcus:/home/marcus:/bin/bash
```
And we have used the sql-injection to get the useful things, so let's try again and enumerate the useful directory or files.

Then we can get the database information from /var/www/html/app/admin/db.php
```
<?php

$dsn = 'mysql:host=127.0.0.1;port=3306;dbname=monitorsthree_db';
$username = 'app_user';
$password = 'php_app_password';
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $username, $password, $options);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
```
But this is a rabbit hole, we can not get any local user credits

So let's come back to /cacti/include
There is a config.php and there is another mysql credits
```
$database_type     = 'mysql';
$database_default  = 'cacti';
$database_hostname = 'localhost';
$database_username = 'cactiuser';
$database_password = 'cactiuser';`
```

And from databases, we get the user credits
`marcus   | $2y$10$Fq8wGXvlM3Le.5LIzmM9weFs9s6W2i1FLg3yrdNGmkIaxo79IBjtK`
Let's crack this hash `password:12345678910`

Then we get the marcus shell.

3, switch to the root shell
Then we check the sudo -l ,but this is user can not do anything with root

So we check the netstat
```
netstat -ntlp

Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8084            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:37887         0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8200          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      - 
```
port 8200 and 8084 would be interesting, let's curl it.

When we check it on our browser, we find a interesting service
`## Duplicati , a popular backup solution`
`https://medium.com/@STarXT/duplicati-bypassing-login-authentication-with-server-passphrase-024d6991e9ee`
There is a sqlite file 
`/opt/duplicati/config/Duplicati-server.sqlite`

Lets's get it in our own machine


Then if we successfully login, we just need to backup the /source/root/root.txt
And we can find it in the folder /opt/duplicati/config/


