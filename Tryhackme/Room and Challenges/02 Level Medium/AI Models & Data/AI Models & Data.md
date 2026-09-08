# AI Models & Data
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `aimodelsdata` |
| **Link** | [TryHackMe](https://tryhackme.com/room/aimodelsdata) |
| **Sección** | AI Fundamentals (Section 1 of 5) |
| **Fuente** | [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-1-AI-Fundamentals\03-ai-models-and-data\README.md` |
| **Componentes** | IA/ML, Data Provenance, Common Crawl, ML-BOM, entrenamiento (epoch, overfitting, quantisation, federated learning), fine-tuning, model cards, HuggingFace |
| **Impacto** | Inmersión en el origen de la data de entrenamiento de IA y sus riesgos de seguridad pre-despliegue: procedencia de datos, PII, decisiones de construcción del modelo, problema de herencia del fine-tuning y la caja negra de los pesos. |
---
**Contexto:** Inmersión profunda en de dónde viene la data de entrenamiento de la IA, por qué importa para la seguridad y qué riesgos están horneados en los modelos antes de que se desplieguen. Cubre la procedencia de datos, PII en datos de entrenamiento, decisiones clave de construcción de modelos, el problema de la herencia con el fine-tuning y por qué los modelos entrenados son cajas negras opacas.
*EN: A deep dive into where AI training data comes from, why it matters for security, and what risks are baked into models before deployment. Covers data provenance, PII in training data, key model-building decisions, the inheritance problem with fine-tuning, and why trained models are opaque black boxes.*
## Solucionario
### Task 1 — Introducción / Introduction
**Explicación:** Objetivos de aprendizaje de la sala: entender el origen de los datos de entrenamiento y su impacto en seguridad.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to learn about AI models and data! | `No answer needed` |
### Task 2 — Data de Entrenamiento / Training Data
**Explicación:** **Data Provenance** es la capacidad de responder de dónde vino la data, cuándo se recopiló y si ha sido modificada (la mayoría de organizaciones no pueden responderlo; la Data Provenance Initiative auditó 1800+ datasets y el 70%+ de licencias figuran como "Unspecified"). **Common Crawl** es el corpus público más usado que sustenta a toda familia de modelos importante (web scrape de 400TB+; Truffle Security halló casi 12,000 API keys y contraseñas vivas solo en el archivo de diciembre 2024). El **ML-BOM** (Machine Learning Bill of Materials) es el equivalente IA de un SBOM: inventario de fuentes de datasets, licencias, categorías de PII y decisiones de filtrado.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What term describes the ability to answer where data came from, when it was collected, and whether it has been modified? | `Data Provenance` |
| 2 | What is the name of the most widely used public corpus that underpins essentially every major model family? | `Common Crawl` |
| 3 | What is the AI equivalent of a Software Bill of Materials (SBOM), used to document dataset sources, licenses, and filtering decisions? | `ML-BOM` |
### Task 3 — Construyendo el Modelo / Building the Model
**Explicación:** Conceptos clave de construcción de modelos y sus riesgos:
- **Epoch:** un pase completo de la data de entrenamiento por el algoritmo → más epochs = más riesgo de overfitting.
- **Overfitting:** el modelo memoriza la data en vez de aprender patrones → puede reproducir data sensible verbatim al promptear.
- **Quantisation:** reduce la precisión numérica de los pesos para cortar memoria/cómputo → trade-offs de seguridad raramente documentados; hereda comportamiento desconocido.
- **Federated Learning:** entrena a través de dispositivos descentralizados enviando solo actualizaciones de pesos → los participantes pueden enviar gradientes envenenados, muy difíciles de detectar.
- **Validation Set:** data retenida que nunca se usa en entrenamiento para detectar overfitting → omitirlo = comportamiento real desconocido = riesgo.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What term describes one complete pass of the training algorithm through the entire dataset? | `Epoch` |
| 2 | What problem occurs when a model memorises training data rather than learning general patterns? | `Overfitting` |
| 3 | What post-training optimisation technique reduces the numerical precision of model weights to cut memory and compute requirements? | `Quantisation` |
| 4 | What training approach trains a model across decentralised devices, sending only weight updates rather than raw data to a central server? | `Federated Learning` |
### Task 4 — El Problema de la Herencia / The Inheritance Problem
**Explicación:** Fine-tunear un modelo pre-entrenado significa heredar **todo** lo que hay debajo: los sesgos del pre-entrenamiento persisten; la alineación de seguridad se erosiona (Stanford/Princeton: se puede romper con tan solo 10 ejemplos adversarios por menos de $0.20); los modelos fine-tuneados son mediblemente más susceptibles a prompt injection que sus modelos base (Cisco); y el fine-tuning apunta a un checkpoint concreto — si éste tenía un backdoor, todo derivado lo hereda.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the process of taking a pre-trained model and continuing to train it on a smaller, task-specific dataset? | `Fine-tuning` |
| 2 | What term describes a model that has already been trained on a large general-purpose dataset? | `Pre-trained Model` |
### Task 5 — El Problema de la Caja Negra / The Black Box Problem
**Explicación:** Los **Weights** de un modelo entrenado son miles de millones de números de punto flotante sin registro legible de qué los moldeó; no puedes auditar un modelo como auditas código. El testing de seguridad solo puede muestrear comportamiento, no auditar la superficie completa. Los **Model Cards** son el mecanismo principal de transparencia, pero siguen siendo voluntarios, frecuentemente incompletos o ausentes.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What documentation artifact accompanies a model to describe what it is, how it was built, and where it falls short? | `Model Card` |
| 2 | What are the billions of floating-point numbers that make up a trained model collectively referred to as? | `Weights` |
### Task 6 — Práctica (Auditoría de Model Card) / Practical (Model Card Audit)
**Explicación:** Repositorio simulado estilo HuggingFace. Auditoría de seguridad de un model card identificando red flags por severidad: Training data from publicly available web sources (**High**), Training data includes forums and Q&A sites (**High**), Base model `enterprise-base-v1.1` unverified (**Medium**), F1 score macro-promediado de 0.91 solo (evaluación limitada) (**Medium**), licencia custom — contact vendor (**Medium**), tamaño de archivo 268 MB inusualmente pequeño (**Medium**).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the exercise to get the flag! | `THM{A_m0del_Stud3nt}` |
### Task 7 — Conclusión / Conclusion
**Explicación:** Cierre. Lecciones: los riesgos no comienzan cuando un modelo se despliega, comienzan mucho antes (la cadena de suministro de datos es tan real como la de software); un model card ausente o vago es una advertencia de seguridad; el federated learning resuelve la privacidad pero crea envenenamiento de gradientes; el fine-tuning hereda la historia completa del modelo base.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | All Done! | `No answer needed` |
---
**Metodología:** Teoría de la cadena de suministro de IA (procedencia, corpora, ML-BOM) → construcción de modelos (epoch/overfitting/quantisation/federated) → herencia del fine-tuning → caja negra (weights/model cards) → auditoría práctica de un model card.
**Learning chain:** de dónde viene la data → cómo se construye el modelo → qué se hereda al fine-tunear → cómo se documenta (o no) → auditoría práctica de red flags.
**MITRE ATT&CK / ATLAS:** AML.T0007 (Discover ML Artifacts), AML.T0010 (ML Supply Chain Compromise), AML.T0020 (Data Poisoning), T1195.001 (Compromise Software Dependencies and Development Tools); mitigaciones: M1038 (Execution Prevention), M1016 (Vulnerability Scanning).
**Fuente:** [TryHackMe - AI Models & Data](https://tryhackme.com/room/aimodelsdata)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
