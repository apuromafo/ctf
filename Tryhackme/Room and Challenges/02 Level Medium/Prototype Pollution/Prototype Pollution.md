# Prototype Pollution

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teoría + Laboratorio / Theory + Lab | prototypepollution | https://tryhackme.com/room/prototypepollution | 02 Level Medium | TryHackMe | JavaScript, `__proto__`, Server-Side JS, Bibliotecas (lodash), Análisis de dependencias | Inyección de propiedades, manipulación de datos y flags de explotación |

---

**Contexto:** La sala **Prototype Pollution** explica y explota la vulnerabilidad de JavaScript que permite inyectar propiedades a través de `__proto__`. El laboratorio parte de una introducción (sin respuesta), continúa contaminando el prototipo para alterar valores mostrados en la aplicación, abusa de bibliotecas vulnerables como `lodash`, provoca crash/sobreescritura de estados y finaliza con preguntas teóricas sobre detección (estática y análisis de dependencias).

## Solucionario

### Task 1: Preparación / Preparation
**Explicación:**

Tarea de arranque de la sala; no requiere respuesta, solo lectura del material introductorio.

Respuesta: `No answer needed`

### Task 2: Polución básica del prototipo / Basic prototype pollution
**Explicación:**

Se intercepta y modifica la petición para contaminar el prototipo del objeto: el valor de edad mostrado cambia a 25, el saludo pasa a `Hello, Ben S!` y el resultado numérico de la operación es 4.

1. `25`
2. `Hello, Ben S!`
3. `4`

### Task 3: Polución en el navegador / Polluting the browser
**Explicación:**

Se poluciona el objeto del navegador para reemplazar el mensaje mostrado por `You've been hacked, I'm Bob`, usando la clave reservada `__proto__`.

1. `You've been hacked, I'm Bob`
2. `__proto__`

### Task 4: Biblioteca vulnerable / Vulnerable library
**Explicación:**

Se identifica la biblioteca JavaScript vulnerable (`lodash`) y el índice/campo usado para desencadenar la contaminación (`i`).

1. `lodash`
2. `i`

### Task 5: Propiedad inyectada y flag / Injected property and flag
**Explicación:**

La propiedad inyectada deja la aplicación en estado `hacked`, activada por el parámetro `b`, y se obtiene la flag que acredita el `FAKEPROPERTY_ADDED`.

1. `hacked`
2. `b`
3. `THM{FAKEPROPERTY_ADDED}`

### Task 6: Crash y sobreescritura / Crash and override
**Explicación:**

La explotación provoca dos flags: la primera asociada al crash de la aplicación y la segunda a la sobrescritura (override) del comportamiento esperado.

1. `THM{CRA5H#D)`
2. `THM{OV3RRID3}`

### Task 7: Confirmación / Confirmation
**Explicación:**

Respuesta afirmativa de confirmación sobre el comportamiento observado en el laboratorio.

Respuesta: `yea`

### Task 8: Detección del patrón / Pattern detection
**Explicación:**

Pregunta teórica sobre el enfoque/método de detección de esta vulnerabilidad; la respuesta es el análisis de dependencias y explotación.

Respuesta: `Dependency Analysis and Exploitation`

### Task 9: Cierre / Closing
**Explicación:**

Tarea final de cierre sin respuesta requerida.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de preparación inicial | `No answer needed` |
| 2.1 | Valor mostrado tras la polución (edad) | `25` |
| 2.2 | Saludo mostrado tras la polución | `Hello, Ben S!` |
| 2.3 | Resultado numérico tras la polución | `4` |
| 3.1 | Mensaje inyectado en la página | `You've been hacked, I'm Bob` |
| 3.2 | Clave reservada utilizada | `__proto__` |
| 4.1 | Biblioteca vulnerable | `lodash` |
| 4.2 | Índice/campo usado para la polución | `i` |
| 5.1 | Estado de la aplicación tras la inyección | `hacked` |
| 5.2 | Parámetro que activa la propiedad | `b` |
| 5.3 | Flag de la propiedad inyectada | `THM{FAKEPROPERTY_ADDED}` |
| 6.1 | Flag asociada al crash | `THM{CRA5H#D)` |
| 6.2 | Flag asociada al override | `THM{OV3RRID3}` |
| 7 | ¿Se confirma el comportamiento observado? | `yea` |
| 8 | ¿Qué enfoque/método detecta el patrón? | `Dependency Analysis and Exploitation` |
| 9 | Tarea final de cierre | `No answer needed` |

---

**Metodología:** Interceptación de peticiones, inyección de propiedades vía `__proto__`, explotación de bibliotecas vulnerables (lodash) y combinación de análisis estático y de dependencias para detectar y explotar la contaminación de prototipos.

### Cadena de ataque / Attack Chain

```
Petición interceptada (proxy)
        │
        ▼
Inyección de __proto__ sobre el objeto
        │
        ▼
Alteración de valores (edad/saludo) y estado (hacked)
        │
        ▼
Abuso de biblioteca vulnerable (lodash, índice "i")
        │
        ▼
Crash / override → flags
```

**Learning chain:** Intercepción → polución de prototipo → alteración de estado → dependencias → explotación → flags.

**Lección:** *La contaminación de prototipos convierte la manipulación de claves reservadas (`__proto__`) en control del estado de la aplicación; las bibliotecas de merge/copy deben validar qué claves se aceptan.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059.007 Command and Scripting Interpreter (JavaScript) · T1596.002 DNS (reconocimiento de dependencias).

**Fuente:** [TryHackMe - Prototype Pollution](https://tryhackme.com/room/prototypepollution)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.