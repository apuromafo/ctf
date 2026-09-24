1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 68:af:80:86:6e:61:7e:bf:0b:ea:10:52:d7:7a:94:3d (ECDSA)
|_  256 52:f4:8d:f1:c7:85:b6:6f:c6:5f:b2:db:a6:17:68:ae (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://heal.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Page check
![](images/Pasted%20image%2020250101060923.png)
In this page, the login button or register button didn't work in this place.There is no any post response here.
![](images/Pasted%20image%2020250101062055.png)
From the source code, I found the label "noscript", I think I can try to change it and check the effect of this script.
By using the burp to catch the package, I found something interesting,
![](images/Pasted%20image%2020250101062411.png)
```
In this place, There is a special word `cross-domain magic`, that means there is a sub-domain like a `api.example.com`

1. 跨域 (Cross-Domain) 的背景
在 Web 开发中，浏览器对跨域请求的限制是为了安全性。比如，从 https://example.com 请求 https://api.example.com 就属于跨域。如果没有正确的设置，浏览器会阻止这些请求。

跨域魔法（Cross-Domain Magic）可能指的是开发者利用某些技术或手段绕过或实现跨域请求。
```

By check `/resume` page, we can found 
![](images/Pasted%20image%2020250101070328.png)
And also, we can get another sub-domain
`http://take-survey.heal.htb/index.php/552933?lang=en`
And also, we can by submit the form to get the valid cookie and we can come to `api.heal.htb` to download files.
![](images/Pasted%20image%2020250101071932.png)
From the `/etc/passwd` we found the valid user is `ron`
We have known the version of this service, so we can use this LFI to check the configuration.
![](images/Pasted%20image%2020250101072312.png)
```
test:
  <<: *default
  database: storage/test.sqlite3

production:
  <<: *default
  database: storage/development.sqlite3
```
We got it `storage/development.sqlite3` and check what is going on here.
```
sqlite> .tables
ar_internal_metadata  token_blacklists    
schema_migrations     users               
sqlite> select * from users;
1|ralph@heal.htb|$2a$12$dUZ/O7KJT3.zE4TOK8p4RuxH3t.Bz45DSr7A94VLvY9SWx1GCSZnG|2024-09-27 07:49:31.614858|2024-09-27 07:49:31.614858|Administrator|ralph|1
2|cooper@cooper.cooper|$2a$12$7W6nhIB6/hRdmbzTXt2qeuoSta6zxbhIun6jfkfqezHHGHjM/JX.y|2025-01-01 07:19:48.318586|2025-01-01 07:19:48.318586|cooper|cooper|0
3|cooper2@cooper.cooper|$2a$12$4Lm6RuaXlRIxkNYcq3ClrOtvM4kIE7pSC1yoJUSPOrCCiS.uteBla|2025-01-01 08:03:42.999713|2025-01-01 08:03:42.999713|cooper2|cooper2|0
```
Then by using the hashcat to crack it 
we get `$2a$12$dUZ/O7KJT3.zE4TOK8p4RuxH3t.Bz45DSr7A94VLvY9SWx1GCSZnG:147258369`


So I would continue to check the valid web-contents.
By using `fuff` to check the valid sub-domain, I found a valid sub-domain name `api.heal.htb`
![](images/Pasted%20image%2020250101061351.png)
Then we can get versions here.
So let's continue to enumerate the valid web-contents

As before, we have get the credit `ralph : 147258369`
So let's come to login to admin dashboard
![](images/Pasted%20image%2020250101072957.png)

Then we login successfully 
![](images/Pasted%20image%2020250101073035.png)
And in the bottom of page, we can get the version of `LimeSurvey`
`[LimeSurvey Community Edition](https://community.limesurvey.org) [Version 6.6.4])`
By check the versions from the exploit-db, we found
`LimeSurvey 5.2.4 - Remote Code Execution (RCE) (Authenticated)`
`https://github.com/Y1LD1R1M-1337/Limesurvey-RCE.git`
![](images/Pasted%20image%2020250101073943.png)
Besides change the reverse shell and we need to change the version of config, we need the version 6.0
Then let's curl `http://take-survey.heal.htb/upload/plugins/111/php-rev.php`
Finally we can get the reverse shell as `www-data`

Let's enumerate the config file `/var/www/limesurvey/application/config/config.php`
```
db' => array(
                        'connectionString' => 'pgsql:host=localhost;port=5432;user=db_user;password=AdmiDi0_pA$$w0rd;dbname=survey;',
                        'emulatePrepare' => true,
                        'username' => 'db_user',
                        'password' => 'AdmiDi0_pA$$w0rd',
                        'charset' => 'utf8',
                        'tablePrefix' => 'lime_',
                ),

```
I hope we can just use this password to login as `ron` .We are lucky, we get it.

2, shell as root
Firstly, I would check `sudo -l` first.
`Sorry, user ron may not run sudo on heal.`
Then I would continue to check the netstate
```
ron@heal:~$ netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8300          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8301          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8302          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8600          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8500          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8503          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3001          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      - 
```
And I found port 8500 seems like our target
```
curl 127.0.0.1:8500
<a href="/ui/">Moved Permanently</a>.

```
Let's Port forwarding to local machine and check it from firefox.
![](images/Pasted%20image%2020250101075657.png)
We found the version `Consul v1.19.2`
And by searching from exploit-db, we found 
`Hashicorp Consul v1.0 - Remote Command Execution (RCE)`
Let's run the script and over this machine.

