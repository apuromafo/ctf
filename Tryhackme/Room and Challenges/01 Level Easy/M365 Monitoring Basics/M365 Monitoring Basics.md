# M365 Monitoring Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `m365monitoringbasics` | [TryHackMe](https://tryhackme.com/room/m365monitoringbasics) | Cloud Monitoring | TryHackMe | Microsoft 365, Entra ID, sign-in logs, audit logs, Splunk | Detección de compromisos de identidades cloud mediante sign-in logs y audit logs exportados a Splunk |

---

**Contexto:** Este room cubre los fundamentos del monitoreo en el ecosistema Microsoft 365, desde el rol de Entra ID como Identity Provider hasta la caza de amenazas en identidades cloud. Aprenderemos a rastrear inicios de sesión, registros de actividad y cambios en cuentas usando los sign-in logs y audit logs integrados, todo exportado a Splunk para análisis. El foco está en detectar compromisos de identidades usando evidencia real de logs.
**Learning chain:** Identity Providers → MFA → Logs → Sign-in Analysis → Audit Logs → Inbox Rules
**MITRE ATT&CK:** T1078.004 (Valid Accounts: Cloud Accounts), T1098 (Account Manipulation), T1114 (Email Collection)
**Fuente:** [TryHackMe - M365 Monitoring Basics](https://tryhackme.com/r/room/m365monitoringbasics)

---

## Solucionario

### Task 1: Introduction

**Explicación:** Se introducen los conceptos base del monitoreo en Microsoft 365: el papel de Entra ID como Identity Provider, los tipos de identidad y los recursos de autenticación y detección (MFA y Logs) que previenen compromisos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of application is Entra ID? | `Identity Provider` |
| 2 | What type of identity is a server account? | `Device` |
| 3 | What authentication resource can prevent attackers from authenticating with only a stolen password? | `MFA` |
| 4 | What can help us detect and monitor cloud identity threats? | `Logs` |

### Task 2: Compromised User - Sign-In Logs

**Explicación:** Se analizan los sign-in logs del usuario comprometido para identificar la identidad afectada, la dirección IP del atacante, la ubicación geográfica de origen y el momento exacto del primer inicio de sesión exitoso tras los intentos fallidos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the email address of the compromised identity? | `allan.smith@finegalo.thm` |
| 2 | What is the IP address used by the attacker? | `2804:2488:7082:a4c0:fd97:b11b:9895:49c0` |
| 3 | What is the city of the IP address used by the attacker? | `Belo Horizonte` |
| 4 | When was the first successful sign-in in the compromised account after the failure attempts? (Exact Splunk Time value) | `2/11/26 6:16:53.000 PM` |

### Task 3: Compromised User - Audit Logs

**Explicación:** Se examinan los audit logs para reconstruir las acciones del atacante sobre la cuenta comprometida: la primera aplicación accedida, el registro de seguridad, la actividad de actualización de usuario y el cambio de contraseña.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first application the attacker accessed after the office home page? | `One Outlook Web` |
| 2 | What was the first change made by the attacker in the compromised user account? | `User started security info registration` |
| 3 | What is the activityDisplayName that reveals all the details of the modified properties in a user? | `Update user` |
| 4 | What is the second change made in the account? | `Reset password (self-service)` |

### Task 4: Compromised User - Email Rules

**Explicación:** Se investiga la persistencia del atacante mediante reglas de bandeja de entrada: la aplicación utilizada, el cambio `New-InboxRule`, el asunto del correo, el momento de acceso a la respuesta y la carpeta donde esta se almacenó.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the application used by the attacker? | `Exchange` |
| 2 | What is the change made in the user application by the attacker? | `New-InboxRule` |
| 3 | What is the subject of the email message sent by the attacker? | `URGENT: Approval for new internal VPN Access` |
| 4 | When did the attacker access the response to the message? (Exact Splunk Time value) | `2/11/26 6:20:09.000 PM` |
| 5 | Which path was the response stored in? | `\Deleted Items` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Introduction | What type of application is Entra ID? | `Identity Provider` |
| 2 | Introduction | What type of identity is a server account? | `Device` |
| 3 | Introduction | What authentication resource can prevent attackers from authenticating with only a stolen password? | `MFA` |
| 4 | Introduction | What can help us detect and monitor cloud identity threats? | `Logs` |
| 5 | Compromised User - Sign-In Logs | What is the email address of the compromised identity? | `allan.smith@finegalo.thm` |
| 6 | Compromised User - Sign-In Logs | What is the IP address used by the attacker? | `2804:2488:7082:a4c0:fd97:b11b:9895:49c0` |
| 7 | Compromised User - Sign-In Logs | What is the city of the IP address used by the attacker? | `Belo Horizonte` |
| 8 | Compromised User - Sign-In Logs | When was the first successful sign-in in the compromised account after the failure attempts? (Exact Splunk Time value) | `2/11/26 6:16:53.000 PM` |
| 9 | Compromised User - Audit Logs | What is the first application the attacker accessed after the office home page? | `One Outlook Web` |
| 10 | Compromised User - Audit Logs | What was the first change made by the attacker in the compromised user account? | `User started security info registration` |
| 11 | Compromised User - Audit Logs | What is the activityDisplayName that reveals all the details of the modified properties in a user? | `Update user` |
| 12 | Compromised User - Audit Logs | What is the second change made in the account? | `Reset password (self-service)` |
| 13 | Compromised User - Email Rules | What is the application used by the attacker? | `Exchange` |
| 14 | Compromised User - Email Rules | What is the change made in the user application by the attacker? | `New-InboxRule` |
| 15 | Compromised User - Email Rules | What is the subject of the email message sent by the attacker? | `URGENT: Approval for new internal VPN Access` |
| 16 | Compromised User - Email Rules | When did the attacker access the response to the message? (Exact Splunk Time value) | `2/11/26 6:20:09.000 PM` |
| 17 | Compromised User - Email Rules | Which path was the response stored in? | `\Deleted Items` |

---

**Metodología:** El room sigue un escenario de compromiso completo: primero se identifica la identidad y el origen del ataque en sign-in logs, luego se analizan los audit logs para rastrear cambios en la cuenta (registro de MFA, reset de contraseña), y finalmente se examinan las reglas de correo (inbox rules) y tráfico de email para comprender el alcance del compromiso. Cada paso usa Splunk con la fuente M365 exportada.

### Cadena de ataque / Attack Chain

```text
sign-in logs -> identificar identidad comprometida -> localizar IP y geolocalización -> audit logs -> cambios de cuenta (MFA registration, reset password) -> inbox rules (New-InboxRule) -> exfiltración de correo -> análisis del alcance
```

**Learning chain:** Identity Providers → MFA → Logs → Sign-in Analysis → Audit Logs → Inbox Rules

**Lección:** *Un compromiso de identidades cloud casi nunca se limita al primer inicio de sesión; los sign-in logs, audit logs y reglas de correo revelan la cadena completa de acciones del atacante y permiten dimensionar el daño.*

**MITRE ATT&CK:** T1078.004 (Valid Accounts: Cloud Accounts), T1098 (Account Manipulation), T1114 (Email Collection), T1114.003 (Email Collection: Email Forwarding Rule)

**Fuente:** [TryHackMe - M365 Monitoring Basics](https://tryhackme.com/r/room/m365monitoringbasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.