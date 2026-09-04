# MS Sentinel: Just Looking [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** Easy
* **Tipo / Type:** CTF
* **Slug:** `justlooking`
* **Link:** https://tryhackme.com/room/justlooking
* **Descripción / Description:** Microsoft Sentinel challenge para SOC Analysts: investigación de incidentes y threat hunting. Despliegas un tenant de Azure/Sentinel en vivo, configuras reglas analíticas (analytics rules) y analizas incidentes reales.
* **Nota / Note:** Aunque aparece "Premium" para acceder a las tareas interactivas, la sala es **Free** (gratuita) y se documenta con fines educativos.

---

## Solucionario de Tareas / Task Solutions

Fuentes principales / Main sources:
- https://github.com/thmrevenant/tryhackme (rooms/ms sentinel just looking.txt)
- https://ligniform.blog/posts/ms-sentinel-just-looking/
- https://medium.com/h7w/ms-sentinel-just-looking-tryhackme-answers-d92560b4cb60

### Tarea 1 / Task 1 — Deploy Microsoft Sentinel Challenge Workspace

Desplegar el laboratorio y loguearse en Azure Portal con las credenciales del lab (Cloud Details > Environment tab > Join Lab). Confirmar el Resource Group `rg-AZURE_LAB_ID`.

* **Respuesta / Answer:** No answer needed.

### Tarea 2 / Task 2 — Logs Ready, Steady, Go!

Desplegar los logs del challenge y consultarlos desde Log Analytics / Sentinel (Logs).

**Pregunta 1 / Question 1:** What's the row count for `SigninLogs_CL` table?
* **Respuesta / Answer:** 930

**Pregunta 2 / Question 2:** What's the row count for `AuditLogs_CL` table?
* **Respuesta / Answer:** 58

**Pregunta 3 / Question 3:** Key combination for running KQL queries in Query Editor? ___ + Enter
* **Respuesta / Answer:** Shift

### Tarea 3 / Task 3 — Analytics

Desplegar / activar las analytics rules en `Sentinel -> Configuration -> Analytics`.

**Pregunta 1 / Question 1:** MITRE ATT&CK sub-technique for rule: Account Created and Deleted in Short Timeframe
* **Respuesta / Answer:** T1078.004

**Pregunta 2 / Question 2:** Rule frequency (in hrs) for rule: Attempts to sign in to disabled accounts
* **Respuesta / Answer:** 1

**Pregunta 3 / Question 3:** ResultType filter in rule: Explicit MFA Deny
* **Respuesta / Answer:** 500121

**Pregunta 4 / Question 4:** AppDisplayName filter in rule: Brute force attack against Azure Portal
* **Respuesta / Answer:** Azure Portal

**Pregunta 5 / Question 5:** Category filter in rule: Privileged Role Assigned Outside PIM
* **Respuesta / Answer:** RoleManagement

### Tarea 4 / Task 4 — Incident #1: Account Created and Deleted in Short Timeframe

Ir a `Sentinel -> Threat Management -> Incidents`.

**Pregunta 1 / Question 1:** How many accounts were created and deleted in a short time frame?
* **Respuesta / Answer:** 5

**Pregunta 2 / Question 2:** Which entity deleted these accounts?
* **Respuesta / Answer:** thmMultiTenantApp

**Pregunta 3 / Question 3:** Tactic for this incident?
* **Respuesta / Answer:** Initial Access

**Pregunta 4 / Question 4:** Workflow Id involved in this incident?
* **Respuesta / Answer:** b3f33fbcc5a541dc803a9b9bb7a5105f

**Pregunta 5 / Question 5:** UPNSuffix
* **Respuesta / Answer:** tryhackmelabs.onmicrosoft.com

### Tarea 5 / Task 5 — Incident #2: Attempts to Sign in to Disabled Accounts

**Pregunta 1 / Question 1:** What's the IP Address involved in this incident?
* **Respuesta / Answer:** 181.214.151.205

**Pregunta 2 / Question 2:** IP Geolocation (City)
* **Respuesta / Answer:** Miami

**Pregunta 3 / Question 3:** Disabled account?
* **Respuesta / Answer:** marcus@tryhackmelabs.onmicrosoft.com

**Pregunta 4 / Question 4:** ResultType filter in rule?
* **Respuesta / Answer:** 50057

### Tarea 6 / Task 6 — Incident #3: Explicit MFA Deny

**Pregunta 1 / Question 1:** Tactic for this incident?
* **Respuesta / Answer:** Credential Access

**Pregunta 2 / Question 2:** How about its technique?
* **Respuesta / Answer:** Brute Force

**Pregunta 3 / Question 3:** What's the error code when MFA is denied?
* **Respuesta / Answer:** 500121

**Pregunta 4 / Question 4:** What's the name of the Access Policy that triggered this MFA during authentication?
* **Respuesta / Answer:** Security Defaults

**Pregunta 5 / Question 5:** Which authentication method was used for this MFA?
* **Respuesta / Answer:** Mobile app notification

**Pregunta 6 / Question 6:** Browser version of the device initiated this authentication?
* **Respuesta / Answer:** 125.0

**Pregunta 7 / Question 7:** How many entities are mapped in this incident?
* **Respuesta / Answer:** 2

### Tarea 7 / Task 7 — Incident #4: Privileged Role Assigned Outside PIM

**Pregunta 1 / Question 1:** Which UPN escalated Marcus' privileges?
* **Respuesta / Answer:** breakglass@tryhackmelabs.onmicrosoft.com

**Pregunta 2 / Question 2:** Which privileged role has been assigned to Marcus?
* **Respuesta / Answer:** Privileged Role Administrator

**Pregunta 3 / Question 3:** In which source table has this privilege escalation been logged?
* **Respuesta / Answer:** AuditLogs_CL

**Pregunta 4 / Question 4:** Which other user has been a target?
* **Respuesta / Answer:** usr-24052103@tryhackmelabs.onmicrosoft.com

**Pregunta 5 / Question 5:** What's the initiating IP Address?
* **Respuesta / Answer:** 2.59.157.197

---

*Documentación para propósitos educativos y registro de CTF.*
