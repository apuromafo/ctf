# U.A. High School

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `uahighschool` | [TryHackMe](https://tryhackme.com/room/uahighschool) | 01 Level Easy | THM | servidor web, CTF, My Hero Academia, flags | Obtención de flags en un servidor web temático de la escuela U.A. |

---

**Contexto:**

> **ES:** La sala reta a descubrir los secretos ocultos en un servidor web ambientado en la escuela de héroes U.A. High School (My Hero Academia). Explorando la web y sus recursos se obtienen las dos flags escondidas en el entorno.

> **EN:** This room challenges you to uncover the secrets hidden in a web server themed around U.A. High School (My Hero Academia). Exploring the web and its resources leads to the two flags hidden in the environment.

## Solucionario

### Task 1: Resolución de la sala / U.A. High School Walkthrough

**Explicación:**

1. 1. THM{W3lC0m3_D3kU_1A_0n3f0rAll??}
   2. THM{Y0U_4r3_7h3_NUm83r_1_H3r0}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag found on the server? | `THM{W3lC0m3_D3kU_1A_0n3f0rAll??}` |
| 2 | What is the flag hidden in the environment? | `THM{Y0U_4r3_7h3_NUm83r_1_H3r0}` |

---

**Metodología:** Se explora el servidor web temático de la U.A. High School, inspeccionando las páginas y recursos disponibles, y se recurre a la enumeración de rutas y al análisis del contenido para localizar las dos flags escondidas en el entorno.

### Cadena de ataque / Attack Chain

Web reconnaissance → resource discovery → first flag → hidden content → second flag.

**Learning chain:** web exploration → content discovery → flag extraction

**Lección:** *En la web, lo que no está enlazado no significa que no exista: la enumeración de recursos descubre lo que la interfaz oculta.*

**MITRE ATT&CK:** T1505.003 (Web Shell), T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - U.A. High School](https://tryhackme.com/room/uahighschool)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.