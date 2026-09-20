# KQL (Kusto)_ Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `kqlkustointroduction` | [TryHackMe](https://tryhackme.com/room/kqlkustointroduction) | 01 Level Easy | TryHackMe | KQL / Kusto Query Language, Sentinel, Azure Data Explorer, where, render, contains, SecurityEvent | Introducción al lenguaje de consultas Kusto y su uso en SIEM/SOAR para buscar y visualizar datos de seguridad. |

---

**Contexto:** La sala presenta el lenguaje de consultas Kusto (KQL) en el contexto de los productos de Microsoft (Sentinel y Azure Data Explorer). Se explican los bloques de construcción (tablas, columnas), los operadores de filtrado (`where`, `contains`), la búsqueda de textos en escenarios de seguridad (intentos de inicio de sesión fallidos) y la visualización de datos con `render`.

> **ES:** Fundamentos de KQL: qué es, dónde se ejecuta (Azure Data Explorer/Sentinel), operadores para filtrar y buscar (where, contains, search) y visualización de resultados con render sobre la tabla SecurityEvent.
> **EN:** KQL fundamentals: what it is, where it runs (Azure Data Explorer/Sentinel), operators to filter and search (where, contains, search) and rendering results with render over the SecurityEvent table.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Tarea introductoria que sitúa la sala. No requiere respuesta.

```text
1. No answer needed
```

### Task 2: SOAR y REST API / SOAR and REST API
**Explicación:** Se introducen los conceptos de SOAR (Security Orchestration, Automation and Response) y cómo las herramientas se integran mediante REST API para automatizar las tareas de respuesta.

```text
2. 1. SOAR
   2. REST API Integration
```

### Task 3: Azure Data Explorer / Azure Data Explorer
**Explicación:** Se identifica el motor de consultas principal de KQL (Azure Data Explorer), el límite de resultados de una consulta (10) y la tabla de latido `Heartbeat` utilizada en los ejemplos de monitorización.

```text
3. 1. Azure Data Explorer
   2. 10
   3. Heartbeat
```

### Task 4: render y where / render and where
**Explicación:** Se emplea el operador `render` para visualizar los resultados y `where` para filtrar las filas por máquina (`JBOX00$`).

```text
4. 1. render
   2. where
   3. JBOX00$
```

### Task 5: Tabla SecurityEvent / SecurityEvent table
**Explicación:** Se consulta la tabla `SecurityEvent` (eventos de seguridad de Windows) y se usa la columna `EventCount` para contar el número de registros.

```text
5. 1. SecurityEvent
   2. EventCount
```

### Task 6: Búsqueda de intentos fallidos / Failed login attempts
**Explicación:** Se busca la cadena "failed login attempts" con el operador `contains`, que comprueba si un valor de la columna contiene la subcadena indicada.

```text
6. 1. failed login attempts
   2. Contains
```

### Task 7: Conclusión / Conclusion
**Explicación:** Tarea final de repaso. No requiere respuesta.

```text
7. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Tarea introductoria | `No answer needed` |
| 2 | Orquestación, automatización y respuesta | `SOAR` |
| 2 | Integración de herramientas | `REST API Integration` |
| 3 | Motor de consultas de KQL | `Azure Data Explorer` |
| 3 | Límite de resultados de la consulta | `10` |
| 3 | Tabla de monitorización | `Heartbeat` |
| 4 | Operador de visualización | `render` |
| 4 | Operador de filtrado de filas | `where` |
| 4 | Máquina de la que se extrae la información | `JBOX00$` |
| 5 | Tabla de eventos de seguridad | `SecurityEvent` |
| 5 | Columna de recuento de eventos | `EventCount` |
| 6 | Cadena buscada | `failed login attempts` |
| 6 | Operador de búsqueda de subcadena | `Contains` |
| 7 | Conclusión | `No answer needed` |

---

**Metodología:** Se explican las bases de KQL y su ecosistema (Sentinel, Azure Data Explorer), se revisan los operadores de filtrado y búsqueda (`where`, `contains`) y se practica la consulta sobre `SecurityEvent` con visualización (`render`) para un caso de intentos de inicio de sesión fallidos.

### Cadena de ataque / Attack Chain

```text
Entendimiento de KQL -> Sentinel/Azure Data Explorer -> selección de tabla (SecurityEvent/Heartbeat) -> filtrado con where -> búsqueda con contains -> recuento con EventCount -> visualización con render -> extracción de respuestas
```

**Learning chain:** KQL -> SOAR/REST API -> Azure Data Explorer -> where -> render -> SecurityEvent -> EventCount -> contains -> failed login attempts

**Lección:** *KQL es el puente entre los datos crudos de seguridad y las respuestas investigativas: conocer los operadores de filtrado (`where`, `contains`) y la visualización (`render`) permite convertir registros en conclusiones.*

**MITRE ATT&CK:** T1078 - Valid Accounts, T1110 - Brute Force (detección de intentos de autenticación fallidos)

**Fuente:** [TryHackMe - KQL (Kusto)_ Introduction](https://tryhackme.com/room/kqlkustointroduction)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.