# Supplemental Memory [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Premium)
* **Slug:** `supplementalmemory`
* **Link:** https://tryhackme.com/room/supplementalmemory
* **Sección / Section:** Forensics / Memory
* **Fuente / Source:** Web (jalilayed/Medium, VALKYRI3/Medium, Francesco Pastore/Medium, Iram Jack/Medium, simontaplin.net)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de análisis forense de memoria. Como miembro de un equipo DFIR debes analizar un volcado de memoria de la estación WIN-015, cuyo usuario Cain Omoore guarda claves de acceso al sistema de control de la fábrica TryHatMe. Investigarás movimiento lateral, exfiltración, escalada de privilegios y robo de credenciales usando Volatility 3.
> **EN:** Memory forensics room. As a DFIR team member you must analyze a memory dump of the WIN-015 workstation, whose user Cain Omoore stores access keys to the TryHatMe factory control system. You will investigate lateral movement, exfiltration, privilege escalation and credential theft using Volatility 3.

---

### Task 1 — Movimiento Lateral y Descubrimiento / Lateral Movement and Discovery

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which executed process provides evidence of lateral movement to this host? | `WmiPrvSE.exe` |
| What is the MITRE technique ID associated with the lateral movement method used by the threat actor? | `T1021.006` |
| Which other process was executed as part of the lateral movement activity on this host? | `TeamsView.exe` |
| What is the Security Identifier (SID) of the user account under which the process was executed on this host? | `S-1-5-21-3147497877-3647478928-1701467185-1008` |
| What is the name of the domain-related security group the user account was a member of? | `Domain Users` |
| Which processes linked to discovery activity were executed by the threat actor? (Alphabetical order) | `ipconfig.exe, systeminfo.exe, whoami.exe` |
| What is the Command and Control IP address that the threat actor connected to from this host? (Format: IP:Port) | `34.244.169.133:1995` |

---

### Task 2 — Escalada de Privilegios y Robo de Credenciales / Privilege Escalation and Credential Dumping

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Identify another suspicious process on the host. Provide the full path to the process. | `C:\Windows\Temp\pan.exe` |
| Which account was used to execute this malicious process? | `Local System` |
| What was the malicious command line executed by this process? | `privilege::debug sekurlsa::logonpasswords` |
| Given the command line from the previous question, which well-known hacking tool was likely used? | `Mimikatz` |
| What is the MITRE ATT&CK technique ID for the attacker's evasion method? | `T1036` |

---

## Metodología / Methodology

1. **Paso / Step:** Correr Volatility 3 sobre el volcado `WIN-015-20250522-111717.dmp` y usar el plugin `windows.pstree` (o los resultados precocinados) para reconstruir el árbol de procesos. / Run Volatility 3 on the `WIN-015-20250522-111717.dmp` dump and use the `windows.pstree` plugin (or the precooked results) to rebuild the process tree.
2. **Paso / Step:** Detectar el movimiento lateral: `svchost.exe (748)` lanzó `WmiPrvSE.exe (2376)`, que a su vez ejecutó `TeamsView.exe (1672)`, seguido de comandos de reconocimiento `systeminfo.exe`, `ipconfig.exe` y `whoami.exe`. La técnica empleada es Windows Remote Management (WinRM/WMI), catalogada como T1021.006. / Detect lateral movement: `svchost.exe (748)` spawned `WmiPrvSE.exe (2376)`, which in turn executed `TeamsView.exe (1672)`, followed by the recon commands `systeminfo.exe`, `ipconfig.exe` and `whoami.exe`. The technique used is Windows Remote Management (WinRM/WMI), catalogued as T1021.006.
3. **Paso / Step:** Obtener el contexto del usuario con `windows.getsids` (PID 1672): el proceso corrió como `cain.omoore` (SID S-1-5-21-3147497877-3647478928-1701467185-1008), miembro del grupo `Domain Users`. / Obtain the user context with `windows.getsids` (PID 1672): the process ran as `cain.omoore` (SID S-1-5-21-3147497877-3647478928-1701467185-1008), a member of the `Domain Users` group.
4. **Paso / Step:** Inspeccionar `windows.netscan` filtrando por `TeamsView.exe` para identificar la conexión de mando y control establecida (34.244.169.133:1995) como resultado de las acciones previas. / Inspect `windows.netscan` filtering by `TeamsView.exe` to identify the established command-and-control connection (34.244.169.133:1995) as a result of the previous actions.
5. **Paso / Step:** Profundizar en el análisis: localizar el proceso malicioso adicional (`pan.exe` en `C:\Windows\Temp`) mediante `cmdline.txt` y confirmar con `getsids --pid 4840` que se ejecutó como `Local System` (escalada de privilegios). / Dig deeper: locate the additional malicious process (`pan.exe` in `C:\Windows\Temp`) using `cmdline.txt` and confirm with `getsids --pid 4840` that it ran as `Local System` (privilege escalation).
6. **Paso / Step:** Identificar la línea de comandos maliciosa `privilege::debug sekurlsa::logonpasswords`, propia de Mimikatz, ejecutada bajo el nombre falso `pan.exe` (masquerading, T1036), lo que confirma el dumping de credenciales. / Identify the malicious command line `privilege::debug sekurlsa::logonpasswords`, typical of Mimikatz, executed under the fake name `pan.exe` (masquerading, T1036), which confirms credential dumping.

### Cadena de ataque / Attack Chain

```
Cain Omoore (credenciales cacheadas en WIN-001)
  -> Robo de credenciales (cached credentials)
  -> Movimiento lateral a WIN-015 (WinRM/WMI - T1021.006)
  -> svchost.exe (748) -> WmiPrvSE.exe (2376) -> TeamsView.exe (1672)
  -> Descubrimiento: systeminfo.exe, ipconfig.exe, whoami.exe
  -> C2 establecida: 34.244.169.133:1995
  -> Escalada a Local System (servicio/ejecución privilegiada)
  -> pan.exe (mimikatz renombrado, T1036):
      privilege::debug sekurlsa::logonpasswords
  -> Dumping de credenciales (T1003)
```

**Lección:** Un dump de memoria permite reconstruir la cadena completa de un ataque: desde el movimiento lateral (WMI/WinRM) hasta el robo de credenciales con Mimikatz, incluso cuando la herramienta está renombrada o "masqueradeada"; el análisis cruzado de procesos, SIDs y conexiones con Volatility 3 es clave.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.