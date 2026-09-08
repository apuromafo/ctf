# Windows Event Logs

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `windowseventlogs` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowseventlogs) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Windows Event Logs / Get-WinEvent / XPath / PowerShell / Sysmon / Security audit |
| **Impacto** | Consultar y filtrar Event Logs de Windows con PowerShell (Get-WinEvent, XPath) para investigar actividad de proceso y seguridad |

---

**Contexto:** Sala sobre Windows Event Logs: aprender a consultar logs (Application, Security) con `Get-WinEvent` y filtros XPath, identificar metadatos (evento, proveedor, usuario) y reconstruir actividades (ejecución de comandos, creación de usuarios, logons).

## Solucionario

### Task 1: (Intro)

**Explicación:**

Introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: (Artefactos / Event metadata)

**Explicación:**

Artefactos de Windows Event Logs: se explora el formato y los metadatos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Metadata - 1) | `1. No answer needed` |
| 2 | (Event ID) | `2. 40961` |
| 3 | (Executed command) | `3. whoami` |
| 4 | (Description) | `4. Execute a Remote Command` |
| 5 | (Detail) | `5. Pipeline Execution Details` |

### Task 3: (Filtrado / Filtering)

**Explicación:**

Filtrado de eventos: se repasan filtros Get-WinEvent; el índice de búsqueda indica unos eventos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Event ID) | `1. 1071` |
| 2 | (Keywords) | `2. event log, log file, structured query` |
| 3 | (XPath parameter) | `3. /lf:true` |
| 4 | (Filter type) | `4. Xpath query` |
| 5 | (Filter - 5) | `5. No answer needed` |
| 6 | (Log name) | `6. Application` |
| 7 | (Direction) | `7. Event read direction` |
| 8 | (Max events) | `8. Maximum number of events to read` |

### Task 4: (Consulta de logs / Querying logs)

**Explicación:**

Consultas de logs: las fuentes de log son `OpenSSH/Admin,OpenSSH/Operational`; el proveedor es `Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager`; el número de eventos es `192`; el parámetro de limite `-MaxEvents`; y el conteo de eventos `4`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Log - 1) | `1. No answer needed` |
| 2 | (Sources) | `2. OpenSSH/Admin,OpenSSH/Operational` |
| 3 | (Provider) | `3. Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager` |
| 4 | (Event count) | `4. 192` |
| 5 | (Parameter) | `5. -MaxEvents` |
| 6 | (Count 2) | `6. 4` |

### Task 5: (Filtros XPath / XPath filters)

**Explicación:**

Filtros XPath en PowerShell: la consulta que retorna el evento de WLMS en una fecha concreta es `Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]'`. La consulta para el EventID 4720 del usuario "Sam" es `Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4720'`. El número de eventos es `2`; la descripción es `A user account was created`; la fecha es `12/17/2020 1:57:14 PM`; y el proveedor es `Microsoft-Windows-Security-Auditing`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Filter 1) | `1. Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]'` |
| 2 | (Filter 2) | `2. Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4720'` |
| 3 | (Count) | `3. 2` |
| 4 | (Description) | `4. A user account was created` |
| 5 | (Date) | `5. 12/17/2020 1:57:14 PM` |
| 6 | (Provider) | `6. Microsoft-Windows-Security-Auditing` |

### Task 6: (Revisión / Review)

**Explicación:**

Revisión de seguridad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Review) | `No answer needed` |

### Task 7: (Registro de seguridad / Security log - User)

**Explicación:**

Registro de seguridad (usuario): el ID de evento es `400`; la fecha es `12/18/2020 7:50:33 AM`; el número de llamada es `27736`; el host es `PC01.example.corp`; la contraseña es `$Va5w3n8`; la fecha 2 es `8/25/2020 10:09:28 PM`; el PID es `6620`; el SID del grupo administradores es `S-1-5-32-544`; y el ID de evento de grupo es `4799`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Event ID) | `1. 400` |
| 2 | (Date) | `2. 12/18/2020 7:50:33 AM` |
| 3 | (Call) | `3. 27736` |
| 4 | (Host) | `4. PC01.example.corp` |
| 5 | (Password) | `5. $Va5w3n8` |
| 6 | (Date 2) | `6. 8/25/2020 10:09:28 PM` |
| 7 | (PID) | `7. 6620` |
| 8 | (Admin SID) | `8. S-1-5-32-544` |
| 9 | (Group event) | `9. 4799` |

### Task 8: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión) | `No answer needed` |

---

**Metodología:**

1. Revisar metadatos de eventos y el comando ejecutado (`whoami`).
2. Usar `Get-WinEvent` con filtros XPath para seleccionar eventos concretos (WLMS, EventID 4720, etc.).
3. Consultar múltiples logs (Application, OpenSSH/Operational) y proveedores.
4. Interpretar el registro de seguridad (user creation, logons, grupos) para reconstruir actividades.

**Learning chain:** metadatos/Event ID 40961 -> whoami -> filtros Get-WinEvent -> XPath filters -> WLMS/4720 -> Application/Security logs -> user creation -> logons

**Lección:** *`Get-WinEvent` con filtros XPath es la forma precisa de consultar Event Logs de Windows; correlacionando eventos (ejecución 40961, creación de usuario 4720, grupo 4799) se reconstruye la actividad del sistema y de seguridad.*

**MITRE ATT&CK:** T1059.001 (PowerShell) · T1070.001 (Clear Windows Event Logs) · T1136.001 (Create Local Account) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Windows Event Logs](https://tryhackme.com/room/windowseventlogs)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
