# AI Security Threats

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `aisecuritythreats` | [TryHackMe](https://tryhackme.com/room/aisecuritythreats) | AI Security | THM | Vulnerabilidades IA, Ataques mejorados con IA, IA defensiva | Amenazas de seguridad en IA/ML |

---

**Contexto:** Segundo room del path *AI Fundamentals* de TryHackMe (2026), en su variante **MENTOR AI**. Presenta la doble cara de la IA en ciberseguridad: las vulnerabilidades inherentes a los modelos de IA/ML, cómo los atacantes usan la IA para mejorar sus ataques, y cómo la IA se usa de forma defensiva. La parte práctica es un laboratorio de *prompt injection* contra el asistente virtual MENTOR.

## Solucionario

### Task 1: Introduction

**Explicación:** Task introductoria en la que el participante confirma su disposición a comenzar el aprendizaje del path de seguridad en IA.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Introducción)* I'm ready to learn | `No answer needed` |

### Task 2: Vulnerabilities in AI Models

**Explicación:** Se revisan las vulnerabilidades inherentes a los modelos de IA/ML: las capas de una red neuronal, los métodos de aprendizaje (incluido el deep learning, que no requiere datos etiquetados) y las conexiones ponderadas que simulan las sinapsis del cerebro humano.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first layer in a neural network that handles incoming raw data? | `input layer` |
| 2 | Which learning method does not require human-labeled data and can extract features from raw unstructured input? | `deep learning` |
| 3 | What are the weighted connections between nodes in a neural network meant to simulate in the human brain? | `synapses` |

### Task 4: AI-Enhanced Attacks

**Explicación:** Se analizan los ataques aumentados con IA: el framework ATLAS de MITRE para amenazas específicas de IA, el robo de modelos (model theft), los deepfakes y el phishing mejorado con mensajes generados por IA en lenguaje fluido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What framework was developed by MITRE for AI-specific cyber threats? | `ATLAS` |
| 2 | What type of attack involves cloning an AI model by interacting with its API? | `model theft` |
| 3 | What generative AI technique can replicate a person's voice/appearance realistically? | `deepfake` |
| 4 | What common social engineering attack became harder to detect due to AI-generated fluent messages? | `phishing` |

### Task 5: Defensive AI

**Explicación:** Se repasan las ventajas defensivas de la IA: los días que IBM cuantifica de reducción para identificar y contener brechas, el apoyo al threat hunting al imaginar comportamientos de atacante no contemplados, y las herramientas de explicabilidad (SHAP, LIME) aplicadas a la monitorización de modelos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to IBM, how many days faster does AI help identify and contain breaches? | `108` |
| 2 | What cybersecurity task benefits from AI imagining attacker behavior we might not consider? | `threat hunting` |
| 3 | Explainability tools such as SHAP and LIME help with what? | `model monitoring` |

### Task 6: Practical (MENTOR prompt-injection)

**Explicación:** Laboratorio práctico de *prompt injection* contra el asistente virtual MENTOR: mediante un prompt malicioso se consigue que el modelo exfiltre información interna, obteniendo la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{pr0mpt_1nj3ct_p01s0n_l34k_dr1ft}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Introducción) I'm ready to learn | `No answer needed` |
| 2 | What is the first layer in a neural network that handles incoming raw data? | `input layer` |
| 3 | Which learning method does not require human-labeled data and can extract features from raw unstructured input? | `deep learning` |
| 4 | What are the weighted connections between nodes in a neural network meant to simulate in the human brain? | `synapses` |
| 5 | What framework was developed by MITRE for AI-specific cyber threats? | `ATLAS` |
| 6 | What type of attack involves cloning an AI model by interacting with its API? | `model theft` |
| 7 | What generative AI technique can replicate a person's voice/appearance realistically? | `deepfake` |
| 8 | What common social engineering attack became harder to detect due to AI-generated fluent messages? | `phishing` |
| 9 | According to IBM, how many days faster does AI help identify and contain breaches? | `108` |
| 10 | What cybersecurity task benefits from AI imagining attacker behavior we might not consider? | `threat hunting` |
| 11 | Explainability tools such as SHAP and LIME help with what? | `model monitoring` |
| 12 | What's the flag? | `THM{pr0mpt_1nj3ct_p01s0n_l34k_dr1ft}` |

---

**Metodología:** Comprender las capas y métodos de aprendizaje de una red neuronal, identificar el framework de amenazas IA de MITRE (ATLAS) y los ataques reales (model theft, deepfake, phishing aumentado), repasar las ventajas defensivas cuantificadas por IBM, y en la parte práctica ejecutar un *prompt injection* contra el asistente MENTOR para exfiltrar la flag.

**Learning chain:** Fundamentos de IA/ML → Vulnerabilidades del modelo → Ataques aumentados con IA → Defensa con IA → Práctica de prompt injection

**Lección:** *La IA es un arma de doble filo: los mismos modelos vulnerables se explotan por sus debilidades mientras que la IA también acelera la defensa (threat hunting, monitorización y explicabilidad).*

**MITRE ATT&CK:** N/A (Laboratorio de prompt injection en un asistente virtual)

**Fuente:** [TryHackMe - AI Security Threats](https://tryhackme.com/room/aisecuritythreats)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.