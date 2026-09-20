# Sigma
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `sigma` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sigma) |
| **Sección** | Blue Team / Detection Engineering / Sigma |
| **Fuente** | TryHackMe |
| **Componentes** | Sigma, Sigmac, pySigma, Sysmon, Windows Event Logs, Detection Rules, YAML |
| **Impacto** | Aprende a escribir, estructurar y convertir reglas Sigma en consultas para distintos backends SIEM, además de aplicar una regla Sigma para cazar actividad de ransomware (Purelocker) en telemetría Sysmon. |
---
**Contexto:** Sigma es un lenguaje abierto y genérico para describir detecciones de logs basadas en firmas, de forma independiente del SIEM. Las reglas se escriben en YAML con una estructura clara (metadatos, detección, campos y condición) y se traducen a consultas específicas de cada plataforma mediante herramientas como **Sigmac** o **pySigma**. Esta room enseña la anatomía de una regla Sigma y el flujo de conversión, finalizando con un reto práctico de escritura de reglas.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de los objetivos de la sala: entender qué es Sigma, cómo se estructura una regla y cómo convertirla a las consultas de distintos SIEM. No hay preguntas técnicas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: Sigma Overview / Visión general de Sigma
**Explicación:** Se introduce el propósito de Sigma como formato de firma genérico y portable. Explica que una regla Sigma es un archivo YAML con metadatos (title, id, status, description, author, logsource, detection, fields) y que puede convertirse a consultas de SIEM con herramientas de conversión. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Visión general de Sigma (sin preguntas). | `No answer needed` |
### Task 3: Rule Structure / Estructura de la regla
**Explicación:** Anatomía de una regla Sigma. El campo `status` admite valores como `stable`, `test`, `experimental`, `deprecated` y `unsupported`; `experimental` es el estado para reglas nuevas/poco probadas. La sección `detection` usa **identificadores de búsqueda** (search identifiers) para agrupar condiciones, y los **lists and maps** permiten definir listas de valores y mapeos reutilizables dentro de la regla.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the status used for rules that are experimental? | `experimental` |
| 2. What is the name of the identifiers used in the detection section? | `search identifiers` |
| 3. What can be used to define lists and maps of values? | `lists and maps` |
### Task 4: Sigmac / Conversión con Sigmac
**Explicación:** **Sigmac** es la herramienta de conversión de reglas Sigma a queries de SIEM (Splunk, Elasticsearch, etc.). En la versión mostrada en la sala, la build corresponde a `Jun 28, 2022 @ 22:19:00` y la versión del propio Sigmac es `7.0.10`. El flujo típico es `sigmac -t <backend> rule.yml` para generar la consulta destino.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the name of the tool used to convert Sigma rules? | `Sigmac` |
| 2. What is the build date of Sigmac? | `Jun 28, 2022 @ 22:19:00` |
| 3. What is the version of Sigmac? | `7.0.10` |
### Task 5: Converting rules / Conversión de reglas
**Explicación:** Práctica de conversión de una regla Sigma usando Sigmac hacia un backend concreto, comprobando cómo la sección `detection` y la `condition` se traducen a la sintaxis de la plataforma destino. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conversión de una regla Sigma con Sigmac (sin preguntas). | `No answer needed` |
### Task 6: Writing Rules / Escribir reglas
**Explicación:** Reto práctico de escritura de una regla Sigma para detectar la actividad de **Purelocker** (ransomware). Se identifica la línea de comando de `schtasks.exe`, el tipo de evento de proceso (`spawn`), la hora de la ejecución (`20:10`), el logsource de eventos de fichero (`file_event`), el nombre del archivo de nota de rescate (`YOUR_FILES.txt`), el número de reglas/sucesos observados (`11`) y la técnica asociada (`T1486 - Purelocker Ransom Note`).
- `\schtasks.exe`
- `spawn`
- `20:10`
- `file_event`
- `YOUR_FILES.txt`
- `11`
- `T1486 - Purelocker Ransom Note`
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the command line of the scheduled task? | `\schtasks.exe` |
| 2. What is the event type of the process creation? | `spawn` |
| 3. At what time was the scheduled task executed? | `20:10` |
| 4. Which logsource category relates to file events? | `file_event` |
| 5. What is the name of the ransom note file? | `YOUR_FILES.txt` |
| 6. How many events were observed? | `11` |
| 7. What is the ATT&CK technique related to Purelocker? | `T1486 - Purelocker Ransom Note` |
### Task 7: Conclusion / Conclusión
**Explicación:** Cierre de la sala con recomendaciones para seguir practicando la escritura de reglas Sigma y su integración en pipelines de detección. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conclusión de la sala (sin preguntas). | `No answer needed` |
---
**Metodología:** Comprender la estructura YAML de Sigma → identificar logsource y campos → definir search identifiers y condition → convertir con Sigmac al backend destino → escribir una regla propia a partir de telemetría Sysmon → validar la detección.
### Cadena de ataque / Attack Chain
```
schtasks.exe (persistencia/ejecución programada) -> despliegue de Purelocker -> cifrado y creación de YOUR_FILES.txt -> detección mediante regla Sigma (file_event + process spawn)
```
**Learning chain:** concepto Sigma → estructura de la regla → conversión con Sigmac → regla personalizada → detección de ransomware.
**Lección:** *Sigma estandariza las detecciones: una sola regla en YAML puede traducirse a múltiples SIEM, lo que facilita compartir, versionar y reutilizar lógica de detección entre organizaciones.*
**MITRE ATT&CK:** T1053.005 (Scheduled Task/Job: Scheduled Task), T1486 (Data Encrypted for Impact), T1204 (User Execution), T1059.003 (Windows Command Shell).
**Fuente:** [TryHackMe - Sigma](https://tryhackme.com/room/sigma)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
