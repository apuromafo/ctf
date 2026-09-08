# Detecting Adversarial Attacks

| **Dificultad** | MEDIUM | **Tipo** | Premium | **Slug** | `idadversarialattacks` |
| **Link** | [TryHackMe](https://tryhackme.com/room/idadversarialattacks) | **Sección** | 02 Level Medium | **Fuente** | Simon Taplin (writeup) |
| **Componentes** | Adversarial Attacks / PGD / BIM / FGSM / ML Detection / Hands-on Lab | **Impacto** | Enseña a identificar y analizar ataques adversariales contra modelos de IA |

---

**Contexto:** Sala para aprender a identificar y analizar ataques adversariales contra modelos de IA. Learn how to identify and analyse adversarial attacks against AI models.

## Solucionario

### Task 1: Introduction to Adversarial Attacks

**Explicación:** Se introducen los ataques adversariales más comunes. El ataque PGD (Projected Gradient Descent) es ampliamente usado para probar la robustez de los modelos ML. El ataque BIM (Basic Iterative Method) extiende las perturbaciones sobre múltiples iteraciones. FGSM significa **Fast Gradient Sign Method** (Método del Signo del Gradiente Rápido).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What adversarial attack is widely used for testing the robustness of ML models? | `PGD` |
| 2 | What adversarial attack spreads perturbations over multiple iterations? | `BIM` |
| 3 | What does FGSM stand for? | `Fast Gradient Sign Method` |

### Task 2: Detecting Adversarial Attacks

**Explicación:** Algunos ataques son más difíciles de detectar que otros. El ataque PGD es usualmente el más difícil de detectar por un modelo de IA, debido a su naturaleza iterativa y optimizada. El ataque FGSM tiene cambios mínimos a nivel de píxel (perturbación de un solo paso), siendo más detectable.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which attack is usually the hardest to detect by an AI model? | `PGD` |
| 2 | Which attack has minimal pixel-level changes? | `FGSM` |

### Task 3: Hands-on Lab

**Explicación:** Lab práctico donde se obtienen las flags de cada ataque (BIM, FGSM, PGD). Al obtener cada flag, reinicia el kernel y regenera todas las opciones antes de continuar. After getting each flag, restart the kernel and regenerate all options before continuing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag for BIM? | `THM{32d70a18c100}` |
| 2 | What's the flag for FGSM? | `THM{2c1eed7b927f}` |
| 3 | What's the flag for PGD? | `THM{fe0f9ac5b371}` |

---

**Metodología:**
1. Identificar los ataques adversariales básicos (PGD, BIM, FGSM) y sus características.
2. Entender qué ataques son más difíciles de detectar (PGD iterativo) y cuáles tienen cambios mínimos (FGSM).
3. En el lab práctico, ejecutar cada ataque (BIM, FGSM, PGD), capturar la flag y reiniciar el kernel/regenerar opciones antes de continuar.

**Learning chain:** Adversarial attacks intro → PGD (robustness testing) → BIM (multiple iterations) → FGSM (Fast Gradient Sign Method) → Detection (PGD hardest, FGSM minimal pixels) → Lab: BIM flag → FGSM flag → PGD flag

**Lección:** *Los ataques adversariales iterativos como PGD son los más difíciles de detectar, mientras que FGSM usa cambios mínimos en un solo paso; conocerlos es clave para construir defensas robustas.*

**MITRE ATT&CK:** T1565.002 (Data Manipulation: Transmitted Data Manipulation), NVD CWE-20 (Improper Input Validation)

**Fuente:** [TryHackMe - Detecting Adversarial Attacks](https://tryhackme.com/room/idadversarialattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
