# Enumerating Active Directory [MEDIUM]

https://tryhackme.com/room/adenumeration

answers




What native Windows binary allows us to inject credentials legitimately into memory?
><details><summary>Click for answer</summary>runas.exe</details>

What parameter option of the runas binary will ensure that the injected credentials are used for all network connections?
><details><summary>Click for answer</summary>/netonly</details>

What network folder on a domain controller is accessible by any authenticated AD account and stores GPO information?
><details><summary>Click for answer</summary>SYSVOL</details>

When performing dir \\za.tryhackme.com\SYSVOL, what type of authentication is performed by default?
><details><summary>Click for answer</summary>Kerberos Authentication</details>

How many Computer objects are part of the Servers OU?
><details><summary>Click for answer</summary>2</details>

How many Computer objects are part of the Workstations OU?
><details><summary>Click for answer</summary>1</details>

How many departments (Organisational Units) does this organisation consist of?
><details><summary>Click for answer</summary>7</details>

How many Admin tiers does this organisation have?
><details><summary>Click for answer</summary>3</details>

What is the value of the flag stored in the description attribute of the t0_tinus.green account?
><details><summary>Click for answer</summary>THM{Enumerating.Via.MMC}</details>

Apart from the Domain Users group, what other group is the aaron.harris account a member of?
><details><summary>Click for answer</summary>Internet Access</details>

Is the Guest account active? (Yay,Nay)
><details><summary>Click for answer</summary>Nay</details>

How many accounts are a member of the Tier 1 Admins group?
><details><summary>Click for answer</summary>7</details>

What is the account lockout duration of the current password policy in minutes?
><details><summary>Click for answer</summary>30</details>

What is the value of the Title attribute of Beth Nolan (beth.nolan)?
><details><summary>Click for answer</summary>Senior</details>

What is the value of the DistinguishedName attribute of Annette Manning (annette.manning)?
><details><summary>Click for answer</summary>CN=annette.manning,OU=Marketing,OU=People,DC=za,DC=tryhackme,DC=com</details>

When was the Tier 2 Admins group created?
><details><summary>Click for answer</summary>2/24/2022 10:04:41 PM</details>

What is the value of the SID attribute of the Enterprise Admins group?
><details><summary>Click for answer</summary>S-1-5-21-3330634377-1326264276-632209373-519</details>

Which container is used to store deleted AD objects?
><details><summary>Click for answer</summary>CN=Deleted Objects,DC=za,DC=tryhackme,DC=com</details>

What command can be used to execute Sharphound.exe and request that it recovers Session information only from the za.tryhackme.com domain without touching domain controllers?
><details><summary>Click for answer</summary>Sharphound.exe --CollectionMethods Session --Domain za.tryhackme.com --ExcludeDCs</details>

Apart from the krbtgt account, how many other accounts are potentially kerberoastable?
><details><summary>Click for answer</summary>4</details>

How many machines do members of the Tier 1 Admins group have administrative access to?
><details><summary>Click for answer</summary>2</details>

How many users are members of the Tier 2 Admins group?
><details><summary>Click for answer</summary>15</details>
