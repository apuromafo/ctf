# Expose

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `expose` | [TryHackMe - Expose](https://tryhackme.com/room/expose) | `01 Level Easy` | THM | enumeración, servicios expuestos, privesc, boot2root, flags | Exploitation — compromiso total de la máquina |

> **Objeto:** Explotar la máquina Expose a partir de servicios expuestos o mal configurados, obtener la flag de usuario y escalar privilegios para capturar la flag de root.

---

**Contexto:** Expose es una sala CTF tipo boot2root en la que hay que comprometer completamente una máquina aprovechando servicios o recursos que están expuestos. El reto se completa en dos fases: obtener la flag de usuario y posteriormente escalar privilegios hasta root para capturar la segunda flag.

> **ES:** Máquina boot2root: se abusa de servicios expuestos para obtener acceso y la flag de usuario, y se escala privilegios para conseguir la flag de root.
>
> **EN:** Boot2root box: exposed services are abused to gain access and the user flag, then privileges are escalated to root for the root flag.

## Solucionario

### Task 1: Obtener las banderas / Obtain the Flags

**Explicación:** Se explota el vector expuesto de la máquina para obtener la primera flag (usuario) y se escala privilegios para leer la segunda flag (root).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario | `THM{USER_FLAG_1231_EXPOSE}` |
| 2 | Flag de root | `THM{ROOT_EXPOSED_1001}` |

---

**Metodología:** Se inicia con el reconocimiento de los servicios expuestos en la máquina objetivo. Identificado el vector (servicio mal configurado o con información sensible accesible), se obtiene acceso inicial y la flag de usuario; posteriormente se enumeran vectores de escalada de privilegios dentro del sistema hasta conseguir una sesión de root y leer la flag final.

### Cadena de ataque / Attack Chain

Enumeración de servicios expuestos → Explotación del vector → Acceso inicial → Flag de usuario → Enumeración de privesc → Escalada de privilegios → Flag de root.

**Learning chain:** Network/service enumeration → Exposed service abuse → Initial access → User flag → Privilege escalation → Root flag

**Lección:** *Los servicios "expuestos" (recursos compartidos, backends, configuraciones olvidadas) son el punto de entrada predilecto del atacante: una exposición aparentemente inofensiva se convierte en acceso inicial y, combinada con mala configuración de privilegios, en compromiso total.*

**MITRE ATT&CK:** T1046 - Network Service Discovery, T1190 - Exploit Public-Facing Application, T1068 - Exploitation for Privilege Escalation, T1005 - Data from Local System

**Fuente:** [TryHackMe - Expose](https://tryhackme.com/room/expose)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.