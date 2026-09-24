# Detection Opsec Cyber Range


---
## Page 1

Atomic Red Team
Command
Description
Import-Module ~/AtomicRedTeam/invoke-
atomicredteam/Invoke-
AtomicRedTeam.psd1
Imports the AtomicRedTeam module.
Invoke-AtomicTest <Test>
Executing an Atomic Red Team test
(atomic).
Invoke-AtomicTest T1014 -TestNumbers 3
Executing the third test related to T1014
Atomic Red Team test (atomic) related to
Rootkits.
Invoke-AtomicTest T1014 -TestNumbers 3
-ShowDetails
Displays the details of the T1014-related
Atomic Red Team test (atomic) without
executing the test.
Credentials
Instance
Username
Password
Splunk
Management
Console (Port
7777)
root
P3n#31337@LOG
DETECTION & OPSEC CYBER
RANGE
CHEAT SHEET

---
## Page 2

Instance
Username
Password
Suricata
root
P3n#31337@LOG
Wazuh
admin
68xHq*Mt48kDpeZOHhBcrgi?
YR7BK+VH
Wazuh
dfir
P3n#31337@LOG
Wazuh
forensics
P3n#31337@LOG
Wazuh
htb-analyst
P3n#31337@LOG
Wazuh
hunters
P3n#31337@LOG
Wazuh
socteam
P3n#31337@LOG
Wazuh
Management
lab_adm
P3n#31337@LOG
TheHive
htb-analyst
P3n#31337@LOG
TheHive
socteam@hackthebox.com
P3n#31337@LOG
File Transfer
Command
Description
scp /path/to/local/file
username@<Target_IP>:/path/to/remote/destination
Copy files from Pwnbox
to a Purple Module
target
scp username@<Target_IP>:/path/to/remote/file
/path/to/local/destination
Copy files from a
Purple Module target
back to Pwnbox
rsync -avz /path/to/local/file
username@<Target_IP>:/path/to/remote/destination
Transferring Files from
Pwnbox to a Linux
Purple Module Target

---
## Page 3

Command
Description
rsync -avz username@<Target_IP>:/path/to/remote/file
/path/to/local/destination
Transferring Files from
a Linux Purple Module
Target to Pwnbox
sftp username@<Target_IP>
Connect to Linux
Purple Module Target
via sftp
put /path/to/local/file /path/to/remote/destination
Command to upload a
file via sftp to a Linux
Purple module target
get /path/to/remote/file /path/to/local/destination
Command to download
a file via sftp from a
Linux Purple module
target
Splunk Queries (SPL)
Query
Description
index=main host="ubuntu" source="auditd" type=PATH
name="/etc/ld.so.preload"
SPL query designed to
detect signs of T1014-3
dynamic-linker-based
rootkit.
index=main host="ubuntu"
source="journald://sysmon" EventCode=1 Image="*dd"
CommandLine="*of=*"
SPL query designed to
detect signs of T1485-2
FreeBSD/macOS/Linux -
Overwrite files with DD.
index="main" host="LOGGING-VM"
source=WinEventLog:Security EventCode=4720| stats
count by host, Subject_Account_Name,
New_Account_Account_Name, New_Account_Domain,
Primary_Group_ID, status, _time
SPL query design to detect
signs T1136.001 - Create
Account: Local Account.
index=zeek
source="/opt/zeek/logs/current/conn.log"
orig_bytes=0 dest_ip IN (192.168.0.0/16,
172.16.0.0/12, 10.0.0.0/8) | bin span=5m _time |
stats dc(dest_port) as num_dest_port by _time,
src_ip, dest_ip | where num_dest_port >= 3
SPL query designed to
detect signs of port
scanning.

---
## Page 4

Wazuh Queries (WQL)
Query
Description
agent.name:"LINUX-LOGGING" AND data.system.channel: "Linux-
Sysmon/Operational" AND data.system.eventId: 11 AND
data.eventdata.targetFilename:*/etc/cron.d/*
WQL query
designed to
display events
related to file
creation or file
write.
agent.name: "Logging-VM" AND data.win.system.channel:
"Microsoft-Windows-Sysmon/Operational" AND
data.win.eventdata.image: *reg.exe
WQL query
designed to detect
signs of
T1547.001-1 Reg
Key Run.
agent.name:"Logging-VM" AND data.win.system.eventID:7 AND
data.win.eventdata.originalFileName:"vaultcli.dll"
WQL query
designed to detect
the loading of the
vaultcli.dll
DLL.