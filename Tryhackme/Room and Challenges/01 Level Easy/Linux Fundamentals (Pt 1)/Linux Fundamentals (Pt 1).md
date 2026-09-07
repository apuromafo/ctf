# Linux Fundamentals (Pt 1)

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `linuxfundamentalspt15vm` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/linuxfundamentalspt15vm) |
| **Sección** | Linux |
| **Fuente** | THM |
| **Componentes** | whoami, echo, ls, cat, grep, Shell operators, Redirectors |
| **Impacto** | Fundamentos Linux |

---

**Contexto:** Room introductorio a los comandos básicos de Linux, cubriendo identidad del usuario, navegación del sistema de archivos, búsqueda de texto y operadores de shell.

## Solucionario

### T2 - Talking to Linux

| Pregunta | Respuesta | Explicación ES |
|----------|-----------|----------------|
| Comando para saber quién somos | whoami | Retorna el nombre del usuario actual en el sistema |
| Comando para imprimir texto | echo | Muestra en terminal el texto proporcionado como argumento |

### T3 - Finding Your Way Around

| Pregunta | Respuesta |
|----------|-----------|
| Ejecutar ls - ¿Cuántas carpetas hay? | 4 |
| ¿Qué carpeta contiene un archivo? | folder4 |
| Ejecutar cat sobre el archivo - ¿Qué dice? | Hello World |

### T4 - Let the Machine Do the Searching

| Pregunta | Respuesta |
|----------|-----------|
| grep THM access.log - ¿Qué flag se encontró? | THM{ACCESS} |

### T5 - Shell Operators

| Pregunta | Respuesta |
|----------|-----------|
| Operador que espera a que termine el primer comando antes de ejecutar el siguiente | && |
| Redireccionador que guarda salida SIN sobreescribir el archivo | >> |

---

**Fuentes:** https://electronicsreference.com/thm/linux_fundamentals_pt1/ | https://github.com/thmrevenant/tryhackme/blob/main/rooms/linux%20fundamentals%20part%201.txt
