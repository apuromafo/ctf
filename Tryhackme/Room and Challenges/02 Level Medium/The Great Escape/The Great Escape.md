# The Great Escape [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `thegreatescape`
* **Link:** https://tryhackme.com/room/thegreatescape
* **Sección / Section:** Linux / CTF
* **Fuente / Source:** (thmrevenant)

---

## Solucionario de Tareas / Task Solutions

> **ES:** CTF de Linux centrado en escapar del entorno mediante una explotación inicial vía una aplicación web, seguida de una escalada de privilegios con técnicas de "container escape" o escape de restricciones, que culmina en la obtención de varias flags de root.
> **EN:** Linux CTF focused on escaping the environment through an initial exploitation via a web application, followed by a privilege escalation using container escape or restriction escape techniques, culminating in several root flags.

---

### Task 1 — Flag en la Webapp / Webapp Flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Find the flag hidden in the webapp | `THM{b801135794bf1ed3a2aafaa44c2e5ad4}` |

---

### Task 2 — Flags de Root / Root Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Find the root flag? | `THM{0cb4b947043cb5c0486a454b75a10876}` |
| Find the real root flag | `THM{c62517c0cad93ac93a92b1315a32d734}` |

---

## Metodología / Methodology

1. **Paso / Step:** Enumerar y analizar la aplicación web hasta localizar la flag oculta dentro de ella. / Enumerate and analyze the web application until locating the flag hidden inside it.
2. **Paso / Step:** Obtener una shell en el host a través de la vulnerabilidad de la webapp y escalar privilegios para leer la primera flag de root. / Obtain a shell on the host through the webapp vulnerability and escalate privileges to read the first root flag.
3. **Paso / Step:** Continuar el proceso de escape del entorno (container/restricciones) para alcanzar el nivel real de root y capturar la flag raíz definitiva. / Continue the environment escape process (container/restrictions) to reach the real root level and capture the definitive root flag.

### Cadena de ataque / Attack Chain

```
Webapp -> flag oculta = THM{b801135794bf1ed3a2aafaa44c2e5ad4}
  -> explotación -> shell en el host
  -> privesc -> root flag = THM{0cb4b947043cb5c0486a454b75a10876}
  -> escape del entorno -> real root flag = THM{c62517c0cad93ac93a92b1315a32d734}
```

**Lección:** Las flags "falsas" o intermedias pueden actuar como señuelos; hay que continuar la investigación más allá del primer root para escapar de las restricciones del entorno y encontrar la flag real.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.