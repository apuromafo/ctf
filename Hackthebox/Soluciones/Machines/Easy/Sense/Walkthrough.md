1, Recon
port scan
```
PORT    STATE SERVICE  VERSION
80/tcp  open  http     lighttpd 1.4.35
|_http-title: Did not follow redirect to https://10.10.10.60/
|_http-server-header: lighttpd/1.4.35
443/tcp open  ssl/http lighttpd 1.4.35
|_http-server-header: lighttpd/1.4.35
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=Common Name (eg, YOUR name)/organizationName=CompanyName/stateOrProvinceName=Somewhere/countryName=US
| Not valid before: 2017-10-14T19:21:35
|_Not valid after:  2023-04-06T19:21:35
|_http-title: Login
```
page check
The page is a pfsense login screen:
![](images/Pasted%20image%2020241207080649.png)

Directory Brute Force:
I started with gobuster
```
root@kali# gobuster -u https://10.10.10.60/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -k

Gobuster v1.4.1              OJ Reeves (@TheColonial)
=====================================================
=====================================================
[+] Mode         : dir
[+] Url/Domain   : https://10.10.10.60/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Status codes : 200,204,301,302,307
=====================================================
/themes (Status: 301)
/css (Status: 301)
/includes (Status: 301)
/javascript (Status: 301)
/classes (Status: 301)
/widgets (Status: 301)
/tree (Status: 301)
/shortcuts (Status: 301)
/installer (Status: 301)
/wizards (Status: 301)
/csrf (Status: 301)
/filebrowser (Status: 301)
=====================================================
```

Nothing useful here.

So I wanted to run a much more extensive brute force, looking in subdirectories and for more extensions. I kicked it off with the following:
```
dirbuster -u https://10.10.10.60 -t 20 -l /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r sense-10.10.10.60/dirbuster_dir-med -e php,txt,html
```
![](images/Pasted%20image%2020241207081620.png)

Anything of size 453 is a redirect to the login page.
`system-users.txt` is a good thing to checkout!
```
####Support ticket###

Please create the following user


username: Rohit
password: company defaults (Username: admin, Password: pfsense)
```
Then we can successfully login 
![](images/Pasted%20image%2020241207081940.png)
And also, I can also get the version of `pfsense` is `2.1.3-RELEASE(amd64)`

Then just search about that, we can find
`pfSense < 2.1.4 - 'status_rrd_graph_img.php' Command Injection`

Or just use msf to get shell.