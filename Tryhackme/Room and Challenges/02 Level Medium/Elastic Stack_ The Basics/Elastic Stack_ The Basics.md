# Elastic Stack_ The Basics

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `elasticstackthebasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/elasticstackthebasics) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Elastic Stack / Elasticsearch / Logstash / Kibana / Beats / SIEM / consultas |
| **Impacto** | Fundamentos de Elastic Stack como SIEM: ingesta de datos, búsquedas en Kibana y localización de eventos concretos en los logs |

---

**Contexto:** La sala introduce los componentes de Elastic Stack (Elasticsearch, Logstash, Kibana y Beats) y su uso como SIEM: ingesta de logs, indexación en Elasticsearch y búsquedas en Kibana (Discover). Los ejercicios prácticos piden localizar eventos concretos en los datos almacenados (conteos de eventos, IPs, usuarios, timestamps) mediante consultas sobre el entorno Kibana desplegado.

## Solucionario

### Task 1: Introducción al Elastic Stack

**Explicación:** Tarea introductoria que presenta los componentes del stack (Beats, Logstash, Elasticsearch, Kibana) y el caso de uso como SIEM. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a los componentes del Elastic Stack | `No answer needed` |

### Task 2: Conceptos iniciales

**Explicación:** Primera ronda de preguntas conceptuales sobre la arquitectura del stack: las dos respuestas de esta tarea son **nay** (negativas). Se validan los conceptos de ingesta y tratamiento de datos explicados en la lectura previa.

1. nay
2. nay

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Es correcta la afirmación planteada? | `nay` |
| 2 | ¿Es correcta la segunda afirmación planteada? | `nay` |

### Task 3: Uso del entorno

**Explicación:** Tarea práctica de familiarización con el entorno Kibana desplegado. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Familiarización con el entorno Kibana | `No answer needed` |

### Task 4: Búsquedas en los datos

**Explicación:** Utilizando las búsquedas de Kibana sobre el dataset se responden las preguntas: **2861** (conteo de eventos), **238.163.231.224** (IP relacionada), el usuario **James**, y las IPs **107.14.1.247** y **172.201.60.191**, junto con el valor **48**. La última sub-pregunta es informativa.

1. 2861
2. 238.163.231.224
3. James
4. 107.14.1.247
5. 172.201.60.191
6. 48
7. (informativo)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué conteo de eventos se obtiene? | `2861` |
| 2 | ¿Qué IP se reporta en la búsqueda? | `238.163.231.224` |
| 3 | ¿Qué usuario aparece en los resultados? | `James` |
| 4 | ¿Qué otra IP se reporta? | `107.14.1.247` |
| 5 | ¿Qué IP adicional se reporta? | `172.201.60.191` |
| 6 | ¿Qué valor/cantidad se obtiene? | `48` |
| 7 | Sub-pregunta informativa | `No answer needed` |

### Task 5: Identificadores de eventos

**Explicación:** Las búsquedas sobre los eventos devuelven el identificador **161** y el valor **1** como respuestas de esta tarea.

1. 161
2. 1

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué identificador/valor se obtiene? | `161` |
| 2 | ¿Qué valor se reporta en la segunda búsqueda? | `1` |

### Task 6: Usuarios y contadores

**Explicación:** En los resultados de esta tarea aparece el usuario **Simon** y el valor **274**, que completan el análisis de eventos solicitado.

1. Simon
2. 274

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuario se reporta? | `Simon` |
| 2 | ¿Qué valor se reporta? | `274` |

### Task 7: Ejercicio adicional

**Explicación:** Tarea de ejercicio adicional de búsquedas en los datos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejercicio adicional | `No answer needed` |

### Task 8: Cierre

**Explicación:** Tarea de cierre de la sala con repaso de los conceptos de Elastic Stack. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala | `No answer needed` |

---

**Metodología:**

1. Desplegar el entorno del stack y comprender el flujo Beats -> Logstash -> Elasticsearch -> Kibana.
2. Comprobar la ingesta de datos en Elasticsearch y su indexación.
3. Usar el Discover de Kibana para construir consultas y filtrar eventos.
4. Responder las preguntas localizando conteos, IPs, usuarios e identificadores en los resultados.
5. Verificar cada respuesta contra los datos devueltos por el entorno.

**Learning chain:** Beats -> Logstash -> Elasticsearch -> Kibana -> Consultas (Discover) -> Conteo de eventos -> IPs/usuarios -> Identificadores -> Respuestas

**Lección:** *Un SIEM basado en Elastic Stack permite almacenar, indexar y buscar cualquier tipo de log sin esquema previo: Kibana convierte los datos crudos en respuestas operativas.*

**MITRE ATT&CK:** N/A (fundamentos SIEM / blue team, no una técnica ofensiva)

**Fuente:** [TryHackMe - Elastic Stack_ The Basics](https://tryhackme.com/room/elasticstackthebasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.