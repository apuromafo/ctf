# Web Enumeration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `webenumeration` | https://tryhackme.com/room/webenumeration | 01 Level Easy | TryHackMe | gobuster, Wappalyzer, WordPress, nmap, cabeceras HTTP, robots.txt | Enumeración sistemática de activos web (directorios, tecnologías, CMS, servicios y cabeceras) |

---

**Contexto:** Sala dedicada a la enumeración web: descubrimiento de archivos y directorios con gobuster, identificación de tecnologías (Wappalyzer), reconocimiento pasivo, enumeración de WordPress, escaneo con nmap y análisis de cabeceras HTTP. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Enumeración web completa: gobuster, Wappalyzer, reconocimiento pasivo, WordPress, nmap y cabeceras HTTP para cartografiar el sitio objetivo.
> **EN:** Full web enumeration: gobuster, Wappalyzer, passive reconnaissance, WordPress, nmap and HTTP headers to map the target site.

## Solucionario

### Task 1: Despliegue y preparación / Deploy and Preparation

**Explicación:** Se despliega la máquina y se prepara el entorno de trabajo. No requiere respuesta.

```
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: ¿Qué es la enumeración? / What is Enumeration?

**Explicación:** Concepto teórico de la enumeración como fase activa de recopilación de información. No requiere respuesta.

```
2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 3: ¿Por qué enumerar? / Why Enumerate?

**Explicación:** Se justifica la importancia de la enumeración dentro del proceso de pentest. No requiere respuesta.

```
3. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 4: Robots.txt / Robots.txt

**Explicación:** Se revisa el archivo `robots.txt` como fuente de directorios restringidos. No requiere respuesta.

```
4. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 5: Exploración manual / Manual Exploration

**Explicación:** Se explora el sitio manualmente buscando enlaces y recursos en el código fuente. No requiere respuesta.

```
5. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 6: Gobuster / Gobuster

**Explicación:** Se fuerza la enumeración de directorios con gobuster. Se descubren las carpetas `public`, `Changes` y `VIDEO`, las extensiones `conf` y `js`, la flag `thm{n1c3_w0rk}` del directorio encontrado, los directorios `learning` y `products`, y la flag `thm{gobuster_is_fun}`.

```
6. 1. public,Changes,VIDEO
   2. conf,js
   3. thm{n1c3_w0rk}
   4. learning,products
   5. thm{gobuster_is_fun}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `public,Changes,VIDEO` |
| 2 | *(Pregunta 2 no especificada en el original)* | `conf,js` |
| 3 | *(Pregunta 3 no especificada en el original)* | `thm{n1c3_w0rk}` |
| 4 | *(Pregunta 4 no especificada en el original)* | `learning,products` |
| 5 | *(Pregunta 5 no especificada en el original)* | `thm{gobuster_is_fun}` |

### Task 7: Wappalyzer / Wappalyzer

**Explicación:** Se identifica el perfil tecnológico del sitio con la extensión Wappalyzer. No requiere respuesta.

```
7. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 8: Reconocimiento pasivo / Passive Reconnaissance

**Explicación:** Se aplica reconocimiento pasivo sobre una web de ejemplo: la ruta del tema es `http://cmnatics.playground/wp-content/themes/twentynineteen`; se distingue entre la enumeración activa (`enumerate`) y la pasiva (`passive`).

```
8. 1. http://cmnatics.playground/wp-content/themes/twentynineteen
   2. enumerate
   3. passive
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `http://cmnatics.playground/wp-content/themes/twentynineteen` |
| 2 | *(Pregunta 2 no especificada en el original)* | `enumerate` |
| 3 | *(Pregunta 3 no especificada en el original)* | `passive` |

### Task 9: Enumeración de WordPress / WordPress Enumeration

**Explicación:** Se enumera un sitio WordPress: el tema activo es `twentynineteen`, el plugin `nextgen-gallery`, y se identifican los usuarios `phreakazoid` y `linkinpark`.

```
9. 1. twentynineteen
   2. nextgen-gallery
   3. phreakazoid
   4. linkinpark
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `twentynineteen` |
| 2 | *(Pregunta 2 no especificada en el original)* | `nextgen-gallery` |
| 3 | *(Pregunta 3 no especificada en el original)* | `phreakazoid` |
| 4 | *(Pregunta 4 no especificada en el original)* | `linkinpark` |

### Task 10: Sitemap / Sitemap

**Explicación:** Se revisa el sitemap del sitio para localizar más rutas. No requiere respuesta.

```
10. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 11: Nmap / Nmap

**Explicación:** Se usa nmap para escanear el host: el flag de puertos es `-p 80,8080` y el flag de rendering de la respuesta es `-Display 2`.

```
11. 1. -p 80,8080
    2. -Display 2
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `-p 80,8080` |
| 2 | *(Pregunta 2 no especificada en el original)* | `-Display 2` |

### Task 12: Cabeceras HTTP / HTTP Headers

**Explicación:** Se analizan las cabeceras HTTP de los servicios: el servidor Apache reporta `Apache/2.4.7`, el servidor de aplicaciones `Apache-Coyote/1.1` y la cookie de sesión es `JSESSIONID`.

```
12. 1. Apache/2.4.7
    2. Apache-Coyote/1.1
    3. JSESSIONID
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Apache/2.4.7` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Apache-Coyote/1.1` |
| 3 | *(Pregunta 3 no especificada en el original)* | `JSESSIONID` |

### Task 13: Resultados y resumen / Results and Wrap-up

**Explicación:** Tarea de cierre que resume lo aprendido sobre enumeración web. No requiere respuesta.

```
13. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Preparación y despliegue → conceptos de enumeración → robots.txt y exploración manual → gobuster (directorios y extensiones) → Wappalyzer → reconocimiento pasivo → enumeración de WordPress → sitemap → nmap → análisis de cabeceras HTTP.

### Cadena de ataque / Attack Chain

```text
Deploy -> robots.txt -> exploración manual -> gobuster (public/Changes/VIDEO, conf/js, learning/products) -> Wappalyzer -> passive recon (themes/plugins) -> WordPress users (twentynineteen, nextgen-gallery, phreakazoid, linkinpark) -> sitemap -> nmap (-p 80,8080) -> HTTP headers (Apache/2.4.7, JSESSIONID) -> flags
```

**Learning chain:** Preparación → conceptos → robots.txt → gobuster → detección de tecnologías → reconocimiento pasivo → WordPress → nmap → cabeceras HTTP → inventario completo

**Lección:** *La enumeración web combina técnicas activas (gobuster, nmap) y pasivas (robots.txt, Wappalyzer) que, combinadas, construyen un inventario completo del sitio objetivo: directorios, tecnologías, CMS, usuarios y servicios.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595.001 (Active Scanning: Scanning IP Blocks), T1083 (File and Directory Discovery), T1592.002 (Gather Victim Host Information: Software)

**Fuente:** [TryHackMe - Web Enumeration](https://tryhackme.com/room/webenumeration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.