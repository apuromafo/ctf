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

**Explicación:** Presentación de la sala de hardening: un servidor Ubuntu con múltiples servicios configurados de forma insegura. El objetivo es endurecer cada servicio y verificar la corrección. Se despliega la máquina y se empieza con el escaneo de servicios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción al hardening y despliega el laboratorio. | `No answer needed` |

### Task 2: Hardening - Redis

**Explicación:** Redis está escuchando sin contraseña (acceso público a todas las claves). Se configura `requirepass` en `/etc/redis/redis.conf` y se reinicia el servicio (`systemctl restart redis`). Verificando con `redis-cli -a <pass>`/AUTH la flag confirma el fix: `THM{ae4e5bb7aac2c2252363ca466f10ffd0}`.

```bash
nano /etc/redis/redis.conf        # requirepass <pass>
systemctl restart redis
redis-cli -a <pass> ping
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al asegurar Redis sin contraseña (redis)? | `THM{ae4e5bb7aac2c2252363ca466f10ffd0}` |

### Task 3: Hardening - SNMP

**Explicación:** SNMP (UDP 161) responde con la comunidad por defecto `public`, lo que permite enumerar el sistema (snmpwalk). Se cambia/elimina la comunidad y se restringe el agente en `/etc/snmp/snmpd.conf`; al reiniciar snmpd la flag confirma el fix: `THM{aa397a808d527fd71f023c78d3c04591}`.

```bash
nano /etc/snmp/snmpd.conf         # rocommunity público → restringir/eliminar
systemctl restart snmpd
# La flag de confirmación aparece al validar
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al desactivar la comunidad pública de SNMP? | `THM{aa397a808d527fd71f023c78d3c04591}` |

### Task 4: Hardening - nginx

**Explicación:** nginx se ejecuta como `root` (directiva `user` en `/etc/nginx/nginx.conf`), un riesgo ya que una vulnerabilidad en el worker daría root. Se cambia a un usuario sin privilegios (`user www-data;`) y se recarga: `nginx -t && systemctl reload nginx`. La flag confirma el fix: `THM{bebb02b22bb56b2f79ba706975714ee2}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al corregir nginx ejecutado como root? | `THM{bebb02b22bb56b2f79ba706975714ee2}` |

### Task 5: Hardening - Servicios en claro

**Explicación:** En el puerto `69/udp` se ejecuta `TFTP`, un servicio de transferencia de archivos sin encriptación (todo en claro). Se deshabilita el servicio tftpd y la flag confirma que ya no hay servicios en texto plano: `THM{33704d74ec53c8cf50daf817bea836a1}`.

```bash
systemctl disable --now tftpd-hpa
# o comentar el servicio xinetd/inetd según la distro
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué otro servicio de texto claro se ejecuta en el puerto 69/udp? | `TFTP` |
| 2 | ¿Cuál es la flag al deshabilitar los servicios en texto plano? | `THM{33704d74ec53c8cf50daf817bea836a1}` |

### Task 6: Hardening - SSH

**Explicación:** En `/etc/ssh/sshd_config` se endurece el servidor SSH en tres frentes: quitar los MACs débiles con `MACs hmac-sha2-256,hmac-sha2-512`, limitar los KEX con `KexAlgorithms curve25519-sha256,...` y restringir los cifrados con `Ciphers chacha20-poly1305@openssh.com,...`. Tras cada cambio se reinicia sshd y se valida:

```bash
nano /etc/ssh/sshd_config
systemctl restart sshd
```

Flags: MACs → `THM{e3d6b82f291b64f95213583dcd89b659}`; KEX → `THM{d9baf598ee934d79346f425a81bd693a}`; cifrados → `THM{9ff9c182cad601291d45951c01d0b2c7}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag al deshabilitar los MACs débiles de SSH? | `THM{e3d6b82f291b64f95213583dcd89b659}` |
| 2 | ¿Cuál es la flag al deshabilitar los algoritmos de intercambio de claves (KEX) débiles? | `THM{d9baf598ee934d79346f425a81bd693a}` |
| 3 | ¿Cuál es la flag al deshabilitar los cifrados débiles de SSH? | `THM{9ff9c182cad601291d45951c01d0b2c7}` |

### Task 7: Hardening - FTP anónimo

**Explicación:** El servidor vsftpd permite conexión anónima (`anonymous_enable=YES`), lo que expone archivos sin credenciales. Se desactiva en `/etc/vsftpd.conf` (`anonymous_enable=NO`) y se reinicia vsftpd. La flag confirma el fix: `THM{f20b5ff5a3d4c779e99c3a93d1f68c6d}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida al deshabilitar el acceso anónimo al FTP? | `THM{f20b5ff5a3d4c779e99c3a93d1f68c6d}` |

### Task 8: Hardening - Contraseñas

**Explicación:** Hay usuarios con contraseñas débiles que deben rotar. Se cambian las contraseñas con `passwd` y se fuerza expiración/edad máxima con `chage`:

```bash
passwd <usuario>
chage -M 90 <usuario>
```

Las dos flags confirman ambos fixes: `THM{be74a521c3982298d2e9b0e347a3807d}` y `THM{1b354db0e71f75057abe69de26a637ab}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag obtenida al forzar el cambio de contraseña? | `THM{be74a521c3982298d2e9b0e347a3807d}` |
| 2 | ¿Cuál es la segunda flag tras completar los cambios de contraseña? | `THM{1b354db0e71f75057abe69de26a637ab}` |

### Task 9: Hardening - sudoers

**Explicación:** Las entradas de `/etc/sudoers` (o `/etc/sudoers.d/`) conceden permisos sudo demasiado amplios a usuarios que no deberían tenerlos. Se edita con `visudo` para limitar los comandos permitidos por cada usuario. Las flags de ambos fixes: `THM{1e9ee13fb42fea2a9eb2730c51448241}` y `THM{a0bcb9b72fd26d0ad55cdcdcd21698f1}`.

```bash
sudo visudo
# Usuario1: quitar ALL → listar comandos concretos (o eliminar la línea)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag al corregir los permisos sudo del primer usuario? | `THM{1e9ee13fb42fea2a9eb2730c51448241}` |
| 2 | ¿Cuál es la flag al corregir los permisos sudo del segundo usuario? | `THM{a0bcb9b72fd26d0ad55cdcdcd21698f1}` |

### Task 10: Hardening - Puertos públicos (MySQL/Redis)

**Explicación:** MySQL y Redis escuchan en todas las interfaces. Se restringe el bind a localhost en sus configuraciones (`/etc/mysql/mysql.conf.d/mysqld.cnf` `bind-address=127.0.0.1` y `redis.conf` `bind 127.0.0.1`) y se reinician los servicios. Flags: MySQL → `THM{526e33142b54e13bb47b17056823ab60}`; Redis → `THM{20a809866dbcf94109189c5bafabc5c2}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag al cerrar la exposición pública de MySQL? | `THM{526e33142b54e13bb47b17056823ab60}` |
| 2 | ¿Cuál es la flag al cerrar la exposición pública de Redis? | `THM{20a809866dbcf94109189c5bafabc5c2}` |

### Task 11: Conclusión

**Explicación:** Con todos los servicios endurecidos y validados, se completa la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Haz clic en completar la sala. | `No answer needed` |

---

**Metodología:** Con escaneo y revisión de configuración se identifican los servicios inseguros. Cada tarea aplica la corrección: se añade requerimiento de contraseña a Redis (requirepass), se cierra la comunidad pública SNMP, se cambia el usuario de nginx (user), se deshabilitan los enlaces de texto claro (TFTP), se restringen MACs/KEX/cifrados en sshd_config, se desactiva el anonymous FTP, se fuerza cambio de contraseñas (chage/paaswd), se ajustan las entradas de /etc/sudoers y se aislan los puertos de MySQL y Redis (bind/interfaces). Cada cambio se valida con su flag.

**Learning chain:** enumeración de servicios → hardening Redis → SNMP → nginx → servicios en claro → SSH → FTP → contraseñas → sudoers → aislamiento de puertos.

**MITRE ATT&CK:** T1548 (Abuse Elevation Control Mechanism), T1021 (Remote Services), T1078 (Valid Accounts), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Bulletproof Penguin](https://tryhackme.com/room/bppenguin)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
