# Windows Command Line

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `windowscommandline` | [TryHackMe](https://tryhackme.com/room/windowscommandline) | 01 Level Easy | TryHackMe | cmd.exe / ver / hostname / ipconfig /all / netstat / type / tasklist / taskkill / shutdown | Introducción a la línea de comandos de Windows (cmd.exe): información del sistema, red, gestión de procesos y apagado |

---

**Contexto:** Sala introductoria al intérprete de comandos de Windows (cmd.exe). Sobre una máquina Windows Server virtualizada se practican comandos esenciales: obtener la versión del sistema y el hostname, comprobar la configuración de red, listar servicios en escucha, leer archivos, gestionar procesos y controlar el reinicio o el apagado del sistema.

> **ES:** La sala enseña a manejar cmd.exe: comandos de información del sistema (ver, hostname), diagnóstico de red (ipconfig /all, netstat), lectura de archivos (type), gestión de procesos (tasklist, taskkill) y apagado/reinicio (shutdown).
> **EN:** This room teaches how to use cmd.exe: system information commands (ver, hostname), network troubleshooting (ipconfig /all, netstat), file reading (type), process management (tasklist, taskkill) and system shutdown/restart (shutdown).

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Pregunta introductoria de la sala sobre el intérprete de comandos por defecto del entorno Windows. Contenido original de la sala (verbatim): `cmd.exe`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es el intérprete de línea de comandos por defecto en el entorno Windows? | `cmd.exe` |

### Task 2: Información básica del sistema / Basic System Information
**Explicación:** Se emplean comandos para obtener información del sistema. El comando `ver` muestra la versión del sistema operativo de la máquina Windows 10.0.20348.2655 y `hostname` revela que el host se llama `WINSRV2022-CORE`. Contenido original de la sala (verbatim): `10.0.20348.2655`, `WINSRV2022-CORE`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la versión del sistema operativo de la máquina Windows? | `10.0.20348.2655` |
| ¿Cuál es el hostname de la máquina Windows? | `WINSRV2022-CORE` |

### Task 3: Solución de problemas de red / Network Troubleshooting
**Explicación:** Se diagnostica la red de la máquina. Con `ipconfig /all` se consulta la dirección física (MAC) del servidor y con `netstat` se identifican los servicios en escucha: `RpcSs` (puerto 135) y `TermService` (puerto 3389). Contenido original de la sala (verbatim): `ipconfig /all`, `RpcSs`, `TermService`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué comando podemos usar para consultar la dirección física (MAC) del servidor? | `ipconfig /all` |
| ¿Cuál es el nombre del servicio que escucha en el puerto 135? | `RpcSs` |
| ¿Cuál es el nombre del servicio que escucha en el puerto 3389? | `TermService` |

### Task 4: Gestión de archivos y discos / File and Disk Management
**Explicación:** Se lee el contenido de un archivo de texto con el comando `type` sobre la ruta `C:\Treasure\Hunt`, encontrando la flag. Contenido original de la sala (verbatim): `THM{CLI_POWER}`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuáles son los contenidos del archivo en C:\Treasure\Hunt? | `THM{CLI_POWER}` |

### Task 5: Gestión de tareas y procesos / Task and Process Management
**Explicación:** Se gestionan los procesos en ejecución. Para buscar procesos relacionados con notepad.exe se usa `tasklist /FI "imagename eq notepad.exe"` y para terminar el proceso con PID 1516 se usa `taskkill /PID 1516`. Contenido original de la sala (verbatim): `tasklist /FI "imagename eq notepad.exe"`, `taskkill /PID 1516`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué comando usarías para encontrar los procesos en ejecución relacionados con notepad.exe? | `tasklist /FI "imagename eq notepad.exe"` |
| ¿Qué comando puedes usar para matar el proceso con PID 1516? | `taskkill /PID 1516` |

### Task 6: Conclusión / Conclusion
**Explicación:** Preguntas finales sobre el control del apagado del sistema. Para reiniciar se usa `shutdown /r` y para abortar un apagado inminente `shutdown /a`. Contenido original de la sala (verbatim): `shutdown /r`, `shutdown /a`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué comando puedes usar para reiniciar el sistema? | `shutdown /r` |
| ¿Qué comando puedes usar para abortar el apagado del sistema? | `shutdown /a` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Intérprete de línea de comandos por defecto en Windows | `cmd.exe` |
| 2 | Versión del sistema operativo de la VM | `10.0.20348.2655` |
| 3 | Hostname de la VM | `WINSRV2022-CORE` |
| 4 | Comando para consultar la dirección física (MAC) | `ipconfig /all` |
| 5 | Servicio que escucha en el puerto 135 | `RpcSs` |
| 6 | Servicio que escucha en el puerto 3389 | `TermService` |
| 7 | Contenido del archivo en C:\Treasure\Hunt | `THM{CLI_POWER}` |
| 8 | Comando para encontrar procesos de notepad.exe | `tasklist /FI "imagename eq notepad.exe"` |
| 9 | Comando para matar el proceso con PID 1516 | `taskkill /PID 1516` |
| 10 | Comando para reiniciar el sistema | `shutdown /r` |
| 11 | Comando para abortar el apagado del sistema | `shutdown /a` |

---

**Metodología:** Se conecta por SSH a la máquina Windows Server (WINSRV2022-CORE) y se practican comandos esenciales de cmd.exe: información del sistema con `ver` y `hostname`, diagnóstico de red con `ipconfig /all` y `netstat`, lectura de archivos con `type`, administración de procesos con `tasklist`/`taskkill` y control del apagado/reinicio con `shutdown /r` y `shutdown /a`.

### Cadena de ataque / Attack Chain

```text
cmd.exe -> ver (10.0.20348.2655) -> hostname (WINSRV2022-CORE) -> ipconfig /all (MAC/puertos) -> netstat (RpcSs:135, TermService:3389) -> type (THM{CLI_POWER}) -> tasklist /FI "imagename eq notepad.exe" -> taskkill /PID 1516 -> shutdown /r (reiniciar) / shutdown /a (abortar)
```

**Learning chain:** cmd.exe --> system info (ver, hostname) --> network troubleshooting (ipconfig /all, netstat) --> file management (type) --> task and process management (tasklist, taskkill) --> shutdown /r / shutdown /a

**Lección:** *cmd.exe es el intérprete por defecto de Windows; dominar sus comandos de información del sistema, red, archivos, procesos y arranque resulta esencial para la administración y el análisis inicial del sistema.*

**MITRE ATT&CK:** T1059.003 (Command and Scripting Interpreter: Windows Command Shell)

**Fuente:** [TryHackMe - Windows Command Line](https://tryhackme.com/room/windowscommandline)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.