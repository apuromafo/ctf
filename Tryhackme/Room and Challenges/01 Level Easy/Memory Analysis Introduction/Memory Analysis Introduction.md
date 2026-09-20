# Memory Analysis Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `memoryanalysisintroduction` | [TryHackMe](https://tryhackme.com/room/memoryanalysisintroduction) | 01 Level Easy | THM | RAM, Volatility, Mimikatz, LiME, WinRM, PsExec | Fundamentos del análisis de memoria y su aplicación en SOC y DFIR |

> **Objeto:** Conocer los fundamentos del análisis de memoria: qué artefactos quedan en RAM, cómo se adquieren y qué técnicas de ataque se detectan con herramientas como Volatility.

---

**Contexto:** Sala introductoria al análisis de memoria: se estudian los componentes de la memoria (RAM, disk, heap, swap), las formas de análisis de Windows (Mimikatz, full, hiberfil.sys, DKOM), el formato LiME, las técnicas de evasión como process hollowing y las técnicas de ataque asociadas (WinRM, PsExec) con sus identificadores MITRE.

> **ES:** Sala introductoria al análisis de memoria: componentes de RAM, adquisición, Volatility y técnicas de ataque detectables.
> **EN:** Introductory room to memory analysis: RAM components, acquisition, Volatility and detectable attack techniques.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de la importancia del análisis de memoria en la respuesta a incidentes.

No answer needed

### Task 2: Componentes de la memoria / Memory components
**Explicación:** Se identifican los elementos que componen la memoria de un sistema y dónde reside la información volátil.

1. RAM
2. disk
3. heap
4. swap

### Task 3: Adquisición y análisis de Windows / Windows acquisition and analysis
**Explicación:** Se revisan las herramientas y formatos para capturar y analizar la memoria de Windows, incluidos Mimikatz, el dumping completo, LiME, hiberfil.sys y las técnicas de ofuscación del kernel.

1. Mimikatz
2. full
3. lime
4. hiberfil.sys
5. DKOM

### Task 4: Técnicas de ataque / Attack techniques
**Explicación:** Se reconocen las técnicas de ataque detectables en memoria y sus identificadores MITRE ATT&CK.

1. Process hollowing
2. WinRM
3. T1086
4. PsExec
5. T1053.005

### Task 5: Flag del reto / Challenge flag
**Explicación:** Se completa el ejercicio práctico de la sala y se obtiene la flag final.

1. THM{m3mory_analyst_g00d_job}

### Task 6: Conclusión / Conclusion
**Explicación:** Cierre de la sala y repaso de los conceptos del análisis de memoria.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Componente de memoria 1 | `RAM` |
| 2.2 | Componente de memoria 2 | `disk` |
| 2.3 | Componente de memoria 3 | `heap` |
| 2.4 | Componente de memoria 4 | `swap` |
| 3.1 | Herramienta de extracción de credenciales | `Mimikatz` |
| 3.2 | Tipo de volcado | `full` |
| 3.3 | Formato/module de adquisición | `lime` |
| 3.4 | Archivo de hibernación | `hiberfil.sys` |
| 3.5 | Técnica de ocultación en el kernel | `DKOM` |
| 4.1 | Técnica de inyección detectada | `Process hollowing` |
| 4.2 | Técnica de acceso remoto | `WinRM` |
| 4.3 | ID MITRE asociado | `T1086` |
| 4.4 | Herramienta de ejecución remota | `PsExec` |
| 4.5 | ID MITRE asociado | `T1053.005` |
| 5.1 | Flag del reto | `THM{m3mory_analyst_g00d_job}` |
| 6 | — | `No answer needed` |

---

**Metodología:** Revisión de los componentes de la memoria de un sistema, análisis de las técnicas de adquisición (Mimikatz, full dump, LiME, hiberfil.sys), reconocimiento de mecanismos de evasión como DKOM o process hollowing, y correlación de las técnicas de ataque (WinRM, PsExec) con sus identificadores MITRE ATT&CK.

### Cadena de ataque / Attack Chain

Memoria volátil (RAM/heap/swap) → adquisición → análisis → detección de técnicas (process hollowing, DKOM) → correlación MITRE (T1086, T1053.005) → flag.

**Learning chain:** RAM → adquisición → Volatility → técnicas de ataque → MITRE → flag

*Lección:* La memoria conserva evidencia clave de compromiso: analizarla permite detectar técnicas que otros artefactos no reflejan.

**MITRE ATT&CK:** T1086 - PowerShell, T1053.005 - Scheduled Task, T1055.012 - Process Injection: Process Hollowing.

**Fuente:** [TryHackMe - Memory Analysis Introduction](https://tryhackme.com/room/memoryanalysisintroduction)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.