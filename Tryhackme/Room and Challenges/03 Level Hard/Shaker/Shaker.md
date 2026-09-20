# Shaker

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | shaker | https://tryhackme.com/room/shaker | 03 Level Hard | thmrevenant (GitHub) | Linux / Service Exploitation / Lateral Movement / Privilege Escalation | Compromiso completo de una máquina Linux desde shell inicial hasta root mediante encadenamiento de explotación de servicio, movimiento lateral y escalada de privilegios. |

---

**Contexto:** Máquina Linux CTF en la que el objetivo es obtener una shell inicial y capturar la primera flag, escalar lateralmente al usuario Bob para robar su flag y, finalmente, elevar privilegios a root para completar el reto. Cada etapa requiere explotar un vector distinto (servicio expuesto, abuso de credenciales/configuración y una escalada a root).

> **ES:** Sala Linux CTF: explotar un servicio expuesto para obtener una shell inicial, moverse lateralmente al usuario Bob y elevar privilegios a root.
> **EN:** Linux CTF room: exploit an exposed service to get an initial shell, move laterally to the user Bob and escalate privileges to root.

## Solucionario

### Task 1: Shell inicial y primera flag / Initial shell and first flag
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Get a shell and find the first flag! | `THM{OGZlMzhlMTQyYWMyZTExMjQyNDM2NmIyNTM4NDM3NTI=}` |

### Task 2: Usuario Bob / User Bob
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you find Bob's flag? | `THM{NTA2NTJiYTNmYWQ3NGViMzEyMDIyM2EwODY2MzM1YWQ=}` |

### Task 3: Escalada a root / Root escalation
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Now that you're here, go on, root me :) | `THM{NzFkZGRjNmRkZWQzNWMxZTM3MjM0ZGFlMmVkZDk3MTc=}` |

### Preguntas y Respuestas / Questions and Answers

| # | Task | Pregunta | Respuesta |
|---|---|---|---|
| 1 | Task 1 | Get a shell and find the first flag! | `THM{OGZlMzhlMTQyYWMyZTExMjQyNDM2NmIyNTM4NDM3NTI=}` |
| 2 | Task 2 | Can you find Bob's flag? | `THM{NTA2NTJiYTNmYWQ3NGViMzEyMDIyM2EwODY2MzM1YWQ=}` |
| 3 | Task 3 | Now that you're here, go on, root me :) | `THM{NzFkZGRjNmRkZWQzNWMxZTM3MjM0ZGFlMmVkZDk3MTc=}` |

---

**Metodología:**

1. Reconocimiento inicial de la máquina: barrido de puertos y enumeración de servicios expuestos para localizar el vector de entrada.
2. Se identifica y explota una vulnerabilidad en un servicio o aplicación web que permite obtener una shell en la máquina víctima como un usuario de bajos privilegios.
3. Se localiza y lee la primera flag del usuario inicial (user shell).
4. Enumeración local (usuarios, archivos, permisos y procesos) para detectar credenciales, configuraciones o binarios que permitan el movimiento lateral hacia el usuario Bob.
5. Acceso a la cuenta de Bob y lectura de su flag.
6. Análisis de privilegios (sudo, SUID, capabilities, cron, etc.) para elevar a root.
7. Se explota la escalada y se lee la última flag en la cuenta de root, completando el reto.

### Cadena de ataque / Attack Chain

```text
Recon (nmap + enumeración)
  -> Explotación del servicio expuesto / app web
  -> Shell como usuario inicial
  -> User flag (THM{OGZl...})
  -> Enumeración post-explotación
  -> Movimiento lateral -> usuario Bob
  -> Bob flag (THM{NTA2...})
  -> Escalada de privilegios -> root
  -> Root flag (THM{NzFk...})
```

**Learning chain:**
Recon y enumeración → Explotación del servicio → Shell inicial → User flag → Enumeración post-explotación → Movimiento lateral → Bob flag → Escalada de privilegios → Root flag

**Lección:** *El movimiento lateral se alimenta de la enumeración: cada credencial o configuración abusable encadena un escalón más hacia root.*

**MITRE ATT&CK:**
T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1021 (Remote Services), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Shaker](https://tryhackme.com/room/shaker)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.