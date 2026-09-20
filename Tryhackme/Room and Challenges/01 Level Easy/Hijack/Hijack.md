# Hijack

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `hijack` | https://tryhackme.com/room/hijack | 01 Level Easy | TryHackMe | Enumeración de red / exploit / escalada de privilegios Linux | Compromiso total de la máquina y obtención de las flags de usuario y root. |

---

**Contexto:** Reto tipo CTF de una máquina Linux donde se debe comprometer el objetivo de principio a fin: enumerar el host, encontrar la vía de acceso, explotar una vulnerabilidad y escalar privilegios hasta obtener las dos flags (usuario y root).

> **ES:** Enumera la máquina del reto, explota la vía de acceso y escala privilegios para recuperar ambas flags.
> **EN:** Enumerate the challenge machine, exploit the access vector and escalate privileges to retrieve both flags.

## Solucionario

### Task 1: Comprometiendo la máquina / Compromising the Machine

**Explicación:** La sala consiste en comprometer la máquina del reto mediante enumeración y explotación. Tras obtener la primera flag (usuario o primer acceso) se continúa con la escalada de privilegios hasta conseguir la segunda flag (root o acceso final).

1. 1. THM{fdc8cd4cff2c19e0d1022e78481ddf36}
   2. THM{b91ea3e8285157eaf173d88d0a73ed5a}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{fdc8cd4cff2c19e0d1022e78481ddf36}` |
| 2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{b91ea3e8285157eaf173d88d0a73ed5a}` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{fdc8cd4cff2c19e0d1022e78481ddf36}` |
| 1 | 2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{b91ea3e8285157eaf173d88d0a73ed5a}` |

---

**Metodología:** Enumeración del host (barrido de puertos, fuzzing web), identificación de la vía de acceso, explotación de la vulnerabilidad para obtener una shell, escalada de privilegios hasta root y recolección de las flags.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración web/servicios -> explotación -> shell -> escalada de privilegios -> flags de usuario y root
```

**Learning chain:** Recon -> Web/Service Enum -> Explotación -> Escalada de privilegios Linux.

**Lección:** *La escalada de privilegios es la clave del reto: una vez dentro hay que enumerar binarios SUID, tareas programadas y configuraciones débiles que permitan llegar a root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Hijack](https://tryhackme.com/room/hijack)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
