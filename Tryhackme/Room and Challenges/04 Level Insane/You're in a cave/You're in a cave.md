# You're in a cave

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `inacave` | [TryHackMe](https://tryhackme.com/room/inacave) | 04 Level Insane | TryHackMe | ed / regex / fluidica / flags | Reto de nivel Insane ambientado en una cueva: una expresión regular válida para resolver el primer paso, el nombre de una herramienta, y dos flags finales. |

---

**Contexto:** Sala CTF de nivel Insane ambientada dentro de una cueva. La resolución pasa por construir una expresión regular válida, identificar una herramienta o arma concreta, y atravesar dos tramos finales de túneles que entregan las dos flags de cierre.

> **ES:** Sala CTF de nivel Insane ambientada dentro de una cueva. La resolución pasa por construir una expresión regular válida, identificar una herramienta o arma concreta, y atravesar dos tramos finales de túneles que entregan las dos flags de cierre.

> **EN:** Insane-difficulty CTF room set inside a cave. Solving it involves building a valid regular expression, identifying a specific tool or weapon, and traversing two final tunnel stretches that deliver the two closing flags.

## Solucionario

### Task 1: Respuestas del laboratorio / Lab answers

**Explicación:**
Lista completa de respuestas de la sala tal como se recoge en la nota original, sin modificar:

1. 1. ^ed[h#f]{3}[123]{1,2}xf[!@#*]$
   2. bone-breaking-war-hammer
   3. THM{no_wall_can_stop_me}
   4. THM{digging_down_then_digging_up}

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | 1.1 | `^ed[h#f]{3}[123]{1,2}xf[!@#*]$` |
| 2 | 1.2 | `bone-breaking-war-hammer` |
| 3 | 1.3 | `THM{no_wall_can_stop_me}` |
| 4 | 1.4 | `THM{digging_down_then_digging_up}` |

---

**Metodología:**
1. **Entrada a la cueva:** probar la expresión regular `^ed[h#f]{3}[123]{1,2}xf[!@#*]$` como credencial o llave de acceso.
2. **Herramienta interior:** identificar `bone-breaking-war-hammer` como el objeto/habilidad requerido en la cueva.
3. **Avance por túneles:** superar los tramos de pared y los tramos de excavación para capturar las dos flags.

### Cadena de ataque / Attack Chain

1. Regex de entrada → `^ed[h#f]{3}[123]{1,2}xf[!@#*]$`.
2. Herramienta → `bone-breaking-war-hammer`.
3. Flag 1 → `THM{no_wall_can_stop_me}`.
4. Flag 2 → `THM{digging_down_then_digging_up}`.

**Learning chain:** regex → herramienta → pared (flag 1) → excavación (flag 2).

**Lección:** *Los retos con expresión regular exigen precisión byte a byte: un patrón como `[123]{1,2}` acepta variantes dentro de la clase, así que iterar sobre el rango de caracteres válidos es más rápido que adivinar el valor exacto.*

**MITRE ATT&CK:** N/A (reto de lógica/CTF sin infraestructura ofensiva documentada)

**Fuente:** [TryHackMe - You're in a cave](https://tryhackme.com/room/inacave)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.