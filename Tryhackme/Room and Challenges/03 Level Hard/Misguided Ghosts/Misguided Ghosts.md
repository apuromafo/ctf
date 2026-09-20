# Misguided Ghosts

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | misguidedghosts | https://tryhackme.com/room/misguidedghosts | 03 Level Hard | TryHackMe | Docker escape, pivoting | Alto |

---

**Contexto:**
> **ES:** Reto de nivel Hard centrado en el escape de contenedores Docker y el pivotado dentro del entorno comprometido. Las banderas del room reflejan directamente las técnicas empleadas: escape de contenedor (`{d0ck3r_35c4p3}`) y pivoting (`{p1v0t1ng_15_fun}`).
> **EN:** Hard-level challenge focused on Docker container escape and pivoting inside the compromised environment. The room's flags directly reflect the techniques used: container escape (`{d0ck3r_35c4p3}`) and pivoting (`{p1v0t1ng_15_fun}`).

## Solucionario

### Task 1: Tarea 1
**Explicación:**
1. 1. {d0ck3r_35c4p3}
   2. {p1v0t1ng_15_fun}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `{d0ck3r_35c4p3}` |
| 1.2 | `{p1v0t1ng_15_fun}` |

---

**Metodología:**
1. Compromiso inicial del entorno y reconocimiento dentro del contenedor Docker.
2. Escape del contenedor para obtener la primera bandera (`{d0ck3r_35c4p3}`).
3. Pivotado hacia otras máquinas o segmentos de la red para obtener la segunda bandera (`{p1v0t1ng_15_fun}`).

### Cadena de ataque / Attack Chain
1. Acceso inicial y reconocimiento en el contenedor.
2. Docker escape.
3. Pivoting a la red interna.
4. Obtención de las banderas.

**Learning chain:** Acceso inicial -> Docker escape -> Pivoting -> Banderas.

**Lección:** *El escape de contenedores y el pivoting multiplican el alcance: salir del contenedor abre toda la red interna.*

**MITRE ATT&CK:**
- T1610 (Deploy Container)
- T1021 (Remote Services)
- T1078 (Valid Accounts)
- T1082 (System Information Discovery)

**Fuente:** [TryHackMe - Misguided Ghosts](https://tryhackme.com/room/misguidedghosts)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.