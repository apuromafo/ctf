# Securing AI Systems [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Free (acceso gratuito)
* **Slug:** `securingaisystems`
* **Link:** https://tryhackme.com/room/securingaisystems
* **Sección / Section:** Secure AI Systems (Section 2 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-2-Secure-AI-Systems\01-securing-ai-systems\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

Esta room sirve como el pilar fundamental para entender cómo asegurar pipelines de Inteligencia Artificial y Machine Learning. A diferencia del software tradicional, los sistemas de IA introducen comportamientos no deterministas, dependencia de datasets masivos y cadenas de suministro complejas que requieren un cambio de paradigma en el pensamiento de seguridad. Exploramos el NIST AI Risk Management Framework (RMF) y los principios centrales de la defensa de IA.

**Lo que aprenderás:**
* Las diferencias fundamentales entre seguridad de IT y seguridad de IA.
* El ciclo de vida de desarrollo de IA (desde la recolección de datos hasta el despliegue de modelos) y sus riesgos inherentes.
* Vectores de ataque clave contra sistemas ML incluyendo evasion, poisoning y model inversion.
* Implementación de estrategias de defensa en profundidad para arquitecturas de IA.

---

### Conceptos Clave / Key Concepts

#### El Ciclo de Vida de IA y la Superficie de Ataque

La seguridad de IA no se trata solo de proteger la API desplegada; requiere asegurar todo el pipeline. El ciclo de vida incluye Data Collection, Data Preprocessing, Model Training, Evaluation y Deployment. Cada fase tiene vulnerabilidades únicas: los datos de entrenamiento pueden envenenarse, las métricas de evaluación pueden manipularse y los modelos desplegados pueden someterse a entradas adversariales.

#### Adversarial Machine Learning (AML)

AML se enfoca en las vulnerabilidades de los algoritmos ML. Las categorías principales incluyen:
- **Evasion Attacks:** Modificar datos de entrada sutilmente (p. ej., cambiar píxeles en una imagen) para que el modelo los clasifique erróneamente, sin detección humana.
- **Data Poisoning:** Inyectar datos maliciosos en el set de entrenamiento para crear backdoors o degradar el rendimiento general.
- **Model Inversion/Extraction:** Consultar el modelo repetidamente para hacer reverse-engineering de sus datos de entrenamiento o robar los pesos del modelo.

#### Frameworks de Gestión de Riesgo de IA

Frameworks como el NIST AI RMF proporcionan enfoques estructurados para gestionar riesgos de IA. Enfatiza cuatro funciones centrales: **Map, Measure, Manage y Govern**. Los equipos de seguridad deben adaptar estos frameworks para identificar y mitigar sistemáticamente los riesgos específicos de sus despliegues de IA.

---

### Tarea 1 — Arquitectura del Sistema de IA / AI System Architecture

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What layer in an AI system is responsible for combining the system prompt, user input, and retrieved context before sending it to the model? | `Prompt Construction` |
| In the TryAssist architecture, what boundary does LLM output cross when it triggers a database query? | `LLM-to-tools` |

---

### Tarea 2 — Frameworks de Amenazas / Threat Frameworks

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which OWASP LLM Top 10 (2025) category covers the risk of LLM output being used to execute SQL injection against a backend database? | `LLM05` |
| What is the name of the MITRE knowledge base specifically designed for adversary tactics and techniques against AI and ML systems? | `ATLAS` |

---

### Tarea 3 — Casos de Estudio de Ataques / Attack Case Studies

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| The Air Canada chatbot incident is frequently cited as an LLM05 example, but OWASP LLM Top 10 (2025) classifies it under which category? | `LLM09` |
| What are the three dimensions of excessive agency? | `Excessive Functionality, Excessive Permissions, Excessive Autonomy` |
| A user extracts internal API endpoints from an AI assistant's system prompt. Which OWASP LLM Top 10 (2025) category does this fall under? | `LLM07` |
| An attacker sends thousands of maximum-length requests to an LLM API to generate a large bill. Which OWASP LLM Top 10 (2025) category covers this? | `LLM10` |

---

### Tarea 4 — Principios de Seguridad / Security Principles

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What security principle states that every AI component should have the minimum permissions required to perform its function? | `Least Privilege` |
| What practice integrates security into the machine learning lifecycle, covering monitoring, observability, and incident response? | `MLSecOps` |

---

### Tarea 5 — Auditoría Práctica / Practical Audit

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| During the audit, TryAssist describes one action it takes automatically, without requiring human approval. What is that action? | `Merge Pull Requests` |
| What database role does TryAssist report operating under? | `db_admin` |
| TryAssist logs all conversations without applying which security control? | `PII Filtering` |

---

### Conceptos Adicionales de rahul_ai / Additional Concepts (rahul_ai)

#### Introducción a la Seguridad de IA

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What property of AI systems makes them difficult to secure using traditional rules-based firewalls? | `Non-determinism` |
| Which NIST framework is explicitly designed to help organizations manage AI-related risks? | `NIST AI RMF` |

> La seguridad tradicional depende de entradas y salidas predecibles. La naturaleza probabilística de la IA significa que las defensas deben enfocarse en validación de entrada, monitoreo de comportamiento y entrenamiento robusto en lugar de solo bloqueo basado en firmas.

#### El Pipeline de Machine Learning

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In which phase of the ML pipeline is a data poisoning attack executed? | `Data Collection` |
| What type of attack occurs when an adversary queries a deployed model to replicate its functionality? | `Model Extraction` |

> Asegurar el pipeline significa implementar principios de zero-trust en cada etapa. La procedencia de los datos es crítica — si no puedes confiar en la fuente de tus datos de entrenamiento, no puedes confiar en el modelo.

#### Estrategias Defensivas

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What defensive technique involves training a model with adversarial examples to make it more robust? | `Adversarial Training` |
| Which principle dictates that AI systems should only be given access to the data they strictly need to function? | `Least Privilege` |

> La defensa en profundidad es crucial. El adversarial training endurece el modelo, pero el rate limiting a nivel de red previene la extracción de modelos, y los controles de acceso robustos protegen los datos de entrenamiento.

---

### Conclusiones Personales / Personal Takeaways

* La realización de que un modelo de IA es esencialmente un reflejo de sus datos de entrenamiento; asegurar el pipeline de datos es tan crítico como asegurar la lógica de la aplicación.
* Los ejemplos adversariales son fascinantes — la precisión matemática requerida para voltear la clasificación de un modelo mientras permanece invisible al ojo humano resalta la fragilidad de las redes neuronales profundas.
* El NIST AI RMF es una herramienta altamente práctica para estandarizar evaluaciones de seguridad de IA, cambiando el enfoque de parcheo ad-hoc a gestión de riesgo sistémica.

---

* **Fuente / Source:**
  * [RAHULKATARA1/TryHackMe-AI-Security-Path — securing-ai-systems](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path/tree/main/Section-2-Secure-AI-Systems/01-securing-ai-systems)
  * [Answers for the TryHackMe Securing AI Systems Room — Simon Taplin](https://simontaplin.net/2026/05/17/answers-for-the-tryhackme-securing-ai-systems-room/)

*Documentación para propósitos educativos y registro de CTF.*
