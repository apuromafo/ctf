# AI System Reconnaissance
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `ai-system-reconnaissance` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ai-system-reconnaissance) |
| **Sección** | Secure AI Systems (Section 2 of 5) |
| **Fuente** | [vanshksingh/TryHackMe-AI-Security-Path](https://github.com/vanshksingh/TryHackMe-AI-Security-Path) — `ai-system-reconnaissance\Readme.md` |
| **Componentes** | NVIDIA Triton, TensorFlow Serving, TorchServe, Ollama, vLLM, MLflow, Kubeflow, Ray, Qdrant, Weaviate, Milvus, Chroma, Jupyter, MinIO, Prometheus, gRPC (grpcurl), Shodan, MLOKit, Nmap, SIEM, MITRE ATLAS |
| **Impacto** | Descubre e identifica infraestructura de IA/ML expuesta en una red: componentes, puertos y endpoints, fingerprinting de servicios, enumeración de MLflow/vector DBs, mapeo a MITRE ATLAS y detección en logs SIEM. |
---
**Contexto:** El reconocimiento de IA se centra en descubrir e identificar infraestructura de IA/ML expuesta en una red. A diferencia del threat modelling, el reconocimiento confirma qué está realmente desplegado y accesible. Componentes comunes: servidores de inferencia, trackers de MLflow, servidores de notebooks, bases de datos vectoriales, endpoints de métricas y almacenamiento de objetos. Hallazgos recientes: 42,665 instancias de agentes de IA expuestas, 93.4% vulnerables, muchas con API keys filtradas; 91,000+ sesiones de ataque dirigidas a IA en 3 meses.
*EN: AI reconnaissance is about discovering and identifying exposed AI/ML infrastructure on a network. Unlike threat modelling, it confirms what is actually deployed and reachable. Common components: inference servers, MLflow trackers, notebook servers, vector databases, metrics endpoints and object storage. Recent findings: 42,665 exposed AI agent instances, 93.4% vulnerable, many leaking API keys; 91,000+ AI-targeted attack sessions in 3 months.*
## Solucionario
### Task 1 — Introducción / Introduction
**Explicación:** Objetivos: identificar servicios de IA/ML, puertos y protocolos abiertos, endpoints de API específicos de IA, malas configuraciones y metadatos expuestos. Herramientas: `nmap`, `curl`, `grep`.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to learn about AI system reconnaissance! | `No answer needed` |
### Task 2 — Componentes de Infraestructura de IA / AI Infrastructure Components
**Explicación:** Stack de infraestructura de IA por puertos y endpoints de recon:
- **Model Serving Endpoints:** Triton Inference Server (8000 HTTP / 8001 gRPC / 8002 Prometheus), TensorFlow Serving (8500 gRPC / 8501 HTTP), TorchServe (8080/8081/8082 APIs de inferencia + gestión), Ollama (11434, runtime LLM local), vLLM (8000, API compatible con OpenAI).
- **Orquestación/Tracking:** MLflow (5000: experimentos, modelos, métricas), Kubeflow (80/443), Ray (8265/8000).
- **Vector DBs:** Qdrant (6333/6334), Weaviate (8080, GraphQL), Milvus (19530), Chroma (8000) — a menudo exponen modelos de embeddings, nombres de colecciones y datasets internos.
- **Soporte:** Jupyter Notebook (8888, a menudo sin auth), MinIO (9000/9001, S3), Prometheus Metrics (8002/8082, filtran métricas de modelo y GPU).
- **Endpoints de recon:** Triton `/v2/models`, TorchServe `/models`, Ollama `/api/tags`, MLflow `/api/2.0/mlflow/experiments/search`, Qdrant `/collections`, Weaviate `/v1/schema`, Jupyter `/api/kernels`, Prometheus `/metrics`.
Riesgos reales: dashboards de MLflow sin autenticación, notebooks Jupyter públicos, dashboards Ray abiertos y endpoints Triton expuestos. Dorks de Shodan: `port:5000 "MLflow"`, `port:8888 title:"Home Page - Select or create a notebook"`, `http.title:"Ray Dashboard"`, `port:8001 "triton"`.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the IP address of the host running an HTTP service on port 8888 in your scan results? | `10.10.45.20` |
| 2 | Which port does MLflow Tracking Server run on by default? | `5000` |
### Task 3 — Fingerprinting de Servicios de IA / Fingerprinting AI Services
**Explicación:** La detección estándar (`nmap -sV`) a menudo identifica erróneamente la infraestructura de IA. Fingerprint por **headers HTTP** (TorchServe `Server: TorchServe/0.x.x`, Triton header `NV-Status`, FastAPI `server: uvicorn`, OpenAI-compatible `x-request-id` + `"object": "model"`), **respuestas JSON** (TensorFlow Serving `model_version_status`, Triton `name`/`platform`, OpenAI `object/id`), **mensajes de error** (`tensorinfo_map` → TF Serving, `mlflow.server` → MLflow, `io.jsonwebtoken.IncorrectClaimException` → Databricks Mosaic AI), **convenciones de endpoints** (`/predict`, `/infer`, `/generate`, `/embeddings`; `/v1/models`, `/v2/models`; `/api/2.0/mlflow/`; `/pipeline/apis/v1beta1/`) y **gRPC** (Triton 8001, TF Serving 8500; `grpcurl -plaintext target:8001 list`; si la reflexión está habilitada se enumera el esquema completo). El **fingerprinting TLS (JA3/JA4)** aprovecha firmas TLS únicas por librerías Python/gRPC. Estudio de caso GreyNoise: 91,000+ sesiones de recon de IA; prompts de sonda típicos (`hi`, `How many states...`, `How many letter 'r' in strawberry?`); modelos objetivo GPT-4o, Claude, Llama, Gemini, DeepSeek, Mistral, Qwen, Grok.
```bash
curl -v http://10.10.45.12:5000/
curl http://10.10.45.15:8000/v2/models
curl -X POST http://10.10.45.15:8000/v2/models/fraud_detector/infer -d '{"bad":"data"}'
grpcurl -plaintext 10.10.45.15:8001 list
curl http://10.10.45.18:6333/collections
curl http://10.10.45.20:8888/api/kernels
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which unique HTTP response header does the service on `10.10.45.15:8000` return to identify as an NVIDIA product? | `NV-Status` |
| 2 | When you run `grpcurl` against `10.10.45.15:8001`, what is the name of the inference service listed in the reflection output? | `inference.GRPCInferenceService` |
### Task 4 — Enumerando Sistemas de IA / Enumerating AI Systems
**Explicación:** Enumeración de MLflow por API REST: `POST /api/2.0/mlflow/experiments/search` (nombres de experimentos: `fraud-detection-v3`, `rag-embeddings-tuning`, `customer-churn-prototype`), `GET /api/2.0/mlflow/registered-models/list`, `GET /api/2.0/mlflow/model-versions/search` (campos `source` como `s3://internal-ml-models-corp/...`, `user_id`, stage labels), `POST /api/2.0/mlflow/runs/search` (métricas, hashes Git, tags, hiperparámetros) y `GET /api/2.0/mlflow/artifacts/list`. Servidores de inferencia: Triton `GET /v2/models/<model>/config` (tensores, tamaños, backend `tensorflow_graphdef`/`pytorch_libtorch`/`onnxruntime`) y TF Serving `GET /v1/models/<model>/metadata`. Vector DBs: Weaviate `GET /v1/meta` y `/v1/schema` (+ `/v1/graphql` sin autenticación), Qdrant `GET /collections` y `/collections/<collection>`, Chroma antiguo `GET /api/v1/collections`.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What MLflow REST API endpoint would you use to retrieve the artifact storage location for a specific model version? | `/api/2.0/mlflow/model-versions/search` |
| 2 | What is the cleartext password for the MLflow service account stored in the Jupyter notebook on `10.10.45.20`? | `Cyphira-MLfl0w-2024!` |
### Task 5 — Mapeo de Superficie de Ataque de IA y MITRE ATLAS / AI Attack Surface Mapping & MITRE ATLAS
**Explicación:** Los entornos de IA contienen muchos componentes interconectados (MLflow, Kubeflow, Jupyter, vector DBs, inferencia, Prometheus, registros). Malas configuraciones: **MLflow** sin autenticación, `basic_auth.ini` con credenciales hardcodeadas, directory traversal (CVEs `CVE-2026-2635` y `CVE-2026-2033`, CVSS 9.8: divulgación de credenciales, RCE); **Kubeflow** dashboards sin OIDC → acceso al cluster vía service accounts (`Open Dashboard → Kubernetes Access`); **TorchServe** API de gestión 8081 con registro dinámico de modelos (`POST /models`) → `.mar` maliciosos → RCE; **SageMaker** `DirectInternetAccess: Enabled` (82% de organizaciones con ≥1 notebook así). Cadena de ataque típica: credenciales MLflow en notebook → MLOKit contra el registry → exfiltración de artefactos → mapeo completo de infraestructura ML. **Cadena de suministro:** tokens HF expuestos (dork `filename:.env HF_TOKEN`), dependency confusion en `requirements.txt` (registrar paquete interno en PyPI), fuentes de modelos maliciosos (Hugging Face Hub, PyTorch Hub). **MITRE ATLAS** (15 tácticas, 66 técnicas, 46 sub-técnicas a finales de 2025):
| Actividad | Técnica MITRE ATLAS |
|---|---|
| Port scanning de servicios de IA | `AML.T0006` — Active Scanning |
| Descubrir registros y artefactos | `AML.T0007` — Discover ML Artifacts |
| Tokens HF expuestos y dependencias | `AML.T0010` — ML Supply Chain Compromise |
| Enumerar configuraciones LLM | `AML.T0014` — Discover ML Model Family |
| Recon general | `AML.TA0002` — Reconnaissance |

**Caso ShadowRay (CVE-2023-48022):** Ray Job Submission API (puerto 8265) sin auth por diseño → 230,000+ dashboards expuestos vía Shodan → jobs maliciosos por `/api/jobs/` → `cat /etc/passwd`/`printenv` → credenciales IAM de AWS → pivot lateral, secuestro de nodos GPU, mineros XMRig disfrazados de workers del kernel (CPU limitada al 60%). ShadowRay 2.0 añadió payloads LLM, cron ocultos, persistencia systemd y Sockstress.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The Cyphira Jupyter notebook at `10.10.45.20` contains a Hugging Face token (`hf_kR7mXpQvL9nJwT2yBcDfAeGh8iKlMnOp`). The `internal-kb-embedder` model on MLflow references `sentence-transformers/all-MiniLM-L6-v2` as its base model. What ATLAS technique ID covers the risk of these exposed supply chain dependencies? | `AML.T0010` |
| 2 | You scanned the Cyphira subnet with `nmap`, probed endpoints with `curl`, and extracted metadata from MLflow APIs. All of these activities fall under one overarching ATLAS tactic. What is its ID? | `AML.TA0002` |
### Task 6 — Metodología de Reconocimiento Estructurado y Detección / Structured Reconnaissance Methodology & Detection
**Explicación:** Metodología en 5 fases:
1. **Recon pasivo:** Shodan/Censys/FOFA dorks, GitHub dorks (`filename:.env MLFLOW_TRACKING_URI`, `filename:.env HF_TOKEN`), papers arXiv/blogs, registros de contenedores, listados de empleo → `AML.T0000`.
2. **Escaneo activo:** `nmap -p 5000,6333,8000,8001,8002,8080,8265,8500,8501,8888,9000,11434,19530 -sV --script=http-title,http-headers <target>`; grpcurl en 8001/8500; `/metrics` en 8002/8082.
3. **Fingerprinting de API:** ffuf/feroxbuster/curl con wordlists IA (`/v1/models`, `/v2/health/ready`, `/openapi.json`, `/docs`, `/graphql`, `/collections`...).
4. **Extracción de metadatos:** MLflow (experimentos, modelos, artefactos), Triton/TF config, vector DBs, Jupyter (kernels, notebooks, credenciales en claro).
5. **Revisión de cadena de suministro:** dependencias (requirements.txt, Pipfile), buckets S3/GCS/MinIO, dependency confusion, registros de contenedores.
Herramientas/fases: Shodan/Censys/FOFA (1), GitHub Dorks (1), Nmap (2), grpcurl (2), ffuf/feroxbuster (2-3), curl (3-4), MLOKit (4), Nuclei (2-3), Agrus (2). **Recon en logs SIEM:** ráfagas GET a `/v2/models` desde una IP; acceso scripted a MLflow sin sesión UI (patrón MLOKit); scraping de `/metrics` fuera del CIDR de monitoreo; escaneo secuencial `5000 → 8000 → 8001 → 8080 → 8265 → 8888`; `../` y `%2e%2e%2f` (CVE-2026-2033); `/api/kernels` y `/api/contents` sin cookies. **Quick wins:** habilitar autenticación MLflow (`MLFLOW_TRACKING_USERNAME/PASSWORD`), no exponer Jupyter con `--allow-root`/`--ip=0.0.0.0` (requerir token + VPN/ingress), no exponer 5000/8000-8002/8080/8265/8500-8501/8888/9000, `--model-control-mode none` en Triton, restringir `/metrics`, rotar tokens HF con scope mínimo, eliminar headers de debug. **Caso Hugging Face Spaces 2024:** brecha que exfiltró secretos (tokens HF, acceso a modelos/datasets); lección: las credenciales descubiertas en recon son las mismas expuestas en brechas reales.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A SIEM log shows requests to `/api/2.0/mlflow/registered-models/list` from an IP with no corresponding MLflow UI session. What tool's access pattern does this match? | `MLOKit` |
| 2 | What is the single most effective quick win for preventing unauthenticated access to the MLflow tracking server? | `Enable MLflow authentication` |
### Task 7 — Conclusión / Conclusion
**Explicación:** Mapeo a frameworks: **MITRE ATLAS** (Shodan/GitHub dorks → `AML.T0000`; registros/artefactos → `AML.T0048`; tokens HF/dependency confusion → `AML.T0040`; esquemas LLM → `AML.T0069`; recon → `AML.TA0002`), **ATT&CK** (T1046, T1592, T1595.002, TA0043), **OWASP LLM Top 10 (2025)** (MLflow/Jupyter expuestos → LLM05; artefactos descargables → LLM06; tokens/dependency confusion → LLM03; falta de auth → LLM10), **NIST AI RMF 1.0** (principalmente función `Map`: Map 1.1, 1.5, 3.2; Measure 2.6) y **NIST CSF 2.0** (`Identify`: ID.AM, ID.RA). La siguiente room (`AI Threat Modelling Assessment`) se construye sobre esta metodología.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identify, enumerate and fingerprint the Cyphira AI infrastructure (pregunta de cierre del laboratorio). | `No answer needed` |
---
**Metodología:** Reconocimiento estructurado de IA en 5 fases (pasivo → escaneo → fingerprinting → metadatos → supply chain) con mapeo a MITRE ATLAS y detección defensiva en SIEM.
**Learning chain:** infraestructura de IA y puertos → fingerprinting de servicios → enumeración (MLflow/vector DBs/inferencia) → mapeo de superficie y ATLAS → metodología repetible y detección → hardening rápido.
**MITRE ATT&CK / ATLAS:** AML.T0000/AML.T0006 (Active Scanning, ATT&CK T1595), AML.T0007/AML.T0048 (Discover ML Artifacts), AML.T0010/AML.T0040 (ML Supply Chain Compromise), AML.T0014/AML.T0069 (Discover LLM System Information), AML.TA0002 (Reconnaissance), T1046, T1592, T1595.002.
**Fuente:** [TryHackMe - AI System Reconnaissance](https://tryhackme.com/room/ai-system-reconnaissance)