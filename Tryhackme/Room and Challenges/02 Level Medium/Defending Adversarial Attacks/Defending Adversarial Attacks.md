# Defending Adversarial Attacks

| **Dificultad** | MEDIUM | **Tipo** | Premium | **Slug** | `defadversarialattacks` |
| **Link** | [TryHackMe](https://tryhackme.com/room/defadversarialattacks) | **Sección** | 02 Level Medium | **Fuente** | Simon Taplin (writeup) |
| **Componentes** | Gradient Hiding / MagNet / Regularization / FGSM / PGD / Adversarial Defenses | **Impacto** | Cubre los fundamentos de hardening de modelos de ML contra ataques adversariales |

---

**Contexto:** Sala centrada en los fundamentos de hardening de modelos de ML: gradient hiding, MagNet, y regularización. ML model hardening basics: gradient hiding, MagNet, regularization.

## Solucionario

### Task 1: Gradient Hiding

**Explicación:** La técnica de gradient hiding consiste en ocultar los gradientes del modelo para impedir que los ataques basados en gradientes puedan calcular perturbaciones. El ataque basado en gradiente contra el que mejor defiende el gradient hiding es FGSM (Fast Gradient Sign Method), que usa el signo del gradiente para generar la perturbación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which gradient-based attack does gradient hiding defend against best? | `FGSM` |

### Task 2: MagNet Architecture

**Explicación:** MagNet es una arquitectura de defensa que añade componentes para rechazar y reparar entradas adversarias. Se añade la etiqueta `NULL` al modelo para rechazar entradas adversariales. El componente **Detector** comprueba si una entrada parece normal, y el componente **Reformer** repara las entradas ligeramente perturbadas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which label is added to a model to reject adversarial inputs? | `NULL` |
| 2 | Which component in MagNet checks if an input looks normal? | `Detector` |
| 3 | Which component in MagNet repairs slightly perturbed inputs? | `Reformer` |

### Task 3: Regularization and Overfitting

**Explicación:** El exceso de epochs en el entrenamiento conduce al sobreajuste (overfitting), donde el modelo memoriza los datos de entrenamiento en lugar de generalizar. La regularización se usa para mitigar el overfitting. El ataque PGD (Projected Gradient Descent) es un ataque iterativo que se usa para evaluar la robustez de modelos robustos frente a ese sobreentrenamiento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What can happen if you run too many epochs? | `Overfitting` |
| 2 | What can happen if you run too many epochs? | `PGD` |

---

**Metodología:**
1. Aplicar gradient hiding para obstaculizar ataques basados en gradientes como FGSM.
2. Implementar MagNet: añadir la etiqueta NULL para rechazar entradas adversariales, el Detector para comprobar normalidad y el Reformer para reparar entradas perturbadas.
3. Controlar las epochs para evitar overfitting y aplicar regularización.
4. Usar ataques iterativos como PGD para evaluar la robustez de las defensas.

**Learning chain:** Gradient Hiding → FGSM defense → MagNet → NULL label reject → Detector (normal check) → Reformer (repair) → Epochs/Overfitting → Regularization → PGD robust evaluation

**Lección:** *El hardening de modelos de ML combina la ocultación de gradientes (FGSM), arquitecturas como MagNet (NULL/Detector/Reformer) y la regularización para mitigar overfitting y resistir ataques iterativos como PGD.*

**MITRE ATT&CK:** T1565.002 (Data Manipulation: Transmitted Data Manipulation), NVD CWE-20 (Improper Input Validation)

**Fuente:** [TryHackMe - Defending Adversarial Attacks](https://tryhackme.com/room/defadversarialattacks)
