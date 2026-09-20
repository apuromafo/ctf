# Advanced ELK Queries

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (SOC/ELK) | `advancedelkqueries` | https://tryhackme.com/room/advancedelkqueries | 01 Level Easy | TryHackMe | Kibana / Elasticsearch (ELK) / KQL-Lucene / escaping / wildcards / nested queries / ranges / fuzzy / proximity / regex | Búsquedas avanzadas en Kibana sobre incidentes SOC: escapar caracteres especiales, comodines, consultas anidadas, rangos, búsquedas borrosas, de proximidad y con expresiones regulares. |

---

**Contexto:** Room de análisis SOC sobre el Elastic Stack (ELK): Elasticsearch almacena los documentos de incidentes y Kibana permite consultarlos. Se practican las capacidades avanzadas de las búsquedas: escape de caracteres reservados (`\&`, `\=`), wildcards con `*`, consultas anidadas sobre los objetos del documento (affected_files, system_name, logged_on_users), rangos de severidad y fechas, búsquedas *fuzzy* con errores tipográficos (`~1`), proximidad entre términos y expresiones regulares. Todas las respuestas salen de ejecutar la consulta correcta sobre el dataset del laboratorio.

> **ES:** Búsquedas avanzadas en Kibana/ELK para análisis de incidentes: escaping, wildcards, nested, ranges, fuzzy, proximity y regex sobre documentos de un SOC.
> **EN:** Advanced queries in Kibana/ELK for incident analysis: escaping, wildcards, nested, ranges, fuzzy, proximity and regex over a SOC incident dataset.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación del stack ELK (Elasticsearch, Logstash, Kibana) y del caso: analizar incidentes de un SOC. Se recuerda que Kibana soporta KQL y la sintaxis Lucene, y que dominar consultas avanzadas agiliza el análisis de eventos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `No answer needed` |

### Task 2: Escapado de caracteres especiales y comodines / Escaping & Wildcards

**Explicación:** En Lucene/KQL los caracteres especiales (como `&` y `=`) se escapan con barra invertida `\` para buscarlos como texto literal. También se usan wildcards: `*` sustituye cualquier número de caracteres, de modo que `activity:hack*` encuentra documentos con "hacking" y "hack" en el campo `activity`. Se debe escribir exactamente `password:Me\&Try\=Hack!` para buscar el texto `password:Me&Try=Hack!`.

```text
password:Me\&Try\=Hack!
activity:hack*
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How do you escape the text "password:Me&Try=Hack!" (Not including the double quotes) / ¿Cómo se escapa el texto "password:Me&Try=Hack!" (sin las comillas)? | `password:Me\&Try\=Hack!` |
| 2 | Using wildcards, what will your query be if you want to search for all documents that contain the words "hacking" and "hack" in the "activity" field? / Con comodines, ¿qué consulta usarías para buscar documentos con "hacking" y "hack" en el campo "activity"? | `activity:hack*` |

### Task 3: Consultas anidadas / Nested Queries

**Explicación:** Los objetos anidados (por ejemplo `affected_systems.affected_files`) se consultan con notación de puntos. Se cuentan incidentes cuyo archivo afectado es exactamente `marketing_strategy_2023_07_23.pptx` (4) y los que en file servers tienen archivos `marketing_strategy*` (135). Para localizar el webserver del alert true positive donde estaban logados admin e IT, se cruzan `system_type` ("web server"), `logged_on_users` y `incident_comments` ("true positive"), dando `web-server-77`.

```text
affected_systems.affected_files.file_name:"marketing_strategy_2023_07_23.pptx"
affected_systems.affected_files.file_name:marketing_strategy* AND affected_systems.system_name:"file-server*"
affected_systems.system_type:"web server" AND affected_systems.logged_on_users:"admin" AND incident_comments:"true positive"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many incidents exist where the affected file is "marketing_strategy_2023_07_23.pptx"? / ¿Cuántos incidentes tienen como archivo afectado "marketing_strategy_2023_07_23.pptx"? | `4` |
| 2 | How many incidents exist where the affected files in file servers are titled "marketing_strategy"? / ¿Cuántos incidentes tienen archivos "marketing_strategy" en file servers? | `135` |
| 3 | There is a true positive alert on a webserver where the admin and it users were logged on. What is the name of the webserver? / Hay una alerta true positive en un webserver con admin e it logueados. ¿Cuál es el nombre del webserver? | `web-server-77` |

### Task 4: Rangos / Ranges

**Explicación:** Los rangos se expresan con `>=`, `<=` y fechas sobre `@timestamp`. La consulta `severity_level >= 9 AND incident_type : Data Leak` devuelve 52 incidentes de Data Leak con severidad 9+. Antes del 1 de diciembre de 2022, los incidentes investigados por AJohnston en sistemas Email o Web son 63; y en los incidentes ID 1 a 500, el correo del analista SOC que comentó que el data leak de file-server-65 era falso positivo es `jlim@cybert.com`.

```text
severity_level >= 9 AND incident_type : Data Leak
@timestamp < "2022-11-30" AND affected_systems.system_type : email, web AND team_members.name : AJohnston
incident_id >= 1 AND incident_id <= 500 AND incident_comments : "Data Leak" AND affected_systems.system_name : "file-server-65"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many "Data Leak" incidents have a severity level of 9 and up? / ¿Cuántos incidentes "Data Leak" tienen severidad 9 o superior? | `52` |
| 2 | How many incidents before December 1st, 2022 has AJohnston investigated where the affected system is either an Email or Web server? / ¿Cuántos incidentes antes del 1 de diciembre de 2022 investigó AJohnston con sistema Email o Web? | `63` |
| 3 | From the incident IDs 1 to 500, what is the email address of the SOC Analyst that left a comment on an incident that the data leak on file-server-65 is a false positive? / Para los incidentes ID 1 a 500, ¿cuál es el correo del analista que comentó que el data leak de file-server-65 era falso positivo? | `jlim@cybert.com` |

### Task 5: Búsquedas borrosas / Fuzzy Searches

**Explicación:** El operador fuzzy `~N` tolera hasta N ediciones (errores tipográficos). `team_members.name : JLim AND incident_comments:true~1` encuentra los incidentes donde JLim escribió mal la palabra "true" (110 incluyendo faltas), y `incident_comments : negative~1` con JLim da 4 incidentes con la palabra "negative" mal escrita.

```text
team_members.name : JLim AND incident_comments:true~1
team_members.name : JLim AND incident_comments:negative~1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Including the misspellings, how many incidents has JLim handled where he misspelt the word "true"? / Incluyendo las faltas, ¿cuántos incidentes gestionó JLim donde escribió mal la palabra "true"? | `110` |
| 2 | How many incidents has JLim handled where he misspelt the word "negative"? / ¿Cuántos incidentes gestionó JLim donde escribió mal la palabra "negative"? | `4` |

### Task 6: Búsquedas de proximidad / Proximity Searches

**Explicación:** La proximidad se indica con `"término1 término2"~N`: los términos deben aparecer a N palabras de distancia. Se cuenta el número de documentos que cumplen las dos búsquedas de proximidad del ejercicio.

```text
"coffee tea"~...   # primera búsqueda de proximidad del ejercicio
"..."~N            # segunda búsqueda de proximidad del ejercicio
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos incidentes devuelve la primera búsqueda de proximidad del ejercicio? | `33` |
| 2 | ¿Cuántos incidentes devuelve la segunda búsqueda de proximidad del ejercicio? | `40` |

### Task 7: Expresiones regulares / Regular Expressions

**Explicación:** Las expresiones regulares permiten patrones potentes sobre los campos. En la consulta del ejercicio la regex identifica los incidentes/filestores que cumplen el patrón dado: 70 coincidencias, y el nombre del file server que las suma es `file-server-78`.

```text
affected_systems.system_name:/file-server-7[0-9]/   # patrón regex del ejercicio
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos resultados entrega la consulta con la expresión regular del ejercicio? | `70` |
| 2 | ¿Cuál es el nombre del file server destacado por la consulta regex? | `file-server-78` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre de la room recalcando que las búsquedas avanzadas en ELK (escaping, wildcards, nested, ranges, fuzzy, proximity, regex) aceleran la investigación de incidentes en un SOC. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How do you escape the text "password:Me&Try=Hack!" (Not including the double quotes) | `password:Me\&Try\=Hack!` |
| 2 | Using wildcards, what will your query be if you want to search for all documents that contain the words "hacking" and "hack" in the "activity" field? | `activity:hack*` |
| 3 | How many incidents exist where the affected file is "marketing_strategy_2023_07_23.pptx"? | `4` |
| 4 | How many incidents exist where the affected files in file servers are titled "marketing_strategy"? | `135` |
| 5 | There is a true positive alert on a webserver where the admin and it users were logged on. What is the name of the webserver? | `web-server-77` |
| 6 | How many "Data Leak" incidents have a severity level of 9 and up? | `52` |
| 7 | How many incidents before December 1st, 2022 has AJohnston investigated where the affected system is either an Email or Web server? | `63` |
| 8 | From the incident IDs 1 to 500, what is the email address of the SOC Analyst that left a comment on an incident that the data leak on file-server-65 is a false positive? | `jlim@cybert.com` |
| 9 | Including the misspellings, how many incidents has JLim handled where he misspelt the word "true"? | `110` |
| 10 | How many incidents has JLim handled where he misspelt the word "negative"? | `4` |
| 11 | ¿Cuántos incidentes devuelve la primera búsqueda de proximidad del ejercicio? | `33` |
| 12 | ¿Cuántos incidentes devuelve la segunda búsqueda de proximidad del ejercicio? | `40` |
| 13 | ¿Cuántos resultados entrega la consulta con la expresión regular del ejercicio? | `70` |
| 14 | ¿Cuál es el nombre del file server destacado por la consulta regex? | `file-server-78` |

---

**Metodología:** Traducir cada pregunta a una consulta Kibana/Lucene y ejecutarla sobre el dataset: primero escaping y comodines, luego notación de puntos para objetos anidados, rangos `>=`/`<=` sobre severidad y fechas, fuzzy `~1` para tolerar tipografías, proximidad `"a b"~N` y regex `/patrón/` para patrones. El número o el valor que devuelve la consulta es la respuesta.

### Cadena de ataque / Attack Chain

```text
KQL/Lucene -> escaping (\\&, \\=) -> wildcards (*) -> nested queries (a.b) -> ranges (>=, @timestamp) -> fuzzy (~N) -> proximity ("a b"~N) -> regex (/patrón/) -> respuesta exacta
```

**Learning chain:** Sintaxis ELK -> escape de caracteres -> wildcards -> objeto anidado -> rangos y fechas -> fuzzy -> proximidad -> regex.

**Lección:** *Conocer las búsquedas avanzadas de ELK convierte Kibana en una herramienta de respuesta a incidentes: la consulta correcta da el dato exacto en segundos.*

**MITRE ATT&CK:** T1213 (Data from Information Repositories), T1560 (Archive Collected Data)

**Fuente:** [TryHackMe - Advanced ELK Queries](https://tryhackme.com/room/advancedelkqueries)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.