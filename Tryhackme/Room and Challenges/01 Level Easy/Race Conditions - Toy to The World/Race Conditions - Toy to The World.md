# Race Conditions - Toy to The World

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `race-conditions-aoc2025-d7f0g3h6j9` | https://tryhackme.com/room/race-conditions-aoc2025-d7f0g3h6j9 | Advent of Cyber 2025 | THM | race conditions, TOCTOU, stock manipulation, Burp | Exploiting race conditions in e-commerce stock checks to manipulate inventory |

---

**Contexto:** Una tienda en línea de juguetes navideños tiene una vulnerabilidad de race condition en la lógica de verificación de stock. Al enviar múltiples solicitudes de compra simultáneas, se puede manipular el inventario a valores negativos antes de que se actualice el conteo, demostrando la clásica condición de carrera TOCTOU.

> **ES:** Una tienda en línea de juguetes navideños tiene una vulnerabilidad de race condition en la lógica de verificación de stock. Al enviar múltiples solicitudes de compra simultáneas, se puede manipular el inventario a valores negativos antes de que se actualice el conteo, demostrando la clásica condición de carrera TOCTOU.
> **EN:** An online Christmas toy store has a race condition vulnerability in its stock-check logic. By sending multiple simultaneous purchase requests, the inventory can be driven to negative values before the count is updated, demonstrating the classic TOCTOU race condition.

## Solucionario

### Task 1: SleighToy Limited Edition / SleighToy Limited Edition

**Explicación:** Se aprovecha la ventana TOCTOU (Time-Of-Check To Time-Of-Use) del endpoint de compra: la verificación de stock y la actualización del inventario no son atómicas. Se envía la solicitud de compra del SleighToy Limited Edition de forma simultánea y repetida para que todas las comprobaciones lean el stock antes de que el sistema lo decremente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value once the stocks are negative for SleighToy Limited Edition? | `THM{WINNER_OF_R@CE007}` |

### Task 2: Bunny Plush (Blue) / Bunny Plush (Blue)

**Explicación:** Se repite la misma técnica de race condition sobre el segundo producto, encontrando que puede existir un límite de compras por petición. Hay que relanzar la petición desde cero (nuevo intento) para que los IDs de pedido se reinicien y todas las comprobaciones caigan en la misma ventana de carrera antes del incremento del contador de inventario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)? | `THM{WINNER_OF_Bunny_R@ce}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value once the stocks are negative for SleighToy Limited Edition? | `THM{WINNER_OF_R@CE007}` |
| 2 | Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)? | `THM{WINNER_OF_Bunny_R@ce}` |

---

**Metodología:** Se interceptó la solicitud de compra con Burp Suite y se identificó el endpoint de stock check. Se enviaron múltiples requests simultáneos (Repeater/intruder) para superar la verificación de stock antes de que se decrementara, logrando stock negativo y revelando el flag. Se repitió el proceso para el segundo producto.

### Cadena de ataque / Attack Chain

```text
Interceptar petición de compra (Burp) → identificar endpoint de stock check → duplicar/relanzar requests simultáneos → explotar condición de carrera TOCTOU → stock negativo → extraer flag por producto
```

**Learning chain:** HTTP interception (Burp) → request duplication → race condition exploitation → stock manipulation (TOCTOU) → flag retrieval

**Lección:** *La verificación de stock (check) debe ser atómica con la actualización del inventario (use). Cualquier separación entre ambas operaciones abre una ventana TOCTOU que puede ser explotada con peticiones concurrentes para agotar stock, manipular precios o generar pedidos inválidos.*

**MITRE ATT&CK:** N/A (defensive walkthrough)

**Fuente:** [TryHackMe - Race Conditions - Toy to The World](https://tryhackme.com/room/race-conditions-aoc2025-d7f0g3h6j9)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.