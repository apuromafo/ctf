# IDE

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `ide` | https://tryhackme.com/room/ide | 01 Level Easy | TryHackMe | Enumeración de red / servicios de desarrollo / explotación / escalada de privilegios | Compromiso de la máquina del reto y obtención de ambas flags. |

---

**Contexto:** Reto tipo CTF centrado en un entorno de desarrollo (IDE) expuesto. El objetivo es enumerar la máquina, explotar el servicio o aplicación de desarrollo accesible y escalar privilegios hasta obtener las dos flags del reto.

> **ES:** Enumera el objetivo, explota el servicio de desarrollo y escala privilegios para recuperar las flags.
> **EN:** Enumerate the target, exploit the development service and escalate privileges to retrieve the flags.

## Solucionario

### Task 1: Flags del reto / Challenge Flags

**Explicación:** La sala consiste en comprometer el objetivo mediante enumeración y explotación del entorno de desarrollo. Tras acceder se recogen las dos flags que validan la solución del reto.

1. 1. 02930d21a8eb009f6d26361b2d24a466
   2. ce258cb16f47f1c66f0b0b77f4e0fb8d

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `02930d21a8eb009f6d26361b2d24a466` |
| 2 | ¿Cuál es la segunda flag? / What is the second flag? | `ce258cb16f47f1c66f0b0b77f4e0fb8d` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | ¿Cuál es la primera flag? / What is the first flag? | `02930d21a8eb009f6d26361b2d24a466` |
| 1 | 2 | ¿Cuál es la segunda flag? / What is the second flag? | `ce258cb16f47f1c66f0b0b77f4e0fb8d` |

---

**Metodología:** Enumeración de la máquina (barrido de puertos y servicios), identificación del entorno de desarrollo expuesto, explotación del servicio para obtener una shell, escalada de privilegios y recolección de las dos flags.

### Cadena de ataque / Attack Chain

```text
nmap -> identificar servicio IDE -> explotación -> shell -> escalada de privilegios -> flags
```

**Learning chain:** Recon -> servicios de desarrollo -> explotación -> escalada -> flags.

**Lección:** *Las plataformas y entornos de desarrollo expuestos ofrecen una superficie de ataque amplia (código fuente, credenciales y ejecución de código); conviene aislarlas de Internet y endurecer su configuración.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1210 (Exploitation of Remote Services)

**Fuente:** [TryHackMe - IDE](https://tryhackme.com/room/ide)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
