# Walking An Application

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `walkinganapplication` | https://tryhackme.com/room/walkinganapplication | 01 Level Easy | TryHackMe | View-source, herramientas de desarrollo, comentarios HTML, pestañas Network/Storage, AJAX | Inspección manual de una aplicación web con el navegador para descubrir flags ocultas |

---

**Contexto:** Sala práctica que enseña a inspeccionar una aplicación web usando el navegador: ver el código fuente de las páginas, usar la consola y las herramientas de desarrollo (elementos, red, almacenamiento) y analizar las peticiones AJAX para encontrar contenido oculto y flags. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Usa el navegador (view-source, devtools y peticiones AJAX) para inspeccionar la aplicación y descubrir las flags ocultas.
> **EN:** Use the browser (view-source, devtools and AJAX requests) to inspect the application and discover the hidden flags.

## Solucionario

### Task 1: Preparación / Preparation

**Explicación:** Se despliega la máquina y se accede a la aplicación web desde el navegador. No requiere respuesta.

```
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Vista de la página / Viewing the Page

**Explicación:** Se aplica la técnica de explorar manualmente el sitio con el navegador antes de pasar a herramientas más avanzadas. No requiere respuesta.

```
2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 3: Comentarios HTML / Viewing the Page Source

**Explicación:** Se revisa el código fuente de la página y se encuentran flags ocultas en los comentarios HTML: `THM{HTML_COMMENTS_ARE_DANGEROUS}`, el cambio hacia `THM{NOT_A_SECRET_ANYMORE}`, los permisos incorrectos de un directorio `THM{INVALID_DIRECTORY_PERMISSIONS}` y la falta de actualizaciones `THM{KEEP_YOUR_SOFTWARE_UPDATED}`.

```
3. 1. THM{HTML_COMMENTS_ARE_DANGEROUS}
   2. THM{NOT_A_SECRET_ANYMORE}
   3. THM{INVALID_DIRECTORY_PERMISSIONS}
   4. THM{KEEP_YOUR_SOFTWARE_UPDATED}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{HTML_COMMENTS_ARE_DANGEROUS}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{NOT_A_SECRET_ANYMORE}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{INVALID_DIRECTORY_PERMISSIONS}` |
| 4 | *(Pregunta 4 no especificada en el original)* | `THM{KEEP_YOUR_SOFTWARE_UPDATED}` |

### Task 4: Herramientas de desarrollo / Developer Tools

**Explicación:** Con las herramientas de desarrollo se inspeccionan los elementos y el contenido oculto de la página, revelando la flag `THM{NOT_SO_HIDDEN}`.

```
4. THM{NOT_SO_HIDDEN}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{NOT_SO_HIDDEN}` |

### Task 5: Auditoría de la aplicación / Auditing the Application

**Explicación:** Se audita la aplicación buscando funcionalidades no visibles, obteniendo la flag `THM{CATCH_ME_IF_YOU_CAN}`.

```
5. THM{CATCH_ME_IF_YOU_CAN}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{CATCH_ME_IF_YOU_CAN}` |

### Task 6: AJAX / AJAX

**Explicación:** Se analizan las peticiones AJAX que realiza la página en segundo plano, encontrando la flag `THM{GOT_AJAX_FLAG}`.

```
6. THM{GOT_AJAX_FLAG}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{GOT_AJAX_FLAG}` |

---

**Metodología:** Acceso a la aplicación → vista del código fuente → comentarios HTML → elementos ocultos con devtools → auditoría manual → análisis de peticiones AJAX → obtención de todas las flags.

### Cadena de ataque / Attack Chain

```text
Navegador -> view-source -> comentarios HTML (flags) -> devtools (elemento oculto) -> auditoría de rutas (CATCH_ME) -> peticiones AJAX (GOT_AJAX_FLAG) -> flags completas
```

**Learning chain:** Navegación → código fuente → comentarios → devtools → contenido oculto → AJAX → extracción de flags

**Lección:** *Gran parte de la información sensible de una aplicación web se descubre sin herramientas ofensivas: basta revisar el código fuente, los comentarios HTML, el contenido oculto y el tráfico AJAX desde el propio navegador.*

**MITRE ATT&CK:** T1592.002 (Gather Victim Host Information: Software), T1083 (File and Directory Discovery), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Walking An Application](https://tryhackme.com/room/walkinganapplication)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.