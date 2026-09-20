# Rabbit Hole

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `rabbitholeqq` | https://tryhackme.com/room/rabbitholeqq | 03 Level Hard | TryHackMe | web / enumeración / rabbit hole / flags | Reto de una sola flag: recorrer el "agujero de conejo" de la sala y entregar la bandera final que se esconde al final del camino. |

---

**Contexto:** Sala con una única flag a la que se llega siguiendo el camino completo del reto. La dificultad está en recorrer la vía marcada por la aplicación (el "rabbit hole") sin desviarse y en entregar la bandera exacta que confirma haber llegado al final del laberinto.

> **ES:** "Recorre el agujero de conejo de la sala y entrega la flag final que se esconde al final del camino."
> **EN:** "Go down the room's rabbit hole and submit the final flag hidden at the end of the path."

## Solucionario

### Task 1: Flag del reto / Room flag

**Explicación:** Única flag del reto, entregada al completar el recorrido del laberinto. Contenido original de la tarea:

```text
1. THM{this_is_the_way_step_inside_jNu8uJ9tvKfH1n48}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del reto. | `THM{this_is_the_way_step_inside_jNu8uJ9tvKfH1n48}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del reto. | `THM{this_is_the_way_step_inside_jNu8uJ9tvKfH1n48}` |

---

**Metodología:**
1. Explorar el objetivo y reconocer la superficie expuesta de la aplicación web.
2. Identificar el vector de entrada (parámetro, búsqueda o endpoint) del reto.
3. Explotar el "rabbit hole" hasta recuperar la flag final.

### Cadena de ataque / Attack Chain

```text
Recon -> aplicación web -> vector explotable -> rabbit hole -> THM{this_is_the_way_step_inside_jNu8uJ9tvKfH1n48}
```

**Learning chain:** `Recon -> web -> rabbit hole -> THM{this_is_the_way_step_inside_jNu8uJ9tvKfH1n48}`

**Lección:** *Los retos de una sola flag premian la paciencia: el "agujero de conejo" obliga a seguir cada pista hasta el final; la copia exacta de la bandera cierra el reto.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Rabbit Hole](https://tryhackme.com/room/rabbitholeqq)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.