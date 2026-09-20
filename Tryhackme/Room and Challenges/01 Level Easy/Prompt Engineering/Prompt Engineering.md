# Prompt Engineering

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `promptengineeringaisec` | https://tryhackme.com/room/promptengineeringaisec | AI Security | THM | LLM fundamentals, Anatomy of a prompt, System/User prompts, CoT, Templates | Conceptos de prompt engineering para seguridad |

---

**Contexto:** Room del AI Security Path de TryHackMe que sienta las bases del prompt engineering aplicado a seguridad. Explica cómo procesan texto los LLMs (tokens, nondeterminismo, temperatura), la anatomía de un prompt (instrucción, contexto, formato de salida, constraints), la diferencia entre prompts de sistema y de usuario (jerarquía de instrucciones), y técnicas avanzadas como Chain-of-Thought y templates. Incluye un desafío calificado.

> **ES:** Room del AI Security Path que enseña los fundamentos del prompt engineering aplicado a la seguridad de LLMs: tokenización, anatomía del prompt, jerarquía system/user y técnicas avanzadas (Chain-of-Thought, templates), con un desafío práctico.
> **EN:** An AI Security Path room teaching the fundamentals of prompt engineering applied to LLM security: tokenization, prompt anatomy, system/user hierarchy, and advanced techniques (Chain-of-Thought, templates), with a practical challenge.

## Solucionario

### Task 2: Fundamentos de LLM / LLM Fundamentals

**Explicación:** Se explican los conceptos fundamentales de los LLMs: la tokenización (división del texto en unidades mínimas), el nondeterminismo de las respuestas y la temperatura como parámetro de control de determinismo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the term for the smallest units that an LLM breaks text into to process it? | `tokens` |
| 2 | What parameter would you set to 0.0 to make an LLM behave as close to deterministic as possible? | `temperature` |

### Task 3: Anatomía del prompt / The Anatomy of a Prompt

**Explicación:** Se desglosan los cuatro pilares del prompt engineering: instrucción (core command), contexto (background information), formato de salida (output format) y restricciones (constraints).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which pillar instructs the model on how the answer should be structured (bullet points/JSON)? | `output format` |
| 2 | Which pillar specifies rules or limits imposed on the model's response (tone/forbidden topics)? | `constraints` |
| 3 | Which pillar provides the AI with relevant background information or scenario? | `context` |
| 4 | Which pillar defines the core command or action the AI should perform? | `instruction` |

### Task 4: Prompts de sistema vs. usuario / System vs User Prompts

**Explicación:** Se compara el sistema de prompts de sistema (persistente, definido por el desarrollador) y los prompts de usuario (transitorios), estableciendo la jerarquía de instrucciones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of prompt is developer-defined, persistent, remains constant across all sessions? | `system prompt` |
| 2 | What is the term for the intended order of priority between system and user instructions? | `instruction hierarchy` |

### Task 5: Técnicas avanzadas de prompting / Advanced Prompting Techniques

**Explicación:** Se revisan técnicas avanzadas de prompting: Chain-of-Thought (intermediate reasoning steps), zero-shot (sin ejemplos, conoce el conocimiento pre-entrenado), prompt templates (estructura reutilizable) y la frase triggering zero-shot CoT.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What term for the prompting technique by Google researchers 2022 that breaks tasks into intermediate reasoning steps? | `chain-of-thought` |
| 2 | What prompting technique provides no examples, relying on pre-trained knowledge? | `zero-shot` |
| 3 | What prompting technique saves and reuses a standardised prompt structure for recurring tasks? | `prompt templates` |
| 4 | What simple phrase added to a prompt triggers Zero-shot CoT? | `let's think step by step` |

### Task 6: Desafío / Challenge

**Explicación:** Se aplica todo lo aprendido para completar el desafío práctico del room, formulando un prompt efectivo que revele la flag de validación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{Pr0mpt_3ng1neer}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the term for the smallest units that an LLM breaks text into to process it? | `tokens` |
| 2 | What parameter would you set to 0.0 to make an LLM behave as close to deterministic as possible? | `temperature` |
| 3 | Which pillar instructs the model on how the answer should be structured (bullet points/JSON)? | `output format` |
| 4 | Which pillar specifies rules or limits imposed on the model's response (tone/forbidden topics)? | `constraints` |
| 5 | Which pillar provides the AI with relevant background information or scenario? | `context` |
| 6 | Which pillar defines the core command or action the AI should perform? | `instruction` |
| 7 | What type of prompt is developer-defined, persistent, remains constant across all sessions? | `system prompt` |
| 8 | What is the term for the intended order of priority between system and user instructions? | `instruction hierarchy` |
| 9 | What term for the prompting technique by Google researchers 2022 that breaks tasks into intermediate reasoning steps? | `chain-of-thought` |
| 10 | What prompting technique provides no examples, relying on pre-trained knowledge? | `zero-shot` |
| 11 | What prompting technique saves and reuses a standardised prompt structure for recurring tasks? | `prompt templates` |
| 12 | What simple phrase added to a prompt triggers Zero-shot CoT? | `let's think step by step` |
| 13 | What's the flag? | `THM{Pr0mpt_3ng1neer}` |

---

**Metodología:** Aprender cómo tokeniza y genera el LLM (control de determinismo vía temperatura), dominar los cuatro pilares del prompt engineering, entender la jerarquía system > user, y aplicar técnicas avanzadas (CoT, zero-shot, templates) para completar el desafío de prompt engineering.

### Cadena de ataque / Attack Chain

```text
Entender tokenización → controlar temperatura (determinismo) → diseñar prompt (instrucción + contexto + formato + restricciones) → diferenciar system vs user prompts → aplicar Chain-of-Thought → completar desafío → obtener flag
```

**Learning chain:** Fundamentos de LLM → Anatomía del prompt → System vs User prompts → Técnicas avanzadas (CoT) → Desafío práctico

**Lección:** *El prompt engineering efectivo requiere controlar el nondeterminismo de los LLMs, estructurar prompts con los cuatro pilares (instrucción, contexto, formato, restricciones), y aplicar técnicas avanzadas como Chain-of-Thought para tareas que exigen razonamiento.*

**MITRE ATT&CK:** N/A (Room teórico-práctico de prompt engineering)

**Fuente:** [TryHackMe - Prompt Engineering](https://tryhackme.com/room/promptengineeringaisec)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
