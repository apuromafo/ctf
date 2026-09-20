# DockMagic

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `dockmagic` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dockmagic) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Docker / Contenedores / Linux / container escape / flags |
| **Impacto** | Resolución de un reto CTF de contenedores Docker con obtención de tres flags |

---

**Contexto:** DockMagic es una sala CTF en la que se explota un entorno basado en contenedores Docker. El usuario inicial cuenta con permisos o acceso al CLI de docker que permiten interactuar con las imágenes y volúmenes del sistema. Las tres fases del reto conducen a tres flags distintas que validan la resolución del entorno.

## Solucionario

### Task 1: Flags del reto

**Explicación:** El reto se resuelve obteniendo tres flags: la primera **THM{c674a7e5c42cc4cae67ee0a03e26743c}**, la segunda **THM{2c8203d84b1269a605a362bf4200c691}** y la tercera **THM{dc887d7a23fa028d7892bc85389bc381}**. Cada flag se asocia a una fase del entorno Docker (interacción con el daemon, montajes o escape del contenedor).

1. THM{c674a7e5c42cc4cae67ee0a03e26743c}
2. THM{2c8203d84b1269a605a362bf4200c691}
3. THM{dc887d7a23fa028d7892bc85389bc381}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto? | `THM{c674a7e5c42cc4cae67ee0a03e26743c}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{2c8203d84b1269a605a362bf4200c691}` |
| 3 | ¿Cuál es la tercera flag del reto? | `THM{dc887d7a23fa028d7892bc85389bc381}` |

---

**Metodología:**

1. Enumerar el entorno: usuario/grupos del shell, binarios de docker disponibles y contenedores activos.
2. Comprobar si el usuario puede interactuar con el daemon de Docker o lanzar contenedores.
3. Explorar imágenes y volúmenes montados buscando las flags.
4. En caso de estar dentro de un contenedor, pivotar aprovechando montajes o permisos para obtener las flags restantes.

**Learning chain:** Enumeración docker -> daemon/socket -> imágenes/volúmenes -> Flag 1 -> interacción contenedores -> Flag 2 -> escape/montajes -> Flag 3

**Lección:** *El grupo docker y los montajes abiertos convierten cualquier contenedor en un trampolín: los permisos del usuario deciden qué flags quedan al alcance.*

**MITRE ATT&CK:** T1609 (Container Administration Command), T1610 (Deploy Container), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - DockMagic](https://tryhackme.com/room/dockmagic)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.