# MBR and GPT Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Boot & MBR | mbrandgptanalysis | https://tryhackme.com/room/mbrandgptanalysis | 02 Level Medium | TryHackMe | MBR, GPT, bootkits, análisis forense de disco | Detección y análisis de bootkits MBR/EFI |

---

**Contexto:** La sala **MBR and GPT Analysis** aborda el análisis forense del **Master Boot Record** (MBR) y de la **GUID Partition Table** (GPT), así como los **bootkits** que se ocultan en esas zonas de inicio. Se examinan las particiones, el código del bootloader, las firmas de arranque y se practica la detección de infecciones MBR y EFI sobre imágenes de disco con herramientas forenses.

## Solucionario

### Task 1: Conceptos iniciales
**Explicación:**

Introducción a la estructura de **particiones** de un disco y a los programas maliciosos que las atacan durante el arranque (**bootkits**).

1. `partitions`
2. `bootkits`

### Task 2: Secuencia de arranque
**Explicación:**

Se explica el proceso de arranque: la secuencia comienza con el **Power-On-Self-Test**, continúa con la selección del dispositivo mediante **UEFI** y finaliza con la carga desde el **bootable device**.

1. `Power-On-Self-Test`
2. `UEFI`
3. `bootable device`

### Task 3: Anatomía del MBR
**Explicación:**

Se estudia la estructura del sector de arranque: contiene la **partition table**, ocupa **512** bytes, empieza con el **bootloader code** y termina con la firma `55 AA`. El MBR permite un máximo de **4** particiones primarias y cada entrada de partición ocupa **16** bytes.

1. `partition table`
2. `512 `
3. `bootloader code`
4. `55 AA`
5. `4`
6. `16`

### Task 4: Ejercicio de análisis
**Explicación:**

Preparación de la máquina virtual para el análisis forense de la imagen de disco.

Respuesta: `No answer needed`

### Task 5: Análisis MBR de la imagen
**Explicación:**

Analizando la imagen con herramientas forenses se identifica la partición de interés (`1`), se localiza el proceso de arranque alternativo (`EB`), el tipo de sistema de archivos `NTFS`, el tamaño de la partición (`32`) y, tras revisar el sector de arranque, se recupera la flag `THM{Cure_The_MBR}`.

1. `1`
2. `EB`
3. `NTFS`
4. `32`
5. `THM{Cure_The_MBR}`

### Task 6: Estructura GPT
**Explicación:**

Se examina la estructura GPT: el número máximo de entradas de partición es **128** y el GUID de la partición del sistema EFI es `E3C9E316-0B5C-4DB8-817D-F92DF00215AE`.

1. `128`
2. `E3C9E316-0B5C-4DB8-817D-F92DF00215AE`

### Task 7: Análisis GPT de la imagen
**Explicación:**

Aplicación del análisis forense sobre la imagen con particionado GPT.

Respuesta: `No answer needed`

### Task 8: Bootkit EFI
**Explicación:**

Se detecta el bootkit EFI oculto en la **EFI System Partition** y, al desactivarlo o arrancar, el mensaje que muestra (`Hello, EFI Bootkit!`).

1. `EFI System Partition`
2. `Hello, EFI Bootkit!`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Estructura que traza las particiones | `partitions` |
| 1.2 | Malware que infecta el sector de arranque | `bootkits` |
| 2.1 | Primer paso del arranque | `Power-On-Self-Test` |
| 2.2 | Firmware que selecciona el dispositivo | `UEFI` |
| 2.3 | Dispositivo desde el que se arranca | `bootable device` |
| 3.1 | Tabla que contiene el MBR | `partition table` |
| 3.2 | Tamaño del sector de arranque | `512 ` |
| 3.3 | Código inicial del MBR | `bootloader code` |
| 3.4 | Firma de arranque | `55 AA` |
| 3.5 | Número máximo de particiones primarias | `4` |
| 3.6 | Tamaño de cada entrada de partición | `16` |
| 4 | Preparación del análisis | `No answer needed` |
| 5.1 | Partición analizada | `1` |
| 5.2 | Proceso de arranque alternativo | `EB` |
| 5.3 | Tipo de sistema de archivos | `NTFS` |
| 5.4 | Tamaño de la partición | `32` |
| 5.5 | Flag recuperada del MBR | `THM{Cure_The_MBR}` |
| 6.1 | Máximo de entradas de partición GPT | `128` |
| 6.2 | GUID de la partición EFI | `E3C9E316-0B5C-4DB8-817D-F92DF00215AE` |
| 7 | Análisis GPT de la imagen | `No answer needed` |
| 8.1 | Partición donde se oculta el bootkit | `EFI System Partition` |
| 8.2 | Mensaje mostrado por el bootkit | `Hello, EFI Bootkit!` |

---

**Metodología:** Anatomía del arranque (POST → UEFI → bootable device), análisis del sector MBR (particiones, firma `55 AA`), análisis de la tabla GPT y detección de bootkits MBR/EFI con herramientas forenses de imagen.

**Learning chain:** Secuencia de arranque → estructura MBR → particiones/firmas → forense de imagen → GPT/EFI → detección y neutralización de bootkits.

**Lección:** *El sector de arranque (MBR/GPT) es lo primero que carga el sistema: auditarlo revela bootkits que sobreviven al formateo convencional del sistema operativo.*

**MITRE ATT&CK:** T1542 Pre-OS Boot / Bootkit.

**Fuente:** [TryHackMe - MBR and GPT Analysis](https://tryhackme.com/room/mbrandgptanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.