# AI Forensics
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `aiforensics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/aiforensics) |
| **Sección** | 02 Level Medium |
| **Fuente** | [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\05-ai-forensics\README.md` |
| **Componentes** | DFIR, IA (Anomaly Detection), redes neuronales convolucionales, machine learning (classify_logs.py, file_anomalies.py), SSH, análisis de logs, autoría de ataques (phishing) |
| **Impacto** | Teoría + práctica de IA aplicada a la investigación forense digital (DFIR): qué capacidades de IA ayudan al investigador y cómo el ML detectó el acceso inicial (phishing) y el robo de código fuente en un incidente real. |
---
**Contexto:** Teoría + práctica (investigación DFIR): la IA ayuda al investigador forense a reconocer patrones no aparentes (Anomaly Detection), revisar logs sociales (Sentiment Analysis) y reconstruir la línea de tiempo del incidente (correlación de Event Data). La parte práctica modela el colapso de RobbCo (Poseidon Energy) investigando con scripts ML `classify_logs.py` y `file_anomalies.py` sobre `auth.log`. Esta room no contiene flags tradicionales `THM{...}` — las respuestas son hallazgos de la investigación forense.
*EN: Theory + practical lab (DFIR Investigation): AI assists the forensic investigator in recognizing hidden patterns (Anomaly Detection), reviewing chat/social tone (Sentiment Analysis) and reconstructing incident timelines (Event Data correlation). The practical part models RobbCo's collapse (Poseidon Energy) investigating with ML scripts `classify_logs.py` and `file_anomalies.py` over `auth.log`. This room has no traditional `THM{...}` flags — answers are investigative findings.*
## Solucionario
### Task 1: Introduction
**Explicación:** Presentación de la sala: el papel de la IA en la investigación forense digital (DFIR).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la sala. | `No answer needed` |
### Task 2: AI in DFIR (Teoría)
**Explicación:** Capacidades de IA usadas en DFIR: detección de anomalías (reconocer patrones que el humano no comprende), no determinismo (misma entrada, distinta salida entre ejecuciones), redes neuronales convolucionales (espacial en imagen/vídeo), análisis de sentimiento (tono emocional en redes sociales/chats), correlación de datos de eventos (reconstruir línea de tiempo) y análisis dinámico (observar el comportamiento del programa, p. ej. secuencia de llamadas API).
*EN: AI abilities used in DFIR: anomaly detection (recognizing patterns a human might not comprehend), nondeterminism (same input, different outputs across runs), convolutional neural networks (spatial patterns in image/video), sentiment analysis (emotional tone in social media/chat logs), event data correlation (auto-reconstructing incident timelines) and dynamic analysis (observing program behavior, e.g. API call sequences).*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What ability of AI helps a DFIR investigator by recognising patterns they might not have been able to comprehend? | `Anomaly Detection` |
| 2 | What term describes the AI characteristic where the same input may yield different outputs across different runs? | `Nondeterminism` |
| 3 | What type of neural network is commonly used in image and video forensics due to its ability to learn spatial patterns in visual data? | `Convolutional Neural Network` |
| 4 | What kind of analysis can be performed on social media or chat logs to assess the emotional tone of messages? | `Sentiment Analysis` |
| 5 | What type of data do AI systems correlate to reconstruct the timeline of an incident automatically? | `Event Data` |
| 6 | What type of analysis observes how a program behaves to determine whether it is malicious, e.g., using its API call sequence? | `Dynamic Analysis` |
### Task 3: The Digital Trail (Investigación práctica)
**Explicación:** SSH a la máquina comprometida como `o.deer` con contraseña `TryHackMe!`. Con `python3 classify_logs.py auth.log` el modelo ML marca los inicios de sesión anómalos y `file_anomalies.py` detecta archivos sospechosos; después se hace la validación humana de cada artefacto. Se encuentra el acceso inicial (03:01:02 como j.morgan), el vector Phishing, el email del atacante, el comando con el que escalaron a la cuenta r.house y el archivo comprimido/cifrado del robo de código fuente.
*EN: SSH into the compromised machine as `o.deer` with password `TryHackMe!`. Running `python3 classify_logs.py auth.log` the ML model flags anomalous logins and `file_anomalies.py` flags suspicious files; then each flagged artifact is human-validated. Findings: the initial access time (03:01:02 as j.morgan), the Phishing vector, the attacker's email, the command used to reach the r.house account and the encrypted archive used to steal RobbCo's source code.*
```bash
ssh o.deer@<ip>   # contraseña: TryHackMe!
python3 classify_logs.py auth.log
python3 file_anomalies.py
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | At what time does the attacker successfully log in as j.morgan? | `03:01:02` |
| 2 | What attack method was used to gain initial access? | `Phishing` |
| 3 | Can you find the attacker's email address? | `akeane@poseidonenergy.net` |
| 4 | What command did the attacker run as j.morgan to gain access to the r.house account? | `sudo nano /home/r.house/.ssh/authorized_keys` |
| 5 | What is the full path of the archive used to steal RobbCo's source code? | `/dev/shm/.core_dump_2025.tgz.enc` |
---
**Metodología:** Teoría de IA en DFIR (anomaly detection, CNN, sentiment analysis, event correlation, dynamic analysis) + práctica con clasificación ML de logs (`classify_logs.py`), detección de anomalías de archivo (`file_anomalies.py`) y validación humana del incidente.
**Learning chain:** capacidades de IA → detección de anomalías → correlación de eventos → análisis del acceso inicial y escalada → localización del archivo exfiltrado.
**MITRE ATT&CK:** T1078 (Valid Accounts), T1098.004 (SSH Authorized Keys), T1566 (Phishing), T1005 (Data from Local System), T1560.001 (Archive via Utility), T1071.001 (Web Protocols).
**Fuente:** [TryHackMe - AI Forensics](https://tryhackme.com/room/aiforensics)