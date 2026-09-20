# Request Smuggling_ WebSockets

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room / Web attacks | requestsmugglingwebsockets | https://tryhackme.com/room/requestsmugglingwebsockets | 02 Level Medium | TryHackMe | HTTP Request Smuggling, Websockets, handshake (101), inyección de peticiones | Bypass de restricciones y manipulación de conexiones websocket |

> **Objeto:** Explotar vulnerabilidades de request smuggling y abusar del canal WebSocket: interpretar el código de estado del handshake, inyectar peticiones desplazadas hacia el backend y capturar las dos flags que acreditan la manipulación del tráfico.

---

**Contexto:** La sala **Request Smuggling: WebSockets** combina dos técnicas de abuso del protocolo HTTP/WebSocket: el **request smuggling** (desincronización de peticiones entre un proxy/frontend y el backend) y la manipulación de conexiones **WebSocket** (cuyo handshake de actualización devuelve el código de estado `101`). El laboratorio guía al jugador desde los fundamentos (sin respuesta) hasta el objetivo práctico de esconder una petición dentro de otra y leer las flags del compromiso.

## Solucionario

### Task 1: Fundamentos / Fundamentals
**Explicación:**

Introducción teórica a la sala, sin respuesta obligatoria.

1. `No answer needed`

### Task 2: Código de estado del handshake / Handshake status code
**Explicación:**

Se identifica el código de estado HTTP que devuelve el servidor al completar el protocolo de actualización del handshake WebSocket (`101 Switching Protocols`).

1. `101`

### Task 3: Primera flag / First flag
**Explicación:**

Tras completar la fase de manipulación del tráfico websocket se obtiene la primera flag del laboratorio.

1. `THM{bf208caddc31c6bb52621fdc2b3a73e5}`

### Task 4: Segunda flag / Second flag
**Explicación:**

Completada la fase de smuggling/inyección se obtiene la segunda flag del laboratorio.

1. `THM{a87d4e5b777c010ed3266e59fb42ccac}`

### Task 5: Cierre / Wrap-up
**Explicación:**

Última pregunta de confirmación de la sala, sin respuesta obligatoria.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fundamentos | `No answer needed` |
| 2 | Código de estado del handshake | `101` |
| 3 | Primera flag | `THM{bf208caddc31c6bb52621fdc2b3a73e5}` |
| 4 | Segunda flag | `THM{a87d4e5b777c010ed3266e59fb42ccac}` |
| 5 | Cierre | `No answer needed` |

---

**Metodología:** Comprensión del request smuggling (desincronización de peticiones entre frontend y backend) y del flujo de upgrade WebSocket, envío de peticiones manipuladas, verificación del handshake mediante el código de estado y captura de las flags.

**Learning chain:** Fundamentos del protocolo → armsado de peticiones de smuggling → abuso del canal WebSocket → captura de flags.

**Lección:** *Los servidores que reenvían tráfico a un backend interpretando campos como Content-Length o Transfer-Encoding de forma distinta son terreno fértil para esconder peticiones y saltarse restricciones de la capa frontal.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1041 Exfiltration Over C2 Channel · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Request Smuggling_ WebSockets](https://tryhackme.com/room/requestsmugglingwebsockets)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.