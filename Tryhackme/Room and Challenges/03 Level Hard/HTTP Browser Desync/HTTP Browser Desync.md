# HTTP Browser Desync

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Web | requestsmugglingbrowserdesync | [HTTP Browser Desync](https://tryhackme.com/room/requestsmugglingbrowserdesync) | 03 Level Hard | TryHackMe | Conceptos Web, Flag | Alto |

---

**Contexto:**

> **ES:** Room sobre desincronización de peticiones HTTP (browser desync) y contrabando de requests. Se exploran HTTP Pipelining, Keep-Alive, el rol del navegador, el número de peticiones, `fetch`, CORS, XSS y el contrabando de peticiones hasta obtener la flag.
> **EN:** Room about HTTP request desynchronisation (browser desync) and request smuggling. It covers HTTP Pipelining, Keep-Alive, the browser's role, the number of requests, `fetch`, CORS, XSS and request smuggling until the flag is obtained.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:**

El contenido original de la tarea es el siguiente:

1. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

### Task 2: Pipelining y Keep-Alive / Pipelining and Keep-Alive

**Explicación:**

El contenido original de la tarea es el siguiente:

2. 1. Pipelining
   2. Keep-Alive

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 2 | ¿Qué técnica envía múltiples peticiones sin esperar respuesta? / Which technique sends multiple requests without waiting for a response? | `Pipelining` |
| 2 | ¿Qué cabecera mantiene viva la conexión? / What header keeps the connection alive? | `Keep-Alive` |

### Task 3: Rol del navegador / Browser role

**Explicación:**

El contenido original de la tarea es el siguiente:

3. 1. Browser
   2. Three

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 3 | ¿Qué componente clave interviene en la desincronización? / What key component is involved in the desync? | `Browser` |
| 3 | ¿Cuántas peticiones están involucradas? / How many requests are involved? | `Three` |

### Task 4: Fetch y CORS / Fetch and CORS

**Explicación:**

El contenido original de la tarea es el siguiente:

4. 1. fetch
   2. CORS

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 4 | ¿Qué API de JavaScript se utiliza para lanzar las peticiones? / What JavaScript API is used to fire the requests? | `fetch` |
| 4 | ¿Qué política debe validarse para el cruce de orígenes? / What policy must be validated for cross-origin requests? | `CORS` |

### Task 5: Ataque con XSS / XSS attack

**Explicación:**

El contenido original de la tarea es el siguiente:

5. XSS

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 5 | ¿Qué tipo de ataque se encadena con la desincronización? / What type of attack is chained with the desync? | `XSS` |

### Task 6: Flag del contrabando / Smuggling flag

**Explicación:**

El contenido original de la tarea es el siguiente:

6. THM{SMUGGLING_IS_FUN}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 6 | ¿Cuál es la flag del contrabando de peticiones? / What is the request smuggling flag? | `THM{SMUGGLING_IS_FUN}` |

### Task 7: Concepto adicional / Additional concept

**Explicación:**

El contenido original de la tarea es el siguiente:

7. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 7 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

### Task 8: Síntesis / Synthesis

**Explicación:**

El contenido original de la tarea es el siguiente:

8. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 8 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

---

**Metodología:**

Estudio de HTTP Pipelining y Keep-Alive, análisis de la desincronización cliente-servidor provocada por el navegador, construcción de peticiones con `fetch`, evasión de CORS y encadenamiento con XSS para lograr el contrabando de peticiones.

### Cadena de ataque / Attack Chain

1. Comprensión de HTTP Pipelining y Keep-Alive como base del desync.
2. Identificación del navegador y las tres peticiones que provocan la confusión de conexiones.
3. Lanzamiento de peticiones mediante `fetch` respetando CORS.
4. Encadenamiento con XSS para consumir la respuesta del contrabando.
5. Obtención de la flag final.

**Learning chain:**

`HTTP Pipelining` → `Keep-Alive` → `Browser` → `Three` → `fetch` → `CORS` → `XSS` → `THM{SMUGGLING_IS_FUN}`.

**Lección:** *La diferencia entre cómo el navegador y el servidor interpretan el fin de una petición crea ventanas de desincronización: un único navegador comprometido puede convertirse en un proxy para contrabandear peticiones contra el servidor.*

**MITRE ATT&CK:** T1557 Adversary-in-the-Middle, T1189 Drive-by Compromise, T1204.001 User Execution: Malicious Link, T1505.003 Web Shell.

**Fuente:** [TryHackMe - HTTP Browser Desync](https://tryhackme.com/room/requestsmugglingbrowserdesync)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.