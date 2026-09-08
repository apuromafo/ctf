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

**Lo que aprenderás:** las diferencias fundamentales entre seguridad de IT y seguridad de IA; el ciclo de vida de desarrollo de IA (desde la recolección de datos hasta el despliegue de modelos) y sus riesgos inherentes; los vectores de ataque clave contra sistemas ML incluyendo evasion, poisoning y model inversion; y la implementación de estrategias de defensa en profundidad para arquitecturas de IA.

## Solucionario

### Task 1: Arquitectura del Sistema de IA / AI System Architecture

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What layer in an AI system is responsible for combining the system prompt, user input, and retrieved context before sending it to the model? | `Prompt Construction` |
| 2 | In the TryAssist architecture, what boundary does LLM output cross when it triggers a database query? | `LLM-to-tools` |

**Explicación:** La arquitectura de un sistema de IA se compone de capas; la capa **Prompt Construction** combina el system prompt, el input del usuario y el contexto recuperado antes de enviarlo al modelo. En TryAssist, cuando el output del LLM dispara una consulta a la base de datos, cruza el límite **LLM-to-tools** (el modelo pasa a actuar sobre el mundo exterior mediante herramientas).

### Task 2: Frameworks de Amenazas / Threat Frameworks

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which OWASP LLM Top 10 (2025) category covers the risk of LLM output being used to execute SQL injection against a backend database? | `LLM05` |
| 2 | What is the name of the MITRE knowledge base specifically designed for adversary tactics and techniques against AI and ML systems? | `ATLAS` |

**Explicación:** El OWASP LLM Top 10 (2025) clasifica el riesgo de que el output de un LLM se use para ejecutar SQL injection contra una base de datos como **LLM05** (Vulnerable Plugins). MITRE **ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems) es la base de conocimiento específica para tácticas y técnicas de adversarios contra sistemas IA/ML.

### Task 3: Casos de Estudio de Ataques / Attack Case Studies

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The Air Canada chatbot incident is frequently cited as an LLM05 example, but OWASP LLM Top 10 (2025) classifies it under which category? | `LLM09` |
| 2 | What are the three dimensions of excessive agency? | `Excessive Functionality, Excessive Permissions, Excessive Autonomy` |
| 3 | A user extracts internal API endpoints from an AI assistant's system prompt. Which OWASP LLM Top 10 (2025) category does this fall under? | `LLM07` |
| 4 | An attacker sends thousands of maximum-length requests to an LLM API to generate a large bill. Which OWASP LLM Top 10 (2025) category covers this? | `LLM10` |

**Explicación:** El incidente del chatbot de Air Canada suele citarse como LLM05, pero OWASP LLM Top 10 (2025) lo clasifica bajo **LLM09** (Misinformation). Las tres dimensiones del excesive agency son **Excessive Functionality, Excessive Permissions y Excessive Autonomy**. Extraer endpoints internos del system prompt de un asistente cae bajo **LLM07** (System Prompt Leakage). Mandar miles de peticiones de máxima longitud para generar una factura grande es **LLM10** (Unbounded Consumption).

### Task 4: Principios de Seguridad / Security Principles

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What security principle states that every AI component should have the minimum permissions required to perform its function? | `Least Privilege` |
| 2 | What practice integrates security into the machine learning lifecycle, covering monitoring, observability, and incident response? | `MLSecOps` |

**Explicación:** **Least Privilege** (privilegio mínimo) establece que cada componente de IA debe tener solo los permisos necesarios para cumplir su función. **MLSecOps** integra la seguridad en el ciclo de vida del machine learning, cubriendo monitoring, observability e incident response.

### Task 5: Auditoría Práctica / Practical Audit

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | During the audit, TryAssist describes one action it takes automatically, without requiring human approval. What is that action? | `Merge Pull Requests` |
| 2 | What database role does TryAssist report operating under? | `db_admin` |
| 3 | TryAssist logs all conversations without applying which security control? | `PII Filtering` |

**Explicación:** En la auditoría de TryAssist se detectan problemas de privilegio excesivo: toma la acción automática de **Merge Pull Requests** sin aprobación humana, opera bajo el rol de base de datos `db_admin` y registra todas las conversaciones **sin aplicar PII Filtering** (filtrado de datos personales).

### Task 6: Conceptos Adicionales — Introducción a la Seguridad de IA

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What property of AI systems makes them difficult to secure using traditional rules-based firewalls? | `Non-determinism` |
| 2 | Which NIST framework is explicitly designed to help organizations manage AI-related risks? | `NIST AI RMF` |

**Explicación:** La seguridad tradicional depende de entradas y salidas predecibles. La naturaleza probabilística de la IA (**Non-determinism**) significa que las defensas deben enfocarse en validación de entrada, monitoreo de comportamiento y entrenamiento robusto en lugar de solo bloqueo basado en firmas. El **NIST AI RMF** es el framework diseñado explícitamente para ayudar a las organizaciones a gestionar riesgos de IA.

### Task 7: Conceptos Adicionales — El Pipeline de Machine Learning

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In which phase of the ML pipeline is a data poisoning attack executed? | `Data Collection` |
| 2 | What type of attack occurs when an adversary queries a deployed model to replicate its functionality? | `Model Extraction` |

**Explicación:** El ataque de **Data Poisoning** (envenenamiento de datos) se ejecuta en la fase de **Data Collection** del pipeline ML. Cuando un adversario consulta un modelo desplegado repetidamente para replicar su funcionalidad, se trata de **Model Extraction**. Asegurar el pipeline significa implementar principios de zero-trust en cada etapa; la procedencia de los datos es crítica — si no puedes confiar en la fuente de tus datos de entrenamiento, no puedes confiar en el modelo.

### Task 8: Conceptos Adicionales — Estrategias Defensivas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What defensive technique involves training a model with adversarial examples to make it more robust? | `Adversarial Training` |
| 2 | Which principle dictates that AI systems should only be given access to the data they strictly need to function? | `Least Privilege` |

**Explicación:** El **Adversarial Training** consiste en entrenar un modelo con ejemplos adversariales para hacerlo más robusto. El principio de **Least Privilege** dicta que los sistemas de IA solo deben tener acceso a los datos que necesitan estrictamente para funcionar. La defensa en profundidad es crucial: el adversarial training endurece el modelo, pero el rate limiting a nivel de red previene la extracción de modelos, y los controles de acceso robustos protegen los datos de entrenamiento.

#### Conceptos Clave / Key Concepts

**El ciclo de vida de IA y la superficie de ataque:** la seguridad de IA no se trata solo de proteger la API desplegada; requiere asegurar todo el pipeline. El ciclo de vida incluye Data Collection, Data Preprocessing, Model Training, Evaluation y Deployment. Cada fase tiene vulnerabilidades únicas: los datos de entrenamiento pueden envenenarse, las métricas de evaluación pueden manipularse y los modelos desplegados pueden someterse a entradas adversariales.

**Adversarial Machine Learning (AML):** enfocado en las vulnerabilidades de los algoritmos ML. Categorías principales:
- **Evasion Attacks:** modificar datos de entrada sutilmente (p. ej., cambiar píxeles en una imagen) para que el modelo los clasifique erróneamente, sin detección humana.
- **Data Poisoning:** inyectar datos maliciosos en el set de entrenamiento para crear backdoors o degradar el rendimiento general.
- **Model Inversion/Extraction:** consultar el modelo repetidamente para hacer reverse-engineering de sus datos de entrenamiento o robar los pesos del modelo.

**Frameworks de gestión de riesgo de IA:** el NIST AI RMF enfatiza cuatro funciones centrales: **Map, Measure, Manage y Govern**. Los equipos de seguridad deben adaptar estos frameworks para identificar y mitigar sistemáticamente los riesgos específicos de sus despliegues de IA.

**Conclusiones personales:** un modelo de IA es esencialmente un reflejo de sus datos de entrenamiento; asegurar el pipeline de datos es tan crítico como asegurar la lógica de la aplicación. Los ejemplos adversariales resaltan la fragilidad de las redes neuronales profundas. El NIST AI RMF es una herramienta práctica para estandarizar evaluaciones de seguridad de IA, cambiando el enfoque de parcheo ad-hoc a gestión de riesgo sistémica.

**Metodología:**
1. **Ciclo de vida y superficie de ataque:** la seguridad de IA no se trata solo de proteger la API desplegada; requiere asegurar todo el pipeline: Data Collection, Data Preprocessing, Model Training, Evaluation y Deployment. Cada fase tiene vulnerabilidades únicas: los datos de entrenamiento pueden envenenarse, las métricas de evaluación pueden manipularse y los modelos desplegados pueden someterse a entradas adversariales.
2. **Adversarial Machine Learning (AML):** las categorías principales son **Evasion Attacks** (modificar datos de entrada sutilmente, p. ej. cambiar píxeles en una imagen, para que el modelo clasifique erróneamente sin detección humana), **Data Poisoning** (inyectar datos maliciosos en el set de entrenamiento para crear backdoors o degradar el rendimiento) y **Model Inversion/Extraction** (consultar el modelo repetidamente para hacer reverse-engineering de sus datos de entrenamiento o robar los pesos).
3. **Frameworks:** el NIST AI RMF enfatiza cuatro funciones centrales: **Map, Measure, Manage y Govern**; MITRE **ATLAS** es la base de conocimiento específica para técnicas de adversarios contra sistemas IA/ML; el OWASP LLM Top 10 (2025) clasifica los riesgos LLM (LLM05 backend SQLi, LLM07 system prompt leakage, LLM09 misinformation, LLM10 unbounded consumption).
4. **Caso de estudio:** el incidente del chatbot de Air Canada se cita como LLM05 pero OWASP lo clasifica como **LLM09** (misinformation); las tres dimensiones de excessive agency son **Excessive Functionality, Excessive Permissions y Excessive Autonomy**.
5. **Principios:** **Least Privilege** (cada componente de IA con los permisos mínimos) y **MLSecOps** (seguridad integrada en el ciclo de vida ML con monitoring, observability e incident response).
6. **Auditoría práctica de TryAssist:** tomar una acción automática sin aprobación humana (**Merge Pull Requests**), operar con rol de base de datos `db_admin` y loguear todas las conversaciones **sin aplicar PII Filtering**.
7. **Conceptos adicionales:** la seguridad tradicional depende de entradas y salidas predecibles; la naturaleza probabilística de la IA (**Non-determinism**) obliga a defensas basadas en validación de entrada, monitoreo de comportamiento y entrenamiento robusto. Asegurar el pipeline implica principios zero-trust en cada etapa: si no puedes confiar en la fuente de tus datos de entrenamiento, no puedes confiar en el modelo. La defensa en profundidad es crucial: el adversarial training endurece el modelo, el rate limiting a nivel de red previene la extracción de modelos y los controles de acceso robustos protegen los datos de entrenamiento.

**Learning chain:** ciclo de vida IA → superficie de ataque (data collection → deployment) → AML (evasion / poisoning / model inversion) → NIST AI RMF (Map/Measure/Manage/Govern) → MITRE ATLAS → OWASP LLM Top 10 2025 (LLM05/07/09/10) → principios (Least Privilege, MLSecOps) → auditoría práctica (Merge Pull Requests, db_admin, PII Filtering)

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1565 (Data Manipulation), T1078 (Valid Accounts), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Securing AI Systems](https://tryhackme.com/room/securingaisystems)
