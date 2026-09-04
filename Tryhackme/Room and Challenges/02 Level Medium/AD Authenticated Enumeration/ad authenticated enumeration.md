# AD Authenticated Enumeration [MEDIUM]

AD: Authenticated Enumeration
https://tryhackme.com/room/adauthenticatedenumeration

What flag must be set on an AD account for it to be vulnerable to AS-REP Roasting?
UF_DONT_REQUIRE_PREAUTH

Which tool automatically identifies roastable users without needing a username list?
Rubeus

What is the Hashcat mode used to crack AS-REP hashes?
18200

What is the password of the user asrepuser1?
qwerty123!

How many domain user accounts are there?
31

What is the full name of the user rduke?
Raoul Duke

How many local user accounts are there on the WRK machine?
5

How many domain groups are there?
21

What is the distinguishedName value of the asrepuser1 account?
CN=ASREPUSER1,CN=USERS,DC=TRYHACKME,DC=LOC

According to the "All Domain Admins" query, how many users are part of the Domain Admins group?
4

What is the type of relationship (edge) between the DRGONZ0 account and the DOMAIN ADMINS group?
MemberOf

How many computer accounts were you able to find?
2

How many groups did Get-DomainGroup "*admin*" return?
13

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
