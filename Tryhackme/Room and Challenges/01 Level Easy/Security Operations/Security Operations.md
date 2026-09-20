# Security Operations

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `securityoperations` | [TryHackMe](https://tryhackme.com/room/securityoperations) | `01 Level Easy` | THM | SOC, Security Operations Center, network security monitoring, detección | Resolución completa del reto de operaciones de seguridad |

---

**Contexto:** Room de operaciones de seguridad: se repasa el concepto de Security Operations Center (SOC), su funcionamiento 24/7, la monitorización de la seguridad de la red como servicio principal y cómo una alerta permite bloquear un ataque.

> **ES:** Introducción al centro de operaciones de seguridad (SOC): su papel 24/7, la monitorización de la seguridad de la red y la detección que bloquea los ataques.
> **EN:** Introduction to the Security Operations Center (SOC): its 24/7 role, network security monitoring and the detection that blocks attacks.

## Solucionario

### Task 1: El centro de operaciones de seguridad / The Security Operations Center

**Explicación:** Se define el término SOC (Security Operations Center) y su régimen de funcionamiento continuo las 24 horas.

1. Security Operations Center
2. 24

### Task 2: Monitorización de la red / Network monitoring

**Explicación:** Se identifica la práctica principal del SOC para vigilar el tráfico y detectar actividad maliciosa en la red.

2. Network security monitoring

### Task 3: Flag final / Final flag

**Explicación:** Tras responder las preguntas se obtiene la flag que confirma el bloqueo del ataque simulado.

3. THM{ATTACK_BLOCKED}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Siglas del centro de operaciones de seguridad | `Security Operations Center` |
| 1.2 | Horas de operación del SOC | `24` |
| 2.1 | Práctica principal de vigilancia de la red | `Network security monitoring` |
| 3.1 | Flag de confirmación del bloqueo | `THM{ATTACK_BLOCKED}` |

---

**Metodología:** 1) Definir el SOC y su operación 24/7. 2) Reconocer la monitorización de la seguridad de la red como función central. 3) Capturar la flag que confirma que el ataque fue bloqueado.

### Cadena de ataque / Attack Chain

```text
Definición del SOC (Security Operations Center, 24h) -> monitorización de la seguridad de la red -> detección del ataque -> THM{ATTACK_BLOCKED}
```

**Learning chain:** SOC fundamentals -> operación 24/7 -> network security monitoring -> detección y bloqueo -> flag

**Lección:** *Un SOC vigila la red de forma continua; la monitorización y la detección temprana son lo que permite bloquear el ataque antes de que cause daño.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1040 (Network Sniffing), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Security Operations](https://tryhackme.com/room/securityoperations)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.