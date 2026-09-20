# Detection Rules Development

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `detectionrulesdevelopment` | https://tryhackme.com/room/detectionrulesdevelopment | Detection Engineering | TryHackMe | Elastic SIEM, custom queries, ML rules, threshold rules, EQL | Medium |

---

**Contexto:** Este room se enfoca en el desarrollo y tuning de reglas de detección dentro de Elastic SIEM. Aprenderemos a crear Custom Queries, reglas de umbral y secuencias EQL, identificar falsos positivos, configurar suppressión y aplicar estrategias de tuning para maximizar la detección de amenazas reales como password spraying y Lateral Movement.

> **ES:** Desarrollo y ajuste de reglas de detección en Elastic SIEM: Custom Queries, reglas de umbral, secuencias EQL, Machine Learning, falsos positivos, supresión y tuning.
> **EN:** Building and tuning detection rules in Elastic SIEM: Custom Queries, threshold rules, EQL sequences, Machine Learning, false positives, suppression and tuning.

## Solucionario

### Task 1: Construcción de una regla de Custom Query / Building a Custom Query Rule

**Explicación:** Se crea una regla de tipo Custom Query en Elastic SIEM para detectar la ejecución de comandos de reconocimiento. La consulta sugerida revela al usuario que ejecutó los comandos (`tryhatme.thm\sysadmin`), identifica un falso positivo en los resultados (`ngentask.exe`) y muestra que falta una herramienta usada por el atacante (`nltest.exe`). Con estos datos se ajusta la consulta base.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user executed the recon commands? | `tryhatme.thm\sysadmin` |
| 2 | What is the Image of a false-positive identified in the results of the suggested query? | `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngentask.exe` |
| 3 | What is the executable name of the recon tool used by the attacker that is missing in the suggested query? | `nltest.exe` |

### Task 2: Afinando reglas de Custom Query / Tuning Custom Query Rules

**Explicación:** Se analiza el volumen de alertas generadas por la regla afinada: al generar una alerta por cada comando de reconocimiento ejecutado por el atacante se obtienen `22` alertas. Se repasa de nuevo que el tipo de regla responsable de crear detecciones atómicas en Elastic es `Custom Query`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Considering that 1 alert was generated for each recon command performed by the attacker, how many alerts were generated? | `22` |
| 2 | What is the name of the detection rule type responsible for creating atomic detections on Elastic? | `Custom Query` |

### Task 3: Construcción de una regla de umbral / Building a Threshold Rule

**Explicación:** Se construye una regla de umbral (Threshold) para detectar un patrón de password spraying. Se obtienen `5` alertas relacionadas con el patrón, la IP del atacante es `5.62.18.132` con `50` intentos fallidos totales, el atacante probó `12` usuarios y el mejor campo de supresión para la detección es `source.ip`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many alerts were generated related to a password spraying pattern? | `5` |
| 2 | What is the attack IP, and how many total failure attempts did the attacker IP have? | `5.62.18.132`, `50` |
| 3 | How many usernames did the attacker test? | `12` |
| 4 | What field would be the best to be configured as a suppression field for your detection? | `source.ip` |

### Task 4: Construcción de una regla de secuencia EQL / Building an EQL Sequence Rule

**Explicación:** Se crea una regla de secuencia EQL. Eliminar la condición `with runs` del evento reduciría las alertas duplicadas, pero haría que la detección fuese más susceptible de generar alertas del tipo `True Positive`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Removing the with runs condition from the EQL sequence would reduce the number of duplicate alerts. What type of alerts would your detection be more susceptible to generating with that change? | `True Positive` |

### Task 5: Reglas de Machine Learning en Elastic / Elastic Machine Learning Rules

**Explicación:** Se exploran las reglas de Machine Learning de Elastic: el tipo de regla que usa trabajos de detección de anomalías y líneas base estadísticas para identificar desviaciones de la actividad normal es `Machine Learning`. Un usuario que inicia sesión entre 08:00 y 18:00 y autentica a las 03:00 es anómalo solo por el contexto temporal: una anomalía `Contextual`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Elastic rule type uses anomaly detection jobs and statistical baselines to identify deviations from normal activity? | `Machine Learning` |
| 2 | A user who normally logs in between 08:00 and 18:00 authenticates at 03:00. This data point is only abnormal because of the timing context. What type of anomaly is this? | `Contextual` |

### Task 6: Traza de ataque y tuning / Attack Trace and Tuning

**Explicación:** Se reconstruye la traza del ataque: el LogonId del atacante es `0x557e9`. Aplicando la estrategia de tuning correspondiente se reduce el ruido sin perder la detección: la estrategia aplicada es `Threshold`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the attacker's LogonId? | `0x557e9` |
| 2 | What type of tuning strategy did you apply in this task? | `Threshold` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user executed the recon commands? | `tryhatme.thm\sysadmin` |
| 2 | What is the Image of a false-positive identified in the results of the suggested query? | `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngentask.exe` |
| 3 | What is the executable name of the recon tool used by the attacker that is missing in the suggested query? | `nltest.exe` |
| 4 | Considering that 1 alert was generated for each recon command performed by the attacker, how many alerts were generated? | `22` |
| 5 | What is the name of the detection rule type responsible for creating atomic detections on Elastic? | `Custom Query` |
| 6 | How many alerts were generated related to a password spraying pattern? | `5` |
| 7 | What is the attack IP, and how many total failure attempts did the attacker IP have? | `5.62.18.132`, `50` |
| 8 | How many usernames did the attacker test? | `12` |
| 9 | What field would be the best to be configured as a suppression field for your detection? | `source.ip` |
| 10 | Removing the with runs condition from the EQL sequence would reduce the number of duplicate alerts. What type of alerts would your detection be more susceptible to generating with that change? | `True Positive` |
| 11 | What Elastic rule type uses anomaly detection jobs and statistical baselines to identify deviations from normal activity? | `Machine Learning` |
| 12 | A user who normally logs in between 08:00 and 18:00 authenticates at 03:00. This data point is only abnormal because of the timing context. What type of anomaly is this? | `Contextual` |
| 13 | What is the attacker's LogonId? | `0x557e9` |
| 14 | What type of tuning strategy did you apply in this task? | `Threshold` |

---

**Metodología:** El room recorre el ciclo completo de Detection Engineering en Elastic SIEM: desde la creación de reglas Custom Query pasando por umbral y secuencias EQL, hasta Machine Learning para anomalías contextuales. Se practica la identificación de falsos positivos, la supresión por campos como `source.ip` y el tuning con estrategias de threshold para reducir ruido sin perder cobertura.

### Cadena de ataque / Attack Chain

```text
Reconocimiento con nltest.exe (usuario tryhatme.thm\sysadmin) -> 22 alertas de Custom Query -> password spraying (5.62.18.132, 50 fallos, 12 usuarios) -> regla Threshold con supresión source.ip -> secuencia EQL (riesgo de True Positives) -> anomalía contextual de ML (login 03:00) -> LogonId 0x557e9 -> tuning Threshold
```

**Learning chain:** Custom Query → False Positive identification → Threshold rules → EQL sequences → Machine Learning anomaly detection → Tuning strategies (suppression, threshold)

**Lección:** *Una regla de detección no termina al crearla: el tuning continuo —identificando falsos positivos, eligiendo el campo de supresión correcto como `source.ip` y ajustando umbrales— es lo que separa una alerta accionable del ruido del SOC.*

**MITRE ATT&CK:** T1078 - Valid Accounts, T1110 - Brute Force (Password Spraying), T1071 - Application Layer Protocol

**Fuente:** [TryHackMe - Detection Rules Development](https://tryhackme.com/room/detectionrulesdevelopment)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.