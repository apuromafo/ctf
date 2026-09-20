# IR Philosophy and Ethics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `irphilosophyandethics` | [TryHackMe](https://tryhackme.com/room/irphilosophyandethics) | 01 Level Easy | TryHackMe | IR, ética, filosofía de respuesta, objetividad, cadena de custodia, transparencia, confianza, autorización | Aplicar la filosofía y la ética en la respuesta a incidentes: prioridades, objetividad, custodia de la evidencia y dilemas éticos del DFIR. |

---

**Contexto:** Sala dedicada a la filosofía y la ética de la respuesta a incidentes. Examina las prioridades del equipo (aislar y contener, aplicar parches a las vulnerabilidades), la objetividad del investigador, la cadena de custodia de la evidencia y la transparencia. También cubre la confianza, la obligación de informar, el dilema riesgo frente a vergüenza pública, la necesidad de políticas claras y la autorización para actuar sobre los sistemas. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Determinar las prioridades de la IR, actuar con objetividad y mantener la cadena de custodia, ser transparente, gestionar la confianza y la comunicación, equilibrar riesgo y reputación y trabajar solo con la autorización adecuada.
> **EN:** Set the IR priorities, act with objectivity and maintain the chain of custody, be transparent, manage trust and communication, balance risk and reputation and only act with proper authorisation.

## Solucionario

### Task 1: Filosofía de la IR / IR Philosophy
**Explicación:** Se presenta la filosofía que guía las decisiones en la respuesta a incidentes.

1. No answer needed

### Task 2: Prioridades del equipo / Team Priorities
**Explicación:** Se establecen las prioridades de actuación del equipo de respuesta: aislar y contener, el punto de origen y parchear las vulnerabilidades.

1. Isolate and quarantine
2. Ground zero
3. Patch vulnerabilities

### Task 3: Ética del investigador / Investigator Ethics
**Explicación:** Se aplican los principios éticos fundamentales del análisis: objetividad, cadena de custodia y transparencia.

1. Objectivity
2. chain of custody
3. Transparency

### Task 4: Confianza y comunicación / Trust and Communication
**Explicación:** Se gestionan la confianza del equipo, el deber de informar, el dilema entre riesgo y vergüenza, las políticas claras y la autorización.

1. Trustworthiness
2. Inform
3. Risk vs Embarrassment
4. Clear policies and procedures
5. Authorisation

### Task 5: Dilemas éticos DFIR / DFIR Ethical Dilemmas
**Explicación:** Se resuelve el dilema ético práctico planteado en la sala, obteniendo la flag.

1. THM{Face_Your_DFIR_Ethical_Dilemmas}

### Task 6: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre la filosofía y la ética de la respuesta a incidentes.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | Prioridad: aislar y contener / Isolate and quarantine priority | `Isolate and quarantine` |
| 3 | Punto de origen del incidente / Incident ground zero | `Ground zero` |
| 4 | Prioridad: parchear vulnerabilidades / Patch vulnerabilities priority | `Patch vulnerabilities` |
| 5 | Objetividad del análisis / Analysis objectivity | `Objectivity` |
| 6 | Cadena de custodia / Chain of custody | `chain of custody` |
| 7 | Transparencia / Transparency | `Transparency` |
| 8 | Confiabilidad / Trustworthiness | `Trustworthiness` |
| 9 | Deber de información / Duty to inform | `Inform` |
| 10 | Dilema riesgo frente a vergüenza / Risk vs embarrassment | `Risk vs Embarrassment` |
| 11 | Políticas y procedimientos claros / Clear policies and procedures | `Clear policies and procedures` |
| 12 | Autorización / Authorisation | `Authorisation` |
| 13 | Flag del dilema ético DFIR / DFIR ethical dilemma flag | `THM{Face_Your_DFIR_Ethical_Dilemmas}` |
| 14 | (Pregunta 14 no especificada en el original) | `No answer needed` |

---

**Metodología:** Revisar la filosofía y las prioridades de la IR, aplicar los principios éticos del análisis (objetividad, cadena de custodia, transparencia), gestionar la confianza y la comunicación con los interesados y resolver el dilema ético final con su flag.

### Cadena de ataque / Attack Chain

```text
prioridades (aislar y contener, ground zero, parchear) -> objetividad -> cadena de custodia -> transparencia -> confianza y comunicación -> riesgo vs reputación -> autorización -> flag del dilema
```

**Learning chain:** filosofía IR -> prioridades -> ética del analista -> cadena de custodia -> confianza y comunicación -> autorización -> dilemas DFIR.

**Lección:** *La respuesta a incidentes se sostiene sobre decisiones éticas: objetividad, custodia de la evidencia, transparencia y autorización son los principios que separan una buena investigación de una decisión comprometida.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1021 (Remote Services), T1562 (Impair Defenses)

**Fuente:** [TryHackMe - IR Philosophy and Ethics](https://tryhackme.com/room/irphilosophyandethics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.