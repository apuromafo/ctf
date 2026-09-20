# Forensics - Registry Furensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `registry-forensics-aoc2025-h6k9j2l5p8` | https://tryhackme.com/room/registry-forensics-aoc2025-h6k9j2l5p8 | Advent of Cyber 2025 | TryHackMe | Windows Registry, persistence, forensic analysis | Alarmed — Evidence of persistence mechanism on dispatch-srv01 |

---

> **Objeto:** Investigar la máquina `dispatch-srv01` tras detectar actividad anómala en Advent of Cyber 2025 (Día 16), analizando el registro de Windows para identificar la aplicación instalada antes del incidente y el mecanismo de persistencia (Run/RunOnce) con el que se ejecuta en cada inicio.

**Contexto:** During Advent of Cyber 2025 Day 16, investigamos la máquina dispatch-srv01 tras detectar actividad anómala. Analizando el registro de Windows, descubrimos una aplicación sospechosa instalada previamente y el mecanismo de persistencia que configuró para ejecutarse en cada inicio del sistema.

> **ES:** Día 16 de Advent of Cyber 2025 — forense de registro: identificar la app instalada (DroneManager Updater) y su persistencia en Run/RunOnce sobre dispatch-srv01.
> **EN:** Advent of Cyber 2025 Day 16 — registry forensics: find the app installed on dispatch-srv01 before the anomaly (DroneManager Updater) and the autostart value it added.

## Solucionario

### Task 1: Investigación del Registro / Registry Investigation

**Explicación:** Se inspeccionan las claves del registro de Windows para reconstruir qué se instaló en `dispatch-srv01` y cómo persiste. En las claves de desinstalación (`Uninstall`) aparece la aplicación `DroneManager Updater` como la última instalada antes de la actividad anómala. Comprobando los artefactos de instalación (prefetch/instalación) se obtiene la ruta de donde el usuario lanzó el setup: `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe`. Por último, en las claves de persistencia (`Run`/`RunOnce`) se encuentra el valor añadido por la aplicación para sobrevivir a los reinicios: `"C:\Program Files\DroneManager\dronehelper.exe" --background`.

```powershell
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" /s
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What application was installed on the dispatch-srv01 before the abnormal activity started? | `DroneManager Updater` |
| 2 | What is the full path where the user launched the application (found in question 1) from? | `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe` |
| 3 | Which value was added by the application to maintain persistence on startup? | `"C:\Program Files\DroneManager\dronehelper.exe" --background` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What application was installed on the dispatch-srv01 before the abnormal activity started? | `DroneManager Updater` |
| 2 | What is the full path where the user launched the application (found in question 1) from? | `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe` |
| 3 | Which value was added by the application to maintain persistence on startup? | `"C:\Program Files\DroneManager\dronehelper.exe" --background` |

---

**Metodología:** Se inspeccionaron las claves del registro de Windows (Uninstall, Run/RunOnce, y artefactos de instalación) para identificar la aplicación instalada y su mecanismo de persistencia en la máquina dispatch-srv01.

### Cadena de ataque / Attack Chain

```text
Actividad anómala en dispatch-srv01 -> inspección de Uninstall (DroneManager Updater) -> ruta de lanzamiento en Downloads -> Run/RunOnce (dronehelper.exe --background) -> persistencia confirmada
```

**Learning chain:** Windows Registry → Persistence Analysis → Startup Keys → Forensic Artifact Recovery

**Lección:** *Las claves de persistencia del registro (`Run`/`RunOnce`) y los artefactos de instalación (`Uninstall`) son las primeras fuentes de evidencia para correlacionar la instalación de software con una actividad anómala en el sistema.*

**MITRE ATT&CK:** T1547.001 — Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

**Fuente:** [TryHackMe - Forensics - Registry Furensics](https://tryhackme.com/room/registry-forensics-aoc2025-h6k9j2l5p8)

> **Fuente original / Original source:** https://tryhackme.com/r/room/registry-forensics-aoc2025-h6k9j2l5p8

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.