# Detection and Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `detectionandanalysis` | https://tryhackme.com/room/detectionandanalysis | Incident Response | TryHackMe | Validation, Scoping, IOC Tracker, Ticketing, EntraID logs, Phishing analysis | Segunda fase del ciclo IR NIST |

---

**Contexto:** Segunda fase del ciclo de vida IR: detección y análisis. Cubre validación de incidentes, alcance (scoping), triggers IR, inventario de activos, tracker de IOCs y laboratorio práctico con análisis de phishing e intrusión en Entra ID.

> **ES:** Segunda fase del ciclo de respuesta a incidentes: detección y análisis, validación, scoping, triggers IR, inventario de activos, tracker de IOCs, ticketing y laboratorio con phishing e intrusión en Entra ID.
> **EN:** Second phase of the incident response lifecycle: detection and analysis, validation, scoping, IR triggers, asset inventory, IOC tracker, ticketing, and a practical lab with phishing and an Entra ID intrusion.

## Solucionario

### Task 2: Detección y análisis / Detection and Analysis

**Explicación:** Se distinguen las dos primeras acciones de esta fase del ciclo IR. La detección (Detection) confirma que un incidente de seguridad realmente ocurrió, mientras que el análisis (Analysis) determina el alcance completo del incidente, incluyendo cuentas, sistemas y datos afectados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Proceso de confirmar que un incidente de seguridad realmente ocurrió | `Detection` |
| 2 | Proceso de entender el alcance completo de un incidente | `Analysis` |

### Task 3: Triggers IR y comunicación / IR Triggers and Communication

**Explicación:** Se repasan los eventos que disparan la respuesta a incidentes y la importancia de registrar cada acción durante la investigación en sistemas de ticketing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tipo de trigger cuando un proveedor de inteligencia notifica de un compromiso | `Third-party notification` |
| 2 | Sistema que debe usarse para registrar cada acción durante la investigación IR | `Ticketing systems` |

### Task 4: Inventario de activos y tracker de IOCs / Asset Inventory and IOC Tracker

**Explicación:** Se define el concepto de IOC y la herramienta que mantiene un registro continuo de los indicadores maliciosos observados en la organización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa IOC? | `Indicator of Compromise` |
| 2 | Herramienta que proporciona registro continuo de indicadores maliciosos | `IOC Tracker` |

### Task 5: Contexto del incidente actual / Current Incident Context

**Explicación:** Se confirma que el alumno está listo para abordar las tareas prácticas de detección y análisis del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Estoy listo para tareas prácticas | `Completar` |

### Task 6: Práctica de detección / Detection Practical

**Explicación:** Se investigan los sign-ins sospechosos de Laura Chen en Entra ID: la IP de origen es `223.123.4.50` desde Ámsterdam, con un primer acceso sospechoso el `2026-03-30 04:41:30 PM`. El email de phishing recibido tiene por asunto `HR Policy Update — Immediate Action Required` y procede del dominio `nexus-verify.thm`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | IP de origen de los eventos de inicio de sesión sospechosos | `223.123.4.50` |
| 2 | Ciudad de origen del sign-in sospechoso | `Amsterdam` |
| 3 | Timestamp exacto del primer sign-in sospechoso en Laura Chen | `2026-03-30 04:41:30 PM` |
| 4 | Asunto del email de phishing entregado a Laura Chen | `HR Policy Update — Immediate Action Required` |
| 5 | Dominio del remitente del email de phishing | `nexus-verify.thm` |

### Task 7: Práctica de análisis / Analysis Practical

**Explicación:** Se analiza el alcance del incidente en Nexus Financial: hay `2` cuentas con actividad desde la IP del atacante, la segunda cuenta comprometida es `k.patel@nexusfinancial.thm`, se crea la regla de bandeja de entrada `Junk Filter Update` en Laura Chen y `2` empleados recibieron el email de phishing inicial.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cuentas de Nexus Financial con actividad desde IP del atacante | `2` |
| 2 | Email de la segunda cuenta comprometida | `k.patel@nexusfinancial.thm` |
| 3 | Nombre de la regla de inbox creada en Laura Chen | `Junk Filter Update` |
| 4 | Empleados que recibieron el email de phishing inicial | `2` |

### Task 8: Conclusión / Conclusion

**Explicación:** Se cierra la fase de detección y análisis confirmando que se está listo para continuar con la fase de respuesta y recuperación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Great work! Ready for Response and Recovery | `Completar` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Proceso de confirmar que un incidente de seguridad realmente ocurrió | `Detection` |
| 2 | Proceso de entender el alcance completo de un incidente | `Analysis` |
| 3 | Tipo de trigger cuando un proveedor de inteligencia notifica de un compromiso | `Third-party notification` |
| 4 | Sistema que debe usarse para registrar cada acción durante la investigación IR | `Ticketing systems` |
| 5 | ¿Qué significa IOC? | `Indicator of Compromise` |
| 6 | Herramienta que proporciona registro continuo de indicadores maliciosos | `IOC Tracker` |
| 7 | Estoy listo para tareas prácticas | `Completar` |
| 8 | IP de origen de los eventos de inicio de sesión sospechosos | `223.123.4.50` |
| 9 | Ciudad de origen del sign-in sospechoso | `Amsterdam` |
| 10 | Timestamp exacto del primer sign-in sospechoso en Laura Chen | `2026-03-30 04:41:30 PM` |
| 11 | Asunto del email de phishing entregado a Laura Chen | `HR Policy Update — Immediate Action Required` |
| 12 | Dominio del remitente del email de phishing | `nexus-verify.thm` |
| 13 | Cuentas de Nexus Financial con actividad desde IP del atacante | `2` |
| 14 | Email de la segunda cuenta comprometida | `k.patel@nexusfinancial.thm` |
| 15 | Nombre de la regla de inbox creada en Laura Chen | `Junk Filter Update` |
| 16 | Empleados que recibieron el email de phishing inicial | `2` |
| 17 | Great work! Ready for Response and Recovery | `Completar` |

---

**Metodología:** Se aplica la segunda fase del ciclo IR (NIST): primero se validan los sign-ins sospechosos de Laura Chen en Entra ID (IP `223.123.4.50`, origen Ámsterdam, primer acceso `2026-03-30 04:41:30 PM`), se registra la investigación en el sistema de ticketing y se alimenta el IOC Tracker. El análisis del phishing revela el asunto `HR Policy Update — Immediate Action Required` y el dominio `nexus-verify.thm`. En el análisis del alcance se identifican las `2` cuentas afectadas (incluida `k.patel@nexusfinancial.thm`), la regla de inbox `Junk Filter Update` y los `2` empleados que recibieron el correo inicial.

### Cadena de ataque / Attack Chain

```text
Phishing desde nexus-verify.thm (asunto HR Policy Update — Immediate Action Required) -> 2 empleados afectados -> sign-ins sospechosos en Entra ID (223.123.4.50, Amsterdam, 2026-03-30 04:41:30 PM) -> regla de inbox Junk Filter Update en Laura Chen -> 2 cuentas comprometidas en Nexus Financial -> Detección y Análisis (validación, scoping, IOC Tracker, ticketing) -> Respuesta y Recuperación
```

**Learning chain:** Detección/Análisis → Validación → Scoping → Triggers IR → Ticketing → Inventario de activos → IOC Tracker → Análisis de phishing → Análisis de intrusión en Entra ID.

**Lección:** *La detección solo confirma que el incidente ocurrió; es el análisis el que dimensiona su alcance, y sin un registro sistemático (ticketing) y un tracker de IOCs la reconstrucción completa del compromiso se vuelve inviable.*

**MITRE ATT&CK:** T1566 (Phishing), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1110 (Brute Force)

**Fuente:** [TryHackMe - Detection and Analysis](https://tryhackme.com/room/detectionandanalysis)

> **Fuente original / Original source:** https://simontaplin.net/2026/06/10/answers-for-the-tryhackme-detection-and-analysis-room/
> **Fuente original / Original source:** https://medium.com/@sudoroot523/tryhackme-detection-and-analysis-8f4508665146
> **Fuente original / Original source:** https://medium.com/@lawvye/detection-and-analysis-thm-tryhackme-walkthrough-7523715d5475

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.