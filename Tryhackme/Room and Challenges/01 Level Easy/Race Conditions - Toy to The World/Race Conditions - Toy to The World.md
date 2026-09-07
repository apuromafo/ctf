# Race Conditions - Toy to The World

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `race-conditions-aoc2025-d7f0g3h6j9` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/race-conditions-aoc2025-d7f0g3h6j9) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | race conditions, TOCTOU, stock manipulation, Burp |
| **Impacto** | Exploiting race conditions in e-commerce stock checks to manipulate inventory |

---

**Contexto:** Una tienda en línea de juguetes navideños tiene una vulnerabilidad de race condition en la lógica de verificación de stock. Al enviar múltiples solicitudes de compra simultáneas, se puede manipular el inventario a valores negativos antes de que se actualice el conteo, demostrando la clásica condición de carrera TOCTOU.

## Solucionario

### Task 1: SleighToy Limited Edition

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value once the stocks are negative for SleighToy Limited Edition? | `THM{WINNER_OF_R@CE007}` |

### Task 2: Bunny Plush (Blue)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)? | `THM{WINNER_OF_Bunny_R@ce}` |

---

**Metodología:** Se interceptó la solicitud de compra con Burp Suite y se identificó el endpoint de stock check. Se enviaron múltiples requests simultáneos (Repeater/intruder) para superar la verificación de stock antes de que se decrementara, logrando stock negativo y revelando el flag. Se repitió el proceso para el segundo producto.
**Learning chain:** HTTP interception (Burp) → request duplication → race condition exploitation → stock manipulation (TOCTOU) → flag retrieval
**MITRE ATT&CK:** N/A (defensive walkthrough)
**Fuente:** [TryHackMe - Race Conditions - Toy to The World](https://tryhackme.com/r/room/race-conditions-aoc2025-d7f0g3h6j9)
