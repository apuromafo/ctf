# XSS - Merry XSSMas

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `xss-aoc2025-c5j8b1m4t6` | [TryHackMe](https://tryhackme.com/r/room/xss-aoc2025-c5j8b1m4t6) | Advent of Cyber 2025 | TryHackMe | XSS, reflected XSS, stored XSS | Web Exploitation - fundamentos de XSS, diferencias entre reflected y stored |

---

**Contexto:** En el Día 11 del Advent of Cyber 2025, aprendemos los fundamentos de Cross-Site Scripting (XSS). Debemos identificar y explotar ambos tipos de XSS - reflected y stored - para obtener las flags correspondientes y entender la diferencia clave entre un payload persistido en el backend vs uno reflejado en el response.

> **ES:** Sala temática navideña: se practican los fundamentos de XSS, se inyectan payloads en parámetros de entrada para explotar un XSS reflejado (flag Evil_Bunny) y un XSS almacenado (flag Evil_Stored_Egg).
> **EN:** This room covers the XSS basics with a festive twist: input payloads are used to exploit a reflected XSS (Evil_Bunny flag) and a stored XSS (Evil_Stored_Egg flag), understanding the persistence difference.

## Solucionario

### Task 1: ¿Qué es el XSS? / What is XSS?
**Explicación:** Se repasan los fundamentos de Cross-Site Scripting. En este ejercicio se practican ambos tipos de XSS - reflected y stored. Contenido original de la sala (verbatim): `Stored`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Which type of XSS attack requires payloads to be persisted on the backend? | `Stored` |

### Task 2: XSS reflejado / Reflected XSS
**Explicación:** Se inyecta un payload en el parámetro de la URL del formulario de inicio de sesión: el payload se refleja en el response HTTP sin persistir. Se obtiene la flag `THM{Evil_Bunny}`. Contenido original de la sala (verbatim): `THM{Evil_Bunny}`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| What's the reflected XSS flag? | `THM{Evil_Bunny}` |

### Task 3: XSS almacenado / Stored XSS
**Explicación:** Se inyecta un payload persistente en el formulario que se almacena en la base de datos del backend y se ejecuta al renderizarse para otros usuarios. Se obtiene la flag `THM{Evil_Stored_Egg}`. Contenido original de la sala (verbatim): `THM{Evil_Stored_Egg}`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| What's the stored XSS flag? | `THM{Evil_Stored_Egg}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which type of XSS attack requires payloads to be persisted on the backend? | `Stored` |
| 2 | What's the reflected XSS flag? | `THM{Evil_Bunny}` |
| 3 | What's the stored XSS flag? | `THM{Evil_Stored_Egg}` |

---

**Metodología:** Se inyectaron payloads XSS en parámetros de entrada para identificar reflected XSS (el payload se refleja en el response HTTP sin persistir) y stored XSS (el payload se almacena en la base de datos y se ejecuta al ser renderizado por otros usuarios).
**Learning chain:** Input sanitization failure  →  reflected XSS (URL parameter injection)  →  stored XSS (persistent payload in backend)  →  JavaScript execution in browser context
**Lección:** *La diferencia clave entre reflected y stored XSS está en la persistencia: un payload almacenado en el backend se ejecuta para todos los usuarios, lo que lo hace más peligroso que una inyección que solo se refleja en la respuesta.*
**MITRE ATT&CK:** T1189 - Drive-by Compromise
**Fuente:** [TryHackMe - XSS - Merry XSSMas](https://tryhackme.com/r/room/xss-aoc2025-c5j8b1m4t6)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.