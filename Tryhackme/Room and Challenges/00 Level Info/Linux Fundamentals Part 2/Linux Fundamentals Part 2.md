# Linux Fundamentals Part 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Info | Walkthrough | `linuxfundamentalspart2` | https://tryhackme.com/room/linuxfundamentalspart2 | 00 Level Info | TryHackMe | Linux / terminal / man pages / manipulación de archivos / usuarios y su / logs y directorios del sistema | Fundamento esencial de Linux: navegación en terminal, páginas del manual, creación y movimiento de archivos, gestión de usuarios con `su`, procesos y logs |

---

**Contexto:** Segunda parte del curso introductorio de Linux de TryHackMe. Continúa donde acabó la primera parte y cubre, de forma práctica sobre una máquina desplegada, la navegación por la terminal, el uso de las páginas del manual y la ayuda por terminal, la creación y manipulación de archivos y carpetas, la gestión de usuarios y el cambio entre usuarios con `su`, así como el logging, los directorios del sistema y un cierre de la sala.

> **ES:** Se practica sobre una máquina Linux real la terminal: man pages, creación y movimiento de archivos, creación de usuarios y el comando `su`, finalizando con procesos, logs y directorios del sistema.
> **EN:** Practice on a real Linux machine: man pages, creating and moving files, adding users and the `su` command, finishing with processes, logs and system directories.

## Solucionario

### Task 1: Acceso a tu primera máquina Linux / Accessing Your First Linux Machine

**Explicación:** La sala despliega una máquina virtual Linux. La primera tarea es introductoria: arrancar el entorno y leer la información que da comienzo al recorrido. No hay pregunta que responder, de ahí que el valor original sea "No answer needed".

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desplegar la máquina y leer la información. / Deploy the machine and read the information. | No answer needed |

### Task 2: Conectarse a la máquina / Connecting to the machine

**Explicación:** La tarea explica cómo acceder al entorno, normalmente mediante SSH, y comprobar que la sesión responde. Solo requiere realizar el paso de conexión y verificar el acceso; por eso el valor original es "No answer needed".

```text
2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conectarse a la máquina desplegada. / Connect to the deployed machine. | No answer needed |

### Task 3: Páginas de manual y ayuda / Man pages and help

**Explicación:** La tarea presenta las páginas del manual y la ayuda integrada de los comandos. Para recorrer de forma interactiva una página larga se utiliza la tecla de flecha hacia abajo (`down`) y, para obtener información de ayuda de un comando, se usa el flag `-h`. El primer punto es de lectura pura.

```text
3. 1. No answer needed
   2. down
   3. -h
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea. / Read the task information. | No answer needed |
| 2 | ¿Cómo se baja una página dentro de la ayuda/man page? / How would you move down a page inside the man page/help? | `down` |
| 3 | ¿Qué flag se añade a un comando para mostrar su ayuda? / What flag do you add to a command to show its help? | `-h` |

### Task 4: Manipulación de archivos y carpetas / Working with files and folders

**Explicación:** La tarea practica la creación y movimiento de archivos. `touch` crea un archivo nuevo, `file` identifica el tipo de un archivo (`ASCII text`), y `mv` lo mueve a otra carpeta. Con ello se obtiene la flag que confirma la comprensión del sistema de archivos.

```text
4. 1. touch newnote
   2. ASCII text
   3. mv myfile myfolder
   4. THM{FILESYSTEM}
   5. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se crea el archivo llamado "newnote"? / How would you create the file named "newnote"? | `touch newnote` |
| 2 | ¿Qué tipo de archivo es "myfile"? / What type of file is "myfile"? | `ASCII text` |
| 3 | ¿Cómo se mueve el archivo "myfile" a la carpeta "myfolder"? / How would you move "myfile" to the "myfolder" directory? | `mv myfile myfolder` |
| 4 | ¿Cuál es la flag de la tarea? / What is the flag of this task? | `THM{FILESYSTEM}` |
| 5 | Leer la información de la tarea. / Read the task information. | No answer needed |

### Task 5: Añadir usuarios y cambio de usuario / Adding users and su

**Explicación:** La tarea cubre la gestión de usuarios en Linux: se crea el usuario `user2` y se cambia a esa cuentra con `su user2`. Tras explorar la sesión del nuevo usuario se obtiene una flag que acredita el cambio de usuario completado.

```text
5. 1. user2
   2. su user2
   3. No answer needed
   4. THM{SU_USER2}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuario se crea/emplea en la tarea? / What user is created/used in this task? | `user2` |
| 2 | ¿Cómo se cambia a ese usuario? / How do you switch to that user? | `su user2` |
| 3 | Leer la información de la tarea. / Read the task information. | No answer needed |
| 4 | ¿Cuál es la flag de la tarea? / What is the flag of this task? | `THM{SU_USER2}` |

### Task 6: Logging y directorios del sistema / Logging and system directories

**Explicación:** La tarea describe la estructura de directorios del sistema. Los registros (logs) se almacenan en `/var/log`, los archivos temporales en `/tmp`, y el directorio personal del usuario root es `/root`. Los apartados primero y último son de lectura.

```text
6. 1. No answer needed
   2. /var/log
   3. /tmp
   4. /root
   5. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea. / Read the task information. | No answer needed |
| 2 | ¿Cuál es la ruta completa del directorio de logs? / What is the full path to the log directory? | `/var/log` |
| 3 | ¿Dónde se guardan los archivos temporales? / Where are temporary files stored? | `/tmp` |
| 4 | ¿Cuál es el directorio home del usuario root? / What is the root user's home directory? | `/root` |
| 5 | Leer la información de la tarea. / Read the task information. | No answer needed |

### Task 7: Procesos 101 / Processes 101

**Explicación:** Introducción conceptual a los procesos de Linux: qué es un proceso, cómo verlos y cómo gestionarlos. La tarea es de lectura únicamente y no exige respuesta, así que el valor original es "No answer needed".

```text
7. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea. / Read the task information. | No answer needed |

### Task 8: Cierre de la sala / End of room

**Explicación:** Cierre del recorrido: repaso de lo aprendido y transición hacia la siguiente parte del curso. Ambas entradas son de lectura pura, por lo que se marcan como "No answer needed".

```text
8. 1. No answer needed
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Terminar la sala y repasar el contenido. / Finish the room and review the content. | No answer needed |
| 2 | Leer la conclusión de la sala. / Read the conclusion of the room. | No answer needed |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desplegar la máquina y leer la información. / Deploy the machine and read the information. | No answer needed |
| 2 | Conectarse a la máquina desplegada. / Connect to the deployed machine. | No answer needed |
| 3 | Leer la información de la Task 3. / Read the Task 3 information. | No answer needed |
| 4 | ¿Cómo se baja una página dentro de la ayuda/man page? / How would you move down a page inside the man page/help? | `down` |
| 5 | ¿Qué flag se añade a un comando para mostrar su ayuda? / What flag do you add to a command to show its help? | `-h` |
| 6 | ¿Cómo se crea el archivo llamado "newnote"? / How would you create the file named "newnote"? | `touch newnote` |
| 7 | ¿Qué tipo de archivo es "myfile"? / What type of file is "myfile"? | `ASCII text` |
| 8 | ¿Cómo se mueve el archivo "myfile" a la carpeta "myfolder"? / How would you move "myfile" to the "myfolder" directory? | `mv myfile myfolder` |
| 9 | ¿Cuál es la flag del sistema de archivos? / What is the filesystem flag? | `THM{FILESYSTEM}` |
| 10 | Leer la información de la Task 4. / Read the Task 4 information. | No answer needed |
| 11 | ¿Qué usuario se crea/emplea en la tarea? / What user is created/used in this task? | `user2` |
| 12 | ¿Cómo se cambia a ese usuario? / How do you switch to that user? | `su user2` |
| 13 | Leer la información de la Task 5. / Read the Task 5 information. | No answer needed |
| 14 | ¿Cuál es la flag de su? / What is the su flag? | `THM{SU_USER2}` |
| 15 | Leer la información de la Task 6. / Read the Task 6 information. | No answer needed |
| 16 | ¿Cuál es la ruta completa del directorio de logs? / What is the full path to the log directory? | `/var/log` |
| 17 | ¿Dónde se guardan los archivos temporales? / Where are temporary files stored? | `/tmp` |
| 18 | ¿Cuál es el directorio home del usuario root? / What is the root user's home directory? | `/root` |
| 19 | Leer la información de la Task 6 (final). / Read the Task 6 information (end). | No answer needed |
| 20 | Leer la información de la Task 7. / Read the Task 7 information. | No answer needed |
| 21 | Terminar la sala y repasar el contenido. / Finish the room and review the content. | No answer needed |
| 22 | Leer la conclusión de la sala. / Read the conclusion of the room. | No answer needed |

---

**Metodología:** Desplegar y acceder a la máquina Linux, leer las páginas del manual y la ayuda (`-h`), crear y mover archivos (`touch`, `file`, `mv`), gestionar usuarios (`su` a `user2`) y, finalmente, ubicar logs y directorios del sistema (`/var/log`, `/tmp`, `/root`), recogiendo las flags de cada fase.

### Cadena de ataque / Attack Chain

```text
Deploy VM -> SSH/login -> man pages & -h -> touch newnote -> file myfile -> mv myfile myfolder -> THM{FILESYSTEM} -> user2 -> su user2 -> THM{SU_USER2} -> /var/log -> /tmp -> /root -> procesos -> cierre
```

**Learning chain:** Linux -> Terminal -> man pages (ayuda) -> Manipulación de archivos -> Gestión de usuarios (su) -> Logs y directorios del sistema -> Procesos 101

**Lección:** *Dominar la terminal y la estructura de directorios de Linux es la base sobre la que se asienta todo el trabajo posterior de enumeración, explotación y gestión de un sistema.*

**MITRE ATT&CK:** N/A (sala introductoria de fundamentos Linux)

**Fuente:** [TryHackMe - Linux Fundamentals Part 2](https://tryhackme.com/room/linuxfundamentalspart2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.