# The Impossible Challenge
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Challenge / Steganografía | theimpossiblechallenge | https://tryhackme.com/room/theimpossiblechallenge | 02 Level Medium | TryHackMe | Steganografía, caracteres de ancho cero (zero-width), decodificación, análisis de archivos | Reto que oculta la flag mediante caracteres invisibles dentro de un archivo descargable |

> **Objeto:** Descargar el archivo del reto y encontrar la flag.

---
**Contexto:** **The Impossible Challenge** es un reto de dificultad Media que aparenta ser imposible pero esconde su solución en la esteganografía. Se entrega un archivo descargable que, a simple vista, no revela nada; el reto consiste en descubrir el mecanismo de ocultación empleado. La respuesta final (`THM{Zero_Width_Characters_EZPZ}`) y la propia temática apuntan al uso de **caracteres de ancho cero** (zero-width) para esconder la flag. La resolución pasa por inspeccionar el archivo y decodificar esos caracteres invisibles.
> **ES:** Descarga el archivo y encuentra la flag.
> **EN:** Download the file, and find the Flag!

## Solucionario
### Task 1: Enviar la flag / Submit the flag
**Explicación:** Se descarga el archivo del reto y se inspecciona su contenido en busca de información oculta. El archivo contiene una cadena de caracteres aparentemente inofensiva, pero entre ellos se esconden caracteres de ancho cero que codifican la flag. Decodificando esos caracteres invisibles se obtiene la respuesta en formato `THM{}`.

Contenido original de la tarea (cadena entregada):

```
qo qt q` r6 ro su pn s_ rn r6 p6 s_ q2 ps qq rs rp ps rt r4 pu pt qn r4 rq pt q` so pu ps r4 sq pu ps q2 su rn on oq o_ pu ps ou r5 pu pt r4 sr rp qt pu rs q2 qt r4 r4 ro su pq o5
```

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| flag is in the format THM{} | `THM{Zero_Width_Characters_EZPZ}` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | flag is in the format THM{} | `THM{Zero_Width_Characters_EZPZ}` |

---
**Metodología:** Descarga del archivo → inspección del contenido en busca de caracteres invisibles → decodificación de los caracteres de ancho cero → obtención de la flag.

### Cadena de ataque / Attack Chain
```
Descargar archivo -> inspeccionar contenido -> detectar caracteres de ancho cero (zero-width)
-> decodificar la secuencia oculta -> THM{Zero_Width_Characters_EZPZ}
```
**Learning chain:** Descarga → análisis de esteganografía → identificación de caracteres invisibles → decodificación → flag.
**Lección:** *La información puede ocultarse en caracteres que no se ven; ante un reto "imposible" hay que inspeccionar el contenido a nivel de bytes/Unicode.*
**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1140 (Deobfuscate/Decode Files or Information).
**Fuente:** [TryHackMe - The Impossible Challenge](https://tryhackme.com/room/theimpossiblechallenge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
