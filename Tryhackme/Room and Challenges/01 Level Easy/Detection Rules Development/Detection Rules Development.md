# Detection Rules Development

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `detectionrulesdevelopment` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/detectionrulesdevelopment) |
| **Sección** | Detection Engineering |
| **Fuente** | THM |
| **Componentes** | Elastic SIEM, custom queries, ML rules, threshold rules, EQL |
| **Impacto** | Medium |

---

**Contexto:** Este room se enfoca en el desarrollo y tuning de reglas de detección dentro de Elastic SIEM. Aprenderemos a crear Custom Queries, reglas de umbral y secuencias EQL, identificar falsos positivos, configurar suppressión y aplicar estrategias de tuning para maximizar la detección de amenazas reales como password spraying y Lateral Movement.

## Solucionario

### Task 1: Building a Custom Query Rule

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user executed the recon commands? | `tryhatme.thm\sysadmin` |
| 2 | What is the Image of a false-positive identified in the results of the suggested query? | `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngentask.exe` |
| 3 | What is the executable name of the recon tool used by the attacker that is missing in the suggested query? | `nltest.exe` |

### Task 2: Tuning Custom Query Rules

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Considering that 1 alert was generated for each recon command performed by the attacker, how many alerts were generated? | `22` |
| 2 | What is the name of the detection rule type responsible for creating atomic detections on Elastic? | `Custom Query` |

### Task 3: Building a Threshold Rule

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many alerts were generated related to a password spraying pattern? | `5` |
| 2 | What is the attack IP, and how many total failure attempts did the attacker IP have? | `5.62.18.132`, `50` |
| 3 | How many usernames did the attacker test? | `12` |
| 4 | What field would be the best to be configured as a suppression field for your detection? | `source.ip` |

### Task 4: Building an EQL Sequence Rule

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Removing the with runs condition from the EQL sequence would reduce the number of duplicate alerts. What type of alerts would your detection be more susceptible to generating with that change? | `True Positive` |

### Task 5: Elastic Machine Learning Rules

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Elastic rule type uses anomaly detection jobs and statistical baselines to identify deviations from normal activity? | `Machine Learning` |
| 2 | A user who normally logs in between 08:00 and 18:00 authenticates at 03:00. This data point is only abnormal because of the timing context. What type of anomaly is this? | `Contextual` |

### Task 6: Attack Trace and Tuning

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the attacker's LogonId? | `0x557e9` |
| 2 | What type of tuning strategy did you apply in this task? | `Threshold` |

---

**Metodología:** El room recorre el ciclo completo de Detection Engineering en Elastic SIEM: desde la creación de reglas Custom Query pasando por umbral y secuencias EQL, hasta Machine Learning para anomalías contextuales. Se practica la identificación de falsos positivos, la supresión por campos como `source.ip` y el tuning con estrategias de threshold para reducir ruido sin perder cobertura.
**Learning chain:** Custom Query → False Positive identification → Threshold rules → EQL sequences → Machine Learning anomaly detection → Tuning strategies (suppression, threshold)
**MITRE ATT&CK:** T1078 - Valid Accounts, T1110 - Brute Force (Password Spraying), T1071 - Application Layer Protocol
**Fuente:** [TryHackMe - Detection Rules Development](https://tryhackme.com/r/room/detectionrulesdevelopment)
