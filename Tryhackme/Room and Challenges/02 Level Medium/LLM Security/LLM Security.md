# LLM Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teoría / Theory | llmsecurity | https://tryhackme.com/room/llmsecurity | 02 Level Medium | RAHULKATARA1/TryHackMe-AI-Security-Path (`Section-2-Secure-AI-Systems\02-llm-security\README.md`) + vanshsaini48/thm-ai-security (`llm-security\README.md`) | OWASP LLM Top 10, Prompt Injection, RAG, Plugins, SSRF, Model inversion | Clasificación y mitigación de amenazas en sistemas LLM |

> **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-2-Secure-AI-Systems\02-llm-security\README.md` + [vanshsaini48/thm-ai-security](https://github.com/vanshsaini48/thm-ai-security) — `llm-security\README.md`

---

**Contexto:** La sala **LLM Security** recorre el OWASP Top 10 específico para Modelos de Lenguaje (LLM) y organiza las amenazas en cuatro planos: datos, modelo, sistema y usuario. Cada tarea plantea preguntas teóricas para afianzar categorías como Prompt Injection (LLM01), Overreliance (LLM09), SSRF por plugins, extracción de datos de entrenamiento, envenenamiento de memoria y amplificación de phishing. El cierre exige adoptar un mindset de seguridad que anticipe el abuso de estos sistemas.

## Solucionario

### Task 1 / Tarea 1: The OWASP LLM Top 10 / Introduction & Learning Objectives
**Explicación:**

La tarea introductoria presenta el OWASP Top 10 para LLM y fija las categorías de vulnerabilidad que se tratarán en el resto de la sala.

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

### Task 2 / Tarea 2: Deep Dive: Indirect Prompt Injection / Data-Based Threats
**Explicación:**

Se profundiza en la inyección indirecta de prompts y en las amenazas basadas en datos: cuándo el input malicioso llega a través de datos externos (como un currículum), qué arquitectura separa el plano de datos del de instrucciones, y cómo el modelo puede reproducir o revelar su material de entrenamiento.

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

### Task 3 / Tarea 3: Insecure Plugin Design / Model-Based Threats
**Explicación:**

Se trata el diseño inseguro de plugins (que pueden desencadenar SSRF al recuperar URLs suministradas por el usuario) y las amenazas basadas en el propio modelo, como tratar de reconstruir información sensible codificada en sus representaciones internas.

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

### Task 4 / Tarea 4: System-Based Threats
**Explicación:**

Se analizan las amenazas a nivel de sistema, donde un único componente combina instrucciones, datos recuperados y entrada del usuario; además se práctica un ataque de persuasión al modelo para obtener la flag.

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

### Task 5 / Tarea 5: User-Based Threats
**Explicación:**

Se cubren las amenazas originadas por el usuario/atacante, incluyendo paquetes maliciosos con aspecto legítimo y la amplificación de ataques de ingeniería social existentes como phishing.

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

### Task 6 / Tarea 6: Conclusion — A Secure LLM Mindset
**Explicación:**

Tarea conclusiva sin respuesta: se pide consolidar el panorama de amenazas data/model/system/user y adoptar una mentalidad de seguridad aplicable a cualquier sistema basado en LLM.

No se requiere respuesta; resume las amenazas data/model/system/user y el mindset de seguridad para LLMs.
*No answer required — wraps up the data/model/system/user threat landscape.*

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Which OWASP LLM vulnerability category deals with an attacker manipulating the system prompt? | `LLM01: Prompt Injection` |
| 1.2 | What vulnerability arises when users trust LLM outputs without verification, leading to security flaws? | `LLM09: Overreliance` |
| 2.1 | If an LLM reads a malicious resume and subsequently acts as a malicious agent, what type of attack is this? | `Indirect Prompt Injection` |
| 2.2 | What mitigation strategy involves separating the data plane from the instruction plane in LLM processing? | `Dual LLM Architecture` |
| 2.3 | Which data-based threat involves the model reproducing memorised snippets of its training data? | `Training data extraction` |
| 2.4 | Which attack determines whether a known data sample was part of an LLM's training set? | `Membership inference` |
| 3.1 | What traditional web vulnerability is commonly triggered when an LLM insecurely fetches data from a user-supplied URL? | `SSRF` |
| 3.2 | Should LLM plugins run with administrative privileges to ensure smooth operation? (Yea/Nay) | `Nay` |
| 3.3 | Which model-based threat attempts to reconstruct sensitive information encoded within a model's internal representations? | `Model inversion` |
| 4.1 | Which system component combines system instructions, retrieved data, and user input into a single sequence? | `Context window` |
| 4.2 | Did you convince the model? What's the flag? | `THM{MEMORY_POISONED}` |
| 5.1 | Which package should you NOT download? | `robbco-llm-audit` |
| 5.2 | LLM-powered social engineering primarily amplifies which existing attack category? | `Phishing` |
| 6 | Conclusión — resume las amenazas data/model/system/user y el mindset de seguridad | `No answer needed` |

---

**Metodología:** Estudio teórico del OWASP LLM Top 10 con clasificación de amenazas por planos (data/model/system/user), análisis de ataques conocidos (indirect prompt injection, SSRF, training data extraction, membership inference, model inversion, memory poisoning) y práctica de mitigaciones en cada tarea.

**Learning chain:** OWASP LLM Top 10 → indirect prompt injection y data-based threats → insecure plugin design y model-based threats → system-based threats → user-based threats → mindset de seguridad LLM.

**Lección:** *Un LLM no es una caja aislada: cada plano (datos, modelo, sistema y usuario) amplía la superficie de ataque que debe protegerse.*

**MITRE ATT&CK:** T1656 Impersonation · T1566 Phishing (amplificación LLM) · T1195 Supply Chain Compromise (paquete `robbco-llm-audit`) · T1213 Data from Information Repositories (extracción de datos de entrenamiento).

**Fuente:** [TryHackMe - LLM Security](https://tryhackme.com/room/llmsecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.