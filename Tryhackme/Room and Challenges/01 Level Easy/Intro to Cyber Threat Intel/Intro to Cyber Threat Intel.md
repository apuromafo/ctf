# Intro to Cyber Threat Intel

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtocyberthreatintel` | https://tryhackme.com/room/introtocyberthreatintel | 01 Level Easy | TryHackMe | CTI / ciclo de vida (Direction-Processing) / TAXII / STIX / kill chain / análisis de phishing | Conocer qué es la ciberinteligencia de amenazas (CTI), su ciclo de vida, los estándares TAXII/STIX, la kill chain y construir un perfil de amenaza desde un correo de phishing. |

---

**Contexto:** La room introduce la Cyber Threat Intelligence (CTI / Ciberinteligencia de Amenazas): qué significan las siglas (Cyber Threat Intelligence), la clasificación de los datos de amenaza (artefactos como IPs y hashes bajo **Technical Intel**), el ciclo de vida de la inteligencia (**Direction** y **Processing**), los estándares de compartición **TAXII** (modelos Collection y Channel) y **STIX**, la cyber kill chain (fase **Actions on Objectives** al exfiltrar datos) y un análisis práctico de un correo de phishing.

> **ES:** Ciberinteligencia de amenazas: definición, tipos de inteligencia, ciclo de vida, estándares TAXII/STIX, kill chain y análisis práctico de un phishing para construir el perfil de la amenaza.
> **EN:** Cyber threat intelligence: definition, intelligence types, lifecycle, TAXII/STIX standards, kill chain and a practical phishing analysis to build the threat profile.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presentación de la room, objetivos y glosario base sobre inteligencia de amenazas. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ready to get started! / Listo para empezar. | `No answer needed` |

### Task 2: Cyber Threat Intelligence / Ciberinteligencia de amenazas

**Explicación:** CTI significa **Cyber Threat Intelligence** (ciberinteligencia de amenazas): información estudiada y analizada sobre las amenazas que afectan a la organización, para tomar mejores decisiones. Los artefactos técnicos como direcciones IP, hashes y otros indicadores se encuentran en la clasificación **Technical Intel** (inteligencia técnica).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does CTI stand for? / ¿Qué significan las siglas CTI? | `Cyber Threat Intelligence` |
| 2 | IP addresses, Hashes and other threat artefacts would be found under which Threat Intelligence classification? / ¿Bajo qué clasificación de Threat Intelligence se encuentran las IPs, los hashes y otros artefactos de amenaza? | `Technical Intel` |

### Task 3: CTI Lifecycle / Ciclo de vida de CTI

**Explicación:** El ciclo de vida de la inteligencia de amenazas tiene varias fases. En la fase **Direction** (dirección), los analistas definen las preguntas a investigar y los objetivos. Los datos se convierten en formatos utilizables mediante ordenación, organización, correlación y presentación en la fase de **Processing** (procesamiento).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | At which phase of the CTI lifecycle is data converted into usable formats through sorting, organising, correlation and presentation? / ¿En qué fase del ciclo de vida de CTI los datos se convierten en formatos utilizables mediante ordenación, organización, correlación y presentación? | `Processing` |
| 2 | During which phase do security analysts get the chance to define the questions to investigate incidents? / ¿En qué fase los analistas de seguridad tienen la oportunidad de definir las preguntas para investigar incidentes? | `Direction` |

### Task 4: CTI Standards & Frameworks / Estándares y frameworks de CTI

**Explicación:** Se presentan los estándares de la industria: **TAXII** (Trusted Automated eXchange of Indicator Information), que soporta los modelos de compartición **Collection and Channel**; y **STIX** (Structured Threat Information eXpression) para estructurar datos. También se introduce la cyber kill chain: cuando el adversario ya accedió a la red y está extrayendo datos, se encuentra en la fase **Actions on Objectives** (acciones sobre los objetivos).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What sharing models are supported by TAXII? / ¿Qué modelos de compartición soporta TAXII? | `Collection and Channel` |
| 2 | When an adversary has obtained access to a network and is extracting data, what phase of the kill chain are they on? / Cuando el adversario accedió a la red y está extrayendo datos, ¿en qué fase de la kill chain se encuentra? | `Actions on Objectives` |

### Task 5: Practical Analysis / Análisis práctico

**Explicación:** Ejercicio práctico con un correo de phishing: se inspeccionan las cabeceras y adjuntos del email para identificar el origen, el archivo malicioso y construir un perfil de amenaza. De las cabeceras del correo se obtiene la dirección del remitente (**vipivillain@badbank.com**), el archivo que se descargaba era **flbpfuh.exe**, y al completar el perfil de la amenaza se entrega la flag final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What was the source email address? / ¿Cuál era la dirección de correo de origen? | `vipivillain@badbank.com` |
| 2 | What was the name of the file downloaded? / ¿Cuál era el nombre del archivo descargado? | `flbpfuh.exe` |
| 3 | After building the threat profile, what message do you receive? / Tras construir el perfil de la amenaza, ¿qué mensaje recibes? | `THM{NOW_I_CAN_CTI}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does CTI stand for? | `Cyber Threat Intelligence` |
| 2 | IP addresses, Hashes and other threat artefacts would be found under which Threat Intelligence classification? | `Technical Intel` |
| 3 | At which phase of the CTI lifecycle is data converted into usable formats through sorting, organising, correlation and presentation? | `Processing` |
| 4 | During which phase do security analysts get the chance to define the questions to investigate incidents? | `Direction` |
| 5 | What sharing models are supported by TAXII? | `Collection and Channel` |
| 6 | When an adversary has obtained access to a network and is extracting data, what phase of the kill chain are they on? | `Actions on Objectives` |
| 7 | What was the source email address? | `vipivillain@badbank.com` |
| 8 | What was the name of the file downloaded? | `flbpfuh.exe` |
| 9 | After building the threat profile, what message do you receive? | `THM{NOW_I_CAN_CTI}` |

---

**Metodología:** Del concepto a la práctica: (1) definir CTI y sus tipos de inteligencia (Technical Intel); (2) recorrer el ciclo de vida (Direction -> Processing); (3) conocer los estándares de compartición TAXII (Collection/Channel) y la kill chain (Actions on Objectives); (4) aplicar todo en el análisis forense de un correo de phishing: extraer remitente, archivo adjunto y construir el perfil de la amenaza.

### Cadena de ataque / Attack Chain

```text
Phishing email (vipivillain@badbank.com) -> flbpfuh.exe descargado -> perfil de amenaza construido -> THM flag
```

**Learning chain:** Definicion de CTI -> tipos de inteligencia -> ciclo de vida -> TAXII/STIX -> kill chain -> analisis de phishing.

**Lección:** *La inteligencia no es el dato crudo: un email, un archivo o un hash solo se convierten en CTI cuando pasan por el ciclo (Direction, Processing) y se integran en el contexto de la organización.*

**MITRE ATT&CK:** T1566 (Phishing), T1204.002 (User Execution: Malicious File), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Intro to Cyber Threat Intel](https://tryhackme.com/room/introtocyberthreatintel)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.