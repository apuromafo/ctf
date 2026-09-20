# Operating System Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `operatingsystemsecurity` | [TryHackMe](https://tryhackme.com/room/operatingsystemsecurity) | `01 Level Easy` | THM | hardening, contraseñas débiles, cuentas | Seguridad del sistema operativo |

> **Objeto:** Practicar conceptos de seguridad del sistema operativo: identificar software instalado, detectar contraseñas débiles y acceder a cuentas privilegiadas hasta obtener el flag final `THM{YouGotRoot}`.

---

**Contexto:** Sala centrada en la seguridad del sistema operativo: se inspecciona la máquina para descubrir el software instalado (Thunderbird), se identifican credenciales débiles o por defecto en el sistema (abc123, happyHack!NG) y se consigue acceso privilegiado con la bandera final `THM{YouGotRoot}`.

> **ES:** Sala centrada en la seguridad del sistema operativo: se inspecciona la máquina para descubrir el software instalado (Thunderbird), se identifican credenciales débiles o por defecto en el sistema (abc123, happyHack!NG) y se consigue acceso privilegiado con la bandera final `THM{YouGotRoot}`.

> **EN:** Room focused on operating system security: the machine is inspected to discover the installed software (Thunderbird), weak or default credentials on the system are identified (abc123, happyHack!NG) and privileged access is achieved with the final flag `THM{YouGotRoot}`.

## Solucionario

### Task 1: Operating System Security / Operating System Security

**Explicación:** La tarea recoge las respuestas del reto de seguridad del sistema operativo. El contenido original, conservado íntegramente, es el siguiente:

1. Thunderbird
2. LearnM00r
3. 1. abc123
   2. happyHack!NG
   3. THM{YouGotRoot}

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué cliente de correo se encuentra instalado? | `Thunderbird` |
| 2 | Respuesta del apartado 2 del reto | `LearnM00r` |
| 3.1 | Credencial débil o por defecto 1 | `abc123` |
| 3.2 | Credencial débil o por defecto 2 | `happyHack!NG` |
| 3.3 | Flag final del reto | `THM{YouGotRoot}` |

---

**Metodología:** 1) Inventariar el software instalado en el sistema operativo y responder el apartado 1 (Thunderbird). 2) Localizar las credenciales débiles o por defecto almacenadas (LearnM00r, abc123, happyHack!NG). 3) Utilizar las credenciales para obtener acceso privilegiado y extraer la bandera final `THM{YouGotRoot}`.

### Cadena de ataque / Attack Chain

1. Inventario de software del sistema operativo → `Thunderbird`.
2. Descubrimiento de credenciales débiles o por defecto (`LearnM00r`, `abc123`, `happyHack!NG`).
3. Acceso privilegiado con las credenciales encontradas.
4. Extracción del flag final → `THM{YouGotRoot}`.

**Learning chain:** inventario de software → credenciales débiles / por defecto → acceso privilegiado → root flag

**Lección:** *Las contraseñas débiles y el software desactualizado son vectores habituales de compromiso: la seguridad del sistema operativo se sustenta en el hardening, las actualizaciones y una política de credenciales estricta.*

**MITRE ATT&CK:** T1078 - Valid Accounts, T1552.001 - Unsecured Credentials: Credentials In Files, T1021 - Remote Services

**Fuente:** [TryHackMe - Operating System Security](https://tryhackme.com/room/operatingsystemsecurity)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.