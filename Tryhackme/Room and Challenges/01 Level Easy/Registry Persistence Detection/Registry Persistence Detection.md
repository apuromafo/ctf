# Registry Persistence Detection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `registrypersistencedetection` | https://tryhackme.com/room/registrypersistencedetection | 01 Level Easy | TryHackMe | Registro de Windows / Run keys / PS-AutoRuns / BootExecute / PrintMonitorDLLs / Winlogon / Userinit | Detección de persistencia en el registro de Windows: claves Run, PS-AutoRuns y ubicaciones como BootExecute, PrintMonitorDLLs y Winlogon/Userinit. |

---

**Contexto:** Sala centrada en la detección de persistencia malware en el registro de Windows. Se analizan las claves de autoarranque (Run/RunOnce) con el payload que deja un bat malicioso, se automatiza la detección con los cmdlets de PS-AutoRuns (Get-PSAutorun, New-AutoRunsBaseLine, Compare-AutoRunsBaseLine) y se revisan ubicaciones menos conocidas como BootExecute, PrintMonitorDLLs y la clave Winlogon con su valor Userinit, donde también se esconden payloads.

> **ES:** "Registry Persistence Detection" — detectar persistencia en el registro de Windows: claves Run, PS-AutoRuns, BootExecute, PrintMonitorDLLs y Winlogon/Userinit.
> **EN:** "Registry Persistence Detection" — detect Windows registry persistence: Run keys, PS-AutoRuns, BootExecute, PrintMonitorDLLs and Winlogon/Userinit.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala: qué es la persistencia en el registro de Windows y cómo detectarla. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |

### Task 2: Persistencia vía claves Run / Run Keys Persistence

**Explicación:** Se analiza una clave Run en la que el valor es `(Default)`. El payload registrado apunta al archivo `C:\Users\Administrator\AppData\Local\bd84\24d9.bat` y deja la cadena `pleaseletmepersist` como señal del mecanismo de persistencia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué nombre de valor usa la entrada maliciosa en la clave Run? / What value name does the malicious entry use in the Run key? | `(Default)` |
| 2 | ¿Qué ruta de archivo se registra como payload en la persistencia? / What file path is registered as the persistence payload? | `C:\Users\Administrator\AppData\Local\bd84\24d9.bat` |
| 3 | ¿Qué cadena secreta deja el payload de la persistencia? / What secret string does the persistence payload leave? | `pleaseletmepersist` |

### Task 3: Detección con PS-AutoRuns / Detection with PS-AutoRuns

**Explicación:** Para automatizar la detección se usa la librería PS-AutoRuns: `Get-PSAutorun` recoge las entradas de autoarranque actuales, `New-AutoRunsBaseLine` crea la línea base de entradas y `Compare-AutoRunsBaseLine` compara la línea base actual con la anterior para detectar cambios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué función obtiene las entradas de autoarranque actuales? / What function gets the current autorun entries? | `Get-PSAutorun` |
| 2 | ¿Qué función crea la línea base de autoarranques? / What function creates the autorun baseline? | `New-AutoRunsBaseLine` |
| 3 | ¿Qué función compara la línea base actual con la anterior? / What function compares the current baseline with the previous one? | `Compare-AutoRunsBaseLine` |

### Task 4: Otras ubicaciones de persistencia / Other Persistence Locations

**Explicación:** Se revisan otras ubicaciones de persistencia del registro: el valor `BootExecute` tiene `1` entrada sospechosa, la clave de `PrintMonitorDLLs` acumula `5` entradas, la comprobación de la política `VerifyDigitalSignature` detecta `3` entradas válidas y el resto de la verificación no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué valor se observa la persistencia vía boot? / In which value is boot persistence observed? | `BootExecute` |
| 2 | ¿Cuántas entradas se detectan en BootExecute? / How many entries are detected in BootExecute? | `1` |
| 3 | ¿Qué clave de DLLs de impresión se usa para persistencia? / What print monitor DLLs key is used for persistence? | `PrintMonitorDLLs` |
| 4 | ¿Cuántas entradas se detectan en PrintMonitorDLLs? / How many entries are detected in PrintMonitorDLLs? | `5` |
| 5 | ¿Qué política de firma digital se comprueba durante la detección? / What digital signature policy is checked during detection? | `VerifyDigitalSignature` |
| 6 | ¿Cuántas entradas validan la firma digital? / How many entries pass the digital signature validation? | `3` |
| 7 | Completa la verificación de la tarea. / Complete the task's verification. | `No answer needed` |

### Task 5: Persistencia vía Winlogon / Winlogon Persistence

**Explicación:** La clave Winlogon (`HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`) usa su valor `Userinit` para persistir, configurado con la cadena `C:\Windows\system32\userinit.exe,C:\Users\Administrator\AppData\Local\THM\789a.bat`. El evento se registra en el contexto `Logon` y el payload deja la cadena `letmestaymyfriend`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta de registro de la clave Winlogon? / What is the registry path of the Winlogon key? | `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` |
| 2 | ¿Qué valor de Winlogon se modifica para persistir? / What Winlogon value is modified for persistence? | `Userinit` |
| 3 | ¿Qué cadena completa de Userinit se configura con el payload? / What full Userinit string is configured with the payload? | `C:\Windows\system32\userinit.exe,C:\Users\Administrator\AppData\Local\THM\789a.bat` |
| 4 | ¿En qué contexto o evento se registra esta modificación? / In what context or event is this modification logged? | `Logon` |
| 5 | ¿Qué cadena secreta acompaña al payload de Winlogon? / What secret string accompanies the Winlogon payload? | `letmestaymyfriend` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen de las técnicas de persistencia y su detección. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |
| 2 | ¿Qué nombre de valor usa la entrada maliciosa en la clave Run? / What value name does the malicious entry use in the Run key? | `(Default)` |
| 3 | ¿Qué ruta de archivo se registra como payload en la persistencia? / What file path is registered as the persistence payload? | `C:\Users\Administrator\AppData\Local\bd84\24d9.bat` |
| 4 | ¿Qué cadena secreta deja el payload de la persistencia? / What secret string does the persistence payload leave? | `pleaseletmepersist` |
| 5 | ¿Qué función obtiene las entradas de autoarranque actuales? / What function gets the current autorun entries? | `Get-PSAutorun` |
| 6 | ¿Qué función crea la línea base de autoarranques? / What function creates the autorun baseline? | `New-AutoRunsBaseLine` |
| 7 | ¿Qué función compara la línea base actual con la anterior? / What function compares the current baseline with the previous one? | `Compare-AutoRunsBaseLine` |
| 8 | ¿En qué valor se observa la persistencia vía boot? / In which value is boot persistence observed? | `BootExecute` |
| 9 | ¿Cuántas entradas se detectan en BootExecute? / How many entries are detected in BootExecute? | `1` |
| 10 | ¿Qué clave de DLLs de impresión se usa para persistencia? / What print monitor DLLs key is used for persistence? | `PrintMonitorDLLs` |
| 11 | ¿Cuántas entradas se detectan en PrintMonitorDLLs? / How many entries are detected in PrintMonitorDLLs? | `5` |
| 12 | ¿Qué política de firma digital se comprueba durante la detección? / What digital signature policy is checked during detection? | `VerifyDigitalSignature` |
| 13 | ¿Cuántas entradas validan la firma digital? / How many entries pass the digital signature validation? | `3` |
| 14 | Completa la verificación de la tarea. / Complete the task's verification. | `No answer needed` |
| 15 | ¿Cuál es la ruta de registro de la clave Winlogon? / What is the registry path of the Winlogon key? | `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` |
| 16 | ¿Qué valor de Winlogon se modifica para persistir? / What Winlogon value is modified for persistence? | `Userinit` |
| 17 | ¿Qué cadena completa de Userinit se configura con el payload? / What full Userinit string is configured with the payload? | `C:\Windows\system32\userinit.exe,C:\Users\Administrator\AppData\Local\THM\789a.bat` |
| 18 | ¿En qué contexto o evento se registra esta modificación? / In what context or event is this modification logged? | `Logon` |
| 19 | ¿Qué cadena secreta acompaña al payload de Winlogon? / What secret string accompanies the Winlogon payload? | `letmestaymyfriend` |
| 20 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

**Metodología:** Inspeccionar las claves de autoarranque (Run con valor `(Default)` y payload en `...\bd84\24d9.bat`), automatizar la detección con PS-AutoRuns (Get-PSAutorun, New-AutoRunsBaseLine, Compare-AutoRunsBaseLine), repasar ubicaciones de persistencia menos visibles (BootExecute, PrintMonitorDLLs, VerifyDigitalSignature) y terminar en la clave Winlogon/Userinit de Windows NT CurrentVersion, comparando líneas base para localizar el payload `...\THM\789a.bat`.

### Cadena de ataque / Attack Chain

```text
Inspeccionar Run keys (Default -> 24d9.bat) -> PS-AutoRuns (Get / New-AutoRunsBaseLine / Compare) -> BootExecute (1) -> PrintMonitorDLLs (5) -> VerifyDigitalSignature (3) -> Winlogon\Userinit (userinit.exe + 789a.bat) -> flag del payload
```

**Learning chain:** Claves Run -> PS-AutoRuns y líneas base -> BootExecute -> PrintMonitorDLLs -> Winlogon/Userinit -> detección del payload.

**Lección:** *El registro de Windows ofrece muchas superficies para persistir; conocer las ubicaciones Run, Winlogon/Userinit, BootExecute y PrintMonitorDLLs, y comparar líneas base con PS-AutoRuns, es la forma de detectar el payload escondido.*

**MITRE ATT&CK:** T1547 (Boot or Logon Autostart Execution), T1547.001 (Registry Run Keys / Startup Folder), T1547.004 (Winlogon Helper DLL)

**Fuente:** [TryHackMe - Registry Persistence Detection](https://tryhackme.com/room/registrypersistencedetection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.