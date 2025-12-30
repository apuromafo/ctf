- **Splunk**: inverstigate web-based command injection attack
- Detect suspicious web requests
     1. Search Apache access logs for indicators like cmd.exe, PowerShell, and Invoke-Expression
     2. Identify command injection attempts througha vulnerable CGI script (hello.bat)

- Check Apache Error logs
- Sysmon logs -> to see what processes Apache spawned
- looking for cmd.exe running whoami -> confirms attacker gained interactive command execution
- Search for PowerShell using -EncodedCommand, enc, Base64 strings; If no results -> encoded payloads did not successfully execute


## Answers: 
- What is the reconnaissance executable file name? : `whoami.exe`
- What executable did the attacker attempt to run through the command injection? : `PowerShell.exe`
