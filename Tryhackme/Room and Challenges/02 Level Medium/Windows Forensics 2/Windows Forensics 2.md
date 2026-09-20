# Windows Forensics 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Walkthrough | windowsforensics2 | https://tryhackme.com/room/windowsforensics2 | 02 Level Medium | TryHackMe | Análisis forense, imagen USB, sistema de archivos, artefactos de ejecución, timestamps | Reconstrucción de un incidente de exfiltración de datos vía dispositivo USB |

---

**Contexto:** La sala **Windows Forensics 2** es un ejercicio práctico de análisis forense sobre la imagen de un dispositivo USB empleado para extraer información confidencial de una máquina Windows. Se analiza la geometría del dispositivo (bits por sector, número de lados, sistema de archivos), los tamaños de clúster, los archivos involucrados en la fuga, la línea de tiempo de ejecución y los artefactos de instalación de dispositivos. Cada hallazgo se confirma respondiendo con los valores exactos obtenidos del análisis.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación del escenario forense, montaje de la evidencia y preparación de las herramientas de análisis. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Análisis del dispositivo USB / USB device analysis
**Explicación:**

Se examina la configuración física y lógica del dispositivo USB incautado a partir de los datos de la imagen y del sistema.

1. `28 bits`
2. `4`
3. `exFAT`

### Task 3: Geometría del dispositivo / Device geometry
**Explicación:**

Se determinan los valores de geometría del dispositivo y del sistema de archivos, como el tamaño del sector y del clúster.

1. `49152`
2. `4096`

### Task 4: Archivos de la exfiltración / Exfiltration files
**Explicación:**

Se identifican los archivos presentes en el dispositivo involucrados en la fuga de información.

1. `Tryhackme.xlsx`
2. `TryHackMe2.txt`
3. `thm-4n6-2-4`

### Task 5: Línea de tiempo de ejecución / Execution timeline
**Explicación:**

Se reconstruye la línea de tiempo del incidente: ejecuciones, duraciones y programas implicados en la copia de los datos.

1. `2`
2. `12/01/2021 13:04`
3. `00:00:41`
4. `Notepad.exe`

### Task 6: Marcas de tiempo de los archivos / File timestamps
**Explicación:**

Se recuperan las marcas de tiempo de creación y modificación de los archivos claves del incidente.

1. `12/1/2021 13:01`
2. `12/1/2021 12:31`

### Task 7: Instalación de dispositivos / Device installation
**Explicación:**

Se identifica el artefacto del sistema que registra la instalación y conexión del dispositivo USB.

Respuesta: `Setupapi.dev.log`

### Task 8: Cierre / Conclusion
**Explicación:**

Recapitulación de los hallazgos forenses. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción al análisis forense | `No answer needed` |
| 2.1 | Bits por sector del dispositivo | `28 bits` |
| 2.2 | Número de lados/sectores del dispositivo | `4` |
| 2.3 | Sistema de archivos del dispositivo | `exFAT` |
| 3.1 | Primer valor de geometría | `49152` |
| 3.2 | Segundo valor de geometría | `4096` |
| 4.1 | Archivo exfiltrado 1 | `Tryhackme.xlsx` |
| 4.2 | Archivo exfiltrado 2 | `TryHackMe2.txt` |
| 4.3 | Artefacto/etiqueta de la exfiltración | `thm-4n6-2-4` |
| 5.1 | Número de ejecuciones relacionadas | `2` |
| 5.2 | Fecha/hora de ejecución | `12/01/2021 13:04` |
| 5.3 | Duración de la ejecución | `00:00:41` |
| 5.4 | Programa implicado en la copia | `Notepad.exe` |
| 6.1 | Marca de tiempo 1 | `12/1/2021 13:01` |
| 6.2 | Marca de tiempo 2 | `12/1/2021 12:31` |
| 7 | Artefacto de instalación de dispositivos | `Setupapi.dev.log` |
| 8 | Cierre del análisis | `No answer needed` |

---

**Metodología:** Análisis forense de la imagen de un dispositivo USB y de los artefactos del sistema Windows: inspección de geometría y sistema de archivos, recuperación de archivos, correlación de timestamps y revisión de logs de instalación (Setupapi.dev.log) para reconstruir la secuencia de exfiltración.

### Cadena de ataque / Attack Chain

```text
Incautación de la imagen USB → análisis de geometría/configuración → localización de archivos exfiltrados → correlación de timestamps → artefactos de instalación → reconstrucción del incidente
```

**Learning chain:** Montaje de evidencia → análisis de sistema de archivos → identificación de archivos → línea de tiempo → timestamps → artefactos de instalación → conclusión forense.

**Lección:** *En un caso de exfiltración por USB, la geometría del medio, los timestamps y los logs de instalación forman una cadena de evidencia que reconstruye el incidente sin depender de testimonios.*

**MITRE ATT&CK:** T1005 Data from Local System · T1025 Data from Removable Media · T1083 File and Directory Discovery · T1070 Indicator Removal.

**Fuente:** [TryHackMe - Windows Forensics 2](https://tryhackme.com/room/windowsforensics2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.