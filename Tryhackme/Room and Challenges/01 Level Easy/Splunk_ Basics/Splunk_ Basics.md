# Splunk: Basics [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `splunk101`
* **Link:** https://tryhackme.com/room/splunk101
* **Sección / Section:** Cyber Defense / SIEM
* **Fuente / Source:** Writeup de jesusgavancho (GitHub) + Rahul Kumar (System Weakness)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Splunk es una de las soluciones SIEM líderes en el mercado que proporciona la capacidad de recopilar, analizar y correlacionar los logs de red y de máquina en tiempo real. En esta room exploramos los conceptos básicos de Splunk y sus funcionalidades.
> **EN:** Splunk is one of the leading SIEM solutions in the market that provides the ability to collect, analyze and correlate the network and machine logs in real-time. In this room, we explore the basics of Splunk and its functionalities.

---

### Task 1 — Introduction

Splunk es una de las soluciones SIEM líderes. Permite recopilar, analizar y correlacionar logs de red y de máquina en tiempo real.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 2 — Splunk Components

Splunk tiene tres componentes principales: **Forwarder**, **Indexer** y **Search Head**.

* **Forwarder:** recopila y envía datos a la instancia de Splunk.
* **Indexer:** indexa y almacena los logs.
* **Search Head:** lugar donde los usuarios buscan los logs indexados usando SPL (Splunk Search Processing Language).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which component is used to collect and send data over the Splunk instance? | `Forwarder` |

---

### Task 3 — Navigating Splunk

Para subir datos: **Add Data** → **Upload** → seleccionar el archivo → **Select Source Type** → **Input Settings** (seleccionar el índice) → **Review** → **Done**.

Subir el archivo `VPN_logs` y crear el índice `VPN_Logs`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Upload the data attached to this task and create an index "VPN_Logs". How many events are present in the log file? | `2862` |
| How many log events by the user Maleena are captured? | `60` |
| What is the name associated with IP 107.14.182.38? | `Smith` |
| What is the number of events that originated from all countries except France? | `2814` |
| How many VPN Events were observed by the IP 107.3.206.58? | `14` |

---

## Metodología / Methodology

1. **Componentes:** Forwarder (recopila/envía), Indexer (indexa/almacena), Search Head (busca/visualiza).
2. **Ingesta de logs:** Add Data → Upload → seleccionar source type → definir índice.
3. **Búsqueda:** usar SPL para consultar los logs indexados y obtener eventos como field-value pairs.

**Lección:** Splunk proporciona mejor visibilidad de las actividades de red y ayuda a acelerar la detección de incidentes.

---

*Documentación para propósitos educativos y registro de CTF.*
