# Startup

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `startup` | [TryHackMe](https://tryhackme.com/room/startup) | 01 Level Easy | TryHackMe | FTP, SSH, Hydra, escalada de privilegios en Linux | Compromiso total del host Linux mediante acceso FTP/SSH y escalada de privilegios |

---

**Contexto:** Sala de explotación de una máquina Linux que expone servicios FTP, SSH y web. La enumeración del FTP anónimo y el acceso por SSH permiten obtener el usuario `love` y capturar las flags de usuario y de root de la sala. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Máquina Linux con FTP, SSH y web. Se obtiene el usuario `love` explotando el FTP, se accede por SSH y se capturan el user flag `THM{03ce3d619b80ccbfb3b7fc81e46c0e79}` y el root flag `THM{f963aaa6a430f210222158ae15c3d76d}` tras la escalada de privilegios.
> **EN:** A Linux box exposing FTP, SSH and web. User `love` is obtained through the FTP, SSH access is gained and the user flag `THM{03ce3d619b80ccbfb3b7fc81e46c0e79}` and the root flag `THM{f963aaa6a430f210222158ae15c3d76d}` are captured after privilege escalation.

## Solucionario

### Task 1: Explotación / Exploitation

**Explicación:** Se obtiene el nombre de usuario descubierto a través del FTP y se capturan la flag de usuario y la flag de root de la sala. Todo el contenido original se conserva verbatim:

1. 1. love
   2. THM{03ce3d619b80ccbfb3b7fc81e46c0e79}
   3. THM{f963aaa6a430f210222158ae15c3d76d}

### Task 2: Cierre de la sala / Room Wrap-up

**Explicación:** Pregunta complementaria de cierre de la sala, sin respuesta que introducir. Todo el contenido original se conserva verbatim:

2. No answer needed

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre de usuario del FTP / FTP username | `love` |
| 2 | Flag de usuario / User flag | `THM{03ce3d619b80ccbfb3b7fc81e46c0e79}` |
| 3 | Flag de root / Root flag | `THM{f963aaa6a430f210222158ae15c3d76d}` |
| 4 | Pregunta informativa de cierre / Closing informational question | `No answer needed` |

---

**Metodología:** Enumeración de la máquina → acceso FTP anónimo → obtención del usuario `love` → acceso por SSH → captura del user flag → escalada de privilegios → captura del root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> FTP anónimo -> usuario love -> SSH -> user flag THM{03ce3d619b80ccbfb3b7fc81e46c0e79} -> escalada de privilegios -> root flag THM{f963aaa6a430f210222158ae15c3d76d}
```

**Learning chain:** FTP enumeration --> credential discovery --> SSH access --> user flag --> privilege escalation --> root flag

**Lección:** *Los servicios FTP mal configurados y las credenciales débiles o expuestas permiten obtener acceso inicial y escalar hasta el compromiso total de la máquina.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1021.001 (Remote Services: SSH), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Startup](https://tryhackme.com/room/startup)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.