# Linux System Hardening

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | linuxsystemhardening | https://tryhackme.com/room/linuxsystemhardening | Linux / Hardening | TryHackMe | grub2-mkpasswd-pbkdf2 (PBKDF2), LUKS, UFW, SSH (Secure Shell), /sbin/nologin, wheel/sudo, SFTP, yum/dnf/apt, kern.log | Endurecimiento del sistema Linux |

---

**Contexto:** La sala **Linux System Hardening** se centra en reforzar la seguridad de un sistema Linux: cifrado de disco con **LUKS**, protección del bootloader GRUB con contraseña PBKDF2, configuración segura de **UFW** e **SSH** (Secure Shell, escucha en 2441), administración de cuentas con shell `/sbin/nologin` y grupos `wheel`/`sudo`, sustitución de FTP por **SFTP**, gestión de actualizaciones con yum/dnf/apt y auditoría básica de logs (`kern.log`, `secure`).

## Solucionario

### Task 1
**Explicación:**

Acceso al sistema y configuración inicial del entorno.

`No answer needed`

### Task 2
**Explicación:**

Configuración de la contraseña de GRUB: se genera con la utilidad indicada y se identifica el algoritmo de derivación de clave usado.

1. `grub2-mkpasswd-pbkdf2`
2. `Password-Based Key Derivation Function 2`

### Task 3
**Explicación:**

Configuración del cifrado de disco con LUKS y obtención de la flag.

1. `Linux Unified Key Setup`
2. `THM{LUKS_not_LUX}`

### Task 4
**Explicación:**

Configuración del firewall UFW: se comprueban la política por defecto y las reglas de tráfico entrante.

1. `12526`
2. `14298`

### Task 5
**Explicación:**

Configuración segura del servicio SSH (Secure Shell) y obtención de la flag.

`THM{secure_SEA_shell}`

### Task 6
**Explicación:**

Gestión de cuentas y grupos administrativos: shell de servicios, grupo de root y grupo sudo.

1. `/sbin/nologin`
2. `wheel`
3. `sudo`
4. `blacksmith`

### Task 7
**Explicación:**

Sustitución del FTP por el protocolo de transferencia seguro elegido.

`SFTP`

### Task 8
**Explicación:**

Actualización de paquetes en las distintas familias de distribuciones y expansión de los acrónimos de los gestores de paquetes.

1. `yum update`
2. `dnf update`
3. `apt update && apt upgrade`
4. `Yellowdog Updater, Modified`
5. `Dandified YUM`
6. `THM{not_Advanced_Persistent_Threat}`

### Task 9
**Explicación:**

Auditoría básica de logs: se consultan los mensajes del kernel y los eventos denegados de autenticación.

1. `tail -n 15 kern.log`
2. `grep denied secure`

### Task 10
**Explicación:**

Cuestionario final de consolidación del hardening aplicado.

`No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 - Respuesta | `No answer needed` |
| 2.1 | Task 2 - Respuesta 1 | `grub2-mkpasswd-pbkdf2` |
| 2.2 | Task 2 - Respuesta 2 | `Password-Based Key Derivation Function 2` |
| 3.1 | Task 3 - Respuesta 1 | `Linux Unified Key Setup` |
| 3.2 | Task 3 - Respuesta 2 | `THM{LUKS_not_LUX}` |
| 4.1 | Task 4 - Respuesta 1 | `12526` |
| 4.2 | Task 4 - Respuesta 2 | `14298` |
| 5 | Task 5 - Respuesta | `THM{secure_SEA_shell}` |
| 6.1 | Task 6 - Respuesta 1 | `/sbin/nologin` |
| 6.2 | Task 6 - Respuesta 2 | `wheel` |
| 6.3 | Task 6 - Respuesta 3 | `sudo` |
| 6.4 | Task 6 - Respuesta 4 | `blacksmith` |
| 7 | Task 7 - Respuesta | `SFTP` |
| 8.1 | Task 8 - Respuesta 1 | `yum update` |
| 8.2 | Task 8 - Respuesta 2 | `dnf update` |
| 8.3 | Task 8 - Respuesta 3 | `apt update && apt upgrade` |
| 8.4 | Task 8 - Respuesta 4 | `Yellowdog Updater, Modified` |
| 8.5 | Task 8 - Respuesta 5 | `Dandified YUM` |
| 8.6 | Task 8 - Respuesta 6 | `THM{not_Advanced_Persistent_Threat}` |
| 9.1 | Task 9 - Respuesta 1 | `tail -n 15 kern.log` |
| 9.2 | Task 9 - Respuesta 2 | `grep denied secure` |
| 10 | Task 10 - Respuesta | `No answer needed` |

---

**Metodología:** Hardening progresivo del sistema: protección del bootloader (GRUB + PBKDF2), cifrado de disco (LUKS), configuración de firewall (UFW) y SSH en puerto no estándar, gestión de cuentas y grupos administrativos, sustitución de FTP por SFTP, actualización de paquetes (yum/dnf/apt) y auditoría final de logs.

**Learning chain:** GRUB con PBKDF2 → LUKS → UFW → SSH seguro → cuentas (nologin, wheel, sudo) → SFTP → yum/dnf/apt → auditoría de logs.

**Lección:** *El hardening Linux se construye por capas: cifrado en reposo, bootloader protegido, firewall, SSH endurecido, principio de menor privilegio en cuentas y actualización constante del parque de paquetes; la auditoría de logs cierra el ciclo validando cada cambio.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1046 Network Service Scanning · T1110 Brute Force · T1548.002 Abuse Elevation Control Mechanism: Sudo · T1518.001 Software Discovery: Security Software Discovery.

**Fuente:** [TryHackMe - Linux System Hardening](https://tryhackme.com/room/linuxsystemhardening)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.