# Corridor

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF / Web challenge | `corridor` | https://tryhackme.com/room/corridor | 01 Level Easy | TryHackMe | Web / puertas (doors) / descifrado de nombres de rutas / hashes / lógica del reto | Reto web minimalista: identificar la puerta correcta de un pasillo mediante el descifrado de los nombres de las rutas para obtener la bandera. |

---

**Contexto:** Reto CTF de nivel fácil consistente en un pasillo virtual con múltiples puertas. Cada puerta lleva un identificador en forma de hash/etiqueta y solo una de ellas contiene la bandera. El objetivo es averiguar cuál de las puertas corresponde realmente a la bandera, aplicando una pequeña lógica de descifrado/conversión sobre los identificadores de las rutas.

> **ES:** "Un pasillo con puertas donde cada puerta tiene un identificador. Descifra los identificadores para encontrar la puerta correcta y obtén la bandera."
> **EN:** "A corridor with doors where each door has an identifier. Decode the identifiers to find the correct door and get the flag."

## Solucionario

### Task 1: Encuentra la bandera / Find the flag

**Explicación:** Se visita la aplicación web y se observan varias puertas, cada una con un identificador. Los identificadores son representaciones (por ejemplo, hash/MSD5 o codificación) del nombre de cada puerta. Aplicando la misma lógica de codificación sobre la palabra esperada se identifica cuál de las puertas es la correcta: es la que corresponde a la bandera del reto. La bandera se presenta con el formato `flag{...}`.

```text
1. Revisar el HTML y los nombres de las rutas de las puertas.
2. Descifrar/convertir los identificadores para saber la puerta a la que pertenecen.
3. Identificar la puerta cuyo identificador se corresponde con la bandera.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera? / What is the flag? | `flag{2477ef02448ad9156661ac40a6b8862e}` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | ¿Cuál es la bandera? / What is the flag? | `flag{2477ef02448ad9156661ac40a6b8862e}` |

---

**Metodología:** Abrir el reto en el navegador -> inspeccionar las puertas y sus identificadores -> descifrar los identificadores (conversión/hash) -> cruzar el resultado con el nombre esperado -> entrar en la puerta correcta -> leer la bandera.

### Cadena de ataque / Attack Chain

```text
Acceder al pasillo -> enumerar puertas/IDs -> descifrar identificadores -> localizar la puerta de la flag -> abrir la puerta -> flag{...}
```

**Learning chain:** web -> puertas -> identificadores -> descifrado/decodificación -> puerta correcta -> flag.

**Lección:** *En un CTF, los nombres y parámetros de las rutas rara vez son aleatorios; suelen ser codificaciones que esconden la respuesta.*

**MITRE ATT&CK:** N/A (reto web de lógica/decodificación)

**Fuente:** [TryHackMe - Corridor](https://tryhackme.com/room/corridor)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.