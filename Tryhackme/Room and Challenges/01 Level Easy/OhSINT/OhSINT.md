# OhSINT

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `ohsint` | [TryHackMe](https://tryhackme.com/room/ohsint) | `01 Level Easy` | THM | OSINT, EXIF, redes sociales, GitHub | Resolución completa del reto OSINT |

> **Objeto:** Resolver un reto de inteligencia de fuentes abiertas a partir de una imagen: correlacionar los metadatos EXIF con los perfiles en redes sociales y repositorios de GitHub para recuperar avatar, ubicaciones, SSID, correo, sitio de creación de contraseña y la contraseña final.

---

**Contexto:** Reto de OSINT puro: a partir de pistas públicas de un usuario, se combinan los metadatos EXIF de una imagen con su presencia en redes sociales y en GitHub hasta recuperar todos los datos solicitados, incluida la contraseña final del usuario (OWoodflint).

> **ES:** Reto de OSINT puro: a partir de pistas públicas de un usuario, se combinan los metadatos EXIF de una imagen con su presencia en redes sociales y en GitHub hasta recuperar todos los datos solicitados, incluida la contraseña final del usuario (OWoodflint).

> **EN:** Pure OSINT challenge: from public clues of a user, the EXIF metadata of an image is combined with their presence on social media and GitHub to recover all the requested data, including the user's final password (OWoodflint).

## Solucionario

### Task 1: OhSINT / OhSINT

**Explicación:** Se aplica inteligencia de fuentes abiertas sobre la imagen proporcionada y sobre la identidad digital del usuario. El contenido original del reto, conservado íntegramente, es el siguiente:

1. 1. cat
   2. London
   3. UnileverWiFi
   4. OWoodflint@gmail.com
   5. Github
   6. New York
   7. pennYDr0pper.!

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el avatar del usuario? | `cat` |
| 2 | ¿En qué ciudad se encuentra esta persona? | `London` |
| 3 | ¿Cuál es el SSID del punto de acceso al que se conectó? | `UnileverWiFi` |
| 4 | ¿Cuál es la dirección de correo electrónico de la persona? | `OWoodflint@gmail.com` |
| 5 | ¿En qué sitio probablemente creó la persona su contraseña? | `Github` |
| 6 | ¿En qué ciudad se encuentra la persona según la segunda pista? | `New York` |
| 7 | ¿Cuál es la contraseña? | `pennYDr0pper.!` |

---

**Metodología:** 1) Descargar la imagen y extraer sus metadatos EXIF (comentarios, geolocalización). 2) Localizar el perfil del usuario en redes sociales y recuperar su avatar (cat) y su ciudad (London). 3) Consultar el SSID del punto de acceso cercano (UnileverWiFi). 4) Obtener el correo (OWoodflint@gmail.com) desde el perfil. 5) Identificar el sitio en el que se creó la contraseña (Github). 6) Recuperar la segunda ubicación (New York). 7) Extraer la contraseña final (pennYDr0pper.!).

### Cadena de ataque / Attack Chain

1. Extracción de los metadatos de la imagen.
2. Localización y análisis del perfil del usuario en redes sociales.
3. Reconstrucción de la identidad: avatar, correo, ubicaciones y SSID.
4. Correlación con GitHub y el sitio de creación de la contraseña.
5. Obtención de la credencial final.

**Learning chain:** EXIF metadata → OSINT en redes sociales → geolocalización y SSID → enumeración de correo → OSINT en GitHub → recuperación de la contraseña

**Lección:** *La huella digital pública (metadatos, redes sociales y repositorios) permite reconstruir la identidad de una persona: el OSINT consiste en correlacionar pistas aparentemente aisladas.*

**MITRE ATT&CK:** T1593.002 - Search Open Websites/Domains: Social Engineering, T1592.001 - Gather Victim Host Information: Hardware, T1595.002 - Active Scanning: Vulnerability Scanning

**Fuente:** [TryHackMe - OhSINT](https://tryhackme.com/room/ohsint)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.