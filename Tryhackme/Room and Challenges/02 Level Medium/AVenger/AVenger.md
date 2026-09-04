# AVenger [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Premium)
* **Slug:** `avenger`
* **Link:** https://tryhackme.com/room/avenger
* **Sección / Section:** Windows / CTF
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de CTF Linux de nivel medio en la que hay que comprometer un sistema para obtener las flags de usuario y root.
> **EN:** Medium-level Linux CTF room where you must compromise the system to obtain user and root flags.

---

### Task 1 — Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which is the user flag? | `THM{WITH_GREAT_POWER_COMES_GREAT_RESPONSIBILITY}` |
| Which is the root flag? | `THM{I_CAN_DO_THIS_ALL_DAY}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Enumerar el objetivo para descubrir servicios y vulnerabilidades explotables.
2. **Paso 2 / Step 2:** Obtener acceso inicial como usuario y capturar la flag de usuario.
3. **Paso 3 / Step 3:** Escalar privilegios hasta root para obtener la flag root.txt.

### Cadena de ataque / Attack Chain

```
Enumeración → Acceso Inicial → User Flag → Escalada de Privilegios → Root
```

**Lección:** La identificación correcta de vectores de escalada de privilegios permite completar la cadena de compromiso hasta root.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.