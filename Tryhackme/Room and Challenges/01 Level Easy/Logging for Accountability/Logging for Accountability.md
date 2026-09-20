# Logging for Accountability

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | loggingforaccountability | [TryHackMe](https://tryhackme.com/room/loggingforaccountability) | 01 Level Easy | THM | non-repudiation, SIEM, Splunk, search head, correlación, wmic | Logging para la rendición de cuentas: non-repudiation, búsquedas en SIEM y correlación de eventos |

---

**Contexto:** Sala centrada en el logging como herramienta de rendición de cuentas (`accountability`). Se cubre el concepto de `non-repudiation`, la estructura de un SIEM clásico (`search head`), los modos de búsqueda `Manual` y `Automated`, la correlación de eventos y ejercicios prácticos de búsqueda sobre Splunk (con `wmic` y varias estadísticas).

> **EN:**
> 1. No answer needed
> 2. non-repudiation
> 3. 1. search head
>    2. 1
> 4. 1. Manual
>    2. Automated
> 5. correlation
> 6. 1. 12,256
>    2. 12,250
>    3. 4
>    4. 5
>    5. wmic
>    6. 3

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta la idea de que los logs sirven también para rendir cuentas: demostrar quién hizo qué y cuándo dentro de un sistema.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Non-repudiation / Non-repudiation

**Explicación:** Se introduce el término que define la imposibilidad de negar una acción realizada, base del logging orientado a la rendición de cuentas.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué concepto impide negar las propias acciones? / Which concept prevents denying one's own actions? | `non-repudiation` |

### Task 3: Estructura de un SIEM / SIEM structure

**Explicación:** Se describe la arquitectura clientes/servidor de un SIEM como Splunk, donde el componente encargado de las búsquedas es el `search head`.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué componente del SIEM realiza las búsquedas? / Which SIEM component performs the searches? | `search head` |
| 2 | ¿Cuántos search heads intervienen en el ejercicio? / How many search heads are involved in the exercise? | `1` |

### Task 4: Modos de búsqueda / Search modes

**Explicación:** Se comparan los dos enfoques de búsqueda de eventos: la búsqueda hecha a mano (`Manual`) y la ejecutada por reglas o programación (`Automated`).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Modo de búsqueda hecho manualmente / Search mode done by hand | `Manual` |
| 2 | Modo de búsqueda ejecutado automáticamente / Search mode executed automatically | `Automated` |

### Task 5: Correlación / Correlation

**Explicación:** Se destaca la operación clave que relaciona eventos aparentemente aislados para construir el contexto de un incidente.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué operación relaciona varios eventos entre sí? / Which operation relates several events to each other? | `correlation` |

### Task 6: Práctica con Splunk / Splunk practice

**Explicación:** Ejercicio práctico: aplicar búsquedas de correlación en Splunk y registrar los volúmenes de eventos (`12,256` y `12,250`), las estadísticas extraídas de los comandos y el binario asociado al hallazgo (`wmic`).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Volumen de eventos de la primera búsqueda / Event volume of the first search | `12,256` |
| 2 | Volumen de eventos de la segunda búsqueda / Event volume of the second search | `12,250` |
| 3 | Estadística numérica 1 del resultado / Numeric statistic 1 of the result | `4` |
| 4 | Estadística numérica 2 del resultado / Numeric statistic 2 of the result | `5` |
| 5 | Binario/conmutador identificado en la búsqueda / Binary/switch identified in the search | `wmic` |
| 6 | Última estadística confirmada del ejercicio / Last statistic confirmed in the exercise | `3` |

---

**Metodología:** Repasar el concepto de `non-repudiation` como objetivo del registro. Identificar los componentes del SIEM (el `search head` como motor de búsqueda). Distinguir la búsqueda `Manual` de la `Automated` y aplicar `correlation` para ligar eventos. En el ejercicio de Splunk se ejecutan las búsquedas indicadas, se anotan los volúmenes de eventos y se interpretan las estadísticas resultantes, fijándose en el uso de `wmic`.

### Cadena de ataque / Attack Chain

Non-repudiation → estructura del SIEM (search head) → modos de búsqueda → correlación → práctica de búsqueda en Splunk → análisis de resultados (wmic)

**Learning chain:** non-repudiation → search head → Manual → Automated → correlation → 12,256 → 12,250 → wmic → 3

**Lección:** *El logging no solo sirve para detectar, sino para rendir cuentas: la `non-repudiation` y la `correlation` de eventos en un SIEM permiten reconstruir la autoría y el orden exacto de las acciones durante un incidente.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1016 (System Network Configuration Discovery), T1047 (Windows Management Instrumentation), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Logging for Accountability](https://tryhackme.com/room/loggingforaccountability)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.