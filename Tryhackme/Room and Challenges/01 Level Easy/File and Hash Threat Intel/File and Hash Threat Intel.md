# File and Hash Threat Intel

| **Dificultad** | Easy |
| **Tipo** | Inteligencia de amenazas (laboratorio) |
| **Slug** | `fileandhashthreatintel` |
| **Link** | [TryHackMe](https://tryhackme.com/room/fileandhashthreatintel) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | VirusTotal / Hybrid Analysis / Enriquecimiento de hashes / Ransomware Akira |
| **Impacto** | Laboratorio de inteligencia de amenazas orientado a enriquecer artefactos (archivos y hashes) con fuentes de inteligencia: análisis de heurísticas de archivo, etiquetas de VirusTotal, comportamiento en sandbox de Hybrid Analysis, técnica de DLL Side-Loading e identificación del ransomware Akira y su inhibición de recuperación. |

---

**Contexto:** La sala enseña a enriquecer archivos y hashes con inteligencia de amenazas. Se comienza detectando técnicas de evasión en el nombre del archivo (extensiones dobles), se analiza el malware "bl0gger" en VirusTotal y Hybrid Analysis (hash, etiqueta de amenaza, comportamiento y procesos), se estudia el "Morse-Code-Analyzer" (falso positivo de un vendor, DLL Side-Loading y su infraestructura C2) y se termina identificando una muestra del ransomware Akira (hash, familia, nota de rescate y técnica de inhibición de restauración).

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación del laboratorio: enriquecer archivos y hashes con fuentes de inteligencia (VirusTotal, Hybrid Analysis). Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción a la inteligencia de archivos y hashes. | `No answer needed` |

### Task 2: Heurística y nombres de archivo

**Explicación:** El archivo detectado es `payroll.pdf`; usa una extensión doble (realmente un ejecutable disfrazado de PDF), técnica de evasión clásica (`Double extensions`) que engaña según la configuración de Windows.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué archivo fue detectado durante la investigación? | `payroll.pdf` |
| 2 | ¿Qué técnica de evasión utilizaba el archivo? | `Double extensions` |

### Task 3: Análisis del malware "bl0gger"

**Explicación:** La muestra SHA256 `2672b668...` se clasifica en VirusTotal como `trojan.graftor/blackmoon`; primera detección `2025-05-15 12:03:49`. El vendor `CyberFortress` dio inicialmente un falso negativo. La técnica clave identificada es `DLL Side-Loading`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash SHA256 de la muestra? | `2672b6688d7b32a90f9153d2ff607d6801e6cbde61f509ed36d0450745998d58` |
| 2 | ¿Cuál es la etiqueta de amenaza según VirusTotal? | `trojan.graftor/blackmoon` |
| 3 | ¿Cuál es la fecha de la primera detección registrada? | `2025-05-15 12:03:49` |
| 4 | ¿Qué vendor lo clasificó inicialmente como no malicioso? | `CyberFortress` |
| 5 | ¿Qué técnica de MITRE ATT&CK se identificó en el archivo? | `DLL Side-Loading` |

### Task 4: Análisis del malware "Morse-Code-Analyzer"

**Explicación:** Hybrid Analysis le asigna las etiquetas `BlackMoon, Discovery, windows-server-utility`. En el sandbox ejecuta `regsvr32 %WINDIR%\Media\ActiveX.ocx /s` (sigiloso), aparece el proceso secundario `werfault.exe` y usa `svchost.exe` como señuelo legítimo. La infraestructura C2 es `hxxp://121.182.174.27:3000/server.exe` y la muestra expone `454` strings.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué etiquetas muestra Hybrid Analysis para la muestra? | `BlackMoon, Discovery, windows-server-utility` |
| 2 | ¿Qué comando sigiloso ejecutó la muestra en el sandbox? | `regsvr32 %WINDIR%\Media\ActiveX.ocx /s` |
| 3 | ¿Qué proceso secundario apareció? | `werfault.exe` |
| 4 | ¿Qué proceso con aspecto legítimo se utilizó como señuelo? | `svchost.exe` |
| 5 | ¿Cuál es la URL de la infraestructura de C2 asociada? | `hxxp://121.182.174.27:3000/server.exe` |
| 6 | ¿Cuántas strings se extrajeron en total de la muestra? | `454` |

### Task 5: Ransomware Akira

**Explicación:** La muestra de Akira (SHA256 `43b0ac11...`) se etiqueta como `akira, filecryptor`; primera detección `2024-10-30 17:17:24 UTC`. Deja la nota `akira_readme.txt` y, para impedir la restauración, borra las Shadow Copies con `Get-WmiObject Win32_Shadowcopy | Remove-WmiObject` (MITRE `T1490`).

```powershell
Get-WmiObject Win32_Shadowcopy | Remove-WmiObject
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hash SHA256 de la muestra de Akira? | `43b0ac119ff957bb209d86ec206ea1ec3c51dd87bebf7b4a649c7e6c7f3756e7` |
| 2 | ¿Qué etiquetas de familia identificaron la muestra? | `akira, filecryptor` |
| 3 | ¿Cuál es la marca de tiempo de la primera detección? | `2024-10-30 17:17:24 UTC` |
| 4 | ¿Cómo se llama la nota de rescate? | `akira_readme.txt` |
| 5 | ¿Qué comando se usa para inhibir la recuperación del sistema (borrado de copias de seguridad)? | `Get-WmiObject Win32_Shadowcopy \| Remove-WmiObject` |
| 6 | ¿Cuál es el ID de la técnica de MITRE ATT&CK utilizada? | `T1490` |

### Task 6: Conclusión

**Explicación:** Repaso: heurística de nombres de archivo, enriquecimiento de hashes con VirusTotal, sandboxing con Hybrid Analysis y clasificación de ransomware.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa los puntos clave que refuerza el laboratorio. | `No answer needed` |

---

**Metodología:** Se parte del archivo sospechoso (`payroll.pdf`) y de la heurística de doble extensión para sospechar de evasión. El enriquecimiento empieza por los hashes: se consultan fuentes de inteligencia (VirusTotal) para obtener la etiqueta de la familia (`trojan.graftor/blackmoon`), la primera detección y el vendor que dio falso positivo; luego se cruza con el sandbox (Hybrid Analysis) para recuperar comandos sigilosos, procesos secundarios, tags, C2 y strings extraídas. La muestra del ransomware Akira se clasifica por familia, nota de rescate y la técnica T1490 (inhibición de la recuperación borrando las Shadow Copies).

**Learning chain:** heurística de archivo → enriquecimiento de hash → sandbox (comportamiento) → identificación de C2 → clasificación de ransomware.

**MITRE ATT&CK:** T1490 (Inhibit System Recovery), T1574.002 (DLL Side-Loading), T1036.005 (Masquerading: Match Legitimate Name or Location), T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:** [TryHackMe - File and Hash Threat Intel](https://tryhackme.com/room/fileandhashthreatintel)