# AI Forensics [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Teoría + Práctica (investigación DFIR) / Theory + Practical Lab (DFIR Investigation)
* **Slug:** `aiforensics`
* **Link:** https://tryhackme.com/room/aiforensics
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\05-ai-forensics\README.md`

---

## Solucionario de Tareas / Task Solutions

### Tarea 1 / Task 1: Introduction

No se requiere respuesta.
*No answer needed.*

---

### Tarea 2 / Task 2: AI in DFIR (Teoría)

**Pregunta / Question:** What ability of AI helps a DFIR investigator by recognising patterns they might not have been able to comprehend?

**Respuesta / Answer:**

```
Anomaly Detection
```

**Pregunta / Question:** What term describes the AI characteristic where the same input may yield different outputs across different runs?

**Respuesta / Answer:**

```
Nondeterminism
```

**Pregunta / Question:** What type of neural network is commonly used in image and video forensics due to its ability to learn spatial patterns in visual data?

**Respuesta / Answer:**

```
Convolutional Neural Network
```

**Pregunta / Question:** What kind of analysis can be performed on social media or chat logs to assess the emotional tone of messages?

**Respuesta / Answer:**

```
Sentiment Analysis
```

**Pregunta / Question:** What type of data do AI systems correlate to reconstruct the timeline of an incident automatically?

**Respuesta / Answer:**

```
Event Data
```

**Pregunta / Question:** What type of analysis observes how a program behaves to determine whether it is malicious, e.g., using its API call sequence?

**Respuesta / Answer:**

```
Dynamic Analysis
```

---

### Tarea 3 / Task 3: The Digital Trail (Investigación práctica)

**Setup:** SSH a la máquina comprometida como `o.deer` con contraseña `TryHackMe!`.

**Pasos / Steps:**
1. `python3 classify_logs.py auth.log` — el modelo ML marca los inicios de sesión anómalos.
2. `python3 file_anomalies.py` — detecta archivos sospechosos.
3. Validación humana de cada artefacto marcado.

**Pregunta / Question:** At what time does the attacker successfully log in as j.morgan?

**Respuesta / Answer:**

```
03:01:02
```

**Pregunta / Question:** What attack method was used to gain initial access?

**Respuesta / Answer:**

```
Phishing
```

**Pregunta / Question:** Can you find the attacker's email address?

**Respuesta / Answer:**

```
akeane@poseidonenergy.net
```

**Pregunta / Question:** What command did the attacker run as j.morgan to gain access to the r.house account?

**Respuesta / Answer:**

```
sudo nano /home/r.house/.ssh/authorized_keys
```

**Pregunta / Question:** What is the full path of the archive used to steal RobbCo's source code?

**Respuesta / Answer:**

```
/dev/shm/.core_dump_2025.tgz.enc
```

---

> **Nota:** Esta room no contiene flags tradicionales `THM{...}` — las respuestas son hallazgos de la investigación forense descrita arriba.
> **Note:** This room has no traditional `THM{...}` flags — answers are investigative findings from the forensic analysis.

---

*Documentación para propósitos educativos y registro de CTF.*
