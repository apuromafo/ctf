# Diskrupt

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Walkthrough | `diskrupt` | https://tryhackme.com/room/diskrupt | 03 Level Hard | TryHackMe | DFIR / forense de disco / particiones / FAT/NTFS / hexeditor / volcado de memoria / ransomware/wiper / timeline | Sala DFIR sobre un incidente de borrado de disco: recuperar de los artefactos del sistema los sectores tipo ACBD, direcciones hexadecimales, tamaños, fechas y nombres de un documento sensible junto al binario wiper `diskwipe.exe` y la flag del caso. |

---

**Contexto:** Sala DFIR centrada en la interrupción (wiper/borrado) de un disco. La única tarea recoge doce valores forenses: un identificador de sector (`ACBD`), direcciones de memoria o de cluster en hexadecimal (`0x01387800`), tamaños (`30.23`, `9.76`, `163896`), las horas de creación y último acceso, el nombre del PDF sensible (`Quantum-Resistant Cryptographic Algorithms.pdf`), direcciones/offsets de recuperación (`4E7B0E000`, `4E7B0E43D`), la flag del caso y el binario responsable del wiper (`diskwipe.exe`).

> **ES:** "Sala DFIR de análisis de un disco interrumpido (wiper): recupera sectores, direcciones, fechas y el binario diskwipe.exe responsable del incidente."
> **EN:** "DFIR room analyzing a interrupted (wiped) disk: recover sectors, addresses, dates and the diskwipe.exe binary responsible for the incident."

## Solucionario

### Task 1: Análisis forense del disco / Disk forensic analysis

**Explicación:** Tarea única con las doce respuestas de la investigación forense del disco. Se conservan los valores exactos, incluido el formato hexadecimal y las fechas. Contenido original de la tarea:

```text
1. 1. ACBD
   2. 0x01387800
   3. 30.23
   4. 9.76
   5. 2025-03-19 22:01:57
   6. Quantum-Resistant Cryptographic Algorithms.pdf
   7. 2025-03-20 00:44:37
   8. 163896
   9. 4E7B0E000
   10. 4E7B0E43D
   11. FLAG:{RECOVERED_SECRET_THM}
   12. diskwipe.exe
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identificador de sector encontrado en el análisis. | `ACBD` |
| 2 | Dirección en hexadecimal del artefacto. | `0x01387800` |
| 3 | Tamaño en MB del documento. | `30.23` |
| 4 | Tamaño en MB de otra parte del artefacto. | `9.76` |
| 5 | Fecha y hora de creación del documento. | `2025-03-19 22:01:57` |
| 6 | Nombre del documento sensible. | `Quantum-Resistant Cryptographic Algorithms.pdf` |
| 7 | Fecha y hora del último acceso/modificación. | `2025-03-20 00:44:37` |
| 8 | Tamaño en bytes (sector de lectura). | `163896` |
| 9 | Offset/dirección de recuperación 1. | `4E7B0E000` |
| 10 | Offset/dirección de recuperación 2. | `4E7B0E43D` |
| 11 | Flag del caso. | `FLAG:{RECOVERED_SECRET_THM}` |
| 12 | Binario responsable del borrado del disco. | `diskwipe.exe` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identificador de sector encontrado en el análisis. | `ACBD` |
| 2 | Dirección en hexadecimal del artefacto. | `0x01387800` |
| 3 | Tamaño en MB del documento. | `30.23` |
| 4 | Tamaño en MB de otra parte del artefacto. | `9.76` |
| 5 | Fecha y hora de creación del documento. | `2025-03-19 22:01:57` |
| 6 | Nombre del documento sensible. | `Quantum-Resistant Cryptographic Algorithms.pdf` |
| 7 | Fecha y hora del último acceso/modificación. | `2025-03-20 00:44:37` |
| 8 | Tamaño en bytes (sector de lectura). | `163896` |
| 9 | Offset/dirección de recuperación 1. | `4E7B0E000` |
| 10 | Offset/dirección de recuperación 2. | `4E7B0E43D` |
| 11 | Flag del caso. | `FLAG:{RECOVERED_SECRET_THM}` |
| 12 | Binario responsable del borrado del disco. | `diskwipe.exe` |

---

**Metodología:**
1. Montar/imagenear el disco y localizar los sectores marcados con `ACBD`.
2. Inspeccionar en hexadecimal el área señalada (`0x01387800`) y registrar tamaños y offsets.
3. Documentar las fechas de creación y último acceso del PDF sensible.
4. Identificar el binario wiper `diskwipe.exe` como causa del borrado.

### Cadena de ataque / Attack Chain

```text
Imagen del disco -> sectores ACBD -> 0x01387800 -> Quantum-Resistant Cryptographic Algorithms.pdf -> fechas -> offsets 4E7B0E000/4E7B0E43D -> FLAG:{RECOVERED_SECRET_THM} -> diskwipe.exe
```

**Learning chain:** `Forense de disco -> sectores/signatures -> hex -> documento PDF -> timeline -> wiper diskwipe.exe -> flag`

**Lección:** *Los borrados de disco dejan firmas y áreas hexadecimales recuperables; el binario wiper (`diskwipe.exe`) y los offsets re-ensamblados permiten reconstruir el documento exfiltrado.*

**MITRE ATT&CK:** T1485 (Data Destruction), T1561.001 (Disk Wipe), T1005 (Data from Local System), T1070.004 (Indicator Removal on Host: File Deletion)

**Fuente:** [TryHackMe - Diskrupt](https://tryhackme.com/room/diskrupt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.