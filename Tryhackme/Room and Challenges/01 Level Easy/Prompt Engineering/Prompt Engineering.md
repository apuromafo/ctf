# Prompt Engineering

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `promptengineeringaisec` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/promptengineeringaisec) |
| **Sección** | AI Security |
| **Fuente** | THM |
| **Componentes** | LLM fundamentals, Anatomy of a prompt, System/User prompts, CoT, Templates |
| **Impacto** | Conceptos de prompt engineering para seguridad |

---

**Contexto:** Room del AI Security Path de TryHackMe que sienta las bases del prompt engineering aplicado a seguridad. Explica cómo procesan texto los LLMs (tokens, nondeterminismo, temperatura), la anatomía de un prompt (instrucción, contexto, formato de salida, constraints), la diferencia entre prompts de sistema y de usuario (jerarquía de instrucciones), y técnicas avanzadas como Chain-of-Thought y templates. Incluye un desafío calificado.

## Solucionario

### Task 2: LLM Fundamentals

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the term for the smallest units that an LLM breaks text into to process it? | `tokens` |
| 2 | What parameter would you set to 0.0 to make an LLM behave as close to deterministic as possible? | `temperature` |

### Task 3: The Anatomy of a Prompt

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which pillar instructs the model on how the answer should be structured (bullet points/JSON)? | `output format` |
| 2 | Which pillar specifies rules or limits imposed on the model's response (tone/forbidden topics)? | `constraints` |
| 3 | Which pillar provides the AI with relevant background information or scenario? | `context` |
| 4 | Which pillar defines the core command or action the AI should perform? | `instruction` |

### Task 4: System vs User Prompts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of prompt is developer-defined, persistent, remains constant across all sessions? | `system prompt` |
| 2 | What is the term for the intended order of priority between system and user instructions? | `instruction hierarchy` |

### Task 5: Advanced Prompting Techniques

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What term for the prompting technique by Google researchers 2022 that breaks tasks into intermediate reasoning steps? | `chain-of-thought` |
| 2 | What prompting technique provides no examples, relying on pre-trained knowledge? | `zero-shot` |
| 3 | What prompting technique saves and reuses a standardised prompt structure for recurring tasks? | `prompt templates` |
| 4 | What simple phrase added to a prompt triggers Zero-shot CoT? | `let's think step by step` |

### Task 6: Challenge

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{Pr0mpt_3ng1neer}` |

---

**Metodología:** Aprender cómo tokeniza y genera el LLM (control de determinismo vía temperatura), dominar los cuatro pilares del prompt engineering, entender la jerarquía system > user, y aplicar técnicas avanzadas (CoT, zero-shot, templates) para completar el desafío de prompt engineering.

**Learning chain:** Fundamentos de LLM → Anatomía del prompt → System vs User prompts → Técnicas avanzadas (CoT) → Desafío práctico

**MITRE ATT&CK:** N/A (Room teórico-práctico de prompt engineering)

**Fuente:** [TryHackMe - Prompt Engineering](https://tryhackme.com/r/room/promptengineeringaisec)
