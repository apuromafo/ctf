# Detecting LSASS Memory Dumping

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `detectinglsassmemorydumping` | [TryHackMe](https://tryhackme.com/room/detectinglsassmemorydumping) | 02 Level Medium | TryHackMe | lsass.exe, Mimikatz, ProcDump, comsvcs.dll, Sysmon (10/1/11), Security (4656/4688/4663), PowerShell (4104), Amcache, MFT, USN, YARA, RunAsPPL, Credential Guard | Detección y mitigación del volcado de memoria de LSASS (credential dumping) mediante registros, artefactos y endurecimiento del host |

---

**Contexto:** La sala enseña a detectar y mitigar el credential dumping sobre el proceso LSASS (Local Security Authority Subsystem Service), la técnica MITRE ATT&CK más usada por los adversarios para robar credenciales. Se estudian los datos que LSASS conserva en memoria (hashes NT, tickets Kerberos), los métodos reales de volcado observados en campañas de HAFNIUM, Sandworm, APT41 y Gentleman ransomware, y las capas de detección: registros Sysmon/Security/PowerShell, artefactos (Amcache, MFT, USN) y reglas YARA. El laboratorio entrega una VM objetivo con credenciales `Administrator:Secure!` sobre `MACHINE_IP` (RDP) y recomienda el uso de la DefenseBox (`DFIRUser:Secure!`) para profundizar en los artefactos. Por último se aplican las contramedidas: LSA Protection (RunAsPPL), Vulnerable Driver Blocklist y Credential Guard. Su único prerrequisito es la sala Windows Credentials.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presenta la sala y sus objetivos de aprendizaje: descubrir las técnicas de volcado de LSASS observadas en intrusiones reales, aprender a detectarlas con event logs de Windows, confirmar el volcado con artefactos cuando falten logs y mitigarlo. También describe el laboratorio: VM objetivo (`Administrator:Secure!`) y la DefenseBox opcional (`DFIRUser:Secure!`), ambas accesibles por RDP a `MACHINE_IP`. Parte de la sala Windows Credentials como prerrequisito.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's go! | `No answer needed` |

### Task 2: LSASS Credential Dumping / Volcado de Credenciales de LSASS

**Explicación:** Explica qué datos sensibles conserva LSASS en memoria (hashes NT de usuarios con sesión iniciada, tickets Kerberos TGT y de servicio, y más según la configuración) y por qué es por ello el objetivo preferido del credential dumping. Recorre las técnicas reales: utilidades de Microsoft (Task Manager, Process Explorer y ProcDump, abusado por HAFNIUM), LOLBins (sqldumper.exe y comsvcs.dll con rundll32, como en el caso Gentleman), la API de Windows (MiniDumpWriteDump, usada de forma nativa por Mimikatz, PowerSploit, Nanodump y Cobalt Strike, como en APT41) y métodos avanzados que evadirán LSA Protection (WSASS, KslDump, Nanodump). El parseo posterior del dump es trivial para el atacante (Mimikatz en el host o pypykatz offline), por lo que toda la batalla gira en torno a impedir y detectar el acceso a esa memoria. (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run Mimikatz by following the APT41 example. What is the NT (NTLM) hash of Administrator? | `-` |
| 2 | Run runas.ps1. It will simulate an interactive user logon. What new user do you see after running klist sessions? | `-` |
| 3 | Run Mimikatz again. Now you should see a user from Q2. What is the NT (NTLM) hash of that user? | `-` |

### Task 3: Detecting LSASS Dumping With Logs / Detección del Volcado de LSASS mediante Registros

**Explicación:** La vía más fiable es monitorizar el acceso al proceso lsass.exe con Sysmon Event ID 10 (o Security 4656), donde la access mask 0x1FFFFF (PROCESS_ALL_ACCESS) delata a las herramientas de dumping frente a máscaras legítimas como 0x0400; las masks también permiten atribuir la técnica a una herramienta concreta (0x1010 en `Mimikatz sekurlsa`). Se complementa con la creación de procesos (Sysmon 1 / Security 4688) y sus evasiones típicas: renamed LOLBin (detectable por OriginalFileName y Description del PE), comsvcs.dll enmascarado y PowerShell (PowerShell/Operational 4104). La creación de volcados se caza con Sysmon 11 / Security 4663 (extensiones .dmp, .mdmp, .save, .bin típicas de %Temp% y %AppData%). La práctica pide investigar los logs Sysmon exportados del proceso malicioso WindowsTweaker.exe detectado en el servidor de archivos FS-EU-01. (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The WindowsTweaker malware used its own dumping capabilities first. Which access mask did it use to dump LSASS? | `-` |
| 2 | The C2 also used a masqueraded comsvcs.dll copy. What command line was used to dump LSASS via this method? | `-` |
| 3 | What is the size of the LSASS dump from Q2, in megabytes? (Answer using the number shown in the file properties, such as "22.9") | `-` |

### Task 4: Detecting LSASS Dumping With Artifacts / Detección del Volcado de LSASS mediante Artefactos

**Explicación:** Cuando los logs no están configurados se recurre a artefactos del sistema: Prefetch, Amcache (cuyo UnassociatedFileEntries guarda hashes SHA1 de los binarios dropeados, permitiendo reconocer pd64.exe como un ProcDump renombrado) y AppCompatCache; un `myeasylog.log` vacío junto a un binario puede incluso delatar el uso de ProcDump. En el sistema de archivos se correlacionan las entradas de MFT y USN (rutas absolutas, timestamps de creación, renombrados y copias hacia el directorio de recolección) y se aplican reglas YARA que buscan el header MiniDump MDMP (4D 44 4D 50) para localizar volcados aunque estén renombrados (p. ej. familyphotos.png). La práctica se apoya en las exportaciones de Amcache y artefactos de archivo ya preparadas en la carpeta Task 4, revisables con Timeline Explorer o Notepad. (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the path to the dump file, as revealed by MFT records? | `-` |
| 2 | What binary is likely responsible for creating the dump file? | `-` |
| 3 | What program does this binary represent (e.g., Mimikatz)? | `-` |

### Task 5: Hardening Against LSASS Dumping / Endurecimiento contra el Volcado de LSASS

**Explicación:** LSA Protection (RunAsPPL) convierte a LSASS en un proceso protegido accesible solo por procesos del sistema protegidos, lo que mitiga todos los métodos clásicos de volcado; se configura por registro (HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa → `RunAsPPL` = 1, o 2 con bloqueo UEFI) o por GPO y requiere reinicio. El Vulnerable Driver Blocklist (integrado en Defender desde Windows 11 22H2 / Server 2022 o desplegable vía WDAC) frena el bypass BYOVD, mientras que Credential Guard elimina de LSASS las credenciales por defecto (hashes NTLM y tickets Kerberos), aunque exige hardware y virtualización, solo está en Enterprise y no funciona en domain controllers. La práctica valida el ciclo completo con Mimikatz: error al volcar con RunAsPPL activo, instalación del driver mimidrv (genera System Event ID 7045) con `!+` y `!processprotect /remove /process:LSASS.EXE`, y recuperación del dump. (las dos primeras respuestas no están confirmadas: los valores capturados en el lab aparecen redactados y requieren verificación en laboratorio)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run Mimikatz after enabling LSA Protection. What error name do you see (e.g., kuhl_err)? | `-` |
| 2 | Install the Mimikatz driver by running the commands from the task. What is the ServiceType of the generated System Event ID 7045? | `-` |
| 3 | Run Mimikatz again; you should see the same output you got in Task 2! | `No answer needed` |

### Task 6: Conclusion / Conclusión

**Explicación:** Cierre de la sala: las credenciales solo aparecen en LSASS cuando alguien inicia sesión, por lo que nunca se debe autenticarse como Domain Admin en dispositivos no confiables ni en workstations normales. Se recomienda aplicar el modelo de AD por niveles (tiered model) y mantener una monitorización sólida con Sysmon para detectar el acceso a la memoria de LSASS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room! | `No answer needed` |

---

**Metodología:** La sala propone un flujo defensivo completo frente al dump de LSASS: (1) entender qué credenciales vive en la memoria de LSASS y por qué es el objetivo preferido del adversario, (2) conocer las técnicas reales de volcado (herramientas de Microsoft, LOLBins, API de Windows y variantes avanzadas), (3) detectar la actividad con logs (Sysmon/Security/PowerShell) distinguiendo access masks y evasiones (renamed LOLBins, comsvcs enmascarado, PowerShell), (4) confirmar los hallazgos con artefactos (Amcache, MFT, USN, YARA) cuando faltan los logs, y (5) aplicar las contramedidas (RunAsPPL, GPO, Vulnerable Driver Blocklist, Credential Guard) y verificar experimentalmente su efecto con Mimikatz y el driver BYOVD.

### Cadena de ataque / Attack Chain

```text
Credential Access - Volcado de memoria de LSASS (T1003.001)
  │
  ├─ 1. Objetivo: LSASS (lsass.exe)
  │      Almacena NT hashes y tickets Kerberos de los usuarios con sesión iniciada
  │
  ├─ 2. Técnicas de volcado
  │      Herramientas de Microsoft: Task Manager, Process Explorer, ProcDump (HAFNIUM)
  │      LOLBins: sqldumper.exe, comsvcs.dll / rundll32 MiniDump (Gentleman ransomware)
  │      Windows API: MiniDumpWriteDump → Mimikatz/PowerSploit/Nanodump/Cobalt Strike (APT41)
  │      Avanzadas: WSASS (WerFaultSecure), KslDump, Nanodump (bypass de LSA Protection)
  │      Parseo: el atacante lo hace en el host o offline con pypykatz (indetectable)
  │
  ├─ 3. Detección por logs
  │      Sysmon 10 / Security 4656: Process Access a lsass.exe (mask 0x1FFFFF, 0x1010)
  │      Sysmon 1 / Security 4688: Process Creation (renamed LOLBin → OriginalFileName)
  │      PowerShell/Operational 4104: Out-MiniDump y payloads completos
  │      Sysmon 11 / Security 4663: File Creation (lsass.dmp, .mdmp, .save, .bin)
  │
  ├─ 4. Detección por artefactos
  │      Amcache (SHA1), Prefetch, AppCompatCache + myeasylog.log
  │      MFT y USN: rutas, timestamps, renombrados y copias de volcados
  │      YARA: header MiniDump MDMP (4D 44 4D 50) en todo el disco
  │
  └─ 5. Mitigación
         LSA Protection (RunAsPPL = 1/2) vía Registry o GPO (exige reinicio)
         Vulnerable Driver Blocklist / WDAC → bloquea el bypass BYOVD (mimidrv)
         Credential Guard: elimina NTLM/Kerberos de la memoria de LSASS
```

**Learning chain:** Ubicación de credenciales en LSASS → técnicas de volcado (ProcDump, Task Manager, comsvcs.dll, MiniDumpWriteDump) → detección por logs (Sysmon 10/1/11, Security 4656/4688/4663, PowerShell 4104, access masks) → detección por artefactos (Amcache, MFT, USN, YARA MDMP) → mitigación (RunAsPPL, Vulnerable Driver Blocklist/WDAC, Credential Guard).

**Lección:** *El volcado de LSASS solo es útil si hay credenciales en memoria y el parseo posterior es indetectable, de modo que la defensa debe centrarse en impedir y monitorizar el acceso a la memoria del proceso (Sysmon/RunAsPPL) y en eliminar el valor de esas credenciales con Credential Guard.*

**MITRE ATT&CK:** T1003.001 (OS Credential Dumping: LSASS Memory), T1218.011 (Signed Binary Proxy Execution: Rundll32), T1059.001 (PowerShell), T1543.003 (Create or Modify System Process: Windows Service), T1068 (Exploitation for Privilege Escalation).

**Fuente:** [TryHackMe - Detecting LSASS Memory Dumping](https://tryhackme.com/room/detectinglsassmemorydumping)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.