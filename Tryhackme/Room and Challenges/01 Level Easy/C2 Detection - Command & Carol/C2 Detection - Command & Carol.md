# C2 Detection - Command & Carol

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `detecting-c2-with-rita-aoc2025-m9n2b5v8c1` | [TryHackMe](https://tryhackme.com/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1) | Advent of Cyber 2025 | THM | RITA, beaconing, threat modifiers, network detection | Detección de comunicaciones C2 en tráfico de red |

---

**Contexto:** RITA (Real Intelligence Threat Analytics) es una herramienta de análisis de tráfico de red que detecta patrones de beaconing y comunicaciones con dominios maliciosos. En esta práctica se analizan logs de red para identificar hosts comprometidos que se comunican con servidores C2, aplicando filtros de amenaza y modificadores de severidad.

## Solucionario

### Task 1: RITA Analysis

**Explicación:** Se importan los logs de red en RITA y se analizan los beacon scores para identificar los hosts que se comunican con los dominios maliciosos (`malhare.net` y `rabbithole.malhare.net`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many hosts are communicating with malhare.net? | `6` |
| 2 | Which Threat Modifier tells us the number of hosts communicating to a certain destination? | `prevalence` |
| 3 | What is the highest number of connections to rabbithole.malhare.net? | `40` |

### Task 2: Advanced Filtering

**Explicación:** Se aplican filtros avanzados de búsqueda sobre los datos de RITA para aislar las comunicaciones más sospechosas y determinar los puertos de conexión específicos utilizados por los hosts comprometidos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)? | `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc` |
| 2 | Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net? | `80` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many hosts are communicating with malhare.net? | `6` |
| 2 | Which Threat Modifier tells us the number of hosts communicating to a certain destination? | `prevalence` |
| 3 | What is the highest number of connections to rabbithole.malhare.net? | `40` |
| 4 | Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)? | `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc` |
| 5 | Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net? | `80` |

---

**Metodología:** Se utilizó RITA para analizar logs de red Zeek, identificando dominios maliciosos y patrones de beaconing. Se aplicaron modificadores de amenaza (threat modifiers) como `prevalence` para cuantificar la propagación. Se usaron filtros avanzados para aislar las comunicaciones más sospechosas y determinar puertos de conexión específicos.

### Cadena de ataque / Attack Chain

```text
Logs de red (Zeek) → importación en RITA → análisis de beacon scores → identificación de hosts comprometidos → threat modifiers (prevalence) → filtros avanzados (beacon:>=70, sort:duration-desc) → IOCs (dominios y puertos)
```

**Learning chain:** Network log analysis → RITA → beaconing detection → threat modifiers → advanced filtering → IOC extraction

**Lección:** *El análisis de beaconing con herramientas como RITA permite a los equipos defensivos detectar hosts comprometidos por C2 antes de que el adversario complete su misión.*

**MITRE ATT&CK:** T1071.001 - Application Layer Protocol: Web Protocols, T1573.002 - Encrypted Channel: Asymmetric Cryptography

**Fuente:** [TryHackMe - C2 Detection - Command & Carol](https://tryhackme.com/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.