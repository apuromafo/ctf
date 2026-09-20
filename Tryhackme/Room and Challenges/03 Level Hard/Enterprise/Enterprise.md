# Enterprise

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `enterprise` | https://tryhackme.com/room/enterprise | 03 Level Hard | TryHackMe | CTF corporativo / enumeración / red empresarial / AD / flags | Reto CTF de nivel Hard con sabor corporativo: cinco pasos prácticos sin respuesta (tareas guiadas) y dos flags que cierran el compromiso del entorno empresarial. |

---

**Contexto:** Sala CTF de temática empresarial. La primera tarea contiene cinco pasos prácticos del recorrido (todos sin respuesta, marcados como "No answer needed"), que corresponden a los pasos guiados de reconocimiento y explotación; la segunda tarea recoge las dos flags del entorno una vez completada la cadena. El objetivo del reto es dominar el dominio corporativo y validarlo con las banderas finales.

> **ES:** "CTF corporativo: completa los pasos prácticos del entorno empresarial y entrega las dos flags finales del compromiso."
> **EN:** "Corporate CTF: complete the practical steps of the enterprise environment and submit the two final flags of the compromise."

## Solucionario

### Task 1: Pasos guiados del compromiso / Guided compromise steps

**Explicación:** Cinco pasos prácticos del recorrido hacia el compromiso corporativo; ninguno requiere respuesta. Contenido original de la tarea:

```text
1. 1. No answer needed
   2. No answer needed
   3. No answer needed
   4. No answer needed
   5. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico 1 del compromiso. | `No answer needed` |
| 2 | Paso práctico 2 del compromiso. | `No answer needed` |
| 3 | Paso práctico 3 del compromiso. | `No answer needed` |
| 4 | Paso práctico 4 del compromiso. | `No answer needed` |
| 5 | Paso práctico 5 del compromiso. | `No answer needed` |

### Task 2: Flags del entorno / Environment flags

**Explicación:** Las dos flags finales obtenidas al completar el compromiso del entorno empresarial. Contenido original de la tarea:

```text
2. 1. THM{ed882d02b34246536ef7da79062bef36}
   2. THM{1a1fa94875421296331f145971ca4881}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del entorno. | `THM{ed882d02b34246536ef7da79062bef36}` |
| 2 | Flag 2 del entorno. | `THM{1a1fa94875421296331f145971ca4881}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico 1 del compromiso. | `No answer needed` |
| 2 | Paso práctico 2 del compromiso. | `No answer needed` |
| 3 | Paso práctico 3 del compromiso. | `No answer needed` |
| 4 | Paso práctico 4 del compromiso. | `No answer needed` |
| 5 | Paso práctico 5 del compromiso. | `No answer needed` |
| 6 | Flag 1 del entorno. | `THM{ed882d02b34246536ef7da79062bef36}` |
| 7 | Flag 2 del entorno. | `THM{1a1fa94875421296331f145971ca4881}` |

---

**Metodología:**
1. Reconocer el entorno corporativo (dominio, hosts expuestos y servicios).
2. Completar los pasos prácticos guiados de enumeración y explotación.
3. Avanzar por la cadena del compromiso hasta el dominio empresarial.
4. Recoger las dos flags finales del entorno.

### Cadena de ataque / Attack Chain

```text
Recon corporativo -> pasos guiados (enumeración -> explotación) -> dominio -> THM{ed882d02b34246536ef7da79062bef36} -> THM{1a1fa94875421296331f145971ca4881}
```

**Learning chain:** `Enumeración -> explotación -> dominio corporativo -> compromiso total -> flags`

**Lección:** *Los CTF corporativos combinan pasos guiados con banderas que validan cada fase; la disciplina en la enumeración y la documentación de cada paso llevan a dominar el entorno.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation), T1021.002 (Remote Services: SMB/Windows Admin Shares)

**Fuente:** [TryHackMe - Enterprise](https://tryhackme.com/room/enterprise)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.