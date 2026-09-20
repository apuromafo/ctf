# Madeye's Castle

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | madeyescastle | https://tryhackme.com/room/madeyescastle | 02 Level Medium | TryHackMe | Enumeración web, warp, comandos restringidos, flags | Obtención de tres flags mediante exploración del entorno del reto |

---

**Contexto:** **Madeye's Castle** es una sala CTF en la que el jugador explora el castillo de Madeye a través de una interfaz con comandos restringidos, descubriendo referencias a los personajes de Harry Potter (el niño que vivió, Pico -pitch-, y la marca de cada hora) y capturando tres flags a lo largo del recorrido.

## Solucionario

### Task 1: Captura de flags / Flag Hunt
**Explicación:**

Se explora el entorno del castillo interactuando con la interfaz y sus comandos, y se capturan las tres flags del reto.

1. `RME{th3-b0Y-wHo-l1v3d-f409da6f55037fdc}`
2. `RME{p1c0-iZ-oLd-sk00l-nANo-64e977c63cb574e6}`
3. `RME{M@rK-3veRy-hOur-0135d3f8ab9fd5bf}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Primera flag de Madeye's Castle | `RME{th3-b0Y-wHo-l1v3d-f409da6f55037fdc}` |
| 1.2 | Segunda flag de Madeye's Castle | `RME{p1c0-iZ-oLd-sk00l-nANo-64e977c63cb574e6}` |
| 1.3 | Tercera flag de Madeye's Castle | `RME{M@rK-3veRy-hOur-0135d3f8ab9fd5bf}` |

---

**Metodología:** Exploración iterativa de la interfaz de la sala: enumeración de comandos disponibles, navegación por el entorno del castillo, correlación de las pistas temáticas y captura de las tres flags al completar cada etapa.

**Learning chain:** Reconocimiento del entorno → interacción con la interfaz → primera flag → segunda flag → tercera flag.

**Lección:** *En un CTF con interfaz restringida, la enumeración paciente de comandos y la correlación de las pistas del escenario son más rentables que forzar el sistema.*

**MITRE ATT&CK:** T1083 File and Directory Discovery · T1059 Command and Scripting Interpreter · T1082 System Information Discovery.

**Fuente:** [TryHackMe - Madeye's Castle](https://tryhackme.com/room/madeyescastle)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.