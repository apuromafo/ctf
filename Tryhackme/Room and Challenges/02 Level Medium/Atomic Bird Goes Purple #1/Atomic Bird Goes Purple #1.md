# Atomic Bird Goes Purple #1

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | atomicbirdgoespurple1 |
| Link | https://tryhackme.com/room/atomicbirdgoespurple1 |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Atomic Red Team, MITRE ATT&CK, Emulation |
| Impacto | Alto |

---

**Contexto:** Sala de emulación ofensiva que guía al participante a ejecutar técnicas del MITRE ATT&CK utilizando Atomic Red Team. El objetivo es practicar la emulación de adversarios de forma controlada, ejecutando pruebas atómicas específicas, analizando resultados y limpiando rastros. Se enfoca en el ciclo completo de emulación: planificación, ejecución, análisis y limpieza.

## Solucionario

### Task 1: Introduccion
**Explicación:** Esta task presenta el concepto de emulación ofensiva y su importancia en la ciberseguridad defensiva. Se familiariza al participante con Atomic Red Team como framework de emulación basado en el MITRE ATT&CK.

1. No answer needed

### Task 2: Preparacion del Entorno
**Explicación:** Configuración del entorno de laboratorio para ejecutar pruebas atómicas. Se instalan herramientas necesarias y se prepara el sistema para la emulación.

2. No answer needed

### Task 3: Ejecucion de Pruebas Atomicas
**Explicación:** Ejecución práctica de pruebas atómicas del MITRE ATT&CK. Se ejecuta la técnica T0123 para emular comportamientos de adversarios y se验证a la detección. La limpieza se realiza con Invoke-AtomicTest T0123-4 -Cleanup.

3. 1. THM{Emulation_is_fun_but_needs_focus_and_exploration}
   2. Invoke-AtomicTest T0123-4 -Cleanup

### Task 4: Analisis de Resultados
**Explicación:** Análisis de los resultados obtenidos de la ejecución de pruebas atómicas. Se examina la información del sistema operativo y se valida la emulación realizada.

4. 1. 10.0.17763 N/A Build 17763
   2. THM{THM_Emulation_Room}
   3. <!bin/bash>

### Task 5: Verificacion de Indicadores
**Explicación:** Verificación de indicadores de compromiso generados durante la emulación. Se analizan hashes de archivos creados o modificados durante las pruebas.

5. 1. 3CA9FB42ACF0A347BDFDC78E0435331BC458194E4BC7FBFFB255BC4CF02CDC1A
   2. 626DBB861DCFF600DABEFCE7BF93F2C72C0F6462CC5729B963FC8242D7D43990

### Task 6: Exfiltracion y Credenciales
**Explicación:** Emulación de técnicas de exfiltración y obtención de credenciales. Se simula el movimiento de un adversario dentro de la red y se documentan los hallazgos.

6. 1. THM{THM_analytics_to_exfiltration_with_NexGenHunt}
   2. THM{NextGenHunt.thm.jhn}

### Task 7: Limpieza y Conclusion
**Explicación:** Limpieza final del entorno de emulación y cierre de la actividad. Se eliminan artefactos creados durante las pruebas.

7. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2 | No answer needed |
| 3 | Task 3.1 | THM{Emulation_is_fun_but_needs_focus_and_exploration} |
| 3 | Task 3.2 | Invoke-AtomicTest T0123-4 -Cleanup |
| 4 | Task 4.1 | 10.0.17763 N/A Build 17763 |
| 4 | Task 4.2 | THM{THM_Emulation_Room} |
| 4 | Task 4.3 | <!bin/bash> |
| 5 | Task 5.1 | 3CA9FB42ACF0A347BDFDC78E0435331BC458194E4BC7FBFFB255BC4CF02CDC1A |
| 5 | Task 5.2 | 626DBB861DCFF600DABEFCE7BF93F2C72C0F6462CC5729B963FC8242D7D43990 |
| 6 | Task 6.1 | THM{THM_analytics_to_exfiltration_with_NexGenHunt} |
| 6 | Task 6.2 | THM{NextGenHunt.thm.jhn} |
| 7 | Task 7 | No answer needed |

---

**Metodología:** Atomic Red Team / Emulación de adversarios basada en MITRE ATT&CK. Ejecución controlada de pruebas atómicas para validar capacidades de detección y respuesta.

**Learning chain:** Emulación ofensiva -> Ejecución de pruebas -> Análisis de resultados -> Detección -> Limpieza

**Lección:** _La emulación de adversarios con Atomic Red Team permite validar defensas de forma controlada y repetible._

**MITRE ATT&CK:** TA0002 (Execution), T1106 (Native API), T1059.001 (PowerShell), T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - Atomic Bird Goes Purple #1](https://tryhackme.com/room/atomicbirdgoespurple1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
