# Splunk: The Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `splunk101` |
| **Link** | [TryHackMe](https://tryhackme.com/room/splunk101) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de jesusgavancho (GitHub) + Rahul Kumar (System Weakness) |
| **Componentes** | Splunk / SPL / Forwarder / Indexer / Search Head / SIEM |
| **Impacto** | Fundamentos de Splunk como SIEM: componentes, ingesta de logs y búsqueda de eventos con SPL |

---

**Contexto:** Splunk es una de las soluciones SIEM líderes en el mercado que proporciona la capacidad de recopilar, analizar y correlacionar los logs de red y de máquina en tiempo real. En esta room exploramos los conceptos básicos de Splunk y sus funcionalidades: los tres componentes principales (Forwarder, Indexer y Search Head), la ingesta de datos y las búsquedas con SPL.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

### Task 2: Splunk Components

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which component is used to collect and send data over the Splunk instance? | `Forwarder` |

### Task 3: Navigating Splunk

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Upload the data attached to this task and create an index "VPN_Logs". How many events are present in the log file? | `2862` |
| 2 | How many log events by the user Maleena are captured? | `60` |
| 3 | What is the name associated with IP 107.14.182.38? | `Smith` |
| 4 | What is the number of events that originated from all countries except France? | `2814` |
| 5 | How many VPN Events were observed by the IP 107.3.206.58? | `14` |

---

**Metodología:**
1. **Componentes de Splunk:** el **Forwarder** recopila y envía datos a la instancia de Splunk; el **Indexer** indexa y almacena los logs; el **Search Head** es el lugar donde los usuarios buscan los logs indexados usando SPL (Splunk Search Processing Language).
2. **Ingesta de logs:** para subir datos: **Add Data** → **Upload** → seleccionar el archivo → **Select Source Type** → **Input Settings** (seleccionar el índice) → **Review** → **Done**. En el lab se sube el archivo `VPN_logs` y se crea el índice `VPN_Logs`.
3. **Búsqueda:** usar SPL para consultar los logs indexados y obtener eventos como field-value pairs: el archivo tiene `2862` eventos; la usuaria `Maleena` aparece en `60`; el IP `107.14.182.38` se asocia al nombre `Smith`; los eventos de todos los países excepto Francia son `2814`; y el IP `107.3.206.58` observa `14` eventos VPN.

**Learning chain:** Splunk (SIEM) → componentes (Forwarder / Indexer / Search Head) → ingesta (Add Data → Upload → índice VPN_Logs) → búsqueda SPL (2862 eventos, Maleena=60, 107.14.182.38=Smith, !=France=2814, 107.3.206.58=14)

**MITRE ATT&CK:** No aplica técnicas ofensivas; herramienta defensiva (SIEM) para monitoreo y detección de eventos de red

**Fuente:** [TryHackMe - Splunk: The Basics](https://tryhackme.com/room/splunk101)