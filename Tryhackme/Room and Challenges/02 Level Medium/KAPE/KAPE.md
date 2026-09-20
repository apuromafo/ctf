# KAPE

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Forensics DFIR | kape | https://tryhackme.com/room/kape | 02 Level Medium | TryHackMe | KAPE, gkape, Targets/Modules, Registro, Línea de tiempo | Automatización de adquisición y parseo de evidencias forenses con KAPE |

---

**Contexto:** La sala **KAPE** enseña a usar **Kroll Artifact Parser Extractor** para automatizar la colección y el procesamiento de artefactos forenses en Windows. Se tratan los ficheros de configuración `.tkape` (targets compuestos) y `.mkape` (módulos), la aplicación gráfica **gkape.exe**, las variables de ruta de salida (`%d`, `%m`), las opciones de línea de comandos (`debug`, `tlist`) y el análisis práctico de un registro de ejecución (Run/RunOnce de `HKCU`) para reconstruir una línea de tiempo de ejecución de programas en la máquina analizada.

## Solucionario

### Task 1: Preparación
**Explicación:**

Se descarga y prepara KAPE en el entorno de análisis. No requiere respuesta escrita.

Respuesta: `No answer needed`

### Task 2: Aplicación gráfica
**Explicación:**

KAPE se compone de utilidades de línea de comandos (`kape.exe`) y de una interfaz gráfica llamada **gkape**. Se identifica el ejecutable que lanza la GUI.

Respuesta: `gkape.exe`

### Task 3: Targets y tipos de objetivo
**Explicación:**

Los ficheros de definición de objetivos (targets) de KAPE usan la extensión `.tkape`. Dentro de `gkape` se distingue el tipo de objetivo ***Compound Targets***, que agrupa varios targets en uno solo.

1. `.tkape`
2. `Compound Targets`

Respuesta:

1. `.tkape`
2. `Compound Targets`

### Task 4: Módulos y estructura
**Explicación:**

Los módulos de procesamiento usan la extensión `.mkape`. El directorio `bin` contiene los binarios/herramientas auxiliares que los módulos invocan durante el parseo.

1. `.mkape`
2. `bin`

Respuesta:

1. `.mkape`
2. `bin`

### Task 5: Targets y módulos de ejemplo
**Explicación:**

Se reconocen targets y módulos típicos: `KapeTriage` como target compuesto que recoge los artefactos principales y `!EZParser` como módulo que invoca Eric Zimmerman Tools. Las variables de salida emplean `%d` (destino/drive) y `%m` (ruta del módulo).

1. `KapeTriage`
2. `!EZParser`
3. `%d`
4. `%m`

Respuesta:

1. `KapeTriage`
2. `!EZParser`
3. `%d`
4. `%m`

### Task 6: Opciones de línea de comandos
**Explicación:**

Las opciones avanzadas de ejecución controlan el destino (`%d`), la ruta del módulo (`%m`), el modo depuración de logs (`debug`), la lista de targets a ejecutar (`tlist`) y otras banderas como `cu` empleadas por la herramienta.

1. `%d`
2. `%m`
3. `debug`
4. `tlist`
5. `cu`

Respuesta:

1. `%d`
2. `%m`
3. `debug`
4. `tlist`
5. `cu`

### Task 7: Análisis forense práctico
**Explicación:**

Con los artefactos recopilados por KAPE se analiza la persistencia del usuario vía `HKCU\...\Run`. Se obtiene el GUID de la clave de ejecución, la ruta del binario (`Z:\Setups`), la marca de tiempo de creación (`11/25/2021 03:33`), el nombre del script de arranque (`RunWallpaperSetup.cmd`), la marca de tiempo de la última modificación y la unidad origen (`E:`).

1. `1C6F654E59A3B0C179D366AE`
2. `Z:\Setups`
3. `11/25/2021 03:33`
4. `RunWallpaperSetup.cmd`
5. `11/30/2021 15:44`
6. `E:`

Respuesta:

1. `1C6F654E59A3B0C179D366AE`
2. `Z:\Setups`
3. `11/25/2021 03:33`
4. `RunWallpaperSetup.cmd`
5. `11/30/2021 15:44`
6. `E:`

### Task 8: Conclusión
**Explicación:**

Se resume el flujo completo de adquisición y parseo con KAPE. No requiere respuesta escrita.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1: Preparación | `No answer needed` |
| 2 | Task 2: Aplicación gráfica de KAPE | `gkape.exe` |
| 3 | Task 3: Extensión de los ficheros de targets | `.tkape` |
| 3 | Task 3: Tipo de target que agrupa varios | `Compound Targets` |
| 4 | Task 4: Extensión de los módulos | `.mkape` |
| 4 | Task 4: Directorio de binarios auxiliares | `bin` |
| 5 | Task 5: Target de recopilación principal | `KapeTriage` |
| 5 | Task 5: Módulo parser de Eric Zimmerman | `!EZParser` |
| 5 | Task 5: Variable de salida | `%d` |
| 5 | Task 5: Variable de módulo | `%m` |
| 6 | Task 6: Variable de destino | `%d` |
| 6 | Task 6: Variable de módulo | `%m` |
| 6 | Task 6: Modo de depuración | `debug` |
| 6 | Task 6: Lista de targets | `tlist` |
| 6 | Task 6: Bandeja adicional | `cu` |
| 7 | Task 7: GUID de la clave Run | `1C6F654E59A3B0C179D366AE` |
| 7 | Task 7: Ruta del binario | `Z:\Setups` |
| 7 | Task 7: Marca de tiempo de creación | `11/25/2021 03:33` |
| 7 | Task 7: Script de arranque | `RunWallpaperSetup.cmd` |
| 7 | Task 7: Marca de tiempo de modificación | `11/30/2021 15:44` |
| 7 | Task 7: Unidad de origen | `E:` |
| 8 | Task 8: Conclusión | `No answer needed` |

---

**Metodología:** Planificación de la adquisición (targets `.tkape`) → ejecución con gkape/kape → procesamiento con módulos (`.mkape`) → revisión de logs y líneas de tiempo → análisis de artefactos de persistencia (Run de `HKCU`) → reconstrucción de la actividad del sistema.

**Learning chain:** Colección → parseo → targets/módulos → macros de ruta → artefactos Run → línea de tiempo.

**Lección:** *KAPE escanea y procesa artefactos de forma masiva en minutos; saber definir targets y leer las variables de salida es clave para no perder evidencia ni contexto temporal.*

**MITRE ATT&CK:** T1005 Data from Local System · T1547.001 Boot/Logon Autostart Execution: Registry Run Keys / Startup Folder · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - KAPE](https://tryhackme.com/room/kape)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.