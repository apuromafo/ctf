# Velociraptor

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `velociraptorhp` |
| **Link** | [TryHackMe](https://tryhackme.com/room/velociraptorhp) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Velociraptor / VQL / DFIR / endpoint analysis / artifacts / threat hunting |
| **Impacto** | Usar Velociraptor y consultas VQL para analizar endpoints y detectar artefactos maliciosos (PrintNightmare, etc.) |

---

**Contexto:** Sala de DFIR con Velociraptor: aprender el flujo de despliegue (velociraptor.exe gui), consultas VQL, artefactos de usuarios/redes y detección de amenazas sobre endpoint (p. ej. PrintNightmare).

## Solucionario

### Task 1: (Intro)

**Explicación:**

Introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: (Setup / Deploy)

**Explicación:**

El comando para lanzar la interfaz gráfica de Velociraptor es `velociraptor.exe gui`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (GUI command) | `1. velociraptor.exe gui` |

### Task 3: (Usuarios / Users artifact)

**Explicación:**

Análisis del artefacto de usuarios: el host es `THM-VELOCIRAPTOR.eu-west-1.compute.internal`; el timestamp de último acceso es `2021-04-11T22:11:10Z`; la consulta VQL del artefacto es `LET Generic_Client_Info_Users_0_0=SELECT Name, Description, Mtime AS LastLogin FROM Artifact.Windows.Sys.Users()`; el flujo de salida donde ver el resultado es `Stdout`; y el comando de powershell (decodificado `ZwBlAHQALQBkAGEAdABlAA==` = "get-date") es `powershell -ExecutionPolicy Unrestricted -encodedCommand ZwBlAHQALQBkAGEAdABlAA==`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Host) | `1. THM-VELOCIRAPTOR.eu-west-1.compute.internal` |
| 2 | (Timestamp) | `2. 2021-04-11T22:11:10Z` |
| 3 | (VQL) | `3. LET Generic_Client_Info_Users_0_0=SELECT Name, Description, Mtime AS LastLogin FROM Artifact.Windows.Sys.Users()` |
| 4 | (Output flow) | `4. Stdout` |
| 5 | (Command) | `5. powershell -ExecutionPolicy Unrestricted -encodedCommand ZwBlAHQALQBkAGEAdABlAA==` |

### Task 4: (WSL / Redes)

**Explicación:**

Detección del subsistema: el resultado del artefacto de red muestra `Ubuntu on Windows Subsystem for Linux` y el número de interfaces `19`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (WSL) | `1. Ubuntu on Windows Subsystem for Linux` |
| 2 | (Interfaces) | `2. 19` |

### Task 5: (Vista de Flujos / Flows)

**Explicación:**

En el análisis de archivos y flows: el accessor de archivos es `ntfs accessor`; el accessor de registro es `registry accessor`; el archivo de escritorio (`desktop.ini`) aparece; y la flag de la sala es `THM{VkVMT0NJUkFQVE9S}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (NTFS accessor) | `1. ntfs accessor` |
| 2 | (Registry accessor) | `2. registry accessor` |
| 3 | (Desktop file) | `3. desktop.ini` |
| 4 | (Flag) | `4. THM{VkVMT0NJUkFQVE9S}` |

### Task 6: (VQL UI)

**Explicación:**

El VQL Query Builder de la UI: `Column Selectors` (selector de columnas), `VQL Plugin` (fuente de datos), `Filter expression` (expresión de filtro). El plugin `?` (cuatro preguntas) usa el acceso `execve()`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Column selector) | `1. Column Selectors` |
| 2 | (VQL plugin) | `2. VQL Plugin` |
| 3 | (Filter expression) | `3. Filter expression` |
| 4 | (?) | `4. ?` |
| 5 | (Accessor) | `5. execve()` |

### Task 7: (Artefactos / Filesystem)

**Explicación:**

El plugin que lista directorios es `parse_mft` y el campo que indica si es directorio es `IsDir`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (MFT plugin) | `1. parse_mft` |
| 2 | (IsDir) | `2. IsDir` |

### Task 8: (PrintNightmare)

**Explicación:**

Detección de PrintNightmare: el artefacto es `Windows.Detection.PrintNightmare`; la consulta VQL para detectar el DLL malicioso es `SELECT "C:/" + FullPath AS Full_Path,FileName AS File_Name,parse_pe(file="C:/" + FullPath) AS PE`; el archivo malicioso es `nightmare.dll`; y la ruta del PDB es `C:\Users\caleb\source\repos\nightmare\x64\Release\nightmare.pdb`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Artifact) | `1. Windows.Detection.PrintNightmare` |
| 2 | (VQL) | `2. SELECT "C:/" + FullPath AS Full_Path,FileName AS File_Name,parse_pe(file="C:/" + FullPath) AS PE` |
| 3 | (DLL) | `3. nightmare.dll` |
| 4 | (PDB path) | `4. C:\Users\caleb\source\repos\nightmare\x64\Release\nightmare.pdb` |

### Task 9: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión) | `No answer needed` |

---

**Metodología:**

1. Desplegar Velociraptor con `velociraptor.exe gui` y conectarse al endpoint.
2. Ejecutar artefactos de usuarios (VQL `Artifact.Windows.Sys.Users`) y revisar Stdout/flows.
3. Inspeccionar redes (WSL, interfaces) y flows de archivos (accessors ntfs/registry, `desktop.ini`).
4. Familiarizarse con el VQL Query Builder (Column Selectors, VQL Plugin, Filter expression).
5. Usar artefactos de filesystem (parse_mft, IsDir) y específicos (Windows.Detection.PrintNightmare) para localizar malware (nightmare.dll) y obtener la flag.

**Learning chain:** velociraptor.exe gui -> artifact users VQL -> WSL/interfaces -> flows/accessors -> desktop.ini -> flag THM{VkVMT0NJUkFQVE9S} -> VQL builder -> parse_mft -> PrintNightmare artifact -> nightmare.dll

**Lección:** *Velociraptor centraliza la recolección forense y el hunting en endpoints mediante artefactos VQL; conocer plugins (parse_mft, parse_pe) y accessors (ntfs, registry) permite pivotar de la teoría a la detección concreta de amenazas como PrintNightmare.*

**MITRE ATT&CK:** T1203 (Exploitation for Client Execution) · T1059.001 (PowerShell) · T1082 (System Information Discovery) · CWE-426 (Untrusted Search Path)

**Fuente:** [TryHackMe - Velociraptor](https://tryhackme.com/room/velociraptorhp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
