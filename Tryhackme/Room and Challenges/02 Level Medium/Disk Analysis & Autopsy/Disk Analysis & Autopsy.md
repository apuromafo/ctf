# Disk Analysis & Autopsy

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Forensics |
| **Slug** | diskanalysisautopsy |
| **Link** | https://tryhackme.com/room/diskanalysisautopsy |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Autopsy, Disk Forensics, Artifact Analysis, Malware, Credential Dumping |
| **Impacto** | Alto — Análisis forense completo de imagen de disco comprometida |

---

**Contexto:** Esta sala enseña análisis forense de disco con Autopsy. Mediante el examen de una imagen de disco, el aprendiz identifica la imagen sospechosa, el sistema operativo, usuarios del sistema, conexiones de red, placas de red, herramientas de geolocalización y malware plantado. Termina con el análisis de herramientas de robo de credenciales como LaZagne y Mimikatz.

## Solucionario

### Task 1: Análisis forense inicial

**Explicación:** Se identifica la imagen de disco sospechosa y se inicia el análisis con Autopsy.

1. 1. 3f08c518adb3b5c1359849657a9b2079

### Task 2: Análisis del sistema

**Explicación:** Se identifican el nombre del equipo y los usuarios del sistema.

2. 1. DESKTOP-0R59DJ3
2. 2. H4S4N,joshwa,keshav,sandhya,shreya,sivapriya,srini,suba
   3. sivapriya

### Task 3: Análisis de red

**Explicación:** Se identifican la IP, la dirección MAC y el adaptador de red utilizados.

3. 1. 192.168.130.216
   2. 08-00-27-2c-c4-b9
   3. Intel(R) PRO/1000 MT Desktop Adapter

### Task 4: Herramientas y geolocalización

**Explicación:** Se identifica la herramienta de geolocalización utilizada y las coordenadas obtenidas.

4. 1. Look@LAN
   2. 12°52'23.0"N 80°13'25.0"E

### Task 5: Usuario comprometido

**Explicación:** Se identifica al usuario responsable de la actividad maliciosa.

5. 1. Anto Joshwa

### Task 6: Flags del análisis

**Explicación:** Se obtienen las flags encontradas durante el análisis de la imagen de disco.

6. 1. flag{HarleyQuinnForQueen}
   2. flag{I-hacked-you}

### Task 7: Herramientas de robo de credenciales

**Explicación:** Se identifican las herramientas de robo de credenciales (LaZagne, Mimikatz) presentes en la imagen y su autor.

7. 1. Lazagne,Mimikatz
   2. Benjamin DELPY (gentilkiwi)

### Task 8: Archivos de interés

**Explicación:** Se identifica un archivo comprimido cifrado relacionado con Zerologon.

8. 1. 2.2.0 20200918 Zerologon encrypted.zip

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Imagen sospechosa | `3f08c518adb3b5c1359849657a9b2079` |
| 2.1 | Nombre del equipo | `DESKTOP-0R59DJ3` |
| 2.2 | Usuarios del sistema | `H4S4N,joshwa,keshav,sandhya,shreya,sivapriya,srini,suba` |
| 2.3 | Usuario sospechoso | `sivapriya` |
| 3.1 | IP utilizada | `192.168.130.216` |
| 3.2 | Dirección MAC | `08-00-27-2c-c4-b9` |
| 3.3 | Adaptador de red | `Intel(R) PRO/1000 MT Desktop Adapter` |
| 4.1 | Herramienta de geolocalización | `Look@LAN` |
| 4.2 | Coordenadas | `12°52'23.0"N 80°13'25.0"E` |
| 5.1 | Usuario comprometido | `Anto Joshwa` |
| 6.1 | Flag de escritorio | `flag{HarleyQuinnForQueen}` |
| 6.2 | Flag de banner | `flag{I-hacked-you}` |
| 7.1 | Herramientas de credential dumping | `Lazagne,Mimikatz` |
| 7.2 | Autor de Mimikatz | `Benjamin DELPY (gentilkiwi)` |
| 8.1 | Archivo cifrado | `2.2.0 20200918 Zerologon encrypted.zip` |

---

**Metodología:** Identificación de imagen → Análisis con Autopsy → Extracción de artefactos (usuarios, red, software) → Correlación de evidencia → Obtención de flags.

**Learning chain:** Disk image triage → Autopsy artifact analysis → Network & user profiling → Malware identification → Credential harvesting tools → Flag recovery

**Lección:** *Una imagen de disco contiene la historia completa del compromiso; el artefacto forense es la prueba definitiva.*

**MITRE ATT&CK:**
- T1003 — OS Credential Dumping
- T1555 — Credentials from Password Stores
- T1105 — Ingress Tool Transfer

**Fuente:** [TryHackMe - Disk Analysis & Autopsy](https://tryhackme.com/room/diskanalysisautopsy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.