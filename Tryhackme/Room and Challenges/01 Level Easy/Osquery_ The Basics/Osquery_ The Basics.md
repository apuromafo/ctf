# Osquery_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `osquerythebasics` | [TryHackMe](https://tryhackme.com/room/osquerythebasics) | `01 Level Easy` | THM | osquery, SQL, Windows, persistencia | Práctica de consultas osqueryi |

> **Objeto:** Usar osqueryi para consultar el sistema Windows del laboratorio (procesos, programas, bibliotecas, usuarios y persistencia) y responder las preguntas forenses del reto.

---

**Contexto:** Sala práctica de osquery sobre una máquina Windows: se ejecutan consultas contra las tablas del sistema (procesos en ejecución, bibliotecas cargadas, usuarios con SID, programas instalados) y se analizan artefactos de persistencia (userassist, carpeta de inicio, batstartup.bat).

> **ES:** Sala práctica de osquery sobre una máquina Windows: se ejecutan consultas contra las tablas del sistema (procesos en ejecución, bibliotecas cargadas, usuarios con SID, programas instalados) y se analizan artefactos de persistencia (userassist, carpeta de inicio, batstartup.bat).

> **EN:** Hands-on osquery room on a Windows machine: queries are run against the system tables (running processes, loaded libraries, users with SIDs, installed programs) and persistence artifacts are analyzed (userassist, startup folder, batstartup.bat).

## Solucionario

### Task 1: Osquery_ The Basics / Osquery_ The Basics

**Explicación:** La tarea recoge todas las respuestas del reto. El contenido original, conservado íntegramente, es el siguiente:

1. No answer needed
2. No answer needed
3. 1. 3
   2. pid
   3. 5
4. 1. 56
   2. 180
   3. programs
   4. data
5. 1. 19
   2. Creative Artist
   3. S-1-5-21-1966530601-3185510712-10604624-1009
   4. C:\Windows\System32\ieframe.dll
   5. Wireshark 4.4.9 x64
6. 1. userassist
   2. DiskWipe.exe
   3. ProtonVPN
   4. 215
   5. batstartup.bat
   6. C:\Users\James\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\batstartup.bat

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | No answer needed (paso 1) | `No answer needed` |
| 2 | No answer needed (paso 2) | `No answer needed` |
| 3.1 | Respuesta del apartado 3.1 | `3` |
| 3.2 | Respuesta del apartado 3.2 | `pid` |
| 3.3 | Respuesta del apartado 3.3 | `5` |
| 4.1 | Respuesta del apartado 4.1 | `56` |
| 4.2 | Respuesta del apartado 4.2 | `180` |
| 4.3 | Respuesta del apartado 4.3 | `programs` |
| 4.4 | Respuesta del apartado 4.4 | `data` |
| 5.1 | Respuesta del apartado 5.1 | `19` |
| 5.2 | Respuesta del apartado 5.2 | `Creative Artist` |
| 5.3 | Respuesta del apartado 5.3 (SID del usuario) | `S-1-5-21-1966530601-3185510712-10604624-1009` |
| 5.4 | Respuesta del apartado 5.4 (biblioteca cargada) | `C:\Windows\System32\ieframe.dll` |
| 5.5 | Respuesta del apartado 5.5 (programa instalado) | `Wireshark 4.4.9 x64` |
| 6.1 | Respuesta del apartado 6.1 | `userassist` |
| 6.2 | Respuesta del apartado 6.2 | `DiskWipe.exe` |
| 6.3 | Respuesta del apartado 6.3 | `ProtonVPN` |
| 6.4 | Respuesta del apartado 6.4 | `215` |
| 6.5 | Respuesta del apartado 6.5 (artefacto de inicio) | `batstartup.bat` |
| 6.6 | Respuesta del apartado 6.6 (ruta del artefacto de inicio) | `C:\Users\James\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\batstartup.bat` |

---

**Metodología:** 1) Abrir osqueryi sobre la máquina Windows del laboratorio. 2) Ejecutar las consultas SQL sobre las tablas correspondientes (procesos, programas, usuarios, bibliotecas, persistencia). 3) Anotar los resultados de cada consulta según el orden de las preguntas del reto. 4) Analizar los artefactos de persistencia (userassist, carpeta de inicio y batstartup.bat) para completar las respuestas finales.

### Cadena de ataque / Attack Chain

1. Consulta de procesos y contadores (respuestas `3`, `pid`, `5`).
2. Consulta del contador de programas y datos (`56`, `180`, `programs`, `data`).
3. Enumeración de usuarios y bibliotecas (`19`, `Creative Artist`, SID, `ieframe.dll`, `Wireshark 4.4.9 x64`).
4. Análisis de persistencia (`userassist`, `DiskWipe.exe`, `ProtonVPN`, `215`, `batstartup.bat` y su ruta de inicio).

**Learning chain:** osquery → SQL → tablas de procesos y programas → usuarios y bibliotecas → artefactos de persistencia → respuestas

**Lección:** *osquery convierte el sistema en una base de datos consultable: conocer las tablas (procesos, programas, usuarios, persistencia) permite responder preguntas forenses con consultas SQL precisas.*

**MITRE ATT&CK:** T1082 - System Information Discovery, T1012 - Query Registry, T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

**Fuente:** [TryHackMe - Osquery_ The Basics](https://tryhackme.com/room/osquerythebasics)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.