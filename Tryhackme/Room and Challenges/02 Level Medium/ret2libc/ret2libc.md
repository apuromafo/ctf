# ret2libc

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room / Explotación de binarios | ret2libc | https://tryhackme.com/room/ret2libc | 02 Level Medium | TryHackMe | Buffer overflow, ret2libc, rop, .got.plt, setuid | Ejecución de código arbitrario y escalada a root |

> **Objeto:** Explotar una vulnerabilidad de desbordamiento de búfer aplicando la técnica **ret2libc**: analizar los permisos del binario, encontrar direcciones de libc y la tabla `.got.plt`, calcular el offset del overwrite y desviar la ejecución hacia `system("/bin/sh")` para escalar a root y capturar la flag.

---

**Contexto:** La sala **ret2libc** practica la técnica de explotación que redirige la ejecución de un binario vulnerable a funciones de `libc` (como `system`) en lugar de inyectar shellcode en el stack. El flujo del laboratorio pasa por identificar el binario con bit **setuid**, comprobar los permisos (`-rwsrwxr-x`), localizar la dirección base del binario (`0x400000`), calcular el desplazamiento hasta el control de `RIP` (18 bytes), resolver `system` a través de la tabla `.got.plt` y disparar la escalada. La flag final, en formato base64, acredita el compromiso como root.

## Solucionario

### Task 1: Preparación / Preparation
**Explicación:**

Primera parte del laboratorio: puesta en marcha y análisis previo del binario, sin respuesta obligatoria.

1. `No answer needed`

### Task 2: Función de ataque / Attack function
**Explicación:**

Se identifica la primera pregunta sin respuesta y a continuación la función de `libc` que se usará como objetivo de la redirección.

1. `No answer needed`
2. `system`

### Task 3: Técnica general / General technique
**Explicación:**

Lectura teórica de la técnica ret2libc, sin respuesta obligatoria.

1. `No answer needed`

### Task 4: Análisis del binario / Binary analysis
**Explicación:**

Datos obtenidos del análisis del binario: los permisos del ejecutable en el listado (`-rwsrwxr-x 1 root root`), la dirección de carga base (`0x400000`) y el tamaño del offset que permite tomar el control del flujo (18 bytes).

1. `-rwsrwxr-x 1 root root`
2. `0x400000`
3. `18`

### Task 5: Tabla de resolución / Resolution table
**Explicación:**

Se identifica la sección de la tabla de resoluciones dinámicas del binario sobre la que se apoyará la cadena de explotación.

1. `.got.plt`

### Task 6: Bit de privilegios / Privilege bit
**Explicación:**

Se identifica el bit de permisos especial que da al binario la ejecución con privilegios elevados.

1. `setuid`

### Task 7: Flag final / Final flag
**Explicación:**

Una vez conseguida la ejecución de `system("/bin/sh")` y la escalada a root se captura la flag final del laboratorio (codificada en base64 dentro del formato `thm{...}`).

1. `thm{dGhlIG1vc3QgcmFuZG9tIHZhbHVlIHlvdSBjb3VsZCBldmVyIGd1ZXNz}`

### Task 8: Cierre / Wrap-up
**Explicación:**

Última pregunta de confirmación de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación | `No answer needed` |
| 2 | Función de libc (preparación) | `No answer needed` |
| 3 | Función de libc | `system` |
| 4 | Técnica general | `No answer needed` |
| 5 | Permisos del binario | `-rwsrwxr-x 1 root root` |
| 6 | Dirección base | `0x400000` |
| 7 | Offset del overwrite | `18` |
| 8 | Tabla de resolución | `.got.plt` |
| 9 | Bit de privilegios | `setuid` |
| 10 | Flag final | `thm{dGhlIG1vc3QgcmFuZG9tIHZhbHVlIHlvdSBjb3VsZCBldmVyIGd1ZXNz}` |
| 11 | Cierre | `No answer needed` |

---

**Metodología:** Análisis del binario vulnerable (permisos setuid, direcciones y offsets), resolución de las funciones de libc vía la tabla `.got.plt`, construcción del payload ret2libc que redirige el flujo hacia `system("/bin/sh")` y escalada a root para leer la flag.

**Learning chain:** Preparación → análisis del binario (permisos/base/offset) → resolución de `system` por `.got.plt` → desbordamiento ret2libc → shell como root → flag.

**Lección:** *Cuando el stack es no ejecutable, no hay que inyectar código: alcanzar funciones de libc como `system` reutilizando sus direcciones permite obtener una shell sin shellcode propio.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1068 Exploitation for Privilege Escalation · T1078 Valid Accounts.

**Fuente:** [TryHackMe - ret2libc](https://tryhackme.com/room/ret2libc)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.