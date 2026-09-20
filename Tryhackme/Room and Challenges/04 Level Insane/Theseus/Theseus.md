# Theseus

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `theseus` | [TryHackMe](https://tryhackme.com/room/theseus) | 04 Level Insane | TryHackMe | ctf / cadena de flags | Resolución del reto Theseus: cuatro flags encadenadas que se obtienen de forma progresiva. |

---

**Contexto:** Sala CTF de nivel Insane que homenajea al mito de Teseo. El recorrido entrega cuatro flags de forma progresiva, donde cada fase habilita el acceso a la siguiente hasta completar el laberinto.

> **ES:** Sala CTF de nivel Insane que homenajea al mito de Teseo. El recorrido entrega cuatro flags de forma progresiva, donde cada fase habilita el acceso a la siguiente hasta completar el laberinto.

> **EN:** Insane-difficulty CTF room paying homage to the myth of Theseus. The run delivers four flags progressively, where each phase unlocks access to the next until the labyrinth is completed.

## Solucionario

### Task 1: Respuestas del laboratorio / Lab answers

**Explicación:**
Lista completa de respuestas de la sala tal como se recoge en la nota original, sin modificar:

1. 1. THM{499a89a2a064426921732e7d31bc08a}
   2. THM{6154ea526254375613650183962bf431}
   3. THM{c307b8045208fac06b9faa90e68d2ad4}
   4. THM{bb2af471e0aea04e982c2e5d0a6fa404}

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | 1.1 | `THM{499a89a2a064426921732e7d31bc08a}` |
| 2 | 1.2 | `THM{6154ea526254375613650183962bf431}` |
| 3 | 1.3 | `THM{c307b8045208fac06b9faa90e68d2ad4}` |
| 4 | 1.4 | `THM{bb2af471e0aea04e982c2e5d0a6fa404}` |

---

**Metodología:**
1. **Progresión por fases:** superar cada sección del laberinto y recoger su flag exacta.
2. **Encadenado:** usar el avance de cada fase para desbloquear la siguiente.
3. **Cierre:** confirmar las cuatro flags para dar por resuelta la sala.

### Cadena de ataque / Attack Chain

1. Fase 1 → `THM{499a89a2a064426921732e7d31bc08a}`.
2. Fase 2 → `THM{6154ea526254375613650183962bf431}`.
3. Fase 3 → `THM{c307b8045208fac06b9faa90e68d2ad4}`.
4. Fase 4 → `THM{bb2af471e0aea04e982c2e5d0a6fa404}`.

**Learning chain:** flag 1 → flag 2 → flag 3 → flag 4 (salida del laberinto).

**Lección:** *Los CTF por fases castigan avanzar sin registrar: anotar cada flag en el momento en que aparece evita retroceder por un laberinto ya recorrido cuando una fase posterior falla.*

**MITRE ATT&CK:** N/A (CTF interactivo sin infraestructura ofensiva documentada)

**Fuente:** [TryHackMe - Theseus](https://tryhackme.com/room/theseus)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.