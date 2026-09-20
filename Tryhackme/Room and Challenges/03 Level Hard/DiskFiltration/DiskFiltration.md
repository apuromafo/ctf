# DiskFiltration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Walkthrough | `diskfiltration` | https://tryhackme.com/room/diskfiltration | 03 Level Hard | TryHackMe | DFIR / forense de almacenamiento / Volatility / particiones / passwords ZIP / WMI / Win32_Share / timeline | Sala de forensía de disco vinculada a un caso de exfiltración de datos: identificar el device conectado (iPhone), recuperar el plan ZIP cifrado, resolver contraseñas, cruzar la linea temporal de archivos y descubrir el comando usado para enumerar los recursos compartidos. |

---

**Contexto:** Sala DFIR sobre exfiltración de datos desde un dispositivo de almacenamiento. La investigación arranca por una tarea de contexto sin respuesta y continúa con trece respuestas forenses: el ID del dispositivo conectado, el dispositivo (`Liam's Iphone`), el plan de exfiltración en un ZIP (`Shadow_Plan.zip`), la contraseña del archivo (`Qwerty@123`), el propietario y el tipo de archivo, las categorías de datos filtrados, el nombre del proyecto y el plan, la fecha y el número de secreto, la flag técnica, la última hora de acceso, la URL del plan y el comando PowerShell (WMI) que lista los recursos compartidos (`Win32_Share`).

> **ES:** "Investiga la exfiltración de datos por un dispositivo de almacenamiento: recupera el plan ZIP, resuelve contraseñas y encuentra el comando WMI que enumeró los recursos compartidos."
> **EN:** "Investigate data exfiltration through a storage device: recover the ZIP plan, crack passwords and find the WMI command that enumerated the shared resources."

## Solucionario

### Task 1: Contexto del caso / Case context

**Explicación:** Tarea de contexto e introducción al caso de exfiltración de datos. No requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer el contexto del caso. | `No answer needed` |

### Task 2: Investigación forense / Forensic investigation

**Explicación:** Trece respuestas de la investigación forense del dispositivo de almacenamiento. Se conservan los valores exactos, incluidos plurales, comas y espacios. Contenido original de la tarea:

```text
2. 1. 2651931097993496666
   2. Liam's Iphone
   3. Shadow_Plan.zip
   4. Qwerty@123
   5. Henry
   6. PNG
   7. Financial, Revenue
   8. Critical Data TECH THM, Exfiltration Plan
   9. 2025-01-29 11:26:09, 2
   10. FLAGT{THM_TECH_DATA}
   11. 2025-01-29 11:29:02
   12. https://www.facebook.com/
   13. Get-WmiObject -Class Win32_Share | Select-Object Name, Path
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ID del dispositivo de almacenamiento conectado. | `2651931097993496666` |
| 2 | Nombre del dispositivo/iPhone del caso. | `Liam's Iphone` |
| 3 | Archivo del plan de exfiltración. | `Shadow_Plan.zip` |
| 4 | Contraseña del archivo ZIP. | `Qwerty@123` |
| 5 | Propietario del archivo. | `Henry` |
| 6 | Tipo/formato del archivo. | `PNG` |
| 7 | Categorías de datos filtrados. | `Financial, Revenue` |
| 8 | Nombre del proyecto y del plan de exfiltración. | `Critical Data TECH THM, Exfiltration Plan` |
| 9 | Fecha de creación y número del secreto. | `2025-01-29 11:26:09, 2` |
| 10 | Flag técnica del caso. | `FLAGT{THM_TECH_DATA}` |
| 11 | Última hora de acceso del archivo. | `2025-01-29 11:29:02` |
| 12 | URL del plan de exfiltración. | `https://www.facebook.com/` |
| 13 | Comando PowerShell usado para enumerar los recursos compartidos. | `Get-WmiObject -Class Win32_Share | Select-Object Name, Path` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer el contexto del caso. | `No answer needed` |
| 2 | ID del dispositivo de almacenamiento conectado. | `2651931097993496666` |
| 3 | Nombre del dispositivo/iPhone del caso. | `Liam's Iphone` |
| 4 | Archivo del plan de exfiltración. | `Shadow_Plan.zip` |
| 5 | Contraseña del archivo ZIP. | `Qwerty@123` |
| 6 | Propietario del archivo. | `Henry` |
| 7 | Tipo/formato del archivo. | `PNG` |
| 8 | Categorías de datos filtrados. | `Financial, Revenue` |
| 9 | Nombre del proyecto y del plan de exfiltración. | `Critical Data TECH THM, Exfiltration Plan` |
| 10 | Fecha de creación y número del secreto. | `2025-01-29 11:26:09, 2` |
| 11 | Flag técnica del caso. | `FLAGT{THM_TECH_DATA}` |
| 12 | Última hora de acceso del archivo. | `2025-01-29 11:29:02` |
| 13 | URL del plan de exfiltración. | `https://www.facebook.com/` |
| 14 | Comando PowerShell usado para enumerar los recursos compartidos. | `Get-WmiObject -Class Win32_Share | Select-Object Name, Path` |

---

**Metodología:**
1. Analizar el dispositivo de almacenamiento conectado al sistema (identificar `2651931097993496666`).
2. Examinar la imagen/imagenes del iPhone y localizar el plan `Shadow_Plan.zip`.
3. Recuperar/descifrar la contraseña del ZIP (`Qwerty@123`) y extraer su contenido (plan, PNG, categorías y proyecto).
4. Construir la línea temporal del caso: creación (`2025-01-29 11:26:09`) y último acceso (`2025-01-29 11:29:02`).
5. Enumerar los recursos compartidos con WMI y documentar el comando del atacante.

### Cadena de ataque / Attack Chain

```text
Dispositivo 2651931097993496666 -> Liam's Iphone -> Shadow_Plan.zip -> Qwerty@123 -> plan PNG -> categorías Financial, Revenue -> Critical Data TECH THM -> FLAGT{THM_TECH_DATA} -> Win32_Share (WMI)
```

**Learning chain:** `Forense de dispositivo -> iPhone -> ZIP cifrado -> crackear ZIP -> plan de exfiltración -> linea temporal -> comando WMI Win32_Share`

**Lección:** *La exfiltración deja rastro en el almacenamiento: desde el dispositivo conectado y el ZIP cifrado del plan hasta el comando WMI (`Get-WmiObject -Class Win32_Share | Select-Object Name, Path`) que el atacante usó para localizar los recursos compartidos.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1560.001 (Archive Collected Data), T1074 (Data Staged), T1041 (Exfiltration Over C2 Channel), T1059.001 (PowerShell)

**Fuente:** [TryHackMe - DiskFiltration](https://tryhackme.com/room/diskfiltration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.