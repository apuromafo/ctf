# Trusted By Default [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF
* **Slug:** `trustedbydefault`
* **Link:** https://tryhackme.com/room/trustedbydefault
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=trustedbydefault` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala **DFIR (Digital Forensics & Incident Response)** de dificultad Media, Premium y muy reciente (lanzada hace pocos días). El caso: *"Investigate suspected abuse of a trusted service account at Aurora Retail Group."* — investigar un presunto abuso de una **cuenta de servicio de confianza** en la empresa Aurora Retail Group. La estructura pública tiene 2 tareas: un "Case Briefing" (sitio estático) y "The Investigation" (máquina virtual con datos forenses). Al no existir aún writeups públicos, las respuestas exactas no están publicadas.
> **EN:** **DFIR (Digital Forensics & Incident Response)** room of Medium difficulty, Premium and very recent (released days ago). Case: *"Investigate suspected abuse of a trusted service account at Aurora Retail Group."* — investigate a suspected abuse of a **trusted service account** at Aurora Retail Group. The public structure has 2 tasks: a "Case Briefing" (static site) and "The Investigation" (VM with forensic data). Since no public writeups exist yet, exact answers are not published.

### Task 1 - Case Briefing

> **ES:** Tarea de briefing (sitio estático): presenta el caso de Aurora Retail Group — una cuenta de servicio considerada "de confianza" ha sido presuntamente abusada. Contiene 1 pregunta de confirmación: hay que leer el briefing e indicar que se está listo para empezar la investigación.
> **EN:** Briefing task (static site): presents the Aurora Retail Group case — a "trusted" service account has allegedly been abused. It has 1 confirmation question: read the briefing and state that you are ready to begin the investigation.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I have reviewed the case briefing and am ready to begin the investigation. | `I have reviewed the case briefing and am ready to begin the investigation.` |

### Task 2 - The Investigation

> **ES:** Tarea de investigación (máquina virtual) con **10 preguntas**. La descripción pública empuja a sospechar de una cuenta de servicio "de confianza" y a investigar su abuso. Dado que la sala es muy reciente y aún no hay writeups verificados, tanto los enunciados exactos como las respuestas (incluidas las flags `THM{...}`) no están publicadas públicamente por el momento.
> **EN:** Investigation task (VM) with **10 questions**. The public description points at a "trusted" service account and asks to investigate its abuse. As the room is very recent and no verified writeup exists yet, both the exact questions and the answers (including any `THM{...}` flag) are not publicly published so far.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (10 preguntas / 10 questions) | `THM{...redacted...}` — respuestas aún no publicadas públicamente / answers not yet publicly published |

> **Nota / Note:** Estructura documentada con la API pública (`api/v2/rooms/tasks?roomCode=trustedbydefault`). Metodología y respuestas se completarán cuando existan writeups verificados.
> **EN:** Structure documented via the public API (`api/v2/rooms/tasks?roomCode=trustedbydefault`). Methodology and answers will be completed once verified writeups exist.

## Metodología / Methodology

1. **Paso / Step - Documentación preliminar:** La sala sale a la luz hace pocos días. Se documenta su estructura pública (2 tareas: Case Briefing + The Investigation, con 1 + 10 preguntas) mediante la API pública de THM y la descripción oficial del caso ("suspected abuse of a trusted service account at Aurora Retail Group").
2. **Paso / Step - Pendiente de publicación:** A fecha de esta redacción no existen walkthroughs públicos verificados; sin ellos no se puede documentar la metodología forense concreta ni ofrecer respuestas reales.
3. **Paso / Step - Actualización futura:** Este writeup se completará en cuanto exista una solución pública verificada (afecta a las 10 preguntas de la Task 2).

### Cadena de ataque / Attack Chain

```
n/d (documentación en construcción)
  - Sala reciente (Premium) sin writeups públicos aún
  - Estructura: Task 1 Case Briefing (1 pregunta) + Task 2 The Investigation (10 preguntas)
  - Caso: abuso de una cuenta de servicio "de confianza" en Aurora Retail Group
  - -> se actualizará cuando exista una solución verificada
```

**Lección:** La documentación forense debe partir siempre de fuentes verificadas; cuando una sala es tan reciente que no tiene soluciones públicas, la única práctica honesta es reflejar la estructura conocida por la API y marcar el resto como pendiente de publicación.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.