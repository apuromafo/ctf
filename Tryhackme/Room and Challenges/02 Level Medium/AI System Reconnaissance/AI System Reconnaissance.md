# AI System Reconnaissance [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory + Practical Lab
* **Slug:** `ai-system-reconnaissance`
* **Link:** https://tryhackme.com/room/ai-system-reconnaissance
* **Sección / Section:** Secure AI Systems (Section 2 of 5)
* **Fuente / Source:** [vanshksingh/TryHackMe-AI-Security-Path](https://github.com/vanshksingh/TryHackMe-AI-Security-Path) — `ai-system-reconnaissance\Readme.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

El reconocimiento de IA se centra en descubrir e identificar infraestructura de IA/ML expuesta en una red. A diferencia del threat modelling, el reconocimiento confirma qué está realmente desplegado y accesible. Los componentes comunes de IA incluyen servidores de inferencia, trackers de MLflow, servidores de notebooks, bases de datos vectoriales, endpoints de métricas y almacenamiento de objetos.

**Por qué importa:** Hallazgos recientes muestran 42,665 instancias de agentes de IA expuestas descubiertas en línea, 93.4% vulnerables, muchas con API keys filtradas a través de acceso no autenticado, y 91,000+ sesiones de ataque dirigidas a IA observadas en 3 meses. Los escáneres tradicionales a menudo fallan en detectar infraestructura de IA.

**Objetivos del reconocimiento:** Identificar servicios de IA/ML, puertos y protocolos abiertos, endpoints de API específicos de IA, malas configuraciones y metadatos expuestos. Herramientas comunes: `nmap`, `curl`, `grep`.

---

### Tarea 1 — Introducción / Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I understand the learning objectives and am ready to learn about AI system reconnaissance! | `No answer needed` |

---

### Tarea 2 — Componentes de Infraestructura de IA / AI Infrastructure Components

La infraestructura de IA introduce servicios, APIs y puertos que los escaneos de seguridad tradicionales a menudo pasan por alto. A diferencia de los entornos estándar, los despliegues de IA incluyen frameworks de model serving, plataformas de tracking de experimentos, bases de datos vectoriales, registros de modelos, entornos de notebooks y sistemas de orquestación de IA.

**Stack de infraestructura de IA:**

**Model Serving Endpoints** (cargan modelos entrenados y exponen APIs de inferencia):

| Componente | Puertos | Notas |
| --- | --- | --- |
| Triton Inference Server | 8000, 8001, 8002 | HTTP, gRPC, Prometheus |
| TensorFlow Serving | 8500, 8501 | gRPC + HTTP |
| TorchServe | 8080, 8081, 8082 | APIs de inferencia + gestión |
| Ollama | 11434 | Runtime LLM local |
| vLLM | 8000 | API compatible con OpenAI |

**Orquestación y Tracking de Experimentos:**

| Componente | Puertos | Notas |
| --- | --- | --- |
| MLflow | 5000 | Almacena experimentos, modelos, métricas |
| Kubeflow | 80, 443 | Orquestación de pipelines ML |
| Ray | 8265, 8000 | Workloads de IA distribuidos |

**Bases de datos vectoriales:**

| Componente | Puertos | Notas |
| --- | --- | --- |
| Qdrant | 6333, 6334 | HTTP + gRPC |
| Weaviate | 8080 | Soporte GraphQL |
| Milvus | 19530 | Almacenamiento de embeddings |
| Chroma | 8000 | Base de datos vectorial |

Las bases de datos vectoriales a menudo exponen modelos de embeddings, nombres de colecciones y referencias a datasets internos.

**Infraestructura de soporte:**

| Componente | Puertos | Notas |
| --- | --- | --- |
| Jupyter Notebook | 8888 | A menudo expuesto sin auth |
| MinIO | 9000, 9001 | Almacenamiento compatible con S3 |
| Prometheus Metrics | 8002, 8082 | Filtra métricas de modelo y GPU |

**Endpoints de recon importantes:**

| Servicio | Endpoint |
| --- | --- |
| Triton | `/v2/models` |
| TorchServe | `/models` |
| Ollama | `/api/tags` |
| MLflow | `/api/2.0/mlflow/experiments/search` |
| Qdrant | `/collections` |
| Weaviate | `/v1/schema` |
| Jupyter | `/api/kernels` |
| Prometheus | `/metrics` |

**Por qué la infraestructura de IA es riesgosa:** Servicios expuestos comunes descubiertos en escaneos del mundo real: dashboards de MLflow sin autenticación, notebooks Jupyter públicos, dashboards de Ray abiertos y endpoints de inferencia Triton expuestos. Los atacantes usan consultas simples de Shodan:

```bash
port:5000 "MLflow"
port:8888 title:"Home Page - Select or create a notebook"
http.title:"Ray Dashboard"
port:8001 "triton"
```

**Ejercicio 2:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the IP address of the host running an HTTP service on port 8888 in your scan results? | `10.10.45.20` |
| Which port does MLflow Tracking Server run on by default? | `5000` |

---

### Tarea 3 — Fingerprinting de Servicios de IA / Fingerprinting AI Services

La detección de servicios estándar (`nmap -sV`) a menudo identifica erróneamente la infraestructura de IA. El fingerprinting de IA se basa en headers HTTP, estructuras de respuesta JSON, mensajes de error, convenciones de nombres de endpoints y comportamiento gRPC.

**Fingerprinting por headers HTTP:**

| Framework | Firma |
| --- | --- |
| TorchServe | `Server: TorchServe/0.x.x` |
| Triton | Header `NV-Status` |
| FastAPI ML APIs | `server: uvicorn` |
| OpenAI-Compatible APIs | `x-request-id` + `"object": "model"` |

Triton también puede exponer utilización de GPU, métricas de CPU y telemetría de hardware.

**Fingerprinting por respuesta de API:**

* **TensorFlow Serving:**
```json
{
  "model_version_status": [
    {
      "version": "1",
      "state": "AVAILABLE"
    }
  ]
}
```
* **Triton Inference Server:**
```json
{
  "name": "fraud_detector",
  "versions": ["1"],
  "platform": "tensorflow_graphdef"
}
```
* **OpenAI-Compatible APIs:**
```json
{
  "object": "model",
  "id": "llama-3.1-8b"
}
```

**Fingerprinting por mensajes de error:** Las solicitudes malformadas a menudo revelan detalles del framework. Ejemplos: `tensorinfo_map` → TensorFlow Serving, `mlflow.server` → MLflow, `io.jsonwebtoken.IncorrectClaimException` → Databricks Mosaic AI. Los frameworks de IA comúnmente exponen salida de debugging verbosa.

**Convenciones de nombres de endpoints:**

| Propósito | Endpoints |
| --- | --- |
| Inferencia | `/predict`, `/infer`, `/generate`, `/embeddings` |
| Modelos | `/v1/models`, `/v2/models` |
| MLflow | `/api/2.0/mlflow/` |
| Kubeflow | `/pipeline/apis/v1beta1/` |

Útiles durante `ffuf`, `feroxbuster` y enumeración de API.

**Fingerprinting gRPC:**
* Puertos gRPC comunes: Triton → `8001`, TensorFlow Serving → `8500`.
* Comandos de ejemplo:
```bash
grpcurl -plaintext target:8001 list
grpcurl -plaintext target:8001 describe inference.GRPCInferenceService
```
* Si la reflexión está habilitada, se puede enumerar el esquema completo de la API.

**Fingerprinting TLS (JA3/JA4):** Los despliegues de IA a menudo tienen firmas TLS únicas debido a librerías de Python, tráfico gRPC y pipelines ML automatizados. Útil para detectar reconocimiento automatizado e identificar patrones de tráfico de IA.

**Estudio de caso GreyNoise:**
* 91,000+ sesiones de reconocimiento de IA observadas; 80,000+ solicitudes dirigidas a endpoints LLM.
* Prompts de sonda comunes: `hi`, `How many states are there in the United States?`, `How many letter 'r' are in the word strawberry?`.
* Objetivo: identificar proveedores de modelos, detectar esquemas de API y construir listas de objetivos de explotación.
* Modelos objetivo: GPT-4o, Claude, Llama, Gemini, DeepSeek, Mistral, Qwen, Grok.

**Ejercicio práctico:**
1. **Check MLflow Headers:** `curl -v http://10.10.45.12:5000/`
2. **Probe Triton Models:** `curl http://10.10.45.15:8000/v2/models`
3. **Trigger Framework Errors:** `curl -X POST http://10.10.45.15:8000/v2/models/fraud_detector/infer -d '{"bad":"data"}'`
4. **Check gRPC Reflection:** `grpcurl -plaintext 10.10.45.15:8001 list`
5. **Probe Remaining Services:** `curl http://10.10.45.18:6333/collections` y `curl http://10.10.45.20:8888/api/kernels`

**Ejercicio:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which unique HTTP response header does the service on `10.10.45.15:8000` return to identify as an NVIDIA product? | `NV-Status` |
| When you run `grpcurl` against `10.10.45.15:8001`, what is the name of the inference service listed in the reflection output? | `inference.GRPCInferenceService` |

---

### Tarea 4 — Enumerando Sistemas de IA / Enumerating AI Systems

Esta tarea se centra en enumerar servicios de IA/ML expuestos después del fingerprinting. La enumeración ayuda a identificar detalles operativos como modelos, experimentos, metadatos de entrenamiento, ubicaciones de artefactos y configuraciones de infraestructura.

**Enumeración de MLflow:** MLflow es un objetivo valioso porque centraliza experimentos, modelos, artefactos y metadatos de entrenamiento a través de APIs REST.

* **List Experiments:** `POST /api/2.0/mlflow/experiments/search` — Devuelve nombres e IDs de experimentos; puede exponer nombres en clave de proyectos, workflows internos y objetivos de negocio. Ejemplos: `fraud-detection-v3`, `rag-embeddings-tuning`, `customer-churn-prototype`.
* **List Registered Models:** `GET /api/2.0/mlflow/registered-models/list` — Devuelve nombres de modelos, descripciones y timestamps de creación.
* **Enumerate Model Versions:** `GET /api/2.0/mlflow/model-versions/search` — Campos útiles: `source` (URI de almacenamiento de artefactos), `user_id` (identidad del creador), stage labels (`Production`, `Staging`), timestamps. Ejemplo de ruta de artefacto: `s3://internal-ml-models-corp/experiments/1/artifacts/`.
* **Search Training Runs:** `POST /api/2.0/mlflow/runs/search` — Puede exponer métricas de entrenamiento, hashes de commits Git, identificadores de despliegue, tags personalizados e hiperparámetros.
* **List Artifacts:** `GET /api/2.0/mlflow/artifacts/list` — Revela artefactos de modelo descargables y proporciona visibilidad de activos ML.

**Metadatos de servidores de inferencia:** Los servidores de inferencia a menudo exponen endpoints de metadatos que revelan cómo deben estructurarse las solicitudes de inferencia.

* **Triton Inference Server:** `GET /v2/models/<model>/config` — Devuelve nombres de tensores de entrada, formas, tipos de datos, tamaño máximo de batch y framework backend. Frameworks comunes: `tensorflow_graphdef`, `pytorch_libtorch`, `onnxruntime`.
* **TensorFlow Serving:** `GET /v1/models/<model>/metadata` — Devuelve especificaciones de tensores de entrada/salida, nombres, formas y tipos de datos.

**Enumeración de bases de datos vectoriales:** Las bases de datos vectoriales pueden exponer datasets indexados y configuraciones de embeddings.

* **Weaviate:** `GET /v1/meta` y `GET /v1/schema` — Puede exponer versión del servidor, módulos instalados, definiciones de clases, nombres de propiedades y configuración de vectorizer. Endpoint adicional: `/v1/graphql` — soporta introspección de esquema y puede permitir consultas en instancias sin autenticación.
* **Qdrant:** `GET /collections` y `GET /collections/<collection>` — Devuelve nombres de colecciones, dimensiones de vectores, métricas de distancia y conteos de puntos. Ejemplo de inteligencia: `internal-hr-policies`, vectores de 768 dimensiones, 50,000 puntos.
* **Chroma:** Versiones antiguas pueden exponer `GET /api/v1/collections` — a veces accesible sin autenticación.

**Conclusiones clave:** La enumeración extrae inteligencia operativa de la infraestructura de IA expuesta. MLflow revela experimentos, modelos, artefactos y metadatos de entrenamiento. Los endpoints de metadatos de inferencia exponen estructuras de solicitud válidas. Las bases de datos vectoriales revelan categorías de datos indexados y configuraciones de embeddings. Los servicios de IA mal configurados pueden filtrar inteligencia organizacional significativa.

**Ejercicio:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What MLflow REST API endpoint would you use to retrieve the artifact storage location for a specific model version? | `/api/2.0/mlflow/model-versions/search` |
| What is the cleartext password for the MLflow service account stored in the Jupyter notebook on `10.10.45.20`? | `Cyphira-MLfl0w-2024!` |

---

### Tarea 5 — Mapeo de Superficie de Ataque de IA y MITRE ATLAS / AI Attack Surface Mapping & MITRE ATLAS

Esta tarea se centra en conectar los hallazgos de reconocimiento en un mapa completo de superficie de ataque de IA. En lugar de tratar los servicios expuestos como hallazgos aislados, el objetivo es entender cómo interactúan los componentes de infraestructura de IA y cómo los atacantes encadenan debilidades.

**Cómo la IA expande la superficie de ataque:** Las aplicaciones tradicionales exponen solo unos pocos servicios, pero los entornos de IA contienen muchos componentes interconectados: MLflow, Kubeflow, Jupyter Notebooks, bases de datos vectoriales, servidores de inferencia, Prometheus y registros de modelos. Estos sistemas se comunican constantemente entre sí: los servidores de inferencia extraen datos de bases de datos vectoriales, las plataformas de orquestación empujan actualizaciones a registros, los notebooks Jupyter se conectan a infraestructura interna y los servicios de monitoreo scrapean métricas de cada componente. Si un servicio se enlaza a `0.0.0.0` en lugar de `127.0.0.1`, la infraestructura interna puede volverse alcanzable externamente.

**Malas configuraciones de plataforma:**

* **MLflow:** Las versiones antiguas se enviaron sin autenticación; `basic_auth.ini` contenía credenciales hardcodeadas; vulnerable a ataques de directory traversal. CVEs importantes: `CVE-2026-2635` y `CVE-2026-2033`, ambos con CVSS 9.8. Riesgos: divulgación de credenciales, acceso a artefactos, ejecución remota de código (RCE).
* **Kubeflow:** Los dashboards se exponen frecuentemente sin autenticación OIDC. Riesgos: acceso no autenticado al dashboard, spawn de notebooks Jupyter, acceso al cluster Kubernetes a través de service accounts. Esto crea una ruta directa de `Open Dashboard → Kubernetes Access`.
* **TorchServe:** Expone una API de gestión en el puerto 8081. Característica peligrosa: registro dinámico de modelos desde URLs arbitrarias (`POST /models`). Los atacantes pueden cargar archivos `.mar` maliciosos que ejecutan código de inicialización durante la carga del modelo. Resultado: RCE.
* **SageMaker:** Los notebooks configurados con `DirectInternetAccess: Enabled` aceptan conexiones entrantes de internet. Un informe de seguridad en la nube de 2024 encontró que el 82% de las organizaciones tenían al menos un notebook configurado de esta manera.

**Registros de modelos: objetivos de alto valor:** Un registro MLflow expuesto revela la línea completa de productos ML: nombres de modelos, historial de versiones, stage labels, run IDs, URIs de artefactos, IDs de usuario contribuyentes y metadatos de entrenamiento.

**Ejemplo de cadena de ataque:**
```
1. Attacker finds MLflow credentials in Jupyter notebook
2. Uses MLOKit against registry
3. Exfiltrates model artifacts
4. Maps entire ML infrastructure
```

**Reconocimiento de cadena de suministro:** Los sistemas de IA dependen en gran medida de dependencias externas.

* **Hugging Face Tokens:** Ubicaciones comunes de exposición: archivos `.env`, repositorios GitHub, logs de CI/CD, secretos de Kubernetes. Ejemplo de dork de GitHub: `filename:.env HF_TOKEN`. Los tokens comprometidos pueden otorgar acceso de lectura/escritura, acceso a modelos privados y acceso a datasets.
* **Dependency Confusion:** Los pipelines ML a menudo contienen nombres de paquetes internos dentro de `requirements.txt`. Ejemplo: `company-data-utils`. Si el paquete no está registrado públicamente, los atacantes pueden registrarlo en PyPI. Resultado: los pipelines de entrenamiento pueden instalar paquetes maliciosos durante los builds de contenedores.
* **Fuentes de modelos maliciosos:** Las ubicaciones de descarga de modelos a menudo son visibles en celdas de notebooks, archivos de configuración y logs de contenedores. Fuentes comunes: Hugging Face Hub, PyTorch Hub. Si los atacantes comprometen modelos upstream o tokens, pueden envenenar toda la cadena de suministro ML.

**Mapeo MITRE ATLAS:** MITRE ATLAS es un framework estilo ATT&CK centrado en amenazas de IA y ML. A finales de 2025: 15 tácticas, 66 técnicas, 46 sub-técnicas.

| Actividad | Técnica MITRE ATLAS |
| --- | --- |
| Port scanning de servicios de IA | `AML.T0006` — Active Scanning |
| Descubrir registros y artefactos | `AML.T0007` — Discover ML Artifacts |
| Tokens HF expuestos y dependencias | `AML.T0010` — ML Supply Chain Compromise |
| Enumerar configuraciones LLM | `AML.T0014` — Discover ML Model Family |
| Actividades generales de reconocimiento | `AML.TA0002` — Reconnaissance |

**Estudio de caso: Campaña ShadowRay (CVE-2023-48022):** La campaña ShadowRay demostró cómo un solo componente de IA expuesto puede llevar al compromiso completo de la infraestructura.

* **Debilidad inicial:** La API de Job Submission de Ray en el puerto 8265 se envió sin autenticación por diseño. Los atacantes usaron Shodan para localizar 230,000+ dashboards de Ray expuestos.
* **Acceso inicial:** Los atacantes enviaron jobs maliciosos a través de `/api/jobs/`.
* **Reconocimiento:** Los payloads ejecutaron `cat /etc/passwd` y `printenv` para enumerar usuarios, robar credenciales IAM de AWS y cosechar variables de entorno.
* **Post-explotación:** Los atacantes pivotaron lateralmente a través de la infraestructura en la nube, secuestraron nodos de cómputo GPU, desplegaron mineros XMRig y disfrazaron procesos como workers del kernel de Linux. El uso de CPU se limitó al 60% para evitar detección.
* **ShadowRay 2.0:** Variantes posteriores añadieron payloads de malware generados por LLM, cron jobs ocultos, persistencia systemd, hosting de payloads en GitHub/GitLab y ataques de agotamiento TCP Sockstress.

**Ejercicio:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| The Cyphira Jupyter notebook at `10.10.45.20` contains a Hugging Face token (`hf_kR7mXpQvL9nJwT2yBcDfAeGh8iKlMnOp`). The `internal-kb-embedder` model on MLflow references `sentence-transformers/all-MiniLM-L6-v2` as its base model. What ATLAS technique ID covers the risk of these exposed supply chain dependencies? | `AML.T0010` |
| You scanned the Cyphira subnet with `nmap`, probed endpoints with `curl`, and extracted metadata from MLflow APIs. All of these activities fall under one overarching ATLAS tactic. What is its ID? | `AML.TA0002` |

---

### Tarea 6 — Metodología de Reconocimiento Estructurado y Detección / Structured Reconnaissance Methodology & Detection

Esta tarea combina todo lo aprendido en tareas anteriores en una metodología de reconocimiento de IA repetible. También cambia la perspectiva al lado del defensor, demostrando cómo aparece la actividad de reconocimiento dentro de los logs SIEM y cómo las organizaciones pueden detectar o reducir la exposición.

**Metodología de reconocimiento de IA en 5 fases:**

**Fase 1: Reconocimiento Pasivo** — Antes de interactuar con la red objetivo, recopilar inteligencia disponible públicamente.
* **Motores de búsqueda a nivel de internet:** Shodan, Censys, FOFA. Dorks de ejemplo: `port:5000 "MLflow"`, `port:8888 title:"Home Page - Select or create a notebook"`, `http.title:"Ray Dashboard"`.
* **Caza de credenciales en GitHub:** Dorks de ejemplo: `filename:.env MLFLOW_TRACKING_URI`, `filename:.env HF_TOKEN`, `filename:config.json model_name site:github.com`. Posibles hallazgos: cadenas de conexión MLflow, tokens de Hugging Face, referencias a modelos internos.
* **Objetivos adicionales de recon pasivo:** Investigación pública (papers de arXiv, blogs de ingeniería, publicaciones de conferencias) → `AML.T0000 — Search for Victim's Publicly Available Research Materials`; registros de contenedores (DockerHub, GitHub Container Registry); listados de empleo (roles como `MLflow Administrator`, `Kubeflow Platform Engineer` revelan tecnologías desplegadas).

**Fase 2: Escaneo Activo**
* **Escaneo de puertos enfocado en IA:**
```bash
nmap -p 5000,6333,8000,8001,8002,8080,8265,8500,8501,8888,9000,11434,19530 -sV --script=http-title,http-headers <target>
```
* **Puertos importantes:** 5000 (MLflow), 6333 (Qdrant), 8000-8002 (Triton/AI APIs), 8080 (TorchServe), 8265 (Ray Dashboard), 8500/8501 (TensorFlow Serving), 8888 (Jupyter), 11434 (Ollama), 19530 (Milvus).
* **Enumeración gRPC:** Puertos como 8001 y 8500 pueden exponer servicios gRPC. Usar `grpcurl`.
* **Endpoints de métricas:** Verificar `/metrics` en puertos comunes: Triton → 8002, TorchServe → 8082. Pueden exponer nombres de modelos, utilización de GPU, topología de despliegue y tamaños de batch.

**Fase 3: Fingerprinting de API** — Usar herramientas como `ffuf`, `feroxbuster`, `curl` con wordlists específicas de IA. Endpoints comunes: `/v1/models`, `/v2/models`, `/v2/health/ready`, `/api/2.0/mlflow/experiments/list`, `/api/2.0/mlflow/registered-models/list`, `/pipeline/apis/v1beta1/pipelines`, `/api/serve/deployments/`, `/v1/schema`, `/v1/meta`, `/api/kernels`, `/api/contents`, `/openapi.json`, `/docs`, `/graphql`, `/metrics`, `/collections`, `/healthz`, `/ping`. Técnicas: analizar headers de respuesta, estructuras JSON, mensajes de error y comportamientos de API.

**Fase 4: Extracción de Metadatos** — Después de identificar servicios, enumerarlos a fondo.
* **MLflow:** Recopilar experimentos, modelos registrados, versiones de modelo, URIs de artefactos, IDs de usuario, runs de entrenamiento y listados de artefactos. Estas llamadas de API pueden mapear todo el portfolio ML.
* **Triton / TensorFlow Serving:** Consultar endpoints de configuración de modelo para extraer especificaciones de tensores, detalles de framework y esquemas de entrada/salida.
* **Bases de datos vectoriales:** Enumerar esquemas, colecciones, dimensiones de embeddings y tipos de datos.
* **Jupyter:** Buscar listados de kernels, contenidos de notebooks y credenciales en texto claro.

**Fase 5: Revisión de Cadena de Suministro**
* **Revisar fuentes de dependencias:** Inspeccionar celdas de notebooks, archivos de configuración, logs de build, `requirements.txt`, `Pipfile`.
* **Buckets de artefactos públicos:** Verificar S3, GCS, MinIO para artefactos de modelo legibles públicamente.
* **Dependency Confusion:** Paquete interno de ejemplo: `company-data-utils`. Si no está registrado públicamente, los atacantes pueden registrar versiones maliciosas en PyPI.
* **Exposición de registros de contenedores:** Verificar si las imágenes de contenedor pueden extraerse sin autenticación.

**Referencia de herramientas:**

| Herramienta | Propósito | Fase |
| --- | --- | --- |
| Shodan / Censys / FOFA | Buscar banners de servicios de IA | Fase 1 |
| GitHub Dorks | Encontrar credenciales filtradas | Fase 1 |
| Nmap | Escaneo de puertos y detección de versiones | Fase 2 |
| grpcurl | Enumerar servicios gRPC | Fase 2 |
| ffuf / feroxbuster | Fuerza bruta de directorios | Fase 2-3 |
| curl | Sondear APIs manualmente | Fase 3-4 |
| MLOKit | Enumeración y exfiltración de MLflow | Fase 4 |
| Nuclei | Escanear malas configuraciones de IA conocidas | Fase 2-3 |
| Agrus Scanner | Detección de shadow AI específica de IA | Fase 2 |

**Cómo se ve el reconocimiento en logs SIEM:**
* **Patrón de enumeración de modelos:** Ráfaga de solicitudes GET a `/v2/models` (10-50 solicitudes, mismo endpoint, misma IP, en segundos).
* **Acceso scripted a MLflow:** Solicitudes a `/registered-models/list` y `/model-versions/search` sin sesiones UI válidas o cookies. Este comportamiento coincide con MLOKit.
* **Scraping de métricas no autorizado:** Solicitudes a `/metrics` originadas fuera del CIDR de monitoreo.
* **Escaneo de puertos consciente de IA:** `5000 → 8000 → 8001 → 8080 → 8265 → 8888` escaneados secuencialmente desde la misma fuente. Sugiere fuertemente reconocimiento específico de IA.
* **Sondeo de path traversal de MLflow:** `../` y `%2e%2e%2f` dentro de solicitudes de artefactos. Posible objetivo: CVE-2026-2033.
* **Enumeración de Jupyter:** `/api/kernels` y `/api/contents` sin cookies de sesión válidas.

**Quick wins para reducir exposición:**
* **MLflow:** Habilitar autenticación (`MLFLOW_TRACKING_USERNAME`, `MLFLOW_TRACKING_PASSWORD`) o desplegar detrás de un reverse proxy autenticado.
* **Jupyter:** Evitar `--allow-root` y `--ip=0.0.0.0`; requerir autenticación por token y VPN o ingress autenticado.
* **Restringir puertos de IA:** No exponer públicamente 5000, 8000-8002, 8080, 8265, 8500/8501, 8888, 9000 a menos que sea necesario.
* **Deshabilitar control de modelo Triton:** Usar `--model-control-mode none` para prevenir carga de modelos no autorizada.
* **Restringir endpoints de métricas:** Permitir acceso a `/metrics` solo desde infraestructura de monitoreo interna.
* **Asegurar tokens de Hugging Face:** Rotar tokens regularmente, usar permisos de grano fino, aplicar scope mínimo y evitar almacenar tokens en secretos o repos.
* **Reducir fuga de información:** Eliminar headers de debug, suprimir mensajes de error verbosos y restringir el acceso público a buckets de artefactos.

**Estudio de caso: Brecha de Hugging Face Spaces (2024):** Los atacantes obtuvieron acceso no autorizado a Hugging Face Spaces y extrajeron secretos de autenticación de desarrolladores. Los secretos comprometidos incluían tokens HF, acceso a modelos privados, acceso a datasets y acceso a configuración. Lección clave: las mismas credenciales descubiertas durante el reconocimiento son a menudo las mismas credenciales expuestas durante brechas del mundo real. Defensas primarias: rotación de tokens, permisos de grano fino, almacenamiento seguro de secretos y scope mínimo de tokens.

**Ejercicio:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| A SIEM log shows requests to `/api/2.0/mlflow/registered-models/list` from an IP with no corresponding MLflow UI session. What tool's access pattern does this match? | `MLOKit` |
| What is the single most effective quick win for preventing unauthenticated access to the MLflow tracking server? | `Enable MLflow authentication` |

---

### Tarea 7 — Conclusión / Conclusion

Esta tarea resume cómo las técnicas de reconocimiento de IA se mapean a los principales frameworks de seguridad de la industria: MITRE ATLAS, MITRE ATT&CK, OWASP Top 10 para Aplicaciones LLM, NIST AI RMF y NIST CSF 2.0. El objetivo es comunicar los hallazgos de reconocimiento de IA usando lenguaje de seguridad estandarizado entendido por equipos de seguridad, auditoría, gobernanza y cumplimiento.

**Mapeo MITRE ATLAS:**

| Contenido de la room | ID de técnica ATLAS | Nombre de técnica |
| --- | --- | --- |
| Shodan y GitHub dorks para infraestructura de IA | `AML.T0000` | Active Scanning |
| Localizar registros de modelos y artefactos | `AML.T0048` | Discover ML Artifacts |
| Tokens HF expuestos y dependency confusion | `AML.T0040` | ML Supply Chain Compromise |
| Enumerar configuraciones y esquemas LLM | `AML.T0069` | Discover LLM System Information |
| Actividades generales de reconocimiento | `AML.TA0002` | Reconnaissance (Tactic) |

**Mapeo MITRE ATT&CK:**

| Contenido de la room | ID de técnica ATT&CK | Nombre de técnica |
| --- | --- | --- |
| Escaneo de puertos de servicios de IA | `T1046` | Network Service Scanning |
| Extraer topología de despliegue y metadatos | `T1592` | Gather Victim Host Information |
| Sondear interfaces de gestión | `T1595.002` | Vulnerability Scanning |
| Recopilar inteligencia de infraestructura de IA | `TA0043` | Reconnaissance (Tactic) |

**Mapeo OWASP Top 10 para Aplicaciones LLM (2025):**

| Hallazgo de la room | ID OWASP LLM | Riesgo |
| --- | --- | --- |
| Servidores MLflow y notebooks Jupyter expuestos | `LLM05` | Improper Output Handling |
| Artefactos de modelo descargables de registros no asegurados | `LLM06` | Excessive Agency |
| Tokens HF filtrados y dependency confusion | `LLM03` | Training Data Poisoning / Supply Chain Vulnerabilities |
| Autenticación faltante y credenciales por defecto | `LLM10` | Model Theft |

**NIST AI Risk Management Framework (AI RMF 1.0):** Esta room se alinea principalmente con la función `Map`. Mapeos: Map 1.1 (los componentes e interacciones del sistema de IA se identifican — Tareas 2, 3, 4), Map 1.5 (los riesgos potenciales del sistema de IA se evalúan — malas configuraciones, registros expuestos, debilidades de cadena de suministro), Map 3.2 (los riesgos de recursos de IA de terceros se identifican — dependencias de Hugging Face, registros de modelos públicos, dependencias de PyTorch Hub), Measure 2.6 (determinar si los sistemas de IA funcionan como se pretende — exposición de métricas Prometheus, interfaces de debug, endpoints públicos inesperados).

**NIST Cybersecurity Framework (CSF 2.0):** La room se alinea principalmente con la función `Identify`. Mapeos: ID.AM (Asset Management — inventariar infraestructura de IA, descubrir componentes de IA desplegados, mapear servicios expuestos), ID.RA (Risk Assessment — identificar superficies de ataque, detectar configuraciones inseguras, evaluar riesgos de exposición).

**Qué viene después:** La siguiente room, `AI Threat Modelling Assessment`, se construye directamente sobre la metodología de reconocimiento aprendida aquí. Áreas de enfoque: identificar vulnerabilidades explotables, medir impacto, priorizar mitigaciones y modelar amenazas de infraestructura de IA.

**Conclusiones finales:**
* El reconocimiento de IA se mapea directamente a frameworks de seguridad establecidos.
* Los sistemas de IA introducen superficies de ataque altamente interconectadas.
* El descubrimiento de activos es fundamental para la seguridad de IA.
* Los hallazgos de reconocimiento se convierten en entradas de threat modelling.
* Las organizaciones no pueden asegurar infraestructura de IA que no pueden descubrir.

**Lo que aprendí:**
* Cómo identificar y enumerar infraestructura de IA a través de una red.
* Servicios, frameworks e interfaces de gestión expuestas comunes de IA.
* Cómo los atacantes hacen fingerprinting de MLflow, Triton, TorchServe, Ray, Kubeflow, bases de datos vectoriales y entornos Jupyter.
* Cómo la extracción de metadatos revela inteligencia operativa sobre sistemas ML.
* Los riesgos asociados con registros de modelos expuestos, almacenamiento de artefactos y APIs de inferencia.
* Cómo los ataques de cadena de suministro apuntan a tokens de Hugging Face, hubs de modelos públicos y dependencias ML internas.
* Cómo el reconocimiento de IA se mapea a MITRE ATLAS, MITRE ATT&CK, OWASP LLM y frameworks NIST.
* Cómo se ve la actividad de reconocimiento desde la perspectiva del defensor dentro de logs SIEM.
* Medidas defensivas prácticas que reducen la exposición al reconocimiento de IA.

---

* **Fuente / Source:**
  * [vanshksingh/TryHackMe-AI-Security-Path — ai-system-reconnaissance](https://github.com/vanshksingh/TryHackMe-AI-Security-Path/tree/main/ai-system-reconnaissance)

*Documentación para propósitos educativos y registro de CTF.*
