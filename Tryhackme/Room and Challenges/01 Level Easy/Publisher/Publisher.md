# Publisher

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `publisher` | https://tryhackme.com/room/publisher | 01 Level Easy | THM | PGP key export, RCE, SUID escalation, Enumeration | Boot-to-root en plataforma de publicación web |

---

**Contexto:** Boot-to-root que pone a prueba habilidades de enumeration (fuzzing de directorios, identificación de versión), explotación de RCE, escalada de privilegios mediante binarios SUID y explotación de configuraciones permisivas, finalizando en root.

> **ES:** Boot-to-root que pone a prueba habilidades de enumeration (fuzzing de directorios, identificación de versión), explotación de RCE, escalada de privilegios mediante binarios SUID y explotación de configuraciones permisivas, finalizando en root.
> **EN:** A boot-to-root testing enumeration skills (directory fuzzing, version identification), RCE exploitation, privilege escalation via SUID binaries and permissive configurations, ending in root.

## Solucionario

### Task 1: Publisher / Publisher

**Explicación:** Se explota la capacidad de exportación de claves PGP de la plataforma web para conseguir una shell, se enumeran binarios SUID y se escala a root abusando de un binario privilegiado que permite ejecutar comandos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `fa229046d44eda6a3598c73ad96f4ca5` |
| 2 | What is the root flag? | `3a4225cc9e85709adda6ef55d6a4f2ca` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `fa229046d44eda6a3598c73ad96f4ca5` |
| 2 | What is the root flag? | `3a4225cc9e85709adda6ef55d6a4f2ca` |

---

**Metodología:** Fuzzing de directorios web → enumeración de servicios y versiones → explotación de RCE a través de la funcionalidad de exportación → acceso a la máquina → enumeración de binarios SUID → escalada a root.

### Cadena de ataque / Attack Chain

```text
Nmap + gobuster → identificar exportador PGP → RCE via export key → shell como www-data → enumeración SUID → abusar binario privilegiado → root → flag
```

**Learning chain:** Recon → Web fuzzing → RCE exploitation → Intrusión inicial → Privilege escalation (SUID) → Root flag

**Lección:** *Las funciones de administración expuestas en plataformas web (como la exportación de claves PGP) pueden ser vectores de RCE si no validan input; los binarios SUID y las listas de control de acceso permisivas son la ruta clásica para elevar privilegios hacia root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1548.001 (Setuid and Setgid)

**Fuente:** [TryHackMe - Publisher](https://tryhackme.com/room/publisher)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.