# VulnNet_ Internal

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `vulnnetinternal` | [TryHackMe](https://tryhackme.com/room/vulnnetinternal) | 01 Level Easy | THM | Enumeración SMB, shares, credenciales, servicio interno, root, flags | Resolución completa del reto |

---

**Contexto:** Box Linux enfocada a la explotación de recursos internos. Se enumeran puertos y se descubre un share SMB con credenciales que dan acceso a un servicio interno de la máquina; a partir de ahí se compromete el sistema y se recuperan cuatro flags: services.txt, internal flag, user.txt y root.txt.

> **ES:** Box Linux: enumeración de puertos y SMB → credenciales en shares → acceso a un servicio interno → escalada hasta root, con flags services, internal, user y root.
> **EN:** Linux box: port and SMB enumeration → credentials in shares → access to an internal service → privilege escalation to root, with services, internal, user and root flags.

## Solucionario

### Task 1: Encuentra las flags / Find the flags

**Explicación:** Se aplican técnicas de enumeración (Nmap, SMB) para descubrir credenciales que permiten acceder a un servicio interno de la caja. Mediante la explotación del servicio y la escalada de privilegios se obtienen las cuatro flags.

1. `What is the services flag?`
2. `THM{0a09d51e488f5fa105d8d866a497440a}`
3. `What is the internal flag?`
4. `THM{ff8e518addbbddb74531a724236a8221}`
5. `What is the user.txt flag?`
6. `THM{da7c20696831f253e0afaca8b83c07ab}`
7. `What is the root.txt flag?`
8. `THM{e8996faea46df09dba5676dd271c60bd}`

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the services flag? | `THM{0a09d51e488f5fa105d8d866a497440a}` |
| 2 | What is the internal flag? | `THM{ff8e518addbbddb74531a724236a8221}` |
| 3 | What is the user.txt flag? | `THM{da7c20696831f253e0afaca8b83c07ab}` |
| 4 | What is the root.txt flag? | `THM{e8996faea46df09dba5676dd271c60bd}` |

---

**Metodología:** namp → enumeración SMB (shares) → credenciales → acceso al servicio interno → compromiso inicial (user) → enumeración post-explotación → escalada de privilegios → root. Las flags services, internal, user y root se capturan en el orden del reto.

### Cadena de ataque / Attack Chain

Reconocimiento (puertos y servicios) → Enumeración SMB (shares) → Credenciales → Acceso al servicio interno → Compromiso inicial → Escalada de privilegios → root → services flag → internal flag → user.txt → root.txt

**Learning chain:** Enumeration → SMB shares → credentials → internal service exploitation → user access → privilege escalation → root

**Lección:** *Un share SMB abierto y credenciales reutilizadas abren la puerta a servicios internos que no deberían ser visibles; la enumeración persistente y la reutilización de credenciales suelen ser el hilo conductor entre el acceso inicial y root.*

**MITRE ATT&CK:** T1049 (System Network Connections Discovery), T1078 (Valid Accounts), T1110 (Brute Force), T1087 (Account Discovery), T1068 (Exploitation for Privilege Escalation), T1548 (Abuse Elevation Control Mechanism)

**Fuente:** [TryHackMe - VulnNet: Internal](https://tryhackme.com/room/vulnnetinternal)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.