# Lian_Yu

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `lianyu` | [TryHackMe](https://tryhackme.com/room/lianyu) | 01 Level Easy | TryHackMe | GoBuster/CTF, FTP, SSH, credenciales, subdominios, flags | Caja CTF "Lian_Yu" basada en Arrow: enumeración de un puerto elevado, un "ticket" con credenciales y recuperación del user flag y del root flag. |

---

**Contexto:** Lian_Yu hace referencia al arquero "Green Arrow"/Oliver Queen. Es una caja CTF en la que se debe enumerar un servicio con un puerto alto (2100), recuperar un archivo llamado `green_arrow.ticket`, obtener las credenciales (`!#th3h00d`), identificarse como el usuario `shado` y recorrer el sistema para capturar las dos flags de usuario y de root.

> **ES:** Enumeración del servicio de la caja Lian_Yu: puerto 2100, archivo `green_arrow.ticket`, credencial `!#th3h00d`, usuario `shado`, user flag y root flag de la familia Arrow.
> **EN:** Lian_Yu box enumeration: port 2100, `green_arrow.ticket` file, credential `!#th3h00d`, user `shado`, and the Arrow-family user and root flags.

## Solucionario

### Task 1: Flags de Lian_Yu / Lian_Yu flags
**Explicación:** La enumeración inicial se hace tanto por la web (primeros pasos sin respuesta) como pelando el servicio ejecutándose en el puerto 2100. Se encuentra el archivo `green_arrow.ticket` que contiene las credenciales `!#th3h00d`, con las que se inicia sesión como el usuario `shado`. Tras recorrer la caja se capturan el user flag `THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}` y el root flag `THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}`.

```text
1. 1. No answer needed
   2. 2100
   3. green_arrow.ticket
   4. !#th3h00d
   5. shado
   6. THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
   7. THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Empezamos con el escaneo? | `No answer needed` |
| 1 | Puerto donde corre el servicio | `2100` |
| 1 | Archivo de credenciales encontrado | `green_arrow.ticket` |
| 1 | Credenciales de acceso | `!#th3h00d` |
| 1 | Usuario del sistema | `shado` |
| 1 | User flag | `THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}` |
| 1 | Root flag | `THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}` |

---

**Metodología:** Se comenzó con la enumeración del dominio y de la caja: escaneo de puertos y fuzzing web/ctf para localizar el servicio en el puerto 2100. De la respuesta se extrajo el archivo `green_arrow.ticket`, que contenía las credenciales `!#th3h00d`. Se probaron contra el inicio de sesión del sistema y se entró como el usuario `shado`. La escalada/recorrido permitió leer el user flag y, subiendo de privilegios, el root flag.

### Cadena de ataque / Attack Chain

```text
Enumeración web/ctf -> escaneo de puertos -> puerto 2100 -> green_arrow.ticket -> credenciales !#th3h00d -> usuario shado -> user flag -> escalada -> root flag
```

**Learning chain:** recon -> port 2100 -> ticket file -> credentials -> user shado -> user flag -> privilege escalation -> root flag

**Lección:** *Las pistas (cuentas "ticket") y los puertos no estándar son vectores frecuentes de credenciales filtradas en cajas CTF: la enumeración meticulosa convierte un archivo pequeño en acceso total.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1003 (OS Credential Dumping), T1078 (Valid Accounts), T1021 (Remote Services: SSH), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Lian_Yu](https://tryhackme.com/room/lianyu)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.