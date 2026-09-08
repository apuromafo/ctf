# SOC L1 Alert Reporting

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (SOC / Blue Team) |
| **Slug** | `socl1alertreporting` |
| **Link** | [TryHackMe](https://tryhackme.com/room/socl1alertreporting) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | SOC / triaje de alertas L1-L2 / Alert Reporting / Alert Escalation / 5 Ws / phishing / webshell / elegir L2 |
| **Impacto** | Sala que entrena la transición del analista SOC L1 al L2: documentar correctamente una alerta (Alert Reporting), saber cuándo y cómo escalar (Alert Escalation), comunicarse de forma efectiva con otros departamentos y supervisores, y aplicar el enfoque de las 5 Ws (Who, What, When, Where, Why) para reportar incidentes como filtración de documentos sensibles o phishing. |

---

**Contexto:** Con las alertas ya triadas por un analista L1, el siguiente paso es documentarlas (volcado de la sala: "el enfoque de las 5 Ws") y escalarlas al analista L2 cuando corresponda. En el laboratorio se analiza un correo que filtró un documento sensible (remitente `m.boslan@tryhackme.thm`, procedente de un correo de phishing de `support@microsoft.com`), se rellena un reporte con las 5 Ws, se asigna el incidente al analista L2 (en turno: `E.Fleming`) y se investiga una segunda alerta (webshell vía Exchange antiguo). También se repasan los protocolos de comunicación: ante una amenaza crítica no se llama primero al manager (Nay), pero si crees que omitiste un ataque se contacta a L2 inmediatamente (Yea).

## Solucionario

### Task 1: Introducción

**Explicación:** Presenta el flujo completo del SOC para un L1: triaje → documentación → escalación → comunicación. Alerta para empezar la práctica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del módulo. | `No answer needed` |

### Task 2: Embudo de Alertas

**Explicación:** Tras el triaje inicial, las alertas se dividen en dos procesos: **Alert Escalation** (pasar alertas sospechosas o complejas a un analista L2 para revisión profunda o remediación) y **Alert Reporting** (describir formalmente los detalles y hallazgos de una alerta). La comunicación con otros departamentos (IT, RRHH, etc.) sirve para validar actividades o pedir información adicional.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Proceso de pasar alertas a un analista L2? | `Alert Escalation` |
| 2 | ¿Proceso de describir formalmente los detalles? | `Alert Reporting` |

### Task 3: Guía de Reportes

**Explicación:** Un buen reporte ahorra tiempo al analista L2 y sirve como registro histórico (los logs crudos expiran, pero las alertas suelen ser permanentes). Se recomienda el enfoque de las **5 Ws**: Who (usuario o cuenta), What (secuencia de eventos), When (marcas de tiempo), Where (dispositivo/IP/URL) y Why (razonamiento del veredicto). Analizando el lab: el correo que filtró el documento sensible fue enviado por `m.boslan@tryhackme.thm` tras un intento de phishing en el que el remitente se hacía pasar por `support@microsoft.com`; al completar el reporte correctamente se obtiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Email que filtró el documento sensible. | `m.boslan@tryhackme.thm` |
| 2 | Remitente del correo de phishing. | `support@microsoft.com` |
| 3 | Flag por escribir un buen reporte (5 Ws). | `THM{nice_attempt_faking_microsoft_support}` |

### Task 4: Guía de Escalación

**Explicación:** Se debe escalar si la alerta indica un ataque mayor, requiere acciones de remediación (aislar host, resetear contraseña), requiere comunicación externa o si el analista L1 no comprende completamente la alerta. Pasos en el dashboard: escribir el reporte y dar un veredicto → cambiar el estado a **In Progress** → asignar al **L2 de turno** (`E.Fleming`). Escalar correctamente otorga una flag; la segunda alerta (webshell vía Exchange antiguo) entrega otra.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del analista L2 actual. | `E.Fleming` |
| 2 | Flag tras escalar correctamente la primera alerta a L2. | `THM{good_job_escalating_your_first_alert}` |
| 3 | Flag tras investigar la segunda alerta (Webshell). | `THM{looks_like_webshell_via_old_exchange}` |

### Task 5: Comunicación SOC

**Explicación:** Casos críticos y mejores prácticas: si una alerta crítica no es atendida en 30 min, se llama por teléfono a L2, luego a L3 y finalmente al Manager (por eso contactar primero al manager es **Nay**). Si Slack/Teams está comprometido, no usar ese chat para contactar al usuario. Si días después descubres que clasificaste mal una alerta, informa inmediatamente a L2 (contactar a L2 de inmediato si omitiste un ataque es **Yea**).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Contactar primero al manager ante una amenaza crítica? | `Nay` |
| 2 | ¿Contactar a L2 inmediatamente si crees que omitiste un ataque? | `Yea` |

### Task 6: Conclusión

**Explicación:** Cierre del módulo: **Alert Reporting** preserva el contexto para el L2, **Escalation** garantiza remediación a tiempo con personal más especializado y **Communication** facilita la coordinación entre el SOC y otros departamentos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to move on! | `No answer needed` |

---

**Metodología:** Revisión del dashboard de alertas → análisis del correo de phishing con las 5 Ws → redacción del reporte → veredicto → escalación al L2 → comunicación ante incidentes críticos → verificación de coherencia del flujo L1→L2.
**Learning chain:** entender el flujo de alertas → documentar con 5 Ws → escalar técnicamente (estado, asignación L2) → aplicar protocolos de comunicación → cerrar el ciclo del analista L1.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell), T1566 (Phishing), T1566.001 (Spearphishing Attachment), T1048 (Exfiltration Over Alternative Protocol)
**Fuente:** [TryHackMe - SOC L1 Alert Reporting](https://tryhackme.com/room/socl1alertreporting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
