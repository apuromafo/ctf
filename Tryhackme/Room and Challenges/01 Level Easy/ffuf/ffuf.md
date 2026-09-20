# ffuf

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `ffuf` | [TryHackMe - ffuf](https://tryhackme.com/room/ffuf) | `01 Level Easy` | THM | ffuf, fuzzing, content discovery, vhost, parámetros, opciones | Exploitation — fuzzing web y descubrimiento de contenido |

> **Objeto:** Dominar la herramienta ffuf para descubrir contenido, directorios ocultos, extensiones, subdominios/vhosts y parámetros, así como sus opciones de filtrado y salida.

---

**Contexto:** La sala ffuf es una guía práctica de la herramienta de fuzzing ffuf. Se aprende a descubrir contenido web (robots.txt, extensiones, directorios), a aplicar fuzzing recursivo y con wordlists, a descubrir parámetros y valores ocultos, y a utilizar las opciones de salida, filtros y flags de ffuf para optimizar los resultados.

> **ES:** Sala práctica de ffuf: descubrimiento de contenido, extensiones, fuzzing recursivo, parámetros ocultos y opciones de la herramienta.
>
> **EN:** Hands-on ffuf room: content discovery, extensions, recursive fuzzing, hidden parameters and tool options.

## Solucionario

### Task 1: Preparación / Preparation

**Explicación:** Se conecta con la máquina de práctica y se comprueban los ficheros y configuración inicial del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación del laboratorio | `No answer needed` |
| 2 | Comprobación inicial | `No answer needed` |

### Task 2: Fuzzing de favicon / Favicon Fuzzing

**Explicación:** Se utiliza ffuf (o una wordlist de hashes) para identificar el archivo favicon del sitio, lo que permite reconocer el framework mediante su hash.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Archivo favicon detectado | `favicon.ico` |

### Task 3: Descubrimiento de contenido / Content Discovery

**Explicación:** Se hace fuzzing de directorios con wordlist, se descubre `robots.txt`, se identifican las extensiones activas (`php`, `phps`) y el archivo `about.php`, terminando con el recuento de resultados encontrados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer fichero descubierto | `robots.txt` |
| 2 | Extensiones encontradas en el sitio | `php,phps` |
| 3 | Archivo con la ruta oculta | `about.php` |
| 4 | Número de resultados obtenidos | `4` |

### Task 4: Fuzzing recursivo / Recursive Fuzzing

**Explicación:** Se combina fuzzing recursivo con una wordlist mayor sobre el directorio descubierto para localizar más resultados y ficheros relevantes como `wp-forum.phps`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Número de resultados con la nueva wordlist | `11` |
| 2 | Número de directorios/resultados filtrados por tamaño | `6` |
| 3 | Fichero relevante descubierto | `wp-forum.phps` |

### Task 5: Fuzzing de parámetros / Parameter Fuzzing

**Explicación:** Se localiza el nombre de un parámetro activo (`id`), se fuzzea su valor para descubrir el correcto y se descubre también la contraseña del usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Parámetro encontrado | `id` |
| 2 | Valor del parámetro que da resultado | `14` |
| 3 | Contraseña descubierta | `p@ssword` |

### Task 6: Práctica con vhosts / Vhost Practice

**Explicación:** Se practica el fuzzing de hosts virtuales sobre la máquina de práctica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejercicio de vhosts | `No answer needed` |

### Task 7: Otras herramientas / Other Tools

**Explicación:** Se mencionan otras herramientas de fuzzing y descubrimiento complementarias a ffuf.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Herramientas complementarias | `No answer needed` |

### Task 8: Opciones de ffuf / ffuf Flags

**Explicación:** Se revisan las opciones de formato de salida y control de ffuf: escritura a fichero en Markdown, uso de ficheros de request, ignorar comentarios, leer wordlist desde stdin, verbosidad, seguir redirects y salida en color.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Opción de salida a fichero Markdown | `-of md -o ffuf.md` |
| 2 | Opción para usar un fichero de request | `-request` |
| 3 | Opción para ignorar comentarios en la wordlist | `-ic` |
| 4 | Opción para leer la wordlist desde stdin | `-w -` |
| 5 | Opción de salida verbosa | `-v` |
| 6 | Opción para seguir redirects | `-r` |
| 7 | Opción de color en la salida | `-c` |

### Task 9: Conclusión / Conclusion

**Explicación:** La sala cierra resumiendo lo aprendido sobre el uso de ffuf en reconocimiento de aplicaciones web.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Se trabaja sobre la máquina de práctica con ffuf usando wordlists (por defecto `/usr/share/wordlists/SecLists/...`). Se fuzzea contenido, extensiones y directorios; se aplica fuzzing recursivo y de parámetros; se practica con hosts virtuales; y finalmente se repasan las opciones de salida (`-of`, `-o`, `-request`, `-ic`, `-w -`, `-v`, `-r`, `-c`) para controlar formato, filtros y verbosidad de los resultados.

### Cadena de ataque / Attack Chain

Fuzzing de favicon → Descubrimiento de directorios/archivos (robots.txt, about.php) → Identificación de extensiones (php, phps) → Fuzzing recursivo (wp-forum.phps) → Fuzzing de parámetros (id → 14; p@ssword) → Vhosts → Opciones de salida de ffuf.

**Learning chain:** ffuf basics → favicon hashing → content discovery → extension filtering → recursive fuzzing → parameter/value fuzzing → vhost fuzzing → output/filter options

**Lección:** *ffuf es el acelerador del reconocimiento web: saber combinarlo con wordlists adecuadas, filtros por tamaño y opciones de salida permite descubrir en minutos contenido, parámetros y hosts que el ojo humano pasaría por alto.*

**MITRE ATT&CK:** T1595.001 - Active Scanning: Scanning IP Blocks, T1595.002 - Active Scanning: Vulnerability Scanning, T1046 - Network Service Discovery, T1110.001 - Brute Force: Password Guessing

**Fuente:** [TryHackMe - ffuf](https://tryhackme.com/room/ffuf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.