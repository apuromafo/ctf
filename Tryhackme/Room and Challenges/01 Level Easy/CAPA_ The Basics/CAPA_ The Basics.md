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

**Explicación:** Presentación de CAPA, el analizador de capacidades de Mandiant (FireEye) para malware: identifica comportamientos ("capabilities") en binarios a partir de reglas. Solo lectura de la introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Descripción general de la herramienta

**Explicación:** Uso básico de CAPA: `-h` muestra la ayuda; `-v` (verboso) lista las reglas que coinciden; `-vv` añade la descripción de cada regla. En PowerShell, el ejemplo descarga/lee el archivo de muestra con `Get-Content`.

```bash
capa -h
capa -v muestra.exe
capa -vv muestra.exe
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción se usa para mostrar la ayuda de CAPA? | `-h` |
| 2 | ¿Qué bandera muestra los nombres de las reglas que coinciden (verboso)? | `-v` |
| 3 | ¿Qué bandera muestra también la descripción de las reglas? | `-vv` |
| 4 | ¿Qué comando de PowerShell se usa en el ejemplo para obtener el archivo de muestra? | `Get-Content` |

### Task 3: Resultados de CAPA - Información general, MITRE y MAEC

**Explicación:** Análisis de la salida de CAPA sobre la muestra. Su SHA256 es `ae7bc6...`; CAPA encuentra ofuscamiento de datos (`T1027`) y de cadenas (`T1027.005`), funciones de lanzamiento (`launcher`) y comportamiento de descarga (MAEC: `Downloader`).

```bash
Get-FileHash muestra.exe
capa muestra.exe
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el SHA256 de la muestra analizada con CAPA? | `ae7bc6b6f6ecb206a7b957e4bb86e0d11845c5b2d9f7a00a482bef63b567ce4c` |
| 2 | ¿Qué técnica de MITRE ATT&CK identifica el ofuscamiento de datos (id principal)? | `T1027` |
| 3 | ¿Qué sub-técnica de MITRE se usa para el ofuscamiento de cadenas? | `T1027.005` |
| 4 | ¿Qué capability (nombre) se reporta para la función de lanzamiento? | `launcher` |
| 5 | ¿Qué capability de tipo Downloader se identifica con MAEC? | `Downloader` |

### Task 4: Resultados de CAPA - Catálogo de Comportamientos de Malware (MBC)

**Explicación:** CAPA mapea capabilities al MBC (`Malware Behavior Catalogue`, de MITRE): los comportamientos se organizan por `Objective`; `C0017` es el micro-comportamiento "Create Process". La muestra incluye detección de `Virtual Machine Detection`, codificación (`Encode Data`) y comunicaciones (`HTTP Communication`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la base de datos de comportamientos que usa CAPA (MBC)? | `Malware Behavior Catalogue` |
| 2 | ¿Qué categoría/pilar organiza los comportamientos del catálogo? | `Objective` |
| 3 | ¿Cuál es el identificador del micro-comportamiento 'Create Process'? | `C0017` |
| 4 | ¿Qué behavior detecta que la muestra comprueba si corre en una máquina virtual? | `Virtual Machine Detection` |
| 5 | ¿Qué micro-behavior se asocia a la codificación de datos? | `Encode Data` |
| 6 | ¿Qué micro-behavior identifica las comunicaciones HTTP? | `HTTP Communication` |

### Task 5: Resultados de CAPA - Namespaces

**Explicación:** Cada regla de CAPA pertenece a un namespace: `anti-analysis` y `anti-vm/vm-detection` (detección/evasión de VM), `persistence` (persistencia), `obfuscation` (ofuscamiento). Las reglas aún incompletas se guardan en `Nursery`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer namespace de la regla analizada? | `anti-analysis` |
| 2 | ¿Cuál es el segundo namespace de la regla? | `anti-vm/vm-detection` |
| 3 | ¿Qué namespace corresponde a la persistencia? | `persistence` |
| 4 | ¿Qué namespace corresponde al ofuscamiento? | `obfuscation` |
| 5 | ¿Cómo se llama la categoría/sandbox donde se guardan las reglas incompletas? | `Nursery` |
| 6 | Continúa con el desglose de namespaces. | `No answer needed` |

### Task 6: Más información, más diversión (análisis de reglas)

**Explicación:** Se disecciona una regla: `check-http-status-code.yml` valida códigos de estado HTTP; la detección de cadenas anti-VM referenciada es `reference anti-VM strings`; la carga de código en memoria es la capability `load-code`; y la regla inspecciona la API `RegOpenKeyEx` del registro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la regla que comprueba el código de estado HTTP? | `check-http-status-code.yml` |
| 2 | ¿De qué regla se referencia la detección de cadenas anti-VM? | `reference anti-VM strings` |
| 3 | ¿Qué capability se identifica con la carga de código en memoria? | `load-code` |
| 4 | ¿Qué llamada al registro clave inspecciona la regla (RegOpenKeyEx)? | `RegOpenKeyEx` |

### Task 7: Exploración de recursos web

**Explicación:** Pinzón de CAPA: `-j` genera el reporte en JSON; la herramienta web de Mandiant para explorar resultados es `CAPA Web Explorer`; su `Global Search Box` permite buscar reglas por nombre.

```bash
capa -j muestra.exe -o reporte.json
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué bandera genera el reporte en formato JSON? | `-j` |
| 2 | ¿Cómo se llama la herramienta web de Mandiant para explorar resultados de CAPA? | `CAPA Web Explorer` |
| 3 | ¿Qué elemento de la web permite buscar reglas por nombre? | `Global Search Box` |

### Task 8: Conclusión

**Explicación:** Fin de la sala; con las bases de CAPA, MITRE y MBC claras, se completa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completa la sala. | `No answer needed` |

---

**Metodología:** Se descarga una muestra y se ejecuta CAPA con distintos niveles de salida (-v/-vv) para ver las capabilities y sus técnicas asociadas. Los resultados se cruzan con MITRE ATT&CK (T1027, T1027.005) y con el MBC para clasificar behaviors. Después se disecciona la estructura interna de una regla (namespaces, referencias, APIs) y se usa CAPA Web Explorer para buscar la capability de descarga de código.

**Learning chain:** instalación y flags de CAPA → resultados generales y MITRE → MAEC/MBC → namespaces → anatomía de reglas → búsqueda en CAPA Web Explorer.

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1027.005 (Indicator Removal from Tools), T1105 (Ingress Tool Transfer), T1497 (Virtualization/Sandbox Evasion)

**Fuente:** [TryHackMe - CAPA: The Basics](https://tryhackme.com/room/capabasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
