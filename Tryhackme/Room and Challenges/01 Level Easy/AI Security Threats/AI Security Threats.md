# AI Security Threats

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `aisecuritythreats` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/aisecuritythreats) |
| **Sección** | AI Security |
| **Fuente** | THM |
| **Componentes** | Vulnerabilidades IA, Ataques mejorados con IA, IA defensiva |
| **Impacto** | Amenazas de seguridad en IA/ML |

---

**Contexto:** Segundo room del path *AI Fundamentals* de TryHackMe (2026), en su variante **MENTOR AI**. Presenta la doble cara de la IA en ciberseguridad: las vulnerabilidades inherentes a los modelos de IA/ML, cómo los atacantes usan la IA para mejorar sus ataques, y cómo la IA se usa de forma defensiva. La parte práctica es un laboratorio de *prompt injection* contra el asistente virtual MENTOR.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Introducción)* I'm ready to learn | `No answer needed` |

### Task 2: Vulnerabilities in AI Models

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first layer in a neural network that handles incoming raw data? | `input layer` |
| 2 | Which learning method does not require human-labeled data and can extract features from raw unstructured input? | `deep learning` |
| 3 | What are the weighted connections between nodes in a neural network meant to simulate in the human brain? | `synapses` |

### Task 4: AI-Enhanced Attacks

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What framework was developed by MITRE for AI-specific cyber threats? | `ATLAS` |
| 2 | What type of attack involves cloning an AI model by interacting with its API? | `model theft` |
| 3 | What generative AI technique can replicate a person's voice/appearance realistically? | `deepfake` |
| 4 | What common social engineering attack became harder to detect due to AI-generated fluent messages? | `phishing` |

### Task 5: Defensive AI

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to IBM, how many days faster does AI help identify and contain breaches? | `108` |
| 2 | What cybersecurity task benefits from AI imagining attacker behavior we might not consider? | `threat hunting` |
| 3 | Explainability tools such as SHAP and LIME help with what? | `model monitoring` |

### Task 6: Practical (MENTOR prompt-injection)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{pr0mpt_1nj3ct_p01s0n_l34k_dr1ft}` |

---

**Metodología:** Comprender las capas y métodos de aprendizaje de una red neuronal, identificar el framework de amenazas IA de MITRE (ATLAS) y los ataques reales (model theft, deepfake, phishing aumentado), repasar las ventajas defensivas cuantificadas por IBM, y en la parte práctica ejecutar un *prompt injection* contra el asistente MENTOR para exfiltrar la flag.

**Learning chain:** Fundamentos de IA/ML → Vulnerabilidades del modelo → Ataques aumentados con IA → Defensa con IA → Práctica de prompt injection

**MITRE ATT&CK:** N/A (Laboratorio de prompt injection en un asistente virtual)

**Fuente:** [TryHackMe - AI Security Threats](https://tryhackme.com/r/room/aisecuritythreats)
