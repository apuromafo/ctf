# Revenge

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Boot2Root Linux | revenge | https://tryhackme.com/room/revenge | 02 Level Medium | TryHackMe | Enumeración web, acceso inicial, escalada de privilegios, tres flags | Compromiso total de la máquina (tres flags) |

> **Objeto:** Comprometer la máquina objetivo aplicando una vía de ataque controlada: conseguir el acceso inicial, escalar privilegios y capturar las tres flags del laboratorio que completan la cadena de ataque.

---

**Contexto:** La sala **Revenge** es un CTF boot2root en el que el jugador debe recorrer una cadena de ataque completa. La resolución comienza con la enumeración de la máquina y de sus servicios, continúa con el acceso inicial (break in), avanza hacia el primer hito (*almost there*) y termina con la consecución del objetivo final (*mission accomplished*). Las tres flags del laboratorio se corresponden con esos tres hitos del compromiso.

## Solucionario

### Task 1: Preparación / Preparation
**Explicación:**

Primera parte del laboratorio: instrucciones y montaje, sin respuesta obligatoria.

1. `No answer needed`

### Task 2: Cadena de flags / Flag chain
**Explicación:**

Las tres flags corresponden a los hitos de la cadena de ataque: el acceso inicial (*break-in*), el progreso intermedio (*almost there*) y la consecución del objetivo (*mission accomplished*).

1. `thm{br3ak1ng_4nd_3nt3r1ng}`
2. `thm{4lm0st_th3re}`
3. `thm{m1ss10n_acc0mpl1sh3d}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación | `No answer needed` |
| 2 | Flag del acceso inicial | `thm{br3ak1ng_4nd_3nt3r1ng}` |
| 3 | Flag de progreso intermedio | `thm{4lm0st_th3re}` |
| 4 | Flag final | `thm{m1ss10n_acc0mpl1sh3d}` |

---

**Metodología:** Enumeración de la máquina y sus servicios, obtención del acceso inicial, escalada de privilegios y captura secuencial de las tres flags que marcan los hitos del compromiso.

**Learning chain:** Reconocimiento → acceso inicial (break in) → progreso intermedio (almost there) → objetivo final (mission accomplished).

**Lección:** *Una cadena de ataque se completa encadenando pasos verificables: cada flag intermedia confirma que el estado del compromiso permite abordar la siguiente fase.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1068 Exploitation for Privilege Escalation · T1005 Data from Local System.

**Fuente:** [TryHackMe - Revenge](https://tryhackme.com/room/revenge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.