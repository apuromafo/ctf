# Windows Network Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `windowsnetworkanalysis` | [TryHackMe](https://tryhackme.com/room/windowsnetworkanalysis) | 01 Level Easy | TryHackMe | SRUM / Firewall logs / Get-NetTCPConnection / Get-DnsClientCache / qwinsta / netstat / SMB | Análisis de red en Windows: cmdlets de conexiones, caché DNS, sesiones RDP, netstat, SRUM y comparticiones SMB para detectar compromisos |

---

**Contexto:** Sala centrada en la búsqueda de artefactos de un compromiso en una máquina Windows a través de la red. Se analiza la base de datos SRUM, los logs de Firewall, las conexiones TCP activas con `Get-NetTCPConnection`, la caché DNS, las sesiones RDP con `qwinsta`, los flags de `netstat` (`-b`, `-o`, `>`), la exfiltración de datos y las comparticiones SMB sospechosas.

> **ES:** La sala enseña forensia de red en Windows: monitor de uso de recursos (SRUM), logs de Firewall, conexiones activas (Get-NetTCPConnection), caché DNS, sesiones RDP (qwinsta), netstat y análisis de comparticiones SMB para identificar una reverse shell y exfiltración.
> **EN:** This room teaches Windows network forensics: the System Resource Usage Monitor (SRUM), Firewall logs, active connections (Get-NetTCPConnection), DNS cache, RDP sessions (qwinsta), netstat and SMB shares analysis to spot a reverse shell and data exfiltration.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¡Listo para comenzar! | `No answer needed` |

### Task 2: Requisitos previos / Pre-requisites
**Explicación:** Se repasan dos fuentes de datos: el System Resource Usage Monitor, que registra las estadísticas de los últimos 30 a 60 días, y el directorio donde Windows escribe los logs de Firewall: `C:\Windows\System32\LogFiles\Firewall`. Contenido original de la sala (verbatim): `System Resource Usage Monitor`, `C:\Windows\System32\LogFiles\Firewall`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es el nombre completo de la característica de Windows que rastrea las últimas estadísticas de 30 a 60 días del sistema? | `System Resource Usage Monitor` |
| ¿Cuál es la ruta completa al directorio donde Windows escribe los logs de Firewall? | `C:\Windows\System32\LogFiles\Firewall` |

### Task 3: Comandos básicos / Basic Commands
**Explicación:** Se practican los comandos y cmdlets básicos de análisis de red: `Get-NetTCPConnection` para conexiones TCP activas, `Get-DnsClientCache` para la caché DNS y `qwinsta` para listar las sesiones RDP activas. Contenido original de la sala (verbatim): `Get-NetTCPConnection`, `Get-DnsClientCache`, `qwinsta`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué cmdlet se puede usar para mostrar las conexiones TCP activas? | `Get-NetTCPConnection` |
| ¿Qué cmdlet se puede usar para mostrar la caché DNS del host? | `Get-DnsClientCache` |
| ¿Qué comando se puede usar para listar todas las sesiones RDP activas del host? | `qwinsta` |

### Task 4: netstat / netstat
**Explicación:** Se estudian los flags de `netstat`: `-b` muestra el ejecutable responsable de la conexión, `-o` muestra los PID asociados a cada conexión y el carácter `>` permite guardar la salida en un archivo de texto. Contenido original de la sala (verbatim): `-b`, `-o`, `>`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué flag de netstat podemos usar para mostrar el ejecutable responsable de una conexión? | `-b` |
| ¿Qué flag usaríamos para mostrar todas las conexiones TCP con su PID asociado? | `-o` |
| ¿Qué carácter especial podemos usar para guardar la salida de netstat en un archivo de texto? | `>` |

### Task 5: Análisis / Analysing
**Explicación:** Se analiza la máquina comprometida: hay una reverse shell escuchando en el puerto `4444` (proceso `pythonw.exe`), se ha añadido el dominio `attackerc2.thm` al archivo hosts, la base de datos SRUM revela un proceso de exfiltración con ruta `\device\harddiskvolume3\program files\updater\exfil.exe` y la compartición SMB que destaca es `confidential`. Contenido original de la sala (verbatim): `4444`, `pythonw.exe`, `attackerc2.thm`, `\device\harddiskvolume3\program files\updater\exfil.exe`, `confidential`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Usa el cmdlet Get-NetTCPConnection para listar las conexiones activas. Un puerto popular de reverse shells está activo. ¿Cuál es el número de puerto? | `4444` |
| ¿Cuál es el nombre del proceso que se conecta al servidor C2? | `pythonw.exe` |
| ¿Qué dominio se ha añadido al archivo hosts de la estación de trabajo? | `attackerc2.thm` |
| Analiza la base de datos SRUM. Hay otro proceso que envió una gran cantidad de bytes, indicando exfiltración. ¿Cuál es la ruta completa del proceso (según figura en SRUM)? | `\device\harddiskvolume3\program files\updater\exfil.exe` |
| Por último, analiza las comparticiones SMB de la máquina. ¿Cuál es el nombre de la compartición que destaca? | `confidential` |

### Task 6: Conclusión / Conclusion
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para continuar? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Listo para comenzar! | `No answer needed` |
| 2 | Característica que rastrea 30-60 días de estadísticas | `System Resource Usage Monitor` |
| 3 | Ruta del directorio de logs de Firewall | `C:\Windows\System32\LogFiles\Firewall` |
| 4 | Cmdlet para conexiones TCP activas | `Get-NetTCPConnection` |
| 5 | Cmdlet para mostrar la caché DNS | `Get-DnsClientCache` |
| 6 | Comando para listar sesiones RDP activas | `qwinsta` |
| 7 | Flag de netstat para el ejecutable responsable | `-b` |
| 8 | Flag de netstat para mostrar los PID | `-o` |
| 9 | Carácter para guardar la salida en un archivo | `>` |
| 10 | Puerto popular de reverse shells activo | `4444` |
| 11 | Proceso que conecta con el C2 | `pythonw.exe` |
| 12 | Dominio añadido al archivo hosts | `attackerc2.thm` |
| 13 | Ruta del proceso de exfiltración en SRUM | `\device\harddiskvolume3\program files\updater\exfil.exe` |
| 14 | Compartición SMB sospechosa | `confidential` |
| 15 | ¿Preparado para continuar? | `No answer needed` |

---

**Metodología:** Se inspecciona la máquina desde PowerShell y CMD: `Get-NetTCPConnection` para detectar la reverse shell, `Get-DnsClientCache` y el archivo hosts para el dominio C2, `qwinsta` para sesiones RDP, `netstat -b -o` para procesos y PIDs, SRUM (System Resource Usage Monitor) para localizar la exfiltración y `Get-SmbConnection` para identificar la compartición anómala.

### Cadena de ataque / Attack Chain

```text
Reverse shell (pythonw.exe) en puerto 4444 -> dominio añadido al hosts (attackerc2.thm) -> sesiones RDP (qwinsta) -> netstat -b -o -> SRUM: exfiltración (\device\harddiskvolume3\program files\updater\exfil.exe) -> compartición SMB anómala (confidential)
```

**Learning chain:** System Resource Usage Monitor (SRUM) --> Firewall logs --> Get-NetTCPConnection --> Get-DnsClientCache --> qwinsta --> netstat -b -o --> hosts file (attackerc2.thm) --> SRUM exfiltration (exfil.exe) --> SMB share (confidential)

**Lección:** *La evidencia de red en Windows no se encuentra en un solo lugar: correlacionando conexiones TCP, caché DNS, hosts file, SRUM y comparticiones SMB es posible reconstruir una reverse shell y un canal de exfiltración.*

**MITRE ATT&CK:** T1041 (Exfiltration Over C2 Channel)

**Fuente:** [TryHackMe - Windows Network Analysis](https://tryhackme.com/room/windowsnetworkanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.