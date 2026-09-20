# Sudo Security Bypass

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough (CVE-2019-14287) | `sudovulnsbypass` | [TryHackMe](https://tryhackme.com/room/sudovulnsbypass) | 00 Level Info | THM | CVE-2019-14287, Sudo, sudo -u#-1, /bin/bash, Escalada de privilegios | Escalada de privilegios a root explotando un fallo de validación de sudo |

---

**Contexto:**
> **ES:** Laboratorio guiado sobre la vulnerabilidad CVE-2019-14287 del programa Unix Sudo: una política que excluye a root con `(ALL, !root)` puede ser burlada usando un UID negativo (-1) para ejecutar comandos con identidad de root.
> **EN:** Guided lab about the CVE-2019-14287 vulnerability in the Unix Sudo program: a policy that excludes root with `(ALL, !root)` can be bypassed using a negative UID (-1) to run commands as root.

## Solucionario

### Task 1: Despliegue / Deploy
**Explicación:**
1. No answer needed

### Task 2: Bypass de seguridad / Security Bypass
**Explicación:**
1. /bin/bash
2. THM{l33t_s3cur1ty_bypass}

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Deploy the virtual machine and connect via SSH. | `No answer needed` |
| 2.1 | What command are you allowed to run with sudo? | `/bin/bash` |
| 2.2 | What is the flag in /root/root.txt? | `THM{l33t_s3cur1ty_bypass}` |

---

**Metodología:**
Conexión SSH a la máquina, comprobación de los privilegios de sudo con `sudo -l`, identificación del binario permitido (`/bin/bash` bajo `(ALL, !root)`), explotación del bypass con `sudo -u#-1 /bin/bash` y lectura de `/root/root.txt`.

### Cadena de ataque / Attack Chain
1. Conexión a la máquina objetivo por SSH.
2. `sudo -l` revela que `/bin/bash` se puede ejecutar como `(ALL, !root)`.
3. Explotación del CVE-2019-14287: `sudo -u#-1 /bin/bash` abre una shell como root.
4. Lectura de `/root/root.txt` y captura de la flag.

**Learning chain:**
SSH -> sudo -l -> CVE-2019-14287 -> sudo -u#-1 -> shell root -> flag root.txt

**Lección:** *Sudo interpreta el UID -1 como UID 0 (root); una regla que excluye a root con `!root` no protege frente a ejecuciones con un UID negativo.*

**MITRE ATT&CK:**
- T1548.003 — Abuse Elevation Control Mechanism: Sudo and sudo caching (CVE-2019-14287)

**Fuente:** [TryHackMe - Sudo Security Bypass](https://tryhackme.com/room/sudovulnsbypass)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.