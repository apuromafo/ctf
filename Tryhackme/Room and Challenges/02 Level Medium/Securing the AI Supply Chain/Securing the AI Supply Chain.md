# Securing the AI Supply Chain [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory + Lab
* **Slug:** `securing-the-ai-supplychain`
* **Link:** https://tryhackme.com/room/securing-the-ai-supplychain
* **Sección / Section:** AI Supply Chain Security (Section 4 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-4-AI-Supply-Chain-Security\03-securing-the-ai-supply-chain\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

Entender los ataques es solo la mitad de la misión. Esta room cubre el playbook defensivo completo para la seguridad de la cadena de suministro de IA: desde gobernanza de datos y procedencia de modelos hasta hardening de MLOps y cumplimiento regulatorio. El objetivo es arquitecturar un pipeline de desarrollo de IA que sea **resiliente, auditable y endurecido** en cada eslabón de la cadena.

**Lo que aprenderás:**
* Gobernanza de datos: tracking de procedencia, verificación de integridad y pipelines de ingesta seguros.
* Firma de modelos, versionado y procedencia criptográfica.
* Gestión de dependencias: SBOMs para ML, mirrors de paquetes privados y lock files.
* Hardening de MLOps: CI/CD de menor privilegio, gestión de secretos y seguridad de registros.
* Detección de backdoors: neural cleanse, activation clustering y firmas espectrales.
* Frameworks regulatorios y de cumplimiento: NIST AI RMF, EU AI Act y SLSA.

---

### Conceptos Clave / Key Concepts

#### Pilar 1 — Gobernanza de Datos y Procedencia

**Los datos son el componente más fundamental — y más pasado por alto — de la cadena de suministro.** Asegurar el pipeline de datos de entrenamiento requiere:

**Tracking de Data Lineage:** Cada muestra de entrenamiento debe tener un registro de procedencia: de dónde vino, quién la recopiló, cuándo, bajo qué licencia y si ha sido revisada.

```yaml
# Example data lineage record (stored in metadata sidecar)
dataset_record:
  source: "CommonCrawl-2023-Q3"
  ingestion_date: "2023-09-15"
  ingestion_engineer: "data-pipeline-svc@company.com"
  review_status: "approved"
  reviewer: "alice@company.com"
  integrity_hash: "sha256:3f8a9d2e..."
  licence: "CC-BY-4.0"
  pii_scan: "passed"
  poison_scan: "passed"
```

**Verificación de Integridad de Datos:** Cada versión de dataset debe tener hash criptográfico. Antes de que comience el entrenamiento, el pipeline verifica el hash contra un manifest de confianza:

```bash
# Generate manifest at data preparation time
sha256sum training_data/*.parquet > MANIFEST.sha256

# Verify before training (in CI/CD)
sha256sum --check MANIFEST.sha256
# If any file has changed: ABORT TRAINING
```

**Pipeline de Sanitización de Datos:** Antes de que los datos entren al pipeline de entrenamiento, pasan por:
1. **PII scrubbing** — eliminar información personal identificable.
2. **Deduplication** — los duplicados excesivos amplifican los efectos del envenenamiento de datos.
3. **Anomaly detection** — la detección estadística de outliers marca muestras potencialmente envenenadas.
4. **Human review** — para categorías de alto riesgo, aprobación humana obligatoria.

#### Pilar 2 — Procedencia y Firma de Modelos

**Model cards** (popularizadas originalmente por Google y Hugging Face) proporcionan metadatos legibles por humanos sobre el proceso de entrenamiento, los datos y el uso previsto de un modelo. Para seguridad, esto debe extenderse con **firma criptográfica**:

```bash
# After training, sign the model with your organization's private key
cosign sign-blob --key cosign.key model_weights.safetensors > model.sig

# Before deploying, any party can verify:
cosign verify-blob --key cosign.pub \
  --signature model.sig \
  model_weights.safetensors
# ✅ Verified OK — provenance chain intact
```

**Herramientas:**
* **Sigstore/Cosign** — firma keyless para artefactos ML (la misma herramienta usada para firma de contenedores).
* **DVC (Data Version Control)** — versionado tipo Git para datasets y artefactos de modelo.
* **MLflow** — rastrea lineage de modelo, parámetros y métricas con registros de run inmutables.

**Enforcement de SafeTensors:** Mandatar el formato SafeTensors para todos los artefactos de modelo. Pickle y formatos antiguos deben **bloquearse a nivel de registro**:

```python
# Registry upload hook — reject Pickle files
def validate_upload(file_path: str):
    if file_path.endswith((".pkl", ".pickle", ".pt")):
        raise SecurityError(
            f"Unsafe serialization format rejected: {file_path}. "
            f"Please use SafeTensors format."
        )
    run_modelscan(file_path)  # Additional malware scanning
```

#### Pilar 3 — Gestión de Dependencias

**Software Bill of Materials (SBOM) para ML:** Un **ML-SBOM** documenta cada dependencia en el stack ML: paquetes de Python, sus versiones y sus dependencias transitivas. Generado en tiempo de build y firmado:

```bash
# Generate SBOM for ML environment
pip-audit --requirement requirements.txt --format cyclonedx-json > sbom.json
syft scan . -o spdx-json > sbom-spdx.json

# Audit for known CVEs
pip-audit --requirement requirements.txt
```

**Mirror de Paquetes Privado + Lock Files:**
```bash
# Use a private Artifactory/Nexus mirror — block direct PyPI access
pip install --index-url https://pypi.internal.company.com/simple/ \
            --no-index \
            -r requirements.txt

# Pin ALL dependencies with hashes
pip-compile --generate-hashes requirements.in > requirements.txt
# requirements.txt now contains:
# torch==2.1.0 \
#   --hash=sha256:3f8a9d2e... \
#   --hash=sha256:7b2c1e4f...
```

**Revisión de Dependencias en CI/CD:**
```yaml
# GitHub Actions — auto-review new dependencies
- name: Dependency Review
  uses: actions/dependency-review-action@v3
  with:
    fail-on-severity: moderate
    deny-licenses: GPL-3.0, AGPL-3.0
```

#### Pilar 4 — Hardening del Pipeline MLOps

**Service Accounts de Menor Privilegio:** Cada componente del pipeline ML debe ejecutarse con los permisos mínimos necesarios:

| Etapa del Pipeline | Permisos Requeridos | NO Requeridos |
|---------------|---------------------|--------------|
| Data ingestion | Leer del bucket S3 | Escribir en el registro de modelos |
| Training job | Leer datos, escribir artefactos | Acceso a la base de datos de producción |
| Evaluation | Leer modelo, leer test set | Escribir en datos de entrenamiento |
| Deployment | Push al registro de producción | Acceso a datos de entrenamiento |

**Gestión de Secretos:**
```bash
# NEVER do this:
HUGGINGFACE_TOKEN=hf_abc123  # Hardcoded in .env or code

# DO this — use a secrets manager:
export HUGGINGFACE_TOKEN=$(aws secretsmanager get-secret-value \
  --secret-id prod/ml/huggingface-token \
  --query SecretString --output text)
```

**Artefactos Inmutables y Puertas de Promoción:**
```
[Development] → [Staging] → [Production]
    ↓               ↓              ↓
 Any version     Signed + scanned  Signed + scanned
                 + human approval  + security gate
                                   + rollback plan
```

#### Pilar 5 — Detección de Backdoors

Incluso con todos los controles de prevención, asume la brecha — e implementa detección:

* **Neural Cleanse:** Analiza el comportamiento del modelo para detectar "atajos" anómalos en la toma de decisiones que podrían indicar un trigger de backdoor. Funciona haciendo reverse-engineering de triggers potenciales para cada clase y marcando clases con tamaños de trigger anormalmente pequeños (un indicador de implantación de backdoor).
* **Activation Clustering:** Examina las activaciones internas de una red neuronal en muestras limpias vs. potencialmente envenenadas. Las muestras con backdoor a menudo se agrupan anómalamente en el espacio de activaciones — distinto de la distribución natural de muestras limpias.
* **Spectral Signature Detection:** Las muestras envenenadas dejan un rastro detectable en la **descomposición de valores singulares** de sus representaciones de features. Un outlier espectral repentino en un batch de entrenamiento es un fuerte indicador de envenenamiento de datos.

```python
# Simplified spectral signature detection
import numpy as np
from sklearn.decomposition import TruncatedSVD

def detect_poisoning(features: np.ndarray, top_k: int = 5) -> bool:
    """Returns True if spectral anomalies suggest poisoning."""
    svd = TruncatedSVD(n_components=top_k)
    svd.fit(features)
    # Anomalous variance concentration in top singular vectors
    variance_ratio = svd.explained_variance_ratio_[0]
    return variance_ratio > 0.8  # Threshold from literature
```

---

### Tarea 1 — Seguridad de Serialización de Modelos / Model Serialization Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What serialisation format was created by Hugging Face to replace pickle for ML models? | `SafeTensors` |
| What PyTorch parameter prevents code execution when loading pickle-based models? | `weights_only=True` |

---

### Tarea 2 — Framework de Adquisición de Modelos / Model Acquisition Framework

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the first step in the Model Acquisition Framework when a new model is received? | `Quarantine` |
| Examine the checksums on the VM. Which model file does not match its expected hash? | `model_review_v2.pkl` |

---

### Tarea 3 — Análisis de Telemetría / Telemetry Analysis

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What object type does the compromised model's telemetry show on load completion, instead of a model? | `int` |

---

### Tarea 4 — Herramientas de Análisis Estático / Static Analysis Tools

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which Trail of Bits tool performs static analysis of pickle files? | `Fickling` |
| What severity level does ModelScan assign to an `os.system` call in a model file? | `CRITICAL` |

---

### Tarea 5 — Inspección de Arquitectura / Architecture Inspection

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Open the Telemetry terminal. How many layers does the compromised model's architecture contain? | `5` |

---

### Tarea 6 — Capas Sospechosas / Suspicious Layers

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Run `inspect_h5_model.py` on `image_classifier_v2.h5`. What is the name of the suspicious Lambda layer? | `manipulate_output` |

---

### Tarea 7 — Seguridad de Dependencias / Dependency Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the recommended practice for specifying package versions in requirements.txt? | `Version Pinning` |
| What tool scans Python dependencies against known vulnerability databases? | `pip-audit` |
| Which SBOM format is maintained by OWASP and focuses on security? | `CycloneDX` |

---

### Tarea 8 — Gobernanza de Cadena de Suministro LLM / LLM Supply Chain Governance

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What should you establish to detect when an API provider silently updates their model? | `Behavioural Baseline` |
| What type of artefact should be version-controlled and reviewed like code, to prevent untrusted content from altering LLM behaviour? | `System Prompts` |
| What company name does Config B identify as the service provider? | `TryTrainML` |

---

### Flags / Final Answers (rahul_ai)

| Flag # | Valor / Value |
|--------|-------|
| Flag 1 (Data Governance) | `THM{d4t4_pr0v3n4nc3_s3cur3d}` |
| Flag 2 (Model Signing) | `THM{c0s1gn_m0d3l_s1gn3d_s4f3}` |
| Flag 3 (Backdoor Detection) | `THM{n3ur4l_cl34ns3_b4ckd00r_cl4ss2}` |

---

### Conclusiones Personales / Personal Takeaways

* **Cadena de suministro de IA segura = cadena de suministro tradicional segura + 3 nuevas capas**: procedencia de datos, firma de modelos y detección de backdoors. Las organizaciones con DevSecOps maduro pueden adaptar esos controles con esfuerzo adicional relativamente modesto — el tooling está cada vez más disponible.
* **La adopción de SafeTensors debería ser un mandato organizacional duro**, no una recomendación. El cálculo de riesgo-recompensa es simple: Pickle no ahorra nada y cuesta todo si se carga un modelo envenenado. No hay razón legítima para usar Pickle para distribución de modelos en 2025.
* **La detección de backdoors debería ser parte de cada pipeline de evaluación de modelos** — especialmente para modelos de fuentes externas o fine-tuneados. Neural Cleanse y Activation Clustering son computacionalmente baratos comparados con el costo de enviar un modelo con backdoor a producción.
* El **panorama regulatorio está convergiendo** en requisitos de cadena de suministro. El EU AI Act manda documentación técnica y trazabilidad. NIST AI RMF requiere gobernanza sobre datos de entrenamiento. SLSA (Supply Chain Levels for Software Artifacts) se está aplicando cada vez más a ML. El cumplimiento proactivo con estos frameworks es tanto un imperativo de seguridad como de negocio.

---

* **Fuente / Source:**
  * [RAHULKATARA1/TryHackMe-AI-Security-Path — securing-the-ai-supply-chain](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path/tree/main/Section-4-AI-Supply-Chain-Security/03-securing-the-ai-supply-chain)
  * [Answers for the TryHackMe Securing the AI Supply Chain Room — Simon Taplin](https://simontaplin.net/2026/06/21/answers-for-the-tryhackme-securing-the-ai-supply-chain-room/)

*Documentación para propósitos educativos y registro de CTF.*
