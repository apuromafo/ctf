# Snowy ARMageddon

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `armageddon2r` | [TryHackMe](https://tryhackme.com/room/armageddon2r) | 04 Level Insane | TryHackMe | arm / explotación / clave derivada | Reto ARM de nivel Insane: una flag temática y una clave de acceso derivada de la fase de explotación. |

---

**Contexto:** Sala CTF de nivel Insane con temática "ARMageddon", centrada en la explotación de un binario o dispositivo ARM. Se recogen una flag temática y una clave de acceso (con prefijo `2-K@...`) generada durante la fase final del reto.

> **ES:** Sala CTF de nivel Insane con temática "ARMageddon", centrada en la explotación de un binario o dispositivo ARM. Se recogen una flag temática y una clave de acceso (con prefijo `2-K@...`) generada durante la fase final del reto.

> **EN:** Insane-difficulty CTF room with an "ARMageddon" theme, focused on exploiting an ARM binary or device. A thematic flag and an access key (with a `2-K@...` prefix) generated during the final phase of the challenge are collected.

## Solucionario

### Task 1: Respuestas del laboratorio / Lab answers

**Explicación:**
Lista completa de respuestas de la sala tal como se recoge en la nota original, sin modificar:

1. 1. THM{YETI_ON_SCREEN_ELUSIVE_CAMERA_STAR}
   2. 2-K@bWJ5oHFCR8o%whAvK5qw8Sp$5qf!nCqGM3ksaK

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | 1.1 | `THM{YETI_ON_SCREEN_ELUSIVE_CAMERA_STAR}` |
| 2 | 1.2 | `2-K@bWJ5oHFCR8o%whAvK5qw8Sp$5qf!nCqGM3ksaK` |

---

**Metodología:**
1. **Análisis del objetivo ARM:** identificar el binario o firmware y su superficie de explotación.
2. **Explotación/ingeniería inversa:** alcanzar el estado que revela la flag temática y posteriormente la clave de acceso.
3. **Registro de la clave:** conservar la cadena de prefijo `2-K@...` completa, tal como se genera.

### Cadena de ataque / Attack Chain

1. Flag temática → `THM{YETI_ON_SCREEN_ELUSIVE_CAMERA_STAR}`.
2. Clave de acceso final → `2-K@bWJ5oHFCR8o%whAvK5qw8Sp$5qf!nCqGM3ksaK`.

**Learning chain:** explotación ARM → flag temática → clave de acceso final.

**Lección:** *Prefijos como `2-K@` delatan claves de cierre en los retos ARM/hardware: anotar la cadena exacta con su símbolo `%`, `$` y `!` es imprescindible, porque un solo carácter mal copiado invalida la respuesta.*

**MITRE ATT&CK:** N/A (reto de explotación local/ARM sin cadena de infraestructura documentada)

**Fuente:** [TryHackMe - Snowy ARMageddon](https://tryhackme.com/room/armageddon2r)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.