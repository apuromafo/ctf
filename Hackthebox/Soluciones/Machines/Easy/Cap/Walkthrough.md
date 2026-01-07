1, Recon
port scan
	21/tcp ftp `vsfrpd 3.0.3`
	22/tcp ssh `OpenSSH 8.2p1`
	80/tcp http `gunicorn`
page analysis
There are 3 pages `\capture \ip \netstat`
`\ip` would be ifconfig
`\netstat` would be netstat
but capture like a wireshark, and we have try it and redirect to `/data/1` not from `/data/0`

This a tricky thing and we successfully get something interesting from that
![](images/Pasted%20image%2020240909092313.png)We get the ftp credit `nathan:Buck3tH4TF0RM3!`
And also we can use this credit to ssh connect to the machine.

When I come to find root shell, there is nothing could be used or exploited.

So let's come to the service directory.
We can find the relative command injection in the app.py and even use root.
```
path = os.path.join(app.root_path, "upload", str(pcapid) + ".pcap")
ip = request.remote_addr
command = f"""python3 -c 'import os; os.setuid(0); os.system("timeout 5 tcpdump -w {path} -i any host {ip}")'"""
```
In this place, I am curious about how python can exec as root
```
-rw-r--r-- 1 nathan nathan 4293 May 25  2021 app.py

nathan@cap:/var/www/html$ ls -l /usr/bin/python3
lrwxrwxrwx 1 root root 9 Mar 13  2020 /usr/bin/python3 -> python3.8

nathan@cap:/var/www/html$ ls -l /usr/bin/python3.8
-rwxr-xr-x 1 root root 5486384 Jan 27  2021 /usr/bin/python3.8

nathan@cap:/var/www/html$ getcap /usr/bin/python3.8
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
```

The man page describes cap_net_bind_service as:
```
Bind a socket to Internet domain privileged ports (port
numbers less than 1024).
```
This is a really useful capability because it allows this one action without giving full root. In fact, I’ve set this capability on python on my VM so I don’t have to run sudo every time I want to start a Python webserver.

The man page describes cap_setuid as:
```
* Make arbitrary manipulations of process UIDs (setuid(2),
setreuid(2), setresuid(2), setfsuid(2));
* forge UID when passing socket credentials via UNIX
domain sockets;
* write a user ID mapping in a user namespace (see
user_namespaces(7)).
```
cap_seduid has some good uses on binaries, but on something like Python which can take arbitrary user input, it is dangerous.

Then we can use python to get reverse shell or just change the uid.
