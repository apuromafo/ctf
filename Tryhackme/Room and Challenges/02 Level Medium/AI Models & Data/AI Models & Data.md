# AI Models & Data [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory + Practical Lab
* **Slug:** `aimodelsdata`
* **Link:** https://tryhackme.com/room/aimodelsdata
* **Sección / Section:** AI Fundamentals (Section 1 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\03-ai-models-and-data\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

Una inmersión profunda en de dónde viene la data de entrenamiento de la IA, por qué importa para la seguridad, y qué riesgos están horneados en los modelos antes de que se desplieguen. Cubre la procedencia de datos, PII en datos de entrenamiento, decisiones clave de construcción de modelos, el problema de la herencia con el fine-tuning, y por qué los modelos entrenados son cajas negras opacas.

### Conceptos Clave / Key Concepts

#### Data Provenance
La capacidad de responder tres preguntas sobre cualquier pieza de data de entrenamiento: de dónde vino, cuándo se recopiló, y si ha sido modificada. En la práctica, la mayoría de organizaciones que despliegan IA hoy no pueden responder completamente ninguna de estas. La Data Provenance Initiative auditó 1,800+ datasets y encontró que más del 70% de las licencias figuran como "Unspecified".

#### Common Crawl
El corpus público más usado que sustenta esencialmente a toda familia de modelos importante. Es un web scrape masivo — 400TB+ — y Truffle Security encontró casi **12,000 API keys y contraseñas vivas y verificadas** solo en el archivo de diciembre 2024. Una vez en la data de entrenamiento, las credenciales pueden ser extraídas al promptear el modelo — y ningún parche lo arregla post-despliegue.

#### ML-BOM (Machine Learning Bill of Materials)
El equivalente IA de un Software Bill of Materials (SBOM). Un inventario documentado de fuentes de datasets, licencias, categorías de PII, y decisiones de filtrado. La adopción aún es temprana; la mayoría de organizaciones no tienen nada parecido.

#### Conceptos Clave de Construcción de Modelos
| Concepto | Definición | Riesgo de Seguridad |
|---------|-----------|---------------|
| Epoch | Un pase completo de la data de entrenamiento por el algoritmo | Más epochs → más riesgo de overfitting |
| Overfitting | El modelo memoriza la data de entrenamiento en vez de aprender patrones | Puede reproducir data sensible de entrenamiento verbatim al promptear |
| Quantisation | Reduce la precisión numérica de los pesos para cortar memoria/cómputo | Trade-offs de seguridad raramente documentados; hereda comportamiento desconocido |
| Federated Learning | Entrena a través de dispositivos descentralizados; solo se envían actualizaciones de pesos | Los participantes pueden enviar actualizaciones de gradiente envenenadas — muy difícil de detectar |
| Validation Set | Data retenida que nunca se usa en entrenamiento, usada para detectar overfitting | Omitirlo = comportamiento real desconocido = riesgo de seguridad |

#### El Problema de la Herencia
Fine-tunear un modelo pre-entrenado significa heredar **todo** lo que hay debajo:
- Los sesgos horneados durante el pre-entrenamiento persisten
- La alineación de seguridad se erosiona — Stanford/Princeton encontró que puede romperse con tan solo **10 ejemplos de fine-tuning adversariamente diseñados** por menos de $0.20
- Los modelos fine-tuneados son **mediblemente más susceptibles a prompt injection** que sus modelos base (investigación de Cisco)
- El fine-tuning siempre apunta a un checkpoint específico — si ese checkpoint tenía un backdoor, todo derivado lo hereda

#### El Problema de la Caja Negra
Los pesos de un modelo entrenado son miles de millones de números de punto flotante sin registro legible por humanos de qué los moldeó. No puedes auditar un modelo como auditas código. El testing de seguridad solo puede **muestrear comportamiento** — no puede auditar la superficie de ataque completa. Los model cards son el mecanismo principal de transparencia, pero siguen siendo voluntarios, frecuentemente incompletos, o totalmente ausentes.

### Tarea 1 — Introducción / Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I understand the learning objectives and am ready to learn about AI models and data! | `No answer needed` |

### Tarea 2 — Data de Entrenamiento / Training Data

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What term describes the ability to answer where data came from, when it was collected, and whether it has been modified? | `Data Provenance` |
| What is the name of the most widely used public corpus that underpins essentially every major model family? | `Common Crawl` |
| What is the AI equivalent of a Software Bill of Materials (SBOM), used to document dataset sources, licenses, and filtering decisions? | `ML-BOM` |

### Tarea 3 — Construyendo el Modelo / Building the Model

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What term describes one complete pass of the training algorithm through the entire dataset? | `Epoch` |
| What problem occurs when a model memorises training data rather than learning general patterns? | `Overfitting` |
| What post-training optimisation technique reduces the numerical precision of model weights to cut memory and compute requirements? | `Quantisation` |
| What training approach trains a model across decentralised devices, sending only weight updates rather than raw data to a central server? | `Federated Learning` |

### Tarea 4 — El Problema de la Herencia / The Inheritance Problem

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the process of taking a pre-trained model and continuing to train it on a smaller, task-specific dataset? | `Fine-tuning` |
| What term describes a model that has already been trained on a large general-purpose dataset? | `Pre-trained Model` |

### Tarea 5 — El Problema de la Caja Negra / The Black Box Problem

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What documentation artifact accompanies a model to describe what it is, how it was built, and where it falls short? | `Model Card` |
| What are the billions of floating-point numbers that make up a trained model collectively referred to as? | `Weights` |

### Tarea 6 — Práctica (Auditoría de Model Card) / Practical (Model Card Audit)

Un repositorio simulado estilo HuggingFace. Realiza una auditoría de seguridad de un model card, identificando red flags a través de metadatos, listados de archivos, y detalles de entrenamiento. Cada hallazgo se califica por severidad.

**Red flags encontrados y sus severidades:**

| Hallazgo / Finding | Severidad / Severity |
|---------|----------|
| Training data from publicly available web sources | High |
| Training data includes forums and Q&A sites | High |
| Base model: `enterprise-base-v1.1` (unverified) | Medium |
| Macro-averaged F1 score of 0.91 only (limited eval) | Medium |
| Custom licence — contact vendor for terms | Medium |
| Model file size: 268 MB (unexpectedly small) | Medium |

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Complete the exercise to get the flag! | `THM{A_m0del_Stud3nt}` |

### Tarea 7 — Conclusión / Conclusion

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| All Done! | `No answer needed` |

---

## 🚩 Flags

| Flag | Valor / Value |
|------|-------|
| Task 6 — Model Card Audit | `THM{A_m0del_Stud3nt}` |

---

### Qué Enseña Esta Sala / What This Room Teaches You

- "Los riesgos no comienzan cuando un modelo se despliega. Comienzan mucho antes." — la cadena de suministro de datos es tan real como la cadena de suministro de software.
- Un model card ausente o vago es una advertencia de seguridad, no una molestia menor.
- El federated learning resuelve el problema de privacidad de datos pero crea un nuevo problema de envenenamiento de gradientes — los trade-offs de seguridad siempre se apilan.
- El fine-tuning es poderoso pero no sanitiza lo que hay debajo; heredas la historia completa del modelo base.

---

* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\03-ai-models-and-data\README.md`

*Documentación para propósitos educativos y registro de CTF.*
