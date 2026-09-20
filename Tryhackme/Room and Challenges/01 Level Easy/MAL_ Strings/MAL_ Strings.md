# MAL_ Strings

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `malstrings` | [TryHackMe](https://tryhackme.com/room/malstrings) | 01 Level Easy | THM | strings, Sysinternals Strings, FlatPress, CVE-2019-6499, análisis estático | Análisis estático de malware extrayendo cadenas e indicadores sin ejecutar la muestra |

> **Objeto:** Aprender a usar la utilidad `strings` (GNU y Sysinternals) para analizar muestras de malware de forma estática y extraer cadenas, flags e indicadores valiosos.

---

**Contexto:** Sala del módulo MAL que enseña a emplear `strings` sobre binarios maliciosos: se identifican cadenas incrustadas como autores, CVEs, rutas, direcciones de C2, metadatos y flags ocultas en muestras reales como WannaCry y FlatPress.

> **ES:** Sala de introducción a strings: extracción de cadenas legibles de binarios para el análisis estático de malware y la búsqueda de flags e indicadores.
> **EN:** Introductory room to strings: extracting readable strings from binaries for static malware analysis and hunting flags and indicators.

## Solucionario

### Task 1: Introducción a strings y primeras cadenas / Introduction to strings and first strings
**Explicación:** Se presentan los conceptos básicos de la utilidad strings y se localizan las primeras cadenas incrustadas en la muestra, incluyendo el autor, un CVE y un valor de prueba.

1. intellian
2. CVE-2019-6499
3. one

### Task 2: Flags ocultas / Hidden flags
**Explicación:** Continuando con el análisis se identifican cadenas relacionadas con el autor de la muestra y se recupera la primera flag oculta.

1. cmnatic
2. TryHackMeMerchWhen
3. THM{Not_So_Hidden_Flag}

### Task 3: C2 y familias de malware / C2 and malware families
**Explicación:** Las cadenas revelan funcionalidad de comando y control, así como la familia de malware asociada a la muestra.

1. Command and Control
2. Wannacry

### Task 4: Metadatos y direcciones / Metadata and addresses
**Explicación:** Se extraen cadenas con metadatos temporales y direcciones BTC encadenadas a la muestra analizada.

1. 05/12/2017
2. 1LVB65imeojrgC3JPZGBwWhK1BdVZ2vYNC

### Task 5: Herramientas y filtrado / Tools and filtering
**Explicación:** Se comparan variantes de la herramienta strings y se practica el filtrado de caracteres y la búsqueda de cadenas como direcciones de bitcoin.

1. Sysinternals
2. >
3. bitcoin

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | Cadena con el autor de la muestra | `intellian` |
| 1.2 | CVE relacionado con la muestra | `CVE-2019-6499` |
| 1.3 | Valor de la primera cadena de prueba | `one` |
| 2.1 | Autor o creador de la muestra | `cmnatic` |
| 2.2 | Cadena de pista encontrada | `TryHackMeMerchWhen` |
| 2.3 | Flag oculta encontrada | `THM{Not_So_Hidden_Flag}` |
| 3.1 | Funcionalidad identificada | `Command and Control` |
| 3.2 | Familia de malware detectada | `Wannacry` |
| 4.1 | Fecha encontrada en las cadenas | `05/12/2017` |
| 4.2 | Dirección de bitcoin detectada | `1LVB65imeojrgC3JPZGBwWhK1BdVZ2vYNC` |
| 5.1 | Herramienta alternativa a GNU strings | `Sysinternals` |
| 5.2 | Carácter usado para el filtrado | `>` |
| 5.3 | Tipo de cadena buscada | `bitcoin` |

---

**Metodología:** Ejecución de `strings` sobre la muestra, inspección de las cadenas extraídas, filtrado con símbolos y búsquedas dirigidas, correlación de autores, CVEs, fechas y direcciones, y recuperación de la flag oculta. Comparación entre `strings` de GNU y la variante Sysinternals.

### Cadena de ataque / Attack Chain

Muestra maliciosa → `strings` → extracción de cadenas → filtrado y análisis → autor/CVE/familia/metadatos → IOC (C2, dirección BTC) → flag.

**Learning chain:** strings → extracción de cadenas → análisis estático → IOCs → flags

*Lección:* El análisis estático con `strings` es el primer paso para triar malware sin ejecutarlo: revela autores, rutas, C2, metadatos y flags.

**MITRE ATT&CK:** T1105 - Ingress Tool Transfer, T1071.001 - Application Layer Protocol.

**Fuente:** [TryHackMe - MAL_ Strings](https://tryhackme.com/room/malstrings)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.