# Incident Response Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `incidentresponsefundamentals` | [TryHackMe](https://tryhackme.com/room/incidentresponsefundamentals) | 01 Level Easy | THM | Incident Response, Alerts, True/False Positive, Playbooks, Containment, Phishing | Comprensión y práctica del ciclo de respuesta a incidentes con un ejercicio de correo malicioso |

> **Objeto:** Aprender las fases de la respuesta a incidentes, clasificar alertas (true/false positive), aplicar playbooks y practicar la investigación de un correo de phishing en un ejercicio hands-on.

---

**Contexto:** Sala de TryHackMe sobre los fundamentos de la respuesta a incidentes (IR). Explica qué es un incidente, la clasificación de alertas (true positive y false positive), ejemplos de incidentes como infección de malware y denegación de servicio, las fases del ciclo (incluyendo containment y Post Incident Activity), el uso de playbooks y un ejercicio práctico donde se investiga un correo malicioso.

> **ES:** Una sala guiada para entender el ciclo de vida de la respuesta a incidentes, distinguir alertas reales y falsos positivos, seguir playbooks y completar un ejercicio práctico de análisis de un correo de phishing.
> **EN:** A guided room to understand the incident response lifecycle, tell true positives from false ones, follow playbooks, and complete a hands-on phishing email investigation.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Primera aproximación al concepto de incidente y a la respuesta a incidentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Hay algo que responder en este apartado? / Is there anything to answer here? | `No answer needed` |

### Task 2: Alertas y clasificación / Alerts & Classification

**Explicación:** Llega un aviso de seguridad; se clasifica la alerta y se determina si es un true positive o un false positive.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | ¿Qué se recibe en primer lugar? / What is received first? | `Alert` |
| 2.2 | Clasificación de la alerta confirmada / Classification of the confirmed alert | `true positive` |
| 2.3 | Clasificación de la alerta sin confirmar / Classification of the unconfirmed alert | `false positive` |

### Task 3: Tipos de incidentes / Incident Types

**Explicación:** Ejemplos típicos de incidentes de seguridad que motivan una respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3.1 | Primer ejemplo de incidente / First incident example | `malware infection` |
| 3.2 | Segundo ejemplo de incidente / Second incident example | `Denial of service` |

### Task 4: Fases de la respuesta / Response Phases

**Explicación:** El ciclo de la respuesta a incidentes: contener el incidente y cerrar con la actividad posterior al incidente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4.1 | Fase que limita el impacto / Phase that limits the impact | `containment` |
| 4.2 | Fase que se realiza al finalizar / Phase performed when finished | `Post Incident Activity` |

### Task 5: Playbooks / Playbooks

**Explicación:** Los playbooks proporcionan los pasos predefinidos que el equipo debe seguir durante la respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | ¿Qué documento define los pasos de respuesta predefinidos? / Which document defines the predefined response steps? | `Playbooks` |

### Task 6: Ejercicio práctico - Correo malicioso / Hands-on - Malicious Email

**Explicación:** Investigación práctica de un correo malicioso: se identifica al remitente, el vector de entrega, los recuentos y se recupera la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6.1 | ¿Quién es el remitente del correo? / Who is the sender of the email? | `Jeff Johnson` |
| 6.2 | ¿Cuál es el vector de entrega? / Which is the delivery vector? | `Email Attachment` |
| 6.3 | Primer valor del recuento / First count value | `3` |
| 6.4 | Segundo valor del recuento / Second count value | `1` |
| 6.5 | Obtenga la bandera / Get the flag | `THM{My_First_Incident_Response}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre del ejercicio validando el proceso completo de respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | ¿Hay algo que responder al final? / Is there anything to answer at the end? | `No answer needed` |

---

**Metodología:** Se estudiaron los conceptos de IR y la clasificación de alertas (true/false positive). En el ejercicio práctico se abrió el correo sospechoso, se identificó al remitente `Jeff Johnson`, se inspeccionó el adjunto malicioso (`Email Attachment`) como vector de entrega y se revisaron los detalles del incidente (valores 3 y 1) hasta recuperar la bandera `THM{My_First_Incident_Response}`, cerrando con las fases de containment y Post Incident Activity.

### Cadena de ataque / Attack Chain

Recepción de una alerta → clasificación del aviso (false/true positive) → identificación del incidente (malware infection / DoS) → aplicación del playbook → contención → actividad posterior al incidente → investigación del correo malicioso → identificación del remitente y vector → obtención de la bandera.

**Learning chain:** Concepto de incidente → alertas y clasificación → tipos de incidentes → fases de IR (containment, Post Incident Activity) → playbooks → análisis de correo de phishing → bandera.

**Lección:** *La respuesta a incidentes es un proceso estructurado: una alerta debe clasificarse, el incidente contenerse y el aprendizaje consolidarse con playbooks. Investigar el correo malicioso exige revisar remitente, adjuntos y evidencias antes de declarar la contención.*

**MITRE ATT&CK:** T1566 (Phishing), T1204 (User Execution), T1105 (Ingress Tool Transfer), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Incident Response Fundamentals](https://tryhackme.com/room/incidentresponsefundamentals)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.