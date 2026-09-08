# Operating Systems: Introduction

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `operatingsystemsintroduction` |
| **Link** | [TryHackMe](https://tryhackme.com/room/operatingsystemsintroduction) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + máquina Ubuntu MATE proporcionada por el room |
| **Componentes** | Ubuntu MATE (1.26.2) / System Monitor / kernel space vs user space / gestión de usuarios |
| **Impacto** | Fundamentos de SO: distinguir kernel/user space, responsabilidades del SO y navegar un Linux real para extraer datos (note.txt) |

---

**Contexto:** El SO "gestiona la casa": media entre hardware y programas. Habla de dos espacios: **kernel space** (acceso sin restricciones al hardware, donde corre el núcleo y los drivers) y **user space** (donde corren las aplicaciones con más restricciones). Entre sus responsabilidades: **gestión de usuarios** (cuentas, autenticación, permisos), procesos, memoria, archivos y hardware. En el lab (Ubuntu MATE **1.26.2**, RAM **1.9 GiB**), el System Monitor revela que `/dev/root` es **ext4**, el directorio Home tiene **3** carpetas de usuario, y en el `Documents` de Alex hay un `note.txt` con un flag. Es una práctica de "explorar el sistema" muy típica de engagement inicial.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to learn about operating systems! | `No answer needed` |

**Explicación:** Módulo de sistemas operativos (Pre Security); se utiliza una máquina Ubuntu MATE.

### Task 2: The Invisible Manager

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which OS space has **unrestricted** access to your computer's hardware? | `Kernel space` |
| 2 | Which OS responsibility manages **user accounts, authentication, and permissions**? | `User management` |
| 3 | After opening the About This Computer shortcut, what version of **Ubuntu Mate** is your computer running? | `1.26.2` |
| 4 | Check out the Hardware section of the System tab. How much memory is allocated to your machine? | `1.9 GiB` |

**Explicación:**
- **Kernel space:** el núcleo corre con acceso total al hardware; las aplicaciones (user space) solo lo piden a través de syscalls.
- **User management:** cuentas, autenticación y permisos son responsabilidad explícita del SO.
- **En el lab:** menú → *About This Computer* → versión **1.26.2**; pestaña *System → Hardware* → memoria **1.9 GiB**.

### Task 3: OS Interaction and Landscape

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Open the File Systems tab in System Monitor. What Type is listed for the `/dev/root` device? | `ext4` |
| 2 | After opening the Home directory on the Desktop, how many user directories exist? | `3` |
| 3 | Navigate to Alex's home directory and explore the Documents folder. What is the flag value contained in `note.txt`? | `THM{new_pc_for_free!}` |

**Explicación:**
- **ext4:** en System Monitor → File Systems, el filesystem `/dev/root` aparece como **ext4** (sistemas de archivos estándar de Linux).
- **3 dirs:** en `~/` (Home) del equipo se ven **3** carpetas de usuario (p. ej. alex, ... más alguna de sistema/sesión).
- **Flag:** abrir `~/alex/Documents/note.txt` → `THM{new_pc_for_free!}`.

### Task 4: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room and continue on your cyber learning journey! | `No answer needed` |

**Explicación:** Puente hacia "Windows Basics" en el path Pre Security.

**Metodología:**
1. **Desplegar la máquina** Ubuntu MATE y abrir *About This Computer* para obtener la versión (`1.26.2`) y la RAM (`1.9 GiB`, pestaña *System → Hardware*).
2. **Conceptos:** el kernel corre en **kernel space** con acceso total al hardware; las aplicaciones (user space) solo lo piden vía syscalls; la **User management** (cuentas, autenticación, permisos) es responsabilidad explícita del SO.
3. **Reconocimiento del sistema:** abrir *System Monitor → File Systems* → `/dev/root` aparece como **ext4**.
4. **Descubrimiento de archivos:** en el dektop, abrir `~/` (Home): **3** carpetas de usuario; navegar a `~/alex/Documents/note.txt` → flag `THM{new_pc_for_free!}`.

```
SO (OS): kernel space vs user space
  -> responsabilidades del SO (gestión de usuarios, memoria, procesos)
  -> reconocimiento del sistema en vivo (versión, RAM, fs)
  -> extraer flag de archivos locales (note.txt)
```

**Lección:** *Conocer tu SO es conocer el campo de batalla.* Kernel vs user space, permisos y filesystems determinan qué puedes hacer y qué detectarás.

**Learning chain:** SO (kernel space vs user space) → responsabilidades del SO (gestión de usuarios, memoria, procesos) → reconocimiento en vivo (versión 1.26.2, RAM 1.9 GiB, fs ext4) → extracción de flag local (note.txt) → THM{new_pc_for_free!}

**MITRE ATT&CK:** T1082 (System Information Discovery), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Operating Systems: Introduction](https://tryhackme.com/room/operatingsystemsintroduction)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
