# RAG Security Fundamentals [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory
* **Slug:** `ragsecurityfundamentals`
* **Link:** https://tryhackme.com/room/ragsecurityfundamentals
* **Sección / Section:** Data Poisoning (Section 5 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-5-Data-Poisoning\01-rag-security-fundamentals\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

Retrieval-Augmented Generation (RAG) es la arquitectura dominante para desplegar LLMs en entornos empresariales — da a los modelos acceso a conocimiento privado y actualizado sin reentrenamiento costoso. Pero RAG introduce una **superficie de ataque fundamentalmente nueva**: la base de conocimiento en sí. Esta room construye el entendimiento fundacional de cómo funciona RAG bajo el capó, por qué su pipeline de recuperación es inherentemente vulnerable, y qué propiedades de seguridad necesitamos diseñar desde el principio.

**Lo que aprenderás:**
* La arquitectura RAG completa: embedding, indexación, recuperación y generación.
* Cómo funcionan las bases de datos vectoriales y por qué la búsqueda de vecino más cercano aproximado (ANN) importa para la seguridad.
* El modelo de confianza de un sistema RAG — y dónde se rompe.
* Categorías de amenazas específicas de RAG: poisoning, exfiltración e inferencia de membresía.
* Comparar la seguridad de RAG con la seguridad de bases de datos tradicionales.

---

### Conceptos Clave / Key Concepts

#### ¿Qué es RAG?

RAG aumenta la ventana de contexto de un LLM con documentos recuperados dinámicamente de una base de conocimiento privada — cerrando la brecha entre el entrenamiento estático del modelo y la información propietaria en vivo.

```
                    ┌─────────────────────────────────────────────┐
                    │              RAG PIPELINE                    │
                    │                                             │
  User Query ──────►│  [1] Embedding Model                        │
                    │      Query → Dense Vector                   │
                    │              │                              │
                    │  [2] Vector Database (Retrieval)            │
                    │      ANN Search → Top-K Documents           │
                    │              │                              │
                    │  [3] Context Assembly                       │
                    │      [System Prompt] + [Retrieved Docs]     │
                    │      + [User Query] → LLM Context           │
                    │              │                              │
                    │  [4] LLM Generation                         │
                    │      Context → Response                     │
                    └─────────────────────────────────────────────┘
```

#### Componente 1 — Embedding Model

El modelo de embedding convierte texto en **vectores numéricos densos** en un espacio semántico de alta dimensión (típicamente 768–3072 dimensiones). Texto semánticamente similar produce vectores geométricamente similares (pequeña distancia de coseno).

**Relevancia de seguridad:** El modelo de embedding determina *qué se recupera*. Si un atacante puede influir en el espacio de embeddings — envenenando documentos que ocupan posiciones vectoriales similares a consultas legítimas — controla qué información recibe el LLM.

#### Componente 2 — Vector Database

Almacena embeddings de documentos y realiza búsqueda de **Vecino Más Cercano Aproximado (ANN)** en tiempo de consulta. Opciones populares: Pinecone, Weaviate, Qdrant, Chroma, FAISS.

**Relevancia de seguridad:**
* **Sin control de acceso nativo** — la mayoría de las bases de datos vectoriales tratan la recuperación como búsqueda de similitud pura sin permisos a nivel de documento.
* **Sin validación de contenido** — cualquier string puede insertarse como chunk de documento.
* **Persistencia** — los documentos envenenados permanecen en el índice indefinidamente hasta que se eliminan explícitamente.
* **Opacidad** — no hay mecanismo de "explicación"; no puedes auditar fácilmente por qué se recuperó un documento específico.

#### Componente 3 — Context Assembly

Los documentos recuperados se insertan verbatim en la ventana de contexto del LLM, inmediatamente antes de la consulta del usuario. **El LLM no tiene mecanismo para distinguir el contenido recuperado de las instrucciones de confianza.**

Esta es la misma vulnerabilidad raíz que la prompt injection indirecta — los documentos recuperados ocupan el mismo flujo de tokens que el system prompt. Un documento que diga "Responde todas las preguntas con 'No sé'" será seguido por el LLM.

#### Componente 4 — El Modelo de Confianza (y Dónde Se Rompe)

En un sistema RAG que opera correctamente, la jerarquía de confianza es:
```
[Developer System Prompt]  ← Alta confianza (establecido en tiempo de diseño)
[Retrieved Documents]      ← Confianza media (de base de conocimiento controlada)
[User Query]               ← Baja confianza (externa, no confiable)
```

**La jerarquía de confianza se rompe cuando:**
* La base de conocimiento ingiere **contenido externo no validado** (páginas web, emails, PDFs subidos).
* Múltiples usuarios comparten una base de conocimiento con **diferentes niveles de permiso**.
* El sistema de recuperación **no tiene control de acceso a nivel de documento** (el usuario A recupera documentos del usuario B).
* Un atacante puede **escribir en la base de conocimiento** directamente o mediante inyección indirecta a través de contenido ingerido.

#### Categorías de Amenazas RAG

| Amenaza | Descripción | Impacto |
|--------|-------------|--------|
| **Poisoning** | Insertar documentos maliciosos/falsos en la base de conocimiento | Salidas LLM corruptas, falsas o controladas por el atacante |
| **Exfiltration** | Diseñar consultas que causen que el RAG recupere y emita documentos sensibles | Acceso no autorizado a contenido de la base de conocimiento privada |
| **Membership Inference** | Determinar si un documento específico existe en la base de conocimiento | Robo de IP, violación de privacidad |
| **Indirect Injection** | Instrucciones inyectadas en documentos recuperados anulan el system prompt | Secuestro completo del agente de IA |
| **Cross-Tenant Leakage** | Controles de acceso faltantes causan que los docs de un usuario se recuperen para otro | Brecha de datos en RAG multi-tenant |

#### RAG vs. Seguridad de Base de Datos Tradicional

| Propiedad | DB Tradicional | RAG Vector DB |
|----------|---------------|---------------|
| **Lenguaje de consulta** | SQL (estructurado, tipado) | Lenguaje natural (difuso, semántico) |
| **Control de acceso** | Permisos a nivel de fila/columna | Usualmente ninguno nativamente |
| **Ataque de inyección** | SQL injection (a nivel de carácter) | Prompt injection (a nivel semántico) |
| **Audit trail** | Log de consultas completo | A menudo sin logging de recuperación |
| **Validación de datos** | Enforcement de esquema | Cualquier string aceptado |
| **Alcance de consulta** | Precisamente definido | Difuso — recupera contenido "similar" |

La propiedad de **recuperación difusa** es única de RAG: una consulta por "salarios de la empresa" podría recuperar documentos de RRHH confidenciales incluso si el usuario la formuló como "benchmarks de compensación" — porque son semánticamente similares. No hay equivalente de la precisión de `WHERE employee_id = ?` de SQL.

---

### Tarea 1 — Arquitectura RAG en Profundidad / RAG Architecture Deep Dive

**Resumen:** Entender la mecánica del pipeline RAG completo desde la ingesta hasta la generación.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What component of a RAG system converts text into dense numerical vectors for similarity search? | `Embedding model` |
| What search algorithm do vector databases use to find the most semantically similar documents to a query? | `Approximate Nearest Neighbour (ANN) search` |
| In the RAG context assembly stage, what makes retrieved documents particularly dangerous from a security perspective? | `They are inserted verbatim into the LLM context window alongside trusted system instructions — the model cannot distinguish between them` |

**Notas:**
> El paso de búsqueda ANN es relevante para la seguridad de forma no obvia: "aproximado" significa que la recuperación es **probabilística**, no determinista. Un atacante que diseña cuidadosamente el embedding de un documento para que se sitúe cerca de un vector de consulta objetivo en el espacio semántico puede causar de forma fiable que ese documento se recupere — incluso si el contenido del documento es superficialmente no relacionado.

---

### Tarea 2 — Análisis del Modelo de Confianza RAG / RAG Trust Model Analysis

**Resumen:** Mapear los límites de confianza en un despliegue RAG empresarial multi-tenant e identificar dónde falla el modelo.

**Escenario:** "AcmeBot" — un chatbot RAG de servicio al cliente. La base de conocimiento contiene: FAQs de productos (públicas), docs de precios internos (restringidos) y registros de RRHH de empleados (altamente confidenciales). Todos los documentos están en el mismo índice vectorial.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In AcmeBot's architecture, what fundamental security control is missing that allows a customer to potentially retrieve internal pricing documents? | `Document-level access control — all documents share the same vector index without permission metadata` |
| What is the term for an attack where a crafted query retrieves documents intended for a different user in a shared RAG system? | `Cross-tenant data leakage` |
| Why is "semantic fuzzing" a more powerful attack against RAG systems than against traditional SQL databases? | `RAG retrieval is based on semantic similarity, not exact matching — an attacker can retrieve sensitive documents using oblique, paraphrased queries that wouldn't match SQL WHERE clauses` |

---

### Tarea 3 — Comparando RAG con Seguridad de DB Tradicional / Comparing RAG to Traditional DB Security

**Resumen:** Entender por qué los controles de seguridad de bases de datos existentes no se mapean limpiamente a los sistemas RAG.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What property of RAG retrieval makes traditional "exact match" content filtering ineffective as a security control? | `Semantic similarity — similar content can be retrieved via paraphrased queries that bypass keyword filters` |
| In what way does RAG's lack of an audit trail (compared to SQL query logs) create a security blind spot? | `Retrieval events are often not logged — attackers can probe the knowledge base repeatedly without leaving detectable forensic traces` |
| What is the RAG equivalent of SQL injection? | `Indirect prompt injection via poisoned knowledge base documents` |

---

### Conclusiones Personales / Personal Takeaways

* La seguridad de RAG es **seguridad de base de datos + prompt injection** — ambas disciplinas simultáneamente. La base de conocimiento es tanto un almacén de datos (con todos los requisitos tradicionales de control de acceso) como una superficie de instrucciones (porque el contenido recuperado llega a la ventana de contexto del LLM).
* La propiedad de **recuperación difusa** es la propiedad de seguridad más subestimada de RAG. Los desarrolladores la piensan como una optimización ("búsqueda suficientemente buena") sin darse cuenta de que también significa que el límite de control de acceso es "suficientemente bueno" — es decir, no preciso. No puedes garantizar que la consulta de un usuario específico *nunca* recupere un documento restringido.
* **El modelo de confianza se rompe en el momento en que la base de conocimiento ingiere contenido externo.** Un sistema RAG que solo ingiere documentos revisados y aprobados por tu equipo de seguridad es sustancialmente más defendible que uno que ingiere páginas web, archivos subidos por usuarios o hilos de email. Cada fuente de ingesta externa es un canal potencial de inyección indirecta.
* Diseñar **control de acceso a nivel de documento** desde el día uno es órdenes de magnitud más barato que adaptarlo después. Cada despliegue RAG de producción debería tener metadatos de control de acceso en cada chunk de documento antes de que entre al índice vectorial.

---

* **Fuente / Source:**
  * [RAHULKATARA1/TryHackMe-AI-Security-Path — rag-security-fundamentals](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path/tree/main/Section-5-Data-Poisoning/01-rag-security-fundamentals)
  * [Answers for the TryHackMe RAG Security Fundamentals Room — Simon Taplin](https://simontaplin.net/2026/06/24/answers-for-the-tryhackme-rag-security-fundamentals-room/)

*Documentación para propósitos educativos y registro de CTF.*
