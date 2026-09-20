# Looking Glass

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | lookingglass | https://tryhackme.com/room/lookingglass | 02 Level Medium | TryHackMe | Enumeración, servicio SSH, comandos limitados, ingeniería inversa de prompts | Obtención de flags en un CTF guiado por interface con comandos restringidos |

---

**Contexto:** **Looking Glass** es una sala CTF en la que el jugador interactúa con una interfaz que restringe los comandos y obliga a descubrir caminos alternativos para mover los sufijos de texto (warp) y obtener las dos flags de la sala. Se trata de un ejercicio de ingeniería inversa sobre cómo interactuar con un sistema que solo acepta comandos específicos.

## Solucionario

### Task 1: Primera flag / First Flag
**Explicación:**

Mediante la exploración del entorno y la manipulación de la interfaz (envío de texto a través del warp y uso de los comandos permitidos) se consigue la primera flag de la sala.

1. `thm{65d3710e9d75d5f346d2bac669119a23}`

### Task 2: Segunda flag / Second Flag
**Explicación:**

Se repite el proceso con la variante de salida de la interfaz para descubrir la segunda flag, cerrando la sala.

1. `thm{bc2337b6f97d057b01da718ced6ead3f}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primera flag de la sala Looking Glass | `thm{65d3710e9d75d5f346d2bac669119a23}` |
| 2 | Segunda flag de la sala Looking Glass | `thm{bc2337b6f97d057b01da718ced6ead3f}` |

---

**Metodología:** Interacción iterativa con la interfaz de la sala: enumeración de los comandos restringidos disponibles, manipulación de los parámetros del warp (texto y direcciones) y cierre del ejercicio con la captura de ambas flags.

**Learning chain:** Reconocimiento de la interfaz → identificación de comandos disponibles → manipulación de warp → primera flag → variante de salida → segunda flag.

**Lección:** *Cuando un sistema ofrece una interfaz restringida, la enumeración de sus comandos y la comprensión de cómo procesa la entrada son la clave para forzar el comportamiento deseado.*

**MITRE ATT&CK:** T1082 System Information Discovery · T1083 File and Directory Discovery · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Looking Glass](https://tryhackme.com/room/lookingglass)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.