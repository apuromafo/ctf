# Trusted By Default

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `trustedbydefault` |
| **Link** | [TryHackMe](https://tryhackme.com/room/trustedbydefault) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | DFIR / service account / trusted account abuse / Windows forensics |
| **Impacto** | Investigar el presunto abuso de una cuenta de servicio de confianza en un entorno corporativo Windows |

---

**Contexto:** Sala **DFIR (Digital Forensics & Incident Response)** de dificultad Media, Premium y muy reciente. El caso: *"Investigate suspected abuse of a trusted service account at Aurora Retail Group."* - investigar un presunto abuso de una **cuenta de servicio de confianza** en la empresa Aurora Retail Group. La estructura pública tiene 2 tareas: un "Case Briefing" (sitio estático) y "The Investigation" (máquina virtual con datos forenses). Al no existir aún writeups públicos, las respuestas exactas no están publicadas.

## Solucionario

### Task 1: Case Briefing

**Explicación:**

Tarea de briefing (sitio estático): presenta el caso de Aurora Retail Group - una cuenta de servicio considerada "de confianza" ha sido presuntamente abusada. Contiene 1 pregunta de confirmación: hay que leer el briefing e indicar que se está listo para empezar la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have reviewed the case briefing and am ready to begin the investigation. | `I have reviewed the case briefing and am ready to begin the investigation.` |

### Task 2: The Investigation

**Explicación:**

Tarea de investigación (máquina virtual) con **10 preguntas**. La descripción pública empuja a sospechar de una cuenta de servicio "de confianza" y a investigar su abuso. Dado que la sala es muy reciente y aún no hay writeups verificados, tanto los enunciados exactos como las respuestas (incluidas las flags `THM{...}`) no están publicadas públicamente por el momento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (10 preguntas / 10 questions) | `THM{...redacted...}` - respuestas aún no publicadas públicamente |

> **Nota:** Estructura documentada con la API pública (`api/v2/rooms/tasks?roomCode=trustedbydefault`). Metodología y respuestas se completarán cuando existan writeups verificados.

---

**Metodología:**

1. **Documentación preliminar:** La sala sale a la luz hace pocos días. Se documenta su estructura pública (2 tareas: Case Briefing + The Investigation, con 1 + 10 preguntas) mediante la API pública de THM y la descripción oficial del caso ("suspected abuse of a trusted service account at Aurora Retail Group").
2. **Pendiente de publicación:** A fecha de esta redacción no existen walkthroughs públicos verificados; sin ellos no se puede documentar la metodología forense concreta ni ofrecer respuestas reales.
3. **Actualización futura:** Este writeup se completará en cuanto exista una solución pública verificada (afecta a las 10 preguntas de la Task 2).

**Learning chain:** caso Aurora Retail Group -> cuenta de servicio "de confianza" abusada -> investigar abuso -> estructura 2 tareas (briefing + investigación) -> respuestas pendientes de writeup

**Lección:** *La documentación forense debe partir siempre de fuentes verificadas; cuando una sala es tan reciente que no tiene soluciones públicas, la única práctica honesta es reflejar la estructura conocida por la API y marcar el resto como pendiente de publicación.*

**MITRE ATT&CK:** T1078 (Valid Accounts) · T1069 (Permission Groups Discovery) · CWE-269 (Improper Privilege Management)

**Fuente:** [TryHackMe - Trusted By Default](https://tryhackme.com/room/trustedbydefault)
