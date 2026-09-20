# Minotaur's Labyrinth

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | minotaurslabyrinth | https://tryhackme.com/room/minotaurslabyrinth | 02 Level Medium | TryHackMe | FTP, bases de datos, cuentas de usuario, root | Compromiso total de la máquina (4 flags) |

---

**Contexto:** La sala **Minotaur's Labyrinth** es un CTF en varias fases, como atravesar un laberinto. La primera flag se obtiene a través del servicio **FTP**, la segunda accediendo a la **base de datos**, la tercera localizando las credenciales o secretos de un **usuario** y la cuarta escalando privilegios hasta **root**. Cada fase del laberinto entrega una flag que acredita el avance.

## Solucionario

### Task 1: Capturar las flags
**Explicación:**

Resolviendo el laberinto se obtienen las cuatro flags: la primera la entrega el reto en la fase **FTP** (`fl4g{tHa75_TH3_$7Ar7_ftPFLA9}`), la segunda aparece en la fase de la **base de datos** (`fla6{7H@Ts_tHe_Dat48as3_F149}`), la tercera corresponde al **usuario** secreto del sistema (`fla9{5upeR_secr37_uSEr_flaG}`) y la cuarta confirma el compromiso total como **root** (`fL4G{YoU_R0OT3d_1T_coN9ra7$}`).

1. `fl4g{tHa75_TH3_$7Ar7_ftPFLA9}`
2. `fla6{7H@Ts_tHe_Dat48as3_F149}`
3. `fla9{5upeR_secr37_uSEr_flaG}`
4. `fL4G{YoU_R0OT3d_1T_coN9ra7$}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la fase FTP | `fl4g{tHa75_TH3_$7Ar7_ftPFLA9}` |
| 2 | Flag de la fase base de datos | `fla6{7H@Ts_tHe_Dat48as3_F149}` |
| 3 | Flag del usuario | `fla9{5upeR_secr37_uSEr_flaG}` |
| 4 | Flag de root | `fL4G{YoU_R0OT3d_1T_coN9ra7$}` |

---

**Metodología:** Enumeración multi-servicio → acceso por FTP → explotación de la base de datos → enumeración de usuarios/credenciales → escalada de privilegios a root → captura secuencial de las 4 flags.

**Learning chain:** FTP → flag 1 → base de datos → flag 2 → usuario/secretos → flag 3 → escalada → root → flag 4.

**Lección:** *Cada servicio del laberinto es una etapa: avanzar requiere explotar FTP, moverte por la base de datos, pivotar por cuentas y, finalmente, escalar a root para cerrar el compromiso total.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Minotaur's Labyrinth](https://tryhackme.com/room/minotaurslabyrinth)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.