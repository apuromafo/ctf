# The Game

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `thegame` | [TryHackMe](https://tryhackme.com/room/thegame) | 01 Level Easy | THM | Análisis de juego, lectura de información | Obtención de la flag oculta |

---

**Contexto:**

> **ES:** Sala de nivel fácil en la que el jugador debe "leerlo todo" dentro del juego, encontrando información oculta y la bandera del laboratorio.
> **EN:** Easy room in which the player must "read it all" inside the game, finding hidden information and the lab flag.

## Solucionario

### Task 1: Lectura de la información / Reading it all

**Explicación:**

La lista de respuestas del room original contiene un único valor que corresponde a la flag del laboratorio. Se conserva de forma literal:

1. THM{I_CAN_READ_IT_ALL}

### Tabla Unificada de Preguntas y Respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del flag? | `THM{I_CAN_READ_IT_ALL}` |

---

**Metodología:** Exploración del juego → localización de la información oculta → extracción del flag.

### Cadena de ataque / Attack Chain

- Interacción con el juego/escenario
- Búsqueda sistemática del contenido visible u oculto
- Lectura y captura del flag

**Learning chain:** Exploración → Observación → Extracción de información → Captura de flag

**Lección:** *A veces la "vulnerabilidad" más importante es prestar atención: la información sensible puede estar a la vista y solo requiere esforzarse por leerla.*

**MITRE ATT&CK:** N/A (Challenge/CTF)

**Fuente:** [TryHackMe - The Game](https://tryhackme.com/room/thegame)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.