# Investigating with ELK 101 [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `investigatingwithelk101`
* **Link:** https://tryhackme.com/room/investigatingwithelk101
* **Sección / Section:** SOC / ELK
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala enseña a realizar investigaciones de seguridad usando el Elastic Stack (ELK), consultando el índice vpn_connections en Kibana para analizar conexiones VPN, identificar picos de tráfico, usuarios sospechosos, intentos fallidos y detectar actividad posterior a una terminación de contrato.
> **EN:** This room teaches how to perform security investigations using the Elastic Stack (ELK), querying the vpn_connections index in Kibana to analyze VPN connections, identify traffic spikes, suspicious users, failed attempts and detect activity after a contract termination.

---

### Task 1 — Conceptos de Elastic Stack / Elastic Stack Concepts

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Logstash is used to visualize the data. (yay / nay) | `nay` |
| Elasticstash supports all data formats apart from JSON. (yay / nay) | `nay` |

---

### Task 2 — Análisis de Conexiones VPN / VPN Connections Analysis

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Select the index vpn_connections and filter from 31st December 2021 to 2nd Feb 2022. How many hits are returned? | `2861` |
| Which IP address has the max number of connections? | `238.163.231.224` |
| Which user is responsible for max traffic? | `James` |
| Apply Filter on UserName Emanda; which SourceIP has max hits? | `107.14.1.247` |
| On 11th Jan, which IP caused the spike observed in the time chart? | `172.201.60.191` |
| How many connections were observed from IP 238.163.231.224, excluding the New York state? | `48` |
| Create a search query to filter out the logs from Source_Country as the United States and show logs from User James or Albert. How many records were returned? | `161` |

---

### Task 3 — Detección de Anomalías / Anomaly Detection

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| As User Johny Brown was terminated on 1st January 2022, create a search query to determine how many times a VPN connection was observed after his termination. | `1` |
| Which user was observed with the greatest number of failed attempts? | `Simon` |
| How many wrong VPN connection attempts were observed in January? | `274` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Se comprenden los componentes del Elastic Stack, aclarando que Logstash se usa para el procesamiento/logging de datos y no para visualización, y que Elasticsearch soporta múltiples formatos además de JSON.
2. **Paso 2 / Step 2:** Se selecciona el índice vpn_connections y se aplican filtros de tiempo para analizar los hits del período. Se identifican la IP con más conexiones, el usuario con más tráfico, y se segmentan los datos por usuario y por estado geográfico.
3. **Paso 3 / Step 3:** Se construyen queries combinadas (Source_Country = United States con usuarios James o Albert) y se correlacionan eventos para detectar picos de tráfico en fechas concretas, actividad posterior a una terminación, y se analizan los intentos fallidos de autenticación.

### Cadena de ataque / Attack Chain

```
Selección de índice vpn_connections → Filtros de tiempo → Identificación de IPs y usuarios con mayor tráfico → Segmentación por estado/usuario → Queries combinadas → Correlación de eventos sospechosos → Detección de actividad post-terminación → Análisis de intentos fallidos
```

**Lección:** La investigación en Elastic/Kibana permite correlacionar grandes volúmenes de logs de conexión para detectar anomalías: picos de tráfico, usuarios con múltiples intentos fallidos y actividad de cuentas desvinculadas, lo que es esencial para la detección de compromisos en un entorno SOC.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
