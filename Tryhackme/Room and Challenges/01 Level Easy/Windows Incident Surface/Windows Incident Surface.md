# Windows Incident Surface [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `winincidentsurface`
* **Link:** https://tryhackme.com/room/winincidentsurface
* **Sección / Section:** DFIR / Windows
* **Fuente / Source:** Writeup de Simon Taplin (simontaplin.net) + thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Aprende a implementar técnicas de DFIR para explorar la superficie de incidentes de Windows. Identifica artefactos que dan un buen ROI en la caza de amenazas.
> **EN:** Learn how to implement DFIR techniques to explore the Windows incident surface. Identify artefacts that give a good ROI on threat hunts.

---

### Task 1 — Introduction

En el cambiante panorama de la ciberseguridad, no se puede depender solo de un enfoque reactivo. El objetivo no es un análisis exhaustivo, sino un triage eficiente y un descubrimiento accionable.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 2 — Reliability of the System Tools

Los atacantes pueden modificar las variables de entorno para secuestrar el flujo de ejecución (ATT&CK ID: T1574.007). Un perfil de PowerShell es un script que se ejecuta cada vez que se ejecuta PowerShell.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What **tool** did the adversary use to delete the logs? | `wevtutil` |
| What was the **registry path** used by the adversary to store and steal the login credentials? | `HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest` |

---

### Task 3 — System Information

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **hostname** of the compromised host? | `CCTL-WS-018-b21` |
| What is the **OS version** of the compromised host? | `10.0.17763` |
| What is the **Time ID** of the compromised host? | `Turkey Standard Time` |

---

### Task 4 — User Accounts

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the total number of suspicious accounts? | `3` |
| What is the security identifier (SID) of the Guest account? | `S-1-5-21-1966530601-3185510712-10604624-501` |
| When was the last time the Admin account (the one with the deliberate typo) was logged in? (Answer format: MM/DD/YY HH:MM:SS XM) | `2/28/2024 10:21:10 AM` |

---

### Task 5 — Processes

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **name** of the malicious process? Enter your answer in a **defanged** format. | `INITIAL_LANTERN[.]exe` |
| What is the **directory path** where the malicious process is located? | `C:\Users\Administrator\AppData\SpcTmp\` |
| What is the **remote port** used by the malicious process? | `8888` |
| What is the **full path** of the suspicious program for AnyDesk? Enter your answer in a **defanged** format. | `D:\AnyDesk[.]exe` |
| What **port** is used by the LMV Co. firewall rules? | `5985` |

---

### Task 6 — Persistence

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which **user account** will be used to run the AnyDesk application? | `Public` |
| What is the **value data** stored in the **"Userinit" key**? Enter your answer in a **defanged** format. | `C:\Windows\system32\userinit[.]exe, cmd[.]exe /c "start /min netsh[.]exe -c"` |
| What is the **name** of the suspicious **DLL** linked under the **netshell** hive key? | `.\fwshield.dll` |

---

### Task 7 — Services

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **name** of the suspicious active service? | `LMVCSS` |
| What is the **SHA256 value** of the suspicious active service executable? | `E9AA7564B2D1D612479E193A9F8CB70DF9CFBE02A39900EEE22FE266F5320EBF` |
| What is the **name** of the non-running service that caught our attention? | `aurora-agent` |
| What is the **SHA256 value** of the non-running service executable? | `D5C8BF2D3B56B21639D8152DB277DD714BA1A61BDAF2350BD0FF7E61D2A99003` |
| What is the **original filename** of the non-running service executable? Enter your answer in a **defanged** format. | `x3xv5weg[.]exe` |

---

### Task 8 — Network

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **parent process** name of the suspicious executable (INITIAL_LANTERN) process? Enter your answer in a **defanged** format. | `services[.]exe` |
| Which **user name** is used for the SSH connection attempts? | `James` |
| What is the **parent process** of the malicious aurora process? Enter your answer in a **defanged** format. | `svchost[.]exe` |
| What is the **file name** located in the default user's temp directory? Enter your answer in a **defanged** format. | `jmp[.]exe` |
| What is the **name** of the potential proxy script located in the suspicious non-default temp folder? Enter your answer in a **defanged** format. | `Invoke-SocksProxy[.]psm1` |
| What is the **SHA256 value** of the potential proxy script located in the suspicious non-default temp folder? | `E7697645F36DE5978C1B640B6B3FC819E55B00EE8D9E9798919C11CC7A6FC88B` |
| What is the **label** of the hidden disc volume? | `Setups` |

---

## Metodología / Methodology

1. **System tools:** revisar perfiles de PowerShell y variables de entorno para detectar hijacking de ejecución (T1574.007).
2. **System info:** hostname, OS version y zona horaria.
3. **User accounts:** identificar cuentas sospechosas y sus SIDs.
4. **Processes:** encontrar procesos maliciosos, sus rutas y puertos.
5. **Persistence:** revisar claves de registro (Userinit, netshell) y servicios.
6. **Network:** analizar procesos padre, conexiones SSH y scripts de proxy.

**Lección:** la caza de amenazas en Windows requiere revisar artefactos clave (perfiles, registro, servicios, procesos) para un triage eficiente y descubrimiento accionable.

---

*Documentación para propósitos educativos y registro de CTF.*
