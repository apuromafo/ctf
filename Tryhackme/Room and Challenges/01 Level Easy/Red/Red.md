# Red

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `red` | https://tryhackme.com/room/red | 01 Level Easy | TryHackMe | CTF / red vs blue / flags / captura de banderas | Reto CTF en el que el equipo Red se enfrenta al equipo Blue en una partida guiada para capturar tres flags consecutivas. |

---

**Contexto:** Sala tipo CTF donde un atacante (Red) se enfrenta a un defensor (Blue) en una partida guiada. A lo largo del reto hay que comprometer el sistema desplegado y superar la defensa del Blue para ir capturando cada bandera enlazada a la siguiente pregunta.

> **ES:** "Red" — desafío CTF de captura de banderas entre el equipo Red y el equipo Blue.
> **EN:** "Red" — capture-the-flag challenge between the Red team and the Blue team.

## Solucionario

### Task 1: Captura las flags / Capture the flags

**Explicación:** El reto se resuelve superando los obstáculos de la partida para obtener tres flags consecutivas que demuestran el avance sobre el equipo Blue. La última interacción cierra la partida y no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag de la partida? / What is the first flag of the match? | `THM{Is_thAt_all_y0u_can_d0_blU3?}` |
| 2 | ¿Cuál es la segunda flag de la partida? / What is the second flag of the match? | `THM{Y0u_won't_mak3_IT_furTH3r_th@n_th1S}` |
| 3 | ¿Cuál es la tercera flag de la partida? / What is the third flag of the match? | `THM{Go0d_Gam3_Blu3_GG}` |
| 4 | Interacción final de la partida. / Final interaction of the match. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag de la partida? / What is the first flag of the match? | `THM{Is_thAt_all_y0u_can_d0_blU3?}` |
| 2 | ¿Cuál es la segunda flag de la partida? / What is the second flag of the match? | `THM{Y0u_won't_mak3_IT_furTH3r_th@n_th1S}` |
| 3 | ¿Cuál es la tercera flag de la partida? / What is the third flag of the match? | `THM{Go0d_Gam3_Blu3_GG}` |
| 4 | Interacción final de la partida. / Final interaction of the match. | `No answer needed` |

---

**Metodología:** Desplegar el entorno de la partida Red vs Blue, comprometer el sistema objetivo y superar las defensas del equipo Blue para ir capturando cada flag de forma secuencial hasta completar la partida.

### Cadena de ataque / Attack Chain

```text
Despliegue del objetivo -> Compromiso del sistema -> Superar defensa (Blue) -> Flag 1 -> Flag 2 -> Flag 3 -> Fin de partida
```

**Learning chain:** Explotación del sistema de la partida -> captura de flags secuenciales (Red vs Blue) -> cierre de partida.

**Lección:** *Un CTF encadenado obliga a resolver cada etapa sin romper el entorno: cada flag conseguida habilita la siguiente y la defensa del equipo Blue puede adaptarse en tiempo real.*

**MITRE ATT&CK:** N/A (reto CTF Red vs Blue; referencia genérica T1190 - Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Red](https://tryhackme.com/room/red)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.