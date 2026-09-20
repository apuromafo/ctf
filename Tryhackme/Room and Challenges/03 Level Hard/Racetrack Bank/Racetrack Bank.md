# Racetrack Bank

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `racetrackbank` | https://tryhackme.com/room/racetrackbank | 03 Level Hard | TryHackMe | web / race condition / lógica bancaria / flags | Reto CTF de lógica bancaria: dos flags que se entregan al resolver las condiciones de carrera y el análisis de la aplicación del banco. |

---

**Contexto:** Sala tipo reto cuya temática gira en torno a un banco y la explotación de su lógica (condiciones de carrera / races). Se entregan dos flags como resultado de los dos pasos clave del reto. Toda la información original recogida es únicamente el par de banderas.

> **ES:** "Explota la lógica del banco y entrega las dos flags que cierran el reto."
> **EN:** "Exploit the bank's logic and submit the two flags that complete the challenge."

## Solucionario

### Task 1: Flags del reto / Challenge flags

**Explicación:** Las dos flags del reto, asociadas a la resolución de la explotación lógica del banco. Contenido original de la tarea:

```text
1. 1. THM{178c31090a7e0f69560730ad21d90e70}
   2. THM{55a9d6099933f6c456ccb2711b8766e3}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{178c31090a7e0f69560730ad21d90e70}` |
| 2 | Flag 2 del reto. | `THM{55a9d6099933f6c456ccb2711b8766e3}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{178c31090a7e0f69560730ad21d90e70}` |
| 2 | Flag 2 del reto. | `THM{55a9d6099933f6c456ccb2711b8766e3}` |

---

**Metodología:**
1. Enumerar la aplicación web del banco y entender su lógica de negocio.
2. Identificar las operaciones sujetas a condiciones de carrera (race conditions).
3. Explotarlas para obtener la primera flag.
4. Completar la cadena lógica restante y entregar la segunda flag.

### Cadena de ataque / Attack Chain

```text
Recon web -> lógica bancaria -> race condition -> explotación -> THM{178c31090a7e0f69560730ad21d90e70} -> THM{55a9d6099933f6c456ccb2711b8766e3}
```

**Learning chain:** `Recon -> análisis de lógica -> race condition -> flags de explotación`

**Lección:** *La lógica de negocio es tan crítica como los bugs clásicos: las condiciones de carrera permiten operaciones no previstas y su explotación se valida con flags.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Racetrack Bank](https://tryhackme.com/room/racetrackbank)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.