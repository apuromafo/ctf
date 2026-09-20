# Linux Process Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | linuxprocessanalysis | [TryHackMe](https://tryhackme.com/room/linuxprocessanalysis) | 01 Level Easy | THM | lsof, ps, netstat, /proc, C2, beacon, ifconfig, exfiltración | Análisis de procesos en Linux: detección de beacons C2, exfiltración de datos y artefactos maliciosos |

---

**Contexto:** Sala dedicada al análisis de procesos en Linux para detectar compromisos. Se usan herramientas como `lsof`, `ps` y `netstat` para descubrir procesos sospechosos, endpoints de C2 (`http://c2.intelligent-software.thm:8310/beacon`), rutas de exfiltración y flags incrustadas en los artefactos encontrados.

> **EN:**
> 1. No answer needed
> 2. THM{8c860435f00c943c21f6b6e0f1b2f854}
> 3. 1. lsof
>    2. abzkd83o4jakxld
> 4. 1. http://c2.intelligent-software.thm:8310/beacon
>    2. THM{4682786cf2d92f01c4d30a2bbf4621f7}
>    3. THM{851a981445dbfb9485c3771510a53568}
> 5. 1. THM{4922066dc6494e8d4d507eef2205c262}
>    2. THM{053c12e620acea8a77b4bdcba578ca19}
> 6. 1. http://aabab.best-it-services.thm/id_rsa
>    2. ifconfig
> 7. 1. THM{4a8fd984228d89999342d189e6b916de}
>    2. THM{5d5cb0ffe8369ab08f1e90aa9e9bc24e}
> 8. No answer needed

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta el objetivo: analizar los procesos de una máquina Linux comprometida para identificar el C2, la exfiltración y el resto de artefactos de la intrusión.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Primeros indicios / First indicators

**Explicación:** Se identifican los primeros indicadores de compromiso en los procesos y archivos del sistema, confirmando la presencia de actividad maliciosa.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué flag se encuentra en los primeros indicios? / What flag is found in the first indicators? | `THM{8c860435f00c943c21f6b6e0f1b2f854}` |

### Task 3: Archivos abiertos y procesos / Open files and processes

**Explicación:** Se inspeccionan los archivos abiertos por el proceso malicioso con `lsof` y se identifica el identificador del proceso involucrado en la comunicación.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué herramienta lista los archivos abiertos por un proceso? / Which tool lists files opened by a process? | `lsof` |
| 2 | ¿Cuál es el identificador del proceso malicioso? / What is the malicious process identifier? | `abzkd83o4jakxld` |

### Task 4: C2 y beacon / C2 and beacon

**Explicación:** Se descubre el endpoint del servidor de comando y control (`/beacon`) al que el proceso malicioso realiza peticiones periódicas, y se extraen las flags relacionadas con la comunicación.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué URL de C2 usa el beacon? / Which C2 URL does the beacon use? | `http://c2.intelligent-software.thm:8310/beacon` |
| 2 | Flag encontrada durante el análisis del C2 / Flag found during C2 analysis | `THM{4682786cf2d92f01c4d30a2bbf4621f7}` |
| 3 | Flag adicional encontrada / Additional flag found | `THM{851a981445dbfb9485c3771510a53568}` |

### Task 5: Flags y artefactos / Flags and artifacts

**Explicación:** Se profundiza en los artefactos asociados al proceso malicioso, extrayendo dos flags adicionales que completan el árbol de actividad del atacante.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Primera flag del artefacto / First artifact flag | `THM{4922066dc6494e8d4d507eef2205c262}` |
| 2 | Segunda flag del artefacto / Second artifact flag | `THM{053c12e620acea8a77b4bdcba578ca19}` |

### Task 6: Exfiltración / Exfiltration

**Explicación:** Se identifica la vía de exfiltración de datos: una petición a un dominio de estafa (`aabab.best-it-services.thm`) para sustraer la clave `id_rsa`, empleando `ifconfig` para reconocer el equipo comprometido.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué URL se usa para la exfiltración de la clave? / Which URL is used for key exfiltration? | `http://aabab.best-it-services.thm/id_rsa` |
| 2 | ¿Qué comando usa el atacante para reconocer la red? / Which command does the attacker use to survey the network? | `ifconfig` |

### Task 7: Fase final de análisis / Final analysis phase

**Explicación:** Última fase de recolección de evidencias: se extraen las flags finales vinculadas al análisis completo de procesos.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Flag final del análisis 1 / Final analysis flag 1 | `THM{4a8fd984228d89999342d189e6b916de}` |
| 2 | Flag final del análisis 2 / Final analysis flag 2 | `THM{5d5cb0ffe8369ab08f1e90aa9e9bc24e}` |

### Task 8: Conclusión / Conclusion

**Explicación:** Se consolidan los hallazgos del análisis de procesos: endpoint de C2, beacon, archivos abiertos y rutas de exfiltración.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Enumerar procesos con `ps -ef` y establecer cuáles son sospechosos por conexiones y comportamiento. Con `lsof -p <PID>` se listan los archivos abiertos por el proceso malicioso. `netstat -tulpn` y el volcado de `/proc` permiten ver las conexiones activas y descubrir el endpoint de C2 `http://c2.intelligent-software.thm:8310/beacon`. Se correlacionan las peticiones del beacon con las flags incrustadas en los binarios y scripts. Finalmente se detecta la exfiltración hacia `aabab.best-it-services.thm/id_rsa` y el uso de `ifconfig` para reconocer el host comprometido.

### Cadena de ataque / Attack Chain

Enumeración de procesos → inspección de archivos abiertos (`lsof`) → conexiones activas (`netstat`) → descubrimiento del C2 `c2.intelligent-software.thm:8310/beacon` → extracción de flags → exfiltración de `id_rsa` hacia `aabab.best-it-services.thm` → reconocimiento con `ifconfig`

**Learning chain:** ps -ef → lsof → netstat -tulpn → /proc → c2.intelligent-software.thm:8310/beacon → flags → aabab.best-it-services.thm/id_rsa → ifconfig

**Lección:** *El análisis de procesos convierte un host comprometido en un mapa de la infraestructura del atacante: los beacons C2, los archivos abiertos y las rutas de exfiltración trazadas con `lsof`, `netstat` y `/proc` revelan qué se robó y a dónde fue a parar.*

**MITRE ATT&CK:** T1105 (Ingress Tool Transfer), T1071 (Application Layer Protocol), T1041 (Exfiltration Over C2 Channel), T1057 (Process Discovery), T1082 (System Information Discovery), T1049 (System Network Connections Discovery)

**Fuente:** [TryHackMe - Linux Process Analysis](https://tryhackme.com/room/linuxprocessanalysis)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.