# Hardening Basics Part 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hardeningbasicspart2` | [TryHackMe](https://tryhackme.com/room/hardeningbasicspart2) | 01 Level Easy | THM | GPG, SSH, AppArmor, Hardening | Endurecimiento básico de servicios Linux |

---

**Contexto:** Sala del principiante dedicada al hardening de Linux. Repasa el cifrado y firma con GPG (`gpg --gen-key`, `gpg -c`, `gpg -e`), la gestión de claves SSH (`ssh-keygen`, configuración en `/etc/ssh/sshd_config`) y el control de acceso del kernel con AppArmor (`/etc/apparmor.d`, profiles, aa-status).

> **ES:** Endurecer un sistema Linux: GPG, SSH y AppArmor, con tareas conceptuales y de configuración.
> **EN:** Harden a Linux system: GPG, SSH and AppArmor, with conceptual and configuration tasks.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de los objetivos de hardening.

No answer needed

### Task 2: GPG y SSH / GPG and SSH

**Explicación:** Práctica de cifrado con GPG y de claves SSH: número de elementos implicados, el nonce, la contraseña `Yey`, la generación de claves con `gpg --gen-key`, cifrado simétrico con `gpg -c`, cifrado asimétrico con `gpg -e`, generación de claves SSH con `ssh-keygen`, el directorio `.ssh`, el flag `-t` para el tipo de cifrado y el archivo de configuración `/etc/ssh/sshd_config`.

1. `2`
2. `nonce`
3. `Yey`
4. `gpg --gen-key`
5. `gpg -c`
6. `gpg -e`
7. `ssh-keygen`
8. `.ssh`
9. `-t`
10. `/etc/ssh/sshd_config`

### Task 3: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 4: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 5: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 6: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 7: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 8: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 9: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 10: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 11: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 12: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 13: AppArmor / AppArmor

**Explicación:** Configuración de AppArmor: el directorio de perfiles `/etc/apparmor.d`, los recursos compartidos con `abstractions`, los separadores de sintaxis `,`, el modo de auditoría `audit` y el comando de estado `aa-status`.

1. `/etc/apparmor.d`
2. `abstractions`
3. `,`
4. `audit`
5. `aa-status`

### Task 14: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y conceptualización del hardening.

No answer needed

### Task 15: Tarea informativa / Informational Task

**Explicación:** Tarea de repaso y cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Número de elementos | `2` |
| 2.2 | Valor único del cifrado | `nonce` |
| 2.3 | Contraseña de ejemplo | `Yey` |
| 2.4 | Generar claves GPG | `gpg --gen-key` |
| 2.5 | Cifrado simétrico | `gpg -c` |
| 2.6 | Cifrado asimétrico | `gpg -e` |
| 2.7 | Generar claves SSH | `ssh-keygen` |
| 2.8 | Directorio de claves | `.ssh` |
| 2.9 | Flag del tipo de clave | `-t` |
| 2.10 | Configuración del daemon SSH | `/etc/ssh/sshd_config` |
| 3 | — | `No answer needed` |
| 4 | — | `No answer needed` |
| 5 | — | `No answer needed` |
| 6 | — | `No answer needed` |
| 7 | — | `No answer needed` |
| 8 | — | `No answer needed` |
| 9 | — | `No answer needed` |
| 10 | — | `No answer needed` |
| 11 | — | `No answer needed` |
| 12 | — | `No answer needed` |
| 13.1 | Directorio de perfiles | `/etc/apparmor.d` |
| 13.2 | Recursos compartidos | `abstractions` |
| 13.3 | Separador de síntaxis | `,` |
| 13.4 | Modo de auditoría | `audit` |
| 13.5 | Comando de estado | `aa-status` |
| 14 | — | `No answer needed` |
| 15 | — | `No answer needed` |

---

**Metodología:** Endurecer servicios críticos: configurar el cifrado y firmas con GPG, proteger el acceso remoto con claves SSH y `sshd_config`, y aplicar control de acceso de procesos con AppArmor, revisando con `aa-status` que los cambios son efectivos.

### Cadena de ataque / Attack Chain

```text
Introducción -> GPG (gen-key/c/e) -> SSH (ssh-keygen, sshd_config) -> tareas informativas -> AppArmor (profile, abstractions, audit, aa-status) -> cierre
```

**Learning chain:** Hardening intro → GPG → SSH → AppArmor

**Lección:** *Endurecer un sistema es reforzar sus tres capas básicas: cifrado (GPG), acceso remoto (SSH) y control de procesos (AppArmor); lo invisible para el usuario final es lo que frena al atacante.*

**MITRE ATT&CK:** N/A (Room de hardening)

**Fuente:** [TryHackMe - Hardening Basics Part 2](https://tryhackme.com/room/hardeningbasicspart2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.