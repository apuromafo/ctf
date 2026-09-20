# Network Discovery Detection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Módulo / Laboratorio | networkdiscoverydetection | https://tryhackme.com/room/networkdiscoverydetection | Detección de Descubrimiento de Red | TryHackMe | Zeek, logs de sesión, análisis de tráfico, escaneo de red | Medium |

> **Objeto:** Aprender a detectar actividades de descubrimiento de red (escaneos) en el tráfico. Usar Zeek para generar y analizar logs, identificar hosts, puertos y tipos de escaneo y responder a los ejercicios del laboratorio.

---

**Contexto:**

Esta sala enseña a detectar reconocimiento y escaneo de red analizando tráfico capturado. Se despliega Zeek sobre los archivos de captura para generar logs de conexión (`conn.log`), se inspeccionan métricas como el número de paquetes y bytes, se identifican subredes escaneadas, direcciones IP de origen, puertos de destino y el tipo de escaneo (por ejemplo, *TCP SYN Scan*). Los ejercicios piden relacionar las respuestas derivadas de los logs.

> **ES:** Se utilizan las herramientas de detección para examinar una red con actividad de escaneo. Con Zeek se generan los logs de sesión, se identifica la subred objetivo (203.0.113.0/24), la IP del escáner (192.168.230.127), los puertos observados (80, 445, 3389) y el tipo de escaneo (TCP SYN Scan). A partir de estadísticas por pares en los logs se responden los ejercicios.

> **EN:** Detection tools are used to examine a network with scanning activity. With Zeek the session logs are generated, the target subnet (203.0.113.0/24), the scanner IP (192.168.230.127), the observed ports (80, 445, 3389) and the scan type (TCP SYN Scan) are identified. The exercises are answered from per-pair statistics in the logs.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Se presenta la sala y el objetivo: detectar escaneo de red mediante análisis de logs.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |

### Task 2: Qué detectar / What to Detect
**Explicación:**

Se exponen los artefactos que deja el descubrimiento de red en los logs, principalmente el tipo de conexiones registradas.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 2. ¿Qué tipo de actividad se observa? / What type of activity is observed? | `Services` |

### Task 3: Logs de sesión / Session Logs
**Explicación:**

Se procesa lo capturado con Zeek para generar los logs de sesión (`conn.log`). Se identifica el archivo de log con la actividad relevante, se consulta su métrica (número de pares/sesiones) y una de las IP implicadas.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Archivo de log con la actividad | `log-session-2.csv` |
| 2. Número de sesiones/entradas | `2276` |
| 3. Dirección IP identificada | `203.0.113.25` |

### Task 4: Análisis del escaneo / Scan Analysis
**Explicación:**

Se correlacionan los logs para delimitar el alcance del escaneo: la subred atacada, la IP del origen del tráfico de escaneo y los puertos de destino observados.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Subred escaneada | `203.0.113.0/24` |
| 2. IP del escáner | `192.168.230.145` |
| 3. Puertos de destino | `80, 445, 3389` |

### Task 5: Tipo de escaneo / Scan Type
**Explicación:**

Se identifica quién realiza el escaneo y con qué técnica: la IP de origen, el tipo de escaneo utilizado (TCP SYN Scan) y si la traza muestra indicadores adicionales.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. IP de origen del escáner | `192.168.230.127` |
| 2. Tipo de escaneo | `TCP SYN Scan` |
| 3. Indicador adicional / N | `N` |

### Task 6: Resumen / Summary
**Explicación:**

Se consolida el flujo completo de detección del descubrimiento de red.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 6 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Task 1 | `No answer needed` |
| 2 | Tipo de actividad | `Services` |
| 3 | 1. Archivo del log | `log-session-2.csv` |
| 3 | 2. Número de sesiones | `2276` |
| 3 | 3. IP identificada | `203.0.113.25` |
| 4 | 1. Subred escaneada | `203.0.113.0/24` |
| 4 | 2. IP del escáner | `192.168.230.145` |
| 4 | 3. Puertos | `80, 445, 3389` |
| 5 | 1. IP del escáner | `192.168.230.127` |
| 5 | 2. Tipo de escaneo | `TCP SYN Scan` |
| 5 | 3. Indicador | `N` |
| 6 | Task 6 | `No answer needed` |

---

**Metodología:**

1. Procesar las capturas con Zeek para generar `conn.log` y logs derivados.
2. Identificar el archivo de log con actividad anómala (`log-session-2.csv`) y su estadística (`2276`).
3. Agrupar por par origen/destino para localizar la subred escaneada y las IPs implicadas.
4. Determinar puertos de destino (`80, 445, 3389`), técnica de escaneo (TCP SYN) y alcance.

### Cadena de ataque / Attack Chain

```
Captura de tráfico con actividad de escaneo
        |
        v
Zeek --> conn.log / log-session-2.csv (2276 sesiones)
        |
        v
Identificar subred objetivo: 203.0.113.0/24
        |
        v
Origen del escaneo: 192.168.230.127 / 192.168.230.145
        |
        v
Puertos: 80, 445, 3389  |  Tipo: TCP SYN Scan
```

**Learning chain:**

- ¿Qué artefactos deja un escaneo de red en los logs de Zeek?
- ¿Cómo se traduce un `conn.log` en una subred y una IP de origen?
- ¿Cómo se distingue un escaneo SYN (half-open) de otras técnicas observando las banderas?

**Lección:**

*Un escaneo deja huellas claras en los logs de sesión: mirando pares origen/destino, puertos y banderas se reconstruye al escáner, su objetivo y el alcance completo de su reconocimiento.*

**MITRE ATT&CK:**

- T1595.001 (Active Scanning: Scanning IP Blocks)
- T1595.002 (Active Scanning: Vulnerability Scanning)
- T1046 (Network Service Discovery)
- Detección vía NF/SIEM (Network Traffic Analysis)

**Fuente:** [TryHackMe - Network Discovery Detection](https://tryhackme.com/room/networkdiscoverydetection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.