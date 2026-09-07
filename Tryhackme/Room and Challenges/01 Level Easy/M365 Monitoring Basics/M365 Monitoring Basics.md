# M365 Monitoring Basics

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `m365monitoringbasics` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/m365monitoringbasics) |
| **Sección** | Cloud Monitoring |
| **Fuente** | THM |
| **Componentes** | Microsoft 365, Entra ID, sign-in logs, audit logs, Splunk |
| **Impacto** | Medium |

---

**Contexto:** Este room cubre los fundamentos del monitoreo en el ecosistema Microsoft 365, desde el rol de Entra ID como Identity Provider hasta la caza de amenazas en identidades cloud. Aprenderemos a rastrear inicios de sesión, registros de actividad y cambios en cuentas usando los sign-in logs y audit logs integrados, todo exportado a Splunk para análisis. El foco está en detectar compromisos de identidades usando evidencia real de logs.
**Learning chain:** Identity Providers → MFA → Logs → Sign-in Analysis → Audit Logs → Inbox Rules
**MITRE ATT&CK:** T1078.004 (Valid Accounts: Cloud Accounts), T1098 (Account Manipulation), T1114 (Email Collection)
**Fuente:** [TryHackMe - M365 Monitoring Basics](https://tryhackme.com/r/room/m365monitoringbasics)

---

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of application is Entra ID? | `Identity Provider` |
| 2 | What type of identity is a server account? | `Device` |
| 3 | What authentication resource can prevent attackers from authenticating with only a stolen password? | `MFA` |
| 4 | What can help us detect and monitor cloud identity threats? | `Logs` |

### Task 2: Compromised User - Sign-In Logs

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the email address of the compromised identity? | `allan.smith@finegalo.thm` |
| 2 | What is the IP address used by the attacker? | `2804:2488:7082:a4c0:fd97:b11b:9895:49c0` |
| 3 | What is the city of the IP address used by the attacker? | `Belo Horizonte` |
| 4 | When was the first successful sign-in in the compromised account after the failure attempts? (Exact Splunk Time value) | `2/11/26 6:16:53.000 PM` |

### Task 3: Compromised User - Audit Logs

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first application the attacker accessed after the office home page? | `One Outlook Web` |
| 2 | What was the first change made by the attacker in the compromised user account? | `User started security info registration` |
| 3 | What is the activityDisplayName that reveals all the details of the modified properties in a user? | `Update user` |
| 4 | What is the second change made in the account? | `Reset password (self-service)` |

### Task 4: Compromised User - Email Rules

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the application used by the attacker? | `Exchange` |
| 2 | What is the change made in the user application by the attacker? | `New-InboxRule` |
| 3 | What is the subject of the email message sent by the attacker? | `URGENT: Approval for new internal VPN Access` |
| 4 | When did the attacker access the response to the message? (Exact Splunk Time value) | `2/11/26 6:20:09.000 PM` |
| 5 | Which path was the response stored in? | `\Deleted Items` |

---

**Metodología:** El room sigue un escenario de compromiso completo: primero se identifica la identidad y el origen del ataque en sign-in logs, luego se analizan los audit logs para rastrear cambios en la cuenta (registro de MFA, reset de contraseña), y finalmente se examinan las reglas de correo (inbox rules) y tráfico de email para comprender el alcance del compromiso. Cada paso usa Splunk con la fuente M365 exportada.
