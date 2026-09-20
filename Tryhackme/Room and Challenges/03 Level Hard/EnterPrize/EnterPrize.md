# EnterPrize

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `enterprize` | https://tryhackme.com/room/enterprize | 03 Level Hard | TryHackMe | CTF / enumeración / explotación web / escalada / flags | Reto CTF de nivel Hard en dos fases: dos flags que validan el compromiso inicial y la escalada/fase final del objetivo. |

---

**Contexto:** Sala CTF de nivel Hard. El reto se compone de dos tareas con una flag cada una: la primera bandera se obtiene en la fase inicial del compromiso (acceso al objetivo tras la enumeración y explotación) y la segunda al completar la escalada o último paso del reto. Ambas flags responden al formato estándar THM.

> **ES:** "CTF Hard: obtén la primera flag en el acceso inicial y la segunda al completar la escalada final del reto."
> **EN:** "Hard CTF: get the first flag during initial access and the second one after completing the final escalation of the challenge."

## Solucionario

### Task 1: Flag inicial / Initial flag

**Explicación:** Primera flag del reto, obtenida durante el acceso inicial al objetivo. Contenido original de la tarea:

```text
1. THM{a99acf52687be464db48eca3b3359572}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del acceso inicial. | `THM{a99acf52687be464db48eca3b3359572}` |

### Task 2: Flag final / Final flag

**Explicación:** Segunda flag del reto, obtenida al completar la escalada o la fase final. Contenido original de la tarea:

```text
2. THM{568a171c9460d2b3871618b9d5232919}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la fase final del reto. | `THM{568a171c9460d2b3871618b9d5232919}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del acceso inicial. | `THM{a99acf52687be464db48eca3b3359572}` |
| 2 | Flag de la fase final del reto. | `THM{568a171c9460d2b3871618b9d5232919}` |

---

**Metodología:**
1. Enumerar el objetivo (puertos, servicios y aplicación web).
2. Explotar el vector identificado para obtener el acceso inicial y la primera flag.
3. Escalar privilegios o completar la fase final del reto y recoger la segunda flag.

### Cadena de ataque / Attack Chain

```text
Recon -> enumeración -> explotación -> THM{a99acf52687be464db48eca3b3359572} -> escalada -> THM{568a171c9460d2b3871618b9d5232919}
```

**Learning chain:** `Recon -> web exploitation -> initial flag -> privesc -> final flag`

**Lección:** *Un CTF breve pero completo: cada flag marca un hito (acceso inicial y escalada); la persistencia en la enumeración define el éxito del reto.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1595 (Active Scanning), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - EnterPrize](https://tryhackme.com/room/enterprize)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.