# XSS - Merry XSSMas

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `xss-aoc2025-c5j8b1m4t6` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/xss-aoc2025-c5j8b1m4t6) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | XSS, reflected XSS, stored XSS |
| **Impacto** | Web Exploitation — fundamentos de XSS, diferencias entre reflected y stored |

---

**Contexto:** En el Día 11 del Advent of Cyber 2025, aprendemos los fundamentos de Cross-Site Scripting (XSS). Debemos identificar y explotar ambos tipos de XSS — reflected y stored — para obtener las flags correspondientes y entender la diferencia clave entre un payload persistido en el backend vs uno reflejado en el response.

## Solucionario

### Task 1: What is XSS?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which type of XSS attack requires payloads to be persisted on the backend? | `Stored` |

### Task 2: Reflected XSS

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the reflected XSS flag? | `THM{Evil_Bunny}` |

### Task 3: Stored XSS

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the stored XSS flag? | `THM{Evil_Stored_Egg}` |

---

**Metodología:** Se inyectaron payloads XSS en parámetros de entrada para identificar reflected XSS (el payload se refleja en el response HTTP sin persistir) y stored XSS (el payload se almacena en la base de datos y se ejecuta al ser renderizado por otros usuarios).
**Learning chain:** Input sanitization failure → reflected XSS (URL parameter injection) → stored XSS (persistent payload in backend) → JavaScript execution in browser context
**MITRE ATT&CK:** T1189 - Drive-by Compromise
**Fuente:** [TryHackMe - XSS - Merry XSSMas](https://tryhackme.com/r/room/xss-aoc2025-c5j8b1m4t6)
