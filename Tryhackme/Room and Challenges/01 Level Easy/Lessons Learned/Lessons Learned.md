# Lessons Learned

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `lessonslearned` | [TryHackMe](https://tryhackme.com/room/lessonslearned) | 01 Level Easy | TryHackMe | DFIR, IR, TTPs, Sigma, detección, análisis de correo, defensa | Sala de Defensive Security sobre cómo extraer lecciones aprendidas de un incidente y convertir la evidencia (IOCs, tácticas) en mejoras de detección y respuesta. |

---

**Contexto:** La sala "Lessons Learned" presenta un caso práctico de respuesta a incidentes (DFIR) ambientado en la empresa "SwiftSpend Finance". A partir de un incidente real se recorren las fases de gestión (Preparation, Detection and Analysis, Containment, Eradication, Remediation and Recovery, Post-Incident Activity), se analizan los indicadores de compromiso del correo (remitente, SPF/DKIM/DMARC, IP 3.250.38.141, adjunto Dropper.exe), se identifica el dropper (`Dropper`) y el script `backup.sh` como vector de pivotaje, y se escribe una regla Sigma para detectar futuros eventos similares creando consultas Hash ("create_stream_hash").

> **ES:** Caso de defensa/soc: análisis de un incidente phishing con Dropper.exe y backup.sh, tácticas (pivoting desde backup.sh), indicadores (alex.swift@swiftspend[.]finance, Ticket#2023012398704232, 3[.]250[.]38[.]141) y creación de reglas Sigma.
> **EN:** Defense/soc case: analysis of a phishing incident with Dropper.exe and backup.sh, tactics (pivoting from backup.sh), indicators (alex.swift@swiftspend[.]finance, Ticket#2023012398704232, 3[.]250[.]38[.]141) and creating Sigma rules.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Introducción al caso de la sala. No requiere respuesta.

```text
1. No answer needed
```

### Task 2: Fases del IR / IR phases
**Explicación:** Se repasan las fases de respuesta a incidentes: la primera es la Preparación, y una de las fases finales del ciclo es Erradicación, Remediación y Recuperación.

```text
2. 1. Preparation
   2. Eradication, Remediation, and Recovery
```

### Task 3: Identificación de elementos / Identifying components
**Explicación:** Se identifican los elementos clave del incidente: el archivo malicioso que actúa como dropper inicial y el script `backup.sh` utilizado en la cadena de ataque.

```text
3. 1. Dropper
   2. backup.sh
```

### Task 4: Análisis de IOCs / IOC analysis
**Explicación:** Se analizan los indicadores de compromiso: la dirección del remitente y el número de ticket de soporte (`alex.swift@swiftspend[.]finance, Ticket#2023012398704232`), los mecanismos de autenticación del correo cuya falta se estudia (`(i.e., SPF, DKIM, DMARC)`), la IP del servidor malicioso y el archivo adjunto (`3[.]250[.]38[.]141, Dropper.exe`) y el método de desplazamiento lateral/pivotaje (`Pivoting from backup.sh`).

```text
4. 1. alex.swift@swiftspend[.]finance, Ticket#2023012398704232
   2. (i.e., SPF, DKIM, DMARC)
   3. 3[.]250[.]38[.]141, Dropper.exe
   4. Pivoting from backup.sh
```

### Task 5: Reglas Sigma / Sigma rules
**Explicación:** Se escribe una regla de detección con el formato Sigma y se genera un hash de la regla con la herramienta/opción `create_stream_hash`.

```text
5. 1. Sigma
   2. create_stream_hash
```

### Task 6: Conclusión / Conclusion
**Explicación:** Tarea final de cierre. No requiere respuesta.

```text
6. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Introducción al caso | `No answer needed` |
| 2 | Primera fase de gestión de incidentes | `Preparation` |
| 2 | Fase final del ciclo | `Eradication, Remediation, and Recovery` |
| 3 | Archivo malicioso inicial | `Dropper` |
| 3 | Script de pivotaje | `backup.sh` |
| 4 | Remitente y ticket de soporte | `alex.swift@swiftspend[.]finance, Ticket#2023012398704232` |
| 4 | Mecanismos de autenticación de correo | `(i.e., SPF, DKIM, DMARC)` |
| 4 | IP y archivo adjunto | `3[.]250[.]38[.]141, Dropper.exe` |
| 4 | Método de pivotaje | `Pivoting from backup.sh` |
| 5 | Formato de reglas de detección | `Sigma` |
| 5 | Opción para generar el hash de la regla | `create_stream_hash` |
| 6 | Conclusión | `No answer needed` |

---

**Metodología:** Se analizó un incidente real de phishing/DFIR retrotrayéndolo a sus indicadores: la fase de preparación, los componentes del ataque (Dropper y backup.sh), los IOCs del correo (remitente, ticket, IP y archivo) y el método de pivotaje. Con esa evidencia se generó una regla de detección en formato Sigma, calculando su hash con `create_stream_hash`.

### Cadena de ataque / Attack Chain

```text
Preparation -> phishing a SwiftSpend Finance -> Dropper.exe -> IP 3.250.38.141 -> backup.sh -> pivoting -> detección (Sigma) -> Eradication, Remediation, and Recovery -> post-incident learnings
```

**Learning chain:** Phishing -> email IOCs (SPF/DKIM/DMARC) -> Dropper -> backup.sh -> pivoting -> Sigma rule -> Eradication/Remediation/Recovery -> lessons learned

**Lección:** *Toda la evidencia de un incidente (remitentes, IOCs, archivos y movimientos laterales) debe convertirse en detección accionable (reglas Sigma) y en mejoras de preparación y recuperación para el siguiente incidente.*

**MITRE ATT&CK:** T1566 (Phishing), T1566.001 (Phishing: Spearphishing Attachment), T1204 (User Execution), T1059.004 (Command and Scripting Interpreter: Unix Shell), T1021 (Remote Services: SMB/SSH), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Lessons Learned](https://tryhackme.com/room/lessonslearned)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.