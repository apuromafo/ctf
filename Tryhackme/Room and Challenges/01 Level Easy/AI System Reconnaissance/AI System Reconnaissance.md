# AI System Reconnaissance

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `aisystemreconnaissance` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/aisystemreconnaissance) |
| **Sección** | AI Security Path |
| **Fuente** | THM |
| **Componentes** | MLflow, NVIDIA Triton, grpcurl, ATLAS, model registry |
| **Impacto** | Alto |

---

**Contexto:** Sala práctica del AI Security Path centrada en el reconocimiento y enumeración de infraestructura de IA. Se explora un entorno con MLflow Tracking Server, NVIDIA Triton Inference Server y Jupyter Notebook, identificando servicios expuestos, extrayendo credenciales de supply chain y mapeando superficies de ataque con el framework ATLAS. El participante practica herramientas de recon (nmap, grpcurl) aplicadas a componentes específicos de MLOps.

## Solucionario

### Task 1: Network Reconnaissance

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the IP address of the host running an HTTP service on port 8888 in your scan results? | `10.10.45.20` |

### Task 2: MLflow Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Which port does MLflow Tracking Server run on by default? | `5000` |
| 3 | What MLflow REST API endpoint would you use to retrieve the artifact storage location for a specific model version? | `/api/2.0/mlflow/model-versions/search` |

### Task 3: NVIDIA Triton Discovery

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | Which unique HTTP response header does the service on 10.10.45.15:8000 return to identify as an NVIDIA product? | `NV-Status` |
| 5 | When you run grpcurl against 10.10.45.15:8001, what is the name of the inference service listed in the reflection output? | `inference.GRPCInferenceService` |

### Task 4: Credential & Supply Chain Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | What is the cleartext password for the MLflow service account stored in the Jupyter notebook on 10.10.45.20? | `cyphira-MLfl0w-2024!` |
| 7 | ...what ATLAS technique ID covers the risk of these exposed supply chain dependencies? | `AML.T0010` |

### Task 5: Threat Mapping & Defense

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 8 | ...All of these activities fall under one overarching ATLAS tactic. What is its ID? | `AML.TA0002` |
| 9 | A SIEM log shows requests to /api/2.0/mlflow/registered-models/list ... What tool's access pattern does this match? | `MLOKIT` |
| 10 | What is the single most effective quick win for preventing unauthenticated access to the MLflow tracking server? | `Enable MLflow authentication` |

---

**Metodología:** Se realizó reconocimiento activo con nmap para descubrir hosts y servicios (HTTP 8888, MLflow 5000, Triton HTTP 8000/gRPC 8001). Se enumeró MLflow vía REST API para localizar artifacts y credenciales en notebooks. Se identificó NVIDIA Triton mediante headers HTTP (`NV-Status`) y reflección gRPC (`grpcurl`). Se mapearon hallazgos al framework ATLAS (AML.TA0002 — Reconocimiento, AML.T0010 — Supply Chain) y se identificó el tool MLOKIT por su patrón de acceso a APIs MLflow. La mitigación principal es habilitar autenticación en MLflow.

**Learning chain:** Nmap Recon → MLflow Enumeration → NVIDIA Triton Discovery → Credential Extraction → ATLAS Mapping → MLOKIT Detection → Authentication Hardening

**MITRE ATT&CK:** AML.TA0002 (Reconocimiento), AML.T0010 (Supply Chain)

**Fuente:** [TryHackMe - AI System Reconnaissance](https://tryhackme.com/r/room/aisystemreconnaissance)
