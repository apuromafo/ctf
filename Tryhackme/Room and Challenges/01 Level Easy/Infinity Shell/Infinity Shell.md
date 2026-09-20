# Infinity Shell

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `infinityshell` | [TryHackMe](https://tryhackme.com/room/infinityshell) | 01 Level Easy | THM | Web shell, upload bypass, command execution | Ejecución de comandos a través de una web shell subida al servidor |

> **Objeto:** Subir una web shell al servidor objetivo y ejecutar comandos para obtener la bandera del reto.

---

**Contexto:** Reto de TryHackMe en el que la aplicación permite subir archivos. Al cargar una web shell (por ejemplo, una variante de "infinity shell") se consigue ejecución de comandos en el servidor y se puede leer la bandera del reto.

> **ES:** Un reto web sencillo donde se sube una web shell para conseguir ejecución de comandos en el servidor y leer la bandera.
> **EN:** A simple web challenge where you upload a web shell to get command execution on the server and read the flag.

## Solucionario

### Task 1: Obtener la bandera / Get the Flag

**Explicación:** Se sube la web shell al servidor objetivo, se invoca pasando un comando y se obtiene la salida que incluye la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera del reto? / What is the flag? | `THM{sup3r_34sy_w3bsh3ll}` |

---

**Metodología:** Se localizó el punto de subida de archivos y se cargó una web shell. Al acceder a ella se ejecutaron comandos en el servidor y se leyó el contenido de la bandera, obteniendo `THM{sup3r_34sy_w3bsh3ll}`.

### Cadena de ataque / Attack Chain

Reconocimiento de la aplicación → localización del formulario de subida → subida de la web shell → invocación con parámetro de comando → ejecución remota de comandos → lectura de la bandera.

**Learning chain:** Reconocimiento web → subida de archivos → web shell → ejecución de comandos → bandera.

**Lección:** *Una subida de archivos sin validación convierte un endpoint inocuo en una puerta de ejecución remota: el control de tipos, contenido y extensiones es obligatorio antes de aceptar cualquier archivo.*

**MITRE ATT&CK:** T1505.003 (Server Software Component: Web Shell), T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1059 (Command and Scripting Interpreter).

**Fuente:** [TryHackMe - Infinity Shell](https://tryhackme.com/room/infinityshell)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.