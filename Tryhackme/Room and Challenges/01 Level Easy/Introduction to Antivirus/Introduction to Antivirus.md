# Introduction to Antivirus

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontoantivirus` | [TryHackMe](https://tryhackme.com/room/introductiontoantivirus) | 01 Level Easy | TryHackMe | Antivirus, McAfee, Emulator, Unpacker, Signature, sigtool, Dynamic Detection, Static Analysis | Fundamentos del funcionamiento de los antivirus: firmas, emulación, desempaquetado, detección estática y dinámica |

> **Objeto:** Entender cómo funciona el software antivirus y las técnicas de detección usadas para verificar ficheros maliciosos: qué es un antivirus, sus características (emulador, unpacker), la detección estática por firmas con sigtool/strings y la detección dinámica en entornos virtuales.

---

**Contexto:** Sala que explica cómo funcionan los antivirus: el significado de AV, el primer software antivirus del mercado (McAfee) y su condición de solución basada en host; las características de análisis (emulador que ejecuta código sospechoso en un entorno aislado y unpacker que restaura o desencripta los ejecutables comprimidos); la detección estática con sigtool de ClamAV (hash MD5 de AV-Check.exe y el flag con strings) y la detección dinámica mediante sandboxing para analizar malware en entornos virtuales.

> **ES:** Sala de introducción a los antivirus: firmas, emulador, unpacker, detección estática (sigtool/strings) y detección dinámica en entornos virtuales.
> **EN:** Introduction to antivirus room: signatures, emulator, unpacker, static detection (sigtool/strings) and dynamic detection in virtual environments.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: cómo funcionan los antivirus y qué técnicas de detección se usan para saltarse los chequeos de ficheros maliciosos.

No answer needed

### Task 2: Descripción general / Overview
**Explicación:** Se aprende qué significa AV, qué vendor implementó el primer antivirus del mercado y que el software antivirus es una solución de seguridad basada en host.

1. Antivirus
2. McAfee
3. Host

### Task 3: Características del antivirus / Antivirus Features
**Explicación:** Se describen las características clave del AV: el emulador, que analiza el malware en un entorno seguro y aislado, y el unpacker, que restaura o desencripta los ejecutables comprimidos.

1. Emulator
2. unpacker
3. No answer needed

### Task 4: Detección estática / Static Detection
**Explicación:** Tarea de repaso o demostración sobre el análisis estático: intro.

No answer needed

### Task 5: Detección estática del AV / AV Static Detection
**Explicación:** Se usa sigtool de ClamAV para generar el MD5 del binario AV-Check.exe (salida hash:size:nombre) y la herramienta strings para listar las cadenas legibles del binario, obteniendo la flag.

1. f4a974b0cf25dca7fbce8701b7ab3a88:6144:AV-Check.exe
2. THM{Y0uC4nC-5tr16s}

### Task 6: Otras técnicas de detección / Other Detection Techniques
**Explicación:** Se aprende la detección dinámica, que analiza el malware dentro de entornos virtuales (sandboxing) observando su comportamiento.

Dynamic Detection

### Task 7: Análisis estático / Static Analysis
**Explicación:** Pasos de análisis estático sobre la muestra: intro práctica con varias comprobaciones.

1. No answer needed
2. No answer needed

### Task 8: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2.1 | ¿Qué significa AV? | `Antivirus` |
| 2.2 | ¿Qué vendor de antivirus implementó el primer software AV del mercado? | `McAfee` |
| 2.3 | El software antivirus es una solución de seguridad basada en ____ | `Host` |
| 3.1 | ¿Qué característica del AV analiza malware en un entorno seguro y aislado? | `Emulator` |
| 3.2 | Característica que restaura o desencripta los ficheros ejecutables comprimidos | `unpacker` |
| 3.3 | Pregunta sin respuesta / práctica | `No answer needed` |
| 4 | Repaso de la detección estática | `No answer needed` |
| 5.1 | Salida de sigtool para generar el MD5 de AV-Check.exe | `f4a974b0cf25dca7fbce8701b7ab3a88:6144:AV-Check.exe` |
| 5.2 | Flag obtenida con strings sobre el binario AV-Check | `THM{Y0uC4nC-5tr16s}` |
| 6 | Método de detección usado para analizar malware dentro de entornos virtuales | `Dynamic Detection` |
| 7.1 | Paso de análisis estático | `No answer needed` |
| 7.2 | Paso de análisis estático | `No answer needed` |
| 8 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Estudio conceptual del antivirus y su historia, análisis de las características de detección (emulador y unpacker), generación de firmas con sigtool (MD5 de la muestra AV-Check.exe), extracción de cadenas legibles con strings para obtener la flag, y repaso de la detección dinámica en entornos virtuales y del análisis estático de la muestra.

### Cadena de ataque / Attack Chain

Antivirus (host) -> firma -> emulador/unpacker -> sigtool (MD5 de la muestra) -> strings -> flag -> detección dinámica (sandbox) -> análisis estático

**Learning chain:** antivirus -> AV history -> host-based security -> emulator -> unpacker -> static detection -> sigtool -> strings -> dynamic detection

**Lección:** *Los antivirus combinán detección por firmas con emulación y desempaquetado para vencer la ofuscación, pero la detección dinámica es imprescindible frente a malware que solo se revela en ejecución.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information) / T1055 (Process Injection).

**Fuente:** [TryHackMe - Introduction to Antivirus](https://tryhackme.com/room/introductiontoantivirus)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.