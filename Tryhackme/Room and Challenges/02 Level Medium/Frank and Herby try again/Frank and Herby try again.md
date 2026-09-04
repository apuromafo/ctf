# Frank and Herby try again [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `frankandherbytryagain`
* **Link:** https://tryhackme.com/room/frankandherbytryagain
* **Sección / Section:** Web / CTF
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Frank y Herby vuelven a intentarlo en esta sala CTF de nivel medio. El objetivo es comprometer el sistema, obtener acceso como usuario y escalar privilegios hasta conseguir la flag de root.
> **EN:** Frank and Herby try again in this medium-level CTF room. The objective is to compromise the system, gain user access and escalate privileges to obtain the root flag.

---

### Task 1 — Flags de Usuario y Root / User & Root Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| User flag? | `THM{I-2h0uld-f1r3-fr4nK}` |
| Root Flag? | `THM{frank-and-herby-still-suck}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Se enumera el sistema y se identifican vulnerabilidades web para obtener acceso inicial y conseguir la flag de usuario.
2. **Paso 2 / Step 2:** Se realiza escalada de privilegios en el sistema para lograr acceso como root y obtener la flag final.

### Cadena de ataque / Attack Chain

```
Reconocimiento y enumeración → Explotación web para acceso inicial → Obtención de user flag → Escalada de privilegios → Obtención de root flag
```

**Lección:** En las salas CTF de tipo web es fundamental combinar la explotación de la aplicación accesible con una correcta enumeración del sistema para lograr escalar privilegios y completar la máquina.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
