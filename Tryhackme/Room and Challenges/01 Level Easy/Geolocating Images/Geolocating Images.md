# Geolocating Images

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | OSINT / walkthrough | `geolocatingimages` | https://tryhackme.com/room/geolocatingimages | 01 Level Easy | TryHackMe | OSINT / geolocalización / image search / cross-referencing / Google Maps | Defensivo: localizar el lugar de origen de varias fotografías usando pistas visuales (señalética, arquitectura, nombres) y buscadores de imágenes. |

---

> **Objeto:** Resolver una serie de ejercicios de geolocalización OSINT: examinar cada fotografía, explotar referencias visuales (carteles, tiendas, edificios, cruces de calles), apoyarse en búsqueda inversa de imágenes y mapas, y anotar dónde fue tomada cada toma.

**Contexto:** Sala de OSINT que entrena la geolocalización de imágenes reales. Cada tarea entrega una foto y hay que averiguar el lugar, el establecimiento o el hito representado combinando el análisis de detalles visibles (nombres en fachadas, países en banderas, arquitectura típica) con herramientas como la búsqueda inversa de imágenes y cruces con mapas. Las ubicaciones van desde edificios concretos (el templo rojo en `China`, la tienda `Wrigleyville Sports` junto al Wrigley Field en Chicago, el `Meudon Observatory` en París) hasta famosos cruces icónicos como `Abbey Road` en Londres.

> **ES:** "Geolocating Images" — ejercicios de geolocalización OSINT guiados por pistas visuales, búsqueda inversa y mapas.
> **EN:** OSINT geolocation drills where visual clues and reverse image search pin down real-world photo locations.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Lectura de la introducción de la sala: metodología para geolocalizar imágenes (carteles, clima, arquitectura, redes sociales y búsqueda inversa). No hay respuesta que escribir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the introduction. / Lee la introducción. | `No answer needed` |

### Task 2: Primer ejercicio / First Exercise

**Explicación:** La primera fotografía muestra un edificio de estilo asiático con elementos distintivos (tejados y un cartel claramente chino). Cruzando la señalética y el idioma de los carteles con la búsqueda visual se determina que la imagen fue tomada en `China`, concretamente en el recinto de un templo conocido con estructuras rojas decoradas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | ¿Dónde fue tomada la imagen? / Where was the image taken? | `China` |

### Task 3: Análisis de la pista / Clue Analysis

**Explicación:** Paso de comprobación dentro del proceso de geolocalización (p. ej. confirmar la ciudad o el hito con mapas). No se rellena texto de respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | Follow the OSINT process. / Sigue el proceso OSINT. | `No answer needed` |

### Task 4: Tienda identificada / Identified Shop

**Explicación:** La fotografía muestra la fachada de un comercio cuya señalética y decoración temática de béisbol apuntan a la zona del estadio del Wrigley Field (Chicago). Buscando el nombre visible en el escaparate se identifica la tienda: `Wrigleyville Sports`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | Identifica la tienda de la imagen. / Identify the shop in the image. | `Wrigleyville Sports` |

### Task 5: Verificación / Verification

**Explicación:** Confirmación del punto exacto (recorrido virtual/Street View o consulta del negocio en mapas). No requiere respuesta escrita.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | Verify the location. / Verifica la ubicación. | `No answer needed` |

### Task 6: Observatorio / Observatory

**Explicación:** La imagen muestra la cúpula de un edificio histórico de observatorio en Francia. El hito coincide con el gran observatorio al sur de París conocido por su cúpula de hierro: el `Meudon Observatory` (observatorio de París-Meudon).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | ¿Qué observatorio aparece en la imagen? / Which observatory is in the image? | `Meudon Observatory` |

### Task 7: Paso de cebra icónico / Iconic Zebra Crossing

**Explicación:** La última fotografía es un paso de peatones con una señal de calle reconocible en el contexto de la cultura pop británica. Es el célebre cruce de `Abbey Road`, hecho famoso por la portada del álbum de The Beatles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | ¿Dónde está la imagen? / Where is the image? | `Abbey Road` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre de la sala tras localizar todas las imágenes. No hay respuesta que escribir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 8 | Complete the room. / Completa la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the introduction. | `No answer needed` |
| 2 | Where was the image taken? | `China` |
| 3 | Follow the OSINT process. | `No answer needed` |
| 4 | Identify the shop in the image. | `Wrigleyville Sports` |
| 5 | Verify the location. | `No answer needed` |
| 6 | Which observatory is in the image? | `Meudon Observatory` |
| 7 | Where is the image? | `Abbey Road` |
| 8 | Complete the room. | `No answer needed` |

---

**Metodología:** Por cada imagen se aplica el mismo flujo: analizar pistas visuales (idioma de carteles, señalética, arquitectura, estilo de comercio), hacer búsqueda inversa de la imagen y cruzar con mapas para localizar el hito. Las respuestas resultan de identificar puntos de referencia (templo en China, `Wrigleyville Sports` en Chicago, `Meudon Observatory` en París y el cruce de `Abbey Road` en Londres).

### Cadena de ataque / Attack Chain

```text
Análisis visual de la foto -> pistas (carteles/arquitectura/nombres) -> búsqueda inversa de imagen -> cruce con mapas/Street View -> ubicación confirmada
```

**Learning chain:** photo analysis -> visual clues -> reverse image search -> map cross-referencing -> confirmed geolocation.

**Lección:** *Geolocalizar imágenes es un proceso de verificación cruzada: cada detalle visible (un cartel, un toldo, una cúpula) reduce el espacio de búsqueda hasta identificar de forma inequívoca el lugar exacto.*

**MITRE ATT&CK:** N/A (OSINT — ioc development / general Open Source Intelligence techniques)

**Fuente:** [TryHackMe - Geolocating Images](https://tryhackme.com/room/geolocatingimages)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.