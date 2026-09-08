# Securing the AI Supply Chain

| **Dificultad** | Medium |
| **Tipo** | Theory + Lab |
| **Slug** | `securingtheaisupplychain` |
| **Link** | [TryHackMe](https://tryhackme.com/room/securingtheaisupplychain) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | data governance / model signing / SBOM / MLOps hardening / backdoor detection / NIST AI RMF / EU AI Act / SLSA |
| **Impacto** | Arquitectar un pipeline de desarrollo de IA resiliente, auditable y endurecido en cada eslabón de la cadena |

---

**Contexto:** Entender los ataques es solo la mitad de la misión. Esta room cubre el playbook defensivo completo para la seguridad de la cadena de suministro de IA: desde gobernanza de datos y procedencia de modelos hasta hardening de MLOps y cumplimiento regulatorio.

## Solucionario

### Task 1: Seguridad de Serialización de Modelos / Model Serialization Security

**Explicación:**

**Pilar 2 — Procedencia y Firma de Modelos:** Los **model cards** (popularizadas originalmente por Google y Hugging Face) proporcionan metadatos legibles por humanos sobre el proceso de entrenamiento, los datos y el uso previsto de un modelo. Para seguridad, esto debe extenderse con **firma criptográfica**:

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What serialisation format was created by Hugging Face to replace pickle for ML models? | `SafeTensors` |
| 2 | What PyTorch parameter prevents code execution when loading pickle-based models? | `weights_only=True` |

### Task 2: Framework de Adquisición de Modelos / Model Acquisition Framework

**Explicación:**

El primer paso en el Model Acquisition Framework al recibir un nuevo modelo es ponerlo en **cuarentena** (Quarantine). En la VM, examinando los checksums, el archivo que no coincide con su hash esperado es `model_review_v2.pkl`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first step in the Model Acquisition Framework when a new model is received? | `Quarantine` |
| 2 | Examine the checksums on the VM. Which model file does not match its expected hash? | `model_review_v2.pkl` |

### Task 3: Análisis de Telemetría / Telemetry Analysis

**Explicación:**

La telemetría del modelo comprometido muestra, al completar la carga, un objeto de tipo **`int`** en lugar de un modelo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What object type does the compromised model's telemetry show on load completion, instead of a model? | `int` |

### Task 4: Herramientas de Análisis Estático / Static Analysis Tools

**Explicación:**

**Herramientas de detección de backdoors (Pilar 5):** Incluso con todos los controles de prevención, asume la brecha — e implementa detección:

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which Trail of Bits tool performs static analysis of pickle files? | `Fickling` |
| 2 | What severity level does ModelScan assign to an `os.system` call in a model file? | `CRITICAL` |

### Task 5: Inspección de Arquitectura / Architecture Inspection

**Explicación:**

Al abrir el terminal de Telemetría, la arquitectura del modelo comprometido contiene **5** capas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Open the Telemetry terminal. How many layers does the compromised model's architecture contain? | `5` |

### Task 6: Capas Sospechosas / Suspicious Layers

**Explicación:**

Ejecutando `inspect_h5_model.py` sobre `image_classifier_v2.h5`, el nombre de la capa Lambda sospechosa es `manipulate_output`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run `inspect_h5_model.py` on `image_classifier_v2.h5`. What is the name of the suspicious Lambda layer? | `manipulate_output` |

### Task 7: Seguridad de Dependencias / Dependency Security

**Explicación:**

**Pilar 3 — Gestión de Dependencias:** Un **ML-SBOM** documenta cada dependencia en el stack ML: paquetes de Python, sus versiones y sus dependencias transitivas. Generado en tiempo de build y firmado:

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the recommended practice for specifying package versions in requirements.txt? | `Version Pinning` |
| 2 | What tool scans Python dependencies against known vulnerability databases? | `pip-audit` |
| 3 | Which SBOM format is maintained by OWASP and focuses on security? | `CycloneDX` |

### Task 8: Gobernanza de Cadena de Suministro LLM / LLM Supply Chain Governance

**Explicación:**

Para detectar cuándo un proveedor API actualiza silenciosamente su modelo, se establece una **Behavioural Baseline** (línea base de comportamiento). Los **System Prompts** deben versionarse y revisarse como código, para evitar que contenido no confiable altere el comportamiento del LLM. En la Config B, la empresa proveedora del servicio se identifica como **TryTrainML**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What should you establish to detect when an API provider silently updates their model? | `Behavioural Baseline` |
| 2 | What type of artefact should be version-controlled and reviewed like code, to prevent untrusted content from altering LLM behaviour? | `System Prompts` |
| 3 | What company name does Config B identify as the service provider? | `TryTrainML` |

### Flags / Final Answers (rahul_ai)

**Explicación:**

Flags obtenidos en el laboratorio de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 (Data Governance) | `THM{d4t4_pr0v3n4nc3_s3cur3d}` |
| 2 | Flag 2 (Model Signing) | `THM{c0s1gn_m0d3l_s1gn3d_s4f3}` |
| 3 | Flag 3 (Backdoor Detection) | `THM{n3ur4l_cl34ns3_b4ckd00r_cl4ss2}` |

---

**Metodología:**

1. **Pilar 1 — Gobernanza de Datos y Procedencia:** tracking de data lineage, verificación de integridad (hash + manifest), y pipeline de sanitización (PII scrubbing, deduplication, anomaly detection, human review). Los datos son el componente más fundamental — y más pasado por alto — de la cadena de suministro.
2. **Pilar 2 — Procedencia y Firma de Modelos:** firma criptográfica (Sigstore/Cosign), versionado (DVC, MLflow) y enforcement de SafeTensors con validación de upload a nivel de registro.
3. **Pilar 3 — Gestión de Dependencias:** ML-SBOM (CycloneDX/SPDX), mirrors privados con lock files y hashes, y dependency review en CI/CD.
4. **Pilar 4 — Hardening del Pipeline MLOps:** service accounts de menor privilegio (por etapa), gestión de secretos con secrets manager, artefactos inmutables y puertas de promoción (`[Development] → [Staging] → [Production]`).
5. **Pilar 5 — Detección de Backdoors:** Neural Cleanse, Activation Clustering y Spectral Signature Detection como backstop cuando falla la prevención.

**Learning chain:** data governance -> lineage/integrity -> model signing (cosign) -> SafeTensors -> ML-SBOM -> lock files -> least-privilege MLOps -> backdoor detection -> SLSA/compliance

**Lección:** *La adopción de SafeTensors que debería ser un mandato organizacional duro, y la detección de backdoors (Neural Cleanse, Activation Clustering) parte de cada pipeline de evaluación de modelos: el EU AI Act, NIST AI RMF y SLSA están convergiendo en requisitos de cadena de suministro.*

**MITRE ATT&CK:** T1185 (Browser Session Hijacking) · T1204 (User Execution) · CWE-502 (Deserialization of Untrusted Data) · CWE-94 (Code Injection) · CWE-829 (Inclusion of Functionality from Untrusted Control Sphere)

**Fuente:** [TryHackMe - Securing the AI Supply Chain](https://tryhackme.com/room/securingtheaisupplychain)
