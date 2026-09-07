# SOC L2 Alert Triage [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `socl2alerttriage`
* **Link:** https://tryhackme.com/room/socl2alerttriage
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + static-site "Learning Lessons"
* **Componentes:** SOC L2 workflow · triage · log analysis · threat response · containment
* **Impacto rol:** El día a día del L2: triage, entender la regla antes de actuar, decidir cuándo contener y cuándo no.

## Solucionario de Tareas / Task Solutions

> **ES:** L2 workflow: el trigger más común de triage es una **escalated alert** (de L1). Antes de actuar debes entender la regla que generó la alerta (**Yea**); una secuencia cronológica de eventos del ataque se llama **timeline**. La respuesta temporal que detiene la propagación es **containment**. Si ves actividad maliciosa clara durante un pentest autorizado y los red team no responden, **Yea** aíslas el dispositivo antes de confirmar (primero la seguridad del entorno). El static-site "Learning Lessons" usa un exercise interactivo para practicar el proceso.
> **EN:** L2 workflow: the most common triage trigger is an **escalated alert** (from L1). Before acting you must understand the rule behind the alert (**Yea**); a chronological sequence of attack events is a **timeline**. The temporary response that stops propagation is **containment**. If you see clear malicious activity on a corporate device during an authorised pentest and red teamers don't respond, **Yea** you isolate the device before confirmation (environment safety first). The static-site "Learning Lessons" uses an interactive exercise to practice the process.

### Task 1 — Introducción / Introduction

* **Check:** `Continue to the next task.`

### Task 2 — SOC L2 Workflow

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **most common trigger** for L2 to start the triage? | `Escalated Alert` |

* **Trigger / Trigger:** en un SOC típico, L1 escanea y escala; L2 tria. El escalado automático o manual de un alerta es el punto de entrada del workflow de L2.

### Task 3 — Log Analysis as L2

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Should you **understand the rule purpose** before triaging the alert? (Yea/Nay) | `Yea` |
| What term is used for a **chronological list of events** (related to the attack)? | `Timeline` |

* **Yea:** una regla sin contexto genera falsos positivos; entender *qué* intenta detectar es el primer paso.
* **Timeline:** cadena temporal de eventos (timestamp → event → timestamp → event). Fundamental en cualquier investigación (DFIR, reportes).

### Task 4 — Threat Response

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the term for a **temporary response** that stops the threat from spreading? | `Containment` |
| You see clearly malicious activity on one of the corporate devices during an ongoing pentest, but red teamers do not respond. Would you **isolate the device** before receiving a confirmation? (Yea/Nay) | `Yea` |

* **Containment:** acción temporal (bloqueo de IP, aislamiento de host, cortafuegos) que frena la propagación sin borrar evidencia.
* **Yea:** la seguridad del entorno real prevalece; la confirmación del pentest no justifica dejar activo un comportamiento malicioso (puede ser un ataque real o un escenario de testing que el red team no monitora).

### Task 5 — Learning Lessons *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **flag** you get at the end of the challenge? | `THM{triage_done_right!}` |

* **Static-site:** exercise interactivo de lecciones aprendidas tras un incidente → completar y anotar el flag.

### Task 6 — Conclusión / Conclusion

* **Check:** `Complete the room!`

## Metodología / Methodology

1. **Paso / Step:** T2–T4: responder conceptos del workflow de L2.
2. **Paso / Step:** T5: abrir el static-site, resolver el exercise → `THM{triage_done_right!}`.

### Cadena de aprendizaje / Learning Chain

```
trigger = escalated alert (L1 -> L2)
  -> regla: entender antes de triar (Yea)
  -> timeline: eventos cronológicos
  -> containment: respuesta temporal
  -> decisión: aislar primero (Yea) en pentest autorizado
  -> lesson learned: THM{triage_done_right!}
```

**Mapeo MITRE ATT&CK:** T1107 (File Deletion) y T1562 (Impair Defenses) son las acciones que busca prevenir el containment · SEI / D3FEND · CWE-693 (Protection Mechanism Failure).

**Lección:** *La pregunta antes de aislar no es "¿estoy seguro?" sino "¿puedo permitirme no aislar?"*

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.