1, Enumerate the ports and services
22/tcp ssh
80/tcp http
8065/tcp unknown(http)

exited domain and sub-domain
`delivery.htb helpdesk.delivery.htb`

2, enumerate the pages and web-contents
1. `http://helpdesk.delivery.htb`  # Welcome to the Support Center and powered by `osTicket`  we guess this would be exploited.
	`osTicket 1.14.2 - SSRF`
	`osTicket 1.10.1 - Arbitrary File Upload`
	
1. `http://delivery.htb:8065/login` # `Mattermost` There is a login page to the dashboard.

This is an instance of osTicket:
![](images/Pasted%20image%2020240831105618.png)

As a guest user, I can create a ticket:
![](images/Pasted%20image%2020240831105632.png)

And it will give me a page saying it’s been accepted:
![](images/Pasted%20image%2020240831105644.png)

The email to add to the ticket is interesting. I’ll note that.

The Sign In link has a form, as well as a registration link:
![](images/Pasted%20image%2020240831105705.png)

On clicking “Create an account” and filling out the form, it gives me a page that says a link has been sent to the email to activate it. On HTB, that’s basically a deadend. If I try to log in, it returns this error:
![](images/Pasted%20image%2020240831105718.png)
If I click the Check Ticket Status link, it asks for an email or ticket number. Because no validation was done of my email when submitting a ticket as a Guest User, I can enter that email and ticket number:

![](images/Pasted%20image%2020240831105731.png)

This page gives the current ticket, with the option to update it:
![](images/Pasted%20image%2020240831105743.png)

delivery.htb - TCP 8065
The main page here is a login form:
![](images/Pasted%20image%2020240831105810.png)

The create account link leads to another form:

![](images/Pasted%20image%2020240831105822.png)

Submitting also leads to an email confirmation step:
![](images/Pasted%20image%2020240831105832.png)
Without an email address, not much I can do here.

In this place, I would try to use the helper contact email, then we can successfully login to the chat group:
![](images/Pasted%20image%2020240831105958.png)

And also, we get the credits
`maildeliverer:Youve_G0t_Mail!`

3,shell as user and root
By check `sudo -l`
`Sorry, user maildeliverer may not run sudo on Delivery.`

Let's check the mattermost config
```
"SqlSettings": {
        "DriverName": "mysql",
        "DataSource": "mmuser:Crack_The_MM_Admin_PW@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s",
        "DataSourceReplicas": [],
        "DataSourceSearchReplicas": [],
        "MaxIdleConns": 20,
        "ConnMaxLifetimeMilliseconds": 3600000,
        "MaxOpenConns": 300,
        "Trace": false,
        "AtRestEncryptKey": "n5uax3d4f919obtsp1pw1k5xetq1enez",
        "QueryTimeout": 30,
        "DisableDatabaseSearch": false
    }
```
And we get the database credit
`mmuser:Crack_The_MM_Admin_PW`

Enumerate the database and we get the password of root
`root:$2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO`

From the comment of root
`PleaseSubscribe! may not be in RockYou but if any hacker manages to get our hashes, they can use hashcat rules to easily crack all variations of common words or phrases.`

`hashcat -m 3200 hash password --user -r /usr/share/hashcat/rules/best64.rule `
By cracking it, we get `PleaseSubscribe!21`

Then just su root.
