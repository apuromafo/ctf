# DarkMatter

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `darkmatter` | [TryHackMe](https://tryhackme.com/room/darkmatter) | 01 Level Easy | THM | Node.js, Módulos, Criptografía, Análisis de código | Análisis de módulos de Node.js para recuperar la flag |

> **Objeto:** Analizar los módulos de una aplicación Node.js y aplicar técnicas de inspección/desofuscación para recuperar la flag de la sala.

---

**Contexto:** Sala de ingeniería inversa sobre una aplicación Node.js. El análisis se centra en revisar los módulos incluidos en el paquete, detectar las piezas de criptografía mal implementada y aplicar la transformación correcta para obtener la flag.

> **ES:** Inspecciona los módulos de Node.js, identifica la pieza criptográfica débil y recupera la flag.
> **EN:** Inspect the Node.js modules, identify the weak cryptographic piece and recover the flag.

## Solucionario

### Task 1: Investigación / Investigation
**Explicación:** Análisis de los módulos de la aplicación y de la lógica criptográfica para obtener la flag.

1. THM{d0nt_l34k_y0ur_w34k_m0dulu5}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Flag de la sala | `THM{d0nt_l34k_y0ur_w34k_m0dulu5}` |

---

**Metodología:** Revisión de la estructura del paquete Node.js, inspección de cada módulo, identificación de la función de cifrado/transformación empleada, aplicación inversa de la operación y validación del flag.

### Cadena de ataque / Attack Chain

Paquete Node.js → revisión de módulos → identificación de la lógica criptográfica → transformación inversa → flag.

**Learning chain:** módulos → análisis de código → crypto → decode → flag

*Lección:* Los módulos de Node.js con credenciales débiles o lógica criptográfica improvisada filtran información aunque estén ofuscados.

**MITRE ATT&CK:** TA0002 Execution, TA0006 Credential Access, T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - DarkMatter](https://tryhackme.com/room/darkmatter)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.