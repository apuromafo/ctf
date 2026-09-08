# CAPA: The Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `capabasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/capabasics) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | CAPA / PowerShell / MITRE ATT&CK / MAEC (MBC) / CAPA Web Explorer |
| **Impacto** | Iniciación a CAPA: identificación de capacidades en muestras de malware mediante reglas, mapeo a MITRE ATT&CK y al Catálogo de Comportamientos de Malware. |

---

**Contexto:** Sala teórico-práctica para aprender a usar CAPA, la herramienta de FireEye/Mandiant que identifica capacidades en archivos ejecutables. Se analiza una muestra real, se interpretan los resultados (información general, técnicas MITRE T1027/T1027.005, nubes/namespaces), el Malware Behavior Catalogue (MBC) con sus objectives/behaviors, se profundiza en la estructura de una regla de capacidad y se exploran los recursos web de CAPA para consultar reglas y resultados.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Descripción general de la herramienta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción se usa para mostrar la ayuda de CAPA? | `-h` |
| 2 | ¿Qué bandera muestra los nombres de las reglas que coinciden (verboso)? | `-v` |
| 3 | ¿Qué bandera muestra también la descripción de las reglas? | `-vv` |
| 4 | ¿Qué comando de PowerShell se usa en el ejemplo para obtener el archivo de muestra? | `Get-Content` |

### Task 3: Resultados de CAPA - Información general, MITRE y MAEC

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el SHA256 de la muestra analizada con CAPA? | `ae7bc6b6f6ecb206a7b957e4bb86e0d11845c5b2d9f7a00a482bef63b567ce4c` |
| 2 | ¿Qué técnica de MITRE ATT&CK identifica el ofuscamiento de datos (id principal)? | `T1027` |
| 3 | ¿Qué sub-técnica de MITRE se usa para el ofuscamiento de cadenas? | `T1027.005` |
| 4 | ¿Qué capability (nombre) se reporta para la función de lanzamiento? | `launcher` |
| 5 | ¿Qué capability de tipo Downloader se identifica con MAEC? | `Downloader` |

### Task 4: Resultados de CAPA - Catálogo de Comportamientos de Malware (MBC)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la base de datos de comportamientos que usa CAPA (MBC)? | `Malware Behavior Catalogue` |
| 2 | ¿Qué categoría/pilar organiza los comportamientos del catálogo? | `Objective` |
| 3 | ¿Cuál es el identificador del micro-comportamiento 'Create Process'? | `C0017` |
| 4 | ¿Qué behavior detecta que la muestra comprueba si corre en una máquina virtual? | `Virtual Machine Detection` |
| 5 | ¿Qué micro-behavior se asocia a la codificación de datos? | `Encode Data` |
| 6 | ¿Qué micro-behavior identifica las comunicaciones HTTP? | `HTTP Communication` |

### Task 5: Resultados de CAPA - Namespaces

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer namespace de la regla analizada? | `anti-analysis` |
| 2 | ¿Cuál es el segundo namespace de la regla? | `anti-vm/vm-detection` |
| 3 | ¿Qué namespace corresponde a la persistencia? | `persistence` |
| 4 | ¿Qué namespace corresponde al ofuscamiento? | `obfuscation` |
| 5 | ¿Cómo se llama la categoría/sandbox donde se guardan las reglas incompletas? | `Nursery` |
| 6 | Continúa con el desglose de namespaces. | `No answer needed` |

### Task 6: Más información, más diversión (análisis de reglas)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la regla que comprueba el código de estado HTTP? | `check-http-status-code.yml` |
| 2 | ¿De qué regla se referencia la detección de cadenas anti-VM? | `reference anti-VM strings` |
| 3 | ¿Qué capability se identifica con la carga de código en memoria? | `load-code` |
| 4 | ¿Qué llamada al registro clave inspecciona la regla (RegOpenKeyEx)? | `RegOpenKeyEx` |

### Task 7: Exploración de recursos web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué bandera genera el reporte en formato JSON? | `-j` |
| 2 | ¿Cómo se llama la herramienta web de Mandiant para explorar resultados de CAPA? | `CAPA Web Explorer` |
| 3 | ¿Qué elemento de la web permite buscar reglas por nombre? | `Global Search Box` |

### Task 8: Conclusión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completa la sala. | `No answer needed` |

---

**Metodología:** Se descarga una muestra y se ejecuta CAPA con distintos niveles de salida (-v/-vv) para ver las capabilities y sus técnicas asociadas. Los resultados se cruzan con MITRE ATT&CK (T1027, T1027.005) y con el MBC para clasificar behaviors. Después se disecciona la estructura interna de una regla (namespaces, referencias, APIs) y se usa CAPA Web Explorer para buscar la capability de descarga de código.

**Learning chain:** instalación y flags de CAPA → resultados generales y MITRE → MAEC/MBC → namespaces → anatomía de reglas → búsqueda en CAPA Web Explorer.

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1027.005 (Indicator Removal from Tools), T1105 (Ingress Tool Transfer), T1497 (Virtualization/Sandbox Evasion)

**Fuente:** [TryHackMe - CAPA: The Basics](https://tryhackme.com/room/capabasics)