# File Inclusion, Path Traversal

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Web / LFI y Path Traversal | fileinclusionpathtraversal | https://tryhackme.com/room/fileinclusionpathtraversal | 02 Level Medium | TryHackMe | PHP include, path traversal, wrappers, Log Poisoning | Lectura de archivos, RCE y robo de flag mediante inclusión de archivos |

---

**Contexto:** **File Inclusion, Path Traversal** (room `filepathtraversal`) profundiza en las variantes de inclusión de archivos en aplicaciones PHP. Se distinguen dos estilos de pathing (**Relative Pathing** y **Absolute Pathing**), los **PHP Wrappers** que permiten leer código fuente o incluso ejecutar comandos, y técnicas de **Log Poisoning** para componer un webshell dentro de un log (como el de Apache) que luego se incluye para ejecutar comandos arbitrarios. La resolución culmina con la obtención de la flag mediante la cadena de inclusión.

## Solucionario

### Task 1: Introduction
**Explicación:**

Introducción a las vulnerabilidades de inclusión de archivos y traversal de rutas. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 2: Deploy the VM
**Explicación:**

Se despliega la VM del laboratorio. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 3: Path Traversal
**Explicación:**

Cuando el prefijo/directorio impide el acceso directo a `/etc/passwd`, se emplea el pathing relativo con `../` para subir directorios hasta la raíz. Se distinguen **Relative Pathing** (rutas relativas con `../`) y **Absolute Pathing** (rutas absolutas como `/etc/passwd`).

Respuestas del lab (contenido original):

```
1. Relative Pathing
2. Absolute Pathing
```

### Task 4: PHP Wrappers
**Explicación:**

Los **PHP wrappers** (como `php://filter`) son streams integrados en PHP que permiten manipular la entrada/salida de datos; a menudo sirven para leer código fuente en base64 o, combinados, alcanzar ejecución de código. La respuesta de la sala es el propio concepto.

**Respuesta:** `PHP Wrappers`

### Task 5: LFI vía wrappers (lectura de código fuente)
**Explicación:**

Ejercicio con los wrappers `php://filter/convert.base64-encode/resource=...` para leer el código fuente de la aplicación y entender la inclusión. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 6: RCE con wrappers
**Explicación:**

Manipulación de los datos de entrada mediante el wrapper `data://` para alcanzar ejecución remota de comandos. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 7: Log Poisoning
**Explicación:**

El **Log Poisoning** consiste en inyectar código PHP en un archivo de log (por ejemplo, en la cabecera `User-Agent` de una petición a Apache) y después incluir ese log vía LFI para que el código se ejecute. El concepto que define esta técnica es `Log Poisoning`.

**Respuesta:** `Log Poisoning`

### Task 8: Flag final
**Explicación:**

Se encadena la inclusión (path traversal / wrappers / log poisoning) para ejecutar comandos en el servidor y recuperar la flag final del laboratorio.

**Respuesta:** `THM{fl4g_cd3c67e5079de2700af6cea0a405f9cc}`

### Task 9: Conclusion
**Explicación:**

Cierre y repaso de la sala. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 (Introduction) | `No answer needed` |
| 2 | Task 2 (Deploy the VM) | `No answer needed` |
| 3 | ¿Qué pathing se usa cuando hay prefijo de directorio? | `Relative Pathing` |
| 4 | ¿Qué estilo de pathing es definir la ruta absoluta? | `Absolute Pathing` |
| 5 | ¿Qué permiten leer los wrappers de PHP? | `PHP Wrappers` |
| 6 | Lectura de código fuente vía wrapper | `No answer needed` |
| 7 | RCE mediante wrapper | `No answer needed` |
| 8 | ¿Qué técnica inyecta código en logs para incluir y ejecutar? | `Log Poisoning` |
| 9 | Flag final de la sala | `THM{fl4g_cd3c67e5079de2700af6cea0a405f9cc}` |
| 10 | Conclusion | `No answer needed` |

---

**Metodología:** Reconocimiento de parámetros PHP vulnerables, prueba de path traversal relativo y absoluto, uso de PHP wrappers (`php://filter`, `data://`) para lectura de código y RCE, e inyección de webshell en logs (Log Poisoning) mediante cabeceras HTTP para ejecutar comandos.

**Learning chain:** Introducción → Deploy → Path Traversal → PHP Wrappers → LFI por wrappers → RCE con wrappers → Log Poisoning → Flag → Conclusion.

**Lección:** *La inclusión de archivos no solo lee ficheros: combinada con wrappers PHP y el envenenamiento de logs convierte cualquier entrada reflejada en ejecución remota de código, multiplicando el impacto de un simple `?file=`.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1005 Data from Local System · T1059 Command and Scripting Interpreter · T1505.003 Server Software Component: Web Shell.

**Fuente:** [TryHackMe - File Inclusion, Path Traversal](https://tryhackme.com/room/fileinclusionpathtraversal)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.