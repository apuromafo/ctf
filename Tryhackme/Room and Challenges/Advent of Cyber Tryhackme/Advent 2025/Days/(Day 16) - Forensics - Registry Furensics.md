# Forensics - Registry Furensics [EASY]

### Información de la Sala / Room Information

| Propiedad / Property | Valor / Value |
| --- | --- |
| **Nombre / Name** | Forensics - Registry Furensics |
| **Evento / Event** | Advent of Cyber 2025 — Día 16 |
| **Sala / Room URL** | https://tryhackme.com/room/adventofcyber25 |
| **Dificultad / Difficulty** | Easy |
| **Descripción / Description** | Día 16 del calendario AoC 2025 (Forensics - Registry Furensics). Solución/respuestas del reto diario. |

---


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

## Respuestas / Answers
- What application was installed on the dispatch-srv01 before the abnormal activity started? : 
`DroneManager Updater`
- What is the full path where the user launched the application (found in question 1) from? : 
`C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe`
- Which value was added by the application to maintain persistence on startup? : 
`*C:\Program Files\DroneManager\dronehelper.exe* --background`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
