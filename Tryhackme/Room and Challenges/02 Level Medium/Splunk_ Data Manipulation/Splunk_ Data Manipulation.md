# Splunk_ Data Manipulation
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `splunkdatamanipulation` |
| **Link** | [TryHackMe](https://tryhackme.com/room/splunkdatamanipulation) |
| **Sección** | Blue Team / SIEM / Splunk |
| **Fuente** | TryHackMe |
| **Componentes** | Splunk, props.conf, transforms.conf, inputs.conf, LINE_BREAKER, breakers, SEDCMD, regex, apps |
| **Impacto** | Domina la manipulación de datos en Splunk: configuración de ficheros de app (props/transforms/inputs), rotura de eventos, extracción de campos y transformaciones con regex. |
---
**Contexto:** Splunk ingiere datos en bruto y los divide en eventos mediante reglas de **event breaking**, definidas en ficheros de configuración de las apps. Esta room profundiza en la manipulación de datos: `inputs.conf` (qué y cómo se ingiere), `props.conf` (rotura de líneas, timestamps, transformaciones) y `transforms.conf` (expresiones regulares, lookups). Se practican directivas como `LINE_BREAKER`, `BREAK_ONLY_BEFORE`, `BREAK_ONLY_AFTER`, `MUST_BREAK_AFTER` y `SEDCMD`, junto con la estructura de directorios de una app Splunk.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de los objetivos: comprender cómo Splunk manipula los datos en el momento de la ingesta. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: App Structure / Estructura de una app
**Explicación:** Una app de Splunk se organiza en directorios (`bin`, `default`, `local`, `lookups`, `metadata`). Se observa el número de apps/ficheros de configuración del entorno de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Observation about the app structure (no answer required). | `No answer needed` |
| 2. What is the observed count? | `3` |
### Task 3: Configuration Files / Ficheros de configuración
**Explicación:** Repaso de los ficheros de configuración clave: `inputs.conf`, `props.conf` y `transforms.conf`, y su prioridad (`default` vs `local`). Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Ficheros de configuración de Splunk (sin preguntas). | `No answer needed` |
### Task 4: Event Breaking / Rotura de eventos
**Explicación:** Directivas de rotura de eventos: `BREAK_ONLY_AFTER` (crea un evento nuevo tras el patrón), `LINE_BREAKER` (regex que define el límite de línea/evento). Los cambios de parsing se aplican en **transforms.conf** (transformaciones/regex) y en **inputs.conf** (definición de la fuente/datos de entrada).
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Which directive creates a new event after the pattern? | `BREAK_ONLY_AFTER` |
| 2. Which setting defines the regex used to break lines/events? | `LINE_BREAKER` |
| 3. In which file are transforms defined? | `transforms.conf` |
| 4. In which file are inputs defined? | `inputs.conf` |
### Task 5: App Directory / Directorio de la app
**Explicación:** Ruta del directorio de la app de la sala dentro de la instalación de Splunk: `/opt/splunk/etc/apps/THM`. Contiene las configuraciones `default` y `local` que aplican a los datos de práctica.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the path of the THM app directory? | `/opt/splunk/etc/apps/THM` |
### Task 6: props.conf / props.conf
**Explicación:** Uso de `props.conf` para definir la rotura de eventos y transformaciones. La regex `(DISCONNECT|CONNECT)` identifica los conectores como límite, `MUST_BREAK_AFTER` fuerza la creación de un evento después de la coincidencia y el valor booleano `false` desactiva una opción (p. ej. `SHOULD_LINEMERGE`).
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. In which file is the event breaking configured? | `props.conf` |
| 2. What regex matches CONNECT and DISCONNECT? | `(DISCONNECT\|CONNECT)` |
| 3. Which directive forces a break after a match? | `MUST_BREAK_AFTER` |
| 4. What boolean value disables the option? | `false` |
### Task 7: BREAK_ONLY_BEFORE / BREAK_ONLY_BEFORE
**Explicación:** La directiva `BREAK_ONLY_BEFORE` crea un evento nuevo **antes** de la coincidencia, de modo que el patrón (aquí la cabecera `[Authentication]`) marca el inicio de cada evento.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Which directive creates an event before the pattern? | `BREAK_ONLY_BEFORE` |
| 2. What is the pattern that starts the event? | `\[Authentication\]` |
### Task 8: SEDCMD / SEDCMD
**Explicación:** Además de `MUST_BREAK_AFTER`, Splunk permite sustituir contenido en el momento de la indexación mediante `SEDCMD` con sintaxis sed: `s/oldValue/newValue/g` reemplaza todas las apariciones de `oldValue` por `newValue` en el evento.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Which directive forces a break after a match? | `MUST_BREAK_AFTER` |
| 2. What is the sed expression used for substitution? | `s/oldValue/newValue/g` |
### Task 9: Practice / Práctica
**Explicación:** Ejercicio práctico de manipulación de datos sobre los eventos de la app. Las respuestas numéricas son los valores observados (recuentos/resultados) tras aplicar la configuración de parsing.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Observation of the practice (no answer required). | `No answer needed` |
| 2. What is the observed value? | `14` |
| 3. What is the observed value? | `16` |
### Task 10: Conclusion / Conclusión
**Explicación:** Cierre de la sala con recomendaciones para practicar la manipulación de datos y la escritura de configuraciones en Splunk. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conclusión de la sala (sin preguntas). | `No answer needed` |
---
**Metodología:** Conocer la estructura de una app de Splunk → identificar los ficheros de configuración → aplicar directivas de event breaking (`LINE_BREAKER`, `BREAK_ONLY_*`, `MUST_BREAK_AFTER`) → usar `transforms.conf` para regex → aplicar transformaciones con `SEDCMD` → validar con búsquedas.
### Cadena de ataque / Attack Chain
```
Datos en bruto -> inputs.conf (ingesta) -> props.conf (rotura de eventos/timestamps) -> transforms.conf (regex/transformaciones) -> eventos indexados consultables
```
**Learning chain:** estructura de app → ficheros de configuración → event breaking → transforms/regex → validación de datos.
**Lección:** *La calidad de las búsquedas en Splunk depende de cómo se trocean y transforman los datos en la ingesta: dominar props.conf y transforms.conf es esencial para obtener eventos correctos y campos utilizables.*
**MITRE ATT&CK:** (Blue Team) T1070 (Indicator Removal), T1005 (Data from Local System) — relevantes para ingesta y manipulación de logs.
**Fuente:** [TryHackMe - Splunk: Data Manipulation](https://tryhackme.com/room/splunkdatamanipulation)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
