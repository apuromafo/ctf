# Supplemental Memory

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `supplementalmemory` |
| **Link** | [TryHackMe](https://tryhackme.com/room/supplementalmemory) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | memory forensics / Volatility 3 / lateral movement / credential dumping / Mimikatz / WinRM / T1021.006 |
| **Impacto** | Reconstruir una cadena completa de ataque (movimiento lateral, escalada y robo de credenciales) desde un volcado de memoria |

---

**Contexto:** Sala de análisis forense de memoria. Como miembro de un equipo DFIR debes analizar un volcado de memoria de la estación WIN-015, cuyo usuario Cain Omoore guarda claves de acceso al sistema de control de la fábrica TryHatMe. Investigarás movimiento lateral, exfiltración, escalada de privilegios y robo de credenciales usando Volatility 3.

## Solucionario

### Task 1: Movimiento Lateral y Descubrimiento / Lateral Movement and Discovery

**Explicación:**

Análisis con Volatility 3 sobre el volcado `WIN-015-20250522-111717.dmp`. El plugin `windows.pstree` reconstruye el árbol de procesos. El proceso que evidencia el movimiento lateral a este host es `WmiPrvSE.exe`; la técnica MITRE asociada es `T1021.006` (Windows Remote Management/WinRM). Otro proceso ejecutado como parte del movimiento lateral es `TeamsView.exe`. El SID del usuario bajo el que se ejecutó es `S-1-5-21-3147497877-3647478928-1701467185-1008`, y su grupo de seguridad de dominio era `Domain Users`. Los procesos de descubrimiento ejecutados (en orden alfabético) son `ipconfig.exe, systeminfo.exe, whoami.exe`. La dirección de C2 a la que se conectó el atacante es `34.244.169.133:1995`.

**Detalle del árbol de procesos:** `svchost.exe (748)` lanzó `WmiPrvSE.exe (2376)`, que a su vez ejecutó `TeamsView.exe (1672)`, seguido de los comandos de reconocimiento. La técnica usada es Windows Remote Management (WinRM/WMI), catalogada como T1021.006.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which executed process provides evidence of lateral movement to this host? | `WmiPrvSE.exe` |
| 2 | What is the MITRE technique ID associated with the lateral movement method used by the threat actor? | `T1021.006` |
| 3 | Which other process was executed as part of the lateral movement activity on this host? | `TeamsView.exe` |
| 4 | What is the Security Identifier (SID) of the user account under which the process was executed on this host? | `S-1-5-21-3147497877-3647478928-1701467185-1008` |
| 5 | What is the name of the domain-related security group the user account was a member of? | `Domain Users` |
| 6 | Which processes linked to discovery activity were executed by the threat actor? (Alphabetical order) | `ipconfig.exe, systeminfo.exe, whoami.exe` |
| 7 | What is the Command and Control IP address that the threat actor connected to from this host? (Format: IP:Port) | `34.244.169.133:1995` |

### Task 2: Escalada de Privilegios y Robo de Credenciales / Privilege Escalation and Credential Dumping

**Explicación:**

Profundizamos: con `cmdline.txt` se localiza el proceso malicioso adicional `C:\Windows\Temp\pan.exe`, confirmado con `getsids --pid 4840` que se ejecutó como **Local System** (escalada de privilegios). La línea de comandos maliciosa es `privilege::debug sekurlsa::logonpasswords`, propia de **Mimikatz**, ejecutada bajo el nombre falso `pan.exe` (masquerading, técnica T1036). Esto confirma el dumping de credenciales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identify another suspicious process on the host. Provide the full path to the process. | `C:\Windows\Temp\pan.exe` |
| 2 | Which account was used to execute this malicious process? | `Local System` |
| 3 | What was the malicious command line executed by this process? | `privilege::debug sekurlsa::logonpasswords` |
| 4 | Given the command line from the previous question, which well-known hacking tool was likely used? | `Mimikatz` |
| 5 | What is the MITRE ATT&CK technique ID for the attacker's evasion method? | `T1036` |

---

**Metodología:**

1. Correr Volatility 3 sobre el volcado `WIN-015-20250522-111717.dmp` y usar el plugin `windows.pstree` (o los resultados precocinados) para reconstruir el árbol de procesos.
2. Detectar el movimiento lateral: `svchost.exe (748)` lanzó `WmiPrvSE.exe (2376)`, que a su vez ejecutó `TeamsView.exe (1672)`, seguido de comandos de reconocimiento `systeminfo.exe`, `ipconfig.exe` y `whoami.exe`. La técnica empleada es Windows Remote Management (WinRM/WMI), catalogada como T1021.006.
3. Obtener el contexto del usuario con `windows.getsids` (PID 1672): el proceso corrió como `cain.omoore` (SID S-1-5-21-3147497877-3647478928-1701467185-1008), miembro del grupo `Domain Users`.
4. Inspeccionar `windows.netscan` filtrando por `TeamsView.exe` para identificar la conexión de mando y control establecida (34.244.169.133:1995) como resultado de las acciones previas.
5. Profundizar: localizar el proceso malicioso adicional (`pan.exe` en `C:\Windows\Temp`) mediante `cmdline.txt` y confirmar con `getsids --pid 4840` que se ejecutó como `Local System` (escalada de privilegios).
6. Identificar la línea de comandos maliciosa `privilege::debug sekurlsa::logonpasswords`, propia de Mimikatz, ejecutada bajo el nombre falso `pan.exe` (masquerading, T1036), lo que confirma el dumping de credenciales.

**Learning chain:** Cain Omoore credenciales cacheadas -> robo de credenciales -> movimiento lateral a WIN-015 (WinRM/WMI T1021.006) -> svchost -> WmiPrvSE -> TeamsView -> discovery -> C2 34.244.169.133:1995 -> escalada a Local System -> pan.exe (mimikatz renombrado, T1036) -> dumping (T1003)

**Lección:** *Un dump de memoria permite reconstruir la cadena completa de un ataque: desde el movimiento lateral (WMI/WinRM) hasta el robo de credenciales con Mimikatz, incluso cuando la herramienta está renombrada o "masqueradeada"; el análisis cruzado de procesos, SIDs y conexiones con Volatility 3 es clave.*

**MITRE ATT&CK:** T1021.006 (Remote Services: Windows Remote Management) · T1003 (OS Credential Dumping) · T1036 (Masquerading) · T1071 (C2) · T1087 (Account Discovery)

**Fuente:** [TryHackMe - Supplemental Memory](https://tryhackme.com/room/supplementalmemory)
