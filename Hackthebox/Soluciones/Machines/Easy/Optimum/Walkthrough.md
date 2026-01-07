1,Recon
port scan
```
PORT   STATE SERVICE VERSION
80/tcp open  http    HttpFileServer httpd 2.3
|_http-title: HFS /
|_http-server-header: HFS 2.3
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

We only get the version of the service of port 80 `HttpFileServer httpd 2.3`
Then we can search about the exploit of that and we would get the result
`Rejetto HTTP File Server (HFS) 2.3.x - Remote Command Execution (2)`
from exploit-db

So let's try to prove the exploit script and change it from python2 to python3

But it seems not to work, so we can try another one
`HFS (HTTP File Server) 2.3.x - Remote Command Execution (3)`

Then we successfully get the shell as `kostas`

2, switch to SYSTEM shell
Firstly we would check the existed users 
```
net user

User accounts for \\OPTIMUM

-------------------------------------------------------------------------------
Administrator            Guest                    kostas      
```

and the sysinfo
```
Host Name:                 OPTIMUM
OS Name:                   Microsoft Windows Server 2012 R2 Standard
OS Version:                6.3.9600 N/A Build 9600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User

```

The very old version of windows server !!!!

Privilege Escalation
```
Running sysinfo in Meterpreter shows that the target is a Windows 2012 R2 server with x64
architecture. It would be wise to migrate to an x64 process at this point, as the default
reverse_tcp shell is x32 architecture. Use the ps command to list processes, then migrate to the
explorer.exe process as it is x64, using the command migrate <pid>
Due to the unreliability of the local_exploit_suggester module on x64 systems, the best way
forward is to do search exploit/windows/local in Metasploit and review exploits for potential
target system matches.
After a bit of searching and some trial and error, ms16_032_secondary_logon_handle_privesc
ends up successfully creating a root shell. 
```