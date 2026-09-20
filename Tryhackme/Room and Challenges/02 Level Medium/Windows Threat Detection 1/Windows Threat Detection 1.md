# Windows Threat Detection 1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | windowsthreatdetection1 | https://tryhackme.com/room/windowsthreatdetection1 | 02 Level Medium | TryHackMe | Splunk, Windows Event Logs, Sysmon, MITRE ATT&CK | Detección e investigación de una cadena de intrusión Windows a partir de logs (caso TR-07) |

---

**Contexto:** La sala **Windows Threat Detection 1** plantea el caso "TR-07" usando telemetría de Windows: un usuario reporta un correo sospechoso, el sistema sufrió el envío de un archivo con doble extensión (.jpg.exe), y se ejecutó una cadena de malware con comunicación a un C2. El alumno correlaciona eventos (endpoint, proceso, red) en Splunk para reconstruir el ataque completo: acceso inicial por phishing, descarga del payload, interacción con el dominio de mando y control, y exfiltración de datos mediante una memoria USB.

## Solucionario

### Task 1: Introducción y contexto de la investigación

**Explicación:**

La sala presenta el escenario de una intrusión real: un ticket de usuario informa de un correo sospechoso y se inicia la investigación forense con los logs de Windows.

Respuesta: `No answer needed`

### Task 2: Acceso inicial y vector de ataque

**Explicación:**

Se identifica el vector de acceso inicial: el código de la técnica empleada contra un servicio público es `T1190` (Exploit Public-Facing Application) y el mecanismo de entrega de la amenaza fue un correo de phishing.

1. `T1190`
2. `Phishing`

### Task 3: Sistema comprometido y cuenta involucrada

**Explicación:**

Se identifican los datos del sistema comprometido en la fase de acceso inicial: la cuenta utilizada, la dirección IP interna desde la que se ejecutó el acceso y el nombre del equipo afectado.

1. `Administrator`
2. `203.205.34.107`
3. `DESKTOP-QNBC4UU`

### Task 4: Entrega del payload

**Explicación:**

La flag de la sala es `THM{misleading_extension}` y se confirma la técnica del archivo con extensión engañosa. El primer comando ejecutado descarga el archivo desde el servidor del actor y el archivo .jpg sospechoso es `best-cat.jpg.exe`.

1. `THM{misleading_extension}`
2. `http://wp16.hqywlqpa.thm:8000/cgi-bin/f`
3. `best-cat.jpg.exe`

### Task 5: Artefactos de la descarga y C2

**Explicación:**

Se localizan los artefactos de la descarga en el sistema: la ruta del archivo ZIP bajado, la ruta del segundo comando ejecutado, el puerto utilizado para la comunicación y el dominio de C2.

1. `C:\Users\Administrator\Downloads\top-cats.zip`
2. `C:\Users\Administrator\Pictures`
3. `5484`
4. `rjj.store`

### Task 6: Exfiltración por USB

**Explicación:**

Se reconstruye la fase final del ataque: el archivo correspondiente a la unidad USB extraíble, el archivo copiado desde el sistema hacia el USB y la letra de la unidad de almacenamiento.

1. `E:\Open Sandisk 4GB USB.exe`
2. `C:\Users\Public\Documents\winupdate.exe`
3. `F:`

### Task 7: Conclusión del análisis

**Explicación:**

La investigación del caso TR-07 concluye tras reconstruir toda la cadena de ataque: phishing, descarga, ejecución, comunicación con el C2 y exfiltración por dispositivo extraíble.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2.1 | Código de la técnica explotada | `T1190` |
| 2.2 | Vector de acceso inicial | `Phishing` |
| 3.1 | Cuenta comprometida | `Administrator` |
| 3.2 | IP interna del acceso | `203.205.34.107` |
| 3.3 | Nombre del equipo | `DESKTOP-QNBC4UU` |
| 4.1 | Flag de la sala | `THM{misleading_extension}` |
| 4.2 | Primer comando ejecutado | `http://wp16.hqywlqpa.thm:8000/cgi-bin/f` |
| 4.3 | Nombre del archivo .jpg | `best-cat.jpg.exe` |
| 5.1 | Ruta del ZIP descargado | `C:\Users\Administrator\Downloads\top-cats.zip` |
| 5.2 | Segundo comando ejecutado | `C:\Users\Administrator\Pictures` |
| 5.3 | Puerto de comunicación | `5484` |
| 5.4 | Dominio C2 | `rjj.store` |
| 6.1 | Archivo de la unidad USB | `E:\Open Sandisk 4GB USB.exe` |
| 6.2 | Archivo copiado al USB | `C:\Users\Public\Documents\winupdate.exe` |
| 6.3 | Letra de la unidad USB | `F:` |
| 7 | Conclusión | `No answer needed` |

---

**Metodología:** Reconstrucción forense de una intrusión Windows a partir de logs: identificación del punto de entrada, correlación de eventos de descarga y ejecución, seguimiento del C2 e identificación de la exfiltración por dispositivos extraíbles.

**Learning chain:** Phishing → descarga del payload → ejecución con doble extensión → comunicación C2 → copia a USB → síntesis del caso TR-07.

**Lección:** *Las extensiones engañosas y los archivos de doble extensión son la firma clásica de una intrusión; cada artefacto del sistema deja un rastro correlacionable en los logs.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1566 Phishing · T1204 User Execution · T1105 Ingress Tool Transfer.

**Fuente:** [TryHackMe - Windows Threat Detection 1](https://tryhackme.com/room/windowsthreatdetection1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.