# SOC Workbooks and Lookups

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `socworkbooksandlookups` | [TryHackMe](https://tryhackme.com/room/socworkbooksandlookups) | 01 Level Easy | TryHackMe | SOC Workbooks, Lookups, Asset Inventory, Enrichment | Operational — Using workbooks and lookups for SOC investigations |

---

**Contexto:** Este room aborda el uso de workbooks y lookups en un SOC para enriquecer investigaciones, gestionar inventarios de activos y correlacionar datos de múltiples fuentes durante la respuesta a incidentes.

## Solucionario

### Task 1: SOC Workbooks Introduction

**Explicación:** Se Introducen los conceptos de workbooks de SOC sin requerir una respuesta específica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the intro | `No answer needed` |

### Task 2: Financial Investigation

**Explicación:** Se Analiza un caso de investigación financiera utilizando workbooks de SOC para identificar al asesor financiero y los registros involucrados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who is the financial adviser? | `US Financial Adviser` |
| 2 | What records were accessed? | `Financial records` |
| 3 | Was the data exfiltrated? | `Yea` |

### Task 3: Network Analysis

**Explicación:** Se Identifican los componentes de red involucrados en un incidente, incluyendo VPN y subredes de base de datos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What technology was used to access the network? | `VPN` |
| 2 | Which subnet was targeted? | `Database subnet` |
| 3 | What is the threat actor's initials? | `TP` |

### Task 4: SOC Roles and Enrichment

**Explicación:** Se Identifica el rol del analista SOC y las herramientas de enriquecimiento utilizadas en las investigaciones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What SOC role handled the investigation? | `SOC L1 Analyst` |
| 2 | What process was used to gather additional context? | `Enrichment` |
| 3 | What HR platform was used to look up employee data? | `BambooHR` |

### Task 5: Flags

**Explicación:** Se Resuelven los ejercicios prácticos identificando las flags correctas de workbooks, lookups e inventario de activos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the workbook flag? | `THM{the_most_common_soc_workbook}` |
| 2 | What is the PowerShell flag? | `THM{be_vigilant_with_powershell}` |
| 3 | What is the asset inventory flag? | `THM{asset_inventory_is_essential}` |

### Task 6: Practical Exercise

**Explicación:** Se Aplica los conocimientos de workbooks y lookups en un ejercicio práctico de SOC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the practical exercise | `No answer needed` |

---

**Metodología:** Se Utilizan workbooks y lookups de SOC para enriquecer investigaciones, correlacionar datos de múltiples fuentes y gestionar inventarios de activos de manera efectiva.

### Cadena de ataque / Attack Chain

**Learning chain:** SOC Workbooks → Data Lookup → Asset Inventory → Enrichment → Investigation Correlation

**Lección:** *Los workbooks y lookups son herramientas esenciales en un SOC que permiten enriquecer investigaciones, correlacionar datos de múltiples fuentes y mantener inventarios de activos actualizados para una respuesta más efectiva a incidentes.*

**MITRE ATT&CK:** T1087 — Account Discovery; T1018 — Remote System Discovery

**Fuente:** [TryHackMe - SOC Workbooks and Lookups](https://tryhackme.com/room/socworkbooksandlookups)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.