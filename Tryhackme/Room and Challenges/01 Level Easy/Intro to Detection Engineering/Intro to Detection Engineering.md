# Intro to Detection Engineering [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `introtodetectioneng`
* **Link:** https://tryhackme.com/room/introtodetectioneng
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe (room teórico con 8 flags inline en el contenido de lectura)
* **Componentes:** Detection engineering (definición, lifecycle, mentalidad) · gestión de falsos positivos/negativos · diseño de reglas vs IOCs/TTPs · retos del detection engineering
* **Impacto rol:** Teoría fundamental del detection engineering: crear y mantener reglas de detección con precisión, bajos falsos positivos y cobertura de TTPs reales.

## Solucionario de Tareas / Task Solutions

> **ES:** Detection Engineering es el arte de diseñar, implementar y mantener reglas que detectan comportamientos maliciosos con el menor número de falsos positivos posible. El room es teórico pero cada sección incluye un **flag inline** que revela una lección clave. El lifecycle va de planear → diseñar → probar → deploy → monitorear → mejorar. La mentalidad correcta es la **de atacante** (adversarial mindset): pensar en cómo evadiría tus propias reglas. Los retos incluyen falsos positivos, la degradación de reglas por cambios en infraestructura, y la necesidad de version control. Cada flag es un recordatorio de estos principios.
> **EN:** Detection Engineering is the craft of designing, implementing and maintaining rules that detect malicious behaviour with the fewest false positives. The room is theory-heavy but each section includes an **inline flag** highlighting a key lesson. The lifecycle runs plan → design → test → deploy → monitor → improve. The right mentality is the **attacker mindset**: think about how you'd evade your own rules. Challenges include false positives, rule degradation from infrastructure changes, and the need for version control. Each flag is a reminder of these principles.

### Task 1 — Introducción / Introduction

* **Check:** `Ready to dive into Detection Engineering!`

### Task 2 — Qué es Detection Engineering / What is Detection Engineering?

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **first flag**? | `THM{PR0ACT1V3_D3T3CT10N_3NG1N33R}` |
| What is the **second flag**? | `THM{V3RS10N_C0NTR0L_1S_K3Y}` |

* **T2 Reading:** Detection engineering ≠ detection operations. Detectar activamente vs. reaccionar; mantener reglas propias, versionadas (flag: **version control is key**).

### Task 3 — Ciclo de Vida / Detection Engineering Life Cycle

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **third flag**? | `THM{D4T3_R3V13W_B3F0R3_D3S1GN}` |
| What is the **fourth flag**? | `THM{P33R_R3V13W_B3F0R3_D3PL0Y}` |

* **Lifecycle:** plan → design → test → deploy → monitor → improve. Pre-deployment review (flag: **data review before design**; **peer review before deploy**).

### Task 4 — Mentalidad de un Detection Engineer

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **fifth flag**? | `THM{PR3C1S10N_PR0BL3M_D3T3CT3D}` |
| What is the **sixth flag**? | `THM{B3HAV10UR_0V3R_10CS}` |

* **Mentalidad / Mindset:** pensar como atacante (adversarial); priorizar **detección por comportamiento** (TTPs) sobre IOC estáticos (flag: **behaviour over IOCs**). Control de falsos positivos: precisión primero, recuerda el **precision problem**.

### Task 5 — Retos del Detection Engineering

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **seventh flag**? | `THM{D3_G03S_B3Y0ND_RUL3S}` |
| What is the **eighth flag**? | `THM{D3T3CT10N_L1BR4RY_D3GR4D3S}` |

* **Retos / Challenges:** reglas que parecían buenas dejan de funcionar con cambios de infraestructura → **detection library degrades**. Un detection engineer va más allá de las reglas (flag: **GOES BEYOND RULES**): automatización, enrichment, contextualización.

### Task 6 — Conclusión / Conclusion

* **Check:** `Ready to create high-quality detections!`

## Metodología / Methodology

1. **Paso / Step:** Leer las secciones del room (T2–T5) y anotar los 8 flags inline en orden.
2. **Paso / Step:** Completar las preguntas (flags 1–8) con el contenido de cada sección.
3. **Paso / Step:** Recordar las lecciones clave: lifecycle, peer review, behaviour over IOCs, version control, precision.

### Cadena de aprendizaje / Learning Chain

```
Detection Engineering != detection operations
  -> lifecycle: plan -> design -> test -> deploy -> monitor -> improve
  -> peer review + data review before design -> precision
  -> mindset: adversarial / attacker mindset
  -> behaviour over IOCs -> GOES BEYOND RULES
  -> problem: detection library degrades with infra changes -> version control
```

**Mapeo MITRE ATT&CK:** no mapea a técnicas; se alinea a la fase de *Detection & Analytics* de MITRE D3FEND/ATT&CK.

**Lección:** *La mejor regla de detección se invalida mañana: la mentalidad de atacante y el version control son lo que la mantiene viva.*

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.