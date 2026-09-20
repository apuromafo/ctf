# Windows Fundamentals 1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `windowsfundamentals1xbx` | [TryHackMe](https://tryhackme.com/room/windowsfundamentals1xbx) | 00 Level Info | THM | Ediciones de Windows, GUI, NTFS, %windir%, Cuentas de usuario, UAC, Panel de control, Task Manager | Fundamentos del sistema operativo Windows: desktop, NTFS, cuentas, UAC, panel de control y administrador de tareas |

---

**Contexto:**
> **ES:** Primera parte del módulo Windows Fundamentals: ediciones de Windows, escritorio y barra de tareas, sistema de archivos NTFS, carpetas del sistema (%windir%), cuentas de usuario, Control de Cuentas de Usuario (UAC), Panel de control y Administrador de tareas.
> **EN:** First part of the Windows Fundamentals module: Windows editions, desktop and taskbar, NTFS file system, system folders (%windir%), user accounts, User Account Control (UAC), Control Panel and Task Manager.

## Solucionario

### Task 1: Introducción a Windows / Introduction to Windows
**Explicación:**
1. No answer needed

### Task 2: Ediciones de Windows / Windows Editions
**Explicación:**
2. BitLocker

### Task 3: El Escritorio (GUI) / The Desktop (GUI)
**Explicación:**
1. Hidden
2. Show Task View button
3. Action Center

### Task 4: El Sistema de Archivos / The File System
**Explicación:**
4. New Technology File System

### Task 5: Las Carpetas Windows\System32 / The Windows\System32 Folders
**Explicación:**
5. %windir%

### Task 6: Cuentas de Usuario, Perfiles y Permisos / User Accounts, Profiles, and Permissions
**Explicación:**
1. tryhackmebilly
2. Remote Desktop Users,Users
3. Guest
4. window$Fun1!

### Task 7: Control de Cuentas de Usuario / User Account Control
**Explicación:**
7. User Account Control

### Task 8: Configuración y Panel de Control / Settings and the Control Panel
**Explicación:**
8. Windows Defender Firewall

### Task 9: Administrador de Tareas / Task Manager
**Explicación:**
9. Ctrl+Shift+Esc

### Task 10: Conclusión / Conclusion
**Explicación:**
10. No answer needed

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Read the above and start the virtual machine. | `No answer needed` |
| 2 | What encryption can you enable on Pro that you can't enable in Home? | `BitLocker` |
| 3.1 | Which selection will hide/disable the Search box? | `Hidden` |
| 3.2 | Which selection will hide/disable the Task View button? | `Show Task View button` |
| 3.3 | Besides Clock and Network, what other icon is visible in the Notification Area? | `Action Center` |
| 4 | What is the meaning of NTFS? | `New Technology File System` |
| 5 | What is the system variable for the Windows folder? | `%windir%` |
| 6.1 | What is the name of the other user account? | `tryhackmebilly` |
| 6.2 | What groups is this user a member of? | `Remote Desktop Users,Users` |
| 6.3 | What built-in account is for guest access to the computer? | `Guest` |
| 6.4 | What is the account description? | `window$Fun1!` |
| 7 | What does UAC mean? | `User Account Control` |
| 8 | In the Control Panel, change the view to Small icons. What is the last setting in the Control Panel view? | `Windows Defender Firewall` |
| 9 | What is the keyboard shortcut to open Task Manager? | `Ctrl+Shift+Esc` |
| 10 | Read the above. | `No answer needed` |

---

**Metodología:**
Exploración guiada de una máquina Windows: repaso de ediciones y cifrado BitLocker, configuración de la barra de tareas, sistema de archivos NTFS, variables del sistema, gestión de cuentas de usuario (grupos, invitado, descripción), UAC, panel de control y atajos del administrador de tareas.

### Cadena de ataque / Attack Chain
1. Familiarización con el escritorio, la barra de tareas y la zona de notificación.
2. Revisión de las ediciones de Windows y del sistema de archivos NTFS.
3. Exploración de las carpetas del sistema y de la variable %windir%.
4. Gestión de cuentas de usuario y grupos (RDP, invitado).
5. Configuración de UAC, panel de control y administrador de tareas.

**Learning chain:**
Windows Editions -> GUI -> NTFS -> System32 -> User Accounts -> UAC -> Control Panel -> Task Manager

**Lección:** *Windows se administra con una combinación de herramientas gráficas (panel de control, administrador de tareas), utilidades del sistema y cuentas con privilegios regulados por UAC.*

**MITRE ATT&CK:**
- N/A (Room de aprendizaje / walkthrough — fundamentos de Windows)

**Fuente:** [TryHackMe - Windows Fundamentals 1](https://tryhackme.com/room/windowsfundamentals1xbx)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.