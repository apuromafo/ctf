# Core Windows Processes

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Defensive Security / Análisis de procesos Windows | `corewindowsprocesses` | https://tryhackme.com/room/corewindowsprocesses | 01 Level Easy | TryHackMe | Task Manager / Process Hacker / System (PID 4) / smss.exe / csrss.exe / wininit.exe / winlogon.exe / lsass.exe / lsaiso.exe / services.exe / svchost.exe / userinit.exe | Entender el comportamiento normal de los procesos esenciales de Windows para poder identificar procesos maliciosos o sospechosos en un endpoint durante la monitorización de seguridad. |

---

**Contexto:** Sala de nivel SOC/defensa donde se exploran los procesos núcleo de un sistema Windows y qué se considera comportamiento normal. El objetivo es conocer qué proceso debe existir siempre, con qué PID, a quién pertenece y qué relaciones de parentesco tiene, de forma que un analista detecte anomalías (procesos ocultos, dobles extensiones, padres inusuales) cuando un adversario se mueve por el endpoint.

> **ES:** "Explora los procesos núcleo dentro del sistema operativo Windows y entiende qué es un comportamiento normal. Este conocimiento fundamental te ayudará a identificar procesos maliciosos ejecutándose en un endpoint."
> **EN:** "Explore the core processes within a Windows operating system and understand what normal behaviour is. This foundational knowledge will help you identify malicious processes running on an endpoint!"

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Task de entrada: se lee la introducción de la sala y se despliega la máquina virtual asociada. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la introducción y he desplegado la máquina virtual. / I've read the intro and deployed the attached virtual machine. | `No answer needed` |

---

### Task 2: ¿Qué es un proceso? / What is a Process?

**Explicación:** Se introducen los conceptos de proceso, hilo, imagen y estado de un proceso en Windows, junto a las herramientas (Task Manager, Process Hacker 2, Process Explorer, Procmon) que se usan para inspeccionarlos. Task de solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continúa con la siguiente tarea. / On to the next task. | `No answer needed` |

---

### Task 3: ¿Qué PID debería tener siempre System? / What PID should System always be?

**Explicación:** En Windows, el proceso `System` (el kernel) es uno de los primeros en arrancar y su PID está fuertemente asociado con el PID 4, por lo que un `System` con un PID distinto al esperado es una señal de alarma.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué PID debería tener siempre System? / What PID should System always be? | `4` |

---

### Task 4: Procesos de logon / Logon Processes (winlogon.exe)

**Explicación:** `winlogon.exe` (Windows Logon Manager) gestiona el proceso de inicio y cierre de sesión de los usuarios: intercepta la secuencia de atención segura (Ctrl+Alt+Supr), gestiona el inicio de sesión interactivo y lanza el shell del usuario (`userinit.exe`). Su imagen debe residir siempre en `%SystemRoot%\System32`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso gestiona el inicio y cierre de sesión del usuario (secure attention sequence)? / Which process manages user logon/logoff (secure attention sequence)? | `winlogon.exe` |

---

### Task 5: SMSS / Session Manager Subsystem (smss.exe)

**Explicación:** `smss.exe` es el primer proceso en modo usuario que arranca el kernel. Es responsable de crear nuevas sesiones, iniciar los procesos de entorno (variables, archivos de paginación) y arrancar `csrss.exe` con `wininit.exe` en la Session 0 y `csrss.exe` con `winlogon.exe` en la Session 1. En el análisis del lab, este proceso aparece con PIDs como 384 y 488.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso tenía los PIDs 384 y 488 en el análisis del lab? / What was the process which had PID 384 and PID 488? | `smss.exe` |

---

### Task 6: LSAISO / Credential Guard (lsaiso.exe)

**Explicación:** `lsaiso.exe` (LSA Isolated) es parte de Credential Guard: aísla las credenciales en un proceso aislado que se ejecuta fuera de `lsass.exe`. Si Credential Guard no está habilitado, `lsaiso.exe` no debería aparecer, por lo que verlo puede indicar que la característica de seguridad está activa, mientras que su ausencia es normal en máquinas sin Credential Guard.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso podría no verse ejecutándose si Credential Guard no está habilitado? / Which process might you not see running if Credential Guard is not enabled? | `lsaiso.exe` |

---

### Task 7: Sesiones de los procesos de logon / Sessions of the logon processes

**Explicación:** Los procesos de logon del usuario interactivo se ejecutan en la Session 1 (sesión de usuario), mientras que la Session 0 queda aislada para los servicios del sistema. Esa distinción es la que permite separar los procesos del sistema de los del usuario conectado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué sesión (Session) se ejecutan los procesos de logon del usuario? / In which session do the user logon processes run? | `1` |

---

### Task 8: Inspección de procesos / Inspecting processes

**Explicación:** Al inspeccionar el árbol de procesos con la herramienta del lab (Process Hacker / Task Manager) se observan las propiedades de cada proceso: imagen, parent process, PID, sesión, etc. La opción correcta seleccionada en el ejercicio corresponde a la respuesta siguiente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | De las opciones mostradas en el ejercicio, ¿cuál es la correcta? / Which of the options shown in the exercise is correct? | `k` |

---

### Task 9: WININIT / Windows Initialization Process (wininit.exe)

**Explicación:** `wininit.exe` es el proceso de inicialización de Windows que se lanza en la Session 0 y es el responsable de arrancar `services.exe` (Service Control Manager), `lsass.exe` (Local Security Authority) y `lsaiso.exe`. Su imagen debe estar en `%SystemRoot%\System32` y su proceso padre es `smss.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso es responsable de lanzar services.exe, lsass.exe y lsaiso.exe? / Which process is responsible for launching services.exe, lsass.exe and lsaiso.exe? | `wininit.exe` |

---

### Task 10: Creación de sesiones / Session creation (smss.exe)

**Explicación:** `smss.exe` se copia a sí mismo en cada nueva sesión y se autotermina, dejando que la instancia hija arranque los procesos correspondientes de esa sesión. Por eso cada instancia de SMSS controla una sesión concreta y su comportamiento es distinto al de otros procesos persistentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso se copia a sí mismo en la nueva sesión y se autotermina (self-terminating)? / Which process copies itself into the new session and self-terminates? | `smss.exe` |

---

### Task 11: USERINIT (userinit.exe)

**Explicación:** `winlogon.exe` ejecuta `userinit.exe`, que lanza el valor de `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell` (normalmente `explorer.exe`). Tras lanzar el shell, `userinit.exe` termina, por lo que el proceso padre de `explorer.exe` suele aparecer como inexistente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso lanza explorer.exe tras el inicio de sesión y luego termina (por eso su padre no existe)? / What process launches explorer.exe after logon and then exits (so its parent is non-existent)? | `userinit.exe` |

---

### Task 12: Conclusión / Conclusion

**Explicación:** Resumen de la sala: conocer los procesos núcleo de Windows y su comportamiento normal es la base para detectar procesos anómalos o maliciosos en el endpoint. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He anotado los conceptos clave de la sala. / I've taken note of the key concepts. | `No answer needed` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Introducción. / Introduction. | `No answer needed` |
| 2 | Task 2 | ¿Qué es un proceso? / What is a Process? | `No answer needed` |
| 3 | Task 3 | ¿Qué PID debería tener siempre System? / What PID should System always be? | `4` |
| 4 | Task 4 | ¿Qué proceso gestiona el inicio/cierre de sesión? / Which process manages logon/logoff? | `winlogon.exe` |
| 5 | Task 5 | ¿Qué proceso tenía los PIDs 384 y 488? / What was the process which had PID 384 and PID 488? | `smss.exe` |
| 6 | Task 6 | ¿Qué proceso no aparece si Credential Guard está deshabilitado? / Which process might you not see if Credential Guard is not enabled? | `lsaiso.exe` |
| 7 | Task 7 | ¿En qué sesión se ejecutan los procesos de logon? / In which session do logon processes run? | `1` |
| 8 | Task 8 | ¿Cuál es la opción correcta del ejercicio? / Which option is correct? | `k` |
| 9 | Task 9 | ¿Qué proceso lanza services.exe, lsass.exe y lsaiso.exe? / Which process launches services.exe, lsass.exe and lsaiso.exe? | `wininit.exe` |
| 10 | Task 10 | ¿Qué proceso se copia a sí mismo y se autotermina? / Which process copies itself and self-terminates? | `smss.exe` |
| 11 | Task 11 | ¿Qué proceso lanza explorer.exe tras el logon? / What process launches explorer.exe after logon? | `userinit.exe` |
| 12 | Task 12 | Conclusión. / Conclusion. | `No answer needed` |

---

**Metodología:** Revisar en la máquina desplegada cada uno de los procesos núcleo con el Administrador de tareas o Process Hacker, comprobando PID, imagen, sesión y relación de parentesco. Para cada proceso se verifica el comportamiento normal (ruta `System32`, padre esperado, PID esperado) y se conecta cada dato con la sección teórica de la sala: System (PID 4), smss (creador de sesiones), winlogon/wininit (logon e inicialización), lsaiso (Credential Guard) y userinit (lanzador del shell).

### Cadena de ataque / Attack Chain

```text
Leer la teoría de la sala -> desplegar la VM -> abrir Task Manager / Process Hacker -> identificar System (PID 4) -> repasar smss.exe -> wininit.exe -> winlogon.exe -> lsass.exe -> lsaiso.exe -> services.exe -> svchost.exe -> userinit.exe -> responder cada tarea con el proceso/sesión correcto
```

**Learning chain:** procesos e hilos -> Session 0 / Session 1 -> System (PID 4) -> smss -> csrss -> wininit -> winlogon -> lsass/lsaiso -> services/svchost -> userinit/explorer -> baseline de comportamiento normal.

**Lección:** *Conocer el baseline (PID, ruta, padre, sesión) de los procesos núcleo de Windows es lo que permite a un analista detectar un proceso anómalo antes de que sea demasiado tarde.*

**MITRE ATT&CK:** N/A (sala defensiva de fundamentos; relevante para detección de T1036 - Masquerading y T1204 en procesos de usuario)

**Fuente:** [TryHackMe - Core Windows Processes](https://tryhackme.com/room/corewindowsprocesses)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.