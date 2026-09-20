# Spring

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | spring | https://tryhackme.com/room/spring | 03 Level Hard | TryHackMe | Repositorio .git expuesto, reutilización de contraseñas, SSH | Alto |

---

**Contexto:**
> **ES:** Sala CTF que explota la exposición de un repositorio `.git` en Internet, la reutilización de credenciales y la tolerancia de sshd a entradas basura. Las tres banderas reflejan cada vector del reto.
> **EN:** CTF room that exploits an exposed `.git` repository on the internet, credential reuse and sshd's tolerance of junk input. The three flags reflect each vector of the challenge.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. 1. THM{dont_expose_.git_to_internet}
   2. THM{this_is_still_password_reuse}
   3. THM{sshd_does_not_mind_the_junk}
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{dont_expose_.git_to_internet}` |
| 1.2 | `THM{this_is_still_password_reuse}` |
| 1.3 | `THM{sshd_does_not_mind_the_junk}` |

---

**Metodología:**
1. Detección del repositorio `.git` expuesto y recuperación de su contenido (código, configuraciones e historia).
2. Obtención de la primera flag: `THM{dont_expose_.git_to_internet}`.
3. Reutilización de credenciales halladas en el material filtrado para acceder a otro sistema.
4. Obtención de la segunda flag: `THM{this_is_still_password_reuse}`.
5. Uso del acceso SSH, admitiendo entradas basura en la autenticación, para obtener la tercera flag: `THM{sshd_does_not_mind_the_junk}`.

### Cadena de ataque / Attack Chain
```text
.git expuesto -> Recuperación de credenciales -> Flag 1 -> Reutilización de contraseña -> Flag 2 -> SSH (entrada basura) -> Flag 3
```

**Learning chain:**
.git expuesto -> Credenciales filtradas -> Reutilización -> SSH -> Tres flags.

**Lección:** *Un `.git` expuesto es una puerta trasera de información: de su historia salen credenciales que, reutilizadas, abren el resto del entorno.*

**MITRE ATT&CK:**
- T1190 Exploit Public-Facing Application
- T1078 Valid Accounts
- T1059 Command and Scripting Interpreter

**Fuente:** [TryHackMe - Spring](https://tryhackme.com/room/spring)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.