# Aratus [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `aratus`
* **Link:** https://tryhackme.com/room/aratus
* **Sección / Section:** Linux / CTF
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de CTF Linux de nivel medio donde se debe comprometer un sistema para obtener las flags user.txt y root.txt.
> **EN:** Medium-level Linux CTF room where you must compromise the system to obtain the user.txt and root.txt flags.

---

### Task 1 — Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user.txt flag? | `THM{ba8d3b87bfdb9d10115cbe24feabbc20}` |
| What is the root.txt flag? | `THM{d8afc85983603342f6c6979b20e06cf6}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Realizar enumeración del sistema objetivo para identificar servicios y vulnerabilidades.
2. **Paso 2 / Step 2:** Obtener acceso inicial al sistema mediante explotación de vulnerabilidades encontradas.
3. **Paso 3 / Step 3:** Escalar privilegios hasta root para obtener la flag root.txt.

### Cadena de ataque / Attack Chain

```
Enumeración → Explotación → Acceso Inicial → Escalada de Privilegios → Obtención de Flags
```

**Lección:** La combinación de enumeración cuidadosa y explotación de vulnerabilidades permite comprometer sistemas Linux de nivel medio.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
