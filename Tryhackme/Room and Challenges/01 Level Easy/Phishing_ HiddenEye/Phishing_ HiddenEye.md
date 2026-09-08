# Phishing: HiddenEye

| **Dificultad** | Easy |
| **Tipo** | Sala teórica (phishing) |
| **Slug** | `phishinghiddeneye` |
| **Link** | [TryHackMe](https://tryhackme.com/room/phishinghiddeneye) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Phishing / HiddenEye / HTTPS / ciberseguridad humana / phishing pages |
| **Impacto** | Sala que explica qué es HiddenEye, una herramienta ofensiva usada para crear campañas de phishing, cómo se ve una página de phishing frente a una legítima, el propósito educativo de estas herramientas, el eslabón más débil de la ciberseguridad (humanos) y un dato clave: la mayoría de las páginas de phishing se sirven por HTTPS. |

---

**Contexto:** HiddenEye es una herramienta que permite a un atacante construir páginas de phishing atractivas que imitan servicios legítimos, además de facilitar la creación de correos falsos. La sala advierte que la herramienta debe usarse con fines académicos y éticos. Sus claves para detección: aunque una página de phishing active HTTPS (y de hecho la mayoría lo tiene), el factor humano sigue siendo el eslabón más débil; por eso se debe inspeccionar no solo el candado sino la URL real, el dominio y cualquier diferencia visual sutil frente a la página legítima.

## Solucionario

### Task 1: Introducción

**Explicación:** La tarea introduce el concepto de phishing y de la herramienta HiddenEye. Son pasos de lectura; en el volcado original hay 16 sub-pasos, todos sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue los pasos de lectura de la introducción (16 sub-pasos). | `No answer needed` |

### Task 2: Despliegue y recursos

**Explicación:** Se desplegó la máquina de la sala y se revisaron los recursos asociados. Los 4 sub-pasos son de ejecución/lectura; ninguno requiere una respuesta concreta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee los recursos y despliega la máquina de la sala (4 sub-pasos). | `No answer needed` |

### Task 3: Preguntas de la sala

**Explicación:** De los 17 ítems de la tarea, solo 4 corresponden a preguntas con respuesta. La clave del análisis visual: una página clonada de phishing puede verse idéntica a la legítima y tener HTTPS habilitado; la intención de uso debe ser educativa y el eslabón más débil sigue siendo el ser humano.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué imagen muestra una página web legítima? Son idénticas y la mayoría de las páginas de phishing hoy tienen HTTPS habilitado (Image 1 o Image 2). | `Image 2` |
| 2 | ¿Para qué usarás esta herramienta? | `Educational Purposes` |
| 3 | ¿Cuál es el eslabón más débil en ciberseguridad? | `humans` |
| 4 | ¿La mayoría de las páginas de phishing tienen HTTPS (Yay/Nay)? | `Yay` |

---

**Metodología:** Lectura de la teoría de phishing y de HiddenEye → análisis visual de páginas (clonada vs. legítima) → reflexión sobre el uso ético y el factor humano → verificación del uso de HTTPS en campañas reales.
**Learning chain:** entender el phishing → conocer HiddenEye como herramienta de creación de páginas/emails → detectar páginas clonadas pese al HTTPS → concluir que el ser humano es el eslabón más débil.
**MITRE ATT&CK:** T1566 (Phishing), T1566.002 (Spearphishing Link), T1204.001 (User Execution: Malicious Link), T1036 (Masquerading), T1598 (Phishing for Information)
**Fuente:** [TryHackMe - Phishing: HiddenEye](https://tryhackme.com/room/phishinghiddeneye)