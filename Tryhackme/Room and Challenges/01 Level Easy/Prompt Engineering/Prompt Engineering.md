# Prompt Engineering [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Theory + Interactive Lab (PromptSec Agent)
* **Slug:** `promptengineeringaisec`
* **Link:** https://tryhackme.com/room/promptengineeringaisec
* **Sección / Section:** AI Fundamentals (Section 1 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\04-prompt-engineering\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

Una guía práctica para entender cómo los LLMs procesan texto y cómo crear prompts efectivos — tanto para tareas de seguridad legítimas como para testing adversarial. Cubre fundamentos de LLM, los cuatro pilares del prompt engineering, la jerarquía de instrucciones, y técnicas avanzadas incluyendo Chain-of-Thought y Few-shot prompting. Concluye con un desafío calificado en vivo usando el agente AI **PromptSec**.

### Conceptos Clave / Key Concepts

#### Cómo Procesan Texto los LLMs
Los LLMs no leen palabras — leen **tokens** (aproximadamente 3–4 caracteres cada uno). Cada palabra se divide en fragmentos de tokens, se convierte a IDs numéricos, y se procesa como números. El modelo nunca ve lenguaje natural directamente.

Los LLMs son **nondeterministas**: la misma entrada puede producir salidas diferentes entre ejecuciones. Las respuestas son probabilísticas. Esto importa enormemente en contextos de seguridad donde la consistencia y reproducibilidad son críticas.

#### Parámetros Clave
| Parámetro | Qué Controla |
|-----------|-----------------|
| Temperature | Aleatoriedad de la salida. `0.0` = casi determinista (siempre elige el token de mayor probabilidad). Mayor = más creativo/impredecible |
| Top-P | Limita la selección de tokens a una masa de probabilidad acumulativa — controla la diversidad |

#### Los Cuatro Pilares del Prompt Engineering
| Pilar | Propósito |
|--------|---------|
| **Instruction** | La tarea o comando central — qué quieres que haga la AI |
| **Context** | Información de fondo o escenario para que el modelo entienda la situación |
| **Output Format** | Cómo debe estructurarse la respuesta (bullet points, JSON, tabla, etc.) |
| **Constraints** | Reglas, límites o restricciones impuestas a la respuesta (tono, longitud, temas prohibidos) |

> 💡 **Sweet spot:** Proporciona suficiente detalle para eliminar ambigüedad, pero no sobrecargues — demasiada verbosidad causa alucinación y respuestas desenfocadas.

#### La Jerarquía de Instrucciones
Los LLMs procesan toda la entrada como un único flujo de texto, pero hay un orden de prioridad intencionado: **system prompt > user prompt**. Esta jerarquía es central para la seguridad — los ataques de prompt injection intentan sobreescribirla.

El término para este orden de prioridad intencionado: **instruction hierarchy**.

#### Técnicas Avanzadas de Prompting
| Técnica | Descripción | Mejor Para |
|-----------|-------------|----------|
| **Zero-shot** | Sin ejemplos — se basa enteramente en conocimiento pre-entrenado | Tareas simples y bien definidas |
| **One-shot** | Un ejemplo de entrada/salida antes de la tarea | Demostración básica de patrones |
| **Few-shot** | 2–5 ejemplos variados antes de la tarea | Tareas de clasificación matizadas |
| **Chain-of-Thought (CoT)** | Pide al modelo razonar paso a paso antes de responder | Análisis complejo de múltiples pasos |
| **Zero-shot CoT** | Solo añade "Let's think step by step" | Mejora rápida de razonamiento, sin ejemplos |
| **Prompt Templates** | Estructuras de prompt estandarizadas y reutilizables con placeholders | Tareas de seguridad recurrentes |

> ⚠️ **Caveat de CoT:** Solo funciona de forma fiable con modelos por encima de ~100B parámetros. Los modelos más pequeños pueden generar cadenas de razonamiento que parecen coherentes pero llevan a respuestas equivocadas.

#### Estructura de Plantilla de Prompt
```
Task: [Define the task]
Context: [Provide relevant background]
Output: [Specify format — JSON, bullet points, table, etc.]
Constraints: [Set rules or restrictions]
```

#### Aplicación de Seguridad — CoT para Análisis de Logs
```
You are a SOC analyst. Analyze the following HTTP logs for SQL injection attempts.
Think through each step:
Step 1: Filter the logs — isolate only entries with a 200 OK status code.
Step 2: For each 200 OK entry, scan request parameters for suspicious patterns
        such as ' OR 1=1, UNION SELECT, --, or encoded variants like %27.
Step 3: For each suspicious entry, explain why the pattern indicates SQL injection.
Step 4: Summarise findings in a table with columns: Timestamp | URI | Pattern Found | Risk Level
```

### Tarea 1 — Introducción / Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I understand the learning objectives and am ready to learn about prompt engineering! | `No answer needed` |

### Tarea 2 — Fundamentos de LLM / LLM Fundamentals

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the term for the smallest units that an LLM breaks text into in order to process it? | `tokens` |
| What parameter would you set to 0.0 to make an LLM behave as close to deterministic as possible? | `temperature` |
| What parameter restricts which tokens the model considers by limiting selection to a cumulative probability mass? | `top-p` |

### Tarea 3 — Estructura de Prompt / Prompt Structure

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which pillar instructs the model on how the answer should be structured, such as bullet points or a JSON object? | `output format` |
| Which pillar specifies rules or limits imposed on the model's response, such as enforcing a tone or forbidding certain topics? | `constraints` |
| Which pillar provides the AI with relevant background information or scenario so it understands the situation? | `context` |
| Which pillar of prompt engineering defines the core command or action you want the AI to perform? | `instruction` |
| What is the term for the intended order of priority between system and user instructions in an LLM application? | `instruction hierarchy` |

### Tarea 4 — Técnicas Avanzadas / Advanced Techniques

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the term for the prompting technique introduced by Google researchers in 2022 that asks models to break tasks into intermediate reasoning steps? | `chain-of-thought` |
| What prompting technique involves providing no examples and relying entirely on the model's pre-trained knowledge? | `zero-shot` |
| What prompting technique involves saving and reusing a standardised prompt structure for recurring tasks? | `prompt templates` |

### Tarea 5 — Práctica (Desafío PromptSec) / Practical (PromptSec Challenge)

**Cómo funciona:** PromptSec te da una técnica + tarea de seguridad. Escribes un prompt, te califica de 0 a 10. Alcanza 40 puntos totales para obtener la flag. Puedes pedir pistas pero no escribirá el prompt por ti.

**Tips para puntuaciones máximas:**
- Para tareas **CoT**: lista explícitamente cada paso de razonamiento usando pasos numerados; no digas solo "think step by step"
- Para tareas **Few-shot**: proporciona 2+ ejemplos cubriendo diferentes casos (p. ej. prioridad crítica, alta, media, baja)
- Para tareas **Template**: usa placeholders claros como `[LOG_ENTRY]`, `[STATUS_CODE]`, `[OUTPUT_FORMAT]`
- Siempre especifica el formato de salida explícitamente (JSON, tabla, bullet points)
- Siempre asigna un rol ("You are a SOC analyst...")

> 💡 Puedes superar 40/40 — los prompts perfectos pueden puntuar más alto que el objetivo.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Complete the PromptSec challenge and get the flag | `THM{Pr0mpt_3ng1n33r}` |

**Notas:**
> El valor de la flag puede variar — recupérala del agente PromptSec después de alcanzar 40+ puntos.

---

## 🚩 Flags

| Flag | Valor / Value |
|------|-------|
| Task 5 — PromptSec Challenge | `THM{Pr0mpt_3ng1n33r}` |

---

### Qué Enseña Esta Sala / What This Room Teaches You

- Los prompts no son solo peticiones de lenguaje natural — son instrucciones estructuradas con una jerarquía que puede explotarse.
- La jerarquía de instrucciones (system > user) es exactamente lo que los ataques de prompt injection atacan — entender esto desde el lado de ingeniería hace mucho más claro el lado del ataque.
- El prompting CoT es la palanca individual más grande para mejorar la calidad de salida en tareas de seguridad complejas.
- El nondeterminismo significa que un prompt que funciona hoy puede no funcionar mañana — siempre prueba con temperature=0 cuando necesites consistencia.

---

* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\04-prompt-engineering\README.md`

*Documentación para propósitos educativos y registro de CTF.*
