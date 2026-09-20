# Red Team Engagements

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `redteamengagements` | https://tryhackme.com/room/redteamengagements | 01 Level Easy | TryHackMe | Red Team / alcance / SOW / vectores de acceso / phishing / Cobalt Strike / vectr.io / presupuesto | Sala formativa sobre el ciclo de vida completo de un compromiso de Red Team: alcance, planificación, simulación, presupuesto y evaluación de resultados. |

---

**Contexto:** Sala que explica cómo se organiza y ejecuta un compromiso de Red Team de principio a fin. Recorre el alcance del ejercicio (rangos y activos autorizados), los vectores de acceso inicial (phishing como vector principal), la planificación operativa con sus plazos y herramientas (Cobalt Strike), los costes y recursos del proyecto y la evaluación final de la simulación con plataformas como vectr.io.

> **ES:** "Red Team Engagements" — cómo planificar, ejecutar y evaluar un compromiso real de Red Team: alcance, plazos, presupuesto, herramientas y medición de resultados.
> **EN:** "Red Team Engagements" — how to plan, execute and evaluate a real Red Team engagement: scope, timelines, budget, tooling and outcomes measurement.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala: concepto de compromiso de Red Team y de los elementos que se van a cubrir (alcance, presupuesto, vectores, planificación y evaluación). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |

### Task 2: Alcance y preparación / Pre-Engagement & Scope

**Explicación:** La tarea define el alcance del compromiso: el rango de red autorizado para las operaciones es `10.0.4.0/22`. Las preguntas confirmatorias de alcance se responden con `Y` (los rangos objetivos están autorizados) y `N` (aquello que queda fuera del contrato no es válido).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el escenario inicial de la sala. / Review the room's initial scenario. | `No answer needed` |
| 2 | Completa la revisión del alcance del compromiso. / Complete the engagement scope review. | `No answer needed` |
| 3 | ¿Qué rango de red se define como alcance del compromiso? / What network range is defined as the engagement scope? | `10.0.4.0/22` |
| 4 | ¿El alcance del compromiso incluye el rango indicado? (Y/N) / Does the engagement scope include the indicated range? (Y/N) | `Y` |
| 5 | ¿Está permitido atacar sistemas fuera del alcance del contrato? (Y/N) / Is it allowed to attack systems outside the contract scope? (Y/N) | `N` |

### Task 3: Vectores de acceso inicial / Initial Access Vectors

**Explicación:** Se identifican los vectores de acceso inicial a tener en cuenta en la operación. De las opciones planteadas hay `3` vectores válidos y el principal entre ellos es el `Phishing`. La pregunta confirmatoria sobre si el vector mencionado es el adecuado responden `N`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee las opciones de vector de acceso de la sala. / Read the room's access vector options. | `No answer needed` |
| 2 | ¿Cuántos vectores de acceso válidos se identifican? / How many valid access vectors are identified? | `3` |
| 3 | ¿Cuál es el vector de acceso principal considerado? / What is the primary access vector considered? | `Phishing` |
| 4 | ¿El vector elegido se considera el correcto para este escenario? (Y/N) / Is the chosen vector considered the right one for this scenario? (Y/N) | `N` |

### Task 4: Bases de conocimiento / Knowledge Bases

**Explicación:** Apartado sobre las bases de conocimiento y recursos que documentan el compromiso (tácticas, técnicas y procedimientos del adversario). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el apartado de bases de conocimiento. / Read the knowledge bases section. | `No answer needed` |

### Task 5: Plan operativo / Operational Planning

**Explicación:** Fase de planificación operativa del compromiso: definición de objetivos de red, tiempos y estructuras del ejercicio. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el apartado de plan operativo. / Read the operational planning section. | `No answer needed` |

### Task 6: Tiempos y herramientas / Timelines & Tooling

**Explicación:** La planificación temporal del compromiso establece una duración total de `1 Month`, de los cuales `3 Weeks` corresponden a la fase de simulación activa. La herramienta central utilizada como C2 para la operación es `Cobalt Strike`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee los tiempos definidos para el compromiso. / Read the timelines defined for the engagement. | `No answer needed` |
| 2 | Lee las herramientas seleccionadas para la operación. / Read the tooling selected for the operation. | `No answer needed` |
| 3 | ¿Cuál es la duración total del compromiso? / What is the total duration of the engagement? | `1 Month` |
| 4 | ¿Cuánto dura la fase de simulación activa? / How long does the active simulation phase last? | `3 Weeks` |
| 5 | ¿Qué herramienta de C2 se utiliza en la operación? / What C2 tool is used in the operation? | `Cobalt Strike` |

### Task 7: Presupuesto y recursos / Budget & Resources

**Explicación:** Se revisa el presupuesto del proyecto: la comprobación de la fecha indicada es `11/14/2021` y el gasto planificado para la operación es de `$1000`. La pregunta sobre si el gasto supera el presupuesto autorizado se responde con `N`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el presupuesto del proyecto. / Read the project budget. | `No answer needed` |
| 2 | ¿Qué fecha aparece en la comprobación del proyecto? / What date appears in the project check? | `11/14/2021` |
| 3 | ¿Qué coste está planificado para la operación? / What cost is planned for the operation? | `$1000` |
| 4 | ¿El coste planificado supera el presupuesto autorizado? (Y/N) / Does the planned cost exceed the authorized budget? (Y/N) | `N` |

### Task 8: Phishing y herramientas de simulación / Phishing & Simulation Tools

**Explicación:** El vector de acceso simulado con más éxito es `Spearphishing`, y la plataforma usada para medir y documentar la simulación de adversarios es `vectr.io`. La pregunta sobre si el compromiso ya ha finalizado en este punto responde `F`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el apartado de phishing y simulación. / Read the phishing and simulation section. | `No answer needed` |
| 2 | ¿Qué tipo de phishing se emplea como vector? / What type of phishing is used as the vector? | `Spearphishing` |
| 3 | ¿Qué plataforma se utiliza para la simulación del adversario? / What platform is used for adversary simulation? | `vectr.io` |
| 4 | ¿El compromiso se da por finalizado en esta fase? (T/F) / Is the engagement considered finished at this point? (T/F) | `F` |

### Task 9: Evaluación final / Final Assessment

**Explicación:** Evaluación final del compromiso: la fecha de cierre registrada es `10/23/2021`. Las preguntas de verificación sobre si los objetivos de la red se han cumplido y sobre si la operación global ha sido un éxito se responden con `N` y `F` respectivamente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la evaluación final del ejercicio. / Read the exercise's final assessment. | `No answer needed` |
| 2 | ¿Qué fecha de cierre se registra en la evaluación? / What closing date is recorded in the assessment? | `10/23/2021` |
| 3 | ¿Se han cumplido todos los objetivos de la red? (Y/N) / Have all the network objectives been met? (Y/N) | `N` |
| 4 | ¿La operación global se considera un éxito? (T/F) / Is the overall operation considered a success? (T/F) | `F` |

### Task 10: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen del ciclo de vida completo de un compromiso de Red Team. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |
| 2 | Revisa el escenario inicial de la sala. / Review the room's initial scenario. | `No answer needed` |
| 3 | Completa la revisión del alcance del compromiso. / Complete the engagement scope review. | `No answer needed` |
| 4 | ¿Qué rango de red se define como alcance del compromiso? / What network range is defined as the engagement scope? | `10.0.4.0/22` |
| 5 | ¿El alcance del compromiso incluye el rango indicado? (Y/N) / Does the engagement scope include the indicated range? (Y/N) | `Y` |
| 6 | ¿Está permitido atacar sistemas fuera del alcance del contrato? (Y/N) / Is it allowed to attack systems outside the contract scope? (Y/N) | `N` |
| 7 | Lee las opciones de vector de acceso de la sala. / Read the room's access vector options. | `No answer needed` |
| 8 | ¿Cuántos vectores de acceso válidos se identifican? / How many valid access vectors are identified? | `3` |
| 9 | ¿Cuál es el vector de acceso principal considerado? / What is the primary access vector considered? | `Phishing` |
| 10 | ¿El vector elegido se considera el correcto para este escenario? (Y/N) / Is the chosen vector considered the right one for this scenario? (Y/N) | `N` |
| 11 | Lee el apartado de bases de conocimiento. / Read the knowledge bases section. | `No answer needed` |
| 12 | Lee el apartado de plan operativo. / Read the operational planning section. | `No answer needed` |
| 13 | Lee los tiempos definidos para el compromiso. / Read the timelines defined for the engagement. | `No answer needed` |
| 14 | Lee las herramientas seleccionadas para la operación. / Read the tooling selected for the operation. | `No answer needed` |
| 15 | ¿Cuál es la duración total del compromiso? / What is the total duration of the engagement? | `1 Month` |
| 16 | ¿Cuánto dura la fase de simulación activa? / How long does the active simulation phase last? | `3 Weeks` |
| 17 | ¿Qué herramienta de C2 se utiliza en la operación? / What C2 tool is used in the operation? | `Cobalt Strike` |
| 18 | Lee el presupuesto del proyecto. / Read the project budget. | `No answer needed` |
| 19 | ¿Qué fecha aparece en la comprobación del proyecto? / What date appears in the project check? | `11/14/2021` |
| 20 | ¿Qué coste está planificado para la operación? / What cost is planned for the operation? | `$1000` |
| 21 | ¿El coste planificado supera el presupuesto autorizado? (Y/N) / Does the planned cost exceed the authorized budget? (Y/N) | `N` |
| 22 | Lee el apartado de phishing y simulación. / Read the phishing and simulation section. | `No answer needed` |
| 23 | ¿Qué tipo de phishing se emplea como vector? / What type of phishing is used as the vector? | `Spearphishing` |
| 24 | ¿Qué plataforma se utiliza para la simulación del adversario? / What platform is used for adversary simulation? | `vectr.io` |
| 25 | ¿El compromiso se da por finalizado en esta fase? (T/F) / Is the engagement considered finished at this point? (T/F) | `F` |
| 26 | Lee la evaluación final del ejercicio. / Read the exercise's final assessment. | `No answer needed` |
| 27 | ¿Qué fecha de cierre se registra en la evaluación? / What closing date is recorded in the assessment? | `10/23/2021` |
| 28 | ¿Se han cumplido todos los objetivos de la red? (Y/N) / Have all the network objectives been met? (Y/N) | `N` |
| 29 | ¿La operación global se considera un éxito? (T/F) / Is the overall operation considered a success? (T/F) | `F` |
| 30 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

**Metodología:** Recorrer el ciclo de vida del compromiso de Red Team: definir el alcance y los rangos autorizados, identificar los vectores de acceso (Phishing / Spearphishing), planificar plazos (1 Month, 3 Weeks) y herramientas (Cobalt Strike, vectr.io), validar el presupuesto (`$1000`) y cerrar con la evaluación de fechas y resultados del ejercicio.

### Cadena de ataque / Attack Chain

```text
Definir alcance (10.0.4.0/22) -> Seleccionar vectores (Phishing / Spearphishing) -> Planificar plazos (1 Month / 3 Weeks) -> Preparar C2 (Cobalt Strike) -> Presupuesto ($1000) -> Simulación (vectr.io) -> Evaluación final y cierre
```

**Learning chain:** Alcance -> Vectores de acceso -> Plan operativo -> Tiempos y herramientas -> Presupuesto -> Simulación (vectr.io) -> Evaluación final.

**Lección:** *Un compromiso de Red Team exitoso se juega antes de atacar: un alcance bien definido, un presupuesto realista y una medición (vectr.io) de los resultados son tan importantes como las propias herramientas de ataque.*

**MITRE ATT&CK:** T1566 (Phishing), T1190 (Exploit Public-Facing Application), T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - Red Team Engagements](https://tryhackme.com/room/redteamengagements)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.