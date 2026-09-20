# Cyber Crisis Management

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `cybercrisismanagement` | [TryHackMe](https://tryhackme.com/room/cybercrisismanagement) | 01 Level Easy | THM | Gestión de crisis, CSIRT, CMT, Triage, Comunicación | Gestión de crisis y respuesta ante incidentes |

> **Objeto:** Aprender a gestionar una cibercrisis simulada: los roles del equipo de gestión de crisis (CMT), la clasificación de severidad, el triage y la toma de decisiones de comunicación.

---

**Contexto:** Sala orientada al blue team y a la gestión de crisis. El jugador asume el papel de un miembro del equipo de gestión de crisis (Crisis Management Team) mientras la empresa sufre un incidente, debiendo decidir cómo priorizar, escalar y comunicar.

> **ES:** Experimenta una cibercrisis desde dentro: priorizar la severidad, conocer los roles del CMT, escalar al CEO y contener el incidente hasta su resolución.
> **EN:** Experience a cyber crisis from the inside: prioritise severity, know the CMT roles, escalate to the CEO and contain the incident until it is resolved.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Introducción a la sala y al escenario de cibercrisis.

No answer needed

### Task 2: Severidad y prioridad / Severity and Priority
**Explicación:** Se aprende a clasificar la severidad de los incidentes para prioritizar la respuesta.

1. Moderate
2. Low
3. Critical

### Task 3: Actores del CMT / CMT Roles
**Explicación:** Se identifican los roles que componen el equipo de gestión de crisis.

1. Scribe
2. Chair
3. Legal
4. Communication
5. Subject Matter Experts

### Task 4: Estructura / Structure
**Explicación:** Se comprende cómo se organiza la estructura de respuesta.

1. Assembly
2. CSIRT

### Task 5: Flujo de crisis / Crisis Flow
**Explicación:** Se recorre el flujo de la crisis: del triage al escalado y la decisión final.

1. Triage
2. CMT Chair
3. CEO

### Task 6: Escalado / Escalation
**Explicación:** Se determina quién interviene cuando el incidente requiere conocimientos especializados.

Subject Matter Experts

### Task 7: Flag final / Final Flag
**Explicación:** Una vez gestionada la crisis de forma correcta, se obtiene el flag.

THM{The.Crisis.has.been.managed!}

### Task 8: Recapitulación / Recap
**Explicación:** Recapitulación final de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Severidad 1 | `Moderate` |
| 2.2 | Severidad 2 | `Low` |
| 2.3 | Severidad 3 | `Critical` |
| 3.1 | Rol que documenta | `Scribe` |
| 3.2 | Rol que preside | `Chair` |
| 3.3 | Rol legal | `Legal` |
| 3.4 | Rol de comunicaciones | `Communication` |
| 3.5 | Expertos convocados | `Subject Matter Experts` |
| 4.1 | Conjunto de respuesta 1 | `Assembly` |
| 4.2 | Equipo de respuesta a incidentes | `CSIRT` |
| 5.1 | Paso 1 del flujo | `Triage` |
| 5.2 | Paso 2 del flujo | `CMT Chair` |
| 5.3 | Paso 3 del flujo | `CEO` |
| 6 | ¿Quién es convocado? | `Subject Matter Experts` |
| 7 | Flag final | `THM{The.Crisis.has.been.managed!}` |
| 8 | — | `No answer needed` |

---

**Metodología:** Análisis del escenario de crisis, clasificación de la severidad del incidente, asignación de roles y estructura del CMT, triage del flujo de decisiones, escalado cuando es necesario y obtención del flag tras gestionar la crisis correctamente.

### Cadena de ataque / Attack Chain

Escenario de crisis → priorización de severidad → activación del CMT → triage → escalado al CEO → contención → flag.

**Learning chain:** crisis awareness → severidad → roles del CMT → triage → escalado → resolución → flag

*Lección:* La gestión de crisis requiere roles claros, triage de severidad y comunicación estructurada para responder con rapidez y contener el impacto.

**MITRE ATT&CK:** N/A.

**Fuente:** [TryHackMe - Cyber Crisis Management](https://tryhackme.com/room/cybercrisismanagement)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.