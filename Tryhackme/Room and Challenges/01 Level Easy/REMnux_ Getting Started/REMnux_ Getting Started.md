# REMnux_ Getting Started

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `remnuxgettingstarted` | https://tryhackme.com/room/remnuxgettingstarted | 01 Level Easy | TryHackMe | REMnux / oledump.py / PowerShell / análisis de malware / PsTree / PsList / strings | Análisis de malware con REMnux: de la extracción del documento malicioso con oledump.py y la cadena de descarga en PowerShell hasta la identificación del proceso suplantado y el payload oculto. |

---

**Contexto:** Sala práctica de malware analysis con REMnux. Se analiza un documento malicioso (PDF/Office) con oledump.py y la opción `-s`, siguiendo la cadena de descarga que usa `Invoke-WebRequest` de PowerShell para traer el ejecutable `Doc-3737122pdf.exe` a `$TempFile`. En el laboratorio se obtiene una flag y se estudia el árbol de procesos (PsTree, PsList) y las cadenas (strings) para identificar procesos legítimos suplantados como `csrss.exe` y `winlogon.exe`, con el payload oculto en `C:\Intel\ivecuqmanpnirkt615`.

> **ES:** "REMnux Getting Started" — análisis de malware con REMnux: oledump.py, cadenas de descarga PowerShell, procesos y strings.
> **EN:** "REMnux Getting Started" — malware analysis with REMnux: oledump.py, PowerShell download chains, processes and strings.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala: qué es REMnux y cómo se usa para el análisis de malware. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |

### Task 2: Configuración del entorno / Environment Setup

**Explicación:** Preparación del entorno REMnux (máquina virtual y herramientas del laboratorio). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura el entorno REMnux. / Set up the REMnux environment. | `No answer needed` |

### Task 3: Análisis del documento malicioso / Malicious Document Analysis

**Explicación:** Se analiza el documento malicioso con `oledump.py` y su opción `-s` para volcar streams. El documento ejecuta una descarga con `Invoke-WebRequest`, que trae el ejecutable `Doc-3737122pdf.exe` y lo guarda en `$TempFile`. El archivo resultante tiene un tamaño esperado de `16` y el documento contiene `8` streams relevantes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta de REMnux analiza los streams OLE de un documento? / What REMnux tool analyzes the OLE streams of a document? | `oledump.py` |
| 2 | ¿Qué opción de oledump.py vuelca un stream concreto? / What oledump.py option dumps a specific stream? | `-s` |
| 3 | ¿Qué comando de PowerShell usa el documento para descargar el payload? / What PowerShell command does the document use to download the payload? | `Invoke-WebRequest` |
| 4 | ¿Cómo se llama el archivo ejecutable descargado? / What is the downloaded executable file called? | `Doc-3737122pdf.exe` |
| 5 | ¿En qué variable se guarda el archivo descargado? / In what variable is the downloaded file stored? | `$TempFile` |
| 6 | ¿Qué tamaño esperado tiene el archivo descargado? / What is the expected size of the downloaded file? | `16` |
| 7 | ¿Cuántos streams relevantes contiene el documento? / How many relevant streams does the document contain? | `8` |

### Task 4: Laboratorio del malware / Malware Lab

**Explicación:** En el laboratorio de detección se obtiene la flag `Tryhackme{remnux_edition}` y se identifica el método HTTP `GET` usado en la petición de descarga observada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag se obtiene en el laboratorio? / What flag is obtained in the lab? | `Tryhackme{remnux_edition}` |
| 2 | ¿Qué método HTTP utiliza la petición de descarga? / What HTTP method does the download request use? | `GET` |

### Task 5: Procesos y strings / Processes & Strings

**Explicación:** Se analiza el binario en ejecución: `PsTree` muestra el árbol de procesos y `PsList` lista los procesos activos, mientras `strings` extrae las cadenas del ejecutable. El malware suplanta procesos legítimos de Windows como `csrss.exe` y `winlogon.exe`, y el payload descargado se oculta en la ruta `C:\Intel\ivecuqmanpnirkt615`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta muestra el árbol de procesos? / What tool shows the process tree? | `PsTree` |
| 2 | ¿Qué herramienta lista los procesos en ejecución? / What tool lists the running processes? | `PsList` |
| 3 | ¿Qué utilidad extrae las cadenas de texto de un binario? / What utility extracts the strings from a binary? | `strings` |
| 4 | ¿Qué proceso legítimo de Windows aparece suplantado en el árbol? / What legitimate Windows process appears spoofed in the tree? | `csrss.exe` |
| 5 | ¿Qué otro proceso de Windows se ve imitado? / What other Windows process is imitated? | `winlogon.exe` |
| 6 | ¿En qué ruta se oculta el payload descargado? / In what path is the downloaded payload hidden? | `C:\Intel\ivecuqmanpnirkt615` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen del flujo de análisis de malware con REMnux. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |
| 2 | Configura el entorno REMnux. / Set up the REMnux environment. | `No answer needed` |
| 3 | ¿Qué herramienta de REMnux analiza los streams OLE de un documento? / What REMnux tool analyzes the OLE streams of a document? | `oledump.py` |
| 4 | ¿Qué opción de oledump.py vuelca un stream concreto? / What oledump.py option dumps a specific stream? | `-s` |
| 5 | ¿Qué comando de PowerShell usa el documento para descargar el payload? / What PowerShell command does the document use to download the payload? | `Invoke-WebRequest` |
| 6 | ¿Cómo se llama el archivo ejecutable descargado? / What is the downloaded executable file called? | `Doc-3737122pdf.exe` |
| 7 | ¿En qué variable se guarda el archivo descargado? / In what variable is the downloaded file stored? | `$TempFile` |
| 8 | ¿Qué tamaño esperado tiene el archivo descargado? / What is the expected size of the downloaded file? | `16` |
| 9 | ¿Cuántos streams relevantes contiene el documento? / How many relevant streams does the document contain? | `8` |
| 10 | ¿Qué flag se obtiene en el laboratorio? / What flag is obtained in the lab? | `Tryhackme{remnux_edition}` |
| 11 | ¿Qué método HTTP utiliza la petición de descarga? / What HTTP method does the download request use? | `GET` |
| 12 | ¿Qué herramienta muestra el árbol de procesos? / What tool shows the process tree? | `PsTree` |
| 13 | ¿Qué herramienta lista los procesos en ejecución? / What tool lists the running processes? | `PsList` |
| 14 | ¿Qué utilidad extrae las cadenas de texto de un binario? / What utility extracts the strings from a binary? | `strings` |
| 15 | ¿Qué proceso legítimo de Windows aparece suplantado en el árbol? / What legitimate Windows process appears spoofed in the tree? | `csrss.exe` |
| 16 | ¿Qué otro proceso de Windows se ve imitado? / What other Windows process is imitated? | `winlogon.exe` |
| 17 | ¿En qué ruta se oculta el payload descargado? / In what path is the downloaded payload hidden? | `C:\Intel\ivecuqmanpnirkt615` |
| 18 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

**Metodología:** Empezar volcando los streams del documento con oledump.py y la opción `-s`, seguir la cadena de descarga PowerShell (Invoke-WebRequest -> Doc-3737122pdf.exe -> $TempFile) y, con el binario en el laboratorio, comparar el árbol de procesos (PsTree, PsList) y las cadenas (strings) para localizar los procesos suplantados (csrss.exe, winlogon.exe) y el payload oculto en C:\Intel\ivecuqmanpnirkt615, obteniendo la flag del laboratorio.

### Cadena de ataque / Attack Chain

```text
Documento malicioso -> oledump.py (-s) -> Invoke-WebRequest -> Doc-3737122pdf.exe -> $TempFile -> Laboratorio (flag + método GET) -> PsTree / PsList -> strings -> csrss.exe / winlogon.exe suplantados -> C:\Intel\ivecuqmanpnirkt615
```

**Learning chain:** oledump -> cadena PowerShell -> descarga del payload -> procesos (PsTree/PsList) -> strings -> identificación del payload.

**Lección:** *El malware "legítimo" se esconde imitando procesos del sistema como csrss.exe o winlogon.exe; combinar la cadena completa (documento -> descarga -> proceso) con strings y árboles de procesos permite desenmascararlo sin ejecutarlo.*

**MITRE ATT&CK:** T1204 (User Execution), T1105 (Ingress Tool Transfer), T1036 (Masquerading), T1059.001 (PowerShell)

**Fuente:** [TryHackMe - REMnux_ Getting Started](https://tryhackme.com/room/remnuxgettingstarted)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.