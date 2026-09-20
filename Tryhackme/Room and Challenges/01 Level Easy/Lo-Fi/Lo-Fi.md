# Lo-Fi

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | lofi | [TryHackMe](https://tryhackme.com/room/lofi) | 01 Level Easy | THM | web challenge, análisis de la aplicación, flag oculta | Challenge web: inspección de la aplicación para obtener la flag oculta |

---

**Contexto:** Challenge web de tipo CTF en el que se debe auditar una pequeña aplicación para descubrir la flag oculta `flag{e4478e0eab69bd642b8238765dcb7d18}`, practicando la inspección del código y los recursos de la página.

> **EN:**
> 1. flag{e4478e0eab69bd642b8238765dcb7d18}

## Solucionario

### Task 1: El challenge / The challenge

**Explicación:** Se analiza la aplicación web (código fuente, peticiones y recursos) hasta localizar la flag incrustada en uno de sus elementos.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuál es la flag del challenge? / What is the flag of the challenge? | `flag{e4478e0eab69bd642b8238765dcb7d18}` |

---

**Metodología:** Inspeccionar la aplicación web: revisar el código fuente de la página (HTML/JS/CSS), observar las peticiones de red en las herramientas de desarrollador y probar parámetros interesantes si la aplicación lo permite. La flag aparece directamente al examinar los recursos de la aplicación.

### Cadena de ataque / Attack Chain

Reconocimiento de la web → inspección del código fuente → revisión de recursos y peticiones → localización de la flag

**Learning chain:** web challenge → view-source → peticiones → flag{e4478e0eab69bd642b8238765dcb7d18}

**Lección:** *Muchos challenges web esconden la flag en el propio código fuente, comentarios o recursos de la aplicación; la inspección directa del navegador y de las peticiones suele ser más rápida que lanzar herramientas pesadas.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1505.003 (Web Shell)

**Fuente:** [TryHackMe - Lo-Fi](https://tryhackme.com/room/lofi)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.