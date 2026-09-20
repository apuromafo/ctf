# Server-side Template Injection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Web (SSTI) | serversidetemplateinjection | https://tryhackme.com/room/serversidetemplateinjection | 02 Level Medium | TryHackMe | Plantillas del lado del servidor, Smarty (PHP), Pug (NodeJS), Jinja2 (Python), detección con `{{7*7}}`, SSTImap, automatización, CVE-2024-22722 en Form Tools, RCE | Ejecución remota de código por inyección en motores de plantillas (Smarty, Pug, Jinja2) y explotación automatizada hasta leer ficheros ocultos del servidor |

---

**Contexto:** La sala **Server-side Template Injection** explica qué es la **inyección de plantillas del lado del servidor (SSTI)**, una vulnerabilidad que se produce cuando la entrada del usuario se interpola directamente en un motor de plantillas y se evalúa como código. Recorre los motores más comunes por lenguaje: **Smarty** en PHP, **Pug** en NodeJS y **Jinja2** en Python; en cada uno se detecta la inyección con el clásico payload `{{7*7}}` (si se renderiza "49", hay SSTI) y se explota para leer un archivo oculto del directorio del servidor. Después presenta la automatización de la explotación con **SSTImap** y cierra con el *Extra-Mile Challenge*: aprovechar la **CVE-2024-22722** (SSTI en Form Tools 3.1.1 a través del campo "Group Name") para ejecutar comandos como `exec('whoami')` y leer la flag final oculta.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Definición de SSTI: entrada del usuario tratada como código de plantilla en el servidor. Se deben conocer el entorno, el lenguaje y el motor de plantillas para explotarlo. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer la introducción de la sala | `No answer needed` |

### Task 2: Panorama SSTI / SSTI Overview
**Explicación:** Cómo se genera la vulnerabilidad y cómo la detección (inyectar expresiones como `{{7*7}}`) permite confirmarla antes de buscar el motor. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer el material de la tarea | `No answer needed` |

### Task 3: Motores de plantillas / Template Engines
**Explicación:** Comparación de motores de plantillas (Smarty/PHP, Pug/NodeJS, Jinja2/Python) y del riesgo de evaluar la entrada sin sanitizar. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer el material de la tarea | `No answer needed` |

### Task 4: PHP - Smarty
**Explicación:** Con Smarty se confirma la inyección y se obtiene la lectura del archivo oculto del servidor. Con payloads propios de Smarty (por ejemplo, acceso a literales y funciones del motor) se hace el *read* del fichero que contiene la flag.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the content of the hidden text file in the server directory? (PHP - Smarty) | `THM{0739eea78f5c7f4b1690737c6258e38b}` |

### Task 5: NodeJS - Pug
**Explicación:** En el motor **Pug** (NodeJS) se aprovechan las peculiaridades de su sintaxis de interpolación para ejecutar código JavaScript y leer el archivo oculto del directorio del servidor.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the content of the hidden text file in the server directory? (NodeJS - Pug) | `THM{1f8c3b32ad3217e84c145398bae00876}` |

### Task 6: Python - Jinja2
**Explicación:** En **Jinja2** (Python) el clásico camino de SSTI a RCE recorre los *builtins* y módulos de Python: mediante payloads como `{{request.application.__globals__.__builtins__...}}` (o el acceso directo a `__import__('os')`) se ejecuta un comando y se lee el archivo oculto del servidor.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the content of the hidden text file in the server directory? (Python - Jinja2) | `THM{ecc43642dd6934d37c69598174e6e126}` |

### Task 7: Automatizando la explotación / Automating the Exploitation
**Explicación:** Se presenta **SSTImap**, una herramienta que automatiza la detección y explotación de SSTI en diferentes motores. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Seguir el material sobre SSTImap | `No answer needed` |

### Task 8: Extra-Mile Challenge
**Explicación:** Aprovechando la **CVE-2024-22722** (SSTI en **Form Tools 3.1.1** a través del campo "Group Name" en la sección de Views) se confirma con `{{7*7}}` → 49, se ejecutan comandos con `{{exec('whoami')}}` y se localiza el fichero oculto del directorio web (`ls -r /var/www/html/*.txt`) para, finalmente, leerlo con `cat` y obtener la flag.

```text
{{7*7}} -> 49                  (confirmación de SSTI)
{{exec('whoami')}}             (RCE)
{{exec('ls -r /var/www/html/*.txt')}}
   -> /var/www/html/105e15924c1e41bf53ea64afa0fa72b2.txt
{{exec('cat /var/www/html/105e15924c1e41bf53ea64afa0fa72b2.txt')}}
   -> THM{w0rK1Ng_sST1}
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the content of the hidden text file in the server directory? (Extra-Mile Challenge) | `THM{w0rK1Ng_sST1}` |

### Task 9: Mitigación / Mitigation
**Explicación:** Cómo prevenir SSTI: no pasar entradas de usuario directamente a los motores de plantillas, sanitizar caracteres especiales, usar entornos de plantillas aislados (sandbox) que bloqueen `exec()` y aplicar el principio de menor privilegio al proceso del servidor. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer las recomendaciones de mitigación | `No answer needed` |

### Task 10: Conclusión / Conclusion
**Explicación:** Resumen final de la sala. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer el cierre de la sala | `No answer needed` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the hidden text file in the server directory? (PHP - Smarty) | `THM{0739eea78f5c7f4b1690737c6258e38b}` |
| 2 | What is the content of the hidden text file in the server directory? (NodeJS - Pug) | `THM{1f8c3b32ad3217e84c145398bae00876}` |
| 3 | What is the content of the hidden text file in the server directory? (Python - Jinja2) | `THM{ecc43642dd6934d37c69598174e6e126}` |
| 4 | What is the content of the hidden text file in the server directory? (Extra-Mile Challenge) | `THM{w0rK1Ng_sST1}` |

---

**Metodología:** Contexto e identificación del motor de plantillas → detección de SSTI con `{{7*7}}` → explotación por motor (Smarty, Pug, Jinja2) para lectura de archivos → automatización con SSTImap → aplicación práctica: CVE-2024-22722 en Form Tools (campo "Group Name") → RCE (`exec`) y lectura del flag oculto → recomendaciones de mitigación y sandboxing.

**Learning chain:** Comprender el renderizado de plantillas → detectar la inyección (`{{7*7}}`) → discriminar el motor (PHP/NodeJS/Python) → encadenar payloads específicos hasta RCE → automatizar con SSTImap → explotar una CVE real (Form Tools) → hardened del servidor.

**Lección:** *Un campo mal sanitizado que termina en un motor de plantillas es una puerta directa a RCE en PHP, NodeJS y Python; la detección temprana (`{{7*7}}`) y el sandboxing de los motores son la primera línea de defensa.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059.007 Command and Scripting Interpreter (JavaScript) · T1059.006 Command and Scripting Interpreter (Python) · T1059.003 Command and Scripting Interpreter (Windows Command Shell/PHP) · T1071.001 Web Protocols · T1005 Data from Local System (lectura de ficheros).

**Fuente:** [TryHackMe - Server-side Template Injection](https://tryhackme.com/room/serversidetemplateinjection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.