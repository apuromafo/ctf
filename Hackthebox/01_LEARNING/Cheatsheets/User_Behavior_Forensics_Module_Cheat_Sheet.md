# User Behavior Forensics


---
## Page 1

Some common registry paths are mentioned as follows:
Artifact
Registry Path
Shellbags
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Bags
Shellbags
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\BagMRU
UserAssist
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
WordWheelQuery
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
JumpList
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search\JumplistData
RunMRU
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
RunMRU
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
RecentDocs
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
Open/Save
Dialog MRUs
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\
TypedPaths
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
MS Office MRU
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\
Adobe Recent
Files
HKEY_CURRENT_USER\Software\Adobe\Adobe Acrobat\DC\AVGeneral\cRecentFiles
WinZip
HKEY_CURRENT_USER\SOFTWARE\WinZip Computing\WinZip\extract
USER BEHAVIOR FORENSICS
CHEAT SHEET

---
## Page 2

Artifact
Registry Path
SSH (Putty)
HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys
tsclient
HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default
Tools locations, and commands used in the module target system are mentioned as follows:
Command
Description
Run Registry
Explorer
C:\Tools\DFIR-Data\Tools\EZ-Tools\net6\RegistryExplorer\RegistryExplorer.exe
List all RegRipper
Plugins
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -l
Run RegRipper's
shellbags plugin
 C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r "C:\Tools\DFIR-
Data\evidence\001.shellbags_data\D\Users\John
Doe\AppData\Local\Microsoft\Windows\UsrClass.dat" -p shellbags
Run RegRipper's
userassist plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\002.userassist\NTUSER.DAT -p userassist_tln
Run RegRipper's
wordwheelquery
plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\003.searchhistory\NTUSER.DAT -p wordwheelquery
Parse Jumplist data
using JLECMD
C:\Tools\DFIR-Data\Tools\EZ-Tools\net6\JLECmd.exe -d "C:\Tools\DFIR-
Data\evidence\004.jumplists\KAPE_Output\D\Users\John
Doe\AppData\Roaming\Microsoft\Windows\Recent" --csv "C:\Tools\DFIR-
Data\evidence\004.jumplists\JLE csv"
Run RegRipper's
jumplistdata plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\004.jumplists\NTUSER.DAT -p jumplistdata
Parse single LNK file
using LECMD
C:\Tools\DFIR-Data\Tools\EZ-Tools\net6\LECmd.exe -f "C:\Tools\DFIR-
Data\evidence\005.lnk\KAPE_Output\D\Users\John
Doe\AppData\Roaming\Microsoft\Windows\Recent\passwords.lnk"
Parse multiple LNK
files using LECMD
C:\Tools\DFIR-Data\Tools\EZ-Tools\net6\LECmd.exe -d "C:\Tools\DFIR-
Data\evidence\005.lnk\lnk_files\"
Run RegRipper's
runmru plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\006.run_mru\NTUSER.DAT" -p runmru

---
## Page 3

Command
Description
Run RegRipper's
recentdocs plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\007.recentdocs\NTUSER.DAT" -p recentdocs
Run RegRipper's
comdlg32 plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\008.open_save\NTUSER.DAT" -p comdlg32
Run RegRipper's
typedpaths plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\009.typedpaths\NTUSER.DAT" -p typedpaths
Run RegRipper's
msoffice plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\010.msoffice\NTUSER.DAT" -p msoffice
Run RegRipper's
winzip plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\018.archive_history\NTUSER.DAT" -p winzip
Run RegRipper's
adobe plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\017.adobe\NTUSER.DAT" -p adobe
Parse Sticky Notes
db using stickyparser
py C:\Tools\DFIR-Data\Tools\StickyParser\stickyparser.py -p C:\Tools\DFIR-
Data\evidence\011.stickynotes\plum.sqlite -d C:\Temp
Run RegRipper's
putty plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\014.sshHostKeys\NTUSER.DAT" -p putty
Run RegRipper's
tsclient plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\016.tsclient\NTUSER.DAT" -p tsclient
Parse
ActivitiesCache.db
using WxTCmd
C:\Tools\DFIR-Data\Tools\EZ-Tools\net6\WxTCmd.exe -f C:\Tools\DFIR-
Data\evidence\015.activityCache\ActivitiesCache.db --csv C:\tmp
Run RegRipper's
usbstor plugin
C:\Tools\DFIR-Data\Tools\RegRipper\rip.exe -r C:\Tools\DFIR-
Data\evidence\019.usb-devices\exercise\SYSTEM" -p usbstor