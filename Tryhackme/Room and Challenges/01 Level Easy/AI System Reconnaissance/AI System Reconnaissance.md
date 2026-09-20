# AI System Reconnaissance

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `aisystemreconnaissance` | [TryHackMe](https://tryhackme.com/room/aisystemreconnaissance) | AI Security Path | THM | MLflow, NVIDIA Triton, grpcurl, ATLAS, model registry | Alto |

---

**Contexto:** Sala práctica del AI Security Path centrada en el reconocimiento y enumeración de infraestructura de IA. Se explora un entorno con MLflow Tracking Server, NVIDIA Triton Inference Server y Jupyter Notebook, identificando servicios expuestos, extrayendo credenciales de supply chain y mapeando superficies de ataque con el framework ATLAS. El participante practica herramientas de recon (nmap, grpcurl) aplicadas a componentes específicos de MLOps.

## Solucionario

### Task 1: Network Reconnaissance

**Explicación:** Reconocimiento activo con nmap sobre la red del laboratorio para descubrir hosts y servicios. En los resultados aparece un host con un servicio HTTP en el puerto 8888 (Jupyter Notebook).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the IP address of the host running an HTTP service on port 8888 in your scan results? | `10.10.45.20` |

### Task 2: MLflow Enumeration

**Explicación:** Enumeración del servidor MLflow Tracking Server: se identifica el puerto por defecto del servicio y se consulta su API REST para localizar la ubicación de almacenamiento de artefactos de modelos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Which port does MLflow Tracking Server run on by default? | `5000` |
| 3 | What MLflow REST API endpoint would you use to retrieve the artifact storage location for a specific model version? | `/api/2.0/mlflow/model-versions/search` |

### Task 3: NVIDIA Triton Discovery

**Explicación:** Se identifica el NVIDIA Triton Inference Server mediante el header HTTP `NV-Status` en el puerto 8000 y se enumera el servicio de inferencia gRPC con `grpcurl` contra el puerto 8001, usando la reflexión del servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | Which unique HTTP response header does the service on 10.10.45.15:8000 return to identify as an NVIDIA product? | `NV-Status` |
| 5 | When you run grpcurl against 10.10.45.15:8001, what is the name of the inference service listed in the reflection output? | `inference.GRPCInferenceService` |

### Task 4: Credential & Supply Chain Analysis

**Explicación:** Análisis de credenciales y dependencias de supply chain: se extrae la contraseña en claro de la cuenta de servicio de MLflow almacenada en el Jupyter Notebook y se identifica la técnica ATLAS que cubre el riesgo de las dependencias expuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | What is the cleartext password for the MLflow service account stored in the Jupyter notebook on 10.10.45.20? | `cyphira-MLfl0w-2024!` |
| 7 | ...what ATLAS technique ID covers the risk of these exposed supply chain dependencies? | `AML.T0010` |

### Task 5: Threat Mapping & Defense

**Explicación:** Mapeo de los hallazgos al framework ATLAS: se agrupan las actividades bajo una táctica global, se reconoce el patrón de acceso del tool MLOKIT en los logs del SIEM y se determina la mitigación de mayor impacto para el MLflow tracking server.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 8 | ...All of these activities fall under one overarching ATLAS tactic. What is its ID? | `AML.TA0002` |
| 9 | A SIEM log shows requests to /api/2.0/mlflow/registered-models/list ... What tool's access pattern does this match? | `MLOKIT` |
| 10 | What is the single most effective quick win for preventing unauthenticated access to the MLflow tracking server? | `Enable MLflow authentication` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the IP address of the host running an HTTP service on port 8888 in your scan results? | `10.10.45.20` |
| 2 | Which port does MLflow Tracking Server run on by default? | `5000` |
| 3 | What MLflow REST API endpoint would you use to retrieve the artifact storage location for a specific model version? | `/api/2.0/mlflow/model-versions/search` |
| 4 | Which unique HTTP response header does the service on 10.10.45.15:8000 return to identify as an NVIDIA product? | `NV-Status` |
| 5 | When you run grpcurl against 10.10.45.15:8001, what is the name of the inference service listed in the reflection output? | `inference.GRPCInferenceService` |
| 6 | What is the cleartext password for the MLflow service account stored in the Jupyter notebook on 10.10.45.20? | `cyphira-MLfl0w-2024!` |
| 7 | ...what ATLAS technique ID covers the risk of these exposed supply chain dependencies? | `AML.T0010` |
| 8 | ...All of these activities fall under one overarching ATLAS tactic. What is its ID? | `AML.TA0002` |
| 9 | A SIEM log shows requests to /api/2.0/mlflow/registered-models/list ... What tool's access pattern does this match? | `MLOKIT` |
| 10 | What is the single most effective quick win for preventing unauthenticated access to the MLflow tracking server? | `Enable MLflow authentication` |

---

**Metodología:** Se realizó reconocimiento activo con nmap para descubrir hosts y servicios (HTTP 8888, MLflow 5000, Triton HTTP 8000/gRPC 8001). Se enumeró MLflow vía REST API para localizar artifacts y credenciales en notebooks. Se identificó NVIDIA Triton mediante headers HTTP (`NV-Status`) y reflexión gRPC (`grpcurl`). Se mapearon hallazgos al framework ATLAS (AML.TA0002 — Reconocimiento, AML.T0010 — Supply Chain) y se identificó el tool MLOKIT por su patrón de acceso a APIs MLflow. La mitigación principal es habilitar autenticación en MLflow.

**Learning chain:** Nmap Recon → MLflow Enumeration → NVIDIA Triton Discovery → Credential Extraction → ATLAS Mapping → MLOKIT Detection → Authentication Hardening

**Lección:** *La infraestructura de MLOps (MLflow, Triton, notebooks) queda frecuentemente expuesta sin autenticación; el reconocimiento de headers, puertos y APIs REST/gRPC permite mapearla contra frameworks como ATLAS para priorizar hardening.*

**MITRE ATT&CK:** AML.TA0002 (Reconocimiento), AML.T0010 (Supply Chain)

**Fuente:** [TryHackMe - AI System Reconnaissance](https://tryhackme.com/room/aisystemreconnaissance)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.