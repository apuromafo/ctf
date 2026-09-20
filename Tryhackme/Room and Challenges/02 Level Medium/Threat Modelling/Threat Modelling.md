# Threat Modelling
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Threat Modelling | threatmodelling | https://tryhackme.com/room/threatmodelling | 02 Level Medium | TryHackMe | STRIDE, DREAD, PASTA, MITRE ATT&CK, ATT&CK Navigator, modelado de amenazas | Construcción de ciberresiliencia y capacidades de emulación mediante el modelado de amenazas |

> **Objeto:** Construir capacidades de ciberresiliencia y emulación mediante el modelado de amenazas.

---
**Contexto:** **Threat Modelling** es una sala guiada de dificultad Media dedicada al **modelado de amenazas**. Se revisan los conceptos generales del threat modelling, su relación con **MITRE ATT&CK** y el mapeo de técnicas con el **ATT&CK Navigator**, y después se profundiza en tres frameworks clásicos: **DREAD** (priorización de riesgos), **STRIDE** (categorización de amenazas) y **PASTA** (metodología en fases centrada en el riesgo). El objetivo es anticipar y priorizar amenazas antes de que se materialicen, alineando el modelado con técnicas reales de adversario.
> **ES:** Construir capacidades de ciberresiliencia y emulación mediante el modelado de amenazas.
> **EN:** Building cyber resiliency and emulation capabilities through threat modelling.

## Solucionario
### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos del modelado de amenazas.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 1 | `No answer needed` |

### Task 2: Panorama del modelado de amenazas / Threat Modelling Overview
**Explicación:** Conceptos fundamentales del threat modelling: qué es una vulnerabilidad, la fase de identificación de activos y la representación del modelado de ataques en forma de árbol.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Concepto de debilidad explotable | `vulnerability` |
| Identificación de activos | `Asset Identification` |
| Representación en árbol de los ataques | `attack tree` |

### Task 3: Modelado con MITRE ATT&CK / Modelling with MITRE ATT&CK
**Explicación:** Se vincula el modelado de amenazas con **MITRE ATT&CK**. Se identifica la técnica de explotación de aplicaciones expuestas y la táctica de acceso inicial asociada.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Técnica ATT&CK de acceso inicial | `T1190` |
| Táctica asociada | `Initial Access` |

### Task 4: Mapeo con ATT&CK Navigator / Mapping with ATT&CK Navigator
**Explicación:** Uso del **ATT&CK Navigator** para representar y cuantificar la cobertura de técnicas sobre la matriz ATT&CK.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 4 (1) | `31` |
| Task 4 (2) | `13` |

### Task 5: Framework DREAD / DREAD Framework
**Explicación:** Se aplica **DREAD** para priorizar riesgos, evaluando categorías como el daño potencial, la descubribilidad y los usuarios afectados.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Categoría de daño potencial | `Damage` |
| Descubribilidad | `Discoverability` |
| Usuarios afectados | `Affected Users` |

### Task 6: Framework STRIDE / STRIDE Framework
**Explicación:** Se aplica **STRIDE** para categorizar amenazas. Se relaciona con la **CIA Triad**, con la confidencialidad y el *tampering*, y con la denegación de servicio; el ejercicio concluye con la flag del framework.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 6 (1) | `CIA Triad` |
| Task 6 (2) | `Confidentiality` |
| Task 6 (3) | `Tampering` |
| Task 6 (4) | `Denial of Service` |
| Task 6 (5) | `THM{m0d3ll1ng_w1th_STR1D3}` |

### Task 7: Framework PASTA / PASTA Framework
**Explicación:** Se aplica **PASTA**, una metodología de modelado de amenazas centrada en el riesgo y organizada en fases: descomposición de la aplicación, análisis de los ataques y definición del alcance técnico. El ejercicio concluye con la flag del framework.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 7 (1) | `Decompose the Application` |
| Task 7 (2) | `Analyse the Attacks` |
| Task 7 (3) | `Define the Technical Scope` |
| Task 7 (4) | `THM{c00k1ng_thr34ts_w_P4ST4}` |

### Task 8: Conclusión / Conclusion
**Explicación:** Cierre de la sala y resumen de los frameworks de modelado de amenazas vistos.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 8 | `No answer needed` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | `No answer needed` |
| 2.1 | Concepto de debilidad explotable | `vulnerability` |
| 2.2 | Identificación de activos | `Asset Identification` |
| 2.3 | Representación en árbol de los ataques | `attack tree` |
| 3.1 | Técnica ATT&CK de acceso inicial | `T1190` |
| 3.2 | Táctica asociada | `Initial Access` |
| 4.1 | ATT&CK Navigator (1) | `31` |
| 4.2 | ATT&CK Navigator (2) | `13` |
| 5.1 | Categoría de daño potencial | `Damage` |
| 5.2 | Descubribilidad | `Discoverability` |
| 5.3 | Usuarios afectados | `Affected Users` |
| 6.1 | Task 6 (1) | `CIA Triad` |
| 6.2 | Task 6 (2) | `Confidentiality` |
| 6.3 | Task 6 (3) | `Tampering` |
| 6.4 | Task 6 (4) | `Denial of Service` |
| 6.5 | Task 6 (5) | `THM{m0d3ll1ng_w1th_STR1D3}` |
| 7.1 | Task 7 (1) | `Decompose the Application` |
| 7.2 | Task 7 (2) | `Analyse the Attacks` |
| 7.3 | Task 7 (3) | `Define the Technical Scope` |
| 7.4 | Task 7 (4) | `THM{c00k1ng_thr34ts_w_P4ST4}` |
| 8 | Task 8 | `No answer needed` |

---
**Metodología:** Introducción → panorama del threat modelling → modelado con MITRE ATT&CK → mapeo con ATT&CK Navigator → DREAD → STRIDE → PASTA → conclusión.

### Cadena de ataque / Attack Chain
```
Introducción -> Threat Modelling Overview (vulnerability / Asset Identification / attack tree)
-> Modelling with MITRE ATT&CK (T1190, Initial Access) -> ATT&CK Navigator (31, 13)
-> DREAD (Damage / Discoverability / Affected Users)
-> STRIDE (CIA Triad / Confidentiality / Tampering / Denial of Service / THM{m0d3ll1ng_w1th_STR1D3})
-> PASTA (Decompose the Application / Analyse the Attacks / Define the Technical Scope / THM{c00k1ng_thr34ts_w_P4ST4})
-> Conclusión
```
**Learning chain:** Conceptos de modelado → ATT&CK y Navigator → priorización con DREAD → categorización con STRIDE → metodología por fases con PASTA.
**Lección:** *El modelado de amenazas con STRIDE, DREAD y PASTA, alineado con MITRE ATT&CK, permite anticipar y priorizar riesgos antes de que se materialicen.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) — técnica usada como ejemplo y mapeada con el ATT&CK Navigator.
**Fuente:** [TryHackMe - Threat Modelling](https://tryhackme.com/room/threatmodelling)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
