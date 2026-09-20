# Threat Hunting With YARA
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Threat Hunting | threathuntingwithyara | https://tryhackme.com/room/threathuntingwithyara | 02 Level Medium | TryHackMe | YARA, threat hunting, IOCs y TTPs, detección de malware, strings y condiciones, XOR | Uso de YARA como herramienta de caza de amenazas para detectar indicadores de compromiso en el sistema de archivos |

> **Objeto:** Aprender a utilizar YARA para la caza de amenazas (threat hunting) y la detección de indicadores de compromiso.

---
**Contexto:** **Threat Hunting With YARA** es una sala guiada de dificultad Media centrada en el uso de **YARA** para la caza de amenazas. Se parte de un escenario realista (una regla de detección de un dropper de ROOTSAW y la técnica de manipulación de tokens de acceso), se repasan los estilos de threat hunting y el proceso de investigación, y se profundiza en la sintaxis de YARA (secciones, strings, modificadores y condiciones). La parte práctica usa YARA sobre un conjunto de archivos para localizar la flag y distintos artefactos (nombres de fichero, claves XOR y cadenas cifradas).
> **ES:** Esta sala se centra en el uso de YARA para la caza de amenazas.
> **EN:** This room focuses on using YARA for threat hunting.

## Solucionario
### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos de threat hunting con YARA; se pide confirmar que se está listo para cazar malware.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Are you ready to hunt for malware? | `No answer needed` |

### Task 2: Descripción del escenario / Scenario Description
**Explicación:** Se presenta un escenario con una regla de detección (`M_APT_Dropper_Rootsaw_Obfuscated`) y la técnica MITRE **T1134**. La regla busca detectar payloads de ROOTSAW ofuscados.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What technique does ID T1134 describe? | `Access Token Manipulation` |
| What does the detection rule *M_APT_Dropper_Rootsaw_Obfuscated* detect? | `Detects obfuscated ROOTSAW payloads` |

### Task 3: Oportunidades para el threat hunting / Opportunities for Threat Hunting
**Explicación:** Se diferencian los estilos de threat hunting. El **structured hunting** es proactivo y usa indicadores de ataque (IOA) y TTPs; el **unstructured hunting** parte de indicadores de compromiso (IOC). Las herramientas como YARA o Volatility se emplean en la fase de **Investigación** del proceso de hunting.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Which threat hunting style is proactive and uses indicators of attack and TTPs? | `structured hunting` |
| In which phase of the threat hunting process, tools like YARA or Volatility are used? | `Investigation` |
| You have received a threat intelligence report consisting only of Indicators of Compromise. What threat hunting style do you recommend to use? | `unstructured hunting` |

### Task 4: YARA: introducción / YARA: Introduction
**Explicación:** Introducción a la estructura de una regla YARA. Además del nombre de la regla, toda regla necesita la sección **condition**, que determina cuándo coincide.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Apart from the rule name, which other section is also required in a YARA rule? | `condition` |

### Task 5: YARA: strings y condiciones / YARA: Strings and Conditions
**Explicación:** Se estudian los modificadores de strings y las condiciones. El modificador **wide** sirve para buscar caracteres codificados en 2 bytes; la condición **none of them** coincide solo cuando no está presente ninguna de las cadenas definidas.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What modifier should be used if you want to search for 2-byte encoded characters? | `wide` |
| Which condition matches only when none of the defined strings are present? | `none of them` |

### Task 6: Entorno y configuración / Environment and Setup
**Explicación:** Se inicia la máquina virtual del laboratorio para poder ejecutar las reglas YARA.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Start the VM and continue to the next task. | `No answer needed` |

### Task 7: YARA: cómo usar reglas YARA para cazar IOC / YARA: How To Use YARA Rules To Hunt for Indicators of Compromise
**Explicación:** Uso de la herramienta YARA desde línea de comandos. Para escanear directorios de forma recursiva se emplea la opción `-r`.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What option do you need to pass to ensure you scan all directories recursively? | `-r` |

### Task 8: Indicadores de compromiso detectados: ¿y ahora qué? / Indicators of Compromise Detected - Now What
**Explicación:** Se introduce el marco DAIR para estructurar la respuesta tras detectar indicadores de compromiso.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What does DAIR stand for? | `Dynamic Approach to Incident Response` |

### Task 9: YARA: ejercicio práctico / YARA: Hands-on Exercise
**Explicación:** Ejercicio práctico ejecutando reglas YARA sobre un conjunto de archivos. El ejercicio 1 devuelve una flag; el 2 y el 3 exigen localizar los nombres de fichero (probando strings anchos y modificadores); el 4 requiere identificar la clave XOR empleada y la cadena cifrada resultante.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the flag found in exercise 1? | `THM{Threathuntingisawesome}` |
| What is the filename found in exercise 2? (Format: filename.extension) | `file10.txt` |
| What is the filename found in exercise 3? (Format: filename.extension) | `file13.txt` |
| What was the XOR key used for encryption in exercise 4? | `0x01` |
| What encrypted string did you find in exercise 4? | `UILzGntoeRnlduihofIheedo\|` |

### Task 10: Conclusión / Conclusion
**Explicación:** Cierre de la sala y transición al siguiente reto.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Are you ready for your next challenge? | `No answer needed` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are you ready to hunt for malware? | `No answer needed` |
| 2.1 | What technique does ID T1134 describe? | `Access Token Manipulation` |
| 2.2 | What does the detection rule M_APT_Dropper_Rootsaw_Obfuscated detect? | `Detects obfuscated ROOTSAW payloads` |
| 3.1 | Which threat hunting style is proactive and uses indicators of attack and TTPs? | `structured hunting` |
| 3.2 | In which phase of the threat hunting process, tools like YARA or Volatility are used? | `Investigation` |
| 3.3 | Which threat hunting style for a report with only IOCs? | `unstructured hunting` |
| 4 | Apart from the rule name, which other section is also required in a YARA rule? | `condition` |
| 5.1 | What modifier should be used to search for 2-byte encoded characters? | `wide` |
| 5.2 | Which condition matches only when none of the defined strings are present? | `none of them` |
| 6 | Start the VM and continue to the next task. | `No answer needed` |
| 7 | What option do you need to pass to ensure you scan all directories recursively? | `-r` |
| 8 | What does DAIR stand for? | `Dynamic Approach to Incident Response` |
| 9.1 | What is the flag found in exercise 1? | `THM{Threathuntingisawesome}` |
| 9.2 | What is the filename found in exercise 2? | `file10.txt` |
| 9.3 | What is the filename found in exercise 3? | `file13.txt` |
| 9.4 | What was the XOR key used for encryption in exercise 4? | `0x01` |
| 9.5 | What encrypted string did you find in exercise 4? | `UILzGntoeRnlduihofIheedo\|` |
| 10 | Are you ready for your next challenge? | `No answer needed` |

---
**Metodología:** Introducción → escenario (T1134 / regla ROOTSAW) → estilos de hunting (structured vs unstructured) → sintaxis YARA (secciones, strings, condiciones) → configuración del entorno → uso de YARA (`-r`) → DAIR → ejercicio práctico → conclusión.

### Cadena de ataque / Attack Chain
```
Introducción -> Escenario (T1134 Access Token Manipulation / regla ROOTSAW)
-> Estilos de hunting (structured / unstructured, Investigación)
-> YARA: condición -> strings y modificadores (wide, none of them)
-> Setup VM -> yara -r -> DAIR -> Hands-on: THM{Threathuntingisawesome},
   file10.txt, file13.txt, XOR key 0x01, cadena cifrada -> Conclusión
```
**Learning chain:** Contexto → estilos de hunting → sintaxis YARA → ejecución → detección de IOC → respuesta (DAIR).
**Lección:** *YARA convierte strings y condiciones en reglas reutilizables de caza; elegir bien el estilo de hunting (structured frente a unstructured) depende de si se dispone de TTPs o solo de IOCs.*
**MITRE ATT&CK:** T1134 (Access Token Manipulation) — técnica referenciada en el escenario; las reglas YARA permiten detectar droppers e implantes como ROOTSAW.
**Fuente:** [TryHackMe - Threat Hunting With YARA](https://tryhackme.com/room/threathuntingwithyara)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
