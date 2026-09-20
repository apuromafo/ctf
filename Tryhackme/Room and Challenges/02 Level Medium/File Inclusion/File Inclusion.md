# File Inclusion

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Web / LFI-RFI y Path Traversal | fileinclusion | https://tryhackme.com/room/fileinclusion | 02 Level Medium | TryHackMe | PHP, file_get_contents, include, LFI/RFI | Lectura de archivos remotos/locales y RCE mediante inclusiones PHP |

---

**Contexto:** **File Inclusion** (room `fileinc`) introduce las vulnerabilidades de inclusión de archivos: **Path Traversal**, **Local File Inclusion (LFI)** y **Remote File Inclusion (RFI)** en PHP. Se explota `file_get_contents` e `include` a través de parámetros tipo `?file=`, se saltan restricciones con `../../` y null bytes, se identifican directorios de inclusión, se exploran wrappers PHP y cookies, y en el challenge final se consigue **RCE** por RFI. El laboratorio usa una VM y devuelve las flags de `/etc/flag1`, `/etc/flag2`, `/etc/flag3`.

## Solucionario

### Task 1: Introduction
**Explicación:**

Introducción a las vulnerabilidades de file inclusion (LFI, RFI y directory traversal). No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 2: Deploy the VM
**Explicación:**

Se despliega la VM y se espera a que el servidor web arranque antes de continuar. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 3: Path Traversal
**Explicación:**

El path traversal (directory traversal) ocurre cuando la entrada del usuario se pasa a una función como `file_get_contents`. La función que causa path traversal en PHP es **file_get_contents**. El ataque típico usa `../` para subir de directorio y leer archivos fuera de la raíz de la aplicación.

**Respuesta:** `file_get_contents`

### Task 4: Local File Inclusion - LFI (Labs 1-2)
**Explicación:**

En el Lab #1, introduciendo `/etc/passwd` en el campo de inclusión, la request URI resultante es `?file=/etc/passwd`. En el Lab #2, provocando un error de PHP con entrada inválida se revela el contenido de la función include, cuyo directorio especificado es **includes**.

Respuestas del lab (contenido original):

```
1. /lab1.php?file=/etc/passwd
2. includes
```

### Task 5: Local File Inclusion - LFI #2 (Labs 3-4-6)
**Explicación:**

En el Lab #3 la aplicación añade automáticamente `.php`; se añaden `../` para subir hasta `/etc` y se termina con el null byte `%00`, obteniendo `?file=../../../../etc/passwd`. La función que causa directory traversal en el Lab #4 es **file_get_contents**. En el Lab #6 el directorio requerido en el campo de entrada es **THM-profile**, y leyendo `/etc/os-release` el valor de **VERSION_ID** es **12.04**.

Respuestas del lab (contenido original):

```
1. /lab3.php?file=../../../../etc/passwd
2. file_get_contents
3. THM-profile
4. 12.04
```

### Task 6: Remote File Inclusion - RFI
**Explicación:**

En la parte de RFI se investiga cómo lograr Remote Command Execution (RCE) con inclusión remota. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 7: Remediation
**Explicación:**

Sección sobre cómo remediar las vulnerabilidades de inclusión. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 8: Challenge
**Explicación:**

En el challenge final se capturan las flags manipulando parámetros GET (input), cookies y POST del playground PHP, y se consigue RCE por RFI ejecutando `hostname` en `/playground.php`.

Respuestas del lab (contenido original):

```
1. F1x3d-iNpu7-f0rrn
2. c00k13_i5_yuMmy1
3. P0st_1s_w0rk1in9
4. lfi-vm-thm-f8c5b1a78692
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 (Introduction) | `No answer needed` |
| 2 | Task 2 (Deploy the VM) | `No answer needed` |
| 3 | ¿Qué función provoca path traversal en PHP? | `file_get_contents` |
| 4 | URI de la request para leer /etc/passwd en Lab #1 | `/lab1.php?file=/etc/passwd` |
| 5 | ¿Qué directorio especifica la función include en Lab #2? | `includes` |
| 6 | Request para leer /etc/passwd en Lab #3 | `/lab3.php?file=../../../../etc/passwd` |
| 7 | ¿Qué función causa directory traversal en Lab #4? | `file_get_contents` |
| 8 | ¿Qué directorio debe ir en el input del Lab #6? | `THM-profile` |
| 9 | ¿Cuál es el valor de VERSION_ID en /etc/os-release? | `12.04` |
| 10 | Investigación sobre RCE vía RFI | `No answer needed` |
| 11 | ¿Listo para los challenges? | `No answer needed` |
| 12 | Flag 1 (inclusión por input/GET en el challenge) | `F1x3d-iNpu7-f0rrn` |
| 13 | Flag 2 (inclusión vía cookie) | `c00k13_i5_yuMmy1` |
| 14 | Flag 3 (inclusión vía POST) | `P0st_1s_w0rk1in9` |
| 15 | Salida del comando hostname (RCE por RFI) | `lfi-vm-thm-f8c5b1a78692` |

---

**Metodología:** Enumeración de parámetros PHP vulnerables, explotación de path traversal con `../` y null bytes (`%00`), abuso de `include`/`file_get_contents`, lectura de archivos sensibles (`/etc/passwd`, `/etc/os-release`), manipulación de cookies/POST y ejecución remota de comandos por RFI.

**Learning chain:** Introducción → Deploy → Path Traversal → LFI (labs 1-2) → LFI #2 (labs 3-4-6) → RFI → Remediation → Challenge.

**Lección:** *Las funciones `include` y `file_get_contents` con entrada no validada convierten parámetros GET/cookies/POST en lecturas arbitrarias de archivos y, extendiendo con RFI, en ejecución remota de comandos; validar y restringir rutas es la única mitigación real.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1005 Data from Local System · T1027.001 Obfuscated Files or Information · T1059 Command and Scripting Interpreter · T1213 Data from Information Repositories.

**Fuente:** [TryHackMe - File Inclusion](https://tryhackme.com/room/fileinclusion)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.