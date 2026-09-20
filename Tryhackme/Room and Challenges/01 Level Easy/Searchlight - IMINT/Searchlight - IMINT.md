# Searchlight - IMINT

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `searchlightimint` | [TryHackMe](https://tryhackme.com/room/searchlightimint) | `01 Level Easy` | THM | OSINT, IMINT, geolocalización, análisis de imágenes | Resolución completa del reto de inteligencia de imágenes |

---

**Contexto:** Reto de IMINT (inteligencia a partir de imágenes) en la línea de los CTF de OSINT tipo geolocalización: se analizan fotografías para identificar lugares (calles, monumentos, aeropuertos, restaurantes, hoteles), personas (Andrew Knowlton, Kjersti Stensrud) y datos como direcciones, números de teléfono o correos. Las respuestas son flags en formato `sl{...}`.

> **ES:** Reto de inteligencia de imágenes (IMINT): a partir de fotografías se deben geolocalizar lugares, identificar personas y recuperar datos como direcciones, teléfonos y correos, respondiendo en formato sl{...}.
> **EN:** IMINT (imagery intelligence) challenge: from photographs you must geolocate places, identify people and recover data such as addresses, phone numbers and emails, answering in sl{...} format.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea de confirmación: tan solo se solicita demostrar que se está listo para comenzar el reto.

1. sl{ready}

### Task 2: Primera calle / First street

**Explicación:** Se geolocaliza la primera fotografía; el lugar identificado es Carnaby Street.

2. sl{carnaby street}

### Task 3: Londres, ¡no leas el título! / London, don't read the title!

**Explicación:** A partir de la localización inicial se identifican la ciudad (London), un punto emblemático (Piccadilly Circus), el año (1906) y el número de calles (4).

1. sl{london}
2. sl{piccadilly circus}
3. sl{1906}
4. sl{4}

### Task 4: Un avión / A plane

**Explicación:** La fotografía corresponde al aeropuerto Vancouver International Airport, en Canada, ubicado en Richmond.

1. sl{vancouver international airport}
2. sl{canada}
3. sl{richmond}

### Task 5: Cafetería y pueblo escocés / Coffee shop and Scottish town

**Explicación:** Se identifica la cafetería The Wee Coffee Shop en Blairgowrie (Allan Street), con su número de teléfono y correo; el propietario aporta el apellido Cochrane.

1. sl{blairgowrie}
2. sl{allan street}
3. sl{+447878 839128}
4. sl{theweecoffeeshop@aol.com}
5. sl{cochrane}

### Task 6: Katz's Deli / Katz's Deli

**Explicación:** Se identifica el famoso delicatesen neoyorquino Katz's Deli y a la persona ligada a la imagen, Andrew Knowlton.

1. sl{katz's deli}
2. sl{andrew knowlton}

### Task 7: De vuelta al polo norte / Back to the North Pole

**Explicación:** La escena festiva lleva a Rudolph the Chrome Nosed Reindeer y a la persona identificada como Kjersti Stensrud.

1. sl{rudolph the chrome nosed reindeer}
2. sl{kjersti stensrud}

### Task 8: Una estatua preocupante / A worrying statue

**Explicación:** La estatua de Lady Justice apunta a Alexandria, Virginia, y al hotel The Westin Alexandria Old Town.

1. sl{lady justice}
2. sl{alexandria, virginia}
3. sl{the westin alexandria old town}

### Task 9: Un hotel en Singapur / A hotel in Singapore

**Explicación:** La fotografía final corresponde al hotel Novotel Singapore Clarke Quay.

9. sl{novotel singapore clarke quay}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Confirmación de inicio del reto | `sl{ready}` |
| 2.1 | Primera calle identificada | `sl{carnaby street}` |
| 3.1 | Ciudad de la localización | `sl{london}` |
| 3.2 | Punto emblemático identificado | `sl{piccadilly circus}` |
| 3.3 | Año de la foto | `sl{1906}` |
| 3.4 | Número de calles | `sl{4}` |
| 4.1 | Aeropuerto identificado | `sl{vancouver international airport}` |
| 4.2 | País | `sl{canada}` |
| 4.3 | Ciudad del aeropuerto | `sl{richmond}` |
| 5.1 | Pueblo escocés | `sl{blairgowrie}` |
| 5.2 | Calle de la cafetería | `sl{allan street}` |
| 5.3 | Teléfono de la cafetería | `sl{+447878 839128}` |
| 5.4 | Correo de la cafetería | `sl{theweecoffeeshop@aol.com}` |
| 5.5 | Apellido del propietario | `sl{cochrane}` |
| 6.1 | Delicatesen identificado | `sl{katz's deli}` |
| 6.2 | Persona identificada | `sl{andrew knowlton}` |
| 7.1 | Figura navideña de la imagen | `sl{rudolph the chrome nosed reindeer}` |
| 7.2 | Persona identificada en la escena | `sl{kjersti stensrud}` |
| 8.1 | Estatua de la imagen | `sl{lady justice}` |
| 8.2 | Ciudad de la estatua | `sl{alexandria, virginia}` |
| 8.3 | Hotel donde se ubica | `sl{the westin alexandria old town}` |
| 9.1 | Hotel final en Singapur | `sl{novotel singapore clarke quay}` |

---

**Metodología:** 1) Analizar cada fotografía (arquitectura, señalética, vallas, elementos distintivos). 2) Geolocalizar el lugar (calle, ciudad, país). 3) Buscar en fuentes públicas el establecimiento y sus datos (teléfono, correo, propietario). 4) Identificar a las personas presentes o relacionadas. 5) Responder cada pista con la flag sl{...} correspondiente.

### Cadena de ataque / Attack Chain

```text
sl{ready} -> Carnaby Street -> London (Piccadilly Circus, 1906, 4 calles) -> Vancouver Airport (Canada, Richmond) -> The Wee Coffee Shop (Blairgowrie, +44..., correo, Cochrane) -> Katz's Deli (Andrew Knowlton) -> Rudolph the Chrome Nosed Reindeer (Kjersti Stensrud) -> Lady Justice (Alexandria, Westin) -> Novotel Singapore Clarke Quay
```

**Learning chain:** IMINT (análisis visual de fotografías) -> geolocalización -> identificación de establecimientos y personas -> búsqueda de datos públicos -> flags sl{...}

**Lección:** *La inteligencia de imágenes combina observación visual, búsqueda en fuentes abiertas y geolocalización: cada detalle de una fotografía es una pista verificable.*

**MITRE ATT&CK:** T1593.002 (Search Open Websites/Domains: Social Engineering), T1596.001 (Search Open Technical Databases: DNS/Passive DNS)

**Fuente:** [TryHackMe - Searchlight - IMINT](https://tryhackme.com/room/searchlightimint)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.