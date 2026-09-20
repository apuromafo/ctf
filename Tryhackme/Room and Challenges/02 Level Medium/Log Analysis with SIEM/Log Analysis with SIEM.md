# Log Analysis with SIEM

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teoría / Laboratorio | loganalysiswithsiem | https://tryhackme.com/room/loganalysiswithsiem | 02 Level Medium | TryHackMe | SIEM, correlación, centralización, normalización, logs host/web, EDR, WordPress | Detección y análisis de ataques mediante correlación de logs |

---

**Contexto:** La sala **Log Analysis with SIEM** ejercita el análisis de logs apoyándose en una plataforma SIEM. Combina los fundamentos teóricos del SIEM —centralización, correlación y normalización— con el análisis práctico de eventos de un endpoint comprometido (IPs, procesos sospechosos, hashes, instaladores) y de ataques web como fuerza bruta a `/wp-login.php` llevados a cabo con WPScan.

## Solucionario

### Task 1: Introducción
**Explicación:**

Tarea de contexto inicial que prepara el escenario del análisis de logs y el acceso a la plataforma SIEM.

1. `No answer needed`

### Task 2: Funciones del SIEM
**Explicación:**

Se identifican los dos beneficios centrales del SIEM: la correlación entre eventos y la centralización de las fuentes de log en un único lugar.

1. `Correlation`
2. `Centralisation`

### Task 3: Proceso de datos y tipos de logs
**Explicación:**

Se cubre la normalización de los eventos (conversión a un formato común) y la clasificación de los logs según el sistema que los genera (host-based frente a network-based).

1. `Normalisation`
2. `Host-Based`

### Task 4: Análisis de endpoint / Windows
**Explicación:**

Se investigan los eventos de un endpoint comprometido: la IP de origen, el ejecutable malicioso implicado, su hash SHA1 y el software/instalador relacionado.

1. `10.10.114.80`
2. `SharePoInt.exe`
3. `770D14FFA142F09730B415506249E7D1`
4. `Office365 Install`

### Task 5: Análisis de accesos remotos
**Explicación:**

Se examinan las conexiones de escritorio remoto: fecha y hora del acceso, usuario implicado, IP de origen, número de conexiones y puerto de la sesión.

1. `2025-08-12 09:52:57`
2. `jack-brown`
3. `10.14.94.82`
4. `4`
5. `7654`

### Task 6: Análisis de tráfico web
**Explicación:**

Se analizan los ataques contra una aplicación web: ruta atacada, IP atacante, tipo de ataque (fuerza bruta) y la herramienta utilizada para lanzarlo.

1. `/wp-login.php`
2. `10.10.243.134`
3. `Brute Force`
4. `WPScan`

### Task 7: Cierre
**Explicación:**

Se consolida el análisis de las distintas fuentes de log y se cierra la práctica.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de introducción inicial | `No answer needed` |
| 2.1 | Beneficio del SIEM: relación entre eventos | `Correlation` |
| 2.2 | Beneficio del SIEM: almacenamiento unificado de logs | `Centralisation` |
| 3.1 | Proceso de estandarización de los eventos | `Normalisation` |
| 3.2 | Clasificación de los logs del propio sistema | `Host-Based` |
| 4.1 | IP de origen del evento de endpoint | `10.10.114.80` |
| 4.2 | Ejecutable sospechoso | `SharePoInt.exe` |
| 4.3 | Hash del archivo (SHA1) | `770D14FFA142F09730B415506249E7D1` |
| 4.4 | Software/instalador relacionado | `Office365 Install` |
| 5.1 | Fecha y hora del acceso remoto | `2025-08-12 09:52:57` |
| 5.2 | Usuario implicado | `jack-brown` |
| 5.3 | IP de origen de la conexión | `10.14.94.82` |
| 5.4 | Número de conexiones | `4` |
| 5.5 | Puerto de la sesión | `7654` |
| 6.1 | Ruta atacada | `/wp-login.php` |
| 6.2 | IP atacante | `10.10.243.134` |
| 6.3 | Tipo de ataque | `Brute Force` |
| 6.4 | Herramienta de ataque | `WPScan` |
| 7 | Tarea final de cierre | `No answer needed` |

---

**Metodología:** Análisis de logs guiado por un SIEM: desde los fundamentos (centralización, correlación, normalización y logs host-based) hasta la investigación de eventos concretos de endpoint (IP, proceso, hash SHA1, instalador) y de ataques web (brute force a WordPress con WPScan), correlacionando las fuentes para reconstruir la actividad maliciosa.

**Learning chain:** Fundamentos SIEM → normalización y tipos de logs → análisis de endpoint comprometido → análisis de acceso remoto → análisis web/brute force → cierre.

**Lección:** *Un SIEM solo aporta valor si los logs están normalizados, centralizados y correlacionados: son los pequeños datos (IPs, hashes, timestamps) los que, unidos, reconstruyen el ataque completo.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1110 Brute Force · T1078 Valid Accounts (RDP) · T1059 Command and Scripting Interpreter · T1005 Data from Local System.

**Fuente:** [TryHackMe - Log Analysis with SIEM](https://tryhackme.com/room/loganalysiswithsiem)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.