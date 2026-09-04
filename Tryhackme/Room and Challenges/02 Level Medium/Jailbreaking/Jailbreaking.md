# Jailbreaking [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Teoría + Laboratorio / Theory + Lab
* **Slug:** `jailbreaking`
* **Link:** https://tryhackme.com/room/jailbreaking
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-3-Prompt-Security\02-jailbreaking\README.md` + [vanshsaini48/thm-ai-security](https://github.com/vanshsaini48/thm-ai-security) — `Jailbreaking\Readme.md`

---

## Solucionario de Tareas / Task Solutions

### Tarea 2 / Task 2: Prompt Injection vs Jailbreaking

**Pregunta / Question:** What class of attacks attempts to subvert safety filters built into LLMs themselves?

**Respuesta / Answer:**

```
Jailbreaking
```

**Pregunta / Question:** Unlike prompt injection, which exploits application-level data mixing, what does jailbreaking target directly?

**Respuesta / Answer:**

```
The Model
```

---

### Tarea 3 / Task 3: Why Models Have "Jails" (The Psychology of Safety Alignment)

**Pregunta / Question:** What technique uses human raters to rank outputs and teach models to prefer helpful, harmless responses?

**Respuesta / Answer:**

```
RLHF
```

**Pregunta / Question:** Safety alignment can degrade when fine-tuning models on just 1,000 benign samples, by over __%?

**Respuesta / Answer:**

```
60
```

**Pregunta / Question:** What term describes the performance cost of making models safe?

**Respuesta / Answer:**

```
Alignment tax
```

**Pregunta / Question:** What term describes automatically generated nonsensical suffixes that reliably bypass safety filters via gradient optimization?

**Respuesta / Answer:**

```
Adversarial Suffix (GCG Attack)
```

**Pregunta / Question:** Which jailbreaking technique exploits sparse RLHF training data in non-English languages?

**Respuesta / Answer:**

```
Language Switching / Multilingual Attack
```

---

### Tarea 4 / Task 4: Classic Jailbreaking Techniques (Persona Attacks Lab)

**Pregunta / Question:** Which kinds of languages can models trained primarily on English be beneficial for in jailbreaking attempts?

**Respuesta / Answer:**

```
Low-resource languages
```

**Pregunta / Question:** What jailbreak technique buries harmful requests among multiple benign tasks?

**Respuesta / Answer:**

```
Instruction sandwiching
```

**Pregunta / Question:** Which jailbreaking technique uses emotional manipulation in an attempt to make the model more likely to provide malicious instructions?

**Respuesta / Answer:**

```
The Grandma Exploit
```

**Pregunta / Question:** According to research cited in the content, what success rate do roleplay attacks achieve on commercial systems?

**Respuesta / Answer:**

```
84.3%
```

**Pregunta / Question:** Which technique produced the first full bypass — extracting technically accurate exploit information?

**Respuesta / Answer:**

```
Fiction Layering (novel dialogue scene)
```

**Pregunta / Question:** What is the core psychological principle exploited by "academic framing" jailbreaks?

**Respuesta / Answer:**

```
Models are trained to be helpful to researchers; academic framing creates an exception in intent detection
```

**Pregunta / Question:** What flag was revealed after the successful OAuth2 bypass extraction?

**Respuesta / Answer:**

```
THM{p3rs0n4_j41lbr34k_succ3ss}
```

---

### Tarea 5 / Task 5: Multi-turn Jailbreaking & Conditioning / Token-Level Attacks

**Pregunta / Question:** What term describes the phenomenon where models become less likely to refuse as they engage with a conversation?

**Respuesta / Answer:**

```
Consistency bias
```

**Pregunta / Question:** What multi-turn technique plants harmful concepts gradually without triggering immediate refusal?

**Respuesta / Answer:**

```
Trigger phrases
```

**Pregunta / Question:** What term describes the gradual embedding of harmful ideas across multiple turns, using small incremental steps to avoid detection?

**Respuesta / Answer:**

```
Poisonous seeds
```

**Pregunta / Question:** Why does submitting a harmful request in an obscure language sometimes bypass safety filters?

**Respuesta / Answer:**

```
RLHF training data is heavily skewed toward English; non-English refusal training is sparse
```

**Pregunta / Question:** What Unicode technique inserts invisible characters into flagged words to confuse tokenizer-level content filters?

**Respuesta / Answer:**

```
Zero-width joiner (U+200D) token smuggling
```

**Pregunta / Question:** What is the fundamental weakness in keyword-based safety filters exposed by Base64 attacks?

**Respuesta / Answer:**

```
They operate on surface token patterns, not semantic meaning of decoded content
```

---

### Tarea 6 / Task 6: Case Study — DAN & the AI Security Community

**Pregunta / Question:** What does DAN stand for?

**Respuesta / Answer:**

```
Do Anything Now
```

---

### Tarea 7 / Task 7: Challenge

**Flag del desafío / Challenge flag:**

```
THM{ja1lbre3ker}
```

---

> **Flags adicionales / Additional flags (fuente rahul_ai):**
> - **Flag 2 (Encoding Bypass):** `THM{b4s364_3nc0d1ng_byp4ss}`
> - **Flag 3 (Language Switch):** `THM{mult1l1ngu4l_j41lbr34k}`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
