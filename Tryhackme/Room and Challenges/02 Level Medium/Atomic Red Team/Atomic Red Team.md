# Atomic Red Team
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `atomicredteam` |
| **Link** | [TryHackMe](https://tryhackme.com/room/atomicredteam) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Atomic Red Team (REDMUD, Invoke-AtomicRedTeam), YAML, MITRE ATT&CK Atlas/Navigator, Sysmon, Aurora EDR, PowerShell, GUI, APT37 |
| **Impacto** | Aprende a emular adversarios con Atomic Red Team: entender los YAML (executor, guid, cleanup), ejecutar Atomic Tests, usar Sysmon/EDR para detectar y finalmente emular a APT37 de punta a punta. |
---
**Contexto:** Sala orientada a blue team. Atomic Red Team es una librería de tests simples y modulares mapeados al marco MITRE ATT&CK; se usan para replicar las TTPs de un adversario y así mejorar las detecciones. La sala explica la estructura de los archivos YAML, cómo ejecutar los tests (PowerShell/Interfaz Gráfica) y cierra con un caso de estudio emulando al grupo APT37 (cartografiado con el ATT&CK Navigator y supervisado con Sysmon + Aurora EDR).
## Solucionario
### Task 1: Introduction
**Explicación:** Se presenta Atomic Red Team y el objetivo: entender cómo ejecutan sus TTPs los adversarios reales y qué tan importante es verlas en acción para construir mejores defensas.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Familiarízate con la sala/entorno antes de comenzar. | `No answer needed` |
### Task 2: Understanding Atomic Tests
**Explicación:** Cada Atomic Test se define en un archivo YAML. Campos clave: `executor` (define cómo se ejecuta; si no puede automatizarse se usa **manual**), `auto_generated_guid` (identificador único de cada Atomic, sirve para aislarlo y ejecutarlo individualmente) y `cleanup_command` (comandos que eliminan los archivos de emulación o revierten configuraciones modificadas al terminar el test).
```yaml
executor: name: powershell
auto_generated_guid: expone al
cleanup_command: sanadata
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de executor se usa para acciones que no pueden automatizarse? | `manual` |
| 2 | ¿Cuál es el campo de un archivo Atomic YAML rellenado con un identificador único para aislar un Atomic específico? | `auto_generated_guid` |
| 3 | ¿Cuál es el campo de un archivo Atomic YAML rellenado con comandos para borrar archivos usados para emulación o revertir configuraciones modificadas? | `cleanup_command` |
### Task 3: Executing Atomic Tests
**Explicación:** Con `Invoke-AtomicRedTeam` se ejecutan los tests. Se cuenta cuántos son compatibles con Windows (p. ej. 4 para T1110.001), se nombra un test concreto (T1218.005-2: *"Mshta executes VBScript to execute malicious command"*), se ven los prerequisitos no cumplidos, se ejecuta un test concreto por GUID con el parámetro **TestGuids**, y se identifican los efectos secundarios (tarea programada **spawn** de T1053.005-2 y la clave de registro modificada por T1547.001-2: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend`).
```powershell
Invoke-AtomicTest T1218.005 -TestGuids <guid>
Invoke-AtomicTest T1053.005 -TestGuids <guid> -CheckPrereqs
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos tests atómicos hay bajo Atomic T1110.001 soportados en hosts Windows? | `4` |
| 2 | ¿Cuál es el nombre del segundo test bajo Atomic T1218.005? | `Mshta executes VBScript to execute malicious command` |
| 3 | ¿Cuántos prerequisitos no se cumplen para Atomic T1003? | `4` |
| 4 | ¿Qué parámetro se usa para ejecutar un test atómico concreto mediante GUID? | `TestGuids` |
| 5 | ¿Cuál es el nombre de la tarea programada creada tras ejecutar el 2º test de Atomic T1053.005? | `spawn` |
| 6 | ¿Qué clave de registro se modifica tras ejecutar el 2º test de Atomic T1547.001? | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend` |
### Task 4: APT37 Emulation: The Start
**Explicación:** Primera parte de la emulación de APT37. Usando el **ATT&CK Navigator**, a `admin@338` se le atribuyen **9** técnicas y la técnica de phishing es **T1566.001**. En el laboratorio se responde: cuántos tests de T1083 soportan Windows (**4**), el archivo que debe existir como prerequisito de T1049-4 (**Sharpview.exe**), el string que imprime T1059.003-3 (*"Hello, from CMD!"*), el hostname de la máquina según T1082-6 (**ATOMIC**) y cuántas cuentas están deshabilitadas según T1087.001-9 (**3**).
```powershell
Invoke-AtomicTest T1082 -TestGuids <guid>
Invoke-AtomicTest T1087.001 -TestGuids <guid>
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usando el ATT&CK Navigator, ¿cuántas técnicas se atribuyen a admin@338? | `9` |
| 2 | Según el mapeo del ATT&CK Navigator, ¿cuál es el ID de la técnica de phishing usada por el grupo? | `T1566.001` |
| 3 | ¿Cuántos tests atómicos de T1083 están soportados en hosts Windows? | `4` |
| 4 | ¿Qué archivo debe existir para cumplir el prerequisito del test atómico T1049-4? | `Sharpview.exe` |
| 5 | ¿Cuál es el string que imprime al ejecutar el test atómico T1059.003-3? | `Hello, from CMD!` |
| 6 | ¿Cuál es el hostname de la máquina según el test atómico T1082-6? | `ATOMIC` |
| 7 | ¿Cuántas cuentas están deshabilitadas según el test atómico T1087.001-9? | `3` |
### Task 5: APT37 Emulation: Sysmon & EDR
**Explicación:** Aquí se observan los tests desde la telemetría. Tras ejecutar T1547.001-4 se generan **14** eventos Sysmon (15 menos 1, porque el propio Atomic queda registrado). El archivo creado es `vbsstartup.vbs`. En el evento Registry Value Set de T1547.001-13, el TargetObject es `HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\atomictest`. En **Aurora EDR**, excluyendo la detección WHOAMI, las primeras reglas disparadas por T1547.001-7 y T1547.001-8 son *"PowerShell Writing Startup Shortcuts"* y *"Registry Persistence Mechanisms in Recycle Bin"*.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos eventos Sysmon se generan tras ejecutar el test atómico T1547.001-4? | `14` |
| 2 | Según los mismos eventos de la Q1, ¿cuál es el nombre de archivo creado por el test? | `vbsstartup.vbs` |
| 3 | Según el evento Registry Value Set generado tras ejecutar el test atómico T1547.001-13, ¿cuál es el valor del campo TargetObject? | `HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\atomictest` |
| 4 | Excluyendo la detección WHOAMI, ¿cuál es el título de la primera regla disparada en Aurora EDR tras ejecutar el test atómico T1547.001-7? | `PowerShell Writing Startup Shortcuts` |
| 5 | Excluyendo la detección WHOAMI, ¿cuál es el título de la primera regla disparada en Aurora EDR tras ejecutar el test atómico T1547.001-8? | `Registry Persistence Mechanisms in Recycle Bin` |
### Task 6: Atomic GUI
**Explicación:** Existe una interfaz gráfica para Atomic Red Team. Para personalizar interactivamente los argumentos de entrada se usa el parámetro **PromptForInputArgs**; en combinación con InputArgs/PromptForInputArgs, **Cleanup** revierte los cambios hechos por el test. El puerto por defecto de la Atomic **GUI** es **8487**.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué parámetro deberías usar para personalizar interactivamente los argumentos de entrada? | `PromptForInputArgs` |
| 2 | ¿Qué parámetro deberías usar junto con InputArgs/PromptForInputArgs para revertir los cambios realizados por el test? | `Cleanup` |
| 3 | ¿Cuál es el puerto por defecto usado por la GUI de Atomic? | `8487` |
### Task 7: APT37 Emulation: ATT&CK Navigator
**Explicación:** Última fase de la emulación de APT37. En el ATT&CK Navigator, APT37 tiene **29** técnicas atribuidas y su técnica de phishing es **Spearphishing Attachment**. De esas técnicas, **21** tienen un archivo Atomic existente y la que no tiene tests soportados en Windows es **T1059.006**. El prerequisito de T1055-1 es *"The 64-bit version of Microsoft Office must be installed"* (15 resultados de prerequisito). Ejecutando T1547.001-3 se registran los Event IDs **1,11,13**; el comando por defecto de T1529-1 es `shutdown /s /t 1`; el TargetFilename del Event ID 11 de T1106-1 es `C:\Users\Administrator\AppData\Local\Temp\2\T1106.exe` y el último valor buscado da **28**.
```powershell
Invoke-AtomicTest T1529 -TestGuids <guid> -ShowDetails
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usando el ATT&CK Navigator, ¿cuántas técnicas se atribuyen a APT37? | `29` |
| 2 | Según el mapeo del ATT&CK Navigator, ¿cuál es la técnica de phishing usada por el grupo? | `Spearphishing Attachment` |
| 3 | ¿Cuántas técnicas atribuidas a APT37 tienen un archivo Atomic existente? | `21` |
| 4 | Según los resultados de Q3, ¿qué Atomic no tiene tests soportados en Windows? | `T1059.006` |
| 5 | ¿Cuál es la descripción del prerequisito necesario para el test atómico T1055-1? | `The 64-bit version of Microsoft Office must be installed` |
| 6 | ¿Cuál es el número de prerequisitos encontrados/resultados de la comprobación para T1055-1? | `15` |
| 7 | ¿Cuáles son los tres Event IDs registrados por la ejecución del test atómico T1547.001-3? Proporciónalos en orden ascendente. | `1,11,13` |
| 8 | ¿Qué comando ejecuta (con valor de entrada por defecto) el test atómico T1529-1? No lo ejecutes sin el parámetro ShowDetails. | `shutdown /s /t 1` |
| 9 | ¿Cuál es el valor del TargetFilename dentro del log de creación de archivo (Event ID 11) generado por el test atómico T1106-1? | `C:\Users\Administrator\AppData\Local\Temp\2\T1106.exe` |
| 10 | ¿Cuál es el valor del TargetFilename dentro del log de creación de archivo (Event ID 11) generado por el test atómico T1106-1? (correlación con la Q anterior) | `28` |
### Task 8: Conclusion
**Explicación:** Con esto se completa el caso práctico: desde entender los YAML hasta emular y detectar a APT37 completo. Clave: ver los tests en acción (Sysmon/EDR) para refinar las detecciones y conocer el valor del emulation.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala. | `No answer needed` |
---
**Metodología:** Emulación de adversario (basada en MITRE ATT&CK) con Atomic Red Team; verificación de detecciones vía telemetría (Sysmon) y EDR (Aurora).
**Learning chain:** Estructura de YAML Atomic → ejecución de tests (PowerShell/GUI) → comprobación de prerequisitos y cleanup → cartografiado con ATT&CK Navigator → emulación de APT37 → correlación con eventos Sysmon y reglas EDR.
**MITRE ATT&CK:** T1110.001 (Password Guessing), T1218.005 (Mshta), T1003 (Credential Dumping), T1053.005 (Scheduled Task), T1547.001 (Registry Run Keys), T1082 (System Information Discovery), T1087.001 (Local Account), T1059.003 (Windows Command Shell), T1055 (Process Injection), T1529 (System Shutdown/Reboot), T1106 (Native API), T1566.001 (Spearphishing Attachment).
**Fuente:** [TryHackMe - Atomic Red Team](https://tryhackme.com/room/atomicredteam)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
