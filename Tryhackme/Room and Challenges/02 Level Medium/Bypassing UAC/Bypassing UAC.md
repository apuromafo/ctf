# Bypassing UAC
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `bypassinguac` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bypassinguac) |
| **Sección** | Windows / Privilege Escalation |
| **Fuente** | Writeup de Yash22222 (GitHub) |
| **Componentes** | Windows, UAC (Integrity Levels), elevación automática (auto-elevate), msconfig, azman.msc, fodhelper, fodhelper-curver, Disk Cleanup (scheduled tasks), variables de entorno, PowerShell |
| **Impacto** | Sala Medium del path Windows Privilege Escalation: entender UAC e Integrity Levels y ejecutar cinco bypasses prácticos (GUI: msconfig/azman.msc, auto-elevación: fodhelper y su variante que cae en antivirus, y abuso de scheduled tasks con variables de entorno). |
---
**Contexto:** UAC (User Account Control) limita qué procesos corren con privilegios elevados usando Integrity Levels. Un token no elevado tiene nivel "medium"; uno elevado, "high"; el nivel más alto es "system". La sala enseña a evadirlo explotando procesos marcados como auto-elevados y registros de Windows que los lanzan, logrando una shell elevada: msconfig y azman.msc (GUI), fodhelper (manipulando la clave `App Paths`), una variante de fodhelper que no dispara el antivirus y el abuso de una scheduled task de Disk Cleanup con variables de entorno.
*EN: UAC (User Account Control) restricts which processes run with elevated privileges using Integrity Levels. A non-elevated token is "medium", an elevated one "high", and the top level is "system". The room teaches how to bypass it by abusing auto-elevated processes and the registry keys that launch them, obtaining an elevated shell: msconfig and azman.msc (GUI), fodhelper (by tampering with the `App Paths` key), a fodhelper variant that avoids the antivirus, and abusing a Disk Cleanup scheduled task with environment variables.*
## Solucionario
### Task 1 — Deploy the Machine
**Explicación:** Desplegar la máquina Windows. Pregunta de despliegue, sin respuesta.
*EN: Deploy the Windows machine. Deployment question, no answer needed.*
### Task 2 — UAC
**Explicación:** Antes de atacar hay que conocer los Integrity Levels: un proceso con token sin elevar corre en nivel "medium"; un token elevado ("administrator" en la práctica) es "high"; el nivel más alto es "system". El servicio *Application Information* (appinfo) es el encargado de gestionar la elevación de aplicaciones marcadas como tallas para auto-elevarse.
*EN: Before attacking, understand Integrity Levels: a process with a non-elevated token runs at "medium", an elevated one (practically "administrator") is "high", and the top level is "system". The Application Information service (appinfo) is the one that handles the elevation of applications flagged to auto-elevate.*

```powershell
whoami /groups        # Integrity Level del token actual
```
### Task 3 — Bypassing UAC with GUI
**Explicación:** Algunas herramientas con manifest marcado para auto-elevarse se pueden abrir con credenciales de administrador sin pasar por el prompt de UAC. Abusando del diálogo de ayuda de `msconfig` (la ayuda la lanza un proceso desde una ruta controlable) se consigue una shell elevada y la primera bandera. Repitiendo la técnica con `azman.msc` se obtiene la segunda bandera.
*EN: Tools whose manifest is flagged to auto-elevate can be opened with admin credentials without the UAC prompt. Abusing the help dialog of `msconfig` (its help launches a process from a controllable path) yields an elevated shell and the first flag. Repeating the technique with `azman.msc` gives the second flag.*

```powershell
# msconfig -> combinación de teclas/ayuda para forzar la ruta de un binario controlado
# azman.msc -> mismo vector GUI
```
### Task 4 — Bypassing UAC with fodhelper
**Explicación:** `fodhelper.exe` (On-Demand Feature Helper) está marcado para elevarse automáticamente. Manipulando `HKCU\Software\Classes\ms-settings\Shell\open\command` para que apunte a nuestro binario (por ejemplo PowerShell), al lanzar `fodhelper` se ejecuta sin prompt de UAC y con privilegios de administrador.
*EN: `fodhelper.exe` (On-Demand Feature Helper) is flagged to auto-elevate. By tampering with `HKCU\Software\Classes\ms-settings\Shell\open\command` so it points to our binary (e.g. PowerShell), launching `fodhelper` executes it without a UAC prompt and with admin privileges.*

```powershell
New-Item "HKCU:\Software\Classes\ms-settings\Shell\open\command" -Force
Set-ItemProperty "HKCU:\Software\Classes\ms-settings\Shell\open\command" -Name "(default)" -Value "powershell.exe"
# (o "cmd /c start powershell") y luego lanzar fodhelper.exe
Start-Process fodhelper.exe
```
### Task 5 — Bypassing UAC with fodhelper-curver
**Explicación:** Variante de fodhelper que evita que el AV detecte los cambios en el registro: en lugar de tocar `ms-settings` se diseña la modificación para que el antivirus no bloquee la clave, consiguiendo el mismo resultado (shell elevada) y la bandera correspondiente.
*EN: A fodhelper variant that prevents the antivirus from flagging the registry tampering: instead of touching `ms-settings`, the modification is crafted so the AV does not block the key, achieving the same result (elevated shell) and its associated flag.*
### Task 6 — Bypassing UAC with scheduled tasks and environment variables
**Explicación:** La scheduled task de disk cleanup (SilentCleanup/Task Scheduler) se puede disparar con `schtasks` y ejecuta un comando que, tras expandir una variable de entorno controlable (`windir` o similar apuntando a nuestro payload), lanza nuestro binario con privilegios elevados sin prompt.
*EN: The disk cleanup scheduled task (SilentCleanup / Task Scheduler) can be triggered with `schtasks`; it runs a command that, after expanding a controllable environment variable (e.g. `windir` pointing to our payload), launches our binary with elevated privileges and no prompt.*

```powershell
schtasks /run /tn \Microsoft\Windows\DiskCleanup\SilentCleanup /i
set windir=C:\temp\malicious                       # apuntar a nuestro payload
```
### Task 7 — Summary RCE with UAC Bypass
**Explicación:** Resumen de la sala: cómo integrar estos bypasses en un flujo de compromiso. Sin pregunta con respuesta.
*EN: Room summary: how to integrate these bypasses into a compromise flow. No answer needed.*
### Task 8 — Conclusion
**Explicación:** Conclusión y recomendaciones de mitigación (default UAC settings, monitoring). Sin pregunta con respuesta.
*EN: Conclusion and mitigation recommendations (default UAC settings, monitoring). No answer needed.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the highest integrity level? | `system` |
| 2 | What is the integrity level of an elevated token? | `high` |
| 3 | What is the name of the Windows service responsible for the auto-elevation of applications? | `application information service` |
| 4 | What is the flag obtained by bypassing UAC with msconfig (GUI)? | `THM{UAC_HELLO_WORLD}` |
| 5 | What is the flag obtained by bypassing UAC with azman.msc (GUI)? | `THM{GUI_UAC_BYPASSED_AGAIN}` |
| 6 | What is the flag obtained by bypassing UAC with fodhelper? | `THM{AUTOELEVATE4THEWIN}` |
| 7 | What is the flag obtained by the fodhelper variant that bypasses the antivirus? | `THM{AV_UAC_BYPASS_4_ALL}` |
| 8 | What is the flag obtained bypassing UAC with scheduled tasks and environment variables? | `THM{SCHEDULED_TASKS_AND_ENVIRONMENT_VARS}` |
---
**Metodología:** Entender UAC/Integrity Levels → identificar procesos auto-elevados (msconfig, azman.msc, fodhelper) → manipular claves de registro (`HKCU\Software\Classes\ms-settings\...` y App Paths) para redirigir el binario → ejecutar el proceso y obtener shell "high" → variante fodhelper-curver para evitar AV → abuso de scheduled task (SilentCleanup) con variable de entorno → banderas.
**Learning chain:** UAC → GUI auto-elevation (msconfig/azman.msc) → registry tampering (fodhelper) → AV evasion (fodhelper-curver) → scheduled tasks + env vars (Disk Cleanup) → elevated shell sin prompt.
**Lección:** *UAC no es un límite de seguridad del kernel: es una barrera de conveniencia. Cualquier ejecutable marcado como auto-elevado se convierte en un vector si controlas la clave de registro que indica qué binario lanza.*
**MITRE ATT&CK:** T1548.002 (Bypass User Account Control), T1068 (Exploitation for Privilege Escalation), T1059.001 (PowerShell), T1574.011 (Services File Permissions Weakness, registry paths), T1036.
**Fuente:** [TryHackMe - Bypassing UAC](https://tryhackme.com/room/bypassinguac)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.