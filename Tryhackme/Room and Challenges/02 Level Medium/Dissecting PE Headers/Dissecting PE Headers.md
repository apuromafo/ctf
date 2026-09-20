# Dissecting PE Headers

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `dissectingpeheaders` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dissectingpeheaders) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Python / pefile / Cabeceras PE / análisis estático de malware / packing |
| **Impacto** | Análisis estático de un binario PE malicioso con pefile: cabeceras DOS/NT, secciones, imports y detección de packing |

---

**Contexto:** La sala enseña a diseccionar un binario PE (Portable Executable) malicioso mediante análisis estático con Python y la librería pefile. Se recorren los campos del DOS header y del IMAGE_NT_HEADERS (machine, timestamp y optional header), se interpreta el magic y el subsystem, se cuentan las secciones con sus características y se listan las DLL importadas. El objetivo final es identificar la técnica de empaquetado de la muestra y extraer la flag.

## Solucionario

### Task 1: Introducción y despliegue

**Explicación:** Tarea de presentación y arranque del entorno de prácticas de la sala. No requiere ninguna respuesta: basta con desplegar la máquina y abrir la terminal de trabajo para empezar con la disección de la muestra.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Presentación y despliegue del entorno | `No answer needed` |

### Task 2: Empaquetado de la muestra

**Explicación:** Se determina cómo está empaquetado el binario analizado: la técnica de packing identificada es `STRUCT`. Detectar el packer es el primer paso del análisis estático, porque condiciona cómo se verán las cabeceras y los imports una vez la muestra se desempaquete en memoria.

1. STRUCT

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué técnica de packing se identifica en la muestra? | `STRUCT` |

### Task 3: DOS header y NT headers

**Explicación:** Con pefile se leen las primeras cabeceras del binario. El campo `Machine` indica que es un binario de **64** bits; el nombre asociado al diseño original del formato PE es **Mark Zbikowski**; el campo del DOS header que señala dónde empieza el IMAGE_NT_HEADERS es **e_lfanew**; y el tamaño del optional header reportado es **0x000000f8**.

1. 64
2. Mark Zbikowski
3. e_lfanew
4. 0x000000f8

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos bits de arquitectura reporta el binario? | `64` |
| 2 | ¿Quién aparece asociado al origen del formato PE? | `Mark Zbikowski` |
| 3 | ¿Qué campo del DOS header apunta al PE header? | `e_lfanew` |
| 4 | ¿Qué tamaño de optional header se reporta? | `0x000000f8` |

### Task 4: Machine y TimeDateStamp

**Explicación:** Interpretando el magic del optional header, la muestra se clasifica como **32-bit machine**, y el campo TimeDateStamp **0x62289d45** corresponde a la fecha **Wed Mar  9 12:27:49 2022 UTC**. Ambos valores ayudan a datar la muestra y a elegir el toolset adecuado.

1. 32-bit machine
2. 0x62289d45 Wed Mar  9 12:27:49 2022 UTC

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo clasifica el binario el magic del optional header? | `32-bit machine` |
| 2 | ¿Qué valor y fecha reporta el TimeDateStamp? | `0x62289d45 Wed Mar  9 12:27:49 2022 UTC` |

### Task 5: Optional header y subsystem

**Explicación:** Se inspecciona el optional header: el campo **Magic** indica el formato en uso; su valor es **0x020B**; y el **Subsystem** reportado, **0x0003**, corresponde a **WINDOWS_CUI**. Estos campos confirman el tipo de aplicativo (consola de Windows) y la variante del formato PE.

1. Magic
2. 0x020B
3. 0x0003 WINDOWS_CUI

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué campo del optional header distingue la variante del PE? | `Magic` |
| 2 | ¿Qué valor tiene el campo Magic? | `0x020B` |
| 3 | ¿Qué subsystem reporta la muestra? | `0x0003 WINDOWS_CUI` |

### Task 6: Secciones y características

**Explicación:** El binario cuenta con **7** secciones, y la sección examinada presenta las características **0xe0000040**, que se desglosan como **INITIALIZED_DATA** | **EXECUTE** | **READ** | **WRITE**: un conjunto de permisos propio de una sección con datos inicializados y código ejecutable.

1. 7
2. 0xe0000040 INITIALIZED_DATA | EXECUTE | READ | WRITE

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántas secciones tiene el binario? | `7` |
| 2 | ¿Qué características tiene la sección revisada? | `0xe0000040 INITIALIZED_DATA \| EXECUTE \| READ \| WRITE` |

### Task 7: Imports

**Explicación:** Se listan las librerías importadas por la muestra: la primera DLL importada es **User32.dll**, típica en muestras que interactúan con la interfaz de Windows (ventanas, mensajes, hooks).

1. User32.dll

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la DLL importada que se reporta? | `User32.dll` |

### Task 8: Flag

**Explicación:** Con toda la información estática recopilada se obtiene la flag final de la sala: **zmsuz3pinwl**.

1. zmsuz3pinwl

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la sala? | `zmsuz3pinwl` |

### Task 9: Cierre

**Explicación:** Tarea de cierre y repaso de lo aprendido sobre disección de cabeceras PE. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala | `No answer needed` |

---

**Metodología:**

1. Cargar la muestra en un script Python con pefile y abrir el PE completo.
2. Revisar la técnica de empaquetado (packing) de la muestra.
3. Parsear el DOS header (e_lfanew, origen del formato) y el IMAGE_NT_HEADERS (arquitectura 64, TimeDateStamp, tamaño de optional header).
4. Interpretar el magic (0x020B) y el subsystem para clasificar el tipo de aplicación.
5. Contar las secciones y revisar sus características.
6. Listar los imports y localizar la DLL reportada (User32.dll) y la flag.

**Learning chain:** Muestra PE -> pefile/Python -> packing (STRUCT) -> DOS header (e_lfanew, Mark Zbikowski) -> NT headers (64 bits, timestamps) -> Optional header (Magic 0x020B) -> Subsystem WINDOWS_CUI -> Secciones (7) -> Características 0xe0000040 -> Imports (User32.dll) -> Flag

**Lección:** *La disección estática de cabeceras PE con pefile permite caracterizar un binario (arquitectura, secciones, imports y packing) sin necesidad de ejecutarlo.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1027.002 (Software Packing)

**Fuente:** [TryHackMe - Dissecting PE Headers](https://tryhackme.com/room/dissectingpeheaders)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.