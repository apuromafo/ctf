# DFIR_ An Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `dfiranintroduction` | https://tryhackme.com/room/dfiranintroduction | 01 Level Easy | TryHackMe | DFIR / Digital Forensics / Incident Response / RAM / recolección de evidencia / informe DFIR | Introducción a la forensia digital y la respuesta a incidentes: DFIR, recolección de memoria y fases de IR. |

---

**Contexto:** Introducción a la forensia digital y la respuesta a incidentes (DFIR). Se define qué es DFIR y el rol de los equipos de respuesta, se practica la recolección de memoria volátil (RAM) y la elaboración de un informe, y se repasan las fases finales de la respuesta a incidentes: Recovery, Eradication y Post-incident Activity.

> **ES:** Introducción a DFIR: definiciones (Digital Forensics and Incident Response), laboratorio práctico con captura de RAM y generación de informe, y fases del IR (Recovery, Eradication, Post-incident Activity).
> **EN:** DFIR introduction: definitions (Digital Forensics and Incident Response), hands-on RAM capture and report generation, and IR phases (Recovery, Eradication, Post-incident Activity).

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala de introducción a DFIR. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Definiciones / Definitions

**Explicación:** DFIR significa `Digital Forensics and Incident Response`, y el conjunto de habilidades necesarias para investigar y responder ante un incidente se engloba dentro de la rama de `Incident Response`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa la sigla DFIR? / What does DFIR stand for? | `Digital Forensics and Incident Response` |
| 2 | ¿Cuál es la habilidad vinculada a la respuesta ante incidentes? / Which skill is linked to incident response? | `Incident Response` |

### Task 3: Laboratorio práctico / Practical Lab

**Explicación:** En el laboratorio se recolecta la evidencia volátil del sistema analizado: la memoria `RAM`. Tras generar el informe requerido se obtiene la flag `THM{DFIR_REPORT_DONE}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de memoria se recolecta en el laboratorio? / Which type of memory is collected in the lab? | `RAM` |
| 2 | ¿Cuál es la flag obtenida al completar el informe? / What is the flag obtained after completing the report? | `THM{DFIR_REPORT_DONE}` |

### Task 4: Aplicación práctica / Applying the Knowledge

**Explicación:** Se contextualiza cómo aplicar los conceptos de DFIR en un entorno laboral real. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. | `No answer needed` |

### Task 5: Fases del IR / IR Phases

**Explicación:** Se repasan las etapas finales de la respuesta a incidentes: la fase de `Recovery` (recuperación de los sistemas), la fase de `Eradication` (eliminación de la amenaza) y la fase de `Post-incident Activity` (actividad posterior al incidente, como lecciones aprendidas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fase recupera los sistemas tras el incidente? / Which phase recovers the systems after the incident? | `Recovery` |
| 2 | ¿Qué fase elimina la amenaza por completo? / Which phase fully removes the threat? | `Eradication` |
| 3 | ¿Qué fase corresponde a la actividad posterior al incidente? / Which phase covers post-incident activity? | `Post-incident Activity` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la sala resumiendo los conceptos de DFIR. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué significa la sigla DFIR? | `Digital Forensics and Incident Response` |
| 3 | ¿Cuál es la habilidad vinculada a la respuesta ante incidentes? | `Incident Response` |
| 4 | ¿Qué tipo de memoria se recolecta en el laboratorio? | `RAM` |
| 5 | ¿Cuál es la flag obtenida al completar el informe? | `THM{DFIR_REPORT_DONE}` |
| 6 | Lee el contenido de la tarea. | `No answer needed` |
| 7 | ¿Qué fase recupera los sistemas tras el incidente? | `Recovery` |
| 8 | ¿Qué fase elimina la amenaza por completo? | `Eradication` |
| 9 | ¿Qué fase corresponde a la actividad posterior al incidente? | `Post-incident Activity` |
| 10 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** La sala parte de los conceptos de DFIR (Digital Forensics and Incident Response) y su rama de respuesta a incidentes. En el laboratorio se recolecta la memoria volátil (RAM) del sistema analizado y se genera el informe correspondiente, obteniendo la flag `THM{DFIR_REPORT_DONE}`. Finalmente se repasan las fases de respuesta a incidentes: Recovery, Eradication y Post-incident Activity.

### Cadena de ataque / Attack Chain

```text
Definición de DFIR (Digital Forensics and Incident Response) -> Recolección de evidencia RAM -> Generación de informe -> THM{DFIR_REPORT_DONE} -> Fases de IR: Recovery -> Eradication -> Post-incident Activity
```

**Learning chain:** DFIR → Digital Forensics and Incident Response → Incident Response → RAM -> Informe DFIR -> Recovery -> Eradication -> Post-incident Activity.

**Lección:** *La forensia digital y la respuesta a incidentes van de la mano: recolectar correctamente la evidencia volátil (RAM) antes de cualquier análisis es crítico, y cada incidente debe cerrarse con la recuperación, la erradicación y las lecciones aprendidas.*

**MITRE ATT&CK:** No aplica directamente (sala formativa de DFIR); la recolección de evidencia volátil se alinea con la respuesta a incidentes del NIST.

**Fuente:** [TryHackMe - DFIR_ An Introduction](https://tryhackme.com/room/dfiranintroduction)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.