# Prompt Defence

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teoría + Laboratorio / Theory + Lab | promptdefence | https://tryhackme.com/room/promptdefence | 02 Level Medium | [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-3-Prompt-Security\03-prompt-defence\README.md` + [vanshsaini48/thm-ai-security](https://github.com/vanshsaini48/thm-ai-security) — `prompt-defense\Readme.md` | System Prompt Hardening, Guardrails, NeMo Guardrails, Despliegue seguro | Mitigación de inyección de prompts, extracción de prompts y abuso de agentes LLM |

---

**Contexto:** La sala **Prompt Defence** (ruta de AI Security de TryHackMe) enseña a defender aplicaciones LLM: seguridad probabilística, endurecimiento del system prompt, implementación de guardarraíles (blocklist, clasificadores como Llama Prompt Guard 2 y flujos Colang de NeMo Guardrails) y aseguramiento del despliegue (mínimo privilegio, logs, monitoreo de deriva semántica). Finaliza con un laboratorio de evasión de guardarraíles cuya flag acredita el reto.

## Solucionario

### Task 2: Seguridad probabilística / Probabilistic Security
**Explicación:**

La seguridad probabilística asume que ningún control es infalible y apuesta por apilar capas de defensa de modo que romper una no deje al atacante sin barreras frente a las demás.

**Pregunta / Question:** What term describes the security philosophy of stacking multiple controls so that breaking one still leaves an attacker facing others?

**Respuesta / Answer:**

```
Defence-in-depth
```

### Task 3: System Prompt Hardening / Defensive Prompt Engineering
**Explicación:**

Endurecer el **system prompt** incluye separar instrucciones de datos, restringir el rol y el ámbito del modelo (tight scoping), prohibir la suplantación de roles, vincular las instrucciones del desarrollador al campo `system` del template, mantener fuera los datos sensibles y desplegar canarios para detectar extracciones del prompt.

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

### Task 4: Guardrails (Implementing Guardrails Lab)
**Explicación:**

Los **guardarraíles** filtran entradas y salidas del modelo: listas de bloqueo por regex, guardrail de entrada antes de que el prompt llegue al LLM, clasificadores basados en BERT como Llama Prompt Guard 2, flujos declarativos en Colang (`.co`) para NeMo Guardrails, y clasificadores de respuesta que impiden fugas de PII o del system prompt.

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

### Task 5: Asegurar el despliegue / Securing Deployment
**Explicación:**

Asegurar el despliegue implica aplicar el **Principio de Mínimo Privilegio**, sanear la salida del LLM antes de pasarla a sistemas aguas abajo (evitando la vulnerabilidad LLM05:2025 y el XSS en el navegador), monitorizar la deriva semántica mediante similitud coseno contra los embeddings esperados, y registrar todas las llamadas a herramientas además de la salida del modelo (los ataques many-shot disparan la longitud del prompt).

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

### Task 6: Evasión de guardarraíles / Bypassing Guardrails
**Explicación:**

El laboratorio final pone a prueba las defensas anteriores intentando evadir los guardarraíles; al sortearlos se obtiene la flag del desafío que confirma el bypass y se recopilan las flags adicionales documentadas en la fuente rahul_ai (config de guardrails, alerta de canary y detección de anomalías).

**Flag del desafío / Challenge flag:**

```
THM{fbu349b3u4b934byr93b}
```

> **Flags adicionales / Additional flags (fuente rahul_ai):**
> - **Flag 1 (Guardrails Config):** `THM{gu4rdr41ls_bl0ck1ng_1nj3ct10n}`
> - **Flag 2 (Canary Token Alert):** `THM{c4n4ry_t0k3n_3xp0s3d}`
> - **Flag 3 (Anomaly Detection):** `THM{s3m4nt1c_dr1ft_d3t3ct3d}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Term for stacking multiple security controls | `Defence-in-depth` |
| 2 | Field where developer instructions must go | `system` |
| 3 | What must never be stored in a system prompt | `sensitive data` |
| 4 | Term for limiting the model to its intended purpose | `tight scoping` |
| 5 | Pattern against roleplay/persona bypass | `persona restriction` |
| 6 | Principle treating user content as data, not instructions | `Instruction/Data Plane Separation Directive` |
| 7 | What is a canary token | `A secret phrase embedded in the system prompt that triggers an alert if it appears in model output, indicating system prompt extraction` |
| 8 | Can a system prompt prevent adversarial suffix attacks? | `False` |
| 9 | Guardrail using string matching and regex | `blocklist` |
| 10 | Guardrail that runs before the model receives the prompt | `input guardrail` |
| 11 | Meta BERT-based input guardrail classifier | `Llama Prompt Guard 2` |
| 12 | NeMo Guardrails declarative flow file extension | `.co (Colang format)` |
| 13 | Stage for input classification | `Before — the guardrail classifier runs before the prompt reaches the main LLM` |
| 14 | Guardrail validating output for PII/system prompt | `Output Guardrail / Response Classifier` |
| 15 | Principle of minimal permissions per component | `Principle of Least Privilege` |
| 16 | OWASP id for unsanitised LLM output | `LLM05:2025` |
| 17 | Web vuln from LLM-generated JS without sanitisation | `XSS` |
| 18 | Metric to detect semantic drift | `Cosine similarity against expected topic embeddings` |
| 19 | Log metric that spikes in many-shot jailbreaking | `Input token length / prompt length` |
| 20 | Other interaction data to log in agentic AI | `All tool calls, including function names, parameters, and response data` |
| 21 | Flag del desafío / Challenge flag | `THM{fbu349b3u4b934byr93b}` |
| 22 | Flag adicional 1 (Guardrails Config) | `THM{gu4rdr41ls_bl0ck1ng_1nj3ct10n}` |
| 23 | Flag adicional 2 (Canary Token Alert) | `THM{c4n4ry_t0k3n_3xp0s3d}` |
| 24 | Flag adicional 3 (Anomaly Detection) | `THM{s3m4nt1c_dr1ft_d3t3ct3d}` |

---

**Metodología:** Defensa en profundidad del sistema de IA: separar datos e instrucciones, endurecer el system prompt, desplegar guardarraíles de entrada/salida (blocklist + clasificadores IA + Colang), asegurar el despliegue y monitorizar la deriva semántica y las llamadas a herramientas.

### Cadena de ataque / Attack Chain

```
Prompt malicioso / adversarial suffix
        │
        ▼
Guardrail de entrada (blocklist + Llama Prompt Guard 2)
        │
        ▼
System prompt endurecido (scoping, persona restriction, canary)
        │
        ▼
LLM (NeMo Guardrails, flujos Colang .co)
        │
        ▼
Guardrail de salida / Response Classifier
        │
        ▼
Despliegue seguro (least privilege, sanitización, logs)
```

**Learning chain:** Seguridad probabilística → hardening del system prompt → guardrails de entrada/salida → despliegue seguro → evasión y detección.

**Lección:** *Ningún system prompt por sí solo detiene todos los ataques: la defensa real es probabilística y se construye apilando capas de endurecimiento, clasificadores y monitoreo que se validan intentando evadirlas.*

**MITRE ATT&CK:** OWASP Top 10 for LLM: LLM01 Prompt Injection · LLM05 Excessive Agency · LLM06 Overreliance (NIST AI RMF como marco complementario).

**Fuente:** [TryHackMe - Prompt Defence](https://tryhackme.com/room/promptdefence)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.