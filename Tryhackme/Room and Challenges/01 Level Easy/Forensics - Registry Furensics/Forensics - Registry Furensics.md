# Forensics - Registry Furensics

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `registry-forensics-aoc2025-h6k9j2l5p8` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/registry-forensics-aoc2025-h6k9j2l5p8) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Windows Registry, persistence, forensic analysis |
| **Impacto** | Alarmed — Evidence of persistence mechanism on dispatch-srv01 |

---

**Contexto:** During Advent of Cyber 2025 Day 16, investigamos la máquina dispatch-srv01 tras detectar actividad anómala. Analizando el registro de Windows, descubrimos una aplicación sospechosa instalada previamente y el mecanismo de persistencia que configuró para ejecutarse en cada inicio del sistema.

## Solucionario

### Task 1: Investigación del Registro

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What application was installed on the dispatch-srv01 before the abnormal activity started? | `DroneManager Updater` |
| 2 | What is the full path where the user launched the application (found in question 1) from? | `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe` |
| 3 | Which value was added by the application to maintain persistence on startup? | `"C:\Program Files\DroneManager\dronehelper.exe" --background` |

---

**Metodología:** Se inspeccionaron las claves del registro de Windows (Uninstall, Run/RunOnce, y artefactos de instalación) para identificar la aplicación instalada y su mecanismo de persistencia en la máquina dispatch-srv01.
**Learning chain:** Windows Registry → Persistence Analysis → Startup Keys → Forensic Artifact Recovery
**MITRE ATT&CK:** T1547.001 — Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
**Fuente:** [TryHackMe - Forensics - Registry Furensics](https://tryhackme.com/r/room/registry-forensics-aoc2025-h6k9j2l5p8)
