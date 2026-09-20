# Break Out The Cage

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `breakoutthecage` | [TryHackMe](https://tryhackme.com/room/breakoutthecage) | 01 Level Easy | TryHackMe | brute force, SSH, captura de flags | Compromiso del host mediante credenciales débiles y obtención de las flags del room |

---

**Contexto:** Sala tipo CTF de dificultad fácil en la que se compromete el host de destino y se capturan las flags ocultas, partiendo de credenciales débiles o fáciles de adivinar. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Compromiso inicial / Initial Access

**Explicación:** Se accede al host con credenciales obtenidas o forzadas y se recorre el sistema para localizar y capturar todas las flags requeridas por la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Mydadisghostrideraintthatcoolnocausehesonfirejokes` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{M37AL_0R_P3N_T35T1NG}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{8R1NG_D0WN_7H3_C493_L0N9_L1V3_M3}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Mydadisghostrideraintthatcoolnocausehesonfirejokes` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{M37AL_0R_P3N_T35T1NG}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{8R1NG_D0WN_7H3_C493_L0N9_L1V3_M3}` |

---

**Metodología:** Enumeración del objetivo → acceso con credenciales débiles o fáciles de adivinar → recorrido del sistema → captura de las flags.

### Cadena de ataque / Attack Chain

```text
Enumeración → acceso al host → exploración del sistema → captura de flags
```

**Learning chain:** Acceso con contraseñas fáciles de adivinar → exploración del sistema → captura de banderas

**Lección:** *Las contraseñas largas pero predecibles o basadas en frases comunes no ofrecen seguridad real; son un vector habitual de acceso inicial.*

**MITRE ATT&CK:** T1110 (Brute Force), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Break Out The Cage](https://tryhackme.com/room/breakoutthecage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.