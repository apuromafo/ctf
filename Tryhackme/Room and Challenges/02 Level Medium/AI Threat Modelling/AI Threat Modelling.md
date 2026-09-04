# AI Threat Modelling [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory + Practical Exercise
* **Slug:** `ai-threat-modelling`
* **Link:** https://tryhackme.com/room/ai-threat-modelling
* **Sección / Section:** Secure AI Systems (Section 2 of 5)
* **Fuente / Source:** [vanshksingh/TryHackMe-AI-Security-Path](https://github.com/vanshksingh/TryHackMe-AI-Security-Path) — `ai-threat-modelling\Readme.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

La IA ya está integrada en entornos empresariales a través de chatbots de soporte, motores de recomendación y sistemas de detección de fraude. Estos sistemas introducen nuevas superficies de ataque que los frameworks tradicionales de threat modelling no fueron diseñados para abordar por completo. Esta room enseña a identificar activos y superficies de ataque específicos de IA, aplicar STRIDE a sistemas de IA/ML, usar MITRE ATLAS para enumerar amenazas de IA, mapear riesgos con OWASP LLM Top 10 y producir evaluaciones de amenazas de IA estructuradas.

> Esta room está enfocada en defensa: analizar y documentar amenazas de IA en lugar de explotarlas.

### Escenario / Scenario — MegaCorp

Te uniste al equipo de seguridad de MegaCorp como Threat Analyst. La empresa usa IA en varias áreas:

* **Customer Chatbot:** Chatbot con LLM conectado a bases de conocimiento internas mediante RAG.
* **Recommendation Engine:** Procesa datos sensibles de clientes y genera recomendaciones personalizadas de productos.
* **Fraud Detection System:** Realiza decisiones de autorización de transacciones en tiempo real.

El CISO quiere una evaluación completa de amenazas de IA antes de la reunión trimestral de la junta por preocupaciones sobre manipulación de IA, robo de modelo/datos, prompt injection y comportamiento impredecible de la IA.

---

### Tarea 1 — Introducción / Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I understand the learning objectives and am ready to learn about AI threat modelling! | `No answer needed` |

**Riesgos clave de seguridad de IA:** Los frameworks tradicionales como STRIDE siguen siendo útiles, pero los sistemas de IA añaden amenazas únicas como envenenamiento de datos de entrenamiento, robo de modelo, prompt injection, fuga de datos sensibles y salidas no deterministas. Los sistemas de IA pueden comportarse de forma diferente para la misma entrada, haciendo el análisis de amenazas más complejo que en aplicaciones tradicionales.

---

### Tarea 2 — Activos Específicos de IA y Superficies de Ataque / AI-Specific Assets and Attack Surfaces

Las aplicaciones tradicionales se centran en activos como bases de datos, API keys, código fuente, credenciales y archivos de configuración. Los sistemas de IA introducen categorías de activos completamente nuevas que requieren consideraciones de seguridad separadas.

**Activos específicos de IA:**

| Activo | Descripción | Riesgo de Seguridad |
| --- | --- | --- |
| **Training Data** | Datos usados para entrenar el modelo | Datos envenenados pueden alterar permanentemente el comportamiento del modelo |
| **Model Weights / Parameters** | Valores numéricos que representan el comportamiento aprendido | El robo da a los atacantes una copia completa del modelo de IA |
| **Embedding Vectors** | Representaciones numéricas usadas en RAG y sistemas de recomendación | La manipulación afecta la precisión de recuperación y las decisiones del modelo |
| **System Prompts** | Instrucciones que controlan el comportamiento y las restricciones del LLM | La fuga expone guardarraíles y lógica interna |
| **Feature Stores** | Datos preprocesados que alimentan la inferencia del modelo en vivo | La manipulación cambia lo que el modelo ve durante la ejecución |
| **Model Registry / Artifacts** | Versiones de modelos entrenados almacenadas para despliegue | Los atacantes pueden reemplazar modelos legítimos con maliciosos |

**Por qué importan los activos de IA:** A diferencia de los sistemas tradicionales, los pesos de modelo robados no pueden simplemente "rotarse" como contraseñas; los datos de entrenamiento envenenados pueden permanecer sin detectar hasta el reentrenamiento; la fuga de prompts expone controles internos; y los embeddings manipulados pueden influir silenciosamente en las salidas de IA. Los compromisos de IA a menudo afectan el comportamiento del modelo en sí, no solo los datos almacenados.

**Características de los sistemas de IA:**
* **Comportamiento no determinista:** Los modelos de IA pueden generar salidas diferentes para la misma entrada, haciendo el testing más difícil, la reproducción de incidentes complicada y la validación de seguridad menos predecible.
* **Problema de caja negra:** Los modelos de deep learning carecen de transparencia de código tradicional. Los defensores a menudo no pueden rastrear el razonamiento interno, las rutas de decisión o la lógica exacta de generación de salidas. El análisis de seguridad depende de testing de entrada/salida, observación de comportamiento y análisis de modos de fallo.

**Ejercicio 2:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In a RAG-based system, which AI asset type is used to retrieve relevant context at query time? | `Embedding Vectors` |
| An attacker gains access to MegaCorp's model registry and swaps the production model for a modified version. Which AI-specific asset has been compromised? | `Model Registry / Artifacts` |

---

### Tarea 3 — Cadena de Suministro de Datos y Brechas de STRIDE / Data Supply Chain and STRIDE's Gaps

Los sistemas de IA introducen una nueva superficie de ataque a través de su cadena de suministro de datos. A diferencia de las cadenas de suministro de software tradicionales, los modelos de IA dependen en gran medida de datos de entrenamiento, pipelines de entrenamiento, registros de modelos y sistemas de recuperación. Los compromisos en estas etapas pueden afectar silenciosamente el comportamiento del modelo mucho después del despliegue.

**Etapas de la cadena de suministro de datos de IA:**

| Etapa | Descripción | Riesgo |
| --- | --- | --- |
| **1. Data Collection** | Los datos de entrenamiento pueden venir de web scraping, bases de datos internas, proveedores de terceros o contenido generado por usuarios | Los atacantes pueden inyectar datos maliciosos o manipulados en los datasets |
| **2. Cleaning and Labelling** | Los datos se procesan, filtran y etiquetan | Las etiquetas envenenadas o incorrectas enseñan al modelo patrones y comportamientos falsos |
| **3. Model Training** | El modelo aprende de los datasets preparados | Los datos maliciosos se incrustan en los pesos del modelo y pueden requerir reentrenamiento para eliminarse |
| **4. Validation and Packaging** | Los modelos se evalúan, versionan y almacenan en registros de modelos | Los atacantes pueden reemplazar modelos legítimos con versiones con backdoor; los backdoors a menudo evaden la validación porque las condiciones de activación están ausentes durante el testing |
| **5. Inference** | El modelo desplegado procesa consultas en vivo; los sistemas LLM pueden usar pipelines RAG, bases de datos vectoriales y sistemas de recuperación externos | El contexto recuperado puede manipularse para influir en las salidas del modelo |

**Por qué las cadenas de suministro de IA son diferentes:** Los compromisos de software tradicionales suelen ser más fáciles de detectar y más rápidos de parchear. Los ataques de envenenamiento de IA pueden permanecer ocultos durante semanas o meses, alterar gradualmente el comportamiento del modelo y afectar futuros ciclos de reentrenamiento. Ejemplo: el modelo de detección de fraude de MegaCorp se reentrena mensualmente; un atacante que inyecta lentamente transacciones fraudulentas diseñadas podría desplazar los límites de decisión del modelo hasta que la actividad fraudulenta ya no se detecte.

**Brechas de STRIDE en sistemas de IA:**

| Amenaza de IA | Categoría STRIDE | Problema |
| --- | --- | --- |
| Training Data Poisoning | Tampering | Los efectos son retrasados y difíciles de identificar |
| Adversarial Inputs | Múltiples categorías | Los prompts pueden causar alucinaciones, comportamiento inseguro o evadir salvaguardas |
| Expanded Privileges | Elevation of Privilege | Los sistemas de IA modernos pueden ejecutar código, acceder a bases de datos, navegar la web y enviar emails; comprometer el modelo puede otorgar acceso a herramientas y permisos conectados |
| Model Theft | Information Disclosure | El atacante obtiene una copia completa de la capacidad de IA entrenada de la organización |

**Conclusión clave:** STRIDE sigue siendo útil para evaluaciones de seguridad de IA, pero los defensores deben extenderlo para abordar activos específicos de IA, envenenamiento de datos, manipulación adversarial, robo de modelo y acceso a herramientas de IA.

**Ejercicio 3:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| An attacker injects crafted data points into a training pipeline over several months, gradually shifting the model's decision boundaries. At which supply chain stage does the attacker inject the malicious data? | `Data Collection` |
| Which STRIDE category is insufficient for capturing the delayed, diffuse effects of training data poisoning? | `Tampering` |

---

### Tarea 4 — Adaptando STRIDE para Sistemas de IA / Adapting STRIDE for AI Systems

El STRIDE tradicional sigue aplicándose a los sistemas de IA, pero cada categoría se manifiesta de forma diferente debido a los pipelines de entrenamiento, el comportamiento del modelo, las arquitecturas RAG, los LLM con herramientas y las salidas no deterministas. El objetivo no es reemplazar STRIDE, sino adaptarlo para entornos de IA.

**Refresco de STRIDE:**

| Categoría | Propiedad de Seguridad | Significado Tradicional |
| --- | --- | --- |
| **S — Spoofing** | Autenticidad | Hacerse pasar por otro usuario/servicio |
| **T — Tampering** | Integridad | Modificar datos o sistemas |
| **R — Repudiation** | No repudio | Negar acciones realizadas |
| **I — Information Disclosure** | Confidencialidad | Exponer información sensible |
| **D — Denial of Service** | Disponibilidad | Hacer los sistemas no disponibles |
| **E — Elevation of Privilege** | Autorización | Obtener capacidades no autorizadas |

**STRIDE adaptado para IA:**

**1. Spoofing → Data Source Impersonation**
* **Manifestación IA:** Los atacantes inyectan contenido malicioso en bases de conocimiento RAG, bases de datos vectoriales o fuentes de documentos externas. La IA trata los datos controlados por el atacante como contexto legítimo.
* **Otras amenazas:** Impersonación de modelo, ataques de identidad adversarial.
* **Ejemplo MegaCorp:** Documentos de política falsos inyectados en la base de conocimiento del chatbot, causando respuestas incorrectas.

**2. Tampering → Data Poisoning**
* **Manifestación IA:** Los atacantes manipulan datos de entrenamiento para alterar el comportamiento del modelo. Los efectos aparecen más tarde durante la inferencia, no inmediatamente.
* **Otras amenazas:** Manipulación de modelo, prompt injection, manipulación de features.
* **Ejemplo MegaCorp:** Transacciones fraudulentas diseñadas reentrenan lentamente el modelo de fraude para ignorar patrones maliciosos.
* **MITRE ATLAS:** `AML.T0020 — Data Poisoning`, `AML.T0018 — Backdoor ML Model`

**3. Repudiation → Falta de Pistas de Auditoría de Decisiones**
* **Manifestación IA:** Los sistemas de IA a menudo no pueden explicar completamente por qué se tomó una decisión, qué versión de modelo respondió o qué contexto influyó en la salida.
* **Otras cuestiones:** Volatilidad de contexto, falta de logs de despliegue de modelo.
* **Ejemplo MegaCorp:** El equipo de seguridad no puede determinar por qué el sistema de fraude aprobó una transacción sospechosa semanas antes.

**4. Information Disclosure → Model Extraction**
* **Manifestación IA:** Los atacantes consultan APIs repetidamente para reconstruir una copia funcional del modelo.
* **Otras amenazas:** Extracción de datos de entrenamiento, fuga de system prompt, inversión de embeddings.
* **Ejemplo MegaCorp:** Un competidor reconstruye el motor de recomendación de MegaCorp usando respuestas de API y puntuaciones de confianza.
* **MITRE ATLAS:** `AML.T0024 — Extract ML Model`, `AML.T0025 — Infer Training Data Membership`

**5. Denial of Service → Explotación de Costo de Inferencia**
* **Manifestación IA:** Los atacantes abusan de solicitudes de inferencia de IA costosas para aumentar los costos operativos. También llamado **Denial of Wallet**.
* **Otras amenazas:** Agotamiento de GPU, sponge examples, interrupción del pipeline de entrenamiento.
* **Ejemplo MegaCorp:** Miles de prompts de chatbot diseñados aumentan masivamente los costos de inferencia en la nube sin sacar el sistema offline.
* **OWASP LLM Top 10:** `LLM10:2025 — Unbounded Consumption`

**6. Elevation of Privilege → Jailbreaking**
* **Manifestación IA:** Los atacantes evaden las salvaguardas y restricciones del modelo usando prompts diseñados.
* **Otras amenazas:** Agencia excesiva, explotación de herramientas, escalada cross-plugin.
* **Ejemplo MegaCorp:** Un chatbot jailbreakeado abusa de las herramientas de base de datos conectadas para extraer PII de clientes.
* **OWASP LLM Top 10:** `LLM06:2025 — Excessive Agency`

**Lo que STRIDE aún no cubre:**
* **Adversarial Examples:** Entradas diseñadas para causar clasificación errónea, comportamiento inseguro o evadir controles. Estos ataques abarcan múltiples categorías STRIDE simultáneamente.
* **Model Bias and Fairness:** Los fallos relacionados con sesgos tienen implicaciones de cumplimiento, afectan la confianza y la seguridad, y no se mapean limpiamente a STRIDE.
* **Emergent Behaviour:** Los modelos grandes pueden desarrollar capacidades inesperadas y comportamientos impredecibles difíciles de modelar con frameworks tradicionales.

**Ejercicio 4:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the primary AI-specific manifestation of Information Disclosure in the STRIDE-AI mapping? | `Model Extraction` |
| An attacker crafts prompts that cause an LLM to bypass its safety guidelines and content restrictions. Which STRIDE category does this map to? | `Elevation of Privilege` |
| Which OWASP LLM Top 10 (2025) entry addresses the risks of AI systems being granted too many permissions or too much autonomy? | `LLM06:2025 — Excessive Agency` |
| An attacker drives your monthly inference bill from $15,000 to $180,000 without taking your service offline. What is this type of attack commonly called? | `Denial of Wallet` |

---

### Tarea 5 — MITRE ATLAS: El Catálogo de Técnicas de Amenazas de IA / MITRE ATLAS - The AI Threat Technique Catalogue

MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) es un framework para identificar y analizar ataques contra sistemas de IA y ML. Funciona de forma similar a MITRE ATT&CK para sistemas tradicionales, pero se centra específicamente en amenazas de IA. ATLAS ayuda a los defensores a entender técnicas de ataque de IA, comportamiento del adversario, mitigaciones defensivas y escenarios de ataque de IA del mundo real.

**Qué proporciona MITRE ATLAS:** A principios de 2026, ATLAS contiene 16 tácticas, 155 técnicas, 35 mitigaciones y 52 estudios de caso del mundo real. (Siempre verificar el sitio oficial de MITRE ATLAS para números actualizados.)

**Estructura de ATLAS:**

| Componente | Propósito | Ejemplo |
| --- | --- | --- |
| **Tactic** | Por qué actúa el atacante | `ML Attack Staging (AML.TA0012)` |
| **Technique** | Cómo se realiza el ataque | `Data Poisoning (AML.T0020)` |
| **Sub-technique** | Variación específica del ataque | `Craft Adversarial Data (AML.T0043.004)` |
| **Mitigation** | Contramedida defensiva | Validación de entrada, tracking de procedencia |

**Técnicas ATLAS importantes:**

**Data Poisoning — `AML.T0020`**
* **Descripción:** Inyectar datos maliciosos en pipelines de entrenamiento para alterar el comportamiento del modelo.
* **Mapeo STRIDE:** Tampering
* **Impacto:** Corrompe el comportamiento futuro del modelo; los efectos permanecen hasta que ocurre el reentrenamiento.

**Model Extraction — `AML.T0024`**
* **Descripción:** Los atacantes consultan APIs repetidamente para reconstruir una copia funcional del modelo.
* **Mapeo STRIDE:** Information Disclosure
* **Impacto:** Robo de propiedad intelectual, testing adversarial offline.

**Evade ML Model — `AML.T0015`**
* **Descripción:** Diseñar entradas adversariales para evadir la detección o clasificación del modelo.
* **Mapeo STRIDE:** Tampering, Spoofing, Elevation of Privilege
* **Ejemplo:** Evadir detección de malware, evitar moderación de contenido.

**LLM Prompt Injection — `AML.T0051`**
* **Descripción:** Manipular el comportamiento del modelo mediante prompts maliciosos.
* **Tipos:** Direct Injection (prompts creados por el usuario) e Indirect Injection (instrucciones maliciosas incrustadas en contenido recuperado).
* **Mapeo STRIDE:** Tampering
* **Riesgo MegaCorp:** Prompt injection indirecta a través de la base de conocimiento RAG.

**Backdoor ML Model — `AML.T0018`**
* **Descripción:** Incrustar triggers maliciosos ocultos durante el entrenamiento del modelo.
* **Comportamiento:** El modelo se comporta normalmente durante el testing; el trigger activa comportamiento malicioso más tarde.
* **Similar a:** Logic bombs dentro de redes neuronales.

**Uso de ATLAS con STRIDE (workflow recomendado):**
1. **Empezar con STRIDE:** Identificar qué puede salir mal y qué propiedad de seguridad se ve afectada.
2. **Enriquecer con ATLAS:** Mapear los riesgos identificados a técnicas de ataque específicas de IA, métodos de ataque del mundo real y comportamiento conocido del adversario.
3. **Aplicar mitigaciones:** Usar la guía defensiva de ATLAS como tracking de procedencia de datos, validación de entrada, monitoreo de drift y detección de anomalías.

**Ejemplo MegaCorp:** Hallazgo STRIDE: pipeline de entrenamiento de detección de fraude vulnerable a Tampering. Técnica ATLAS: `AML.T0020 — Data Poisoning`. Mitigaciones recomendadas: validación de procedencia de datos de entrenamiento, detección de anomalías en entradas, monitoreo de drift de modelo. Esto convierte una amenaza genérica en un hallazgo de seguridad detallado y accionable.

**Estudios de caso ATLAS del mundo real:**
* **ShadowRay — `AML.CS0023`:** Los atacantes explotaron vulnerabilidades en el framework Ray de IA para comprometer infraestructura de entrenamiento de IA. Demostró que los ataques a la cadena de suministro de IA ocurren activamente en entornos de producción.
* **Morris II Worm — `AML.CS0024`:** Un gusano de prompt injection auto-replicante dirigido a agentes de IA que usan sistemas basados en RAG. Inyectaba prompts maliciosos automáticamente, extraía PII y se propagaba entre agentes de IA. Mostró cómo la prompt injection puede propagarse autónomamente a través de sistemas de IA.

**Ejercicio 5:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What does the acronym ATLAS stand for? | `Adversarial Threat Landscape for Artificial-Intelligence Systems` |
| Which ATLAS case study described a self-replicating prompt injection worm that spread between AI agents via RAG email systems? | `Morris II` |
| What is the ATLAS technique ID for Model Extraction? | `AML.T0024` |

---

### Tarea 6 — OWASP LLM Top 10: Mapeando Riesgos a Componentes / OWASP LLM Top 10 - Mapping Risks to Components

El OWASP Top 10 para Aplicaciones LLM (2025) identifica los riesgos de seguridad más críticos que afectan los despliegues de LLM. A diferencia de una simple checklist, ayuda a los defensores a mapear riesgos a componentes de arquitectura, identificar sistemas expuestos rápidamente y priorizar esfuerzos de hardening.

**OWASP LLM Top 10 (2025):**

| ID | Riesgo | Descripción | Componentes Vulnerables |
| --- | --- | --- | --- |
| **LLM01** | Prompt Injection | Manipular el comportamiento del modelo usando prompts diseñados | Inference endpoint, RAG pipeline, vector database |
| **LLM02** | Sensitive Information Disclosure | Fuga de PII, credenciales o datos propietarios | Training pipeline, system prompts, inference endpoint |
| **LLM03** | Supply Chain | Modelos, datasets, plugins o dependencias comprometidos | Training pipeline, model registry, integraciones de terceros |
| **LLM04** | Data and Model Poisoning | Datos de entrenamiento o pesos de modelo manipulados | Training pipeline, feature store, model registry |
| **LLM05** | Improper Output Handling | Manejo inseguro de salidas del modelo | Web frontend, API gateway, sistemas downstream |
| **LLM06** | Excessive Agency | Herramientas o permisos de IA demasiado permisivos | Tool integrations, inference endpoint, capas de orquestación |
| **LLM07** | System Prompt Leakage | Exposición de prompts ocultos o lógica interna | System prompts, inference endpoint |
| **LLM08** | Vector and Embedding Weaknesses | Ataques contra embeddings y sistemas RAG | Vector databases, embedding systems, RAG pipelines |
| **LLM09** | Misinformation | Salidas alucinadas o incorrectas | Inference endpoint, vector databases |
| **LLM10** | Unbounded Consumption | Agotamiento de recursos o denial of wallet | API gateway, inference endpoint, training pipeline |

**Lectura del framework:**
* **Riesgo → Componente:** Ejemplo, Prompt Injection impacta inference endpoints, RAG pipelines y vector databases. Estos componentes requieren validación de entrada, controles de límite de prompt y filtrado de contenido.
* **Componente → Riesgo:** Ejemplo, Vector Database está asociado con `LLM01 — Prompt Injection`, `LLM08 — Embedding Weaknesses` y `LLM09 — Misinformation`. Esto define el alcance de seguridad para ese componente.

**Perfiles de riesgo de componentes:**
* **LLM Inference Endpoint:** Mayor concentración de riesgos (Prompt Injection, Sensitive Information Disclosure, Improper Output Handling, Excessive Agency, System Prompt Leakage, Misinformation, Unbounded Consumption). Requiere el hardening y monitoreo más fuerte.
* **Vector Database / RAG Pipeline:** Riesgos primarios: prompt injection indirecta, ataques de embeddings, manipulación de recuperación, datos fuente obsoletos o incorrectos. Enfoque de seguridad: control de acceso, validación de entrada, monitoreo de frescura de fuentes.
* **Training Pipeline:** Riesgos primarios: compromiso de cadena de suministro, envenenamiento de datos, exposición de datos sensibles. Enfoque de seguridad: procedencia de datasets, verificación de modelo, checks de integridad de fine-tuning.

**Relación entre STRIDE, ATLAS y OWASP:**

| Framework | Propósito | Uso |
| --- | --- | --- |
| **STRIDE-AI** | Categoriza amenazas | Identificar qué podría salir mal |
| **MITRE ATLAS** | Documenta técnicas de ataque | Entender cómo funcionan los ataques |
| **OWASP LLM Top 10** | Mapea riesgos a componentes | Priorizar controles de seguridad |

**Ejercicio 6:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many of the OWASP LLM Top 10 entries affect the LLM Inference Endpoint? | `7` |
| An organisation notices their chatbot is rendering LLM output directly in the browser without sanitisation. Which OWASP entry does this fall under? | `Improper Output Handling` |
| Which component in a typical LLM architecture is the primary one that needs hardening against data and model supply chain risks (LLM03)? | `Training Pipeline` |

---

### Tarea Final — Ejercicio de Threat Modelling de IA / AI Threat Modelling Exercise

Ejercicio interactivo completado identificando vulnerabilidades OWASP LLM Top 10, mapeando riesgos a componentes de arquitectura, aplicando conceptos STRIDE-AI y usando técnicas MITRE ATLAS para el análisis de amenazas. Se analizaron con éxito los riesgos de despliegue de IA y se validaron las decisiones de threat modelling a través del ejercicio práctico.

**Flag:**

```
THM{AI_THREAT_MODEL_COMPLETE}
```

---

### Conclusión / Conclusion

Esta room cubrió un workflow completo de threat modelling de IA centrado en identificar, analizar y documentar riesgos en sistemas de IA modernos.

**Lo que se cubrió:**
* **Activos específicos de IA:** Training data, model weights, embedding vectors, system prompts, feature stores, model registries.
* **Cadena de suministro de datos de IA:** Data collection → cleaning/labelling → model training → validation/packaging → inference, y cómo cada etapa puede comprometerse.
* **STRIDE para sistemas de IA:** Data poisoning, prompt injection, model extraction, jailbreaking, excessive agency, denial of wallet.
* **MITRE ATLAS:** Mapeo de técnicas de ataque de IA, comportamiento del adversario, ataques del mundo real y mitigaciones específicas de IA.
* **OWASP LLM Top 10:** Mapeo de riesgos de seguridad directamente a componentes de arquitectura.
* **Evaluación práctica de amenazas:** Aplicación de todos los frameworks a los despliegues de IA de MegaCorp (chatbot, motor de recomendación, sistema de detección de fraude).

**Conclusiones clave:**
* Los sistemas de IA introducen activos y superficies de ataque completamente nuevos.
* Los frameworks tradicionales de threat modelling siguen aplicándose pero requieren adaptación.
* STRIDE identifica categorías de amenazas; MITRE ATLAS proporciona técnicas de ataque específicas de IA; OWASP LLM Top 10 mapea riesgos a componentes vulnerables.
* Las evaluaciones de seguridad de IA deben considerar tanto los modelos como su infraestructura circundante.

**Recursos adicionales:** MITRE ATLAS, OWASP AI Exchange, OWASP LLM Top 10, MITRE ATT&CK.

---

* **Fuente / Source:**
  * [vanshksingh/TryHackMe-AI-Security-Path — ai-threat-modelling](https://github.com/vanshksingh/TryHackMe-AI-Security-Path/tree/main/ai-threat-modelling)

*Documentación para propósitos educativos y registro de CTF.*
