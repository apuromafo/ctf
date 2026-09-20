# Signature Evasion
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `signatureevasion` |
| **Link** | [TryHackMe](https://tryhackme.com/room/signatureevasion) |
| **Sección** | Red Team / Malware Development / Evasion |
| **Fuente** | TryHackMe |
| **Componentes** | AV Signature Evasion, Portable Executable (PE), obfuscación, packers/crypters, in-memory evasion, IAT, Shellcode |
| **Impacto** | Comprende cómo funcionan las firmas de antivirus y las técnicas de evasión a nivel de binario (PE, obfuscación, cifrado, ejecución en memoria) para modificar implantes y evitar la detección estática/dinámica. |
---
**Contexto:** Esta room explora las técnicas que usan los desarrolladores de malware para evadir las firmas de antivirus (AV/EDR). Se estudia la estructura del **Portable Executable (PE)**, los distintos tipos de firmas estáticas y dinámicas, y técnicas de evasión como la ofuscación, el uso de packers/crypters, la modificación de la IAT y la ejecución en memoria (in-memory evasion). El objetivo es entender qué mira un AV y cómo un implante puede reducir su superficie de detección.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de la sala y de los objetivos de aprendizaje sobre evasión de firmas. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: Signature Identification / Identificación de firmas
**Explicación:** Se explica cómo los antivirus identifican malware mediante firmas (hashes, byte patterns, heurística) y cómo obtener métricas del binario/telemetría. La respuesta numérica corresponde a la observación del dato consultado en la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Observación inicial (sin respuesta requerida). | `No answer needed` |
| 2. What is the observed value for the signature-related data? | `51000` |
### Task 3: Portable Executable / Ejecutable Portable (PE)
**Explicación:** Estructura de un archivo PE (DOS header, NT headers, File Header, Optional Header, secciones `.text`, `.data`, etc.) y cómo ciertos valores de cabecera (checksum, entry point, campos de sección) influyen en la detección. La respuesta es un valor hexadecimal de cabecera.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Observación sobre la cabecera PE (sin respuesta requerida). | `No answer needed` |
| 2. What is the value related to the PE header? | `0xC544` |
### Task 4: Challenge / Reto
**Explicación:** Reto práctico donde se aplican técnicas de evasión para obtener la flag. El resultado confirma la comprensión del material de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag del reto. | `THM{70_D373C7_0r_70_N07_D373C7}` |
### Task 5: Obfuscation / Ofuscación
**Explicación:** Técnicas de ofuscación para romper firmas basadas en cadena/byte patterns (cifrado de strings, encoding, generación dinámica de código). La respuesta es un valor numérico asociado al dato de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Observación sobre la ofuscación (sin respuesta requerida). | `No answer needed` |
| 2. What is the observed value for the obfuscated artifact? | `6.354` |
### Task 6: In-Memory Evasion / Evasión en memoria
**Explicación:** Ejecución de shellcode en memoria sin tocar disco, evitando las firmas estáticas del fichero. La flag se obtiene completando el reto de esta sección.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag del reto de evasión en memoria. | `THM{N0_1MP0r75_F0r_Y0U}` |
### Task 7: Additional Evasion Techniques / Técnicas adicionales
**Explicación:** Otras técnicas de evasión: modificación de la IAT, packers, anti-sandbox y automatización por firmas. La flag completa el reto de ofuscación de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag del reto de ofuscación. | `THM{08FU5C4710N_15 MY_10V3_14N6U463}` |
### Task 8: Conclusion / Conclusión
**Explicación:** Cierre de la sala con recomendaciones para practicar desarrollo de malware y evasión de forma ética. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conclusión de la sala (sin preguntas). | `No answer needed` |
---
**Metodología:** Entender el modelo de detección del AV → analizar el PE y sus cabeceras → identificar dónde viven las firmas → aplicar ofuscación/cifrado → ejecutar en memoria → validar la evasión con las flags del reto.
### Cadena de ataque / Attack Chain
```
Implante (PE) -> firma detectable -> modificación de cabeceras/strings (obfuscación) -> cifrado/packing -> ejecución en memoria -> evasión del AV
```
**Learning chain:** cómo detecta un AV → estructura PE → ofuscación → ejecución en memoria → superficie de detección reducida.
**Lección:** *La evasión de firmas es una carrera de gato y ratón: cada técnica rompe un tipo de firma concreta (estática, heurística o dinámica) y debe combinarse para reducir la detección sin comprometer la funcionalidad del implante.*
**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1027.002 (Software Packing), T1055 (Process Injection), T1140 (Deobfuscate/Decode Files or Information), T1620 (Reflective Code Loading).
**Fuente:** [TryHackMe - Signature Evasion](https://tryhackme.com/room/signatureevasion)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
