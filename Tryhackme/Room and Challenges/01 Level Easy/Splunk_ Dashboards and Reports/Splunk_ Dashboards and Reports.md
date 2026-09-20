# Splunk_ Dashboards and Reports

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `splunkdashboardsandreports` | [TryHackMe](https://tryhackme.com/room/splunkdashboardsandreports) | 01 Level Easy | TryHackMe | Splunk, Dashboards, Reports, SPL | Operational — Building dashboards and reports in Splunk |

---

**Contexto:** Este room explora la creación y gestión de dashboards y reportes en Splunk. Se Cubre desde la búsqueda de datos con SPL hasta la creación de alertas, pasando por los tipos de visualizaciones y las opciones de configuración de reportes y dashboards.

## Solucionario

### Task 1: Splunk Dashboards Overview

**Explicación:** Se Introducen los conceptos de dashboards y reportes en Splunk sin requerir una respuesta específica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the overview | `No answer needed` |

### Task 2: Search Fundamentals

**Explicación:** Se Identifica la consulta SPL base utilizada para buscar todos los eventos en un índice de Splunk.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | What is the search query used to find all events? | `index=*` |

### Task 3: Dashboard Creation

**Explicación:** Se Analiza la creación de dashboards, incluyendo el número de paneles y el control de rango de tiempo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many panels were created? | `5` |
| 2 | What control is used to select the time range? | `Time Range Picker` |

### Task 4: Report Settings

**Explicación:** Se Configuran reportes en Splunk, ajustando el límite de resultados y la visualización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the result limit? | `400` |
| 2 | What type of visualization was selected? | `Classic ` |

### Task 5: Alerts Configuration

**Explicación:** Se Configuran alertas en Splunk, incluyendo la acción de disparo, el modo de evaluación en tiempo real y las opciones de throttle.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What action triggers the alert? | `Trigger Action` |
| 2 | What mode evaluates the alert? | `Real-time` |
| 3 | What reduces repeated alerts? | `Throttle` |

### Task 6: Practical Exercise

**Explicación:** Se Aplica los conocimientos de dashboards y reportes en un ejercicio práctico de Splunk.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the practical exercise | `No answer needed` |

---

**Metodología:** Se Configuran dashboards y reportes en Splunk, desde la búsqueda base hasta la creación de alertas, aplicando las mejores prácticas de visualización y monitoreo.

### Cadena de ataque / Attack Chain

**Learning chain:** Splunk Fundamental → SPL Queries → Dashboard Building → Report Configuration → Alert Tuning

**Lección:** *Los dashboards y reportes en Splunk permiten transformar datos crudos en información accionable, facilitando el monitoreo continuo y la detección temprana de incidentes de seguridad.*

**MITRE ATT&CK:** T1562 — Impair Defenses; T1089 — Disabling Security Tools

**Fuente:** [TryHackMe - Splunk_ Dashboards and Reports](https://tryhackme.com/room/splunkdashboardsandreports)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.