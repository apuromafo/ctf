# macOS Forensics_ Artefacts

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Walkthrough | macosforensicsartefacts | https://tryhackme.com/room/macosforensicsartefacts | 03 Level Hard | TryHackMe (Serie macOS Forensics) | apfs-fuse / plistutil / APFS / plist / System Configuration / TTY / creds.txt / Bluetooth | Análisis forense de artefactos de una imagen de disco macOS: montaje APFS, parseo de plists, preferencias, credenciales, configuración de red y Bluetooth para reconstruir la actividad del sistema. |

---

**Contexto:**
> **ES:** Ejercicio de la serie macOS Forensics centrado en los artefactos de un sistema macOS: montaje de la imagen APFS con `apfs-fuse`, parseo de plists con `plistutil`, análisis de preferencias del sistema (fechas, red `en0`/`192.168.64.1`, TTY, archivo `creds.txt`, ventanas y carpetas recientes) y artefactos Bluetooth (`bluetooth/isConnected`).
> **EN:** Exercise from the macOS Forensics series focused on macOS system artefacts: mounting the APFS image with `apfs-fuse`, parsing plists with `plistutil`, analysing system preferences (dates, network `en0`/`192.168.64.1`, TTY, `creds.txt` file, windows and recent folders) and Bluetooth artefacts (`bluetooth/isConnected`).

## Solucionario

### Task 1: Tarea 1
**Explicación:**
1. apfs-fuse -v 4 mac-disk.img ~/mac

### Task 2: Tarea 2
**Explicación:**
2. plistutil

### Task 3: Tarea 3
**Explicación:**
3. 1. 2024-12-08 17:42:28
   2. AE
   3. 2025-01-19 15:47:05

### Task 4: Tarea 4
**Explicación:**
4. 1. en0
   2. 192.168.64.1

### Task 5: Tarea 5
**Explicación:**
5. 1. thm
   2. count to 5
   3. Jan 19 07:52:43

### Task 6: Tarea 6
**Explicación:**
6. 1. vim creds.txt
   2. 452AEA93-AEE7-420B-871E-C57053E15DD0
   3. 2025-01-19 15:52:33
   4. 176

### Task 7: Tarea 7
**Explicación:**
7. 1. Open in list view
   2. Recents

### Task 8: Tarea 8
**Explicación:**
8. bluetooth/isConnected

### Task 9: Tarea 9
**Explicación:**
9. No answer needed

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `apfs-fuse -v 4 mac-disk.img ~/mac` |
| 2.1 | `plistutil` |
| 3.1 | `2024-12-08 17:42:28` |
| 3.2 | `AE` |
| 3.3 | `2025-01-19 15:47:05` |
| 4.1 | `en0` |
| 4.2 | `192.168.64.1` |
| 5.1 | `thm` |
| 5.2 | `count to 5` |
| 5.3 | `Jan 19 07:52:43` |
| 6.1 | `vim creds.txt` |
| 6.2 | `452AEA93-AEE7-420B-871E-C57053E15DD0` |
| 6.3 | `2025-01-19 15:52:33` |
| 6.4 | `176` |
| 7.1 | `Open in list view` |
| 7.2 | `Recents` |
| 8.1 | `bluetooth/isConnected` |
| 9.1 | `No answer needed` |

---

**Metodología:**
1. Montar la imagen de disco con `apfs-fuse -v 4 mac-disk.img ~/mac`.
2. Parsear las plists con `plistutil`.
3. Analizar las preferencias del sistema: fechas de actividad, configuración de red (`en0`, `192.168.64.1`), TTY, archivo `creds.txt`, ventanas y carpetas recientes.
4. Revisar los artefactos Bluetooth (`bluetooth/isConnected`) para completar el análisis.

### Cadena de ataque / Attack Chain
1. Montaje de la imagen APFS.
2. Parseo de plists.
3. Análisis de preferencias, red, TTY y credenciales.
4. Revisión de artefactos Bluetooth.

**Learning chain:** apfs-fuse -> plistutil -> Preferencias -> Red -> TTY/creds -> Bluetooth.

**Lección:** *Los artefactos macOS se reconstruyen desde las plists y la estructura APFS: cada preferencia guarda fechas, rutas y valores clave de la actividad del usuario.*

**MITRE ATT&CK:**
- T1005 (Data from Local System)
- T1555 (Credentials from Password Stores)
- T1074 (Data Staged)

**Fuente:** [TryHackMe - macOS Forensics_ Artefacts](https://tryhackme.com/room/macosforensicsartefacts)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.