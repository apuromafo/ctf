# What is Privilege Escalation in Cyber Security?

**ID Original:** 6646282091ff6400019bdb07
**Slug:** what-is-privilege-escalation
--------------------

In this guide, we’ll discuss what you need to know about privilege escalation in cyber security and how, with TryHackMe, you can learn the fundamental techniques to elevate account privileges in Linux and Windows systems!Let’s get into it…
## What is privilege escalation?
Privilege escalation refers to the process in which a user gains higher levels of access or privileges within a computer system, network, or application. To be more specific, it's the exploitation of a vulnerability, design flaw, or configuration oversight in an operating system or application.Depending on the context, privilege escalation may grant you additional capabilities to:
* Reset passwords
* Bypass access controls to compromise protected data
* Edit software configurations
* Enable persistence
* Change the privilege of existing (or new) users
* Execute any administrative command
## What are privilege escalation attacks?
A privilege escalation attack refers to the exploitation of vulnerabilities or weaknesses in a system to gain higher levels of access or privileges than originally intended by the system's administrators or designers. These attacks typically involve an attacker starting with limited access to a system or network and then leveraging various techniques to potentially elevate their privileges to gain control over the entire system or network.Once an attacker gains elevated privileges, they can perform more damaging actions, such as installing malware, accessing sensitive data, modifying system configurations, and taking control of the entire system.Privilege escalation attacks can be carried out through various means, including exploiting vulnerabilities in the operating system or installed software, abusing misconfigurations, or tricking users or administrators into granting higher privileges unintentionally. Organisations often implement security measures such as least privilege principles, regular software updates, and access control mechanisms to mitigate the risk of privilege escalation attacks.
## Types of privilege escalation attacks
You might be wondering how privilege escalation works! To break things down, there are two main types of privilege escalation attacks: vertical and horizontal. How these privilege escalation attacks work will depend on the type. For example:
## Vertical Privilege Escalation:
Vertical privilege escalation occurs when an attacker with limited privileges seeks to obtain higher-level privileges within the same system. For example, a regular user might attempt to gain administrative privileges on a computer system. One of the common vertical privilege escalation techniques involves tactical social engineering, such as phishing emails, to trick users into granting access inadvertently or revealing sensitive information.
## Horizontal Privilege Escalation:
In this scenario, an attacker with a certain level of access to one system seeks to gain access to a similar level of privilege on another system. For instance, an attacker gaining access to resources from their HR department to snoop on payrolls! This could involve impersonating another user or accessing their privileges, and is a great example of privilege escalation.
## How to prevent privilege escalation attacks
Preventing privilege escalation attacks is crucial in maintaining the security and integrity of systems and networks. These attacks pose a significant threat as they allow malicious actors to gain unauthorised access to sensitive resources, escalate their privileges, and potentially wreak havoc within the system. By preventing privilege escalation, organisations can safeguard their data, protect user privacy, and maintain the trust of their customers and stakeholders. A comprehensive security strategy that combines preventive measures, user education, and proactive monitoring is essential for effectively preventing privilege escalation attacks. To go into more detail about how to prevent privilege escalation attacks, organisations should:
## Adopt a multi-layered approach to security
This includes implementing robust access control measures, such as the principle of least privilege, which limits user permissions to only what is necessary for their role.
## Regularly test systems
Preventive measures may be based on false ideas. Penetration testing allows you to put your controls to the test and likely identify other venues that weren't considered on the design of your security posture!
## Updates and patches
Regularly updating software and promptly patching known vulnerabilities is essential to prevent attackers from exploiting weaknesses in the system.
## Authentication methods
Employing strong authentication mechanisms like multi-factor authentication (MFA) can significantly reduce the risk of unauthorised access.
## Proactive monitoring
Proactive monitoring of system activity and the implementation of [intrusion detection systems](https://tryhackme.com/r/room/idsevasion?ref=blog.tryhackme.com) (IDS) can help identify and respond to potential threats before they escalate.
## Want to learn more about privilege escalation?
And there we have it! Want to learn more about privilege escalation and get hands-on with different privilege escalation techniques? In our [Privilege Escalation module](https://tryhackme.com/module/privilege-escalation?ref=blog.tryhackme.com), you’ll learn the fundamental techniques that will allow you to elevate account privileges through our interactive, hands-on content! We’ll cover both Windows privilege escalation and Linux privilege escalation.Launch Privilege Escalation moduleTo really put your skills to the test, our [Red Team Capstone Challenge Network](https://tryhackme.com/r/room/redteamcapstonechallenge?ref=blog.tryhackme.com) allows you to escalate your privileges in TryHackMe’s very own milestone challenge! This will include both local privilege escalation and AD privilege escalation through different tiers. In total, there are 20 flags for you to collect, spread across 10 different phases!Launch the Challenge Network!