# Securing AI Systems

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `securingaisystems` |
| **Link** | [TryHackMe](https://tryhackme.com/room/securingaisystems) |
| **Sección** | 01 Level Easy |
| **Fuente** | RAHULKATARA1/TryHackMe-AI-Security-Path (GitHub) + Simon Taplin (simontaplin.net) |
| **Componentes** | NIST AI RMF / OWASP LLM Top 10 / MITRE ATLAS / Adversarial Machine Learning / MLSecOps / Least Privilege / Prompt Construction |
| **Impacto** | Fundamentos para asegurar pipelines de IA/ML: ciclo de vida, vectores de ataque (evasion, poisoning, model inversion) y defensa en profundidad |

---

**Contexto:** Esta room sirve como el pilar fundamental para entender cómo asegurar pipelines de Inteligencia Artificial y Machine Learning. A diferencia del software tradicional, los sistemas de IA introducen comportamientos no deterministas, dependencia de datasets masivos y cadenas de suministro complejas que requieren un cambio de paradigma en el pensamiento de seguridad. Exploramos el NIST AI Risk Management Framework (RMF) y los principios centrales de la defensa de IA, junto con casos de estudio de ataques reales y una auditoría práctica de un asistente LLM.

## Solucionario

### Task 1: Arquitectura del Sistema de IA / AI System Architecture

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What layer in an AI system is responsible for combining the system prompt, user input, and retrieved context before sending it to the model? | `Prompt Construction` |
| 2 | In the TryAssist architecture, what boundary does LLM output cross when it triggers a database query? | `LLM-to-tools` |

### Task 2: Frameworks de Amenazas / Threat Frameworks

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which OWASP LLM Top 10 (2025) category covers the risk of LLM output being used to execute SQL injection against a backend database? | `LLM05` |
| 2 | What is the name of the MITRE knowledge base specifically designed for adversary tactics and techniques against AI and ML systems? | `ATLAS` |

### Task 3: Casos de Estudio de Ataques / Attack Case Studies

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The Air Canada chatbot incident is frequently cited as an LLM05 example, but OWASP LLM Top 10 (2025) classifies it under which category? | `LLM09` |
| 2 | What are the three dimensions of excessive agency? | `Excessive Functionality, Excessive Permissions, Excessive Autonomy` |
| 3 | A user extracts internal API endpoints from an AI assistant's system prompt. Which OWASP LLM Top 10 (2025) category does this fall under? | `LLM07` |
| 4 | An attacker sends thousands of maximum-length requests to an LLM API to generate a large bill. Which OWASP LLM Top 10 (2025) category covers this? | `LLM10` |

### Task 4: Principios de Seguridad / Security Principles

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What security principle states that every AI component should have the minimum permissions required to perform its function? | `Least Privilege` |
| 2 | What practice integrates security into the machine learning lifecycle, covering monitoring, observability, and incident response? | `MLSecOps` |

### Task 5: Auditoría Práctica / Practical Audit

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | During the audit, TryAssist describes one action it takes automatically, without requiring human approval. What is that action? | `Merge Pull Requests` |
| 2 | What database role does TryAssist report operating under? | `db_admin` |
| 3 | TryAssist logs all conversations without applying which security control? | `PII Filtering` |

### Task 6: Conceptos Adicionales — Introducción a la Seguridad de IA

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What property of AI systems makes them difficult to secure using traditional rules-based firewalls? | `Non-determinism` |
| 2 | Which NIST framework is explicitly designed to help organizations manage AI-related risks? | `NIST AI RMF` |

### Task 7: Conceptos Adicionales — El Pipeline de Machine Learning

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In which phase of the ML pipeline is a data poisoning attack executed? | `Data Collection` |
| 2 | What type of attack occurs when an adversary queries a deployed model to replicate its functionality? | `Model Extraction` |

### Task 8: Conceptos Adicionales — Estrategias Defensivas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What defensive technique involves training a model with adversarial examples to make it more robust? | `Adversarial Training` |
| 2 | Which principle dictates that AI systems should only be given access to the data they strictly need to function? | `Least Privilege` |

---

**Metodología:**
1. **Ciclo de vida y superficie de ataque:** la seguridad de IA no se trata solo de proteger la API desplegada; requiere asegurar todo el pipeline: Data Collection, Data Preprocessing, Model Training, Evaluation y Deployment. Cada fase tiene vulnerabilidades únicas: los datos de entrenamiento pueden envenenarse, las métricas de evaluación pueden manipularse y los modelos desplegados pueden someterse a entradas adversariales.
2. **Adversarial Machine Learning (AML):** las categorías principales son **Evasion Attacks** (modificar datos de entrada sutilmente, p. ej. cambiar píxeles en una imagen, para que el modelo clasifique erróneamente sin detección humana), **Data Poisoning** (inyectar datos maliciosos en el set de entrenamiento para crear backdoors o degradar el rendimiento) y **Model Inversion/Extraction** (consultar el modelo repetidamente para hacer reverse-engineering de sus datos de entrenamiento o robar los pesos).
3. **Frameworks:** el NIST AI RMF enfatiza cuatro funciones centrales: **Map, Measure, Manage y Govern**; MITRE **ATLAS** es la base de conocimiento específica para técnicas de adversarios contra sistemas IA/ML; el OWASP LLM Top 10 (2025) clasifica los riesgos LLM (LLM05 banket a SQL injection, LLM07 system prompt leakage, LLM09 misinformation, LLM10 unbounded consumption).
4. **Caso de estudio:** el incidente del chatbot de Air Canada se cita como LLM05 pero OWASP lo clasifica como **LLM09** (misinformation); las tres dimensiones de excesive agency son **Excessive Functionality, Excessive Permissions y Excessive Autonomy**.
5. **Principios:** **Least Privilege** (cada componente de IA con los permisos mínimos) y **MLSecOps** (seguridad integrada en el ciclo de vida ML con monitoring, observability e incident response).
6. **Auditoría práctica de TryAssist:** tomar una acción automática sin aprobación humana (**Merge Pull Requests**), operar con rol de base de datos `db_admin` y loguear todas las conversaciones **sin aplicar PII Filtering**.
7. **Conceptos adicionales:** la seguridad tradicional depende de entradas y salidas predecibles; la naturaleza probabilística de la IA (**Non-determinism**) obliga a defensas basadas en validación de entrada, monitoreo de comportamiento y entrenamiento robusto. Asegurar el pipeline implica principios zero-trust en cada etapa: si no puedes confiar en la fuente de tus datos de entrenamiento, no puedes confiar en el modelo. La defensa en profundidad es crucial: el adversarial training endurece el modelo, el rate limiting a nivel de red previene la extracción de modelos y los controles de acceso robustos protegen los datos de entrenamiento.

**Learning chain:** ciclo de vida IA → superficie de ataque (data collection → deployment) → AML (evasion / poisoning / model inversion) → NIST AI RMF (Map/Measure/Manage/Govern) → MITRE ATLAS → OWASP LLM Top 10 2025 (LLM05/07/09/10) → principios (Least Privilege, MLSecOps) → auditoría práctica (Merge Pull Requests, db_admin, PII Filtering)

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1565 (Data Manipulation), T1078 (Valid Accounts), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Securing AI Systems](https://tryhackme.com/room/securingaisystems)