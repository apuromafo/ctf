# Annie [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `annie`
* **Link:** https://tryhackme.com/room/annie
* **Sección / Section:** Linux / CTF
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de CTF Linux de nivel medio que implicaEnumeración, acceso inicial y escalada de privilegios para encontrar las flags user.txt y root.txt.
> **EN:** Medium-level Linux CTF room involving enumeration, initial access, and privilege escalation to find the user.txt and root.txt flags.

---

### Task 1 — Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is user.txt? | `THM{N0t_Ju5t_ANY_D3sk}` |
| What is root.txt? | `THM{0nly_th3m_5.5.2_D3sk}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Realizar enumeración inicial del sistema (puertos, servicios, archivos).
2. **Paso 2 / Step 2:** Obtener acceso inicial al sistema mediante vulnerabilidades identificadas.
3. **Paso 3 / Step 3:** Escalar privilegios hasta root para acceder a la flag root.txt.

### Cadena de ataque / Attack Chain

```
Enumeración → Acceso Inicial → Escalada de Privilegios → Obtención de Flags
```

**Lección:** La enumeración exhaustiva de servicios y archivos es clave para encontrar vectores de ataque en sistemas Linux.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
