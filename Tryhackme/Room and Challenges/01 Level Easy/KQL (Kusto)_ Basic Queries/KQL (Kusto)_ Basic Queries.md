# KQL (Kusto)_ Basic Queries

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `kqlkustobasicqueries` | [TryHackMe](https://tryhackme.com/room/kqlkustobasicqueries) | 01 Level Easy | TryHackMe | KQL / Kusto Query Language, Windows Event Logs, SecurityEvent, where, search, let, now() | Introducción a las consultas KQL para filtrar y analizar logs de eventos de Windows (inicio de sesión fallido, cierre de sesión y privilegios especiales). |

---

**Contexto:** La sala introduce el lenguaje de consultas Kusto (KQL) aplicado al esquema `SecurityEvent` de los logs de Windows. Se aprenden los operadores básicos de filtrado y búsqueda, la declaración de variables con `let`, y se practican consultas sobre eventos de autenticación como el 4625 (inicio de sesión fallido), el 4634 (cierre de sesión) y el 4672 (privilegios especiales asignados a un nuevo inicio de sesión).

> **ES:** Consultas KQL básicas sobre la tabla SecurityEvent: filtrar por tiempo y proceso, usar search/_CL, definir variables con let y responder preguntas sobre eventos de logon/logoff (4625, 4634, 4672 y el tipo de autenticación Kerberos).
> **EN:** Basic KQL queries against the SecurityEvent table: filter by time and process, use search/_CL, define variables with let and answer questions about logon/logoff events (4625, 4634, 4672 and the Kerberos authentication type).

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Tarea introductoria de la sala, de carácter teórico. No requiere respuesta.

```text
1. No answer needed
```

### Task 2: Filtrado de datos / Filtering data
**Explicación:** Se presenta el concepto de filtrado de datos en KQL. La respuesta corresponde al nombre de la técnica utilizada para restringir los resultados de una consulta.

```text
2. Filtering data
```

### Task 3: Últimas 24 horas / Last 24 hours
**Explicación:** Se aprende a filtrar los resultados por ventana de tiempo (últimas 24 horas) y a seleccionar el campo de proceso (`ProcessName`) dentro de la tabla de eventos de seguridad.

```text
3. 1. Last 24 hours
   2. ProcessName
```

### Task 4: Búsqueda global / search and _CL
**Explicación:** Se utiliza el operador `search` para buscar en todas las tablas y columnas, y se usa `_CL` para hacer referencia a la tabla de logs personalizados.

```text
4. 1. search
   2. _CL
```

### Task 5: Declaración de variables / let statement
**Explicación:** Se emplea la sentencia `let` para definir variables que reutilizan valores dentro de la consulta KQL.

```text
5. Let
```

### Task 6: Evento 4625 / Logon failure event
**Explicación:** Se consulta el evento 4625 (inicio de sesión fallido) y se usa la función `now()` para referirse al momento actual en el filtro temporal.

```text
6. 1. 4625
   2. now()
```

### Task 7: Verificación del incidente / Checking the incident
**Explicación:** Se confirma (Yea) que el usuario aparece en el evento de logon fallido y se identifican las columnas implicadas del registro: `Process`, `Computer` y `AccountType`.

```text
7. 1. Yea
   2. Process, Computer, AccountType
```

### Task 8: Análisis de contexto / Context analysis
**Explicación:** Tarea de análisis intermedia en la que no se requiere respuesta.

```text
8. No answer needed
```

### Task 9: Eventos de cierre y privilegios / Logoff and privileges
**Explicación:** Se identifica el evento 4634 (cierre de sesión), el evento 4672 (privilegios especiales asignados a un nuevo inicio de sesión), el índice 21 y el tipo de autenticación Kerberos.

```text
9. 1. 4634
   2. 4672 - Special privileges assigned to new logon
   3. 21
   4. Kerberos
```

### Task 10: Conclusión / Conclusion
**Explicación:** Tarea final de repaso de los conceptos vistos. No requiere respuesta.

```text
10. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Tarea introductoria | `No answer needed` |
| 2 | Filtrado de datos | `Filtering data` |
| 3 | Filtrar las últimas 24 horas | `Last 24 hours` |
| 3 | Campo de proceso | `ProcessName` |
| 4 | Operador de búsqueda global | `search` |
| 4 | Referencia a logs personalizados | `_CL` |
| 5 | Declaración de variable | `Let` |
| 6 | Evento de inicio de sesión fallido | `4625` |
| 6 | Momento actual | `now()` |
| 7 | ¿Aparece el evento tras el filtrado? | `Yea` |
| 7 | Columnas del evento | `Process, Computer, AccountType` |
| 8 | Análisis de contexto | `No answer needed` |
| 9 | Evento de cierre de sesión | `4634` |
| 9 | Evento 4672 | `4672 - Special privileges assigned to new logon` |
| 9 | Índice / número del evento | `21` |
| 9 | Tipo de autenticación | `Kerberos` |
| 10 | Conclusión | `No answer needed` |

---

**Metodología:** Se repasan los operadores básicos de KQL (`where`, `search`, `let`, `now()`) y se practica la consulta sobre la tabla `SecurityEvent` para filtrar por tiempo y proceso, localizar los eventos de interés (4625, 4634, 4672) y responder las preguntas del incidente de autenticación.

### Cadena de ataque / Attack Chain

```text
Acceso al workspace KQL -> tabla SecurityEvent -> filtrado temporal (últimas 24 horas) -> where/ProcessName -> search/_CL -> let -> análisis de eventos 4625/4634/4672 -> identificación de Kerberos -> conclusión
```

**Learning chain:** KQL -> where -> time filter -> ProcessName -> search/_CL -> let -> SecurityEvent -> 4625/4634/4672 -> now() -> Kerberos

**Lección:** *KQL permite responder preguntas forenses sobre logs de Windows combinando filtros temporales, selección de columnas y la identificación de eventos concretos (4625, 4634, 4672) sin salir del esquema SecurityEvent.*

**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter, T1078 - Valid Accounts (análisis de eventos de autenticación)

**Fuente:** [TryHackMe - KQL (Kusto)_ Basic Queries](https://tryhackme.com/room/kqlkustobasicqueries)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.