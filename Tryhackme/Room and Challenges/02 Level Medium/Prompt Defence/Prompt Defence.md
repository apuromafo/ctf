# Prompt Defence [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Teoría + Laboratorio / Theory + Lab
* **Slug:** `promptdefence`
* **Link:** https://tryhackme.com/room/promptdefence
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-3-Prompt-Security\03-prompt-defence\README.md` + [vanshsaini48/thm-ai-security](https://github.com/vanshsaini48/thm-ai-security) — `prompt-defense\Readme.md`

---

## Solucionario de Tareas / Task Solutions

### Tarea 2 / Task 2: Probabilistic Security (Seguridad probabilística)

**Pregunta / Question:** What term describes the security philosophy of stacking multiple controls so that breaking one still leaves an attacker facing others?

**Respuesta / Answer:**

```
Defence-in-depth
```

---

### Tarea 3 / Task 3: System Prompt Hardening / Defensive Prompt Engineering

**Pregunta / Question:** What role field value should developer instructions always be placed under in structured prompt templates?

**Respuesta / Answer:**

```
system
```

**Pregunta / Question:** What should never be stored inside a system prompt?

**Respuesta / Answer:**

```
sensitive data
```

**Pregunta / Question:** What is the term for limiting a model strictly to its intended purpose in a system prompt?

**Respuesta / Answer:**

```
tight scoping
```

**Pregunta / Question:** Which system prompt hardening pattern directly addresses roleplay and persona-based bypass attempts?

**Respuesta / Answer:**

```
persona restriction
```

**Pregunta / Question:** What prompt engineering principle involves explicitly telling the LLM to treat all user content as data, not instructions?

**Respuesta / Answer:**

```
Instruction/Data Plane Separation Directive
```

**Pregunta / Question:** What is a "canary token" in the context of system prompt hardening?

**Respuesta / Answer:**

```
A secret phrase embedded in the system prompt that triggers an alert if it appears in model output, indicating system prompt extraction
```

**Pregunta / Question:** True or False: A well-crafted system prompt can completely prevent adversarial suffix attacks.

**Respuesta / Answer:**

```
False
```

---

### Tarea 4 / Task 4: Guardrails (Implementing Guardrails Lab)

**Pregunta / Question:** What type of guardrail uses string matching and regex patterns to reject requests based on known attack phrases?

**Respuesta / Answer:**

```
blocklist
```

**Pregunta / Question:** What type of guardrail runs before the model receives the user's prompt?

**Respuesta / Answer:**

```
input guardrail
```

**Pregunta / Question:** What BERT-based classifier developed by Meta is used as an AI-powered input guardrail?

**Respuesta / Answer:**

```
Llama Prompt Guard 2
```

**Pregunta / Question:** What file extension does NeMo Guardrails use for its declarative conversation flow definitions?

**Respuesta / Answer:**

```
.co (Colang format)
```

**Pregunta / Question:** In the guardrails pipeline, at which stage should input classification occur relative to the main LLM call?

**Respuesta / Answer:**

```
Before — the guardrail classifier runs before the prompt reaches the main LLM
```

**Pregunta / Question:** What category of guardrail validates that the LLM output doesn't contain sensitive data like PII or system prompt content?

**Respuesta / Answer:**

```
Output Guardrail / Response Classifier
```

---

### Tarea 5 / Task 5: Securing Deployment (Asegurar el despliegue)

**Pregunta / Question:** What foundational security principle states that every component should have only the permissions it needs to perform its job?

**Respuesta / Answer:**

```
Principle of Least Privilege
```

**Pregunta / Question:** What is the OWASP identifier for the vulnerability caused by unsanitised LLM output being passed to downstream systems?

**Respuesta / Answer:**

```
LLM05:2025
```

**Pregunta / Question:** What classic web vulnerability can result from LLM-generated JavaScript being rendered in a browser without sanitisation?

**Respuesta / Answer:**

```
XSS
```

**Pregunta / Question:** What metric can be used to detect semantic drift in an LLM conversation — indicating the topic has shifted from expected customer service queries to potential attack payloads?

**Respuesta / Answer:**

```
Cosine similarity against expected topic embeddings
```

**Pregunta / Question:** What log metric would spike dramatically during a many-shot jailbreaking attack?

**Respuesta / Answer:**

```
Input token length / prompt length
```

**Pregunta / Question:** Besides the LLM's output, what other interaction data should be logged for security monitoring of agentic AI systems?

**Respuesta / Answer:**

```
All tool calls, including function names, parameters, and response data
```

---

### Tarea 6 / Task 6: Bypassing Guardrails (Evasión de guardarraíles)

**Flag del desafío / Challenge flag:**

```
THM{fbu349b3u4b934byr93b}
```

---

> **Flags adicionales / Additional flags (fuente rahul_ai):**
> - **Flag 1 (Guardrails Config):** `THM{gu4rdr41ls_bl0ck1ng_1nj3ct10n}`
> - **Flag 2 (Canary Token Alert):** `THM{c4n4ry_t0k3n_3xp0s3d}`
> - **Flag 3 (Anomaly Detection):** `THM{s3m4nt1c_dr1ft_d3t3ct3d}`

---

*Documentación para propósitos educativos y registro de CTF.*
