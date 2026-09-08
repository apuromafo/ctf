# Redline

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `btredlinejoxr3d` |
| **Link** | [TryHackMe](https://tryhackme.com/room/btredlinejoxr3d) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Redline / FireEye / IOC / collector / memory/disk forensics / keylogger / malware |
| **Impacto** | Dominar las técnicas de colección forense con Redline para localizar indicadores de compromiso y malware |

---

**Contexto:** Sala práctica sobre Redline, la herramienta de recolección y análisis forense de FireEye. Se usan colectores estándar y de búsqueda de IOC para analizar discos y memoria, identificar keyloggers, malware y persistencia.

## Solucionario

### Task 1: Redline Basics

**Explicación:**

Fundamentos de Redline, la herramienta de análisis forense de FireEye. La respuesta es la organización que desarrolla Redline: **FireEye**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Who developed Redline?) | `FireEye` |

### Task 2: Collector and Analysis Process

**Explicación:**

El flujo de trabajo de Redline: se crea un **Standard Collector**, un **IOC Search Collector**, se ejecuta `RunRedlineAudit.bat`, se realiza la **Disk Enumeration**, y se abre el archivo `AnalysisSession1.mans` para el análisis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (What is used to collect the data?) | `1. Standard Collector` |
| 2 | (Second type of collector) | `2. IOC Search Collector` |
| 3 | (Script to run the collection) | `3. RunRedlineAudit.bat` |
| 4 | (What is performed to detect malware on disk?) | `4. Disk Enumeration` |
| 5 | (File opened at the end to analyse) | `5. AnalysisSession1.mans` |

### Task 3: System Information

**Explicación:**

La información del sistema del host analizado: se trata de un **Windows Server 2019 Standard 17763**. Se identifica un archivo falso de actualización de Office (`MSOfficeUpdateFa.ke`), una contraseña (`THM-p3R5IStENCe-m3Chani$m`), y datos de conexiones: `546`, el mensaje `Someone cracked my password. Now I need to rename my puppy-++-`, una URL de descarga `https://wormhole.app/download-stream/gI9vQtChjyYAmZ8Ody0AuA`, la ruta del flag `C:\Program Files (x86)\Windows Mail\SomeMailFolder\flag.txt` y el flag `THM{600D-C@7cH-My-FR1EnD}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (System info) | `1. Windows Server 2019 Standard 17763` |
| 2 | (Sub-question) | `2. No answer needed` |
| 3 | (Suspicious Office file) | `3. MSOfficeUpdateFa.ke` |
| 4 | (Password found) | `4. THM-p3R5IStENCe-m3Chani$m` |
| 5 | (Connection count) | `5. 546` |
| 6 | (Note/message) | `6. Someone cracked my password. Now I need to rename my puppy-++-` |
| 7 | (Download URL) | `7. https://wormhole.app/download-stream/gI9vQtChjyYAmZ8Ody0AuA` |
| 8 | (Flag path) | `8. C:\Program Files (x86)\Windows Mail\SomeMailFolder\flag.txt` |
| 9 | (Flag) | `9. THM{600D-C@7cH-My-FR1EnD}` |

### Task 4: Keylogger

**Explicación:**

Localización del keylogger: el proceso `psylog.exe`, el ejecutable `THM1768.exe`, el usuario `WIN-2DET5DP0NPT\charles`, el PID `35400`, y la ruta del IOC `C:\Users\charles\Desktop\Keylogger-IOCSearch\IOCs\keylogger.ioc`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Keylogger process) | `1. psylog.exe` |
| 2 | (Executable) | `2. THM1768.exe` |
| 3 | (User) | `3. WIN-2DET5DP0NPT\charles` |
| 4 | (PID) | `4. 35400` |
| 5 | (IOC path) | `5. C:\Users\charles\Desktop\Keylogger-IOCSearch\IOCs\keylogger.ioc` |

### Task 5: Process Explorer

**Explicación:**

Análisis de procesos: el ejecutable `C:\Users\Administrator\AppData\Local\Temp\8eJv8w2id6IqN85dfC.exe`, su directorio `C:\Users\Administrator\AppData\Local\Temp\`, el grupo `BUILTIN\Administrators`, el subsystem `Windows_CUI`, el dispositivo `\Device\HarddiskVolume2`, el hash `57492d33b7c0755bb411b22d2dfdfdf088cbbfcd010e30dd8d425d5fe66adff4` y **PsExec.exe**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Executable path) | `1. C:\Users\Administrator\AppData\Local\Temp\8eJv8w2id6IqN85dfC.exe` |
| 2 | (Directory) | `2. C:\Users\Administrator\AppData\Local\Temp\` |
| 3 | (Group) | `3. BUILTIN\Administrators` |
| 4 | (Subsystem) | `4. Windows_CUI` |
| 5 | (Device) | `5. \Device\HarddiskVolume2` |
| 6 | (Hash) | `6. 57492d33b7c0755bb411b22d2dfdfdf088cbbfcd010e30dd8d425d5fe66adff4` |
| 7 | (Tool used) | `7. PsExec.exe` |

### Task 6: Ransomware

**Explicación:**

Análisis del ransomware: se identifica en el sistema **Windows 7 Home Basic**; el archivo de nota es `_R_E_A_D___T_H_I_S___AJYG1O_.txt`; el DLL malicioso `MpSvc.dll`; el zip `eb5489216d4361f9e3650e6a6332f7ee21b0bc9f3f3a4018c69733949be1d481.zip`; el ejecutable `Endermanch@Cerber5.exe`; el hash `fe1bc60a95b2c2d77cd5d232296a7fa4`; la familia de ransomware identificada es **Cerber**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (OS) | `1. Windows 7 Home Basic` |
| 2 | (Note file) | `2. _R_E_A_D___T_H_I_S___AJYG1O_.txt` |
| 3 | (Malicious DLL) | `3. MpSvc.dll` |
| 4 | (Zip) | `4. eb5489216d4361f9e3650e6a6332f7ee21b0bc9f3f3a4018c69733949be1d481.zip` |
| 5 | (Executable) | `5. Endermanch@Cerber5.exe` |
| 6 | (Hash) | `6. fe1bc60a95b2c2d77cd5d232296a7fa4` |
| 7 | (Ransomware family) | `7. Cerber` |

### Task 7: Conclusion

**Explicación:**

Cierre de la sala y resumen del flujo completo de Redline.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusion) | `No answer needed` |

---

**Metodología:**

1. Crear un Standard/IOC Search Collector y ejecutar `RunRedlineAudit.bat` para recolectar los datos.
2. Abrir `AnalysisSession1.mans` y revisar System Information, procesos, y artefactos de disco/memoria.
3. Correlacionar procesos y hashes para identificar el keylogger, el malware y el ransomware.

**Learning chain:** Standard Collector -> IOC Search Collector -> Disk Enumeration -> AnalysisSession1.mans -> keylogger -> ransomware

**Lección:** *La recolección sistemática con Redline (Standard + IOC collectors) permite identificar malware, persistencia y ransomware mediante el análisis cruzado de procesos, hashes y carpetas.*

**MITRE ATT&CK:** T1566 (Phishing) · T1059 (Execution) · T1003 (Credential Dumping) · T1486 (Data Encrypted for Impact / ransomware) · T1547 (Boot or Logon Autostart Execution)

**Fuente:** [TryHackMe - Redline](https://tryhackme.com/room/btredlinejoxr3d)
