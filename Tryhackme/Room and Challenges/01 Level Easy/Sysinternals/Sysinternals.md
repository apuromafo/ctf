# Sysinternals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `sysinternals` | https://tryhackme.com/room/sysinternals | 01 Level Easy | TryHackMe | Sysinternals Suite / Sysinternals Live / Streams (ADS) / Sigcheck / SDelete / TCPView / Autoruns / ProcDump / Process Explorer / Process Monitor / PsExec / Strings / WinObj / WebClient / ZoomIt | Análisis de sistemas Windows con las utilidades Sysinternals: instalación de la suite, uso de Sysinternals Live, lectura de ADS, inspección de procesos y extracción de rutas PDB. |

---

**Contexto:** Room de la ruta SOC Level 1 que enseña a usar las herramientas Sysinternals para analizar sistemas o aplicaciones Windows. Se conecta por RDP a una máquina Windows y se recorre la instalación del conjunto completo (la última herramienta listada es ZoomIt), el uso de Sysinternals Live (que requiere el servicio WebClient), las utilidades de archivos y disco (Sigcheck, Streams para Alternate Data Streams y SDelete), de red (TCPView), de procesos (Autoruns, ProcDump, Process Explorer, Process Monitor y PsExec), de seguridad, WinObj y miscelánea (Strings, que revela la ruta PDB de ZoomIt.exe).

> **ES:** Aprender a usar Sysinternals sobre una máquina Windows: instalar la suite, ejecutar herramientas desde Sysinternals Live (WebClient), leer el ADS de `file.txt` con Streams, consultar WHOIS, revisar Image Hijacks en Autoruns (`taskmgr.exe` -> `c:\tools\sysint\procexp.exe`) y correr Strings sobre ZoomIt.exe para obtener la ruta del PDB.
> **EN:** Learn to use Sysinternals on a Windows box: install the suite, run tools from Sysinternals Live (WebClient), read the ADS of `file.txt` with Streams, query WHOIS, review Image Hijacks in Autoruns (`taskmgr.exe` -> `c:\tools\sysint\procexp.exe`) and run Strings on ZoomIt.exe to get the PDB path.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de Sysinternals: una colección de más de 70 herramientas de Windows categorizadas en utilidades de archivos y disco, red, gestión de procesos, seguridad, información del sistema y miscelánea. Microsoft adquirió las herramientas en 2006.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuándo adquirió Microsoft las herramientas Sysinternals? / When did Microsoft acquire the Sysinternals tools? | `2006` |
| 2 | Completa la tarea de introducción. / Complete the introduction task. | `No answer needed` |

### Task 2: Instalar la suite Sysinternals / Install the Sysinternals Suite

**Explicación:** Se descarga el conjunto completo desde el índice de utilidades o vía Sysinternals Live. La última herramienta listada dentro de la suite es ZoomIt.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la última herramienta listada dentro de la suite Sysinternals? / What is the last tool listed within the Sysinternals Suite? | `ZoomIt` |

### Task 3: Usar Sysinternals Live / Using Sysinternals Live

**Explicación:** Sysinternals Live permite ejecutar las herramientas directamente desde la web sin descargarlas, mediante `\\live.sysinternals.com\tools\`. Para interactuar con live.sysinternals.com hay que habilitar el servicio WebClient en el host local.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué servicio debe estar habilitado para interactuar con live.sysinternals.com? / What service needs to be enabled on the local host to interact with live.sysinternals.com? | `WebClient` |

### Task 4: Utilidades de archivos y disco / File and Disk Utilities

**Explicación:** Se cubren tres utilidades: Sigcheck (verificación de versión, marcas de tiempo y firma digital), Streams (Alternate Data Streams, ADS) y SDelete (borrado seguro). Con Streams se lista el stream oculto de `file.txt` y, leyéndolo con Notepad (`notepad C:\Users\Administrator\Desktop\file.txt:ads.txt`), se obtiene el texto dentro del ADS.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | There is a txt file on the desktop named `file.txt`. Using one of the three discussed tools in this task, what is the text within the ADS? / Hay un archivo txt en el escritorio llamado `file.txt`. Usando una de las tres herramientas de esta tarea, ¿cuál es el texto dentro del ADS? | `I am hiding in the stream.` |

### Task 5: Utilidades de red / Networking Utilities

**Explicación:** TCPView ofrece listados detallados de todos los endpoints TCP y UDP con direcciones locales y remotas y estados de conexión. Con una herramienta WHOIS se consulta la ISP/organización de la dirección remota de las capturas de la tarea.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Using WHOIS tools, what is the ISP/Organization for the remote address in the screenshots above? / Usando herramientas WHOIS, ¿cuál es la ISP/organización de la dirección remota de las capturas anteriores? | `Microsoft Corporation` |

### Task 6: Utilidades de procesos / Process Utilities

**Explicación:** Se presentan Autoruns, ProcDump, Process Explorer, Process Monitor y PsExec. En la pestaña Image Hijacks de Autoruns se detecta una entrada nueva respecto a las capturas: `taskmgr.exe` fue actualizada y su valor ahora apunta a `c:\tools\sysint\procexp.exe`.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Run Autoruns and inspect what are the new entries in the Image Hijacks tab compared to the screenshots above. / Ejecuta Autoruns e inspecciona las nuevas entradas de la pestaña Image Hijacks comparadas con las capturas anteriores. | `No answer needed` |
| 2 | What entry was updated? / ¿Qué entrada fue actualizada? | `taskmgr.exe` |
| 3 | What is the updated value? / ¿Cuál es el valor actualizado? | `c:\tools\sysint\procexp.exe` |

### Task 7: Utilidades de seguridad / Security Utilities

**Explicación:** Se presentan las herramientas de seguridad del paquete (entre ellas Sysmon, un servicio/driver que registra eventos de creación de procesos, conexiones de red, creación y borrado de archivos, y que admite reglas personalizadas orientadas a SIEM). Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la tarea de utilidades de seguridad. / Complete the security utilities task. | `No answer needed` |

### Task 8: Información del sistema / System Information

**Explicación:** WinObj permite ver y gestionar los objetos del namespace de Windows (archivos, directorios, dispositivos, objetos del kernel), incluyendo sus descriptores de seguridad. Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la tarea de información del sistema. / Complete the system information task. | `No answer needed` |

### Task 9: Miscelánea / Miscellaneous

**Explicación:** Entre las utilidades misceláneas (BgInfo, RegJump) se ejecuta la herramienta Strings sobre ZoomIt.exe filtrando por `.pdb` (`strings ZoomIt.exe | findstr /i .pdb`), lo que revela la ruta completa del archivo PDB: `C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb`.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Run the Strings tool on ZoomIt.exe. What is the full path to the .pdb file? / Ejecuta la herramienta Strings sobre ZoomIt.exe. ¿Cuál es la ruta completa al archivo .pdb? | `C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb` |

### Task 10: Conclusión / Conclusion

**Explicación:** Cierre de la room: Sysinternals es un conjunto esencial de herramientas para el análisis de sistemas y aplicaciones Windows, usado tanto por atacantes como por defensores. Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuándo adquirió Microsoft las herramientas Sysinternals? / When did Microsoft acquire the Sysinternals tools? | `2006` |
| 2 | Completa la tarea de introducción. / Complete the introduction task. | `No answer needed` |
| 3 | ¿Cuál es la última herramienta listada dentro de la suite Sysinternals? / What is the last tool listed within the Sysinternals Suite? | `ZoomIt` |
| 4 | ¿Qué servicio debe estar habilitado para interactuar con live.sysinternals.com? / What service needs to be enabled on the local host to interact with live.sysinternals.com? | `WebClient` |
| 5 | There is a txt file on the desktop named `file.txt`. Using one of the three discussed tools in this task, what is the text within the ADS? | `I am hiding in the stream.` |
| 6 | Using WHOIS tools, what is the ISP/Organization for the remote address in the screenshots above? | `Microsoft Corporation` |
| 7 | Run Autoruns and inspect what are the new entries in the Image Hijacks tab compared to the screenshots above. | `No answer needed` |
| 8 | What entry was updated? | `taskmgr.exe` |
| 9 | What is the updated value? | `c:\tools\sysint\procexp.exe` |
| 10 | Completa la tarea de utilidades de seguridad. / Complete the security utilities task. | `No answer needed` |
| 11 | Completa la tarea de información del sistema. / Complete the system information task. | `No answer needed` |
| 12 | Run the Strings tool on ZoomIt.exe. What is the full path to the .pdb file? | `C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb` |
| 13 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

**Metodología:** RDP a la máquina Windows -> leer la introducción y el año de adquisición (2006) -> instalar la suite y anotar el último tool (ZoomIt) -> habilitar WebClient para Sysinternals Live -> usar Streams para leer el ADS de `file.txt` -> consultar WHOIS con TCPView para la ISP -> revisar Image Hijacks en Autoruns (`taskmgr.exe`, valor `c:\tools\sysint\procexp.exe`) -> repasar seguridad, WinObj y miscelánea -> ejecutar Strings sobre ZoomIt.exe y filtrar `.pdb` para obtener `C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb` -> concluir.

### Cadena de ataque / Attack Chain

```text
RDP -> Sysinternals Suite -> ZoomIt (último tool) -> Sysinternals Live (WebClient) -> Streams -> ADS de file.txt -> Streams -> "I am hiding in the stream." -> TCPView/WHOIS -> Microsoft Corporation -> Autoruns Image Hijacks -> taskmgr.exe -> c:\tools\sysint\procexp.exe -> Strings ZoomIt.exe | findstr /i .pdb -> ZoomIt.pdb
```

**Learning chain:** Sysinternals -> instalación -> Sysinternals Live -> WebClient -> Streams/ADS -> WHOIS -> Autoruns/Image Hijacks -> Strings/PDB.

**Lección:** *Las utilidades Sysinternals convierten el análisis de Windows en tareas rutinarias: desde leer Alternate Data Streams ocultos con `streams` hasta descubrir rutas de símbolos con `strings`, siempre conviene probarlas antes de instalar herramientas equivalentes.*

**MITRE ATT&CK:** T1003.001 (OS Credential Dumping), T1005 (Data from Local System), T1083 (File and Directory Discovery), T1106 (Native API).

**Fuente:** [TryHackMe - Sysinternals](https://tryhackme.com/room/sysinternals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.