# IR Playbooks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `irplaybooks` | [TryHackMe](https://tryhackme.com/room/irplaybooks) | 01 Level Easy | TryHackMe | Incident Response, playbooks, ciclo de vida de la IR, Preparation, Containment, WannaCry, línea base conocida | Comprender el uso de playbooks en la respuesta a incidentes y aplicarlos a un caso real de ransomware como WannaCry. |

---

**Contexto:** Sala sobre los playbooks de respuesta a incidentes. Explica la diferencia entre runbooks y playbooks, cuándo usarlos, las fases del ciclo de vida de la IR (preparación), el cierre del incidente, la recuperación y la actividad posterior al incidente. Incluye un caso práctico sobre una infección de WannaCry donde se identifica el servicio sospechoso, el proceso de descifrado y el playbook de malware. El resumen original comenzaba con la URL de la sala (https://tryhackme.com/room/irplaybooks) y conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Decidir cuándo usar un playbook, recorrer el ciclo de vida de la IR, aplicar el playbook de malware al caso WannaCry (servicio, proceso, clasificación y contención) y cerrar el incidente.
> **EN:** Decide when to use a playbook, walk the IR lifecycle, apply the malware playbook to the WannaCry case (service, process, classification and containment) and close the incident.

## Solucionario

### Task 1: Playbooks e IR / Playbooks and IR
**Explicación:** Se presenta el papel de los playbooks dentro de la respuesta a incidentes.

1. No answer needed

### Task 2: ¿Cuándo usar un playbook? / When to Use a Playbook?
**Explicación:** Se decide si el escenario requiere seguir un playbook.

1. y

### Task 3: Ciclo de vida de la IR / IR Lifecycle
**Explicación:** Se identifica la primera fase del ciclo de vida de la respuesta a incidentes: la preparación.

1. Preparation

### Task 4: Cierre del incidente / Closing the Incident
**Explicación:** Se identifica la fase final del incidente, que implica el cierre formal del caso.

1. Close incident

### Task 5: Recuperación / Recovery
**Explicación:** Se aborda la recuperación del sistema usando la última configuración buena conocida.

1. last known good configuration

### Task 6: Actividad posterior / Post-incident
**Explicación:** Se revisa la actividad posterior al incidente y las lecciones aprendidas.

1. Post-incident activity

### Task 7: Caso WannaCry / WannaCry Case Study
**Explicación:** Se aplica el playbook de malware al caso WannaCry: el servicio sospechoso, la confirmación, el proceso de cifrado, la familia de malware, el playbook aplicado, la clasificación y la fase de contención.

1. taskhsvc.exe
2. n
3. @WanaDecryptor@.exe
4. Wannacry
5. malware playbook
6. TP
7. Containment

### Task 8: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre el uso de playbooks en la respuesta a incidentes.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | ¿Usar playbook? / Use a playbook? | `y` |
| 3 | Primera fase del ciclo de vida / First lifecycle phase | `Preparation` |
| 4 | Fase de cierre / Closing phase | `Close incident` |
| 5 | Configuración buena conocida / Last known good configuration | `last known good configuration` |
| 6 | Actividad posterior al incidente / Post-incident activity | `Post-incident activity` |
| 7 | Servicio sospechoso / Suspicious service | `taskhsvc.exe` |
| 8 | Confirmación del proceso / Process confirmation | `n` |
| 9 | Proceso de cifrado / Encryption process | `@WanaDecryptor@.exe` |
| 10 | Familia de malware / Malware family | `Wannacry` |
| 11 | Playbook aplicado / Applied playbook | `malware playbook` |
| 12 | Clasificación del hallazgo / Finding classification | `TP` |
| 13 | Fase de contención / Containment phase | `Containment` |
| 14 | (Pregunta 14 no especificada en el original) | `No answer needed` |

---

**Metodología:** Revisar cuándo se emplean los playbooks, recorrer el ciclo de vida de la IR desde la preparación hasta el cierre, identificar el servicio y el proceso de cifrado del caso WannaCry, clasificar el hallazgo como verdadero positivo con el playbook de malware y aplicar la contención.

### Cadena de ataque / Attack Chain

```text
infección -> taskhsvc.exe -> @WanaDecryptor@.exe -> WannaCry -> clasificación TP -> playbook de malware -> Preparation -> Containment -> Post-incident activity -> Close incident
```

**Learning chain:** playbooks vs runbooks -> ciclo de vida IR -> detección (taskhsvc.exe) -> análisis (@WanaDecryptor@.exe) -> clasificación TP -> playbook de malware -> contención -> recuperación -> cierre.

**Lección:** *Un playbook convierte el caos de un incidente en pasos verificables: saber cuándo aplicarlo y ejecutar la secuencia (preparación, contención, recuperación, cierre) reduce el error humano y acelera la respuesta ante ransomware.*

**MITRE ATT&CK:** T1486 (Data Encrypted for Impact), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1133 (External Remote Services)

**Fuente:** [TryHackMe - IR Playbooks](https://tryhackme.com/room/irplaybooks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.