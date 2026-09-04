# Enumerating Active Directory [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `adenumeration`
* **Link:** https://tryhackme.com/room/adenumeration
* **Sección / Section:** Windows / Active Directory
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala enseña a enumerar un entorno de Active Directory sin volcar el directorio completo, usando herramientas nativas como runas, MMC, BloodHound/Sharphound y consultas LDAP para mapear usuarios, grupos, OUs y rutas de ataque.
> **EN:** This room teaches how to enumerate an Active Directory environment without dumping the directory, using built-in tools like runas, MMC, BloodHound/Sharphound and LDAP queries to map users, groups, OUs and attack paths.

---

### Task 1 — Inyección de Credenciales / Credential Injection

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What native Windows binary allows us to inject credentials legitimately into memory? | `runas.exe` |
| What parameter option of the runas binary will ensure that the injected credentials are used for all network connections? | `/netonly` |

---

### Task 2 — Enumeración con Herramientas Nativas / Enumerating with Built-in Tools

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What network folder on a domain controller is accessible by any authenticated AD account and stores GPO information? | `SYSVOL` |
| When performing dir \\za.tryhackme.com\SYSVOL, what type of authentication is performed by default? | `Kerberos Authentication` |
| How many Computer objects are part of the Servers OU? | `2` |
| How many Computer objects are part of the Workstations OU? | `1` |
| How many departments (Organisational Units) does this organisation consist of? | `7` |
| How many Admin tiers does this organisation have? | `3` |
| What is the value of the flag stored in the description attribute of the t0_tinus.green account? | `THM{Enumerating.Via.MMC}` |
| Apart from the Domain Users group, what other group is the aaron.harris account a member of? | `Internet Access` |
| Is the Guest account active? (Yay,Nay) | `Nay` |
| How many accounts are a member of the Tier 1 Admins group? | `7` |

---

### Task 3 — Política y Atributos de Cuentas / Policy & Account Attributes

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the account lockout duration of the current password policy in minutes? | `30` |
| What is the value of the Title attribute of Beth Nolan (beth.nolan)? | `Senior` |
| What is the value of the DistinguishedName attribute of Annette Manning (annette.manning)? | `CN=annette.manning,OU=Marketing,OU=People,DC=za,DC=tryhackme,DC=com` |
| When was the Tier 2 Admins group created? | `2/24/2022 10:04:41 PM` |
| What is the value of the SID attribute of the Enterprise Admins group? | `S-1-5-21-3330634377-1326264276-632209373-519` |
| Which container is used to store deleted AD objects? | `CN=Deleted Objects,DC=za,DC=tryhackme,DC=com` |

---

### Task 4 — Enumeración con BloodHound / Enumerating with BloodHound

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What command can be used to execute Sharphound.exe and request that it recovers Session information only from the za.tryhackme.com domain without touching domain controllers? | `Sharphound.exe --CollectionMethods Session --Domain za.tryhackme.com --ExcludeDCs` |
| Apart from the krbtgt account, how many other accounts are potentially kerberoastable? | `4` |
| How many machines do members of the Tier 1 Admins group have administrative access to? | `2` |
| How many users are members of the Tier 2 Admins group? | `15` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Se inyectan credenciales legítimamente en memoria usando runas.exe con el parámetro /netonly para forzar su uso en todas las conexiones de red.
2. **Paso 2 / Step 2:** Se accede al SYSVOL del controlador de dominio mediante autenticación Kerberos para revisar información de GPOs, y se usan herramientas como MMC/ADUC para enumerar computadoras, OUs, departamentos y tiers administrativos.
3. **Paso 3 / Step 3:** Se revisan la política de contraseñas, atributos de cuentas (Title, DistinguishedName, SID), fechas de creación de grupos y el contenedor de objetos eliminados mediante consultas LDAP.
4. **Paso 4 / Step 4:** Se ejecuta Sharphound para recolectar información de sesiones y rutas de ataque, y se analiza el grafo en BloodHound para detectar cuentas kerberoastables y acceso administrativo de los grupos de Tier 1 y Tier 2.

### Cadena de ataque / Attack Chain

```
runas /netonly → Acceso a SYSVOL vía Kerberos → Enumeración de OUs y grupos con MMC/LDAP → Revisión de política de contraseñas y atributos → Ejecución de Sharphound → Análisis en BloodHound → Identificación de cuentas kerberoastables y rutas de ataque
```

**Lección:** La enumeración de Active Directory se puede realizar de forma sigilosa y completa sin volcar todo el directorio, usando runas para inyectar credenciales, herramientas nativas para inspeccionar OUs/grupos y BloodHound para mapear rutas de ataque y abusos de permisos.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
