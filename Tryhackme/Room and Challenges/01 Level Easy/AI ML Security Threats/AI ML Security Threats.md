# AI ML Security Threats

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `aimlsecuritythreats` |
| **Link** | [TryHackMe](https://tryhackme.com/room/aimlsecuritythreats) |
| **Sección** | 01 Level Easy |
| **Fuente** | [Jery0843/TryHackMe](https://github.com/Jery0843/TryHackMe) — `AI-ML Security Threats.md` |
| **Componentes** | Machine Learning / Deep Learning / LLMs / Transformer / AI security / MITRE ATLAS / Defensive AI / SIEM |
| **Impacto** | Construye una base de conceptos de IA/ML y su doble rol en la ciberseguridad ofensiva y defensiva. |

---

**Contexto:** Construir una base de conceptos de IA/ML y su doble rol en la ciberseguridad ofensiva y defensiva: desde los bloques fundamentales (aprendizaje supervisado/semi-supervisado, redes neuronales, deep learning) y los Large Language Models hasta las amenazas de seguridad dirigidas a IA (model theft, deepfake) y la IA defensiva (detección y contención de brechas).

## Solucionario

### Task 1: Introduction

**Explicación:** Tarea introductoria y conceptual. Se presenta el objetivo de la sala: construir una base de conceptos de IA/ML y comprender su doble rol en la ciberseguridad ofensiva y defensiva. No se requiere respuesta directa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - conceptual introduction. | `No answer needed` |

### Task 2: Building Blocks of AI

**Explicación:** Se repasan los bloques fundamentales de la IA: la categoría de machine learning que combina datos etiquetados (*labelled*) y no etiquetados (*unlabelled*) es el **semi-supervised learning**; la primera capa de una red neuronal es la **input layer** (capa de entrada); el método de aprendizaje que extrae características de datos crudos y no estructurados sin etiquetas humanas es el **deep learning**; y las conexiones ponderadas entre nodos simulan las **synapses** (sinapsis) del cerebro humano.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What category of machine learning combines both labelled and unlabelled data? | `Semi-supervised learning` |
| 2 | What is the first layer in a neural network? | `Input layer` |
| 3 | Which learning method extracts features from raw, unstructured input without human labels? | `Deep learning` |
| 4 | What do weighted connections between nodes simulate in the human brain? | `Synapses` |

### Task 3: Large Language Models (LLMs)

**Explicación:** Los **Large Language Models** (modelos de lenguaje grandes) son los que impulsaron los avances de ChatGPT. La primera etapa de entrenamiento de un LLM es el **pre-training** (pre-entrenamiento), y la arquitectura de red neuronal que potencia los LLMs modernos es el **Transformer**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What AI model enabled advancements in ChatGPT? | `Large Language Models` |
| 2 | What is the first training stage for LLMs? | `Pre-training` |
| 3 | What neural network powers modern LLMs? | `Transformer` |

### Task 4: AI Security Threats

**Explicación:** Las amenazas de seguridad dirigidas a IA: el framework de **MITRE** que guía el análisis de amenazas específico de IA es **ATLAS**; el ataque que clona un modelo de IA mediante su API es el **model theft** (robo de modelo); la técnica de IA generativa que replica la imagen de una persona es el **deepfake**; y el ataque de ingeniería social que la IA hace más difícil de detectar es el **phishing**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What MITRE framework guides AI-specific threat analysis? | `ATLAS` |
| 2 | What attack clones an AI model via its API? | `Model theft` |
| 3 | Which generative AI technique replicates a person's likeness? | `Deepfake` |
| 4 | What social engineering attack is harder to detect due to AI? | `Phishing` |

### Task 5: Defensive AI

**Explicación:** La IA defensiva: según IBM, la IA ayuda a identificar y contener brechas **108 days** (108 días) más rápido; el **threat hunting** (caza de amenazas) se beneficia de la generación imaginativa de escenarios por parte de la IA; y las herramientas de explainability (explicabilidad) como **SHAP** y **LIME** asisten al **model monitoring** (monitoreo de modelos).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to IBM, AI helps identify and contain breaches how many days faster? | `108 days` |
| 2 | Which task benefits from AI-driven imaginative scenario generation? | `Threat hunting` |
| 3 | Explainability tools like SHAP and LIME assist with what? | `Model monitoring` |

### Task 6: Practical – Using the AI Assistant

**Explicación:** Práctica con el asistente de IA. Se responden los valores de configuración solicitados: **DoH port = 443**, **SYN flood timeout = 20** y **Ephemeral port range size = 16384**. La bandera generada en la fuente original fue `THM{443/60/16384}` (la fuente de la migración marca valores equivalentes como `{443/20/16384}` según la redacción de la respuesta).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the values for DoH port, SYN flood timeout, and ephemeral port range size? | `DoH port = 443 / SYN flood timeout = 20 / Ephemeral port range size = 16384` |

### Task 7: Conclusion

**Explicación:** Tarea de cierre: no se requiere respuesta; destaca la doble naturaleza de la IA, tanto ofensiva como defensiva (double-edged nature of AI).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer required — highlights the double-edged nature of AI. | `No answer needed` |

---

**Metodología:**
1. Revisar los conceptos de IA/ML: tipos de aprendizaje (supervisado, no supervisado, semi-supervisado por datos etiquetados y no etiquetados), primera capa de una red neuronal (input), deep learning como método que extrae características sin etiquetas humanas, y las conexiones ponderadas que simulan sinapsis.
2. Estudiar los LLMs: los Large Language Models impulsaron ChatGPT; su primera etapa de entrenamiento es el pre-training; la arquitectura que los potencia es el Transformer.
3. Analizar las amenazas a la IA: MITRE ATLAS como framework de análisis de amenazas, el model theft que clona un modelo vía API, el deepfake que replica la imagen de una persona, y el phishing más difícil de detectar gracias a la IA.
4. Reconocer la IA defensiva: según IBM la IA ayuda a identificar y contener brechas 108 días antes; el threat hunting se beneficia de la generación de escenarios imaginativos; las herramientas de explainability como SHAP y LIME asisten al model monitoring.
5. Completar la práctica con el asistente IA respondiendo los valores de DoH port (443), SYN flood timeout (20) y tamaño del rango de puertos efímeros (16384).

**Learning chain:** AI/ML concepts (semi-supervised, neural network, deep learning) → Large Language Models (pre-training, Transformer) → AI security threats (ATLAS, model theft, deepfake, phishing) → Defensive AI (breach identification 108 days, threat hunting, model monitoring) → practical assistant values.

**MITRE ATT&CK:** T1566 (Phishing), T1598 (Phishing for Information), T1078.001 (Valid Accounts: Default Accounts).

**Fuente:** [TryHackMe - AI ML Security Threats](https://tryhackme.com/room/aimlsecuritythreats)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
