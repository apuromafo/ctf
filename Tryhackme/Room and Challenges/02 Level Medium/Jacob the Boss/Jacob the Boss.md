# Jacob the Boss

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `jacobtheboss` |
| **Link** | [TryHackMe](https://tryhackme.com/room/jacobtheboss) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Cracking / Hashes / Password Cracking / Análisis de archivos | **Impacto** | Reto práctico donde se obtienen los dos hashes objetivo de la sala para su posterior cracking, cerrando la fase de extracción de credenciales |

---

**Contexto:** Sala práctica centrada en el tratamiento de hashes obtenidos del objetivo ("Jacob the Boss"). Se extraen los dos valores hash que representan la fase de recolección de material para el cracking posterior:

## Solucionario

### Task 1: Obtener los Hashes del Objetivo

**Explicación:** Los dos hashes de la sala:

1. 1. `f4d491f280de360cc49e26ca1587cbcc`
   2. `29a5641eaa0c01abe5749608c8232806`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer hash obtenido? | `f4d491f280de360cc49e26ca1587cbcc` |
| 2 | ¿Cuál es el segundo hash obtenido? | `29a5641eaa0c01abe5749608c8232806` |

---

**Metodología:**
1. Localizar y extraer los recursos del objetivo.
2. Calcular/capturar los hashes de los archivos obtenidos.
3. Registrar los dos hashes para la fase de cracking.

**Learning chain:** Objetivo → extracción → hash 1 (f4d491f2...) → hash 2 (29a5641e...)

**Lección:** *Toda cadena de cracking empieza por una buena recolección: obtener de forma íntegra los hashes objetivos es prerrequisito para la fase de fuerza bruta o diccionario de la sala.*

**MITRE ATT&CK:** T1003.001 - OS Credential Dumping: LSASS Memory; T1110.002 - Brute Force: Password Cracking; T1083 - File and Directory Discovery; la sala es principalmente de extracción/cracking de hashes.

**Fuente:** [TryHackMe - Jacob the Boss](https://tryhackme.com/room/jacobtheboss)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.