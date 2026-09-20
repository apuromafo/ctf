# Regular Expressions

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room / Fundamentos de regex | regularexpressions | https://tryhackme.com/room/regularexpressions | 02 Level Medium | TryHackMe | Expresiones regulares, clases de caracteres, cuantificadores, grupos, anclas | Habilidad de búsqueda, filtrado y extracción de patrones |

> **Objeto:** Dominar la sintaxis de las expresiones regulares: construir patrones sobre conjuntos de caracteres (clases), cuantificadores, comodines, anclas de línea, clases abreviadas y grupos, resolviendo los ejercicios de cada bloque del laboratorio.

---

**Contexto:** La sala **Regular Expressions** es un laboratorio de práctica de expresiones regulares dividido en seis bloques progresivos. Se comienza con preguntas teóricas de preparación y se avanza por ejercicios de clases de caracteres `[...]`, comodines y escapes, cuantificadores `{}`, `*`, `+`, clases abreviadas `\w`, `\d`, `\s`, anclas `^`, `$` y grupos de captura `(...)`. Cada bloque pide escribir el patrón exacto que casa con el texto indicado.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Bloque teórico de introducción a las expresiones regulares, sin respuestas obligatorias.

1. `No answer needed`

### Task 2: Clases de caracteres / Character classes
**Explicación:**

Se escriben patrones usando clases de caracteres `[...]`, rangos y negaciones para casar los conjuntos indicados:

1. `[cog]`
2. `[cfh]at`
3. `[CcHh]at`
4. `[Ff]ile[1-9]`
5. `[Ff]ile[^7]`

### Task 3: Comodines y escapes / Wildcards and escapes
**Explicación:**

Se resuelven ejercicios con el comodín `.`, opcionales `?`, escapes `\.` y negaciones de rango:

1. `.at`
2. `[Cc]ats?`
3. `cat\.xyz`
4. `[ch]ats?\.xyz`
5. `...[^n-z]`
6. `[^r]ats?`

### Task 4: Cuantificadores / Quantifiers
**Explicación:**

Ejercicios con cuantificadores `{}`, `*`, `+`, clases abreviadas `\d`, `\w`, `\s` y alternancia mediante grupos:

1. `cats{4}`
2. `[Cc]ats*`
3. `regex go br+`
4. `[abc]{1,3}[01]{4}`
5. `[Ff]ile\d{1,2}`
6. `kali\s+tools`
7. `\w{5}\W`
8. `\S*\s*\S*`
9. `\S{8}[^!]`
10. `\.?\w+`

### Task 5: Anclas y grupos / Anchors and groups
**Explicación:**

Patrones con anclas `^`, `$`, escapes de fin de línea `\$$`, grupos de captura `(...)` y clases abreviadas para extraer los campos indicados:

1. `Password:[^0]{10}`
2. `^username:\s`
3. `^\D`
4. `EOF\$$`
5. `I use (nano|vim)`
6. `\$\d\$\S+`
7. `(\d{1,3}\.){3}\d{1,3}`
8. `(\w+)@(\w+)\.com`

### Task 6: Cierre / Wrap-up
**Explicación:**

Bloque final de lectura y repaso, sin respuesta obligatoria.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2 | Clase de caracteres 1 | `[cog]` |
| 3 | Clase de caracteres 2 | `[cfh]at` |
| 4 | Clase de caracteres 3 | `[CcHh]at` |
| 5 | Clase de caracteres 4 | `[Ff]ile[1-9]` |
| 6 | Clase de caracteres 5 | `[Ff]ile[^7]` |
| 7 | Comodín / escape 1 | `.at` |
| 8 | Comodín / escape 2 | `[Cc]ats?` |
| 9 | Comodín / escape 3 | `cat\.xyz` |
| 10 | Comodín / escape 4 | `[ch]ats?\.xyz` |
| 11 | Comodín / escape 5 | `...[^n-z]` |
| 12 | Comodín / escape 6 | `[^r]ats?` |
| 13 | Cuantificador 1 | `cats{4}` |
| 14 | Cuantificador 2 | `[Cc]ats*` |
| 15 | Cuantificador 3 | `regex go br+` |
| 16 | Cuantificador 4 | `[abc]{1,3}[01]{4}` |
| 17 | Cuantificador 5 | `[Ff]ile\d{1,2}` |
| 18 | Cuantificador 6 | `kali\s+tools` |
| 19 | Cuantificador 7 | `\w{5}\W` |
| 20 | Cuantificador 8 | `\S*\s*\S*` |
| 21 | Cuantificador 9 | `\S{8}[^!]` |
| 22 | Cuantificador 10 | `\.?\w+` |
| 23 | Anclas / grupos 1 | `Password:[^0]{10}` |
| 24 | Anclas / grupos 2 | `^username:\s` |
| 25 | Anclas / grupos 3 | `^\D` |
| 26 | Anclas / grupos 4 | `EOF\$$` |
| 27 | Anclas / grupos 5 | `I use (nano|vim)` |
| 28 | Anclas / grupos 6 | `\$\d\$\S+` |
| 29 | Anclas / grupos 7 | `(\d{1,3}\.){3}\d{1,3}` |
| 30 | Anclas / grupos 8 | `(\w+)@(\w+)\.com` |
| 31 | Cierre | `No answer needed` |

---

**Metodología:** Práctica progresiva de los bloques de expresiones regulares: clases de caracteres, comodines y escapes, cuantificadores, clases abreviadas, anclas y grupos de captura, verificando cada patrón contra el texto objetivo.

**Learning chain:** Bases → clases `[...]` → comodines y escapes → cuantificadores y clases abreviadas → anclas `^`/`$` y grupos → síntesis en patrones compuestos.

**Lección:** *Una expresión regular se construye de lo específico a lo general: fijar la clase, el rango o la ancla exacta antes de añadir cuantificadores evita patrones que sobre-particionan o dejan de casar el texto real.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1005 Data from Local System · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Regular Expressions](https://tryhackme.com/room/regularexpressions)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.