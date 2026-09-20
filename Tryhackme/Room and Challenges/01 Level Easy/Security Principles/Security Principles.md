# Security Principles

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `securityprinciples` | [TryHackMe](https://tryhackme.com/room/securityprinciples) | `01 Level Easy` | THM | CIA triad, security models, fundamentals, access control | Resolución completa del reto de principios de seguridad |

---

**Contexto:** Room sobre los principios fundamentales de la seguridad de la información: la tríada CIA (Confidencialidad, Integridad, Disponibilidad), los conceptos de revelación (Disclosure) y destrucción/denegación, los modelos de seguridad y las clasificaciones de impacto.

> **ES:** Fundamentos de la seguridad de la información: la tríada CIA, los conceptos de divulgación y destrucción/denegación, y los modelos de seguridad con sus niveles de impacto.
> **EN:** Fundamentals of information security: the CIA triad, the concepts of disclosure and destruction/denial, and security models with their impact levels.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea inicial de la room: se comienza el recorrido sin necesidad de respuesta técnica.

1. No answer needed

### Task 2: Tríada CIA / CIA triad

**Explicación:** Se responde la flag que confirma el conocimiento de la tríada CIA (Confidencialidad, Integridad y Disponibilidad).

2. THM{CIA_TRIAD}

### Task 3: Confidencialidad / Confidentiality

**Explicación:** Se identifican los riesgos para la confidencialidad: la revelación no autorizada de información (Disclosure) y la pérdida de datos por destrucción o denegación.

1. Disclosure
2. Destruction/Denial

### Task 4: Modelos de seguridad / Security models

**Explicación:** Se obtiene la flag correspondiente a los modelos de seguridad de la información.

4. THM{SECURITY_MODELS}

### Task 5: Cierre parcial / Partial wrap-up

**Explicación:** Tarea intermedia de la room: no requiere respuesta técnica.

5. No answer needed

### Task 6: Niveles de impacto / Impact levels

**Explicación:** Se ordenan los niveles de impacto asignados a las distintas pérdidas (valores 2, 1 y 5 según el caso).

1. 2
2. 1
3. 5

### Task 7: Tarea de repaso 1 / Review task 1

**Explicación:** Task de refuerzo de conceptos: la respuesta se evalúa en la plataforma sin texto adicional.

7. No answer needed

### Task 8: Tarea de repaso 2 / Review task 2

**Explicación:** Task de refuerzo de conceptos: la respuesta se evalúa en la plataforma sin texto adicional.

8. No answer needed

### Task 9: Tarea de repaso 3 / Review task 3

**Explicación:** Task de refuerzo de conceptos: la respuesta se evalúa en la plataforma sin texto adicional.

9. No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Despliegue y arranque de la room | `No answer needed` |
| 2.1 | Flag de la tríada CIA | `THM{CIA_TRIAD}` |
| 3.1 | Revelación no autorizada de información | `Disclosure` |
| 3.2 | Pérdida por destrucción o denegación | `Destruction/Denial` |
| 4.1 | Flag de los modelos de seguridad | `THM{SECURITY_MODELS}` |
| 5.1 | Cierre parcial de la room | `No answer needed` |
| 6.1 | Primer nivel de impacto | `2` |
| 6.2 | Segundo nivel de impacto | `1` |
| 6.3 | Tercer nivel de impacto | `5` |
| 7.1 | Repaso 1 | `No answer needed` |
| 8.1 | Repaso 2 | `No answer needed` |
| 9.1 | Repaso 3 | `No answer needed` |

---

**Metodología:** 1) Comenzar la room. 2) Asimilar la tríada CIA (THM{CIA_TRIAD}). 3) Reconocer los riesgos de confidencialidad (Disclosure, Destruction/Denial). 4) Completar los modelos de seguridad (THM{SECURITY_MODELS}). 5) Repasar los conceptos. 6) Asignar los niveles de impacto (2, 1, 5). 7-9) Completar las tareas de repaso sin respuesta adicional.

### Cadena de ataque / Attack Chain

```text
Introducción -> THM{CIA_TRIAD} -> Disclosure + Destruction/Denial -> THM{SECURITY_MODELS} -> revisión de conceptos -> niveles de impacto (2, 1, 5) -> tareas de repaso
```

**Learning chain:** Fundamentos de seguridad -> tríada CIA -> confidencialidad (amenazas) -> modelos de seguridad -> niveles de impacto -> repaso

**Lección:** *La seguridad de la información se cimienta en principios como la tríada CIA y en comprender qué se pierde (revelación o destrucción) para poder modelar y priorizar las defensas.*

**MITRE ATT&CK:** N/A (Fundamentos teóricos de los principios de seguridad de la información)

**Fuente:** [TryHackMe - Security Principles](https://tryhackme.com/room/securityprinciples)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.