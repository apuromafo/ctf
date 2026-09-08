# MS Sentinel: Just Looking

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `justlooking` |
| **Link** | [TryHackMe](https://tryhackme.com/room/justlooking) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (GitHub thmrevenant + ligniform.blog + h7w Medium) |
| **Componentes** | Microsoft Sentinel / Azure Portal / KQL / Log Analytics / Analytics rules / MITRE ATT&CK |
| **Impacto** | Investigación en vivo de incidentes y threat hunting con reglas analíticas en un tenant de Microsoft Sentinel |

---

**Contexto:** Microsoft Sentinel challenge para SOC Analysts: investigación de incidentes y threat hunting. Despliegas un tenant de Azure/Sentinel en vivo, configuras reglas analíticas (analytics rules) y analizas incidentes reales con consultas KQL. Aunque aparece "Premium" para acceder a las tareas interactivas, la sala es **Free** (gratuita) y se documenta con fines educativos.

Fuentes principales: [GitHub thmrevenant](https://github.com/thmrevenant/tryhackme) · [ligniform.blog](https://ligniform.blog/posts/ms-sentinel-just-looking/) · [h7w Medium](https://medium.com/h7w/ms-sentinel-just-looking-tryhackme-answers-d92560b4cb60)

## Solucionario

### Task 1: Deploy Microsoft Sentinel Challenge Workspace

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

**Explicación:** Desplegar el laboratorio y loguearse en Azure Portal con las credenciales del lab (Cloud Details > Environment tab > Join Lab). Confirmar el Resource Group `rg-AZURE_LAB_ID`.

### Task 2: Logs Ready, Steady, Go!

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the row count for `SigninLogs_CL` table? | `930` |
| 2 | What's the row count for `AuditLogs_CL` table? | `58` |
| 3 | Key combination for running KQL queries in Query Editor? ___ + Enter | `Shift` |

**Explicación:** Desplegar los logs del challenge y consultarlos desde Log Analytics / Sentinel (Logs). `SigninLogs_CL` → 930 filas; `AuditLogs_CL` → 58; la combinación de teclas para ejecutar KQL en el Query Editor es **Shift** + Enter.

### Task 3: Analytics

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | MITRE ATT&CK sub-technique for rule: Account Created and Deleted in Short Timeframe | `T1078.004` |
| 2 | Rule frequency (in hrs) for rule: Attempts to sign in to disabled accounts | `1` |
| 3 | ResultType filter in rule: Explicit MFA Deny | `500121` |
| 4 | AppDisplayName filter in rule: Brute force attack against Azure Portal | `Azure Portal` |
| 5 | Category filter in rule: Privileged Role Assigned Outside PIM | `RoleManagement` |

**Explicación:** Desplegar / activar las analytics rules en `Sentinel -> Configuration -> Analytics` y anotar los metadatos de cada regla (T1078.004, frecuencia 1h, ResultType 500121, AppDisplayName Azure Portal, categoría RoleManagement).

### Task 4: Incident #1: Account Created and Deleted in Short Timeframe

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many accounts were created and deleted in a short time frame? | `5` |
| 2 | Which entity deleted these accounts? | `thmMultiTenantApp` |
| 3 | Tactic for this incident? | `Initial Access` |
| 4 | Workflow Id involved in this incident? | `b3f33fbcc5a541dc803a9b9bb7a5105f` |
| 5 | UPNSuffix | `tryhackmelabs.onmicrosoft.com` |

**Explicación:** Ir a `Sentinel -> Threat Management -> Incidents`. 5 cuentas creadas/eliminadas; entidad eliminadora `thmMultiTenantApp`; táctica Initial Access; workflow `b3f33fbcc5a541dc803a9b9bb7a5105f`; UPNSuffix `tryhackmelabs.onmicrosoft.com`.

### Task 5: Incident #2: Attempts to Sign in to Disabled Accounts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the IP Address involved in this incident? | `181.214.151.205` |
| 2 | IP Geolocation (City) | `Miami` |
| 3 | Disabled account? | `marcus@tryhackmelabs.onmicrosoft.com` |
| 4 | ResultType filter in rule? | `50057` |

**Explicación:** IP 181.214.151.205 (Miami); cuenta deshabilitada `marcus@tryhackmelabs.onmicrosoft.com`; ResultType filter 50057.

### Task 6: Incident #3: Explicit MFA Deny

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tactic for this incident? | `Credential Access` |
| 2 | How about its technique? | `Brute Force` |
| 3 | What's the error code when MFA is denied? | `500121` |
| 4 | What's the name of the Access Policy that triggered this MFA during authentication? | `Security Defaults` |
| 5 | Which authentication method was used for this MFA? | `Mobile app notification` |
| 6 | Browser version of the device initiated this authentication? | `125.0` |
| 7 | How many entities are mapped in this incident? | `2` |

**Explicación:** Táctica Credential Access, técnica Brute Force; error 500121; política Security Defaults; método "Mobile app notification"; navegador 125.0; 2 entidades mapeadas.

### Task 7: Incident #4: Privileged Role Assigned Outside PIM

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which UPN escalated Marcus' privileges? | `breakglass@tryhackmelabs.onmicrosoft.com` |
| 2 | Which privileged role has been assigned to Marcus? | `Privileged Role Administrator` |
| 3 | In which source table has this privilege escalation been logged? | `AuditLogs_CL` |
| 4 | Which other user has been a target? | `usr-24052103@tryhackmelabs.onmicrosoft.com` |
| 5 | What's the initiating IP Address? | `2.59.157.197` |

**Explicación:** breakglass escaló a Marcus (Privileged Role Administrator), registrado en `AuditLogs_CL`; otro objetivo `usr-24052103@tryhackmelabs.onmicrosoft.com`; IP iniciadora 2.59.157.197.

**Metodología:**
1. **Deploy:** desplegar el laboratorio (Cloud Details > Environment tab > Join Lab), loguearse en Azure Portal y confirmar el Resource Group del challenge.
2. **Logs:** cargar los logs del challenge y consultarlos desde Log Analytics / Sentinel (Logs): `SigninLogs_CL` (930 filas), `AuditLogs_CL` (58) y ejecutar KQL con Shift + Enter.
3. **Analytics:** activar las analytics rules en `Sentinel → Configuration → Analytics` y anotar los metadatos de cada regla (T1078.004, frecuencia 1h, ResultType 500121, AppDisplayName Azure Portal, categoría RoleManagement).
4. **Incident #1 (Account Created and Deleted):** 5 cuentas creadas/eliminadas; entidad eliminadora `thmMultiTenantApp`; táctica Initial Access; workflow `b3f33fbcc5a541dc803a9b9bb7a5105f`; UPNSuffix `tryhackmelabs.onmicrosoft.com`.
5. **Incident #2 (Sign in to disabled accounts):** IP 181.214.151.205 (Miami); cuenta deshabilitada `marcus@...`; ResultType 50057.
6. **Incident #3 (Explicit MFA Deny):** táctica Credential Access, técnica Brute Force; error 500121; política Security Defaults; método "Mobile app notification"; navegador 125.0; 2 entidades mapeadas.
7. **Incident #4 (Privileged Role Assigned Outside PIM):** breakglass escaló a Marcus (Privileged Role Administrator), registrado en `AuditLogs_CL`; otro objetivo `usr-24052103@...`; IP iniciadora 2.59.157.197.

**Learning chain:** deploy del tenant → ingesta de logs (SigninLogs_CL/AuditLogs_CL) → analytics rules → Incidentes: cuentas creadas/borradas → inicios en cuentas deshabilitadas → MFA denegado → rol asignado fuera de PIM

**MITRE ATT&CK:** T1078.004 (Valid Accounts: Cloud Accounts), T1098 (Account Manipulation), T1110 (Brute Force)

**Fuente:** [TryHackMe - MS Sentinel: Just Looking](https://tryhackme.com/room/justlooking)
