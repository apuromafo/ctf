# Jailbreaking

| **Dificultad** | MEDIUM | **Tipo** | Teoría + Laboratorio / Theory + Lab | **Slug** | `jailbreaking` |
| **Link** | [TryHackMe](https://tryhackme.com/room/jailbreaking) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | LLM Security / Jailbreaking / Prompt Injection / RLHF / GCG Attack / Multilingual Attacks | **Impacto** | Evalúa la comprensión y explotación de bypass de filtros de seguridad en LLMs |

---

**Contexto:** Sala teórico-práctica sobre **jailbreaking** de LLMs: cómo los modelos entrenados con RLHF adquieren "jails" de seguridad y qué técnicas las rompen (persona attacks, instruction sandwiching, adversarial suffixes GCG, language switching, multi-turn conditioning, token-level attacks). Incluye 4 labs con flags de bypass (persona, encoding, language switch) y un challenge final.

## Solucionario

### Task 2: Prompt Injection vs Jailbreaking

**Explicación:** Distinción fundamental: el prompt injection explota la mezcla de datos a nivel de aplicación, mientras que el jailbreaking ataca directamente a los safety filters del propio modelo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What class of attacks attempts to subvert safety filters built into LLMs themselves? | `Jailbreaking` |
| 2 | Unlike prompt injection, which exploits application-level data mixing, what does jailbreaking target directly? | `The Model` |

### Task 3: Why Models Have "Jails" (The Psychology of Safety Alignment)

**Explicación:** El alineamiento de seguridad (RLHF), el "alignment tax" (coste de rendimiento de hacer modelos seguros), y cómo el fine-tuning degrada la seguridad (al menos 60% con solo 1,000 muestras benignas). Técnicas avanzadas: Adversarial Suffix (GCG Attack, sufijos sin sentido autogenerados vía optimización de gradientes) y Language Switching (explotación de datos de entrenamiento RLHF escasos en lenguas no inglesas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What technique uses human raters to rank outputs and teach models to prefer helpful, harmless responses? | `RLHF` |
| 2 | Safety alignment can degrade when fine-tuning models on just 1,000 benign samples, by over __%? | `60` |
| 3 | What term describes the performance cost of making models safe? | `Alignment tax` |
| 4 | What term describes automatically generated nonsensical suffixes that reliably bypass safety filters via gradient optimization? | `Adversarial Suffix (GCG Attack)` |
| 5 | Which jailbreaking technique exploits sparse RLHF training data in non-English languages? | `Language Switching / Multilingual Attack` |

### Task 4: Classic Jailbreaking Techniques (Persona Attacks Lab)

**Explicación:** Técnicas clásicas de jailbreak: lenguaje de bajo recurso, instruction sandwiching (enterrar el request dañino entre tareas benignas), The Grandma Exploit (manipulación emocional), ataques de roleplay (84.3% de éxito en sistemas comerciales), fiction layering (bypass completo extrayendo información de explotación real) y academic framing (excepción en la detección de intención). El lab de persona culmina con el flag de OAuth2 bypass exitoso.

Flags adicionales del lab (fuente rahul_ai): Flag 2 (Encoding Bypass) `THM{b4s364_3nc0d1ng_byp4ss}`, Flag 3 (Language Switch) `THM{mult1l1ngu4l_j41lbr34k}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which kinds of languages can models trained primarily on English be beneficial for in jailbreaking attempts? | `Low-resource languages` |
| 2 | What jailbreak technique buries harmful requests among multiple benign tasks? | `Instruction sandwiching` |
| 3 | Which jailbreaking technique uses emotional manipulation in an attempt to make the model more likely to provide malicious instructions? | `The Grandma Exploit` |
| 4 | According to research cited in the content, what success rate do roleplay attacks achieve on commercial systems? | `84.3%` |
| 5 | Which technique produced the first full bypass — extracting technically accurate exploit information? | `Fiction Layering (novel dialogue scene)` |
| 6 | What is the core psychological principle exploited by "academic framing" jailbreaks? | `Models are trained to be helpful to researchers; academic framing creates an exception in intent detection` |
| 7 | What flag was revealed after the successful OAuth2 bypass extraction? | `THM{p3rs0n4_j41lbr34k_succ3ss}` |

### Task 5: Multi-turn Jailbreaking & Conditioning / Token-Level Attacks

**Explicación:** Técnicas de jailbreak multi-turno (consistency bias, trigger phrases, poisonous seeds) y a nivel de tokens: Unicode (zero-width joiner U+200D token smuggling) y Base64 (los filtros operan sobre patrones superficiales de tokens, no sobre el significado semántico del contenido decodificado). Motivo del lenguaje oscuro: el entrenamiento RLHF está muy sesgado al inglés y el entrenamiento de rechazo en otros idiomas es escaso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What term describes the phenomenon where models become less likely to refuse as they engage with a conversation? | `Consistency bias` |
| 2 | What multi-turn technique plants harmful concepts gradually without triggering immediate refusal? | `Trigger phrases` |
| 3 | What term describes the gradual embedding of harmful ideas across multiple turns, using small incremental steps to avoid detection? | `Poisonous seeds` |
| 4 | Why does submitting a harmful request in an obscure language sometimes bypass safety filters? | `RLHF training data is heavily skewed toward English; non-English refusal training is sparse` |
| 5 | What Unicode technique inserts invisible characters into flagged words to confuse tokenizer-level content filters? | `Zero-width joiner (U+200D) token smuggling` |
| 6 | What is the fundamental weakness in keyword-based safety filters exposed by Base64 attacks? | `They operate on surface token patterns, not semantic meaning of decoded content` |

### Task 6: Case Study — DAN & the AI Security Community

**Explicación:** Caso de estudio del jailbreak más famoso: DAN (Do Anything Now), que inspiró a toda una comunidad de seguridad de IA a explorar y documentar bypasses de filtros.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does DAN stand for? | `Do Anything Now` |

### Task 7: Challenge

**Explicación:** Desafío final de la sala que integra las técnicas vistas (persona, encoding y language switching) para obtener el flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del desafío / Challenge flag | `THM{ja1lbre3ker}` |

---

**Metodología:**
1. Diferenciar prompt injection de jailbreak: el objetivo es el modelo, no la aplicación.
2. Comprender la psicología del alineamiento: RLHF, alignment tax, y la degradación con fine-tuning.
3. Aplicar técnicas clásicas: persona attacks, instruction sandwiching, grandma exploit, roleplay, fiction layering y academic framing.
4. Encadenar turnos y tokens: consistency bias, poisonous seeds, zero-width joiner y encoding (Base64).
5. Ejecutar los labs de bypass (OAuth2 persona, encoding y language switch) y validar los flags.
6. Completar el challenge integrador.

**Learning chain:** Concepto jailbreak vs prompt injection → Alineamiento (RLHF/alignment tax) → Técnicas clásicas (persona/sandwiching/grandma/roleplay/fiction/academic) → Multi-turno (bias/trigger/poisonous seeds) → Token-level (Unicode/Base64) → DAN case study → Labs de bypass (OAuth2/encoding/language) → Challenge flag

**Lección:** *Los filtros de seguridad de un LLM pueden romperse mediante manipulación de rol, contexto o representación: ninguna capa superficial (keywords, regex o tokens) es suficiente si el modelo no distingue datos de instrucciones; la defensa real pasa por arquitectura y monitorización del comportamiento.*

**MITRE ATT&CK:** T1565 - Data Manipulation; T1598 - Phishing for Information; CWE-940 - Improper Verification of Source of a Communication Channel; T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Jailbreaking](https://tryhackme.com/room/jailbreaking)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
