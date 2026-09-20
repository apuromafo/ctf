# Chronicle
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `chronicle` |
| **Link** | [TryHackMe](https://tryhackme.com/room/chronicle) |
| **Sección** | Linux / CTF |
| **Fuente** | Research de cosmicline (GitHub) y writeups de la comunidad |
| **Componentes** | Linux box CTF, enumeración de servicios, explotación web/servicio, escalada de privilegios, user.txt, root.txt |
| **Impacto** | Sala Medium de CTF en Linux: comprometer la máquina buscando la flag de usuario (user.txt) y tras escalar privilegios alcanzar root y capturar la flag de root (root.txt). |
---
**Contexto:** Chronicle es una máquina Linux de CTF. La metodología clásica aplica: enumeración inicial de servicios abiertos, identificación de la superficie de ataque, explotación de una vulnerabilidad para obtener acceso a un usuario con derechos en el sistema, localización de `user.txt` y posterior escalada de privilegios hasta `root` para leer `root.txt`. Las banderas son los dos entregables de la sala.
*EN: Chronicle is a Linux CTF machine. Classic methodology applies: initial service enumeration, attack-surface identification, exploitation of a vulnerability to get access as a user with rights on the system, locating `user.txt`, and then privilege escalation to `root` to read `root.txt`. The flags are the room's two deliverables.*
## Solucionario
### Task 1 — Deploy the Machine
**Explicación:** Desplegar la máquina Linux y esperar a que la sala esté lista. Pregunta de despliegue, sin respuesta.
*EN: Deploy the Linux machine and wait for the room to be ready. Deployment question, no answer needed.*
### Task 2 — The user flag
**Explicación:** Tras comprometer la máquina y obtener superficie de acceso sobre un usuario del sistema, se lee el archivo de la bandera del usuario en el directorio personal del usuario comprometido (`/home/<user>/user.txt`).
*EN: After compromising the machine and obtaining access as a system user, the user flag file is read from the compromised user's home directory (`/home/<user>/user.txt`).*

```bash
# Localizar la flag de usuario
find /home -name "user.txt" 2>/dev/null
cat /home/<user>/user.txt
# 7ba840222ecbdb57af4d24eb222808ad
```
### Task 3 — The root flag
**Explicación:** Con la escalada de privilegios conseguida (binario SUID, credencial root, servicio mal configurado, etc. según la sala), el acceso como `root` permite leer la flag en el directorio raíz (`/root/root.txt`).
*EN: With the privilege escalation achieved (SUID binary, root credential, misconfigured service, etc. depending on the room), `root` access allows reading the flag in the root directory (`/root/root.txt`).*

```bash
# Escalada de privilegios y flag de root
sudo -l          # o binarios SUID: find / -perm -4000 2>/dev/null
cat /root/root.txt
# f21979de76c0302154cc001884143ab2
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `7ba840222ecbdb57af4d24eb222808ad` |
| 2 | What is the root flag? | `f21979de76c0302154cc001884143ab2` |
---
**Metodología:** Enumeración (nmap, web, servicios) → acceso inicial → usuario con derechos → user.txt → enumeración post-explotación (sudo -l, SUID, cron, capabilities) → escalada a root → root.txt.
**Learning chain:** scan → foothold → shell de bajo privilegio → user flag → priv esc → root shell → root flag.
**Lección:** *La bandera de root siempre exige responder "qué tiene permitido hacer el usuario actual": cada reto de escalada es una pregunta de permisos mal concedidos.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1135 (Network Share Discovery), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts), T1548 (Abuse Elevation Control Mechanism).
**Fuente:** [TryHackMe - Chronicle](https://tryhackme.com/room/chronicle)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.