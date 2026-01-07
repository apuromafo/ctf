1,Recon
port scan
```
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 4.3 (protocol 2.0)
| ssh-hostkey: 
|   1024 ad:ee:5a:bb:69:37:fb:27:af:b8:30:72:a0:f9:6f:53 (DSA)
|_  2048 bc:c6:73:59:13:a1:8a:4b:55:07:50:f6:65:1d:6d:0d (RSA)
25/tcp   open  smtp       Postfix smtpd
|_smtp-commands: beep.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN
80/tcp   open  http       Apache httpd 2.2.3
|_http-title: Did not follow redirect to https://10.10.10.7/
|_http-server-header: Apache/2.2.3 (CentOS)
110/tcp  open  pop3       Cyrus pop3d 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_pop3-capabilities: STLS LOGIN-DELAY(0) USER APOP RESP-CODES UIDL AUTH-RESP-CODE PIPELINING EXPIRE(NEVER) TOP IMPLEMENTATION(Cyrus POP3 server v2)
111/tcp  open  rpcbind    2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1            790/udp   status
|_  100024  1            793/tcp   status
143/tcp  open  imap       Cyrus imapd 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_imap-capabilities: Completed OK ANNOTATEMORE MAILBOX-REFERRALS CATENATE LITERAL+ CHILDREN LISTEXT URLAUTHA0001 LIST-SUBSCRIBED X-NETSCAPE IDLE SORT=MODSEQ IMAP4 SORT NO ID STARTTLS THREAD=REFERENCES RENAME ACL UIDPLUS CONDSTORE RIGHTS=kxte MULTIAPPEND IMAP4rev1 BINARY QUOTA ATOMIC UNSELECT THREAD=ORDEREDSUBJECT NAMESPACE
443/tcp  open  ssl/http   Apache httpd 2.2.3 ((CentOS))
|_ssl-date: 2024-10-30T13:26:52+00:00; +6s from scanner time.
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2017-04-07T08:22:08
|_Not valid after:  2018-04-07T08:22:08
|_http-title: Elastix - Login page
|_http-server-header: Apache/2.2.3 (CentOS)
| http-robots.txt: 1 disallowed entry 
|_/
793/tcp  open  status     1 (RPC #100024)
993/tcp  open  ssl/imap   Cyrus imapd
|_imap-capabilities: CAPABILITY
995/tcp  open  pop3       Cyrus pop3d
3306/tcp open  mysql      MySQL (unauthorized)
4190/tcp open  sieve?
4445/tcp open  upnotifyp?
4559/tcp open  hylafax    HylaFAX 4.3.10
5038/tcp open  asterisk   Asterisk Call Manager 1.1
```

Then we firstly check the index page.
![](images/Pasted%20image%2020241030094526.png)

We found Elastix - Login page

```
Elastix is ​​an open source IP communication platform that focuses on VoIP (Internet phone), unified communications (Unified Communications) and call center solutions. It integrates a variety of communication tools to help enterprises build a complete communication system, usually used for telephone systems of small to medium-sized enterprises.
```

Let's dirb and enumerate all the web-content:
![](images/Pasted%20image%2020241030095312.png)

In this place, `/admin` would be our target.
When we check it, it would  be a pop-up authentication window is displayed, asking for authentication, if we do not pass the auth, it would redirect to the url 
`https://10.10.10.7/admin/config.php`
![](images/Pasted%20image%2020241030095517.png)
Then we can get the version of freepbx `FreePBX 2.8.1.4`
We can search the exploit of it and check the vulner.
Thus we found it from exploit-db
`FreePBX 2.10.0 / Elastix 2.2.0 - Remote Code Execution`
It's a RCE, good news for us and we can find the exploit script from github.

https://www.exploit-db.com/exploits/18650 You can download it from here. But it won’t work. You have to make some additional changes to make it work since the server had an SSL certificate which is by the way expired. So I made a few modifications in the script.

Before doing that we have to check what are the extensions available so we can modify the script before it is executed. To check that just run a simple command

We can even find another exploit here 
Exploit: https://www.exploit-db.com/exploits/37637/

Then we successfully get the shell as asterisk.

2,shell as valid user
From the file `/etc/passwd`
```
asterisk:x:100:101:Asterisk VoIP PBX:/var/lib/asterisk:/bin/bash
spamfilter:x:500:500::/home/spamfilter:/bin/bash
fanis:x:501:501::/home/fanis:/bin/bash
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash
```

That means we need to switch to them and then get the access to root.

When we check `sudo -l `
```
User asterisk may run the following commands on this host:
    (root) NOPASSWD: /sbin/shutdown
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/bin/yum
    (root) NOPASSWD: /bin/touch
    (root) NOPASSWD: /bin/chmod
    (root) NOPASSWD: /bin/chown
    (root) NOPASSWD: /sbin/service
    (root) NOPASSWD: /sbin/init
    (root) NOPASSWD: /usr/sbin/postmap
    (root) NOPASSWD: /usr/sbin/postfix
    (root) NOPASSWD: /usr/sbin/saslpasswd2
    (root) NOPASSWD: /usr/sbin/hardware_detector
    (root) NOPASSWD: /sbin/chkconfig
    (root) NOPASSWD: /usr/sbin/elastix-helper

```

It was crazy and tricky, so let's use one of them.
Then we can find some hints from GTBOBins
```
The interactive mode, available on versions 2.02 to 5.21, can be used to execute shell commands.

sudo nmap --interactive
nmap> !sh
```

