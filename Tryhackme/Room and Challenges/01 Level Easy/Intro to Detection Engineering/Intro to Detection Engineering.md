# Intro to Detection Engineering

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `introtodetectioneng` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introtodetectioneng) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe (room teórico con 8 flags inline en el contenido de lectura) |
| **Componentes** | Detection engineering (definición, lifecycle, mentalidad) / gestión de falsos positivos/negativos / diseño de reglas vs IOCs/TTPs / retos del detection engineering |
| **Impacto** | Teoría fundamental del detection engineering: crear y mantener reglas de detección con precisión, bajos falsos positivos y cobertura de TTPs reales. |

---

**Contexto:** Detection Engineering es el arte de diseñar, implementar y mantener reglas que detectan comportamientos maliciosos con el menor número de falsos positivos posible. El room es teórico pero cada sección incluye un **flag inline** que revela una lección clave. El lifecycle va de planear → diseñar → probar → deploy → monitorear → mejorar. La mentalidad correcta es la **de atacante** (adversarial mindset): pensar en cómo evadiría tus propias reglas. Los retos incluyen falsos positivos, la degradación de reglas por cambios en infraestructura, y la necesidad de version control. Cada flag es un recordatorio de estos principios.

## Solucionario

### Task 1: Introducción

**Explicación:** Introducción a la sala y al detection engineering. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - ready to dive into Detection Engineering! | `No answer needed` |

### Task 2: Qué es Detection Engineering (What is Detection Engineering?)

**Explicación:** Detection engineering ≠ detection operations: detectar activamente vs. reaccionar. Implica mantener reglas propias y **versionadas** (flag: version control is key). La proactividad es la clave (flag: PROACTIVE DETECTION ENGINEER).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **first flag**? | `THM{PR0ACT1V3_D3T3CT10N_3NG1N33R}` |
| 2 | What is the **second flag**? | `THM{V3RS10N_C0NTR0L_1S_K3Y}` |

### Task 3: Ciclo de Vida (Detection Engineering Life Cycle)

**Explicación:** Lifecycle: **plan → design → test → deploy → monitor → improve**. Antes del deploy hay que revisar los datos (data review before design) y hacer peer review (peer review before deploy).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **third flag**? | `THM{D4T3_R3V13W_B3F0R3_D3S1GN}` |
| 2 | What is the **fourth flag**? | `THM{P33R_R3V13W_B3F0R3_D3PL0Y}` |

### Task 4: Mentalidad de un Detection Engineer

**Explicación:** Pensar como atacante (adversarial/attacker mindset); priorizar **detección por comportamiento** (TTPs) sobre IOC estáticos (flag: behaviour over IOCs). Control de falsos positivos: precisión primero — el **precision problem**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **fifth flag**? | `THM{PR3C1S10N_PR0BL3M_D3T3CT3D}` |
| 2 | What is the **sixth flag**? | `THM{B3HAV10UR_0V3R_10CS}` |

### Task 5: Retos del Detection Engineering

**Explicación:** Reglas que parecían buenas dejan de funcionar con cambios de infraestructura → **detection library degrades**. Un detection engineer va más allá de las reglas: automatización, enrichment y contextualización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **seventh flag**? | `THM{D3_G03S_B3Y0ND_RUL3S}` |
| 2 | What is the **eighth flag**? | `THM{D3T3CT10N_L1BR4RY_D3GR4D3S}` |

### Task 6: Conclusión

**Explicación:** Cierre del room: ya puedes crear detecciones de alta calidad. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - ready to create high-quality detections! | `No answer needed` |

---

**Metodología:**
1. Leer las secciones del room (T2–T5) y anotar los 8 flags inline en orden.
2. Completar las preguntas (flags 1–8) con el contenido de cada sección.
3. Recordar las lecciones clave: lifecycle, peer review, behaviour over IOCs, version control, precision.

**Learning chain:** Detection Engineering != detection operations → lifecycle: plan → design → test → deploy → monitor → improve → peer review + data review before design → precision → mindset: adversarial / attacker mindset → behaviour over IOCs → GOES BEYOND RULES → problem: detection library degrades with infra changes → version control.

**Lección:** *La mejor regla de detección se invalida mañana: la mentalidad de atacante y el version control son lo que la mantiene viva.*

**MITRE ATT&CK:** no mapea a técnicas; se alinea a la fase de *Detection & Analytics* de MITRE D3FEND/ATT&CK.

**Fuente:** [TryHackMe - Intro to Detection Engineering](https://tryhackme.com/room/introtodetectioneng)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
