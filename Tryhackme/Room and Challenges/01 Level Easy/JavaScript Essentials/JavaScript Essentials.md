# JavaScript Essentials

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `javascriptessentials` | https://tryhackme.com/room/javascriptessentials | 01 Level Easy | TryHackMe | JavaScript / variables / tipos de datos / prompt() / condicionales / bucles | Fundamentos de programación en JavaScript: sintaxis, variables, tipos de datos, interacción con el usuario (prompt) y lógica de control aplicada a mini-desafíos. |

---

**Contexto:** Room introductoria de la ruta de programación de TryHackMe. Cubre los fundamentos de JavaScript: cómo se incluye el código (interno/externo), variables y operaciones, mensajes de entrada con `prompt()`, condicionales y salidas por consola. Cada pregunta evalúa la comprensión de un pequeño fragmento de código.

> **ES:** Sala introductoria de JavaScript: sintaxis básica, formas de incluir el código (internal/external), variables, `prompt()` y condicionales con pequeños ejercicios de código.
> **EN:** Introductory JavaScript room: basic syntax, ways to include code (internal/external), variables, `prompt()` and conditionals through small coding exercises.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea introductoria de la sala. Solo hay que leer la presentación del curso y preparar el entorno. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. / Read the room introduction. | `No answer needed` |

### Task 2: Bucles / Loops

**Explicación:** Se presenta el `loop` (bucle), el bloque de código diseñado para realizar una acción repetidamente mientras se cumpla una condición. JavaScript dispone de bucles `for`, `while` y `do...while`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué bloque de código ejecuta acciones repetidas mientras se cumple una condición? / What block of code performs repeated actions while a condition is met? | `loop` |

### Task 3: Variables y tipos de datos / Variables and Data Types

**Explicación:** Se practica la asignación y la suma de variables con el operador `+=`. Al actualizar el valor de una variable numérica y mostrarla, la consola imprime el resultado de la operación. JavaScript es un lenguaje **interpretado**: el navegador lo ejecuta línea a línea sin necesidad de compilar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el resultado que se muestra tras la operación? / What is the displayed result after the operation? | `The result is: 20` |
| 2 | ¿Qué tipo de lenguaje es JavaScript? / What type of language is JavaScript? | `Interpreted` |

### Task 4: Incluir JavaScript / Including JavaScript

**Explicación:** JavaScript puede incluirse de dos formas en una página web: **interno** (script dentro del HTML en `<script>`) o **externo** (fichero `.js` aparte enlazado). El ejercicio usa un archivo externo llamado `thm_external.js` referenciado mediante el atributo `src`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿De qué forma se incluye el código dentro del propio HTML? / How is code included inside the HTML itself? | `Internal` |
| 2 | ¿De qué forma se incluye el código desde un archivo aparte? / How is code included from a separate file? | `External` |
| 3 | ¿Cómo se llama el archivo JavaScript externo del ejercicio? / What is the name of the external JavaScript file in the exercise? | `thm_external.js` |
| 4 | ¿Qué atributo se usa para enlazar el archivo externo? / Which attribute links the external file? | `src` |

### Task 5: Entrada del usuario / User Input

**Explicación:** Se practica la captura de entrada del usuario con `prompt()`, que muestra un cuadro de diálogo y devuelve el valor introducido. La salida del ejercicio devuelve el valor `5` y la palabra `Tesla` como parte del ejemplo de entrada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la salida del ejercicio? / What is the output of the exercise? | `5` |
| 2 | ¿Qué método/función se usa para preguntar al usuario? / Which method is used to ask the user for input? | `prompt` |
| 3 | ¿Qué valor introduce el usuario en el ejemplo? / What value does the user enter in the example? | `Tesla` |

### Task 6: Condicionales / Conditionals

**Explicación:** Los condicionales `if/else` permiten ramificar el flujo del programa según una condición. En el ejemplo, si la edad es menor de 18 se muestra "You are a minor."; en la validación de contraseña, la cadena fuerte que supera la comprobación es `ComplexPassword`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué mensaje se muestra cuando la condición de edad se cumple? / Which message is shown when the age condition is met? | `You are a minor.` |
| 2 | ¿Qué contraseña supera la validación del ejercicio? / Which password passes the validation in the exercise? | `ComplexPassword` |

### Task 7: Mensajes de bienvenida / Welcome Messages

**Explicación:** Se combinan variables y condicionales para personalizar un mensaje. Con el valor introducido por el usuario, el programa construye el saludo "Welcome to THM" usando el número `21` del ejemplo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué mensaje de bienvenida se muestra? / Which welcome message is displayed? | `Welcome to THM` |
| 2 | ¿Qué número se usa en el ejercicio? / Which number is used in the exercise? | `21` |

### Task 8: Valores booleanos / Boolean Values

**Explicación:** Se repasa el tipo booleano y cómo JavaScript evalúa ciertos valores. La respuesta del ejercicio es la palabra `nay`, resultado del fragmento de código propuesto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la salida/palabra del ejercicio? / What is the output/word of the exercise? | `nay` |

### Task 9: Cierre / Wrap-up

**Explicación:** Tarea de cierre que resume los conceptos vistos (variables, tipos, bucles, condicionales, entrada de usuario). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el resumen final de la room. / Read the final summary of the room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `No answer needed` |
| 2 | ¿Qué bloque de código ejecuta acciones repetidas? | `loop` |
| 3 | ¿Cuál es el resultado que se muestra tras la operación? | `The result is: 20` |
| 4 | ¿Qué tipo de lenguaje es JavaScript? | `Interpreted` |
| 5 | ¿De qué forma se incluye el código dentro del propio HTML? | `Internal` |
| 6 | ¿De qué forma se incluye el código desde un archivo aparte? | `External` |
| 7 | ¿Cómo se llama el archivo JavaScript externo del ejercicio? | `thm_external.js` |
| 8 | ¿Qué atributo se usa para enlazar el archivo externo? | `src` |
| 9 | ¿Cuál es la salida del ejercicio? | `5` |
| 10 | ¿Qué método se usa para preguntar al usuario? | `prompt` |
| 11 | ¿Qué valor introduce el usuario en el ejemplo? | `Tesla` |
| 12 | ¿Qué mensaje se muestra cuando la condición de edad se cumple? | `You are a minor.` |
| 13 | ¿Qué contraseña supera la validación del ejercicio? | `ComplexPassword` |
| 14 | ¿Qué mensaje de bienvenida se muestra? | `Welcome to THM` |
| 15 | ¿Qué número se usa en el ejercicio? | `21` |
| 16 | ¿Cuál es la salida/palabra del ejercicio? | `nay` |
| 17 | Lee el resumen final de la room. | `No answer needed` |

---

**Metodología:** Seguir el curso de JavaScript de forma secuencial: leer los fundamentos teóricos de cada bloque (variables, bucles, condicionales, entrada/salida), analizar los fragmentos de código propuestos y deducir el valor exacto que produce cada ejercicio antes de escribir la respuesta.

### Cadena de ataque / Attack Chain

```text
Leer conceptos de cada task -> analizar el fragmento de código -> deducir la salida exacta -> validar sintaxis (Internal/External/src) -> responder cada pregunta
```

**Learning chain:** sintaxis -> variables (`+=`) -> tipos (interpreted) -> inclusión de código (internal/external/src) -> `prompt()` -> condicionales -> mensajes/salidas.

**Lección:** *JavaScript es un lenguaje interpretado en el que la lógica (variables, bucles, condicionales) se entiende mejor ejecutando y razonando pequeños fragmentos de código línea a línea.*

**MITRE ATT&CK:** N/A (room de fundamentos de programación)

**Fuente:** [TryHackMe - JavaScript Essentials](https://tryhackme.com/room/javascriptessentials)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.