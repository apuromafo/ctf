# AI Threat Modelling

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `aithreatmodelling` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/aithreatmodelling) |
| **Sección** | AI Security Path |
| **Fuente** | THM |
| **Componentes** | STRIDE-AI, ATLAS, OWASP LLM Top 10, RAG, model registry |
| **Impacto** | Alto |

---

**Contexto:** Sala del AI Security Path que profundiza en la amenaza modelada de sistemas de IA mediante los marcos STRIDE-AI, MITRE ATLAS y OWASP LLM Top 10 (2025). Cubre desde la explotación de activos de IA (embedding vectors, model registries, training pipelines) hasta ataques de denegación de billetera, extracción de modelos y worms de prompt injection autoreplicantes. El participante aplica estos marcos a escenarios realistas de supply chain de IA.

## Solucionario

### Task 1: AI Asset Identification

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a RAG-based system, which AI asset type is used to retrieve relevant context at query time? | `Embedding Vectors` |
| 2 | An attacker gains access to MegaCorp's model registry and swaps the production model for a modified version. Which AI-specific asset has been compromised? | `Model Registry / Artifacts` |

### Task 2: AI Supply Chain & STRIDE-AI Mapping

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | An attacker injects crafted data points into a training pipeline over several months, gradually shifting the model's decision boundaries. At which supply chain stage does the attacker inject the malicious data? | `Data Collection` |
| 4 | Which STRIDE category is insufficient for capturing the delayed, diffuse effects of training data poisoning? | `Tampering` |
| 5 | What is the primary AI-specific manifestation of Information Disclosure in the STRIDE-AI mapping? | `Model extraction` |

### Task 3: LLM Vulnerabilities & OWASP LLM Top 10

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | An attacker crafts prompts that cause an LLM to bypass its safety guidelines and content restrictions. Which STRIDE category does this map to? | `Elevation of Privilege` |
| 7 | Which OWASP LLM Top 10 (2025) entry addresses the risks of AI systems being granted too many permissions or too much autonomy? | `LLM06:2025 — Excessive Agency` |
| 8 | An attacker drives your monthly inference bill from $15,000 to $180,000 without taking your service offline. What is this type of attack commonly called? | `Denial of Wallet` |

### Task 4: MITRE ATLAS & Case Studies

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9 | What does the acronym ATLAS stand for? | `Adversarial Threat Landscape for Artificial-Intelligence Systems` |
| 10 | Which ATLAS case study described a self-replicating prompt injection worm that spread between AI agents via RAG email systems? | `Morris II` |
| 11 | What is the ATLAS technique ID for Model Extraction? | `AML.T0024` |

### Task 5: Architecture Analysis & Flags

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 12 | How many of the OWASP LLM Top 10 entries affect the LLM Inference Endpoint? | `6` |
| 13 | An organisation notices their chatbot is rendering LLM output directly in the browser without sanitisation. Which OWASP entry does this fall under? | `Improper Output Handling` |
| 14 | Which component in a typical LLM architecture is the primary one that needs hardening against data and model supply chain risks (LLM03)? | `Training pipeline` |
| 15 | What's the flag? | `THM{AI_THREAT_MODEL_COMPLETE}` |

---

**Metodología:** Se recorrieron los marcos de amenazas AI (STRIDE-AI para mapeo de categorías, MITRE ATLAS para técnicas y casos de estudio, OWASP LLM Top 10 2025 para vulnerabilidades específicas de LLMs). Cada pregunta se respondió mapeando el escenario al framework correspondiente: activos de IA comprometidos, etapas del supply chain, categorías STRIDE insuficientes, y técnicas ATLAS documentadas (AML.T0024, AML.TA0002).

**Learning chain:** AI Assets → Supply Chain → STRIDE-AI → OWASP LLM Top 10 → MITRE ATLAS → Morris II → Model Extraction → Denial of Wallet

**MITRE ATT&CK:** N/A — Sala defensiva de modelado de amenazas AI (marcos ATLAS/STRIDE-AI/OWASP)

**Fuente:** [TryHackMe - AI Threat Modelling](https://tryhackme.com/r/room/aithreatmodelling)
