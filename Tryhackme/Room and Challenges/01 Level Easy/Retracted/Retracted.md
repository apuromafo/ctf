# Retracted

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `retracted` | https://tryhackme.com/room/retracted | 01 Level Easy | TryHackMe | forense Windows / notepad.exe / antivirus.exe / .dmp / direcciones IP / línea de tiempo | Investigación forense de ransomware en Windows: artefactos del escritorio, detección del malware (antivirus.exe y volcados .dmp), conexiones sospechosas y reconstrucción de la línea de tiempo del incidente. |

---

**Contexto:** Sala de forense Windows en la que se investiga un incidente relacionado con ransomware. Se examinan los artefactos creados en el escritorio de la usuaria (archivo SOPHIE.txt abierto con notepad.exe), se detecta la actividad del malware (antivirus.exe lanzado desde la carpeta de descargas, volcados `.dmp`), se registran direcciones IP sospechosas y se ordena una secuencia de 7 eventos para reconstruir la línea de tiempo del ataque.

> **ES:** "Retracted" — investigación forense de ransomware en Windows: artefactos, malware, conexiones y línea de tiempo del incidente.
> **EN:** "Retracted" — Windows ransomware forensics: artifacts, malware, connections and incident timeline.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación del escenario forense: se investiga el caso del ransomware desaparecido y se explica el flujo de trabajo. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del caso. / Read the case introduction. | `No answer needed` |

### Task 2: Artefactos del escritorio / Desktop Artifacts

**Explicación:** Se analizan los artefactos del escritorio de la usuaria: el archivo `C:\Users\Sophie\Desktop\SOPHIE.txt` fue abierto por el proceso `notepad.exe`, y el evento queda registrado con la marca de tiempo `2024-01-08 14:25:30`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué archivo se creó o abrió en el escritorio de Sophie? / What file was created or opened on Sophie's desktop? | `C:\Users\Sophie\Desktop\SOPHIE.txt` |
| 2 | ¿Qué proceso abrió ese archivo? / What process opened that file? | `notepad.exe` |
| 3 | ¿En qué fecha y hora se registró el evento? / At what date and time was the event logged? | `2024-01-08 14:25:30` |

### Task 3: Detección del malware / Malware Detection

**Explicación:** Se identifica el componente malicioso: el proceso `antivirus.exe` se ejecutó desde el directorio `C:\Users\Sophie\download`. Durante su actividad generó volcados de tipo `.dmp` y se asoció a la dirección IP `10.10.8.111`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso malicioso se detecta? / What malicious process is detected? | `antivirus.exe` |
| 2 | ¿Desde qué directorio se ejecutó el proceso? / From which directory was the process executed? | `C:\Users\Sophie\download` |
| 3 | ¿Qué tipo de volcado o artefacto generó? / What kind of dump or artifact did it generate? | `.dmp` |
| 4 | ¿Qué dirección IP se asocia a la descarga o detección? / What IP address is associated with the download or detection? | `10.10.8.111` |

### Task 4: Conexiones del incidente / Incident Connections

**Explicación:** En el análisis de red se registra la conexión sospechosa hacia la dirección IP remota `10.11.27.46`, iniciada en `2024-01-08 14:24:18`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dirección IP remota estableció la conexión sospechosa? / What remote IP address established the suspicious connection? | `10.11.27.46` |
| 2 | ¿Cuándo se inició la conexión? / When was the connection initiated? | `2024-01-08 14:24:18` |

### Task 5: Orden de eventos / Event Ordering

**Explicación:** Se reconstruye el orden correcto de los 7 eventos de la línea de tiempo del incidente, cuya secuencia final es la siguiente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer evento de la secuencia. / First event in the sequence. | `3` |
| 2 | Segundo evento de la secuencia. / Second event in the sequence. | `1` |
| 3 | Tercer evento de la secuencia. / Third event in the sequence. | `6` |
| 4 | Cuarto evento de la secuencia. / Fourth event in the sequence. | `5` |
| 5 | Quinto evento de la secuencia. / Fifth event in the sequence. | `2` |
| 6 | Sexto evento de la secuencia. / Sixth event in the sequence. | `4` |
| 7 | Séptimo evento de la secuencia. / Seventh event in the sequence. | `7` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre del caso forense con el resumen de los hallazgos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión del caso. / Read the case conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del caso. / Read the case introduction. | `No answer needed` |
| 2 | ¿Qué archivo se creó o abrió en el escritorio de Sophie? / What file was created or opened on Sophie's desktop? | `C:\Users\Sophie\Desktop\SOPHIE.txt` |
| 3 | ¿Qué proceso abrió ese archivo? / What process opened that file? | `notepad.exe` |
| 4 | ¿En qué fecha y hora se registró el evento? / At what date and time was the event logged? | `2024-01-08 14:25:30` |
| 5 | ¿Qué proceso malicioso se detecta? / What malicious process is detected? | `antivirus.exe` |
| 6 | ¿Desde qué directorio se ejecutó el proceso? / From which directory was the process executed? | `C:\Users\Sophie\download` |
| 7 | ¿Qué tipo de volcado o artefacto generó? / What kind of dump or artifact did it generate? | `.dmp` |
| 8 | ¿Qué dirección IP se asocia a la descarga o detección? / What IP address is associated with the download or detection? | `10.10.8.111` |
| 9 | ¿Qué dirección IP remota estableció la conexión sospechosa? / What remote IP address established the suspicious connection? | `10.11.27.46` |
| 10 | ¿Cuándo se inició la conexión? / When was the connection initiated? | `2024-01-08 14:24:18` |
| 11 | Primer evento de la secuencia. / First event in the sequence. | `3` |
| 12 | Segundo evento de la secuencia. / Second event in the sequence. | `1` |
| 13 | Tercer evento de la secuencia. / Third event in the sequence. | `6` |
| 14 | Cuarto evento de la secuencia. / Fourth event in the sequence. | `5` |
| 15 | Quinto evento de la secuencia. / Fifth event in the sequence. | `2` |
| 16 | Sexto evento de la secuencia. / Sixth event in the sequence. | `4` |
| 17 | Séptimo evento de la secuencia. / Seventh event in the sequence. | `7` |
| 18 | Lee la conclusión del caso. / Read the case conclusion. | `No answer needed` |

---

**Metodología:** Revisar los artefactos del escritorio (SOPHIE.txt abierto con notepad.exe a las 14:25:30), localizar el malware (antivirus.exe ejecutado desde C:\Users\Sophie\download con volcados .dmp), correlacionar las conexiones (10.10.8.111 y 10.11.27.46, inicio a las 14:24:18) y ordenar los 7 eventos de la línea de tiempo para reconstruir la secuencia completa del incidente.

### Cadena de ataque / Attack Chain

```text
SOPHIE.txt + notepad.exe (14:25:30) -> antivirus.exe desde C:\Users\Sophie\download -> volcados .dmp -> 10.10.8.111 / 10.11.27.46 (14:24:18) -> Reordenar 7 eventos de la línea de tiempo (3,1,6,5,2,4,7)
```

**Learning chain:** Artefactos de escritorio -> detección del malware (antivirus.exe/.dmp) -> conexiones de red -> reconstrucción de la línea de tiempo.

**Lección:** *En forense, los timestamps y los artefactos cuentan la historia: relacionar el proceso que abrió el archivo, la ruta del malware y las IPs de las conexiones permite reordenar los eventos y reconstruir la secuencia real del ataque.*

**MITRE ATT&CK:** T1561 (Disk Wipe), T1486 (Data Encrypted for Impact), T1213 (Collection from Information Repositories)

**Fuente:** [TryHackMe - Retracted](https://tryhackme.com/room/retracted)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.