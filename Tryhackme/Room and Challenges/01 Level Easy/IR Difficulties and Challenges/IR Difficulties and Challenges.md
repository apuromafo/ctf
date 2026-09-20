# IR Difficulties and Challenges

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `irdifficultiesandchallenges` | [TryHackMe](https://tryhackme.com/room/irdifficultiesandchallenges) | 01 Level Easy | TryHackMe | Incident Response, stakeholders, threat model, Risk-Based Prioritisation, Asset Management, Data Retention Policy, antiforense | Conocer las dificultades y los retos de la respuesta a incidentes: gestión de interesados, priorización por riesgo, gestión de activos y técnicas antiforenses. |

---

**Contexto:** Sala sobre las dificultades y retos en la respuesta a incidentes. Cubre la gestión de los stakeholders y los informes de situación (Situation Report), la construcción de un threat model y la priorización basada en riesgo (Risk-Based Prioritisation), la gestión de activos y las políticas de retención de datos (Data Retention Policy), así como las técnicas antiforenses como el borrado de metadatos y la manipulación de logs. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Identificar a los interesados y su informador, construir el modelo de amenazas y priorizar por riesgo, gestionar activos y retención de datos, y reconocer técnicas antiforenses como el borrado de metadatos y la manipulación de logs.
> **EN:** Identify the stakeholders and their reporter, build the threat model and prioritise by risk, manage assets and data retention, and recognise anti-forensic techniques such as metadata stripping and log manipulation.

## Solucionario

### Task 1: Dificultades de la IR / IR Difficulties
**Explicación:** Se presentan los retos generales a los que se enfrenta la respuesta a incidentes.

1. No answer needed

### Task 2: Interesados / Stakeholders
**Explicación:** Se identifican las partes interesadas en el incidente y el documento que informa de la situación.

1. Stakeholders
2. Situation Report

### Task 3: Modelo de amenazas / Threat Modeling
**Explicación:** Se construye el modelo de amenazas y se aplica la priorización basada en riesgo.

1. Threat Model
2. Risk-Based Prioritisation

### Task 4: Activos y retención / Assets and Retention
**Explicación:** Se gestiona el inventario de activos y la política de retención de los datos.

1. Asset Management
2. Data Retention Policy

### Task 5: Retos antiforenses / Anti-forensic Challenges
**Explicación:** Se identifican las técnicas que dificultan la IR, como el borrado de metadatos y la manipulación de logs, con sus flags.

1. Metadata Stripping
2. Log Manipulation
3. THM{M3T4_M4DN3SS}
4. THM{ST3G_T4STIC}

### Task 6: Marcos de decisión / Decision Frameworks
**Explicación:** Se relacionan las dificultades de la IR con los marcos de decisión adecuados.

1. Decision-making frameworks

### Task 7: Retos de la IR / IR Challenges
**Explicación:** Se resuelven los retos de la unidad, cada uno con su flag.

1. THM{19fc1cb5da49c8d9e1fa59ddc65ca48d}
2. THM{242f97166d3d03a3d3bab6bb11011623}
3. THM{4c7ed9e2bba7d998954cdf0980923788}
4. THM{7644848b64724d84a0bc4165c4fab2ce}
5. THM{c042f61657bc18591514d602a641f106}

### Task 8: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre las dificultades y retos de la respuesta a incidentes.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | Partes interesadas / Interested parties | `Stakeholders` |
| 3 | Informe de situación / Situation report | `Situation Report` |
| 4 | Modelo de amenazas / Threat model | `Threat Model` |
| 5 | Priorización basada en riesgo / Risk-based prioritisation | `Risk-Based Prioritisation` |
| 6 | Gestión de activos / Asset management | `Asset Management` |
| 7 | Política de retención de datos / Data retention policy | `Data Retention Policy` |
| 8 | Borrado de metadatos / Metadata stripping | `Metadata Stripping` |
| 9 | Manipulación de logs / Log manipulation | `Log Manipulation` |
| 10 | Flag del reto de metadatos / Metadata challenge flag | `THM{M3T4_M4DN3SS}` |
| 11 | Flag del reto de esteganografía / Steganography challenge flag | `THM{ST3G_T4STIC}` |
| 12 | Marcos de decisión / Decision frameworks | `Decision-making frameworks` |
| 13 | Flag del reto 1 / Challenge 1 flag | `THM{19fc1cb5da49c8d9e1fa59ddc65ca48d}` |
| 14 | Flag del reto 2 / Challenge 2 flag | `THM{242f97166d3d03a3d3bab6bb11011623}` |
| 15 | Flag del reto 3 / Challenge 3 flag | `THM{4c7ed9e2bba7d998954cdf0980923788}` |
| 16 | Flag del reto 4 / Challenge 4 flag | `THM{7644848b64724d84a0bc4165c4fab2ce}` |
| 17 | Flag del reto 5 / Challenge 5 flag | `THM{c042f61657bc18591514d602a641f106}` |
| 18 | (Pregunta 18 no especificada en el original) | `No answer needed` |

---

**Metodología:** Revisar los retos de la IR, identificar stakeholders y canales de información, construir el modelo de amenazas, priorizar por riesgo, gestionar activos y retención de datos y aplicar técnicas de detección de antiforense (borrado de metadatos, manipulación de logs) para resolver cada reto con su flag.

### Cadena de ataque / Attack Chain

```text
dificultades IR -> stakeholders -> Situation Report -> Threat Model -> Risk-Based Prioritisation -> Asset Management -> Data Retention Policy -> antiforense (Metadata Stripping / Log Manipulation) -> flags de retos
```

**Learning chain:** IR -> stakeholders y comunicación -> amenazas y priorización -> gestión de activos -> retención de datos -> técnicas antiforenses -> resolución de retos.

**Lección:** *La respuesta a incidentes falla antes por personas, prioridades y datos incompletos que por técnica: gestionar stakeholders, priorizar por riesgo y conocer las técnicas antiforenses del adversario son tan decisivos como el análisis forense.*

**MITRE ATT&CK:** T1070 (Indicator Removal on Host), T1565 (Data Manipulation), T1564 (Hide Artifacts)

**Fuente:** [TryHackMe - IR Difficulties and Challenges](https://tryhackme.com/room/irdifficultiesandchallenges)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.