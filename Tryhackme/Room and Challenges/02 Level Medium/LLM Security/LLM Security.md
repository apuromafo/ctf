# LLM Security [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Teoría / Theory
* **Slug:** `llmsecurity`
* **Link:** https://tryhackme.com/room/llmsecurity
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-2-Secure-AI-Systems\02-llm-security\README.md` + [vanshsaini48/thm-ai-security](https://github.com/vanshsaini48/thm-ai-security) — `llm-security\README.md`

---

## Solucionario de Tareas / Task Solutions

### Tarea 1 / Task 1: The OWASP LLM Top 10 / Introduction & Learning Objectives

**Pregunta / Question:** Which OWASP LLM vulnerability category deals with an attacker manipulating the system prompt?

**Respuesta / Answer:**

```
LLM01: Prompt Injection
```

**Pregunta / Question:** What vulnerability arises when users trust LLM outputs without verification, leading to security flaws?

**Respuesta / Answer:**

```
LLM09: Overreliance
```

---

### Tarea 2 / Task 2: Deep Dive: Indirect Prompt Injection / Data-Based Threats

**Pregunta / Question:** If an LLM reads a malicious resume and subsequently acts as a malicious agent, what type of attack is this?

**Respuesta / Answer:**

```
Indirect Prompt Injection
```

**Pregunta / Question:** What mitigation strategy involves separating the data plane from the instruction plane in LLM processing?

**Respuesta / Answer:**

```
Dual LLM Architecture
```

**Pregunta / Question:** Which data-based threat involves the model reproducing memorised snippets of its training data?

**Respuesta / Answer:**

```
Training data extraction
```

**Pregunta / Question:** Which attack determines whether a known data sample was part of an LLM's training set?

**Respuesta / Answer:**

```
Membership inference
```

---

### Tarea 3 / Task 3: Insecure Plugin Design / Model-Based Threats

**Pregunta / Question:** What traditional web vulnerability is commonly triggered when an LLM insecurely fetches data from a user-supplied URL?

**Respuesta / Answer:**

```
SSRF
```

**Pregunta / Question:** Should LLM plugins run with administrative privileges to ensure smooth operation? (Yea/Nay)

**Respuesta / Answer:**

```
Nay
```

**Pregunta / Question:** Which model-based threat attempts to reconstruct sensitive information encoded within a model's internal representations?

**Respuesta / Answer:**

```
Model inversion
```

---

### Tarea 4 / Task 4: System-Based Threats

**Pregunta / Question:** Which system component combines system instructions, retrieved data, and user input into a single sequence?

**Respuesta / Answer:**

```
Context window
```

**Pregunta / Question:** Did you convince the model? What's the flag?

**Respuesta / Answer:**

```
THM{MEMORY_POISONED}
```

---

### Tarea 5 / Task 5: User-Based Threats

**Pregunta / Question:** Which package should you NOT download?

**Respuesta / Answer:**

```
robbco-llm-audit
```

**Pregunta / Question:** LLM-powered social engineering primarily amplifies which existing attack category?

**Respuesta / Answer:**

```
Phishing
```

---

### Tarea 6 / Task 6: Conclusion — A Secure LLM Mindset

No se requiere respuesta; resume las amenazas data/model/system/user y el mindset de seguridad para LLMs.
*No answer required — wraps up the data/model/system/user threat landscape.*

---

*Documentación para propósitos educativos y registro de CTF.*
