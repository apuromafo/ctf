# Splunk_ Exploring SPL
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `splunkexploringspl` |
| **Link** | [TryHackMe](https://tryhackme.com/room/splunkexploringspl) |
| **Sección** | Blue Team / SIEM / Splunk |
| **Fuente** | TryHackMe |
| **Componentes** | Splunk, SPL, index=windowslogs, stats/chart, EventCode, Sysmon, Windows Security Logs |
| **Impacto** | Aprende a construir búsquedas SPL para investigar telemetría Windows (Sysmon/Security) y responder preguntas de hunting sobre procesos, cuentas y eventos. |
---
**Contexto:** Esta room enseña a explorar datos en Splunk mediante **SPL (Search Processing Language)**. Usando el índice `windowslogs` (telemetría Windows con Sysmon y logs de seguridad), se practican búsquedas con filtros por `index`, `EventCode`, `Image`, comandos de agregación como `chart count(...) by ...`, `stats` y la correlación de eventos. El fin es construir consultas eficaces para investigar actividad sospechosa y responder preguntas de triage.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de la sala y de los objetivos de aprendizaje de SPL. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: Data Overview / Visión general de los datos
**Explicación:** Exploración inicial de los índices y hosts disponibles en Splunk. Se identifica el host relevante del entorno: **cyber-host**.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Observation of the dataset (no answer required). | `No answer needed` |
| 2. What is the name of the host? | `cyber-host` |
### Task 3: SPL Basics / Fundamentos de SPL
**Explicación:** Construcción de una búsqueda SPL básica para agregar eventos. La consulta `index=windowslogs | chart count(EventCode) by Image` cuenta los eventos por imagen de proceso; se identifican también una IP (`172.90.12.11`) y un recuento (`134`) observados en los resultados.
- Query: `index=windowslogs | chart count(EventCode) by Image`
- IP: `172.90.12.11`
- Conteo: `134`
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the SPL query used to chart EventCode by Image? | `index=windowslogs \| chart count(EventCode) by Image` |
| 2. What is the source IP observed? | `172.90.12.11` |
| 3. What is the observed count? | `134` |
### Task 4: Searching Events / Búsqueda de eventos
**Explicación:** Aplicación de filtros por `EventCode`, `Image`, usuario e IP para acotar los eventos. Las respuestas corresponden a recuentos y valores observados en el índice.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the observed value? | `4` |
| 2. What is the observed value? | `4` |
| 3. What is the source IP? | `172.90.12.11` |
| 4. What is the observed count? | `0` |
| 5. What is the observed value? | `12256` |
### Task 5: Process Analysis / Análisis de procesos
**Explicación:** Investigación de eventos de proceso. El EventCode `4103` corresponde a `PowerShell` Script Block Logging (registro de bloques de script de PowerShell). Se identifica la cuenta de usuario **Salena.Adam**.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the EventCode related to PowerShell script block logging? | `4103` |
| 2. What is the username observed? | `Salena.Adam` |
### Task 6: Account Activity / Actividad de cuentas
**Explicación:** Correlación de la actividad de un usuario con eventos del sistema. Se identifica el usuario **James.browne**, el EventCode `4103` y el proveedor `Microsoft-Windows-Directory-Services-SAM` (relacionado con la creación/cambio de cuentas locales).
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the username observed? | `James.browne` |
| 2. What is the EventCode? | `4103` |
| 3. What is the provider name? | `Microsoft-Windows-Directory-Services-SAM` |
### Task 7: Hunting / Caza
**Explicación:** Búsqueda de actividad relevante dentro del índice Windows. Las respuestas son valores observados al filtrar los eventos del usuario y del entorno.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the observed value? | `196` |
| 2. What is the username? | `James` |
| 3. What is the observed value? | `70` |
### Task 8: Conclusion / Conclusión
**Explicación:** Cierre de la sala con recomendaciones para seguir practicando SPL y búsquedas en Splunk. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conclusión de la sala (sin preguntas). | `No answer needed` |
---
**Metodología:** Identificar el índice/host → explorar los eventos → filtrar por EventCode/Image/usuario → agregar con `chart`/`stats` → correlacionar y responder las preguntas de hunting.
### Cadena de ataque / Attack Chain
```
index=windowslogs -> filtrado por EventCode/Image/usuario -> agregación (chart count by Image) -> correlación de actividad -> hallazgo
```
**Learning chain:** visión del dataset → SPL básico → filtros de eventos → análisis de procesos y cuentas → hunting con correlación.
**Lección:** *SPL permite pivotar rápidamente sobre telemetría Windows: dominar los filtros y comandos de agregación convierte millones de eventos en respuestas claras para el analista SOC.*
**MITRE ATT&CK:** T1059.001 (PowerShell), T1087 (Account Discovery), T1136.001 (Create Account: Local Account), T1078 (Valid Accounts).
**Fuente:** [TryHackMe - Splunk: Exploring SPL](https://tryhackme.com/room/splunkexploringspl)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
