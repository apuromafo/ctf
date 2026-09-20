# XDR_ Operation Global Dagger

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | xdroperationglobaldagger | https://tryhackme.com/room/xdroperationglobaldagger | 02 Level Medium | TryHackMe | Microsoft 365 Defender, XDR, Alertas | Investigación de un incidente real en Microsoft 365 Defender: alertas, tácticas y artefactos de la operación Global Dagger |

---

**Contexto:** La sala **XDR: Operation Global Dagger** plantea la investigación de un incidente dentro de Microsoft 365 Defender. El alumno analiza una cadena de ataque completa registrada en las alertas de la plataforma: ejecución de PowerShell con PowerSploit, dumping de LSASS, bypass de UAC, modificación del registro y comandos hands-on-keyboard de una cuenta comprometida. El solucionario recoge los nombres de las detecciones, sus veredictos (Success/Blocked), los procesos implicados y las fuentes de referencia utilizadas.

## Solucionario

### Task 1: Introducción al incidente

**Explicación:**

La sala presenta el escenario de la operación Global Dagger y el objetivo de la investigación dentro de Microsoft 365 Defender.

Respuesta: `No answer needed`

### Task 2: Preparación de la investigación

**Explicación:**

Se configura el entorno de análisis y se accede a las alertas del incidente para iniciar la investigación.

Respuesta: `No answer needed`

### Task 3: Análisis de las alertas y artefactos

**Explicación:**

Se analizan las alertas que componen la cadena de ataque: la detección de PowerSploit en PowerShell (`HackTool:PowerShell/PowerSploit.F`) con veredicto `Success`, la detección del dumping de LSASS (`HackTool:Win32/DumpLsass.R`) bloqueada (`Blocked`), el proceso implicado (`powershell.exe`), la alerta de bypass de UAC, la ruta del payload (`c:\windows\System32\#{payload}`), el ejecutable del registro (`C:\Windows\System32\reg.exe`), la descripción de la cuenta comprometida realizando un ataque hands-on-keyboard y el comando con el parámetro `-UserConfig` de `ie4uinit.exe`.

Nota de referencia: las pistas y comandos provienen del writeup de la sala disponible en Medium (https://medium.com/@Sle3pyHead/xdr-operation-global-dagger-ctf-notes-tryhackme-ceb0614b5223).

1. `HackTool:PowerShell/PowerSploit.F`
2. `Success`
3. `HackTool:Win32/DumpLsass.R`
4. `Blocked`
5. `powershell.exe`
6. `UAC bypass was detected`
7. `c:\windows\System32\#{payload}`
8. `C:\Windows\System32\reg.exe`
9. `Compromised account conducting hands-on-keyboard attack`
10. `"ie4uinit.exe" -UserConfig`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción al incidente | `No answer needed` |
| 2 | Preparación de la investigación | `No answer needed` |
| 3.1 | Detección de PowerSploit | `HackTool:PowerShell/PowerSploit.F` |
| 3.2 | Veredicto de la detección | `Success` |
| 3.3 | Detección de DumpLsass | `HackTool:Win32/DumpLsass.R` |
| 3.4 | Veredicto de la detección | `Blocked` |
| 3.5 | Proceso involucrado | `powershell.exe` |
| 3.6 | Alerta de UAC | `UAC bypass was detected` |
| 3.7 | Ruta del payload | `c:\windows\System32\#{payload}` |
| 3.8 | Ejecutable del registro | `C:\Windows\System32\reg.exe` |
| 3.9 | Descripción de la cuenta comprometida | `Compromised account conducting hands-on-keyboard attack` |
| 3.10 | Comando con -UserConfig | `"ie4uinit.exe" -UserConfig` |

---

**Metodología:** Investigación de incidente en Microsoft 365 Defender: revisión de las detecciones y veredictos, identificación de los procesos y comandos maliciosos, y reconstrucción de la cadena de ataque desde la ejecución inicial hasta el hands-on-keyboard.

**Learning chain:** Acceso al incidente → alertas → detecciones → procesos → UAC bypass → reg.exe → manos en el teclado → comando final.

**Lección:** *Las alertas de XDR cuentan la historia del ataque por partes: correlacionando nombres de detecciones, veredictos y procesos se reconstruye la cadena completa del incidente.*

**MITRE ATT&CK:** T1059.001 PowerShell · T1003.001 LSASS Memory · T1548.002 Bypass User Account Control · T1112 Modify Registry.

**Fuente:** [TryHackMe - XDR_ Operation Global Dagger](https://tryhackme.com/room/xdroperationglobaldagger)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.