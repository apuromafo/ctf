# SOC L2 Alert Triage

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `socl2alerttriage` |
| **Link** | [TryHackMe](https://tryhackme.com/room/socl2alerttriage) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + static-site "Learning Lessons" |
| **Componentes** | SOC L2 workflow / triage / log analysis / threat response / containment |
| **Impacto** | El día a día del L2: triage, entender la regla antes de actuar, decidir cuándo contener y cuándo no |

---

**Contexto:** L2 workflow: el trigger más común de triage es una **escalated alert** (de L1). Antes de actuar debes entender la regla que generó la alerta (**Yea**); una secuencia cronológica de eventos del ataque se llama **timeline**. La respuesta temporal que detiene la propagación es **containment**. Si ves actividad maliciosa clara durante un pentest autorizado y los red teamers no responden, **Yea** aíslas el dispositivo antes de confirmar (primero la seguridad del entorno). El static-site "Learning Lessons" usa un exercise interactivo para practicar el proceso.

## Solucionario

### Task 1: Introducción / Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continue to the next task. | `No answer needed` |

**Explicación:** Introducción al room; no requiere respuesta.

### Task 2: SOC L2 Workflow

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **most common trigger** for L2 to start the triage? | `Escalated Alert` |

**Explicación:** En un SOC típico, L1 escanea y escala; L2 tria. El escalado automático o manual de una alerta (**Escalated Alert**) es el punto de entrada del workflow de L2: la mayoría de los triages de un analista L2 arrancan con una alerta ya escalada desde L1 o desde el propio SIEM.

### Task 3: Log Analysis as L2

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Should you **understand the rule purpose** before triaging the alert? (Yea/Nay) | `Yea` |
| 2 | What term is used for a **chronological list of events** (related to the attack)? | `Timeline` |

**Explicación:** Una regla sin contexto genera falsos positivos; entender *qué* intenta detectar es el primer paso antes de triar (**Yea**). La cadena temporal de eventos (timestamp → event → timestamp → event) se llama **Timeline** y es fundamental en cualquier investigación (DFIR, reportes).

### Task 4: Threat Response

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the term for a **temporary response** that stops the threat from spreading? | `Containment` |
| 2 | You see clearly malicious activity on one of the corporate devices during an ongoing pentest, but red teamers do not respond. Would you **isolate the device** before receiving a confirmation? (Yea/Nay) | `Yea` |

**Explicación:** **Containment** es la acción temporal (bloqueo de IP, aislamiento de host, cortafuegos) que frena la propagación sin borrar evidencia. Ante actividad claramente maliciosa en un dispositivo corporativo durante un pentest sin respuesta del red team, **Yea** se aísla el dispositivo antes de confirmar: la seguridad del entorno real prevalece frente a la confirmación pendiente (puede ser un ataque real o un escenario de testing que el red team no monitora).

### Task 5: Learning Lessons *(static-site)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **flag** you get at the end of the challenge? | `THM{triage_done_right!}` |

**Explicación:** El static-site "Learning Lessons" es un exercise interactivo de lecciones aprendidas tras un incidente; completarlo entrega el flag `THM{triage_done_right!}` como verificación.

### Task 6: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room! | `No answer needed` |

**Explicación:** Cierre del room.

---

**Metodología:**
1. **SOC L2 Workflow:** en un SOC típico, L1 escanea y escala; L2 tria. El escalado automático o manual de una alerta (**Escalated Alert**) es el punto de entrada del workflow de L2.
2. **Log Analysis como L2:** hay que **entender el propósito de la regla** antes de triar la alerta: una regla sin contexto genera falsos positivos; entender *qué* intenta detectar es el primer paso. La cadena temporal de eventos (timestamp → event → timestamp → event) es el **Timeline**, fundamental en cualquier investigación (DFIR, reportes).
3. **Threat Response:** **Containment** es la acción temporal (bloqueo de IP, aislamiento de host, cortafuegos) que frena la propagación sin borrar evidencia. Ante actividad claramente maliciosa en un dispositivo corporativo durante un pentest sin respuesta del red team, **Yea** se aísla el dispositivo antes de confirmar: la seguridad del entorno real prevalece (puede ser un ataque real o un escenario de testing que el red team no monitora).
4. **Static-site (T5):** abrir "Learning Lessons", resolver el exercise interactivo de lecciones aprendidas tras un incidente → flag `THM{triage_done_right!}`.

**Learning chain:** trigger = escalated alert (L1 → L2) → regla: entender antes de triar (Yea) → timeline: eventos cronológicos → containment: respuesta temporal → decisión: aislar primero (Yea) en pentest autorizado → lesson learned: THM{triage_done_right!}

**MITRE ATT&CK:** T1107 (File Deletion), T1562 (Impair Defenses), CWE-693 (Protection Mechanism Failure)

**Fuente:** [TryHackMe - SOC L2 Alert Triage](https://tryhackme.com/room/socl2alerttriage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
