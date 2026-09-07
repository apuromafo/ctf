# Monitoring Active Directory

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `monitoringactivedirectory` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/monitoringactivedirectory) |
| **Sección** | Active Directory Security |
| **Fuente** | THM |
| **Componentes** | Splunk, NTDS.dit, Event IDs 4768/4769, auditpol |
| **Impacto** | Medium |

---

**Contexto:** Este room introduce las bases del monitoreo en entornos Active Directory, desde la auditoría de eventos Kerberos hasta la detección de creación de cuentas no autorizadas. Aprenderemos a correlacionar logs en Splunk, identificar Event IDs clave como 4768 y 4769, y verificar políticas de auditoría con auditpol. Es una guía práctica para detectar movimiento sospechoso dentro de un dominio.

## Solucionario

### Task 1: Active Directory Basics

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which file stores domain user credentials on the domain controller? | `NTDS.dit` |
| 2 | A local user authenticates to a workstation. Will this generate any events on the Domain Controller? (Answer Format: Yea or Nay) | `Nay` |

### Task 2: Kerberos Events in Splunk

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Event ID is generated when a user requests a TGT? | `4768` |
| 2 | In win index in Splunk, how many unique accounts requested TGTs in the dataset across all time? | `14` |
| 3 | In Splunk, what field contains the group name? | `Group_Name` |
| 4 | What is the MOST common logon type in the dataset? | `3` |
| 5 | What character suffix identifies computer accounts in AD? | `$` |
| 6 | Using Event ID 4769, what is the MOST frequently requested service? | `THM-DC$` |

### Task 3: Auditing Policy in Windows

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command displays all current audit policy settings on a domain controller? | `auditpol /get /category:*` |

### Task 4: Correlating Logs

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the newly created account? | `nathan.brooks` |
| 2 | Who created this account? | `adm-luke.sullivan` |
| 3 | What group was this user added to? | `Marketing` |
| 4 | What was the source IP address of nathan.brooks's first TGT request? | `10.5.50.12` |

---

**Metodología:** Se comienza desde los fundamentos de AD (NTDS.dit, eventos locales vs. del DC), se avanza al análisis de logs Kerberos en Splunk (Event IDs 4768/4769, cuentas de equipo con sufijo $), se verifica la política de auditoría con auditpol, y finalmente se correlacionan eventos para detectar creación y uso de cuentas no autorizadas.
**Learning chain:** NTDS.dit → Kerberos Events (4768/4769) → Splunk Queries → auditpol → Log Correlation
**MITRE ATT&CK:** T1136.002 (Create Account: Domain Account), T1078 (Valid Accounts), T1550 (Use Alternate Authentication Material)
**Fuente:** [TryHackMe - Monitoring Active Directory](https://tryhackme.com/r/room/monitoringactivedirectory)
