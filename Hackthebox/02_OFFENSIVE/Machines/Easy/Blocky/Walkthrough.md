1,Recon
port scan
```
PORT      STATE  SERVICE   VERSION
21/tcp    open   ftp       ProFTPD 1.3.5a
22/tcp    open   ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d6:2b:99:b4:d5:e7:53:ce:2b:fc:b5:d7:9d:79:fb:a2 (RSA)
|   256 5d:7f:38:95:70:c9:be:ac:67:a0:1e:86:e7:97:84:03 (ECDSA)
|_  256 09:d5:c2:04:95:1a:90:ef:87:56:25:97:df:83:70:67 (ED25519)
80/tcp    open   http      Apache httpd 2.4.18
|_http-title: Did not follow redirect to http://blocky.htb
|_http-server-header: Apache/2.4.18 (Ubuntu)
8192/tcp  closed sophos
25565/tcp open   minecraft Minecraft 1.11.2 (Protocol: 127, Message: A Minecraft Server, Users: 0/20)
Service Info: Host: 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

Firstly, by checking the service of port 80, we found it was powered by WordPress 4.8

So I would want to check the existed web-content
```
.htaccess               
index.php               
javascript              
.hta                    
.htpasswd               
phpmyadmin              
plugins                 
server-status           
wiki                    
wp-admin                
wp-includes             
wp-content              
xmlrpc.php              
```

`/wp-admin` and `/phpmyadmin` would be our target.But we did not have any valid credits for both of them.

And because of we have known the version of `wordpress` is 4.8.So we can check the versions of its plugins.

![](images/Pasted%20image%2020241102081159.png)

Looking at the jar files, griefprevention is an open source plugin that is freely available.
BlockyCore, however, appears to be created by the server administrator, as its title relates
directly to the server. Decompiling with JD-GUI exposes the credentials for the root MySQL user.
```
package com.myfirstplugin;  
  
public class BlockyCore {  
  public String sqlHost = "localhost";  
    
  public String sqlUser = "root";  
    
  public String sqlPass = "8YsqfCTnvxAUeduzjNSXe22";  
    
  public void onServerStart() {}  
    
  public void onServerStop() {}  
    
  public void onPlayerJoin() {  
    sendMessage("TODO get username", "Welcome to the BlockyCraft!!!!!!!");  
  }  
    
  public void sendMessage(String username, String message) {}  
}
```

So we get the database credit `root:8YsqfCTnvxAUeduzjNSXe22`

Then we can use this credit to login to `/phpMyAdmin` page
![](images/Pasted%20image%2020241102081421.png)

After enumerate the database, we found the valid user's password hash and username
![](images/Pasted%20image%2020241102081921.png)

We can use hashcat or john to crack that, but it seems like a rabbit hole, we could not crack it in a few minutes.

So maybe, we can try to use the password of database and the valid username `notch` to use ssh to get the shell as notch.

Luckily, it worked.

2,shell as root
When I check what can notch do as root, we get the tricky result
```
sudo -l
Matching Defaults entries for notch on Blocky:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User notch may run the following commands on Blocky:
    (ALL : ALL) ALL

```

so we just need to `sudo /bin/bash -p`, then get the root shell.
