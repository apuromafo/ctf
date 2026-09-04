# JavaScript Basics [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `javascriptbasics`
* **Link:** https://tryhackme.com/room/javascriptbasics
* **Sección / Section:** Coding / Web
* **Fuente / Source:** Writeup de khansiddique (GitHub) + GhostlyPy (autor de la room)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Aprende JavaScript, el lenguaje de alto nivel y multi-paradigma de la web. La room cubre variables, condicionales, funciones, objetos, arrays, bucles, DOM y XSS.
> **EN:** Learn JavaScript, the high-level, multi-paradigm language of the web. The room covers variables, conditionals, functions, objects, arrays, loops, DOM and XSS.

---

### Task 1 — Intro to JavaScript

El propósito principal de JavaScript es implementar interactividad en páginas y aplicaciones web, pero también se usa para controlar servidores, crear videojuegos, aplicaciones móviles y ciberseguridad.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Let's Begin! | `No answer needed` |

---

### Task 2 — Variables & Operators

Hay 3 tipos de variables: `var` (global, se puede actualizar y re-declarar), `let` (block-scoped, se puede actualizar pero no re-declarar) y `const` (block-scoped, no se puede actualizar ni re-declarar). Tipos de datos: Number, String, Boolean, Arrays, Objects, Floating-Point Numbers.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of data type is this: 'Neo'? | `string` |
| What data type is true/false? | `boolean` |
| What is John's occupation? | `Master Hacker` |
| What tag is used for linking a JavaScript file to HTML? | `script` |

---

### Task 3 — Conditionals

Los condicionales `if`, `else if`, `else` y los `switch cases` permiten ejecutar código según condiciones. Los switch cases son mejores para probar múltiples condiciones.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Congratulations! You can now write conditionals! | `No answer needed` |

---

### Task 4 — Functions

Las funciones son una de las partes más vitales de la programación. En ES6 se escriben con arrow functions: `const func = (a, b) => { ... }`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Finished with Functions! | `No answer needed` |

---

### Task 5 — Objects & Arrays

Los objetos son otra variación de variables con propiedades y valores. Los arrays almacenan múltiples valores en una sola variable. La mayoría de lenguajes empiezan a contar desde 0.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of brackets are used for arrays? | `[]` |
| What color pill did we choose? | `Red Pill` |
| What is the output of this code? | `Tyrell` |

---

### Task 6 — Loops

Hay bucles `for`, `while` y `do...while`. El bucle `do...while` siempre se ejecuta al menos una vez porque ejecuta el código antes de comprobar la condición.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Loops repeat until the written code is finished running (true/false) | `true` |
| What loop doesn't require the condition to be true for it execute at least once? | `do...while` |

---

### Task 7 — Document Object Model (DOM)

El DOM permite manipular el HTML de la página. Métodos: `getElementByID`, `getElementByClassName`, `getElementByTagName`. Eventos: `onclick`, `onmouseover`, `onload`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the DOM? | `Document Object Model` |

---

### Task 8 — XSS

Cross-Site Scripting es una vulnerabilidad de seguridad típicamente encontrada en aplicaciones web que permite ejecutar un script malicioso en la máquina del objetivo. Tipos: DOM-Based XSS, Reflected XSS, Stored XSS. Ataques: keylogging, robo de cookies, phishing.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is it called when XSS is used to record keystrokes? | `Keylogging` |

---

### Task 9 — Final Notes

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| JavaScript Basics Master! | `No answer needed` |

---

### Task 10 — JavaScript Challenge

Ordenar un array de números usando el método `.sort()` con una función de comparación.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Sort the array [1,10,5,15,2,7,28,900,45,18,27] | `1,2,5,7,10,15,18,27,28,45,900` |

---

## Metodología / Methodology

1. **Variables:** `var`, `let`, `const` y tipos de datos (string, boolean, number, array, object).
2. **Operadores:** aritméticos, comparación, booleanos y lógicos.
3. **Condicionales:** `if/else if/else` y `switch cases`.
4. **Funciones:** ES5 vs ES6 (arrow functions).
5. **Objetos y arrays:** acceso a propiedades y posiciones (indexado desde 0).
6. **Bucles:** `for`, `while`, `do...while`.
7. **DOM:** manipulación del HTML con métodos y eventos.
8. **XSS:** tipos (DOM, Reflected, Stored) y ataques (keylogging, cookies, phishing).

**Lección:** JavaScript es fundamental en ciberseguridad, especialmente para explotación de aplicaciones web, cross-site scripting e inyección JavaScript.

---

*Documentación para propósitos educativos y registro de CTF.*
