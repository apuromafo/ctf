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


```
{
    "data": [
        {
            "id": 3173,
            "title": "Task 1",
            "description": "How many open TCP ports are listening on Devvortex?",
            "hint": "Start enumerating the host with `nmap`.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": null,
            "completed": false,
            "masked_flag": "number, such as 3, 17, or 4567",
            "options": []
        },
        {
            "id": 3174,
            "title": "Task 2",
            "description": "What subdomain is configured on the target's web server?",
            "hint": "When browsing to the web application, you are redirected to the devvortex.htb domain. Use a tool such as gobuster or ffuf to fuzz for common subdomains that respond differently.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3173,
            "completed": false,
            "masked_flag": "domain name",
            "options": []
        },
        {
            "id": 3175,
            "title": "Task 3",
            "description": "What Content Management System (CMS) is running on dev.devvortex.htb?",
            "hint": "Employ a fuzzer to perform a directory scan and discover potential endpoints and directories on the target web server. One endpoint will lead you to the entry point of the CMS.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3174,
            "completed": false,
            "masked_flag": "******",
            "options": []
        },
        {
            "id": 3176,
            "title": "Task 4",
            "description": "Which version of Joomla is running on the target system?",
            "hint": "Joomla websites publicly disclose their version on a certain endpoint. A quick search using your search engine of choice will lead you to it.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3175,
            "completed": false,
            "masked_flag": "*.*.*",
            "options": []
        },
        {
            "id": 3177,
            "title": "Task 5",
            "description": "What is the 2023 CVE ID for an information disclosure vulnerability in the version of Joomla running on DevVortex?",
            "hint": "Search for terms like \"joomla 4.2.6 information disclosure\".",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3176,
            "completed": false,
            "masked_flag": "***-****-*****",
            "options": []
        },
        {
            "id": 3178,
            "title": "Task 6",
            "description": "What is the lewis user's password for the CMS?",
            "hint": "Leverage the vulnerability to enumerate the service's configuration. There is a configuration endpoint that can be accessed using `?public=true` that will leak a password.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3177,
            "completed": false,
            "masked_flag": "********************",
            "options": []
        },
        {
            "id": 3179,
            "title": "Task 7",
            "description": "What table in the database contains hashed credentials for the logan user?",
            "hint": "Use the admin access to the CMS to write a PHP shell to one of the templates and obtain an interactive shell on the target. From there, enumerate the local services and use what you already know to access them.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3178,
            "completed": false,
            "masked_flag": "*****_*****",
            "options": []
        },
        {
            "id": 3180,
            "title": "Task 8",
            "description": "What is the logan user's password on DevVortex?",
            "hint": "Crack the hash from the database. It makes sense that logan might reuse the same password for Joomla and the host.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3179,
            "completed": false,
            "masked_flag": "*************",
            "options": []
        },
        {
            "id": 3181,
            "title": "Submit User Flag",
            "description": "Submit the flag located in the logan user's home directory.",
            "hint": null,
            "type": {
                "id": 1,
                "text": "user"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": null,
            "completed": true,
            "flag": "User flag owned",
            "flag_rating": 4,
            "masked_flag": "32 hex characters",
            "options": []
        },
        {
            "id": 3182,
            "title": "Task 10",
            "description": "What is the full path to the binary that the logan user can run with root privileges using `sudo`?",
            "hint": "`sudo -l` will show the configuration for the current user.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3181,
            "completed": false,
            "masked_flag": "full path of file",
            "options": []
        },
        {
            "id": 3183,
            "title": "Task 11",
            "description": "What is the 2023 CVE ID of the privilege escalation vulnerability in the installed version of apport-cli?",
            "hint": "First determine the tool's version, then research it to find the exploit and its assigned ID.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3182,
            "completed": false,
            "masked_flag": "***-****-****",
            "options": []
        },
        {
            "id": 3184,
            "title": "Submit Root Flag",
            "description": "Submit the flag located in the root user's home directory.",
            "hint": null,
            "type": {
                "id": 2,
                "text": "root"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": null,
            "completed": true,
            "flag": "Root flag owned",
            "flag_rating": 4,
            "masked_flag": "32 hex characters",
            "options": []
        }
    ]
}

```