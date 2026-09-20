# Relevant

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Boot2Root Windows | relevant | https://tryhackme.com/room/relevant | 02 Level Medium | TryHackMe | SMB, servicios expuestos, explotación inicial, escalada | Compromiso total de la máquina (dos flags) |

> **Objeto:** Comprometer una máquina Windows expuesta en red local, explotando los servicios accesibles para obtener una shell y escalando privilegios hasta capturar las dos flags que acreditan el compromiso total del sistema.

---

**Contexto:** La sala **Relevant** es un CTF boot2root de máquina Windows en el que el objetivo es pasar de una posición de red sin credenciales al compromiso total. La resolución pasa por enumerar los servicios expuestos (especialmente comparticiones SMB abiertas), abusar de los recursos accesibles para obtener una shell en el sistema y escalar privilegios hasta leer las dos flags del objetivo. La hoja de respuestas recoge únicamente las dos flags finales del laboratorio.

## Solucionario

### Task 1: Flags de usuario y de sistema / User and system flags
**Explicación:**

Una vez comprometida la máquina se recogen las dos flags del laboratorio: la primera corresponde al acceso inicial conseguido sobre el sistema y la segunda a la fase final del compromiso.

1. `THM{fdk4ka34vk346ksxfr21tg789ktf45}`
2. `THM{1fk5kf469devly1gl320zafgl345pv}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del compromiso | `THM{fdk4ka34vk346ksxfr21tg789ktf45}` |
| 2 | Flag 2 del compromiso | `THM{1fk5kf469devly1gl320zafgl345pv}` |

---

**Metodología:** Enumeración de la máquina Windows, identificación de servicios expuestos y comparticiones SMB, explotación inicial para obtener ejecución de comandos, escalada de privilegios y captura de las dos flags finales.

**Learning chain:** Reconocimiento → acceso inicial vía servicios expuestos → shell → escalada de privilegios → captura de flags.

**Lección:** *En máquinas Windows, un servicio SMB u otro recurso compartido mal configurado puede ser el punto de entrada; la enumeración de comparticiones y del acceso a recursos es imprescindible antes de probar exploit activos.*

**MITRE ATT&CK:** T1046 Network Service Scanning · T1082 System Information Discovery · T1068 Exploitation for Privilege Escalation · T1005 Data from Local System.

**Fuente:** [TryHackMe - Relevant](https://tryhackme.com/room/relevant)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.