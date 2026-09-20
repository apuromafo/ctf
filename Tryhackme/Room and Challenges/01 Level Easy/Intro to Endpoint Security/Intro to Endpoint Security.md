# Intro to Endpoint Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtoendpointsecurity` | https://tryhackme.com/room/introtoendpointsecurity | 01 Level Easy | TryHackMe | servicios de Windows / services.exe / wininit.exe / Sysinternals / TCPView / Event Logs (.evtx) / Sysmon / OSQuery / Wazuh / EDR | Conocer los fundamentos de la seguridad de endpoints: procesos de Windows, logs de eventos, herramientas de monitorización (TCPView, OSQuery) y análisis con un laboratorio estático de investigación de amenazas. |

---

**Contexto:** La room (perteneciente al camino SOC Level 1) introduce la seguridad de endpoints, disciplina centrada en la monitorización y protección del punto final. Cubre los fundamentos de Windows (el proceso padre normal de `services.exe` es **wininit.exe**), herramientas de red como **TCPView** (Sysinternals), el registro y la monitorización (**logs .evtx** en `C:\Windows\System32\winevt\Logs`, Sysmon, la CLI **osqueryi** y el significado de **EDR** = endpoint detection and response), y termina con un laboratorio estático de análisis de logs donde se investiga y remedia una amenaza en cuatro equipos para obtener la flag.

> **ES:** Fundamentos de endpoint security: proceso services.exe/wininit.exe, TCPView, Event Logs .evtx, OSQuery, EDR, y un laboratorio simulado de análisis de logs con deteccion y remediacion.
> **EN:** Endpoint security fundamentals: services.exe/wininit.exe, TCPView, .evtx event logs, OSQuery, EDR, and a simulated log-analysis lab with detection and remediation.

## Solucionario

### Task 1: Room Introduction / Introducción a la room

**Explicación:** Se presenta la room dentro del camino SOC Level 1 y los objetivos: fundamentos, metodología y herramientas para la monitorización de la seguridad de endpoints. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have read the introduction task. / He leído la tarea de introducción. | `No answer needed` |

### Task 2: Endpoint Security Fundamentals / Fundamentos de seguridad de endpoints

**Explicación:** En Windows, los servicios del sistema se ejecutan bajo el proceso `services.exe`, cuyo proceso padre normal es **wininit.exe** (Windows Initialization). Una desviación de este árbol de procesos es un signo de actividad anómala. Se presenta también la utilidad de red **TCPView**, una herramienta de Sysinternals que muestra en tiempo real las conexiones de red de cada proceso (PID, direcciones, estado).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the normal parent process of services.exe? / ¿Cuál es el proceso padre normal de services.exe? | `wininit.exe` |
| 2 | What is the name of the network utility tool introduced in this task? / ¿Cómo se llama la herramienta de utilidad de red presentada en esta tarea? | `TCPView` |

### Task 3: Endpoint Logging and Monitoring / Registro y monitorización de endpoints

**Explicación:** Las evidencias de actividad en Windows se registran en los Event Logs. Los archivos `.evtx` residen típicamente en **C:\Windows\System32\winevt\Logs**. Para interrogar el sistema a modo de base de datos se usa **OSQuery**: el comando para entrar en su CLI es **osqueryi**. Los Endpoint Detection and Response (EDR) son soluciones que combinan monitorización y respuesta: **EDR** significa **endpoint detection and response**. También se mencionan Sysmon (System Monitor) y Wazuh como EDR open source.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Where do the Windows Event logs (.evtx files) typically reside? / ¿Dónde residen normalmente los archivos de registro de eventos de Windows (.evtx)? | `C:\Windows\System32\winevt\Logs` |
| 2 | Provide the command used to enter OSQuery CLI. / Proporciona el comando para entrar en la CLI de OSQuery. | `osqueryi` |
| 3 | What does EDR mean? Provide the answer in lowercase. / ¿Qué significa EDR? Responde en minúsculas. | `endpoint detection and response` |

### Task 4: Endpoint Log Analysis / Análisis de logs de endpoints

**Explicación:** El análisis combina correlación de eventos (Event Correlation) y establecimiento de líneas base (Baselining): conocer el comportamiento normal de cada activo permite detectar desviaciones. En el laboratorio estático (botón View Site) se sigue la investigación de una amenaza en cuatro equipos: se aplica la remediación en cada equipo (botón Remediate) y se abre la flag que queda en el escritorio del entorno simulado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click on the green View Site button in this task to open the Static Site Lab and start investigating the threat by following the provided instructions. / Pulsa el botón View Site para abrir el laboratorio estático y comienza a investigar la amenaza siguiendo las instrucciones. | `No answer needed` |
| 2 | Provide the flag for the simulated investigation activity. / Proporciona la flag de la actividad de investigación simulada. | `THM{3ndp01nt_s3cur1ty!}` |

### Task 5: Conclusion / Conclusión

**Explicación:** Cierre de la room: repaso de lo aprendido en la investigación simulada (detección, correlación, remediación) y recursos del camino SOC Level 1. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have completed the Introduction to Endpoint Security Monitoring room. / He completado la room Intro to Endpoint Security Monitoring. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the normal parent process of services.exe? | `wininit.exe` |
| 2 | What is the name of the network utility tool introduced in this task? | `TCPView` |
| 3 | Where do the Windows Event logs (.evtx files) typically reside? | `C:\Windows\System32\winevt\Logs` |
| 4 | Provide the command used to enter OSQuery CLI. | `osqueryi` |
| 5 | What does EDR mean? Provide the answer in lowercase. | `endpoint detection and response` |
| 6 | Provide the flag for the simulated investigation activity. | `THM{3ndp01nt_s3cur1ty!}` |

---

**Metodología:** Del árbol de procesos a la investigación real: (1) conocer los procesos de Windows y su genealogía (services.exe -> wininit.exe) y herramientas de red como TCPView; (2) saber dónde viven los logs de eventos (.evtx) y cómo consultar el sistema con OSQuery; (3) entender el papel de un EDR (endpoint detection and response); (4) aplicar correlación de eventos y baselining en el laboratorio: detectar la amenaza, remediarla en los cuatro equipos y recoger la flag.

### Cadena de ataque / Attack Chain

```text
services.exe (padre anômalo vs wininit.exe) -> TCPView (conexiones por proceso) -> .evtx logs -> OSQuery (osqueryi) -> EDR (detección y respuesta) -> correlación + baselining -> remediación (4 equipos) -> flag
```

**Learning chain:** Procesos de Windows -> TCPView -> Event Logs/Sysmon -> OSQuery -> EDR -> análisis de logs -> remediacion.

**Lección:** *Los endpoints no delatan solo por el malware que ejecutan, sino por el linaje de sus procesos: un services.exe sin padre wininit.exe o una conexión fuera de la línea base pueden ser más fiables que cualquier firma.*

**MITRE ATT&CK:** T1543 (Create or Modify System Process), T1059.003 (Windows Command Shell), T1036 (Masquerading)

**Fuente:** [TryHackMe - Intro to Endpoint Security](https://tryhackme.com/room/introtoendpointsecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.