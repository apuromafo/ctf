# Buffer Overflows

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `bufferoverflows` | [TryHackMe](https://tryhackme.com/room/bufferoverflows) | 01 Level Easy | TryHackMe | x86, registros, memoria (heap/stack), buffer overflow, EIP | Comprensión y explotación básica de desbordamientos de búfer con control del flujo de ejecución |

---

**Contexto:** Sala introductoria a los buffer overflows. Repasa la arquitectura x86, los registros y la organización de la memoria (heap y stack) antes de pasar a la práctica: sobrescribir el puntero de ejecución (EIP) con los valores exactos que controlan el flujo del programa. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Fundamentos / Fundamentals

**Explicación:** Preguntas teóricas sobre tipos de memoria y registros x86: se identifican las zonas de memoria (heap/stack), los registros involucrados y el que almacena el valor de retorno o los operandos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `heap`<br>`stack` |
| 3 | *(Pregunta 3 no especificada en el original)* | `l`<br>`push` |
| 4 | *(Pregunta 4 no especificada en el original)* | `rax` |
| 5 | *(Pregunta 5 no especificada en el original)* | `No answer needed` |

### Task 2: Explotación / Exploitation

**Explicación:** Se practica el desbordamiento de un buffer vulnerable: se determina el offset que sobrescribe el EIP y se envía el input que desplaza la ejecución, confirmando el control del programa mediante los mensajes de éxito.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `15` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |
| 3 | *(Pregunta 3 no especificada en el original)* | `omgyoudidthissocool!!` |
| 4 | *(Pregunta 4 no especificada en el original)* | `wowanothertime!!` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `heap`<br>`stack` |
| 3 | *(Task 1, Pregunta 3 no especificada en el original)* | `l`<br>`push` |
| 4 | *(Task 1, Pregunta 4 no especificada en el original)* | `rax` |
| 5 | *(Task 1, Pregunta 5 no especificada en el original)* | `No answer needed` |
| 6 | *(Task 2, Pregunta 1 no especificada en el original)* | `15` |
| 7 | *(Task 2, Pregunta 2 no especificada en el original)* | `No answer needed` |
| 8 | *(Task 2, Pregunta 3 no especificada en el original)* | `omgyoudidthissocool!!` |
| 9 | *(Task 2, Pregunta 4 no especificada en el original)* | `wowanothertime!!` |

---

**Metodología:** Revisión de arquitectura x86 (registros y memoria) → análisis del programa vulnerable → determinación del offset para sobrescribir el EIP → inyección del input controlado → confirmación del control de ejecución con los mensajes exactos.

### Cadena de ataque / Attack Chain

```text
Fundamentos x86 (registros, heap/stack) → fuzzing del buffer → sobrescritura del EIP (offset 15) → control del flujo → mensajes de éxito (omgyoudidthissocool!! / wowanothertime!!)
```

**Learning chain:** Arquitectura x86 → organización de memoria → buffer overflow → sobrescritura de EIP → control de ejecución

**Lección:** *Entender cómo se organiza la pila y qué registros controlan la ejecución es la base para convertir un simple desbordamiento en un control total del flujo del programa.*

**MITRE ATT&CK:** T1203 (Exploitation for Client Execution), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Buffer Overflows](https://tryhackme.com/room/bufferoverflows)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.