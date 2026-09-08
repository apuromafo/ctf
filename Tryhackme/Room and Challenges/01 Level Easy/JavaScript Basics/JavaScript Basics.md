# JavaScript Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `javascriptbasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/javascriptbasics) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de khansiddique (GitHub) + GhostlyPy (autor de la room) |
| **Componentes** | JavaScript / variables (var, let, const) / condicionales / funciones / objetos / arrays / bucles / DOM / XSS |
| **Impacto** | Aprende JavaScript, el lenguaje de alto nivel y multi-paradigma de la web: variables, condicionales, funciones, objetos, arrays, bucles, DOM y XSS. |

---

**Contexto:** Aprende JavaScript, el lenguaje de alto nivel y multi-paradigma de la web. La room cubre variables, condicionales, funciones, objetos, arrays, bucles, DOM y XSS.

## Solucionario

### Task 1: Intro to JavaScript

**Explicación:** El propósito principal de JavaScript es implementar interactividad en páginas y aplicaciones web, pero también se usa para controlar servidores, crear videojuegos, aplicaciones móviles y ciberseguridad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's Begin! | `No answer needed` |

### Task 2: Variables & Operators

**Explicación:** Hay 3 tipos de variables: `var` (global, se puede actualizar y re-declarar), `let` (block-scoped, se puede actualizar pero no re-declarar) y `const` (block-scoped, no se puede actualizar ni re-declarar). Tipos de datos: Number, String, Boolean, Arrays, Objects, Floating-Point Numbers. El tag HTML para enlazar un archivo JS es **`<script>`**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of data type is this: 'Neo'? | `string` |
| 2 | What data type is true/false? | `boolean` |
| 3 | What is John's occupation? | `Master Hacker` |
| 4 | What tag is used for linking a JavaScript file to HTML? | `script` |

### Task 3: Conditionals

**Explicación:** Los condicionales `if`, `else if`, `else` y los `switch cases` permiten ejecutar código según condiciones. Los switch cases son mejores para probar múltiples condiciones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Congratulations! You can now write conditionals! | `No answer needed` |

### Task 4: Functions

**Explicación:** Las funciones son una de las partes más vitales de la programación. En ES6 se escriben con arrow functions: `const func = (a, b) => { ... }`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Finished with Functions! | `No answer needed` |

### Task 5: Objects & Arrays

**Explicación:** Los objetos son otra variación de variables con propiedades y valores. Los arrays almacenan múltiples valores en una sola variable, con corchetes `[]`. La mayoría de lenguajes empiezan a contar desde 0.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of brackets are used for arrays? | `[]` |
| 2 | What color pill did we choose? | `Red Pill` |
| 3 | What is the output of this code? | `Tyrell` |

### Task 6: Loops

**Explicación:** Hay bucles `for`, `while` y `do...while`. El bucle `do...while` siempre se ejecuta al menos una vez porque ejecuta el código antes de comprobar la condición.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Loops repeat until the written code is finished running (true/false) | `true` |
| 2 | What loop doesn't require the condition to be true for it execute at least once? | `do...while` |

### Task 7: Document Object Model (DOM)

**Explicación:** El DOM permite manipular el HTML de la página. Métodos: `getElementByID`, `getElementByClassName`, `getElementByTagName`. Eventos: `onclick`, `onmouseover`, `onload`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the DOM? | `Document Object Model` |

### Task 8: XSS

**Explicación:** Cross-Site Scripting es una vulnerabilidad de seguridad típicamente encontrada en aplicaciones web que permite ejecutar un script malicioso en la máquina del objetivo. Tipos: DOM-Based XSS, Reflected XSS, Stored XSS. Ataques: keylogging (registro de teclado), robo de cookies, phishing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is it called when XSS is used to record keystrokes? | `Keylogging` |

### Task 9: Final Notes

**Explicación:** Notas finales del curso. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | JavaScript Basics Master! | `No answer needed` |

### Task 10: JavaScript Challenge

**Explicación:** Ordenar un array de números usando el método `.sort()` con una función de comparación numérica (para evitar el orden lexicográfico de `.sort()` por defecto).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sort the array [1,10,5,15,2,7,28,900,45,18,27] | `1,2,5,7,10,15,18,27,28,45,900` |

---

**Metodología:**
1. **Variables:** `var`, `let`, `const` y tipos de datos (string, boolean, number, array, object).
2. **Operadores:** aritméticos, comparación, booleanos y lógicos.
3. **Condicionales:** `if/else if/else` y `switch cases`.
4. **Funciones:** ES5 vs ES6 (arrow functions).
5. **Objetos y arrays:** acceso a propiedades y posiciones (indexado desde 0).
6. **Bucles:** `for`, `while`, `do...while`.
7. **DOM:** manipulación del HTML con métodos y eventos.
8. **XSS:** tipos (DOM, Reflected, Stored) y ataques (keylogging, cookies, phishing).

**Lección:** JavaScript es fundamental en ciberseguridad, especialmente para explotación de aplicaciones web, cross-site scripting e inyección JavaScript.

**MITRE ATT&CK:** T1059.007 (Command and Scripting Interpreter: JavaScript), T1189 (Drive-by Compromise), T1059.006 (Command and Scripting Interpreter: Python) en el contexto del challenge.

**Fuente:** [TryHackMe - JavaScript Basics](https://tryhackme.com/room/javascriptbasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
