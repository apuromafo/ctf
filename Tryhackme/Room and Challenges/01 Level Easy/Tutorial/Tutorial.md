# Tutorial

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tutorial` | [TryHackMe](https://tryhackme.com/room/tutorial) | 01 Level Easy | THM | conexión, plataforma TryHackMe, flag de bienvenida | Verificación de la conexión inicial a la plataforma de TryHackMe |

---

**Contexto:**

> **ES:** La sala de bienvenida de TryHackMe guía al usuario a conectarse a la red y a la máquina virtual por primera vez. El objetivo es demostrar que la conexión funciona obteniendo la flag de verificación.

> **EN:** TryHackMe's welcome room guides the user through connecting to the network and to the virtual machine for the first time. The goal is to prove the connection works by obtaining the verification flag.

## Solucionario

### Task 1: Conexión con la sala / Room Connection

**Explicación:**

1. flag{connection_verified}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Connect to the room and complete the verification. | `flag{connection_verified}` |

---

**Metodología:** Se sigue el asistente de conexión de la sala, se establece la conexión VPN o in-browser y se completa el ejercicio de verificación, obteniendo la flag que confirma que el entorno está operativo.

### Cadena de ataque / Attack Chain

Room connection → network verification → flag obtained.

**Learning chain:** platform connection → environment verification → flag extraction

**Lección:** *A veces el primer paso del hacking es solo demostrar que puedes llegar hasta el objetivo: la conexión es el fundamento de todo lo demás.*

**MITRE ATT&CK:** —

**Fuente:** [TryHackMe - Tutorial](https://tryhackme.com/room/tutorial)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.