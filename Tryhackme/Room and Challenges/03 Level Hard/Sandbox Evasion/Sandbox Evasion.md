# Sandbox Evasion

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Guía técnica | `sandboxevasion` | https://tryhackme.com/room/sandboxevasion | 03 Level Hard | TryHackMe | sandbox / análisis dinámico / ofuscación / sleep / geolocalización / flags | Guía de evasión de sandboxes: análisis dinámico vs estático, mail sandboxes, técnicas de evasión como sleeping y comprobación de la información del sistema, y una flag final. |

---

**Contexto:** Sala técnica sobre evasión de sandboxes. Practica la clasificación del análisis (dinámico), un tipo de sandbox (Mail Sandbox) y técnicas de evasión como retrasar la ejecución (Sleeping), comprobar la información del sistema (Checking System Information) o filtrar por geolocalización (Geolocation Filtering), cerrando con una flag final. Una tarea es tipo encuesta sin respuesta.

> **ES:** "Aprende a evadir sandboxes con técnicas de análisis dinámico, sleeping, comprobación del sistema y filtrado por geolocalización."
> **EN:** "Learn how to evade sandboxes with dynamic analysis, sleeping, system information checks and geolocation filtering."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea introductoria de la sala; no requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria sin respuesta. | `No answer needed` |

### Task 2: Tipos de análisis y sandbox / Analysis types and sandbox

**Explicación:** Tarea que clasifica el tipo de análisis que burla el artefacto (Dynamic) e identifica una clase de sandbox (Mail Sandbox). Contenido original de la tarea:

```text
2. 1. Dynamic
   2. Mail Sandbox
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tipo de análisis que el artefacto intenta burlar. | `Dynamic` |
| 2 | Tipo de sandbox presente en el entorno. | `Mail Sandbox` |

### Task 3: Técnicas de evasión / Evasion techniques

**Explicación:** Tarea sobre técnicas de evasión: los dos primeros pasos no requieren respuesta, y después se identifican las técnicas de retraso (Sleeping) y comprobación de la información del sistema (Checking System Information). Contenido original de la tarea:

```text
3. 1. No answer needed
   2. No answer needed
   3. Sleeping
   4. Checking System Information
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Paso práctico previo de la tarea. | `No answer needed` |
| 3 | Primera técnica de evasión identificada. | `Sleeping` |
| 4 | Segunda técnica de evasión identificada. | `Checking System Information` |

### Task 4: Técnicas de evasión avanzadas / Advanced evasion techniques

**Explicación:** Tarea sobre técnicas de evasión avanzadas: paso previo sin respuesta, luego el filtrado por geolocalización (Geolocation Filtering) y el retraso de ejecución (Sleeping). Contenido original de la tarea:

```text
4. 1. No answer needed
   2. Geolocation Filtering
   3. Sleeping
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Técnica de filtrado por ubicación. | `Geolocation Filtering` |
| 3 | Técnica de retraso de ejecución. | `Sleeping` |

### Task 5: Flag final / Final flag

**Explicación:** Flag final del reto, obtenida al completar las técnicas de evasión de sandbox. Contenido original de la tarea:

```text
5. THM{6c1f95ec}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag final del reto. | `THM{6c1f95ec}` |

### Task 6: Conclusión / Conclusion

**Explicación:** Tarea de cierre de la sala; no requiere respuesta. Contenido original de la tarea:

```text
6. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de cierre sin respuesta. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria sin respuesta. | `No answer needed` |
| 2 | Tipo de análisis que el artefacto intenta burlar. | `Dynamic` |
| 3 | Tipo de sandbox presente en el entorno. | `Mail Sandbox` |
| 4 | Paso práctico previo de la tarea. | `No answer needed` |
| 5 | Paso práctico previo de la tarea. | `No answer needed` |
| 6 | Primera técnica de evasión identificada. | `Sleeping` |
| 7 | Segunda técnica de evasión identificada. | `Checking System Information` |
| 8 | Paso práctico previo de la tarea. | `No answer needed` |
| 9 | Técnica de filtrado por ubicación. | `Geolocation Filtering` |
| 10 | Técnica de retraso de ejecución. | `Sleeping` |
| 11 | Flag final del reto. | `THM{6c1f95ec}` |
| 12 | Tarea de cierre sin respuesta. | `No answer needed` |

---

**Metodología:**
1. Identificar el tipo de análisis que el artefacto intenta burlar (Dynamic) y el sandbox del entorno (Mail Sandbox).
2. Aplicar las técnicas de evasión de retraso (Sleeping) y comprobación de información del sistema.
3. Añadir el filtrado por geolocalización (Geolocation Filtering).
4. Completar el reto y recoger la flag final.

### Cadena de ataque / Attack Chain

```text
Análisis dinámico (Dynamic) -> Mail Sandbox -> Sleeping -> Checking System Information -> Geolocation Filtering -> THM{6c1f95ec}
```

**Learning chain:** `Sandbox -> análisis dinámico -> evasiones (sleep, system info, geo) -> flag`

**Lección:** *La evasión de sandboxes se basa en detectar el entorno de análisis: el retardo en la ejecución (sleep), la comprobación del sistema y los filtros geográficos son técnicas clásicas cuyo aprendizaje se valida con la flag.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1562.001 (Impair Defenses: Disable or Modify Tools), T1480 (Execution Guardrails), T1610 (Deploy Container)

**Fuente:** [TryHackMe - Sandbox Evasion](https://tryhackme.com/room/sandboxevasion)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.