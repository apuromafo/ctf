# CyberChef_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `cyberchefthebasics` | [TryHackMe](https://tryhackme.com/room/cyberchefthebasics) | 01 Level Easy | THM | CyberChef, Encoding, Decodificación, Recipe, Magic | Fundamentos de encoding/decoding con CyberChef |

> **Objeto:** Aprender a usar CyberChef desde cero: la interfaz, las operations, las recetas (Recipe) y el flujo Magic para codificar y decodificar datos.

---

**Contexto:** Sala introductoria a CyberChef: se exploran los conceptos de operations, recipes y Magic, se práctica la codificación/decodificación de direcciones, hashes y textos, y se obtienen datos de ejemplo de la propia web de TryHackMe.

> **ES:** Sala introductoria a CyberChef: operations, recipes y Magic para codificar y decodificar datos paso a paso.
> **EN:** Introductory room to CyberChef: operations, recipes and Magic to encode and decode data step by step.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y del objetivo de aprender CyberChef.

No answer needed

### Task 2: Instalación / Installation
**Explicación:** Comprobaciones previas y entorno de trabajo.

No answer needed

### Task 3: Interfaz / Interface
**Explicación:** Se identifican las partes principales de la interfaz de CyberChef.

1. operations
2. Recipe

### Task 4: Primera prueba / First Look Gate
**Explicación:** Primeras operaciones con la herramienta.

1

### Task 5: Codificación / Encoding
**Explicación:** Se codifican y decodifican distintos datos de ejemplo.

1. hidden@hotmail.com
2. 102.20.11.232
3. TryHackMe.com
4. 01001110
5. https://tryhackme.com/r/careers____________

### Task 6: Magic / Magic
**Explicación:** Se usa el flujo de auto-detección Magic para resolver las cadenas propuestas.

1. 10.10.2.10
2. TmljZSBSb29tIQ==
3. https://tryhackme.com/r/room/cyberchefbasics
4. Sun 1 September 2024 00:40:58 UTC
5. This is fun!

### Task 7: Recapitulación / Recap
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2 | — | `No answer needed` |
| 3.1 | Lista de componentes disponibles | `operations` |
| 3.2 | Flujo de operaciones | `Recipe` |
| 4 | Resultado de la primera prueba | `1` |
| 5.1 | Dato codificado 1 | `hidden@hotmail.com` |
| 5.2 | Dato codificado 2 | `102.20.11.232` |
| 5.3 | Dato codificado 3 | `TryHackMe.com` |
| 5.4 | Dato codificado 4 | `01001110` |
| 5.5 | Dato codificado 5 | `https://tryhackme.com/r/careers____________` |
| 6.1 | Magic 1 | `10.10.2.10` |
| 6.2 | Magic 2 | `TmljZSBSb29tIQ==` |
| 6.3 | Magic 3 | `https://tryhackme.com/r/room/cyberchefbasics` |
| 6.4 | Magic 4 | `Sun 1 September 2024 00:40:58 UTC` |
| 6.5 | Magic 5 | `This is fun!` |
| 7 | — | `No answer needed` |

---

**Metodología:** Exploración de la interfaz de CyberChef, reconocimiento de operations y recipes, codificación/decodificación manual de varios formatos (email, IP, URL, binario) y uso del flujo Magic para la auto-detección del formato correcto.

### Cadena de ataque / Attack Chain

Interfaz → operations → recipe → encoding manual → Magic → decodificación de datos → comprensión del flujo.

**Learning chain:** CyberChef → operations → recipe → encoding → decoding → Magic

*Lección:* Conocer las operaciones de CyberChef acelera enormemente el análisis de datos codificados en cualquier investigación.

**MITRE ATT&CK:** N/A.

**Fuente:** [TryHackMe - CyberChef_ The Basics](https://tryhackme.com/room/cyberchefthebasics)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.