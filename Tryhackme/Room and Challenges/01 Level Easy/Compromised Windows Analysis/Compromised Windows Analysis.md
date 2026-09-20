# Compromised Windows Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (DFIR) | `compromisedwindowsanalysis` | https://tryhackme.com/room/compromisedwindowsanalysis | 01 Level Easy | TryHackMe | Timeline Explorer / Scheduled Tasks / LNK (LECmd) / Prefetch (PECmd) / AmcacheParser / Windows Event Logs / RDP / Windows Defender | Investigar una estación Windows comprometida y reconstruir la cadena completa del ataque (RDP, Defender desactivado, RAR malicioso, ejecutable, persistencia y C2). |

---

**Contexto:** Room de forensia/DFIR en Windows. TKM es una startup tecnológica cuyo usuario Aashir generó tráfico SSH sospechoso hacia una IP maliciosa cada minuto; además, Windows Defender está desactivado. Hay que analizar la estación en profundidad con artefactos forenses (scheduled tasks, archivos LNK, prefetch, Amcache y logs de eventos) para determinar la causa raíz, la persistencia y la línea temporal del ataque.

> **ES:** Analiza una estación Windows comprometida: huellas del atacante, persistencia, ejecución de malware y análisis de logs de eventos para reconstruir la cronología completa del incidente.
> **EN:** Investigate a compromised Windows workstation: attacker footprints, persistence, malicious file execution and Windows event log analysis to rebuild the full attack timeline.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta el caso: TKM, con Joe como ingeniero junior de seguridad. El 29 de marzo de 2025 se observa tráfico SSH sospechoso desde el host del empleado Aashir hacia una IP maliciosa, repitiéndose cada minuto y siendo rechazado. El usuario estaba desprevenido y Windows Defender estaba desactivado. Pregunta: el usuario cuyo sistema generó el tráfico SSH sospechoso es `Aashir`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario cuyo sistema generó tráfico SSH sospechoso hacia una IP maliciosa? / What is the user's name whose system generated suspicious SSH traffic to a malicious IP? | `Aashir` |

### Task 2: Preparación / Setup

**Explicación:** Se arranca la máquina del laboratorio (vista split-screen o acceso al host comprometido). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Arrancar/preparar el laboratorio. / Start/set up the lab machine. | `No answer needed` |

### Task 3: Timeline Explorer para visualización / Timeline Explorer for Visualization

**Explicación:** Timeline Explorer es una herramienta de Eric Zimmerman que permite ver ficheros CSV de forma cómoda y aplicar filtros. Las herramientas de los próximos pasos (LECmd, PECmd, AmcacheParser) generan CSV que se importan aquí para visualizar los datos. La herramienta que facilita analizar archivos CSV es `Timeline Explorer`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta hace más fácil analizar archivos CSV? / Which tool makes it easier to analyze CSV files? | `Timeline Explorer` |

### Task 4: Investigando la persistencia / Investigating Persistence

**Explicación:** El prompt que Aashir veía cada minuto sugiere una tarea programada. En el Programador de tareas (o en `C:\Windows\System32\Tasks`) se encuentra la tarea maliciosa `CNC`, que conecta con el servidor de mando y control mediante SSH a intervalos regulares. La tarea se creó a las `10:29`; la IP maliciosa a la que se hacen las peticiones SSH es `101.55.125.10`.

```text
Task Scheduler -> tarea "CNC" creada por el atacante (10:29, repetición cada minuto)
schtasks /query /tn CNC  # acción: ssh hacia la IP maliciosa
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de la tarea programada creada por el atacante? / What is the name of the scheduled task created by the attacker? | `CnC` |
| 2 | ¿Cuál es la IP del servidor C2 malicioso al que se hacen las peticiones SSH? / What is the IP of the malicious C2 server that the SSH requests are made to? | `101.55.125.10` |

### Task 5: Investigando archivos accedidos recientemente / Investigating Recently Accessed Files

**Explicación:** Se revisan los archivos LNK de `C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent Items`, analizándolos con LECmd para extraer su información como CSV y visualizarla en Timeline Explorer. El archivo RAR creado durante el ataque es `Cursed.rar`, creado el `2025-03-29 10:26:07` (poco antes de la tarea programada de las 10:29).

```powershell
.\LECmd.exe -d C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent --csvf Parsed-LNK.csv --csv C:\Users\Administrator\Desktop
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del archivo RAR creado durante el ataque? / What is the name of the RAR file created during the attack? | `Cursed.rar` |
| 2 | ¿Cuándo se creó el archivo RAR en el sistema? Formato YYYY-MM-DD HH:MM:SS. / When was the RAR file created in the system? Format YYYY-MM-DD HH:MM:SS. | `2025-03-29 10:26:07` |

### Task 6: Investigando la ejecución de archivos / Investigating File Execution

**Explicación:** Para ver qué se ejecutó tras acceder al RAR, se parsean los prefetch con PECmd y se busca justo después de las 10:26. El ejecutable malicioso es `Cipher.exe`, se ejecutó `2` veces y su última ejecución fue a las `2025-03-29 10:29:12`.

```powershell
.\PECmd.exe -d "C:\Windows\Prefetch" --csv C:\Users\Administrator\Desktop --csvf Prefetch-Parsed.csv
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del ejecutable malicioso? / What is the name of the malicious executable file? | `Cipher.exe` |
| 2 | ¿Cuántas veces se ejecutó este archivo? / How many times was this file executed? | `2` |
| 3 | ¿Cuándo se ejecutó este archivo? / When was this file executed? | `2025-03-29 10:29:12` |

### Task 7: La excavación del ejecutable / The Dig of Executable

**Explicación:** Con AmcacheParser se parsea `C:\Windows\appcompat\Programs\Amcache.hve` (ya preservado para la sesión del ataque) y se obtiene la ruta completa, el hash SHA1 y la última hora de ejecución del ejecutable. La ruta completa del archivo malicioso es `c:\users\administrator\desktop\cursed\cipher.exe` y su hash SHA1 es `5b15c9d9ef36cae9f24ce63eebd190ac381bb734`.

```powershell
.\AmcacheParser.exe -f "C:\Windows\appcompat\Programs\Amcache.hve" --csv C:\Users\Administrator\Desktop --csvf Amcache_Parsed.csv
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta completa del archivo malicioso? / What is the full path of the malicious file? | `c:\users\administrator\desktop\cursed\cipher.exe` |
| 2 | ¿Cuál es el hash SHA1 de este archivo? / What is the SHA1 hash of this file? | `5b15c9d9ef36cae9f24ce63eebd190ac381bb734` |

### Task 8: Análisis de logs de eventos de Windows / Windows Event Log Analysis

**Explicación:** En los logs se confirma el acceso inicial y la evasión de defensas. En `Applications and Services Logs -> Microsoft -> Windows -> Terminal-Services-RemoteConnectionManager -> Operational` se ve el login RDP exitoso (Event ID 1149) justo antes de soltar el RAR, y en `Windows Defender -> Operational` el log con Event ID 5001 indica cuándo se desactivó Defender: `10:25:14 AM`. La IP del sistema del atacante es `10.11.90.211`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuándo se desactivó Defender? Respuesta en formato de reloj de 12 horas (ej. horas:minutos:segundos AM/PM). / When was Defender disabled? Answer in 12 hour clock format. | `10:25:14 AM` |
| 2 | ¿Cuál es la IP del sistema del atacante? / What is the IP address of the attacker's system? | `10.11.90.211` |

### Task 9: Orden cronológico del ataque / Chronological Order of Attack

**Explicación:** Se reconstruye la cadena completa del atacante con todos los artefactos: acceso por RDP, desactivación de Defender, caída del RAR, apertura y ejecución del ejecutable malicioso (Cipher.exe), creación de la tarea programada persistente que conecta por SSH al C2 cada minuto, y posterior borrado de los archivos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la reconstrucción cronológica del ataque. / Read the chronological order of the attack. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del usuario cuyo sistema generó tráfico SSH sospechoso hacia una IP maliciosa? / What is the user's name whose system generated suspicious SSH traffic to a malicious IP? | `Aashir` |
| 2 | ¿Qué herramienta hace más fácil analizar archivos CSV? / Which tool makes it easier to analyze CSV files? | `Timeline Explorer` |
| 3 | ¿Cuál es el nombre de la tarea programada creada por el atacante? / What is the name of the scheduled task created by the attacker? | `CnC` |
| 4 | ¿Cuál es la IP del servidor C2 malicioso al que se hacen las peticiones SSH? / What is the IP of the malicious C2 server that the SSH requests are made to? | `101.55.125.10` |
| 5 | ¿Cuál es el nombre del archivo RAR creado durante el ataque? / What is the name of the RAR file created during the attack? | `Cursed.rar` |
| 6 | ¿Cuándo se creó el archivo RAR en el sistema? / When was the RAR file created in the system? | `2025-03-29 10:26:07` |
| 7 | ¿Cuál es el nombre del ejecutable malicioso? / What is the name of the malicious executable file? | `Cipher.exe` |
| 8 | ¿Cuántas veces se ejecutó este archivo? / How many times was this file executed? | `2` |
| 9 | ¿Cuándo se ejecutó este archivo? / When was this file executed? | `2025-03-29 10:29:12` |
| 10 | ¿Cuál es la ruta completa del archivo malicioso? / What is the full path of the malicious file? | `c:\users\administrator\desktop\cursed\cipher.exe` |
| 11 | ¿Cuál es el hash SHA1 de este archivo? / What is the SHA1 hash of this file? | `5b15c9d9ef36cae9f24ce63eebd190ac381bb734` |
| 12 | ¿Cuándo se desactivó Defender? / When was Defender disabled? | `10:25:14 AM` |
| 13 | ¿Cuál es la IP del sistema del atacante? / What is the IP address of the attacker's system? | `10.11.90.211` |

---

**Metodología:** Se combinan artefactos forenses de Eric Zimmerman y logs de Windows: Scheduled Tasks para la persistencia (CNC), LNK + LECmd para los archivos accedidos (Cursed.rar), Prefetch + PECmd para la ejecución (Cipher.exe), AmcacheParser para ruta y hash, y los logs de Terminal Services (RDP, Event ID 1149) y Windows Defender (Event ID 5001) para acceso inicial y desactivación de defensas. Con todos los tiempos se reconstruye la cronología del ataque.

### Cadena de ataque / Attack Chain

```text
RDP (10.11.90.211) -> Defender desactivado (10:25:14 AM) -> Cursed.rar (10:26:07) -> RAR abierto -> Cipher.exe ejecutado (10:29:12) -> Scheduled Task "CnC" -> SSH al C2 101.55.125.10 cada minuto -> borrado de archivos
```

**Learning chain:** Story/Caso -> Timeline Explorer (CSV) -> Scheduled Tasks (persistencia) -> LNK/LECmd (acceso) -> Prefetch/PECmd (ejecución) -> Amcache (ruta+hash) -> Event Logs (RDP + Defender) -> cronología final.

**Lección:** *Ante un Windows comprometido, correlacionar los tiempos de artefactos nativos (tareas programadas, LNK, prefetch, amcache y logs de eventos) permite reconstruir paso a paso la cadena del ataque, incluso cuando el atacante borra sus archivos.*

**MITRE ATT&CK:** T1021.001 - Remote Desktop Protocol; T1562.001 - Impair Defenses (Disable or Modify Tools); T1053.005 - Scheduled Task; T1071.001 - Application Layer Protocol

**Fuente:** [TryHackMe - Compromised Windows Analysis](https://tryhackme.com/room/compromisedwindowsanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.