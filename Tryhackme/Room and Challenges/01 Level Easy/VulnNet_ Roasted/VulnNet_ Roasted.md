# VulnNet_ Roasted

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `vulnnetroasted` | [TryHackMe](https://tryhackme.com/room/vulnnetroasted) | 01 Level Easy | THM | Windows AD, ASREP roasting, Kerberoasting, crackmapexec, password spraying, AD enumeration, Impacket | Resolución completa del reto |

---

**Contexto:** Box Windows con Active Directory. El reto está enfocado al AS-REP roasting: se descubren todas las cuentas del dominio con pre-autenticación Kerberos deshabilitada, se obtienen sus hashes ASREP, se crackean y se compromete el dominio. Esto da acceso al sistema y permite capturar las flags Desktop\user.txt y Desktop\system.txt.

> **ES:** Box Windows/AD: enumeración del dominio, AS-REP roasting para recopilar hashes ASREP de cuentas sin pre-autenticación, crackeo de hashes y acceso al sistema; flags Desktop\user.txt y Desktop\system.txt.
> **EN:** Windows/AD box: domain enumeration, AS-REP roasting to collect ASREP hashes from accounts with pre-authentication disabled, hash cracking and system access; Desktop\user.txt and Desktop\system.txt flags.

## Solucionario

### Task 1: Encuentra las flags / Find the flags

**Explicación:** Se aplican técnicas de ataque a Kerberos (AS-REP roasting y, complementariamente, Kerberoasting) para obtener hashes de cuentas del dominio Active Directory. Tras crackear los hashes se consigue acceso al sistema y se recuperan las flags de la raíz del escritorio del usuario comprometido.

1. `THM{726b7c0baaac1455d05c827b5561f4ed}`
2. `THM{16f45e3934293a57645f8d7bf71d8d4c}`

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the user flag? | `THM{726b7c0baaac1455d05c827b5561f4ed}` |
| 2 | What is the system flag? | `THM{16f45e3934293a57645f8d7bf71d8d4c}` |

---

**Metodología:** nmap → enumeración AD (LDAP, RPC, DNS) → AS-REP roasting (GetNPUsers/Impacket) sobre cuentas sin pre-autenticación → crackeo de hashes ASREP (hashcat/john) → acceso al sistema (crackmapexec/password spraying) → flags en el escritorio del usuario comprometido.

### Cadena de ataque / Attack Chain

Reconocimiento (AD: DNS, LDAP, RPC) → Enumeración de cuentas de dominio → AS-REP roasting (GetNPUsers.py) → Crackeo de hashes ASREP → Acceso al sistema (SMB/WinRM) → Lectura de Desktop\user.txt y Desktop\system.txt

**Learning chain:** Active Directory enumeration → Kerberos attacks (AS-REP roasting) → hash cracking → domain access → flags

**Lección:** *Las cuentas de dominio con pre-autenticación Kerberos deshabilitada o con Kerberoasting son un vector clásico de compromiso de AD: sin más que la capacidad de pedir tickets se obtienen hashes que, con contraseñas débiles, se crackean y dan acceso al dominio.*

**MITRE ATT&CK:** T1558.004 (Steal or Forge Kerberos Tickets: AS-REP Roasting), T1558.003 (Kerberoasting), T1078 (Valid Accounts), T1087.002 (Account Discovery: Domain Account), T1110 (Brute Force)

**Fuente:** [TryHackMe - VulnNet: Roasted](https://tryhackme.com/room/vulnnetroasted)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.