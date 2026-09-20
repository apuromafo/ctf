# Wireshark: The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `wiresharkthebasics` | [TryHackMe](https://tryhackme.com/room/wiresharkthebasics) | 01 Level Easy | TryHackMe | Wireshark / pcapng / Capture File Properties / Packet Dissection / expert info / display filters / HTTP streams | Primeros pasos con Wireshark: propiedades de captura, disección de paquetes, navegación, filtros y extracción de información |

---

**Contexto:** Primera sala de la trilogía de Wireshark. Se aprende a abrir capturas `.pcapng`, consultar las propiedades del archivo (comentarios, total de paquetes, hash SHA256), diseccionar paquetes (HTTP, TTL, payload TCP, e-tag), navegar y buscar en la captura, exportar objetos, interpretar el expert info y utilizar filtros de visualización y flujos HTTP.

> **ES:** La sala proporciona los fundamentos de Wireshark: dos archivos (http1.pcapng y Exercise.pcapng), propiedades de captura, disección de paquetes, navegación, mensajes del expert info y filtros de visualización.
> **EN:** This room covers the Wireshark basics: two capture files (http1.pcapng and Exercise.pcapng), capture file properties, packet dissection, packet navigation, expert info and display filtering.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Se presentan los dos archivos de la máquina virtual: `http1.pcapng` se usa para simular las capturas de pantalla y `Exercise.pcapng` para responder las preguntas. Contenido original de la sala (verbatim): `http1.pcapng`, `Exercise.pcapng`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué archivo se usa para simular las capturas de pantalla? | `http1.pcapng` |
| ¿Qué archivo se usa para responder las preguntas? | `Exercise.pcapng` |

### Task 2: Descripción general de la herramienta / Tool Overview
**Explicación:** En Statistics > Capture File Properties se obtiene la flag de los comentarios de la captura (`TryHackMe_Wireshark_Demo`), el total de paquetes (58620) y el hash SHA256 del archivo (f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb). Contenido original de la sala (verbatim): `TryHackMe_Wireshark_Demo`, `58620`, `f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Lee los "capture file comments". ¿Cuál es la flag? | `TryHackMe_Wireshark_Demo` |
| ¿Cuál es el número total de paquetes? | `58620` |
| ¿Cuál es el valor del hash SHA256 del archivo de captura? | `f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb` |

### Task 3: Disección de paquetes / Packet Dissection
**Explicación:** Se disecciona el paquete 38: el lenguaje de marcado bajo el protocolo HTTP es `eXtensible Markup Language`, la fecha de llegada es 05/13/2004, el valor TTL es 47, el tamaño del payload TCP es 424 y el valor e-tag es 9a01a-4696-7e354b00. Contenido original de la sala (verbatim): `eXtensible Markup Language`, `05/13/2004`, `47`, `424`, `9a01a-4696-7e354b00`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Ve al paquete número 38. ¿Qué lenguaje de marcado se usa bajo el protocolo HTTP? | `eXtensible Markup Language` |
| ¿Cuál es la fecha de llegada del paquete? (Formato: Mes/Día/Año) | `05/13/2004` |
| ¿Cuál es el valor TTL? | `47` |
| ¿Cuál es el tamaño del payload TCP? | `424` |
| ¿Cuál es el valor e-tag? | `9a01a-4696-7e354b00` |

### Task 4: Navegación de paquetes / Packet Navigation
**Explicación:** Se navega y busca en la captura: el nombre del artista 1 es `r4w8173`, el comentario del paquete 12 responde `911cd574a42865a956ccde2d04495ebf`, el archivo `.txt` exportado revela que el nombre del alien es `PACKETMASTER` y el expert info muestra 1636 warnings. Contenido original de la sala (verbatim): `r4w8173`, `911cd574a42865a956ccde2d04495ebf`, `PACKETMASTER`, `1636`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Busca la cadena "r4w" en los detalles de los paquetes. ¿Cuál es el nombre del artista 1? | `r4w8173` |
| Ve al paquete 12 y lee los comentarios. ¿Cuál es la respuesta? | `911cd574a42865a956ccde2d04495ebf` |
| Hay un archivo ".txt" dentro de la captura. Encuéntralo y léelo; ¿cuál es el nombre del alien? | `PACKETMASTER` |
| Mira la sección de expert info. ¿Cuál es el número de warnings? | `1636` |

### Task 5: Filtrado de paquetes / Packet Filtering
**Explicación:** Se aplican filtros: el filtro resultante del protocolo HTTP es `http`, el número de paquetes mostrados es 1089, siguiendo el stream del paquete 33790 el número total de artistas es 3 y el nombre del segundo artista es `Blad3`. Contenido original de la sala (verbatim): `http`, `1089`, `3`, `Blad3`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Ve al paquete número 4. Haz clic derecho en "Hypertext Transfer Protocol" y aplícalo como filtro. ¿Cuál es la consulta del filtro? | `http` |
| ¿Cuál es el número de paquetes mostrados? | `1089` |
| Ve al paquete número 33790 y sigue el stream. ¿Cuál es el número total de artistas? | `3` |
| ¿Cuál es el nombre del segundo artista? | `Blad3` |

### Task 6: Conclusión / Conclusion
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para continuar? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Archivo para simular las capturas de pantalla | `http1.pcapng` |
| 2 | Archivo para responder las preguntas | `Exercise.pcapng` |
| 3 | Flag de los comentarios de la captura | `TryHackMe_Wireshark_Demo` |
| 4 | Número total de paquetes | `58620` |
| 5 | Hash SHA256 del archivo de captura | `f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb` |
| 6 | Lenguaje de marcado bajo HTTP (paquete 38) | `eXtensible Markup Language` |
| 7 | Fecha de llegada del paquete 38 | `05/13/2004` |
| 8 | Valor TTL del paquete 38 | `47` |
| 9 | Tamaño del payload TCP | `424` |
| 10 | Valor e-tag del paquete 38 | `9a01a-4696-7e354b00` |
| 11 | Nombre del artista 1 (cadena "r4w") | `r4w8173` |
| 12 | Comentario del paquete 12 | `911cd574a42865a956ccde2d04495ebf` |
| 13 | Nombre del alien en el archivo .txt | `PACKETMASTER` |
| 14 | Número de warnings en el expert info | `1636` |
| 15 | Consulta del filtro HTTP | `http` |
| 16 | Número de paquetes mostrados | `1089` |
| 17 | Número total de artistas en el stream | `3` |
| 18 | Nombre del segundo artista | `Blad3` |
| 19 | ¿Preparado para continuar? | `No answer needed` |

---

**Metodología:** Se abre `Exercise.pcapng` en Wireshark, se consultan las propiedades de la captura (comentarios, conteo de paquetes y SHA256), se disecciona el paquete 38 (capa HTTP, marco, TTL y payload TCP), se navega con las búsquedas de cadenas y la exportación de objetos HTTP, se revisa el expert info y se aplican filtros de visualización y seguimiento de streams HTTP.

### Cadena de ataque / Attack Chain

```text
Open Exercise.pcapng -> Capture File Properties (TryHackMe_Wireshark_Demo, 58620, SHA256) -> packet dissection (paquete 38: XML, 05/13/2004, TTL 47, payload 424, e-tag) -> navigation (r4w8173, comentario 911cd574..., PACKETMASTER) -> expert info (1636 warnings) -> display filter (http, 1089) -> follow HTTP stream (3 artistas, Blad3)
```

**Learning chain:** Wireshark overview --> capture file properties --> packet dissection (HTTP, TTL, e-tag) --> packet navigation (find, comments, export objects) --> expert info --> display filtering (http) --> HTTP stream follow-up (artists)

**Lección:** *Wireshark se domina por capas: propiedades del archivo, disección de paquetes, navegación y filtros; esas cuatro habilidades permiten extraer la información relevante de cualquier pcap de forma metódica.*

**MITRE ATT&CK:** T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Wireshark: The Basics](https://tryhackme.com/room/wiresharkthebasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.