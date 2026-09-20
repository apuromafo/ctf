# Preparation (IR)

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `irpreparation` | [TryHackMe](https://tryhackme.com/room/irpreparation) | Incident Response | THM | NIST SP 800-61, Chain of Custody, SIEM, Detection Gap, VM Practical | Preparación IR |

---

**Contexto:** Primera fase del ciclo NIST de respuesta a incidentes: preparación. Cubre definiciones, marcos NIST, personas/procesos/tecnología, logging y laboratorio práctico con inventario de activos.

> **ES:** Primera fase del ciclo NIST de respuesta a incidentes: definiciones, marcos de trabajo, personas/procesos/tecnología, visibilidad y logging, y un laboratorio práctico de detección.
> **EN:** First phase of the NIST incident response lifecycle: definitions, frameworks, people/processes/technology, visibility and logging, plus a practical detection lab.

## Solucionario

### T2 - What Is Incident Response

**Explicación:** Define qué es la respuesta a incidentes e introduce los conceptos de incidente y alert triage: un incidente se declara tras confirmar una amenaza y el triaje de alertas debe completarse antes de iniciar formalmente la respuesta.

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué se declara tras confirmar una amenaza? | Incident |
| ¿Qué se debe completar antes de que el IR pueda comenzar formalmente? | Alert Triage |

### T3 - IR Frameworks

**Explicación:** Presenta los marcos de respuesta a incidentes y en concreto el ciclo de vida NIST SP 800-61, con sus cuatro fases y el orden que siguen tras la contención, erradicación y recuperación.

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántas fases tiene el ciclo de vida NIST SP 800-61? | 4 |
| ¿Qué fase sigue a Containment, Eradication, and Recovery? | Post-Incident Activity |

### T4 - People, Processes, and Technology

**Explicación:** Explica los pilares de la preparación (personas, procesos y tecnología) y la necesidad de documentar la cadena de custodia de la evidencia desde su recolección hasta su almacenamiento.

| Pregunta | Respuesta |
|----------|-----------|
| Documento que rastrea el manejo de evidencia desde recolección hasta almacenamiento | Chain of Custody |

### T5 - Visibility, Logging, and Detection

**Explicación:** Relaciona visibilidad, registro de logs y detección: qué tipo de logs registran la actividad (audit logs), cómo centralizarlos en un SIEM y qué ocurre cuando existe un gap de detección por falta de reglas de alerta.

| Pregunta | Respuesta |
|----------|-----------|
| Tipo de log que registra quién, qué y cómo respondió el sistema | Audit Log |
| Plataforma centralizada para colectar y analizar logs en una organización | SIEM |
| Situación donde se recolectan logs pero no hay reglas de alerta para actividad sospechosa | Detection Gap |

### T6 - Practical (VM)

**Explicación:** Laboratorio práctico sobre el inventario de activos y los hallazgos del informe: identifica la IP del servidor de correo, los controles de autenticación ausentes, la severidad de los hallazgos, el tipo de ataque del incidente NXF-INC-001, la política de contraseñas y la configuración de auditoría del dominio.

| Pregunta | Respuesta |
|----------|-----------|
| IP del servidor de correo según inventario de activos | 10.10.10.2 |
| Control de autenticación faltante en reporte de pentest | Multi-Factor Authentication |
| Cantidad de hallazgos de alta severidad | 2 |
| Tipo de ataque registrado en NXF-INC-001 | Phishing Campaign |
| Longitud mínima de contraseña configurada | 6 |
| Configuración de auditoría para Audit account logon events | No Auditing |

| Pregunta | Respuesta |
|---|---|
| ¿Qué se declara tras confirmar una amenaza? | `Incident` |
| ¿Qué se debe completar antes de que el IR pueda comenzar formalmente? | `Alert Triage` |
| ¿Cuántas fases tiene el ciclo de vida NIST SP 800-61? | `4` |
| ¿Qué fase sigue a Containment, Eradication, and Recovery? | `Post-Incident Activity` |
| Documento que rastrea el manejo de evidencia desde recolección hasta almacenamiento | `Chain of Custody` |
| Tipo de log que registra quién, qué y cómo respondió el sistema | `Audit Log` |
| Plataforma centralizada para colectar y analizar logs en una organización | `SIEM` |
| Situación donde se recolectan logs pero no hay reglas de alerta para actividad sospechosa | `Detection Gap` |
| IP del servidor de correo según inventario de activos | `10.10.10.2` |
| Control de autenticación faltante en reporte de pentest | `Multi-Factor Authentication` |
| Cantidad de hallazgos de alta severidad | `2` |
| Tipo de ataque registrado en NXF-INC-001 | `Phishing Campaign` |
| Longitud mínima de contraseña configurada | `6` |
| Configuración de auditoría para Audit account logon events | `No Auditing` |

---

**Fuentes:** https://simontaplin.net/2026/06/11/answers-for-the-tryhackme-preparation-room/ | https://medium.com/@lawvye/preparation-thm-tryhackme-practical-walkthrough-b81f0eacf4ee

---

**Metodología:** Estudio del ciclo de vida NIST SP 800-61, análisis de los pilares de la preparación (personas, procesos y tecnología), revisión de visibilidad y logging (audit logs, SIEM, detection gaps) y laboratorio práctico sobre el inventario de activos y los hallazgos del informe de pentest.

### Cadena de ataque / Attack Chain
Preparación de la organización: definición de políticas y marcos (NIST SP 800-61) -> Establecimiento de personas, procesos y tecnología (Chain of Custody) -> Despliegue de visibilidad y logging (Audit Log, SIEM) -> Detección de gaps de detección con logs sin reglas de alerta -> Ejercicio práctico: correlación del inventario de activos (10.10.10.2) con los hallazgos (MFA ausente, phishing NXF-INC-001) y la configuración de auditoría.

**Learning chain:** Ciclo de vida NIST SP 800-61, triaje de alertas, cadena de custodia, audit logs/SIEM/detection gaps y correlación de inventario de activos con hallazgos de pentest.

**Lección:** *La preparación (políticas, visibilidad y logs bien configurados) determina la calidad de toda la respuesta a incidentes: sin reglas de alerta ni inventario, los incidentes pasan desapercibidos.*

**MITRE ATT&CK:** Ciclo de vida de manejo de incidentes NIST SP 800-61 (Preparation, Detection & Analysis, Containment Eradication & Recovery, Post-Incident Activity). En ATT&CK, la visibilidad y el logging preparan la detección de técnicas como T1566 Phishing (incidente NXF-INC-001) y T1110 Brute Force.

**Fuente:** [TryHackMe - Preparation (IR)](https://tryhackme.com/room/irpreparation)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.