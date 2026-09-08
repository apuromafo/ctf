# Windows Memory & User Activity

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `windowsmemoryanduseractivity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsmemoryanduseractivity) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Volatility / sessions / hivelist / userassist / cmdline / handles / dumpfiles / olevba |
| **Impacto** | Reconstruir la actividad de usuario (sesiones, comandos, archivos, macros) a partir de un memory dump de Windows |

---

**Contexto:** Sala DFIR (Premium) centrada en el análisis de un volcado de memoria Windows (`THM-WIN-001_071528_07052025.mem`) con Volatility 3 para reconstruir la actividad del usuario durante un incidente: sesiones iniciadas, hives de registro cargados, actividad de la interfaz gráfica (UserAssist), ejecución de comandos, acceso a archivos y macros maliciosas.

## Solucionario

### Task 1: Introduction

**Explicación:**

La sala enseña a investigar la actividad de usuario desde un volcado de memoria usando Volatility 3: quién inició sesión, qué comandos se ejecutaron y qué archivos se abrieron. Es la segunda de un set de tres salas del módulo Memory Analysis.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click to continue to the room | `No answer needed` |

### Task 2: Scenario Information

**Explicación:**

Escenario del incidente THM-0001 en TryHatMe. Host `WIN-001` (Windows 10 22H2, 10.0.19045). El 5 de mayo de 2025 se toma un volcado de memoria completo con hash MD5 `78535fc49ab54fed57919255709ae650`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I went through the case details and am ready to find out more | `No answer needed` |

### Task 3: Environment & Setup

**Explicación:**

Arrancar la VM y localizar el volcado `THM-WIN-001_071528_07052025.mem` en `/home/ubuntu`. Se usa el comando `vol` para ejecutar Volatility 3.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click here if you were able to start your environment | `No answer needed` |

### Task 4: Tracking Sessions

**Explicación:**

Se identifican las sesiones iniciadas con el plugin `windows.sessions`, el usuario `DESKTOP-3NMNM0H/operator` estaba en la sesión de consola cuando se ejecutaron WINWORD.EXE y updater.exe. Se confirma el bootstrap cargando los hives con `windows.registry.hivelist` (ntuser.dat de operator). El plugin `windows.registry.userassist` revela los programas lanzados desde la GUI (p. ej., Command Prompt → cmd.exe).

```
vol -f THM-WIN-001_071528_07052025.mem windows.sessions > sessions.txt
vol -f THM-WIN-001_071528_07052025.mem windows.registry.hivelist > hivelist.txt
vol -f THM-WIN-001_071528_07052025.mem windows.registry.userassist > userassist.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which plugin should be used to identify user login sessions from memory? | `windows.sessions` |
| 2 | Which user was logged into a console session when WINWORD.EXE and updater.exe were executed? | `DESKTOP-3NMNM0H/operator` |
| 3 | According to the UserAssist data, which executable related to command-line activity was launched via a shortcut? | `cmd.exe` |
| 4 | Which Volatility 3 plugin reveals evidence of programs launched by a user through the graphical interface? | `windows.registry.userassist` |

### Task 5: Command Execution & File Access

**Explicación:**

Con `windows.cmdline` se observa que WINWORD.EXE (PID 5252) abrió el documento `C:\Users\operator\Documents\cv-resume-test.docm` con el modificador `/n`. Con `windows.handles` se confirma que el archivo `cv-resume-test.docm` estaba abierto en el espacio de memoria del proceso WINWORD.EXE.

```
vol -f THM-WIN-001_071528_07052025.mem windows.cmdline > cmdline.txt
vol -f THM-WIN-001_071528_07052025.mem windows.handles > handles.txt
cat handles.txt | grep WINWORD
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file was passed to WINWORD.EXE? | `cv-resume-test.docm` |
| 2 | What is the name of the Volatility3 plugin that extracts open files, registry keys, and kernel objects from process handle tables? | `windows.handles` |
| 3 | What is the full device path where the .docm file was found open in WINWORD.EXE's memory space? | `C:\Users\operator\Documents\cv-resume-test.docm` |
| 4 | What Windows command-line switch was used to open WINWORD.EXE in a new instance? | `/n` |

### Task 6: Tracing User Execution

**Explicación:**

Se vuelca la plantilla `.dotm` vinculada al proceso WINWORD.EXE con `windows.dumpfiles --pid 5252`. Tras confirmar con `file` que es un documento de Word, se descomprime y se analiza `vbaProject.bin` con `olevba`. El macro descarga y ejecuta `pdfupdater.exe` desde `http://attacker.thm/pdfupdater.exe`.

```
vol -f THM-WIN-001_071528_07052025.mem -o 5252/ windows.dumpfiles --pid 5252
ls 5252/ | grep dotm
cp 5252/file.*.DataSectionObject.Normal.dotm.dat .
file file.*.dat
unzip file.*.dat -d extracted/
olevba extracted/word/vbaProject.bin
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command did we use to confirm that the dumped `.dat` file is a Microsoft Word document? | `file` |
| 2 | According to the `olevba` output, what is the name of the file downloaded and executed by the macro? | `pdfupdater.exe` |
| 3 | What is the full URL hardcoded in the macro for downloading the executable? | `http://attacker.thm/pdfupdater.exe` |

### Task 7: Conclusion

**Explicación:**

Se construye la línea de tiempo del incidente usando solo datos de RAM: el usuario operator inició sesión, abrió `cv-resume-test.docm`, el macro descargó y ejecutó `pdfupdater.exe`, que derivó en `windows-update.exe` y `updater.exe`, y posteriormente en cmd.exe y powershell.exe (post-explotación).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click to complete the room | `No answer needed` |

---

**Metodología:**

1. **Identificar sesiones:** Usa `windows.sessions` para ver qué usuarios estaban logueados y en qué tipo de sesión.
2. **Confirmar actividad de usuario:** Con `windows.registry.hivelist` comprueba que el hive `ntuser.dat` del usuario sospechoso estaba cargado en memoria.
3. **Actividad gráfica:** Con `windows.registry.userassist` observa qué aplicaciones (p. ej., cmd.exe) se lanzaron desde la GUI.
4. **Línea de comandos:** Con `windows.cmdline` identifica el proceso WINWORD.EXE y el argumento `.docm` abierto.
5. **Acceso a archivos:** Con `windows.handles` confirma qué archivo estaba abierto por el proceso.
6. **Vuelco de plantilla:** Con `windows.dumpfiles --pid 5252` extrae la plantilla `.dotm` de memoria.
7. **Análisis de macros:** Confirma el tipo con `file`, descomprime el `.dotm` y analiza `vbaProject.bin` con `olevba` para recuperar el macro y la URL de descarga.
8. **Correlación:** Construye la cadena `WINWORD` → `pdfupdater` → `windows-update` → `updater` → `cmd`/`powershell` para la línea de tiempo.

**Learning chain:** operator (sesión consola) -> windows.sessions/hivelist -> cv-resume-test.docm (WINWORD.EXE /n) -> windows.cmdline/handles -> dumpfiles .dotm -> file/unzip/olevba -> http://attacker.thm/pdfupdater.exe -> pdfupdater.exe -> windows-update.exe -> updater.exe -> cmd/powershell

**Lección:** *La actividad completa de un usuario comprometido -sesiones, GUI, comandos, archivos y macros- queda registrada en RAM y puede reconstruirse íntegramente con Volatility 3 aún sin logs de disco, lo que vuelve la memoria un artefacto forense esencial en DFIR.*

**MITRE ATT&CK:** T1204.002 (User Execution: Malicious File) · T1059.001 (PowerShell) · T1105 (Ingress Tool Transfer) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Windows Memory & User Activity](https://tryhackme.com/room/windowsmemoryanduseractivity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
