# Enumerating Active Directory

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Free) | **Slug** | `adenumeration` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adenumeration) | **Sección** | 02 Level Medium | **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Credential Injection / runas / MMC / SYSVOL / BloodHound / Sharphound / LDAP / Kerberos | **Impacto** | Enseña a enumerar AD sin volcar el directorio completo, usando herramientas nativas y BloodHound |

---

**Contexto:** Esta sala enseña a enumerar un entorno de Active Directory sin volcar el directorio completo, usando herramientas nativas como runas, MMC, BloodHound/Sharphound y consultas LDAP para mapear usuarios, grupos, OUs y rutas de ataque. This room teaches how to enumerate an Active Directory environment without dumping the directory, using built-in tools like runas, MMC, BloodHound/Sharphound and LDAP queries to map users, groups, OUs and attack paths.

## Solucionario

### Task 1: Credential Injection

**Explicación:** Se inyectan credenciales legítimamente en memoria usando `runas.exe`. El parámetro `/netonly` de la herramienta runas asegura que las credenciales inyectadas se usen para todas las conexiones de red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What native Windows binary allows us to inject credentials legitimately into memory? | `runas.exe` |
| 2 | What parameter option of the runas binary will ensure that the injected credentials are used for all network connections? | `/netonly` |

### Task 2: Enumerating with Built-in Tools

**Explicación:** Se accede al SYSVOL del controlador de dominio mediante autenticación Kerberos para revisar información de GPOs, y se usan herramientas como MMC/ADUC para enumerar computadoras, OUs, departamentos y tiers administrativos. SYSVOL es la carpeta de red en un DC accesible por cualquier cuenta AD autenticada que almacena información de GPO. Al ejecutar `dir \\za.tryhackme.com\SYSVOL` el tipo de autenticación por defecto es Kerberos. La organización tiene 2 Computer objects en la OU Servers, 1 en la OU Workstations, 7 departamentos, 3 Admin tiers. El flag en el atributo description de t0_tinus.green es THM{Enumerating.Via.MMC}. El grupo Internet Access (además de Domain Users) incluye a aaron.harris. La cuenta Guest no está activa (Nay). 7 cuentas son miembros de Tier 1 Admins.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What network folder on a domain controller is accessible by any authenticated AD account and stores GPO information? | `SYSVOL` |
| 2 | When performing dir \\za.tryhackme.com\SYSVOL, what type of authentication is performed by default? | `Kerberos Authentication` |
| 3 | How many Computer objects are part of the Servers OU? | `2` |
| 4 | How many Computer objects are part of the Workstations OU? | `1` |
| 5 | How many departments (Organisational Units) does this organisation consist of? | `7` |
| 6 | How many Admin tiers does this organisation have? | `3` |
| 7 | What is the value of the flag stored in the description attribute of the t0_tinus.green account? | `THM{Enumerating.Via.MMC}` |
| 8 | Apart from the Domain Users group, what other group is the aaron.harris account a member of? | `Internet Access` |
| 9 | Is the Guest account active? (Yay,Nay) | `Nay` |
| 10 | How many accounts are a member of the Tier 1 Admins group? | `7` |

### Task 3: Policy & Account Attributes

**Explicación:** Se revisan la política de contraseñas, atributos de cuentas (Title, DistinguishedName, SID), fechas de creación de grupos y el contenedor de objetos eliminados mediante consultas LDAP. El lockout duration de la política de contraseñas es de 30 minutos. El atributo Title de Beth Nolan es "Senior". El DistinguishedName de Annette Manning es `CN=annette.manning,OU=Marketing,OU=People,DC=za,DC=tryhackme,DC=com`. El grupo Tier 2 Admins fue creado el 2/24/2022 10:04:41 PM. El SID de Enterprise Admins es `S-1-5-21-3330634377-1326264276-632209373-519`. El contenedor de objetos AD eliminados es `CN=Deleted Objects,DC=za,DC=tryhackme,DC=com`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the account lockout duration of the current password policy in minutes? | `30` |
| 2 | What is the value of the Title attribute of Beth Nolan (beth.nolan)? | `Senior` |
| 3 | What is the value of the DistinguishedName attribute of Annette Manning (annette.manning)? | `CN=annette.manning,OU=Marketing,OU=People,DC=za,DC=tryhackme,DC=com` |
| 4 | When was the Tier 2 Admins group created? | `2/24/2022 10:04:41 PM` |
| 5 | What is the value of the SID attribute of the Enterprise Admins group? | `S-1-5-21-3330634377-1326264276-632209373-519` |
| 6 | Which container is used to store deleted AD objects? | `CN=Deleted Objects,DC=za,DC=tryhackme,DC=com` |

### Task 4: Enumerating with BloodHound

**Explicación:** Se ejecuta Sharphound para recolectar información de sesiones y rutas de ataque, y se analiza el grafo en BloodHound para detectar cuentas kerberoastables y acceso administrativo de los grupos de Tier 1 y Tier 2. El comando para ejecutar Sharphound.exe recuperando solo información de sesiones del dominio za.tryhackme.com sin tocar DCs es `Sharphound.exe --CollectionMethods Session --Domain za.tryhackme.com --ExcludeDCs`. Aparte de krbtgt, hay 4 cuentas potencialmente kerberoastables. 2 máquinas tienen acceso administrativo los miembros de Tier 1 Admins. 15 usuarios son miembros de Tier 2 Admins.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command can be used to execute Sharphound.exe and request that it recovers Session information only from the za.tryhackme.com domain without touching domain controllers? | `Sharphound.exe --CollectionMethods Session --Domain za.tryhackme.com --ExcludeDCs` |
| 2 | Apart from the krbtgt account, how many other accounts are potentially kerberoastable? | `4` |
| 3 | How many machines do members of the Tier 1 Admins group have administrative access to? | `2` |
| 4 | How many users are members of the Tier 2 Admins group? | `15` |

---

**Metodología:**
1. Se inyectan credenciales legítimamente en memoria usando runas.exe con el parámetro /netonly para forzar su uso en todas las conexiones de red.
2. Se accede al SYSVOL del controlador de dominio mediante autenticación Kerberos para revisar información de GPOs, y se usan herramientas como MMC/ADUC para enumerar computadoras, OUs, departamentos y tiers administrativos.
3. Se revisan la política de contraseñas, atributos de cuentas (Title, DistinguishedName, SID), fechas de creación de grupos y el contenedor de objetos eliminados mediante consultas LDAP.
4. Se ejecuta Sharphound para recolectar información de sesiones y rutas de ataque, y se analiza el grafo en BloodHound para detectar cuentas kerberoastables y acceso administrativo de los grupos de Tier 1 y Tier 2.

**Learning chain:** runas /netonly → Acceso a SYSVOL vía Kerberos → Enumeración de OUs y grupos con MMC/LDAP → Revisión de política de contraseñas y atributos → Ejecución de Sharphound → Análisis en BloodHound → Identificación de cuentas kerberoastables y rutas de ataque

**Lección:** *La enumeración de Active Directory se puede realizar de forma sigilosa y completa sin volcar todo el directorio, usando runas para inyectar credenciales, herramientas nativas para inspeccionar OUs/grupos y BloodHound para mapear rutas de ataque y abusos de permisos.*

**MITRE ATT&CK:** T1069.002 (Permission Groups Discovery: Domain Groups), T1087.002 (Account Discovery: Domain Account), T1018 (Remote System Discovery), T1558.003 (Steal or Forge Kerberos Tickets: Kerberoasting)

**CWE:** CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor)

**Fuente:** [TryHackMe - Enumerating Active Directory](https://tryhackme.com/room/adenumeration)
