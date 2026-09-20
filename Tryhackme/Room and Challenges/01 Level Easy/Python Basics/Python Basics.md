# Python Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `pythonbasics` | https://tryhackme.com/room/pythonbasics | 01 Level Easy | THM | Python, Print, Operadores, Variables, If, Loops, Funciones, Files, Imports | Fundamentos del scripting con Python |

---

**Contexto:** Room de la ruta Scripting for Pentesters que enseña los fundamentos de Python: print, operadores matemáticos, variables, tipos de datos, operadores lógicos/booleanos, sentencias if, bucles while/for, funciones, manejo de archivos y módulos. Incluye proyectos prácticos (calculadora de carrito, inversor de Bitcoin).

> **ES:** Room que enseña los fundamentos de Python (print, operadores, variables, if, bucles, funciones, archivos, imports) mediante ejercicios interactivos y proyectos prácticos como la calculadora de carrito, la primera app o el inversor de Bitcoin.
> **EN:** A room teaching Python fundamentals (print, operators, variables, if, loops, functions, files, imports) through interactive exercises and hands-on projects such as the shopping cart, the first app or the Bitcoin investor.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se verifica la versión de Python instalada en la máquina de trabajo y se prepara el entorno.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Verify your Python version to get started | `No answer needed` |

### Task 2: Hola mundo / Hello World

**Explicación:** Se crea el primer script que imprime un mensaje con la función print(), obtiene la flag de validación y se ejecuta con `python3`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is printed by the print statement exercise? | `THM{PRINT_STATEMENTS}` |

### Task 3: Operadores matemáticos / Mathematical Operators

**Explicación:** Se ejecutan los scripts de suma, resta, multiplicación y exponenciación, cada uno revela su flag al completarse correctamente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag of the addition script? | `THM{ADDITI0N}` |
| 2 | What is the flag of the subtraction script? | `THM{SUBTRCT}` |
| 3 | What is the flag of the multiplication script? | `THM{MULTIPLICATION_PYTHON}` |
| 4 | What is the flag of the exponentiation script? | `THM{EXP0N3NT_POWER}` |

### Task 4: Variables y tipos de datos / Variables and Data Types

**Explicación:** Se declaran variables con distintos tipos de datos (string, int, float) y se completa el ejercicio interactivo del canvas que otorga la flag con el resultado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the variables exercise | `No answer needed` |
| 2 | Run the variables script | `No answer needed` |
| 3 | What flag do you get after completing the variables exercise? | `THM{VARIABL3S}` |

### Task 5: Operadores lógicos y booleanos / Logical and Boolean Operators

**Explicación:** Se trabajan los operadores lógicos (and, or, not) y los valores booleanos True/False con el operador de comparación `==`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the logical and boolean operators exercise | `No answer needed` |

### Task 6: Introducción a las sentencias If / Introduction to If Statements

**Explicación:** Se implementan condicionales if/elif/else y se completan los proyectos "Shopping Cart" (carrito de la compra) y "My First App" (primera app).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the if statement exercise | `No answer needed` |
| 2 | What flag is revealed by the Shopping Cart project? | `THM{IF_STATEMENT_SHOPPING}` |
| 3 | What flag is revealed by the My First App project? | `THM{MY_FIRST_APP}` |

### Task 7: Bucles / Loops

**Explicación:** Se utilizan los bucles while y for para iterar sobre rangos y listas, completando el ejercicio que revela la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is revealed by the loops exercise? | `THM{L00PS_WHILE_FOR}` |

### Task 8: Introducción a las funciones / Introduction to Functions

**Explicación:** Se definen funciones con def, parámetros y return, y se completa el proyecto "Bitcoin Investor" que calcula ganancias.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is revealed by the Bitcoin Investor project? | `THM{BITC0IN_INVESTOR}` |
| 2 | Complete the remaining function exercises | `No answer needed` |

### Task 9: Archivos / Files

**Explicación:** Se lee el contenido de un archivo con open() y read(), y su ejercicio revela la flag con el texto extraído.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is revealed by the file reading exercise? | `THM{F1LE_R3AD}` |

### Task 10: Importaciones / Imports

**Explicación:** Se importan librerías estándar (random, os, etc.) para ampliar las capacidades de los scripts y se completa el ejercicio final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the imports exercise | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Verify your Python version to get started | `No answer needed` |
| 2 | What flag is printed by the print statement exercise? | `THM{PRINT_STATEMENTS}` |
| 3 | What is the flag of the addition script? | `THM{ADDITI0N}` |
| 4 | What is the flag of the subtraction script? | `THM{SUBTRCT}` |
| 5 | What is the flag of the multiplication script? | `THM{MULTIPLICATION_PYTHON}` |
| 6 | What is the flag of the exponentiation script? | `THM{EXP0N3NT_POWER}` |
| 7 | Complete the variables exercise | `No answer needed` |
| 8 | Run the variables script | `No answer needed` |
| 9 | What flag do you get after completing the variables exercise? | `THM{VARIABL3S}` |
| 10 | Complete the logical and boolean operators exercise | `No answer needed` |
| 11 | Complete the if statement exercise | `No answer needed` |
| 12 | What flag is revealed by the Shopping Cart project? | `THM{IF_STATEMENT_SHOPPING}` |
| 13 | What flag is revealed by the My First App project? | `THM{MY_FIRST_APP}` |
| 14 | What flag is revealed by the loops exercise? | `THM{L00PS_WHILE_FOR}` |
| 15 | What flag is revealed by the Bitcoin Investor project? | `THM{BITC0IN_INVESTOR}` |
| 16 | Complete the remaining function exercises | `No answer needed` |
| 17 | What flag is revealed by the file reading exercise? | `THM{F1LE_R3AD}` |
| 18 | Complete the imports exercise | `No answer needed` |

---

**Metodología:** Ejecutar los scripts de ejemplo en la máquina remota, completar cada ejercicio en orden (print → operadores → variables → lógicos → if → bucles → funciones → archivos → imports) y anotar la flag que revela cada proyecto.

### Cadena de ataque / Attack Chain

```text
Verificar Python → Hello World (print) → operadores matemáticos → variables y tipos → operadores lógicos → sentencias if (carrito/app) → bucles → funciones (Bitcoin Investor) → archivos → imports
```

**Learning chain:** Introducción → Hello World → Operadores → Variables → Lógicos/Booleanos → If statements → Loops → Funciones → Files → Imports

**Lección:** *Domina primero la sintaxis básica de Python (tipos, condicionales, bucles, funciones, archivos, módulos): es la base para escribir scripts de automatización y pentesting eficaces y legibles.*

**MITRE ATT&CK:** N/A (Room de fundamentos de programación)

**Fuente:** [TryHackMe - Python Basics](https://tryhackme.com/room/pythonbasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.