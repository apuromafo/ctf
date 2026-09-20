# Simple CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF challenge | `simplectf` | https://tryhackme.com/room/simplectf | 01 Level Easy | TryHackMe | Nmap / SSH / CMS Made Simple (CVE-2019-9053) / SQL injection / enumeración web / explotación y escalada | Caja CTF accesible: enumerar servicios, detectar un CMS vulnerable a SQLi, explotarlo para recuperar credenciales y acceder por SSH. |

---

**Contexto:** Caja CTF de nivel básico en la que, partiendo de la IP de la máquina, hay que enumerar puertos y servicios web, descubrir un CMS Made Simple vulnerable a inyección SQL (CVE-2019-9053), explotar la SQLi para obtener credenciales, conectarse por SSH y completar el reto.

> **ES:** Reto CTF básico: enumera la máquina, encuentra el CMS vulnerable, explota la SQLi y consigue acceso vía SSH.
> **EN:** Basic CTF challenge: enumerate the machine, find the vulnerable CMS, exploit the SQLi and gain access via SSH.

## Solucionario

### Task 1: Explota la máquina / Exploit the machine

**Explicación:** El reto se resuelve enumerando la máquina desde cero. Las respuestas corresponden a las preguntas de la room: servicios descubiertos y método de acceso, la vulnerabilidad y su tipo, el directorio/archivo secreto, las credenciales y los mensajes finales del reto. Se preserva el listado original completo de respuestas:

1. 1. 2
   2. ssh
   3. CVE-2019-9053
   4. sqli
   5. secret
   6. ssh
   7. G00d j0b, keep up!
   8. sunbath
   9. vim
   10. W3ll d0n3. You made it!

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta 1 / Question 1 | `2` |
| 2 | Pregunta 2 / Question 2 | `ssh` |
| 3 | Pregunta 3 / Question 3 | `CVE-2019-9053` |
| 4 | Pregunta 4 / Question 4 | `sqli` |
| 5 | Pregunta 5 / Question 5 | `secret` |
| 6 | Pregunta 6 / Question 6 | `ssh` |
| 7 | Pregunta 7 / Question 7 | `G00d j0b, keep up!` |
| 8 | Pregunta 8 / Question 8 | `sunbath` |
| 9 | Pregunta 9 / Question 9 | `vim` |
| 10 | Pregunta 10 / Question 10 | `W3ll d0n3. You made it!` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta 1 / Question 1 | `2` |
| 2 | Pregunta 2 / Question 2 | `ssh` |
| 3 | Pregunta 3 / Question 3 | `CVE-2019-9053` |
| 4 | Pregunta 4 / Question 4 | `sqli` |
| 5 | Pregunta 5 / Question 5 | `secret` |
| 6 | Pregunta 6 / Question 6 | `ssh` |
| 7 | Pregunta 7 / Question 7 | `G00d j0b, keep up!` |
| 8 | Pregunta 8 / Question 8 | `sunbath` |
| 9 | Pregunta 9 / Question 9 | `vim` |
| 10 | Pregunta 10 / Question 10 | `W3ll d0n3. You made it!` |

---

**Metodología:** Enumerar puertos con Nmap para descubrir los servicios (SSH y web), identificar CMS Made Simple en el servicio web, analizar/explotar el CVE-2019-9053 (inyección SQL), recuperar las credenciales y utilizarlas para conectarse por SSH, completando así todas las preguntas de la room.

### Cadena de ataque / Attack Chain

```text
Nmap (detección de servicios) -> identificar CMS Made Simple -> CVE-2019-9053 (SQLi) -> extraer credenciales -> acceso por SSH -> respuestas de la room
```

**Learning chain:** Port discovery -> service identification -> CMS fingerprinting -> SQL injection (CVE-2019-9053) -> credential extraction -> SSH access.

**Lección:** *En los CTF de máquina todo empieza por el escaneo: la versión exacta de un CMS junto con una inyección SQL pública (CVE-2019-9053) convierte la enumeración en acceso completo al sistema.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - Simple CTF](https://tryhackme.com/room/simplectf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.