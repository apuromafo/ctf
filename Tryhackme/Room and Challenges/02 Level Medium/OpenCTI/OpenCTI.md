# OpenCTI

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | opencti | https://tryhackme.com/room/opencti | 02 Level Medium | TryHackMe | OpenCTI, Carbon Black, MITRE ATT&CK, Threat Intelligence, Malware, Intrusion Sets | Aprender a usar OpenCTI como plataforma de threat intelligence: explorar cómo se enriquecen los datos, buscar grupos avanzados (APT/Intrusion Sets), analizar malware e indicadores y correlacionar los resultados con MITRE ATT&CK. |

---

**Contexto:** La sala **OpenCTI** es un laboratorio de **threat intelligence** en el que se utilizan los datos de una empresa de ejemplo recopilados con **Carbon Black** e importados en **OpenCTI**. El alumno aprende a moverse por la interfaz, a usar la vista **Enrichment**, a consultar grupos de actores (Intrusion Sets / APT), a analizar malware e indicadores y a responder preguntas sobre los grupos, sus técnicas MITRE ATT&CK y los datos asociados. Es la introducción práctica a OpenCTI, la plataforma de inteligencia de amenazas de código abierto.

> **ES:** Room de threat intelligence en la que se practica con OpenCTI: explorar telemetría de Carbón Black, buscar grupos APT, analizar malware y mapearlo a MITRE ATT&CK, pisando los pasos de la investigación de Watches Plc.
> **EN:** A threat intelligence room practising with OpenCTI: explore Carbon Black telemetry, hunt APT groups, analyse malware, and map it to MITRE ATT&CK following the Watches Plc investigation.

## Solucionario

### Task 1: ¡Comencemos! / Let's Get Started!
**Explicación:** Presentación del escenario: la plataforma OpenCTI como herramienta de threat intelligence para consumir y correlacionar datos (telemetría) y producir inteligencia accionable. No hay pregunta que responder en esta tarea.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Welcome to the OpenCTI room (no answer required). / Bienvenido a la sala OpenCTI. | `No answer needed` |

### Task 2: Empieza a Explorar / Start to Explore
**Explicación:** Con el login proporcionado por la sala se accede a OpenCTI y se explora el dashboard y las vistas de entidades. No hay preguntas; la tarea es puramente de familiarización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explore the dashboard and be-familiarised with the platform (no answer required). | `No answer needed` |

### Task 3: Cómo Se Enriquecen Los Datos / How Data Gets Enriched
**Explicación:** Se aprende la vista **Enrichment** de OpenCTI y cómo los datos importados (en este caso telemetría de Carbon Black, "Horizon Data") se enriquecen con conexiones externas. El grupo que usa el malware **4H RAT** es **Putter Panda**; la fase del kill-chain vinculada al **Command-Line Interface Attack Pattern** es **Execution-ics**; y dentro de la categoría **Activities**, la pestaña que aloja los **Indicators** es **Observations**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the group that uses the 4H RAT malware? / ¿Cómo se llama el grupo que usa el malware 4H RAT? | `Putter Panda` |
| 2 | What kill-chain phase is linked with the Command-Line Interface Attack Pattern? / ¿Qué fase del kill-chain está ligada al Command-Line Interface Attack Pattern? | `Execution-ics` |
| 3 | Within the Activities category, which tab would house the Indicators? / En la categoría Activities, ¿qué pestaña aloja los Indicators? | `Observations` |

### Task 4: Ve A Cazar (APTs) / Go Hunt!
**Explicación:** Con la pestaña **Threats → Threat Actors** se exploran los grupos del entorno de Watches Plc. Los **Intrusion Sets** asociados al malware **Cobalt Strike** con nivel de confianza *Good* son **CopyKittens** y **FIN7**, y el **autor de la entidad** es **The MITRE Corporation**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What Intrusion sets are associated with the Cobalt Strike malware with a Good confidence level? (Intrusion1, Intrusion2) / ¿Qué Intrusion Sets se asocian al malware Cobalt Strike con confianza Good? | `CopyKittens, FIN7` |
| 2 | Who is the author of the entity? / ¿Quién es el autor de la entidad? | `The MITRE Corporation` |

### Task 5: Ve Más Allá De La Telemetría / Go Beyond the Telemetry
**Explicación:** Se profundiza en el malware y los indicadores con entidades como **CaddyWiper**: la fecha más temprana registrada es **2022/03/15**, la técnica de ejecución usada por el malware es **Native API**, se vinculan **113** relaciones de malware a dicha técnica, y en 2016 esa técnica usó las herramientas **BloodHound**, **Empire** y **ShimRatReporter**. Por último, el grupo **APT37** está asociado con **North Korea** y usa para su acceso inicial las técnicas **T1189** y **T1566**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the earliest date recorded related to CaddyWiper? Format: YYYY/MM/DD | `2022/03/15` |
| 2 | Which Attack technique is used by the malware for execution? / ¿Qué técnica ATT&CK usa el malware para ejecución? | `Native API` |
| 3 | How many malware relations are linked to this Attack technique? / ¿Cuántas relaciones de malware se vinculan a esa técnica? | `113` |
| 4 | Which 3 tools were used by the Attack Technique in 2016? (Ans: Tool1, Tool2, Tool3) | `BloodHound, Empire, ShimRatReporter` |
| 5 | What country is APT37 associated with? / ¿A qué país está asociado APT37? | `North Korea` |
| 6 | Which Attack techniques are used by the group for initial access? (Ans: Technique1, Technique2) / ¿Qué técnicas ATT&CK usa el grupo para acceso inicial? | `T1189, T1566` |

### Task 6: Conclusión / Conclusion
**Explicación:** Cierre de la sala; se repasa el flujo completo de consumo de inteligencia: datos → enriquecimiento → caza de grupos → malware → correlación ATT&CK.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Summarise what you have learnt (no answer required). | `No answer needed` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Welcome to OpenCTI. | `No answer needed` |
| 2 | (Task 2) Exploración del dashboard. | `No answer needed` |
| 3 | (Task 3) Name of the group that uses the 4H RAT malware. | `Putter Panda` |
| 4 | (Task 3) Kill-chain phase linked with the Command-Line Interface Attack Pattern. | `Execution-ics` |
| 5 | (Task 3) Tab that houses the Indicators within the Activities category. | `Observations` |
| 6 | (Task 4) Intrusion sets associated with Cobalt Strike (Good confidence). | `CopyKittens, FIN7` |
| 7 | (Task 4) Who is the author of the entity? | `The MITRE Corporation` |
| 8 | (Task 5) Earliest date recorded related to CaddyWiper (YYYY/MM/DD). | `2022/03/15` |
| 9 | (Task 5) Attack technique used by the malware for execution. | `Native API` |
| 10 | (Task 5) Number of malware relations linked to that technique. | `113` |
| 11 | (Task 5) 3 tools used by the Attack Technique in 2016. | `BloodHound, Empire, ShimRatReporter` |
| 12 | (Task 5) Country associated with APT37. | `North Korea` |
| 13 | (Task 5) Techniques used by the group for initial access. | `T1189, T1566` |
| 14 | (Task 6) Conclusión. | `No answer needed` |

---

**Metodología:** Login en OpenCTI → exploración del dashboard y vistas (Enrichment, Threat Actors, Malware) → búsqueda de entidades y sus técnicas principales → caza de grupos APT (CopyKittens, FIN7) → consulta de información adicional en MalwareBazaar → correlación de malware con técnicas MITRE ATT&CK → conclusiones de la investigación de Watches Plc.

**Learning chain:** OpenCTI como plataforma de CTI → enriquecimiento de datos → caza de grupos avanzados (APT) → análisis de malware → mapping a MITRE ATT&CK → inteligencia accionable.

**Lección:** *La inteligencia de amenazas solo es útil cuando se enriquece y se correlaciona: una plataforma como OpenCTI convierte telemetría cruda en conocimiento accionable sobre grupos, malware y técnicas.*

**MITRE ATT&CK:** T1046 (Network Service Discovery) · T1190 (Exploit Public-Facing Application) · T1566.001 (Phishing: Spearphishing Attachment) · T1189 (Drive-by Compromise) · T1059.006 (Command and Scripting Interpreter: Python) · T1083 (File and Directory Discovery).

**Fuente:** [TryHackMe - OpenCTI](https://tryhackme.com/room/opencti)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.