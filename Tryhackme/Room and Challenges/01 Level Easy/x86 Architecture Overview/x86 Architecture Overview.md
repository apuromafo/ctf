# x86 Architecture Overview

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `x8664arch` | [TryHackMe](https://tryhackme.com/room/x8664arch) | 01 Level Easy | TryHackMe | x86 / registers / ALU / instruction pointer / flags / segments / stack | IntroSoc 1 dashboard, arquitectura x86: registros, ALU, pipelines, flags, segmentos de memoria y stack |

---

**Contexto:** Sala que ofrece una visión general de la arquitectura x86: la memoria, los registros generales (RAX-RDX, RSI-R15), la unidad aritmético-lógica (ALU), las instrucciones de carga/almacenamiento, el pipeline de ejecución, el puntero de instrucciones, el registro de flags (TF, SF), los segmentos de memoria (CS, DS, SS) y el stack con sus instrucciones de empuje y extracción.

> **ES:** La sala comenta los componentes de la CPU x86: memoria, registros, ALU, pipeline, instruction pointer, flags (trap, sign), segmentos (code, data, stack) y el funcionamiento del stack.
> **EN:** This room reviews the x86 CPU components: memory, registers, ALU, pipeline, instruction pointer, flags (trap, sign), segments (code, data, stack) and how the stack works.

## Solucionario

### Task 1: Intro / Intro
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¡Empecemos! | `No answer needed` |

### Task 2: Anatomy of a CPU / Anatomía de una CPU
**Explicación:** Se presentan los componentes clave de la CPU: la `Memory`, los `Registers` y la `Arithmetic Logic Unit`. Contenido original de la sala (verbatim): `Memory`, `Registers`, `Arithmetic Logic Unit`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué componente de la CPU se usa para el acceso a instrucciones y datos? | `Memory` |
| ¿Qué componente de la CPU se usa para el almacenamiento de la CPU? | `Registers` |
| ¿Qué componente de la CPU realiza los cálculos? | `Arithmetic Logic Unit` |

### Task 3: Registers & Instruction Pointer / Registros y puntero de instrucciones
**Explicación:** El `Instruction Pointer` almacena la dirección de la siguiente instrucción, el registro `ECX` es el contador de bucles por defecto y `R8-R15` es el rango de registros de propósito general de 64 bits añadidos en la arquitectura x64. Contenido original de la sala (verbatim): `Instruction Pointer`, `ECX`, `R8-R15`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué registro apunta a la siguiente instrucción a ejecutar? | `Instruction Pointer` |
| ¿Qué registro se usa por defecto como contador de bucles? | `ECX` |
| ¿Qué registros de propósito general se añaden solo en la arquitectura x64? | `R8-R15` |

### Task 4: Flags / Flags
**Explicación:** En el registro de flags: `Trap Flag` es el flag de depuración para la ejecución paso a paso, `Sign Flag` es el indicador que refleja el signo del resultado y `Code Segment` no es uno de los flags básicos de 32 bits. Contenido original de la sala (verbatim): `Trap Flag`, `Sign Flag`, `Code Segment`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué flag se usa para la depuración paso a paso? | `Trap Flag` |
| ¿Qué flag indica el signo del resultado? | `Sign Flag` |
| ¿Cuál de los siguientes NO es un flag básico de 32 bits? | `Code Segment` |

### Task 5: Memory, Segmentation, and the Stack / Memoria, segmentación y el stack
**Explicación:** El flag `N` no forma parte de los flags básicos de 32 bits, la segmentación divide la memoria en segmentos como `Code`, y el stack es una sección de la memoria con LIFO que almacena datos temporalmente. Contenido original de la sala (verbatim): `N`, `Code`, `Stack`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál de los siguientes es un flag que se añadió en arquitecturas más recientes? | `N` |
| La segmentación divide la memoria en secciones. ¿Cómo se llama la sección que contiene las instrucciones a ejecutar? | `Code` |
| ¿Cómo se llama la sección de memoria que almacena los datos temporalmente y es LIFO? | `Stack` |

### Task 6: The Stack / El stack
**Explicación:** Tras terminar de leer el capítulo, se localiza la flag en el texto: `THM{SMASHED_THE_STACK}`. Contenido original de la sala (verbatim): `THM{SMASHED_THE_STACK}`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Encuentra la flag tras terminar de leer | `THM{SMASHED_THE_STACK}` |

### Task 7: Conclusión / Conclusion
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para continuar? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Empecemos! | `No answer needed` |
| 2 | Componente para acceso a instrucciones y datos | `Memory` |
| 3 | Componente de almacenamiento de la CPU | `Registers` |
| 4 | Componente que realiza los cálculos | `Arithmetic Logic Unit` |
| 5 | Registro que apunta a la siguiente instrucción | `Instruction Pointer` |
| 6 | Contador de bucles por defecto | `ECX` |
| 7 | Registros de propósito general añadidos en x64 | `R8-R15` |
| 8 | Flag de depuración paso a paso | `Trap Flag` |
| 9 | Flag de signo del resultado | `Sign Flag` |
| 10 | Flag que NO es básico de 32 bits | `Code Segment` |
| 11 | Flag añadido en arquitecturas más recientes | `N` |
| 12 | Sección de memoria con las instrucciones | `Code` |
| 13 | Sección de memoria LIFO temporal | `Stack` |
| 14 | Flag encontrada al terminar de leer | `THM{SMASHED_THE_STACK}` |
| 15 | ¿Preparado para continuar? | `No answer needed` |

---

**Metodología:** Se lee el capítulo de la sala y se describe la arquitectura x86: componentes de la CPU (memoria, registros, ALU), registros y puntero de instrucciones, el registro de flags y sus usos, los segmentos de memoria y el funcionamiento del stack (push/pop, LIFO).

### Cadena de ataque / Attack Chain

```text
Anatomy of a CPU (Memory, Registers, ALU) -> Instruction Pointer -> ECX loop counter -> R8-R15 (x64) -> Flags (Trap Flag, Sign Flag, Code Segment) -> Segmentation (N, Code, Stack) -> THM{SMASHED_THE_STACK}
```

**Learning chain:** x86 CPU anatomy --> registers --> instruction pointer --> flags --> segmentation --> stack (LIFO) --> SMASHED_THE_STACK flag

**Lección:** *Comprender la arquitectura x86 (memoria, registros, ALU, flags, segmentos y stack) es la base para la explotación de binarios y el análisis de malware.*

**MITRE ATT&CK:** T1204.002 (User Execution: Malicious File)

**Fuente:** [TryHackMe - x86 Architecture Overview](https://tryhackme.com/room/x8664arch)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.