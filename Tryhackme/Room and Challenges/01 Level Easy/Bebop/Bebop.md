# Bebop

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `bebop` | [TryHackMe](https://tryhackme.com/room/bebop) | 01 Level Easy | TryHackMe | telnet / busybox / ftp / FreeBSD | Compromiso de un dispositivo de red FreeBSD mediante el acceso por telnet con busybox, logrando ambas flags |

---

**Contexto:** Bebop es un dispositivo de red antiguo basado en FreeBSD que expone el protocolo telnet y utiliza `busybox` como shell. El acceso inicial se logra aprovechando credenciales débiles, y dentro del sistema se manipulan los servicios para elevar privilegios y capturar las flags de usuario y de root.

> **ES:** La máquina corresponde a un dispositivo FreeBSD con telnet habilitado y `busybox` como shell. Tras identificar al usuario, se obtiene acceso y se explotan los servicios del propio dispositivo para recuperar el user flag y el root flag.
> **EN:** The target is a FreeBSD-based network device with telnet enabled and `busybox` as its shell. After identifying the user, access is gained and the device's own services are exploited to retrieve the user and root flags.

## Solucionario

### Task 1: Reconocimiento / Recon
**Explicación:** La enumeración inicial identifica el sistema operativo FreeBSD y un servicio telnet accesible. Se confirma el nombre del usuario con el que se podrá acceder al dispositivo.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué pregunta de reconocimiento se plantea? | `No answer needed` |
| ¿Cuál es el nombre del usuario identificado? | `pilot` |

### Task 2: Flags / Flags
**Explicación:** Una vez dentro del dispositivo se localizan los archivos con las flags del desafío. El user flag y el root flag se obtienen tras comprometer el sistema y elevar privilegios.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el user flag? | `THM{r3m0v3_b3f0r3_fl16h7}` |
| ¿Cuál es el root flag? | `THM{h16hw4y_70_7h3_d4n63r_z0n3}` |

### Task 3: Explotación / Exploitation
**Explicación:** Se identifica el mecanismo de acceso y el entorno del dispositivo: el usuario es `pilot`, la shell que interpreta los comandos es `busybox`, el protocolo utilizado para la conexión es `telnet` y el sistema operativo subyacente es `FreeBSD`.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Con qué usuario se accede al dispositivo? | `pilot` |
| ¿Qué shell interpreta los comandos del sistema? | `busybox` |
| ¿Qué protocolo se utiliza para la conexión? | `telnet` |
| ¿Qué sistema operativo ejecuta el dispositivo? | `FreeBSD` |

### Task 4: Elevación de privilegios / Privilege escalation
**Explicación:** Con la shell de `busybox` se enumeran los servicios del dispositivo y se explotan las rutinas de acceso para elevar privilegios y completar la captura de las flags.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué pregunta de elevación de privilegios se plantea? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de reconocimiento | `No answer needed` |
| 2 | Nombre del usuario identificado | `pilot` |
| 3 | User flag | `THM{r3m0v3_b3f0r3_fl16h7}` |
| 4 | Root flag | `THM{h16hw4y_70_7h3_d4n63r_z0n3}` |
| 5 | Usuario con el que se accede | `pilot` |
| 6 | Shell del sistema | `busybox` |
| 7 | Protocolo de conexión | `telnet` |
| 8 | Sistema operativo | `FreeBSD` |
| 9 | Pregunta de elevación de privilegios | `No answer needed` |

---

**Metodología:** El primer paso es la enumeración del dispositivo para identificar el sistema operativo y el protocolo telnet. Tras confirmar el usuario y entrar por telnet, se explora la shell `busybox` del dispositivo FreeBSD. A continuación se manipulan los servicios del propio sistema para obtener privilegios elevados y localizar los archivos que contienen el user flag y el root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> identificar FreeBSD y telnet -> usuario pilot -> conexión telnet -> shell busybox -> explotar servicios -> user flag -> escalada -> root flag
```

**Learning chain:** recon --> device fingerprinting (FreeBSD) --> telnet access --> busybox shell --> service abuse --> user flag --> privilege escalation --> root flag

**Lección:** *Los dispositivos de red antiguos suelen quedar desatendidos con servicios inseguros como telnet y shells minimalistas como busybox; enumerarlos correctamente permite comprometerlos por completo.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1021.005 (Remote Services: VNC/Telnet), T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Bebop](https://tryhackme.com/room/bebop)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.