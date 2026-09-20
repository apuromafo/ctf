# x86 Assembly Crash Course

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | x86assemblycrashcourse | https://tryhackme.com/room/x86assemblycrashcourse | 02 Level Medium | TryHackMe | Assembly x86, Registros, EFLAGS, Intel | Curso intensivo de ensamblador x86: opcodes, registros, banderas e instrucciones con ejercicios prácticos |

---

**Contexto:** La sala **x86 Assembly Crash Course** ofrece un curso intensivo de programación en ensamblador x86 (arquitectura Intel). Se cubren los conceptos de opcodes y operandos (incluido el operando de memoria), los registros de propósito general (eax), instrucciones como nop, las banderas del registro de estado (ZF, SF, Carry Flag) y su comportamiento, instrucciones de incremento, llamadas a funciones y la instrucción pusha. Al final se realiza un ejercicio práctico de seguimiento de registros y banderas paso a paso.

## Solucionario

### Task 1: Introducción

**Explicación:**

La sala presenta el objetivo del curso intensivo de ensamblador x86 y la arquitectura en la que se basa (Intel).

Respuesta: `No answer needed`

### Task 2: Opcodes y operandos

**Explicación:**

Se introducen los elementos básicos de una instrucción: los códigos de operación (opcodes) y los operandos, con especial atención al operando de memoria.

1. `Opcodes`
2. `memory operand`

### Task 3: Registros de propósito general

**Explicación:**

Se identifican el registro de propósito general de 32 bits (eax) y la instrucción que no hace nada (nop).

1. `eax`
2. `nop`

### Task 4: Registro de banderas

**Explicación:**

Se identifican las banderas del registro EFLAGS: la bandera de cero (ZF) y la bandera de signo (SF).

1. `ZF`
2. `SF`

### Task 5: Instrucciones aritméticas

**Explicación:**

Se practica la ejecución de instrucciones aritméticas: la bandera afectada (Carry Flag), la instrucción de incremento (inc) y la verificación del resultado de la operación.

1. `Carry Flag`
2. `inc`
3. `yea`

### Task 6: Comparaciones y saltos

**Explicación:**

Se analiza el comportamiento de las instrucciones de comparación: la bandera de cero, el valor resultado de la comparación y la bandera que se modifica en la operación.

1. `Zero flag`
2. `1`
3. `Zero flag`

### Task 7: Llamadas a funciones

**Explicación:**

Se identifican las instrucciones relacionadas con las llamadas a funciones: la instrucción de salto con retorno (call) y la instrucción que apila todos los registros (pusha).

1. `call`
2. `pusha`

### Task 8: Ejercicio práctico

**Explicación:**

Se resuelve el ejercicio de seguimiento de la ejecución: los valores que toman los registros en cada paso (0x00000040, 0x00000025, 0x00000010, 0x0000004B, 0x00000045), el motivo por el que una operación no se permite (movimiento memoria a memoria), y las banderas modificadas en cada etapa (PF,ZF y CF,SF).

1. `0x00000040`
2. `Memory to memory data movement is not allowed.`
3. `0x00000025`
4. `0x00000010`
5. `0x00000010`
6. `PF,ZF`
7. `CF,SF`
8. `0x0000004B`
9. `0x00000045`

### Task 9: Conclusión

**Explicación:**

La sala cierra el curso intensivo tras consolidar los fundamentos de la programación en ensamblador x86.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2.1 | Códigos de operación | `Opcodes` |
| 2.2 | Tipo de operando de memoria | `memory operand` |
| 3.1 | Registro de propósito general | `eax` |
| 3.2 | Instrucción que no hace nada | `nop` |
| 4.1 | Bandera de cero | `ZF` |
| 4.2 | Bandera de signo | `SF` |
| 5.1 | Bandera afectada por la operación | `Carry Flag` |
| 5.2 | Instrucción de incremento | `inc` |
| 5.3 | Verificación del resultado | `yea` |
| 6.1 | Bandera de la comparación | `Zero flag` |
| 6.2 | Valor de la comparación | `1` |
| 6.3 | Segunda bandera de la comparación | `Zero flag` |
| 7.1 | Instrucción de llamada | `call` |
| 7.2 | Instrucción pusha | `pusha` |
| 8.1 | Valor del registro (paso 1) | `0x00000040` |
| 8.2 | Motivo de la operación no permitida | `Memory to memory data movement is not allowed.` |
| 8.3 | Valor del registro (paso 2) | `0x00000025` |
| 8.4 | Valor del registro (paso 3) | `0x00000010` |
| 8.5 | Valor del registro (paso 4) | `0x00000010` |
| 8.6 | Banderas modificadas (paso 5) | `PF,ZF` |
| 8.7 | Banderas modificadas (paso 6) | `CF,SF` |
| 8.8 | Valor del registro (paso 7) | `0x0000004B` |
| 8.9 | Valor del registro (paso 8) | `0x00000045` |
| 9 | Conclusión | `No answer needed` |

---

**Metodología:** Curso progresivo de ensamblador x86: opcodes y operandos, registros, banderas, instrucciones aritméticas y de control, llamadas a funciones y seguimiento práctico de la ejecución registro a registro.

**Learning chain:** Opcodes → registros → banderas → aritmética → comparaciones → llamadas → ejercicio práctico → conclusión.

**Lección:** *Las banderas del EFLAGS son el estado silencioso de la CPU: cada comparación y operación aritmética deja su huella, y leerlas es leer la lógica del programa.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1588 Obtain Capabilities.

**Fuente:** [TryHackMe - x86 Assembly Crash Course](https://tryhackme.com/room/x86assemblycrashcourse)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.