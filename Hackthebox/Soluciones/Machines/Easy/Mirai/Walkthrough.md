1,Recon
port scan 
```
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u3 (protocol 2.0)
| ssh-hostkey: 
|   1024 aa:ef:5c:e0:8e:86:97:82:47:ff:4a:e5:40:18:90:c5 (DSA)
|   2048 e8:c1:9d:c5:43:ab:fe:61:23:3b:d7:e4:af:9b:74:18 (RSA)
|   256 b6:a0:78:38:d0:c8:10:94:8b:44:b2:ea:a0:17:42:2b (ECDSA)
|_  256 4d:68:40:f7:20:c4:e5:52:80:7a:44:38:b8:a2:a7:52 (ED25519)
53/tcp    open  domain  dnsmasq 2.76
| dns-nsid: 
|_  bind.version: dnsmasq-2.76
80/tcp    open  http    lighttpd 1.4.35
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: lighttpd/1.4.35
1159/tcp  open  upnp    Platinum UPnP 1.0.5.13 (UPnP/1.0 DLNADOC/1.50)
32400/tcp open  http    Plex Media Server httpd
|_http-title: Unauthorized
|_http-cors: HEAD GET POST PUT DELETE OPTIONS
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
|_http-favicon: Plex
32469/tcp open  upnp    Platinum UPnP 1.0.5.13 (UPnP/1.0 DLNADOC/1.50)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

By use gobuster to enumerate the valid url
```
/admin                (Status: 301) [Size: 0]
/versions             (Status: 200) [Size: 18]
```

So, `/admin` would be our target
![](images/Pasted%20image%2020241102094858.png)

In the bottom of this page, we can find so many versions of services.
`**Pi-hole Version** v3.1.4``
`**Web Interface Version** v3.1`
`**FTL Version** v2.10`
By searching them from google and we can find one RCE from exploit-db.
`Pi-hole < 4.4 - Authenticated Remote Code Execution`

But very sadly, we don't have any password to pass the auth.

Knowing the target operating system and device, while keeping in mind how the Mirai botnet operates, it can be assumed that the default user credentials have been unchanged. 

A quicksearch reveals that the default Raspbian credentials are `pi:raspberry`. Connecting via SSH with these credentials immediately gives full access to the device, as the default configuration for Raspbian has the pi user as part of the sudoers group.

Then we can try to ssh to connect the shell as pi.
`ssh pi@10.10.10.48`

And when I check `sudo -l`
```
it is very lucky

sudo -l
Matching Defaults entries for pi on localhost:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User pi may run the following commands on localhost:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: ALL

Then we just need to sudo /bin/bash -p and then get the root shell.

but the root.txt is lost, and it said
I lost my original root.txt! I think I may have a backup on my USB stick...

So we need to continue to enumerate this file system.

I found another hint here `/media/usbstick/damnit.txt`
Damnit! Sorry man I accidentally deleted your files off the USB stick.

So we need to find a way to get the lost file back.
While not the intended method, strings will immediately reveal the flag if run on /dev/sdb.

```

```
/dev/sdb 通常指的是系统中的第二块硬盘或存储设备。

在 Linux 系统中，所有存储设备（硬盘、USB 驱动器等）会在 /dev 目录下表示为设备文件。命名规则如下：

/dev/sda：表示系统中的第一块 SCSI/SATA 硬盘。
/dev/sdb：通常表示第二块 SCSI/SATA 硬盘。
/dev/sdc、/dev/sdd 等：依次表示第三、第四块硬盘。
```

![](images/Pasted%20image%2020241102101443.png)





