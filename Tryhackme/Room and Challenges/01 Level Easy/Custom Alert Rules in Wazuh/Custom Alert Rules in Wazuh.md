# Custom Alert Rules in Wazuh

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Defensive Security / SIEM - Wazuh | `customalertrulesinwazuh` | https://tryhackme.com/room/customalertrulesinwazuh | 01 Level Easy | TryHackMe | Wazuh / Sysmon / decoders / regex / reglas personalizadas (local_rules.xml) / Ruleset Test / MITRE ATT&CK / auditd | Entender cómo Wazuh extrae información de los logs (decoders + regex) y cómo crear reglas de alerta personalizadas para cubrir casos no contemplados por las reglas por defecto. |

---

**Contexto:** Sala defensiva sobre Wazuh (SIEM/XDR). El reto simula al analista de SOC que debe afinar un despliegue de Wazuh: primero se analiza cómo los decoders extraen campos de los logs de Sysmon con expresiones regulares, después se revisa la lógica del ruleset (IDs de reglas, niveles y mapeo MITRE) y finalmente se crean reglas personalizadas en `local_rules.xml` para detectar comportamiento relevante para la organización (por ejemplo, ejecución de procesos en directorios de trabajo concretos).

> **ES:** "Aprende cómo funcionan los decoders de Wazuh, cómo extraen campos con regex de los logs de Sysmon y cómo escribir tus propias reglas de alerta personalizadas."
> **EN:** "Learn how Wazuh decoders work, how they extract fields from Sysmon logs with regex, and how to write your own custom alert rules."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta el objetivo de la sala: las reglas por defecto no cubren todos los escenarios, así que las organizaciones crean reglas personalizadas. Se revisan objetivos y contexto de la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la introducción y los objetivos. / I've read the introduction and learning objectives. | `No answer needed` |

---

### Task 2: Decoders y Regex / Decoders and Regex

**Explicación:** En el log de Sysmon se observa la ejecución de PowerShell con un script concreto. El decoder extrae el campo `sysmon.commandLine` con el valor completo de la línea de comandos, y con la expresión regular del reto se extrae el nombre del usuario `WIN-P57C9KN929H\Alberto` (la máquina del lab). Primero se revisa el log de Sysmon dentro del lab de Wazuh.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Mirando el log de Sysmon, ¿cuál será el valor de `sysmon.commandLine`? / Looking at the Sysmon Log, what will the value of `sysmon.commandLine` be? | `"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" "-file" "C:\Users\Alberto\Desktop\test.ps1"` |
| 2 | Aplicando el regex del reto sobre el log, ¿qué valor se extrae (usuario)? / Applying the exercise regex to the log, what value is extracted (user)? | `WIN-P57C9KN929H\Alberto` |

---

### Task 3: Lógica del Ruleset / Understanding Ruleset Logic

**Explicación:** En la pestaña "Ruleset Test" del dashboard de Wazuh, al testear la regla ID 184666 se observa que está mapeada a la técnica MITRE `T1055`. Revisando la documentación oficial de Wazuh, la regla con nivel de clasificación 12 tiene la descripción "High importance event". Al modificar el campo `sysmon.image` a un proceso común como `taskhost.exe`, se observa que Wazuh asigna a esa ejecución el ID de regla `184736`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | De los resultados del Ruleset Test, ¿cuál es el ID MITRE de la regla 184666? / From the Ruleset Test results, what is the MITRE ID of rule id 184666? | `T1055` |
| 2 | Según la documentación de Wazuh, ¿cuál es la descripción de la regla con nivel de clasificación 12? / According to the Wazuh documentation, what is the description of the rule with a classification level of 12? | `High importance event` |
| 3 | ¿Qué ID de regla se asigna al cambiar el valor a `taskhost.exe`? / What is the rule ID assigned when changing the value to `taskhost.exe`? | `184736` |

---

### Task 4: Jerarquía de reglas / Rule hierarchy

**Explicación:** Las reglas de Wazuh se organizan en jerarquías: una regla puede heredar de otra regla padre mediante `<if_sid>`. En el análisis de la jerarquía del ruleset se determina cuál es el ID de la regla padre de la regla 184717.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el ID de la regla padre de la regla 184717? / What is the parent rule ID of rule 184717? | `184716` |

---

### Task 5: Implementando reglas personalizadas / Implementing Custom Rules

**Explicación:** Cuando las reglas por defecto son demasiado genéricas, se edita `local_rules.xml` en el Wazuh Manager para añadir lógica específica. En el ejemplo se vigila el directorio de trabajo actual (current working directory) mediante la etiqueta `<regex>` sobre el campo `audit.cwd`, y la ejecución analizada se produce desde el directorio `/var/log/audit`.

```xml
<rule id="..." level="...">
  <if_sid>...</if_sid>
  <regex field="audit.cwd">/var/log/audit</regex>
  <description>...</description>
</rule>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre del campo regex usado en el `local_rules.xml`? / What is the regex field name used in the `local_rules.xml`? | `audit.cwd` |
| 2 | ¿En qué directorio de trabajo (cwd) se ejecuta el proceso analizado? / What is the current working directory (cwd) of the analyzed process? | `/var/log/audit` |

---

### Task 6: Reglas para auditoría / Rules for auditing

**Explicación:** Para el caso del fichero `test.php` se define/obtiene la regla personalizada con ID `100003`. Además, ejecutando el script de comprobación `malware-checker.sh` sobre la regla creada, el nivel (level) que se asigna al dispararse es `12`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el ID de regla para `test.php`? / What is the rule ID for `test.php`? | `100003` |
| 2 | ¿Qué nivel asigna `malware-checker.sh` a la regla creada? / What is the level assigned by `malware-checker.sh`? | `12` |

---

### Task 7: Conclusión / Conclusion

**Explicación:** Se resume lo aprendido: decoders y regex para extraer datos, lógica de ruleset y creación de reglas personalizadas como práctica habitual de todo SOC. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He completado los objetivos de la sala. / I've completed the room objectives. | `No answer needed` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Introducción. / Introduction. | `No answer needed` |
| 2 | Task 2 | ¿Cuál es el valor de `sysmon.commandLine`? / What is the value of `sysmon.commandLine`? | `"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" "-file" "C:\Users\Alberto\Desktop\test.ps1"` |
| 3 | Task 2 | ¿Qué valor extrae el regex? / What value does the regex extract? | `WIN-P57C9KN929H\Alberto` |
| 4 | Task 3 | ID MITRE de la regla 184666. / MITRE ID of rule 184666. | `T1055` |
| 5 | Task 3 | Descripción de la regla con nivel 12. / Description of the rule with level 12. | `High importance event` |
| 6 | Task 3 | Regla asignada con `taskhost.exe`. / Rule ID assigned with `taskhost.exe`. | `184736` |
| 7 | Task 4 | Regla padre de la 184717. / Parent rule ID of 184717. | `184716` |
| 8 | Task 5 | Campo regex en `local_rules.xml`. / Regex field in `local_rules.xml`. | `audit.cwd` |
| 9 | Task 5 | Directorio de trabajo (cwd). / Current working directory (cwd). | `/var/log/audit` |
| 10 | Task 6 | Regla para `test.php`. / Rule ID for `test.php`. | `100003` |
| 11 | Task 6 | Nivel de `malware-checker.sh`. / Level assigned by `malware-checker.sh`. | `12` |
| 12 | Task 7 | Conclusión. / Conclusion. | `No answer needed` |

---

**Metodología:** Revisar los logs de Sysmon en el dashboard de Wazuh -> entender qué campos extrae el decoder y con qué regex -> usar la pestaña "Ruleset Test" para inspeccionar reglas, niveles y mapeo MITRE -> modificar campos (ej. `taskhost.exe`) para ver el ID resultante -> explorar la jerarquía de reglas (padres) -> escribir la regla personalizada en `local_rules.xml` con `<regex field="audit.cwd">` -> validar con `malware-checker.sh`.

### Cadena de ataque / Attack Chain

```text
Logs Sysmon -> decoder + regex -> sysmon.commandLine -> usuario WIN-P57C9KN929H\Alberto -> Ruleset Test -> T1055 / level 12 -> taskhost.exe -> 184736 -> parent 184716 -> local_rules.xml (audit.cwd /var/log/audit) -> test.php -> 100003 -> level 12 -> alerta válida
```

**Learning chain:** Wazuh -> decoders -> regex -> ruleset test -> MITRE mapping -> reglas jerárquicas -> local_rules.xml -> validación.

**Lección:** *Un SIEM solo es útil si las reglas se adaptan a tu entorno; saber leer qué extrae un decoder y cómo escribir `<regex>` en `local_rules.xml` permite detectar lo que las reglas genéricas no cubren.*

**MITRE ATT&CK:** T1055 (Process Injection; mapeo de la regla 184666), T1059 (Command and Scripting Interpreter - PowerShell)

**Fuente:** [TryHackMe - Custom Alert Rules in Wazuh](https://tryhackme.com/room/customalertrulesinwazuh)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.