# Runtime Detection Evasion

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Guía técnica | `runtimedetectionevasion` | https://tryhackme.com/room/runtimedetectionevasion | 03 Level Hard | TryHackMe | AMSI / PowerShell / Windows Defender / reflection / patching / downgrade | Guía de evasión de detección en tiempo de ejecución: firmas AMSI, reflexión, patching y tres flags que validan las técnicas aplicadas. |

---

**Contexto:** Sala técnica de evasión en tiempo de ejecución. Practica la detección de AMSI en Windows (firma `AMSI_RESULT_DETECTED`), la técnica de downgrade de PowerShell (`N`), y luego la evasión mediante reflexión y patching en memoria, con tres flags que cierran cada fase. Las tareas 8 y 9 son tareas tipo encuesta sin respuesta.

> **ES:** "Aprende a evadir la detección en tiempo de ejecución: AMSI, downgrade de PowerShell, reflexión y patching."
> **EN:** "Learn to evade runtime detection: AMSI, PowerShell downgrade, reflection and patching."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea introductoria de la sala; no requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria sin respuesta. | `No answer needed` |

### Task 2: AMSI / AMSI

**Explicación:** Tarea sobre la detección de AMSI: la primera parte práctica no requiere respuesta y la segunda identifica la firma que detecta la herramienta (AMSI). Contenido original de la tarea:

```text
2. 1. No answer needed
   2. AMSI
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Firma detectada por AMSI (nombre de la firma/componente). | `AMSI` |

### Task 3: Firma de detección / Detection signature

**Explicación:** Tarea que identifica el mensaje/resultado que devuelve AMSI al detectar el payload: `AMSI_RESULT_DETECTED`. Contenido original de la tarea:

```text
3. 1. No answer needed
   2. AMSI_RESULT_DETECTED
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Resultado devuelto por AMSI al detectar el payload. | `AMSI_RESULT_DETECTED` |

### Task 4: Downgrade de PowerShell / PowerShell downgrade

**Explicación:** Tarea sobre la técnica de downgrade de PowerShell: la opción elegida es `N` (no al downgrade). Contenido original de la tarea:

```text
4. 1. No answer needed
   2. N
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Opción elegida (downgrade). | `N` |

### Task 5: Downgrade exitoso / Successful downgrade

**Explicación:** Flag obtenida tras completar la técnica de downgrade de PowerShell. Contenido original de la tarea:

```text
5. 1. No answer needed
   2. THM{p0w3r5h3ll_d0wn6r4d3!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Flag tras el downgrade de PowerShell. | `THM{p0w3r5h3ll_d0wn6r4d3!}` |

### Task 6: Evasión por reflexión / Reflection evasion

**Explicación:** Flag obtenida al aplicar la evasión por reflexión en memoria. Contenido original de la tarea:

```text
6. 1. No answer needed
   2. THM{r3fl3c7_4ll_7h3_7h1n65}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Flag tras la evasión por reflexión. | `THM{r3fl3c7_4ll_7h3_7h1n65}` |

### Task 7: Patching de la firma / Signature patching

**Explicación:** Flag obtenida tras el patching del valor AMSI que hace inofensiva la comprobación en memoria. Contenido original de la tarea:

```text
7. 1. No answer needed
   2. THM{p47ch1n6_15n7_ju57_f0r_7h3_600d_6uy5}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico previo de la tarea. | `No answer needed` |
| 2 | Flag tras el patching del valor AMSI. | `THM{p47ch1n6_15n7_ju57_f0r_7h3_600d_6uy5}` |

### Task 8: Práctica adicional / Further practice

**Explicación:** Tarea de práctica adicional; no requiere respuesta. Contenido original de la tarea:

```text
8. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de práctica adicional sin respuesta. | `No answer needed` |

### Task 9: Conclusión / Conclusion

**Explicación:** Tarea de cierre de la sala; no requiere respuesta. Contenido original de la tarea:

```text
9. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de cierre sin respuesta. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria sin respuesta. | `No answer needed` |
| 2 | Paso práctico previo de la tarea. | `No answer needed` |
| 3 | Firma detectada por AMSI (nombre de la firma/componente). | `AMSI` |
| 4 | Paso práctico previo de la tarea. | `No answer needed` |
| 5 | Resultado devuelto por AMSI al detectar el payload. | `AMSI_RESULT_DETECTED` |
| 6 | Paso práctico previo de la tarea. | `No answer needed` |
| 7 | Opción elegida (downgrade). | `N` |
| 8 | Paso práctico previo de la tarea. | `No answer needed` |
| 9 | Flag tras el downgrade de PowerShell. | `THM{p0w3r5h3ll_d0wn6r4d3!}` |
| 10 | Paso práctico previo de la tarea. | `No answer needed` |
| 11 | Flag tras la evasión por reflexión. | `THM{r3fl3c7_4ll_7h3_7h1n65}` |
| 12 | Paso práctico previo de la tarea. | `No answer needed` |
| 13 | Flag tras el patching del valor AMSI. | `THM{p47ch1n6_15n7_ju57_f0r_7h3_600d_6uy5}` |
| 14 | Tarea de práctica adicional sin respuesta. | `No answer needed` |
| 15 | Tarea de cierre sin respuesta. | `No answer needed` |

---

**Metodología:**
1. Detectar qué firma de AMSI bloquea el payload (`AMSI_RESULT_DETECTED`).
2. Probar el downgrade de PowerShell y registrar la opción elegida (`N`).
3. Validar el downgrade y capturar su flag.
4. Aplicar la evasión por reflexión y capturar su flag.
5. Aplicar el patching del valor AMSI en memoria y capturar la flag final.

### Cadena de ataque / Attack Chain

```text
AMSI detecta payload (AMSI_RESULT_DETECTED) -> downgrade PowerShell (N) -> THM{p0w3r5h3ll_d0wn6r4d3!} -> reflexión -> THM{r3fl3c7_4ll_7h3_7h1n65} -> patching AMSI -> THM{p47ch1n6_15n7_ju57_f0r_7h3_600d_6uy5}
```

**Learning chain:** `AMSI -> detección -> downgrade -> reflexión -> patching -> evasión total`

**Lección:** *La evasión de detección en tiempo de ejecución combina conocimiento de firmas (AMSI), técnicas de downgrade y parcheo en memoria; validar cada fase entraña una flag distinta.*

**MITRE ATT&CK:** T1059.001 (PowerShell), T1068 (Exploitation for Privilege Escalation), T1548 (Abuse Elevation Control Mechanism), T1562.001 (Impair Defenses: Disable or Modify Tools)

**Fuente:** [TryHackMe - Runtime Detection Evasion](https://tryhackme.com/room/runtimedetectionevasion)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.