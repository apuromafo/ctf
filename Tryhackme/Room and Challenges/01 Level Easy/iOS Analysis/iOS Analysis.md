# iOS Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `iosanalysis` | [TryHackMe](https://tryhackme.com/room/iosanalysis) | 01 Level Easy | TryHackMe | iOS, análisis forense móvil, extracción de backups, APFS, keychains, libimobiledevice, iFunbox | Aprender a analizar dispositivos iOS: confiar el certificado, extraer backups con libimobiledevice y recuperar datos de aplicaciones y contactos. |

---

**Contexto:** Sala de análisis forense de dispositivos iOS. Explica los pasos previos a la extracción: confiar el certificado del dispositivo, gestionar el bloqueo por tiempo, el rastreo de Find My y la opción de cifrado del backup y el uso de la bolsa de Faraday. Repasa el sistema de archivos APFS y sus volúmenes, las rutas relevantes de datos de aplicación (/HomeDomain/Library/AddressBook) y de los keychains (/var/keychains), y herramientas como libimobiledevice para realizar backups. Incluye la práctica sobre los datos del dispositivo analizado (contactos, usuarios y fechas). El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Preparar el dispositivo (certificado, Find My, cifrado), conocer el sistema de archivos APFS y sus rutas, realizar la extracción con idevicebackup2 y resolver las preguntas sobre los datos recuperados del iPhone.
> **EN:** Prepare the device (certificate, Find My, encryption), learn the APFS filesystem and its paths, perform the extraction with idevicebackup2 and answer the questions about the recovered iPhone data.

## Solucionario

### Task 1: Introducción al análisis iOS / iOS Analysis Basics
**Explicación:** Se presentan los fundamentos del análisis forense sobre dispositivos iOS.

1. No answer needed

### Task 2: Confianza y cifrado / Trust and Encryption
**Explicación:** Se aborda la confianza del certificado del equipo y el periodo de validez de esa confianza.

1. Trust Certificate
2. 30 Days

### Task 3: Preparación del dispositivo / Device Preparation
**Explicación:** Se gestionan las características del dispositivo que afectan a la extracción: Find My, el cifrado de los datos y el aislamiento con la bolsa de Faraday.

1. Find My
2. Encrypted
3. Faraday Bag

### Task 4: Sistema de archivos / Filesystem
**Explicación:** Se identifica el sistema de archivos de los dispositivos iOS modernos y uno de sus volúmenes principales.

1. APFS
2. System

### Task 5: Rutas de datos / Data Paths
**Explicación:** Se localizan las rutas de los datos de la agenda del dispositivo y de los keychains.

1. /HomeDomain/Library/AddressBook
2. /var/keychains

### Task 6: Extracción / Extraction
**Explicación:** Se utilizan las herramientas de libimobiledevice para realizar la extracción completa del backup.

1. libimobiledevice
2. idevicebackup2 backup --full ./backup

### Task 7: Data del dispositivo / Device Data
**Explicación:** Se resuelven las preguntas sobre los datos recuperados del dispositivo: la aplicación de interés, los contactos y la fecha relevante.

1. No answer needed
2. OneMinuteStaff
3. Wayne,Garcey
4. 30/03/2024

### Task 8: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre el flujo completo de análisis de un dispositivo iOS.

1. No answer needed
2. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | Confianza del certificado / Trust certificate | `Trust Certificate` |
| 3 | Periodo de validez de la confianza / Trust validity period | `30 Days` |
| 4 | Localización del dispositivo / Device location service | `Find My` |
| 5 | Estado del cifrado / Encryption state | `Encrypted` |
| 6 | Aislamiento de señales / Signal isolation | `Faraday Bag` |
| 7 | Sistema de archivos iOS / iOS filesystem | `APFS` |
| 8 | Volumen principal / Main volume | `System` |
| 9 | Ruta de la agenda / AddressBook path | `/HomeDomain/Library/AddressBook` |
| 10 | Ruta de los keychains / Keychains path | `/var/keychains` |
| 11 | Librería de extracción / Extraction library | `libimobiledevice` |
| 12 | Comando de backup completo / Full backup command | `idevicebackup2 backup --full ./backup` |
| 13 | (Pregunta 13 no especificada en el original) | `No answer needed` |
| 14 | Aplicación de interés / App of interest | `OneMinuteStaff` |
| 15 | Contactos identificados / Identified contacts | `Wayne,Garcey` |
| 16 | Fecha relevante / Relevant date | `30/03/2024` |
| 17 | (Pregunta 17 no especificada en el original) | `No answer needed` |
| 18 | (Pregunta 18 no especificada en el original) | `No answer needed` |

---

**Metodología:** Preparar el dispositivo (confiar certificado, desactivar Find My, gestionar cifrado y aislar señales), conocer el sistema de archivos APFS y las rutas de datos, realizar el backup con idevicebackup2 y analizar el contenido extraído para responder sobre aplicaciones, contactos y fechas.

### Cadena de ataque / Attack Chain

```text
certificado Trust -> 30 días de validez -> Find My/encrypted/Faraday Bag -> APFS (System) -> rutas de datos y keychains -> libimobiledevice -> idevicebackup2 backup --full -> análisis del backup -> datos del dispositivo
```

**Learning chain:** análisis iOS -> confianza y cifrado -> preparación del dispositivo -> APFS -> rutas de datos -> extracción (libimobiledevice) -> interpretación de datos.

**Lección:** *La extracción forense de iOS depende de preparar correctamente el dispositivo (confianza, cifrado, aislamiento) y de conocer el sistema de archivos y las rutas donde viven los datos, para después interpretar el backup recuperado.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1204 (User Execution), T1552 (Unsecured Credentials), T1546 (Event Triggered Execution)

**Fuente:** [TryHackMe - iOS Analysis](https://tryhackme.com/room/iosanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.