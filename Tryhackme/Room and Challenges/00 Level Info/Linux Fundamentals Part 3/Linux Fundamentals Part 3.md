# Linux Fundamentals Part 3

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Info | Walkthrough | `linuxfundamentalspart3` | https://tryhackme.com/room/linuxfundamentalspart3 | 00 Level Info | TryHackMe | Linux / editores de texto / wget / procesos / crontab / systemctl / señalización de red | Fundamento esencial de Linux: editores de texto, descarga con wget, gestión de procesos, servicios con systemctl, autocronización y señales |

---

**Contexto:** Tercera y última parte del curso introductorio de Linux de TryHackMe. Profundiza en herramientas reales de trabajo: editores de texto en terminal, descarga de archivos con `wget`, administración de procesos y su señalización, gestión de servicios con `systemctl`, automatización de tareas con cron y una introducción a la transferencia de archivos.

> **ES:** Se completa la base de Linux: editores de texto (vim/nano), `wget`, procesos y señales (SIGTERM), servicios con `systemctl` y tareas programadas con cron.
> **EN:** Complete the Linux basics: text editors (vim/nano), `wget`, processes and signals (SIGTERM), systemctl services and scheduled cron jobs.

## Solucionario

### Task 1: Acceso a tu primera máquina Linux / Accessing Your First Linux Machine

**Explicación:** La sala despliega una máquina virtual Linux para practicar. La primera tarea es introductoria: arrancar el entorno y leer la información sin necesidad de responder nada.

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desplegar la máquina y leer la información. / Deploy the machine and read the information. | No answer needed |

### Task 2: Editores de texto en terminal / Terminal text editors

**Explicación:** La tarea presenta los editores de terminal más usados (nano, vim, etc.). El primer apartado es de lectura; a continuación hay que comprobar que se sabe crear y guardar un archivo con un editor de texto en línea de comandos, obteniendo la flag que lo acredita.

```text
2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información sobre editores de terminal. / Read the information about terminal editors. | No answer needed |

### Task 3: Editores de texto y flag / Text editors and flag

**Explicación:** Con un editor de texto se crea un archivo y se guarda para demostrar el manejo de la herramienta. La flag localizada confirma que se ha completado correctamente el ejercicio con los editores de texto en la terminal.

```text
3. 1. No answer needed
   2. THM{TEXT_EDITORS}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea. / Read the task information. | No answer needed |
| 2 | ¿Cuál es la flag de los editores de texto? / What is the text editors flag? | `THM{TEXT_EDITORS}` |

### Task 4: Utilidades generales (wget) / General utilities (wget)

**Explicación:** Se presenta `wget`, la utilidad para descargar archivos desde la terminal. Se practica descargando archivos de un servidor web y se localiza la flag correspondiente al uso correcto de `wget`.

```text
4. 1. No answer needed
   2. No answer needed
   3. THM{WGET_WEBSERVER}
   4. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de `wget`. / Read the wget information. | No answer needed |
| 2 | Realizar la descarga con `wget`. / Perform the download with wget. | No answer needed |
| 3 | ¿Cuál es la flag del servidor web con wget? / What is the wget web server flag? | `THM{WGET_WEBSERVER}` |
| 4 | Leer la información de la tarea. / Read the task information. | No answer needed |

### Task 5: Procesos 101 / Processes 101

**Explicación:** Gestión de procesos en Linux: identificación, señalización y cierre. Un proceso puede recibir señales como `SIGTERM` y se estudia código de salida del proceso, así como la gestión de servicios con `systemctl` (parar y habilitar un servicio) y el control de procesos en segundo plano con `fg`.

```text
5. 1. No answer needed
   2. 301
   3. SIGTERM
   4. THM{PROCESSES}
   5. systemctl stop myservice
   6. systemctl enable myservice
   7. fg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información sobre procesos. / Read the processes information. | No answer needed |
| 2 | ¿Cuál es el código/salida mostrado? / What is the code/exit shown? | `301` |
| 3 | ¿Qué señal termina un proceso? / What signal terminates a process? | `SIGTERM` |
| 4 | ¿Cuál es la flag de procesos? / What is the processes flag? | `THM{PROCESSES}` |
| 5 | ¿Cómo se detiene el servicio myservice? / How do you stop the myservice service? | `systemctl stop myservice` |
| 6 | ¿Cómo se habilita myservice al arranque? / How do you enable myservice on boot? | `systemctl enable myservice` |
| 7 | ¿Cómo se trae al frente un proceso en segundo plano? / How do you bring a background process to the foreground? | `fg` |

### Task 6: Mantenimiento del sistema: automatización (cron) / System maintenance: automation (cron)

**Explicación:** Se introduce `crontab` para automatizar tareas repetitivas. Se practica la sintaxis de cron, donde la cadena `@reboot` indica que la tarea se ejecutará cada vez que el sistema arranque.

```text
6. 1. No answer needed
   2. @reboot
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información sobre cron. / Read the cron information. | No answer needed |
| 2 | ¿Qué cadena ejecuta un comando en cada arranque? / What string runs a command at every boot? | `@reboot` |

### Task 7: Mantenimiento del sistema: logs / System maintenance: logs

**Explicación:** La tarea revisa la gestión de registros del sistema (logging). Es una tarea de lectura orientada a saber dónde se encuentran y cómo se consultan los logs de Linux, por lo que no requiere responder nada.

```text
7. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información sobre logs del sistema. / Read the system logging information. | No answer needed |

### Task 8: Practicar en la máquina / Practice on the machine

**Explicación:** Ejercicio práctico de conexión y uso de la máquina: se trabaja con la dirección de red y los archivos de ejemplo desplegados. La respuesta identifica la IP del entorno y el archivo de práctica `catsanddogs.jpg`.

```text
8. 1. No answer needed
   2. 10.9.232.111
   3. catsanddogs.jpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea práctica. / Read the practice task information. | No answer needed |
| 2 | ¿Cuál es la IP del entorno de práctica? / What is the IP of the practice environment? | `10.9.232.111` |
| 3 | ¿Qué archivo se usa en la práctica? / What file is used in the practice? | `catsanddogs.jpg` |

### Task 9: Cierre de la sala / End of room

**Explicación:** Conclusión del curso introductorio de Linux. Solo se repasa lo aprendido y se invita a continuar con siguientes retos, por lo que no hay nada que responder.

```text
9. 1. No answer needed
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Terminar la sala. / Finish the room. | No answer needed |
| 2 | Leer la conclusión. / Read the conclusion. | No answer needed |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desplegar la máquina y leer la información. / Deploy the machine and read the information. | No answer needed |
| 2 | Leer la información sobre editores de terminal. / Read the information about terminal editors. | No answer needed |
| 3 | Leer la información de la Task 3. / Read the Task 3 information. | No answer needed |
| 4 | ¿Cuál es la flag de los editores de texto? / What is the text editors flag? | `THM{TEXT_EDITORS}` |
| 5 | Leer la información de `wget`. / Read the wget information. | No answer needed |
| 6 | Realizar la descarga con `wget`. / Perform the download with wget. | No answer needed |
| 7 | ¿Cuál es la flag del servidor web con wget? / What is the wget web server flag? | `THM{WGET_WEBSERVER}` |
| 8 | Leer la información de la Task 4. / Read the Task 4 information. | No answer needed |
| 9 | Leer la información sobre procesos. / Read the processes information. | No answer needed |
| 10 | ¿Cuál es el código/salida mostrado? / What is the code/exit shown? | `301` |
| 11 | ¿Qué señal termina un proceso? / What signal terminates a process? | `SIGTERM` |
| 12 | ¿Cuál es la flag de procesos? / What is the processes flag? | `THM{PROCESSES}` |
| 13 | ¿Cómo se detiene el servicio myservice? / How do you stop the myservice service? | `systemctl stop myservice` |
| 14 | ¿Cómo se habilita myservice al arranque? / How do you enable myservice on boot? | `systemctl enable myservice` |
| 15 | ¿Cómo se trae al frente un proceso en segundo plano? / How do you bring a background process to the foreground? | `fg` |
| 16 | Leer la información sobre cron. / Read the cron information. | No answer needed |
| 17 | ¿Qué cadena ejecuta un comando en cada arranque? / What string runs a command at every boot? | `@reboot` |
| 18 | Leer la información sobre logs del sistema. / Read the system logging information. | No answer needed |
| 19 | Leer la información de la tarea práctica. / Read the practice task information. | No answer needed |
| 20 | ¿Cuál es la IP del entorno de práctica? / What is the IP of the practice environment? | `10.9.232.111` |
| 21 | ¿Qué archivo se usa en la práctica? / What file is used in the practice? | `catsanddogs.jpg` |
| 22 | Terminar la sala. / Finish the room. | No answer needed |
| 23 | Leer la conclusión. / Read the conclusion. | No answer needed |

---

**Metodología:** Conectar y desplegar la máquina, usar un editor de texto para completar el ejercicio, descargar archivos con `wget`, gestionar procesos (señales `SIGTERM`, códigos de salida), administrar servicios con `systemctl` (stop/enable), planificar con cron (`@reboot`) y practicar sobre el entorno con la IP y archivos dados.

### Cadena de ataque / Attack Chain

```text
Deploy VM -> editor de texto -> THM{TEXT_EDITORS} -> wget -> THM{WGET_WEBSERVER} -> procesos (301 / SIGTERM) -> systemctl stop/enable myservice -> fg -> cron @reboot -> IP 10.9.232.111 -> catsanddogs.jpg -> cierre
```

**Learning chain:** Linux -> Editores de texto -> wget -> Procesos y señales -> systemctl (servicios) -> cron (automatización) -> Logs -> Práctica en red

**Lección:** *La administración diaria de un sistema Linux se apoya en un puñado de herramientas (editores, wget, systemctl, cron y la gestión de procesos); dominarlas permite automatizar y mantener cualquier entorno de forma reproducible.*

**MITRE ATT&CK:** N/A (sala introductoria de fundamentos Linux)

**Fuente:** [TryHackMe - Linux Fundamentals Part 3](https://tryhackme.com/room/linuxfundamentalspart3)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.