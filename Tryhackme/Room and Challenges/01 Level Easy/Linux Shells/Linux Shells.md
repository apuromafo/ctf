# Linux Shells

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | linuxshells | [TryHackMe](https://tryhackme.com/room/linuxshells) | 01 Level Easy | THM | Shell, Bash, Fish, ls, grep, history, shebang, chmod +x, loops, authentication.log | Concepto y uso de las shells de Linux, scripting básico con shebang y automatización mediante bucles |

---

**Contexto:** Sala introductoria a las shells de Linux: qué son, los distintos tipos disponibles (Bash, Fish), comandos esenciales (`ls`, `grep`), el historial de la shell, el shebang en scripts (`#!/bin/bash`), permisos de ejecución (`chmod +x`) y estructuras de control como los bucles.

> **EN:**
> 1. Shell
> 2. 1. Bash
>    2. ls
>    3. grep
> 3. 1. Fish
>    2. Bash
>    3. history
> 4. 1. #!/bin/bash
>    2. chmod +x
>    3. loops
> 5. 7385
> 6. 1. authentication.log
>    2. under the table
> 7. No answer needed

## Solucionario

### Task 1: ¿Qué es una shell? / What is a shell?

**Explicación:** Se introduce el concepto de shell como el programa que interpreta y ejecuta los comandos escritos por el usuario en el terminal.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué programa interpreta los comandos del usuario? / Which program interprets the user's commands? | `Shell` |

### Task 2: Shells comunes y comandos / Common shells and commands

**Explicación:** Se exploran las shells más comunes en Linux (destacando Bash) y comandos básicos: `ls` para listar archivos y `grep` para filtrar texto.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuál es la shell más común en Linux? / Which is the most common shell in Linux? | `Bash` |
| 2 | Comando que lista los archivos de un directorio / Command that lists the files in a directory | `ls` |
| 3 | Comando que busca patrones dentro de archivos / Command that searches for patterns in files | `grep` |

### Task 3: Otras shells y el historial / Other shells and the history

**Explicación:** Se comparan shells alternativas como Fish frente a Bash y se repasa el uso del historial (`history`) para recuperar comandos ejecutados previamente.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué otra shell destaca por su experiencia de uso? / Which other shell stands out for its user experience? | `Fish` |
| 2 | ¿Qué shell se usa como referencia en el ejercicio? / Which shell is used as the reference in the exercise? | `Bash` |
| 3 | ¿Qué comando muestra los comandos ejecutados anteriormente? / Which command shows previously executed commands? | `history` |

### Task 4: Scripts y ejecución / Scripts and execution

**Explicación:** Se explica la creación de scripts: el shebang `#!/bin/bash` indica el intérprete, `chmod +x` otorga permiso de ejecución y los bucles (`loops`) permiten automatizar tareas repetitivas.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué primera línea declara el intérprete de un script? / Which first line declares the interpreter of a script? | `#!/bin/bash` |
| 2 | ¿Qué comando hace ejecutable un script? / Which command makes a script executable? | `chmod +x` |
| 3 | ¿Qué estructura de control repite un bloque de código? / Which control structure repeats a block of code? | `loops` |

### Task 5: Análisis de una salida / Analyzing an output

**Explicación:** Se interpreta el resultado de un comando de análisis, fijándose en el valor numérico que responde a la pregunta planteada.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué valor numérico se obtiene del análisis? / What numeric value is obtained from the analysis? | `7385` |

### Task 6: Logs de autenticación / Authentication logs

**Explicación:** Se inspecciona el log de autenticación del sistema (`authentication.log`) buscando patrones de actividad sospechosa, y se responde con la frase localizada en la evidencia.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué archivo de log guarda los eventos de autenticación? / Which log file stores authentication events? | `authentication.log` |
| 2 | ¿Qué frase se encuentra en el log? / What phrase is found in the log? | `under the table` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala: se repasan los conceptos de shell, scripting y logs vistos a lo largo del recorrido.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Comprender que la shell es el intérprete de comandos. Comparar shells disponibles (Bash, Fish) y practicar comandos esenciales (`ls`, `grep`) y el historial (`history`). Para el scripting se escribe un script con shebang `#!/bin/bash`, se otorga permiso de ejecución con `chmod +x` y se estructuran bucles para automatizar. Por último, se aplica `grep` sobre `authentication.log` para localizar actividad sospechosa (frase `under the table`).

### Cadena de ataque / Attack Chain

Concepto de shell → comparación de shells (Bash/Fish) → comandos esenciales (`ls`, `grep`) → historial → escritura de scripts (`#!/bin/bash`) → permisos (`chmod +x`) → bucles → análisis de logs de autenticación

**Learning chain:** Shell → Bash → ls → grep → Fish → history → #!/bin/bash → chmod +x → loops → authentication.log → under the table

**Lección:** *Dominar la shell y el scripting (`shebang`, `chmod +x`, bucles) es la base de la automatización en Linux; saber manejar el historial y los logs de autenticación permite tanto acelerar tareas como detectar actividad no autorizada.*

**MITRE ATT&CK:** T1059.004 (Unix Shell), T1082 (System Information Discovery), T1083 (File and Directory Discovery), T1055 (Process Injection)

**Fuente:** [TryHackMe - Linux Shells](https://tryhackme.com/room/linuxshells)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.