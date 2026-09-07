# Operating Systems: Introduction [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `operatingsystemsintroduction`
* **Link:** https://tryhackme.com/room/operatingsystemsintroduction
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + máquina Ubuntu MATE proporcionada por el room
* **Componentes:** Laboratorio Ubuntu MATE (1.26.2) · System Monitor · kernel space vs user space · gestión de usuarios
* **Impacto rol:** Fundamentos de SO; distinguir kernel/user space, responsabilidades del SO (gestión de usuarios, procesos, hardware), y navegar un sistema Linux real para extraer datos (nota.txt).

## Solucionario de Tareas / Task Solutions

> **ES:** El SO "gestiona la casa": media entre hardware y programas. Habla de dos espacios: **kernel space** (acceso sin restricciones al hardware, donde corre el núcleo y los drivers) y **user space** (donde corren las aplicaciones con más restricciones). Entre sus responsabilidades: **gestión de usuarios** (cuentas, autenticación, permisos), procesos, memoria, archivos y hardware. En el lab (Ubuntu MATE **1.26.2**, RAM **1.9 GiB**), el System Monitor revela que `/dev/root` es **ext4**, el directorio Home tiene **3** carpetas de usuario, y en el `Documents` de Alex hay un `note.txt` con un flag. Es una práctica de "explorar el sistema" muy típica de engagement inicial.
> **EN:** The OS "runs the house": it mediates between hardware and programs. It introduces two spaces: **kernel space** (unrestricted hardware access, where the kernel and drivers run) and **user space** (where applications run with more restrictions). Responsibilities include **user management** (accounts, authentication, permissions), processes, memory, files and hardware. In the lab (Ubuntu MATE **1.26.2**, RAM **1.9 GiB**), System Monitor shows `/dev/root` is **ext4**, Home has **3** user folders, and Alex's `Documents` holds a `note.txt` with a flag. Classic "explore the system" practice for initial engagements.

### Task 1 — Introducción / Introduction

* **Check:** `I understand the learning objectives and am ready to learn about operating systems!`
* **ES:** Módulo de sistemas operativos (Pre Security); con máquina Ubuntu MATE.
* **EN:** Operating systems module (Pre Security); Ubuntu MATE machine is used.

### Task 2 — El Gerente Invisible / The Invisible Manager *(vm)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which OS space has **unrestricted** access to your computer's hardware? | `Kernel space` |
| Which OS responsibility manages **user accounts, authentication, and permissions**? | `User management` |
| After opening the About This Computer shortcut, what version of **Ubuntu Mate** is your computer running? | `1.26.2` |
| Check out the Hardware section of the System tab. How much memory is allocated to your machine? | `1.9 GiB` |

* **Kernel space:** el núcleo corre con acceso total al hardware; las aplicaciones (user space) solo lo piden a través de syscalls.
* **User management:** cuentas, autenticación y permisos son responsabilidad explícita del SO.
* **En el lab:** menú → *About This Computer* → versión **1.26.2**; pestaña *System → Hardware* → memoria **1.9 GiB**.

### Task 3 — Interacción con el SO y Panorama / OS Interaction and Landscape

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Open the File Systems tab in System Monitor. What Type is listed for the `/dev/root` device? | `ext4` |
| After opening the Home directory on the Desktop, how many user directories exist? | `3` |
| Navigate to Alex's home directory and explore the Documents folder. What is the flag value contained in `note.txt`? | `THM{new_pc_for_free!}` |

* **ext4:** en System Monitor → File Systems, el filesystem `/dev/root` aparece como **ext4** (sistemas de archivos estándar de Linux).
* **3 dirs:** en `~/` (Home) del equipo se ven **3** carpetas de usuario (p. ej. alex, ... más alguna de sistema/sesión).
* **Flag:** abrir `~/alex/Documents/note.txt` → `THM{new_pc_for_free!}`.

### Task 4 — Conclusión / Conclusion

* **Check:** `Complete the room and continue on your cyber learning journey!`
* **ES:** Puente hacia "Windows Basics" en el path Pre Security.
* **EN:** Bridge toward "Windows Basics" in the Pre Security path.

## Metodología / Methodology

1. **Paso / Step:** Desplegar la máquina Ubuntu MATE y abrir *About This Computer* (versión y RAM).
2. **Paso / Step:** Abrir *System Monitor → File Systems* para el tipo de `/dev/root`.
3. **Paso / Step:** Contar directorios de usuario en `~/` del Desktop y leer `alex/Documents/note.txt`.

### Cadena de aprendizaje / Learning Chain

```
SO (OS): kernel space vs user space
  -> responsabilidades del SO (gestión de usuarios, memoria, procesos)
  -> reconocimiento del sistema en vivo (versión, RAM, fs)
  -> extraer flag de archivos locales (note.txt)
```

**Mapeo MITRE ATT&CK / relacionado:** T1082 (System Information Discovery) y T1005 (Data from Local System) — exactamente lo que practica este lab ("descubrir info del sistema y leer archivos locales"). Room de fundamentos.

**Lección:** *Conocer tu SO es conocer el campo de batalla.* Kernel vs user space, permisos y filesystems determinan qué puedes hacer y qué detectarás.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.