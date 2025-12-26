# Machine: Bizness
Flags obtained: system, user
Status: Pwned
 
 
##Area of Interest
Web Application
Common Applications
Databases

##Vulnerability
Weak Credentials
Remote Code Execution
Misconfiguration
Insecure Design

##Language
Python
Java

##Technology
NGINX
Apache OFBiz

##Technique
Reconnaissance
Web Site Structure Discovery
Configuration Analysis
Password Reuse
Password Cracking



Bizness is an easy Linux machine showcasing an Apache OFBiz pre-authentication, remote code execution (RCE) foothold, classified as [CVE-2023-49070](https://nvd.nist.gov/vuln/detail/CVE-2023-49070). The exploit is leveraged to obtain a shell on the box, where enumeration of the OFBiz configuration reveals a hashed password in the service's Derby database. Through research and little code review, the hash is transformed into a more common format that can be cracked by industry-standard tools. The obtained password is used to log into the box as the root user.

##Machine Changelog
Last Updated: 2 years ago

`March, 2024
`[~] Change
`Patch CVE-2024-1086
`Updated box to remove vulnerability to CVE-2024-1086.

`January, 2024
`[~] Change
`Removed Testing Artifact
`Removed testing artifact from the user's home directory that was causing confusion and leading people into a rabbit hole.
`

Info.26.12.2025