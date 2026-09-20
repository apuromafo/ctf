# Metamorphosis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Malware | metamorphosis | https://tryhackme.com/room/metamorphosis | 02 Level Medium | TryHackMe | Metamorphic malware, hash analysis | Identificación y correlación de variantes de malware metamórfico |

---

**Contexto:** La sala **Metamorphosis** es un CTF de análisis de **malware metamórfico**. El malware reescribe su propio código en cada generación, cambiando su apariencia sintáctica pero conservando la funcionalidad, lo que dificulta la detección por firmas. Mediante el cálculo de hashes de las muestras se rastrean las variantes generadas por el motor metamórfico y se identifican los checksums del binario y de su payload.

## Solucionario

### Task 1: Rastrear las variantes
**Explicación:**

Se obtienen las variantes metamórficas del binario (muestra original y regenerada por el motor) y se calculan sus hashes **MD5** para identificarlas y correlacionarlas.

1. `4ce794a9d0019c1f684e07556821e0b0`
2. `7ffca2ec63534d165525bf37d91b4ff4`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Hash MD5 de la primera variante | `4ce794a9d0019c1f684e07556821e0b0` |
| 2 | Hash MD5 de la segunda variante | `7ffca2ec63534d165525bf37d91b4ff4` |

---

**Metodología:** Generación/captura de muestras metamórficas, cálculo de hashes MD5 y correlación de variantes del mismo malware.

**Learning chain:** Muestras metamórficas → hashing MD5 → comparación de variantes → evidencia de mutación.

**Lección:** *El malware metamórfico cambia su sintaxis pero no su comportamiento: los hashes siguen siendo útiles para rastrear cada generación y demostrar la mutación entre variantes.*

**MITRE ATT&CK:** T1027.002 Obfuscated Files or Information: Software Packing.

**Fuente:** [TryHackMe - Metamorphosis](https://tryhackme.com/room/metamorphosis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.