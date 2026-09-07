# Entra ID Monitoring

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `entraidmonitoring` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/entraidmonitoring) |
| **Sección** | Cloud Monitoring |
| **Fuente** | THM |
| **Componentes** | Microsoft Entra ID, sign-in logs, audit logs, risky sign-ins, CAP |
| **Impacto** | Medium |

---

**Contexto:** Microsoft Entra ID (anteriormente Azure AD) es el directorio de identidad en la nube de Microsoft. Este room explora el monitoreo de eventos de inicio de sesión, riesgos de usuario, Conditional Access Policies y tráfico SOSPLA/MFA fatigue attacks. Se analizan logs de auditoría para detectar consent grants sospeososos y creación de cuentas backdoor por parte de un adversario.

## Solucionario

### Task 1: Password Spraying & Brute Force

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which IP address is performing a password spraying? | `94.20.222.248` |
| 2 | Which IP address is performing a throttling brute force? | `38.165.231.218` |
| 3 | What is the user's email address that was compromised? | `amanda.costa@finegalo.thm` |

### Task 2: Risky Users

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user email address that is at risk in the tenant? | `allan.senna@finegalo.thm` |
| 2 | When was the last risky sign-in attempt from this risky user? | `2026-03-03 13:51:00.569` |
| 3 | What is the type of risk identified during this risky user sign-in based on risk detection logs? | `anonymizedIPAddress` |

### Task 3: Conditional Access Policy

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the CAP policy that was enforced and blocked some sign-in attempts from this risky user? | `Block Suspicious Countries` |
| 2 | What was the IP address that was blocked from signing in this risky user? | `94.20.222.251` |

### Task 4: MFA Fatigue Attack

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which user was the target of an MFA fatigue attack? | `igor.bicalho@finegalo.thm` |
| 2 | What is the error code of the failed MFA prompts? | `500121` |
| 3 | What is the country code that the user normally signs in before the attack? | `DK` |
| 4 | When does the attacker successfully authenticate in the user account? | `2026-03-04 13:26:22` |

### Task 5: Backdoor Account & Application Consent

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user email address that the attacker created? | `rafael.maciel@finegalo.thm` |
| 2 | Which role was assigned to this new account? | `Global Administrator` |
| 3 | When did the attacker add a new MFA device? | `2026-03-04 13:36:58` |
| 4 | Which permission allows an application to read all mailboxes within a tenant? | `Mail.Read.All` |
| 5 | What is the activityDisplayName value you use to track all consent grants to applications within Entra ID audit logs? | `Consent to application` |

---

**Metodología:** Se analizan sign-in logs y audit logs de Microsoft Entra ID para rastrear un ataque completo: desde password spraying y brute force, pasando por la evaluación de riesgos de usuario y CAP enforcement, hasta la detección de un ataque MFA fatigue, creación de cuenta backdoor con Global Administrator y consent grants maliciosos para persistent access.
**Learning chain:** Sign-in logs → Risk detection → Conditional Access Policies → MFA fatigue attacks → Audit logs → Consent grants → Backdoor accounts
**MITRE ATT&CK:** T1110.003 - Password Spraying, T1621 - Multi-Factor Authentication Request Generation, T1136.003 - Cloud Account, T1098.003 - Additional Cloud Roles, T1550 - Use Alternate Authentication Material
**Fuente:** [TryHackMe - Entra ID Monitoring](https://tryhackme.com/r/room/entraidmonitoring)
