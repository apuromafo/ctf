# NTFS Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | ntfsanalysis | https://tryhackme.com/room/ntfsanalysis | 02 Level Medium | TryHackMe | NTFS, MFT, $UsnJrnl/$J, atributo $I30, FTK Imager, Timeline Explorer | Aprender a analizar el sistema de archivos NTFS para investigaciones forenses: el MFT, el cambio de journal ($UsnJrnl/$J), los atributos $I30 y la recuperación de evidencias en máquinas Windows. |

---

**Contexto:** La sala **NTFS Analysis** es un laboratorio de forense digital centrado en el sistema de archivos NTFS de Windows. Trabaja sobre un entorno con **FTK Imager** y **Timeline Explorer**, con el objetivo de localizar evidencias: qué proceso se ejecutaba, qué archivos se crearon, movieron o eliminaron, qué rutas eran accesibles y cómo se propagó una muestra maliciosa. Se exploran el **Master File Table (MFT)**, el **USN Journal ($UsnJrnl/$J)** y los atributos **$I30** de indexación de directorios para reconstruir la actividad del sistema y responder a las preguntas del caso.

> **ES:** Laboratorio de forense digital en el que se analiza el sistema de archivos NTFS (MFT, $UsnJrnl/$J y $I30) con FTK Imager para reconstruir la actividad de una máquina Windows comprometida.
> **EN:** A digital forensics lab analysing the NTFS file system (MFT, $UsnJrnl/$J and $I30) with FTK Imager to reconstruct the activity of a compromised Windows machine.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación del caso: el laboratorio es una introducción al análisis forense del sistema de archivos NTFS. Se revisan los fundamentos y conceptos previos necesarios para trabajar con el archivo de imagen del disco en FTK Imager.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Indica que entiendes los objetivos del laboratorio (sin respuesta requerida). | `No answer needed` |

### Task 2: Estructura NTFS y componentes / NTFS Structure and Components
**Explicación:** Se revisan los componentes esenciales de NTFS: el **MFT** (Master File Table) al inicio del volumen, el **$UsnJrnl** (USN Journal) en `$Extend` para registrar los cambios en archivos, el atributo **$I30** para la indexación de directorios, y los atributos **$DATA** y **$STANDARD_INFORMATION**. Se prepara el archivo de imagen en FTK Imager.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Reconoce los componentes de NTFS mencionados en la tarea (sin respuesta requerida). | `No answer needed` |

### Task 3: Journaling y USN Journal / Journaling and USN Journal
**Explicación:** Se examina el cambio de journal de NTFS desde el directorio `$Extend`. La carpeta oculta `$Extend` contiene el archivo del diario de cambios **$UsnJrnl**, y dentro de él, al abrirlo con FTK Imager, se encuentra el archivo **$J**, que almacena los registros reales de cambios del sistema de archivos (lo que permite la generación de la línea de tiempo con Timeline Explorer).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which feature does NTFS use to keep track of the changes within the file system? | `journaling` |
| 2 | Double-click on the $UsnJrnl file in the $Extend folder; what is the first evidence file you find? | `$J` |

### Task 4: Análisis del MFT / MFT Analysis
**Explicación:** Se analiza el Master File Table para reconstruir el estado de los archivos. La columna que indica que un archivo ya **no está presente** en el disco es **In Use**. En el registro MFT se identifica el sniffer de red instalado en `\Program Files\` (**wireshark**), la herramienta anti-forense de `\Downloads\Tools` que borra rastros del atacante (**DiskWipe.exe**, que según el MFT **no** está presente en el disco → **nay**), la ruta padre del archivo `flag.txt` (`.\tmp\secret_directory`) con su contenido (**WelDone_You_F0und_M3**) y el archivo asociado a la entrada MFT **584574** (**SharpHound.ps1**).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which column indicates that the file is no longer present on the disk? / ¿Qué columna indica que el archivo ya no está en el disco? | `In Use` |
| 2 | Examine the MFT record; what is the network sniffer installed on this system in the \Program Files\ directory? / ¿Qué sniffer de red está instalado en \Program Files\? | `wireshark` |
| 3 | An anti-forensics tool responsible for wiping out an attacker's traces was installed in the \Downloads\Tools folder. What is the name of the tool? / ¿Cómo se llama la herramienta anti-forense instalada en \Downloads\Tools? | `DiskWipe.exe` |
| 4 | According to the MFT record, is the anti-forensics tool currently present on the disk? (yay or nay) / ¿Está la herramienta anti-forense presente en el disco? | `nay` |
| 5 | Examining the MFT record, it seems there is a record of a flag.txt file. What is the parent path of the file? / ¿Cuál es la ruta padre de flag.txt? | `.\tmp\secret_directory` |
| 6 | What is the content of the flag.txt file? / ¿Cuál es el contenido de flag.txt? | `WelDone_You_F0und_M3` |
| 7 | What is the file name associated with the MFT entry number "584574"? / ¿Qué nombre de archivo está asociado a la entrada MFT 584574? | `SharpHound.ps1` |

### Task 5: Análisis del USN Journal ($J) / USN Journal ($J) Analysis
**Explicación:** Con Timeline Explorer se carga el USN Journal exportado y se analizan los eventos de la entrada MFT **95071**: el archivo de texto asociado antes de ser renombrado es **New Text Document.txt**, la **primera operación** realizada sobre ese archivo es **FileCreate**, el **número de operaciones de rename** registrado en `$J` contra `secret_code.txt` es **2**, y la fecha de **borrado** de `secret_code.txt` es **2025-01-15 08:10:04**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the text file name associated with entry number 95071 before renaming it? / ¿Qué nombre de texto tenía la entrada 95071 antes de renombrarse? | `New Text Document.txt` |
| 2 | According to the record, what is the first operation performed on the file in the question above? / ¿Cuál fue la primera operación realizada sobre ese archivo? | `FileCreate` |
| 3 | According to the record in $J, what is the count of the rename operation found against secret_code.txt? / ¿Cuántas operaciones de rename hay contra secret_code.txt? | `2` |
| 4 | According to the record, when was the secret_code.txt file deleted? / ¿Cuándo se borró secret_code.txt? | `2025-01-15 08:10:04` |

### Task 6: Análisis del atributo $I30 / $I30 Index Allocation Analysis
**Explicación:** Se analiza el atributo **$I30** (Index Allocation) de indexación de directorios, que permite ver los archivos o carpetas que existieron en un directorio aunque hayan sido eliminados. Se cuentan los ficheros/carpetas **borrados** presentes en el atributo $I30 extraído (**52**) y se identifica la entrada MFT padre del directorio `nmap` (**512386**).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many deleted files or folders are present in the $I30 attribute file that was extracted in this task? / ¿Cuántos archivos o carpetas borrados hay en el $I30 extraído? | `52` |
| 2 | What is the parent MFT entry of the nmap directory? / ¿Cuál es la entrada MFT padre del directorio nmap? | `512386` |

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre del laboratorio: se repasa el uso combinado del MFT, del $UsnJrnl/$J y del atributo $I30 para reconstruir la actividad del sistema de archivos y extraer conclusiones forenses sólidas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa los conceptos forenses de NTFS vistos en la sala (sin respuesta requerida). | `No answer needed` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Introducción al laboratorio. | `No answer needed` |
| 2 | (Task 2) Componentes esenciales de NTFS. | `No answer needed` |
| 3 | (Task 3) Which feature does NTFS use to keep track of the changes within the file system? | `journaling` |
| 4 | (Task 3) First evidence file found in $UsnJrnl. | `$J` |
| 5 | (Task 4) Column that indicates the file is no longer present on the disk. | `In Use` |
| 6 | (Task 4) Network sniffer installed in \Program Files\. | `wireshark` |
| 7 | (Task 4) Anti-forensics tool installed in \Downloads\Tools. | `DiskWipe.exe` |
| 8 | (Task 4) Is the anti-forensics tool present on the disk? (yay or nay) | `nay` |
| 9 | (Task 4) Parent path of flag.txt. | `.\tmp\secret_directory` |
| 10 | (Task 4) Content of the flag.txt file. | `WelDone_You_F0und_M3` |
| 11 | (Task 4) File name associated with MFT entry "584574". | `SharpHound.ps1` |
| 12 | (Task 5) Text file name associated with entry 95071 before renaming. | `New Text Document.txt` |
| 13 | (Task 5) First operation performed on that file. | `FileCreate` |
| 14 | (Task 5) Count of rename operations against secret_code.txt. | `2` |
| 15 | (Task 5) When was secret_code.txt deleted? | `2025-01-15 08:10:04` |
| 16 | (Task 6) How many deleted files/folders are present in the $I30 attribute? | `52` |
| 17 | (Task 6) Parent MFT entry of the nmap directory. | `512386` |
| 18 | (Task 7) Conclusión del laboratorio. | `No answer needed` |

---

**Metodología:** Preparación del archivo de imagen en FTK Imager → localización del MFT y del $UsnJrnl en $Extend → exportación del $J a CSV → análisis del MFT (estado "In Use", procesos y rutas) → correlación con el USN Journal en Timeline Explorer → análisis del atributo $I30 → reconstrucción de la actividad y redacción de conclusiones.

**Learning chain:** estructura NTFS → MFT y atributos → journaling ($UsnJrnl/$J) → timeline de eventos (FileCreate) → indexación $I30 → reconstrucción forense del caso.

**Lección:** *El sistema de archivos NTFS guarda un registro forense valioso: el MFT, el $UsnJrnl y el $I30 permiten reconstruir qué, cuándo y quién operó sobre los archivos incluso después de que se eliminen las pruebas directas.*

**MITRE ATT&CK:** T1005 (Data from Local System) · T1003.001 (OS Credential Dumping: LSASS Memory) · T1074.001 (Data Staged: Local Data Staging) · T1036 (Masquerading) · T1059.001 (Command and Scripting Interpreter: PowerShell).

**Fuente:** [TryHackMe - NTFS Analysis](https://tryhackme.com/room/ntfsanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.