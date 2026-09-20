# XSS

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `axss` | [TryHackMe](https://tryhackme.com/room/axss) | 01 Level Easy | TryHackMe | XSS / Stored XSS / Reflected XSS / DOM-based XSS / sanitizeHtml / htmlspecialchars / HttpUtility.HtmlEncode / encodeURIComponent / PHPSESSID | Detección y mitigación de Cross-Site Scripting: tipos de XSS, buenas prácticas de codificación, sanitización y control de entrada |

---

**Contexto:** Sala que introduce los tres tipos de Cross-Site Scripting (Stored, Reflected y DOM-based), el papel del DOM, las buenas prácticas de validación, sanitización y codificación de entrada/salida, así como rutinas seguras en distintos entornos (Python, PHP, .NET, JavaScript) y los vectores de ataque como las cookies (PHPSESSID) y los fragmentos de URL.

> **ES:** La sala repasa qué es el XSS, los tres tipos principales, la diferencia entre validar, sanitizar y codificar, las funciones seguras (sanitizeHtml, htmlspecialchars, HtmlEncode, encodeURIComponent) y ejemplos prácticos de inyecciones.
> **EN:** This room reviews what XSS is, the three main types, the difference between validation, sanitization and encoding, safe functions (sanitizeHtml, htmlspecialchars, HtmlEncode, encodeURIComponent) and practical injection examples.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¡Empecemos! | `No answer needed` |

### Task 2: ¿Qué es el XSS? / What is XSS?
**Explicación:** El almacenamiento persistente en la base de datos se denomina `Stored XSS`, la inyección que se refleja en la respuesta sin almacenarse es `Reflected XSS` y el documento HTML en memoria es el `Document Object Model`. Contenido original de la sala (verbatim): `Stored XSS`, `Reflected XSS`, `Document Object Model`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Almacenar la entrada del usuario en la base de datos del servidor | `Stored XSS` |
| Reflectar la entrada del usuario en la respuesta | `Reflected XSS` |
| La entrada del usuario se lee directamente por JavaScript en el navegador | `Document Object Model` |

### Task 3: Soluciones comunes de desarrollo / Common Alternative Development Solutions
**Explicación:** Una buena protección comienza en el desarrollo: la `validation and sanitization` es el proceso de comprobar y limpiar la entrada del usuario, y `encoding` es el proceso de traducir los caracteres peligrosos a su forma segura. Contenido original de la sala (verbatim): `validation and sanitization`, `encoding`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| El proceso de validar y limpiar la entrada | `validation and sanitization` |
| El proceso de traducir la entrada a una forma segura | `encoding` |

### Task 4: Práctica 1 / Practice 1
**Explicación:** Hay que marcar las líneas problemáticas de los fragmentos de Python: el carácter `&` es de codificación de salida, el carácter `<` forma parte de una payload HTML, `sanitizeHtml()` es una llamada segura y `htmlspecialchars()` es una codificación de salida para escapar HTML. Contenido original de la sala (verbatim): `&`, `<`, `sanitizeHtml()`, `htmlspecialchars()`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| [Código de ejemplo] & | `&` |
| [Código de ejemplo] < | `<` |
| [Código de ejemplo] sanitizeHtml() | `sanitizeHtml()` |
| [Código de ejemplo] htmlspecialchars() | `htmlspecialchars()` |

### Task 5: Práctica 2 / Practice 2
**Explicación:** En el ejemplo, la entrada del usuario se refleja directamente en la URL (sin sanitización ni codificación), por lo que es un caso de `Reflected XSS`; la ruta del fragmento donde vive la vulnerabilidad es `/?h#cc`. Contenido original de la sala (verbatim): `Reflected XSS`, `/?h#cc`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué tipo de XSS es este ejemplo? | `Reflected XSS` |
| ¿Cuál es la ruta del fragmento con vulnereabildad en la URL? | `/?h#cc` |

### Task 6: Práctica 3 / Practice 3
**Explicación:** Los fragmentos seguros: `sanitizeHtml()` para sanitizar la entrada del usuario y `HttpUtility.HtmlEncode()` para codificar la salida en el servidor. Contenido original de la sala (verbatim): `sanitizeHtml()`, `HttpUtility.HtmlEncode()`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Sanitizar la entrada del usuario | `sanitizeHtml()` |
| Codificar la salida (server-side) | `HttpUtility.HtmlEncode()` |

### Task 7: Ejemplo de ataque / Attack Examples
**Explicación:** El ejemplo detecta una inyección persistente: la entrada se almacena en la base de datos y se refleja al resto de usuarios (`Stored XSS`); el vector de ataque es una cookie de sesión, `PHPSESSID`. Contenido original de la sala (verbatim): `Stored XSS`, `PHPSESSID`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué tipo de XSS existe en el ejemplo de ataque? | `Stored XSS` |
| ¿Qué vector de ataque se usa? | `PHPSESSID` |

### Task 8: Buenas prácticas - Encuesta / Best Practices - Survey
**Explicación:** Encuesta de buenas prácticas: la codificación de una entrada ya codificada dos veces no debería protegernos del XSS (`Nay`), el método para evitar la inyección de HTML es codificar la entrada (`Yea`) y para decodificar los caracteres en una URL se usa `encodeURIComponent()`. Contenido original de la sala (verbatim): `Nay`, `Yea`, `encodeURIComponent()`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| [Entrada codificada dos veces] | `Nay` |
| [Método para codificar la entrada] | `Yea` |
| [Método para decodificar caracteres de la URL] | `encodeURIComponent()` |

### Task 9: Buenas prácticas - Resultados de la encuesta / Best Practices - Survey Results
**Explicación:** Tras revisar los resultados de la encuesta sobre las mejores prácticas, la tecla que se debe pulsar para profundizar el control es `Tab`. Contenido original de la sala (verbatim): `Tab`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué tecla debe pulsarse? | `Tab` |

### Task 10: Conclusión / Conclusion
**Explicación:** La vulnerabilidad basada en el propio documento HTML, sin depender del comportamiento del servidor, se denomina `DOM-based XSS`. Contenido original de la sala (verbatim): `DOM-based XSS`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué tipo de XSS es la vulnerabilidad basada en el documento HTML? | `DOM-based XSS` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Empecemos! | `No answer needed` |
| 2 | Almacenar la entrada del usuario en la base de datos | `Stored XSS` |
| 3 | Reflectar la entrada del usuario en la respuesta | `Reflected XSS` |
| 4 | Entrada leída por JavaScript en el navegador | `Document Object Model` |
| 5 | Validar y limpiar la entrada | `validation and sanitization` |
| 6 | Traducir la entrada a una forma segura | `encoding` |
| 7 | Código de ejemplo (&) | `&` |
| 8 | Código de ejemplo (<) | `<` |
| 9 | Código de ejemplo sanitizeHtml() | `sanitizeHtml()` |
| 10 | Código de ejemplo htmlspecialchars() | `htmlspecialchars()` |
| 11 | Tipo de XSS del ejemplo | `Reflected XSS` |
| 12 | Ruta del fragmento vulnerable | `/?h#cc` |
| 13 | Sanitizar la entrada del usuario | `sanitizeHtml()` |
| 14 | Codificar la salida (server-side) | `HttpUtility.HtmlEncode()` |
| 15 | Tipo de XSS del ejemplo de ataque | `Stored XSS` |
| 16 | Vector de ataque usado | `PHPSESSID` |
| 17 | Entrada codificada dos veces | `Nay` |
| 18 | Método para codificar la entrada | `Yea` |
| 19 | Método para decodificar caracteres de la URL | `encodeURIComponent()` |
| 20 | Tecla que debe pulsarse | `Tab` |
| 21 | XSS basado en el documento HTML | `DOM-based XSS` |

---

**Metodología:** Se siguen los tres tipos de XSS (Stored, Reflected, DOM-based), se aplican los principios de validación, sanitización y codificación, se revisan los fragmentos de código de las prácticas (markup, payloads, funciones seguras), se identifican los vectores de ataque (cookies de sesión y fragmentos de URL) y se concluye con la correcta clasificación de cada vulnerabilidad.

### Cadena de ataque / Attack Chain

```text
Stored XSS (base de datos) -> Reflected XSS (respuesta) -> DOM-based XSS (documento HTML) -> validation & sanitization -> encoding -> sanitizeHtml() / htmlspecialchars() / HttpUtility.HtmlEncode() / encodeURIComponent() -> Reflected XSS /?h#cc -> Stored XSS + PHPSESSID -> Nay/Yea/encodeURIComponent -> Tab -> DOM-based XSS
```

**Learning chain:** XSS basics --> stored vs reflected vs DOM-based --> validation/sanitization --> encoding --> safe functions per language --> attack examples (PHPSESSID) --> best practices survey --> DOM based XSS

**Lección:** *El XSS se previene en origen: validar y sanitizar la entrada del usuario y codificar siempre la salida; conocer los tres tipos (Stored, Reflected, DOM-based) permite clasificar e identificar correctamente cada vulnerabilidad.*

**MITRE ATT&CK:** T1189 (Drive-by Compromise) / T1059.007 (JavaScript)

**Fuente:** [TryHackMe - XSS](https://tryhackme.com/room/axss)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.