---
type: Machine
target: Devvortex
flags: system, user
status: Pwned
---

# Machine: Devvortex

## Enumeration
- `nmap -sC -sV Devvortex`

## Exploitation
- User Flag: ✓
- System Flag: ✓



About
Devvortex is an easy-difficulty Linux machine that features a Joomla CMS that is vulnerable to information disclosure.
 Accessing the service&#039;s configuration file reveals plaintext credentials that lead to Administrative access to the Joomla instance.
 With administrative access, the Joomla template is modified to include malicious PHP code and gain a shell. 
 After gaining a shell and enumerating the database contents, hashed credentials are obtained, which are cracked and lead to SSH access to the machine. 
 Post-exploitation enumeration reveals that the user is allowed to run apport-cli as root, which is leveraged to obtain a root shell.
 
 

 ##Area of Interest
Web Application
Common Applications
Databases
 #Vulnerability
Weak Credentials
Information Disclosure
Misconfiguration
 #Technology
MySQL
Joomla
 #Technique
Reconnaissance
Web Site Structure Discovery
Configuration Analysis
Password Reuse
Password Cracking