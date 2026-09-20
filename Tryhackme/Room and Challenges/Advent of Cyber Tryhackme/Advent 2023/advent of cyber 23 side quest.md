# Advent 2023 [N/A]

| **Dificultad** | N/A | **Tipo** | CTF (Free Room - Bonus) | **Slug** | `adventofcyber23sidequest` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber23sidequest) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | side quest / flags de desafío adicional / retos extra del evento | | **Impacto** | Retos extra (Side Quests) del Advent of Cyber 2023 con 4 flags ocultas a lo largo del evento |

---

**Contexto:** Advent of Cyber '23 Side Quest: conjunto de desafíos adicionales (side quests) de dificultad extra lanzados durante el Advent of Cyber 2023. Cada reto otorgaba una flag con prefijo numerado (`1-`, `2-`, `3-`, `4-`) distinta de las flags diarias del room principal. Este solucionario recoge las 4 flags de los challenges 1 a 4 más el paso de confirmación "NO HINTS".

---

## Solucionario

### Task 1: Side Quest Challenge 1

**Explicación:** Primer reto extra del evento. La flag comienza con el prefijo del challenge (`1-`) seguido de un hash SHA256.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Side Quest Challenge 1 Flag | `1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834` |

### Task 2: Side Quest Challenge 2

**Explicación:** Segundo reto extra. La flag es una cadena aleatoria con signos, símbolos y mayúsculas/minúsculas propias de un token de alta entropía.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Side Quest Challenge 2 Flag | `2-K@bWJ5oHFCR8o%whAvK5qw8Sp$5qf!nCqGM3ksaK` |

### Task 3: Side Quest Challenge 3

**Explicación:** Tercer reto extra. Igual que el Challenge 1, la flag es un hash SHA256 con el prefijo `3-`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Side Quest Challenge 3 Flag | `3-d2dc6a02db03401177f0511a6c99007e945d9cb9b96b8c6294f8c5a2c8e01f60` |

### Task 4: Side Quest Challenge 4

**Explicación:** Cuarto reto extra. Flag de alta entropía con símbolos y números, precedida por el prefijo `4-`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Side Quest Challenge 4 Flag | `4-3f$FEBwD6AoqnyLjJ!!Hk4tc*V6w$UuK#evLWkBp` |

### Task 5: Continuación del Reto — NO HINTS

**Explicación:** Para continuar con las side quests, el reto exige escribir textualmente "NO HINTS" como confirmación de que se resolverá sin pistas.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Type NO HINTS to continue. | `NO HINTS` |

---

**Metodología:**

1. Resolución de los retos extra (side quests) publicados durante el evento
2. Recopilación de las 4 flags con prefijo numerado (1-4)
3. Confirmación de continuación del reto respondiendo "NO HINTS" (sin pistas)

**Learning chain:** Side Quest 1 -> Side Quest 2 -> Side Quest 3 -> Side Quest 4 -> NO HINTS

**Lección:** *Las side quests del AoC 2023 premiaron a quienes resolvieron los retos sin pistas: flags de alta entropía aisladas del solucionario diario, reforzando las técnicas vistas cada día en un entorno competitivo.*

**MITRE ATT&CK:**

- N/A (retos extra sin técnica específica declarada)

**Fuente:** [TryHackMe - Advent 2023 [N/A]](https://tryhackme.com/room/adventofcyber23sidequest)


---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.