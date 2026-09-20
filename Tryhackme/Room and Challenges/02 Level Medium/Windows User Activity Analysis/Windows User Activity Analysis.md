# Windows User Activity Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | windowsuseractivityanalysis | https://tryhackme.com/room/windowsuseractivityanalysis | 02 Level Medium | TryHackMe | Windows Event Logs, Security Monitoring, Splunk | Análisis de la actividad de un usuario en Windows para detectar conductas maliciosas y exfiltración de datos |

---

**Contexto:** La sala **Windows User Activity Analysis** presenta un caso de monitoreo de seguridad: un empleado es investigado por actividades maliciosas documentadas en los registros de Windows. El alumno analiza logs de sistema (hive del registro, autenticaciones, procesos y conexiones) para reconstruir lo que hizo el usuario: ubicación de la actividad maliciosa, herramientas utilizadas, credenciales, servidores de exfiltración y la línea temporal exacta de los hechos.

## Solucionario

### Task 1: Introducción al caso

**Explicación:**

La sala introduce el escenario de la investigación y explica de qué trata la actividad de usuario que será analizada.

Respuesta: `No answer needed`

### Task 2: Identificación de la cuenta

**Explicación:**

Se identifica el valor asociado a la cuenta/actividad que se está investigando dentro de los registros de autenticación del sistema.

1. `12`

### Task 3: Registro del sistema y entradas analizadas

**Explicación:**

Se trabaja sobre el hive del registro de Windows: se indica la rama del registro utilizada y el número de entradas procesadas en el análisis.

1. `SOFTWARE`
2. `128`

### Task 4: Actividad maliciosa en el sistema

**Explicación:**

Se analizan los artefactos de la actividad maliciosa del usuario: la ruta donde se localiza la acción, el nombre de la herramienta empleada, la ruta del archivo de código, el archivo de keylogger y el ejecutable de borrado de disco.

1. `C:\system\home\tmp`
2. `wipe`
3. `C:\system\home\tmp\code.txt`
4. `keylogger.exe`
5. `DiskWipe.exe`

### Task 5: Comunicaciones y recursos compartidos

**Explicación:**

Se identifican los destinos de red involucrados: la dirección IP de la máquina externa con la que se comunica el sistema y el nombre del recurso o documento compartido.

1. `10.10.17.228`
2. `secret-doc`

### Task 6: Exfiltración de datos

**Explicación:**

Se determinan los detalles de la exfiltración: el documento con datos exfiltrados y la ruta UNC del recurso compartido remoto donde se depositaron los secretos.

1. `10_ways_to_Exfiltrate_Data.pdf`
2. `\\10.10.17.228\Users\Administrator\Documents\secret-documents`

### Task 7: Evidencia y marco temporal

**Explicación:**

Se recoge la evidencia final del análisis: la fuente del archivo de código, la URL utilizada para la exfiltración y la marca de tiempo exacta en la que se registró la actividad.

1. `C:\system\home\tmp\code.txt`
2. `http://10.10.17.228/`
3. `2024-03-04 12:28:26`

### Task 8: Conclusión de la investigación

**Explicación:**

La investigación de la actividad del usuario llega a su fin con la reconstrucción completa de la cadena maliciosa.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2 | Valor de la cuenta investigada | `12` |
| 3.1 | Rama del registro utilizada | `SOFTWARE` |
| 3.2 | Número de entradas analizadas | `128` |
| 4.1 | Ruta de la actividad maliciosa | `C:\system\home\tmp` |
| 4.2 | Herramienta empleada | `wipe` |
| 4.3 | Ruta del archivo de código | `C:\system\home\tmp\code.txt` |
| 4.4 | Archivo de keylogger | `keylogger.exe` |
| 4.5 | Ejecutable de borrado de disco | `DiskWipe.exe` |
| 5.1 | IP del servidor externo | `10.10.17.228` |
| 5.2 | Recurso compartido | `secret-doc` |
| 6.1 | Documento exfiltrado | `10_ways_to_Exfiltrate_Data.pdf` |
| 6.2 | Ruta UNC de exfiltración | `\\10.10.17.228\Users\Administrator\Documents\secret-documents` |
| 7.1 | Fuente del archivo de código | `C:\system\home\tmp\code.txt` |
| 7.2 | URL de exfiltración | `http://10.10.17.228/` |
| 7.3 | Marca de tiempo de la actividad | `2024-03-04 12:28:26` |
| 8 | Conclusión | `No answer needed` |

---

**Metodología:** Análisis de la actividad de un usuario en Windows mediante la correlación de logs de autenticación, procesos y red: identificación del hive del registro, localización de la actividad maliciosa, seguimiento de las comunicaciones y reconstrucción de la exfiltración.

**Learning chain:** Cuenta → registro del sistema → actividad maliciosa → comunicaciones → exfiltración → marco temporal → síntesis.

**Lección:** *Un usuario malicioso deja una huella completa si se correlacionan los registros: procesos, red y registro forman la línea temporal del incidente.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1059 Command and Scripting Interpreter · T1041 Exfiltration Over C2 Channel · T1219 Remote Access Software.

**Fuente:** [TryHackMe - Windows User Activity Analysis](https://tryhackme.com/room/windowsuseractivityanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.