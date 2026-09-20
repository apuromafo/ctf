# AI Threat Modelling

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `aithreatmodelling` | [TryHackMe](https://tryhackme.com/room/aithreatmodelling) | AI Security Path | THM | STRIDE-AI, ATLAS, OWASP LLM Top 10, RAG, model registry | Alto |

---

**Contexto:** Sala del AI Security Path que profundiza en el modelado de amenazas de sistemas de IA mediante los marcos STRIDE-AI, MITRE ATLAS y OWASP LLM Top 10 (2025). Cubre desde la explotación de activos de IA (embedding vectors, model registries, training pipelines) hasta ataques de denegación de billetera, extracción de modelos y worms de prompt injection autoreplicantes. El participante aplica estos marcos a escenarios realistas de supply chain de IA.

## Solucionario

### Task 1: AI Asset Identification

**Explicación:** Se identifican los activos específicos de un sistema de IA: los embedding vectors usados para recuperar contexto en un sistema RAG y el model registry/artifacts cuando se sustituye el modelo de producción por una versión modificada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a RAG-based system, which AI asset type is used to retrieve relevant context at query time? | `Embedding Vectors` |
| 2 | An attacker gains access to MegaCorp's model registry and swaps the production model for a modified version. Which AI-specific asset has been compromised? | `Model Registry / Artifacts` |

### Task 2: AI Supply Chain & STRIDE-AI Mapping

**Explicación:** Se mapean los riesgos de la supply chain de IA a STRIDE-AI: la etapa del pipeline donde se inyectan datos maliciosos (Data Collection), la categoría STRIDE insuficiente para captar los efectos difusos del envenenamiento de datos (Tampering) y la manifestación de Information Disclosure específica de IA (Model extraction).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | An attacker injects crafted data points into a training pipeline over several months, gradually shifting the model's decision boundaries. At which supply chain stage does the attacker inject the malicious data? | `Data Collection` |
| 4 | Which STRIDE category is insufficient for capturing the delayed, diffuse effects of training data poisoning? | `Tampering` |
| 5 | What is the primary AI-specific manifestation of Information Disclosure in the STRIDE-AI mapping? | `Model extraction` |

### Task 3: LLM Vulnerabilities & OWASP LLM Top 10

**Explicación:** Se analizan vulnerabilidades de LLMs: los prompts que fuerzan al modelo a saltarse sus directrices de seguridad se mapean a Elevation of Privilege, la entrada OWASP LLM Top 10 (2025) sobre permisos excesivos es Excessive Agency, y el incremento descontrolado de la factura de inferencia sin dejar sin servicio es Denial of Wallet.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | An attacker crafts prompts that cause an LLM to bypass its safety guidelines and content restrictions. Which STRIDE category does this map to? | `Elevation of Privilege` |
| 7 | Which OWASP LLM Top 10 (2025) entry addresses the risks of AI systems being granted too many permissions or too much autonomy? | `LLM06:2025 — Excessive Agency` |
| 8 | An attacker drives your monthly inference bill from $15,000 to $180,000 without taking your service offline. What is this type of attack commonly called? | `Denial of Wallet` |

### Task 4: MITRE ATLAS & Case Studies

**Explicación:** Se profundiza en MITRE ATLAS: el significado del acrónimo, el caso de estudio del worm autoreplicante Morris II que se propagó entre agentes de IA vía sistemas de correo RAG, y el identificador de técnica para Model Extraction.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9 | What does the acronym ATLAS stand for? | `Adversarial Threat Landscape for Artificial-Intelligence Systems` |
| 10 | Which ATLAS case study described a self-replicating prompt injection worm that spread between AI agents via RAG email systems? | `Morris II` |
| 11 | What is the ATLAS technique ID for Model Extraction? | `AML.T0024` |

### Task 5: Architecture Analysis & Flags

**Explicación:** Análisis de arquitectura: cuántas entradas del OWASP LLM Top 10 afectan al endpoint de inferencia, la entrada correspondiente a renderizar la salida del LLM sin sanitizar en el navegador, el componente principal a endurecer frente a riesgos de supply chain (LLM03) y la flag final del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 12 | How many of the OWASP LLM Top 10 entries affect the LLM Inference Endpoint? | `6` |
| 13 | An organisation notices their chatbot is rendering LLM output directly in the browser without sanitisation. Which OWASP entry does this fall under? | `Improper Output Handling` |
| 14 | Which component in a typical LLM architecture is the primary one that needs hardening against data and model supply chain risks (LLM03)? | `Training pipeline` |
| 15 | What's the flag? | `THM{AI_THREAT_MODEL_COMPLETE}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a RAG-based system, which AI asset type is used to retrieve relevant context at query time? | `Embedding Vectors` |
| 2 | An attacker gains access to MegaCorp's model registry and swaps the production model for a modified version. Which AI-specific asset has been compromised? | `Model Registry / Artifacts` |
| 3 | An attacker injects crafted data points into a training pipeline over several months, gradually shifting the model's decision boundaries. At which supply chain stage does the attacker inject the malicious data? | `Data Collection` |
| 4 | Which STRIDE category is insufficient for capturing the delayed, diffuse effects of training data poisoning? | `Tampering` |
| 5 | What is the primary AI-specific manifestation of Information Disclosure in the STRIDE-AI mapping? | `Model extraction` |
| 6 | An attacker crafts prompts that cause an LLM to bypass its safety guidelines and content restrictions. Which STRIDE category does this map to? | `Elevation of Privilege` |
| 7 | Which OWASP LLM Top 10 (2025) entry addresses the risks of AI systems being granted too many permissions or too much autonomy? | `LLM06:2025 — Excessive Agency` |
| 8 | An attacker drives your monthly inference bill from $15,000 to $180,000 without taking your service offline. What is this type of attack commonly called? | `Denial of Wallet` |
| 9 | What does the acronym ATLAS stand for? | `Adversarial Threat Landscape for Artificial-Intelligence Systems` |
| 10 | Which ATLAS case study described a self-replicating prompt injection worm that spread between AI agents via RAG email systems? | `Morris II` |
| 11 | What is the ATLAS technique ID for Model Extraction? | `AML.T0024` |
| 12 | How many of the OWASP LLM Top 10 entries affect the LLM Inference Endpoint? | `6` |
| 13 | An organisation notices their chatbot is rendering LLM output directly in the browser without sanitisation. Which OWASP entry does this fall under? | `Improper Output Handling` |
| 14 | Which component in a typical LLM architecture is the primary one that needs hardening against data and model supply chain risks (LLM03)? | `Training pipeline` |
| 15 | What's the flag? | `THM{AI_THREAT_MODEL_COMPLETE}` |

---

**Metodología:** Se recorrieron los marcos de amenazas AI (STRIDE-AI para mapeo de categorías, MITRE ATLAS para técnicas y casos de estudio, OWASP LLM Top 10 2025 para vulnerabilidades específicas de LLMs). Cada pregunta se respondió mapeando el escenario al framework correspondiente: activos de IA comprometidos, etapas del supply chain, categorías STRIDE insuficientes, y técnicas ATLAS documentadas (AML.T0024, AML.TA0002).

**Learning chain:** AI Assets → Supply Chain → STRIDE-AI → OWASP LLM Top 10 → MITRE ATLAS → Morris II → Model Extraction → Denial of Wallet

**Lección:** *El modelado de amenazas de IA requiere combinar marcos (STRIDE-AI, ATLAS y OWASP LLM Top 10) porque los ataques a modelos —poisoning, model extraction, denial of wallet— no encajan del todo en las categorías clásicas.*

**MITRE ATT&CK:** N/A — Sala defensiva de modelado de amenazas AI (marcos ATLAS/STRIDE-AI/OWASP)

**Fuente:** [TryHackMe - AI Threat Modelling](https://tryhackme.com/room/aithreatmodelling)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.