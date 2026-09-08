# Input Manipulation & Prompt Injection

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `inputmanipulationpromptinjection` |
| **Link** | [TryHackMe](https://tryhackme.com/room/inputmanipulationpromptinjection) |
| **Sección** | 01 Level Easy |
| **Creadores** | [tryhackme] & [l000g1c] |
| **Componentes** | LLM / System Prompt / User Prompt / Leakage / Jailbreaking / Prompt Injection (directa e indirecta) / Obfuscation / flags de desafío |
| **Impacto** | Comprender las bases de los ataques de inyección de prompts en LLMs: filtración del prompt del sistema, jailbreaking e inyección directa/indirecta, con un desafío práctico de flags. |

---

**Contexto:** La **manipulación de entrada** es el "momento SQL Injection" para los LLM: ocurre cuando un atacante diseña entradas para anular o confundir las salvaguardas del modelo, forzándolo a ignorar restricciones. Dos conceptos base: **System Prompt** (instrucciones ocultas que definen el rol y límites del modelo) y **User Prompt** (lo que el usuario escribe).

## Solucionario

### Task 1: Introducción

**Explicación:** Introducción a los peligros de confiar ciegamente en los modelos integrados en flujos de trabajo (HR, IT, etc.).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - introduction. | `No answer needed` |

### Task 2: Filtración de Prompt del Sistema (System Prompt Leakage)

**Explicación:** El **leakage** es la exposición de las instrucciones internas del sistema. Si un atacante las obtiene, tiene un mapa de las debilidades del modelo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do we call the exposure of hidden system instructions? | `Leakage` |

### Task 3: Jailbreaking

**Explicación:** Uso de técnicas para que el modelo adopte una personalidad que no sigue reglas (ej. DAN, modo abuela). La técnica de evasión por **obfuscation** reemplaza o altera caracteres (ej. `h@ck` en lugar de `hack`) para evadir filtros de palabras clave naive.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What evasive technique replaces or alters characters to bypass naive keyword filters? | `Obfuscation` |

### Task 4: Inyección de Prompt (Prompt Injection)

**Explicación:** Existen dos tipos principales: **Directa** (instrucciones maliciosas puestas directamente en el chat / en el user input) e **Indirecta** (instrucciones ocultas en documentos cargados, páginas web o plugins que el LLM lee).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which injection type smuggles instructions via uploaded documents, web pages, or plugins? | `Indirect` |
| 2 | Which injection type places malicious instructions directly in the user input? | `Direct` |

### Task 5: Desafío (Flags)

**Explicación:** Desafío práctico interactuando con un agente de IA: aplicar inyección de prompt y filtración del system prompt para obtener ambas flags.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Prompt Injection Flag | `THM{pi_33f7a14a468eba7d3bc2d81a4445134c}` |
| 2 | System Prompt Flag | `THM{spl_52f96576b8389be35f9a87d7262cf96f}` |

### Task 6: Conclusión

**Explicación:** Cierre de la sala: resumen de las técnicas de manipulación de entrada y su defensa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - conclusion. | `No answer needed` |

---

**Metodología:**
1. Conceptos: System Prompt vs User Prompt; la manipulación de entrada es el "momento SQLi" para los LLM.
2. System Prompt Leakage → respuesta `Leakage`.
3. Jailbreaking → obfuscation de caracteres para evadir filtros (`h@ck`).
4. Prompt Injection: directa (en el user input) vs indirecta (documentos, web, plugins.
5. Desafío: inyectar al agente y filtrar el system prompt para obtener `THM{pi_...}` y `THM{spl_...}`.
6. Conclusión.

**Respuestas resumen:** 1) No answer needed · 2) Leakage · 3) Obfuscation · 4) 1. Indirect / 2. Direct · 5) 1. `THM{pi_33f7a14a468eba7d3bc2d81a4445134c}` / 2. `THM{spl_52f96576b8389be35f9a87d7262cf96f}` · 6) No answer needed.

**Learning chain:** System Prompt (oculto) vs User Prompt (entrada) → Leakage (exposición del system prompt) → Jailbreaking (personalidad sin reglas + obfuscation) → Prompt Injection directa (input) e indirecta (documentos/web/plugins) → desafío → flags.

**MITRE ATT&CK:** T1059.007 (Command and Scripting Interpreter: JavaScript) en entornos web con LLM, OWASP LLM01 (Prompt Injection) y OWASP LLM02 (Sensitive Information Disclosure) para la filtración del system prompt.

**Fuente:** [TryHackMe - Input Manipulation & Prompt Injection](https://tryhackme.com/room/inputmanipulationpromptinjection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
