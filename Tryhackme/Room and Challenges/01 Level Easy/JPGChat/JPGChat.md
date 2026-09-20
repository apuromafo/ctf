# JPGChat

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF (Free) | `jpgchat` | https://tryhackme.com/room/jpgchat | 01 Level Easy | TryHackMe | Netcat / servicio de chat Python / python -c / explotación de servicio | Máquina CTF en la que hay que explotar un servicio de chat Python para obtener una shell y recuperar las dos flags del sistema. |

---

**Contexto:** Room/máquina del catálogo de TryHackMe (slug `jpgchat`). Conectándose al servicio de chat que expone la máquina y explotándolo (ejecución remota de comandos) se consigue una shell para recuperar las flags. El objetivo es arrancar la máquina, hackearla y obtener las dos flags del reto.

> **ES:** Arranca la máquina, accede a ella y recupera la flag. / **EN:** Start Machine / Hack into the machine and retrieve the flag.

## Solucionario

### Task 1: Flags

**Explicación:** Hay que arrancar la máquina, conectarse al servicio de chat expuesto y explotarlo para obtener una shell. Desde ahí se recuperan las dos flags del reto.

Start Machine

Hack into the machine and retrieve the flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto? / What is the first flag of the challenge? | `JPC{487030410a543503cbb59ece16178318}` |
| 2 | ¿Cuál es la segunda flag del reto? / What is the second flag of the challenge? | `JPC{665b7f2e59cf44763e5a7f070b081b0a}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto? / What is the first flag of the challenge? | `JPC{487030410a543503cbb59ece16178318}` |
| 2 | ¿Cuál es la segunda flag del reto? / What is the second flag of the challenge? | `JPC{665b7f2e59cf44763e5a7f070b081b0a}` |

---

**Metodología:** Enumerar los puertos de la máquina para localizar el servicio de chat, conectarse con Netcat, interactuar con el servicio y aprovechar la ejecución de comandos (por ejemplo inyectando código Python con `python -c`) para obtener una shell y leer las flags.

### Cadena de ataque / Attack Chain

```text
nmap -> descubrir servicio de chat -> netcat -> interacción -> exploit (python -c) -> shell -> leer flags
```

**Learning chain:** nmap -> servicio chat -> nc -> inyección de comandos -> reverse shell -> flags.

**Lección:** *Los servicios de chat/input que concatenan la entrada del usuario en código Python suelen permitir ejecución remota de comandos; probar con `python -c` antes de descartarlos.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006 (Python)

**Fuente:** [TryHackMe - JPGChat](https://tryhackme.com/room/jpgchat)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.