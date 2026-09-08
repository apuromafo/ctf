# AI Threat Modelling
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `ai-threat-modelling` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ai-threat-modelling) |
| **Sección** | Secure AI Systems (Section 2 of 5) |
| **Fuente** | [vanshksingh/TryHackMe-AI-Security-Path](https://github.com/vanshksingh/TryHackMe-AI-Security-Path) — `ai-threat-modelling\Readme.md` |
| **Componentes** | Threat modelling, STRIDE adaptado a IA, MITRE ATLAS, OWASP LLM Top 10 (2025), RAG, chatbot LLM, modelos de detección de fraude, Denial of Wallet, prompt injection |
| **Impacto** | Enseña a identificar activos y superficies de ataque específicos de IA, aplicar STRIDE a sistemas IA/ML, usar MITRE ATLAS, mapear riesgos con OWASP LLM Top 10 y producir evaluaciones de amenazas de IA estructuradas (escenario MegaCorp). |
---
**Contexto:** La IA ya está integrada en entornos empresariales (chatbots de soporte, motores de recomendación, detección de fraude) e introduce nuevas superficies de ataque que los frameworks tradicionales no abordan por completo. Enfocada en defensa: analizar y documentar amenazas en lugar de explotarlas. Escenario **MegaCorp**: Customer Chatbot (LLM + RAG), Recommendation Engine y Fraud Detection System; el CISO pide una evaluación completa de amenazas.
*EN: AI is already embedded in enterprise environments (support chatbots, recommendation engines, fraud detection) and introduces new attack surfaces that traditional frameworks don't fully address. Defense-focused: analyze and document threats rather than exploit them. Scenario **MegaCorp**: Customer Chatbot (LLM + RAG), Recommendation Engine and Fraud Detection System; the CISO requests a full threat assessment.*
## Solucionario
### Task 1 — Introducción / Introduction
**Explicación:** Riesgos clave de seguridad de IA: los frameworks tradicionales como STRIDE siguen siendo útiles, pero la IA añade amenazas únicas (envenenamiento de datos de entrenamiento, robo de modelo, prompt injection, fuga de datos sensibles, salidas no deterministas). Los sistemas de IA pueden comportarse diferente ante la misma entrada.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to learn about AI threat modelling! | `No answer needed` |
### Task 2 — Activos Específicos de IA y Superficies de Ataque / AI-Specific Assets and Attack Surfaces
**Explicación:** Activos de IA: **Training Data** (envenenada altera permanentemente el modelo), **Model Weights/Parameters** (el robo da una copia completa del modelo — no se "rotan" como contraseñas), **Embedding Vectors** (manipulados afectan a la precisión de recuperación RAG), **System Prompts** (la fuga expone guardarraíles), **Feature Stores** (manipulados cambian lo que ve el modelo en vivo), **Model Registry/Artifacts** (los atacantes pueden reemplazar modelos legítimos por maliciosos). Características: comportamiento no determinista y problema de caja negra (análisis por testing entrada/salida u observación de comportamiento).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a RAG-based system, which AI asset type is used to retrieve relevant context at query time? | `Embedding Vectors` |
| 2 | An attacker gains access to MegaCorp's model registry and swaps the production model for a modified version. Which AI-specific asset has been compromised? | `Model Registry / Artifacts` |
### Task 3 — Cadena de Suministro de Datos y Brechas de STRIDE / Data Supply Chain and STRIDE's Gaps
**Explicación:** Etapas de la cadena de suministro de datos de IA: **1. Data Collection** (inyección de datos maliciosos/manipulados), **2. Cleaning and Labelling** (etiquetas envenenadas enseñan patrones falsos), **3. Model Training** (los datos maliciosos se incrustan en los pesos; requieren reentrenamiento), **4. Validation and Packaging** (reemplazo de modelos con backdoor; los backdoors evaden la validación porque el trigger falta en testing), **5. Inference** (contexto RAG manipulado influye en salidas). Los compromisos de IA permanecen ocultos durante semanas/meses (ej: el modelo de fraude reentrenado mensualmente con transacciones fraudulentas diseñadas). **Brechas de STRIDE:** Training Data Poisoning → **Tampering** (efectos retrasados); Adversarial Inputs → múltiples categorías; Expanded Privileges → **Elevation of Privilege** (los LLM modernos pueden ejecutar código/navegar/enviar emails); Model Theft → **Information Disclosure**.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | An attacker injects crafted data points into a training pipeline over several months, gradually shifting the model's decision boundaries. At which supply chain stage does the attacker inject the malicious data? | `Data Collection` |
| 2 | Which STRIDE category is insufficient for capturing the delayed, diffuse effects of training data poisoning? | `Tampering` |
### Task 4 — Adaptando STRIDE para Sistemas de IA / Adapting STRIDE for AI Systems
**Explicación:** Refresco STRIDE: **S**poofing (autenticidad), **T**ampering (integridad), **R**epudiation (no repudio), **I**nformation Disclosure (confidencialidad), **D**enial of Service (disponibilidad), **E**levation of Privilege (autorización). Adaptación a IA:
1. **Spoofing → Data Source Impersonation:** inyección de contenido malicioso en knowledge bases RAG/vector DBs; impersonación de modelo.
2. **Tampering → Data Poisoning:** manipulación de datos de entrenamiento; MITRE ATLAS `AML.T0020`, `AML.T0018`.
3. **Repudiation → Falta de pistas de auditoría:** la IA no puede explicar por qué decidió, qué versión respondió o qué contexto influyó.
4. **Information Disclosure → Model Extraction:** consultas repetidas a la API para reconstruir el modelo; `AML.T0024 Extract ML Model`, `AML.T0025 Infer Training Data Membership`.
5. **Denial of Service → Explotación de costo de inferencia (Denial of Wallet):** abuso de inferencias caras; agotamiento de GPU, sponge examples; OWASP `LLM10:2025 Unbounded Consumption`.
6. **Elevation of Privilege → Jailbreaking:** evasión de salvaguardas con prompts; agencia excesiva, escalada cross-plugin; OWASP `LLM06:2025 Excessive Agency`.
Lo que STRIDE no cubre: **Adversarial Examples** (abarcan varias categorías), **Model Bias and Fairness** (cumplimiento) y **Emergent Behaviour**.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the primary AI-specific manifestation of Information Disclosure in the STRIDE-AI mapping? | `Model Extraction` |
| 2 | An attacker crafts prompts that cause an LLM to bypass its safety guidelines and content restrictions. Which STRIDE category does this map to? | `Elevation of Privilege` |
| 3 | Which OWASP LLM Top 10 (2025) entry addresses the risks of AI systems being granted too many permissions or too much autonomy? | `LLM06:2025 — Excessive Agency` |
| 4 | An attacker drives your monthly inference bill from $15,000 to $180,000 without taking your service offline. What is this type of attack commonly called? | `Denial of Wallet` |
### Task 5 — MITRE ATLAS: El Catálogo de Técnicas de Amenazas de IA / MITRE ATLAS - The AI Threat Technique Catalogue
**Explicación:** MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) es el framework tipo ATT&CK para ataques contra sistemas de IA/ML (a principios de 2026: 16 tácticas, 155 técnicas, 35 mitigaciones, 52 estudios de caso). Componentes: **Tactic** (por qué, ej. `ML Attack Staging AML.TA0012`), **Technique** (cómo, ej. `AML.T0020`), **Sub-technique** (variación, ej. `AML.T0043.004 Craft Adversarial Data`), **Mitigation**. Técnicas clave: `AML.T0020` Data Poisoning (→Tampering), `AML.T0024` Model Extraction (→Information Disclosure), `AML.T0015` Evade ML Model (→Tampering/Spoofing/EoP), `AML.T0051` LLM Prompt Injection (directa e indirecta), `AML.T0018` Backdoor ML Model (triggers ocultos; comportamiento normal durante testing). Workflow recomendado: empezar con STRIDE → enriquecer con ATLAS (técnicas concretas, real-world behavior) → aplicar mitigaciones (procedencia de datos, validación de entrada, monitoreo de drift). Estudios de caso: **ShadowRay (`AML.CS0023`)** — explotación del framework Ray en producción; **Morris II Worm (`AML.CS0024`)** — gusano de prompt injection auto-replicante vía RAG email.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the acronym ATLAS stand for? | `Adversarial Threat Landscape for Artificial-Intelligence Systems` |
| 2 | Which ATLAS case study described a self-replicating prompt injection worm that spread between AI agents via RAG email systems? | `Morris II` |
| 3 | What is the ATLAS technique ID for Model Extraction? | `AML.T0024` |
### Task 6 — OWASP LLM Top 10: Mapeando Riesgos a Componentes / OWASP LLM Top 10 - Mapping Risks to Components
**Explicación:** OWASP LLM Top 10 (2025): **LLM01** Prompt Injection, **LLM02** Sensitive Information Disclosure, **LLM03** Supply Chain, **LLM04** Data and Model Poisoning, **LLM05** Improper Output Handling, **LLM06** Excessive Agency, **LLM07** System Prompt Leakage, **LLM08** Vector and Embedding Weaknesses, **LLM09** Misinformation, **LLM10** Unbounded Consumption. Lectura bidireccional: riesgo → componente (Prompt Injection impacta inference endpoints, RAG pipelines y vector databases) y componente → riesgo (Vector DB: LLM01, LLM08, LLM09). Perfiles: **LLM Inference Endpoint** concentra 7 de los 10 riesgos (requiere hardening y monitoreo fuertes); **Vector DB/RAG** (prompt injection indirecta, ataques de embeddings, fuentes obsoletas); **Training Pipeline** (compromiso de supply chain, envenenamiento de datos). Relación: STRIDE-AI categoriza amenazas, MITRE ATLAS documenta técnicas, OWASP mapea riesgos a componentes.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many of the OWASP LLM Top 10 entries affect the LLM Inference Endpoint? | `7` |
| 2 | An organisation notices their chatbot is rendering LLM output directly in the browser without sanitisation. Which OWASP entry does this fall under? | `Improper Output Handling` |
| 3 | Which component in a typical LLM architecture is the primary one that needs hardening against data and model supply chain risks (LLM03)? | `Training Pipeline` |
### Task Final — Ejercicio de Threat Modelling de IA / AI Threat Modelling Exercise
**Explicación:** Ejercicio interactivo: identificar vulnerabilidades OWASP LLM Top 10, mapear riesgos a componentes, aplicar STRIDE-AI y usar técnicas MITRE ATLAS. Al completarlo se obtiene la flag.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del ejercicio de threat modelling | `THM{AI_THREAT_MODEL_COMPLETE}` |
---
**Metodología:** Workflow completo de threat modelling de IA: activos/ataque surfaces → STRIDE-AI → MITRE ATLAS → OWASP LLM Top 10 → evaluación estructurada aplicada al escenario MegaCorp.
**Learning chain:** activos específicos de IA → cadena de suministro de datos → adaptación de STRIDE → catálogo ATLAS → mapeo OWASP a componentes → ejercicio práctico de evaluación de amenazas.
**MITRE ATT&CK / ATLAS:** AML.TA0012 (ML Attack Staging), AML.T0020 (Data Poisoning), AML.T0024 (Model Extraction), AML.T0015 (Evade ML Model), AML.T0051 (LLM Prompt Injection), AML.T0018 (Backdoor ML Model), AML.CS0023 (ShadowRay), AML.CS0024 (Morris II); OWASP LLM01-LLM10.
**Fuente:** [TryHackMe - AI Threat Modelling](https://tryhackme.com/room/ai-threat-modelling)