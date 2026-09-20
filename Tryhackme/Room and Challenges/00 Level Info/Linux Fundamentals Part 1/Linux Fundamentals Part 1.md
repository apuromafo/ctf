# Linux Fundamentals Part 1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `linuxfundamentalspart1` | [TryHackMe](https://tryhackme.com/room/linuxfundamentalspart1) | 00 Level Info | TryHackMe | Linux, SSH, comandos básicos, sistema de archivos, permisos, redirección | Primeros pasos en Linux: conexión, comandos básicos, sistema de archivos, permisos y redirección |

---

**Contexto:** Sala de iniciación a Linux: selección del servidor, contexto histórico del kernel, conexión por SSH, primeros comandos (echo), el sistema de archivos de Linux, los permisos y la redirección de entrada/salida. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Selección de un servidor / Selecting a Server

**Explicación:** Pregunta de arranque de la sala sobre la elección del servidor Linux, sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Introducción a Linux / Intro to Linux

**Explicación:** Se presenta la historia de Linux; la primera versión del kernel fue lanzada en el año `1991`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `1991` |

### Task 3: Interactuar con la primera máquina Linux / Interacting with Your First Linux Machine

**Explicación:** Tarea de conexión y familiarización con la primera máquina Linux (SSH), sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 4: Comandos básicos / Basic Commands

**Explicación:** Se practican los comandos básicos de Linux: la salida de texto se consigue con `echo TryHackMe` y se demuestra que los comandos son sensibles a mayúsculas y minúsculas con `tryhackme`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `echo TryHackMe` |
| 2 | *(Pregunta 2 no especificada en el original)* | `tryhackme` |

### Task 5: El sistema de archivos de Linux / The Linux Filesystem

**Explicación:** Se explora el sistema de archivos de Linux: en el directorio personal existen `4` carpetas, la cuarta se llama `folder4`, al leer su archivo se obtiene `Hello World` y su ruta absoluta es `/home/tryhackme/folder4`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `4` |
| 2 | *(Pregunta 2 no especificada en el original)* | `folder4` |
| 3 | *(Pregunta 3 no especificada en el original)* | `Hello World` |
| 4 | *(Pregunta 4 no especificada en el original)* | `/home/tryhackme/folder4` |

### Task 6: Permisos 101 / Permissions 101

**Explicación:** Se introducen los permisos de Linux: la flag `THM{ACCESS}` confirma el acceso conseguido; la segunda parte de la tarea no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{ACCESS}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |

### Task 7: Redirección / Redirection

**Explicación:** Se estudia la redirección de entrada/salida en Linux: el operador para redirigir es `&`, `echo password123 > passwords` sobrescribe un archivo y `echo tryhackme >> passwords` añade contenido al final; la última parte no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `&` |
| 2 | *(Pregunta 2 no especificada en el original)* | `echo password123 > passwords` |
| 3 | *(Pregunta 3 no especificada en el original)* | `echo tryhackme >> passwords` |
| 4 | *(Pregunta 4 no especificada en el original)* | `No answer needed` |

### Task 8: Repaso / Review

**Explicación:** Tarea de repaso de los conceptos vistos hasta el momento, sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 9: Conclusión / Conclusion

**Explicación:** Cierre de la sala; ninguna de sus partes requiere respuesta. Respuestas originales: `No answer needed`, `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `1991` |
| 3 | *(Task 3, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 4 | *(Task 4, Pregunta 1 no especificada en el original)* | `echo TryHackMe` |
| 5 | *(Task 4, Pregunta 2 no especificada en el original)* | `tryhackme` |
| 6 | *(Task 5, Pregunta 1 no especificada en el original)* | `4` |
| 7 | *(Task 5, Pregunta 2 no especificada en el original)* | `folder4` |
| 8 | *(Task 5, Pregunta 3 no especificada en el original)* | `Hello World` |
| 9 | *(Task 5, Pregunta 4 no especificada en el original)* | `/home/tryhackme/folder4` |
| 10 | *(Task 6, Pregunta 1 no especificada en el original)* | `THM{ACCESS}` |
| 11 | *(Task 6, Pregunta 2 no especificada en el original)* | `No answer needed` |
| 12 | *(Task 7, Pregunta 1 no especificada en el original)* | `&` |
| 13 | *(Task 7, Pregunta 2 no especificada en el original)* | `echo password123 > passwords` |
| 14 | *(Task 7, Pregunta 3 no especificada en el original)* | `echo tryhackme >> passwords` |
| 15 | *(Task 7, Pregunta 4 no especificada en el original)* | `No answer needed` |
| 16 | *(Task 8, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 17 | *(Task 9, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 18 | *(Task 9, Pregunta 2 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Seleccionar y desplegar el servidor Linux → conocer la historia del kernel → conectar por SSH a la máquina → practicar comandos básicos (echo) → explorar el sistema de archivos y las rutas absolutas → revisar los permisos → practicar la redirección de entrada y salida → repasar y cerrar con la conclusión.

### Cadena de ataque / Attack Chain

```text
servidor Linux → SSH → echo (mayúsculas/minúsculas) → filesystem (folder4, /home/tryhackme/folder4) → permisos (THM{ACCESS}) → redirección (&, >, >>) → flag THM{...}
```

**Learning chain:** Selección del servidor → historia de Linux → conexión SSH → comandos básicos → sistema de archivos → permisos → redirección → conclusiones

**Lección:** *Los fundamentos de Linux no son teoría abstracta: la práctica inmediata de comandos, rutas y redirección sobre una máquina real es lo que transforma la sintaxis en reflejo operativo.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1070 (Indicator Removal on Host - redirección)

**Fuente:** [TryHackMe - Linux Fundamentals Part 1](https://tryhackme.com/room/linuxfundamentalspart1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.