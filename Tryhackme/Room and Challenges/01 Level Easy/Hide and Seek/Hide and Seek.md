# Hide and Seek

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `hideandseek` | https://tryhackme.com/room/hideandseek | 01 Level Easy | TryHackMe | View Source / análisis del código fuente web / búsqueda de datos ocultos | Localizar la flag oculta dentro del código fuente del sitio del reto. |

---

**Contexto:** Reto tipo CTF de dificultad Easy en el que la flag está oculta dentro del propio sitio web. La clave está en revisar el código fuente de la página (HTML/JavaScript) y examinar comentarios, variables y datos embebidos hasta dar con la bandera.

> **ES:** Inspecciona el código fuente del sitio web del reto y encuentra la flag oculta.
> **EN:** Inspect the challenge website's source code and find the hidden flag.

## Solucionario

### Task 1: Encontrar la flag oculta / Find the Hidden Flag

**Explicación:** La flag está escondida dentro del código fuente de la página. Al abrir el View Source o las DevTools del navegador y revisar con detalle el HTML y el JavaScript, aparece la cadena del flag en alguno de los datos de la web.

1. THM{y0u_g0t_3v3ryth1ng_d0wn}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag? / What is the flag? | `THM{y0u_g0t_3v3ryth1ng_d0wn}` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | ¿Cuál es la flag? / What is the flag? | `THM{y0u_g0t_3v3ryth1ng_d0wn}` |

---

**Metodología:** Reconocimiento pasivo de la web del reto: abrir el código fuente de la página, inspeccionar el HTML y el JavaScript mediante View Source / DevTools y buscar cadenas ocultas hasta localizar el flag.

### Cadena de ataque / Attack Chain

```text
view-source -> inspección de HTML/JS -> búsqueda de datos ocultos -> flag
```

**Learning chain:** Web -> Source Code Review -> descubrimiento de contenido oculto -> flag.

**Lección:** *Siempre revisa el código fuente de las páginas del reto: comentarios, variables y datos embebidos suelen contener flags y pistas valiosas.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1592 (Gather Victim Host Information)

**Fuente:** [TryHackMe - Hide and Seek](https://tryhackme.com/room/hideandseek)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
