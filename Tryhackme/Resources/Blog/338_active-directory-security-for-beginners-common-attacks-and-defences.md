# Active Directory Security for Beginners: Common Attacks and Defences

**ID Original:** no disponible
**Slug:** active-directory-security-for-beginners-common-attacks-and-defences
--------------------

Active Directory (AD) is the identity backbone of the vast majority of enterprise Windows environments. It controls who can log in, what they can access, and how machines on the network trust each other. That central role is also what makes it the most consistently targeted system in enterprise breaches. According to the Verizon 2025 Data Breach Investigations Report , 74% of breaches involved compromised credentials or identity abuse, and the majority of those attacks moved through or against Active Directory.
For anyone learning cyber security, understanding how AD attacks work is not optional. Whether your path leads toward penetration testing, defensive security, or SOC analysis, you will encounter Active Directory constantly. This guide covers the four most commonly seen attacks, how each one works at a technical level a beginner can follow, and what defenders do to detect and stop them.
What Active Directory does, and why attackers target it
Active Directory stores and manages user accounts, computer accounts, and the relationships between them. When a user logs into a Windows workstation on a corporate network, AD authenticates them. When they try to access a shared drive or internal application, AD checks whether they have permission. Every privilege, every group membership, and every trust relationship in the environment is recorded there.
Attackers target AD because compromise of the right account unlocks everything. A domain administrator account has unrestricted access to every machine, every file share, and every system joined to the domain. Even a low-privileged domain user account is enough to start an attack, because the protocols AD relies on give authenticated users the ability to query the directory and request tickets. That is where most of the attacks below begin.
Why it matters for learners: AD attacks appear in almost every real-world penetration test and a significant proportion of actual breaches. Learning this material is not theoretical prep: it maps directly onto what employers test for in SOC analyst and junior pentester interviews.
Attack 01 Kerberoasting
Kerberos is the authentication protocol Active Directory uses for service accounts. When a domain user needs to access a service (a database, a web application, a file server), they request a service ticket from a domain controller. That ticket is encrypted using a hash derived from the service account's password.
Kerberoasting exploits the fact that any authenticated domain user can request these service tickets. An attacker with even a low-privilege domain account uses a tool like Rubeus or Impacket's GetUserSPNs.py to request tickets for every service account they can find, then takes those tickets offline and runs a password cracking tool against them.
The attack is particularly effective against service accounts with weak passwords and against accounts still using RC4 encryption rather than AES. Microsoft's own guidance on Kerberoasting notes that RC4 tickets are significantly easier to crack because the key derivation does not include a salt, allowing attackers to test password guesses much faster. RC4 is being deprecated in Windows Server 2025 and Windows 11 24H2, but many environments remain exposed today.
In 2024, the Ascension Health ransomware incident was traced partly to Kerberoasting against a service account using RC4 encryption. The breach affected 140 hospitals and exposed records for millions of patients.
Defences: Migrate service accounts to Group Managed Service Accounts (gMSA), which have 240-character auto-rotated passwords that cannot be cracked in any practical timeframe. For accounts that cannot be migrated, enforce 25+ character passwords and disable RC4. Monitor Windows Event ID 4769 for unusual volumes of service ticket requests.
Practise this on TryHackMe: Attacking Kerberos
Attack 02 Pass-the-Hash
Windows stores credentials as NTLM hashes in a process called LSASS (Local Security Authority Subsystem Service). When an attacker gains administrative access to a machine, they can use a tool like Mimikatz to dump those hashes from memory. They do not need to crack the hash to use it: the NTLM authentication protocol accepts the hash directly as proof of identity.
Pass-the-Hash (PtH) means the attacker can authenticate to any other system on the network where that account is valid, using nothing but the hash. A local administrator account that reuses the same password across workstations (a very common misconfiguration) turns a single compromised machine into access to dozens. This is how attackers move laterally through an environment after their initial foothold.
The technique has been known since 1997 but remains effective today because NTLM is still widely enabled as a fallback authentication method, and because credential reuse across machines is common.
Defences: Enable Credential Guard on Windows 10/11 endpoints to protect LSASS memory. Deploy Microsoft LAPS to ensure every machine has a unique local administrator password, eliminating the lateral movement path. Restrict NTLM where possible and prefer Kerberos. Segment administrative workstations from regular user machines.
Practise this on TryHackMe: Lateral Movement and Pivoting
Attack 03 LLMNR and NBT-NS Poisoning
Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are fallback name resolution protocols that Windows uses when DNS fails to resolve a hostname. When a machine cannot find a resource by name, it broadcasts a query to the local network asking if anyone knows the address.
An attacker running a tool like Responder on the same network segment can respond to those broadcasts, impersonating the requested resource. The victim's machine then sends its credentials (in the form of an NTLM hash) to the attacker in an attempt to authenticate. The attacker captures the hash and either cracks it offline or relays it directly to another service.
This attack requires no prior credentials and no special access. A laptop plugged into a corporate network and running Responder is enough to begin harvesting hashes from any machine that makes a failed DNS lookup. It is one of the first techniques taught in internal network penetration testing for exactly that reason.
Defences: Disable LLMNR via Group Policy (Computer Configuration > Administrative Templates > Network > DNS Client > Turn off Multicast Name Resolution). Disable NBT-NS through network adapter settings or DHCP options. Enforce SMB signing to prevent relay attacks even when hashes are captured.
Practise this on TryHackMe: Breaching Active Directory
Attack 04 BloodHound Enumeration and Privilege Path Mapping
BloodHound is a tool that maps the relationships between users, groups, computers, and permissions inside Active Directory using graph theory. It ingests data collected by a companion tool called SharpHound, then visualises attack paths: the shortest route from a compromised account to Domain Admin, expressed as a chain of permissions and group memberships.
An attacker who has gained any domain user account can run SharpHound to collect the data, then load it into BloodHound to find paths that would not be obvious from manual inspection. A user might be a member of a group that has GenericWrite permissions on another group, whose members have local admin rights on a machine where a privileged account has an active session. BloodHound surfaces that chain in seconds.
What makes this particularly relevant for defenders is that BloodHound is equally useful for the blue team. Running it defensively, before attackers do, reveals the same paths and allows administrators to close them proactively.
Defences: Run BloodHound regularly in your own environment to identify and remediate dangerous privilege paths. Detect SharpHound collection activity via EDR telemetry (large volumes of LDAP queries in a short window). Clean up stale group memberships, remove unnecessary delegation settings, and apply the principle of least privilege to service accounts.
Practise this on TryHackMe: BloodHound (Community Edition)
Defence summary
The controls that address the attacks above overlap significantly. Most AD attacks succeed because of the same small set of misconfigurations: NTLM enabled where it is not needed, legacy protocols like LLMNR and RC4 left on by default, service account passwords that are weak or never rotated, and privilege paths that have grown organically over years without being audited.
Attack
Primary defences
Kerberoasting
gMSA for service accounts, disable RC4, enforce long passwords, monitor Event ID 4769
Pass-the-Hash
Credential Guard, LAPS for unique local admin passwords, restrict NTLM
LLMNR Poisoning
Disable LLMNR and NBT-NS via Group Policy, enforce SMB signing
BloodHound Recon
Run BloodHound defensively, clean up privilege paths, monitor LDAP enumeration volume
A consistent theme across all four attacks is that they exploit configuration choices rather than unpatched vulnerabilities. The Kerberoasting attack works because RC4 is still enabled. Pass-the-Hash works because NTLM is still available. LLMNR poisoning works because a 30-year-old fallback protocol is switched on by default. None of these require a zero-day. They require a misconfigured environment and a patient attacker.
Learn and practise Active Directory attacks on TryHackMe TryHackMe's Hacking Active Directory module covers enumeration, exploitation, lateral movement, and privilege escalation in a fully browser-based lab environment. No local AD lab required.

---
**Fuente / Source:** [active-directory-security-for-beginners-common-attacks-and-defences](https://tryhackme.com/resources/blog/active-directory-security-for-beginners-common-attacks-and-defences)
