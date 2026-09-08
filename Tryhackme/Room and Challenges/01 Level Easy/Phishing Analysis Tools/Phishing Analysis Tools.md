# Phishing Analysis Tools

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (análisis de phishing) |
| **Slug** | `phishingemails3tryoe` |
| **Link** | [TryHackMe](https://tryhackme.com/room/phishingemails3tryoe) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | PhishTool / Any.Run (malware sandbox) / Thunderbird / CyberChef / análisis de cabeceras / defanging / SHA256 / CVE-2017-11882 |
| **Impacto** | Sala que entrena el análisis completo de correos de phishing: recopilar la información correcta (cabeceras, enlaces, archivos adjuntos), usar PhishTool y sandboxes como Any.Run, extraer el IP de origen y los dominios de interés defangeados, identificar el archivo y su hash SHA256, y clasificar la actividad (suspicious/malicious) hasta entender qué vulnerabilidad intenta explotar el adjunto. |

---

**Contexto:** La sala guía el flujo de un analista de phishing: primero aprender qué información recopilar (cabeceras, cuerpo, enlaces, adjuntos), después analizar la cabecera de un correo que suplanta a un banco (`capitai-one.com` frente al oficial `capitalone.com`) y el cuerpo del correo (obteniendo los enlaces con *Copy Link Location*). Luego se presentan PhishTool y los malware sandbox (Any.Run). Los casos prácticos analizan tres correos: uno que suplanta a Netflix (IP de origen `209[.]85[.]167[.]226`, dominio de interés `etekno[.]xyz`, URL acortada `hxxps[://]t[.]co/yuxfZm8KPg?amp==1`), un PDF malicioso (`Payment-updateid.pdf`, sha256 `cc6f1a04...`, tráfico sospechoso a `2[.]16[.]107[.]24` y `2[.]16[.]107[.]83`, `svchost.exe`) y un Excel (`CBJ200620039539.xlsx`) que explota el ejecutor de fórmulas de Office (CVE-2017-11882).

## Solucionario

### Task 1: Introducción

**Explicación:** Presenta los pasos de un análisis de phishing exitoso y qué se va a cubrir: cabeceras, cuerpo, enlaces y archivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: ¿Qué información debemos recopilar?

**Explicación:** Antes de analizar hay que saber qué capturar de un correo sospechoso: la cabecera completa, el cuerpo, el remitente real, los enlaces incrustados y los archivos adjuntos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee qué información se debe recopilar de un correo sospechoso. | `No answer needed` |

### Task 3: Análisis de la cabecera del correo

**Explicación:** Se analiza una cabecera donde el remitente usa el dominio `capitai-one.com` con una "i" añadida para imitar al sitio oficial del banco.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del sitio oficial del banco al que `capitai-one.com` intentó parecerse? | `capitalone.com` |

### Task 4: Análisis del cuerpo del correo

**Explicación:** Para obtener manualmente la ubicación de un hiperenlace, se hace clic derecho sobre el enlace y se elige **Copy Link Location**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se obtiene manualmente la ubicación de un hiperenlace? | `Copy Link Location` |

### Task 5: Malware Sandbox

**Explicación:** Los sandboxes (como Any.Run) ejecutan los adjuntos en un entorno aislado y reportan su comportamiento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el funcionamiento de los malware sandbox. | `No answer needed` |

### Task 6: PhishTool

**Explicación:** PhishTool permite importar el `.eml` y analizar las cabeceras. En la salida Strings del archivo analizado, el ejecutable incrustado en el correo se llama `#454326_PDF.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Mira la salida Strings. ¿Cuál es el nombre del archivo EXE? | `#454326_PDF.exe` |

### Task 7: Caso de phishing 1

**Explicación:** Con la máquina arrancada se abre el correo en Thunderbird. El correo suplanta a Netflix (desde `NetfIix<JGQ47wazXe1xYVBrkeDg-JOg7ODDQwWdR@JOg7ODDQwWdR-yVkCaBkTNp.gogolecloud.com>`). En "View Source" se localiza el `Received" from"` con el IP de origen, que se defangea con CyberChef. El dominio de interés proviene del *Return-Path* y la URL acortada es la llamada a la acción (*Update Account Now*).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué marca intentaba suplantar este correo? | `Netflix` |
| 2 | ¿Cuál es la dirección de correo del remitente (From)? | `NetfIix<JGQ47wazXe1xYVBrkeDg-JOg7ODDQwWdR@JOg7ODDQwWdR-yVkCaBkTNp.gogolecloud.com>` |
| 3 | ¿Cuál es el IP de origen? Defangea el IP. | `209[.]85[.]167[.]226` |
| 4 | Por lo que puedes deducir, ¿cuál será un dominio de interés? Defangea el dominio. | `etekno[.]xyz` |
| 5 | ¿Cuál es la URL acortada? Defangea la URL. | `hxxps[://]t[.]co/yuxfZm8KPg?amp==1` |

### Task 8: Caso de phishing 2

**Explicación:** Se analiza en Any.Run un PDF malicioso. El sandbox clasifica la actividad como "Suspicious activity"; el archivo es `Payment-updateid.pdf` con hash SHA256 `cc6f1a04...`. En el "Text Report", la sección de conexiones muestra dos IP clasificadas como maliciosas (defangeadas) y el proceso de Windows marcado como "Potentially Bad Traffic" al final del informe es `svchost.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo clasifica Any.Run este correo? | `Suspicious activity` |
| 2 | ¿Cuál es el nombre del archivo PDF? | `Payment-updateid.pdf` |
| 3 | ¿Cuál es el hash SHA 256 del archivo PDF? | `cc6f1a04b10bcb168aeec8d870b97bd7c20fc161e8310b5bce1af8ed420e2c24` |
| 4 | ¿Qué dos direcciones IP se clasifican como maliciosas? Defangea los IP. | `2[.]16[.]107[.]24,2[.]16[.]107[.]83` |
| 5 | ¿Qué proceso de Windows fue marcado como Potentially Bad Traffic? | `svchost.exe` |

### Task 9: Caso de phishing 3

**Explicación:** En Any.Run, el segundo análisis se clasifica como "Malicious activity". El archivo es `CBJ200620039539.xlsx` (sha256 `5f94a66e...`). Del informe de texto se extraen los dominios maliciosos (en orden alfabético), los IP maliciosos (de menor a mayor) y, en "Behavior activities", el CVE que intenta explotar el adjunto (`CVE-2017-11882`, ejecución de código en el *Equation Editor* de Office).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se clasifica este análisis? | `Malicious activity` |
| 2 | ¿Cuál es el nombre del archivo Excel? | `CBJ200620039539.xlsx` |
| 3 | ¿Cuál es el hash SHA 256 del archivo? | `5f94a66e0ce78d17afc2dd27fc17b44b3ffc13ac5f42d3ad6a5dcfb36715f3eb` |
| 4 | ¿Qué dominios se listan como maliciosos? Defangea las URLs y envía las respuestas en orden alfabético. | `biz9holdings[.]com,findresults[.]site,ww38[.]findresults[.]site` |
| 5 | ¿Qué direcciones IP se listan como maliciosas? Defangea las IP y envía las respuestas de menor a mayor. | `75[.]2[.]11[.]242,103[.]224[.]182[.]251,204[.]11[.]56[.]48` |
| 6 | ¿Qué vulnerabilidad intenta explotar este adjunto malicioso? | `CVE-2017-11882` |

### Task 10: Conclusión

**Explicación:** Resumen del flujo completo de análisis de phishing y de las herramientas disponibles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** Recopilación de la información del correo (cabeceras, enlaces, adjuntos) → análisis de cabecera y cuerpo → uso de Thunderbird/view source para el IP de origen → defanging con CyberChef → análisis dinámico con Any.Run (clasificación, hashes, conexiones, comportamiento) → PhishTool → identificación del CVE explotado.
**Learning chain:** identificar qué recopilar → analizar cabecera y enlaces del correo → repasar PhishTool y sandboxes → caso Netflix (suplantación de marca e IP) → caso PDF (IP maliciosas y proceso) → caso Excel (dominios/IP/CVE) → conclusiones.
**MITRE ATT&CK:** T1566 (Phishing), T1566.002 (Spearphishing Link), T1204.002 (User Execution: Malicious File), T1203 (Exploitation for Client Execution), T1059.003 (Windows Command Shell)
**Fuente:** [TryHackMe - Phishing Analysis Tools](https://tryhackme.com/room/phishingemails3tryoe)