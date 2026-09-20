# DAST

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web Security |
| **Slug** | dast |
| **Link** | https://tryhackme.com/room/dast |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | DAST, OWASP ZAP, Spidering, XSS, Command Injection, ZEST |
| **Impacto** | Alto — Detección automatizada de vulnerabilidades web críticas |

---

**Contexto:** Esta sala enseña Dynamic Application Security Testing (DAST) utilizando OWASP ZAP. Cubre el ciclo completo: rastreo de la aplicación, escaneo automatizado, análisis de resultados, generación de reportes y validación manual de vulnerabilidades como XSS reflejado e inyección de comandos.

## Solucionario

### Task 1: Introducción a DAST

**Explicación:** Se presenta el concepto de DAST y su importancia en el testing de seguridad.

1. No answer needed

### Task 2: Crawl y Spidering

**Explicación:** Se configura el rastreo de la aplicación objetivo para descubrir endpoints y parámetros.

2. 1. Nay
   2. Spidering/Crawling
   3. Nay

### Task 3: Análisis de resultados

**Explicación:** Se examina el escaneo automatizado y se identifican endpoints vulnerables.

3. 1. Headless
   2. pass, user
   3. /view.php

### Task 4: Detección de XSS

**Explicación:** Se identifica y valida un XSS reflejado en la aplicación.

4. 1. Yea
   2. Cross Site Scripting (Reflected)

### Task 5: Análisis de respuestas

**Explicación:** Se analizan scripts ZEST y se identifica inyección de comandos remota.

5. 1. ZEST scripts
   2. Remote OS Command Injection

### Task 6: Explotación de Command Injection

**Explicación:** Se explota la inyección de comandos para ejecutar código remoto.

6. 1. Remote OS Command Injection
   2. yea

### Task 7: Validación de hallazgos

**Explicación:** Se confirma la presencia y severidad de las vulnerabilidades encontradas.

7. 1. 3
   2. 4
   3. Remote OS Command Injection

### Task 8: Cierre

**Explicación:** Pregunta final de la sala.

8. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2.1 | Configuración spider | `Nay` |
| 2.2 | Técnica de descubrimiento | `Spidering/Crawling` |
| 2.3 | Confirmación | `Nay` |
| 3.1 | Modo de ejecución | `Headless` |
| 3.2 | Credenciales | `pass, user` |
| 3.3 | Endpoint vulnerable | `/view.php` |
| 4.1 | ¿XSS encontrado? | `Yea` |
| 4.2 | Tipo de XSS | `Cross Site Scripting (Reflected)` |
| 5.1 | Scripts utilizados | `ZEST scripts` |
| 5.2 | Vulnerabilidad | `Remote OS Command Injection` |
| 6.1 | Tipo de inyección | `Remote OS Command Injection` |
| 6.2 | Confirmación | `yea` |
| 7.1 | Número de hallazgos | `3` |
| 7.2 | Severidad | `4` |
| 7.3 | Vulnerabilidad principal | `Remote OS Command Injection` |
| 8 | Cierre | `No answer needed` |

---

**Metodología:** Configuración de ZAP → Spidering de la aplicación → Escaneo automatizado → Análisis de hallazgos → Validación manual → Reporte.

**Learning chain:** Tool setup → Application crawling → Automated scanning → Result analysis → Manual validation → Reporting

**Lección:** *DAST complementa el testing estático al descubrir vulnerabilidades que solo se manifiestan en ejecución.*

**MITRE ATT&CK:**
- T1190 — Exploit Public-Facing Application
- T1059.004 — Unix Shell

**Fuente:** [TryHackMe - DAST](https://tryhackme.com/room/dast)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.