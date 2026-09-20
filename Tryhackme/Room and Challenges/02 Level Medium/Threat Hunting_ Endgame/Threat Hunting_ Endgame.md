# Threat Hunting: Endgame
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Threat Hunting (DFIR) | threathuntingendgame | https://tryhackme.com/room/threathuntingendgame | 02 Level Medium | TryHackMe | Elastic Stack (ELK), KQL, logs de Windows (Security/Sysmon/PowerShell), MITRE ATT&CK, keylogging, exfiltración ICMP, destrucción de shadow copies | Caza de actividades maliciosas en la fase de "Actions on Objectives" (colección, exfiltración e impacto) mediante el análisis de logs |

> **Objeto:** Aprender a cazar y descubrir actividades sospechosas que indican "actions on objectives" (acciones sobre los objetivos).

---
**Contexto:** **Threat Hunting: Endgame** es una sala guiada de dificultad Media centrada en la fase final de la Cyber Kill Chain: **Actions on Objectives**. Se trabaja sobre una instancia de Elastic Stack (ELK) con índices que contienen logs realistas de Windows (`case_collection`, `case_exfiltration` y `case_impact`). A través de consultas KQL se cazan tres tácticas MITRE ATT&CK: **Collection** (keylogging), **Exfiltration** (robo de datos sobre ICMP) e **Impact** (destrucción de shadow copies y manipulación de la recuperación). El objetivo es correlacionar eventos entre múltiples fuentes para identificar los objetivos reales del atacante y reducir el dwell time.
> **ES:** Aprende a cazar y descubrir actividades sospechosas que indican acciones sobre los objetivos.
> **EN:** Learn how to hunt and discover suspicious activities indicating actions on objectives.

## Solucionario
### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: la fase de Actions on Objectives y preguntas clave sobre detección de exfiltración, disrupción y destrucción de datos antes de que causen daño irreversible.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| I am ready to start hunting! | `No answer needed` |

### Task 2: Entender Actions on Objectives / Understanding Actions on Objectives
**Explicación:** Se explican los objetivos habituales del atacante (exfiltración, destrucción de datos, disrupción, cifrado por rescate y manipulación). Se introduce el **Dwell Time** como el tiempo que un actor de amenaza permanece en la red antes de ser detectado y erradicado, y las tácticas MITRE que se van a cazar: Collection (TA0009), Exfiltration (TA0010) e Impact (TA0040).

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the term used for the adversary's lifetime in the network? | `Dwell Time` |

### Task 3: Configuración del laboratorio / Lab Setup
**Explicación:** Se despliega y se accede a la instancia de Elastic Stack (ELK) con la que se realizarán las investigaciones.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| I have started the Elastic Stack instance! | `No answer needed` |

### Task 4: Táctica: Collection / Tactic: Collection
**Explicación:** Se caza actividad de **keylogging**. Mediante patrones de APIs de captura de teclado y el análisis de scripts de PowerShell se descubre un script malicioso (`chrome-update_api.ps1`) que descarga y ejecuta un keylogger y crea una base de datos (`chrome_local_profile.db`). Se identifica el PID del proceso que descarga el script y la cuenta de correo registrada.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the Process ID of the process that downloads the malicious script? | `3388` |
| What is the logged mail account? | `hunted-victim2323@gmail.com` |

### Task 5: Táctica: Exfiltration / Tactic: Exfiltration
**Explicación:** Se caza exfiltración de datos sobre **ICMP**. Se localiza el script `icmp4data.ps1`, que envía el documento exfiltrado en pequeños paquetes ICMP hacia un servidor de destino. Se determinan el número total de paquetes enviados, el tamaño del fragmento (chunk) de cada paquete, el documento exfiltrado y la IP del servidor destino (defangada).

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the total number of sent ICMP packets? | `21` |
| How many bytes (chunk) is the amount of data carried in each packet? | `15` |
| What is the name of the exfiltrated document? | `chrome_local_profile.db` |
| What is the server's IP address (defanged) where the exfiltrated document is sent? | `10[.]10[.]87[.]116` |

### Task 6: Táctica: Impact / Tactic: Impact
**Explicación:** Se caza disrupción de datos y manipulación de la recuperación. Se identifica el ejecutable de sistema usado para eliminar las shadow copies (`vssadmin.exe`), la imagen de shell principal que inicia la cadena de ataque (`powershell.exe`) y el PID desde el que arranca dicha cadena.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the name of the system executable used to remove shadow copies? | `vssadmin.exe` |
| What is the main shell image that started the attack chain? | `powershell.exe` |
| What is the process ID that started the attack chain? | `6512` |

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala y resumen de las metodologías de caza aprendidas para las tácticas de colección, exfiltración e impacto.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| I enjoyed the hunt! | `No answer needed` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to start hunting! | `No answer needed` |
| 2 | What is the term used for the adversary's lifetime in the network? | `Dwell Time` |
| 3 | I have started the Elastic Stack instance! | `No answer needed` |
| 4.1 | What is the Process ID of the process that downloads the malicious script? | `3388` |
| 4.2 | What is the logged mail account? | `hunted-victim2323@gmail.com` |
| 5.1 | What is the total number of sent ICMP packets? | `21` |
| 5.2 | How many bytes (chunk) is the amount of data carried in each packet? | `15` |
| 5.3 | What is the name of the exfiltrated document? | `chrome_local_profile.db` |
| 5.4 | What is the server's IP address (defanged) where the exfiltrated document is sent? | `10[.]10[.]87[.]116` |
| 6.1 | What is the name of the system executable used to remove shadow copies? | `vssadmin.exe` |
| 6.2 | What is the main shell image that started the attack chain? | `powershell.exe` |
| 6.3 | What is the process ID that started the attack chain? | `6512` |
| 7 | I enjoyed the hunt! | `No answer needed` |

---
**Metodología:** Introducción → comprensión de Actions on Objectives (Dwell Time, tácticas TA0009/TA0010/TA0040) → configuración de ELK → caza de Collection (keylogging) → caza de Exfiltration (ICMP) → caza de Impact (shadow copies) → conclusión.

### Cadena de ataque / Attack Chain
```
Introducción -> Actions on Objectives (Dwell Time) -> Lab Setup (Elastic Stack)
-> Collection: keylogger chrome-update_api.ps1 / chrome_local_profile.db (PID 3388, mail hunted-victim2323@gmail.com)
-> Exfiltration (ICMP): 21 paquetes, 15 bytes/chunk, chrome_local_profile.db -> 10[.]10[.]87[.]116
-> Impact: vssadmin.exe elimina shadow copies (powershell.exe, PID 6512) -> Conclusión
```
**Learning chain:** Marco de Actions on Objectives → fuentes de log → consultas KQL → correlación de eventos → identificación de los objetivos del atacante.
**Lección:** *Las acciones sobre objetivos (colección, exfiltración e impacto) dejan rastro en múltiples fuentes de log; correlacionarlas y reducir el dwell time es la esencia del threat hunting.*
**MITRE ATT&CK:** T1056.001 (Input Capture: Keylogging), T1048 (Exfiltration Over Alternative Protocol), T1490 (Inhibit System Recovery), T1485 (Data Destruction).
**Fuente:** [TryHackMe - Threat Hunting: Endgame](https://tryhackme.com/room/threathuntingendgame)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
