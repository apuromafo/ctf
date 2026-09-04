# Baselines and Anomalies [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `baselineanomalies`
* **Link:** https://tryhackme.com/room/baselineanomalies
* **Sección / Section:** SOC / Detection
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala centrada en la detección de anomalías frente a líneas base: identificación de dispositivos no estándar, anomalías de red y análisis de inicios de sesión sospechosos.
> **EN:** Room focused on anomaly detection against baselines: identifying non-standard devices, network anomalies, and analyzing suspicious logins.

---

### Task 1 — Anomalías de Activos / Asset Anomalies

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the workstation that has the anomalous IP address? | `WS-LON-004` |
| What is the name of the server with the anomalous IP address? | `SVR-NYC-BKUP01` |
| Which workstation has a device model different from the rest? | `WS-NYC-004` |
| There are two installed software programs that should not be included in Anna's list. Which ones are they? Share their serial numbers. Answer format: X, Y | `9, 15` |

---

### Task 2 — Conceptos de Detección / Detection Concepts

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| When trying to identify if an activity was performed by the administrator or not, what is the biggest tool that a defender can use? | `communication` |
| Which process can be used to track and approve changes to the firewall Access Control List? | `Change Management and Approvals` |
| If we are looking for DNS traffic bypassing the local DNS server, what should we exclude from the search of all queries to the DNS port? | `Internal DNS server` |
| What kind of alert should be generated if a user logs in from two vastly geographically different places in a short amount of time? | `Impossible travel` |

---

### Task 3 — Investigación de Login Sospechoso / Suspicious Login Investigation

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| You have been alerted of a login outside of normal office hours on the 27th of July, 2024. Can you identify the time this login happened? | `06:37:07.659259000` |
| Which user logged in at this time? | `Mia Perez` |
| This user performed anomalous activities from two different machines; what is the IP address of the other machine? | `192.168.1.36` |
| What suspicious domain does this user connect to? | `c2server.com` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Comparar los activos de la red frente a la línea base establecida para detectar direcciones IP y modelos de dispositivos anómalos.
2. **Paso 2 / Step 2:** Revisar la lista de software instalado y eliminar programas no esperados del inventario.
3. **Paso 3 / Step 3:** Aplicar conceptos de detección como la comunicación con administradores, gestión de cambios y alertas de travel imposible.
4. **Paso 4 / Step 4:** Investigar inicios de sesión fuera del horario laboral y correlacionar actividades anómalas de usuarios con IPs y dominios sospechosos.

### Cadena de ataque / Attack Chain

```
Establecer línea base → Comparar activos (IP/modelo/software) → Identificar anomalías → Detectar login anómalo → Correlacionar usuario, IPs y dominio → Dominio C2
```

**Lección:** La comparación continua con líneas base conocidas y la correlación de eventos (login, IPs, dominios) permiten identificar actividades maliciosas en la red.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.