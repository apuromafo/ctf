# Git and Crumpets [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `gitandcrumpets`
* **Link:** https://tryhackme.com/room/gitandcrumpets
* **Sección / Section:** Web / CTF
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala CTF está centrada en el abuso de repositorios Git expuestos como vector de ataque. El objetivo es explotar información sensible filtrada por un repositorio para obtener acceso de usuario y luego escalar a root.
> **EN:** This CTF room focuses on abusing exposed Git repositories as an attack vector. The objective is to exploit sensitive information leaked by a repository to obtain user access and then escalate to root.

---

### Task 1 — Flags de Usuario y Root / User & Root Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| User Flag | `thm{fd7ab9ffd409064f257cd70cf3d6aa16}` |
| Root Flag | `thm{6320228dd9e315f283b75887240dc6a1}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Se identifica un repositorio Git expuesto en la aplicación web y se extrae información sensible (código, historial, credenciales) para obtener acceso inicial como usuario.
2. **Paso 2 / Step 2:** Se utiliza la información filtrada para escalar privilegios y lograr acceso como root, obteniendo la flag final.

### Cadena de ataque / Attack Chain

```
Enumeración web → Detección de repositorio Git expuesto → Extracción de código e historial → Recuperación de credenciales → Acceso inicial (user flag) → Escalada de privilegios → Root flag
```

**Lección:** Los repositorios Git expuestos en servidores web pueden filtrar historial, código fuente y credenciales. Es crucial proteger el directorio .git y asegurarse de que los metadatos de desarrollo no queden accesibles públicamente.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
