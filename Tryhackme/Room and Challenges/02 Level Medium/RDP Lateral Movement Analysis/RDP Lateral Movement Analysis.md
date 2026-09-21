# RDP Lateral Movement Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `rdplateralmovementanalysis` | [TryHackMe](https://tryhackme.com/room/rdplateralmovementanalysis) | 02 Level Medium | TryHackMe | RDP, T1021.001, Event Logs, Velociraptor, KAPE, bmc-tools, PECmd | Detección e investigación de movimiento lateral por RDP en entornos Windows |

---

**Contexto:** Sala centrada en RDP como técnica de movimiento lateral (T1021.001). Se estudia cómo identificar y correlacionar sesiones RDP legítimas vs maliciosas con logs de eventos (Sysmon 1/3, TerminalServices-RDPClient 1024/1025, Security 4624 Type 10, TS-RemoteConnectionManager 1149, TS-LocalSessionManager 21-25), artefactos en origen (MRU del Terminal Server Client, UsernameHint, bitmap cache, Prefetch MSTSC.EXE) y en destino (rdpclip.exe, tstheme.exe). Todo el análisis se desarrolla sobre una analyst VM a la que se accede por RDP con DFIRUser:TryH@cKMe1!433, con triage en D:\Walkthrough (THM-MKT-WS, THM-SHR-SRV) y D:\Challenge (THM-DEV-WS, THM-SHR-SRV, THM-SQL-SRV, THM-DC), y un challenge de investigación multi-hop (THM-DEV-WS → THM-SHR-SRV → THM-SQL-SRV → THM-DC). Como contexto real se asocia este patrón con RansomHub password spray + RDP chaining (~118 h), Volt Typhoon y BianLian.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Primera toma de contacto con la sala y sus objetivos. No se requiere ninguna respuesta: simplemente se confirma que la analyst workstation se ha iniciado correctamente y se prepara el escenario para el resto de tareas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have successfully started my analyst workstation instance. | `No answer needed` |

---

### Task 2: How RDP Lateral Movement Works / Cómo funciona el movimiento lateral por RDP

**Explicación:** RDP (Remote Desktop Protocol) permite conectarse a un escritorio remoto a través del puerto TCP 3389. La autenticación previa al establecimiento de la sesión la realiza NLA (Network Level Authentication), que valida las credenciales antes de crear el escritorio remoto y ayuda a mitigar ataques como el relay de credenciales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the default TCP port used by RDP? | `3389` |
| 2 | Which authentication mechanism pre-authenticates RDP users before a session is created? | `NLA (Network Level Authentication)` |

---

### Task 3: Legitimate vs Malicious RDP Usage / Uso legítimo vs malicioso de RDP

**Explicación:** Hay que distinguir el uso legítimo de RDP (administración remota habitual) del malicioso (password spraying, encadenamiento de saltos, acceso desde subredes anómalas, uso de cuentas comprometidas). MITRE ATT&CK clasifica RDP dentro de Remote Services (T1021) con la sub-técnica T1021.001.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to MITRE ATT&CK, what is the sub-technique ID for Remote Desktop Protocol under Remote Services? | `T1021.001` |

---

### Task 4: Investigating RDP via Event Logs / Investigando RDP mediante Event Logs

**Explicación:** El triage se realiza en D:\Walkthrough con muestras de THM-MKT-WS (origen) y THM-SHR-SRV (destino). En el origen, Sysmon Event ID 1 muestra la ejecución de mstsc.exe bajo el contexto del usuario luke.sullivan, y TerminalServices-RDPClient (1024/1025) revela la IP 10.5.30.155 y el hostname THM-SHR-SRV al que se conectó por TCP 3389. En el destino, el Security log 4624 con Logon Type 10 (RemoteInteractive) y TS-RemoteConnectionManager (1149) confirman la autenticación exitosa de la cuenta adm-rachel.brooks.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | On the source workstation, which user account launched the RDP client (mstsc.exe)? | `luke.sullivan` |
| 2 | What is the IP address of the destination the client connected to on TCP 3389? | `10.5.30.155` |
| 3 | What destination hostname did the RDP client attempt to connect to? | `THM-SHR-SRV` |
| 4 | Which account successfully authenticated at the destination over RDP? | `adm-rachel.brooks` |

---

### Task 5: Investigating RDP via Forensic Artifacts / Investigando RDP mediante Artefactos Forenses

**Explicación:** Más allá de los logs, los artefactos del sistema corroboran el uso de RDP. En el origen se procesa el bitmap cache (archivos bmc) con bmc-tools y herramientas como RdpCacheStitcher para reconstruir la sesión, siendo recuperados 2701 tiles. El MRU del Terminal Server Client y el UsernameHint aportan las últimas conexiones, y el Prefetch de MSTSC.EXE —parseado con PECmd (EZ Tools)— indica como última ejecución el 2026-05-18 05:15:10. En el destino, procesos como rdpclip.exe y tstheme.exe son señal de una sesión RDP activa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many bitmap cache tiles did bmc-tools recover from the source host? | `2701` |
| 2 | According to the MSTSC.EXE prefetch, what was the last execution time of the RDP client? (Answer Format: YYYY-MM-DD HH:MM:SS) | `2026-05-18 05:15:10` |

---

### Task 6: Investigation Challenge / Challenge de Investigación

**Explicación:** Challenge multi-hop en D:\Challenge con cuatro hosts: THM-DEV-WS (origen), THM-SHR-SRV (file server), THM-SQL-SRV y THM-DC (destino final). Se identifica una sesión RDP anómala que aterriza en el file server desde una subred no estándar: la IP 10.5.30.155 y la cuenta adm-rachel.brooks. Siguiendo la cadena, el operador salta a un segundo host (THM-SQL-SRV) y finalmente al dominio. La pregunta 4 se resuelve correlacionando Security 4624 (Logon Type 10), Sysmon Event ID 1 y el Prefetch en D:\Challenge, host THM-DC, para hallar el binario ejecutado desde C:\Windows\Temp\; la pregunta 5 requiere revisar el Scheduled Task / registro de persistencia en THM-DC. Las respuestas no confirmadas se dejan como `-` para ser completadas tras el triage completo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | An unusual RDP session landed on a file server from a non-standard subnet. What is the source workstation IP? | `10.5.30.155` |
| 2 | What account was used to authenticate that session? | `adm-rachel.brooks` |
| 3 | Continuing the trail, what is the second host the operator landed on after the file server? | `THM-SQL-SRV` |
| 4 | On the final destination, the operator executed a binary from C:\Windows\Temp\. What is the filename? | `-` |
| 5 | What scheduled task did the operator create to persist the binary? | `-` |

---

### Task 7: Prevention and Mitigation Strategies / Estrategias de Prevención y Mitigación

**Explicación:** Para endurecer el acceso remoto se recomienda, entre otras medidas, exigir NLA mediante la política de grupo "Require user authentication for remote connections by using Network Level Authentication", restringir RDP por firewall y subredes, aplicar MFA, limitar cuentas privilegiadas y auditar los eventos 4624/1149/21-25.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which Group Policy setting enforces Network Level Authentication for incoming RDP connections? | `Require user authentication for remote connections by using Network Level Authentication` |

---

### Task 8: Conclusion / Conclusión

**Explicación:** Cierre de la sala: "Good work! ..." Se refuerza la idea de que RDP es un vector frecuente en intrusiones reales y que una correcta correlación de logs y artefactos permite detectar y responder ante el movimiento lateral. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Good work! ... | `No answer needed` |

---

**Metodología:** El análisis siguió un flujo de triage y correlación en tres planos: (1) origen (mstsc.exe + Sysmon 1, TerminalServices-RDPClient 1024/1025, artefactos de conexión), (2) destino (Security 4624 Type 10, TS-RemoteConnectionManager 1149, TS-LocalSessionManager 21-25, rdpclip.exe/tstheme.exe) y (3) artefactos forenses (MRU del Terminal Server Client, UsernameHint, bitmap cache con bmc-tools/RdpCacheStitcher y Prefetch MSTSC.EXE con PECmd). Sobre el entorno, la analyst VM ofrece los datos de acceso DFIRUser:TryH@cKMe1!433 vía RDP, y la evidencia se agrupa en D:\Walkthrough (THM-MKT-WS, THM-SHR-SRV) y D:\Challenge (THM-DEV-WS, THM-SHR-SRV, THM-SQL-SRV, THM-DC). El caso se contextualiza con campañas reales de RansomHub (password spray + RDP chaining con ~118 h de acceso sin detección) y con el abuso de RDP por grupos como Volt Typhoon y BianLian.

### Cadena de ataque / Attack Chain

```text
Reconocimiento y recopilación de credenciales
        │
        ▼
Password spray / credential theft (campaña RansomHub, ~118 h)
        │
        ▼
[Origen] luke.sullivan ejecuta mstsc.exe (Sysmon 1) → RDP a 10.5.30.155 TCP 3389
        │   (TerminalServices-RDPClient 1024/1025, hostname THM-SHR-SRV)
        ▼
[Destino] THM-SHR-SRV: autenticación remota adm-rachel.brooks (4624 Type 10, 1149)
        │   (rdpclip.exe / tstheme.exe = sesión RDP activa)
        ▼
[Multi-hop] THM-DEV-WS → THM-SHR-SRV → THM-SQL-SRV → THM-DC
        │   (10.5.30.155 desde subred no estándar)
        ▼
[Persistencia en THM-DC] binario ejecutado desde C:\Windows\Temp\
        │   (correlacionar 4624 Type 10 + Sysmon 1 + Prefetch)
        ▼
[Persistencia] Scheduled Task creada en el host final (registro de persistencia)
        │
        ▼
[Impacto potencial] Compromiso total del dominio (RansomHub, Volt Typhoon, BianLian)
```

**Learning chain:** Correlación de eventos de origen (Sysmon 1, 1024/1025) y destino (4624 Type 10, 1149, 21-25) → artefactos forenses (MRU, UsernameHint, bitmap cache, Prefetch) → reconstrucción de la cadena multi-hop → persistencia (Scheduled Task) → prevención con NLA/GPO.

**Lección:** *RDP es una puerta giratoria para el movimiento lateral: sin correlación entre logs de origen/destino y sin endurecimiento (NLA, MFA, segmentación), un único par de credenciales permite encadenar saltos a través de la red y persistir con Scheduled Tasks hasta comprometer el dominio.*

**MITRE ATT&CK:** T1021.001, T1078

**Fuente:** [TryHackMe - RDP Lateral Movement Analysis](https://tryhackme.com/room/rdplateralmovementanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.