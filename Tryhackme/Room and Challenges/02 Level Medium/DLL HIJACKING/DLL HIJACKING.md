# DLL HIJACKING

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `dllhijacking` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dllhijacking) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Windows / DLL Hijacking / ProcMon / Process Explorer / C++ / payload DLL |
| **Impacto** | Detección y explotación de un DLL hijacking sobre un proceso Windows vulnerable para ejecutar una DLL maliciosa y acceder a las credenciales objetivo |

---

**Contexto:** La sala es un laboratorio guiado sobre DLL hijacking en Windows. Se explican los conceptos de DLL y de secuestro de carga (DLL search order hijacking / sideloading) y se usa ProcMon para capturar qué librerías carga un proceso vulnerable y desde qué rutas. Generando una DLL maliciosa que se coloca donde el proceso la busca, se logra ejecutar código en el contexto de ese proceso y se avanza hasta obtener las credenciales finales.

## Solucionario

### Task 1: Introducción al DLL Hijacking

**Explicación:** Tarea introductoria que define qué es una DLL, cómo funciona la resolución de dependencias en Windows y en qué consiste el DLL hijacking (secuestro del flujo de carga de una librería). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción conceptual al DLL hijacking | `No answer needed` |
| 2 | Conceptos de DLL y carga de librerías | `No answer needed` |

### Task 2: Preparación del entorno

**Explicación:** Se explican los requisitos del laboratorio (máquina Windows desplegada, herramientas de captura y proceso objetivo). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación y despliegue del entorno | `No answer needed` |

### Task 3: Captura de actividad de DLLs

**Explicación:** Se introduce ProcMon y cómo filtrar las operaciones para observar las DLLs que carga el proceso objetivo y los directorios desde los que se resuelven. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Captura de actividad de DLLs con ProcMon | `No answer needed` |

### Task 4: Identificación de la DLL candidata

**Explicación:** Con la captura realizada se identifican las librerías que el proceso busca en rutas controlables por el usuario (no presentes en el sistema), que son las candidatas al hijack. En este punto aún no hay respuestas que introducir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identificación de la librería candidata al hijack | `No answer needed` |
| 2 | Revisión de rutas de carga | `No answer needed` |

### Task 5: Generación de la DLL maliciosa

**Explicación:** Se explica cómo compilar una DLL de sustitución que, al cargarse, ejecute código (por ejemplo abriendo un proceso hijo o una reverse connection). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Generación de la DLL maliciosa | `No answer needed` |

### Task 6: Proceso objetivo

**Explicación:** El proceso que se aprovecha como vector de carga de la DLL maliciosa es **explorer**: al lanzarse con la DLL suplantada en su ruta de búsqueda, la librería maliciosa se ejecuta en su contexto.

1. explorer

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso se aprovecha para el hijack? | `explorer` |

### Task 7: Versión de Windows

**Explicación:** El entorno objetivo corre sobre Windows 10 **1903**, versión sobre la que se validó el comportamiento de carga de la DLL vulnerada.

1. 1903

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión de Windows 10 se usa como objetivo? | `1903` |

### Task 8: Despliegue de la DLL

**Explicación:** Se detalla cómo colocar la DLL maliciosa en la ubicación indicada y forzar la ejecución del proceso objetivo para que la cargue. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Colocación de la DLL y disparo del proceso | `No answer needed` |

### Task 9: Librería secuestrada

**Explicación:** La DLL concreta que se sustituye para el hijack es **ualapi.dll**: el proceso vulnerable la busca en un directorio que el atacante puede escribir, por lo que al colocarla ahí la carga con su contenido malicioso.

1. ualapi.dll

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué DLL se secuestra para el hijack? | `ualapi.dll` |

### Task 10: Usuario objetivo

**Explicación:** La DLL maliciosa expone las credenciales bajo las que corre el proceso objetivo. El usuario identificado en el laboratorio es **John**.

1. John

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuario se obtiene/identifica en el laboratorio? | `John` |

### Task 11: Contraseña

**Explicación:** Junto al usuario se recupera la contraseña que la carga maliciosa revela: **1q2w3e!Q@W#E1q2w3e**.

1. 1q2w3e!Q@W#E1q2w3e

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué contraseña se obtiene en el laboratorio? | `1q2w3e!Q@W#E1q2w3e` |

### Task 12: Cierre

**Explicación:** Tarea final de repaso y conclusiones del laboratorio de DLL hijacking. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala | `No answer needed` |

---

**Metodología:**

1. Comprender cómo resuelve Windows la carga de DLLs (búsqueda en el directorio del ejecutable, system32, PATH).
2. Capturar con ProcMon la actividad de carga del proceso objetivo y detectar accesos fallidos a librerías en rutas controlables.
3. Seleccionar como candidata una DLL que el proceso busque en un directorio escribible (ualapi.dll).
4. Compilar una DLL maliciosa que ejecute el comando/shell deseado e incluir el payload.
5. Colocar la DLL en la ruta correcta y provocar que el proceso objetivo (explorer) la cargue.
6. Recuperar las credenciales expuestas (John / 1q2w3e!Q@W#E1q2w3e).

**Learning chain:** DLL loading -> Búsqueda de directorios -> ProcMon (accesos fallidos) -> DLL candidata ualapi.dll -> DLL maliciosa -> Proceso explorer -> Ejecución -> Credenciales John -> Cierre

**Lección:** *Si un binario carga una DLL desde un directorio que un atacante puede escribir, es vulnerable a DLL hijacking: ProcMon descubre la librería y una DLL de sustitución otorga ejecución en el contexto del proceso.*

**MITRE ATT&CK:** T1574 (Hijack Execution Flow), T1574.001 (DLL Search Order Hijacking), T1574.002 (DLL Side-Loading)

**Fuente:** [TryHackMe - DLL HIJACKING](https://tryhackme.com/room/dllhijacking)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.