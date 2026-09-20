# Windows x64 Assembly

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | windowsx64assembly | https://tryhackme.com/room/windowsx64assembly | 02 Level Medium | TryHackMe | Assembly x64, Registros, Flags, Pila, Red Team | Fundamentos de programación en ensamblador x64: registros, banderas, pila y convención de llamada en Windows |

---

**Contexto:** La sala **Windows x64 Assembly** enseña los fundamentos del lenguaje ensamblador para la arquitectura x64 de 64 bits. El alumno repasa la representación numérica (decimal y hexadecimal), el tamaño y propósito de los registros de propósito general, las banderas del registro EFLAGS, las instrucciones de control de flujo (ret, call, PUSH), la convención de llamada de Windows x64 y el comportamiento de la pila (LIFO), preparando la base necesaria para el análisis de binarios y el desarrollo de exploits.

## Solucionario

### Task 1: Introducción

**Explicación:**

La sala presenta el objetivo del curso: dominar los conceptos esenciales de la arquitectura x64 y el lenguaje ensamblador en el contexto de Windows.

Respuesta: `No answer needed`

### Task 2: Conversión numérica

**Explicación:**

Se resuelven las conversiones entre sistemas numéricos: la conversión a decimal del valor binario/hexadecimal dado y la conversión opuesta al sistema hexadecimal.

1. `10`
2. `0x19`

### Task 3: Tamaño de los registros

**Explicación:**

Se determinan los tamaños de los registros de propósito general en la arquitectura x64: ámbito de 64 bits y el equivalente en bytes para registros de 128 bits.

1. `2`
2. `16`

### Task 4: Representación binaria

**Explicación:**

Se practica la conversión de valores a binario, tanto para el caso decimal como para el caso hexadecimal.

1. `1000`
2. `0111`

### Task 5: Operaciones con registros

**Explicación:**

Se resuelven los ejercicios de operaciones con registros de 64 bits: el tamaño en bytes de un registro de 64 bits, la instrucción de incremento y la verificación del resultado obtenido.

1. `8`
2. `4`

### Task 6: Instrucciones de control de flujo

**Explicación:**

Se identifican las instrucciones clave del flujo de control en ensamblador: la instrucción de retorno (`ret`), la de llamada a función (`call`) y el orden correcto con la instrucción `PUSH`.

1. `ret`
2. `call`
3. `PUSH`

### Task 7: Introducción a la pila

**Explicación:**

Se introduce el concepto de pila en la convención x64 y se responde a la primera pregunta sobre su funcionamiento.

1. `1`

### Task 8: Convención de llamada

**Explicación:**

Se identifican los registros involucrados en la convención de llamada de Windows x64: RAX y RCX como parte de los registros utilizados.

1. `RAX`
2. `RCX`

### Task 9: Comportamiento de la pila

**Explicación:**

Se define la propiedad estructural de la pila: el tipo de estructura de datos que la gobierna (LIFO, Last-In-First-Out).

- `LIFO`

### Task 10: Conclusión

**Explicación:**

La sala cierra el curso de fundamentos de x64 Assembly con la consolidación de los conceptos vistos.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2.1 | Conversión a decimal | `10` |
| 2.2 | Conversión a hexadecimal | `0x19` |
| 3.1 | Tamaño de registro de 64 bits (bytes) | `2` |
| 3.2 | Tamaño de registro de 128 bits (bytes) | `16` |
| 4.1 | Conversión a binario (decimal) | `1000` |
| 4.2 | Conversión a binario (hexadecimal) | `0111` |
| 5.1 | Tamaño en bytes de un registro de 64 bits | `8` |
| 5.2 | Resultado de la operación de incremento | `4` |
| 6.1 | Instrucción de retorno | `ret` |
| 6.2 | Instrucción de llamada | `call` |
| 6.3 | Instrucción de apilado | `PUSH` |
| 7 | Introducción a la pila | `1` |
| 8.1 | Primer registro de la convención | `RAX` |
| 8.2 | Segundo registro de la convención | `RCX` |
| 9 | Estructura de datos de la pila | `LIFO` |
| 10 | Conclusión | `No answer needed` |

---

**Metodología:** Estudio progresivo del ensamblador x64: representación de datos, tamaños y registros, banderas e instrucciones, convención de llamada y comportamiento de la pila, con ejercicios prácticos de conversión y operaciones.

**Learning chain:** Números → registros → binario → operaciones → control de flujo → pila → convención de llamada → LIFO → síntesis.

**Lección:** *Comprender los registros y la pila en x64 es la base del análisis de binarios y de la explotación de vulnerabilidades en Windows.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1587 Develop Capabilities.

**Fuente:** [TryHackMe - Windows x64 Assembly](https://tryhackme.com/room/windowsx64assembly)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.