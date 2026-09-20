# Linux Fundamentals (Pt 1)

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | linuxfundamentalspt15vm | [TryHackMe](https://tryhackme.com/room/linuxfundamentalspt15vm) | Linux | THM | whoami, echo, ls, cat, grep, Shell operators, Redirectors | Fundamentos Linux |

---

**Contexto:** Room introductorio a los comandos básicos de Linux, cubriendo identidad del usuario, navegación del sistema de archivos, búsqueda de texto y operadores de shell.

> **ES:**
> - Comando para saber quién somos
> - Comando para imprimir texto
> - Ejecutar ls - ¿Cuántas carpetas hay?
> - ¿Qué carpeta contiene un archivo?
> - Ejecutar cat sobre el archivo - ¿Qué dice?
> - grep THM access.log - ¿Qué flag se encontró?
> - Operador que espera a que termine el primer comando antes de ejecutar el siguiente
> - Redireccionador que guarda salida SIN sobreescribir el archivo

## Solucionario

### Task 2: Hablando con Linux / Talking to Linux

**Explicación:** Primera interacción con la terminal: se identifica al usuario actual con `whoami` y se imprime texto en pantalla con `echo`, comprendiendo que la shell interpreta comandos.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Comando para saber quién somos | `whoami` |
| 2 | Comando para imprimir texto | `echo` |

> **Explicación ES (original):** Comando para saber quién somos → `whoami`: Retorna el nombre del usuario actual en el sistema. Comando para imprimir texto → `echo`: Muestra en terminal el texto proporcionado como argumento.

### Task 3: Encontrando tu camino / Finding Your Way Around

**Explicación:** Navegación por el sistema de archivos con `ls` para enumerar directorios y con `cat` para leer el contenido de archivos dentro de un directorio determinado.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Ejecutar ls - ¿Cuántas carpetas hay? | `4` |
| 2 | ¿Qué carpeta contiene un archivo? | `folder4` |
| 3 | Ejecutar cat sobre el archivo - ¿Qué dice? | `Hello World` |

### Task 4: Deja que la máquina busque / Let the Machine Do the Searching

**Explicación:** Uso de `grep` para buscar un patrón de texto dentro de archivos de log, encontrando una flag oculta en `access.log`.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | grep THM access.log - ¿Qué flag se encontró? | `THM{ACCESS}` |

### Task 5: Operadores de Shell / Shell Operators

**Explicación:** Operadores y redireccionadores de la shell: `&&` encadena comandos de forma que el segundo solo se ejecuta si el primero tiene éxito; `>>` anexa la salida a un archivo existente sin sobrescribirlo.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Operador que espera a que termine el primer comando antes de ejecutar el siguiente | `&&` |
| 2 | Redireccionador que guarda salida SIN sobreescribir el archivo | `>>` |

---

**Metodología:** Se interactúa con la shell para identificar al usuario actual (`whoami`) y reproducir texto (`echo`). Con `ls` se enumeran los directorios y se descubre que `folder4` contiene un archivo cuyo contenido se lee con `cat`. Se emplea `grep` para buscar el patrón `THM` en `access.log` y obtener `THM{ACCESS}`. Finalmente se practican operadores de control (`&&`) y redireccionamiento de salida (`>>`) para manejar el flujo de los comandos.

### Cadena de ataque / Attack Chain

Identidad del usuario → impresión de texto → enumeración de directorios → lectura de archivos → búsqueda con grep → operadores y redireccionadores

**Learning chain:** whoami → echo → ls → cat → grep → && → >>

**Lección:** *Los fundamentos de Linux (identidad, navegación, búsqueda y operadores de shell) son la base sobre la que se construye cualquier tarea ofensiva o defensiva posterior.*

**MITRE ATT&CK:** T1059.004 (Unix Shell), T1083 (File and Directory Discovery), T1106 (Native API)

**Fuente:** [TryHackMe - Linux Fundamentals (Pt 1)](https://tryhackme.com/room/linuxfundamentalspt15vm)

> **Fuente original / Original source:** https://electronicsreference.com/thm/linux_fundamentals_pt1/ | https://github.com/thmrevenant/tryhackme/blob/main/rooms/linux%20fundamentals%20part%201.txt

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.