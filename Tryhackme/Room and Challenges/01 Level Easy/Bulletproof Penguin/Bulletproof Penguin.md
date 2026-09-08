# Bulletproof Penguin

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `bppenguin` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bppenguin) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Redis / SNMP / nginx / SSH / TFTP / vsftpd / sudoers / MySQL |
| **Impacto** | Hardening de un servidor Ubuntu reforzando los servicios expuestos (Redis, SNMP, Nginx, SSH, FTP, sudo) y verificando cada corrección con una flag. |

---

**Contexto:** Sala de hardening sobre un servidor Linux (Ubuntu) endeble: se explora el sistema y se endurecen los servicios uno a uno. Se corrige Redis sin contraseña, SNMP con comunidad pública, nginx ejecutado como root, servicios en claro (TFTP), debilidades de SSH (MAC/kex/cifrados), FTP anónimo, contraseñas débilies de usuarios, sudoers y puertos públicos de MySQL/Redis. Cada tarea entrega una flag que confirma la configuración segura aplicada.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción al hardening y despliega el laboratorio. | `No answer needed` |

### Task 2: Hardening - Redis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al asegurar Redis sin contraseña (redis)? | `THM{ae4e5bb7aac2c2252363ca466f10ffd0}` |

### Task 3: Hardening - SNMP

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al desactivar la comunidad pública de SNMP? | `THM{aa397a808d527fd71f023c78d3c04591}` |

### Task 4: Hardening - nginx

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al corregir nginx ejecutado como root? | `THM{bebb02b22bb56b2f79ba706975714ee2}` |

### Task 5: Hardening - Servicios en claro

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué otro servicio de texto claro se ejecuta en el puerto 69/udp? | `TFTP` |
| 2 | ¿Cuál es la flag al deshabilitar los servicios en texto plano? | `THM{33704d74ec53c8cf50daf817bea836a1}` |

### Task 6: Hardening - SSH

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag al deshabilitar los MACs débiles de SSH? | `THM{e3d6b82f291b64f95213583dcd89b659}` |
| 2 | ¿Cuál es la flag al deshabilitar los algoritmos de intercambio de claves (KEX) débiles? | `THM{d9baf598ee934d79346f425a81bd693a}` |
| 3 | ¿Cuál es la flag al deshabilitar los cifrados débiles de SSH? | `THM{9ff9c182cad601291d45951c01d0b2c7}` |

### Task 7: Hardening - FTP anónimo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al deshabilitar el acceso anónimo al FTP? | `THM{f20b5ff5a3d4c779e99c3a93d1f68c6d}` |

### Task 8: Hardening - Contraseñas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag obtenida al forzar el cambio de contraseña? | `THM{be74a521c3982298d2e9b0e347a3807d}` |
| 2 | ¿Cuál es la segunda flag tras completar los cambios de contraseña? | `THM{1b354db0e71f75057abe69de26a637ab}` |

### Task 9: Hardening - sudoers

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag al corregir los permisos sudo del primer usuario? | `THM{1e9ee13fb42fea2a9eb2730c51448241}` |
| 2 | ¿Cuál es la flag al corregir los permisos sudo del segundo usuario? | `THM{a0bcb9b72fd26d0ad55cdcdcd21698f1}` |

### Task 10: Hardening - Puertos públicos (MySQL/Redis)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag al cerrar la exposición pública de MySQL? | `THM{526e33142b54e13bb47b17056823ab60}` |
| 2 | ¿Cuál es la flag al cerrar la exposición pública de Redis? | `THM{20a809866dbcf94109189c5bafabc5c2}` |

### Task 11: Conclusión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Haz clic en completar la sala. | `No answer needed` |

---

**Metodología:** Con escaneo y revisión de configuración se identifican los servicios inseguros. Cada tarea aplica la corrección: se añade requerimiento de contraseña a Redis (requirepass), se cierra la comunidad pública SNMP, se cambia el usuario de nginx (user), se deshabilitan los enlaces de texto claro (TFTP), se restringen MACs/KEX/cifrados en sshd_config, se desactiva el anonymous FTP, se fuerza cambio de contraseñas (chage/paaswd), se ajustan las entradas de /etc/sudoers y se aislan los puertos de MySQL y Redis (bind/interfaces). Cada cambio se valida con su flag.

**Learning chain:** enumeración de servicios → hardening Redis → SNMP → nginx → servicios en claro → SSH → FTP → contraseñas → sudoers → aislamiento de puertos.

**MITRE ATT&CK:** T1548 (Abuse Elevation Control Mechanism), T1021 (Remote Services), T1078 (Valid Accounts), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Bulletproof Penguin](https://tryhackme.com/room/bppenguin)