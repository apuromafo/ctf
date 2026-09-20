# SAST

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / DevSecOps | sast | https://tryhackme.com/room/sast | 02 Level Medium | TryHackMe | SAST (Static Application Security Testing), revisión vs. automatización, análisis estructural/de configuración/semántico, Psalm, Semgrep (VS Code), LFI en PHP (incluse/view.php), ReciPHP y simple-webapp | Detección y triaje de vulnerabilidades en código fuente (LFI, SQLi, XSS) mediante herramientas SAST, y comprensión de falsos positivos y límites frente a la revisión manual |

---

**Contexto:** La sala **SAST** pertenece al learning path de **DevSecOps** y enseña el uso de herramientas de **análisis estático de seguridad de aplicaciones (SAST)**. Primero compara la revisión automatizada con la manual, describe los tipos de análisis (estructural, de configuración y semántico) y aclara el concepto de falso positivo. Después aplica `grep` sobre el proyecto PHP `simple-webapp` para localizar funciones peligrosas de inclusión de archivos (`include()`) y el caso concreto vulnerable a **LFI** (`view.php:22`). En la parte práctica se trabaja con **Psalm** y la extensión **Semgrep** de VS Code sobre el proyecto `reciphp` (ReciPHP): Semgrep reporta problemas en todo el proyecto (entre ellos `tainted-sql-string` y `echoed-request`, asociado a **cross-site scripting**) y permite catalogar los hallazgos y sus falsos positivos.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Introducción a la sala SAST y al análisis estático de código. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Deployar/leer el material de la tarea | `No answer needed` |

### Task 2: Revisión automatizada vs. manual / Automated vs. manual review
**Explicación:** Se explica la diferencia entre la revisión automática de código (SAST) y la revisión manual: la automatización corre más rápido, pero la revisión manual es más exhaustiva y, por tanto, las herramientas no sustituyen la revisión humana.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Are automated code reviews a substitute for manual reviewing? (yea/nay) | `nay` |
| 2 | What type of code review will run faster? (Manual/Automated) | `Automated` |
| 3 | What type of code review will be more thorough? (Manual/Automated) | `Manual` |

### Task 3: LFI con grep en simple-webapp / LFI with grep in simple-webapp
**Explicación:** Con `grep` se buscan las funciones de inclusión de archivos en los `.php` de `html/` del proyecto `simple-webapp`: solo aparece `include()`, con 9 instancias. De ellas, únicamente una recibe datos manipulables (una variable GET/POST) y por eso es la vulnerable a LFI: está en `view.php`, en la línea 22.

```bash
cd /home/ubuntu/Desktop/simple-webapp/html
grep -r -n --include '*.php' 'include(' .
# include() -> 9 instancias
# instancia vulnerable (parámetro manipulable): view.php:22
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Ejecutar el grep y revisar el proyecto | `No answer needed` |
| 2 | Which of the mentioned functions is used in the project? (Include the parenthesis at the end of the function name) | `include()` |
| 3 | How many instances of the function found in question 2 exist in your project's code? | `9` |
| 4 | What file contains the vulnerable instance? | `view.php` |
| 5 | What line in the file found on the previous question is vulnerable to LFI? | `22` |

### Task 4: Análisis estructural, de configuración y semántico / Types of SAST analysis
**Explicación:** Se profundiza en los tipos de análisis SAST: el análisis estructural (structural) detecta, por ejemplo, segmentos de código muerto; el de configuración encuentra fallos en archivos de configuración; y el semántico se asemeja a "grep" en busca de fallos. También se aclara que el análisis estático NO necesita una instancia en ejecución de la aplicación.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Does SAST require a running instance of the application for analysis? (yea/nay) | `nay` |
| 2 | What kind of analysis would likely flag dead code segments? | `structural analysis` |
| 3 | What kind of analysis would likely detect flaws in configuration files? | `configuration analysis` |
| 4 | What kind of analysis is similar to grepping the code in search of flaws? | `semantic analysis` |

### Task 5: Psalm / Psalm
**Explicación:** Se trabaja con Psalm sobre el proyecto: un falso positivo es un informe que la herramienta emite sobre una vulnerabilidad que no existe realmente en el código. Tras anotar el código como se indica en la tarea y re-ejecutar Psalm, se reportan 9 errores.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What type of error occurs when the tool reports on a vulnerability that isn't present in the code? | `false positive` |
| 2 | How many errors are reported after annotating the code as instructed in this task and re-running Psalm? | `9` |

### Task 6: Semgrep en ReciPHP / Semgrep on ReciPHP
**Explicación:** Se abre el workspace `reciphp.code-workspace` en VS Code (cargar tarda unos minutos) y Semgrep escanea el proyecto completo: 27 problemas en total. En `showrecipe.inc.php` se reportan 8 problemas, de dos tipos: `tainted-sql-string` (posibles inyecciones SQL) y `echoed-request`. La regla asociada a `echoed-request` corresponde a vulnerabilidades de **cross-site scripting**.

```bash
# Regla de Semgrep asociada al identificador
cat /home/ubuntu/Desktop/reciphp/semgrep-rules/php.lang.security.injection.echoed-request.echoed-request.yaml
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Abrir el workspace e inspeccionar los problemas | `No answer needed` |
| 2 | How many problems in total are detected by Semgrep in this project? | `27` |
| 3 | How many problems are detected in the showrecipe.inc.php file? | `8` |
| 4 | Open showrecipe.inc.php. One problem identifier is "tainted-sql-string". What other problem identifier is reported by Semgrep in this file? (Write the id reported by Semgrep) | `echoed-request` |
| 5 | What type of vulnerability is associated with the problem identifier on the previous question? | `cross-site scripting` |

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala: el SAST es una herramienta valiosa en el ciclo DevSecOps, pero complementa (no sustituye) a la revisión manual. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer el material de cierre de la sala | `No answer needed` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are automated code reviews a substitute for manual reviewing? (yea/nay) | `nay` |
| 2 | What type of code review will run faster? (Manual/Automated) | `Automated` |
| 3 | What type of code review will be more thorough? (Manual/Automated) | `Manual` |
| 4 | Does SAST require a running instance of the application for analysis? (yea/nay) | `nay` |
| 5 | What kind of analysis would likely flag dead code segments? | `structural analysis` |
| 6 | What kind of analysis would likely detect flaws in configuration files? | `configuration analysis` |
| 7 | What kind of analysis is similar to grepping the code in search of flaws? | `semantic analysis` |
| 8 | What type of error occurs when the tool reports on a vulnerability that isn't present in the code? | `false positive` |
| 9 | How many errors are reported after annotating the code as instructed in this task and re-running Psalm? | `9` |
| 10 | Which of the mentioned functions is used in the project? (Include the parenthesis at the end of the function name) | `include()` |
| 11 | How many instances of the function found in the project exist? | `9` |
| 12 | What file contains the vulnerable instance? | `view.php` |
| 13 | What line in the file found on the previous question is vulnerable to LFI? | `22` |
| 14 | How many problems in total are detected by Semgrep in this project? | `27` |
| 15 | How many problems are detected in the showrecipe.inc.php file? | `8` |
| 16 | What other problem identifier is reported by Semgrep in showrecipe.inc.php? | `echoed-request` |
| 17 | What type of vulnerability is associated with the problem identifier on the previous question? | `cross-site scripting` |

---

**Metodología:** Revisión estática del código (grep de funciones de inclusión en PHP) → análisis con Psalm (falsos positivos y anotaciones) → análisis con Semgrep vía VS Code (detección global de problemas y lectura de reglas `yaml`) → correlación de identificadores de regla con tipos de vulnerabilidad (LFI, SQLi, XSS) → clasificación de hallazgos reales vs. falsos positivos.

**Learning chain:** Fundamentos SAST (manual vs. automática, tipos de análisis) → detección de patrones peligrosos en código PHP (`include()`) → triaje de un LFI real (`view.php:22`) → uso de Psalm y Semgrep → lectura de reglas personalizadas → impacto final (XSS, SQLi, LFI).

**Lección:** *Una herramienta SAST acelera la detección de vulnerabilidades en el código, pero genera falsos positivos y debe complementarse con revisión manual: el contexto (input controlable, línea, proyecto) decide qué hallazgo es explotable.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application (LFI) · T1189 Drive-by Compromise / pobres prácticas en el SDLC · T1059.009 Command and Scripting Interpreter (elementos relacionados con la fase de pruebas estáticas y de seguridad del SDLC) · T1185/taquigrafía de seguridad de aplicaciones (assessment en el ciclo de desarrollo).

**Fuente:** [TryHackMe - SAST](https://tryhackme.com/room/sast)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.