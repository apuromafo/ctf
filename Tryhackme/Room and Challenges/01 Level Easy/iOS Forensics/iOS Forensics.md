# iOS Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `iosforensics` | [TryHackMe](https://tryhackme.com/room/iosforensics) | 01 Level Easy | TryHackMe | iOS forensics, imágenes forenses, adquisición (iFunbox), trust certificate, análisis de backups y cookies | Adquirir y analizar la evidencia de un iPhone: creación de una imagen forense, extracción de datos y recuperación de pistas y flag de la investigación. |

---

**Contexto:** Sala de forensia iOS que trabaja sobre un archivo de imagen de un iPhone. Explica la preparación de los discos de destino (un disco duro vacío), la adquisición con herramientas como iFunbox (Direct Acquisition), la confianza del certificado y la interpretación de la evidencia extraída. La investigación culmina resolviendo los datos del caso: el remitente, el mensaje, el destinatario, el tema, el enlace y la dirección IP, además de la fuente y la flag final. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Preparar el destino con un disco duro vacío, crear y analizar la imagen forense, adquirir los datos del iPhone y seguir las pistas (mensajes, enlaces, IPs, cookies) hasta obtener la flag.
> **EN:** Prepare the destination with an empty hard drive, create and analyse the forensic image, acquire the iPhone data and follow the clues (messages, links, IPs, cookies) until the flag is recovered.

## Solucionario

### Task 1: Introducción a la forensia iOS / iOS Forensics Basics
**Explicación:** Se presentan los fundamentos de la investigación forense sobre iPhone.

1. No answer needed

### Task 2: Preparación del destino / Target Preparation
**Explicación:** Se prepara el medio de destino para la adquisición y se identifica el tipo de archivo de evidencia resultante.

1. an empty hard drive
2. Image

### Task 3: Adquisición / Acquisition
**Explicación:** Se abordan los conceptos teóricos de la adquisición de evidencia.

1. No answer needed

### Task 4: Preparación del dispositivo / Device Preparation
**Explicación:** Se revisan los pasos previos a la extracción del dispositivo.

1. No answer needed

### Task 5: Configuración de herramientas / Tool Setup
**Explicación:** Se preparan las herramientas necesarias para el análisis.

1. No answer needed

### Task 6: Herramientas de adquisición / Acquisition Tools
**Explicación:** Se identifica la herramienta usada para la adquisición directa del iPhone y se confía el certificado.

1. iFunbox
2. Direct Acquisition
3. Trust Certificate

### Task 7: Datos extraídos / Extracted Data
**Explicación:** Se revisan los datos obtenidos de la extracción inicial.

1. No answer needed

### Task 8: Análisis de mensajes / Message Analysis
**Explicación:** Se inspeccionan los mensajes y datos de contacto de la evidencia.

1. No answer needed

### Task 9: Investigación del caso / Case Investigation
**Explicación:** Se resuelve el caso con los datos de la evidencia: el remitente, el contenido del mensaje, el receptor, el tema, el enlace, la IP, la aplicación de origen y la flag.

1. Lewis Randall
2. Did you get the goods?
3. Jenny
4. Transportation
5. https://blog.cmnatic.co.uk
6. 51.32.56.12
7. TryHackMe
8. THM{COOKIES!!!}

### Task 10: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre el flujo forense completo.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | Disco de destino / Destination drive | `an empty hard drive` |
| 3 | Tipo de evidencia / Evidence type | `Image` |
| 4 | (Pregunta 4 no especificada en el original) | `No answer needed` |
| 5 | (Pregunta 5 no especificada en el original) | `No answer needed` |
| 6 | (Pregunta 6 no especificada en el original) | `No answer needed` |
| 7 | Herramienta de adquisición / Acquisition tool | `iFunbox` |
| 8 | Método de adquisición / Acquisition method | `Direct Acquisition` |
| 9 | Confianza del certificado / Trust certificate | `Trust Certificate` |
| 10 | (Pregunta 10 no especificada en el original) | `No answer needed` |
| 11 | (Pregunta 11 no especificada en el original) | `No answer needed` |
| 12 | Remitente del mensaje / Message sender | `Lewis Randall` |
| 13 | Contenido del mensaje / Message content | `Did you get the goods?` |
| 14 | Destinatario / Recipient | `Jenny` |
| 15 | Tema del mensaje / Message subject | `Transportation` |
| 16 | Enlace del mensaje / Message link | `https://blog.cmnatic.co.uk` |
| 17 | Dirección IP / IP address | `51.32.56.12` |
| 18 | Aplicación de origen / Source application | `TryHackMe` |
| 19 | Flag final / Final flag | `THM{COOKIES!!!}` |
| 20 | (Pregunta 20 no especificada en el original) | `No answer needed` |

---

**Metodología:** Preparar un disco de destino vacío, adquirir y analizar la imagen forense del iPhone, realizar la extracción con iFunbox tras confiar el certificado e interpretar los mensajes, enlaces, IPs y cookies para reconstruir el caso y obtener la flag.

### Cadena de ataque / Attack Chain

```text
disco de destino vacío -> imagen forense -> iFunbox (Direct Acquisition) -> Trust Certificate -> extracción de mensajes -> Lewis Randall -> Jenny -> tema Transportation -> enlace https://blog.cmnatic.co.uk -> IP 51.32.56.12 -> TryHackMe -> THM{COOKIES!!!}
```

**Learning chain:** forensia iOS -> preparación del destino -> adquisición de imagen -> extracción (iFunbox) -> análisis de mensajes y cookies -> reconstrucción del caso -> flag.

**Lección:** *La evidencia móvil vive en mensajes, metadatos y cookies: una adquisición limpia sobre un destino preparado y el análisis sistemático del contenido permiten reconstruir la comunicación completa y cerrar el caso con la prueba final.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1555 (Credentials from Password Stores), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - iOS Forensics](https://tryhackme.com/room/iosforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.