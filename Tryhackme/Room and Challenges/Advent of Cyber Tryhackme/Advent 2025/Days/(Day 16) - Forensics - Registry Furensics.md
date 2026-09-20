# Forensics - Registry Furensics

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day16forensicsregistryfurensics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Windows Registry / hives / Registry Explorer / NTUSER.dat / Software hive / Run key / AppCompatFlags / persistence |
| **Impacto** | Analizar el registro de Windows de un sistema comprometido para reconstruir instalación, ejecución y persistencia maliciosas |

---

**Contexto:** Día 16 del Advent of Cyber 2025. El registro de Windows ("el cerebro del SO") almacena configuración del sistema, programas instalados, actividad de usuario, comportamiento de arranque y ajustes de hardware y seguridad en archivos binarios llamados **hives**. Como el editor de registro no permite analizar de forma segura un sistema comprometido ni abrir hives offline, se usa **Registry Explorer** sobre la VM para inspeccionar el hive Software (instalación de `Drone Manager` en `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`), el hive `NTUSER.dat` (full paths de programas ejecutados vía AppCompatFlags) y la clave `Run` (persistencia con `dronehelper.exe --background`). *(English note / Nota EN: Day 16 of AoC 2025 — analyze the offline Windows Registry hives of a compromised dispatch-srv01 with Registry Explorer to answer forensic questions about the installed application, the launcher path and the persistence value.)*

## Solucionario

### Día 16: Forensics - Registry Furensics

**Explicación:**

- Windows Registry -> brain of the OS
- It stores
    1. System configuration
    2. Installed programs
    3. User activity
    4. Startup behavior
    5. Hardware and security settings

- Registry data is stored in multiple binary files called Hives.


- Registry editor -> views registry on a live system; can't safely analyze compromised systems; can't open offline hives

 ## 🔍 Enfoque / Approach

First, we learned that the Windows Registry stores configuration values critical to system operation and user activity.

We then proceeded to run the VM and use a program called "Registry Explorer" which allowed us to review the registry of a compromised system.

The first part we started to inspect was the `Software` module. From this we can see that on the 21st of October the program `Drone Manager` was installed. This was found in the path `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`. As this isn't a familiar Windows application it stands out as suspicious.

To find the file location we swapped hive to `NT_USER.dat`. We then followed the path `ROOT\Software\Microsoft\Windows NT\CurrentVersion\AppCompFlags\Compatibility Assistant\Store`. This reveals a list of full paths for programs the user ran.

We then moved back to the `Software` hive and followed the path `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` which revealed the path (`"C:\Program Files\DroneManager\dronehelper.exe" --background`) that was added so Drone Manager ran on startup.

- **Registry explorer**

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What application was installed on the dispatch-srv01 before the abnormal activity started? | `DroneManager Updater` |
| 2 | What is the full path where the user launched the application (found in question 1) from? | `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe` |
| 3 | Which value was added by the application to maintain persistence on startup? | `*C:\Program Files\DroneManager\dronehelper.exe* --background` |

---

**Metodología:** Se cargó la VM y se abrieron los hives del sistema comprometido con Registry Explorer. En el hive `Software` se localizó la instalación anómala de `Drone Manager Updater` en `Uninstall`. Cambiando al hive `NTUSER.dat` se siguió la ruta AppCompatFlags para descubrir el full path del ejecutable lanzado por el usuario. Volviendo a `Software`, en `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` se identificó el valor de persistencia añadido en el arranque.
**Learning chain:** Windows Registry (hives) -> Registry Explorer -> Software hive (Uninstall: Drone Manager Updater) -> NTUSER.dat (AppCompatFlags: full path del lanzamiento) -> Run key (persistencia dronehelper.exe --background) -> respuestas forenses

Cadena de ataque / Attack Chain:
```
instalación del 21/10 en HKLM\SOFTWARE\...\Uninstall (Drone Manager Updater) -> ruta lanzada: C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe -> persistencia en HKLM\...\CurrentVersion\Run => *C:\Program Files\DroneManager\dronehelper.exe* --background
```

**Lección:** *El registro de Windows escribe la historia completa de una intrusión: instalaciones, ejecuciones por usuario y persistencia; combinando al menos dos hives (SYSTEM/Software para instalación y persistencia, NTUSER.dat para ejecución) se reconstruye la cadena casi sin tocar el sistema vivo.*

**MITRE ATT&CK:** T1547.001 - Boot/Logon Autostart Execution: Registry Run Keys / Startup Folder, T1112 - Modify Registry

**Fuente:** [TryHackMe - Forensics - Registry Furensics](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.