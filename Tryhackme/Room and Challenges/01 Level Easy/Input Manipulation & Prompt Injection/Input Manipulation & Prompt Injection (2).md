# Input Manipulation & Prompt Injection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `inputmanipulationpromptinjection2` | [TryHackMe](https://tryhackme.com/room/inputmanipulationpromptinjection2) | 01 Level Easy | THM | Prompt injection, input manipulation, leakage, obfuscation, direct/indirect injection | Comprensión y práctica de la inyección de instrucciones y de la manipulación de entradas en LLM |

> **Objeto:** Aprender cómo un atacante manipula la entrada de un modelo de lenguaje (prompt injection): exfiltración de contexto (leakage), ofuscación y las variantes directa e indirecta de inyección.

---

**Contexto:** Sala de TryHackMe centrada en la manipulación de entradas y la inyección de prompts en modelos de lenguaje. Introduce el concepto de prompt injection, la posibilidad de provocar una fuga de contexto (leakage) y de ofuscar el prompt para evadir filtros, y distingue los dos tipos principales de inyección: directa e indirecta. Incluye una parte práctica donde se obtienen banderas mediante inyección de prompt.

> **ES:** Una sala guiada para entender la inyección de prompts en LLM: qué es el leakage de contexto, cómo ofuscar el payload, la diferencia entre inyección directa e indirecta y un ejercicio práctico con banderas.
> **EN:** A guided room to understand prompt injection in LLMs: what context leakage is, how to obfuscate the payload, the difference between direct and indirect injection, and a hands-on exercise with flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Punto de partida de la sala sobre manipulación de entradas y prompt injection.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Hay algo que responder en este apartado? / Is there anything to answer here? | `No answer needed` |

### Task 2: Manipulación de entrada / Input Manipulation

**Explicación:** Se estudia cómo la entrada puede manipular el comportamiento del modelo: provocar una fuga del contexto (leakage), ofuscar la instrucción para evitar filtros y clasificar la inyección como directa o indirecta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | ¿Qué técnica permite filtrar el contexto interno? / Which technique leaks the internal context? | `Leakage` |
| 3 | ¿Qué técnica oculta la intención del payload? / Which technique hides the payload's intent? | `Obfuscation` |
| 4.1 | Primer tipo de inyección / First injection type | `Indirect` |
| 4.2 | Segundo tipo de inyección / Second injection type | `Direct` |

### Task 3: Práctica - Inyección de prompts / Practice - Prompt Injection

**Explicación:** Ejercicio práctico donde se inyectan prompts maliciosos contra el modelo para exfiltrar contexto y superar los filtros del sistema, recuperando dos banderas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5.1 | Obtenga la primera bandera (prompt injection) / Get the first flag | `THM{pi_33f7a14a468eba7d3bc2d81a4445134c}` |
| 5.2 | Obtenga la segunda bandera (split payload) / Get the second flag | `THM{spl_52f96576b8389be35f9a87d7262cf96f}` |

### Task 4: Conclusión / Conclusion

**Explicación:** Cierre de la sala consolidando los conceptos de manipulación de entrada e inyección de prompts.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | ¿Hay algo que responder al final? / Is there anything to answer at the end? | `No answer needed` |

---

**Metodología:** Se revisaron los conceptos de manipulación de entrada: leakage (extracción del contexto del sistema), ofuscación del payload y la clasificación directa/indirecta. En la práctica se inyectaron prompts contra el modelo para filtrar información y evadir los filtros, obteniendo `THM{pi_33f7a14a468eba7d3bc2d81a4445134c}` y `THM{spl_52f96576b8389be35f9a87d7262cf96f}`.

### Cadena de ataque / Attack Chain

Análisis del prompt del sistema → detección de entrada manipulable → inyección de instrucciones (directa/indirecta) → leakage del contexto → ofuscación del payload → evasión de filtros → obtención de banderas.

**Learning chain:** Prompt injection → input manipulation → leakage → obfuscation → inyección directa vs indirecta → práctica de exfiltración → banderas.

**Lección:** *Los LLM procesan la entrada del usuario dentro del mismo contexto que el sistema: sin un límite claro de confianza, una instrucción inyectada puede exfiltrar contexto, ofuscarse y clasificarse como directa o indirecta, por lo que el prompt del sistema debe blindarse y las salidas validarse.*

**MITRE ATT&CK:** T1213 (Data from Information Repositories), T1555 (Credentials from Password Stores), T1565 (Data Manipulation), T1190 (Exploit Public-Facing Application).

**Fuente:** [TryHackMe - Input Manipulation & Prompt Injection](https://tryhackme.com/room/inputmanipulationpromptinjection2)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.