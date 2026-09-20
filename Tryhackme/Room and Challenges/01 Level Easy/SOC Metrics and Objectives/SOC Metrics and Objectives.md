# SOC Metrics and Objectives

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `socmetricsandobjectives` | [TryHackMe](https://tryhackme.com/room/socmetricsandobjectives) | 01 Level Easy | TryHackMe | SOC Metrics, MTTD, MTTR, False Positive Rate | Operational — Understanding SOC performance metrics and KPIs |

---

**Contexto:** Este room Explora las métricas y objetivos clave de un Security Operations Center (SOC), incluyendo el tiempo medio de detección (MTTD), el tiempo medio de respuesta (MTTR) y la tasa de falsos positivos. Se Analiza cómo estas métricas impactan la eficiencia del SOC.

## Solucionario

### Task 1: SOC Metrics Introduction

**Explicación:** Se Introducen los conceptos de métricas de SOC sin requerir una respuesta específica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the intro | `No answer needed` |

### Task 2: MTTD (Mean Time to Detect)

**Explicación:** Se Evalúa la comprensión del concepto de MTTD y su valor por defecto en un SOC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Is MTTD a proactive or reactive metric? | `Nay` |
| 2 | What is the acceptable MTTD percentage? | `80%` |

### Task 3: MTTR (Mean Time to Respond)

**Explicación:** Se Analiza el MTTR y su relación con el día de la semana y los tiempos de respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | On which day was the fastest response time recorded? | `Monday` |
| 2 | What were the response times recorded? | `12,10,51` |

### Task 4: False Positive Rate

**Explicación:** Se Evalúa la tasa de falsos positivos y su impacto en la eficiencia del SOC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the acceptable false positive rate? | `80%` |
| 2 | Is a high false positive rate beneficial for the SOC? | `Yea` |

### Task 5: Flags

**Explicación:** Se Resuelven los ejercicios prácticos relacionados con las métricas de SOC, identificando los valores correctos de MTTD, MTTD y FPR.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the MTTD flag? | `THM{mttr:quick_start_but_slow_response}` |
| 2 | What is the MTTR flag? | `THM{mttd:time_between_attack_and_alert}` |
| 3 | What is the FPR flag? | `THM{fpr:the_main_cause_of_l1_burnout}` |

### Task 6: Practical Exercise

**Explicación:** Se Aplica los conocimientos de métricas de SOC en un ejercicio práctico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the practical exercise | `No answer needed` |

---

**Metodología:** Se Utilizan métricas clave de SOC (MTTD, MTTR, FPR) para evaluar la eficiencia del centro de operaciones de seguridad y tomar decisiones informadas sobre su mejora continua.

### Cadena de ataque / Attack Chain

**Learning chain:** SOC Metrics → MTTD/MTTR Understanding → False Positive Analysis → KPI Evaluation → SOC Optimization

**Lección:** *Las métricas de SOC son fundamentales para medir y mejorar la eficiencia del centro de operaciones de seguridad, permitiendo identificar áreas de mejora y optimizar los procesos de detección y respuesta.*

**MITRE ATT&CK:** T1562 — Impair Defenses; T1078 — Valid Accounts

**Fuente:** [TryHackMe - SOC Metrics and Objectives](https://tryhackme.com/room/socmetricsandobjectives)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.