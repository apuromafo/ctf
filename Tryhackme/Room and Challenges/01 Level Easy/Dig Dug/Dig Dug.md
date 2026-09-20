# Dig Dug

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `digdug` | https://tryhackme.com/room/digdug | 01 Level Easy | TryHackMe | Challenge / flag hunting / búsqueda de pistas | Reto corto centrado en localizar la flag mediante búsqueda de pistas ocultas. |

---

**Contexto:** Reto corto tipo challenge de TryHackMe. El objetivo es resolver el desafío siguiendo las pistas proporcionadas hasta localizar la flag. El room está pensado para practicar la búsqueda sistemática de información en el entorno desplegado.

> **ES:** Reto challenge: sigue las pistas del lab hasta localizar la flag escondida.
> **EN:** Challenge room: follow the lab clues until you locate the hidden flag.

## Solucionario

### Task 1: Encuentra la flag / Find the flag

**Explicación:** Se resuelve el reto siguiendo las pistas del laboratorio y al localizar la flag se obtiene `flag{0767ccd06e79853318f25aeb08ff83e2}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto? / What is the flag of the challenge? | `flag{0767ccd06e79853318f25aeb08ff83e2}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto? | `flag{0767ccd06e79853318f25aeb08ff83e2}` |

---

**Metodología:** El reto consiste en examinar exhaustivamente la información disponible del laboratorio hasta dar con la flag oculta: `flag{0767ccd06e79853318f25aeb08ff83e2}`.

### Cadena de ataque / Attack Chain

```text
Exploración del entorno -> búsqueda de pistas -> localizar la flag oculta -> flag{0767ccd06e79853318f25aeb08ff83e2}
```

**Learning chain:** Reconocimiento del challenge → búsqueda de indicios → extracción de la flag.

**Lección:** *Este reto refuerza la exploración metódica: los challenges cortos suelen esconder la flag detrás de una pista aparentemente inocua que solo aparece si se revisa todo el entorno con atención.*

**MITRE ATT&CK:** No aplica directamente (reto de obtención de flag).

**Fuente:** [TryHackMe - Dig Dug](https://tryhackme.com/room/digdug)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.