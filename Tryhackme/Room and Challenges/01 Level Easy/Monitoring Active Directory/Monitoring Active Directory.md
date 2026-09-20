# Monitoring Active Directory

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `monitoringactivedirectory` | https://tryhackme.com/room/monitoringactivedirectory | Active Directory Security | TryHackMe | Splunk, NTDS.dit, Event IDs 4768/4769, auditpol | Medium |

---

**Contexto:** Este room introduce las bases del monitoreo en entornos Active Directory, desde la auditoría de eventos Kerberos hasta la detección de creación de cuentas no autorizadas. Aprenderemos a correlacionar logs en Splunk, identificar Event IDs clave como 4768 y 4769, y verificar políticas de auditoría con auditpol. Es una guía práctica para detectar movimiento sospechoso dentro de un dominio.

> **ES:** Monitoreo de Active Directory: NTDS.dit, eventos Kerberos en Splunk (4768/4769), políticas de auditoría con auditpol y correlación de logs.
> **EN:** Active Directory monitoring: NTDS.dit, Kerberos events in Splunk (4768/4769), audit policy with auditpol and log correlation.

## Solucionario

### Task 1: Bases de Active Directory / Active Directory Basics

**Explicación:** Se repasan los fundamentos de AD que se vigilarán: el almacén de credenciales del dominio (`NTDS.dit`) y qué eventos genera la autenticación local frente a la del Domain Controller. Las respuestas originales se conservan verbatim.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which file stores domain user credentials on the domain controller? | `NTDS.dit` |
| 2 | A local user authenticates to a workstation. Will this generate any events on the Domain Controller? (Answer Format: Yea or Nay) | `Nay` |

### Task 2: Eventos Kerberos en Splunk / Kerberos Events in Splunk

**Explicación:** Se consulta el índice `win` de Splunk para analizar eventos Kerberos: el Event ID `4768` se genera al solicitar un TGT; se cuentan cuentas únicas y se estudian campos como `Group_Name`, el tipo de logon más común (`3`) o el sufijo `$` que identifica a las cuentas de equipo. Con el Event ID `4769` se identifica el servicio más solicitado (`THM-DC$`). Las respuestas originales se conservan verbatim.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Event ID is generated when a user requests a TGT? | `4768` |
| 2 | In win index in Splunk, how many unique accounts requested TGTs in the dataset across all time? | `14` |
| 3 | In Splunk, what field contains the group name? | `Group_Name` |
| 4 | What is the MOST common logon type in the dataset? | `3` |
| 5 | What character suffix identifies computer accounts in AD? | `$` |
| 6 | Using Event ID 4769, what is the MOST frequently requested service? | `THM-DC$` |

### Task 3: Política de auditoría en Windows / Auditing Policy in Windows

**Explicación:** Se verifica la configuración de auditoría del Domain Controller con `auditpol`, cuyo comando para mostrar todas las políticas de auditoría actuales se conserva verbatim.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command displays all current audit policy settings on a domain controller? | `auditpol /get /category:*` |

### Task 4: Correlación de logs / Correlating Logs

**Explicación:** Mediante la correlación de eventos de creación de cuentas, la pertenencia a grupos y las solicitudes de TGT se identifica a la cuenta creada de forma no autorizada (`nathan.brooks`), quién la creó (`adm-luke.sullivan`), el grupo al que se añadió (`Marketing`) y la IP origen de su primer TGT (`10.5.50.12`). Las respuestas originales se conservan verbatim.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the newly created account? | `nathan.brooks` |
| 2 | Who created this account? | `adm-luke.sullivan` |
| 3 | What group was this user added to? | `Marketing` |
| 4 | What was the source IP address of nathan.brooks's first TGT request? | `10.5.50.12` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which file stores domain user credentials on the domain controller? | `NTDS.dit` |
| 2 | A local user authenticates to a workstation. Will this generate any events on the Domain Controller? (Answer Format: Yea or Nay) | `Nay` |
| 3 | What Event ID is generated when a user requests a TGT? | `4768` |
| 4 | In win index in Splunk, how many unique accounts requested TGTs in the dataset across all time? | `14` |
| 5 | In Splunk, what field contains the group name? | `Group_Name` |
| 6 | What is the MOST common logon type in the dataset? | `3` |
| 7 | What character suffix identifies computer accounts in AD? | `$` |
| 8 | Using Event ID 4769, what is the MOST frequently requested service? | `THM-DC$` |
| 9 | What command displays all current audit policy settings on a domain controller? | `auditpol /get /category:*` |
| 10 | What is the name of the newly created account? | `nathan.brooks` |
| 11 | Who created this account? | `adm-luke.sullivan` |
| 12 | What group was this user added to? | `Marketing` |
| 13 | What was the source IP address of nathan.brooks's first TGT request? | `10.5.50.12` |

---

**Metodología:** Se comienza desde los fundamentos de AD (NTDS.dit, eventos locales vs. del DC), se avanza al análisis de logs Kerberos en Splunk (Event IDs 4768/4769, cuentas de equipo con sufijo $), se verifica la política de auditoría con auditpol, y finalmente se correlacionan eventos para detectar creación y uso de cuentas no autorizadas.

### Cadena de ataque / Attack Chain

```text
NTDS.dit y eventos de autenticación -> logs Kerberos en Splunk (Event ID 4768/4769) -> consultas sobre Group_Name, Logon Type, cuentas de equipo -> auditpol /get /category:* -> correlación de creación de cuenta -> nathan.brooks (Marketing, 10.5.50.12)
```

**Learning chain:** NTDS.dit → Kerberos Events (4768/4769) → Splunk Queries → auditpol → Log Correlation

**Lección:** *El monitoreo de AD no depende de una sola fuente: correlacionar eventos Kerberos (4768/4769), políticas de auditoría y el almacén NTDS.dit permite reconstruir una cadena completa de abuso de cuentas.* 

**MITRE ATT&CK:** T1136.002 (Create Account: Domain Account), T1078 (Valid Accounts), T1550 (Use Alternate Authentication Material)

**Fuente:** [TryHackMe - Monitoring Active Directory](https://tryhackme.com/room/monitoringactivedirectory)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.