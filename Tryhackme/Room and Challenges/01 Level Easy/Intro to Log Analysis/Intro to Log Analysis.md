# Intro to Log Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtologanalysis` | [TryHackMe](https://tryhackme.com/room/introtologanalysis) | 01 Level Easy | TryHackMe | Log Analysis, Nginx, Regex, Grok, ELK, CyberChef, Sigma, YARA | Fundamentos del análisis de logs: fuentes, análisis automatizado/manual, regex, Grok, CyberChef y reglas de detección |

> **Objeto:** Aprender las bases del análisis de logs: la teoría de investigación (Super Timeline, hashes), la localización y análisis de logs de servidores web, el análisis automatizado frente al manual, el uso de comandos, regex y Grok, la decodificación con CyberChef y la escritura de reglas de detección (Sigma/YARA).

---

**Contexto:** Sala práctica y teórica de análisis de logs: se aprende la teoría de investigación (qué es un Super Timeline y los File Hashes), se identifica y analiza el log de acceso de un servidor web (nginx) detectando un Path Traversal, se distingue el análisis automatizado del manual, se trabaja con comandos de línea sobre el log (hash, conteos, IP del atacante, timestamp), se usan expresiones regulares y Grok en ELK, se decodifican peticiones con CyberChef y se construye una regla de detección en YAML.

> **ES:** Sala de análisis de logs: teoría de investigación, logs web (nginx), análisis automatizado vs manual, comandos, regex, Grok, CyberChef y reglas de detección.
> **EN:** Log analysis room: investigation theory, web server logs (nginx), automated vs manual analysis, command-line analysis, regex, Grok, CyberChef and detection rules.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los conceptos que se van a trabajar: teoría de investigación, análisis de logs, automatización y herramientas de detección.

No answer needed

### Task 2: Configuración / Setup
**Explicación:** Preparación del entorno de la sala para los ejercicios prácticos.

No answer needed

### Task 3: Teoría de investigación / Investigation Theory
**Explicación:** Se aprenden los conceptos teóricos clave del análisis de logs y la investigación: un Super Timeline como vista cronológica consolidada y los File Hashes como resúmenes de integridad.

1. Super Timeline
2. File Hashes

### Task 4: Análisis de logs de servidor web / Web Server Log Analysis
**Explicación:** Se localiza el log de acceso del servidor web (nginx) y se identifica el tipo de ataque presente en el registro.

1. /var/log/nginx/access.log
2. Path Traversal

### Task 5: Análisis automatizado vs manual / Automated vs Manual Analysis
**Explicación:** Se comparan los dos enfoques de análisis de logs: el automatizado, que usa herramientas y scripts para procesar grandes volúmenes, y el manual, basado en la revisión humana.

1. Automated
2. Manual

### Task 6: Análisis de logs con comandos / Command-Line Log Analysis
**Explicación:** Se analiza el log con comandos de línea: se obtiene el hash MD5 de un artefacto, el número de eventos o peticiones, la IP del atacante y la marca temporal de una petición.

1. c701d43cc5a3acb9b5b04db7f1be94f6
2. 52
3. 145.76.33.201
4. 31/Jul/2023:12:34:40 +0000

### Task 7: Expresiones regulares / Regular Expressions
**Explicación:** Se construyen expresiones regulares para filtrar peticiones concretas del log (como blogs con ID entre 20 y 29) y se usa Grok como herramienta de parseo en ELK.

1. post=2[0-9]
2. Grok

### Task 8: CyberChef / CyberChef
**Explicación:** Se usa CyberChef para extraer IPs del log con regex, decodificar peticiones Base64 y extraer una dirección MAC de un fichero codificado, obteniendo la flag.

1. No answer needed
2. 212.14.17.145
3. THM{CYBERCHEF_WIZARD}
4. 08-2E-9A-4B-7F-61

### Task 9: Reglas de detección / Detection Rules
**Explicación:** Se aprende la estructura de una regla de detección: el formato YAML, el campo title que da nombre a la regla y el bloque rule que define la lógica de detección.

1. YAML
2. title
3. rule

### Task 10: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2 | Configuración del entorno | `No answer needed` |
| 3.1 | Término para la vista cronológica consolidada de eventos de diversas fuentes | `Super Timeline` |
| 3.2 | Resúmenes de integridad usados en el análisis | `File Hashes` |
| 4.1 | Ruta del log de acceso del servidor web | `/var/log/nginx/access.log` |
| 4.2 | Tipo de ataque detectado en el log | `Path Traversal` |
| 5.1 | Tipo de análisis que usa herramientas y scripts | `Automated` |
| 5.2 | Tipo de análisis que requiere revisión humana | `Manual` |
| 6.1 | Hash MD5 obtenido del análisis | `c701d43cc5a3acb9b5b04db7f1be94f6` |
| 6.2 | Número de eventos o peticiones contados | `52` |
| 6.3 | Dirección IP del atacante | `145.76.33.201` |
| 6.4 | Marca temporal de la petición | `31/Jul/2023:12:34:40 +0000` |
| 7.1 | Regex para filtrar peticiones post con ID entre 20 y 29 | `post=2[0-9]` |
| 7.2 | Herramienta de parseo de logs usada en ELK | `Grok` |
| 8.2 | Dirección IP encontrada que empieza por 212 | `212.14.17.145` |
| 8.3 | Flag al decodificar la petición Base64 | `THM{CYBERCHEF_WIZARD}` |
| 8.4 | Dirección MAC extraída del fichero codificado | `08-2E-9A-4B-7F-61` |
| 9.1 | Formato en el que se escriben las reglas de detección | `YAML` |
| 9.2 | Campo que define el nombre de la regla | `title` |
| 9.3 | Bloque principal con la lógica de detección | `rule` |
| 10 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Repaso de la teoría de investigación (Super Timeline y File Hashes), localización del log de acceso de nginx y detección del Path Traversal, comparación del análisis automatizado vs manual, análisis por comandos (md5, conteos, IP y timestamp), filtrado con expresiones regulares, parseo con Grok, decodificación y extracción de artefactos con CyberChef y creación de una regla de detección estructurada en YAML.

### Cadena de ataque / Attack Chain

Logs (nginx) -> teoría de investigación -> análisis automatizado/manual -> comandos y hash -> regex/Grok -> CyberChef (decode) -> regla de detección -> detección del ataque

**Learning chain:** log analysis -> investigation theory -> web server logs -> automated vs manual -> command-line analysis -> regex -> Grok -> CyberChef -> detection rules

**Lección:** *El análisis de logs combina teoría sólida y herramientas concretas (regex, Grok, CyberChef y reglas de detección) para convertir registros anodinos en pruebas accionables de un ataque.*

**MITRE ATT&CK:** N/A (sala defensiva; el Path Traversal detectado se asocia a T1190).

**Fuente:** [TryHackMe - Intro to Log Analysis](https://tryhackme.com/room/introtologanalysis)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.