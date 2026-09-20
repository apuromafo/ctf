# Eradication & Remediation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `eradicationremediation` | [TryHackMe - Eradication & Remediation](https://tryhackme.com/room/eradicationremediation) | `01 Level Easy` | THM | IR, erradicación, remediación, MITRE ATT&CK, respuesta a incidentes | Defensive — ciclo de vida completo de respuesta a incidentes |

> **Objeto:** Comprender las fases de erradicación y remediación de un incidente de seguridad y aplicarlas sobre un caso práctico de compromiso real (SwiftSpend Finance).

---

**Contexto:** La sala Eradication & Remediation cubre la tercera fase del ciclo de respuesta a incidentes: la erradicación. Se exploran los riesgos de erradicar de forma prematura, los métodos de erradicación y reconstrucción de sistemas, las estrategias de remediación y recuperación, y la mejora de la postura de seguridad. Finalmente se practica sobre un caso de compromiso para identificar al actor, sus mecanismos y las técnicas MITRE ATT&CK empleadas.

> **ES:** Sala de defensa sobre la fase de erradicación en respuesta a incidentes, con un caso práctico de investigación de un compromiso en SwiftSpend Finance.
>
> **EN:** Defensive room covering the eradication phase of incident response, with a hands-on investigation case of a SwiftSpend Finance compromise.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** La sala presenta el ciclo de respuesta a incidentes y sitúa la erradicación dentro del proceso global de manejo de incidentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de introducción | `No answer needed` |

### Task 2: Erradicación prematura / Premature Eradication

**Explicación:** Se analizan los peligros de erradicar indicadores antes de conocer el alcance completo del compromiso, evitando el efecto "whack-a-mole" y erradicando la causa raíz.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Concepto de erradicación sin conocer el alcance completo | `Premature erosion` |
| 2 | Efecto de eliminar indicadores que reaparecen | `whack-a-mole` |
| 3 | Objetivo real de la erradicación | `Eradicate the bad guys` |

### Task 3: Métodos de erradicación / Eradication Methods

**Explicación:** Se revisan los distintos métodos y estrategias disponibles para erradicar una intrusión, considerando impacto operativo, tiempo y alcance.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Método automatizado | `Automated Eradication` |
| 2 | Reconstrucción completa del sistema | `Complete System Rebuild` |
| 3 | Consecuencia operativa a considerar | `Downtime` |
| 4 | Determinación del alcance de la erradicación | `Scoping` |

### Task 4: Estrategia de remediación y recuperación / Remediation and Recovery Strategy

**Explicación:** Se estudia la fase de remediación: restauración de la operación segura, segmentación de red y principio de privilegio mínimo para evitar la reincidencia del atacante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Estrategia que combina remediación y recuperación | `Remediation and Recovery strategy` |
| 2 | Control de red para limitar el movimiento lateral | `Network Segmentation` |
| 3 | Principio de acceso mínimo | `Principle of least privilege` |

### Task 5: Postura de seguridad / Security Posture

**Explicación:** Tras erradicar y remediar, se refuerza la postura de seguridad mediante pruebas ofensivas que validen la resiliencia del entorno.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Mejora posterior al incidente | `Security Posture` |
| 2 | Pruebas para validar la seguridad corregida | `Penetration tests and attack simulations` |

### Task 6: Caso práctico SwiftSpend / SwiftSpend Case Study

**Explicación:** Investigación del compromiso sobre la infraestructura de SwiftSpend Finance: se identifica la cuenta comprometida, el hash de credencial, el buzón afectado, el mecanismo de persistencia, la frecuencia de ejecución y el origen geográfico del actor, clasificando la acción según MITRE ATT&CK.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cuenta del usuario comprometido | `swiftspend_admin` |
| 2 | Hash de la credencial comprometida | `f4fe137aeb154299ab1b7349952f6088` |
| 3 | Buzón del administrador afectado | `infra_admin@swiftspend.finance` |
| 4 | Comando de persistencia programado | `/bin/bash /var/lib/jenkins/backup.sh` |
| 5 | Contador/frecuencia asociada | `0` |
| 6 | País de origen del actor | `Russian Federation` |
| 7 | Categoría de la técnica empleada | `Exfiltration` |
| 8 | Táctica MITRE ATT&CK de la acción | `Actions on Objectives` |

### Task 7: Reflexión final / Final Reflection

**Explicación:** La sala cierra con una reflexión sobre el proceso completo de erradicación y remediación aplicado al caso práctico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de cierre | `No answer needed` |

---

**Metodología:** Se parte de la teoría del ciclo de respuesta a incidentes para entender cuándo y cómo erradicar. Luego se pasa a un caso práctico de investigación donde se correlacionan logs, credenciales comprometidas, mecanismos de persistencia y telemetría para reconstruir la intrusión y clasificar las técnicas del actor según la taxonomía MITRE ATT&CK.

### Cadena de ataque / Attack Chain

Preparación → Detección y Análisis → Contención → Erradicación (prematura vs. correcta) → Recuperación/Remediación → Post-incidente (postura de seguridad) → Validación con pruebas ofensivas.

**Learning chain:** Incident response lifecycle → Eradication phases → Remediation strategies → ATT&CK mapping → Blue team validation

**Lección:** *Erradicar sin conocer el alcance completo del incidente genera una falsa sensación de seguridad; la erradicación correcta elimina al actor y su infraestructura, y solo se confirma con la remediación y pruebas de validación.*

**MITRE ATT&CK:** T1070 - Indicator Removal, T1486 - Data Encrypted for Impact, T1036 - Masquerading, T1053.003 - Scheduled Task/Job: Cron, T1567 - Exfiltration Over Web Service; N/A (defensivo/SOC)

**Fuente:** [TryHackMe - Eradication & Remediation](https://tryhackme.com/room/eradicationremediation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.