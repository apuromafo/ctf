# Introduction To Linux Forensics


---
## Page 1

Command
Description
tail -n 10 /var/log/syslog
View recent syslog
entries on a
Debian-based
system
dmesg
Check kernel logs
python3 zircolite.py --events audit.log --auditd --
ruleset rules/rules_linux.json --csv -o
audit_logs_zircolite.csv
Parse auditd logs
using SIGMA rules
with Zircolite and
export detections to
CSV
aureport -if audit.log
Generate
interpreted file
access report from
audit logs
ausearch --syscall EXECVE -if audit.log
Search audit logs
for process
execution events
(EXECVE syscalls)
in interpreted
format
INTRODUCTION TO LINUX
FORENSICS
CHEAT SHEET

---
## Page 2

Command
Description
ausearch -if audit.log -m ADD_USER -m DEL_USER -m
ADD_GROUP -m USER_CHAUTHTOK -m DEL_GROUP -m CHGRP_ID -m
ROLE_ASSIGN -m ROLE_REMOVE -i
Search audit logs
for user and group
management
events (add/delete
users/groups, role
changes)
sudo auditctl -s
Display the current
status of the audit
daemon
stat /etc/sudoers
Display metadata
(timestamps,
permissions) of the
sudoers file
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.bash.Bash
Recover bash
command history
from memory dump
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
banners.Banners
Identify Linux
kernel version and
OS banners from
memory dump
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.sockstat.Sockstat
List active network
sockets and
connections from
memory
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.pslist
Enumerate running
processes from
memory dump
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.netstat
Display network
connections and
ports from memory
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.pstree
Display process
parent-child
relationships
(process tree) from
memory

---
## Page 3

Command
Description
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.lsmod
Enumerate loaded
kernel modules
from memory dump
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.lsof
List files opened by
processes from
memory
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.check_syscall
Detect
modifications to the
syscall table from
memory
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.elfcore
Scan and recover
ELF executables
from memory dump
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.envvars --pid 28645
Extract
environment
variables for a
specific process
from memory
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.malfind.Malfind --pid 28645
Scan for hidden or
injected code in
process memory
python3 ~/volatility3/vol.py -q -f /path/to/server-dump
linux.proc.Maps --dump --pid 910
Dump virtual
memory mappings
for a process to file
strings -a pid.1441.vma.0x7fa7fc0c0000-0x7fa7fc0c6000.dmp
Extract printable
strings from a
dumped memory
segment
sudo ./avml memdump.mem
Acquire Linux
volatile memory
dump using AVML
tool
journalctl --utc
Display timestamps
in UTC

---
## Page 4

Command
Description
journalctl -b
Display logs from
current boot
journalctl --list-boots
List previous boots
journalctl -b -1
See journal from
the previous boot
(you can use boot
ID instead -1)
journalctl --utc -D
/var/log/journal/894062f9af204645a289e8016977fe6c
Use external
journal folder to
retrieve results
from
journalctl --utc --since "2023-10-15 18:00:00" --until
"2023-10-15 19:00:00" -D
/var/log/journal/894062f9af204645a289e8016977fe6c
Use time windows
for your logs
(format: YYYY-MM-
DD HH:MM:SS)
journalctl --utc --since "2023-10-15 18:00:00" --until
"2023-10-15 19:00:00" -D
/var/log/journal/894062f9af204645a289e8016977fe6c/ -u
httpd.service
Filter results by unit
(httpd.service as an
example)
journalctl --utc --since "2023-10-15 18:00:00" --until
"2023-10-15 19:00:00" -D
/var/log/journal/894062f9af204645a289e8016977fe6c/ -u
httpd.service _PID=27804
Filter results by
Process ID (PID)
journalctl /usr/bin/bash
Filter results by
executable
journalctl -p err --no-pager
Filter results by
priority
journalctl -o json-pretty
Output journalctl in
json or any other
formats