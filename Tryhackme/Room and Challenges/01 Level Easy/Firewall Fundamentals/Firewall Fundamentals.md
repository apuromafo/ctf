# Firewall Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `firewallfundamentals` | [TryHackMe - Firewall Fundamentals](https://tryhackme.com/room/firewallfundamentals) | `01 Level Easy` | THM | firewall, stateful, NGFW, proxy, ufw, nftables, iptables | Defensive — fundamentos de firewalls y control de tráfico |

> **Objeto:** Aprender los fundamentos de los firewalls: qué son, sus tipos, cómo clasifican el tráfico por dirección, su aplicación en un escenario real (Core Op / Infra team) y su configuración en Linux con ufw y nftables.

---

**Contexto:** La sala Firewall Fundamentals del path SOC Level 1 introduce los firewalls y su papel en la defensa de la red. Se estudian los tipos de firewall (stateful, next-generation y proxy), las políticas de allow/deny y la dirección del tráfico (inbound/outbound), un caso práctico de segmentación entre equipos (Core Op e Infra team) con una IP específica, y las herramientas de firewall disponibles en Linux (ufw, nftables, iptables).

> **ES:** Sala de defensa sobre firewalls: tipos (stateful, NGFW, proxy), reglas allow/outbound, caso Core Op/Infra team (192.168.13.7) y herramientas Linux (ufw, nftables).
>
> **EN:** Defensive firewall room: types (stateful, NGFW, proxy), allow/outbound rules, Core Op/Infra team scenario (192.168.13.7) and Linux tools (ufw, nftables).

## Solucionario

### Task 1: ¿Qué es un firewall? / What is a Firewall?

**Explicación:** Se introduce el concepto de firewall como elemento que controla el tráfico de red según reglas de filtrado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Elemento que aplica reglas de filtrado al tráfico | `Firewall` |

### Task 2: Tipos de firewall / Firewall Types

**Explicación:** Se identifican los tres tipos principales de firewall según su funcionamiento y capacidades de inspección.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Firewall con tabla de conexiones | `stateful firewall` |
| 2 | Firewall con inspección de aplicaciones y servicios | `next-generation firewall` |
| 3 | Firewall que intermedia las conexiones como proxy | `proxy firewall` |

### Task 3: Políticas de tráfico / Traffic Policies

**Explicación:** Se trabaja con la política por defecto y la dirección del tráfico que se permite configurar en el firewall.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Acción por defecto para el tráfico permitido | `allow` |
| 2 | Dirección del tráfico saliente | `outbound` |

### Task 4: Caso práctico / Practical Case

**Explicación:** En el escenario de la sala, se identifican los equipos implicados (Core Op e Infra team) y la IP de la máquina objetivo dentro del esquema de red del firewall.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Equipo/segmento que solicita el acceso | `Core Op` |
| 2 | Equipo que gestiona o protege la infraestructura | `Infra team` |
| 3 | IP involucrada en el escenario | `192.168.13.7` |

### Task 5: Firewalls en Linux / Linux Firewalls

**Explicación:** Se repasan las herramientas de firewall disponibles en Linux y la sintaxis de reglas en distribución.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Herramienta de filtrado de paquetes en Linux | `nftables` |
| 2 | Regla/acción por defecto para el tráfico saliente | `ufw default deny outgoing` |

---

**Metodología:** Se avanza desde la teoría (qué es un firewall y sus tipos) hacia la práctica: aplicar políticas de tráfico por dirección, analizar el caso de red propuesto con los equipos Core Op e Infra team y la IP 192.168.13.7, y terminar con la configuración de firewalls en Linux usando ufw y nftables para endurecer el acceso saliente y entrante.

### Cadena de ataque / Attack Chain

Concepto de firewall → Tipos (stateful, NGFW, proxy) → Políticas (allow / outbound) → Caso real (Core Op → Infra team, 192.168.13.7) → Implementación Linux (ufw, nftables).

**Learning chain:** Firewall basics → Stateful/NGFW/proxy → Direction-based policies → Real-world segmentation → Linux firewall tools (ufw/nftables)

**Lección:** *Un firewall mal diseñado es tan peligroso como no tenerlo: conocer los tipos de inspección, definir políticas por dirección y aplicar herramientas como ufw/nftables de forma consistente es lo que convierte el filtrado de paquetes en una defensa real.*

**MITRE ATT&CK:** T1046 - Network Service Discovery; N/A (defensivo — firewall/control de red), T1562.004 - Impair Defenses: Disable or Modify Cloud Firewall (contexto defensivo)

**Fuente:** [TryHackMe - Firewall Fundamentals](https://tryhackme.com/room/firewallfundamentals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.