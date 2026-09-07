# Shaker

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `shaker` |
| **Link** | [TryHackMe](https://tryhackme.com/room/shaker) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Linux / Service Exploitation / Lateral Movement / Privilege Escalation |
| **Impacto** | Compromiso completo de una máquina Linux desde shell inicial hasta root mediante encadenamiento de explotación de servicio, movimiento lateral y escalada de privilegios. |

---

**Contexto:** Máquina Linux CTF en la que el objetivo es obtener una shell inicial y capturar la primera flag, escalar lateralmente al usuario Bob para robar su flag y, finalmente, elevar privilegios a root para completar el reto. Cada etapa requiere explotar un vector distinto (servicio expuesto, abuso de credenciales/configuración y una escalada a root).

## Solucionario

### Task 1: Shell inicial y primera flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Get a shell and find the first flag! | `THM{OGZlMzhlMTQyYWMyZTExMjQyNDM2NmIyNTM4NDM3NTI=}` |

### Task 2: Usuario Bob

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you find Bob's flag? | `THM{NTA2NTJiYTNmYWQ3NGViMzEyMDIyM2EwODY2MzM1YWQ=}` |

### Task 3: Escalada a root

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Now that you're here, go on, root me :) | `THM{NzFkZGRjNmRkZWQzNWMxZTM3MjM0ZGFlMmVkZDk3MTc=}` |

---

**Metodología:**

1. Reconocimiento inicial de la máquina: barrido de puertos y enumeración de servicios expuestos para localizar el vector de entrada.
2. Se identifica y explota una vulnerabilidad en un servicio o aplicación web que permite obtener una shell en la máquina víctima como un usuario de bajos privilegios.
3. Se localiza y lee la primera flag del usuario inicial (user shell).
4. Enumeración local (usuarios, archivos, permisos y procesos) para detectar credenciales, configuraciones o binarios que permitan el movimiento lateral hacia el usuario Bob.
5. Acceso a la cuenta de Bob y lectura de su flag.
6. Análisis de privilegios (sudo, SUID, capabilities, cron, etc.) para elevar a root.
7. Se explota la escalada y se lee la última flag en la cuenta de root, completando el reto.

```
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

**Learning chain:** Recon y enumeración → Explotación del servicio → Shell inicial → User flag → Enumeración post-explotación → Movimiento lateral → Bob flag → Escalada de privilegios → Root flag

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1021 (Remote Services), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Shaker](https://tryhackme.com/room/shaker)
