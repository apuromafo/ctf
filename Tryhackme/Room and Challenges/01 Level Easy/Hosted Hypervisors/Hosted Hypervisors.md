# Hosted Hypervisors

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hostedhypervisors` | https://tryhackme.com/room/hostedhypervisors | 01 Level Easy | TryHackMe | VirtualBox / VBoxSVC.exe / Vbox.log / VMware Workstation / vmautostart.xml / logs | Comprensión de los hypervisores hospedados (tipo 2) y de sus logs y archivos de configuración. |

---

**Contexto:** Sala teórico-práctica sobre virtualización hospedada (hypervisores tipo 2): VirtualBox y VMware Workstation. Se exploran procesos de servicio (VBoxSVC), archivos de instalación, logs (Vbox.log, logs de VMware) y configuraciones de inicio automático (vmautostart.xml), además de una práctica que desemboca en una flag.

> **ES:** Revisa los procesos, logs y archivos de configuración de VirtualBox y VMware para responder a las preguntas y obtener la flag.
> **EN:** Review VirtualBox and VMware processes, logs and configuration files to answer the questions and get the flag.

## Solucionario

### Task 1: Lectura de material / Reading Material

**Explicación:** Tarea introductoria de lectura del material de la sala; no requiere respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Virtualización hospedada / Hosted Virtualization

**Explicación:** Se introduce el concepto de hypervisores hospedados (tipo 2); tarea de lectura sin respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el material sobre hypervisores hospedados. | `No answer needed` |

### Task 3: VirtualBox: puerto y servicio / VirtualBox Port and Service

**Explicación:** VirtualBox expone su interfaz de gestión remota a través del proceso VBoxSVC, que escucha en un puerto concreto de la red local.

1. 1. 8096
   2. VBoxSVC.exe

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puerto utiliza VBoxSVC? / What port does VBoxSVC use? | `8096` |
| 2 | ¿Qué proceso corresponde al servicio de gestión de VirtualBox? / What process corresponds to the VirtualBox management service? | `VBoxSVC.exe` |

### Task 4: VirtualBox: instalación y logs / VirtualBox Installation and Logs

**Explicación:** Se localizan la ruta de instalación de VirtualBox y el archivo de log que la instalación o la ejecución de la VM generan en ese directorio.

1. 1. C:\Program Files\Oracle\VirtualBox
   2. Vbox.log

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué ruta se instala VirtualBox? / What path is VirtualBox installed to? | `C:\Program Files\Oracle\VirtualBox` |
| 2 | ¿Qué archivo de log se genera en esa ruta? / What log file is generated in that path? | `Vbox.log` |

### Task 5: VMware: inicio automático y logs / VMware Autostart and Logs

**Explicación:** En VMware Workstation el inicio automático de las máquinas se controla con un archivo XML y los logs se almacenan en el directorio de datos del programa.

1. 1. vmautostart.xml
   2. C:\ProgramData\VMware\logs

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué archivo controla el inicio automático de las máquinas de VMware? / What file controls VMware VM autostart? | `vmautostart.xml` |
| 2 | ¿En qué directorio guarda VMware sus logs? / What directory does VMware store its logs in? | `C:\ProgramData\VMware\logs` |

### Task 6: Práctica: log y acceso / Practice: Log and Access

**Explicación:** En la parte práctica se inspecciona el contenido del entorno (logs y servicios) obteniendo la flag, el puerto de acceso y la IP del host.

1. 1. THM{You_f1nd_th3_l0g!}
   2. 6052
   3. 192.168.182.139

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag? / What is the flag? | `THM{You_f1nd_th3_l0g!}` |
| 2 | ¿Qué puerto hay que usar para acceder? / What port should be used to access? | `6052` |
| 3 | ¿Cuál es la IP del host? / What is the host IP? | `192.168.182.139` |

### Task 7: Cierre / Wrap-up

**Explicación:** Resumen y cierre de la sala; no requiere respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el resumen final de la sala. | `No answer needed` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | 1 | Revisa el material sobre hypervisores hospedados. | `No answer needed` |
| 3 | 1 | ¿Qué puerto utiliza VBoxSVC? / What port does VBoxSVC use? | `8096` |
| 3 | 2 | ¿Qué proceso corresponde al servicio de gestión de VirtualBox? / What process corresponds to the VirtualBox management service? | `VBoxSVC.exe` |
| 4 | 1 | ¿En qué ruta se instala VirtualBox? / What path is VirtualBox installed to? | `C:\Program Files\Oracle\VirtualBox` |
| 4 | 2 | ¿Qué archivo de log se genera en esa ruta? / What log file is generated in that path? | `Vbox.log` |
| 5 | 1 | ¿Qué archivo controla el inicio automático de las máquinas de VMware? / What file controls VMware VM autostart? | `vmautostart.xml` |
| 5 | 2 | ¿En qué directorio guarda VMware sus logs? / What directory does VMware store its logs in? | `C:\ProgramData\VMware\logs` |
| 6 | 1 | ¿Cuál es la flag? / What is the flag? | `THM{You_f1nd_th3_l0g!}` |
| 6 | 2 | ¿Qué puerto hay que usar para acceder? / What port should be used to access? | `6052` |
| 6 | 3 | ¿Cuál es la IP del host? / What is the host IP? | `192.168.182.139` |
| 7 | 1 | Revisa el resumen final de la sala. | `No answer needed` |

---

**Metodología:** Estudio del material sobre hypervisores hospedados, localización de los componentes de VirtualBox (VBoxSVC, puerto 8096, Vbox.log) y de VMware (vmautostart.xml, directorio de logs) y práctica con el entorno hasta obtener la flag.

### Cadena de ataque / Attack Chain

```text
leer material -> localizar VBoxSVC/8096 -> Vbox.log -> vmautostart.xml -> logs de VMware -> acceder al servicio -> flag
```

**Learning chain:** Hypervisores tipo 2 -> VirtualBox (VBoxSVC, logs) -> VMware Workstation (autostart, logs) -> flag.

**Lección:** *Los logs y archivos de configuración de los hypervisores revelan rutas, procesos y datos sensibles; inspeccionarlos forma parte de la enumeración inicial de cualquier entorno virtualizado.*

**MITRE ATT&CK:** T1082 (System Information Discovery), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Hosted Hypervisors](https://tryhackme.com/room/hostedhypervisors)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
