# How Websites Work

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `howwebsiteswork` | https://tryhackme.com/room/howwebsiteswork | 01 Level Easy | TryHackMe | Front End / HTML / JavaScript / View Source / datos sensibles / inyección HTML | Fundamentos del funcionamiento web: estructura, scripts en el cliente y exposición de datos sensibles. |

---

**Contexto:** Sala de fundamentos web que explica cómo funcionan los sitios web: el front-end que se ejecuta en el navegador, HTML como lenguaje de estructura, JavaScript para la interactividad, la exposición de datos sensibles en el código fuente y la inyección de HTML como primer contacto con las vulnerabilidades web.

> **ES:** Aprende la base del funcionamiento web (front-end, HTML, JavaScript) y practica localizando datos expuestos y explotando inyección de HTML.
> **EN:** Learn the basics of how websites work (front-end, HTML, JavaScript) and practise finding exposed data and exploiting HTML injection.

## Solucionario

### Task 1: Cómo funcionan las webs / How Websites Work

**Explicación:** Se explica que una web tiene dos partes: el front-end (una de las partes se ejecuta en el navegador) y el back-end (se ejecuta en el servidor).

1. 1. Front End

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué parte de la web se ejecuta en el navegador? / What part of the website runs in the browser? | `Front End` |

### Task 2: HTML

**Explicación:** Con el View Source se examina la página de práctica y se modifican el título y los elementos HTML siguiendo las indicaciones de la tarea.

1. 1. No answer needed
   2. HTMLHERO
   3. DOGHTML

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre el editor de la tarea y revisa el código. | `No answer needed` |
| 2 | Cambia el título de la página al indicado. | `HTMLHERO` |
| 3 | Añade un elemento DOG con el texto indicado. | `DOGHTML` |

### Task 3: JavaScript

**Explicación:** Se añade una función en JavaScript que muestra el texto solicitado cuando se interactúa con la página.

1. 1. JSISFUN
   2. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Añade la función JavaScript que muestra el texto indicado. | `JSISFUN` |
| 2 | Comprueba el resultado en el navegador. | `No answer needed` |

### Task 4: Exposición de datos sensibles / Sensitive Data Exposure

**Explicación:** Los desarrolladores deben ser cuidadosos con los datos sensibles; aquí la contraseña está expuesta de forma visible dentro de la propia página.

1. 1. testpasswd

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña expuesta en la web? / What is the password exposed on the website? | `testpasswd` |

### Task 5: Inyección de HTML / HTML Injection

**Explicación:** Se prueba la inyección de HTML frente al formulario de la página de práctica, consiguiendo la flag del reto.

1. 1. HTML_INJ3CTI0N

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la inyección de HTML? / What is the HTML injection flag? | `HTML_INJ3CTI0N` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | ¿Qué parte de la web se ejecuta en el navegador? / What part of the website runs in the browser? | `Front End` |
| 2 | 1 | Abre el editor de la tarea y revisa el código. | `No answer needed` |
| 2 | 2 | Cambia el título de la página al indicado. | `HTMLHERO` |
| 2 | 3 | Añade un elemento DOG con el texto indicado. | `DOGHTML` |
| 3 | 1 | Añade la función JavaScript que muestra el texto indicado. | `JSISFUN` |
| 3 | 2 | Comprueba el resultado en el navegador. | `No answer needed` |
| 4 | 1 | ¿Cuál es la contraseña expuesta en la web? / What is the password exposed on the website? | `testpasswd` |
| 5 | 1 | ¿Cuál es la flag de la inyección de HTML? / What is the HTML injection flag? | `HTML_INJ3CTI0N` |

---

**Metodología:** Uso del View Source y de las DevTools del navegador para inspeccionar HTML y JavaScript, modificación controlada de los elementos de la página de práctica, identificación de la contraseña expuesta en el código y prueba de inyección de HTML contra el formulario para obtener la flag.

### Cadena de ataque / Attack Chain

```text
view-source -> inspección HTML -> JavaScript -> datos expuestos (testpasswd) -> inyección HTML -> flag
```

**Learning chain:** Web Fundamentals -> Front End -> HTML -> JavaScript -> Sensitive Data Exposure -> HTML Injection.

**Lección:** *Los datos sensibles nunca deben almacenarse en el código fuente del lado del cliente; además, validar y sanitizar la entrada del usuario evita la inyección de HTML y de otros contenidos.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - How Websites Work](https://tryhackme.com/room/howwebsiteswork)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
