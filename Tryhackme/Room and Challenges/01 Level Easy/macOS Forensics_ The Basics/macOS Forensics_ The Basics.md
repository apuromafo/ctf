# macOS Forensics_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `macosforensicsthebasics` | [TryHackMe](https://tryhackme.com/room/macosforensicsthebasics) | 01 Level Easy | TryHackMe | macOS forensics / APFS / diskutil / mount points / .kext / SIP / csrutil / plist files | Fundamentos de la forensia digital en macOS: estructura de archivos APFS, volúmenes, seguridad del kernel y extracción de datos relevantes |

---

**Contexto:** Sala introductoria a la forensia digital en sistemas macOS. Se cubren las bases del sistema de archivos APFS, la estructura de volúmenes y catálogos, los puntos de montaje, las extensiones del kernel (kext), el mecanismo de protección SIP y los comandos esenciales como `diskutil` y `csrutil` para el análisis forense de un sistema Mac.

## Solucionario

### Task 1

**Explicación:** Pregunta introductoria conceptual, no requiere respuesta escrita.

1. No answer needed

### Task 2

**Explicación:** Se identifican datos sobre el sistema de archivos APFS: la versión de formato y el tipo de estructura correspondiente.

1. 2017
2. APFS

### Task 3

**Explicación:** Se profundiza en la estructura APFS: la fecha límite de detección del sistema y el componente que agrupa los metadatos de archivos y directorios.

1. 06/02/2040
2. Catalog file

### Task 4

**Explicación:** Se utiliza el comando del sistema necesario para listar los volúmenes APFS del disco.

1. diskutil apfs list

### Task 5

**Explicación:** Se identifican los tipos de volúmenes en los que se organiza la información del sistema macOS.

1. System
2. User

### Task 6

**Explicación:** Los datos forenses de rutinas de kernel se extraen de las extensiones de kernel; la respuesta es el tipo de archivo correspondiente.

1. .kext files

### Task 7

**Explicación:** El comando que desactiva la Protección de Integridad del Sistema (SIP) en macOS.

1. csrutil disable

### Task 8

**Explicación:** Los análisis de un sistema comprometido requieren identificar claves de cifrado, usuarios y material de credenciales; las respuestas corresponden a la clave de volumen, el usuario, el archivo y su contenido.

1. 84E5F2BD-503F-4E3A-8105-EEBEBC1925B4
2. thm
3. creds.txt
4. 12345

### Task 9

**Explicación:** Pregunta final, no requiere respuesta escrita.

1. No answer needed

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2 | `2017` |
| 3 | Task 2 | `APFS` |
| 4 | Task 3 | `06/02/2040` |
| 5 | Task 3 | `Catalog file` |
| 6 | Task 4 | `diskutil apfs list` |
| 7 | Task 5 | `System` |
| 8 | Task 5 | `User` |
| 9 | Task 6 | `.kext files` |
| 10 | Task 7 | `csrutil disable` |
| 11 | Task 8 | `84E5F2BD-503F-4E3A-8105-EEBEBC1925B4` |
| 12 | Task 8 | `thm` |
| 13 | Task 8 | `creds.txt` |
| 14 | Task 8 | `12345` |
| 15 | Task 9 | No answer needed |

---

**Metodología:** Se revisa de forma progresiva la anatomía de un sistema macOS: estructura del sistema de archivos APFS con sus volúmenes y catálogos, el uso de `diskutil apfs list` para enumerar volúmenes, la distinción entre volúmenes System y User, la extracción de datos de extensiones de kernel (kext), la desactivación de SIP con `csrutil disable` y, finalmente, la recuperación de claves de cifrado y credenciales del disco analizado.

### Cadena de ataque / Attack Chain

```text
estructura APFS -> enumeración de volúmenes con diskutil -> volúmenes System/User -> análisis de kext files -> desactivación de SIP (csrutil disable) -> recuperación de clave de cifrado -> extracción de credenciales
```

**Learning chain:** APFS basics → diskutil → volume structure → kext extensions → SIP/csrutil → encryption keys → credential recovery

**Lección:** *Conocer la estructura de archivos y los mecanismos de protección de macOS (APFS, SIP, kext) es imprescindible para extraer de forma fiable las evidencias de un sistema comprometido.*

**MITRE ATT&CK:** T1547.001 (Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder), T1059.004 (Command and Scripting Interpreter: Unix Shell)

**Fuente:** [TryHackMe - macOS Forensics_ The Basics](https://tryhackme.com/room/macosforensicsthebasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.