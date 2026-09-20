# Monday Monitor

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (SOC/defensa) | `mondaymonitor` | https://tryhackme.com/room/mondaymonitor | 01 Level Easy | TryHackMe | Análisis de macros (xlsm) / schtasks / T1053.005 / PowerShell / registro de Windows / monitoreo | Análisis defensivo de un documento malicioso que abusa de tareas programadas y PowerShell para establecer persistencia. |

---

**Contexto:** Sala de análisis defensivo tipo caza/Monday monitor: se analiza un documento de Excel con macros (`SwiftSpend_Financial_Expenses.xlsm`) que, al abrirse, modifica el registro y crea una tarea programada con `schtasks.exe`. La tarea lanza PowerShell con un payload ofuscado en base64 (técnica ATOMIC-T1053.005) que ejecuta `ping www.youarevulnerable.thm`. El análisis acumula una contraseña hallada (`I_AM_M0NIT0R1NG`), identifica el proceso `memotech.exe` y concluye con la flag `THM{M0N1T0R_1$_1N_3FF3CT}`. Todo el payload y las respuestas se conservan verbatim.

> **ES:** Analizar un .xlsm malicioso que usa el registro + schtasks para lanzar PowerShell (base64) y confirmar la técnica T1053.005.
> **EN:** Analyze a malicious .xlsm that uses registry + schtasks to launch PowerShell (base64) and confirm technique T1053.005.

## Solucionario

### Task 1: Monitoreo del lunes / Monday monitoring

**Explicación:** El documento malicioso es `SwiftSpend_Financial_Expenses.xlsm`. La macro ejecuta, a través de la creación de una tarea programada diaria a las `12:34`, un comando que añade una clave en el registro (`HKCU\\SOFTWARE\\ATOMIC-T1053.005`) con un valor en base64, y después invoca PowerShell para decodificarlo y ejecutarlo. Decodificando la cadena base64 `cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0=` se obtiene el comando `ping www.youarevulnerable.thm`. Durante la investigación se recupera la contraseña `I_AM_M0NIT0R1NG`, el proceso responsable `memotech.exe` y la flag final `THM{M0N1T0R_1$_1N_3FF3CT}`. El payload completo se conserva a continuación verbatim.

Contenido original de la tarea / Original task content:

```text
1. 1. SwiftSpend_Financial_Expenses.xlsm
   2. \"cmd.exe\" /c \"reg add HKCU\\SOFTWARE\\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN \"ATOMIC-T1053.005\" /TR \"cmd /c start /min \\\"\\\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\\\SOFTWARE\\\\ATOMIC-T1053.005).test)))\" /sc daily /st 12:34\"
   3. 12:34
   4. ping www.youarevulnerable.thm
   5. I_AM_M0NIT0R1NG
   6. memotech.exe
   7. THM{M0N1T0R_1$_1N_3FF3CT}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Documento malicioso / Malicious document | `SwiftSpend_Financial_Expenses.xlsm` |
| 2 | Comando que establece la persistencia / Persistence command | `\"cmd.exe\" /c \"reg add HKCU\\SOFTWARE\\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN \"ATOMIC-T1053.005\" /TR \"cmd /c start /min \\\"\\\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\\\SOFTWARE\\\\ATOMIC-T1053.005).test)))\" /sc daily /st 12:34\"` |
| 3 | Hora de la tarea programada / Scheduled task time | `12:34` |
| 4 | Comando final que ejecuta / Final command executed | `ping www.youarevulnerable.thm` |
| 5 | Contraseña encontrada / Password found | `I_AM_M0NIT0R1NG` |
| 6 | Proceso responsable / Responsible process | `memotech.exe` |
| 7 | Flag de la sala / Room flag | `THM{M0N1T0R_1$_1N_3FF3CT}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Documento malicioso / Malicious document | `SwiftSpend_Financial_Expenses.xlsm` |
| 2 | Comando que establece la persistencia / Persistence command | `\"cmd.exe\" /c \"reg add HKCU\\SOFTWARE\\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN \"ATOMIC-T1053.005\" /TR \"cmd /c start /min \\\"\\\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\\\SOFTWARE\\\\ATOMIC-T1053.005).test)))\" /sc daily /st 12:34\"` |
| 3 | Hora de la tarea programada / Scheduled task time | `12:34` |
| 4 | Comando final que ejecuta / Final command executed | `ping www.youarevulnerable.thm` |
| 5 | Contraseña encontrada / Password found | `I_AM_M0NIT0R1NG` |
| 6 | Proceso responsable / Responsible process | `memotech.exe` |
| 7 | Flag de la sala / Room flag | `THM{M0N1T0R_1$_1N_3FF3CT}` |

---

**Metodología:** Abrir/inspeccionar el `.xlsm` sospechoso, extraer la cadena de comandos de la macro, identificar la creación de la tarea programada diaria (`schtasks.exe /sc daily /st 12:34`) y la escritura en el registro, observar la desofuscación del payload PowerShell en base64 (resultado: `ping www.youarevulnerable.thm`) y correlacionar procesos y credenciales (memotech.exe / I_AM_M0NIT0R1NG) hasta la flag.

### Cadena de ataque / Attack Chain

```text
SwiftSpend_Financial_Expenses.xlsm -> reg add HKCU\SOFTWARE\ATOMIC-T1053.005 (valor base64) -> schtasks.exe /Create /sc daily /st 12:34 -> PowerShell IEX (decodifica base64) -> ping www.youarevulnerable.thm -> credencial I_AM_M0NIT0R1NG -> memotech.exe -> THM{M0N1T0R_1$_1N_3FF3CT}
```

**Learning chain:** Malware documental (xlsm) -> escritura en registro -> Scheduled Task (T1053.005) -> PowerShell en memoria (base64) -> detección y flag.

**Lección:** *Las macros de Office abusan de binarios nativos de Windows (schtasks, reg) y de la desofuscación en memoria para evadir el disco; el monitoreo de tareas programadas y de invocaciones de PowerShell es esencial.* 

**MITRE ATT&CK:** T1053.005 (Scheduled Task/Job: Scheduled Task), T1059.001 (PowerShell), T1112 (Modify Registry), T1055 (Process Injection)

**Fuente:** [TryHackMe - Monday Monitor](https://tryhackme.com/room/mondaymonitor)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.