# Second

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | fearsecond | https://tryhackme.com/room/fearsecond | 03 Level Hard | TryHackMe | Inyección SQL de segundo orden, WAF, control de acceso | Alto |

---

**Contexto:**
> **ES:** Sala CTF centrada en evadir un WAF mediante inyección SQL de segundo orden y abusar del control de accesos del entorno para completar el reto.
> **EN:** CTF room focused on bypassing a WAF through second-order SQL injection and abusing the environment's access control to complete the challenge.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. 1. THM{WaF_wAf_2nd_0rd3r_SQl_1nJ3ct1on}
   2. THM{M1nd_Y0uR_AcC3s$_C0nTr0l}
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{WaF_wAf_2nd_0rd3r_SQl_1nJ3ct1on}` |
| 1.2 | `THM{M1nd_Y0uR_AcC3s$_C0nTr0l}` |

---

**Metodología:**
1. Enumeración del entorno y localización del punto de entrada sobre el que actúa el WAF.
2. Análisis del filtro y construcción de la inyección SQL de segundo orden que lo evada.
3. Obtención de la primera flag: `THM{WaF_wAf_2nd_0rd3r_SQl_1nJ3ct1on}`.
4. Explotación del control de accesos para obtener la segunda flag: `THM{M1nd_Y0uR_AcC3s$_C0nTr0l}`.

### Cadena de ataque / Attack Chain
```text
Enumeración -> Detección del WAF -> Inyección SQL de segundo orden -> Flag 1 -> Control de accesos -> Flag 2
```

**Learning chain:**
Enumeración -> WAF -> SQLi de segundo orden -> Flag 1 -> Control de accesos -> Flag 2.

**Lección:** *Un WAF no es suficiente si las consultas se siguen interpretando en un segundo plano: el control de accesos debe validarse siempre y no solo en la capa de entrada.*

**MITRE ATT&CK:**
- T1190 Exploit Public-Facing Application
- T1059 Command and Scripting Interpreter
- T1078 Valid Accounts

**Fuente:** [TryHackMe - Second](https://tryhackme.com/room/fearsecond)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.