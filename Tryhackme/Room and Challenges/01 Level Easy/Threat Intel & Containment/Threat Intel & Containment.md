# Threat Intel & Containment

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `threatintelcontainment` | [TryHackMe - Threat Intel & Containment](https://tryhackme.com/room/threatintelcontainment) | 01 Level Easy | THM | Threat intelligence, APT, isolación, hash, C2 | Estrategias de inteligencia de amenazas y contención de incidentes |

---

**Contexto:** La sala cubre inteligencia de amenazas aplicada a la contención de incidentes: detección, estrategias de aislamiento (controlado e integral), indicadores como hashes, comportamiento de malware y actividades de C2.

> **ES:** Ejercicio de inteligencia de amenazas y contención: tipos de aislamiento, detección basada en host y la diferencia entre lista blanca, negra y análisis de hash.
> **EN:** Threat intelligence and containment exercise: isolation strategies, host-based detection, and the difference between whitelisting, blacklisting and hash analysis.

## Solucionario

### Task 1: Respuestas del ejercicio / Exercise answers

**Explicación:** Solución del ejercicio de Threat Intel & Containment: se responden las preguntas de detección, aislamiento e indicadores de compromiso.

1. No answer needed
2. Intrusion Detection System
3. 1. Controlled Isolation
   2. Entire Isolation
4. Hash
5. Whack-a-mole
6. 1. 3.250.38.141
   2. dropper.exe
   3. 463F1B1E11D4CA4C7A0C9AAC540513FF7E681D9E5144BDA2AF24B86E438D3F4F
7. No answer needed

### Tabla unificada de preguntas / Unified Q&A

| # | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2 | `Intrusion Detection System` |
| 3 | `Controlled Isolation` / `Entire Isolation` |
| 4 | `Hash` |
| 5 | `Whack-a-mole` |
| 6 | `3.250.38.141` / `dropper.exe` / `463F1B1E11D4CA4C7A0C9AAC540513FF7E681D9E5144BDA2AF24B86E438D3F4F` |
| 7 | `No answer needed` |

---

**Metodología:** Se contrastan las estrategias de contención (aislamiento controlado frente a aislamiento integral), los mecanismos de detección (IDS), el análisis por hash como indicador de compromiso y el reparto de objetivos de dentro y fuera del perímetro (Whack-a-mole), identificando IP, binario dropper y hash SHA-1 del malware.

### Cadena de ataque / Attack Chain

1. Reconocimiento del incidente y activación del IDS.
2. Aplicación de aislamiento controlado o integral según alcance.
3. Identificación del malware por hash y localización del dropper.
4. Seguimiento del C2 (3.250.38.141) para contener la comunicación.
5. Contención y eliminación de la amenaza.

**Learning chain:** Threat intel → detection → isolation strategies → IOC analysis → containment

**Lección:** *La contención eficaz combina inteligencia de amenazas, análisis de indicadores (IP, dropper, hash) y una estrategia de aislamiento elegida según el alcance real del incidente.*

**MITRE ATT&CK:** T1071.001 - Application Layer Protocol: Web Protocols, T1204.002 - User Execution: Malicious File, T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Threat Intel & Containment](https://tryhackme.com/room/threatintelcontainment)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.