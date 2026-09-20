# KaffeeSec - SoMeSINT

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / OSINT | kaffeesecsomesint | https://tryhackme.com/room/kaffeesecsomesint | 02 Level Medium | TryHackMe | OSINT, Redes Sociales, Sockpuppet, Geolocalización | Correlación de identidades y geolocalización de personas vía OSINT en redes sociales |

---

**Contexto:** La sala **KaffeeSec - SoMeSINT** es un reto de OSINT sobre una persona ficticia (**Thomas Straußman**). Se investigan sus perfiles en redes sociales (TikTok, Facebook, Twitter, Instagram, LinkedIn), se descubre su nombre real, fechas de nacimiento, ubicaciones (Koblenz, Nuuk en Groenlandia), gustos culturales y cuentas secundarias alternativas (`sfp_accounts`). La resolución exige correlacionar fragmentos de contenido, colchonear múltiples fuentes y geolocalizar publicaciones para validar identidades y recuperar las flags en formato `ks{...}`.

## Solucionario

### Task 1: Preparación e inicio de la investigación
**Explicación:**

Se inicia la investigación OSINT y se prepara el entorno (cuentas, notas, búsquedas). No requiere respuesta escrita.

Respuesta: `No answer needed`

### Task 2: Identidad primaria
**Explicación:**

Se identifica al objetivo de la investigación. Las primeras flags determinan el prefijo de formato de las flags y revelan el nombre real del personaje.

1. `ks{H}`
2. `ks{thomas straussman}`

Respuesta:

1. `ks{H}`
2. `ks{thomas straussman}`

### Task 3: Datos personales y perfiles
**Explicación:**

Se extraen datos personales de los perfiles sociales del objetivo: su cumpleaños, la fecha de nacimiento completa, su usuario en una de las redes (Twitter/X) y su animal o detalle personal asociado.

1. `Christmas`
2. `12-20-1990`
3. `@fhodgelink`
4. `Buddha`

Respuesta:

1. `Christmas`
2. `12-20-1990`
3. `@fhodgelink`
4. `Buddha`

### Task 4: Cuentas alternativas
**Explicación:**

Se localizan las cuentas secundarias o sockpuppets del objetivo en las redes. La flag se obtiene del ID de una publicación o cuenta alternativa.

1. `sfp_accounts`
2. `ks{1346173539712380929}`

Respuesta:

1. `sfp_accounts`
2. `ks{1346173539712380929}`

### Task 5: Geolocalización y contexto
**Explicación:**

Se geolocaliza el contenido publicado: la ciudad de origen (Koblenz, Alemania), la fecha de una publicación específica, una cuenta de hobby o contenido (Gotank) y un programa cultural citado.

1. `Koblenz, Germany`
2. `December 25th`
3. `Gotank`
4. `90 Day Fiancee`

Respuesta:

1. `Koblenz, Germany`
2. `December 25th`
3. `Gotank`
4. `90 Day Fiancee`

### Task 6: Deep dive en la identidad
**Explicación:**

Se profundiza en la vida del objetivo en Groenlandia: nombre usado o contacto local (Hans Minik), ubicación en Nuuk, y se obtienen dos flags `ks{...}` junto con el nombre y correo de un contacto cercano.

1. `Hans Minik`
2. `Nuuk, Greenland`
3. `ks{ww4ju}`
4. `ks{1qaz2wsx}`
5. `Emilia Moller`
6. `straussmanthom@mail.com`

Respuesta:

1. `Hans Minik`
2. `Nuuk, Greenland`
3. `ks{ww4ju}`
4. `ks{1qaz2wsx}`
5. `Emilia Moller`
6. `straussmanthom@mail.com`

### Task 7: Conclusión
**Explicación:**

Se cierra la investigación confirmando la identidad y las fuentes. No requiere respuestas escritas.

Respuesta:

1. `No answer needed`
2. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1: Inicio de la investigación | `No answer needed` |
| 2 | Task 2: Formato de flags | `ks{H}` |
| 2 | Task 2: Nombre real del objetivo | `ks{thomas straussman}` |
| 3 | Task 3: Cumpleaños | `Christmas` |
| 3 | Task 3: Fecha de nacimiento | `12-20-1990` |
| 3 | Task 3: Usuario de Twitter | `@fhodgelink` |
| 3 | Task 3: Detalle personal | `Buddha` |
| 4 | Task 4: Cuentas secundarias | `sfp_accounts` |
| 4 | Task 4: Flag de cuenta alternativa | `ks{1346173539712380929}` |
| 5 | Task 5: Ciudad de origen | `Koblenz, Germany` |
| 5 | Task 5: Fecha de publicación | `December 25th` |
| 5 | Task 5: Cuenta/plataforma | `Gotank` |
| 5 | Task 5: Programa cultural | `90 Day Fiancee` |
| 6 | Task 6: Contacto en Groenlandia | `Hans Minik` |
| 6 | Task 6: Ubicación | `Nuuk, Greenland` |
| 6 | Task 6: Flag | `ks{ww4ju}` |
| 6 | Task 6: Flag | `ks{1qaz2wsx}` |
| 6 | Task 6: Nombre del contacto | `Emilia Moller` |
| 6 | Task 6: Correo del contacto | `straussmanthom@mail.com` |
| 7 | Task 7: Conclusión | `No answer needed` |
| 7 | Task 7: Conclusión | `No answer needed` |

---

**Metodología:** Definición del objetivo → búsqueda en redes sociales (TikTok, Facebook, Twitter, Instagram, LinkedIn) → extracción de datos personales y fechas → descubrimiento de sockpuppets (`sfp_accounts`) → geolocalización de contenido (Koblenz, Nuuk) → correlación cruzada de identidades → obtención de flags `ks{...}`.

**Learning chain:** Identidad → perfiles sociales → datos personales → cuentas alternativas → geolocalización → validación cruzada → veredicto final.

**Lección:** *Las personas filtran su identidad completa en redes sociales: correlacionar fechas, ubicaciones, contactos y cuentas alternativas reconstruye el perfil OSINT completo.*

**MITRE ATT&CK:** T1532 Data from Cloud Storage · T1057 Process Discovery (correlación de fuentes) · T1585 Establish Accounts.

**Fuente:** [TryHackMe - KaffeeSec - SoMeSINT](https://tryhackme.com/room/kaffeesecsomesint)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.