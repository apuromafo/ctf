# Detecting Persistent DLL Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | walkthrough | `detectingpersistentdllattacks` | [TryHackMe](https://tryhackme.com/room/detectingpersistentdllattacks) | 03 Level Hard | TryHackMe | Sysmon 7/12/13/22, COM hijacking, UsrClass.dat, Print Processor, ServiceDll, LSA Security Packages, RunAsPPL, autorunsc, RECmd, MFTECmd, $MFT | Detección de persistencia por puntos de extensión de DLL en el registro (COM hijacking, print processors, service DLL y paquetes LSA) mediante análisis DFIR offline contra una baseline |

---

**Contexto:** Tras cerrar el caso (archivo eliminado, cuenta reseteada y checklist de persistencia limpia), a la mañana siguiente la misma workstation de THM-DEV-WS vuelve a contactar con el mismo dominio bloqueado sin nada descargado, sin sesión remota abierta y sin nadie en el teclado. La sala reabre el caso desde los ficheros que dejaron los responders, sin host vivo ni consola EDR: en `C:\Case\baseline\` está el mismo build antes del incidente, y en `C:\Case\DEV-WS\triage\`, `evtx\`, `files\` y `mft\$MFT` la recolección del host. Se trabaja con la DefenseBox (usuario `DFIRUser`/`Secure!`, `CONNECTION_IP`) y el almacén IR-Storage (`Administrator`/`Secure!`, `MACHINE_IP`). La metodología construye una baseline, la diferencia de cuatro maneras (autorunsc -z, RECmd, hashes de archivo) y extrae cuatro mecanismos de persistencia por DLL: un COM hijacking en UsrClass.dat (estilo RomCom/UAT-5647), un print processor DLL sustituido (Gelsemium), un ServiceDll repunteado (`syncsvc.dll`) y un paquete LSA (`msvctrl`) que Windows se negó a cargar por LSA Protection, acabando en la erradicación y el triaje de una segunda máquina.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presenta el caso reabierto: el checklist de persistencia salió limpio pero el host vuelve a hacer beaconing, porque existe un mecanismo que esa checklist nunca pudo encontrar. La sala trabaja únicamente con la evidencia recogida por los responders y termina con el triaje de un segundo host.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Tarea informativa | `No answer needed` |

### Task 2: DLL Loads and Extension Points / Cargas de DLL y Puntos de Extensión

**Explicación:** Explica cómo vigilar la carga de una DLL: un módulo mapeado en un proceso no aparece en un árbol de procesos y el Sysmon Event ID 7 es el que registra ese mapeo. Se presentan los campos clave del Event ID 7 (Image, ImageLoaded, Signed, SignatureStatus), sus límites (solo registra cargas con éxito; la firma no discrimina en logs exportados sin catálogo) y el mapa de puntos de extensión por proceso host (explorer.exe, spoolsv.exe, svchost.exe, lsass.exe, netsh.exe, winlogon.exe y AppInit_DLLs) con su trigger y privilegio de escritura.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | A host beacons twenty seconds after boot with no user logged on. Which registry hive can be ruled out as the source of that persistence? (Answer Format: four letters) | `HKCU` |
| 2 | Which UEFI feature, when enabled, makes the AppInit_DLLs mechanism inert? | `Secure Boot` |
| 3 | A configuration names a DLL that was never written to disk. How many Event ID 7 records does that produce? | `0` |

### Task 3: Baselining and Sweeping the Host / Línea Base y Barrido del Host

**Explicación:** Construye una baseline a partir de hives del mismo build antes del incidente y la compara con el triage: montaje offline con `reg load`, parseo con `RECmd` y dos barridos de autostart con `autorunsc -z` (uno por boot), con diffs en PowerShell. De la comparación de UsrClass.dat, de las hives SYSTEM/SOFTWARE y de los archivos capturados salen cuatro leads: un CLSID InprocServer32 que la baseline no tiene, un print processor cuyo archivo no coincide, un ServiceDll que apunta fuera de System32 y un valor de LSA con un nombre desconocido.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which value under Control\Lsa carries a name the baseline does not have? | `Security Packages` |
| 2 | What is the full path that ServiceDll points to? | `C:\ProgramData\Microsoft\DeviceSync\syncsvc.dll` |
| 3 | Hashing the collected files against the baseline returns one mismatch. Which file? | `winprint.dll` |

### Task 4: COM Hijacking and UsrClass.dat / COM Hijacking y UsrClass.dat

**Explicación:** Profundiza en el primer lead: el registro per-usuario de la clase `{2155fee3-2419-4373-b102-6843707eb41f}` en UsrClass.dat, que sombrea a la clase de iconos de Explorer que responde `C:\Windows\System32\thumbcache.dll` en la hive de máquina (el mismo CLSID que publicó Talos para UAT-5647/RomCom). Se confirma la escritura con Sysmon 13, la carga con Sysmon 7 y la datación independiente con el `$MFT`.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which CLSID was hijacked on THM-DEV-WS? | `{2155fee3-2419-4373-b102-6843707eb41f}` |
| 2 | Which DLL answers for the same CLSID in the machine hive? | `C:\Windows\System32\thumbcache.dll` |

### Task 5: The Print Processor / El Print Processor

**Explicación:** El segundo lead es una DLL de print processor: el registro coincide con la baseline (winprint) pero el archivo que hay detrás no (hash mismatch). `spoolsv.exe` resuelve el nombre `winprint.dll` dentro de `prtprocs\x64\` como LocalSystem al arranque; la comparación con sigcheck (sin version resources, entropy alta) y el Sysmon Event ID 7 prueban la carga.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | At what time (UtcTime) did spoolsv.exe load the print processor DLL? | `2026-08-16 23:01:47` |

### Task 6: When the Evidence Is Missing / Cuando la Evidencia Falta

**Explicación:** Resuelve los dos últimos leads con el método de la ausencia: primero se prueba que el canal estaba grabando y después se demuestra que el evento concreto no existe. El servicio SysMain fue repunteado (un repunteo no escribe System 7045) y su DLL cargada por svchost.exe como SYSTEM, y el paquete LSA `msvctrl` no aparece en la lista Security 4622 de paquetes cargados porque CodeIntegrity 3033 muestra que LSA Protection (RunAsPPL) bloqueó la carga.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | At what time (UtcTime) did svchost.exe load the malicious service DLL? | `2026-08-16 23:02:42` |
| 2 | Which registry value under Control\Lsa is the protection that blocked it? | `RunAsPPL` |

### Task 7: Eradication and Verification / Erradicación y Verificación

**Explicación:** Plan de remediación: aislar, recolectar (memoria antes que disco) y quitar primero la configuración y luego el archivo, reiniciar y verificar. Se elimina la clase COM per-usuario, se restaura el print processor desde la baseline, se devuelve el ServiceDll de SysMain al valor de la baseline (REG_EXPAND_SZ) y se limpia `Security Packages` (REG_MULTI_SZ); la verificación final es un re-diff contra la baseline tras el reboot (y un logon del usuario para el COM).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | A boot-triggered print processor implant is removed while its DLL is still mapped into a running spoolsv.exe. What single action must be taken before a re-sweep can confirm eradication? | `Reboot` |

### Task 8: Hands-On Investigation / Investigación Práctica

**Explicación:** Cierra la sala con el triaje de una segunda máquina, THM-MKT-WS: hives SYSTEM/SOFTWARE sin sus .LOG1/.LOG2 (RECmd requiere `--nl`), tres canales de eventos y el `$MFT`. El diff con su baseline propia deja una entrada añadida bajo ShellIconOverlayIdentifiers cuyo CLSID, DLL, autor, timestamp y número de cargas hay que resolver con Sysmon 13/7 y MFTECmd. (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Diffing the two SOFTWARE hives leaves one added entry under ShellIconOverlayIdentifiers. What is the name of that entry? | `-` |
| 2 | Which CLSID does that entry point to? | `-` |
| 3 | What is the full path of the DLL registered in that CLSID's InprocServer32 value? | `-` |
| 4 | Which user account wrote the overlay handler's registry values? | `-` |
| 5 | When was the malicious DLL written to disk, by its $MFT Created0x10 timestamp? | `-` |
| 6 | How many times did explorer.exe load that DLL? | `-` |

### Task 9: Conclusion / Conclusión

**Explicación:** Resumen de las lecciones del room: los puntos de extensión son funcionalidad legítima que el adversario registra para que Windows cargue su código; el análisis del trigger (boot, logon, servicio, a demanda o muerto) estructura la investigación; el diff contra la baseline sustituye al criterio del analista; y una ausencia de evento solo es evidencia si el instrumento estaba grabando. Tarea informativa.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Tarea informativa | `No answer needed` |

---

**Metodología:** La sala sigue un análisis DFIR offline completo: (1) construir una baseline del mismo build pre-incidente, (2) barrer los autostart locations con `autorunsc -z` y comparar hives con `reg load`, RECmd y hashes de archivos, (3) extraer leads por diff contra una referencia adecuada, (4) confirmar la escritura con Sysmon 13, la carga con Sysmon 7 y fechar con `$MFT`, (5) probar la ausencia de eventos con System 7045, Security 4610/4614/4622 y CodeIntegrity 3033, y (6) erradicar, reiniciar y verificar con un re-diff contra la baseline.

### Cadena de ataque / Attack Chain

```text
Incidente reabierto: THM-DEV-WS beaconing 20s tras el boot (sin logon)
  │
  ├─ Baseline + diff (Task 3): autorunsc -z, RECmd, hashes
  │     → 4 leads: CLSID InprocServer32 (UsrClass.dat), winprint.dll, ServiceDll, Security Packages
  │
  ├─ 1. COM hijacking (Task 4) — explorer.exe — sin privilegios (RomCom/UAT-5647)
  │        CLSID {2155fee3-…} → %LocalAppData%\KeyStore\keyprov.dll
  │        Sysmon 13 (write powershell.exe) → Sysmon 7 (load explorer.exe) → Sysmon 22 (C2)
  │        $MFT 06:40:39 + ADS Zone.Identifier (origen externo)
  │
  ├─ 2. Print Processor (Task 5) — spoolsv.exe / LocalSystem — Admin (Gelsemium)
  │        winprint.dll sustituido en prtprocs\x64\ → Sysmon 7: 2026-08-16 23:01:47
  │        sigcheck: sin version resources, entropy 5.927
  │
  ├─ 3. Service DLL (Task 6) — svchost.exe / SYSTEM — Admin
  │        SysMain → ServiceDll = C:\ProgramData\Microsoft\DeviceSync\syncsvc.dll
  │        Carga 23:02:42 (1s tras el write); System 7045 AUSENTE (repunteo)
  │
  └─ 4. LSA Security Package (Task 6) — lsass.exe — Admin
           Security Packages = msvctrl → 4622 no lo lista → CodeIntegrity 3033: LOAD REFUSED (RunAsPPL=2)
```

**Learning chain:** Comprensión de puntos de extensión de DLL → lectura de Sysmon 7/12/13/22 → baseline y barridos offline (autorunsc -z, RECmd) → diffs y leads → confirmación de escritura/carga y datación con $MFT → ausencia probada (7045, 4622, 3033) → erradicación y verificación post-reboot → triaje autónomo de un segundo host.

**Lección:** *La carga de DLL desde puntos de extensión es funcionalidad legítima de Windows; el hallazgo se construye con baselines, con la confirmación de escritura y carga, y probando que la ausencia de un evento no es un fallo del instrumento.*

**MITRE ATT&CK:** T1574.001 (DLL Search Order Hijacking), T1546.015 (Component Object Model Hijacking), T1547.012 (Print Processors), T1543.003 (Windows Service), T1547.005 (Security Support Provider).

**Fuente:** [TryHackMe - Detecting Persistent DLL Attacks](https://tryhackme.com/room/detectingpersistentdllattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.