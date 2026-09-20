# Empire

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `empire` | [TryHackMe](https://tryhackme.com/room/empire) | 01 Level Easy | TryHackMe | Empire / Starkiller / C2 / agents / listeners / modules / post-exploitation / mimikatz / keylogger | Comprender el funcionamiento de un framework de post-explotación (C2) y sus módulos. |

> **Objeto:** Aprender a usar Empire y su GUI Starkiller, un framework de post-explotación (C2): generar launcher/stagers, crear listeners, dar de alta agents, interactuar con ellos y ejecutar módulos como mimikatz o el keylogger de PowerShell.

---

**Contexto:** Empire es un framework de post-explotación y Agents de ratka (C2) que se controla desde una consola o desde Starkiller (su GUI). La room guía por el flujo completo: instalación, staging (generación de payloads/launcher), creación de listeners, creación de agents en las máquinas objetivo, interacción con esos agents y ejecución de módulos para robar credenciales (mimikatz) o capturar teclado (keylogger).

> **ES:** Room práctica del framework Empire/Starkiller. Se recorre: overview del framework, instalación, generación de launcher (stager), creación de listeners (por defecto http 0.0.0.0:8080), creación de agents en la máquina objetivo y ejecución de módulos. En la tarea de "Weaponising" se usan los módulos powershell/credentials/mimikatz/command (T1491) y powershell/collection/keylogger (T1056). Las tareas son guiadas: casi todo responde "No answer needed"; las respuestas reales están solo en la tarea de módulos.
> **EN:** Hands-on Empire/Starkiller room. It walks through: framework overview, installation, launcher/stager generation, creating listeners (default http 0.0.0.0:8080), creating agents on the target machine, and module execution. In the "Weaponising" task the powershell/credentials/mimikatz/command (T1491) and powershell/collection/keylogger (T1056) modules are used. Tasks are guided: almost everything is "No answer needed"; the real answers are only in the modules task.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación del framework Empire y de la room: qué es un C2 y qué se va a practicar. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

### Task 2: Descripción general de Empire / Empire Overview
**Explicación:** Muestra qué es Empire y su flujo de trabajo (stagers, listeners, agents). Tarea de lectura: no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |
| 2 | Follow the steps described. / Sigue los pasos descritos. | `No answer needed` |

### Task 3: Instalando Empire / Installing Empire
**Explicación:** Instalación y puesta en marcha de Empire (e instalación de Starkiller, la GUI). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Follow the installation steps. / Sigue los pasos de instalación. | `No answer needed` |

### Task 4: Staging: generando payloads / Staging: Generating Payloads
**Explicación:** Generación del launcher (stager) que se ejecutará en la máquina víctima y contactará con el listener. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Generate a launcher using the default settings. / Genera un launcher con los ajustes por defecto. | `No answer needed` |

### Task 5: Creando listeners / Creating Listeners
**Explicación:** Creación del listener HTTP (por defecto 0.0.0.0:8080) que esperará las conexiones de los agents. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Create a listener using the default settings. / Crea un listener con los ajustes por defecto. | `No answer needed` |

### Task 6: Creando agents / Creating Agents
**Explicación:** Deploy del launcher en la máquina del laboratorio para que se registre como agent en el C2. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy an agent. / Despliega un agent. | `No answer needed` |
| 2 | Interact with the agent. / Interactúa con el agent. | `No answer needed` |

### Task 7: Interactuando con los agents / Interacting with Agents
**Explicación:** La interacción con el agent permite lanzar comandos y ejecutar módulos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Interact with the agent and execute a command. / Interactúa con el agent y ejecuta un comando. | `No answer needed` |

### Task 8: Weaponising: Mimikatz y Keylogger / Weaponising: Mimikatz & Keylogger
**Explicación:** Se usan dos módulos de post-explotación de Empire: powershell/credentials/mimikatz/command, que permite ejecutar mimikatz contra el agent para volcar credenciales (técnica T1491 según los metadatos del módulo), y powershell/collection/keylogger, que captura las pulsaciones de teclado de la víctima (técnica T1056, Input Capture). El módulo de mimikatz se ejecuta con el comando siguiente (o el indicado en el laboratorio) y el flujo termina probando ambos sobre el agent.

```bash
usemodule powershell/credentials/mimikatz/command
usemodule powershell/collection/keylogger
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What module would you use to run a command with mimikatz? / ¿Qué módulo usarías para ejecutar un comando con mimikatz? | `powershell/credentials/mimikatz/command` |
| 2 | What is the MITRE ATT&CK Technique ID associated with the module? / ¿Cuál es el ID de técnica MITRE ATT&CK del módulo? | `T1491` |
| 3 | What module would you use to log keystrokes on the target? / ¿Qué módulo usarías para registrar las teclas del objetivo? | `powershell/collection/keylogger` |
| 4 | What is the MITRE ATT&CK Technique ID for the keystroke logger? / ¿Cuál es el ID de técnica MITRE ATT&CK del keylogger? | `T1056` |
| 5 | Run the mimikatz module and the keylogger against your agent. / Ejecuta el módulo de mimikatz y el keylogger contra tu agent. | `No answer needed` |

### Task 9: Conclusión / Conclusion
**Explicación:** Resumen de lo aprendido: cómo funciona un C2 con Empire y Starkiller. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

### Task 10: Cierre / Wrapping up
**Explicación:** Cierre de la room con repaso de los conceptos (C2, agents, listeners, módulos).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What module would you use to run a command with mimikatz? | `powershell/credentials/mimikatz/command` |
| 2 | What is the MITRE ATT&CK Technique ID associated with the module? | `T1491` |
| 3 | What module would you use to log keystrokes on the target? | `powershell/collection/keylogger` |
| 4 | What is the MITRE ATT&CK Technique ID for the keystroke logger? | `T1056` |
| 5 | Run the mimikatz module and the keylogger against your agent. | `No answer needed` |

---

**Metodología:** Se despliega Empire y Starkiller, se genera un launcher para la máquina víctima, se crea un listener HTTP y se registra un agent. Con el agent activo se ejecutan módulos de la consola de Empire: powershell/credentials/mimikatz/command para dumpear credenciales (T1491) y powershell/collection/keylogger para capturar teclado (T1056), completando el flujo de post-explotación.

### Cadena de ataque / Attack Chain

```text
Empire + Starkiller -> generación de launcher (stager) -> creación de listener HTTP -> ejecución en la víctima -> agent registrado en el C2 -> interacción -> module mimikatz (credenciales, T1491) -> module keylogger (T1056)
```

**Learning chain:** Empire Overview → Installing Empire → Staging (launchers) → Creating Listeners → Creating Agents → Interacting with Agents → Weaponising (Mimikatz & Keylogger).

**Lección:** *Un framework C2 como Empire centraliza la post-explotación: listeners, agents y módulos (mimikatz, keylogger) permiten moverte y robar credenciales de forma remota; para el defensor, detectar la actividad de stagers/agents y vigilar los procesos PowerShell que cargan estos módulos es clave.*

**MITRE ATT&CK:** T1491 (Defacement - metadatos del módulo de mimikatz), T1056 (Input Capture - keylogger), T1003 (OS Credential Dumping - mimikatz)

**Fuente:** [TryHackMe - Empire](https://tryhackme.com/room/empire)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.