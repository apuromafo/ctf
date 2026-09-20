# Extending Your Network

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `extendingyournetwork` | [TryHackMe](https://tryhackme.com/room/extendingyournetwork) | 00 Level Info | TryHackMe | red, routers, firewalls, VPN, conmutadores, DHCP | Ampliación de redes: enrutamiento entre redes, firewalls (stateful/stateless), VPN y conmutación (capa 2 y 3) |

---

**Contexto:** Sala de redes que amplía los conceptos básicos de LAN hacia infraestructuras mayores: el dispositivo que interconecta redes, los firewalls y su clasificación (stateful/stateless), los protocolos de VPN (PPP/IPSec), la conmutación de capa 2 y 3 con enrutamiento, y un cierre con flags. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Pregunta de arranque sobre los dispositivos que conectan redes entre sí; la respuesta es el `router`, el dispositivo encargado de entregar datos en paquetes entre redes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `router` |

### Task 2: Firewalls / Firewalls

**Explicación:** Se estudian los cortafuegos: en qué capas del modelo OSI operan (`3 & 4`), la distinción entre los que registran el estado de las conexiones (`stateful`) y los que no (`stateless`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `3 & 4` |
| 2 | *(Pregunta 2 no especificada en el original)* | `stateful` |
| 3 | *(Pregunta 3 no especificada en el original)* | `stateless` |

### Task 3: Práctica de firewalls / Firewall Practice

**Explicación:** Ejercicio de aplicación sobre los conceptos de firewall de la tarea anterior, que entrega la flag `THM{FIREWALLS_RULE}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{FIREWALLS_RULE}` |

### Task 4: VPN / Virtual Private Networks

**Explicación:** Se introduce la red privada virtual (VPN): el protocolo de enlace de datos que encapsula el tráfico (`PPP`) y el protocolo que cifra y protege los datos (`IPSec`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `PPP` |
| 2 | *(Pregunta 2 no especificada en el original)* | `IPSec` |

### Task 5: Conmutación y enrutamiento / Switching and Routing

**Explicación:** Se diferencia el papel de los conmutadores según su capa: el enrutamiento de paquetes entre redes se realiza mediante `routing`, y la conmutación moderna opera entre las capas `Layer 2` y `Layer 3`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `routing` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Layer 2,Layer 3` |

### Task 6: Cierre / Conclusion

**Explicación:** Cierre de la sala que entrega la flag `THM{YOU'VE_GOT_DATA}` y una respuesta numérica `5`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{YOU'VE_GOT_DATA}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `5` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `router` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `3 & 4` |
| 3 | *(Task 2, Pregunta 2 no especificada en el original)* | `stateful` |
| 4 | *(Task 2, Pregunta 3 no especificada en el original)* | `stateless` |
| 5 | *(Task 3, Pregunta 1 no especificada en el original)* | `THM{FIREWALLS_RULE}` |
| 6 | *(Task 4, Pregunta 1 no especificada en el original)* | `PPP` |
| 7 | *(Task 4, Pregunta 2 no especificada en el original)* | `IPSec` |
| 8 | *(Task 5, Pregunta 1 no especificada en el original)* | `routing` |
| 9 | *(Task 5, Pregunta 2 no especificada en el original)* | `Layer 2,Layer 3` |
| 10 | *(Task 6, Pregunta 1 no especificada en el original)* | `THM{YOU'VE_GOT_DATA}` |
| 11 | *(Task 6, Pregunta 2 no especificada en el original)* | `5` |

---

**Metodología:** Estudiar el router como dispositivo de interconexión de redes → revisar los firewalls según las capas que inspeccionan y su capacidad de registrar estado (stateful/stateless) → aplicar los conceptos de firewall → conocer los protocolos de VPN (PPP e IPSec) → diferenciar conmutación de capa 2 y 3 y el enrutamiento → cerrar con las flags.

### Cadena de ataque / Attack Chain

```text
router (interconexión) → firewalls (capas 3 y 4, stateful/stateless) → VPN (PPP/IPSec) → conmutación (Layer 2/Layer 3) → enrutamiento → flags THM{...}
```

**Learning chain:** Dispositivos de interconexión → firewalls → VPN → conmutación y enrutamiento → cierre con flags

**Lección:** *Extender una red no es solo añadir cables: cada salto (router, firewall, VPN o conmutador de capa 3) introduce un punto de decisión — sobre estado, capa o ruta — que define la seguridad y el tráfico de toda la infraestructura.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Extending Your Network](https://tryhackme.com/room/extendingyournetwork)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.